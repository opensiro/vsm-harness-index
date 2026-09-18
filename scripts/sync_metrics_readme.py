#!/usr/bin/env python3
"""Project the canonical corpus metrics into a compact README block."""
from __future__ import annotations

import argparse
from pathlib import Path

from render_metrics import compute_metrics

START = "<!-- VSM INDEX METRICS:START -->"
END = "<!-- VSM INDEX METRICS:END -->"


def render_block(repo: Path) -> str:
    metrics = compute_metrics(repo)
    corpus = metrics["corpus"]
    contract = metrics["active_contract"]
    next_row = next((row for row in metrics["milestones"] if row["status"] == "next"), None)

    lines = [
        START,
        "## Corpus snapshot",
        "",
        "| Included | Catalog | Reassessments | Full-A |",
        "| ---: | ---: | ---: | ---: |",
        f"| **{corpus['included_assessments']}** | {corpus['catalog_entries']} | {corpus['reassessment_events']} | {corpus['full_a_assessments']} |",
        "",
    ]
    if next_row is not None:
        target = int(next_row["target"])
        completed = int(next_row["completed"])
        progress = float(next_row["progress_fraction"]) * 100
        lines.append(f"**Next corpus milestone:** {completed}/{target} ({progress:.1f}%).")
        lines.append("")
    lines += [
        f"Active semantic contract: **Profile {contract['profile_version']} / Methodology {contract['methodology_version']}**.",
        "",
        "[Full metrics](METRICS.md) · [Machine-readable metrics](data/metrics.json)",
        END,
    ]
    return "\n".join(lines)


def replace_block(readme: str, block: str) -> str:
    if START in readme or END in readme:
        if readme.count(START) != 1 or readme.count(END) != 1:
            raise ValueError("README metrics markers must occur exactly once")
        before, rest = readme.split(START, 1)
        _, after = rest.split(END, 1)
        return before.rstrip() + "\n\n" + block + after

    anchor = "`data/catalog.psv` is deliberately separate from those artifacts. It is the discovery/order/provenance registry and contains no VSM grades."
    if anchor not in readme:
        raise ValueError("README insertion anchor not found")
    return readme.replace(anchor, anchor + "\n\n" + block, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    path = repo / "README.md"
    current = path.read_text(encoding="utf-8")
    expected = replace_block(current, render_block(repo))

    if args.check:
        if current != expected:
            raise SystemExit("README.md metrics block is stale; run python scripts/sync_metrics_readme.py")
    elif current != expected:
        path.write_text(expected, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
