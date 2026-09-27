from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / "experiments" / "functional-capability-depth" / "system-observations"
PSV = REGISTRY_DIR / "registry.psv"
MARKDOWN = REGISTRY_DIR / "REGISTRY.md"


class SystemObservationRegistryTests(unittest.TestCase):
    def object_records(self) -> list[dict]:
        records: list[dict] = []
        for path in sorted(REGISTRY_DIR.glob("*.json")):
            records.append(json.loads(path.read_text(encoding="utf-8")))
        return records

    def row_records(self) -> list[dict]:
        rows: list[dict] = []
        for path in sorted(REGISTRY_DIR.glob("*.jsonl")):
            for raw in path.read_text(encoding="utf-8").splitlines():
                if raw.strip():
                    rows.append(json.loads(raw))
        return rows

    def registry_rows(self) -> list[dict[str, str]]:
        with PSV.open(encoding="utf-8", newline="") as handle:
            return list(csv.DictReader(handle, delimiter="|"))

    def test_registry_is_one_row_per_raw_observation(self) -> None:
        raw_ids: list[str] = []
        for record in self.object_records():
            raw_ids.extend(obs["observation_id"] for obs in record["observations"])
        raw_ids.extend(row["observation_id"] for row in self.row_records())

        rows = self.registry_rows()
        registry_ids = [row["observation_id"] for row in rows]

        self.assertEqual(len(raw_ids), len(set(raw_ids)))
        self.assertEqual(len(registry_ids), len(set(registry_ids)))
        self.assertEqual(set(registry_ids), set(raw_ids))

    def test_registry_projection_is_neutral(self) -> None:
        rows = self.registry_rows()
        self.assertTrue(rows)
        fields = set(rows[0])

        self.assertIn("observation_id", fields)
        self.assertIn("system_name", fields)
        self.assertIn("canonical_harness_id", fields)
        self.assertIn("evidence_surfaces", fields)
        self.assertIn("evidence_source_class", fields)
        self.assertIn("system_compatibility", fields)

        self.assertNotIn("function", fields)
        self.assertNotIn("benchmark_fit", fields)
        self.assertNotIn("canonical_state", fields)
        self.assertNotIn("autonomy_state", fields)

    def test_registry_does_not_duplicate_numeric_payloads(self) -> None:
        rows = self.registry_rows()
        allowed_fields = {
            "observation_id",
            "system_name",
            "canonical_harness_id",
            "evidence_surfaces",
            "kind",
            "evidence_source_class",
            "system_compatibility",
            "record_ref",
        }
        self.assertEqual(set(rows[0]), allowed_fields)

        for row in rows:
            self.assertTrue((REGISTRY_DIR / row["record_ref"]).is_file())

    def test_generated_markdown_states_interpretation_boundary(self) -> None:
        text = MARKDOWN.read_text(encoding="utf-8")
        self.assertIn("Raw observations:", text)
        self.assertIn("VSM-function relevance is intentionally absent", text)
        self.assertNotIn("| Function |", text)
        self.assertNotIn("| S1 |", text)
        self.assertNotIn("| S2 |", text)

    def test_current_raw_records_have_explicit_provenance_and_compatibility(self) -> None:
        for record in self.object_records():
            self.assertIn(
                record["evidence_source_class"],
                {"external-reproduced", "first-party-reported", "mechanism-only"},
            )
            self.assertIn(
                record["published_implementation"]["system_compatibility"],
                {"native-system", "adapter-preserved", "benchmark-scaffolded", "unclear"},
            )
            self.assertTrue(record["primary_sources"])
            for source in record["primary_sources"]:
                self.assertTrue(source.startswith("https://"))

        for row in self.row_records():
            self.assertNotIn("function", row)
            self.assertNotIn("benchmark_fit", row)
            self.assertNotIn("vsm_interpretation", row)
            self.assertIn(
                row["evidence_source_class"],
                {"external-reproduced", "first-party-reported", "mechanism-only"},
            )
            self.assertIn(
                row["published_implementation"]["system_compatibility"],
                {"native-system", "adapter-preserved", "benchmark-scaffolded", "unclear"},
            )
            self.assertTrue(row["benchmark"]["primary_source"].startswith("https://"))
            self.assertTrue(row["benchmark"]["artifact_source"].startswith("https://"))


if __name__ == "__main__":
    unittest.main()
