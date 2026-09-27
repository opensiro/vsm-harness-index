from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT = ROOT / "experiments" / "functional-capability-depth"
RAW = EXPERIMENT / "system-observations"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def by_id(rows: list[dict], observation_id: str) -> dict:
    for row in rows:
        if row.get("observation_id") == observation_id:
            return row
    raise AssertionError(f"missing historical observation {observation_id}")


def raw_observation(filename: str) -> tuple[dict, dict]:
    record = load(RAW / filename)
    if len(record["observations"]) != 1:
        raise AssertionError(f"expected one bootstrapped observation in {filename}")
    return record, record["observations"][0]


class NeutralRegistryBootstrap790Tests(unittest.TestCase):
    def test_multi_agent_orchestration_payload_matches_historical_projection(self) -> None:
        historical = load(EXPERIMENT / "s3-system-benchmarks" / "observations.json")
        old = by_id(historical, "multi-agent-orchestration-supervisor-ablation-2026-08")
        record, new = raw_observation("multi-agent-orchestration.json")

        self.assertEqual(new["observation_id"], old["observation_id"])
        self.assertEqual(new["baseline_arm"], old["baseline_arm"])
        self.assertEqual(new["supervisor_arm"], old["supervisor_arm"])
        self.assertEqual(
            new["reported_completion_gain_percentage_points"],
            old["reported_completion_gain_percentage_points"],
        )
        self.assertEqual(
            new["reported_routing_accuracy_gain_percentage_points"],
            old["reported_routing_accuracy_gain_percentage_points"],
        )
        self.assertEqual(record["canonical_review_ref"], old["canonical_review_revision"])

    def test_a_evolve_payload_matches_historical_projection(self) -> None:
        historical = load(EXPERIMENT / "s4-system-benchmarks" / "canonical_observations.json")
        old = by_id(historical, "a-evolve-harness-updating-2026")
        record, new = raw_observation("a-evolve.json")

        self.assertEqual(new["observation_id"], old["observation_id"])
        self.assertEqual(
            new["reported_harness_updating_metrics"],
            old["reported_harness_updating_metrics"],
        )
        self.assertEqual(new["benchmarks"], old["benchmarks"])
        self.assertEqual(new["anchor_agents"], old["anchor_agents"])
        self.assertEqual(new["evolver_models"], old["evolver_models"])
        self.assertEqual(record["canonical_review_ref"], old["canonical_review_revision"])

    def test_kadath_payload_matches_historical_projection(self) -> None:
        historical = load(EXPERIMENT / "s4-system-benchmarks" / "canonical_observations.json")
        old = by_id(historical, "kadath-ten-epoch-native-evolution-2026")
        record, new = raw_observation("kadath.json")

        self.assertEqual(new["observation_id"], old["observation_id"])
        self.assertEqual(new["epochs"], old["epochs"])
        self.assertEqual(new["benchmark_scope"], old["benchmark_scope"])
        self.assertEqual(
            new["reported_population_metrics"],
            old["reported_population_metrics"],
        )
        self.assertEqual(record["canonical_review_ref"], old["canonical_review_revision"])

    def test_bootstrap_raw_records_do_not_encode_function_attribution(self) -> None:
        for filename in (
            "multi-agent-orchestration.json",
            "a-evolve.json",
            "kadath.json",
        ):
            record, observation = raw_observation(filename)
            self.assertNotIn("function", record)
            self.assertNotIn("benchmark_fit", record)
            self.assertNotIn("vsm_interpretation", record)
            self.assertNotIn("function", observation)
            self.assertNotIn("benchmark_fit", observation)
            self.assertNotIn("vsm_interpretation", observation)


if __name__ == "__main__":
    unittest.main()
