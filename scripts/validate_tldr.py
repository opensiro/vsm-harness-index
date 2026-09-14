#!/usr/bin/env python3
"""Parse and validate standalone harness assessments."""
from __future__ import annotations
from pathlib import Path

SYSTEM_KEYS = ("s1", "s2", "s3", "s3_star", "s4", "s5")
ALLOWED = {"A", "C", "P", "—", "?"}


def parse_assessment(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError(f"{path}: malformed frontmatter")
    row: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            row[key.strip()] = value.strip()
    row["path"] = str(path)
    return row


def load_assessments(directory: Path) -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for path in sorted(directory.glob("*.md")):
        row = parse_assessment(path)
        harness_id = row.get("harness_id", "")
        if not harness_id or harness_id in rows:
            raise ValueError(f"{path}: missing or duplicate harness_id")
        rows[harness_id] = row
    return rows


def vector(row: dict[str, str]) -> list[str]:
    return [row.get(f"autonomy_{key}", "") for key in SYSTEM_KEYS]


def validate_assessment(row: dict[str, str]) -> None:
    for key in ("harness_id", "project_name", "repository", "review_ref", "reviewed_at", "status"):
        if not row.get(key):
            raise ValueError(f"{row.get('path')}: missing {key}")
    if len(row["review_ref"]) != 40:
        raise ValueError(f"{row['harness_id']}: review_ref must be 40 characters")
    states = vector(row)
    if any(state not in ALLOWED for state in states):
        raise ValueError(f"{row['harness_id']}: invalid autonomy state")
    if any(state == "P" for state in states[:-1]):
        raise ValueError(f"{row['harness_id']}: P is valid only for S5")
    if row["status"] == "included" and states[0] != "A":
        raise ValueError(f"{row['harness_id']}: included harness must establish S1 · A")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    rows = load_assessments(repo / "assessments")
    for row in rows.values():
        validate_assessment(row)
    print(f"Validated {len(rows)} standalone assessment(s)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
