---
harness_id: tandem
project_name: Tandem
repository: https://github.com/frumu-ai/tandem
review_ref: 3ee2d83d76497565680538ef00f1616f55650524
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: C(P)
---

# Tandem

## Review boundary

- System in focus: one first-party Tandem-managed governed agentic-work organization at pinned revision `3ee2d83d76497565680538ef00f1616f55650524`, centered on the native engine model/tool loop, Automation V2 runtime, scheduler, governance/lifecycle review machinery and versioned orchestration/goal surfaces.
- Purpose and identity: execute model-driven work under durable runtime authority while coordinating concurrent work, regulating whole-run state, independently challenging operational evidence and preserving owner/admin authority over the durable orchestration identity and ultimate goal policy.
- Relevant environment: human/operator and administrators; repositories/workspaces; model providers; built-in and MCP tools; external systems and webhooks; tenant/principal context; provider throttling; concurrent runs; tool/artifact evidence; failures, guardrail stops and dependency changes.
- Standard-distribution boundary: the public Tandem engine/server/runtime crates, standard desktop/TUI/control-panel/API entrypoints, native model/provider loop, Automation V2 scheduler/executor, governance engine, orchestration/goal runtime and first-party authoring/control APIs. External model endpoints, MCP servers/connectors and company systems remain dependencies/environment; their internal functions are not imported.
- Credited operating / distribution surfaces: `README.md`; `crates/tandem-core/src/engine_loop/prompt_execution.rs`; `crates/tandem-core/src/engine_loop/prompt_execution_parts/tool_processing.rs`; `crates/tandem-server/src/app/state/automation/scheduler.rs`; `crates/tandem-server/src/automation_v2/executor.rs`; `crates/tandem-server/src/http/routines_automations_parts/part04.rs`; `crates/tandem-governance-engine/src/lib.rs`; `crates/tandem-server/src/app/state/governance_parts/part01.rs`; `docs/WORKFLOW_RUNTIME.md`; `crates/tandem-automation/src/orchestration.rs`; `crates/tandem-server/src/http/orchestrations_api.rs`.
- Adjacent first-party surfaces excluded from ownership: repository CI/release workflows; tests and long-horizon proof fixtures except as corroboration of shipped runtime paths; compliance prose by itself; planned enterprise-sidecar capabilities not implemented at the pinned ref; external coding-agent integrations and external MCP/model reasoning; contributor/development workflows.
- First-party operating / deployment modes considered: ordinary native prompt execution; Automation V2 multi-node execution; concurrent automation runs with workspace admission; local self-hosted operator mode; hosted/enterprise tenant-governed mode; lifecycle health/review; versioned orchestration draft/publish and long-running goal execution.
- Recursion level: one Tandem-managed agentic-work organization is the system-in-focus. Native model/tool sessions and Automation V2 workflow/node executions are S1 operational units where they own separate substantive outcomes. The Tandem runtime, scheduler, executor, governance and orchestration layers form the metasystem at this boundary.
- Reviewed revision: `3ee2d83d76497565680538ef00f1616f55650524`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Tandem is not only a policy proxy around an external agent. The pinned first-party engine contains its own multi-iteration model/tool runtime. `EngineLoop::run_prompt_async_with_execution_context` resolves a provider/model, assembles history and runtime context, selects and scopes tools, dispatches to the model provider, parses streamed tool calls, executes accepted calls through Tandem's permission/policy boundary, returns tool outputs into later iterations and terminates only when the loop reaches a final response or bounded failure. The model chooses substantive tool actions while Tandem owns execution authority, context, persistence, limits and evidence.

Automation V2 lifts multiple such executions into durable workflow/run organizations. The scheduler tracks active runs, queue state, provider throttles and a `workspace_root -> run_id` lock. A second run targeting a live locked workspace is not merely rejected as an unrelated launch error: it remains non-admissible with an explicit `WorkspaceLock` queue reason until the holder releases the workspace, after which the waiting run can become admissible. This supplies a concrete inter-S1 attenuation path rather than generic routing alone.

