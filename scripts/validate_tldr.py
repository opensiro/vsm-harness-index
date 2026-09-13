#!/usr/bin/env python3
"""Validate categorical VSM/OSM autonomy fingerprints in catalog order."""

from __future__ import annotations

import csv
from pathlib import Path

SYSTEMS = ("S1", "S2", "S3", "S3*", "S4", "S5")
ALLOWED = {
    "S1": ("S1 · A:", "S1 · C:", "S1: ?"),
    "S2": ("S2 · A:", "S2 · C:", "S2: —", "S2: ?"),
    "S3": ("S3 · A:", "S3 · C:", "S3: —", "S3: ?"),
    "S3*": ("S3* · A:", "S3* · C:", "S3*: —", "S3*: ?"),
    "S4": ("S4 · A:", "S4 · C:", "S4: —", "S4: ?"),
    "S5": ("S5 · A:", "S5 · C:", "S5 · P:", "S5: —", "S5: ?"),
}

def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    with (repo / "data" / "catalog.psv").open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="|"))
    positions = [int(row["catalog_position"]) for row in rows]
    if positions != sorted(positions) or len(positions) != len(set(positions)):
        raise SystemExit("catalog_position must be unique and ascending")
    included = 0
    for row in rows:
        label = f'{row["catalog_position"]}:{row["harness_id"]}'
        value = row["vsm_tldr"].replace("\\n", "\n")
        status = row["tldr_status"]
        if status == "excluded-no-agentic-vsm":
            if value:
                raise SystemExit(f"{label}: excluded row has a fingerprint")
            continue
        if status != "included":
            raise SystemExit(f"{label}: unknown tldr_status {status!r}")
        included += 1
        if len(value) > 420:
            raise SystemExit(f"{label}: fingerprint is {len(value)} characters")
        lines = value.splitlines()
        if len(lines) != 6:
            raise SystemExit(f"{label}: expected six lines, got {len(lines)}")
        for system, line in zip(SYSTEMS, lines, strict=True):
            if not any(line == prefix or line.startswith(prefix + " ") for prefix in ALLOWED[system]):
                raise SystemExit(f"{label}: invalid {system} line: {line!r}")
    print(f"validated {included} included fingerprints in catalog order")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
