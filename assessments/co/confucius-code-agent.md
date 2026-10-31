---
harness_id: confucius-code-agent
project_name: Confucius Code Agent
repository: https://github.com/facebookresearch/cca-swebench
review_ref: bdeb74b3d828bfbb2c61030c6201fa9da44e69d0
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Confucius Code Agent

## Review boundary

- System in focus: the first-party CCA CodeAssistEntry and shipped coding runtime.
- Purpose and identity: solve repository software tasks through direct actions inside the working environment.
- Relevant environment: target repository/container filesystem, commands, user problem statements and configured model providers.
- Standard-distribution boundary: installed confucius package and Code entry invoked by CLI/PEX/scripts.
- Credited operating / distribution surfaces: CodeAssistEntry, AnthropicLLMOrchestrator, direct command/file extensions, planning/context memory and SoloMode.
- Adjacent first-party surfaces excluded from ownership: SWE-bench scoring and external test harness; offline NoteTaker is inspected as an adjacent observer, not silently wired into the coding run.
- First-party operating / deployment modes considered: documented in-container Code entry, library/CLI invocation and separately invoked note-taking mode.
- Recursion level: one CCA coding run, not benchmark fleet or Meta's development organization.
- Reviewed revision: `bdeb74b3d828bfbb2c61030c6201fa9da44e69d0`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Python package owns a tool-using coding actor. CodeAssistEntry explicitly wires planning, file editing, allowed shell commands, hierarchical memory, prompt caching and SoloMode. The orchestrator calls the model, dispatches tool actions and processes interruptions/observations into subsequent context. SoloMode repeats until progress reaches completion or a blocked status; this is task continuation, not whole-system management. The planner summarizes/omits overflowing history and supplies a next step. The separate NoteTaker reads saved trajectories and writes selective notes; its runner explicitly disallows solving the original task. The scripts package the actual agent inside a container; the surrounding benchmark result is outside the assessed owner boundary. LICENSE is MIT.

## Operational model

The Code actor selects inspection, edits, reproduction/tests and subsequent action. Deterministic extensions dispatch/enforce the actor's choices. A planner/model call is not automatically a second operational unit or metasystem. The user's problem statement and developer command policy bound work; no organizational parent mode is presumed.

## S1 — Operations

- State: A
- Function: implement a requested repository change.
- Disturbance / variety regulated: unknown code, errors and task-specific alternatives.
- Decisive decision or feedback right: choose actions and revise implementation from tool observations.
- Decision owner: model-driven Code actor.
- Supporting / enforcement mechanisms: command/file adapters, memory, interruption loop and progress artifacts.
- Closure path: Code entry → model/tool action → direct environment result → next decision.
- Boundary reachability: The documented script imports CodeAssistEntry and invokes the Code entry; entry.py packages the relevant extensions.
- Why this is / is not agent-owned: Removing the model leaves execution machinery without the discretionary implementation choice.
- Evidence: [confucius/analects/code/entry.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/analects/code/entry.py); [confucius/orchestrator/base.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/orchestrator/base.py); [scripts/run_swebench.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/scripts/run_swebench.py); [confucius/orchestrator/extensions/command_line/base.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/orchestrator/extensions/command_line/base.py).
- Basis: structural
- Confidence: high
- Caveats: Pinned source assessment; no live-model or benchmark-performance claim.

## S2 — Coordination

- State: —
- Function: no evidenced regulation of inter-S1 interference.
- Disturbance / variety regulated: task steps and context size, rather than interacting operational units.
- Decisive decision or feedback right: no coordination discretion established.
- Decision owner: coding actor owns task work; the planner supplies a local plan.
- Supporting / enforcement mechanisms: analect invocation, extension ordering and planner.
- Closure path: extensions execute within one coding conversation; separate benchmark containers do not feed a first-party coordination loop.
- Why this is / is not agent-owned: Multiple calls/extensions and separately invoked note-taking do not demonstrate S2.
- Evidence: [confucius/analects/code/entry.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/analects/code/entry.py); [confucius/orchestrator/extensions/plan/llm.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/orchestrator/extensions/plan/llm.py); [scripts/run_note_taker.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/scripts/run_note_taker.py).
- Basis: structural
- Confidence: high
- Caveats: Pinned source assessment; no live-model or benchmark-performance claim.

### Absence scope

- Surfaces inspected: Code/NoteTaker entry composition, orchestrator extension hooks, planner and runners.
- Plausible first-party paths checked: planner-to-coder handoff, nested analect calls, note-taking and multi-container execution described in README.
- Why no material first-party path remains: No specific inter-operational-unit collision/oscillation and corresponding regulating feedback is supplied at this coding-run boundary.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control function established.
- Disturbance / variety regulated: per-task progress, context limits and action failures.
- Decisive decision or feedback right: progress reporting and fixed iteration limits do not exercise whole-system resource/commitment authority.
- Decision owner: coding actor for local work; developers/operators for configured limits.
- Supporting / enforcement mechanisms: SoloMode meter, max_iterations and token-aware planner.
- Closure path: incomplete progress causes continuation; blocked progress permits stopping.
- Why this is / is not agent-owned: The same S1 actor reports progress; enforcing continuation or a ceiling is not S3 ownership.
- Evidence: [confucius/orchestrator/extensions/solo/base.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/orchestrator/extensions/solo/base.py); [confucius/orchestrator/base.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/orchestrator/base.py); [confucius/orchestrator/extensions/plan/llm.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/orchestrator/extensions/plan/llm.py).
- Basis: structural
- Confidence: high
- Caveats: Pinned source assessment; no live-model or benchmark-performance claim.

