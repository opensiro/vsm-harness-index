from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "experiments/functional-capability-depth/s3-system-benchmarks/matched-cell/validate_s3_matched_canonical_search.py"
text = PATH.read_text(encoding="utf-8")

hydrate_old = '''    if record.get("canonical_harness_id"):\n        effective["canonical_review_revision"] = record.get("canonical_review_ref")\n    return effective\n'''
hydrate_new = '''    if record.get("canonical_harness_id"):\n        effective["canonical_review_revision"] = record.get("canonical_review_ref")\n    raw = matches[0]\n    if "comparison_class" not in effective and isinstance(raw.get("comparison_design"), str):\n        effective["comparison_class"] = raw["comparison_design"]\n    return effective\n'''
if hydrate_old not in text:
    raise SystemExit("S3 matched closure hydration anchor drift")
text = text.replace(hydrate_old, hydrate_new, 1)

mao_old = '''mao_obs = observation_rows[mao_id]\n'''
mao_new = '''mao_obs = hydrate_projection(observation_rows[mao_id])\n'''
if mao_old not in text:
    raise SystemExit("S3 matched closure MAO lookup anchor drift")
text = text.replace(mao_old, mao_new, 1)

PATH.write_text(text, encoding="utf-8")
print("patched S3 matched-canonical closure to hydrate MAO neutral evidence")
