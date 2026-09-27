from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXP=ROOT/"experiments"/"functional-capability-depth"
REG=EXP/"system-observations"; S3=EXP/"s3star-system-benchmarks"
SOURCE_REF="6317c2c57070f50225949104911a90fcdcd58abd"
FILES=("benchmark_observations.json","canonical_observations.json")
DERIVED_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","aggregate_s3star_metric_reported","raw_observation_ref"}
def old_rows():
    out=[]
    for name in FILES:
        txt=subprocess.check_output(["git","show",f"{SOURCE_REF}:experiments/functional-capability-depth/s3star-system-benchmarks/{name}"],cwd=ROOT,text=True)
        out.extend(json.loads(txt))
    return out
def hydrate(link):
    ref=link["raw_observation_ref"]; rel,oid=ref[len("../system-observations/"):].rsplit("#",1)
    record=json.loads((REG/rel).read_text(encoding="utf-8")); raw=[o for o in record["observations"] if o["observation_id"]==oid]
    assert len(raw)==1; effective=dict(link)
    for k,v in raw[0].items():
        if k in {"observation_id","kind","evidence_surface","non_claim"}: continue
        effective[k]=v
    effective["evidence_source_class"]=record["evidence_source_class"]
    effective["system_compatibility"]=record["published_implementation"]["system_compatibility"]
    effective["primary_sources"]=record["primary_sources"]
    if record.get("canonical_harness_id"): effective["canonical_review_revision"]=record["canonical_review_ref"]
    return effective
class S3StarNeutralRegistryMigration802Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=old_rows(); cls.links=[]
        for name in FILES: cls.links.extend(json.loads((S3/name).read_text(encoding="utf-8")))
        cls.effective={x["observation_id"]:hydrate(x) for x in cls.links}
    def test_five_observations_resolve_once(self):
        self.assertEqual(len(self.old),5); self.assertEqual(len(self.links),5)
        ids={o["observation_id"] for o in self.old}; self.assertEqual(ids,set(self.effective))
        counts={oid:0 for oid in ids}
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            for obs in rec.get("observations",[]):
                if obs.get("observation_id") in counts: counts[obs["observation_id"]]+=1
        self.assertTrue(all(v==1 for v in counts.values()),counts)
    def test_moved_fields_are_lossless(self):
        for old in self.old:
            eff=self.effective[old["observation_id"]]
            for key,value in old.items(): self.assertEqual(eff.get(key),value,f"{old['observation_id']}:{key}")
    def test_derived_files_own_only_s3star_interpretation(self):
        for link in self.links:
            self.assertLessEqual(set(link),DERIVED_ALLOWED)
            self.assertIn("raw_observation_ref",link)
            for raw_key in ("primary_sources","paired_runs","reported_mean_baseline_reward","reported_execution_weaknesses_total","audit_loop","published_result_summary"):
                self.assertNotIn(raw_key,link)
    def test_neutral_records_are_vsm_free(self):
        ids={o["observation_id"] for o in self.old}
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            selected=[o for o in rec.get("observations",[]) if o.get("observation_id") in ids]
            if not selected: continue
            for forbidden in ("function","benchmark_fit","vsm_interpretation"):
                self.assertNotIn(forbidden,rec)
                for obs in selected: self.assertNotIn(forbidden,obs)
    def test_appliedscientist_reuses_existing_record(self):
        oid="appliedscientist-iterative-review-2026-09"
        hits=[]
        for path in REG.glob("*.json"):
            rec=json.loads(path.read_text(encoding="utf-8"))
            if any(o.get("observation_id")==oid for o in rec.get("observations",[])): hits.append(path.name)
        self.assertEqual(hits,["appliedscientist.json"])
if __name__=="__main__": unittest.main()
