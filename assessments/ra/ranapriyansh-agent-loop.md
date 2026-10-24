---
harness_id: ranapriyansh-agent-loop
project_name: agent-loop
repository: https://github.com/RanaPriyansh/agent-loop
review_ref: c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# agent-loop

## Review boundary

- System in focus: the first-party `RanaPriyansh/agent-loop` Python terminal coding-repair agent at pinned commit `c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb`.
- Purpose and identity: rerun a selected test command and attempt code fixes in a local workspace until tests pass or a bounded stop condition is met.
- Relevant environment: local code, test failure output, user-chosen allowed files and command, configured LLM provider in the optional mode, and workspace filesystem.
- Standard-distribution boundary: CLI in `src/agent_loop/cli.py`, `Agent` test–plan–write–retest loop, `Planner` deterministic and opt-in model modes, `Tools` path/command checks and JSONL audit events. The Anthropic service, user/operator, tests in a target project and external repository governance do not become independent first-party organizational functions.
- Credited operating / distribution surfaces: `src/agent_loop/agent.py`, `planner.py`, `tools.py`, `cli.py` and the supported `--use-llm` option described in the README.
- Adjacent first-party surfaces excluded from ownership: repository unit tests, `fixtures/broken_code` demonstration, packaging/build metadata, README claims beyond operational source, and maintainer decisions.
- First-party operating / deployment modes considered: deterministic default CLI; explicit `--use-llm` CLI with a separately installed Anthropic SDK and provided API key; selected pytest/cargo/npm test commands; allowlisted/whole-workspace file operations; audit log and bounded termination.
- Recursion level: one locally executing code-repair loop. Test subprocesses and optional remote model completions are not separate first-party subordinate S1 organizations.
- Reviewed revision: `c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`cli.py` accepts a workspace, a restricted test command, optional target files, a log path, and `--use-llm`; it starts one `Agent`. The loop in `agent.py` executes tests, checks success or repetition, heuristically locates a file from failure output, reads it, calls `Planner.plan_fix`, writes a changed result, records append-only JSONL events, and retests. It is bounded at eight iterations and ends early on repeated output, no target, no changed content or errors. `Tools` implements workspace/allowlist path checks and permitted command-prefix checks.

By default, `Planner._plan_deterministic` rewrites a few known Python arithmetic-return patterns, so default success is not itself evidence of autonomous decision-making. Explicit `--use-llm` switches the same loop to `_plan_with_llm`, which sends failing-test evidence and source content to the configured Anthropic model and applies the returned corrected text, subject to the ordinary file path constraint. The package documents installing the SDK separately and supplying `ANTHROPIC_API_KEY`; the optional code branch is wired from the shipped CLI through `Agent` to `Planner`, though its external live behavior was not exercised.

Primary pinned source:

- [`src/agent_loop/cli.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/cli.py)
- [`src/agent_loop/agent.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/agent.py)
- [`src/agent_loop/planner.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/planner.py)
- [`src/agent_loop/tools.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/tools.py)
- [`tests/test_agent.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/tests/test_agent.py)

## Operational model

The runtime owns one repair operation, not a collection of agents. A deterministic supervisor selects each test–plan–edit–retest step. In the first-party optional LLM mode the model selects the actual corrective code under novel failure evidence, and subsequent tests provide closed-loop feedback. The user controls the workspace, goal/test command, permissible files, and whether to opt into LLM mode. In the default mode the patch selection is hard-coded and does **not** independently justify `S1=A`; the positive classification is explicitly limited to the reachable optional mode. The audit log is an operational record, not an independently owned complementary auditor.

## S1 — Operations

