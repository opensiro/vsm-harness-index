from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "experiments" / "functional-capability-depth" / "s3star-system-benchmarks" / "validate.py"

text = TARGET.read_text(encoding="utf-8")
old = '''    metric_note = observation.get("metric_note")\n    if not isinstance(metric_note, str) or "does not report an aggregate S3*-specific" not in metric_note:\n        fail("data-to-paper no-score boundary must remain explicit")\n'''
new = '''    metric_note = observation.get("metric_note")\n    if not isinstance(metric_note, str) or "does not report an aggregate independent-review-specific" not in metric_note:\n        fail("data-to-paper no-score boundary must remain explicit")\n'''
if text.count(old) != 1:
    raise SystemExit("S3* data-to-paper neutral no-score consumer anchor drift")
TARGET.write_text(text.replace(old, new, 1), encoding="utf-8")
print("patched S3* validator to consume neutral independent-review prose")
