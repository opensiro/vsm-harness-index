import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/matched-cell/bamboo-s2-review.json"
MATCHED_CLOSURE = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/matched-cell/s2-matched-canonical-search-closure.json"
OBSERVATIONS = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/observations.json"
BASELINES = ROOT / "experiments/functional-capability-depth/primary-baselines.json"


def assessment_frontmatter(harness_id: str) -> dict[str, str]:
    path = ROOT / "assessments" / f"{harness_id}.md"
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---", text, flags=re.DOTALL)
    if not match:
        raise AssertionError(f"missing frontmatter in {path}")
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


class BambooS2PostClosureReviewTest(unittest.TestCase):
    def test_review_is_bound_to_canonical_bamboo(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        self.assertEqual(review["tracking_issue"], 698)
        self.assertEqual(review["function"], "S2")
        self.assertEqual(review["review_scope"], "post-matched-canonical-search-closure-delta")
        self.assertEqual(review["canonical_harness_id"], "bamboo")
        self.assertEqual(review["canonical_assessment_ref"], "eb1151378d513e820f80513c387056fb14f5c664")
        self.assertEqual(review["canonical_s2_state"], "A")
        self.assertEqual(review["disposition"], "canonical-mechanism-public-eval-planned-no-results")
        self.assertEqual(review["result_surface_review"], "no-direct-s2-result")

        frontmatter = assessment_frontmatter("bamboo")
        self.assertEqual(frontmatter["status"], "included")
        self.assertEqual(frontmatter["review_ref"], review["canonical_assessment_ref"])
        self.assertEqual(frontmatter["autonomy_s2"], review["canonical_s2_state"])

    def test_upstream_eval_is_recorded_as_planned_no_results(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        upstream = review["upstream_eval_issue"]
        self.assertEqual(upstream["repository"], "bigduu/Bamboo-agent")
        self.assertEqual(upstream["issue_number"], 902)
        self.assertEqual(upstream["title"], "[bamboo] eval: measure SubAgent delegation-contract behavior")
        self.assertEqual(upstream["state_at_review"], "open")
        self.assertEqual(upstream["comments_at_review"], 0)
        self.assertEqual(upstream["result_surface_state"], "planned-open-no-results")
        self.assertFalse(upstream["published_results_at_review"])
        self.assertFalse(upstream["published_raw_fixtures_at_review"])
        self.assertFalse(upstream["owner_reviewed_interpretation_at_review"])

        direct_fields = {field.lower() for field in upstream["planned_direct_s2_fields"]}
        self.assertIn("scope violations", direct_fields)
        self.assertIn("duplicate/overlapping assignment", direct_fields)
        self.assertIn("unnecessary nested spawn", direct_fields)

    def test_review_does_not_admit_bamboo_or_reopen_primary(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        self.assertFalse(review["creates_direct_benchmark_family"])
        self.assertFalse(review["creates_observation"])
        self.assertFalse(review["creates_canonical_direct_observation"])
        self.assertFalse(review["changes_primary_baseline"])
        self.assertFalse(review["reopen_condition_satisfied"])
        self.assertEqual(review["primary_baseline_after_review"], "gap")

        observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
        bamboo_rows = [row for row in observations if row.get("canonical_harness_id") == "bamboo"]
        self.assertEqual(bamboo_rows, [])

        baselines = json.loads(BASELINES.read_text(encoding="utf-8"))
        self.assertEqual(baselines["functions"]["S2"]["status"], "gap")

    def test_closed_matched_search_snapshot_is_not_rewritten(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        closure = json.loads(MATCHED_CLOSURE.read_text(encoding="utf-8"))

        self.assertEqual(closure["tracking_issue"], 696)
        self.assertEqual(closure["primary_baseline"], "gap")
        self.assertEqual(
            [row["canonical_harness_id"] for row in closure["canonical_direct_anchors"]],
            ["squad", "thclaws"],
        )
        historical = review["historical_matched_search_snapshot"]
        self.assertEqual(historical["tracking_issue"], closure["tracking_issue"])
        self.assertEqual(historical["primary_baseline"], closure["primary_baseline"])
        self.assertEqual(historical["canonical_direct_anchor_ids"], ["squad", "thclaws"])
        self.assertFalse(historical["rewrite_allowed"])

    def test_review_preserves_public_evidence_only_boundary(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        self.assertTrue(
            any("Opensiro-operated Bamboo benchmark" in reason for reason in review["do_not_reopen_for"])
        )
        self.assertIn("without Opensiro-operated reproduction", review["reopen_when"])


if __name__ == "__main__":
    unittest.main()
