---
harness_id: evot
project_name: Evot
repository: https://github.com/evotai/evot
review_ref: 011af29261930f1589c1ded6f8ca5793e271b83a
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Evot

## Review boundary

- System in focus: the shipped Evot terminal/ACP coding harness, including the app multi-session runtime in one process.
- Purpose and identity: perform model-directed coding and scheduled/watch tasks with local files and shell tools.
- Relevant environment: workspace files, shell/background commands, model providers, users and optional hosted services.
- Standard-distribution boundary: Rust engine/app, native addon and CLI; configured full/planning/readonly/none presets; optional /loop and recurring tasks. Hosted service implementation is not imported from outside this repository.
- Credited operating / distribution surfaces: App bootstrap/turn tools to engine model-tool loop; per-session run registry plus process-wide file mutation queue in multi-session mode.
- Adjacent first-party surfaces excluded from ownership: performance assets/benchmark presentation, test mocks/fixtures, install/release machinery and contributor AGENTS instructions; none supply a runtime metasystem owner.
- First-party operating / deployment modes considered: interactive terminal, app/gateway/ACP sessions, ephemeral/readonly/none tool presets, background shell work and fixed/self-paced loops.
- Recursion level: local multi-session harness. Each independently tasked model session is S1; shell tasks and wakeup turns are internal operational mechanisms.
- Reviewed revision: `011af29261930f1589c1ded6f8ca5793e271b83a`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[src/app/src/agent/agent.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/agent.rs) stores active runs by session and assembles provider/tool context. [src/app/src/bootstrap/agent.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/bootstrap/agent.rs) wires the installed tools, model and skills. [src/engine/src/runner/driver.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/runner/driver.rs) streams model responses, executes selected tools, feeds results back and handles steering/retries/compaction. Read, Bash, Edit and Write are the core task tools; optional web, process and host tools extend them. Persistent sessions and optional memory/skill files support later work. Independent sessions retain separate run identities while shared file mutations use [src/engine/src/tools/file/mutex.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/tools/file/mutex.rs). [cli/src/loop/session.ts](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/cli/src/loop/session.ts) binds /loop turns to a host controller: the model can choose the next wakeup or stop, with fixed host bounds. A separate typed Judge scores recent call relevance and helps prune stale context; its relevance input is the task and reported action trail, not independent workspace truth. ToolCallsReviewed events are projected to clients without blocking execution.

## Operational model

Model sessions own task decisions, including whether/when to check an assigned watch task. Runtime code applies configured execution limits and tool access. In same-process multi-session operation, a deterministic path serializes conflicting file changes and exposes edit mismatch/current content to subsequent decisions; it supplies an S2-specific constructor path but no agent-owned cross-session coordination policy.

## S1 — Operations

- State: A
- Function: Coding and assigned recurring/watch operations.
- Disturbance / variety regulated: Task instructions, current file contents, tool errors, shell completions and changing watched conditions.
- Decisive decision or feedback right: Choose tool calls/arguments, revise work from results and decide final response; in dynamic loops choose wakeup or stop.
- Decision owner: Configured model-backed session agent.
- Supporting / enforcement mechanisms: Engine/app/provider bridge, filesystem and shell tools, persisted session context, wakeup timer and bounded retry/limit enforcement.
- Closure path: Model-selected calls execute, results append to context and another response decides further work; scheduled wakeups invoke the same loop.
- Boundary reachability: Installed CLI/app bootstrap builds Agent and actual tool set; submit/resume invokes the engine driver. /loop installs schedule_wakeup through its shipped host extension.
- Why this is / is not agent-owned: Without model choice, the shell/file dispatcher and timer cannot choose the task-specific changes or continuation judgment.
- Evidence: [src/engine/src/runner/driver.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/runner/driver.rs); [src/app/src/agent/agent.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/agent.rs); [src/app/src/agent/tools/build.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/tools/build.rs); [cli/src/loop/session.ts](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/cli/src/loop/session.ts)
- Basis: structural
- Confidence: high for source reachability
- Caveats: No live model, hosted service or native binary execution was tested.

## S2 — Coordination

