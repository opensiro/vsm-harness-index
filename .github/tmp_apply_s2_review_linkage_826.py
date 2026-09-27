from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments" / "functional-capability-depth"
S2 = EXP / "s2-system-benchmarks"
RAW = EXP / "system-observations"
TESTS = ROOT / "tests"

TARGETS = {
    "squad-shared-state-conflict-attenuation-2026-03": (
        "squad-operational-history.json",
        "squad",
        "assessments/squad.md",
        "2099faf51c08a912c359209447011b06decf0565",
    ),
    "thclaws-team-workspace-interference-attenuation-2026": (
        "thclaws-operational-history.json",
        "thclaws",
        "assessments/thclaws.md",
        "cd700937a71a391f052438d139b7b1c5a6456755",
    ),
}

# 1) Physical direct S2 projections stop using canonical_assessment_ref for a SHA.
obs_path = S2 / "observations.json"
rows = json.loads(obs_path.read_text(encoding="utf-8"))
by_id = {row["observation_id"]: row for row in rows}
for observation_id, (raw_filename, harness_id, assessment_path, review_ref) in TARGETS.items():
    row = by_id[observation_id]
    if row.get("canonical_harness_id") != harness_id:
        raise SystemExit(f"{observation_id}: canonical_harness_id drift")
    if row.get("canonical_assessment_ref") != review_ref:
        raise SystemExit(f"{observation_id}: legacy canonical_assessment_ref SHA drift")
    record = json.loads((RAW / raw_filename).read_text(encoding="utf-8"))
    if record.get("canonical_assessment_ref") != assessment_path:
        raise SystemExit(f"{observation_id}: neutral assessment path drift")
    if record.get("canonical_review_ref") != review_ref:
        raise SystemExit(f"{observation_id}: neutral canonical_review_ref drift")
    del row["canonical_assessment_ref"]
obs_path.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Shared patch helper: hydrate canonical review SHA from record-level neutral ownership.
def add_review_hydration(text: str, *, label: str, require_name: str) -> str:
    anchor = '''    for key, value in record_level.items():\n'''
    start = text.find(anchor)
    if start < 0:
        raise SystemExit(f"{label}: record_level loop anchor missing")
    row_loop = '''    for key, value in row.items():\n'''
    insert_at = text.find(row_loop, start)
    if insert_at < 0:
        raise SystemExit(f"{label}: derived row loop anchor missing")
    block = f'''    raw_harness = record.get("canonical_harness_id")\n    if raw_harness is not None:\n        canonical_review_ref = record.get("canonical_review_ref")\n        if not isinstance(canonical_review_ref, str) or not canonical_review_ref:\n            {require_name}(f"{{row.get('observation_id')}}: canonical neutral raw record missing canonical_review_ref")\n        if "canonical_review_ref" in hydrated and hydrated["canonical_review_ref"] != canonical_review_ref:\n            {require_name}(f"{{row.get('observation_id')}}: canonical_review_ref raw field conflict")\n        hydrated["canonical_review_ref"] = canonical_review_ref\n'''
    if "canonical neutral raw record missing canonical_review_ref" in text:
        raise SystemExit(f"{label}: canonical review hydration already present")
    return text[:insert_at] + block + text[insert_at:]

# 2) Core S2 validator hydrates canonical_review_ref and validates under the correct name.
validate_path = S2 / "validate.py"
text = validate_path.read_text(encoding="utf-8")
text = add_review_hydration(text, label="S2 validate", require_name="fail")
if text.count('"canonical_assessment_ref": "2099faf51c08a912c359209447011b06decf0565"') != 1:
    raise SystemExit("S2 Squad expected field anchor drift")
if text.count('"canonical_assessment_ref": "cd700937a71a391f052438d139b7b1c5a6456755"') != 1:
    raise SystemExit("S2 thClaws expected field anchor drift")
text = text.replace('"canonical_assessment_ref": "2099faf51c08a912c359209447011b06decf0565"', '"canonical_review_ref": "2099faf51c08a912c359209447011b06decf0565"', 1)
text = text.replace('"canonical_assessment_ref": "cd700937a71a391f052438d139b7b1c5a6456755"', '"canonical_review_ref": "cd700937a71a391f052438d139b7b1c5a6456755"', 1)
if text.count('expected["canonical_assessment_ref"]') != 2:
    raise SystemExit("S2 canonical assessment anchor consumer count drift")
text = text.replace('expected["canonical_assessment_ref"]', 'expected["canonical_review_ref"]')
validate_path.write_text(text, encoding="utf-8")

# 3) Primary-search closure hydrates the same neutral review SHA.
primary_path = S2 / "matched-cell" / "validate_s2_primary_search_closure.py"
text = primary_path.read_text(encoding="utf-8")
text = add_review_hydration(text, label="S2 primary closure", require_name="require")
old = '    require(observation.get("canonical_assessment_ref") == review_ref, f"{observation_id}: canonical ref drift")\n'
new = '    require(observation.get("canonical_review_ref") == review_ref, f"{observation_id}: canonical review ref drift")\n'
if text.count(old) != 1:
    raise SystemExit("S2 primary closure canonical observation ref anchor drift")
