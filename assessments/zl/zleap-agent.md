---
harness_id: zleap-agent
project_name: Zleap-Agent
repository: https://github.com/Zleap-AI/Zleap-Agent
review_ref: 8aa5f07a20c535687ee39c6dccade7869ae27fad
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Zleap-Agent

## Review boundary

- System in focus: the source-distributed local Zleap workspace agent application, including Web/CLI, supported task worker and gateway compositions, at one operator-owned deployment recursion.
- Purpose and identity: carry out user work through model-driven, context-isolated workspaces with persistent conversation and memory.
- Relevant environment: users, local project files/processes, configured model providers, MCP tools, PostgreSQL/pg-boss and IM channels.
- Standard-distribution boundary: public preview source distribution; README-supported Web, CLI, tasks and gateway entry points. No private maintainer packaging or unpublished runtime is assumed.
- Credited operating / distribution surfaces: agent kernel/ChatEngine/workspace tool loop, ConversationService, core runtime/memory policy, task service/queue/execution/worker, Web task-management pages and routes.
- Adjacent first-party surfaces excluded from ownership: repository-development tests/CI, release/desktop packaging helpers and the real-agent experimental runner. Source comments referring to unpublished design documents are not evidence that those documents or modes were inspected.
- First-party operating / deployment modes considered: interactive or one-shot CLI, Web chat and plan/permission settings, operator-managed scheduled tasks with worker, shared gateway ConversationService. Custom constructors without supported wiring do not become autonomous controllers.
- Recursion level: one local operator's deployment and current task portfolio; workspace agents/runs are operational cells, not proof of recursive viable systems.
- Reviewed revision: `8aa5f07a20c535687ee39c6dccade7869ae27fad`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/README.md) describes separately packaged AI providers, core runtime, agent engine, avatar run assembly, runtime facades, store, CLI, Web, tasks and gateway. The [kernel](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/kernel/kernel.ts#L21-L80) enters the main workspace. Its model calls `switchWorkspace` to select a serial specialized operation; workspaces load scoped tools, skills, models, memory and histories. Tool results return to the model, and workspace results/handoffs return to Main with preserved overall goal and artifact references.

ConversationService loads history, resolves model/identity, invokes the engine and persists results. Per-service keyed locking protects a conversation's load/run/persist sequence; a configurable semaphore limits concurrent conversations. PostgreSQL holds session, memory and task state. Memory extraction, recall, compaction and offline dream processing support later context. Tool approvals and actor policies constrain access.

The Web task panel and API expose a per-owner portfolio and run history. TaskManagementService writes changes and synchronizes pg-boss schedules; TaskExecutionService re-reads enabled/deleted/task bindings before execution, and the worker creates a model run from current task configuration. Humans configure workspaces, models, skills, task schedules and permissions. These ordinary operator paths are distinct from OSS maintainer governance.

## Operational model

A workspace model agent selects tools to answer a user task or produce artifacts. Independent conversations and scheduled requests can run as separate operational outcomes; serial workspace steps contribute specialized transformations. Runtime transport/limits and storage support agent decisions.

Current-portfolio supervision has two evidenced forms: function-specific task-management surfaces usable to construct an agent controller, and a supported human-operator panel with run feedback and changes returned to worker execution. The ordinary Main prompt restricts task management to explicit user scheduling/history requests; it is not credited as an autonomous whole-portfolio supervisory policy.

## S1 — Operations

- State: A
- Function: complete user and scheduled work through model-selected specialized workspace tools.
- Disturbance / variety regulated: differing user tasks, workspace capabilities, tool errors, missing context and provider responses.
- Decisive decision or feedback right: choose workspace/action, interpret tool results and continue or conclude the assigned work.
- Decision owner: Main and specialized workspace model agents within host-selected scopes.
- Supporting / enforcement mechanisms: kernel/runtime tool invocation, scoped capability bindings, model adapters, turn limits, approvals, session persistence and compaction.
- Closure path: user/task input → Main/workspace model → tool result → subsequent model turn → workspace result/artifact and user reply.
- Boundary reachability: supported Web/CLI and task worker instantiate ConversationService/ChatEngine; the kernel invokes the registered workspace runtime. No external agent's vector is inherited.
- Why this is / is not agent-owned: task-specific next actions depend on model decisions, while deterministic machinery enforces preselected constraints.
- Evidence: [kernel dispatch](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/kernel/kernel.ts#L43-L80), [workspace tool loop](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/workspaces/turnLoop.ts), [Main switch path](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/engine/index.ts#L2143-L2228), [worker operation](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/tasks/src/worker.ts#L141-L195).
- Basis: structural.
- Confidence: high.
- Caveats: preview source availability; no empirical model reliability or viable-organization certification claimed.

## S2 — Coordination

- State: C
- Function: attenuate stale-history interference between conversation runs and repeated/cyclic workspace handoffs.
- Distinct S1 units: separately executing request/conversation agent runs and specialized workspace operations that can hand work onward.
- Inter-S1 disturbance: concurrent messages using one durable conversation could read stale history before either persists; workspace A → B → A handoffs or repeated completed dispatch can replay the same work.
- Attenuating coordination relation: keyed serialization around load/run/persist, visited-workspace/depth guards and duplicate-dispatch feedback carrying the previous completed result instead of executing again.
- Feedback into subsequent S1 behaviour: the next lock holder loads history after the prior run; blocked handoffs become returned failure/switch results and duplicate dispatch returns prior status/carry-back into Main's next context.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: source identifies the actual stale-read critical section and implements explicit re-entry/duplicate suppression. Generic workspace isolation or the switch API alone would not suffice.
- Disturbance / variety regulated: interacting runs' shared conversation state and workspace-chain oscillation.
- Decisive decision or feedback right: choose the serialized scope and cycle/replay suppression policy; autonomous revision of that coordination response remains to be composed.
- Decision owner: developer-selected deterministic policy at this boundary; no autonomous agent coordination regulator is supplied.
- Supporting / enforcement mechanisms: KeyedMutex, visited sets, depth ceiling and projected failure/duplicate tool results.
- Closure path: conflict candidate → fixed gate/lock → suppressed or delayed operation → returned state/current history → subsequent operational choice.
- Boundary reachability: ConversationService owns the mutex; shared worker/gateway compositions reuse a service. ChatEngine's chain/replay protection is on the standard workspace-dispatch path.
- Why this is / is not agent-owned: fixed mechanisms operate without agent discretion. They are function-specific first-party coordination paths supporting C, not evidence for A.
- Evidence: [identified critical section and lock](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/conversation/mutex.ts#L1-L34), [load/run/persist wiring](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/conversation/service.ts#L182-L272), [handoff-cycle suppression](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/engine/index.ts#L2364-L2409), [duplicate result return](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/engine/index.ts#L2454-L2475), [shared gateway service](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/gateway/src/worker.ts).
- Basis: structural.
- Confidence: high.
- Caveats: mutex is per service/process, not a distributed shared-file lock. Web constructs a service per request, so no claim of cross-request Web locking is made. Serial delegation by itself is not the positive witness.

## S3 — Inside-and-now control

- State: C(P)
- Function: supervise the operator-owned current scheduled-work portfolio and revise commitments, model/workspace allocation or execution constraints in response to current state.
- Whole-system current view: task panel/API lists the owner's tasks and recent runs; detail views retrieve run history, status, summaries/errors and next/last run information.
- Current-control decision scope: pause/resume/delete tasks, revise prompt/schedule, select model/project/workspace/permission mode, or request an immediate run. Scope is the visible owner's portfolio, not every tenant or hidden runtime.
- Disturbance / variety regulated: unwanted/repeated commitments, failed runs and unsuitable current task bindings or execution constraints.
- Decisive decision or feedback right: choose which current commitments/resources/constraints to change after reviewing the portfolio and its results.
- Decision owner: human deployment owner in P mode; autonomous supervisory judgment must be composed for the C mode.
- Supporting / enforcement mechanisms: authenticated actor/owner scope, task registry, schedule synchronization, pg-boss, worker task re-read and persisted run reports. Queue timeouts/reclaim are fixed enforcement, not autonomous S3.
- Closure path: operator sees task/run state → authoritative task update → service persists and synchronizes schedule → worker reads current configuration/enabled state → subsequent operation and new run feedback change.
- Boundary reachability: supported Web task pages call the task API and service; supported task worker consumes the same store/queue. Web chat separately wires the Main task-management tools to this service.
- Why this is / is not agent-owned: there is no shipped autonomous observe-portfolio/decide-intervention cycle. Main task tools are explicitly user-request-driven; autonomous regulation is a constructor possibility through the already function-specific ledger/update path.
- Evidence: [operator panel](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/web/components/manage/pages-task.tsx), [whole portfolio plus recent runs](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/web/app/api/tasks/route.ts#L8-L19), [scoped updates and schedule closure](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/tasks/src/service.ts#L19-L115), [worker enforces current task](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/tasks/src/execution.ts#L29-L73), [constructor tool](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/engine/index.ts#L2944-L3013), [Web tool wiring](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/web/app/api/chat/route.ts#L665-L731).
- Basis: structural.
- Confidence: medium-high.
- Caveats: P is current-control over this operator's deployment commitments; not a generic high-risk-tool approval and not organization-level governance. Pausing changes future dispatch; immediate cancellation of all already-running jobs is not claimed.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Autonomous portfolio-regulator actor/authority must be composed by developer | Current task-ledger/result distinctions | Existing list/update/run-now bindings and service/worker path can enforce chosen interventions; autonomous supervisory loop is not preconfigured | ChatEngine task_manage; Web ChatTaskManager; TaskManagementService |
| Parent (`P`) | Human owner of the local task portfolio | Operator reviews task/run history and current commitments | Task panel changes enabled state/bindings → authenticated API → schedule sync → worker reads updated task → new run feedback | pages-task.tsx; tasks route; service.ts; execution.ts; worker.ts |

## S3* — Complementary audit

- State: —
- Function: no material complementary independent operational audit loop supplied.
- Disturbance / variety regulated: ordinary execution errors, reported outcomes and context/memory quality.
- Decisive decision or feedback right: no separately owned independent audit judgment and corrective-return right established.
- Decision owner: producing runtime/model and operator handle ordinary run feedback.
- Supporting / enforcement mechanisms: run records, traces, artifact snapshots, sensitivity checks and repository tests.
- Closure path: ordinary production status/QA, not a separate complementary audit-to-control loop.
- Why this is / is not agent-owned: audit-named persistence or static checks do not provide an independent assessor with different access to operational reality.
- Evidence: [run audit projection](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/tasks/src/execution.ts#L11-L73), [ordinary workspace processing](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/workspaces/turnLoop.ts), [memory dream processing](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/memoryDream.ts#L212-L295).
- Basis: structural.
- Confidence: high.
- Caveats: arbitrary custom audit work can be added, but is not an evidenced shipped audit mode.

### Absence scope

- Surfaces inspected: workspace turn loop, artifact/result persistence, task run ledger/operator history, memory extraction/dream and deterministic package tests.
- Plausible first-party paths checked: independent workspace contexts, readMessage/raw artifacts, task audit projection, skill-sensitivity checks and offline memory extraction.
- Why no material first-party path remains: these provide operational checking, observability or context processing; no first-party audit-specific independence/judgment/feedback arrangement is supplied. A generic isolated workspace is not an independent auditor by itself.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective capability adaptation loop established.
- Disturbance / variety regulated: current requests, memory/context relevance and reusable operational lessons.
- Decisive decision or feedback right: no evidenced prospective adaptation-options decision linked to current capability regulation.
- Decision owner: task agents handle current work; operator configures capabilities and models.
- Supporting / enforcement mechanisms: workspace research, skill discovery, memory recall/experience extraction, dream reconciliation and configuration UI.
- Closure path: memories and skills re-enter future task context; this is not a distinct external/future adaptation conversation.
- Why this is / is not agent-owned: retrospective experience processing and generic tool/model selection alone do not close S4.
- Evidence: [dream payload and memory writes](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/memoryDream.ts#L212-L295), [memory orchestrator](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/core/src/memory/orchestrator.ts), [supported capabilities/entry points](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: externally informed research can be a user's ordinary task without constituting this deployment's S4.

### Absence scope

- Surfaces inspected: kernel/engine skill discovery and memory wiring, dream extraction, core context/recall policies, workspace/task configuration and supported deployment documentation.
- Plausible first-party paths checked: Web Search workspace, reusable experience memory, scheduled dream consolidation, model/workspace/skill changes and human capability configuration.
- Why no material first-party path remains: no shipped path develops prospective external adaptation options and negotiates their return into current whole-system capability; memory replay and operator edits lack that function-specific loop. No separate parent S4 mode is established merely by the configuration UI.

## S5 — Policy and identity

- State: —
- Function: no runtime ultimate-policy/organizational identity resolution loop supplied.
- Disturbance / variety regulated: task permissions, persona facts and access to shared memory/capabilities.
- Decisive decision or feedback right: no identity/ultimate-policy case routed to a legitimate ultimate authority with a specific returned governance decision.
- Decision owner: host/operator chooses persona and access settings; model applies them and stores allowed descriptive memory.
- Supporting / enforcement mechanisms: non-overridable soul rules, avatar/system configuration, approval modes and creator/admin restrictions on global self-memory.
- Closure path: configuration/memory affects context and tool permission; no distinct ultimate-policy adjudication process established.
- Why this is / is not agent-owned: persona text, agent nickname/self-facts and a high-risk-action approval are not identity-level regulatory closure.
- Evidence: [persona/rules distinction](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/soul.ts), [self-memory scope/actor policy](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/core/src/memory/orchestrator.ts), [runtime self-memory guidance](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/agent/src/engine/index.ts#L997-L1012), [tool policy](https://github.com/Zleap-AI/Zleap-Agent/blob/8aa5f07a20c535687ee39c6dccade7869ae27fad/packages/core/src/toolPolicy.ts).
- Basis: structural.
- Confidence: high.
- Caveats: legitimate operator authority exists, but only a function-specific closed S5 path would justify P.

### Absence scope

- Surfaces inspected: soul/persona composition, self-memory/actor role restrictions, Web/CLI approval paths, task permissions and public maintainer/deployment boundary.
- Plausible first-party paths checked: creator/admin global self-memory, avatar persona updates, system prompt overrides, irreversible-tool approval and user task configuration.
- Why no material first-party path remains: these are descriptive identity facts, static policy selection and operational permission control; none supplies a runtime identity/ultimate-policy issue/adjudication/returned governance loop at this deployment recursion.

## Distributed OSS parent arrangement

Apache-2.0 contributors maintain the preview source. No shared OSS organization governance is imported into locally installed deployments. The positive S3 parent is the legitimate local task-portfolio owner, not an inferred project-wide parent.

## Self-hosted and non-human modes

The supported Web/task-worker composition closes human current-control over the owner's current commitments. Generic plan/full-access modes are not independently promoted to S3/S4/S5. A custom unattended supervisory agent could compose the S3 constructor but is not reported as shipped A.

## Recursion

Separate workspace context, actor IDs and handoff depth do not establish complete local viable systems. No full recursive metasystem is claimed.

## Variety and escalation

Workspace-specific tool/context selection attenuates irrelevant context; original-message pointers, tool feedback and memory recall can restore omitted distinctions. Cycle guards and conversation locks attenuate concrete replay/stale-state interference. Permission denial, failed task records, model/tool limits and pg-boss retry/dead-letter states are ordinary exception machinery; no separate algedonic function follows from status labels.

## Evidence gaps

The pinned public source was inspected without private design/release material. No live model, provider, database, gateway or scheduled job was executed. Node/npm/pnpm were unavailable on the inspection hosts, so native TypeScript tests were not run; repository tests were inspected as corroborating source only. Source-based function/ownership findings do not claim operational reliability. Structural and Index validation receipts belong to batch #2194.
