#!/usr/bin/env python3
"""Render harnesses with autonomous ownership across all six VSM functions."""
from __future__ import annotations

import argparse
from pathlib import Path

from render_tldr import anchored_label, base_state, data, escape
from validate_tldr import vector


def has_full_a_coverage(assessment: dict[str, str]) -> bool:
    """Return true when every VSM function has base autonomy state A.

    A(P) counts because it preserves an autonomous mode and additionally exposes
    an optional parent-governed mode. P by itself does not count as autonomous.
    """
    return all(base_state(state) == "A" for state in vector(assessment))


def full_a_rows(repo: Path):
    """Return included canonical rows with autonomous ownership in all six functions."""
    return [row for row in data(repo) if has_full_a_coverage(row[2])]


def render_full_a(repo: Path) -> str:
    lines = [
        "# Full-A Pivot",
        "",
        "Generated projection of included standalone assessments with autonomous ownership across all six VSM functions. `A(P)` counts as autonomous coverage because `P` is an additional optional parent-governed mode; parent-only `P` does not count.",
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
