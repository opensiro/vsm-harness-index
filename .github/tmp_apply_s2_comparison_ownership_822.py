from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S2 = EXP / "s2-system-benchmarks"
RAW = EXP / "system-observations"
TESTS = ROOT / "tests"

TARGETS = {
    "squad-shared-state-conflict-attenuation-2026-03": "squad-operational-history.json",
    "thclaws-team-workspace-interference-attenuation-2026": "thclaws-operational-history.json",
}

# 1) Remove the two exact raw-owned comparison metadata duplicates.
obs_path = S2 / "observations.json"
rows = json.loads(obs_path.read_text(encoding="utf-8"))
by_id = {row["observation_id"]: row for row in rows}
if set(TARGETS) - set(by_id):
    raise SystemExit(f"missing S2 target rows: {sorted(set(TARGETS) - set(by_id))}")
for observation_id, raw_filename in TARGETS.items():
    row = by_id[observation_id]
    local = row.get("comparison_limitation")
    if not isinstance(local, str) or not local:
        raise SystemExit(f"{observation_id}: expected local comparison_limitation before cleanup")
    record = json.loads((RAW / raw_filename).read_text(encoding="utf-8"))
    matches = [item for item in record.get("observations", []) if item.get("observation_id") == observation_id]
    if len(matches) != 1:
        raise SystemExit(f"{observation_id}: expected one neutral raw observation")
    raw_value = matches[0].get("comparison_limitation")
    if local != raw_value:
        raise SystemExit(f"{observation_id}: local/raw comparison_limitation mismatch")
    del row["comparison_limitation"]
obs_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2) Make the S2 hydrator reject reintroduced raw-owned comparison metadata.
validate_path = S2 / "validate.py"
text = validate_path.read_text(encoding="utf-8")
constant_anchor = '''EXPECTED_CANONICAL_OBSERVATION_IDS = {\n    "squad-shared-state-conflict-attenuation-2026-03",\n    "thclaws-team-workspace-interference-attenuation-2026",\n}\n'''
constant_replacement = constant_anchor + '''RAW_OWNED_DIRECT_KEYS = {\n    "comparison_limitation",\n}\n'''
if text.count(constant_anchor) != 1:
    raise SystemExit("S2 RAW_OWNED_DIRECT_KEYS constant anchor drift")
text = text.replace(constant_anchor, constant_replacement, 1)

raw_anchor = '''    raw = matches[0]\n    for forbidden in ("function", "benchmark_fit", "vsm_interpretation"):\n'''
raw_replacement = '''    raw = matches[0]\n    for key in RAW_OWNED_DIRECT_KEYS:\n        if key in raw and key in row:\n            fail(f"{row.get('observation_id')}: derived row duplicates neutral-owned {key}")\n    for forbidden in ("function", "benchmark_fit", "vsm_interpretation"):\n'''
if text.count(raw_anchor) != 1:
    raise SystemExit("S2 raw-owned duplicate guard anchor drift")
validate_path.write_text(text.replace(raw_anchor, raw_replacement, 1), encoding="utf-8")

# 3) Extend the prior ownership regression to treat comparison_limitation as neutral-owned.
old_test = TESTS / "test_direct_projection_neutral_ownership_815.py"
test_text = old_test.read_text(encoding="utf-8")
old_set = '''NEUTRAL_OWNED = {\n    "evidence_source_class", "system_compatibility", "primary_sources",\n    "benchmark_artifact_revision", "comparison_class",\n}\n'''
new_set = '''NEUTRAL_OWNED = {\n    "evidence_source_class", "system_compatibility", "primary_sources",\n    "benchmark_artifact_revision", "comparison_class", "comparison_limitation",\n}\n'''
if test_text.count(old_set) != 1:
    raise SystemExit("#815 NEUTRAL_OWNED anchor drift")
old_test.write_text(test_text.replace(old_set, new_set, 1), encoding="utf-8")

# 4) Focused regression: physical rows are minimal and hydration is evidence-lossless.
(TESTS / "test_s2_comparison_ownership_822.py").write_text(
    '''from __future__ import annotations\n\nimport json\nimport unittest\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nEXP = ROOT / "experiments" / "functional-capability-depth"\nS2 = EXP / "s2-system-benchmarks"\nRAW = EXP / "system-observations"\nTARGETS = {\n    "squad-shared-state-conflict-attenuation-2026-03": "squad-operational-history.json",\n    "thclaws-team-workspace-interference-attenuation-2026": "thclaws-operational-history.json",\n}\n\n\ndef load(path: Path):\n    return json.loads(path.read_text(encoding="utf-8"))\n\n\nclass S2ComparisonOwnership822Tests(unittest.TestCase):\n    def test_comparison_limitation_has_one_neutral_owner(self):\n        rows = {row["observation_id"]: row for row in load(S2 / "observations.json")}\n        for observation_id, raw_filename in TARGETS.items():\n            derived = rows[observation_id]\n            self.assertNotIn("comparison_limitation", derived, observation_id)\n            raw_record = load(RAW / raw_filename)\n            raw_rows = [row for row in raw_record["observations"] if row["observation_id"] == observation_id]\n            self.assertEqual(len(raw_rows), 1)\n            value = raw_rows[0].get("comparison_limitation")\n            self.assertIsInstance(value, str)\n            self.assertTrue(value)\n\n    def test_function_specific_s2_interpretation_remains_local(self):\n        rows = {row["observation_id"]: row for row in load(S2 / "observations.json")}\n        for observation_id in TARGETS:\n            row = rows[observation_id]\n            for key in (\n                "disturbance",\n                "coordination_relation",\n                "subsequent_operation",\n                "vsm_interpretation",\n                "raw_observation_ref",\n            ):\n                self.assertIn(key, row, f"{observation_id}: {key}")\n            self.assertTrue(row["canonical_system_eligible"])\n            self.assertEqual(row["canonical_state_at_review"], "A")\n\n    def test_raw_comparison_limitation_reconstructs_effective_row(self):\n        rows = {row["observation_id"]: row for row in load(S2 / "observations.json")}\n        for observation_id, raw_filename in TARGETS.items():\n            raw_record = load(RAW / raw_filename)\n            raw = next(row for row in raw_record["observations"] if row["observation_id"] == observation_id)\n            effective = dict(raw)\n            effective.update(rows[observation_id])\n            self.assertEqual(effective["comparison_limitation"], raw["comparison_limitation"])\n\n\nif __name__ == "__main__":\n    unittest.main()\n''',
    encoding="utf-8",
)

print("prepared #822 S2 comparison metadata ownership cleanup")
