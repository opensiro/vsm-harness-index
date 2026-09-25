from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DELTA = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/post-closure-deltas/lime-2026-09-25.json"
COVERAGE = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/coverage.json"
OBSERVATIONS = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/observations.json"
BASELINES = ROOT / "experiments/functional-capability-depth/primary-baselines.json"

EXPECTED_STATE = "C"
EXPECTED_REF = "3823e9092d4106c877ae08a1d19d593b647cf27d"


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


class TestS2PostClosureLime(unittest.TestCase):
    def test_lime_delta_is_fail_closed_and_non_admitting(self) -> None:
        delta = json.loads(DELTA.read_text(encoding="utf-8"))
        self.assertEqual(delta["tracking_issue"], 657)
        self.assertEqual(delta["function"], "S2")
        self.assertEqual(delta["disposition"], "canonical-mechanism-no-direct-result")
        self.assertFalse(delta["capability_counts_changed"])
        self.assertFalse(delta["observation_registry_mutated"])
        self.assertFalse(delta["primary_baseline_changed"])
        self.assertFalse(delta["reopen_condition_satisfied"])

        self.assertEqual(len(delta["systems"]), 1)
        row = delta["systems"][0]
        self.assertEqual(row["canonical_harness_id"], "lime")
        self.assertEqual(row["canonical_state_at_review"], EXPECTED_STATE)
        self.assertEqual(row["canonical_review_ref"], EXPECTED_REF)
        self.assertEqual(row["result_surface_review"], "no-direct-s2-result")

        fields = frontmatter(ROOT / "assessments" / "lime.md")
        self.assertEqual(fields.get("status"), "included")
        self.assertEqual(fields.get("autonomy_s2"), EXPECTED_STATE)
        self.assertEqual(fields.get("review_ref"), EXPECTED_REF)

        coverage = json.loads(COVERAGE.read_text(encoding="utf-8"))
        observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
        baselines = json.loads(BASELINES.read_text(encoding="utf-8"))
        reviewed_families = baselines["functions"]["S2"]["reviewed_direct_families"]

        self.assertEqual(coverage["direct_benchmark_family_count"], len(reviewed_families))
        self.assertEqual(coverage["direct_observation_count"], len(observations))
        self.assertEqual(coverage["canonical_direct_observation_count"], 0)
        self.assertEqual(coverage["proxy_projection_count"], 2)
        self.assertIn("lime", coverage["representative_canonical_s2_systems_inspected"])
        self.assertNotIn(
            "lime",
            {observation.get("canonical_harness_id") for observation in observations},
        )
        self.assertEqual(baselines["functions"]["S2"]["status"], "gap")


if __name__ == "__main__":
    unittest.main()
