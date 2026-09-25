from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
S2 = ROOT / "experiments" / "functional-capability-depth" / "s2-system-benchmarks"
MAP = ROOT / "experiments" / "functional-capability-depth" / "vsm-benchmark-family-map" / "map.json"
CLOSURE = S2 / "matched-cell" / "s2-primary-search-closure.json"


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

    def test_explicit_provenance_transaction_admits_grit_noncanonically(self) -> None:
        observations = json.loads((S2 / "observations.json").read_text(encoding="utf-8"))
        grit_rows = [
            row
            for row in observations
            if row.get("observation_id") == "grit-synthetic-merge-contention-2026-04"
        ]
        self.assertEqual(len(grit_rows), 1)
        observation = grit_rows[0]
        self.assertEqual(
            observation["benchmark_artifact_revision"],
            "a2c48735e0a16c49ca1541c4865fce438c479405",
        )
        self.assertEqual(observation["evidence_source_class"], "first-party-reported")
        self.assertEqual(observation["system_compatibility"], "native-system")
        self.assertEqual(observation["comparison_class"], "partially-matched")
        self.assertIsNone(observation["canonical_harness_id"])
        self.assertFalse(observation["canonical_system_eligible"])

        benchmark_map = json.loads(MAP.read_text(encoding="utf-8"))
        grit_families = [
            row
            for row in benchmark_map.get("entries", [])
            if row.get("function") == "S2"
            and row.get("benchmark_id") == "grit-merge-contention"
        ]
        self.assertEqual(len(grit_families), 1)
        self.assertEqual(grit_families[0]["fit"], "direct")
        self.assertEqual(grit_families[0]["system_linkage"], "external-native-noncanonical")

        closure = json.loads(CLOSURE.read_text(encoding="utf-8"))
        self.assertEqual(closure["grit_public_evidence_issue"], 663)
        self.assertEqual(closure["primary_baseline"], "gap")
        self.assertEqual(closure["evidence_depth"]["canonical_direct_observations"], 0)


if __name__ == "__main__":
    unittest.main()