### Absence scope

- Surfaces inspected: SoloMode status/continuation branches, BaseOrchestrator limits, planner token thresholds and Code entry.
- Plausible first-party paths checked: progress meter, blocked/error handling, budget/iteration stops and operator task input.
- Why no material first-party path remains: These paths manage one task's execution without a whole-system view and discretionary current-control/returned parent-control relation.

## S3* — Complementary audit

- State: —
- Function: no complementary independent audit return at the assessed coding boundary.
- Disturbance / variety regulated: possibly incorrect implementation and self-reported completion.
- Decisive decision or feedback right: producer checks/reproduction do not create independent audit judgment.
- Decision owner: Code actor performs its own checks; benchmark scorer is external.
- Supporting / enforcement mechanisms: shell tests, trajectory dump and separate note-taking.
- Closure path: task tool results return to the producer; NoteTaker writes documentation, not an authoritative corrective audit return.
- Why this is / is not agent-owned: The offline observer has trajectories but no original environment access or wired corrective control. Benchmark outcomes are not CCA-owned audit.
- Evidence: [scripts/run_swebench.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/scripts/run_swebench.py); [scripts/run_note_taker.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/scripts/run_note_taker.py); [confucius/analects/note_taker/tasks.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/analects/note_taker/tasks.py).
- Basis: structural
- Confidence: high
- Caveats: Pinned source assessment; no live-model or benchmark-performance claim.

### Absence scope

- Surfaces inspected: Code task/exit instructions, note-taking entry and prompt, trajectory-save utility, runner composition.
- Plausible first-party paths checked: reproduction-script validation, post-run trajectory observation and independent benchmark scoring.
- Why no material first-party path remains: No shipped audit-specific claim challenge with materially independent operational access and returned corrective control closes in the coding run. Generic callback extensibility is insufficient.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective capability adaptation loop established.
- Disturbance / variety regulated: context overflow and reusable observations from prior tasks.
- Decisive decision or feedback right: summarize context or record insights, not select externally grounded adaptation options.
- Decision owner: planner/note-taking actor for summaries; operator for running scripts.
- Supporting / enforcement mechanisms: hierarchical memory, planner summaries and note files.
- Closure path: information can persist, but no prospective option-development/decision path returns to current capability.
- Why this is / is not agent-owned: Future usefulness of notes is not itself S4.
- Evidence: [confucius/orchestrator/extensions/plan/llm.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/orchestrator/extensions/plan/llm.py); [confucius/orchestrator/extensions/memory/hierarchical/extension.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/orchestrator/extensions/memory/hierarchical/extension.py); [confucius/analects/note_taker/tasks.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/analects/note_taker/tasks.py); [scripts/run_note_taker.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/scripts/run_note_taker.py).
- Basis: structural
- Confidence: high
- Caveats: Pinned source assessment; no live-model or benchmark-performance claim.

### Absence scope

- Surfaces inspected: planner, hierarchical memory import/read/write paths, NoteTaker instructions and invocation.
- Plausible first-party paths checked: long-term notes, cross-session memory import, context summarization and model configuration.
- Why no material first-party path remains: These expose retrospective knowledge/context handling without a supplied external/future sensing → adaptation-option → capability-control loop or returned parent adaptation decision.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy adjudication loop established.
- Disturbance / variety regulated: allowed commands and task-level constraints.
- Decisive decision or feedback right: configure/enforce task boundaries, not resolve identity-level policy tension.
- Decision owner: developer/operator supplies task and allowed-command policy.
- Supporting / enforcement mechanisms: system prompt, file access policy interfaces and validators.
- Closure path: ordinary instructions/allow-deny decisions constrain actions; no ultimate-policy issue/decision/return channel.
- Why this is / is not agent-owned: Constraints and a final user task decision are not S5.
- Evidence: [confucius/analects/code/tasks.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/analects/code/tasks.py); [confucius/analects/code/commands.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/analects/code/commands.py); [confucius/orchestrator/extensions/file/policy/base.py](https://github.com/facebookresearch/cca-swebench/blob/bdeb74b3d828bfbb2c61030c6201fa9da44e69d0/confucius/orchestrator/extensions/file/policy/base.py).
- Basis: structural
- Confidence: high
- Caveats: Pinned source assessment; no live-model or benchmark-performance claim.

### Absence scope

- Surfaces inspected: Code task template, command allowlist/validators, file-policy interface and entry/runner settings.
- Plausible first-party paths checked: task authorization prompts, file-policy deny/allow, maintainer/contributor governance outside the runtime.
- Why no material first-party path remains: No supported runtime identity/ultimate-policy proposal reaches legitimate authority and returns to govern subsequent operation; source contribution policy belongs to an adjacent recursion.

## Distributed OSS parent arrangement

OSS contributor authority is outside the Code run. Multiple contributors do not establish S3/S4/S5 parent modes here.

## Self-hosted and non-human modes

The documented container/library modes preserve Code actor ownership; provider credentials and fixed constraints do not establish a parent-governed metasystem.

## Recursion

Analects and extensions are compositional software structure. Their nesting does not demonstrate independently viable operational systems.

## Variety and escalation

Tool observations, planning/context reduction, progress continuation and blocked/error exits absorb coding variety. Iteration ceilings remain deterministic support.

## Evidence gaps

No live model run or benchmark score verification. The adjacent NoteTaker is fully distinguished from the active Code entry; future wiring or undocumented external services are not credited.
