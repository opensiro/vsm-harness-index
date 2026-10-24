---
harness_id: nemocode
project_name: NemoCode
repository: https://github.com/SampleBias/nemocode
review_ref: 6f5489f289d0963cf0c6b7562c9491670000ccd2
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# NemoCode

## Review boundary

- System in focus: one first-party NemoCode coding task/session at frozen revision `6f5489f289d0963cf0c6b7562c9491670000ccd2`, including the Rust CLI/model-tool loop, repository/file/search/bash/Python tools, permission enforcement, task bookkeeping, interruption/steering, context compaction, durable session journals/checkpoints, retrieval, diagnostics and supported chat/headless execution.
- Purpose and identity: perform local repository software-engineering work, with a Python-first tool/prompt surface, through iterative model/tool decisions and recorded task/session state.
- Relevant environment: user task and interrupt guidance; selected workspace/filesystem; git/file revisions; Python project state; shell/test/diagnostic results; local model-server responses; configured permission mode; locally installed Python/LSP tooling.
- Standard-distribution boundary: the shipped NemoCode Rust binary, launcher/configuration logic, first-party coding/retrieval/Python/session tools and task state are inside. `llama-server`, the bundled/downloaded Nemotron model weights, optional pyright/basedpyright/ruff/pytest binaries, host OS and target-project code are dependencies/environment.
- Credited operating / distribution surfaces: `README.md`; `src/main.rs`; `src/session.rs`; `src/storage.rs`; `src/retrieval.rs`; `src/python_tools.rs`; `src/lsp/`; `src/runtime.rs`; `src/process.rs`.
- Adjacent first-party surfaces excluded from ownership: development CI, public eval fixtures and build-review documents, packaging/release maintenance, hardware-profile measurement plans and unfinished future engineering items.
- First-party operating / deployment modes considered: interactive chat/REPL; headless `nemocode run`; resumed headless sessions; `read-only`, `workspace` and `trusted` permission modes; Python-first diagnostics/tests and generic file/bash work; Ctrl+I current-task steering.
- Recursion level: one NemoCode-managed coding task/session. The model-backed coding actor is the operational S1. Parallel read-only tool execution, subprocesses, LSP servers and the external local inference server are mechanisms/dependencies, not additional model-backed S1 units inside the assessed organization.
- Reviewed revision: `6f5489f289d0963cf0c6b7562c9491670000ccd2`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

NemoCode constructs one model-backed coding loop with a fixed first-party system prompt and a permission-filtered tool schema. For each user task, the model receives current session/location/task state, selects repository/Python/shell actions, and receives first-party tool results back in the same conversation before deciding the next action.

The runtime records a structured `Task` with objective, guidance, changed files, verification evidence, phase, next action and failed mutations. Native writes use content revisions and atomic replacement; failed mutations force recovery before successful completion. Python diagnostics, pytest and ruff results can be recorded as verification evidence.

That verification bookkeeping remains part of the same operational loop. If a model response finishes with changed files but no recorded verification, NemoCode explicitly marks the task `finished_unverified` and still returns successfully. No separate reviewer/verifier/judge actor, independent evidence path or mandatory independent acceptance gate is packaged into the standard runtime.

NemoCode contains no first-party sub-agent/delegate/team surface at the frozen ref. Multiple read-only tool calls may be executed concurrently in bounded batches, but they are tool operations selected for one coding actor rather than distinct operational S1 units.

Durable sessions preserve conversation/task state, recover uncertain interrupted tool results and instruct the resumed coding loop to inspect/verify before continuing. Context trimming, retries, current-task interrupt guidance and stored checkpoints preserve execution continuity rather than forming a future-oriented adaptation or ultimate-policy subsystem.

## Operational model

A user supplies a coding task. The single model-backed actor selects an allowed action; NemoCode validates/executes it, records the result and task-state consequences, and returns that evidence to the same model. The loop repeats until the model emits no tool call, an execution limit fails closed, or the user interrupts/steers it.

