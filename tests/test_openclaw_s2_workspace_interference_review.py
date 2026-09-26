import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/matched-cell/openclaw-s2-workspace-interference-review.json"
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


class OpenClawS2WorkspaceInterferenceReviewTest(unittest.TestCase):
    def test_review_is_bound_to_current_canonical_openclaw(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        self.assertEqual(review["tracking_issue"], 756)
        self.assertEqual(review["function"], "S2")
        self.assertEqual(review["review_scope"], "post-matched-canonical-search-closure-delta")
        self.assertEqual(review["canonical_harness_id"], "openclaw")
        self.assertEqual(review["canonical_assessment_ref"], "387da5edaa9d6c6cfcfc15e167fe2e46d8647d86")
        self.assertEqual(review["canonical_s2_state"], "C")

        frontmatter = assessment_frontmatter("openclaw")
        self.assertEqual(frontmatter["status"], "included")
        self.assertEqual(frontmatter["review_ref"], review["canonical_assessment_ref"])
        self.assertEqual(frontmatter["autonomy_s2"], review["canonical_s2_state"])

    def test_semantic_rereview_dependency_is_explicit(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        semantic = review["canonical_semantic_rereview"]
        self.assertEqual(semantic["index_issue"], 263)
        self.assertEqual(semantic["state_at_review"], "open")
        self.assertIn("does not settle", semantic["reason"])
        self.assertIn("issue #263", review["reopen_when"])

    def test_upstream_surface_is_disturbance_not_attenuation(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        upstream = review["upstream_disturbance_issue"]
        self.assertEqual(upstream["repository"], "openclaw/openclaw")
        self.assertEqual(upstream["issue_number"], 113166)
        self.assertEqual(upstream["state_at_review"], "open")
        self.assertEqual(
            upstream["result_surface_state"],
            "source-reproducible-disturbance-no-attenuation-result",
        )
        self.assertTrue(upstream["upstream_review_source_reproducible"])
        self.assertFalse(upstream["upstream_review_live_reproduction"])
        self.assertFalse(upstream["published_fix_at_review"])
        self.assertFalse(upstream["published_native_attenuation_result_at_review"])
        self.assertFalse(upstream["published_matched_before_after_result_at_review"])

        source_check = review["current_upstream_source_check"]
        self.assertEqual(
            source_check["head_at_review"],
            "841f6f78e5f64baa73ad6f63b40648cf30b7943f",
        )
        self.assertTrue(source_check["shared_scope_single_key_without_isolation_subject"])
        self.assertTrue(source_check["rw_workspace_resolves_to_active_agent_workspace"])
        self.assertTrue(source_check["separate_agent_mount_omitted_when_workspace_equals_agent_workspace"])
        self.assertTrue(source_check["hot_config_mismatch_can_retain_running_container"])
        self.assertIn("disturbance evidence only", source_check["interpretation"])

    def test_review_does_not_admit_openclaw_or_reopen_primary(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        self.assertEqual(
            review["disposition"],
            "canonical-current-s2-source-reproducible-disturbance-no-attenuation-result",
        )
        self.assertEqual(review["result_surface_review"], "no-direct-s2-attenuation-result")
        self.assertFalse(review["creates_direct_benchmark_family"])
        self.assertFalse(review["creates_observation"])
        self.assertFalse(review["creates_canonical_direct_observation"])
        self.assertFalse(review["changes_primary_baseline"])
        self.assertFalse(review["reopen_condition_satisfied"])
        self.assertEqual(review["primary_baseline_after_review"], "gap")

        observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
        rows = [row for row in observations if row.get("canonical_harness_id") == "openclaw"]
        self.assertEqual(rows, [])

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

    def test_reopen_gate_requires_attenuation_and_public_provenance(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        self.assertIn("demonstrates attenuation", review["reopen_when"])
        self.assertIn("distinct OpenClaw agents/workspaces", review["reopen_when"])
        self.assertIn("thClaws", review["comparability_note"])
        reasons = review["do_not_reopen_for"]
        self.assertTrue(any("disturbance report by itself" in reason for reason in reasons))
        self.assertTrue(any("fix commit without" in reason for reason in reasons))
        self.assertTrue(any("Opensiro-operated OpenClaw benchmark" in reason for reason in reasons))


if __name__ == "__main__":
    unittest.main()
