#!/usr/bin/env python3
"""Render the current functional-capability public-evidence frontier.

This is a derived projection only. Historical synthesis remains immutable;
current state comes from primary-baselines.json and function-level closure JSON.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "EVIDENCE-FRONTIER.md"
BASELINES = HERE / "primary-baselines.json"

CLOSURES = {
    "S2": HERE / "s2-system-benchmarks" / "matched-cell" / "s2-primary-search-closure.json",
    "S3": HERE / "s3-system-benchmarks" / "matched-cell" / "s3-primary-search-closure.json",
    "S3*": HERE / "s3star-system-benchmarks" / "matched-cell" / "s3star-primary-search-closure.json",
    "S4": HERE / "s4-system-benchmarks" / "matched-cell" / "s4-primary-search-closure.json",
    "S5": HERE / "s5-system-benchmarks" / "matched-cell" / "s5-primary-search-closure.json",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(HERE).as_posix()


def compact_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, list):
        return ", ".join(str(item) for item in value)
    return str(value)


def evidence_depth(closure: dict[str, Any]) -> list[tuple[str, Any]]:
    depth = closure.get("evidence_depth")
    if isinstance(depth, dict) and depth:
        return list(depth.items())

    # S4 intentionally uses a different closure schema. Preserve it rather
    # than inventing a universal evidence-depth vocabulary.
    pairs: list[tuple[str, Any]] = []
    native = closure.get("canonical_native_observations")
    if isinstance(native, list):
        pairs.append(("canonical_native_observations", native))
    routes = closure.get("reviewed_routes")
    if isinstance(routes, list):
        pairs.append(("reviewed_routes", len(routes)))
    return pairs


def depth_inline(closure: dict[str, Any]) -> str:
    pairs = evidence_depth(closure)
    if not pairs:
        return "—"
    chunks = []
    for key, value in pairs:
        if isinstance(value, list):
            chunks.append(f"`{key}`: `{len(value)}`")
        else:
            chunks.append(f"`{key}`: `{compact_value(value)}`")
    return " · ".join(chunks)


def render() -> str:
    baselines = load(BASELINES)
    functions = baselines.get("functions") or {}
    closures = {function: load(path) for function, path in CLOSURES.items()}

    if functions.get("S1", {}).get("status") != "selected":
        raise SystemExit("S1 primary baseline is no longer selected; update frontier renderer contract")

    for function, closure in closures.items():
        baseline = functions.get(function) or {}
        if baseline.get("status") != closure.get("primary_baseline"):
            raise SystemExit(
                f"{function}: primary-baselines status {baseline.get('status')!r} "
                f"!= closure primary_baseline {closure.get('primary_baseline')!r}"
            )
        if closure.get("closure_scope") != "current-public-evidence":
            raise SystemExit(f"{function}: closure_scope drift")

    s1 = functions["S1"]
    primary = s1["primary"]
    harnesses = primary.get("canonical_harness_ids") or []

    lines = [
        "# Current Functional Capability Evidence Frontier",
        "",
        "Generated current-state projection from `primary-baselines.json` and the function-level public-evidence closure records.",
        "",
        "This file is **not** the historical experiment synthesis. `SYNTHESIS.md` and `experiment-state.json` preserve the closed research-cycle snapshot; this projection moves only when the current function-level source records move.",
        "",
        "It is also not a second evidence database: every state, count, blocker and reopen rule below is read from an existing source-of-truth artifact.",
        "",
        "## Current frontier",
        "",
        "| Function | Primary state | Current evidence depth | Reviewed through | Source |",
        "| --- | --- | --- | --- | --- |",
        (
            f"| S1 | `selected` — {primary['benchmark_name']} / `{primary['reference_model']}` | "
            f"`task_count`: `{primary['task_count']}` · `canonical_harnesses`: `{len(harnesses)}` | "
            f"`{baselines.get('selected_at', '—')}` | [`primary-baselines.json`](primary-baselines.json) |"
        ),
    ]

    for function, path in CLOSURES.items():
        closure = closures[function]
        lines.append(
            f"| {function} | `{closure['primary_baseline']}` | {depth_inline(closure)} | "
            f"`{closure.get('reviewed_at', '—')}` | [`{path.name}`]({rel(path)}) |"
        )

    lines.extend(
        [
            "",
            "A `gap` is an empirical evidence state, not a zero capability score and not a statement about canonical VSM ownership.",
            "",
            "## S1 — selected primary",
            "",
            f"- **Primary family:** {primary['benchmark_name']} (`{primary['benchmark_id']}`).",
            f"- **Reference model:** `{primary['reference_model']}`.",
            f"- **Comparison design:** `{primary['comparison_design']}`.",
            f"- **Canonical harnesses in the first cell:** {', '.join(f'`{item}`' for item in harnesses)}.",
            f"- **Primary source:** {primary['primary_source']}.",
            f"- **Provenance note:** {primary['provenance_note']}",
            "- **Source:** [`primary-baselines.json`](primary-baselines.json).",
        ]
    )

    for function, path in CLOSURES.items():
        closure = closures[function]
        baseline = functions[function]
        lines.extend(
            [
                "",
                f"## {function} — current `{closure['primary_baseline']}` frontier",
                "",
                f"- **Reviewed through:** `{closure.get('reviewed_at', '—')}`.",
                f"- **Primary blocking reason:** {baseline.get('blocking_reason', '—')}",
                f"- **Closure claim:** {closure.get('closure_claim', '—')}",
                "- **Evidence depth:**",
            ]
        )
        for key, value in evidence_depth(closure):
            if isinstance(value, list):
                rendered = ", ".join(f"`{item}`" for item in value) if value else "—"
                lines.append(f"  - `{key}`: {rendered}")
            else:
                lines.append(f"  - `{key}`: `{compact_value(value)}`")

        lines.extend(["- **Reopen when:**"])
        for item in closure.get("reopen_when") or []:
            lines.append(f"  1. {item}")

        lines.extend(["- **Do not reopen for:**"])
        for item in closure.get("do_not_reopen_for") or []:
            lines.append(f"  - {item}")

        lines.extend(
            [
                f"- **Non-claim:** {closure.get('non_claim', '—')}",
                f"- **Source:** [`{path.name}`]({rel(path)}).",
            ]
        )

    lines.extend(
        [
            "",
            "## Reading rule",
            "",
            "```text",
            "historical SYNTHESIS.md / experiment-state.json",
            "        = immutable closed-cycle snapshot",
            "",
            "current primary-baselines.json",
            "        +",
            "current S2–S5 function closure records",
            "        ↓",
            "this generated evidence-frontier projection",
            "```",
            "",
            "Function-specific closure schemas remain authoritative. This projection deliberately does not normalize `A`, `C`, `P`, benchmark counts, observation counts, route counts or provenance gates into a scalar maturity/capability score.",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated projection is stale")
    args = parser.parse_args()

    rendered = render()
    if args.check:
        if not OUTPUT.exists():
            raise SystemExit(f"missing generated file: {OUTPUT}")
        current = OUTPUT.read_text(encoding="utf-8")
        if current != rendered:
            raise SystemExit(
                "EVIDENCE-FRONTIER.md is stale; run "
                "python experiments/functional-capability-depth/render_evidence_frontier.py"
            )
        print("Current functional capability evidence frontier is up to date")
        return

    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"wrote {OUTPUT}")


if __name__ == "__main__":
    main()
