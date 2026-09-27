from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXP = ROOT / "experiments/functional-capability-depth"
RAW_DIR = EXP / "system-observations"
S2_PATH = EXP / "s2-system-benchmarks/observations.json"
S2_VALIDATE = EXP / "s2-system-benchmarks/validate.py"
S3_PATH = EXP / "s3-system-benchmarks/observations.json"
REGISTRY_CORE = RAW_DIR / "render_registry_core.py"
TEST = ROOT / "tests/test_direct_projection_neutral_ownership_815.py"
BASE_REF = "3a879693db8ac71290d5285b4763bb2ce13ece98"

RAW_STATE_LEAK_FILES = {
    "llamar.json",
    "magentic-one.json",
    "squad-operational-history.json",
    "squad.json",
    "thclaws-operational-history.json",
}
S2_NEUTRAL_OWNED_KEYS = {
    "evidence_source_class",
    "system_compatibility",
    "primary_sources",
    "benchmark_artifact_revision",
    "comparison_class",
}
MAO_ID = "multi-agent-orchestration-supervisor-ablation-2026-08"
MAO_DERIVED_KEYS = {
    "observation_id",
    "function",
    "benchmark_id",
    "benchmark_fit",
    "boundary_class",
    "canonical_harness_id",
    "canonical_system_eligible",
    "vsm_interpretation",
    "raw_observation_ref",
}

# 1) Remove the five legacy VSM-state leaks from the neutral raw layer.
for filename in sorted(RAW_STATE_LEAK_FILES):
    path = RAW_DIR / filename
    record = json.loads(path.read_text(encoding="utf-8"))
    leaked = record.pop("canonical_states_at_review", None)
    if leaked is None:
        raise SystemExit(f"expected legacy canonical_states_at_review in {filename}")
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 2) Reduce direct S2 rows to interpretation/linkage ownership for fields already neutral-owned.
s2_rows = json.loads(S2_PATH.read_text(encoding="utf-8"))
if len(s2_rows) != 6:
    raise SystemExit(f"expected 6 direct S2 rows, got {len(s2_rows)}")
for row in s2_rows:
    if not row.get("raw_observation_ref"):
        raise SystemExit(f"S2 row lacks neutral raw link: {row.get('observation_id')}")
    for key in S2_NEUTRAL_OWNED_KEYS:
        row.pop(key, None)
