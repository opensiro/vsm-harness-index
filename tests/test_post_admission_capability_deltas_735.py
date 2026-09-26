import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"

ASSESSMENTS = {
    "agentharness-oklahomawhore": (
        ROOT / "assessments" / "agentharness-oklahomawhore.md",
        "6bedcf45fad75e21df5e5cac827a898ef5c7d228",
    ),
    "kot": (
        ROOT / "assessments" / "kot.md",
        "7cf18c4b8389a81ea2f15ab70d1b0bb31b44b6ab",
    ),
    "agentharness-alexandrmotologa": (
        ROOT / "assessments" / "agentharness-alexandrmotologa.md",
        "725ceee14b65bd95365e8e1c2394ac1b245e3b98",
    ),
    "rsih": (
        ROOT / "assessments" / "rsih.md",
        "737bf1f5a5a56f0c49bbd5180e71d651113038ac",
    ),
    "scion-gcp": (
        ROOT / "assessments" / "scion-gcp.md",
        "bdf5b6d135bb7585e242d2f08f4c54b3de2c2940",
    ),
}

FUNCTIONS = {
    "S2": {
        "assessment_key": "autonomy_s2",
        "states": {
            "agentharness-oklahomawhore": "A",
            "kot": "A",
            "scion-gcp": "C",
        },
        "delta": EXP / "s2-system-benchmarks" / "post-closure-deltas" / "agentharness-kot-scion-2026-09-26.json",
        "closure": EXP / "s2-system-benchmarks" / "matched-cell" / "s2-primary-search-closure.json",
        "registries": [EXP / "s2-system-benchmarks" / "observations.json"],
        "result_surface": "no-direct-s2-result",
    },
    "S3": {
        "assessment_key": "autonomy_s3",
        "states": {
            "agentharness-oklahomawhore": "A",
            "kot": "A",
            "scion-gcp": "A",
        },
        "delta": EXP / "s3-system-benchmarks" / "post-closure-deltas" / "agentharness-kot-scion-2026-09-26.json",
        "closure": EXP / "s3-system-benchmarks" / "matched-cell" / "s3-primary-search-closure.json",
        "registries": [EXP / "s3-system-benchmarks" / "observations.json"],
        "result_surface": "no-direct-s3-result",
    },
    "S3*": {
        "assessment_key": "autonomy_s3_star",
        "states": {
            "kot": "A",
            "agentharness-alexandrmotologa": "C",
        },
        "delta": EXP / "s3star-system-benchmarks" / "post-closure-deltas" / "kot-agentharness-alexandrmotologa-2026-09-26.json",
        "closure": EXP / "s3star-system-benchmarks" / "matched-cell" / "s3star-primary-search-closure.json",
        "registries": [
            EXP / "s3star-system-benchmarks" / "canonical_observations.json",
            EXP / "s3star-system-benchmarks" / "benchmark_observations.json",
        ],
        "result_surface": "no-direct-s3star-result",
    },
    "S4": {
        "assessment_key": "autonomy_s4",
        "states": {
            "rsih": "C",
            "scion-gcp": "A",
        },
        "delta": EXP / "s4-system-benchmarks" / "post-closure-deltas" / "rsih-scion-2026-09-26.json",
        "closure": EXP / "s4-system-benchmarks" / "matched-cell" / "s4-primary-search-closure.json",
        "registries": [
            EXP / "s4-system-benchmarks" / "canonical_observations.json",
            EXP / "s4-system-benchmarks" / "benchmark_observations.json",
            EXP / "s4-system-benchmarks" / "proxy_observations.json",
        ],
        "result_surface": "no-direct-s4-result",
    },
    "S5": {
        "assessment_key": "autonomy_s5",
        "states": {"rsih": "C"},
        "delta": EXP / "s5-system-benchmarks" / "post-closure-deltas" / "rsih-2026-09-26.json",
        "closure": EXP / "s5-system-benchmarks" / "matched-cell" / "s5-primary-search-closure.json",
        "registries": [
            EXP / "s5-system-benchmarks" / "canonical_observations.json",
            EXP / "s5-system-benchmarks" / "benchmark_observations.json",
        ],
        "result_surface": "no-direct-s5-result",
    },
}


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"missing front matter: {path}")
    block = text.split("---\n", 2)[1]
    fields: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def contains_canonical_id(value, harness_ids: set[str]) -> bool:
    if isinstance(value, dict):
        if value.get("canonical_harness_id") in harness_ids:
            return True
        return any(contains_canonical_id(v, harness_ids) for v in value.values())
    if isinstance(value, list):
        return any(contains_canonical_id(v, harness_ids) for v in value)
    return False


class PostAdmissionCapabilityDelta735Test(unittest.TestCase):
    def test_late_public_evidence_deltas_are_fail_closed(self):
        assessment_fields: dict[str, dict[str, str]] = {}
        for harness_id, (path, review_ref) in ASSESSMENTS.items():
            fields = frontmatter(path)
            self.assertEqual(fields.get("status"), "included", harness_id)
            self.assertEqual(fields.get("review_ref"), review_ref, harness_id)
            assessment_fields[harness_id] = fields

        for function, cfg in FUNCTIONS.items():
            with self.subTest(function=function):
                expected_states = cfg["states"]
                for harness_id, state in expected_states.items():
                    self.assertEqual(
                        assessment_fields[harness_id].get(cfg["assessment_key"]),
                        state,
                        f"{function}:{harness_id}",
                    )

                delta = json.loads(cfg["delta"].read_text(encoding="utf-8"))
                self.assertEqual(delta.get("schema_version"), 1)
                self.assertEqual(delta.get("status"), "experimental-non-normative")
                self.assertEqual(delta.get("tracking_issue"), 735)
                self.assertEqual(delta.get("reviewed_at"), "2026-09-26")
                self.assertEqual(delta.get("function"), function)
                self.assertIn(
                    delta.get("disposition"),
                    {"canonical-mechanism-no-direct-result", "canonical-mechanisms-no-direct-results"},
                )
                self.assertFalse(delta.get("capability_counts_changed"))
                self.assertFalse(delta.get("observation_registry_mutated"))
                self.assertFalse(delta.get("primary_baseline_changed"))
                self.assertFalse(delta.get("reopen_condition_satisfied"))

                rows = delta.get("systems")
                self.assertIsInstance(rows, list)
                by_id = {row.get("canonical_harness_id"): row for row in rows}
                self.assertEqual(set(by_id), set(expected_states))

                for harness_id, state in expected_states.items():
                    row = by_id[harness_id]
                    self.assertEqual(row.get("canonical_state_at_review"), state)
                    self.assertEqual(row.get("canonical_review_ref"), ASSESSMENTS[harness_id][1])
                    self.assertEqual(row.get("result_surface_review"), cfg["result_surface"])
                    self.assertTrue(row.get("repository", "").startswith("https://github.com/"))
                    self.assertGreaterEqual(len(row.get("primary_sources", [])), 3)
                    self.assertGreater(len(row.get("finding", "")), 100)

                closure = json.loads(cfg["closure"].read_text(encoding="utf-8"))
                self.assertEqual(closure.get("primary_baseline"), "gap")
                self.assertEqual(closure.get("disposition"), "evidence-backed-gap")

                for registry_path in cfg["registries"]:
                    registry = json.loads(registry_path.read_text(encoding="utf-8"))
                    self.assertFalse(
                        contains_canonical_id(registry, set(expected_states)),
                        f"newly reviewed systems unexpectedly appeared in {registry_path}",
                    )


if __name__ == "__main__":
    unittest.main()