primary_path.write_text(text.replace(old, new, 1), encoding="utf-8")

# 4) Matched-canonical closure keeps its frozen historical anchor key, but current observation uses canonical_review_ref.
matched_path = S2 / "matched-cell" / "validate_s2_matched_canonical_search.py"
text = matched_path.read_text(encoding="utf-8")
text = add_review_hydration(text, label="S2 matched closure", require_name="require")
old = '    require(observation.get("canonical_assessment_ref") == review_ref, f"{harness_id}: canonical observation ref drift")\n'
new = '    require(observation.get("canonical_review_ref") == review_ref, f"{harness_id}: canonical observation review ref drift")\n'
if text.count(old) != 1:
    raise SystemExit("S2 matched closure current observation ref anchor drift")
matched_path.write_text(text.replace(old, new, 1), encoding="utf-8")

# 5) Adapt the #815 lossless regression to normalize the legacy pre-migration key name.
legacy_test = TESTS / "test_direct_projection_neutral_ownership_815.py"
text = legacy_test.read_text(encoding="utf-8")
old = '''    if inject_record_level:\n        effective["evidence_source_class"] = record["evidence_source_class"]\n        effective["system_compatibility"] = record["published_implementation"]["system_compatibility"]\n        effective["primary_sources"] = record["primary_sources"]\n    effective.update(row)\n'''
new = '''    if inject_record_level:\n        effective["evidence_source_class"] = record["evidence_source_class"]\n        effective["system_compatibility"] = record["published_implementation"]["system_compatibility"]\n        effective["primary_sources"] = record["primary_sources"]\n        if record.get("canonical_harness_id"):\n            effective["canonical_review_ref"] = record["canonical_review_ref"]\n    effective.update(row)\n'''
if text.count(old) != 1:
    raise SystemExit("#815 hydrate_s2 anchor drift")
text = text.replace(old, new, 1)
old = '''            before = hydrate_s2(old_by_id[row["observation_id"]], inject_record_level=False)\n            after = hydrate_s2(row, inject_record_level=True)\n            self.assertEqual(after, before, row["observation_id"])\n'''
new = '''            before = hydrate_s2(old_by_id[row["observation_id"]], inject_record_level=False)\n            if before.get("canonical_harness_id"):\n                before["canonical_review_ref"] = before.pop("canonical_assessment_ref")\n            after = hydrate_s2(row, inject_record_level=True)\n            self.assertEqual(after, before, row["observation_id"])\n'''
if text.count(old) != 1:
    raise SystemExit("#815 S2 legacy normalization anchor drift")
legacy_test.write_text(text.replace(old, new, 1), encoding="utf-8")

# 6) Focused regression for the path-vs-review-ref distinction.
(TESTS / "test_s2_canonical_review_linkage_826.py").write_text(
    '''from __future__ import annotations\n\nimport json\nimport unittest\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nEXP = ROOT / "experiments" / "functional-capability-depth"\nS2 = EXP / "s2-system-benchmarks"\nRAW = EXP / "system-observations"\nTARGETS = {\n    "squad-shared-state-conflict-attenuation-2026-03": (\n        "squad-operational-history.json", "assessments/squad.md",\n        "2099faf51c08a912c359209447011b06decf0565",\n    ),\n    "thclaws-team-workspace-interference-attenuation-2026": (\n        "thclaws-operational-history.json", "assessments/thclaws.md",\n        "cd700937a71a391f052438d139b7b1c5a6456755",\n    ),\n}\n\n\ndef load(path: Path):\n    return json.loads(path.read_text(encoding="utf-8"))\n\n\nclass S2CanonicalReviewLinkage826Tests(unittest.TestCase):\n    def test_raw_path_and_review_revision_have_distinct_schema_fields(self):\n        rows = {row["observation_id"]: row for row in load(S2 / "observations.json")}\n        for observation_id, (filename, assessment_path, review_ref) in TARGETS.items():\n            derived = rows[observation_id]\n            self.assertNotIn("canonical_assessment_ref", derived, observation_id)\n            self.assertNotIn("canonical_review_ref", derived, observation_id)\n\n            record = load(RAW / filename)\n            self.assertEqual(record["canonical_assessment_ref"], assessment_path)\n            self.assertEqual(record["canonical_review_ref"], review_ref)\n            self.assertNotEqual(record["canonical_assessment_ref"], record["canonical_review_ref"])\n\n            raw = next(\n                row for row in record["observations"]\n                if row["observation_id"] == observation_id\n            )\n            effective = dict(raw)\n            effective["canonical_review_ref"] = record["canonical_review_ref"]\n            effective.update(derived)\n            self.assertEqual(effective["canonical_review_ref"], review_ref)\n            self.assertNotIn("canonical_assessment_ref", effective)\n\n\nif __name__ == "__main__":\n    unittest.main()\n''',
    encoding="utf-8",
)

print("prepared #826 direct S2 canonical review linkage normalization")