Whole-current control is implemented through run checkpoints, node outputs, attempts, pending/completed/blocked sets, active sessions/instances, retry policy, partial-failure modes and terminal-state derivation. Constructor rules can retry a failed node, preserve independent branches, pause downstream work or pause the whole run according to first-party policy. A distinct parent path exists through shipped pause/resume controls: an authorized operator pauses the automation, cancels active sessions and agent-team instances, records lifecycle state, and later explicitly resumes the automation under governance checks.

Tandem also has complementary evidence paths outside the producing model's self-report. Workflow validation can challenge claimed artifacts against concrete execution evidence, while the governance engine separately derives lifecycle-health observations from persisted terminal-run outcomes such as failure count, empty-output count and repeated guardrail stops. Threshold breaches create `HealthDrift` findings and lifecycle review requirements. Governance review forbids self-review, and affected automation governance can remain paused/review-required until independent acknowledgment and an explicit return to operation. The audit judgment is constructor/rule driven rather than owned by an autonomous auditor agent.

The long-running orchestration layer supplies durable, versioned organizational definitions. `OrchestrationSpec` carries the named organization, root, workflow/wait/terminal nodes, transition edges, approval boundaries and `GoalPolicy`; drafts are mutable, publishing snapshots an immutable version, and durable goals execute the published graph across many workflow runs. Mutation is owner/admin governed and creator identity is non-writable. Tandem also deliberately supports agent-authored automation governance primitives, but no standard autonomous actor is established as the legitimate ultimate-policy authority over the full organization. This supports a constructor S5 path plus a separately closed parent/operator mode.

## Operational model

A normal native S1 starts with a user or workflow prompt. Tandem constructs the permitted context/tool surface, calls the configured model, accepts model-selected tool calls that survive runtime policy, executes them, returns outputs and errors to the next model round and repeats until a terminal response or bounded failure. Automation V2 can run several such operational cells under one durable flow and checkpoint.

When multiple runs coexist, Tandem's scheduler attenuates one concrete destructive interaction: concurrent ownership of the same mutable workspace. The lock/admission path queues the later run and returns it to execution only after the conflicting current holder releases the workspace. This is constructor-defined coordination rather than model-owned S2 discretion.

At the metasystem level, current run state is represented explicitly and constructor rules regulate retries, downstream blocking, continuation of independent branches and terminal status. The parent operator can separately pause/resume the whole automation and cancel its active execution population. Complementary governance health review uses persisted run evidence rather than the model's completion narrative and can require independent review before continued operation.

For identity/policy, an orchestration draft defines the durable topology and goal limits of future work. Publishing freezes that definition into an immutable version consumed by later long-running goals. The owner/admin therefore has a closed parent path from organization-level definition to later execution. Agent-authored automation/orchestration primitives expose a specific constructor path for an autonomous policy actor, but Tandem does not wire such an actor as ultimate authority by default.

## S1 — Operations

