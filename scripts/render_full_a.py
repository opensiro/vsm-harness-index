#!/usr/bin/env python3
"""Render harnesses with an exact A/A/A/A/A/A autonomy vector."""
from __future__ import annotations

import argparse
from pathlib import Path

from render_tldr import anchored_label, data, escape
from validate_tldr import vector


FULL_A_VECTOR = ["A", "A", "A", "A", "A", "A"]


def full_a_rows(repo: Path):
    """Return included canonical rows whose six autonomy states are exactly A."""
    return [row for row in data(repo) if vector(row[2]) == FULL_A_VECTOR]


def render_full_a(repo: Path) -> str:
    lines = [
        "# Full-A Pivot",
        "",
        "Generated projection of included standalone assessments whose exact autonomy vector is `A A A A A A`. Composite or parent-governed states such as `A(P)` do not count as exact `A` in this view.",
        "",
        "| Harness | S1 | S2 | S3 | S3* | S4 | S5 | TL;DR |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for _, catalog, assessment, signature in full_a_rows(repo):
        states = vector(assessment)
        lines.append(
            "| "
            + " | ".join([anchored_label(catalog), *states, escape(signature)])
            + " |"
        )

    lines += [
        "",
        "This is a deterministic ownership-coverage view, not a product-quality score or maturity ladder. TL;DR text is reused from the cohort-relative signature corpus in `data/signatures.psv`.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    path = repo / "FULL_A.md"
    rendered = render_full_a(repo)

    if args.check:
        if not path.exists() or path.read_text(encoding="utf-8") != rendered:
            raise SystemExit("FULL_A.md is stale; run scripts/render_full_a.py")
    else:
        path.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
