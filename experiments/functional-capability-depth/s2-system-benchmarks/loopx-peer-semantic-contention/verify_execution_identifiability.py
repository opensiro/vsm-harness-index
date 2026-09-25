#!/usr/bin/env python3
"""Verify the seven preregistered LoopX peer-S2 identifiability gates.

Default mode is deterministic and model-free for CI. Optional --loopx-checkout
imports the exact pinned upstream checkout and replays the registered-peer quota
projection with LoopX's own code. Neither mode invokes Codex or another model.
"""

from __future__ import annotations

import argparse
import importlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parent
S2 = HERE.parent
ROOT = HERE.parents[3]
FAKE = HERE / "fake-artifacts"
PROTOCOL = HERE / "protocol.json"
PLAN = HERE / "execution-plan.json"
OBSERVATIONS = S2 / "observations.json"
ADAPTER = HERE / "adapter.py"
CANONICAL_REF = "ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f"
COORDINATOR = "codex-coordinator"
WORKER_A = "codex-worker-a"
WORKER_B = "codex-worker-b"
GOAL_ID = "loopx-peer-semantic-contention"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_adapter():
    spec = importlib.util.spec_from_file_location("loopx_peer_s2_adapter", ADAPTER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load adapter module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def normalized_worker_surface(command: tuple[str, ...]) -> tuple[str, ...]:
    values = list(command)
    for flag in ("--agent-id", "--project"):
        index = values.index(flag)
        values[index + 1] = f"<{flag[2:].upper()}>"
    return tuple(values)


def static_proof() -> dict[str, Any]:
    protocol = load_json(PROTOCOL)
    plan = load_json(PLAN)
    observations = load_json(OBSERVATIONS)
    adapter = load_adapter()

    assert protocol["status"] == "preregistered-no-results"
    assert protocol["results"] is None
    assert protocol["observation_registry_mutation_allowed"] is False
    assert protocol["upstream_revision"] == CANONICAL_REF
    assert protocol["system_compatibility_target"] == "adapter-preserved"
    assert plan["status"] == "execution-harness-no-live-runs"
    assert plan["loopx_revision"] == CANONICAL_REF
    assert plan["live_execution_default"] is False
    assert plan["ci_live_execution_allowed"] is False
    assert all(value is False for value in plan["effects"].values())

    task_a_scopes = set(protocol["fixture"]["task_a"]["write_scopes"])
    task_b_scopes = set(protocol["fixture"]["task_b"]["write_scopes"])
    assert task_a_scopes
    assert task_b_scopes
    assert task_a_scopes.isdisjoint(task_b_scopes)

    treatment_projection = load_json(FAKE / "treatment-peer-projection.json")
    contract = treatment_projection["task_orchestration_contract"]
    assert treatment_projection["effective_action"] == "coordinate_task_bundle"
    assert contract["schema_version"] == "task_orchestration_contract_v1"
    assert contract["mode"] == "task_scoped_peer"
    assert contract["coordinator_agent_id"] == COORDINATOR
    assert contract["execution_state"] == "ready"
    assert {
        (lane["agent_id"], lane["todo_id"])
        for lane in contract["eligible_peer_lanes"]
    } == {
        (WORKER_A, "todo-task-a"),
        (WORKER_B, "todo-task-b"),
    }

    control_projection = load_json(FAKE / "control-projection.json")
    assert "task_orchestration_contract" not in control_projection
    assert control_projection["effective_action"] != "coordinate_task_bundle"

    expected_stages = {
        "parallel": ((WORKER_A, WORKER_B),),
        "a_then_b": ((WORKER_A,), (WORKER_B,)),
        "b_then_a": ((WORKER_B,), (WORKER_A,)),
    }
    for filename, classification in (
        ("coordinator-parallel.json", "parallel"),
        ("coordinator-a-then-b.json", "a_then_b"),
        ("coordinator-b-then-a.json", "b_then_a"),
    ):
        result = load_json(FAKE / filename)
        schedule = adapter.treatment_schedule(result)
        assert schedule.classification == classification
        assert schedule.stages == expected_stages[classification]
    try:
        adapter.treatment_schedule(load_json(FAKE / "coordinator-invalid.json"))
    except adapter.AdapterProtocolError:
        pass
    else:
        raise AssertionError("invalid coordinator classification did not fail closed")
    assert adapter.control_schedule().stages == ((WORKER_A, WORKER_B),)

    loopx_command = ("python", "-m", "loopx")
    common = {
        "loopx_command": loopx_command,
        "goal_id": GOAL_ID,
        "model_id": "fake-model",
        "validation_argv": ("python", "validate-worker.py"),
    }
    worker_a = adapter.worker_turn_command(
        agent_id=WORKER_A,
        worktree=Path("/tmp/a"),
        **common,
    )
    worker_b = adapter.worker_turn_command(
        agent_id=WORKER_B,
        worktree=Path("/tmp/b"),
        **common,
    )
    assert normalized_worker_surface(worker_a) == normalized_worker_surface(worker_b)
    for command in (worker_a, worker_b):
        assert "turn" in command and "run-once" in command
        assert "--host" in command and "codex-cli" in command
        assert "--codex-sandbox" in command and "workspace-write" in command
        assert "--execute" in command

    coordinator_command = adapter.coordinator_turn_command(
        loopx_command=loopx_command,
        goal_id=GOAL_ID,
        coordinator_agent_id=COORDINATOR,
        project=Path("/tmp/coordinator"),
        model_id="fake-model",
        validation_argv=("python", "validate-coordinator.py"),
    )
    assert "peer_agent_activation" in coordinator_command
    assert "read-only" in coordinator_command

    adapter_source = ADAPTER.read_text(encoding="utf-8")
    for forbidden in (
        "src/envelope.py",
        "src/retry.py",
        '"status"',
        '"code"',
        "read_text(",
        "open(",
    ):
        assert forbidden not in adapter_source, forbidden

    worker_a_receipt = load_json(FAKE / "worker-a-receipt.json")
    worker_b_receipt = load_json(FAKE / "worker-b-receipt.json")
    assert worker_a_receipt["agent_id"] == WORKER_A
    assert worker_b_receipt["agent_id"] == WORKER_B
    assert worker_a_receipt["isolated_acceptance"] is True
    assert worker_b_receipt["isolated_acceptance"] is True

    matched = load_json(FAKE / "matched-pair-a-then-b.json")
    assert matched["scalar_s2_score"] is None
    assert matched["treatment"]["worker_a_start_base_commit"] == "baseline-commit"
    assert matched["treatment"]["worker_b_start_base_commit"] == "after-a-commit"
    assert matched["control"]["worker_a_start_base_commit"] == "baseline-commit"
    assert matched["control"]["worker_b_start_base_commit"] == "baseline-commit"
    assert matched["control"]["control_concurrent_live_overlap_observed"] is True

    loopx_observations = [
        row
        for row in observations
        if isinstance(row, dict) and row.get("canonical_harness_id") == "loopx"
    ]
    assert loopx_observations == []

    return {
        "status": "identifiable-for-local-live-harness",
        "gates": {
            "disjoint_write_scopes": True,
            "ordinary_worker_turn_surfaces": True,
            "treatment_native_peer_contract": True,
            "control_no_peer_contract": True,
            "same_worker_turn_builder": True,
            "pure_classification_to_schedule_mapping": True,
            "no_task_semantic_schedule_logic": True,
        },
        "live_model_runs_attempted": False,
        "observation_admitted": False,
        "scalar_s2_score": None,
    }


def git_head(checkout: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"],
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git rev-parse failed")
    return result.stdout.strip()


def canonical_payload(*, peer_coordinator: bool) -> dict[str, Any]:
    peers = [COORDINATOR, WORKER_A, WORKER_B]
    coordination: dict[str, Any] = {
        "agent_model": "peer_v1",
        "registered_agents": peers,
    }
    if peer_coordinator:
        coordination["peer_task_coordination"] = {
            "coordinator_agent_id": COORDINATOR,
        }
    todos = [
        {
            "index": 1,
            "status": "open",
            "todo_id": "todo-coordinator",
            "task_class": "advancement_task",
            "priority": "P0",
            "text": "Choose the frozen scheduling classification.",
            "claimed_by": COORDINATOR,
        },
        {
            "index": 2,
            "status": "open",
            "todo_id": "todo-task-a",
            "task_class": "advancement_task",
            "priority": "P0",
            "text": "Execute frozen Task A.",
            "claimed_by": WORKER_A,
        },
        {
            "index": 3,
            "status": "open",
            "todo_id": "todo-task-b",
            "task_class": "advancement_task",
            "priority": "P0",
            "text": "Execute frozen Task B.",
            "claimed_by": WORKER_B,
        },
    ]
    quota = {
        "compute": 1.0,
        "window_hours": 24,
        "slot_minutes": 1,
        "allowed_slots": 1440,
        "spent_slots": 0,
    }
    goal = {
        "id": GOAL_ID,
        "status": "active",
        "registry_member": True,
        "adapter_kind": "read_only_project_map_v0",
        "adapter_status": "connected-read-only",
        "quota": quota,
        "coordination": coordination,
    }
    attention = {
        "goal_id": GOAL_ID,
        "status": "state_refreshed",
        "waiting_on": "codex",
        "severity": "action",
        "source": "fixture",
        "recommended_action": "advance the frozen semantic-contention study",
        "coordination": coordination,
        "quota": {**quota, "state": "eligible", "reason": "eligible fixture"},
        "agent_todos": {
            "schema_version": "todo_summary_v0",
            "source_section": "Agent Todo",
            "total": len(todos),
            "open": len(todos),
            "done": 0,
            "items": todos,
        },
    }
    return {
        "ok": True,
        "attention_queue": {"items": [attention]},
        "run_history": {"goals": [goal]},
        "agent_management_projection": {
            "schema_version": "agent_management_projection_v0",
            "agents": [
                {
                    "agent_id": agent_id,
                    "state": "running",
                    "last_activity_at": "2026-09-25T12:00:00Z",
                }
                for agent_id in peers
            ],
        },
    }


def dynamic_proof(loopx_checkout: Path) -> dict[str, Any]:
    checkout = loopx_checkout.expanduser().resolve()
    if git_head(checkout) != CANONICAL_REF:
        raise ValueError(f"LoopX checkout HEAD must equal {CANONICAL_REF}")
    sys.path.insert(0, str(checkout))
    try:
        quota = importlib.import_module("loopx.quota")
        build_quota_should_run = quota.build_quota_should_run

        treatment = build_quota_should_run(
            canonical_payload(peer_coordinator=True),
            goal_id=GOAL_ID,
            agent_id=COORDINATOR,
            available_capabilities=["peer_agent_activation"],
        )
        contract = treatment["task_orchestration_contract"]
        assert treatment["effective_action"] == "coordinate_task_bundle"
        assert contract["schema_version"] == "task_orchestration_contract_v1"
        assert contract["mode"] == "task_scoped_peer"
        assert {
            lane["agent_id"] for lane in contract["eligible_peer_lanes"]
        } == {WORKER_A, WORKER_B}

        control_decisions = {
            agent_id: build_quota_should_run(
                canonical_payload(peer_coordinator=False),
                goal_id=GOAL_ID,
                agent_id=agent_id,
            )
            for agent_id in (WORKER_A, WORKER_B)
        }
        assert all(
            "task_orchestration_contract" not in decision
            for decision in control_decisions.values()
        )
        assert all(
            decision["effective_action"] != "coordinate_task_bundle"
            for decision in control_decisions.values()
        )
        return {
            "loopx_head": CANONICAL_REF,
            "treatment_contract": "task_orchestration_contract_v1/task_scoped_peer",
            "treatment_peer_lanes": sorted([WORKER_A, WORKER_B]),
            "control_contract_absent": True,
            "live_model_runs_attempted": False,
        }
    finally:
        try:
            sys.path.remove(str(checkout))
        except ValueError:
            pass


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--loopx-checkout", type=Path)
    args = parser.parse_args()
    result: dict[str, Any] = {
        "schema_version": 1,
        "static": static_proof(),
        "dynamic": None,
    }
    if args.loopx_checkout is not None:
        result["dynamic"] = dynamic_proof(args.loopx_checkout)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
