from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXP = ROOT / "experiments" / "functional-capability-depth"
S2 = EXP / "s2-system-benchmarks"
RAW = EXP / "system-observations"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def by_id(rows: list[dict], observation_id: str) -> dict:
    matches = [row for row in rows if row.get("observation_id") == observation_id]
    assert len(matches) == 1, (observation_id, len(matches))
    return matches[0]


MIGRATIONS = {
    "nool-trackd-scaleup1-contention-2026-08-21": {
        "filename": "nool-fleet-coordination.json",
        "system_name": "Nool fleet coordination benchmark organization",
        "benchmark": "Nool coding-agent fleet coordination benchmark — Track D scale-up 1",
        "kind": "benchmark-defined-coordination-ablation",
    },
    "specification-gap-recovery-2026-03": {
        "filename": "specification-gap.json",
        "system_name": "The Specification Gap benchmark organization",
        "benchmark": "The Specification Gap / AmbigClass 2×2 conflict-recovery experiment",
        "kind": "benchmark-defined-coordination-ablation",
    },
    "codecrdt-parallel-convergence-2025-10": {
        "filename": "codecrdt.json",
        "system_name": "CodeCRDT",
        "benchmark": "CodeCRDT sequential-versus-parallel evaluation",
        "kind": "native-system-outcome-study",
    },
    "grit-synthetic-merge-contention-2026-04": {
        "filename": "grit.json",
        "system_name": "Grit",
        "benchmark": "Grit synthetic merge-contention sweep",
        "kind": "native-mechanism-ablation",
    },
}

SEMANTIC_ONLY_KEYS = {
    "function",
    "benchmark_fit",
    "boundary_class",
    "canonical_harness_id",
    "canonical_system_eligible",
    "canonical_assessment_ref",
    "canonical_state_at_review",
    "system_compatibility",
    "vsm_interpretation",
    "primary_sources",
    "evidence_source_class",
}

DERIVED_KEYS = {
    "observation_id",
    "function",
    "benchmark_id",
    "benchmark_fit",
    "evidence_source_class",
    "boundary_class",
    "canonical_harness_id",
    "canonical_system_eligible",
    "canonical_assessment_ref",
    "canonical_state_at_review",
    "system_compatibility",
    "comparison_class",
    "benchmark_artifact_revision",
    "vsm_interpretation",
    "primary_sources",
}

observations_path = S2 / "observations.json"
observations = load(observations_path)

for observation_id, spec in MIGRATIONS.items():
    source = by_id(observations, observation_id)
    assert "raw_observation_ref" not in source, f"{observation_id}: already migrated"

    raw_observation = {
        key: value
        for key, value in source.items()
        if key not in SEMANTIC_ONLY_KEYS
    }
    raw_observation["benchmark"] = spec["benchmark"]
    raw_observation["kind"] = spec["kind"]

    record = {
        "schema_version": 1,
        "recorded_at": "2026-09-27",
        "evidence_source_class": source["evidence_source_class"],
        "system_name": spec["system_name"],
        "canonical_harness_id": None,
        "published_implementation": {
            "system_compatibility": source["system_compatibility"],
            "source_revision": source.get("benchmark_artifact_revision"),
            "historical_relation": "preserved from the pre-neutral S2 evidence record; no canonical S2 linkage is introduced by this migration",
        },
        "primary_sources": source["primary_sources"],
        "observations": [raw_observation],
    }
    dump(RAW / spec["filename"], record)

    derived = {key: value for key, value in source.items() if key in DERIVED_KEYS}
    derived["raw_observation_ref"] = f"../system-observations/{spec['filename']}#{observation_id}"
    source.clear()
    source.update(derived)

dump(observations_path, observations)

# Hydrate migrated derived rows for all existing S2 validation without changing the validation targets.
validator_path = S2 / "validate.py"
text = validator_path.read_text(encoding="utf-8")
helper_anchor = "\ndef validate_proxy_links(coverage: dict, by_id: dict[str, dict]) -> None:\n"
assert helper_anchor in text
helper = '''
def hydrate_raw_observation(row: dict) -> dict:
    ref = row.get("raw_observation_ref")
    if ref is None:
        return row
    if not isinstance(ref, str) or not ref.startswith("../system-observations/") or "#" not in ref:
        fail(f"{row.get('observation_id')}: invalid raw_observation_ref")
    path_part, raw_id = ref.split("#", 1)
    raw_path = (HERE / path_part).resolve()
    if raw_path.parent != SYSTEM_OBSERVATIONS.resolve() or not raw_path.is_file():
        fail(f"{row.get('observation_id')}: raw observation record missing or outside shared directory")
    record = json.loads(raw_path.read_text(encoding="utf-8"))
    matches = [candidate for candidate in record.get("observations", []) if candidate.get("observation_id") == raw_id]
    if len(matches) != 1 or raw_id != row.get("observation_id"):
        fail(f"{row.get('observation_id')}: neutral raw observation identity drift")
    raw = matches[0]
    for forbidden in ("function", "benchmark_fit", "vsm_interpretation"):
        if forbidden in record or forbidden in raw:
            fail(f"{row.get('observation_id')}: neutral raw record leaked VSM interpretation field {forbidden}")
    hydrated = dict(raw)
    hydrated.update(row)
    return hydrated


def validate_proxy_links(coverage: dict, by_id: dict[str, dict]) -> None:
'''
text = text.replace(helper_anchor, helper, 1)

main_anchor = '    observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))\n'
assert main_anchor in text
text = text.replace(
    main_anchor,
    main_anchor + '    observations = [hydrate_raw_observation(row) for row in observations]\n',
    1,
)
validator_path.write_text(text, encoding="utf-8")

# Regression: disk-level S2 rows are derived-only for the four migrated result surfaces.
test_path = ROOT / "tests" / "test_s2_neutral_registry_migration_797.py"
test_path.write_text('''from __future__ import annotations

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
''', encoding="utf-8")
