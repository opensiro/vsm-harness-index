---
harness_id: awaken
project_name: Awaken
repository: https://github.com/awakenworks/awaken
review_ref: 2b0d375004ec8723cf40d8a59c0bb486ebce57e0
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Awaken

## Review boundary

- System in focus: one first-party Awaken runtime/server organization at pinned revision `2b0d375004ec8723cf40d8a59c0bb486ebce57e0`, including the Rust agent execution loop, typed tool/state machinery, durable run/mailbox dispatch, worker/lease/retry recovery, run-control service, HITL suspension/resume paths, persisted run/event state and shipped Admin/REST control-plane surfaces.
- Purpose and identity: execute long-running observable AI-agent work through model-selected tools and structured state while making runs durable, recoverable, steerable and operable across local or distributed worker execution.
- Relevant environment: user/operator requests and interventions, model-provider responses, tool outputs and external services, durable thread/run state, concurrent dispatch workers, failures/restarts, provider/MCP availability and parent-authored runtime configuration.
- Standard-distribution boundary: the reusable first-party Awaken runtime/server/worker and shipped admin/control APIs at the pinned revision. External model endpoints, MCP servers, user applications, hosted tenant/auth products and downstream business tools are dependencies and do not donate VSM ownership.
- Credited operating / distribution surfaces: `awaken-runtime` loop runner and tool execution; runtime state/conversation feedback; `awaken-server` run service and routes; mailbox `RunDispatch` lifecycle, priority, leases, retries, interrupt/supersession and recovery; `awaken-worker`; run persistence; HITL decision/resume paths; Admin Console dashboard and REST list/cancel/steer/interrupt controls.
- Adjacent first-party surfaces excluded from ownership: repository CI/contributor workflows; offline `awaken-eval` / `awaken-eval-harness` datasets and reports where they are not wired into ordinary corrective control; documentation examples; tracing/profiling/observability surfaces that only expose evidence; configuration editing as such; benchmark/development tooling that is not part of the assessed operating loop.
- First-party operating / deployment modes considered: direct in-process agent execution; server-backed durable runs; queued mailbox execution with local or distributed workers; background child-agent execution; attended HITL suspension/resume; attended operator current-control through shipped Admin/REST surfaces.
- Recursion level: one running Awaken server/runtime organization is the system-in-focus. Individual model-driven agent runs and background child-agent runs are operational units where they directly execute outcomes; queue workers and transport replicas are supporting runtime machinery unless they themselves own an operational agent decision loop.
- Reviewed revision: `2b0d375004ec8723cf40d8a59c0bb486ebce57e0`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Awaken ships a substantive first-party agent execution loop rather than a provider proxy. `LoopRunner` owns model invocation, conversation/state, tools, budgets and cancellation. Each step constructs the model request with the currently available tools, receives model-selected tool calls, executes those tools, appends tool results back into the conversation and returns `Continue` for another inference step until a completion, suspension, stop, cancellation or budget condition closes the run. The model therefore chooses substantive operational actions while the runtime owns execution and observation return.

Durability and control are separated from model choice. The server persists `RunRecord` state and uses `RunDispatch` for delivery. The mailbox supplies priority, atomic single-winner claims, claim tokens, lease extension/recovery, retry/backoff, dead-lettering and dispatch epochs. `interrupt_then_queue` bumps the epoch, supersedes stale queued work, cancels the active run and queues newer input; `steer` can target the live run first and fall back to durable delivery. These are strong current-work regulation mechanisms, but their scheduling/control regime is deterministic/configured rather than an autonomous metasystem actor.

Awaken also ships a whole-system operator view. `/v1/runs/summary` aggregates current `Running`, `Waiting` and `Created` run counts for the Admin dashboard, and the first-party run surfaces list individual current runs. The Admin/REST control plane can cancel runs, steer active work, interrupt an active run and replace it with newer queued input, or resume/cancel suspended tool calls. That closes a legitimate parent-governed current-control mode. The base machinery itself is constructor-owned, so S3 is `C(P)` rather than `A`.

