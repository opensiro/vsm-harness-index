#!/usr/bin/env python3
"""Fail-closed validator for the LoopX registered-peer S2 preregistration."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
S2 = HERE.parent
ROOT = HERE.parents[3]
PROTOCOL = HERE / "protocol.json"
RUN_TEMPLATE = HERE / "run-template.json"
ASSESSMENT = ROOT / "assessments" / "loopx.md"
OBSERVATIONS = S2 / "observations.json"
PARENT_README = S2 / "README.md"
FIXTURE = HERE / "fixture"
CANONICAL_REF = "ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f"
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)

EXPECTED_METRICS = {
    "treatment_peer_contract_present",
    "control_peer_contract_absent",
    "coordinator_scheduling_classification",
    "distinct_worker_s1_executions_observed",
    "worker_a_start_base_commit",
    "worker_b_start_base_commit",
    "control_concurrent_live_overlap_observed",
    "task_a_isolated_acceptance",
    "task_b_isolated_acceptance",
    "composed_acceptance",
    "worker_b_contract_key",
    "worker_b_started_after_a_integration",
    "worker_b_behavior_changed_between_matched_arms",
    "subsequent_s1_behavior_changed_by_coordination",
}

REQUIRED_FILES = {
    "README.md",
    "protocol.json",
    "run-template.json",
    "fixture/src/envelope.py",
    "fixture/src/retry.py",
    "fixture/task-a.md",
    "fixture/task-b.md",
    "fixture/tests/test_envelope.py",
    "fixture/tests/test_retry.py",
}


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot load {path.relative_to(ROOT)}: {exc}")


def assessment_fields() -> dict[str, str]:
    text = ASSESSMENT.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        fail("LoopX assessment has no front matter")
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def require_text(path: Path, *needles: str) -> None:
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            fail(f"{path.relative_to(ROOT)} lost preregistered text: {needle!r}")


def main() -> None:
    for rel in REQUIRED_FILES:
        if not (HERE / rel).exists():
            fail(f"missing preregistration file: {rel}")

    protocol = load_json(PROTOCOL)
    run_template = load_json(RUN_TEMPLATE)
    observations = load_json(OBSERVATIONS)
    fields = assessment_fields()

    if protocol.get("schema_version") != 1:
        fail("protocol schema_version drift")
    if protocol.get("status") != "preregistered-no-results":
        fail("protocol must remain preregistered-no-results before execution")
    if protocol.get("tracking_issue") != 609:
        fail("tracking issue drift")
    if protocol.get("function") != "S2":
        fail("function must remain S2")
    if protocol.get("canonical_harness_id") != "loopx":
        fail("canonical harness id drift")
    if protocol.get("canonical_assessment_ref") != CANONICAL_REF:
        fail("canonical assessment ref drift")
    if protocol.get("upstream_revision") != CANONICAL_REF:
        fail("upstream revision drift")
    if protocol.get("canonical_state_at_design") != "A":
        fail("canonical S2 state-at-design drift")
    if protocol.get("system_compatibility_target") != "adapter-preserved":
        fail("study must remain adapter-preserved")
    if protocol.get("results") is not None:
        fail("preregistration must not embed results")
    if protocol.get("observation_registry_mutation_allowed") is not False:
        fail("preregistration must forbid observation-registry mutation")

    if fields.get("harness_id") != "loopx" or fields.get("status") != "included":
        fail("canonical LoopX assessment identity/status drift")
    if fields.get("review_ref") != CANONICAL_REF:
        fail("canonical LoopX review_ref changed; this protocol requires review")
    if fields.get("autonomy_s2") != "A":
        fail("canonical LoopX S2 state changed; preregistration requires review")

    parent_text = PARENT_README.read_text(encoding="utf-8")
    if "native or adapter-preserved" not in parent_text:
        fail("parent S2 benchmark contract no longer permits adapter-preserved primary evidence")

    fixture = protocol.get("fixture")
    if not isinstance(fixture, dict):
        fail("fixture object missing")
    if fixture.get("root") != "fixture" or fixture.get("language") != "python":
        fail("fixture root/language drift")
    task_a = fixture.get("task_a")
    task_b = fixture.get("task_b")
    if not isinstance(task_a, dict) or not isinstance(task_b, dict):
        fail("task A/B records missing")
    scopes_a = set(task_a.get("write_scopes") or [])
    scopes_b = set(task_b.get("write_scopes") or [])
    if scopes_a != {"src/envelope.py", "tests/test_envelope.py"}:
        fail(f"Task A write scopes drift: {sorted(scopes_a)!r}")
    if scopes_b != {"src/retry.py", "tests/test_retry.py"}:
        fail(f"Task B write scopes drift: {sorted(scopes_b)!r}")
    if scopes_a & scopes_b:
        fail("Task A/B write scopes must remain disjoint")
    if fixture.get("composed_test") != "fixture/tests/test_retry.py":
        fail("composed test drift")
    selection_rule = str(fixture.get("selection_rule") or "")
    if "must not be replaced or widened" not in selection_rule:
        fail("fixture anti-post-hoc selection rule missing")

    envelope_text = (FIXTURE / "src" / "envelope.py").read_text(encoding="utf-8")
    retry_text = (FIXTURE / "src" / "retry.py").read_text(encoding="utf-8")
    if 'return {"status": status}' not in envelope_text or '"code"' in envelope_text:
        fail("baseline producer must expose only the status key")
    if "return False" not in retry_text:
        fail("baseline retry consumer drift")
    require_text(
        FIXTURE / "task-a.md",
        "status` to the key `code",
        "Do not edit `src/retry.py`",
        "src/envelope.py",
        "tests/test_envelope.py",
    )
    require_text(
        FIXTURE / "task-b.md",
        "response payload contract that is present in the worker's starting tree",
        "Do not edit `src/envelope.py`",
        "src/retry.py",
        "tests/test_retry.py",
    )
    require_text(
        FIXTURE / "tests" / "test_envelope.py",
        '{"code": 200}',
    )
    require_text(
        FIXTURE / "tests" / "test_retry.py",
        "make_response(429)",
        "make_response(503)",
        "make_response(200)",
    )

    organization = protocol.get("organization")
    if not isinstance(organization, dict):
        fail("organization block missing")
    if organization.get("coordinator_agent_id") != "codex-coordinator":
        fail("coordinator identity drift")
    if organization.get("worker_agent_ids") != ["codex-worker-a", "codex-worker-b"]:
        fail("worker identities drift")
    if organization.get("functional_worker_count") != 2:
        fail("functional worker count must remain 2")
    if organization.get("coordinator_counts_as_functional_worker") is not False:
        fail("coordinator must remain outside functional worker count")
    if organization.get("agent_model") != "peer_v1":
        fail("registered peer model drift")

    adapter = protocol.get("adapter_boundary")
    if not isinstance(adapter, dict) or adapter.get("role") != "transport-and-execution-only":
        fail("adapter preservation boundary missing")
    forbidden = "\n".join(adapter.get("forbidden_actions") or [])
    for phrase in (
        "choose parallel versus serial",
        "override or repair the coordinator decision",
        "repair worker code",
        "mutate canonical observations",
    ):
        if phrase not in forbidden:
            fail(f"adapter forbidden-action gate lost: {phrase!r}")

    arms = protocol.get("arms")
    if not isinstance(arms, dict) or set(arms) != {"treatment", "control"}:
        fail("treatment/control arm set drift")
    treatment = arms["treatment"]
    control = arms["control"]
    if treatment.get("id") != "loopx-registered-peer-s2":
        fail("treatment id drift")
    if treatment.get("peer_task_coordinator_configured") is not True:
        fail("treatment must configure peer task coordinator")
    if treatment.get("coordinator_capabilities") != ["peer_agent_activation"]:
        fail("treatment coordinator capability drift")
    if treatment.get("required_contract_schema") != "task_orchestration_contract_v1":
        fail("treatment peer contract schema drift")
    if treatment.get("required_contract_mode") != "task_scoped_peer":
        fail("treatment peer contract mode drift")
    if treatment.get("allowed_scheduling_classifications") != [
        "parallel",
        "a_then_b",
        "b_then_a",
    ]:
        fail("treatment scheduling classification set drift")
    if treatment.get("decision_owner") != "model-driven LoopX task coordinator":
        fail("treatment decision owner drift")

    if control.get("id") != "loopx-peer-s2-ablation":
        fail("control id drift")
    if control.get("peer_task_coordinator_configured") is not False:
        fail("control must not configure peer coordinator")
    if control.get("coordinator_turn_present") is not False:
        fail("control must not run coordinator Turn")
    if control.get("peer_agent_activation_capability_present") is not False:
        fail("control must not report peer_agent_activation")
    if control.get("task_orchestration_contract_allowed") is not False:
        fail("control must reject task-orchestration contract")
    if "concurrent" not in str(control.get("fixed_worker_launch") or ""):
        fail("control fixed concurrent disturbance generator missing")

    execution = protocol.get("execution")
    if not isinstance(execution, dict):
        fail("execution block missing")
    if execution.get("minimum_primary_replicates_per_arm", 0) < 3:
        fail("minimum replicate count must remain at least 3")
    if execution.get("fresh_repo_per_run") is not True:
        fail("fresh repository per run required")
    if execution.get("fresh_worker_worktree_per_execution") is not True:
        fail("fresh worker worktree per execution required")
    if execution.get("integration_order") != ["task_a", "task_b"]:
        fail("deterministic A-then-B integration order drift")
    if len(execution.get("exclusion_rules") or []) < 3:
        fail("exclusion rules missing")

    metrics = protocol.get("primary_metrics")
    if not isinstance(metrics, list) or set(metrics) != EXPECTED_METRICS:
        fail("primary metric set drift")

    gates = protocol.get("pre_execution_identifiability_gates")
    if not isinstance(gates, list) or len(gates) != 7:
        fail("pre-execution identifiability gate drift")
    gate_text = "\n".join(gates)
    for phrase in (
        "write scopes are disjoint",
        "task_scoped_peer",
        "control projects no task-orchestration contract",
        "same two worker Turn surfaces",
        "adapter makes no S2-specific decision",
    ):
        if phrase not in gate_text:
            fail(f"identifiability gate lost requirement: {phrase!r}")

    admission = protocol.get("admission_gate")
    if not isinstance(admission, list) or len(admission) < 6:
        fail("admission gate missing")
    admission_text = "\n".join(admission)
    for phrase in (
        "two distinct worker S1s",
        "model-driven registered-peer S2 decision path",
        "coordination decision changes",
        "no autonomy state",
    ):
        if phrase not in admission_text:
            fail(f"admission gate lost requirement: {phrase!r}")

    if run_template.get("schema_version") != 1:
        fail("run-template schema drift")
    if run_template.get("protocol_status_required") != "preregistered-no-results":
        fail("run-template protocol status drift")
    if run_template.get("tracking_issue") != 609:
        fail("run-template issue drift")
    if run_template.get("loopx_revision") != CANONICAL_REF:
        fail("run-template LoopX revision drift")
    for unset_field in (
        "run_id",
        "arm",
        "replicate",
        "index_protocol_revision",
        "fixture_revision",
        "codex_version",
        "worker_model_id",
        "coordinator_model_id",
        "coordinator_result",
        "coordinator_scheduling_classification",
        "composed_acceptance",
    ):
        if run_template.get(unset_field) is not None:
            fail(f"preregistered run-template must leave {unset_field} unset")
    if run_template.get("excluded") is not False:
        fail("run-template excluded must default false")

    if not isinstance(observations, list):
        fail("S2 observations registry must remain a list")
    loopx_rows = [
        row
        for row in observations
        if isinstance(row, dict) and row.get("canonical_harness_id") == "loopx"
    ]
    if loopx_rows:
        fail("preregistration cannot coexist with an admitted LoopX direct observation")

    print("LoopX registered-peer semantic-contention preregistration validation passed")


if __name__ == "__main__":
    main()
