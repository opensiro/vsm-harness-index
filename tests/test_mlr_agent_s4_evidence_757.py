import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
REVIEW_REF = "f728d571a992d71c8b526eeb4d9ab6bb5c8cc824"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise AssertionError(f"missing front matter: {path}")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields


def contains_canonical_id(value, harness_id: str) -> bool:
    if isinstance(value, dict):
        if value.get("canonical_harness_id") == harness_id:
            return True
        return any(contains_canonical_id(v, harness_id) for v in value.values())
    if isinstance(value, list):
        return any(contains_canonical_id(v, harness_id) for v in value)
    return False


class MLRAgentS4Evidence757Test(unittest.TestCase):
    def test_canonical_anchor_and_public_result_surface(self):
        assessment = frontmatter(ROOT / "assessments" / "mlr-agent.md")
        self.assertEqual(assessment.get("status"), "included")
        self.assertEqual(assessment.get("review_ref"), REVIEW_REF)
        self.assertEqual(assessment.get("autonomy_s1"), "A")
        self.assertEqual(assessment.get("autonomy_s2"), "—")
        self.assertEqual(assessment.get("autonomy_s3"), "—")
        self.assertEqual(assessment.get("autonomy_s3_star"), "—")
        self.assertEqual(assessment.get("autonomy_s4"), "A")
        self.assertEqual(assessment.get("autonomy_s5"), "—")

        raw = load(EXP / "system-observations" / "mlr-agent.json")
        self.assertEqual(raw.get("canonical_harness_id"), "mlr-agent")
        self.assertEqual(raw.get("canonical_review_ref"), REVIEW_REF)
        self.assertEqual(raw.get("canonical_states_at_review", {}).get("S4"), "A")
        self.assertEqual(raw.get("s4_classification"), "native-result-surface-no-direct-s4-observation")
        self.assertIn("do not isolate", raw.get("non_claim", ""))

        surfaces = {row["surface_id"]: row for row in raw.get("public_result_surfaces", [])}
        self.assertEqual(
            set(surfaces),
            {"mlrbench-proposal-generation-201-task", "mlrbench-end-to-end-10-task"},
        )
        proposal = surfaces["mlrbench-proposal-generation-201-task"]
        self.assertEqual(proposal.get("task_count"), 201)
        self.assertEqual(len(proposal.get("models", [])), 6)
        self.assertIn("does not isolate", proposal.get("interpretation", ""))

        end_to_end = surfaces["mlrbench-end-to-end-10-task"]
        self.assertEqual(end_to_end.get("task_count"), 10)
        results = {row["model"]: row for row in end_to_end.get("reported_average_results", [])}
        self.assertEqual(results["o4-mini-high"]["overall"], 3.95)
        self.assertEqual(results["Gemini-2.5-Pro-Preview"]["overall"], 3.75)
        self.assertEqual(results["Claude-3.7-Sonnet"]["overall"], 4.70)
        self.assertEqual(results["Claude-3.7-Sonnet"]["cost_usd"], 2.40)
        self.assertIn("mixes", end_to_end.get("interpretation", ""))

    def test_s4_delta_remains_non_admitted(self):
        delta = load(
            EXP
            / "s4-system-benchmarks"
            / "post-closure-deltas"
            / "mlr-agent-2026-09-26.json"
        )
        self.assertEqual(delta.get("tracking_issue"), 757)
        self.assertEqual(delta.get("canonical_harness_id"), "mlr-agent")
        self.assertEqual(delta.get("canonical_state_at_review"), "A")
        self.assertEqual(delta.get("canonical_review_ref"), REVIEW_REF)
        self.assertEqual(delta.get("result_surface_review"), "no-direct-s4-result")
        self.assertFalse(delta.get("capability_counts_changed"))
        self.assertFalse(delta.get("observation_registry_mutated"))
        self.assertFalse(delta.get("primary_baseline_changed"))
        self.assertFalse(delta.get("reopen_condition_satisfied"))
        self.assertGreaterEqual(len(delta.get("primary_sources", [])), 5)
        self.assertTrue(delta.get("reassess_if"))

        canonical = load(EXP / "s4-system-benchmarks" / "canonical_observations.json")
        benchmark = load(EXP / "s4-system-benchmarks" / "benchmark_observations.json")
        proxy = load(EXP / "s4-system-benchmarks" / "proxy_observations.json")
        self.assertFalse(contains_canonical_id(canonical, "mlr-agent"))
        self.assertFalse(contains_canonical_id(benchmark, "mlr-agent"))
        self.assertFalse(contains_canonical_id(proxy, "mlr-agent"))

        coverage = load(EXP / "s4-system-benchmarks" / "coverage.json")
        self.assertEqual(coverage.get("canonical_direct_observation_count"), len(canonical))
        self.assertEqual(coverage.get("composed_direct_observation_count"), len(benchmark))
        self.assertEqual(coverage.get("proxy_observation_count"), len(proxy))

        closure = load(
            EXP / "s4-system-benchmarks" / "matched-cell" / "s4-primary-search-closure.json"
        )
        self.assertEqual(closure.get("primary_baseline"), "gap")
        self.assertEqual(closure.get("disposition"), "evidence-backed-gap")


if __name__ == "__main__":
    unittest.main()