The same evidence does not establish S2. Awaken supports child agents, cross-thread durable messages and distributed workers, and its mailbox prevents duplicate claims of one dispatch. However the reviewed standard distribution does not identify a concrete conflict/oscillation among distinct autonomous S1 units together with a coordination relation specifically intended to attenuate that inter-S1 disturbance. Handoff, mailbox delivery, atomic dispatch ownership and generic worker coordination remain routing/execution mechanisms at this recursion unless that missing functional relation is established.

Evaluation, replay, tracing and profiling are also not credited as S3*. The Admin Console can capture trace fixtures and run datasets/evals, but those are evaluation/observability surfaces adjacent to ordinary operation. At the assessed boundary there is no packaged complementary audit path that independently challenges a specific ordinary S1/S3 claim and necessarily returns findings into corrective current control. HITL approval likewise evaluates a pending action in the ordinary production path rather than supplying a materially independent complementary audit channel.

No S4 closure is established. Durable history, replay, current steering, retries, config restoration and offline evaluation can inform future human engineering, but the standard operating distribution does not autonomously or constructor-specifically turn external/future distinctions into adaptation options and return a selected capability change into S3/S1. Likewise, prompts, permission rules, provider/tool configuration and Admin publishing do not establish S5: they configure or enforce already-selected operating policy, without an identified identity/ultimate-policy issue and legitimate ultimate authority closure at the declared recursion.

Primary evidence:

- [`README.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/README.md) — shipped runtime/server boundary, model/tool execution, durable workflows, dispatch, HITL and operational surfaces.
- [`crates/awaken-runtime/src/loop_runner/orchestrator.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-runtime/src/loop_runner/orchestrator.rs) — repeated step execution and run-loop termination/continuation control.
- [`crates/awaken-runtime/src/loop_runner/step.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-runtime/src/loop_runner/step.rs) — model request construction, tool-call selection/execution, tool-result observation return and next-step continuation.
- [`crates/awaken-server/src/run_dispatch.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-server/src/run_dispatch.rs) — direct/queued dispatch integration and durable execution handoff.
- [`apps/www/src/content/docs/explanation/hitl-and-mailbox.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/explanation/hitl-and-mailbox.md) — executable mailbox semantics: priority, leases, claim ownership, retry/recovery, steer, interrupt/supersession, HITL and run-control closure.
- [`crates/awaken-server/src/services/run_service.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-server/src/services/run_service.rs) — whole-system current run summary and run list/get service.
- [`crates/awaken-server/src/routes.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-server/src/routes.rs) — first-party run list/start/get/input/cancel/control route family.
- [`apps/www/src/content/docs/reference/admin-console.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/reference/admin-console.md) — shipped Admin control plane, live workload dashboard, current run control, config, audit and eval surfaces.

## S1 — Operations