- State: C
- Function: Attenuate same-file mutation interference between independently tasked sessions sharing one app process/workspace.
- Disturbance / variety regulated: Overlapping read-modify-write edits can race and overwrite another session's change.
- Decisive decision or feedback right: Choose serialization/revalidation for a shared canonical file path; no model coordinator owns that choice.
- Decision owner: Developer-selected process-global mutex/queue protocol; agents only respond locally to results.
- Supporting / enforcement mechanisms: FILE_MUTEXES keyed by canonical path, acquire_file_lock in Edit/Write, session-keyed RunRegistry and tool-result feedback.
- Closure path: A conflicting mutation waits; Edit reads the file after acquiring the lock, applies unique/nonoverlapping old-text matching or returns current-content/mismatch guidance, then the next session model acts on that result.
- Boundary reachability: App supports separate session run identities; its full tool builder instantiates the supplied Edit/Write implementations, which share a process-global mutex registry. No test-only lock or outside actor is borrowed.
- Why this is / is not agent-owned: The coordination response is deterministic; no agent jointly negotiates or revises the cross-session policy. C records the existing disturbance-specific path, not generic runtime extensibility.
- Evidence: [src/engine/src/tools/file/mutex.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/tools/file/mutex.rs); [src/engine/src/tools/file/edit.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/tools/file/edit.rs); [src/engine/src/tools/file/write.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/tools/file/write.rs); [src/app/src/agent/run/registry.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/run/registry.rs); [src/app/src/agent/tools/build.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/tools/build.rs)
- Basis: structural
- Confidence: medium-high within same-process multi-session scope
- Caveats: Not a file ownership/merge protocol across separate processes, Bash or external writers; blind Write can still replace content. A single active session alone is not the inter-S1 witness.
- Distinct S1 units: Separately tasked model sessions indexed independently by RunRegistry.
- Inter-S1 disturbance: Concurrent Edit/Write transactions targeting the same canonical workspace file can interleave reads and writes.
- Attenuating coordination relation: One shared per-file mutation queue covers the complete tool mutation critical section; unrelated files retain parallel execution.
- Feedback into subsequent S1 behaviour: Queued Edit observes the preceding mutation; mismatch feedback directs reread/current-text revision and becomes a later model input.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The queue is specifically wired to shared file mutation collisions between sessions; neither prompt routing nor task decomposition is used as the witness.

## S3 — Inside-and-now control

- State: —
- Function: Whole-system current control is not established.
- Disturbance / variety regulated: Active-run/session registries, configured budgets, tool presets and abort/steering manage execution; /loop's timing choice serves the assigned task rather than whole-harness commitments.
- Decisive decision or feedback right: No qualifying function-specific decisive right/returned regulation is supplied.
- Decision owner: No credited owner; runtime/developer presets and operator task choices remain distinct.
- Supporting / enforcement mechanisms: Run registry, limits, cancellation, tool guards, event projection and persistent sessions.
- Closure path: No qualifying function-specific metasystem closure.
- Why this is / is not agent-owned: Active-run/session registries, configured budgets, tool presets and abort/steering manage execution; /loop's timing choice serves the assigned task rather than whole-harness commitments.
- Evidence: [src/app/src/agent/agent.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/agent.rs); [src/app/src/agent/run/policy.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/run/policy.rs); [cli/src/loop/controller.ts](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/cli/src/loop/controller.ts)
- Basis: structural
- Confidence: high within the inspected operating modes
- Caveats: External orchestrators, custom host extensions and real deployments are outside this finding.

### Absence scope

- Surfaces inspected: Application bootstrap/run registry/tool builder/policy and engine agent/driver/tool execution; file mutation queue/edit/write; relevance judge/projection, compaction/memory; CLI loop/task controller/prompt; ACP/configuration/skills and source test roles.
- Plausible first-party paths checked: run registry/current snapshots, limits, model selection, planning presets, background task stop and loop scheduling
- Why no material first-party path remains: No shipped whole-current regulator chooses resource/commitment priorities across sessions and returns them as binding current control. User steering/kill is not enough to establish a parent S3 loop.

## S3* — Complementary audit

- State: —
- Function: Complementary audit is not established.
- Disturbance / variety regulated: Judge relevance scoring reads task plus recent assistant tool-call trail; compaction judging chooses context relevance. Separate inference alone is not materially different access to operational truth.
- Decisive decision or feedback right: No qualifying function-specific decisive right/returned regulation is supplied.
- Decision owner: No credited owner; runtime/developer presets and operator task choices remain distinct.
- Supporting / enforcement mechanisms: Run registry, limits, cancellation, tool guards, event projection and persistent sessions.
- Closure path: No qualifying function-specific metasystem closure.
- Why this is / is not agent-owned: Judge relevance scoring reads task plus recent assistant tool-call trail; compaction judging chooses context relevance. Separate inference alone is not materially different access to operational truth.
- Evidence: [src/engine/src/judge/relevance.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/judge/relevance.rs); [src/engine/src/runner/driver.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/runner/driver.rs); [src/app/src/agent/run/projection.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/run/projection.rs)
- Basis: structural
- Confidence: high within the inspected operating modes
- Caveats: External orchestrators, custom host extensions and real deployments are outside this finding.

### Absence scope

- Surfaces inspected: Application bootstrap/run registry/tool builder/policy and engine agent/driver/tool execution; file mutation queue/edit/write; relevance judge/projection, compaction/memory; CLI loop/task controller/prompt; ACP/configuration/skills and source test roles.
- Plausible first-party paths checked: relevance review windows, ToolCallsReviewed client events, prune Judge, context memories, tool guards and tests
- Why no material first-party path remains: The reviewed Judge path supplies task-relevance/retention judgments, not independent raw-artifact validation of an operational success claim with corrective control return; normal execution continues regardless of late/missing relevance scores.

