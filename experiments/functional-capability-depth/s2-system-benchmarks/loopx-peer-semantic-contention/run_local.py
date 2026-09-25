#!/usr/bin/env python3
"""Local-only runner for the preregistered LoopX peer semantic-contention study.

Without --execute-live this command performs preflight and emits a side-effect-free
plan. Real Codex execution requires the explicit flag, an exact pinned LoopX
checkout, and a caller-provided output directory. CI must never pass that flag.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable, Sequence


HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixture"
PROTOCOL = HERE / "protocol.json"
OBSERVATIONS = HERE.parent / "observations.json"
COORDINATOR_VALIDATOR = HERE / "validate_coordinator_result.py"
CANONICAL_REF = "ade21106b4bc31a9bc4e61d2f5809b1b4d04d14f"
GOAL_ID = "loopx-peer-semantic-contention"
COORDINATOR = "codex-coordinator"
WORKER_A = "codex-worker-a"
WORKER_B = "codex-worker-b"


def load_adapter():
    import importlib.util

    path = HERE / "adapter.py"
    spec = importlib.util.spec_from_file_location("loopx_peer_s2_adapter_live", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load adapter")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def run(
    argv: Sequence[str],
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        list(argv),
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    if check and result.returncode != 0:
        raise RuntimeError(
            f"command failed ({result.returncode}): {' '.join(argv)}\n"
            f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}"
        )
    return result


def parse_json_output(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if not stripped:
        raise ValueError("command returned empty JSON output")
    try:
        payload = json.loads(stripped)
        if isinstance(payload, dict):
            return payload
    except json.JSONDecodeError:
        pass
    for line in reversed(stripped.splitlines()):
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            return payload
    raise ValueError("command did not return one recoverable JSON object")


def git_head(path: Path) -> str:
    return run(["git", "-C", str(path), "rev-parse", "HEAD"]).stdout.strip()


def fixture_digest() -> str:
    digest = hashlib.sha256()
    for path in sorted(p for p in FIXTURE.rglob("*") if p.is_file()):
        digest.update(str(path.relative_to(FIXTURE)).encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return "sha256:" + digest.hexdigest()


def protocol_preflight() -> dict[str, Any]:
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    observations = json.loads(OBSERVATIONS.read_text(encoding="utf-8"))
    if protocol.get("status") != "preregistered-no-results":
        raise RuntimeError("protocol is no longer preregistered-no-results")
    if protocol.get("results") is not None:
        raise RuntimeError("protocol already contains results")
    if protocol.get("upstream_revision") != CANONICAL_REF:
        raise RuntimeError("protocol LoopX revision drift")
    if any(
        isinstance(row, dict) and row.get("canonical_harness_id") == "loopx"
        for row in observations
    ):
        raise RuntimeError("LoopX observation already admitted; stop before live execution")
    scopes_a = set(protocol["fixture"]["task_a"]["write_scopes"])
    scopes_b = set(protocol["fixture"]["task_b"]["write_scopes"])
    if not scopes_a.isdisjoint(scopes_b):
        raise RuntimeError("frozen worker write scopes are no longer disjoint")
    return {
        "protocol_status": protocol["status"],
        "fixture_digest": fixture_digest(),
        "observations_unchanged": True,
    }


def live_preflight(loopx_checkout: Path) -> dict[str, Any]:
    checkout = loopx_checkout.expanduser().resolve()
    if git_head(checkout) != CANONICAL_REF:
        raise RuntimeError(f"LoopX checkout HEAD must equal {CANONICAL_REF}")
    codex = shutil.which("codex")
    if not codex:
        raise RuntimeError("codex executable is not on PATH")
    version = run([codex, "--version"]).stdout.strip()
    if not version:
        raise RuntimeError("codex --version returned no version")
    return {
        "loopx_checkout": str(checkout),
        "loopx_head": CANONICAL_REF,
        "codex_executable": codex,
        "codex_version": version,
    }


def loopx_env(loopx_checkout: Path) -> dict[str, str]:
    env = dict(os.environ)
    prior = env.get("PYTHONPATH")
    env["PYTHONPATH"] = str(loopx_checkout) + (os.pathsep + prior if prior else "")
    return env


def loopx_prefix(runtime_root: Path) -> tuple[str, ...]:
    return (
        sys.executable,
        "-m",
        "loopx",
        "--runtime-root",
        str(runtime_root),
    )


def run_loopx_json(
    prefix: Sequence[str],
    args: Sequence[str],
    *,
    cwd: Path,
    env: dict[str, str],
) -> dict[str, Any]:
    result = run(tuple(prefix) + ("--format", "json") + tuple(args), cwd=cwd, env=env)
    return parse_json_output(result.stdout)


def init_fixture_repo(root: Path) -> str:
    shutil.copytree(FIXTURE, root)
    (root / ".gitignore").write_text(
        ".loopx/\n.codex/goals/\n.local/\n",
        encoding="utf-8",
    )
    run(["git", "init", "-q"], cwd=root)
    run(["git", "config", "user.name", "Opensiro Experiment"], cwd=root)
    run(["git", "config", "user.email", "founders@opensiro.com"], cwd=root)
    run(["git", "add", "."], cwd=root)
    run(["git", "commit", "-q", "-m", "fixture: frozen baseline"], cwd=root)
    return git_head(root)


def bootstrap_loopx(
    *,
    root: Path,
    prefix: Sequence[str],
    env: dict[str, str],
    arm: str,
) -> dict[str, str]:
    run_loopx_json(
        prefix,
        (
            "bootstrap",
            "--project",
            ".",
            "--goal-id",
            GOAL_ID,
            "--objective",
            "Execute the frozen LoopX peer semantic-contention experiment exactly as preregistered.",
            "--adapter-kind",
            "read_only_project_map_v0",
            "--adapter-status",
            "connected-read-only",
        ),
        cwd=root,
        env=env,
    )
    run_loopx_json(
        prefix,
        (
            "configure-goal",
            "--goal-id",
            GOAL_ID,
            "--write-scope",
            "src/**",
            "--write-scope",
            "tests/**",
            "--execute",
        ),
        cwd=root,
        env=env,
    )
    for agent_id in (COORDINATOR, WORKER_A, WORKER_B):
        run_loopx_json(
            prefix,
            (
                "register-agent",
                "--goal-id",
                GOAL_ID,
                "--agent-id",
                agent_id,
                "--require-new",
                "--execute",
            ),
            cwd=root,
            env=env,
        )
    if arm == "treatment":
        run_loopx_json(
            prefix,
            (
                "configure-goal",
                "--goal-id",
                GOAL_ID,
                "--peer-task-coordinator",
                COORDINATOR,
                "--execute",
            ),
            cwd=root,
            env=env,
        )

    todo_specs = (
        (
            COORDINATOR,
            "Read task-a.md and task-b.md. Choose exactly one schedule token: parallel, a_then_b, or b_then_a. Return that token only in the typed classification field. Do not edit repository files.",
            (),
        ),
        (
            WORKER_A,
            "Read task-a.md and execute frozen Task A exactly. Do not perform Task B.",
            ("src/envelope.py", "tests/test_envelope.py"),
        ),
        (
            WORKER_B,
            "Read task-b.md and execute frozen Task B exactly against the current starting tree. Do not perform Task A.",
            ("src/retry.py", "tests/test_retry.py"),
        ),
    )
    todo_ids: dict[str, str] = {}
    for agent_id, text, scopes in todo_specs:
        args: list[str] = [
            "todo",
            "add",
            "--goal-id",
            GOAL_ID,
            "--role",
            "agent",
            "--text",
            text,
            "--claimed-by",
            agent_id,
            "--task-class",
            "advancement_task",
            "--action-kind",
            "implement" if agent_id != COORDINATOR else "coordinate",
        ]
        for scope in scopes:
            args.extend(["--required-write-scope", scope])
        added = run_loopx_json(prefix, args, cwd=root, env=env)
        todo_id = str(added.get("todo_id") or "")
        if not todo_id:
            raise RuntimeError(f"LoopX todo add did not return todo_id for {agent_id}")
        todo_ids[agent_id] = todo_id
    return todo_ids


def make_worktree(root: Path, path: Path, base_commit: str) -> None:
    run(["git", "-C", str(root), "worktree", "add", "--detach", str(path), base_commit])


def capture_patch(worktree: Path, base_commit: str, destination: Path) -> None:
    result = run(
        ["git", "-C", str(worktree), "diff", "--binary", base_commit, "--"],
        check=True,
    )
    destination.write_text(result.stdout, encoding="utf-8")


def apply_patch_and_commit(root: Path, patch: Path, message: str) -> str:
    if patch.stat().st_size == 0:
        raise RuntimeError(f"worker produced an empty patch: {patch.name}")
    run(["git", "apply", "--index", str(patch)], cwd=root)
    run(["git", "commit", "-q", "-m", message], cwd=root)
    return git_head(root)


def find_classifications(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        classification = value.get("classification")
        if isinstance(classification, str):
            found.add(classification)
        for child in value.values():
            found.update(find_classifications(child))
    elif isinstance(value, list):
        for child in value:
            found.update(find_classifications(child))
    return found


def task_validation(agent_id: str) -> tuple[str, ...]:
    if agent_id == WORKER_A:
        code = "from src.envelope import make_response; assert make_response(200) == {'code': 200}"
    elif agent_id == WORKER_B:
        code = (
            "from src.envelope import make_response; from src.retry import should_retry; "
            "assert should_retry(make_response(429)) is True; "
            "assert should_retry(make_response(503)) is True; "
            "assert should_retry(make_response(200)) is False"
        )
    else:
        raise ValueError(agent_id)
    return (sys.executable, "-c", code)


def run_worker(
    *,
    adapter: Any,
    prefix: Sequence[str],
    env: dict[str, str],
    agent_id: str,
    worktree: Path,
    model_id: str,
    output_path: Path,
) -> dict[str, Any]:
    command = adapter.worker_turn_command(
        loopx_command=prefix,
        goal_id=GOAL_ID,
        agent_id=agent_id,
        worktree=worktree,
        model_id=model_id,
        validation_argv=task_validation(agent_id),
    )
    result = run(command, cwd=worktree, env=env, check=False)
    output_path.write_text(
        json.dumps(
            {
                "argv": list(command),
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    payload = parse_json_output(result.stdout) if result.stdout.strip() else {}
    return {
        "returncode": result.returncode,
        "payload": payload,
        "command": list(command),
    }


def run_coordinator(
    *,
    adapter: Any,
    prefix: Sequence[str],
    env: dict[str, str],
    root: Path,
    model_id: str,
    output_path: Path,
) -> dict[str, Any]:
    command = adapter.coordinator_turn_command(
        loopx_command=prefix,
        goal_id=GOAL_ID,
        coordinator_agent_id=COORDINATOR,
        project=root,
        model_id=model_id,
        validation_argv=(sys.executable, str(COORDINATOR_VALIDATOR)),
    )
    result = run(command, cwd=root, env=env, check=False)
    output_path.write_text(
        json.dumps(
            {
                "argv": list(command),
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    payload = parse_json_output(result.stdout) if result.stdout.strip() else {}
    classifications = find_classifications(payload)
    allowed = classifications.intersection(adapter.ALLOWED_CLASSIFICATIONS)
    if len(allowed) != 1:
        raise adapter.AdapterProtocolError(
            f"coordinator output did not expose exactly one allowed classification: {sorted(classifications)}"
        )
    classification = next(iter(allowed))
    return {
        "returncode": result.returncode,
        "payload": payload,
        "classification": classification,
    }


def execute_arm(
    *,
    arm: str,
    loopx_checkout: Path,
    model_id: str,
    output_dir: Path,
) -> dict[str, Any]:
    adapter = load_adapter()
    output_dir.mkdir(parents=True, exist_ok=False)
    with tempfile.TemporaryDirectory(prefix=f"loopx-peer-s2-{arm}-") as temp:
        temp_root = Path(temp)
        root = temp_root / "fixture-repo"
        runtime_root = temp_root / "runtime"
        baseline = init_fixture_repo(root)
        env = loopx_env(loopx_checkout)
        prefix = loopx_prefix(runtime_root)
        todo_ids = bootstrap_loopx(root=root, prefix=prefix, env=env, arm=arm)

        coordinator_record: dict[str, Any] | None = None
        if arm == "treatment":
            coordinator_record = run_coordinator(
                adapter=adapter,
                prefix=prefix,
                env=env,
                root=root,
                model_id=model_id,
                output_path=output_dir / "coordinator-turn.json",
            )
            schedule = adapter.treatment_schedule(
                {"classification": coordinator_record["classification"]}
            )
        else:
            schedule = adapter.control_schedule()

        patch_paths = {
            WORKER_A: output_dir / "worker-a.patch",
            WORKER_B: output_dir / "worker-b.patch",
        }
        worker_records: dict[str, dict[str, Any]] = {}
        worker_bases: dict[str, str] = {}

        def execute_stage_worker(agent_id: str, base_commit: str) -> tuple[str, dict[str, Any]]:
            label = "a" if agent_id == WORKER_A else "b"
            worktree = temp_root / f"worker-{label}-{len(worker_records)}"
            make_worktree(root, worktree, base_commit)
            worker_bases[agent_id] = base_commit
            record = run_worker(
                adapter=adapter,
                prefix=prefix,
                env=env,
                agent_id=agent_id,
                worktree=worktree,
                model_id=model_id,
                output_path=output_dir / f"worker-{label}-turn.json",
            )
            capture_patch(worktree, base_commit, patch_paths[agent_id])
            return agent_id, record

        for stage in schedule.stages:
            stage_base = git_head(root)
            if len(stage) == 2:
                with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
                    futures = [pool.submit(execute_stage_worker, agent, stage_base) for agent in stage]
                    for future in futures:
                        agent_id, record = future.result()
                        worker_records[agent_id] = record
                for agent_id in (WORKER_A, WORKER_B):
                    apply_patch_and_commit(
                        root,
                        patch_paths[agent_id],
                        f"integrate {agent_id}",
                    )
            else:
                agent_id = stage[0]
                agent_id, record = execute_stage_worker(agent_id, stage_base)
                worker_records[agent_id] = record
                apply_patch_and_commit(root, patch_paths[agent_id], f"integrate {agent_id}")

        composed = run(task_validation(WORKER_B), cwd=root, check=False)
        final_commit = git_head(root)
        summary = {
            "schema_version": 1,
            "arm": arm,
            "loopx_revision": CANONICAL_REF,
            "goal_id": GOAL_ID,
            "model_id": model_id,
            "baseline_commit": baseline,
            "final_commit": final_commit,
            "coordinator_classification": schedule.classification if arm == "treatment" else None,
            "schedule_stages": [list(stage) for stage in schedule.stages],
            "todo_ids": todo_ids,
            "worker_start_base_commits": worker_bases,
            "worker_returncodes": {
                agent: record["returncode"] for agent, record in worker_records.items()
            },
            "composed_acceptance": composed.returncode == 0,
            "composed_stdout": composed.stdout,
            "composed_stderr": composed.stderr,
            "scalar_s2_score": None,
        }
        (output_dir / "run-summary.json").write_text(
            json.dumps(summary, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return summary


def dry_plan(arm: str, model_id: str) -> dict[str, Any]:
    adapter = load_adapter()
    if arm == "treatment":
        schedules = {
            token: [list(stage) for stage in adapter.treatment_schedule({"classification": token}).stages]
            for token in adapter.ALLOWED_CLASSIFICATIONS
        }
    else:
        schedules = {"parallel": [list(stage) for stage in adapter.control_schedule().stages]}
    command = adapter.worker_turn_command(
        loopx_command=(sys.executable, "-m", "loopx"),
        goal_id=GOAL_ID,
        agent_id=WORKER_A,
        worktree=Path("<WORKTREE>"),
        model_id=model_id,
        validation_argv=task_validation(WORKER_A),
    )
    return {
        "schema_version": 1,
        "mode": "dry-plan",
        "arm": arm,
        "schedules": schedules,
        "shared_worker_turn_surface": list(command),
        "live_model_runs_attempted": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--arm", choices=("treatment", "control"), required=True)
    parser.add_argument("--loopx-checkout", type=Path)
    parser.add_argument("--model-id", default="gpt-5.6-sol")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--execute-live", action="store_true")
    args = parser.parse_args()

    preflight = protocol_preflight()
    if not args.execute_live:
        print(json.dumps({"preflight": preflight, "plan": dry_plan(args.arm, args.model_id)}, indent=2))
        return 0

    if args.loopx_checkout is None or args.output_dir is None:
        parser.error("--execute-live requires --loopx-checkout and --output-dir")
    live = live_preflight(args.loopx_checkout)
    summary = execute_arm(
        arm=args.arm,
        loopx_checkout=args.loopx_checkout.expanduser().resolve(),
        model_id=args.model_id,
        output_dir=args.output_dir.expanduser().resolve(),
    )
    print(json.dumps({"preflight": {**preflight, **live}, "summary": summary}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
