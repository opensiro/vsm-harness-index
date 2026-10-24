---
harness_id: ally
project_name: Ally
repository: https://github.com/Bronya0/ally-agent
review_ref: dafc35cdc2ff1bae6b89b0f9398448f752fc418d
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Ally

## Review boundary

- System in focus: the first-party `Bronya0/ally-agent` desktop/CLI coding-agent distribution at frozen revision `dafc35cdc2ff1bae6b89b0f9398448f752fc418d`, including its main model/tool loop, built-in coding tools, parallel sub-agent path, shared-workspace file mutation controls, planning/session/memory machinery, scheduled-task runtime and directly owned local/remote execution surfaces where they bear on organizational function.
- Purpose and identity: complete software-development work through a conversational coding agent that can inspect and modify local or remote workspaces, execute commands, retain sessions/memory and delegate substantial independent work to bounded sub-agents.
- Relevant environment: user requests and approvals, local/SSH project workspaces, changing file contents, shell/process state, model/provider responses, MCP services, public web/API resources, persistent session/memory state and scheduled-task instructions.
- Standard-distribution boundary: the shipped Ally application/runtime, `runChat` loop, built-in tool executor, `subagent`/`agent_delegate` path, file-operation lock/version machinery, first-party prompt/planning/session/memory/scheduler surfaces and shipped UI/CLI execution are inside. Model/provider inference, external MCP servers, SSH hosts beyond Ally's adapter boundary, host operating system, target-project governance and fetched external content are dependencies/environment rather than Ally organizational decision owners.
- Credited operating / distribution surfaces: `README.md`; `docs/agent-core-loop.md`; `internal/app/app.go`; `internal/app/orch_subagent.go`; `internal/app/orch_batch_policy.go`; `internal/app/orch_edit.go`; `internal/app/biz_prompt.go`; directly reached first-party scheduler/session/memory/tool surfaces.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/build machinery; tests; contributor/development governance; repository documentation as an actor; implementation reference projects; any development-only validation not wired into supported user runs.
- First-party operating / deployment modes considered: desktop conversational coding runs, supported CLI/runtime paths, local and remote workspace tools, ordinary parallel tool batches, parallel sub-agent delegation, persistent sessions/memory, scheduled task execution and supported MCP augmentation.
- Recursion level: one Ally coding organization around one user/workspace mission. The main model-backed coding loop is one S1; each concurrently executing delegated sub-agent can be a distinct bounded S1 because it independently performs repository-facing investigation/edit/command work in the shared project environment and returns an outcome to the parent.
- Reviewed revision: `dafc35cdc2ff1bae6b89b0f9398448f752fc418d`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Ally's standard coding path is a first-party model/tool feedback loop. `runChat` builds the session/system context, streams a model response, executes returned tools and appends their results for the next model step until the model finishes or runtime limits/cancellation stop the run. The runtime deliberately parallelizes independent non-file tools while ordering file mutations. Built-in coding actions include repository reads/searches, versioned edits, create/delete, command/background-process execution, web/HTTP access, plans, skills, MCP and local/remote workspace operations.

The standard prompt exposes `subagent` for substantial self-contained work and explicitly encourages multiple independent investigations/modules to be delegated in the same model response. Such calls enter the normal parallel tool pool, acquire bounded sub-agent slots and run independent model/tool loops concurrently. Each sub-agent has fresh model context, its own read cache and tool-call budget while sharing the selected project workspace. The parent receives each finished sub-agent's report and file/activity metadata as tool feedback.

That shared workspace exposes a concrete cross-S1 interference mode. File-changing operations are serialized through Ally's application-owned file-operation lock, while edits require a version returned by a prior read. `editFilesWithConfig` compares the submitted version with current bytes immediately before applying changes and rejects stale snapshots with `E_VERSION_MISMATCH`; it also rechecks the version before commit. The prompt instructs an agent receiving that error to re-read current state before retrying. Thus a concurrent worker that changes a file invalidates another worker's stale write rather than allowing silent overwrite, and the rejection feeds back into the losing worker's later behavior.

Planning, live sub-agent status, cancellation, sessions, memory, scheduled tasks and safety policy are substantial supporting mechanisms. At the reviewed boundary they do not independently establish whole-current management, complementary audit, prospective organizational adaptation or ultimate-policy closure.

Primary evidence:

