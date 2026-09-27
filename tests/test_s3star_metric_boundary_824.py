from __future__ import annotations

import copy
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
RAW_PATH = EXP / "system-observations" / "data-to-paper-review-revision.json"
PROJECTION_PATH = EXP / "s3star-system-benchmarks" / "canonical_observations.json"
BASE_REF = "fb1601845884ea16b1c0786e40b8976dae6e569b"
OBSERVATION_ID = "data-to-paper-review-revision-2024"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def historical_raw():
    text = subprocess.check_output(
        [
            "git", "show",
            f"{BASE_REF}:experiments/functional-capability-depth/system-observations/data-to-paper-review-revision.json",
        ],
        cwd=ROOT,
        text=True,
    )
    return json.loads(text)


class S3StarMetricBoundary824Tests(unittest.TestCase):
    def test_raw_payload_diff_is_exactly_one_removed_function_key(self):
        before = historical_raw()
        after = load(RAW_PATH)
        before_without_boundary = copy.deepcopy(before)
        observations = [
            row for row in before_without_boundary["observations"]
            if row.get("observation_id") == OBSERVATION_ID
        ]
        self.assertEqual(len(observations), 1)
        self.assertIs(observations[0].pop("aggregate_s3star_metric_reported"), False)
        self.assertEqual(after, before_without_boundary)

    def test_function_specific_metric_absence_is_derived_only(self):
        raw = load(RAW_PATH)
        raw_observation = next(
            row for row in raw["observations"]
            if row["observation_id"] == OBSERVATION_ID
        )
        self.assertNotIn("aggregate_s3star_metric_reported", raw_observation)
        self.assertIn("does not report an aggregate S3*-specific", raw_observation["metric_note"])

        projections = load(PROJECTION_PATH)
        derived = next(
            row for row in projections
            if row["observation_id"] == OBSERVATION_ID
        )
        self.assertIs(derived["aggregate_s3star_metric_reported"], False)
        self.assertEqual(derived["function"], "S3*")
        self.assertEqual(derived["benchmark_fit"], "direct")
        self.assertTrue(derived["canonical_system_eligible"])

        effective = dict(derived)
        for key, value in raw_observation.items():
            if key in {"observation_id", "kind", "evidence_surface", "non_claim"}:
                continue
            self.assertTrue(key not in effective or effective[key] == value, key)
            effective[key] = value
        self.assertIs(effective["aggregate_s3star_metric_reported"], False)
        self.assertEqual(effective["comparison_class"], "descriptive-only")
        self.assertEqual(effective["published_example_count"], 1)


if __name__ == "__main__":
    unittest.main()
