#!/usr/bin/env python3
"""Render deterministic corpus metrics from canonical Index artifacts."""
from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path

from render_full_a import full_a_rows
from render_tldr import data, read_psv
from validate_tldr import load_assessments, validate_assessment

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


def compute_core_metrics(repo: Path) -> dict[str, int]:
    """Return repository-owned corpus stock metrics usable on historical trees."""
    return {
        "included_assessments": len(data(repo)),
        "catalog_entries": len(read_psv(repo / "data" / "catalog.psv")),
    }


def compute_metrics(repo: Path) -> dict[str, object]:
    core = compute_core_metrics(repo)
    catalog_entries = core["catalog_entries"]
    included_rows = data(repo)
    included_assessments = core["included_assessments"]
    if not included_rows:
        raise ValueError("cannot compute snapshot_date for an empty included cohort")
    snapshot_date = max(catalog["pinned_at"] for _, catalog, _, _ in included_rows)

    assessments = load_assessments(repo / "assessments")
    for row in assessments.values():
        validate_assessment(row)
    proposed_assessments = sum(row["status"] == "proposed" for row in assessments.values())
    excluded_assessments = sum(row["status"] == "excluded-no-agentic-vsm" for row in assessments.values())
    canonical_assessments = len(assessments) - proposed_assessments

    if included_assessments + excluded_assessments != canonical_assessments:
        raise ValueError("canonical assessment status counts are inconsistent")
    if canonical_assessments != catalog_entries:
        raise ValueError("canonical assessment count must match catalog entries")

    active_contract = read_psv(repo / "data" / "active-contract.psv")
    if len(active_contract) != 1:
        raise ValueError("active-contract.psv must contain exactly one row")
    contract = active_contract[0]

    reassessment_events = len(read_psv(repo / "data" / "reassessment-history.psv"))

    return {
        "schema_version": 1,
        "snapshot_date": snapshot_date,
        "corpus": {
            "included_assessments": included_assessments,
            "canonical_assessments": canonical_assessments,
            "excluded_assessments": excluded_assessments,
            "proposed_assessments": proposed_assessments,
            "catalog_entries": catalog_entries,
            "catalog_entries_without_included_assessment": catalog_entries - included_assessments,
            "reassessment_events": reassessment_events,
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
        f"| Included standalone assessments | {corpus['included_assessments']} | Canonical assessments with `status: included`; this is the public corpus-size milestone counter. |",
        f"| Canonical assessment records | {corpus['canonical_assessments']} | Included plus canonical `excluded-no-agentic-vsm` assessment records. |",
        f"| Canonical exclusions | {corpus['excluded_assessments']} | Completed assessments with `status: excluded-no-agentic-vsm`. |",
        f"| Proposed intake assessments | {corpus['proposed_assessments']} | Assessment files still in `status: proposed`; not counted in the canonical corpus. |",
        f"| Catalog entries | {corpus['catalog_entries']} | Rows in `data/catalog.psv`; this is discovery/order/provenance infrastructure, not a second assessment database. |",
        f"| Catalog entries without an included assessment | {corpus['catalog_entries_without_included_assessment']} | `catalog entries - included assessments`; this includes canonical exclusions and is not automatically equivalent to pending work. |",
        f"| Reassessment events | {corpus['reassessment_events']} | Recorded events in `data/reassessment-history.psv`. |",
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
        if completed >= target:
            progress_text = f"Achieved (current corpus: {completed})"
        else:
            progress_text = f"{completed}/{target} ({progress:.1f}%)"
        lines.append(f"| {target} | {status} | {progress_text} |")

    lines += [
        "",
        "## Machine-readable view",
        "",
        "The same snapshot is available in [`data/metrics.json`](data/metrics.json) for downstream synchronization such as `opensiro.com`.",
        "",
        "Source-of-truth relationship:",
        "",
        "```text",
        "assessments/*.md + data/catalog.psv + data/reassessment-history.psv",
        "                  + data/active-contract.psv",
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
    parser.add_argument(
        "--source-root",
        type=Path,
        help="read metric sources from this repository tree instead of the current checkout",
    )
    parser.add_argument(
        "--stdout-core-json",
        action="store_true",
        help="print read-only core corpus metrics as JSON and exit",
    )
    args = parser.parse_args()

    repo = (
        args.source_root.resolve()
        if args.source_root is not None
        else Path(__file__).resolve().parents[1]
    )

    if args.stdout_core_json:
        print(json.dumps(compute_core_metrics(repo), sort_keys=True))
        return 0
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
