#!/usr/bin/env python3
"""Render the experimental cross-function primary-baseline status view."""

from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SELECTION = HERE / "primary-baselines.json"
OUTPUT = HERE / "FUNCTION-BASELINES.md"
FUNCTION_ORDER = ("S1", "S2", "S3", "S3*", "S4", "S5")
SUPPORTED_STATUSES = {"selected", "gap"}
COVERAGE_PATHS = {
    "S2": HERE / "s2-system-benchmarks" / "coverage.json",
    "S3": HERE / "s3-system-benchmarks" / "coverage.json",
    "S3*": HERE / "s3star-system-benchmarks" / "coverage.json",
    "S4": HERE / "s4-system-benchmarks" / "coverage.json",
    "S5": HERE / "s5-system-benchmarks" / "coverage.json",
}
OPTIONAL_COUNT_FIELDS = (
    ("direct_benchmark_family_count", "direct families"),
    ("direct_family_count", "direct families"),
    ("direct_observation_count", "direct observations"),
    ("canonical_direct_observation_count", "canonical direct observations"),
    ("composed_direct_observation_count", "composed direct observations"),
)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def load_json(path: Path) -> dict:
    if not path.exists():
        fail(f"missing source: {path.relative_to(ROOT)}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"{path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def selected_primary(function: str, item: dict) -> tuple[str, str]:
    primary = item.get("primary")
    if not isinstance(primary, dict):
        fail(f"{function}: selected baseline requires primary object")
    benchmark_id = primary.get("benchmark_id")
    benchmark_name = primary.get("benchmark_name")
    reference_model = primary.get("reference_model")
    if not isinstance(benchmark_id, str) or not benchmark_id:
        fail(f"{function}: selected primary benchmark_id missing")
    if not isinstance(benchmark_name, str) or not benchmark_name:
        fail(f"{function}: selected primary benchmark_name missing")
    if not isinstance(reference_model, str) or not reference_model:
        fail(f"{function}: selected primary reference_model missing")
    return benchmark_name, reference_model


def gap_reason(function: str, item: dict) -> str:
    reason = item.get("blocking_reason")
    if isinstance(reason, str) and reason.strip():
        return reason.strip()

    reviewed = item.get("reviewed_direct_families")
    if isinstance(reviewed, list):
        reasons: list[str] = []
        for family in reviewed:
            if not isinstance(family, dict):
                continue
            candidate = family.get("blocking_reason")
            if isinstance(candidate, str) and candidate.strip():
                candidate = candidate.strip()
                if candidate not in reasons:
                    reasons.append(candidate)
        if reasons:
            return " ".join(reasons)

    fail(f"{function}: gap baseline requires blocking_reason evidence")


def load_gap_coverage(function: str) -> tuple[dict, Path]:
    path = COVERAGE_PATHS.get(function)
    if path is None:
        fail(f"{function}: no expected gap coverage source is defined")
    coverage = load_json(path)
    if coverage.get("function") != function:
        fail(
            f"{function}: coverage function mismatch in "
            f"{path.relative_to(ROOT)}: {coverage.get('function')!r}"
        )
    reviewed_at = coverage.get("reviewed_at")
    if not isinstance(reviewed_at, str) or not reviewed_at.strip():
        fail(f"{function}: gap coverage reviewed_at missing")
    cases = coverage.get("cases")
    if not isinstance(cases, list) or not cases:
        fail(f"{function}: gap coverage cases must be a non-empty list")
    return coverage, path


def evidence_summary(coverage: dict, path: Path) -> str:
    cases = coverage["cases"]
    reviewed_at = coverage["reviewed_at"]
    rel = path.relative_to(HERE).as_posix()
    parts = [
        f"[`coverage.json`]({rel})",
        f"reviewed `{reviewed_at}`",
        f"{len(cases)} reviewed cases",
    ]
    seen_labels: set[str] = set()
    for field, label in OPTIONAL_COUNT_FIELDS:
        if field not in coverage:
            continue
        value = coverage[field]
        if not isinstance(value, int) or value < 0:
            fail(f"{coverage.get('function')}: {field} must be a non-negative integer")
        # Some function-specific schemas use different field names for the same
        # concept. Preserve the source schema without printing duplicate labels.
        if label in seen_labels:
            continue
        seen_labels.add(label)
        parts.append(f"{label}: `{value}`")
    return " · ".join(parts)


def render() -> str:
    selection = load_json(SELECTION)
    functions = selection.get("functions")
    if not isinstance(functions, dict):
        fail("primary-baselines.json functions must be an object")

    rows: list[tuple[str, str, str, str, str]] = []
    gap_rows: list[tuple[str, str, str]] = []

    for function in FUNCTION_ORDER:
        item = functions.get(function)
        if not isinstance(item, dict):
            fail(f"primary-baselines.json missing {function}")
        status = item.get("status")
        if status not in SUPPORTED_STATUSES:
            fail(f"{function}: unsupported baseline status {status!r}")

        if status == "selected":
            family, model = selected_primary(function, item)
            if function == "S1":
                evidence = "[generated S1 baseline](S1-BASELINE.md)"
            else:
                evidence = "selected primary in `primary-baselines.json`"
            rows.append((function, status, family, model, evidence))
            continue

        reason = gap_reason(function, item)
        coverage, coverage_path = load_gap_coverage(function)
        evidence = evidence_summary(coverage, coverage_path)
        rows.append((function, status, "—", "—", evidence))
        gap_rows.append(
            (
                function,
                coverage_path.relative_to(HERE).as_posix(),
                reason,
            )
        )

    lines = [
        "# Function Capability Baselines",
        "",
        "Generated experimental projection from `primary-baselines.json` and the function-specific S2–S5 coverage records.",
        "",
        "This view reports baseline availability and evidence coverage only. It does not change canonical VSM ownership, create a capability score, or replace the function-specific evidence records.",
        "",
        "## Current primary-baseline state",
        "",
        "| Function | Status | Primary family | Reference model | Evidence state |",
        "| --- | --- | --- | --- | --- |",
    ]

    for function, status, family, model, evidence in rows:
        model_cell = model if model == "—" else f"`{model}`"
        lines.append(
            f"| {function} | `{status}` | {family} | {model_cell} | {evidence} |"
        )

    lines += [
        "",
        "A `gap` means that no matched canonical-harness primary baseline has been selected for that function. It is not a zero capability score and it does not mean benchmark evidence is absent.",
        "",
        "## Why the current gaps remain",
        "",
    ]

    for function, coverage_rel, reason in gap_rows:
        lines += [
            f"### {function}",
            "",
            reason,
            "",
            f"Evidence search: [`{coverage_rel}`]({coverage_rel}).",
            "",
        ]

    lines += [
        "## Reading rule",
        "",
        "```text",
        "canonical VSM ownership",
        "        ↓",
        "one selected primary benchmark per function when evidence permits",
        "        ↓",
        "matched canonical-harness comparison",
        "        ↓",
        "secondary evidence and domain projections",
        "",
        "separate evidence class:",
        "adaptive / self-organizing S",
        "```",
        "",
        "Function-specific coverage schemas remain authoritative for their own evidence vocabulary. This projection intentionally consumes their common review metadata without forcing those schemas into one normalized replacement database.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    rendered = render()
    if args.check:
        actual = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if actual != rendered:
            diff = "".join(
                difflib.unified_diff(
                    actual.splitlines(keepends=True),
                    rendered.splitlines(keepends=True),
                    fromfile=str(OUTPUT.relative_to(ROOT)),
                    tofile="generated",
                )
            )
            if diff:
                print(diff, end="")
            raise SystemExit(
                "FUNCTION-BASELINES.md is stale; run "
                "experiments/functional-capability-depth/render_function_baselines.py"
            )
    else:
        OUTPUT.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
