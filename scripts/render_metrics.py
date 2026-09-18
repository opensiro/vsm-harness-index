#!/usr/bin/env python3
"""Render deterministic corpus metrics from canonical Index artifacts."""
from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path

from render_full_a import full_a_rows
from render_tldr import data, read_psv

MILESTONES = (100, 250, 500, 1000)


def milestone_rows(included: int) -> list[dict[str, object]]:
    pending = [target for target in MILESTONES if target > included]
    next_target = pending[0] if pending else None
    rows: list[dict[str, object]] = []
    for target in MILESTONES:
        if included >= target:
            status = "achieved"
        elif target == next_target:
            status = "next"
        else:
            status = "planned"
        rows.append(
            {
                "target": target,
                "status": status,
                "completed": included,
                "progress_fraction": min(included / target, 1.0),
            }
        )
    return rows


def compute_metrics(repo: Path) -> dict[str, object]:
    catalog_entries = len(read_psv(repo / "data" / "catalog.psv"))
    included_assessments = len(data(repo))
    if included_assessments > catalog_entries:
        raise ValueError("included assessments cannot exceed catalog entries")

    active_contract = read_psv(repo / "data" / "active-contract.psv")
    if len(active_contract) != 1:
        raise ValueError("active-contract.psv must contain exactly one row")
    contract = active_contract[0]

    return {
        "schema_version": 1,
        "corpus": {
            "included_assessments": included_assessments,
            "catalog_entries": catalog_entries,
            "catalog_entries_without_included_assessment": catalog_entries - included_assessments,
            "full_a_assessments": len(full_a_rows(repo)),
        },
        "active_contract": {
            "profile_version": contract["profile_version"],
            "methodology_version": contract["methodology_version"],
        },
        "milestones": milestone_rows(included_assessments),
    }


def render_json(repo: Path) -> str:
    return json.dumps(compute_metrics(repo), indent=2, ensure_ascii=False) + "\n"


def render_markdown(repo: Path) -> str:
    metrics = compute_metrics(repo)
    corpus = metrics["corpus"]
    contract = metrics["active_contract"]

    lines = [
        "# VSM Harness Index Metrics",
        "",
        "Deterministic numerical snapshot generated from canonical Index artifacts. Do not edit the values by hand; run `python scripts/render_metrics.py` after corpus changes.",
        "",
        "## Corpus",
        "",
        "| Metric | Value | Definition |",
        "| --- | ---: | --- |",
        f"| Included standalone assessments | {corpus['included_assessments']} | Canonical assessments with `status: included`. |",
        f"| Catalog entries | {corpus['catalog_entries']} | Rows in `data/catalog.psv`; this is discovery/order/provenance infrastructure, not a second assessment database. |",
        f"| Catalog entries without an included assessment | {corpus['catalog_entries_without_included_assessment']} | `catalog entries - included assessments`; these are not automatically equivalent to pending admissions. |",
        f"| Full-A assessments | {corpus['full_a_assessments']} | Included assessments whose base state is autonomous across S1, S2, S3, S3*, S4 and S5. `A(P)` counts as autonomous coverage. |",
        "",
        "## Active semantic contract",
        "",
        f"Profile **{contract['profile_version']}** / Methodology **{contract['methodology_version']}**",
        "",
        "## Public corpus milestones",
        "",
        "Milestones count included completed standalone assessments only. They are corpus-size checkpoints, not coverage or quality scores.",
        "",
        "| Target | Status | Progress |",
        "| ---: | --- | ---: |",
    ]

    for row in metrics["milestones"]:
        status = str(row["status"]).capitalize()
        target = int(row["target"])
        completed = int(row["completed"])
        progress = float(row["progress_fraction"]) * 100
        lines.append(f"| {target} | {status} | {completed}/{target} ({progress:.1f}%) |")

    lines += [
        "",
        "## Machine-readable view",
        "",
        "The same snapshot is available in [`data/metrics.json`](data/metrics.json) for downstream synchronization such as `opensiro.com`.",
        "",
        "Source-of-truth relationship:",
        "",
        "```text",
        "assessments/*.md + data/catalog.psv + data/active-contract.psv",
        "                         ↓",
        "              scripts/render_metrics.py",
        "                         ↓",
        "             METRICS.md + data/metrics.json",
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    outputs = {
        repo / "METRICS.md": render_markdown(repo),
        repo / "data" / "metrics.json": render_json(repo),
    }

    if args.check:
        stale: list[str] = []
        for path, rendered in outputs.items():
            rel = str(path.relative_to(repo))
            current = path.read_text(encoding="utf-8") if path.exists() else ""
            if current == rendered:
                continue
            stale.append(rel)
            print(
                "".join(
                    difflib.unified_diff(
                        current.splitlines(keepends=True),
                        rendered.splitlines(keepends=True),
                        fromfile=rel,
                        tofile=f"generated/{rel}",
                    )
                ),
                end="",
            )
        if stale:
            raise SystemExit("stale generated metric file(s): " + ", ".join(stale))
    else:
        for path, rendered in outputs.items():
            path.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
