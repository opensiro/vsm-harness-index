from __future__ import annotations

import csv
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"


def load(name: str) -> dict:
    return json.loads((RAW / name).read_text(encoding="utf-8"))


class OperationalEvidenceSurfaces799Tests(unittest.TestCase):
    def test_operational_records_are_neutral_and_nonbenchmark(self) -> None:
        expected = {
            "squad-operational-history.json": "squad-shared-state-conflict-attenuation-2026-03",
            "thclaws-operational-history.json": "thclaws-team-workspace-interference-attenuation-2026",
        }
        for filename, observation_id in expected.items():
            record = load(filename)
            self.assertEqual(len(record["observations"]), 1)
            observation = record["observations"][0]
            self.assertEqual(observation["observation_id"], observation_id)
            self.assertTrue(observation["evidence_surface"])
            self.assertNotIn("benchmark", observation)
            self.assertNotIn("benchmark_results", observation)
            for forbidden in ("function", "benchmark_fit", "vsm_interpretation"):
                self.assertNotIn(forbidden, record)
                self.assertNotIn(forbidden, observation)

    def test_generated_registry_uses_generic_evidence_surface_field(self) -> None:
        with (RAW / "registry.psv").open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="|"))
        self.assertTrue(rows)
        self.assertIn("evidence_surfaces", rows[0])
        self.assertNotIn("benchmark_labels", rows[0])
        by_id = {row["observation_id"]: row for row in rows}
        self.assertIn("repository history", by_id["squad-shared-state-conflict-attenuation-2026-03"]["evidence_surfaces"])
        self.assertIn("operational", by_id["thclaws-team-workspace-interference-attenuation-2026"]["evidence_surfaces"].lower())

    def test_existing_benchmark_rows_still_project_as_evidence_surfaces(self) -> None:
        with (RAW / "registry.psv").open(encoding="utf-8", newline="") as handle:
            rows = {row["observation_id"]: row for row in csv.DictReader(handle, delimiter="|")}
        self.assertEqual(
            rows["grit-synthetic-merge-contention-2026-04"]["evidence_surfaces"],
            "Grit synthetic merge-contention sweep",
        )
        self.assertEqual(
            rows["squad-marble-completion-ablation"]["evidence_surfaces"],
            "MARBLE factorial ablation",
        )


if __name__ == "__main__":
    unittest.main()
