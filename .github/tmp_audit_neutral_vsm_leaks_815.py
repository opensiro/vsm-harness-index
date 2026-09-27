from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "experiments/functional-capability-depth/system-observations"

FORBIDDEN_EXACT = {
    "function",
    "benchmark_fit",
    "vsm_interpretation",
    "canonical_state_at_review",
    "canonical_states_at_review",
    "canonical_system_eligible",
    "coverage_class",
}


def forbidden_key(key: str) -> bool:
    return (
        key in FORBIDDEN_EXACT
        or key.startswith("autonomy_s")
        or key.startswith("vsm_")
        or re.match(r"^canonical_.*state", key) is not None
    )


def walk(value, path="$"):
    if isinstance(value, dict):
        for key, child in value.items():
            key_path = f"{path}.{key}"
            if forbidden_key(key):
                yield key_path, child
            yield from walk(child, key_path)
    elif isinstance(value, list):
        for idx, child in enumerate(value):
            yield from walk(child, f"{path}[{idx}]")

hits = []
for path in sorted(RAW.glob("*.json")):
    data = json.loads(path.read_text(encoding="utf-8"))
    for key_path, value in walk(data):
        hits.append((path.name, key_path, value))

print(f"raw_json_files={len(list(RAW.glob('*.json')))}")
print(f"forbidden_field_hits={len(hits)}")
for filename, key_path, value in hits:
    print(f"{filename}\t{key_path}\t{json.dumps(value, ensure_ascii=False, sort_keys=True)}")