- State: A
- Function: execute agent objectives through a repeated model/tool/observation loop that changes action in response to current conversation, state and tool results.
- Disturbance / variety regulated: request ambiguity, external/tool results, structured run state, failures, pending tool outcomes and intermediate evidence that changes the next useful operational action.
- Decisive decision or feedback right: choose which exposed tool calls to make and with what arguments, interpret returned observations and decide whether to continue acting or produce a completion within runtime bounds.
- Decision owner: the model-driven Awaken agent running through the first-party loop runner.
- Supporting / enforcement mechanisms: model adapters, tool registry/executor, structured state, conversation history, budgets, cancellation, policy/permission plugins, persistence and event emission.
- Closure path: run input enters the runtime → model receives current messages/state and tool schemas → model chooses tool calls or response → runtime executes tools → tool results are appended as observations → subsequent inference chooses the next action or completes → final result returns to the run environment.
- Boundary reachability: the standard `Agent::run` / server run paths execute this first-party loop without requiring a downstream organization to implement the action/feedback cycle.
- Why this is / is not agent-owned: deterministic runtime machinery constrains and executes choices but does not predetermine the substantive sequence of tool selections. Removing the model actor removes the ordinary operational decision path.
- Evidence: [`crates/awaken-runtime/src/loop_runner/orchestrator.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-runtime/src/loop_runner/orchestrator.rs); [`crates/awaken-runtime/src/loop_runner/step.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-runtime/src/loop_runner/step.rs); [`README.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: direct server/run-control transitions, retries and policy gates are deterministic. `A` rests on the substantive model-owned operational tool/action path, not on every runtime transition being autonomous.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination relation is established at the declared Awaken recursion under the pinned revision.
- Disturbance / variety regulated: no specific inter-S1 conflict/oscillation with a qualifying attenuation relation is established.
- Decisive decision or feedback right: not established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: child-agent inboxes, durable cross-thread mailbox messages, handoff/delegation, priority queues, atomic dispatch claims, leases, retry/backoff, dedupe and distributed worker ownership.
- Closure path: messaging and dispatch paths move or serialize work, but the reviewed evidence does not establish a concrete inter-S1 disturbance and a coordination result fed back to alter the participating S1 units specifically to attenuate that disturbance.
- Why this is / is not agent-owned: model-driven child agents can communicate and the mailbox can ensure one worker owns a dispatch, but communication/delivery/worker mutual exclusion are not S2 by themselves. No autonomous or constructor-owned inter-S1 coordination decision right is established at this system boundary.
- Evidence: [`apps/www/src/content/docs/explanation/hitl-and-mailbox.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/explanation/hitl-and-mailbox.md); [`crates/awaken-runtime/src/extensions/background/manager.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-runtime/src/extensions/background/manager.rs); [`crates/awaken-server-contract/src/contract/mailbox.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-server-contract/src/contract/mailbox.rs).
- Basis: explicit + structural absence
- Confidence: medium-high
- Caveats: a downstream multi-agent application can use Awaken messaging, priorities or mailbox semantics to implement a genuine coordination regime. That would require separate evidence at that application's system boundary.

### Absence scope

