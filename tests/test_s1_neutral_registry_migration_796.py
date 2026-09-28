from __future__ import annotations
import json, subprocess, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/"experiments"/"functional-capability-depth"/"system-observations"
SOURCE_REF="fe99079baaf48d6fdb23310c13751cbfaef9e2b8"
SOURCE_PATH="experiments/functional-capability-depth/system-observations/public-system-benchmarks.jsonl"

def load_jsonl(text:str)->list[dict]: return [json.loads(line) for line in text.splitlines() if line.strip()]
def expand(record:dict,obs:dict)->dict:
    return {"schema_version":record["schema_version"],"observation_id":obs["observation_id"],
        "evidence_source_class":record["evidence_source_class"],"system_name":record["system_name"],
        "canonical_harness_id":record["canonical_harness_id"],"canonical_assessment_ref":record["canonical_assessment_ref"],
        "canonical_review_ref":record["canonical_review_ref"],"canonical_repository":record["canonical_repository"],
        "published_implementation":obs["published_implementation"],"benchmark":obs["benchmark"],"result":obs["result"],
        "provenance":obs["provenance"],"comparison":obs["comparison"],"notes":obs["notes"]}
class S1NeutralRegistryMigration796Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls)->None:
        old=subprocess.check_output(["git","show",f"{SOURCE_REF}:{SOURCE_PATH}"],cwd=ROOT,text=True)
        cls.old=load_jsonl(old); ids={r["observation_id"] for r in cls.old}; cls.new=[]
        for path in sorted(REG.glob("*.json")):
            record=json.loads(path.read_text(encoding="utf-8"))
            for obs in record.get("observations",[]):
                if obs.get("observation_id") in ids: cls.new.append(expand(record,obs))
    def test_all_19_rows_are_migrated_once(self):
        self.assertEqual(len(self.old),19); self.assertEqual(len(self.new),19)
        self.assertEqual({r["observation_id"] for r in self.old},{r["observation_id"] for r in self.new})
    def test_migration_is_lossless_from_801(self):
        by={r["observation_id"]:r for r in self.new}
        for old in self.old:
            current=dict(by[old["observation_id"]])
            current["notes"]=old["notes"]
            self.assertEqual(current,old,old["observation_id"])
    def test_raw_records_have_no_vsm_attribution(self):
        ids={r["observation_id"] for r in self.old}
        for path in sorted(REG.glob("*.json")):
            record=json.loads(path.read_text(encoding="utf-8"))
            selected=[o for o in record.get("observations",[]) if o.get("observation_id") in ids]
            if not selected: continue
            for forbidden in ("function","benchmark_fit","vsm_interpretation"):
                self.assertNotIn(forbidden,record)
                for obs in selected: self.assertNotIn(forbidden,obs)
    def test_qwenpaw_pawbench_provenance_preserved(self):
        target=next(r for r in self.new if r["observation_id"]=="qwenpaw__pawbench-v1.0__qwen3.6-35b-a3b__20260529")
        self.assertEqual(target["evidence_source_class"],"first-party-reported")
    def test_neutral_registry_has_one_raw_format(self):
        self.assertEqual(list(REG.glob("*.jsonl")),[])
if __name__=="__main__": unittest.main()
