from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DELTA = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/post-closure-deltas/shep-axocoatl-2026-09-25.json"
COVERAGE = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/coverage.json"
OBSERVATIONS = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/observations.json"
BASELINES = ROOT / "experiments/functional-capability-depth/primary-baselines.json"

EXPECTED = {
    "shep": ("C", "a874b3238fd01ebdbafc11015cccd9a63ed6e2f2"),
    "axocoatl": ("C", "edfe5031463686dc782cf3539e5aabae4e8eb9ab"),
}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    block = text.split("---\n", 2)[1]
    out: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip()
    return out


class TestS2PostClosureShepAxocoatl(unittest.TestCase):
    def test_delta_is_fail_closed_and_non_admitting(self) -> None:
        delta = json.loads(DELTA.read_text(encoding="utf-8"))
        self.assertEqual(delta["tracking_issue"], 626)
        self.assertEqual(delta["function"], "S2")
        self.assertEqual(delta["disposition"], "canonical-mechanisms-no-direct-results")
        self.assertFalse(delta["capability_counts_changed"])
        self.assertFalse(delta["observation_registry_mutated"])
        self.assertFalse(delta["primary_baseline_changed"])
        self.assertFalse(delta["reopen_condition_satisfied"])

        rows = {row["canonical_harness_id"]: row for row in delta["systems"]}
        self.assertEqual(set(rows), set(EXPECTED))
        for harness_id, (state, review_ref) in EXPECTED.items():
            fields = frontmatter(ROOT / "assessments" / f"{harness_id}.md")
            self.assertEqual(fields.get("status"), "included")
            self.assertEqual(fields.get("autonomy_s2"), state)
            self.assertEqual(fields.get("review_ref"), review_ref)
            self.assertEqual(rows[harness_id]["canonical_state_at_review"], state)
            self.assertEqual(rows[harness_id]["canonical_review_ref"], review_ref)
            self.assertEqual(rows[harness_id]["result_surface_review"], "no-direct-s2-result")

        # This regression test proves only that the Shep/Axocoatl delta itself
        # did not admit capability evidence. Later independent public-evidence
        # transactions may legitimately increase the global S2 family or
        # observation counts, so bind those counts to their current sources of
        # truth rather than freezing the values that happened to exist at #626.
        coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
        observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
        baselines = json.loads(BASELINES.read_text(encoding="utf-8"))
        reviewed_families = baselines["functions"]["S2"]["reviewed_direct_families"]

        self.assertEqual(
            coverage["direct_benchmark_family_count"],
            len(reviewed_families),
        )
        self.assertEqual(coverage["direct_observation_count"], len(observations))
        self.assertEqual(coverage["canonical_direct_observation_count"], 0)
        self.assertEqual(coverage["proxy_projection_count"], 2)
        self.assertEqual(len(coverage["representative_canonical_s2_systems_inspected"]), 15)
        self.assertIn("shep", coverage["representative_canonical_s2_systems_inspected"])
        self.assertIn("axocoatl", coverage["representative_canonical_s2_systems_inspected"])
        self.assertNotIn(
            "shep",
            {row.get("canonical_harness_id") for row in observations},
        )
        self.assertNotIn(
            "axocoatl",
            {row.get("canonical_harness_id") for row in observations},
        )
        self.assertEqual(baselines["functions"]["S2"]["status"], "gap")


if __name__ == "__main__":
    unittest.main()
