#!/usr/bin/env python3
"""Render cohort signatures, autonomy rankings, and temporal projections."""
from __future__ import annotations
import argparse, csv
from collections import defaultdict
from datetime import date
from pathlib import Path
from validate_tldr import load_assessments, validate_assessment, vector


FUNCTIONS = ("S1", "S2", "S3", "S3*", "S4", "S5")


def read_psv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="|"))


def escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def base_state(state: str) -> str:
    if state == "A(P)":
        return "A"
    if state == "C(P)":
        return "C"
    return state


def has_parent_mode(state: str) -> bool:
    return state in {"A(P)", "C(P)", "P"}


def display_name(catalog: dict[str, str]) -> str:
    # Public naming can evolve without changing the stable harness_id used by
    # assessments/signatures. GSD is the current project name for gsd-core.
    if catalog["harness_id"] == "get-shit-done":
        return "GSD"
    return catalog["project_name"]


def anchored_label(catalog: dict[str, str]) -> str:
    """Render a project link with a stable per-harness HTML anchor."""
    anchor = f'<a id="{catalog["harness_id"]}"></a>'
    return f"{anchor}[{escape(display_name(catalog))}]({catalog['repository']})"


def year(catalog: dict[str, str]) -> str:
    return catalog["repository_created_at"][:4]


def quarter_from_timestamp(timestamp: str) -> str:
    """Derive a calendar quarter from an ISO-style repository timestamp."""
    month = int(timestamp[5:7])
    if not 1 <= month <= 12:
        raise ValueError(f"invalid month in repository_created_at: {timestamp}")
    return f"Q{((month - 1) // 3) + 1}"


def quarter(catalog: dict[str, str]) -> str:
    return quarter_from_timestamp(catalog["repository_created_at"])


