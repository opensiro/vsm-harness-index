---
harness_id: yielded-agent
project_name: Yielded Agent
repository: https://github.com/yielded-dev/agent
review_ref: 1866af9f9ec153f7db0ba56d76082e9a34a2e660
reviewed_at: 2026-10-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Yielded Agent

## Review boundary

- System in focus: The shipped model-backed **agent execution cell** of the `@yielded/agent` library, in its supported TypeScript/Effect in-memory or durable Thread/Run modes and example application hosts. The credited organizational activity is a configured first-party Agent Definition being executed by the agent runtime with user-supplied model services and tool handlers, not the unrelated enterprise operating the application.
- Purpose and identity: Convert application-authorized user input into typed goal-seeking model/tool decisions and bounded tool results, with durable continuation/recovery of a logical Run where configured.
- Relevant environment: Application-defined requests, effect/ai model outputs, tool results/handler failures, host identities/authorizers, durable storage, process interruptions and recovery, optional subagent workers, peer messages and workflow dispatch.
- Standard-distribution boundary: `packages/effect-agent/src/core`, `engine` and `durable` shipped library; packaged `packages/workflow`, `packages/platform-node`, `packages/platform-cloudflare`, and `packages/storage-*` first-party supported modes. External application authorization/model/tool business logic, arbitrary independently designed specialist teams, operator policies, hosted providers, databases and service deployments are not silently assigned organizational ownership.
- Credited operating / distribution surfaces: [README.md](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/README.md#L1); [packages/effect-agent/src/engine/AgentRuntime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/AgentRuntime.ts#L37); [packages/effect-agent/src/engine/internal/agent-runtime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/internal/agent-runtime.ts#L8960); [packages/effect-agent/src/engine/ToolBroker.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/ToolBroker.ts#L1); [packages/effect-agent/src/durable/DurableAgentRuntime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/DurableAgentRuntime.ts#L1); [packages/effect-agent/src/durable/WorkerHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/WorkerHost.ts#L1); [packages/effect-agent/src/engine/MessagingHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/MessagingHost.ts#L1); [packages/workflow/src/WorkflowExecution.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/workflow/src/WorkflowExecution.ts#L1); [docs/src/content/docs/concepts/runtime-model.mdx](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/docs/src/content/docs/concepts/runtime-model.mdx#L1).
- Adjacent first-party surfaces excluded from ownership: Product/application-specific goals and policies, user-selected provider/model Layer, host-supplied authorization and tool handlers, underlying Effect AI LanguageModel clients, remote model inference and tool services, operator-run recovery administration, and README/example program configuration. Shipped optional capabilities are still reviewed as plausible first-party paths but not promoted beyond their proved owner/closure.
- First-party operating / deployment modes considered: `AgentRuntime.run`, `start`, `stream` and durable single-owner Thread/Run/Attempt runtime; Node and Cloudflare host adapters, in-memory/SQL-backed storage, optional subagent worker capabilities, bounded workflow dispatch and peer messaging. Tool approval/reconciliation/recovery, steering/follow-up, direct and programmatic tools, compacted context, and structured agent updates are included in negative-path checks. Application-provided Layers/config must be supplied for real execution.
- Recursion level: One configured model-backed Agent Definition working a Thread/Run as the accountable S1 activity. A host may spawn additional agent Threads or peers, but their existence does not imply an evidenced whole organization with autonomous coordination, metasystem or legitimate parent at this declared boundary.
- Reviewed revision: `1866af9f9ec153f7db0ba56d76082e9a34a2e660` (GitHub repository ID 1316603236); independent clean Git tree `85cf76ddc5e00d8fc8ae466250b6f3aa9f95f646`, frozen in [Index batch #1729](https://github.com/opensiro/vsm-harness-index/issues/1729).
- Observation date: 2026-10-19; Profile 0.2.4 / Methodology 0.3.7; immutable generation pair matches current initial procedure.

## Repository architecture

Yielded Agent exposes typed `Agent.make` definitions (input/output schemas, instructions, toolkit, bounded policy) and `AgentRuntime.run/start/stream` interpreter entrypoints. In the supported app-composed Layer mode, its execution turn loop obtains the actual LanguageModel service, sends prompt/context/tool declarations, handles the model's response/tool requests, dispatches declared executable handlers with policy and approval checks and then incorporates settled tool results into subsequent model turns. The source's `while (request !== undefined)` advancing `makeTurn` / `makeResumeTurn` / `NextTurn` is a first-party control/feedback path, distinct from a static example or a deterministic call graph with no model action discretion. [README.md](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/README.md#L1); [packages/effect-agent/src/engine/AgentRuntime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/AgentRuntime.ts#L36); [packages/effect-agent/src/engine/internal/agent-runtime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/internal/agent-runtime.ts#L8960); [packages/effect-agent/src/engine/internal/agent-runtime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/internal/agent-runtime.ts#L8637); [packages/effect-agent/src/engine/ToolBroker.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/ToolBroker.ts#L8).

In durable mode, a Thread is one conversation and one host-routed process owner; a Run is logical work, an Attempt is one period advancing it, and a Turn is one model response and settled tool batch. The host admits input, retains obligations and checks authority, settles validated outcomes in declared order and recovers from interrupted attempts without promising exactly-once external side effects. Admission/recovery, steering, audit fields, idempotency, budgets and single-writer storage preserve task continuity and limit operations; these properties alone do not establish a separate governing whole-current S3 owner. [docs/src/content/docs/concepts/runtime-model.mdx](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/docs/src/content/docs/concepts/runtime-model.mdx#L1); [packages/effect-agent/src/durable/WorkerAdmission.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/WorkerAdmission.ts#L1); [packages/effect-agent/src/durable/RunContinuation.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/RunContinuation.ts#L1); [packages/effect-agent/src/durable/ToolReconciler.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/ToolReconciler.ts#L1); [packages/effect-agent/src/durable/OperationAuthorizer.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/OperationAuthorizer.ts#L30).

First-party optional `SubagentHost` can create task workers whose models/tools remain separately configured; `MessagingHost` defines peer send/reply/inbox/inspect/retry operations. Its trusted peer route and authorizer are expressly **application-owned**, and the default unavailable/deny implementations forbid unconfigured interactions. `WorkerHost` configures an authorization-bounded slot ceiling and worker admission rules; `packages/workflow` exposes typed planned workflow execution. These are useful capabilities for composing organizations but not source evidence that the default library owns a concrete conflict-specific inter-S1 coordination decision, executive resource adjustment, autonomous audit or strategy/identity policy. [packages/effect-agent/src/engine/SubagentHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/SubagentHost.ts#L16); [packages/effect-agent/src/engine/MessagingHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/MessagingHost.ts#L21); [packages/effect-agent/src/engine/MessagingHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/MessagingHost.ts#L68); [packages/effect-agent/src/durable/WorkerHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/WorkerHost.ts#L92); [packages/workflow/src/WorkflowExecution.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/workflow/src/WorkflowExecution.ts#L1).

`AgentUpdates.Update` is a schema-encoded intermediate **run-scoped output** with immutable idempotency and input validation, not a demonstrated autonomous update of the agent's enduring strategic instructions or deployment policy. `ToolBroker` permits bounded model-programmatic tool invocations and records outcomes; error diagnostics, retries, checkpoints, usage accounting and persisted events support reliable operation, not automatically complementary S3* auditor ownership. [packages/effect-agent/src/core/AgentUpdates.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/core/AgentUpdates.ts#L8); [packages/effect-agent/src/engine/ToolBroker.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/ToolBroker.ts#L10); [packages/effect-agent/src/durable/RunJournal.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/RunJournal.ts#L1).

## Operational model

The real operational transformation is goal-conditioned model choice of the next available tool action or typed completion, followed by actual tool outcome processing and potentially another turn. In durable mode the same logical Run is resumed after a process interruption under host-issued authority and bounded accounting. App Layer/tool/authorization choices and deterministic job/ledger rules bound S1 activity but are not model-owned S2/S3/S3*/S4/S5 organizational rights.

## S1 — Operations

- State: A
- Function: Select context-dependent model-generated tool calls or final structured output and advance work on an application-defined task.
- Disturbance / variety regulated: Different task inputs, partial tool results, handler failures, dynamic model output, resumed history and user follow-up/steering.
- Decisive decision or feedback right: Configured model creates action/tool selections based on accumulated prompt and current task; the interpreter executes authorized tool calls and supplies settled results for subsequent model turns.
- Decision owner: The model-backed Agent Definition in the shipped interpreter operating mode, with the external model as cognition supplier; host authorization limits what can be enacted but does not ordinarily choose the substantive next tool.
- Supporting / enforcement mechanisms: Effect Layers, policy budgets, tool schemas, ordered tool batches, tool broker, host admission, durable journal/recovery, approvals, thread history and compacted context.
- Closure path: App-authorized task/input → assembled model prompt and declared toolkit → model-selected tool arguments/terminal output → validated and authorized handler execution → settled tool result/history update → repeated model turn or structured result/durable settlement.
- Boundary reachability: The published `AgentRuntime.run(triage, ...)` and durable host examples connect model/Layer/toolkit services to the exported runtime; `makeTurn` and `NextTurn` handle repeated model/tool feedback. External providers are required to operate but no custom agent-loop implementation is needed.
- Why this is / is not agent-owned: Without the configured model, the interpreter can validate, recover and dispatch only already-determined work but cannot produce unfamiliar task-specific tool selections. The model is the decisive S1 action owner; deterministic orchestration is a support mechanism.
- Evidence: [README.md](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/README.md#L1); [packages/effect-agent/src/engine/AgentRuntime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/AgentRuntime.ts#L36); [packages/effect-agent/src/engine/internal/agent-runtime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/internal/agent-runtime.ts#L8637); [packages/effect-agent/src/engine/internal/agent-runtime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/internal/agent-runtime.ts#L8960); [packages/effect-agent/src/engine/ToolBroker.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/ToolBroker.ts#L8); [docs/src/content/docs/concepts/runtime-model.mdx](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/docs/src/content/docs/concepts/runtime-model.mdx#L12).
- Basis: Explicit shipped model-to-tool-to-next-turn execution loop.
- Confidence: High for supported first-party structural capability, not measured production success or model quality.
- Caveats: Application configuration, real provider and tool handlers are required; no external provider inference was performed in this source inspection.

## S2 — Coordination

- State: —
- Function: No first-party coordination process was shown that judges and attenuates concrete mutual interference among independently viable S1 workers, with the decision changing the competing units' subsequent operation.
- Disturbance / variety regulated: Concurrent subagents, peer messages, worker slot contention, per-Thread delivery and shared model-call budgets could introduce interference in host applications, but the published API alone does not identify a source-grounded shared operational conflict and distinct adaptive regulator.
- Decisive decision or feedback right: The application supplies peer routing/authorization and worker policy; the framework enforces declared grants, slot counts, idempotency and message delivery. Model-based parent delegation is a task choice; no bundled coordination owner demonstrably arbitrates opposing S1 demands.
- Decision owner: Host-defined policies/routing and deterministic worker/session enforcement; parent model may choose subtask but no separate conflict-specific S2 mandate is evidenced.
- Supporting / enforcement mechanisms: `MessagingHost` send/reply/inbox, `PeerRoutes`, `PeerAuthorizer`, `WorkerHost` capacity/authorization, tool-batch ordering and workflow dispatch.
- Closure path: Parent chooses child or sends configured peer message → authorized delivery/worker completion → result back to task owner; no concrete inter-unit oscillation → S2-specific judgment/attenuation → regulated feedback to affected workers is wired by the standard default.
- Why this is / is not agent-owned: Existence of multiple running models and peer messaging establishes possible interactions, not a distinct coordination function; resource grants and queues mechanically enforce host-provided configuration.
- Evidence: [packages/effect-agent/src/engine/SubagentHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/SubagentHost.ts#L16); [packages/effect-agent/src/engine/MessagingHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/MessagingHost.ts#L21); [packages/effect-agent/src/engine/MessagingHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/MessagingHost.ts#L68); [packages/effect-agent/src/durable/WorkerHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/WorkerHost.ts#L92); [packages/workflow/src/WorkflowExecution.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/workflow/src/WorkflowExecution.ts#L1).
- Basis: Bounded negative after direct subagent/peer/workflow source audit under the declared shipped library boundary.
- Confidence: Medium-high.
- Caveats: A particular host application could build a real autonomous S2 on top; that independent composition cannot be presumed here.

### Absence scope

- Surfaces inspected: Shipped SubagentHost, MessagingHost, WorkerHost worker capacity, workflow interfaces, app-owned peer routing and authorizer.
- Plausible first-party paths checked: Concurrent children, peer send/reply/retry and mailbox, worker slot pressure, run/turn ordered tool dispatch.
- Why no material first-party path remains: No source-grounded inter-S1 disturbance-specific adjudicator and returned adaptive stabilization path is assigned to a first-party actor rather than host configuration or deterministic transport.


## S3 — Inside-and-now control

- State: —
- Function: No autonomous whole-current operational management over a portfolio of independent S1 units with discretionary binding resource and commitment reallocation is established.
- Disturbance / variety regulated: Interrupted Runs, uncertain external effects, budget saturation, authority revocation, failed tool results and pending work are serious present-state conditions; the library maintains safety/accounting rather than allocating autonomous whole-system priorities.
- Decisive decision or feedback right: Application/host owner decides authorization and max worker permits; deterministic worker/runtime machinery enforces exact admission/recovery/abort/settlement and can retry/park based on retained state.
- Decision owner: Host application for durable authority, user/provider limits and legitimate workload priorities; runtime for mechanical enforcement, S1 model for local task choice.
- Supporting / enforcement mechanisms: One-owner Thread routing, worker receipts, WAL/journal/ledger, CAS, budget checks, reconciliation, scheduling alarms, admission queues and approval machinery.
- Closure path: Run interruption, pending receipt, failed operation or quota limit → host-owned grants/recovery rules → resume/park/fail current task; no independent whole-current management decision → changed multi-S1 commitments feedback is shown.
- Why this is / is not agent-owned: Run lifecycle coordination/limits are explicit, but infrastructure ownership of bookkeeping is not a discretionary S3 executive authority. Multiple processes and database tables do not change that.
- Evidence: [docs/src/content/docs/concepts/runtime-model.mdx](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/docs/src/content/docs/concepts/runtime-model.mdx#L13); [packages/effect-agent/src/durable/WorkerAdmission.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/WorkerAdmission.ts#L1); [packages/effect-agent/src/durable/WorkerHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/WorkerHost.ts#L92); [packages/effect-agent/src/durable/RunContinuation.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/RunContinuation.ts#L1); [packages/effect-agent/src/durable/OperationAuthorizer.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/OperationAuthorizer.ts#L53).
- Basis: Bounded absence after inspection of host-authority and durable operational control paths.
- Confidence: Medium-high.
- Caveats: Higher-recursion service fleet management would need its own first-party operating/parent-governance evidence, not a presumed runtime library grade.

### Absence scope

- Surfaces inspected: Thread/Run/Attempt runtime model, WorkerAdmission, WorkerHost, durable storage/continuation, model-steering, scheduling and operation authorization.
- Plausible first-party paths checked: App-defined worker allocations, new request admission, recovery/abort, pending operations and tool approval.
- Why no material first-party path remains: The source assigns mandate and priorities to the surrounding application/host while framework operations are constrained by recorded approvals, quotas and recovery rules; no first-party discretionary whole-current regulator and cross-S1 return is connected.


## S3* — Complementary audit

- State: —
- Function: No independently mandated complementary audit of an S3 executive's operational reports with corrective findings returned to organizational current-control is established.
- Disturbance / variety regulated: Uncertain external mutations, duplicate receipts, corrupt checkpoint history and inconsistent worker state can be detected or reconciled; these are integrity and durability checks, not automatically an independent organizational reality audit.
- Decisive decision or feedback right: Source checks persisted execution evidence, signatures/digests, tool outcomes, authorizer grants and reconciliation receipts; no separately authorized auditor chooses a corrective organizational intervention based on independent operational evidence.
- Decision owner: Deterministic runtime validators/recovery and the host's supplied reconciler; any outside evaluator of run results belongs to the app, not the default harness.
- Supporting / enforcement mechanisms: `ToolReconciler`, storage conformance tests, RunJournal, submission/receipt consistency, error classification and settlement diagnostics.
- Closure path: Integrity or uncertain tool result → typed validation/reconciliation/blocked settlement → current Run resumption or failure; no independent audit finding → S3 corrective authority → changed regulated operation.
- Why this is / is not agent-owned: A complete journal or reproducible trace can be useful evidence for human audit but does not act as a separately empowered S3* agent or complementary corrective institution.
- Evidence: [packages/effect-agent/src/durable/ToolReconciler.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/ToolReconciler.ts#L1); [packages/effect-agent/src/durable/RunJournal.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/RunJournal.ts#L1); [packages/effect-agent/src/durable/OperationAuthorizer.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/OperationAuthorizer.ts#L1); [packages/effect-agent/src/durable/Certification.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/Certification.ts#L1); [packages/effect-agent/src/engine/ToolBroker.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/ToolBroker.ts#L50).
- Basis: Bounded negative for claimed autonomous complementary audit at shipped library recursion.
- Confidence: Medium-high.
- Caveats: Consistency checking and tool reconciliation remain material engineering controls even though they do not establish this VSM function.

### Absence scope

- Surfaces inspected: RunJournal, ToolReconciler, operation authorizer, certification/conformance and tool execution record/diagnostic paths.
- Plausible first-party paths checked: Durable replay integrity, external unknown side-effect reconciliation, audit events, saved receipts and optional app examination.
- Why no material first-party path remains: These implement deterministic history and recovery safeguards or app-owned repair rather than a separate independent operational reality investigator with an empowered corrective return to S3.


## S4 — Outside-and-then intelligence

- State: —
- Function: No packaged prospective environmental scan → alternative strategy → authorized adoption → changed future organizational capability cycle is evidenced.
- Disturbance / variety regulated: Changing user input, model context saturation and provider/tool disruptions can require task-level adaptation; model steering, compaction, memory and agent updates are not by themselves future strategic institutional adaptation.
- Decisive decision or feedback right: The app declares an Agent Definition, model/tool Layers and configuration. A first-party `AgentUpdates.Update` records validated schema-constrained intermediate Run output; there is no demonstrated agent-owned decision that deploys a new durable agent capability/policy after evaluating future opportunities.
- Decision owner: External application/developer for enduring strategy/agent definition; current task model for S1 action content; runtime for update emission and history persistence.
- Supporting / enforcement mechanisms: Context compaction, thread history, structured AgentUpdates, optional memory/storage, tool and model selection Layers, run updates and workflow API.
- Closure path: Observations and model updates → current run/context or app-facing record; no default source-wired prospective options and binding adoption feedback into later independent organizational operations.
- Why this is / is not agent-owned: `AgentUpdates` is explicitly a schema-encoded intermediate output scoped to one logical Run, not autonomous alteration of `Agent.make` definitions and operating policy. Changing developer supplied Layers in a future application is outside this first-party function.
- Evidence: [packages/effect-agent/src/core/AgentUpdates.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/core/AgentUpdates.ts#L8); [packages/effect-agent/src/engine/Compaction.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/Compaction.ts#L1); [packages/effect-agent/src/engine/AgentRuntime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/AgentRuntime.ts#L36); [docs/src/content/docs/concepts/runtime-model.mdx](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/docs/src/content/docs/concepts/runtime-model.mdx#L77); [README.md](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/README.md#L1).
- Basis: Bounded negative after separating update, context/history and static application definition from prospective strategy.
- Confidence: Medium-high.
- Caveats: Future self-evolving applications can be built on this toolkit; the toolkit's shipped configuration does not prove one.

### Absence scope

- Surfaces inspected: Structured AgentUpdates emission, context compaction/history, memory and model selection interfaces, platform workflow hosts.
- Plausible first-party paths checked: Model-generated update events, context summarization, durable histories, dynamic task steering and source-defined model Layers.
- Why no material first-party path remains: No first-party actor owns an outside-and-then environmental alternative and binds its adoption to later autonomous organizational capability; emitted updates are current Run data and persistent configurations remain app-controlled.


## S5 — Policy and identity

- State: —
- Function: No first-party ultimate-purpose/identity policy arbitration and returned constitutional decision into later operation is established.
- Disturbance / variety regulated: Competing users' permissions, tool authorization, process recovery and host access boundaries require enforcement, not autonomous determination of the app organization's identity or enduring mission.
- Decisive decision or feedback right: The host application supplies authorization, tool handlers, models and policy ceilings; built-in authorization validates possession and explicit grants or denies operation. No independent first-party S5 authority settles an identity/ultimate-purpose matter.
- Decision owner: Host/operator/developer and application principal for ultimate goals and scope; local model for authorized task actions.
- Supporting / enforcement mechanisms: `OperationAuthorizer`, `PeerAuthorizer`, worker policy config, typed agent declarations, static tool schemas, approval/denial and audit trails.
- Closure path: Existing host policy → runtime admission/denial or tool approval → local S1 operation; no surfaced ultimate-purpose disagreement → legitimate identity/policy decision → revised enduring authorization/mission.
- Why this is / is not agent-owned: Enforcing external grants is not choosing ultimate ends, and peer authorization carries an externally specified principal rather than a legitimate in-boundary parent policy mode.
- Evidence: [README.md](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/README.md#L1); [packages/effect-agent/src/durable/OperationAuthorizer.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/OperationAuthorizer.ts#L30); [packages/effect-agent/src/engine/MessagingHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/MessagingHost.ts#L68); [packages/effect-agent/src/durable/WorkerHost.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/durable/WorkerHost.ts#L67); [packages/effect-agent/src/engine/AgentRuntime.ts](https://github.com/yielded-dev/agent/blob/1866af9f9ec153f7db0ba56d76082e9a34a2e660/packages/effect-agent/src/engine/AgentRuntime.ts#L36).
- Basis: Source-bounded negative after inspecting app-owned authority/approval and identity boundaries.
- Confidence: Medium-high.
- Caveats: The application operator's genuine human S5 governance is not a first-party agent/parent mode without source evidence of an intake–decision–return process.

### Absence scope

- Surfaces inspected: Host authority declarations, OperationAuthorizer/PeerAuthorizer, WorkerHost grants, agent definition policy, run approval and admission.
- Plausible first-party paths checked: User/host task objectives, permission checks, peer access, worker policy bounds and human intervention.
- Why no material first-party path remains: No first-party empowered actor arbitrates enduring identity or ultimate purpose and sends a legitimate binding governance decision into future operational configuration.


## Recursion

The assessed primary S1 is one configured agent definition operating a Thread/Run. Additional worker Threads, peer messages, and workflows allow optional higher-recursion compositions, but their app-provided route/authority/strategy determine whether actual separate S1 units, S2 regulation and metasystem governance arise. These external assemblies are not imputed to the shipped default agent cell.

## Variety and escalation

Agent tool/model turns absorb task/observation variety. Policies, approvals, reconciliation, backpressure, subscriptions, journaling and scheduled wakes bound risks and persist work. A status flag or pending receipt is not by itself an algedonic signal, a newly owned management right or a first-party S5 escalation route. External host decides if/how it will be escalated.

## Evidence gaps

- Frozen exact-first-party source and official docs were read; no live model inference, Cloudflare/Node service deployment, database recovery experiment or production inter-agent coordination session is claimed.
- The running application's configured authorization and peer routes are intentionally external service inputs; no particular multi-agent business organization can be inferred from the mere existence of library interfaces.
- Negative states are bounded to the shipped first-party standard distribution/modes at this ref, not assertions that all future host applications cannot implement those functions.
- This proposed assessment is not included in the canonical catalog, signature or derived cohort outputs until a separately validated admission PR.
