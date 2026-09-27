from __future__ import annotations

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S2 = EXP / "s2-system-benchmarks"
RAW = EXP / "system-observations"
TARGETS = {
    "squad-shared-state-conflict-attenuation-2026-03": "squad-operational-history.json",
    "thclaws-team-workspace-interference-attenuation-2026": "thclaws-operational-history.json",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class S2ComparisonOwnership822Tests(unittest.TestCase):
    def test_comparison_limitation_has_one_neutral_owner(self):
        rows = {row["observation_id"]: row for row in load(S2 / "observations.json")}
        for observation_id, raw_filename in TARGETS.items():
            derived = rows[observation_id]
            self.assertNotIn("comparison_limitation", derived, observation_id)
            raw_record = load(RAW / raw_filename)
            raw_rows = [row for row in raw_record["observations"] if row["observation_id"] == observation_id]
            self.assertEqual(len(raw_rows), 1)
            value = raw_rows[0].get("comparison_limitation")
            self.assertIsInstance(value, str)
            self.assertTrue(value)

    def test_function_specific_s2_interpretation_remains_local(self):
        rows = {row["observation_id"]: row for row in load(S2 / "observations.json")}
        for observation_id in TARGETS:
            row = rows[observation_id]
            for key in (
                "disturbance",
                "coordination_relation",
                "subsequent_operation",
                "vsm_interpretation",
                "raw_observation_ref",
            ):
                self.assertIn(key, row, f"{observation_id}: {key}")
            self.assertTrue(row["canonical_system_eligible"])
            self.assertEqual(row["canonical_state_at_review"], "A")

    def test_raw_comparison_limitation_reconstructs_effective_row(self):
        rows = {row["observation_id"]: row for row in load(S2 / "observations.json")}
        for observation_id, raw_filename in TARGETS.items():
            raw_record = load(RAW / raw_filename)
            raw = next(row for row in raw_record["observations"] if row["observation_id"] == observation_id)
            effective = dict(raw)
            effective.update(rows[observation_id])
            self.assertEqual(effective["comparison_limitation"], raw["comparison_limitation"])


if __name__ == "__main__":
    unittest.main()