def period(catalog: dict[str, str]) -> str:
    return f"{year(catalog)}-{quarter(catalog)}"


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
    rows = data(repo)
    rows.sort(key=lambda item: (item[1]["repository_created_at"], item[0]), reverse=True)
    lines = [
        "# VSM Harness TL;DR",
        "",
        "Cohort-relative signatures derived from standalone assessments. Display order is newest-first by GitHub repository creation time; Period is the repository creation quarter derived from `repository_created_at` as `YYYY-QN`. Signature synthesis still follows ascending catalog order.",
        "",
        "| Harness | Period | S1 | S2 | S3 | S3* | S4 | S5 | Signature |",
        "| --- | ---: | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for _, catalog, assessment, signature in rows:
        states = vector(assessment)
        label = anchored_label(catalog)
        lines.append("| " + " | ".join([label, period(catalog), *states, escape(signature)]) + " |")
    lines += ["", "Assessments are repository-relative; signatures are cohort-relative and may change when the ordered cohort changes.", ""]
    return "\n".join(lines)


def render_rankings(repo: Path) -> str:
    rows = []
    for position, catalog, assessment, _ in data(repo):
        states = vector(assessment)
        bases = [base_state(s) for s in states]
        rows.append((
            sum(s == "A" for s in bases[1:]),
            sum(s == "A" for s in bases),
            sum(s == "C" for s in bases),
            sum(has_parent_mode(s) for s in states),
            sum(s == "?" for s in states),
            catalog["repository_created_at"],
            position,
            catalog,
            states,
        ))
    # Coverage determines rank. Freshness is presentation-only inside an equal
    # coverage tie and never changes the rank key.
    rows.sort(key=lambda r: (r[0], r[1], r[5], r[6]), reverse=True)
    lines = [
        "# VSM Harness Autonomy Rankings",
        "",
        "This ranks out-of-box agent ownership of VSM functions, not product quality or organizational viability. Equal agent-owned coverage receives the same rank; C, P, and ? are reported but never used as weighted scores. Within the same rank, newer repositories are displayed first. Period is the GitHub repository creation quarter and does not affect rank.",
        "",
        "| Rank | Harness | Period | Agent-owned | Metasystem A | C | P | ? | Vector |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    rank = 0
    previous_key = None
    for row in rows:
        meta_a, total_a, c_count, p_count, unknown, _, _, catalog, states = row
        key = (meta_a, total_a)
        if key != previous_key:
            rank += 1
            previous_key = key
        label = anchored_label(catalog)
        lines.append(f"| {rank} | {label} | {period(catalog)} | {total_a}/6 | {meta_a}/5 | {c_count} | {p_count} | {unknown} | `{' '.join(states)}` |")
    lines.append("")
    return "\n".join(lines)


def snapshot_date(rows) -> date:
    """Use canonical intake provenance rather than wall-clock time for rendering."""
    if not rows:
        raise ValueError("cannot render temporal projection for an empty included cohort")
    return max(date.fromisoformat(catalog["pinned_at"]) for _, catalog, _, _ in rows)


def group_temporal(rows, key_fn) -> dict[str, list[list[str]]]:
    groups: dict[str, list[list[str]]] = defaultdict(list)
    for _, catalog, assessment, _ in rows:
        groups[key_fn(catalog)].append(vector(assessment))
    return dict(groups)


def share(count: int, total: int) -> str:
    return f"{count}/{total} ({100.0 * count / total:.1f}%)"


def render_temporal_table(
    groups: dict[str, list[list[str]]],
    *,
    base: bool,
    current_key: str,
    current_suffix: str,
) -> list[str]:
    lines = [
        "| Period | N | S1 | S2 | S3 | S3* | S4 | S5 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for key in sorted(groups):
        vectors = groups[key]
        total = len(vectors)
        counts = []
        for index in range(len(FUNCTIONS)):
            states = [states[index] for states in vectors]
            if base:
                count = sum(base_state(state) == "A" for state in states)
            else:
                count = sum(state == "A" for state in states)
            counts.append(share(count, total))
        label = f"{key} {current_suffix}" if key == current_key else key
        lines.append("| " + " | ".join([label, str(total), *counts]) + " |")
    return lines


def render_temporal(repo: Path) -> str:
    rows = data(repo)
    as_of = snapshot_date(rows)
    current_year = str(as_of.year)
    current_period = f"{as_of.year}-{quarter_from_timestamp(as_of.isoformat())}"
    annual = group_temporal(rows, year)
    quarterly = group_temporal(rows, period)

    lines = [
        "# VSM Harness Temporal Projection",
        "",
        "Deterministic descriptive cohorts derived from canonical included assessments and GitHub repository creation time.",
        "",
        "- **Period meaning:** GitHub repository creation quarter from `data/catalog.psv:repository_created_at`",
        "- **Quarter convention:** Q1 Jan-Mar, Q2 Apr-Jun, Q3 Jul-Sep, Q4 Oct-Dec",
        f"- **Current year:** {current_year} is marked **YTD**",
        f"- **Current quarter:** {current_period} is marked **partial**",
        "",
        "Repository creation time selects cohorts only. VSM states come from standalone canonical assessments. These projections describe ownership arrangements; they are not product-quality, maturity, or viability rankings.",
        "",
        "## Quarterly strict `A` share",
        "",
        "Strict counts include literal `A` only; `A(P)` remains visible as a distinct state and does not count here.",
        "",
        *render_temporal_table(quarterly, base=False, current_key=current_period, current_suffix="(partial)"),
        "",
        "## Quarterly base `A` share",
        "",
        "Base ownership follows ranking semantics: `A(P)` collapses to base `A`; `C`, `C(P)`, `P`, `—`, and `?` receive no fractional autonomous score.",
        "",
        *render_temporal_table(quarterly, base=True, current_key=current_period, current_suffix="(partial)"),
        "",
        "## Annual strict `A` share",
        "",
        *render_temporal_table(annual, base=False, current_key=current_year, current_suffix="(YTD)"),
        "",
        "## Annual base `A` share",
        "",
        *render_temporal_table(annual, base=True, current_key=current_year, current_suffix="(YTD)"),
        "",
        "The current year and quarter are incomplete observation windows. Compare closed periods directly; treat YTD/partial rows as provisional temporal slices.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--check", action="store_true"); args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    outputs = {
        repo / "TLDR.md": render_tldr(repo),
        repo / "RANKINGS.md": render_rankings(repo),
        repo / "analytics" / "temporal.md": render_temporal(repo),
    }
    if args.check:
        stale = [str(path) for path, text in outputs.items() if not path.exists() or path.read_text(encoding="utf-8") != text]
        if stale: raise SystemExit("stale generated file(s): " + ", ".join(stale))
    else:
        for path, text in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
