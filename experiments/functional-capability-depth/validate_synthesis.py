#!/usr/bin/env python3
"""Fail-closed validator for the functional-capability-depth research-cycle synthesis."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE_PATH = HERE / "experiment-state.json"
SYNTHESIS_PATH = HERE / "SYNTHESIS.md"
BASELINES_PATH = HERE / "primary-baselines.json"
PUBLIC_EVIDENCE_PATH = HERE / "PUBLIC-EVIDENCE.md"

FUNCTIONS = ("S1", "S2", "S3", "S3*", "S4", "S5")
GAP_FUNCTIONS = ("S2", "S3", "S3*", "S4", "S5")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def function_state_table(state: dict) -> str:
    s1 = state["functions"]["S1"]
    rows = [
        "<!-- BEGIN FUNCTION STATE -->",
        "| Function | Cycle result | Primary / evidence state |",
        "| --- | --- | --- |",
        f"| S1 | `{s1['status']}` | {s1['primary']} / `{s1['reference_model']}` |",
    ]
    for function in GAP_FUNCTIONS:
        rows.append(
            f"| {function} | `{state['functions'][function]['status']}` | "
            "no matched canonical-harness primary |"
        )
    rows.append("<!-- END FUNCTION STATE -->")
    return "\n".join(rows)


state = load_json(STATE_PATH)
baselines = load_json(BASELINES_PATH)
synthesis = SYNTHESIS_PATH.read_text(encoding="utf-8")

require(PUBLIC_EVIDENCE_PATH.is_file(), "public-evidence contract is missing")
require(state["schema_version"] == 1, "experiment-state schema_version drift")
require(state["status"] == "experimental-non-normative", "experiment-state status drift")
require(state["tracking_issue"] == 571, "experiment-state tracking issue drift")
require(
    state["research_cycle_disposition"] == "complete-current-public-evidence",
    "research-cycle disposition drift",
)
require(state["evidence_model"] == "public-evidence-first", "evidence model drift")
require(
    state["opensiro_owned_execution_required"] is False,
    "Opensiro-owned execution must remain optional for this cycle",
)
require(
    state["selection_gate"] == baselines["selection_gate"],
    "experiment-state selection gate drift from primary-baselines.json",
)
require(set(state["functions"]) == set(FUNCTIONS), "experiment-state function set drift")
require(
    state["separate_evidence_class"] == "self-organizing/adaptive-S",
    "self-organizing/adaptive-S separation drift",
)

primary_functions = baselines["functions"]
require(set(primary_functions) == set(FUNCTIONS), "primary-baselines function set drift")

s1_state = state["functions"]["S1"]
s1_primary = primary_functions["S1"]
require(s1_state["status"] == "selected", "S1 synthesis state must remain selected")
require(s1_primary["status"] == "selected", "S1 primary-baselines status drift")
require(
    s1_state["primary"] == s1_primary["primary"]["benchmark_name"],
    "S1 selected primary drift",
)
require(
    s1_state["reference_model"] == s1_primary["primary"]["reference_model"],
    "S1 reference model drift",
)
require(
    s1_state["comparison_design"] == s1_primary["primary"]["comparison_design"],
    "S1 comparison design drift",
)

for function in GAP_FUNCTIONS:
    function_state = state["functions"][function]
    require(
        function_state["status"] == "evidence-backed-gap",
        f"{function} experiment-state disposition drift",
    )
    require(
        primary_functions[function]["status"] == "gap",
        f"{function} primary was selected without reopening this research-cycle synthesis",
    )

    closure_path = HERE / function_state["closure"]
    require(closure_path.is_file(), f"{function} closure record is missing: {closure_path}")
    closure = load_json(closure_path)

    require(closure["schema_version"] == 1, f"{function} closure schema_version drift")
    require(
        closure["status"] == "experimental-non-normative",
        f"{function} closure status drift",
    )
    require(
        closure["disposition"] == function_state["status"],
        f"{function} closure disposition drift from experiment-state",
    )
    require(closure["primary_baseline"] == "gap", f"{function} closure no longer records a gap")
    require(
        closure["closure_scope"] == "current-public-evidence",
        f"{function} closure scope drift",
    )
    require(
        closure["reviewed_at"] == state["reviewed_at"],
        f"{function} closure review date drift from this research-cycle snapshot",
    )
    require(
        isinstance(closure.get("reopen_when"), list) and closure["reopen_when"],
        f"{function} closure lost explicit reopen conditions",
    )
    require(
        isinstance(closure.get("do_not_reopen_for"), list) and closure["do_not_reopen_for"],
        f"{function} closure lost anti-churn conditions",
    )
    require(closure.get("non_claim"), f"{function} closure lost non-claim boundary")

expected_table = function_state_table(state)
require(
    expected_table in synthesis,
    "SYNTHESIS.md function-state table drift from experiment-state.json",
)
require(
    "[`experiment-state.json`](experiment-state.json)" in synthesis,
    "SYNTHESIS.md must link the machine-readable experiment state",
)
require(
    "[`PUBLIC-EVIDENCE.md`](PUBLIC-EVIDENCE.md)" in synthesis,
    "SYNTHESIS.md must link the public-evidence contract",
)
for function in GAP_FUNCTIONS:
    closure_rel = state["functions"][function]["closure"]
    require(
        f"({closure_rel})" in synthesis,
        f"SYNTHESIS.md must link the {function} closure record",
    )

required_claim_fragments = (
    "Ownership and capability are separate variables",
    "Capability evidence does not require Opensiro to operate the benchmark",
    "Direct functional evidence is not automatically canonical-native evidence",
    "Canonical-native evidence is not automatically a matched primary",
    "A fail-closed gap is an empirical result",
    "Self-organizing `S` remains a separate evidence class",
)
for fragment in required_claim_fragments:
    require(fragment in synthesis, f"SYNTHESIS.md lost required conclusion: {fragment}")

print("functional capability synthesis validation passed")