After mutations, task bookkeeping asks for relevant checks but does not substitute an independent audit actor. The session can resume from durable checkpoint state, including explicit uncertainty after interrupted operations, so the same S1 can inspect the workspace before retrying.

## S1 — Operations

- State: A
- Function: perform environment-facing repository software-engineering work by interpreting a user task, inspecting code/state, selecting allowed coding actions, editing/running/checking the workspace, observing outcomes and revising subsequent actions.
- Disturbance / variety regulated: heterogeneous repository contents, Python/non-Python project structure, ambiguous implementation choices, file revision races, tool/permission failures, diagnostics/test failures, command output, local model responses, interruptions and context/task-budget pressure.
- Decisive decision or feedback right: choose what evidence to inspect, which offered repository/Python/shell action to invoke, what file change to attempt, how to respond to tool/diagnostic/test results, how to recover failed mutations and when to finish the task.
- Decision owner: the single model-backed NemoCode coding actor running in the first-party task loop.
- Supporting / enforcement mechanisms: permission-filtered tool schema; workspace path checks; SHA-256 stale-edit detection; atomic writes; Python diagnostics/pytest/ruff tools; retrieval; subprocess timeout/cancellation; task budgets; repetition nudges; context compaction; durable checkpoints and Ctrl+I guidance.
- Closure path: user task + current workspace/session state → model chooses a tool/action → NemoCode authorizes and executes it → tool/environment result plus updated task state returns into the same model context → the model chooses the next action or final response.
- Boundary reachability: ordinary interactive `nemocode` and headless `nemocode run` directly instantiate this shipped loop; no application-authored orchestration layer is required.
- Why this is / is not agent-owned: removing the model-backed coding actor leaves deterministic tools/state/enforcement but removes the open-ended task-specific software-engineering decision owner.
- Evidence: [`README.md`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/README.md); [`src/main.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/main.rs); [`src/session.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/session.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: local model inference is an external dependency; the assessment credits NemoCode's first-party role/tool/feedback composition rather than the downloaded model or `llama-server` internals.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: no standard population of distinct concurrently acting model-backed S1 units exists inside one NemoCode task/session, so no inter-S1 interference disturbance is operationalized.
- Decisive decision or feedback right: none established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: safe read-only tool calls can run in bounded parallel batches; writes use stale-revision checks/atomic replacement; subprocesses are bounded; one session lock prevents simultaneous opening of the same session state.
- Closure path: not applicable; no distinct-S1 disturbance → attenuation relation → changed subsequent S1 behavior loop exists in the reviewed standard distribution.
- Why this is / is not agent-owned: tool-level parallelism, optimistic file-write safety and session locking protect one S1's execution but do not coordinate multiple autonomous operational units.
- Evidence: [`README.md`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/README.md); [`src/main.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/main.rs); [`src/storage.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/storage.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an external user could run several independent NemoCode processes, but the repository does not package them into one first-party coordinated organization at this boundary.

### Absence scope

- Surfaces inspected: main model/tool loop; safe parallel read-only tool execution; file revision/atomic-write path; session lock and checkpoints; subprocess execution; README/implementation architecture; source tree searches for subagent/delegate/team mechanisms.
- Plausible first-party paths checked: parallel tool batches as S2; independent CLI processes; session locking; stale-edit rejection; subprocess/LSP processes; implicit multiple model workers.
- Why no material first-party path remains: only one model-backed coding actor is instantiated in a standard task/session. Other concurrent entities are tools/processes/dependencies without their own operational decision right, so no S2-specific inter-S1 attenuation loop exists.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-organization current-control function distinct from the single coding S1 and deterministic task/runtime safeguards was established.
- Disturbance / variety regulated: task phase, failed mutations, budgets, pending calls, current workspace location and interruption state regulate one operational loop rather than a population of current S1 commitments/resources.
- Decisive decision or feedback right: none established at S3 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: structured `Task` phase/next-action state; tool-round and token/time budgets; cancellation/interruption; session checkpoints; permission modes; subprocess timeouts.
- Closure path: not applicable; there is no whole-system current view over multiple relevant operations plus substantive organization-wide priority/resource/commitment intervention.
- Why this is / is not agent-owned: the coding model may replan its own task after failures or user guidance, but self-management of one S1 is not the distinct inside-and-now control function.
- Evidence: [`src/main.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/main.rs); [`src/session.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/session.rs); [`src/process.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/process.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: Ctrl+I lets the user steer the current S1, and runtime guards constrain it, but neither creates a metasystem-level current-control actor at the selected recursion.

### Absence scope

- Surfaces inspected: task state/phase transitions; failed-mutation recovery; budgets; pending calls; interrupt/steering; session resume; subprocess cancellation; permission state; CLI/headless lifecycle.
- Plausible first-party paths checked: task bookkeeping as S3; Ctrl+I human intervention; session supervision; budgets as resource control; current verification state; process monitoring/cancellation.
- Why no material first-party path remains: all located mechanisms govern or steer one coding loop. No first-party actor receives a whole-organization view of multiple current S1 commitments and owns reallocating/prioritizing/accountability decisions across them.

## S3* — Complementary audit

- State: —
- Function: no material complementary audit role with sufficiently independent access, judgment and corrective return into the supported runtime was established.
- Disturbance / variety regulated: NemoCode can run diagnostics/tests and record verification evidence, but those checks are selected and interpreted inside the implementing S1's own loop.
- Decisive decision or feedback right: none established for an independent audit actor/path.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `python_diagnostics`, `run_pytest`, `ruff_check`; task verification evidence; failed-write recovery; static system-prompt instruction to verify after changes.
- Closure path: not applicable; no separate challenge actor or complementary evidence path produces an independent audit judgment and returns that judgment into corrective control.
- Why this is / is not agent-owned: tests/diagnostics are evidence tools for the same implementing S1. The runtime can label an otherwise successful task `finished_unverified`, demonstrating that verification evidence is not a mandatory independent acceptance gate.
- Evidence: [`README.md`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/README.md); [`src/main.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/main.rs); [`src/session.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/session.rs); [`src/python_tools.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/python_tools.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: deterministic checking materially improves reliability, but Methodology 0.3.6 requires complementary audit independence rather than ordinary self-verification.

### Absence scope

- Surfaces inspected: Python diagnostics/test/ruff tools; task verification state; finish path; static system prompt; public eval/development artifacts; source tree searches for reviewer/verifier/judge/subagent roles.
- Plausible first-party paths checked: pytest/diagnostics as auditor; `Task.verification` as audit state; failed-mutation recovery; development eval fixtures; a hidden reviewer/subagent; an implicit independent LSP verifier.
- Why no material first-party path remains: no review-specific runtime actor/path exists, external LSP/checker processes supply raw diagnostic evidence rather than an organizational audit judgment, and ordinary runtime can finish mutated work as `finished_unverified`.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party prospective environment-intelligence and organizational adaptation loop was established.
- Disturbance / variety regulated: retrieval, Python project detection, session persistence, context compaction, runtime/model installation/update commands and retry behavior help current execution or maintenance but do not convert future/environmental intelligence into persistent organizational adaptation.
- Decisive decision or feedback right: none established for prospective capability/strategy adaptation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: local lexical retrieval; Python project detection; durable sessions/checkpoints; context shrinking; context-overflow retry; runtime/model management commands; current-task task-state recovery.
- Closure path: not applicable; no prospective scan → adaptation-option selection → persistent organizational capability/strategy change → later operation loop was found.
- Why this is / is not agent-owned: current-task context management and externally invoked runtime/model maintenance can change execution conditions without constituting S4.
- Evidence: [`README.md`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/README.md); [`src/main.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/main.rs); [`src/runtime.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/runtime.rs); [`src/session.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/session.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: development roadmap/evals discuss future measurements and quality work, but those are maintainer R&D surfaces outside ordinary runtime adaptation.

### Absence scope

- Surfaces inspected: retrieval/project detection; sessions/checkpoints; context compaction; retries; runtime/model install/update/status/bench commands; configuration; implementation/evaluation documentation; source searches for learning/memory/self-improvement mechanisms.
- Plausible first-party paths checked: session memory as learning; context compaction as adaptation; runtime/model update as self-adaptation; local retrieval as environmental scanning; hardware bench/profile selection; public evals feeding later policy.
- Why no material first-party path remains: located mechanisms preserve current-task continuity, expose externally requested maintenance, or support offline development. None closes a runtime prospective intelligence-to-adaptation loop.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy closure was established.
- Disturbance / variety regulated: NemoCode has a fixed system prompt plus externally supplied workspace/config/permission/model/runtime parameters and user task guidance.
- Decisive decision or feedback right: none established for an identity/ultimate-policy issue.
- Decision owner: not established inside the assessed organization; authoritative operating purpose and policy remain developer/operator/user supplied.
- Supporting / enforcement mechanisms: fixed `SYSTEM_PROMPT`; `read-only`/`workspace`/`trusted` permission configuration; workspace/config environment; task budgets; current-turn Ctrl+I guidance.
- Closure path: not applicable; no identity/ultimate-policy issue reaches a first-party autonomous or qualifying parent decision path and returns as an authoritative durable policy change to later operation.
- Why this is / is not agent-owned: static prompt/configuration and user guidance define or constrain the coding actor; they do not let NemoCode decide its own ultimate policy. No `AGENTS.md`/project-policy loading or model-authored durable governance layer was found at the frozen ref.
- Evidence: [`src/main.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/main.rs); [`src/runtime.rs`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/src/runtime.rs); [`README.md`](https://github.com/SampleBias/nemocode/blob/6f5489f289d0963cf0c6b7562c9491670000ccd2/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: human users retain real authority over tasks/configuration, but generic operator ownership does not create a Methodology-qualified S5 parent mode.

### Absence scope

- Surfaces inspected: fixed system prompt; runtime/environment configuration; permission modes; task budgets; user/interrupt guidance; session persistence; source searches for project instructions, policy mutation and identity/governance layers.
- Plausible first-party paths checked: environment/config as S5; permission mode as policy; Ctrl+I/user task as parent governance; model self-revision; durable project instructions; session state as standing policy.
- Why no material first-party path remains: durable authoritative values are external/static, while user guidance is task-level steering. No first-party identity-level decision loop or qualifying parent return path is packaged into the assessed runtime.

## Distributed OSS parent arrangement

Repository maintainers and local operators can modify NemoCode code/configuration outside the running coding organization. That ordinary external governance is not a supported runtime S5 parent loop at the selected task/session recursion.

## Self-hosted and non-human modes

NemoCode is local/self-hosted in the ordinary deployment sense, but local execution does not change VSM ownership. The model-backed S1 can run without per-step human choices after task/configuration input, while no additional S2/S3/S3*/S4/S5 autonomous or qualifying parent mode is established.

## Recursion

At the selected recursion there is one operational model-backed coding S1. Read-only parallel tool batches, Python/LSP checker processes, the model server and subprocesses are mechanisms/dependencies rather than additional S1 units. Therefore their scheduling, checking or locking is not promoted to S2/S3/S3* without the corresponding organizational role/closure.

## Variety and escalation

Open-ended coding variety is absorbed by the S1 model/tool loop. Permissions, stale-write rejection, budgets, subprocess limits and task bookkeeping constrain execution variety. Failed mutations feed a deterministic recovery requirement back to the same S1; uncertain resumed operations are surfaced for inspection. Verification evidence likewise returns to the same actor rather than an independent auditor.

## Evidence gaps

No evidence gap requires `?` for the published vector. The frozen repository exposes a compact single-agent architecture and explicit finish/recovery behavior; the negative metasystem classifications follow from absence of distinct organizational actors/return loops rather than missing repository access.

## Assessment summary

NemoCode closes autonomous S1 through its single local model/tool coding loop. Safe tool parallelism and file/session safeguards remain intra-S1, current task bookkeeping does not establish whole-system S3, diagnostics/tests are self-verification rather than independent S3*, durable sessions/context management do not close prospective S4, and externally supplied prompt/configuration/permissions do not establish S5.

Proposed vector: **`A · — · — · — · — · —`**.
