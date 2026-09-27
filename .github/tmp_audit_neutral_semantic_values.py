from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments" / "functional-capability-depth" / "system-observations"

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


def field_name(json_path: str) -> str:
    return json_path.rsplit(".", 1)[-1]


hits = []
for path in sorted(RAW.glob("*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    for json_path, value in walk(data):
        matched = sorted({m.group(0) for pattern in PATTERNS for m in pattern.finditer(value)})
        if matched:
            hits.append({
                "record": path.name,
                "path": json_path,
                "field": field_name(json_path),
                "tokens": matched,
                "value": value,
            })

by_field = Counter(hit["field"] for hit in hits)
by_record = Counter(hit["record"] for hit in hits)
records_by_field = defaultdict(set)
for hit in hits:
    records_by_field[hit["field"]].add(hit["record"])

summary = {
    "hit_count": len(hits),
    "record_count": len(by_record),
    "by_field": [
        {
            "field": field,
            "hits": count,
            "record_count": len(records_by_field[field]),
            "records": sorted(records_by_field[field]),
        }
        for field, count in by_field.most_common()
    ],
    "by_record": [
        {"record": record, "hits": count}
        for record, count in by_record.most_common()
    ],
}

print("=== SUMMARY ===")
print(json.dumps(summary, indent=2, ensure_ascii=False))
print("=== HITS ===")
print(json.dumps(hits, indent=2, ensure_ascii=False))
