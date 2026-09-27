from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"

# Explicit VSM/function-attribution vocabulary should not live in neutral raw evidence
# values. Report it for manual classification rather than mutating anything.
PATTERNS = [
    re.compile(r"(?<![A-Za-z0-9])S1(?![A-Za-z0-9])", re.I),
    re.compile(r"(?<![A-Za-z0-9])S2(?![A-Za-z0-9])", re.I),
    re.compile(r"(?<![A-Za-z0-9])S3\*(?![A-Za-z0-9])", re.I),
    re.compile(r"(?<![A-Za-z0-9])S3(?![A-Za-z0-9])", re.I),
    re.compile(r"(?<![A-Za-z0-9])S4(?![A-Za-z0-9])", re.I),
    re.compile(r"(?<![A-Za-z0-9])S5(?![A-Za-z0-9])", re.I),
    re.compile(r"\bVSM\b", re.I),
    re.compile(r"\bviable system model\b", re.I),
]


def walk(value, path="$"):
    if isinstance(value, dict):
        for key, child in value.items():
            yield from walk(child, f"{path}.{key}")
    elif isinstance(value, list):
        for idx, child in enumerate(value):
            yield from walk(child, f"{path}[{idx}]")
    elif isinstance(value, str):
        yield path, value


hits = []
for path in sorted(RAW.glob("*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    for json_path, value in walk(data):
        matched = sorted({m.group(0) for pattern in PATTERNS for m in pattern.finditer(value)})
        if matched:
            hits.append({
                "record": path.name,
                "path": json_path,
                "tokens": matched,
                "value": value,
            })

print(json.dumps(hits, indent=2, ensure_ascii=False))
print(f"semantic-value-hit-count={len(hits)}")
