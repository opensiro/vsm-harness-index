#!/usr/bin/env python3
"""Validate registry, standalone assessments, signatures, and generated views."""
from __future__ import annotations
import csv
from pathlib import Path
from validate_tldr import load_assessments, validate_assessment
from render_tldr import render_tldr, render_rankings


def read_psv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="|"))


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    catalog = read_psv(repo / "data" / "catalog.psv")
    positions = [int(row["catalog_position"]) for row in catalog]
    if positions != list(range(1, len(catalog) + 1)):
        raise SystemExit("catalog positions must be contiguous from 1")
    if len({row["harness_id"] for row in catalog}) != len(catalog):
        raise SystemExit("catalog harness_id values must be unique")
    by_id = {row["harness_id"]: row for row in catalog}

    assessments = load_assessments(repo / "assessments")
    completed_positions = []
    for harness_id, assessment in assessments.items():
        validate_assessment(assessment)
        if harness_id not in by_id:
            raise SystemExit(f"unknown assessment harness_id: {harness_id}")
        source = by_id[harness_id]
        for key in ("project_name", "repository", "review_ref", "reviewed_at"):
            if assessment[key] != source[key]:
                raise SystemExit(f"{harness_id}: assessment {key} differs from catalog")
        completed_positions.append(int(source["catalog_position"]))
    completed_positions.sort()
    if completed_positions != list(range(1, len(completed_positions) + 1)):
        raise SystemExit("assessment migration must be a contiguous catalog prefix")

    signatures = read_psv(repo / "data" / "signatures.psv")
    signature_ids = [row["harness_id"] for row in signatures]
    included_ids = [h for h, row in assessments.items() if row["status"] == "included"]
    if set(signature_ids) != set(included_ids):
        raise SystemExit("signatures must cover exactly the included assessments")
    for row in signatures:
        if int(row["catalog_position"]) != int(by_id[row["harness_id"]]["catalog_position"]):
            raise SystemExit(f"{row['harness_id']}: signature position mismatch")

    expected = {repo / "TLDR.md": render_tldr(repo), repo / "RANKINGS.md": render_rankings(repo)}
    for path, text in expected.items():
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            raise SystemExit(f"{path.name} is stale; run scripts/render_tldr.py")
    print(f"Validated {len(assessments)} assessment(s) across {len(catalog)} catalog candidates")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
