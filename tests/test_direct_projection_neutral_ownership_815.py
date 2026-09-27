from __future__ import annotations

import json
import re
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments/functional-capability-depth"
RAW_DIR = EXP / "system-observations"
BASE_REF = "3a879693db8ac71290d5285b4763bb2ce13ece98"
S2_REL = "experiments/functional-capability-depth/s2-system-benchmarks/observations.json"
S3_REL = "experiments/functional-capability-depth/s3-system-benchmarks/observations.json"
MAO_ID = "multi-agent-orchestration-supervisor-ablation-2026-08"
NEUTRAL_OWNED = {
    "evidence_source_class", "system_compatibility", "primary_sources",
    "benchmark_artifact_revision", "comparison_class", "comparison_limitation",
}
FORBIDDEN_EXACT = {
    "function", "benchmark_fit", "vsm_interpretation",
    "canonical_state_at_review", "canonical_states_at_review",
    "canonical_system_eligible", "coverage_class",
}


def old_json(path: str):
    text = subprocess.check_output(["git", "show", f"{BASE_REF}:{path}"], cwd=ROOT, text=True)
    return json.loads(text)


def resolve(link: dict):
    ref = link["raw_observation_ref"]
    prefix = "../system-observations/"
    assert ref.startswith(prefix) and "#" in ref
    rel, oid = ref[len(prefix):].rsplit("#", 1)
    record = json.loads((RAW_DIR / rel).read_text(encoding="utf-8"))
    matches = [row for row in record["observations"] if row["observation_id"] == oid]
    assert len(matches) == 1
    return record, matches[0]


def hydrate_s2(row: dict, *, inject_record_level: bool) -> dict:
    record, raw = resolve(row)
    effective = dict(raw)
    if inject_record_level:
        effective["evidence_source_class"] = record["evidence_source_class"]
        effective["system_compatibility"] = record["published_implementation"]["system_compatibility"]
        effective["primary_sources"] = record["primary_sources"]
        if record.get("canonical_harness_id"):
            effective["canonical_review_ref"] = record["canonical_review_ref"]
    effective.update(row)
    return effective


def hydrate_s3(row: dict) -> dict:
    record, raw = resolve(row)
    effective = dict(row)
    for key, value in raw.items():
        if key in {"observation_id", "kind", "evidence_surface", "benchmark"}:
            continue
        effective[key] = value
    effective["evidence_source_class"] = record["evidence_source_class"]
    effective["system_compatibility"] = record["published_implementation"]["system_compatibility"]
    effective["primary_sources"] = record["primary_sources"]
    if record.get("canonical_harness_id"):
        effective["canonical_review_revision"] = record.get("canonical_review_ref")
    if row.get("observation_id") == MAO_ID:
        effective["benchmark_artifact_revision"] = record.get("canonical_review_ref")
        if "comparison_class" not in effective and isinstance(raw.get("comparison_design"), str):
            effective["comparison_class"] = raw["comparison_design"]
    return effective


def forbidden_key(key: str) -> bool:
    return (
        key in FORBIDDEN_EXACT
        or key.startswith("autonomy_s")
        or key.startswith("vsm_")
        or re.match(r"^canonical_.*state", key) is not None
    )


def walk(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


class DirectProjectionNeutralOwnership815Tests(unittest.TestCase):
    def test_s2_effective_rows_are_lossless(self):
        old_rows = old_json(S2_REL)
        new_rows = json.loads((ROOT / S2_REL).read_text(encoding="utf-8"))
        self.assertEqual([r["observation_id"] for r in old_rows], [r["observation_id"] for r in new_rows])
        old_by_id = {r["observation_id"]: r for r in old_rows}
        for row in new_rows:
            before = hydrate_s2(old_by_id[row["observation_id"]], inject_record_level=False)
            if before.get("canonical_harness_id"):
                before["canonical_review_ref"] = before.pop("canonical_assessment_ref")
            after = hydrate_s2(row, inject_record_level=True)
            self.assertEqual(after, before, row["observation_id"])
            self.assertFalse(NEUTRAL_OWNED & set(row), row["observation_id"])

    def test_mao_s3_effective_row_is_lossless_and_minimal(self):
        old_rows = old_json(S3_REL)
        new_rows = json.loads((ROOT / S3_REL).read_text(encoding="utf-8"))
        old = next(r for r in old_rows if r["observation_id"] == MAO_ID)
        new = next(r for r in new_rows if r["observation_id"] == MAO_ID)
        before = old
        after = hydrate_s3(new)
        stable_keys = (
            "observation_id",
            "function",
            "benchmark_id",
            "benchmark_fit",
            "evidence_source_class",
            "boundary_class",
            "canonical_harness_id",
            "canonical_system_eligible",
            "system_compatibility",
            "canonical_review_revision",
            "benchmark_artifact_revision",
            "result_artifact",
            "result_id",
            "result_started_at",
            "embedded_run_git_sha",
            "embedded_run_git_sha_publicly_resolvable_at_review",
            "scenario_count",
            "provider",
            "provider_configuration",
            "comparison_class",
            "held_constant",
            "primary_sources",
            "raw_observation_ref",
        )
        for key in stable_keys:
            self.assertEqual(after[key], before[key], key)
        self.assertEqual(new["vsm_interpretation"], before["vsm_interpretation"])
        self.assertIn("HeuristicRouter-only", after["treatment"])
        self.assertIn("six retry scenarios", after["scope_note"])
        self.assertIn("committed result artifact", after["provenance_limitation"])
        self.assertEqual(
            set(new),
            {
                "observation_id", "function", "benchmark_id", "benchmark_fit",
                "boundary_class", "canonical_harness_id", "canonical_system_eligible",
                "vsm_interpretation", "raw_observation_ref",
            },
        )

    def test_raw_registry_contains_no_vsm_state_or_function_attribution(self):
        files = sorted(RAW_DIR.glob("*.json"))
        self.assertTrue(files)
        hits = []
        for path in files:
            data = json.loads(path.read_text(encoding="utf-8"))
            for key in walk(data):
                if forbidden_key(key):
                    hits.append((path.name, key))
        self.assertEqual(hits, [])


if __name__ == "__main__":
    unittest.main()
