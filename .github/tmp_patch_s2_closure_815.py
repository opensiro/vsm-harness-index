from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "experiments/functional-capability-depth/s2-system-benchmarks/matched-cell/validate_s2_primary_search_closure.py"
text = PATH.read_text(encoding="utf-8")
old = '''    hydrated = dict(matches[0])\n    hydrated.update(row)\n    return hydrated\n'''
new = '''    hydrated = dict(matches[0])\n    record_level = {\n        "evidence_source_class": record.get("evidence_source_class"),\n        "system_compatibility": (record.get("published_implementation") or {}).get("system_compatibility"),\n        "primary_sources": record.get("primary_sources"),\n    }\n    for key, value in record_level.items():\n        require(value is not None, f"{row.get('observation_id')}: neutral raw record missing {key}")\n        require(key not in hydrated or hydrated[key] == value, f"{row.get('observation_id')}: neutral raw field conflict: {key}")\n        hydrated[key] = value\n    for key, value in row.items():\n        require(key not in hydrated or hydrated[key] == value, f"{row.get('observation_id')}: derived/raw field conflict: {key}")\n        hydrated[key] = value\n    return hydrated\n'''
if old not in text:
    raise SystemExit("S2 primary-search closure hydration anchor drift")
PATH.write_text(text.replace(old, new, 1), encoding="utf-8")
print("patched S2 primary-search closure to hydrate neutral record-level provenance")
