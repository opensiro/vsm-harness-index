from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S2 = EXP / "s2-system-benchmarks"
RAW = EXP / "system-observations"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def by_id(rows: list[dict], observation_id: str) -> dict:
    matches = [row for row in rows if row.get("observation_id") == observation_id]
    if len(matches) != 1:
        raise AssertionError((observation_id, len(matches)))
    return matches[0]


class S2NeutralRegistryMigration797Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.derived = load(S2 / "observations.json")

    def raw(self, filename: str, observation_id: str) -> tuple[dict, dict]:
        record = load(RAW / filename)
        return record, by_id(record["observations"], observation_id)

    def assert_neutral(self, record: dict, raw: dict) -> None:
        for forbidden in ("function", "benchmark_fit", "vsm_interpretation"):
            self.assertNotIn(forbidden, record)
            self.assertNotIn(forbidden, raw)

    def test_nool_numeric_payload_owned_by_neutral_record(self) -> None:
        oid = "nool-trackd-scaleup1-contention-2026-08-21"
        row = by_id(self.derived, oid)
        record, raw = self.raw("nool-fleet-coordination.json", oid)
        self.assertEqual(row["raw_observation_ref"], f"../system-observations/nool-fleet-coordination.json#{oid}")
        for key in ("worker_count", "ticket_count", "git_uncoordinated_runs", "coordinated_runs", "excluded_variant"):
            self.assertNotIn(key, row)
        self.assertEqual([(r["accepted"], r["clean_merges"]) for r in raw["git_uncoordinated_runs"]], [(1, 14), (13, 13)])
        self.assertEqual([(r["accepted"], r["clean_merges"]) for r in raw["coordinated_runs"]], [(19, 20), (19, 20)])
        self.assert_neutral(record, raw)

    def test_specification_gap_numeric_payload_owned_by_neutral_record(self) -> None:
        oid = "specification-gap-recovery-2026-03"
        row = by_id(self.derived, oid)
        record, raw = self.raw("specification-gap.json", oid)
        self.assertEqual(row["raw_observation_ref"], f"../system-observations/specification-gap.json#{oid}")
        for key in ("task_count", "worker_count", "recovery_conditions", "single_agent_l0_ceiling", "reported_effects"):
            self.assertNotIn(key, row)
        self.assertEqual([r["pass_rate"] for r in raw["recovery_conditions"]], [0.527, 0.527, 0.889, 0.823])
        self.assertEqual(raw["reported_effects"]["full_specification_vs_blind_pp"], 36.2)
        self.assert_neutral(record, raw)

    def test_codecrdt_numeric_payload_owned_by_neutral_record(self) -> None:
        oid = "codecrdt-parallel-convergence-2025-10"
        row = by_id(self.derived, oid)
        record, raw = self.raw("codecrdt.json", oid)
        self.assertEqual(row["raw_observation_ref"], f"../system-observations/codecrdt.json#{oid}")
        for key in ("task_count", "total_evaluations", "sequential_runs", "parallel_runs", "environment", "reported_parallel_properties"):
            self.assertNotIn(key, row)
        self.assertEqual(raw["total_evaluations"], 600)
        self.assertEqual(raw["reported_parallel_properties"]["convergence_rate"], 1.0)
        self.assertEqual(raw["reported_parallel_properties"]["merge_failures"], 0)
        self.assert_neutral(record, raw)

    def test_grit_numeric_payload_owned_by_neutral_record(self) -> None:
        oid = "grit-synthetic-merge-contention-2026-04"
        row = by_id(self.derived, oid)
        record, raw = self.raw("grit.json", oid)
        self.assertEqual(row["raw_observation_ref"], f"../system-observations/grit.json#{oid}")
        for key in (
            "agent_counts",
            "rounds_per_iteration",
            "iterations",
            "reported_raw_git_failures_per_iteration",
            "reported_raw_git_conflicts_per_iteration",
            "reported_grit_failures",
            "reported_mean_raw_git_failure_rates",
            "reported_mean_grit_failure_rates",
        ):
            self.assertNotIn(key, row)
        self.assertEqual(raw["agent_counts"], [1, 2, 5, 10, 20, 50])
        self.assertEqual(raw["reported_grit_failures"], [0, 0, 0, 0, 0, 0])
        self.assertEqual(raw["reported_mean_grit_failure_rates"], {"1": 0.0, "2": 0.0, "5": 0.0, "10": 0.0, "20": 0.0, "50": 0.0})
        self.assertIsNone(record["canonical_harness_id"])
        self.assert_neutral(record, raw)

    def test_descriptive_nonbenchmark_witnesses_remain_function_specific(self) -> None:
        squad = by_id(self.derived, "squad-shared-state-conflict-attenuation-2026-03")
        thclaws = by_id(self.derived, "thclaws-team-workspace-interference-attenuation-2026")
        self.assertNotIn("raw_observation_ref", squad)
        self.assertNotIn("raw_observation_ref", thclaws)
        self.assertIsNone(squad.get("benchmark_id"))
        self.assertIsNone(thclaws.get("benchmark_id"))


if __name__ == "__main__":
    unittest.main()
