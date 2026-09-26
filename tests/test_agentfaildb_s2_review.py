import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/matched-cell/agentfaildb-s2-review.json"
CLOSURE = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/matched-cell/s2-primary-search-closure.json"
OBSERVATIONS = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/observations.json"


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


class AgentFailDBS2ReviewTest(unittest.TestCase):
    def test_review_is_fail_closed_against_current_canonical_states(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        self.assertEqual(review["tracking_issue"], 688)
        self.assertEqual(review["upstream_revision"], "870bade0db014281362cfe5a7c41e9be4bde86d0")
        self.assertEqual(review["disposition"], "matched-framework-non-direct-s2")
        self.assertFalse(review["creates_direct_benchmark_family"])
        self.assertFalse(review["creates_observation"])
        self.assertFalse(review["creates_canonical_direct_observation"])
        self.assertFalse(review["changes_primary_baseline"])
        self.assertEqual(review["primary_baseline_after_review"], "gap")

        expected = {
            "autogen-agentchat": ("027ecf0a379bcc1d09956d46d12d44a3ad9cee14", "A"),
            "crewai": ("894898f84c4ac0a89f24bf7bee6c381eb0e67f51", "—"),
            "langgraph": ("e539ac122f4126f6dd850581c1494948cf620e31", "—"),
        }
        reviewed_rows = {row["canonical_harness_id"]: row for row in review["frameworks"]}
        self.assertEqual(set(reviewed_rows), set(expected))

        for harness_id, (expected_ref, expected_s2) in expected.items():
            frontmatter = assessment_frontmatter(harness_id)
            self.assertEqual(frontmatter["review_ref"], expected_ref)
            self.assertEqual(frontmatter["autonomy_s2"], expected_s2)
            self.assertEqual(reviewed_rows[harness_id]["canonical_assessment_ref"], expected_ref)
            self.assertEqual(reviewed_rows[harness_id]["canonical_s2_state"], expected_s2)
            self.assertFalse(reviewed_rows[harness_id]["native_s2_comparison_eligible"])

    def test_review_does_not_mutate_s2_observations_or_primary(self) -> None:
        closure = json.loads(CLOSURE.read_text(encoding="utf-8"))
        self.assertEqual(closure["primary_baseline"], "gap")

        observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
        serialized = json.dumps(observations).lower()
        self.assertNotIn("agentfaildb", serialized)
        self.assertNotIn("870bade0db014281362cfe5a7c41e9be4bde86d0", serialized)

    def test_conflicting_outputs_is_recorded_as_post_hoc_signal(self) -> None:
        review = json.loads(REVIEW.read_text(encoding="utf-8"))
        definition = review["candidate_signal_definition"].lower()
        self.assertIn("post-hoc", definition)
        self.assertIn("not a preregistered inter-s1 disturbance", definition)
        self.assertIn("only one compared canonical system has s2=a", " ".join(review["direct_s2_gate_failures"]).lower())


if __name__ == "__main__":
    unittest.main()