- State: A
- Function: produce and iteratively revise a local code repair to satisfy a selected test suite.
- Disturbance / variety regulated: failing tests, evolving diagnostics after a patch, unexpected current file content and repeated errors.
- Decisive decision or feedback right: in explicitly selected LLM mode, choose corrected code based on test diagnostics and file content; the harness writes it and returns fresh test output to the next planning step.
- Decision owner: model-assisted `Planner` within one `Agent` loop in `--use-llm` mode; the operator establishes the task boundary and provider access.
- Supporting / enforcement mechanisms: bounded eight-iteration scheduler, allowlisted test commands/paths, test feedback, target-file heuristic, JSONL event log and early-stop guards.
- Closure path: selected test command → failure output → target file and current code → optional model-selected repair → allowlisted file write → rerun tests → further repair or stop.
- Boundary reachability: `cli.py` explicitly wires `--use-llm` to `Agent(use_llm=True)`, whose constructor calls `Planner(use_llm=True)` and whose `run` calls `plan_fix`; this selects `_plan_with_llm` with the documented separate SDK/key prerequisites. No unregistered tool or external orchestration layer is required for this branch.
- Why this is / is not agent-owned: model-selected correction is open-ended task-specific discretion inside a first-party feedback loop; the default regex-like arithmetic rewrites alone would be a non-agentic fixed script. Harness guardrails and remote inference do not establish another independent VSM unit.
- Evidence: [`cli.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/cli.py); [`agent.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/agent.py); [`planner.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/planner.py); [`README.md`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/README.md).
- Basis: explicit + structural; 14 first-party deterministic tests passed, with no live model invocation.
- Confidence: medium-high for shipped optional-mode reachability; unmeasured for production LLM repair performance.
- Caveats: no Anthropic SDK/key or live model was used; script-only tests validate deterministic behavior and the absent-key guard, not model decision quality.

## S2 — Coordination

- State: —
- Function: no first-party interference-damping coordination among distinct repair S1 units is established.
- Disturbance / variety regulated: concurrent changes or competing agent commitments are outside this one-loop distribution.
- Decisive decision or feedback right: none over interference between independent S1 agents.
- Decision owner: one `Agent` sequentially runs tests, planning and writes.
- Supporting / enforcement mechanisms: a sequential bounded iteration counter, file allowlist and subprocess restrictions.
- Closure path: no distinct S1 population → S2-specific detection/coordination → behavior correction circuit is shipped.
- Why this is / is not agent-owned: ordering one agent's steps and restricting filenames is not cross-S1 damping.
- Evidence: [`agent.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/agent.py); [`tools.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/tools.py).
- Basis: full small-source structural absence review.
- Confidence: high.
- Caveats: downstream users could separately coordinate multiple processes; that coordination is not included here.

### Absence scope

- Surfaces inspected: CLI, Agent loop, Planner, Tools and first-party tests.
- Plausible first-party paths checked: separate worker processes, subagent dispatch, shared-file coordination, concurrent plan execution and task queues.
- Why no material first-party path remains: only one `Agent` instance and one sequential correction loop are constructed; test subprocesses do not form separate autonomous S1 decisions.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current multi-unit resource, priority or commitment management is established at a metasystem recursion.
- Disturbance / variety regulated: test failure and iteration exhaustion are task-local issues, not system-wide agent-capacity imbalances.
- Decisive decision or feedback right: no higher-level current management decision over an agent population.
- Decision owner: user supplies initial task/boundaries; deterministic Agent guards stop or continue one loop.
- Supporting / enforcement mechanisms: MAX_ITERATIONS, fixed per-test timeout, repeat-error stop, allowlisted paths/commands and audit logs.
- Closure path: test output changes the local repair sequence or terminates it; there is no whole-current S3 view → management decision → returned allocation/intervention path.
- Why this is / is not agent-owned: resource caps and stop rules constrain one S1 and are not current metasystem discretion, including parent-governed S3.
- Evidence: [`agent.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/agent.py); [`cli.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/cli.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: operator-provided workspace/paths and test commands do not supply an operational S3 parent decision return.

### Absence scope

- Surfaces inspected: loop state, diagnostic parsing, early stops, CLI boundaries, tests and audit log.
- Plausible first-party paths checked: runtime supervisory controller, parent operator management, dynamic job allocation, priority/commitment revision and budget policy.
- Why no material first-party path remains: the program only executes a preset task and stops based on fixed conditions; there is no whole-system current-control scope or parent return workflow.

## S3* — Complementary audit

- State: —
- Function: no separate reality-checking audit path with a corrective return independent of ordinary repair reporting is established.
- Disturbance / variety regulated: tests observe the immediate artifact and the log records activity, but neither supplies complementary organizational audit.
- Decisive decision or feedback right: no independent audit finding or escalation owner.
- Decision owner: the same loop reads test output and appends log records.
- Supporting / enforcement mechanisms: tests, `test_run` and `fix_applied` JSONL events, and unit tests in the development repository.
- Closure path: ordinary test failure → same repair planner; no independent claimed-status challenge → separate management corrective return is shipped.
- Why this is / is not agent-owned: running tests as an operational success gate is not complementary audit; append-only logging does not make an auditor.
- Evidence: [`agent.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/agent.py); [`tests/test_agent.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/tests/test_agent.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: an outside auditor could consume JSONL, but none is packaged as a first-party return path.

### Absence scope

- Surfaces inspected: test-run, log-write, output parsing and correction code; first-party test suite.
- Plausible first-party paths checked: independent verifier, external evidence sampling, log-based reviewer, regression tests as audit and human operator reading logs.
- Why no material first-party path remains: all feedback is ordinary same-loop test evidence; JSONL is written but no audit-specific separate authority, trigger or returned correction exists.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective environmental scanning and strategic capability adaptation is closed.
- Disturbance / variety regulated: test errors and current code are used for immediate fixes, not to forecast changing external conditions.
- Decisive decision or feedback right: no future-oriented capability selection or policy change from external distinctions.
- Decision owner: user picks planner mode and goal in CLI; the planner selects a current file patch.
- Supporting / enforcement mechanisms: optional LLM code fix, static mode switch, tests and log.
- Closure path: failure evidence feeds present S1 repair; there is no outside/future sensing → alternatives → adaptation decision → implementation/return path.
- Why this is / is not agent-owned: an LLM-generated patch is current operations, not strategic adaptation of the harness.
- Evidence: [`planner.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/planner.py); [`cli.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/cli.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: repairing downstream code may help future tests, but does not establish an S4 decision owner.

### Absence scope

- Surfaces inspected: full Planner, CLI options, loop persistence and tests.
- Plausible first-party paths checked: adaptation of planning strategies, historical trend analysis, external monitoring, self-upgrade and persistent capability selection.
- Why no material first-party path remains: the only model choice is immediate source correction; log data is not read to select future capability changes.

## S5 — Policy and identity

- State: —
- Function: no legitimate first-party decision path for ultimate organizational identity, purpose or policy is implemented.
- Disturbance / variety regulated: potentially unsafe commands/paths are checked under fixed enforcement rules, not resolved as ultimate-policy questions.
- Decisive decision or feedback right: user determines initial task and permitted files; no shipped S5 deliberation and authoritative return.
- Decision owner: external operator/maintainer for goals and configuration; script enforces fixed constraints.
- Supporting / enforcement mechanisms: command allowlist, path checks, max-iteration cap, API credential requirement and CLI flags.
- Closure path: prescribed safety settings gate local operations; no identity/policy issue → legitimate deciding authority → durable system-governance return loop.
- Why this is / is not agent-owned: permission/command checks and task selection are not ultimate organizational policy governance.
- Evidence: [`tools.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/tools.py); [`cli.py`](https://github.com/RanaPriyansh/agent-loop/blob/c4c5dcd35bf89a36b6b477f4d9cb66c4b838a4eb/src/agent_loop/cli.py).
- Basis: structural absence review.
- Confidence: high.
- Caveats: repository maintainers retain real-world governance outside the runtime boundary.

### Absence scope

- Surfaces inspected: CLI initialization, `Tools` restrictions, Planner key requirement, Agent termination and adjacent packaging/README.
- Plausible first-party paths checked: owner identity, appeal/exception mechanism, policy committee or parent mandate, organizational-purpose governance and durable policy decision return.
- Why no material first-party path remains: the source only has predefined task-level technical constraints and no legitimate ultimate-policy issue or deciding circuit.

## Recursion

One local operational loop is established in the opt-in LLM mode. Tests are subprocesses and remote completion is used as inference; neither creates another separately governed harness S1. No independent child/team recursion is shipped.

## Variety and escalation

Test failure evidence and model-generated code changes amplify the optional S1's repertoire; allowed commands/paths, eight iterations, a 30-second test timeout and no-progress/repeat-stop guards attenuate risk. Error conditions stop the current task and return a CLI result. There is no implemented ascent to a higher S2–S5 decision actor.

## Evidence gaps

- No LLM-agent runs were performed, in accordance with the script-only batch protocol. `PYTHONPATH=src uv run --offline --no-project --with pytest python -m pytest -q` passed **14/14** first-party tests, covering deterministic patching, bounded stops, logging and an absent-key guard. This verifies neither live Anthropic availability nor the quality of LLM-selected corrections.
- The `--use-llm` code path is first-party and explicitly reachable but depends on an separately installed SDK, operator API key and service. If those are unavailable to an installation, only the deterministic non-agentic mode runs; `S1=A` is not assigned to that mode.
- The absence conclusions are bounded to the small first-party pinned source and documented optional modes, not to hypothetical external orchestrators, independent auditors or maintained future releases.

## Assessment summary

At the frozen revision, `agent-loop` provides a single bounded test–patch–retest S1. Its default rule-based corrections are deterministic, while its wired, documented opt-in LLM mode delegates corrective-code choice to a model and uses fresh test feedback for autonomous operational revision (`S1=A`). No separate first-party S2 coordination, S3 whole-current control, S3* complementary audit, S4 prospective adaptation or S5 identity-policy circuit is established.

Proposed vector: **`A · — · — · — · — · —`**