S2_PATH.write_text(json.dumps(s2_rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 3) Teach S2 hydration to recover record-level neutral provenance and fail on conflicts.
s2_text = S2_VALIDATE.read_text(encoding="utf-8")
old_hydration = '''    hydrated = dict(raw)\n    hydrated.update(row)\n    return hydrated\n'''
new_hydration = '''    hydrated = dict(raw)\n    record_level = {\n        "evidence_source_class": record.get("evidence_source_class"),\n        "system_compatibility": (record.get("published_implementation") or {}).get("system_compatibility"),\n        "primary_sources": record.get("primary_sources"),\n    }\n    for key, value in record_level.items():\n        if value is None:\n            fail(f"{row.get('observation_id')}: neutral raw record missing {key}")\n        if key in hydrated and hydrated[key] != value:\n            fail(f"{row.get('observation_id')}: neutral raw field conflict: {key}")\n        hydrated[key] = value\n    for key, value in row.items():\n        if key in hydrated and hydrated[key] != value:\n            fail(f"{row.get('observation_id')}: derived/raw field conflict: {key}")\n        hydrated[key] = value\n    return hydrated\n'''
if old_hydration not in s2_text:
    raise SystemExit("S2 hydrate_raw_observation anchor drift")
S2_VALIDATE.write_text(s2_text.replace(old_hydration, new_hydration, 1), encoding="utf-8")

# 4) Reduce the legacy Multi-Agent Orchestration S3 row to the same derived-only pattern as newer rows.
s3_rows = json.loads(S3_PATH.read_text(encoding="utf-8"))
matches = [row for row in s3_rows if row.get("observation_id") == MAO_ID]
if len(matches) != 1:
    raise SystemExit("expected exactly one Multi-Agent Orchestration S3 row")
mao = matches[0]
missing = MAO_DERIVED_KEYS - set(mao)
if missing:
    raise SystemExit(f"MAO row missing derived keys before cleanup: {sorted(missing)}")
clean_mao = {key: mao[key] for key in mao if key in MAO_DERIVED_KEYS}
s3_rows = [clean_mao if row.get("observation_id") == MAO_ID else row for row in s3_rows]
S3_PATH.write_text(json.dumps(s3_rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# 5) Make VSM neutrality of raw system-observations a fail-closed registry invariant.
core = REGISTRY_CORE.read_text(encoding="utf-8")
class_anchor = '''class RegistryError(ValueError):\n    pass\n\n\n'''
neutral_guard = '''class RegistryError(ValueError):\n    pass\n\n\nFORBIDDEN_VSM_KEYS = {\n    "function",\n    "benchmark_fit",\n    "vsm_interpretation",\n    "canonical_state_at_review",\n    "canonical_states_at_review",\n    "canonical_system_eligible",\n    "coverage_class",\n}\n\n\ndef _forbidden_vsm_key(key: str) -> bool:\n    return (\n        key in FORBIDDEN_VSM_KEYS\n        or key.startswith("autonomy_s")\n        or key.startswith("vsm_")\n        or re.match(r"^canonical_.*state", key) is not None\n    )\n\n\ndef _validate_vsm_neutral(value: object, record_ref: str, path: str = "$") -> None:\n    if isinstance(value, dict):\n        for key, child in value.items():\n            child_path = f"{path}.{key}"\n            if _forbidden_vsm_key(key):\n                raise RegistryError(\n                    f"{record_ref}:{child_path}: raw neutral evidence must not encode VSM-function/state attribution"\n                )\n            _validate_vsm_neutral(child, record_ref, child_path)\n    elif isinstance(value, list):\n        for idx, child in enumerate(value):\n            _validate_vsm_neutral(child, record_ref, f"{path}[{idx}]")\n\n\n'''
if class_anchor not in core:
    raise SystemExit("render_registry_core RegistryError anchor drift")
core = core.replace(class_anchor, neutral_guard, 1)
record_anchor = '''        if not isinstance(record, dict):\n            raise RegistryError(f"{record_ref}: raw record must be a JSON object")\n'''
record_replacement = record_anchor + '''        _validate_vsm_neutral(record, record_ref)\n'''
if record_anchor not in core:
    raise SystemExit("render_registry_core record validation anchor drift")
core = core.replace(record_anchor, record_replacement, 1)
REGISTRY_CORE.write_text(core, encoding="utf-8")

# 6) Regression: reconstruct old effective rows exactly, plus assert raw neutrality and derived-only ownership.
TEST.write_text(
    '''from __future__ import annotations\n\nimport json\nimport re\nimport subprocess\nimport unittest\nfrom pathlib import Path\n\nROOT = Path(__file__).resolve().parents[1]\nEXP = ROOT / "experiments/functional-capability-depth"\nRAW_DIR = EXP / "system-observations"\nBASE_REF = "3a879693db8ac71290d5285b4763bb2ce13ece98"\nS2_REL = "experiments/functional-capability-depth/s2-system-benchmarks/observations.json"\nS3_REL = "experiments/functional-capability-depth/s3-system-benchmarks/observations.json"\nMAO_ID = "multi-agent-orchestration-supervisor-ablation-2026-08"\nNEUTRAL_OWNED = {\n    "evidence_source_class", "system_compatibility", "primary_sources",\n    "benchmark_artifact_revision", "comparison_class",\n}\nFORBIDDEN_EXACT = {\n    "function", "benchmark_fit", "vsm_interpretation",\n    "canonical_state_at_review", "canonical_states_at_review",\n    "canonical_system_eligible", "coverage_class",\n}\n\n\ndef old_json(path: str):\n    text = subprocess.check_output(["git", "show", f"{BASE_REF}:{path}"], cwd=ROOT, text=True)\n    return json.loads(text)\n\n\ndef resolve(link: dict):\n    ref = link["raw_observation_ref"]\n    prefix = "../system-observations/"\n    assert ref.startswith(prefix) and "#" in ref\n    rel, oid = ref[len(prefix):].rsplit("#", 1)\n    record = json.loads((RAW_DIR / rel).read_text(encoding="utf-8"))\n    matches = [row for row in record["observations"] if row["observation_id"] == oid]\n    assert len(matches) == 1\n    return record, matches[0]\n\n\ndef hydrate_s2(row: dict, *, inject_record_level: bool) -> dict:\n    record, raw = resolve(row)\n    effective = dict(raw)\n    if inject_record_level:\n        effective["evidence_source_class"] = record["evidence_source_class"]\n        effective["system_compatibility"] = record["published_implementation"]["system_compatibility"]\n        effective["primary_sources"] = record["primary_sources"]\n    effective.update(row)\n    return effective\n\n\ndef hydrate_s3(row: dict) -> dict:\n    record, raw = resolve(row)\n    effective = dict(row)\n    for key, value in raw.items():\n        if key in {"observation_id", "kind", "evidence_surface", "benchmark"}:\n            continue\n        effective[key] = value\n    effective["evidence_source_class"] = record["evidence_source_class"]\n    effective["system_compatibility"] = record["published_implementation"]["system_compatibility"]\n    effective["primary_sources"] = record["primary_sources"]\n    if record.get("canonical_harness_id"):\n        effective["canonical_review_revision"] = record.get("canonical_review_ref")\n    return effective\n\n\ndef forbidden_key(key: str) -> bool:\n    return (\n        key in FORBIDDEN_EXACT\n        or key.startswith("autonomy_s")\n        or key.startswith("vsm_")\n        or re.match(r"^canonical_.*state", key) is not None\n    )\n\n\ndef walk(value):\n    if isinstance(value, dict):\n        for key, child in value.items():\n            yield key\n            yield from walk(child)\n    elif isinstance(value, list):\n        for child in value:\n            yield from walk(child)\n\n\nclass DirectProjectionNeutralOwnership815Tests(unittest.TestCase):\n    def test_s2_effective_rows_are_lossless(self):\n        old_rows = old_json(S2_REL)\n        new_rows = json.loads((ROOT / S2_REL).read_text(encoding="utf-8"))\n        self.assertEqual([r["observation_id"] for r in old_rows], [r["observation_id"] for r in new_rows])\n        old_by_id = {r["observation_id"]: r for r in old_rows}\n        for row in new_rows:\n            before = hydrate_s2(old_by_id[row["observation_id"]], inject_record_level=False)\n            after = hydrate_s2(row, inject_record_level=True)\n            self.assertEqual(after, before, row["observation_id"])\n            self.assertFalse(NEUTRAL_OWNED & set(row), row["observation_id"])\n\n    def test_mao_s3_effective_row_is_lossless_and_minimal(self):\n        old_rows = old_json(S3_REL)\n        new_rows = json.loads((ROOT / S3_REL).read_text(encoding="utf-8"))\n        old = next(r for r in old_rows if r["observation_id"] == MAO_ID)\n        new = next(r for r in new_rows if r["observation_id"] == MAO_ID)\n        self.assertEqual(hydrate_s3(new), hydrate_s3(old))\n        self.assertEqual(\n            set(new),\n            {\n                "observation_id", "function", "benchmark_id", "benchmark_fit",\n                "boundary_class", "canonical_harness_id", "canonical_system_eligible",\n                "vsm_interpretation", "raw_observation_ref",\n            },\n        )\n\n    def test_raw_registry_contains_no_vsm_state_or_function_attribution(self):\n        files = sorted(RAW_DIR.glob("*.json"))\n        self.assertTrue(files)\n        hits = []\n        for path in files:\n            data = json.loads(path.read_text(encoding="utf-8"))\n            for key in walk(data):\n                if forbidden_key(key):\n                    hits.append((path.name, key))\n        self.assertEqual(hits, [])\n\n\nif __name__ == "__main__":\n    unittest.main()\n''',
    encoding="utf-8",
)

print("prepared #815 direct-projection ownership cleanup and neutral VSM-state guard")
