from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
RAW = EXP / "system-observations"
S3STAR = EXP / "s3star-system-benchmarks"
BASE_REF = "fb1601845884ea16b1c0786e40b8976dae6e569b"
OID = "data-to-paper-review-revision-2024"
RAW_REL = "experiments/functional-capability-depth/system-observations/data-to-paper-review-revision.json"
PROJ_REL = "experiments/functional-capability-depth/s3star-system-benchmarks/canonical_observations.json"
KEY = "aggregate_s3star_metric_reported"


def git_text(path: str) -> str:
    return subprocess.check_output(["git", "show", f"{BASE_REF}:{path}"], cwd=ROOT, text=True)


def git_json(path: str):
    return json.loads(git_text(path))


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def by_id(rows: list[dict], oid: str) -> dict:
    matches = [row for row in rows if row.get("observation_id") == oid]
    assert len(matches) == 1
    return matches[0]


def hydrate(link: dict, record: dict) -> dict:
    raw = by_id(record["observations"], link["observation_id"])
    effective = dict(link)
    for key, value in raw.items():
        if key in {"kind", "evidence_surface", "non_claim", "observation_id"}:
            continue
        if key in effective and effective[key] != value:
            raise AssertionError(f"derived/raw conflict: {key}")
        effective[key] = value
    effective["evidence_source_class"] = record.get("evidence_source_class")
    effective["system_compatibility"] = (record.get("published_implementation") or {}).get("system_compatibility")
    effective["primary_sources"] = record.get("primary_sources")
    effective["canonical_review_revision"] = record.get("canonical_review_ref")
    return effective


class S3StarNeutralMetricKey824Tests(unittest.TestCase):
    def test_raw_changes_only_by_removing_the_s3star_metric_key(self) -> None:
        before = git_json(RAW_REL)
        after = load(RAW / "data-to-paper-review-revision.json")
        old_obs = by_id(before["observations"], OID)
        new_obs = by_id(after["observations"], OID)
        self.assertIs(old_obs[KEY], False)
        self.assertNotIn(KEY, new_obs)
        expected_obs = dict(old_obs)
        expected_obs.pop(KEY)
        self.assertEqual(new_obs, expected_obs)
        expected = dict(before)
        expected["observations"] = [expected_obs]
        self.assertEqual(after, expected)

    def test_s3star_projection_owns_the_same_false_claim_boundary(self) -> None:
        before_rows = git_json(PROJ_REL)
        after_rows = load(S3STAR / "canonical_observations.json")
        before = by_id(before_rows, OID)
        after = by_id(after_rows, OID)
        self.assertNotIn(KEY, before)
        self.assertIs(after[KEY], False)
        expected = dict(before)
        expected[KEY] = False
        self.assertEqual(after, expected)

    def test_effective_observation_is_lossless_across_the_move(self) -> None:
        old_record = git_json(RAW_REL)
        old_link = by_id(git_json(PROJ_REL), OID)
        new_record = load(RAW / "data-to-paper-review-revision.json")
        new_link = by_id(load(S3STAR / "canonical_observations.json"), OID)
        self.assertEqual(hydrate(new_link, new_record), hydrate(old_link, old_record))

    def test_neutral_guard_rejects_the_metric_key_recursively(self) -> None:
        path = RAW / "render_registry_core.py"
        spec = importlib.util.spec_from_file_location("neutral_registry_core_824", path)
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        with self.assertRaises(module.RegistryError):
            module._validate_vsm_neutral({"observations": [{KEY: False}]}, "synthetic.json")

    def test_no_raw_record_contains_the_metric_key(self) -> None:
        def walk(value) -> bool:
            if isinstance(value, dict):
                return KEY in value or any(walk(child) for child in value.values())
            if isinstance(value, list):
                return any(walk(child) for child in value)
            return False

        hits = [path.name for path in RAW.glob("*.json") if walk(load(path))]
        self.assertEqual(hits, [])

    def test_registry_counts_capability_counts_and_primary_are_unchanged(self) -> None:
        registry_before = git_text(
            "experiments/functional-capability-depth/system-observations/registry.psv"
        )
        registry_after = (RAW / "registry.psv").read_text(encoding="utf-8")
        self.assertEqual(registry_after, registry_before)
        self.assertEqual(len(registry_after.strip().splitlines()) - 1, 53)

        coverage = load(S3STAR / "coverage.json")
        self.assertEqual(coverage["direct_benchmark_family_count"], 5)
        self.assertEqual(coverage["composed_direct_observation_count"], 3)
        self.assertEqual(coverage["canonical_direct_observation_count"], 2)
        baselines = load(EXP / "primary-baselines.json")["functions"]
        self.assertEqual(baselines["S3*"]["status"], "gap")


if __name__ == "__main__":
    unittest.main()
