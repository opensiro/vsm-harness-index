#!/usr/bin/env python3
from pathlib import Path

path = Path("experiments/functional-capability-depth/s3-system-benchmarks/matched-cell/validate_s3_primary_search_closure.py")
text = path.read_text(encoding="utf-8")
needle = 'closure = load(HERE / "s3-primary-search-closure.json")\n'
helper = '''RAW_OBSERVATIONS = EXPERIMENT / "system-observations"\nRAW_PREFIX = "../system-observations/"\n\n\ndef hydrate_projection(link: dict) -> dict:\n    oid = link.get("observation_id")\n    ref = link.get("raw_observation_ref")\n    require(isinstance(oid, str) and oid, "S3 closure projection requires observation_id")\n    require(isinstance(ref, str) and ref.startswith(RAW_PREFIX) and "#" in ref, f"{oid}: invalid raw_observation_ref")\n    rel, ref_oid = ref[len(RAW_PREFIX):].rsplit("#", 1)\n    require(ref_oid == oid and rel.endswith(".json") and "/" not in rel, f"{oid}: raw_observation_ref drift")\n    raw_path = RAW_OBSERVATIONS / rel\n    require(raw_path.is_file(), f"{oid}: neutral raw record missing: {rel}")\n    record = load(raw_path)\n    matches = [row for row in record.get("observations", []) if row.get("observation_id") == oid]\n    require(len(matches) == 1, f"{oid}: expected exactly one neutral raw observation in {rel}")\n    effective = dict(link)\n    for key, value in matches[0].items():\n        if key in {"observation_id", "kind", "evidence_surface", "benchmark"}:\n            continue\n        require(key not in effective or effective[key] == value, f"{oid}: derived/raw field conflict: {key}")\n        effective[key] = value\n    effective["evidence_source_class"] = record.get("evidence_source_class")\n    effective["system_compatibility"] = (record.get("published_implementation") or {}).get("system_compatibility")\n    effective["primary_sources"] = record.get("primary_sources")\n    if record.get("canonical_harness_id"):\n        effective["canonical_review_revision"] = record.get("canonical_review_ref")\n    return effective\n\n\n'''
assert needle in text and "def hydrate_projection(" not in text
text = text.replace(needle, helper + needle)
old = 'smas = observation_by_id[SMAS_OBSERVATION_ID]\n'
new = 'smas = hydrate_projection(observation_by_id[SMAS_OBSERVATION_ID])\n'
assert old in text
text = text.replace(old, new)
path.write_text(text, encoding="utf-8")
print("patched S3 primary-search closure to hydrate neutral SMAS evidence")
