from __future__ import annotations
import csv, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REGISTRY_DIR=ROOT/"experiments"/"functional-capability-depth"/"system-observations"
PSV=REGISTRY_DIR/"registry.psv"; MARKDOWN=REGISTRY_DIR/"REGISTRY.md"
class SystemObservationRegistryTests(unittest.TestCase):
    def object_records(self): return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(REGISTRY_DIR.glob("*.json"))]
    def registry_rows(self):
        with PSV.open(encoding="utf-8",newline="") as h: return list(csv.DictReader(h,delimiter="|"))
    def test_registry_is_one_row_per_raw_observation(self):
        raw=[o["observation_id"] for r in self.object_records() for o in r["observations"]]
        rows=self.registry_rows(); ids=[r["observation_id"] for r in rows]
        self.assertEqual(len(raw),len(set(raw))); self.assertEqual(len(ids),len(set(ids))); self.assertEqual(set(ids),set(raw))
    def test_registry_projection_is_neutral(self):
        rows=self.registry_rows(); self.assertTrue(rows); fields=set(rows[0])
        for key in ("observation_id","system_name","canonical_harness_id","evidence_surfaces","evidence_source_class","system_compatibility"): self.assertIn(key,fields)
        for key in ("function","benchmark_fit","canonical_state","autonomy_state"): self.assertNotIn(key,fields)
    def test_registry_does_not_duplicate_numeric_payloads(self):
        rows=self.registry_rows(); allowed={"observation_id","system_name","canonical_harness_id","evidence_surfaces","kind","evidence_source_class","system_compatibility","record_ref"}
        self.assertEqual(set(rows[0]),allowed)
        for row in rows: self.assertTrue((REGISTRY_DIR/row["record_ref"]).is_file())
    def test_generated_markdown_states_interpretation_boundary(self):
        text=MARKDOWN.read_text(encoding="utf-8"); self.assertIn("Raw observations:",text); self.assertIn("VSM-function relevance is intentionally absent",text); self.assertNotIn("| Function |",text)
    def test_current_raw_records_have_explicit_provenance_and_compatibility(self):
        self.assertEqual(list(REGISTRY_DIR.glob("*.jsonl")),[])
        for record in self.object_records():
            self.assertIn(record["evidence_source_class"],{"external-reproduced","first-party-reported","mechanism-only"})
            self.assertIn(record["published_implementation"]["system_compatibility"],{"native-system","adapter-preserved","benchmark-scaffolded","unclear"})
            self.assertTrue(record["primary_sources"]); self.assertTrue(all(s.startswith("https://") for s in record["primary_sources"]))
if __name__=="__main__": unittest.main()
