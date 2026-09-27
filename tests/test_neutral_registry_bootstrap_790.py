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
    raise AssertionError(f"missing observation {observation_id}")


def raw_observation(filename: str, observation_id: str) -> tuple[dict, dict]:
    record = load(RAW / filename)
    return record, by_id(record["observations"], observation_id)


class NeutralRegistryBootstrap790Tests(unittest.TestCase):
    def test_multi_agent_orchestration_neutral_record_owns_numeric_payload(self) -> None:
        historical = load(EXPERIMENT / "s3-system-benchmarks" / "observations.json")
        derived = by_id(historical, "multi-agent-orchestration-supervisor-ablation-2026-08")
        record, raw = raw_observation(
            "multi-agent-orchestration.json",
            "multi-agent-orchestration-supervisor-ablation-2026-08",
        )
        self.assertEqual(
            derived["raw_observation_ref"],
            "../system-observations/multi-agent-orchestration.json#multi-agent-orchestration-supervisor-ablation-2026-08",
        )
        for key in (
            "baseline_arm",
            "supervisor_arm",
            "reported_completion_gain_percentage_points",
            "reported_routing_accuracy_gain_percentage_points",
        ):
            self.assertNotIn(key, derived)
        self.assertEqual(raw["baseline_arm"]["scenarios_passed"], 11)
        self.assertEqual(raw["supervisor_arm"]["scenarios_passed"], 48)
        self.assertEqual(raw["reported_completion_gain_percentage_points"], 68.5)
        self.assertEqual(raw["reported_routing_accuracy_gain_percentage_points"], 43.3333)
        self.assertEqual(record["canonical_review_ref"], derived["canonical_review_revision"])

    def test_a_evolve_neutral_record_owns_numeric_payload(self) -> None:
        historical = load(EXPERIMENT / "s4-system-benchmarks" / "canonical_observations.json")
        derived = by_id(historical, "a-evolve-harness-updating-2026")
        record, raw = raw_observation("a-evolve.json", "a-evolve-harness-updating-2026")
        self.assertEqual(
            derived["raw_observation_ref"],
            "../system-observations/a-evolve.json#a-evolve-harness-updating-2026",
        )
        self.assertNotIn("reported_harness_updating_metrics", derived)
        self.assertEqual(
            raw["reported_harness_updating_metrics"],
            {
                "maximum_best_vs_worst_evolver_spread_pp": 3.1,
                "qwen3_235b_swe_gain_pp": 8.2,
                "qwen3_235b_mcp_gain_pp": 0.6,
                "qwen3_5_9b_skillsbench_gain_pp": 3.8,
                "opus_4_6_skillsbench_gain_pp": 2.3,
                "qwen3_235b_skillsbench_gain_pp": 1.5,
            },
        )
        self.assertEqual(record["canonical_review_ref"], derived["canonical_review_revision"])

    def test_kadath_neutral_record_owns_numeric_payload(self) -> None:
        historical = load(EXPERIMENT / "s4-system-benchmarks" / "canonical_observations.json")
        derived = by_id(historical, "kadath-ten-epoch-native-evolution-2026")
        record, raw = raw_observation("kadath.json", "kadath-ten-epoch-native-evolution-2026")
        self.assertEqual(
            derived["raw_observation_ref"],
            "../system-observations/kadath.json#kadath-ten-epoch-native-evolution-2026",
        )
        self.assertNotIn("reported_population_metrics", derived)
        self.assertEqual(
            raw["reported_population_metrics"],
            {
                "best_fitness_epoch_1": 18,
                "best_fitness_epoch_10": 91,
                "best_fitness_improvement": 73,
                "top5_median_epoch_1": 8,
                "top5_median_epoch_10": 77,
                "top5_median_improvement": 69,
                "top5_floor_epoch_1": 1,
                "top5_floor_epoch_10": 71,
                "top5_floor_improvement": 70,
            },
        )
        self.assertEqual(record["canonical_review_ref"], derived["canonical_review_revision"])

    def test_bootstrap_raw_records_do_not_encode_function_attribution(self) -> None:
        for filename, observation_id in (
            ("multi-agent-orchestration.json", "multi-agent-orchestration-supervisor-ablation-2026-08"),
            ("a-evolve.json", "a-evolve-harness-updating-2026"),
            ("kadath.json", "kadath-ten-epoch-native-evolution-2026"),
        ):
            record, observation = raw_observation(filename, observation_id)
            self.assertNotIn("function", record)
            self.assertNotIn("benchmark_fit", record)
            self.assertNotIn("vsm_interpretation", record)
            self.assertNotIn("function", observation)
            self.assertNotIn("benchmark_fit", observation)
            self.assertNotIn("vsm_interpretation", observation)


if __name__ == "__main__":
    unittest.main()
