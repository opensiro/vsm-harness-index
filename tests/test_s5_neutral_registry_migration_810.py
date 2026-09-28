from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXP=ROOT/"experiments"/"functional-capability-depth"
REG=EXP/"system-observations"; S5=EXP/"s5-system-benchmarks"
SOURCE_REF="faf351e02ae48d205bcd1d1a9b46d221e52bad84"
FILES=("benchmark_observations.json","canonical_observations.json")
GOV="govsim-selfgovern-membership-authority-2026-09"
OURO="ouroboros-parent-governed-cyber-pro-policy-enactment-2026-09"
GOV_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","s5_boundary","result_scope_note","vsm_interpretation","raw_observation_ref"}
OURO_ALLOWED={"observation_id","function","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","canonical_s5_state","ownership_mode_observed","comparison_class","vsm_interpretation","non_claim","raw_observation_ref"}

def old_rows():
    out=[]
    for name in FILES:
        txt=subprocess.check_output(["git","show",f"{SOURCE_REF}:experiments/functional-capability-depth/s5-system-benchmarks/{name}"],cwd=ROOT,text=True)
        out.extend(json.loads(txt))
    return {row["observation_id"]:row for row in out}

def hydrate(link):
    ref=link["raw_observation_ref"]; rel,oid=ref[len("../system-observations/"):].rsplit("#",1)
    rec=json.loads((REG/rel).read_text(encoding="utf-8")); matches=[o for o in rec["observations"] if o["observation_id"]==oid]
    assert len(matches)==1
    eff=dict(link)
    for k,v in matches[0].items():
        if k in {"observation_id","kind"}: continue
        eff[k]=v
    eff["evidence_source_class"]=rec["evidence_source_class"]
    eff["system_compatibility"]=rec["published_implementation"]["system_compatibility"]
    eff["primary_sources"]=rec["primary_sources"]
    if rec["published_implementation"].get("code_revision_status") is not None: eff["code_revision_status"]=rec["published_implementation"]["code_revision_status"]
    if rec["published_implementation"].get("paper_version") is not None: eff["paper_version"]=rec["published_implementation"]["paper_version"]
    if rec.get("canonical_harness_id"): eff["canonical_review_revision"]=rec["canonical_review_ref"]
    return eff

class S5NeutralRegistryMigration810Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=old_rows(); cls.links={}
        for name in FILES:
            for row in json.loads((S5/name).read_text(encoding="utf-8")): cls.links[row["observation_id"]]=row
        cls.effective={oid:hydrate(link) for oid,link in cls.links.items()}
    def test_two_direct_observations_resolve_once(self):
        self.assertEqual(set(self.old),{GOV,OURO}); self.assertEqual(set(self.links),{GOV,OURO})
        counts={GOV:0,OURO:0}
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            for obs in rec.get("observations",[]):
                if obs.get("observation_id") in counts: counts[obs["observation_id"]]+=1
        self.assertEqual(counts,{GOV:1,OURO:1})
    def test_moved_fields_are_lossless(self):
        for oid,old in self.old.items():
            eff=self.effective[oid]
            for key,value in old.items():
                if key=="broader_g1_result":
                    current=dict(eff.get(key))
                    current["scope_note"]=value["scope_note"]
                    self.assertEqual(current,value,f"{oid}:{key}")
                    continue
                self.assertEqual(eff.get(key),value,f"{oid}:{key}")
    def test_function_files_are_derived_only(self):
        self.assertLessEqual(set(self.links[GOV]),GOV_ALLOWED)
        self.assertLessEqual(set(self.links[OURO]),OURO_ALLOWED)
        for oid in (GOV,OURO):
            self.assertIn("raw_observation_ref",self.links[oid])
            for raw_key in ("primary_sources","evidence_source_class","system_compatibility","authority_path","non_thinking_exile","thinking_exile","policy_change_commit","enactment_pr","lineage","decision_chain","executable_effects"):
                self.assertNotIn(raw_key,self.links[oid],f"{oid}:{raw_key}")
    def test_neutral_records_are_vsm_free(self):
        for oid,link in self.links.items():
            rel=link["raw_observation_ref"][len("../system-observations/"):].split("#",1)[0]
            rec=json.loads((REG/rel).read_text(encoding="utf-8")); obs=next(o for o in rec["observations"] if o["observation_id"]==oid)
            for container in (rec,obs):
                for forbidden in ("function","benchmark_fit","vsm_interpretation","canonical_s5_state","ownership_mode_observed"):
                    self.assertNotIn(forbidden,container)
    def test_boundaries_remain_distinct(self):
        gov=json.loads((REG/"govsim-selfgovern.json").read_text(encoding="utf-8"))
        self.assertIsNone(gov["canonical_harness_id"])
        self.assertEqual(gov["published_implementation"]["system_compatibility"],"benchmark-scaffolded")
        self.assertEqual(gov["published_implementation"]["code_revision_status"],"unresolved-authoritative-public-repository")
        ouro=json.loads((REG/"ouroboros-policy-enactment.json").read_text(encoding="utf-8"))
        self.assertEqual(ouro["canonical_harness_id"],"ouroboros")
        self.assertEqual(ouro["canonical_review_ref"],"86806ee123ce8e26cc063cc1a618f975eea64f26")
        self.assertTrue(next(o for o in ouro["observations"] if o["observation_id"]==OURO)["lineage"]["merge_commit_is_ancestor"])
if __name__=="__main__": unittest.main()
