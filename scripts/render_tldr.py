#!/usr/bin/env python3
"""Render cohort signatures and deterministic autonomy rankings."""
from __future__ import annotations
import argparse, csv
from pathlib import Path
from validate_tldr import load_assessments, validate_assessment, vector


def read_psv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="|"))


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def data(repo: Path):
    catalog = read_psv(repo / "data" / "catalog.psv")
    by_id = {row["harness_id"]: row for row in catalog}
    assessments = load_assessments(repo / "assessments")
    for row in assessments.values():
        validate_assessment(row)
    signatures = {row["harness_id"]: row["signature"] for row in read_psv(repo / "data" / "signatures.psv")}
    completed = []
    for harness_id, assessment in assessments.items():
        if assessment["status"] != "included":
            continue
        catalog_row = by_id[harness_id]
        completed.append((int(catalog_row["catalog_position"]), catalog_row, assessment, signatures.get(harness_id, "? pending synthesis")))
    completed.sort(key=lambda item: item[0])
    return completed


def render_tldr(repo: Path) -> str:
    lines = ["# VSM Harness TL;DR", "", "Cohort-relative signatures derived from standalone assessments in ascending catalog order.", "", "| Harness | S1 | S2 | S3 | S3* | S4 | S5 | Signature |", "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for _, catalog, assessment, signature in data(repo):
        states = vector(assessment)
        label = f"[{escape(catalog['project_name'])}]({catalog['repository']})"
        lines.append("| " + " | ".join([label, *states, escape(signature)]) + " |")
    lines += ["", "Assessments are repository-relative; signatures are cohort-relative and may change when the ordered cohort changes.", ""]
    return "\n".join(lines)


def render_rankings(repo: Path) -> str:
    rows = []
    for position, catalog, assessment, _ in data(repo):
        states = vector(assessment)
        rows.append((sum(s == "A" for s in states[1:]), sum(s == "A" for s in states), sum(s == "C" for s in states), sum(s == "P" for s in states), sum(s == "?" for s in states), position, catalog, states))
    rows.sort(key=lambda r: (-r[0], -r[1], r[4], r[5]))
    lines = ["# VSM Harness Autonomy Rankings", "", "This ranks out-of-box agent ownership of VSM functions, not product quality or organizational viability. No fractional weights are assigned to C, P, or ?.", "", "| Rank | Harness | Agent-owned | Metasystem A | C | P | ? | Vector |", "| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |"]
    for rank, row in enumerate(rows, 1):
        meta_a, total_a, c_count, p_count, unknown, _, catalog, states = row
        label = f"[{escape(catalog['project_name'])}]({catalog['repository']})"
        lines.append(f"| {rank} | {label} | {total_a}/6 | {meta_a}/5 | {c_count} | {p_count} | {unknown} | `{' '.join(states)}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--check", action="store_true"); args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    outputs = {repo / "TLDR.md": render_tldr(repo), repo / "RANKINGS.md": render_rankings(repo)}
    if args.check:
        stale = [str(path) for path, text in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != text]
        if stale: raise SystemExit("stale generated file(s): " + ", ".join(stale))
    else:
        for path, text in outputs.items(): path.write_text(text, encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
