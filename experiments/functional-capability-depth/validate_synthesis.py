#!/usr/bin/env python3
"""Fail-closed validator for the historical functional-capability-depth synthesis."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
STATE_PATH = HERE / "experiment-state.json"
SYNTHESIS_PATH = HERE / "SYNTHESIS.md"
EXPERIMENT_REL = Path("experiments/functional-capability-depth")

FUNCTIONS = ("S1", "S2", "S3", "S3*", "S4", "S5")
GAP_FUNCTIONS = ("S2", "S3", "S3*", "S4", "S5")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def git_text(revision: str, relpath: Path) -> str:
    spec = f"{revision}:{relpath.as_posix()}"
    try:
        result = subprocess.run(
            ["git", "show", spec],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        detail = exc.stderr.strip() or exc.stdout.strip() or "unknown git show error"
        raise SystemExit(f"cannot read historical synthesis input {spec}: {detail}") from exc
    return result.stdout


def historical_json(revision: str, relpath: Path):
    return json.loads(git_text(revision, relpath))


def require_ancestor(revision: str) -> None:
    result = subprocess.run(
        ["git", "merge-base", "--is-ancestor", revision, "HEAD"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    require(result.returncode == 0, f"cycle input revision is not an ancestor of HEAD: {revision}")


def pinned_url(revision: str, relpath: Path) -> str:
    return (
        "https://github.com/opensiro/vsm-harness-index/blob/"
        f"{revision}/{relpath.as_posix()}"
    )


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
synthesis = SYNTHESIS_PATH.read_text(encoding="utf-8")

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
require(set(state["functions"]) == set(FUNCTIONS), "experiment-state function set drift")
require(
    state["separate_evidence_class"] == "self-organizing/adaptive-S",
    "self-organizing/adaptive-S separation drift",
)

revision = state.get("cycle_input_revision")
require(
    isinstance(revision, str) and len(revision) == 40,
    "experiment-state must pin a full cycle_input_revision",
)
require_ancestor(revision)

baselines_rel = EXPERIMENT_REL / "primary-baselines.json"
public_evidence_rel = EXPERIMENT_REL / "PUBLIC-EVIDENCE.md"
baselines = historical_json(revision, baselines_rel)
# Resolve the historical contract as an immutable input even though its content
# is not duplicated into the cycle state.
git_text(revision, public_evidence_rel)

require(
    state["selection_gate"] == baselines["selection_gate"],
    "experiment-state selection gate drift from pinned primary-baselines.json",
)
primary_functions = baselines["functions"]
require(set(primary_functions) == set(FUNCTIONS), "pinned primary-baselines function set drift")

s1_state = state["functions"]["S1"]
s1_primary = primary_functions["S1"]
require(s1_state["status"] == "selected", "S1 synthesis state must remain selected")
require(s1_primary["status"] == "selected", "pinned S1 primary status drift")
require(
    s1_state["primary"] == s1_primary["primary"]["benchmark_name"],
    "S1 selected primary drift from pinned inputs",
)
require(
    s1_state["reference_model"] == s1_primary["primary"]["reference_model"],
    "S1 reference model drift from pinned inputs",
)
require(
    s1_state["comparison_design"] == s1_primary["primary"]["comparison_design"],
    "S1 comparison design drift from pinned inputs",
)

for function in GAP_FUNCTIONS:
    function_state = state["functions"][function]
    require(
        function_state["status"] == "evidence-backed-gap",
        f"{function} experiment-state disposition drift",
    )
    require(
        primary_functions[function]["status"] == "gap",
        f"{function} pinned primary state no longer matches the historical synthesis",
    )

    closure_rel = EXPERIMENT_REL / function_state["closure"]
    closure = historical_json(revision, closure_rel)

    require(closure["schema_version"] == 1, f"{function} pinned closure schema_version drift")
    require(
        closure["status"] == "experimental-non-normative",
        f"{function} pinned closure status drift",
    )
    require(
        closure["disposition"] == function_state["status"],
        f"{function} pinned closure disposition drift from experiment-state",
    )
    require(closure["primary_baseline"] == "gap", f"{function} pinned closure must record a gap")
    require(
        closure["closure_scope"] == "current-public-evidence",
        f"{function} pinned closure scope drift",
    )
    require(
        closure["reviewed_at"] == state["reviewed_at"],
        f"{function} pinned closure review date drift from research-cycle snapshot",
    )
    require(
        isinstance(closure.get("reopen_when"), list) and closure["reopen_when"],
        f"{function} pinned closure lost explicit reopen conditions",
    )
    require(
        isinstance(closure.get("do_not_reopen_for"), list) and closure["do_not_reopen_for"],
        f"{function} pinned closure lost anti-churn conditions",
    )
    require(closure.get("non_claim"), f"{function} pinned closure lost non-claim boundary")

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
    revision in synthesis,
    "SYNTHESIS.md must expose the immutable cycle input revision",
)
require(
    pinned_url(revision, public_evidence_rel) in synthesis,
    "SYNTHESIS.md must pin the historical public-evidence contract",
)
for function in GAP_FUNCTIONS:
    closure_rel = EXPERIMENT_REL / state["functions"][function]["closure"]
    require(
        pinned_url(revision, closure_rel) in synthesis,
        f"SYNTHESIS.md must pin the historical {function} closure record",
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

print("historical functional capability synthesis validation passed")