## S4 — Outside-and-then intelligence

- State: —
- Function: External/prospective capability adaptation is not established.
- Disturbance / variety regulated: Watched external events cause further task operations; memory/environment facts and provider context handling preserve execution context rather than develop future organizational capability options.
- Decisive decision or feedback right: No qualifying function-specific decisive right/returned regulation is supplied.
- Decision owner: No credited owner; runtime/developer presets and operator task choices remain distinct.
- Supporting / enforcement mechanisms: Run registry, limits, cancellation, tool guards, event projection and persistent sessions.
- Closure path: No qualifying function-specific metasystem closure.
- Why this is / is not agent-owned: Watched external events cause further task operations; memory/environment facts and provider context handling preserve execution context rather than develop future organizational capability options.
- Evidence: [cli/src/loop/session.ts](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/cli/src/loop/session.ts); [src/engine/src/context/compaction/memory.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/context/compaction/memory.rs); [src/app/src/agent/prompt/prompts/memory.md](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/prompt/prompts/memory.md)
- Basis: structural
- Confidence: high within the inspected operating modes
- Caveats: External orchestrators, custom host extensions and real deployments are outside this finding.

### Absence scope

- Surfaces inspected: Application bootstrap/run registry/tool builder/policy and engine agent/driver/tool execution; file mutation queue/edit/write; relevance judge/projection, compaction/memory; CLI loop/task controller/prompt; ACP/configuration/skills and source test roles.
- Plausible first-party paths checked: dynamic/fixed /loop, scheduled tasks, memory/skills, provider selection and compaction/pruning
- Why no material first-party path remains: No supplied external-and-prospective model develops/selects adaptations and returns a changed capability into present regulation. Future wakeup timing alone does not close S4.

## S5 — Policy and identity

- State: —
- Function: Identity/ultimate-policy closure is not established.
- Disturbance / variety regulated: System/project instructions, path/sandbox guards, execution presets and user cancel configure ordinary task boundaries.
- Decisive decision or feedback right: No qualifying function-specific decisive right/returned regulation is supplied.
- Decision owner: No credited owner; runtime/developer presets and operator task choices remain distinct.
- Supporting / enforcement mechanisms: Run registry, limits, cancellation, tool guards, event projection and persistent sessions.
- Closure path: No qualifying function-specific metasystem closure.
- Why this is / is not agent-owned: System/project instructions, path/sandbox guards, execution presets and user cancel configure ordinary task boundaries.
- Evidence: [src/app/src/agent/run/policy.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/agent/run/policy.rs); [src/app/src/bootstrap/agent.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/app/src/bootstrap/agent.rs); [src/engine/src/tools/guard.rs](https://github.com/evotai/evot/blob/011af29261930f1589c1ded6f8ca5793e271b83a/src/engine/src/tools/guard.rs)
- Basis: structural
- Confidence: high within the inspected operating modes
- Caveats: External orchestrators, custom host extensions and real deployments are outside this finding.

### Absence scope

- Surfaces inspected: Application bootstrap/run registry/tool builder/policy and engine agent/driver/tool execution; file mutation queue/edit/write; relevance judge/projection, compaction/memory; CLI loop/task controller/prompt; ACP/configuration/skills and source test roles.
- Plausible first-party paths checked: project instruction/skill loading, full/planning/readonly/none tools, host trust, provider and ACP configuration
- Why no material first-party path remains: No identity-level issue reaches legitimate ultimate authority and returns a governing decision; constraints and ordinary operator configuration are not an S5 parent mode.

## Distributed OSS parent arrangement

The README declares Apache-2.0 but no root LICENSE is shipped at this pin; this public-source assessment does not invent missing license provenance or authorize downstream reuse. Contributor governance is outside runtime ownership.

## Self-hosted and non-human modes

Terminal/ACP/gateway modes use the supplied local engine. Ephemeral/readonly/none settings alter persistence/tool access; they do not supply function-specific parent S3/S4/S5 closure. Hosted backend internals are outside available first-party source.

## Recursion

Independent sessions can share workspace resources. Background shell jobs, loop turns and native tool calls do not establish recursive viable systems or subagent organizations.

## Variety and escalation

Streaming retries, doom-loop detection, compaction, background output, stop/steer and wakeup bounds absorb operational variety. Low relevance/event status does not itself establish an algedonic authority channel.

## Evidence gaps

Static source inspection only. Rust/cargo and Node/Bun are unavailable in the execution environment, so native Rust/CLI tests and builds were not run; no live provider or hosted service interaction occurred. The source test serializes_same_path corroborates intended mutex behavior but was not executed. S2 is deliberately limited to supplied same-process file-tool interference attenuation.