- [`README.md`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/README.md)
- [`docs/agent-core-loop.md`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/docs/agent-core-loop.md)
- [`internal/app/app.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/app.go)
- [`internal/app/orch_subagent.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/orch_subagent.go)
- [`internal/app/orch_batch_policy.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/orch_batch_policy.go)
- [`internal/app/orch_edit.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/orch_edit.go)
- [`internal/app/biz_prompt.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/biz_prompt.go)

## Operational model

A normal Ally run receives a task and workspace context. The main model-backed actor chooses coding tools, the first-party runtime executes or rejects those calls and the results return into subsequent model turns. For sufficiently independent work, the same actor can issue several `subagent` calls in one response; the backend executes those non-file calls concurrently, and each child performs its own bounded coding/investigation loop before returning a report.

All children share the project workspace. Ally therefore combines parallel operational capacity with deterministic write serialization and optimistic concurrency feedback. A child that read an old file version cannot silently write through a sibling's later change: its edit fails, the tool result returns to that child's model loop, and the standard editing discipline requires a fresh read before retry. This is credited as a real S2 function with constructor/runtime ownership rather than agent-owned coordination discretion.

## S1 — Operations

- State: A
- Function: perform environment-facing software-development work by interpreting a task, inspecting project/environment evidence, choosing coding actions, applying changes or commands and reacting to returned results.
- Disturbance / variety regulated: heterogeneous repository structure and source code, tool/command output, changing workspace state, remote/local execution differences, model/provider failures and implementation choices encountered while completing the requested work.
- Decisive decision or feedback right: choose which available repository/tool action to invoke next, what evidence to inspect, what edits/commands to perform, whether to delegate a bounded independent subtask, and when enough work/evidence exists to produce the next outcome.
- Decision owner: the model-backed main Ally actor and, for bounded delegated work, the model-backed sub-agent actor running Ally's first-party sub-agent loop.
- Supporting / enforcement mechanisms: `runChat`; tool registry/executor; project/system context; file-operation controls; sessions/memory; model/provider adapters; MCP; command/runtime safeguards; sub-agent budgets and concurrency semaphore.
- Closure path: user task/workspace state → Ally model request → model selects tool/action → first-party runtime executes/rejects it → result enters the actor's message history → actor changes subsequent action or terminates with an outcome.
- Boundary reachability: the downloaded/standard Ally application directly instantiates the main coding loop and exposes delegation and built-in coding tools through its shipped prompt/tool surface; application authors do not have to build a separate agent loop to obtain the credited operation.
- Why this is / is not agent-owned: removing the model-backed decision actor while retaining the deterministic runtime leaves tools, persistence and safety controls but removes the open-ended repository-facing judgment that chooses and sequences the work.
- Evidence: [`README.md`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/README.md); [`docs/agent-core-loop.md`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/docs/agent-core-loop.md); [`internal/app/orch_subagent.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/orch_subagent.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference and external tool services remain dependencies; the assessment credits Ally's first-party role/tool/feedback composition, not provider internals.

## S2 — Coordination

- State: C
- Function: attenuate destructive shared-workspace interference among concurrently executing Ally S1 workers, especially stale or colliding file mutations from parallel delegated work.
- Disturbance / variety regulated: two or more concurrently active sub-agents can inspect the same shared workspace and act from different file snapshots; without coordination, a later stale mutation could overwrite or invalidate another S1's intervening change.
- Decisive decision or feedback right: determine whether a proposed file mutation may commit against current workspace state or must be rejected as stale/conflicting, and force the losing actor to observe the new state before retrying.
- Decision owner: deterministic first-party runtime policy (`fileOpsMu` serialization, version/hash checks and batch conflict rules). No autonomous coordination actor owns the decisive cross-S1 conflict policy in the reviewed standard distribution.
- Supporting / enforcement mechanisms: global file-operation lock; per-read file version tokens; pre-apply and pre-commit current-version checks; `E_VERSION_MISMATCH`; same-batch same-path conflict rejection; ordered file-mutation phase; bounded parallel sub-agent/tool execution.
- Closure path: parent launches independent sub-agents concurrently in one shared workspace → one S1 changes a file or otherwise advances its version → another S1 submits a mutation based on its earlier snapshot → first-party version/serialization machinery rejects the stale write rather than overwriting current state → the tool error enters that sub-agent's own model history → standard prompt directs it to re-read and choose a subsequent action from current state.
- Boundary reachability: parallel `subagent` calls and the shared built-in file tools are part of the standard Ally application; all local model-facing edits route through the application-owned file-operation lock/version checks, so the coordination path is directly reachable without application-side custom composition.
- Why this is / is not agent-owned: the S2 disturbance and feedback path are operationally closed, but the decisive conflict rule is encoded by the runtime. Removing any autonomous coordinator while retaining these mechanisms leaves materially the same stale-write arbitration, so the path is constructor/runtime-owned rather than `A`.
- Evidence: [`README.md`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/README.md); [`internal/app/biz_prompt.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/biz_prompt.go); [`internal/app/orch_subagent.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/orch_subagent.go); [`internal/app/app.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/app.go); [`internal/app/orch_edit.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/orch_edit.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic parallel tool batching is not the witness. The mapping depends specifically on concurrently executing delegated S1s sharing one workspace plus Ally's concrete stale-write/collision attenuation and returned error path.
- Distinct S1 units: independently executing model-backed sub-agents launched concurrently by the parent run, each with its own context/tool loop and bounded task while sharing the selected workspace.
- Inter-S1 disturbance: a sibling can change a file after another S1 has read it, making the latter's planned mutation stale and risking lost/overwritten work.
- Attenuating coordination relation: application-wide serialization of file operations plus version/hash comparison before apply/commit; stale or same-batch conflicting writes are refused rather than applied.
- Feedback into subsequent S1 behaviour: the rejected S1 receives `E_VERSION_MISMATCH`/conflict as a tool result; Ally's standard prompt requires a fresh read before a retry, so subsequent behavior is based on the coordinated current state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited path specifically detects and attenuates a shared-work mutation collision created by concurrent S1 execution and returns that regulation result to the affected S1.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-organization current-control function was established beyond task decomposition, sub-agent lifecycle visibility and deterministic runtime limits.
- Disturbance / variety regulated: not established at S3 ownership level.
- Decisive decision or feedback right: not established. The main actor can delegate independent subtasks and later consume their summaries, while the UI/runtime can show live sub-agent status and enforce concurrency/step limits; no distinct actor is shown holding a whole-system current view plus authority to revise shared resources, commitments, priorities or constraints on behalf of a persistent multi-S1 organization.
- Decision owner: not established.
- Supporting / enforcement mechanisms: sub-agent semaphore and step budgets; live run records/events; task descriptions/roles; plan tool; cancellation; background task/service tracking; scheduler limits.
- Closure path: not applicable; observed parent/sub-agent paths are task decomposition and bounded execution rather than a separately evidenced S3 regulation loop.
- Why this is / is not agent-owned: the main model can choose to delegate, but the Profile explicitly distinguishes delegation/task allocation from S3 whole-current regulation. Runtime concurrency and budgets enforce preset policy rather than supply organizational management discretion.
- Evidence: [`internal/app/orch_subagent.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/orch_subagent.go); [`internal/app/biz_prompt.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/biz_prompt.go); [`README.md`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: this does not deny useful orchestration or supervision; the missing evidence is the stronger whole-current organizational-control relation at the selected recursion.

### Absence scope

- Surfaces inspected: main model/tool loop; sub-agent spawn/run/status/result path; delegation prompt; plan tool/batch policy; concurrency/step limits; scheduled-task execution; background-service/task-center controls; UI-visible sub-agent state.
- Plausible first-party paths checked: parent allocation of subwork; live sub-agent monitoring; cancellation; concurrency budgets; scheduled work; plan revision; returned child summaries; current resource/commitment intervention.
- Why no material first-party path remains: located mechanisms either decompose the current user task, expose status or mechanically enforce preset bounds. No standard actor is assigned an organization-wide current-management mandate with substantive reallocation/accountability authority across ongoing S1s.

## S3* — Complementary audit

- State: —
- Function: no material sufficiently independent complementary audit role with a corrective return into organizational control was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. Ally instructs ordinary coding actors to verify their changes and allows a parent to delegate arbitrary research/work, but it does not ship a distinct independent reviewer/auditor path whose mandate is to challenge ordinary S1 claims using materially complementary access and return a verdict into later control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: command/test execution, validation attached to edits, live tool/run evidence, sub-agent reports and optional user inspection are ordinary operation/observability rather than an evidenced complementary-audit function.
- Closure path: not applicable; no standard independent challenge → audit judgment → corrective current-control path was found.
- Why this is / is not agent-owned: a developer/model could choose to use a generic sub-agent as a reviewer, but generic delegation capability does not meet the Methodology's function-first constructor threshold without a first-party audit-specific path and closure.
- Evidence: [`internal/app/biz_prompt.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/biz_prompt.go); [`internal/app/orch_subagent.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/orch_subagent.go); [`README.md`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: ordinary verification can be strong without being S3*; this assessment does not convert a flexible sub-agent primitive into `C` absent an audit-specific first-party construction path.

### Absence scope

- Surfaces inspected: standard prompt verification guidance; edit validation; command/test tools; sub-agent role/delegation path; run/tool event records; user-facing diff/review surfaces; repository tests/development tooling boundary.
- Plausible first-party paths checked: child-agent review roles; post-edit validation; test execution; user visual diff review; tool/run logs; independent model invocation paths.
- Why no material first-party path remains: all located runtime checking is either performed by ordinary S1 work, deterministic validation or generic optional delegation. No shipped audit-specific independent access/mandate plus corrective return was found.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-then organizational intelligence/adaptation loop was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Web/HTTP tools, cross-project memory, project lessons, skills, session history and scheduled tasks can provide information or persistence, but no standard actor turns external/future-relevant distinctions into options that change Ally's persistent organizational capability or strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `web_fetch`/HTTP; MCP/skills; durable memories and project lessons; persistent sessions; scheduled tasks; provider/model configuration.
- Closure path: not applicable; no prospective environmental sensing → adaptation-option formation → current capability change → subsequent operation path was found.
- Why this is / is not agent-owned: the coding S1 can research outside information and change its immediate task behavior, and can store reusable knowledge. That is not the Profile's stronger prospective organizational adaptation function without a capability/strategy return loop.
- Evidence: [`README.md`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/README.md); [`internal/app/biz_prompt.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/biz_prompt.go); [`internal/app/orch_subagent.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/orch_subagent.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: long-lived memory and future scheduled execution are not equivalent to future-oriented organizational intelligence/adaptation.

### Absence scope

- Surfaces inspected: web/HTTP and MCP/skill affordances; durable cross-project memory; project lessons; provider/model configuration; session persistence; scheduled-task execution; delegation/research prompt guidance.
- Plausible first-party paths checked: external research; future scheduled work; learned project lessons; reusable memory; skills/capability extension; model/provider changes; autonomous self-update/evolution paths.
- Why no material first-party path remains: located features retain knowledge, execute future instructions or expose operator-selected capabilities, but no first-party prospective actor develops adaptation options and returns them as persistent organizational capability/strategy changes.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy closure was established.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. Core safety/tool contracts, workspace boundaries, model/provider settings, project/custom instructions and user approvals constrain operation, but their authoritative purpose/policy values are developer/operator inputs rather than a runtime identity-level decision owned inside Ally.
- Decision owner: not established inside the assessed organization; ultimate task/policy authority remains external to the autonomous coding organization.
- Supporting / enforcement mechanisms: system-prompt priority rules; safety boundaries; workspace/path checks; command restrictions; user `ask` path; provider/model settings; project/custom instructions; scheduled-task configuration.
- Closure path: not applicable; no identity/ultimate-policy issue is shown reaching a qualifying first-party S5 owner and returning as an authoritative policy revision governing later operation.
- Why this is / is not agent-owned: Ally strongly enforces authored constraints and can ask the user operational questions, but enforcement and generic human approval do not establish S5 ownership under Profile 0.2.4.
- Evidence: [`internal/app/biz_prompt.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/biz_prompt.go); [`internal/app/app.go`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/internal/app/app.go); [`README.md`](https://github.com/Bronya0/ally-agent/blob/dafc35cdc2ff1bae6b89b0f9398448f752fc418d/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a rich safety policy and user-question tool can support governance without supplying runtime identity/ultimate-policy closure.

### Absence scope

- Surfaces inspected: system prompt priority/safety policy; `ask`/suggest tool handling; workspace and destructive-action restrictions; provider/model settings; project/custom/user-profile instructions; scheduler configuration; main/sub-agent prompt boundaries.
- Plausible first-party paths checked: policy revision by an agent; human approval/escalation; purpose/identity conflict handling; safety exceptions; model/provider and workspace policy changes; persistent returned governance decisions.
- Why no material first-party path remains: authoritative identity/policy remains developer/operator-authored and ordinary user interaction is operational. No dedicated ultimate-policy decision-and-return path at the assessed recursion was found.

## Assessment summary

Ally closes a strong autonomous coding S1 and, unlike a purely sequential single-agent harness, ships a concrete constructor-owned S2 relation for its parallel sub-agents. Concurrent children share one workspace, while first-party serialization and version checks reject stale/conflicting writes and return the conflict to the affected model loop for a fresh read/retry. That establishes S2 functionally but keeps ownership at `C`, because runtime policy—not an autonomous coordinator—makes the decisive conflict decision. Delegation/status/budgets do not by themselves establish S3; ordinary verification and flexible sub-agents do not establish S3*; memory/web/scheduling do not establish prospective S4; and strong authored safety policy does not establish S5.

Proposed vector: **`A · C · — · — · — · —`**.
