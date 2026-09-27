from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "experiments/functional-capability-depth/s3-system-benchmarks/validate.py"
text = PATH.read_text(encoding="utf-8")
old = '''    validate_mao_observation(by_observation_id[MAO_OBSERVATION_ID])\n'''
new = '''    validate_mao_observation(hydrate_s3_projection(by_observation_id[MAO_OBSERVATION_ID]))\n'''
if old not in text:
    raise SystemExit("S3 MAO validation call anchor drift")
PATH.write_text(text.replace(old, new, 1), encoding="utf-8")
print("patched MAO direct S3 validation to hydrate neutral raw evidence")
