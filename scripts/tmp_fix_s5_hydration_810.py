#!/usr/bin/env python3
from pathlib import Path

paths = [
    Path("experiments/functional-capability-depth/s5-system-benchmarks/validate.py"),
    Path("experiments/functional-capability-depth/s5-system-benchmarks/matched-cell/validate_s5_primary_search_closure.py"),
    Path("experiments/functional-capability-depth/s5-system-benchmarks/matched-cell/validate_second_canonical_search.py"),
    Path("tests/test_s5_neutral_registry_migration_810.py"),
]
for path in paths:
    text = path.read_text(encoding="utf-8")
    old = '{"observation_id", "kind", "evidence_surface"}'
    old_compact = '{"observation_id","kind","evidence_surface"}'
    if old in text:
        text = text.replace(old, '{"observation_id", "kind"}')
    elif old_compact in text:
        text = text.replace(old_compact, '{"observation_id","kind"}')
    else:
        raise SystemExit(f"expected hydration skip set not found in {path}")
    path.write_text(text, encoding="utf-8")
print("S5 hydration now preserves generic neutral evidence_surface")
