from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
S2 = ROOT / "experiments" / "functional-capability-depth" / "s2-system-benchmarks"
MAP = ROOT / "experiments" / "functional-capability-depth" / "vsm-benchmark-family-map" / "map.json"


class GritS2PublicEvidenceReviewTest(unittest.TestCase):
    def test_review_remains_fail_closed_without_new_provenance_transaction(self) -> None:
        review = json.loads((S2 / "grit-public-evidence-review.json").read_text(encoding="utf-8"))

        self.assertEqual(review["status"], "reviewed-no-admitted-result")
        self.assertEqual(review["tracking_issue"], 619)
        self.assertEqual(review["function"], "S2")
        self.assertEqual(
            review["review_ref"],
            "0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe",
        )
        self.assertEqual(review["benchmark_fit"], "candidate-direct")
        self.assertIsNone(review["canonical_harness_id"])
        self.assertFalse(review["family_promoted"])
        self.assertFalse(review["observation_admitted"])
        self.assertFalse(review["primary_baseline_eligible"])
        self.assertGreaterEqual(len(review["blocking_reasons"]), 4)
        self.assertGreaterEqual(len(review["reopen_when"]), 3)

    def test_grit_has_not_silently_entered_observation_or_direct_family_state(self) -> None:
        observations = json.loads((S2 / "observations.json").read_text(encoding="utf-8"))
        self.assertFalse(
            any("grit" in json.dumps(row).lower() for row in observations),
            "Grit requires a new provenance review before observation admission",
        )

        benchmark_map = json.loads(MAP.read_text(encoding="utf-8"))
        direct_s2 = [
            row
            for row in benchmark_map.get("entries", [])
            if row.get("function") == "S2" and row.get("fit") == "direct"
        ]
        self.assertFalse(
            any("grit" in json.dumps(row).lower() for row in direct_s2),
            "Grit requires a new evidence transaction before direct-family promotion",
        )


if __name__ == "__main__":
    unittest.main()
