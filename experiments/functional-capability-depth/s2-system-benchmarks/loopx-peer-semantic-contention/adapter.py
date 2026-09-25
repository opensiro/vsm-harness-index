#!/usr/bin/env python3
"""Transport-only scheduling helpers for the LoopX peer S2 study.

This module intentionally knows worker identities and frozen schedule tokens only.
It does not inspect fixture source, infer dependencies, repair output, or choose a
treatment schedule independently of the coordinator's typed result.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence


ALLOWED_CLASSIFICATIONS = ("parallel", "a_then_b", "b_then_a")
WORKER_A = "codex-worker-a"
WORKER_B = "codex-worker-b"


class AdapterProtocolError(ValueError):
    """Fail-closed protocol violation at the adapter boundary."""


@dataclass(frozen=True)
class Schedule:
    classification: str
    stages: tuple[tuple[str, ...], ...]

    @property
    def concurrent(self) -> bool:
        return any(len(stage) > 1 for stage in self.stages)


def treatment_schedule(coordinator_result: Mapping[str, Any]) -> Schedule:
    """Map one model-authored classification token to the frozen schedule."""

    classification = coordinator_result.get("classification")
    if classification not in ALLOWED_CLASSIFICATIONS:
        raise AdapterProtocolError(
            "coordinator classification must be exactly one of: "
            + ", ".join(ALLOWED_CLASSIFICATIONS)
        )
    if classification == "parallel":
        stages = ((WORKER_A, WORKER_B),)
    elif classification == "a_then_b":
        stages = ((WORKER_A,), (WORKER_B,))
    else:
        stages = ((WORKER_B,), (WORKER_A,))
    return Schedule(classification=classification, stages=stages)


def control_schedule() -> Schedule:
    """Return the frozen concurrent disturbance generator for the control arm."""

    return Schedule(classification="parallel", stages=((WORKER_A, WORKER_B),))


def worker_turn_command(
    *,
    loopx_command: Sequence[str],
    goal_id: str,
    agent_id: str,
    worktree: Path,
    model_id: str,
    validation_argv: Sequence[str],
) -> tuple[str, ...]:
    """Build the one shared worker Turn surface used by both study arms."""

    if agent_id not in {WORKER_A, WORKER_B}:
        raise AdapterProtocolError(f"unsupported functional worker: {agent_id}")
    if not model_id.strip():
        raise AdapterProtocolError("worker model id must be explicit")
    if not validation_argv:
        raise AdapterProtocolError("worker validation argv must be non-empty")

    import json

    return tuple(loopx_command) + (
        "--format",
        "json",
        "turn",
        "run-once",
        "--goal-id",
        goal_id,
        "--agent-id",
        agent_id,
        "--host",
        "codex-cli",
        "--project",
        str(worktree),
        "--codex-sandbox",
        "workspace-write",
        "--codex-model",
        model_id,
        "--validation-command-json",
        json.dumps(list(validation_argv), separators=(",", ":")),
        "--execute",
    )


def coordinator_turn_command(
    *,
    loopx_command: Sequence[str],
    goal_id: str,
    coordinator_agent_id: str,
    project: Path,
    model_id: str,
    validation_argv: Sequence[str],
) -> tuple[str, ...]:
    """Build the treatment-only read-only coordinator Turn surface."""

    if not validation_argv:
        raise AdapterProtocolError("coordinator validation argv must be non-empty")

    import json

    return tuple(loopx_command) + (
        "--format",
        "json",
        "turn",
        "run-once",
        "--goal-id",
        goal_id,
        "--agent-id",
        coordinator_agent_id,
        "--available-capability",
        "peer_agent_activation",
        "--host",
        "codex-cli",
        "--project",
        str(project),
        "--codex-sandbox",
        "read-only",
        "--codex-model",
        model_id,
        "--validation-command-json",
        json.dumps(list(validation_argv), separators=(",", ":")),
        "--execute",
    )
