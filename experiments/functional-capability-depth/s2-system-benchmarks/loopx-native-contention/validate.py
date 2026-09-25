#!/usr/bin/env python3
"""Fail-closed validator for the preregistered LoopX native-S2 study."""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
S2 = HERE.parent
ROOT = HERE.parents[3]
PROTOCOL = HERE / "protocol.json"
RUN_TEMPLATE = HERE / "run-template.json"
EXECUTION_FEASIBILITY = HERE / "execution-feasibility.json"
OBSERVATIONS = S2 / "observations.json"
ASSESSMENT = ROOT / "assessments" / "loopx.md"
FIXTURE = HERE / "fixture"

CANONICAL_REF = "ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f"
EXPECTED_PRIMARY_METRICS = {
    "coordinator_decision",
    "overlapping_work_admitted_concurrently",
    "selected_write_scopes",
    "lease_admission_events",
    "write_scope_conflict_events",
    "stale_or_duplicate_work_events",
    "clean_integration",
    "accepted_task_a",
    "accepted_task_b",
    "subsequent_s1_behavior_changed_by_coordination_feedback",
}
REQUIRED_FILES = {
    "README.md",
    "protocol.json",
    "run-template.json",
    "execution-feasibility.json",
    "NOT_IDENTIFIABLE.md",
    "verify_execution_feasibility.py",
    "fixture/src/dispatch.py",
    "fixture/task-a.md",
    "fixture/task-b.md",
    "fixture/tests/test_request_id.py",
    "fixture/tests/test_retryable.py",
}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def load_json(path: Path):
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
    feasibility = load_json(EXECUTION_FEASIBILITY)
    observations = load_json(OBSERVATIONS)
    fields = assessment_fields()

    if protocol.get("schema_version") != 1:
        fail("LoopX S2 protocol schema_version drift")
    if protocol.get("status") != "preregistered-no-results":
        fail("LoopX S2 protocol must remain preregistered-no-results before execution")
    if protocol.get("tracking_issue") != 602:
        fail("LoopX S2 tracking issue drift")
    if protocol.get("function") != "S2":
        fail("LoopX protocol function must remain S2")
    if protocol.get("canonical_harness_id") != "loopx":
        fail("LoopX canonical_harness_id drift")
    if protocol.get("canonical_assessment_ref") != CANONICAL_REF:
        fail("LoopX canonical assessment ref drift")
    if protocol.get("upstream_revision") != CANONICAL_REF:
        fail("LoopX upstream protocol revision must remain pinned to canonical assessed ref")
    if protocol.get("canonical_state_at_design") != "A":
        fail("LoopX canonical S2 state-at-design drift")
    if protocol.get("native_substrate") != "examples/control_plane/task-lease-runtime-smoke.py":
        fail("LoopX native substrate path drift")
    if protocol.get("results") is not None:
        fail("LoopX preregistration must not embed results")
    if protocol.get("observation_registry_mutation_allowed") is not False:
        fail("LoopX preregistration must forbid observation-registry mutation")

    if fields.get("harness_id") != "loopx" or fields.get("status") != "included":
        fail("canonical LoopX assessment identity/status drift")
    if fields.get("review_ref") != CANONICAL_REF:
        fail("canonical LoopX review_ref changed; create a new-ref protocol review")
    if fields.get("autonomy_s2") != "A":
        fail("canonical LoopX S2 state changed; preregistration requires review")

    fixture = protocol.get("fixture")
    if not isinstance(fixture, dict):
        fail("LoopX protocol fixture object missing")
    if fixture.get("root") != "fixture":
        fail("LoopX fixture root drift")
    if fixture.get("shared_write_surface") != "fixture/src/dispatch.py":
        fail("LoopX shared write surface drift")
    tasks = fixture.get("tasks")
    if not isinstance(tasks, list) or len(tasks) != 2:
        fail("LoopX study requires exactly two frozen tasks")
    expected_tasks = {
        "request-id-propagation": ("fixture/task-a.md", "fixture/tests/test_request_id.py"),
        "retryability-classification": ("fixture/task-b.md", "fixture/tests/test_retryable.py"),
    }
    actual_tasks = {
        row.get("task_id"): (row.get("instruction_file"), row.get("primary_test"))
        for row in tasks
        if isinstance(row, dict)
    }
    if actual_tasks != expected_tasks:
        fail(f"LoopX frozen task set drift: {actual_tasks!r}")
    selection_rule = fixture.get("selection_rule")
    if not isinstance(selection_rule, str) or "must not be replaced" not in selection_rule:
        fail("LoopX task selection anti-post-hoc rule missing")

    dispatch_text = (FIXTURE / "src" / "dispatch.py").read_text(encoding="utf-8")
    if "request_id" in dispatch_text or "retryable" in dispatch_text:
        fail("baseline fixture already contains one of the treatment task features")
    require_text(FIXTURE / "task-a.md", "src/dispatch.py", "Do not implement retryability")
    require_text(FIXTURE / "task-b.md", "src/dispatch.py", "Do not implement request-id")
    require_text(FIXTURE / "tests" / "test_request_id.py", "record.request_id == \"req-123\"")
    require_text(FIXTURE / "tests" / "test_retryable.py", "429", "503", "retryable is True")

    arms = protocol.get("arms")
    if not isinstance(arms, dict) or set(arms) != {"treatment", "control"}:
        fail("LoopX treatment/control arm set drift")
    treatment = arms["treatment"]
    control = arms["control"]
    if treatment.get("id") != "loopx-native-s2":
        fail("LoopX treatment id drift")
    if control.get("id") != "loopx-coordination-ablation":
        fail("LoopX control id drift")
    treatment_requirements = "\n".join(treatment.get("requirements", []))
    control_requirements = "\n".join(control.get("requirements", []))
    for phrase in ("model-driven coordinator", "parallel versus serial", "task-lease/write-scope"):
        if phrase not in treatment_requirements:
            fail(f"LoopX treatment lost agent-owned S2 requirement: {phrase!r}")
    for phrase in ("remove only the S2-specific", "benchmark-authored replacement coordinator", "not-identifiable"):
        if phrase not in control_requirements:
            fail(f"LoopX control lost identifiability guard: {phrase!r}")

    execution = protocol.get("execution")
    if not isinstance(execution, dict):
        fail("LoopX execution contract missing")
    if execution.get("worker_count") != 2:
        fail("LoopX preregistered worker count must remain 2")
    replicates = execution.get("minimum_primary_replicates_per_arm")
    if not isinstance(replicates, int) or replicates < 3:
        fail("LoopX study requires at least three primary replicates per arm")
    if execution.get("fresh_repo_per_run") is not True:
        fail("LoopX study requires a fresh repository per run")
    exclusions = execution.get("exclusion_rules")
    if not isinstance(exclusions, list) or len(exclusions) < 3:
        fail("LoopX exclusion rules missing")

    metrics = protocol.get("primary_metrics")
    if not isinstance(metrics, list) or set(metrics) != EXPECTED_PRIMARY_METRICS:
        fail("LoopX primary metric set drift")

    provenance = protocol.get("provenance_required")
    if not isinstance(provenance, list):
        fail("LoopX provenance requirement list missing")
    for required in {
        "loopx_revision",
        "index_protocol_revision",
        "fixture_revision",
        "model_provider",
        "model_id",
        "coordinator_prompt",
        "worker_prompts",
        "arm_configuration",
        "run_id",
        "raw_artifact_paths",
    }:
        if required not in provenance:
            fail(f"LoopX provenance gate lost field: {required}")

    gate = protocol.get("admission_gate")
    if not isinstance(gate, list) or len(gate) < 6:
        fail("LoopX observation admission gate missing")
    gate_text = "\n".join(gate)
    for phrase in ("distinct S1 workers", "model-driven LoopX S2 decision path", "changes subsequent worker behavior", "public and immutable"):
        if phrase not in gate_text:
            fail(f"LoopX admission gate lost requirement: {phrase!r}")

    if run_template.get("schema_version") != 1:
        fail("LoopX run-template schema drift")
    if run_template.get("protocol_status_required") != "preregistered-no-results":
        fail("LoopX run-template protocol status drift")
    if run_template.get("loopx_revision") != CANONICAL_REF:
        fail("LoopX run-template revision drift")
    if run_template.get("worker_count") != 2:
        fail("LoopX run-template worker count drift")
    for empty_field in (
        "run_id",
        "arm",
        "replicate",
        "index_protocol_revision",
        "fixture_revision",
        "model_provider",
        "model_id",
        "reasoning_configuration",
        "coordinator_decision",
        "clean_integration",
    ):
        if run_template.get(empty_field) is not None:
            fail(f"LoopX preregistration run-template must leave {empty_field} unset")

    if feasibility.get("schema_version") != 1:
        fail("LoopX execution-feasibility schema drift")
    if feasibility.get("status") != "not-identifiable":
        fail("LoopX frozen execution must remain not-identifiable until a new-ref review")
    if feasibility.get("tracking_issue") != 606:
        fail("LoopX execution-feasibility tracking issue drift")
    if feasibility.get("canonical_harness_id") != "loopx":
        fail("LoopX execution-feasibility harness id drift")
    if feasibility.get("canonical_loopx_revision") != CANONICAL_REF:
        fail("LoopX execution-feasibility revision drift")
    if feasibility.get("canonical_s2_state_unchanged") != "A":
        fail("LoopX execution-feasibility must not rewrite canonical S2 state")
    if feasibility.get("protocol_status_unchanged") != "preregistered-no-results":
        fail("LoopX execution-feasibility must not promote protocol status")
    if feasibility.get("reason_code") != "frozen_two_task_overlap_has_no_native_child_topology":
        fail("LoopX execution-feasibility reason drift")
    frozen = feasibility.get("frozen_fixture")
    if frozen != {
        "worker_count": 2,
        "task_a": "fixture/task-a.md",
        "task_b": "fixture/task-b.md",
        "shared_write_surface": "src/dispatch.py",
    }:
        fail("LoopX execution-feasibility no longer describes the frozen pair")
    if feasibility.get("treatment_identifiability", {}).get("identifiable") is not False:
        fail("LoopX treatment identifiability stop was removed")
    if feasibility.get("control_identifiability", {}).get("identifiable") is not False:
        fail("LoopX control identifiability stop was removed")
    expected_effects = {
        "live_model_runs_attempted": False,
        "observations_registry_mutated": False,
        "canonical_assessment_changed": False,
        "capability_result_admitted": False,
        "scalar_s2_score_produced": False,
    }
    if feasibility.get("effects") != expected_effects:
        fail("LoopX feasibility artifact must remain a no-run/non-observation record")
    evidence = feasibility.get("evidence")
    if not isinstance(evidence, list) or len(evidence) != 5:
        fail("LoopX execution-feasibility evidence set drift")
    expected_evidence_paths = {
        "loopx/control_plane/quota/task_orchestration_admission.py",
        "loopx/control_plane/turn_driver/driver.py",
        "tests/control_plane/test_task_orchestration_admission.py",
        "tests/test_loopx_turn_codex_cli.py",
        "docs/integrations/codex-subagent-orchestration.md",
    }
    if {row.get("path") for row in evidence if isinstance(row, dict)} != expected_evidence_paths:
        fail("LoopX execution-feasibility evidence paths drift")
    if any(CANONICAL_REF not in str(row.get("url") or "") for row in evidence if isinstance(row, dict)):
        fail("LoopX execution-feasibility evidence must remain pinned to canonical ref")
    require_text(
        HERE / "NOT_IDENTIFIABLE.md",
        "No live/model run was attempted.",
        "distinct S1 workers",
        "not a negative S2 capability result",
    )
    require_text(
        HERE / "verify_execution_feasibility.py",
        CANONICAL_REF,
        "apply_task_orchestration_contract",
        "child_execution_receipts",
        "spawn_agent",
    )

    if not isinstance(observations, list):
        fail("S2 observations registry must remain a list")
    loopx_observations = [
        row for row in observations
        if isinstance(row, dict) and row.get("canonical_harness_id") == "loopx"
    ]
    if loopx_observations:
        fail("LoopX preregistration cannot coexist with an admitted LoopX observation; execute a new admission transaction")

    print("LoopX native S2 preregistration validation passed")
    print("LoopX native S2 execution feasibility validation passed")


if __name__ == "__main__":
    main()