- State: A
- Function: perform substantive model-driven work through a first-party iterative reasoning/tool loop and produce durable task/workflow outputs.
- Disturbance / variety regulated: user/workflow ambiguity; changing repository and external-system state; tool observations; provider/model outputs; failed or denied tool calls; incomplete evidence; context limits; cancellation and task-specific blockers.
- Decisive decision or feedback right: choose the next context-sensitive model response/tool action in light of returned tool/environment observations and continue or terminate the operational work.
- Decision owner: the model actor inside Tandem's first-party `EngineLoop` execution path.
- Supporting / enforcement mechanisms: provider routing; context assembly; tool retrieval/routing; tenant/tool allowlists; permission and data-boundary gates; tool execution; retry and iteration budgets; session/run persistence; event/audit records.
- Closure path: prompt/workflow objective enters `EngineLoop` -> model receives current context and permitted tool schemas -> model emits text/tool calls -> Tandem executes accepted tools -> results/errors return into later model iterations -> model changes subsequent action or terminates -> final output and state are persisted.
- Boundary reachability: the native engine loop is part of the shipped Tandem engine used by desktop, TUI, SDK, web/control-panel and automation surfaces; no external coding-agent harness is required to supply this operational loop.
- Why this is / is not agent-owned: removing the model actor leaves context/tool/policy enforcement but not the substantive contextual choice of which operation/tool to attempt next. Tandem constrains and executes the decision without replacing the operational discretion.
- Evidence: [`README.md`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/README.md); [`prompt_execution.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-core/src/engine_loop/prompt_execution.rs); [`tool_processing.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-core/src/engine_loop/prompt_execution_parts/tool_processing.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: runtime tool selection, policy enforcement and retry guards are supporting machinery; the `A` claim is based on the model-owned next-action loop, not on those deterministic controls.

## S2 — Coordination

- State: C
- Function: attenuate destructive interference among concurrent S1 work cells that would otherwise operate on the same mutable workspace at the same time.
- Disturbance / variety regulated: two concurrent automation/work cells attempting to mutate or reason over one shared workspace concurrently, producing file/repository races, stale assumptions or inconsistent outputs.
- Decisive decision or feedback right: determine whether a candidate run may enter the shared workspace now or must remain queued because another live run owns that workspace.
- Decision owner: constructor-defined `AutomationScheduler` workspace-lock/admission rules; no autonomous model actor owns the collision policy.
- Supporting / enforcement mechanisms: `active_runs`; `locked_workspaces`; `queue_state`; `QueueReason::WorkspaceLock`; provider rate-limit admission; global run capacity; release/recovery paths.
- Closure path: one run is admitted and reserves the workspace -> a sibling run requests admission to the same `workspace_root` -> scheduler returns `WorkspaceLock` and keeps the second run out of execution -> the holder releases the workspace -> the queued run becomes admissible and can subsequently execute.
- Boundary reachability: the scheduler and workspace-lock recovery paths are wired into the shipped Automation V2 runtime and exercised by first-party run/recovery behavior; no adopter-defined coordination transport is required.
- Why this is / is not agent-owned: the inter-S1 conflict and returned behavioral change are real, but the decisive attenuation rule is deterministic constructor policy. Removing the worker models leaves the same workspace-lock/backoff decision.
- Distinct S1 units: separately admitted Tandem automation/workflow executions with independent run IDs, sessions and work outcomes sharing one runtime/workspace environment.
- Inter-S1 disturbance: simultaneous access to one mutable workspace can create conflicting writes and stale repository state between otherwise independent work cells.
- Attenuating coordination relation: `AutomationScheduler::can_admit_for_tenant` checks `locked_workspaces` and withholds admission while a sibling holds the same `workspace_root`.
- Feedback into subsequent S1 behaviour: the second run does not start in the conflicting workspace; after release/recovery, admission succeeds and its S1 behavior occurs later against the released workspace state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping is tied to a concrete sibling collision class and a first-party lock/queue feedback path that changes when the affected S1 may operate; generic DAG dependencies and task routing are not used as the S2 witness.
- Evidence: [`scheduler.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-server/src/app/state/automation/scheduler.rs); [`automations_parts/part05.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-server/src/app/state/tests/automations_parts/part05.rs).
- Basis: structural.
- Confidence: high.
- Caveats: generic workflow ordering, node dependencies and provider routing are not credited as S2; the claim is limited to the concrete shared-workspace interference loop.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate the current Automation V2 organization from a whole-run view, deciding retries, downstream blocking/continuation, terminal state and whole-automation intervention.
- Disturbance / variety regulated: failed or incomplete nodes; exhausted retries; validation failures; stalled or timed-out sessions; blocked descendants; partial failures that should or should not stop independent work; active sessions/instances needing whole-automation pause/resume.
- Decisive decision or feedback right: base mode — determine current retry/repair/continuation/blocking/terminal treatment from the run checkpoint and configured failure policy; parent mode — decide to pause or resume the automation as a whole and thereby cancel or restore its current execution population.
- Decision owner: base `C` mode — constructor-defined Automation V2 executor/recovery rules; parent `P` mode — the authorized Tandem owner/operator through the shipped governance/control surface.
- Supporting / enforcement mechanisms: run checkpoint; pending/completed/blocked node sets; node attempts/outputs; partial-failure mode; retry policy; active session and instance registries; scheduler; lifecycle records; cancellation manager; governance checks and protected audit.
- Closure path: base mode — whole-run checkpoint and node outcomes are evaluated -> constructor policy chooses retry, continue-independent, pause-downstream/pause-all, block or terminal state -> checkpoint/current run state changes -> later nodes/sessions execute or remain blocked accordingly; parent mode — operator pauses/resumes the automation -> Tandem cancels active sessions/instances or reactivates the automation -> later current operation follows the returned parent decision.
- Boundary reachability: Automation V2 executor/recovery is the normal shipped runtime; pause/resume handlers are first-party HTTP/control surfaces and operate directly on live stored automations/runs under owner/admin governance.
- Why this is / is not agent-owned: the function is operationally substantial, but the base current-control decisions are encoded in deterministic executor/retry/failure rules rather than owned by an autonomous manager agent. The separately supported operator mode closes parent current control.
- Whole-system current view: run status plus checkpoint-wide pending/completed/blocked nodes, node attempts and outputs, active session/instance IDs, failure records, wait/gate state and scheduler state represent the current managed organization rather than one worker's local task.
- Current-control decision scope: retry/repair admission; downstream blocking; whether independent branches continue; partial-failure handling; terminal run classification; whole-automation pause/resume and cancellation of active sessions/instances.
- Evidence: [`executor.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-server/src/automation_v2/executor.rs); [`routines_automations_parts/part04.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-server/src/http/routines_automations_parts/part04.rs); [`AI_RUNTIME_INFRASTRUCTURE.md`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/docs/AI_RUNTIME_INFRASTRUCTURE.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: static workflow sequencing, tool permission gates and generic process kill capability are not independently credited as S3; the positive mapping uses whole-run state and organization-level intervention.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | constructor-defined Automation V2 executor/recovery policy; autonomous manager must be composed for agent-owned S3 | checkpoint-wide failure/retry/blocking/current-run state | executor updates pending/blocked/completed state, retries or derives terminal treatment; subsequent nodes/runs follow the changed current state | `crates/tandem-server/src/automation_v2/executor.rs`; `docs/AI_RUNTIME_INFRASTRUCTURE.md` |
| Parent (`P`) | authorized owner/operator | operator decides the whole automation should pause or resume | pause sets automation/run state, cancels active sessions/instances and records lifecycle evidence; resume reactivates under governance checks so later operation can continue | `crates/tandem-server/src/http/routines_automations_parts/part04.rs`; `crates/tandem-server/src/app/state/governance_parts/part01.rs` |

## S3* — Complementary audit

- State: C
- Function: challenge ordinary agent/run claims with independent runtime/governance evidence and return audit findings into current control before the organization continues unchecked.
- Disturbance / variety regulated: model/stage reports that do not match actual artifact/tool evidence; repeated failed or empty terminal runs; repeated guardrail stops; lifecycle/dependency drift; governance ownership anomalies that ordinary completion reporting can miss.
- Decisive decision or feedback right: determine from complementary persisted evidence that an operational or lifecycle claim is no longer sufficiently trustworthy and require repair/review before normal continuation.
- Decision owner: constructor-defined validators/governance health rules and an explicitly independent reviewer where lifecycle acknowledgment is required; no autonomous first-party auditor agent owns the audit judgment in the standard mode.
- Supporting / enforcement mechanisms: artifact contracts; concrete read/tool evidence; validation state; terminal-run health summaries; failure/empty-output/guardrail-stop counters; `HealthDrift` and dependency/ownership findings; `review_required`; lifecycle pause; approval receipts; self-review prohibition; explicit resume.
- Closure path: ordinary S1/run output is persisted -> complementary validator/governance paths inspect execution receipts or accumulated terminal-run evidence -> mismatch/drift creates a failed validation or lifecycle finding/review requirement -> repair/review is required and normal continuation can remain blocked/paused -> accepted repair or independent acknowledgment plus explicit resume returns the finding into later operation.
- Boundary reachability: artifact validation and governance health/review are shipped runtime paths used by Automation V2/governance state; they operate outside the producing model loop and on persisted first-party evidence. Governance review explicitly rejects self-review.
- Why this is / is not agent-owned: the audit function and corrective return are established, but the deciding thresholds/contracts are constructor rules and the independent reviewer is not an autonomous standard-distribution audit agent. This supports `C`, not `A`.
- Claim being audited: that the agent/workflow actually produced the claimed valid artifact and that the automation remains operationally healthy enough to continue without lifecycle review.
- Ordinary reporting path: model completion text, node output/status and normal run completion state.
- Complementary access path: runtime validators can inspect concrete execution/artifact evidence; the governance engine separately summarizes persisted terminal-run outcomes and detects failure/empty-output/guardrail-stop drift rather than trusting the model's narrative.
- Independence boundary: the governance/validation machinery is separate from the provider model producing the work; governance approval cannot be reviewed by the same identified requester, and lifecycle review state is persisted independently of the run's own success claim.
- Who acts on findings: constructor repair/retry/control paths act on validation findings; an eligible independent reviewer acknowledges lifecycle findings, after which explicit resume can return the automation to operation.
- Evidence: [`WORKFLOW_RUNTIME.md`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/docs/WORKFLOW_RUNTIME.md); [`executor.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-server/src/automation_v2/executor.rs); [`tandem-governance-engine/src/lib.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-governance-engine/src/lib.rs); [`governance_parts/part01.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-server/src/app/state/governance_parts/part01.rs).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: ordinary mandatory validation alone is not treated as sufficient S3*. The positive finding depends on the materially different persisted evidence channel plus lifecycle health/review path and independent-review boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no standard-distribution external-and-prospective adaptation loop is established at the reviewed boundary.
- Disturbance / variety regulated: Tandem can wait on external conditions, persist long-running goals, repair failed current work, expose a named `replan` transition and let users/models author workflow plans, but these features do not by themselves establish an S4 conversation that develops future-facing adaptation options from environmental change and returns them into present organizational capability.
- Decisive decision or feedback right: no qualifying first-party S4 adaptation judgment is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: external-condition/webhook waits; long-running goal state; Goal -> Plan -> Execute -> Verify -> Replan graph support; workflow planner/product authoring; memory/context; current-run self-healing; governance health drift.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: there is no established S4 function to classify. The model can plan/replan a task or author a workflow when asked, while deterministic waits and repair loops react to current conditions; neither establishes the required external/future distinction -> adaptation option -> changed present capability loop.
- Evidence: [`orchestration.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-automation/src/orchestration.rs); [`orchestration_goal_plan_execute_verify_proof.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-server/src/http/tests/orchestration_goal_plan_execute_verify_proof.rs); [`WORKFLOW_RUNTIME.md`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/docs/WORKFLOW_RUNTIME.md); [`CHANGELOG.md`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/CHANGELOG.md).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: a downstream developer can compose future-oriented adaptation from Tandem's workflow/orchestration primitives, but Methodology 0.3.6 does not award `C` for generic graph/planner expressiveness without a material first-party S4-specific loop.

### Absence scope

- Surfaces inspected: native engine loop; workflow planner/product authoring; Automation V2 repair/retry; memory/context injection; webhook and external-condition waits; long-running goal/orchestration model; named replan route; governance health/lifecycle review.
- Plausible first-party paths checked: Goal -> Plan -> Execute -> Verify -> Replan; external-condition waits; self-healing workflows; workflow plan revision; memory-driven later prompts; lifecycle health drift and dependency revocation.
- Why no material first-party path remains: the `replan` edge is a pre-authored/caller-selected control transition, external waits gate or wake execution without generating adaptation options, self-healing repairs current failed work, and product authoring is driven by operator/current task intent. No reviewed standard path couples an environmental/future distinction to developed adaptation options and then changes present organizational capability.

## S5 — Policy and identity

- State: C(P)
- Function: define and revise the durable identity/topology and ultimate operating policy of a Tandem-managed long-running organization, with a first-party constructor path and a separately closed owner/admin parent mode.
- Disturbance / variety regulated: proposals or disputes about what the orchestration is for, which workflow topology/root governs it, which transitions and approval boundaries are legitimate, what goal limits apply, and who is authorized to alter or publish that durable organizational definition.
- Decisive decision or feedback right: choose the authoritative orchestration definition and `GoalPolicy` that future long-running goals will execute; in the parent mode, decide whether a draft is changed/published under owner/admin authority.
- Decision owner: base `C` mode — Tandem supplies versioned orchestration/goal-policy primitives plus governed agent-authored automation creation/mutation paths, but no standard autonomous actor is established as legitimate ultimate-policy authority for the organization; parent `P` mode — the recorded owner or authorized administrator/operator owns mutation/publication authority.
- Supporting / enforcement mechanisms: `OrchestrationSpec`; root/node/edge graph; transition approvals; `GoalPolicy`; non-writable `created_by`; owner/admin checks; draft validation; immutable published versions; tenant scope; governance capability/lineage limits; durable goal/run lineage.
- Closure path: identity/ultimate-policy proposal is expressed as an orchestration draft/goal policy -> authorized constructor/parent path selects the definition -> validation and publish snapshot it into an immutable version -> later `LongRunningGoal` instances execute that published root/topology/transitions/policy -> subsequent operation is governed by the returned durable definition.
- Boundary reachability: orchestration draft/update/publish APIs and long-running goal execution are shipped first-party runtime surfaces; governance explicitly supports agent-authored automation records while owner/admin authoring and publication are part of the ordinary API/control boundary.
- Why this is / is not agent-owned: Tandem intentionally exposes a policy/identity-specific versioned definition and return path, supporting `C`, but standard operation does not give a native autonomous model legitimate ultimate publication authority. The closed authoritative mode is owner/admin governed, supporting `(P)` rather than `A(P)`.
- Identity / ultimate-policy issue: the durable organization's purpose/name, root topology, allowed transitions/approval boundaries and goal-wide limits determine what the long-running organization is and the envelope under which future workflow runs may proceed; this is distinguished from approving one ordinary task/tool action.
- Ultimate authority in each claimed mode: base constructor mode — an autonomous ultimate-policy actor must be explicitly composed/authorized against the first-party orchestration/governance primitives; parent mode — the recorded orchestration owner or authorized administrator/operator.
- Return-to-operation path: published immutable orchestration version and goal policy are loaded by future long-running goals, which create and transition workflow runs according to that version; changed published policy therefore governs subsequent operation.
- Evidence: [`orchestration.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-automation/src/orchestration.rs); [`orchestrations_api.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-server/src/http/orchestrations_api.rs); [`tandem-governance-engine/src/lib.rs`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/crates/tandem-governance-engine/src/lib.rs); [`CHANGELOG.md`](https://github.com/frumu-ai/tandem/blob/3ee2d83d76497565680538ef00f1616f55650524/CHANGELOG.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: ordinary tool approvals, tenant permissions and runtime security policy are not treated as S5. The positive mapping is limited to the durable organization-level orchestration/goal-policy definition and its legitimate publication authority.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | autonomous ultimate-policy actor must be composed/authorized; Tandem supplies the specific versioned orchestration/governance path | proposed change to durable purpose/topology/goal policy | actor can use first-party draft/version/governance primitives, but autonomous ultimate authority is not wired by default | `crates/tandem-automation/src/orchestration.rs`; `crates/tandem-governance-engine/src/lib.rs`; `crates/tandem-server/src/http/orchestrations_api.rs` |
| Parent (`P`) | recorded owner / authorized administrator or local self-hosted operator | parent chooses to revise/publish the durable organization definition | owner/admin mutates the draft; validated publish creates immutable version; future goals/runs execute under that version and policy | `crates/tandem-server/src/http/orchestrations_api.rs`; `CHANGELOG.md`; `crates/tandem-automation/src/orchestration.rs` |
