from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXP=ROOT/"experiments"/"functional-capability-depth"
REG=EXP/"system-observations"
S3=EXP/"s3-system-benchmarks"
SOURCE_REF="da303195717b9db468e1993d3e1f988637141d73"
SOURCE_PATH="experiments/functional-capability-depth/s3-system-benchmarks/observations.json"
IDS={"omnigent-child-session-recovery-2026-09","supervisoragent-smas-gaia-pass1-2026"}
DERIVED_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","raw_observation_ref"}

def old_rows():
    text=subprocess.check_output(["git","show",f"{SOURCE_REF}:{SOURCE_PATH}"],cwd=ROOT,text=True)
    return {row["observation_id"]:row for row in json.loads(text) if row["observation_id"] in IDS}

def hydrate(link):
    ref=link["raw_observation_ref"]
    rel,oid=ref[len("../system-observations/"):].rsplit("#",1)
    record=json.loads((REG/rel).read_text(encoding="utf-8"))
    matches=[o for o in record["observations"] if o["observation_id"]==oid]
    assert len(matches)==1
    raw=matches[0]
    effective=dict(link)
    for k,v in raw.items():
        if k in {"observation_id","kind","evidence_surface","benchmark"}: continue
        effective[k]=v
    effective["evidence_source_class"]=record["evidence_source_class"]
    effective["system_compatibility"]=record["published_implementation"]["system_compatibility"]
    effective["primary_sources"]=record["primary_sources"]
    if record.get("canonical_harness_id"):
        effective["canonical_review_revision"]=record["canonical_review_ref"]
    return effective

class S3NeutralRegistryMigration807Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.old=old_rows()
        current=json.loads((S3/"observations.json").read_text(encoding="utf-8"))
        cls.links={row["observation_id"]:row for row in current if row["observation_id"] in IDS}
        cls.effective={oid:hydrate(link) for oid,link in cls.links.items()}
    def test_two_rows_migrated_and_resolve_once(self):
        self.assertEqual(set(self.old),IDS); self.assertEqual(set(self.links),IDS)
        counts={oid:0 for oid in IDS}
        for path in REG.glob("*.json"):
            record=json.loads(path.read_text(encoding="utf-8"))
            for obs in record.get("observations",[]):
                if obs.get("observation_id") in counts: counts[obs["observation_id"]]+=1
        self.assertEqual(counts,{oid:1 for oid in IDS})
    def test_moved_fields_are_lossless(self):
        for oid,old in self.old.items():
            effective=self.effective[oid]
            for key,value in old.items():
                self.assertEqual(effective.get(key),value,f"{oid}:{key}")
    def test_derived_rows_own_only_s3_interpretation(self):
        for link in self.links.values():
            self.assertLessEqual(set(link),DERIVED_ALLOWED)
            self.assertIn("raw_observation_ref",link)
            for key in ("primary_sources","reported_operational_witness","regression_evidence","baseline_arm","supervised_arm","reported_average_token_reduction_percent"):
                self.assertNotIn(key,link)
    def test_raw_records_are_vsm_free(self):
        for oid,link in self.links.items():
            rel=link["raw_observation_ref"][len("../system-observations/"):].split("#",1)[0]
            record=json.loads((REG/rel).read_text(encoding="utf-8"))
            obs=next(o for o in record["observations"] if o["observation_id"]==oid)
            for container in (record,obs):
                for forbidden in ("function","benchmark_fit","vsm_interpretation"):
                    self.assertNotIn(forbidden,container)
    def test_boundaries_remain_distinct(self):
        omni=json.loads((REG/"omnigent-child-session-recovery.json").read_text(encoding="utf-8"))
        self.assertEqual(omni["canonical_harness_id"],"omnigent")
        self.assertEqual(omni["canonical_review_ref"],"4d963a360e798f076d4fdbd4665e7188e4da05df")
        self.assertEqual(omni["published_implementation"]["revision_relation"],"post-assessment-descendant")
        smas=json.loads((REG/"supervisoragent-smas.json").read_text(encoding="utf-8"))
        self.assertIsNone(smas["canonical_harness_id"])
        self.assertEqual(smas["published_implementation"]["system_compatibility"],"benchmark-scaffolded")
if __name__=="__main__": unittest.main()
