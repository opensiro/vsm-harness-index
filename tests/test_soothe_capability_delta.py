import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
ASSESSMENT = ROOT / "assessments" / "soothe.md"
REVIEW_REF = "be4fa14c0aa53203b8861dbff367eccb0df77668"

FUNCTIONS = {
    "S2": {
        "assessment_key": "autonomy_s2",
        "delta": EXP / "s2-system-benchmarks" / "post-closure-deltas" / "soothe-2026-09-26.json",
        "closure": EXP / "s2-system-benchmarks" / "matched-cell" / "s2-primary-search-closure.json",
        "registries": [EXP / "s2-system-benchmarks" / "observations.json"],
        "result_surface": "no-direct-s2-result",
    },
    "S3": {
        "assessment_key": "autonomy_s3",
        "delta": EXP / "s3-system-benchmarks" / "post-closure-deltas" / "soothe-2026-09-26.json",
        "closure": EXP / "s3-system-benchmarks" / "matched-cell" / "s3-primary-search-closure.json",
        "registries": [EXP / "s3-system-benchmarks" / "observations.json"],
        "result_surface": "no-direct-s3-result",
    },
    "S3*": {
        "assessment_key": "autonomy_s3_star",
        "delta": EXP / "s3star-system-benchmarks" / "post-closure-deltas" / "soothe-2026-09-26.json",
        "closure": EXP / "s3star-system-benchmarks" / "matched-cell" / "s3star-primary-search-closure.json",
        "registries": [
            EXP / "s3star-system-benchmarks" / "canonical_observations.json",
            EXP / "s3star-system-benchmarks" / "benchmark_observations.json",
        ],
        "result_surface": "no-direct-s3star-result",
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


def contains_soothe_canonical_id(value) -> bool:
    if isinstance(value, dict):
        if value.get("canonical_harness_id") == "soothe":
            return True
        return any(contains_soothe_canonical_id(v) for v in value.values())
    if isinstance(value, list):
        return any(contains_soothe_canonical_id(v) for v in value)
    return False


class SootheCapabilityDeltaTest(unittest.TestCase):
    def test_negative_public_evidence_delta_is_fail_closed(self):
        fields = frontmatter(ASSESSMENT)
        self.assertEqual(fields.get("status"), "included")
        self.assertEqual(fields.get("review_ref"), REVIEW_REF)

        for function, cfg in FUNCTIONS.items():
            with self.subTest(function=function):
                self.assertEqual(fields.get(cfg["assessment_key"]), "C")

                delta = json.loads(cfg["delta"].read_text(encoding="utf-8"))
                self.assertEqual(delta.get("schema_version"), 1)
                self.assertEqual(delta.get("status"), "experimental-non-normative")
                self.assertEqual(delta.get("tracking_issue"), 671)
                self.assertEqual(delta.get("reviewed_at"), "2026-09-26")
                self.assertEqual(delta.get("function"), function)
                self.assertEqual(delta.get("disposition"), "canonical-mechanism-no-direct-result")
                self.assertFalse(delta.get("capability_counts_changed"))
                self.assertFalse(delta.get("observation_registry_mutated"))
                self.assertFalse(delta.get("primary_baseline_changed"))
                self.assertFalse(delta.get("reopen_condition_satisfied"))

                rows = delta.get("systems")
                self.assertIsInstance(rows, list)
                self.assertEqual(len(rows), 1)
                row = rows[0]
                self.assertEqual(row.get("canonical_harness_id"), "soothe")
                self.assertEqual(row.get("canonical_state_at_review"), "C")
                self.assertEqual(row.get("canonical_review_ref"), REVIEW_REF)
                self.assertEqual(row.get("repository"), "https://github.com/mirasoth/soothe")
                self.assertEqual(row.get("result_surface_review"), cfg["result_surface"])
                self.assertGreaterEqual(len(row.get("primary_sources", [])), 4)
                self.assertGreater(len(row.get("finding", "")), 100)

                closure = json.loads(cfg["closure"].read_text(encoding="utf-8"))
                self.assertEqual(closure.get("primary_baseline"), "gap")
                self.assertEqual(closure.get("disposition"), "evidence-backed-gap")

                for registry_path in cfg["registries"]:
                    registry = json.loads(registry_path.read_text(encoding="utf-8"))
                    self.assertFalse(
                        contains_soothe_canonical_id(registry),
                        f"Soothe unexpectedly appeared in {registry_path}",
                    )


if __name__ == "__main__":
    unittest.main()
