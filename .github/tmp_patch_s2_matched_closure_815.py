from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/matched-cell/validate_s2_matched_canonical_search.py"
text = PATH.read_text(encoding="utf-8")

anchor = '''HERE = Path(__file__).resolve().parent\nS2 = HERE.parent\nEXPERIMENT = S2.parent\n'''
replacement = anchor + 'SYSTEM_OBSERVATIONS = EXPERIMENT / "system-observations"\n'
if anchor not in text:
    raise SystemExit("matched closure path anchor drift")
text = text.replace(anchor, replacement, 1)

helper_anchor = '''def require(condition: bool, message: str) -> None:\n    if not condition:\n        raise SystemExit(message)\n\n\n'''
helper = helper_anchor + '''def hydrate_raw_observation(row: dict) -> dict:\n    ref = row.get("raw_observation_ref")\n    if ref is None:\n        return row\n    require(\n        isinstance(ref, str) and ref.startswith("../system-observations/") and "#" in ref,\n        f"{row.get('observation_id')}: invalid raw observation ref",\n    )\n    path_part, raw_id = ref.split("#", 1)\n    raw_path = (S2 / path_part).resolve()\n    require(\n        raw_path.parent == SYSTEM_OBSERVATIONS.resolve() and raw_path.is_file(),\n        f"{row.get('observation_id')}: raw observation missing",\n    )\n    record = load(raw_path)\n    matches = [\n        candidate\n        for candidate in record.get("observations", [])\n        if candidate.get("observation_id") == raw_id\n    ]\n    require(\n        len(matches) == 1 and raw_id == row.get("observation_id"),\n        f"{row.get('observation_id')}: raw observation identity drift",\n    )\n    hydrated = dict(matches[0])\n    record_level = {\n        "evidence_source_class": record.get("evidence_source_class"),\n        "system_compatibility": (record.get("published_implementation") or {}).get("system_compatibility"),\n        "primary_sources": record.get("primary_sources"),\n    }\n    for key, value in record_level.items():\n        require(value is not None, f"{row.get('observation_id')}: neutral raw record missing {key}")\n        require(\n            key not in hydrated or hydrated[key] == value,\n            f"{row.get('observation_id')}: neutral raw field conflict: {key}",\n        )\n        hydrated[key] = value\n    for key, value in row.items():\n        require(\n            key not in hydrated or hydrated[key] == value,\n            f"{row.get('observation_id')}: derived/raw field conflict: {key}",\n        )\n        hydrated[key] = value\n    return hydrated\n\n\n'''
if helper_anchor not in text:
    raise SystemExit("matched closure helper anchor drift")
text = text.replace(helper_anchor, helper, 1)

load_anchor = '''observations = load(S2 / "observations.json")\n'''
load_replacement = '''observations = [hydrate_raw_observation(row) for row in load(S2 / "observations.json")]\n'''
if load_anchor not in text:
    raise SystemExit("matched closure observation load anchor drift")
text = text.replace(load_anchor, load_replacement, 1)

PATH.write_text(text, encoding="utf-8")
print("patched S2 matched-canonical closure to hydrate neutral record-level provenance")