- Surfaces inspected: background child-agent manager/inboxes, handoff/delegation paths, durable mailbox/cross-thread messaging, `RunDispatch` priority/claim/lease/retry/dedupe semantics, workflow concurrency and distributed worker execution.
- Plausible first-party paths checked: live child messaging, durable parent/agent mailbox sends, dispatch priorities, atomic single-winner claim, lease recovery, duplicate suppression and parallel/background execution.
- Why no material first-party path remains: the inspected mechanisms transport work, prevent duplicate infrastructure execution or provide generic concurrency/delivery. They do not identify a concrete conflict/oscillation among distinct autonomous S1 units together with a function-specific attenuation relation and feedback into their subsequent behaviour.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the organization's current run commitments and execution pressure through a durable whole-run control plane, with an additional legitimate operator-owned intervention mode.
- Disturbance / variety regulated: current runs can accumulate, wait on HITL, fail, lose workers, compete for dispatch attention, become stale relative to newer user input or continue after the operator's current priority has changed.
- Decisive decision or feedback right: base mode — determine the function-specific current-work regime by which dispatch priority, claim ownership, retries/recovery, interrupt epochs and replacement/cancellation govern which current commitment executes next; parent mode — inspect current organization workload/runs and choose to cancel, steer, interrupt/replace or resume current work.
- Decision owner: base mode — no autonomous metasystem actor; the first-party runtime exposes and deterministically enforces a constructor-owned current-control regime whose priorities/modes are supplied by callers/configuration. Parent mode — the legitimate Awaken operator using shipped Admin/REST controls.
- Supporting / enforcement mechanisms: persisted `RunRecord`; `RunDispatch`; priority and availability time; atomic claim/token validation; leases/reclaim; retry/backoff/dead-letter; dispatch epochs/supersession; cancellation tokens; `/v1/runs/summary`; run list/get routes; Admin dashboard and bearer-authenticated control surfaces.
- Closure path: base mode — current durable work enters the mailbox → function-specific scheduling/claim/lease/epoch rules determine current execution/recovery/replacement → resulting dispatch/run state changes what executes next. Parent mode — operator reads live workload and current runs → sends cancel/steer/interrupt/resume decision → server cancels or redirects current execution and persists/queues the resulting commitment → subsequent operation follows the changed current-work state.
- Boundary reachability: queue-backed server operation ships the deterministic current-control regime; the Admin/REST operator surfaces are first-party supported deployment paths and directly reach the same persisted run/mailbox control state.
- Why this is / is not agent-owned: the base scheduler/control machinery owns enforcement but not discretionary autonomous whole-system judgment; priority and control mode are selected by configured/caller inputs. The operator mode has a reconstructable human decision owner. Therefore the standard distribution supports `C(P)`, not `A`.
- Evidence: [`apps/www/src/content/docs/explanation/hitl-and-mailbox.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/explanation/hitl-and-mailbox.md); [`crates/awaken-server/src/services/run_service.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-server/src/services/run_service.rs); [`crates/awaken-server/src/routes.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-server/src/routes.rs); [`apps/www/src/content/docs/reference/admin-console.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/reference/admin-console.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: queue status and leases alone would not establish S3. Positive credit depends on their role inside the first-party run-wide control plane plus the aggregate current workload view. HITL approval is ordinary action-level control and is not independently credited as S3.
- Whole-system current view: `/v1/runs/summary` aggregates all current `Running`, `Waiting` and `Created` runs for the Admin workload dashboard; run list/get surfaces expose the underlying current commitments and their persisted status.
- Current-control decision scope: determine execution/recovery/replacement of current durable run commitments through priority/claim/lease/retry/interrupt mechanics, and in parent mode cancel, steer, interrupt/replace or resume current runs.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Downstream caller/configuration selects current-work priority/control mode; first-party Awaken runtime enforces the function-specific regime | New/current durable run work, worker failure/lease expiry, retry eligibility or a newer dispatch epoch | current dispatch/run state → deterministic priority/claim/lease/retry/epoch decision path → execution, requeue, recovery, supersession or cancellation → changed subsequent current workload | `hitl-and-mailbox.md`, `run_dispatch.rs`, mailbox contract/store paths |
| Parent (`P`) | Legitimate Awaken operator | Operator sees current workload/run state and decides a live commitment should be stopped, steered, interrupted/replaced or resumed | Admin/REST current view → operator control request → server/mailbox cancellation/steering/interrupt/resume → persisted/queued changed commitment → later operation follows new current state | `run_service.rs`, `routes.rs`, `admin-console.md`, `hitl-and-mailbox.md` |

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit path is established for the declared Awaken operating boundary at the pinned revision.
- Disturbance / variety regulated: not established as S3*.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: traces/event replay, audit logs, profiler/runtime stats, offline datasets/eval runs/reports, permission checks, HITL decisions and ordinary tool/run validation.
- Closure path: no standard operating path was found in which materially complementary evidence independently challenges an ordinary S1/S3 claim and the resulting audit finding is required to return into corrective current control.
- Why this is / is not agent-owned: evals and trace replay can inspect recorded behaviour, but they are evaluation/observability surfaces rather than a packaged independent audit owner for ordinary operation. HITL permission decisions sit in the production action path and do not become S3* merely because they review a tool call.
- Evidence: [`apps/www/src/content/docs/reference/admin-console.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/reference/admin-console.md); [`apps/www/src/content/docs/explanation/hitl-and-mailbox.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/explanation/hitl-and-mailbox.md); [`crates/awaken-server/src/eval_router.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-server/src/eval_router.rs).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: a downstream organization can use Awaken's eval/replay infrastructure as evidence for its own independent audit organization; that separate wiring is not part of the assessed standard runtime.

### Absence scope

- Surfaces inspected: trace/event replay, audit log, runtime stats/profiler, dataset capture, eval routes/runs/reports, permission/HITL suspension, run validation and ordinary event history.
- Plausible first-party paths checked: offline eval datasets, replayed traces, Admin eval runs, audit-log review, runtime profiling and human approval of suspended tool calls.
- Why no material first-party path remains: these surfaces observe, evaluate offline or gate ordinary production actions. None establishes a sufficiently independent complementary evidence path plus audit judgment plus mandatory return of findings into ordinary S1/S3 correction.

## S4 — Outside-and-then adaptation

- State: —
- Function: no material first-party outside-and-then adaptation loop is established for the declared Awaken operating boundary at the pinned revision.
- Disturbance / variety regulated: not established as prospective organizational adaptation.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persisted history, replay, eval datasets/reports, provider/MCP health, config history/restore, prompt/tool/model editing, retries and current-run steering.
- Closure path: no first-party operating path was found that senses an external/future-relevant distinction, generates an adaptation option, decides among such options and returns a changed organizational capability or S3 regime into subsequent operation.
- Why this is / is not agent-owned: evaluation and configuration surfaces can inform a human maintainer/operator, but no autonomous or constructor-specific S4 decision path is wired from those observations to a prospective capability change. Replay/history alone is retrospective evidence, not outside-and-then intelligence.
- Evidence: [`apps/www/src/content/docs/reference/admin-console.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/reference/admin-console.md); [`README.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/README.md).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: operators can manually edit and publish agent configuration after reviewing evals or environmental changes. Generic human reconfiguration is not credited as S4 without an explicit first-party adaptation function and closure at this recursion.

### Absence scope

- Surfaces inspected: eval datasets/runs/reports, trace/replay, provider/MCP health, configuration versioning/restore/publish, model/tool/prompt edits, runtime retry/recovery and current steering.
- Plausible first-party paths checked: eval-driven tuning, replay-driven change, provider-health response, configuration restore/publish, agent prompt/model/tool changes and runtime recovery.
- Why no material first-party path remains: the inspected mechanisms are retrospective evaluation, present-operation recovery or generic parent configuration. They do not package an external-and-prospective adaptation decision path whose option is returned into present organizational capability.

## S5 — Identity and ultimate policy

- State: —
- Function: no material first-party identity/ultimate-policy authority loop is established for the declared Awaken operating boundary at the pinned revision.
- Disturbance / variety regulated: not established at identity/ultimate-policy level.
- Decisive decision or feedback right: no first-party path identifies an identity/ultimate-policy issue and routes it to a legitimate ultimate authority for adjudication/amendment with returned closure.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: system prompts and agent definitions, permission/policy rules, provider/model/tool configuration, admin bearer authority, registry snapshots, config history/restore/publish and HITL approval.
- Closure path: no identity/ultimate-policy issue → legitimate authority → adjudication/amendment → subsequent-operation-under-new-policy chain is established.
- Why this is / is not agent-owned: the Admin Console can edit prompts, models, tools, plugins and other configuration and publish registry snapshots, while permission/HITL paths enforce already-selected constraints. Generic configuration authority does not become S5 without evidence that the decision class is organizational identity/ultimate policy and that this authority is the legitimate S5 closure at the chosen recursion.
- Evidence: [`apps/www/src/content/docs/reference/admin-console.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/reference/admin-console.md); [`apps/www/src/content/docs/explanation/hitl-and-mailbox.md`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/apps/www/src/content/docs/explanation/hitl-and-mailbox.md); [`crates/awaken-server/src/config_routes.rs`](https://github.com/awakenworks/awaken/blob/2b0d375004ec8723cf40d8a59c0bb486ebce57e0/crates/awaken-server/src/config_routes.rs).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: an operator may intentionally encode identity-level content in a system prompt or config snapshot. The Profile requires the organizational function and authority chain to be established, not inferred from the editable object name.

### Absence scope

- Surfaces inspected: agent/system prompt configuration, model/tool/plugin assignment, permission/policy rules, Admin Assistant policy, registry versioning/publish/restore, admin bearer control, HITL approval and configuration audit history.
- Plausible first-party paths checked: prompt edits, agent definition changes, permission-rule changes, registry publish/restore, admin configuration authority and approval decisions.
- Why no material first-party path remains: these surfaces configure or enforce operating choices. The reviewed distribution does not define an identity/ultimate-policy issue class, legitimate ultimate authority for that class and a return path proving subsequent operation under an authoritative identity/policy decision.
