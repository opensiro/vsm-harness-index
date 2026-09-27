from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
RAW = EXP / "system-observations"
S3STAR = EXP / "s3star-system-benchmarks"
TESTS = ROOT / "tests"

OBSERVATION_ID = "data-to-paper-review-revision-2024"
BASE_REF = "fb1601845884ea16b1c0786e40b8976dae6e569b"

# 1) Preserve raw formatting exactly: remove only the function-specific boolean.
raw_path = RAW / "data-to-paper-review-revision.json"
raw_text = raw_path.read_text(encoding="utf-8")
raw_line = '      "aggregate_s3star_metric_reported": false,\n'
if raw_text.count(raw_line) != 1:
    raise SystemExit("data-to-paper raw metric-boundary line drift")
raw_path.write_text(raw_text.replace(raw_line, "", 1), encoding="utf-8")

# 2) Preserve the same claim boundary in the S3* derived canonical projection.
projection_path = S3STAR / "canonical_observations.json"
projection_text = projection_path.read_text(encoding="utf-8")
anchor = '    "canonical_harness_id": "data-to-paper",\n    "raw_observation_ref": "../system-observations/data-to-paper-review-revision.json#data-to-paper-review-revision-2024"\n'
replacement = '    "canonical_harness_id": "data-to-paper",\n    "aggregate_s3star_metric_reported": false,\n    "raw_observation_ref": "../system-observations/data-to-paper-review-revision.json#data-to-paper-review-revision-2024"\n'
if projection_text.count(anchor) != 1:
    raise SystemExit("data-to-paper S3* projection anchor drift")
projection_path.write_text(projection_text.replace(anchor, replacement, 1), encoding="utf-8")

# 3) Fail closed if the function-specific key ever returns to neutral raw evidence.
guard_path = RAW / "render_registry_core.py"
guard_text = guard_path.read_text(encoding="utf-8")
guard_anchor = '    "mixed_function_caveat",\n'
guard_replacement = '    "mixed_function_caveat",\n    "aggregate_s3star_metric_reported",\n'
if guard_text.count(guard_anchor) != 1:
    raise SystemExit("neutral guard anchor drift")
guard_path.write_text(guard_text.replace(guard_anchor, guard_replacement, 1), encoding="utf-8")

# 4) The S3* migration contract now explicitly permits this function-specific claim-boundary field.
migration_test = TESTS / "test_s3star_neutral_registry_migration_802.py"
test_text = migration_test.read_text(encoding="utf-8")
old_allowed = 'DERIVED_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","raw_observation_ref"}\n'
new_allowed = 'DERIVED_ALLOWED={"observation_id","function","benchmark_id","benchmark_fit","boundary_class","canonical_harness_id","canonical_system_eligible","vsm_interpretation","aggregate_s3star_metric_reported","raw_observation_ref"}\n'
if test_text.count(old_allowed) != 1:
    raise SystemExit("S3* DERIVED_ALLOWED anchor drift")
migration_test.write_text(test_text.replace(old_allowed, new_allowed, 1), encoding="utf-8")

# 5) Pinned regression: raw payload changes by exactly one removed key; effective S3* value stays false.
(TESTS / "test_s3star_metric_boundary_824.py").write_text(
    f'''from __future__ import annotations\n\nimport copy\nimport json\nimport subprocess\nimport unittest\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nEXP = ROOT / "experiments" / "functional-capability-depth"\nRAW_PATH = EXP / "system-observations" / "data-to-paper-review-revision.json"\nPROJECTION_PATH = EXP / "s3star-system-benchmarks" / "canonical_observations.json"\nBASE_REF = "{BASE_REF}"\nOBSERVATION_ID = "{OBSERVATION_ID}"\n\n\ndef load(path: Path):\n    return json.loads(path.read_text(encoding="utf-8"))\n\n\ndef historical_raw():\n    text = subprocess.check_output(\n        [\n            "git", "show",\n            f"{{BASE_REF}}:experiments/functional-capability-depth/system-observations/data-to-paper-review-revision.json",\n        ],\n        cwd=ROOT,\n        text=True,\n    )\n    return json.loads(text)\n\n\nclass S3StarMetricBoundary824Tests(unittest.TestCase):\n    def test_raw_payload_diff_is_exactly_one_removed_function_key(self):\n        before = historical_raw()\n        after = load(RAW_PATH)\n        before_without_boundary = copy.deepcopy(before)\n        observations = [\n            row for row in before_without_boundary["observations"]\n            if row.get("observation_id") == OBSERVATION_ID\n        ]\n        self.assertEqual(len(observations), 1)\n        self.assertIs(observations[0].pop("aggregate_s3star_metric_reported"), False)\n        self.assertEqual(after, before_without_boundary)\n\n    def test_function_specific_metric_absence_is_derived_only(self):\n        raw = load(RAW_PATH)\n        raw_observation = next(\n            row for row in raw["observations"]\n            if row["observation_id"] == OBSERVATION_ID\n        )\n        self.assertNotIn("aggregate_s3star_metric_reported", raw_observation)\n        self.assertIn("does not report an aggregate S3*-specific", raw_observation["metric_note"])\n\n        projections = load(PROJECTION_PATH)\n        derived = next(\n            row for row in projections\n            if row["observation_id"] == OBSERVATION_ID\n        )\n        self.assertIs(derived["aggregate_s3star_metric_reported"], False)\n        self.assertEqual(derived["function"], "S3*")\n        self.assertEqual(derived["benchmark_fit"], "direct")\n        self.assertTrue(derived["canonical_system_eligible"])\n\n        effective = dict(derived)\n        for key, value in raw_observation.items():\n            if key in {{"observation_id", "kind", "evidence_surface", "non_claim"}}:\n                continue\n            self.assertTrue(key not in effective or effective[key] == value, key)\n            effective[key] = value\n        self.assertIs(effective["aggregate_s3star_metric_reported"], False)\n        self.assertEqual(effective["comparison_class"], "descriptive-only")\n        self.assertEqual(effective["published_example_count"], 1)\n\n\nif __name__ == "__main__":\n    unittest.main()\n''',
    encoding="utf-8",
)

print("prepared #824 S3* metric-boundary cleanup")
