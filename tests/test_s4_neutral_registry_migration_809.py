from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXP=ROOT/"experiments"/"functional-capability-depth"
REG=EXP/"system-observations"; S4=EXP/"s4-system-benchmarks"
SOURCE_REF="d0753a1375548d1db09cfbcae047f119d0cbba03"
FILES=("benchmark_observations.json","canonical_observations.json")
BENCH_DERIVED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","raw_observation_ref"}
CANON_DERIVED=BENCH_DERIVED|{"canonical_assessment_ref","ordinary_s4_boundary","comparison_scope_note"}


def old_rows():
    out=[]
    for name in FILES:
        txt=subprocess.check_output(["git","show",f"{SOURCE_REF}:experiments/functional-capability-depth/s4-system-benchmarks/{name}"],cwd=ROOT,text=True)
        out.extend(json.loads(txt))
    return {row["observation_id"]:row for row in out}


def hydrate(link):
    ref=link["raw_observation_ref"]
    rel,oid=ref[len("../system-observations/"):].rsplit("#",1)
    record=json.loads((REG/rel).read_text(encoding="utf-8"))
    matches=[o for o in record["observations"] if o.get("observation_id")==oid]
    assert len(matches)==1
    effective=dict(link)
    for k,v in matches[0].items():
        if k in {"observation_id","kind","benchmark","evidence_surface","non_claim"}: continue
        effective[k]=v
    effective["evidence_source_class"]=record["evidence_source_class"]
    effective["system_compatibility"]=record["published_implementation"]["system_compatibility"]
    effective["primary_sources"]=record["primary_sources"]
    if record.get("canonical_harness_id"):
        effective["canonical_review_revision"]=record["canonical_review_ref"]
    return effective


class S4NeutralRegistryMigration809Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=old_rows(); cls.links={}
        for name in FILES:
            for row in json.loads((S4/name).read_text(encoding="utf-8")):
                cls.links[row["observation_id"]]=row
        cls.effective={oid:hydrate(link) for oid,link in cls.links.items()}
    def test_six_direct_rows_resolve_once(self):
        self.assertEqual(len(self.old),6); self.assertEqual(set(self.old),set(self.links))
        counts={oid:0 for oid in self.old}
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            for obs in rec.get("observations",[]):
                if obs.get("observation_id") in counts: counts[obs["observation_id"]]+=1
        self.assertEqual(counts,{oid:1 for oid in self.old})
    def test_moved_fields_are_lossless(self):
        for oid,old in self.old.items():
            effective=self.effective[oid]
            for key,value in old.items():
                if key=="raw_observation_ref": continue
                self.assertEqual(effective.get(key),value,f"{oid}:{key}")
    def test_function_files_are_derived_only(self):
        for oid,link in self.links.items():
            allowed=CANON_DERIVED if oid in {"a-evolve-harness-updating-2026","kadath-ten-epoch-native-evolution-2026"} else BENCH_DERIVED
            self.assertLessEqual(set(link),allowed,oid)
            self.assertIn("raw_observation_ref",link)
            for raw_key in ("primary_sources","system_compatibility","evidence_source_class","adaptation_loop","published_results","epochs","source_artifact_revision"):
                self.assertNotIn(raw_key,link,oid)
    def test_raw_records_are_vsm_free(self):
        for oid,link in self.links.items():
            rel=link["raw_observation_ref"][len("../system-observations/"):].split("#",1)[0]
            rec=json.loads((REG/rel).read_text(encoding="utf-8"))
            obs=next(o for o in rec["observations"] if o["observation_id"]==oid)
            for container in (rec,obs):
                for forbidden in ("function","benchmark_fit","vsm_interpretation","ordinary_s4_boundary","comparison_scope_note"):
                    self.assertNotIn(forbidden,container)
    def test_composed_and_canonical_boundaries_stay_separate(self):
        a_comp=json.loads((REG/"a-evolve-composed.json").read_text(encoding="utf-8"))
        self.assertIsNone(a_comp["canonical_harness_id"])
        a_native=json.loads((REG/"a-evolve.json").read_text(encoding="utf-8"))
        self.assertEqual(a_native["canonical_harness_id"],"a-evolve")
        k=json.loads((REG/"kadath.json").read_text(encoding="utf-8"))
        self.assertEqual(k["canonical_harness_id"],"kadath")
        evo=json.loads((REG/"evoharnessbench.json").read_text(encoding="utf-8"))
        self.assertIsNone(evo["canonical_harness_id"])
        self.assertEqual(evo["published_implementation"].get("code_revision_status"),"unresolved-official-github-repository")
if __name__=="__main__": unittest.main()
