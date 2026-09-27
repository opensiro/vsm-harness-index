from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments" / "functional-capability-depth"
RAW_PATH = EXPERIMENT / "system-observations" / "appliedscientist.json"
HISTORICAL_PATH = EXPERIMENT / "s3star-system-benchmarks" / "canonical_observations.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


class AppliedScientistNeutralObservation792Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.raw = load(RAW_PATH)
        self.observation = self.raw["observations"][0]
        historical = load(HISTORICAL_PATH)
        self.old = next(
            row
            for row in historical
            if row["observation_id"] == "appliedscientist-iterative-review-2026-09"
        )

    def test_published_quantitative_payload_is_preserved(self) -> None:
        fields = (
            "paper_count",
            "rejected_paper_count",
            "borderline_paper_count",
            "revision_rounds",
            "reported_execution_weaknesses_total",
            "reported_execution_weaknesses_resolved",
            "reported_execution_weakness_resolution_rate",
            "reported_idea_weaknesses_total",
            "reported_idea_weaknesses_resolved",
            "reported_idea_weakness_resolution_rate",
        )
        for field in fields:
            self.assertEqual(self.observation[field], self.old[field], field)
        self.assertEqual(self.observation["revision_conditions"], self.old["revision_conditions"])

    def test_system_linkage_is_preserved_without_fake_run_binding(self) -> None:
        self.assertEqual(self.raw["canonical_harness_id"], "appliedscientist")
        self.assertEqual(
            self.raw["canonical_review_ref"],
            self.old["canonical_review_revision"],
        )
        self.assertEqual(
            self.raw["published_implementation"]["canonical_revision_match"],
            "publication-system-lineage-run-revision-unbound",
        )
        self.assertIn("does not expose an exact Git revision", self.raw["published_implementation"]["note"])
        self.assertIn("does not bind", self.observation["provenance_limitation"])

    def test_raw_record_contains_no_vsm_function_attribution(self) -> None:
        for container in (self.raw, self.observation):
            self.assertNotIn("function", container)
            self.assertNotIn("benchmark_fit", container)
            self.assertNotIn("vsm_interpretation", container)


if __name__ == "__main__":
    unittest.main()
