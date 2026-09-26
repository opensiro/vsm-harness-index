---
harness_id: boundflow
project_name: BoundFlow
repository: https://github.com/boundflow/boundflow
review_ref: 15c0b20a3a98d3413956cab7fba2fd77c1fa32e2
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# BoundFlow

## Review boundary

- System in focus: the first-party BoundFlow control-plane plus Python SDK worker organization at pinned revision `15c0b20a3a98d3413956cab7fba2fd77c1fa32e2`, including the model/tool `Orchestrator`, `BoundFlowWorker`, durable workflow/run state, scheduler, runtime/lifecycle policy machinery and first-party approval/input gates.
- Purpose and identity: run operator-authored AI-agent workflows durably while BoundFlow itself drives agent model/tool turns and applies operator-defined runtime and workflow governance across current and subsequent runs.
- Relevant environment: operator-authored workflow/operation handlers and agent definitions; user/task inputs; external LLM providers and inference keys; external tool/business services; worker crashes and network failures; workflow cost/latency/failure/tool-use metrics; human approval/input decisions; Postgres and deployment infrastructure.
- Standard-distribution boundary: the Apache-2.0 backend plus MIT Python SDK shipped in this repository and reached by the documented self-hosted quick-start. External inference providers, LangChain/LangGraph internals, customer tool implementations/business systems, Postgres itself and BoundFlow Cloud hosting infrastructure remain dependencies or deployment environment rather than imported organizational owners.
- Credited operating / distribution surfaces: `README.md`; `docs/concepts.md`; `sdk/python/boundflow/worker.py`; `sdk/python/boundflow/llm.py`; `sdk/python/boundflow/governed.py`; `sdk/python/boundflow/lifecycle.py`; `sdk/python/boundflow/policies.py`; `sdk/python/boundflow/control_plane.py`; backend scheduler/lifecycle-policy implementation under `internal/lifecyclepolicy/` and the server/worker paths that dispatch and resume operations.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor governance; landing-site material; mock/live-LLM test suites as tests rather than operating actors; hosted BoundFlow Cloud operations beyond the same public control-plane API; examples as evidence of reachability rather than separate systems-in-focus.
- First-party operating / deployment modes considered: documented self-hosted backend (`server`, `scheduler`, `worker`) with a connected `BoundFlowWorker` using a supported LLM client; operator-defined runtime/agent/workflow lifecycle policies; approval/input gates; optional customer-driven loops under BoundFlow governance. The parent S3 result uses the supported self-hosted operator-governed policy mode.
- Recursion level: one BoundFlow-managed workflow organization, spanning its current and repeated runs. Agent steps and workflow operations are lower-level operational transformations inside that managed workflow unless an application separately instantiates independently accountable operational units.
- Reviewed revision: `15c0b20a3a98d3413956cab7fba2fd77c1fa32e2`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

BoundFlow deliberately splits management from execution. The backend runs server, scheduler and worker process modes over shared Postgres state, while a Python `BoundFlowWorker` in the operator environment executes workflow handlers, LLM calls and tools. This is not merely a remote control plane around an unrelated agent runtime: the SDK contains a first-party `Orchestrator.run_step()` agent loop. `OperationContext.run_agent()` resolves the current policy, constructs an `AgentStepConfig` and calls that orchestrator. The orchestrator repeatedly invokes the configured model, executes model-selected first-party tool callbacks, returns tool results into the message history and continues until the model calls `submit_result` or a governed limit terminates the step.

Workflow operations return a small first-party state-machine vocabulary: `Complete`, `Next`, `AwaitApproval` and `AwaitInput`. State is persisted so an approval/input gate or worker interruption does not require recreating the workflow from scratch. The backend scheduler leases and dispatches due work, while platform interruption recovery and durable run state maintain continuity across workers.

Governance has three materially different layers. Runtime policy hard-caps model calls, tokens, tool calls/failures, cost, call time and model choice during a run. Agent lifecycle rules inspect prior-run metrics and can change the effective model or resource caps. Workflow lifecycle rules inspect workflow-level rolling/version metrics and can pause, cool down or roll the workflow to an operator-selected version. The rules and their thresholds/actions are explicitly the policy surface customers write; deterministic first-party evaluators and governors enforce them and audit policy actions.

The decisive ownership distinction is therefore important. The autonomous model owns the task-specific S1 choices inside `run_step()`. By contrast, the repository does not ship an autonomous manager that chooses which lifecycle objective, threshold, version target or resource posture the workflow should adopt. In the standard operator-governed lifecycle mode, the operator supplies those whole-workflow current-control decisions as policy, and BoundFlow closes the return path by applying them to later execution. That establishes parent-governed S3, not autonomous S3.

Primary evidence:

- [`README.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/README.md) — control-plane/data-plane split, documented `BoundFlowWorker` agent execution, durable workflow outcomes, runtime policy, agent/workflow lifecycle policy, approval/input gates and governance audit log.
- [`docs/concepts.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/docs/concepts.md) — workflow/agent objects, lifecycle states and the server/scheduler/worker responsibilities; explicitly states that the connected SDK worker runs the actual agents.
- [`sdk/python/boundflow/worker.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/worker.py) — `AgentDefinition`, operation results, `OperationContext.run_agent()`, policy resolution and dispatch into the first-party orchestrator.
- [`sdk/python/boundflow/llm.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/llm.py) — `Orchestrator.run_step()` model→tool→observation loop, governed calls/tool execution and final result submission.
- [`sdk/python/boundflow/policies.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/policies.py) — operator-authored runtime, agent-lifecycle and workflow-lifecycle policy types and actions.
- [`sdk/python/boundflow/lifecycle.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/lifecycle.py) — deterministic evaluation of agent lifecycle rules against recorded invocation history and application to effective runtime policy.
- [`internal/lifecyclepolicy/engine.go`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/internal/lifecyclepolicy/engine.go) — workflow-wide rolling/version metric evaluation and selection of pause/cooldown/version goal state from configured rules.

## Operational model

An operator deploys the backend, connects a `BoundFlowWorker`, defines workflow handlers and `AgentDefinition`s, configures inference and optionally writes governance policies. A run is scheduled and dispatched to the connected SDK worker. Inside an operation, `ctx.run_agent()` resolves the current effective policy and invokes the first-party orchestrator. The model selects tool calls, receives concrete callback results and chooses subsequent task actions until it submits a result or a policy limit ends the step. The workflow handler then returns `Complete`, `Next`, `AwaitApproval` or `AwaitInput`, and server-side state determines whether the workflow finishes, advances, parks or later resumes.

Across runs, the control plane collects metrics. Agent lifecycle rules can deterministically alter effective model/resource caps; workflow lifecycle rules can deterministically pause, cool down or select a prior workflow version. Those current-control actions alter subsequent operation, but their decisive thresholds/actions/version targets come from operator-authored policy. Human approval/input is separately available for application-level gates; it is not used here as generic evidence of S3/S5.

## S1 — Operations

- State: A
- Function: perform the substantive model-driven work of a configured workflow operation by choosing and executing task-relevant tool actions, interpreting observations and deciding when the agent step is complete.
- Disturbance / variety regulated: open-ended task inputs; model/tool choice within the configured agent definition; changing tool results and failures; uncertain intermediate state; bounded cost/token/call/tool budgets; external service responses; incomplete information requiring another action.
- Decisive decision or feedback right: choose the next task-specific tool/action and arguments from current model context and returned observations, then decide whether to continue or submit the operation result.
- Decision owner: the model-driven first-party BoundFlow `Orchestrator` path instantiated by `OperationContext.run_agent()`.
- Supporting / enforcement mechanisms: `BoundFlowWorker`; `AgentDefinition`; provider adapter; `AgentGovernor`; runtime-policy caps; tool registry/callback dispatch; operation context; traces; durable workflow/request state and backend job dispatch.
- Closure path: workflow operation/context -> `run_agent()` resolves policy and calls `Orchestrator.run_step()` -> model chooses tool call -> first-party callback executes -> tool result returns into message history -> next model call changes action or calls `submit_result` -> operation receives `StepResult` and workflow progresses.
- Boundary reachability: the README quick-start directly constructs a first-party `BoundFlowWorker`, registers a workflow, calls `ctx.run_agent(AgentDefinition(...))` and invokes that workflow through the shipped control plane; the credited loop requires no adjacent benchmark or development-only actor.
- Why this is / is not agent-owned: deterministic code supplies policy, transport, callbacks and limits, but it does not choose the contextual task action. Removing the model decision path while retaining those mechanisms would not produce materially the same next-tool/argument/completion decisions.
- Evidence: [`README.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/README.md); [`sdk/python/boundflow/worker.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/worker.py); [`sdk/python/boundflow/llm.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/llm.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: workflow handlers and tool callbacks are operator/developer supplied, and external providers supply inference. The autonomy claim is specifically the contextual operational decision loop first-party BoundFlow drives over those configured capabilities.

## S2 — Coordination

- State: —
- Function: no qualifying inter-S1 coordination function is established in the generic standard distribution at the assessed workflow recursion.
- Disturbance / variety regulated: workflows can contain several operations/agent definitions and the scheduler can queue many runs, but no specific first-party inter-S1 conflict, oscillation or mutual-interference problem is established merely by this plurality.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: workflow sequencing through `Next`; shared context; scheduler queues/leases; operation dispatch; approval/input parking; model/tool routing.
- Closure path: no material distinct-S1 disturbance -> S2-specific attenuation decision -> changed subsequent behaviour of the affected S1 units is supplied by the generic runtime.
- Why this is / is not agent-owned: sequencing, durable state and dispatch coordinate software execution in the ordinary sense, but the Profile requires concrete regulation of interference among distinct operational units rather than generic orchestration primitives.
- Evidence: [`docs/concepts.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/docs/concepts.md); [`sdk/python/boundflow/worker.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/worker.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: an application built with BoundFlow may instantiate several independently accountable operations and implement its own coordination logic; that downstream organization would require its own system-in-focus assessment.

### Absence scope

- Surfaces inspected: workflow operations/outcomes, shared context, scheduler/job dispatch, worker leases/recovery, approval/input gates, multi-step examples and the model/tool orchestrator.
- Plausible first-party paths checked: `Next` sequencing; multiple named agents; queued runs; scheduler leases; shared workflow state; approval/input state; concurrent workers.
- Why no material first-party path remains: these are generic execution/state/lifecycle mechanisms. The reviewed standard distribution does not establish distinct S1 units plus a specific inter-S1 disturbance and S2-specific attenuation/feedback relation.

## S3 — Inside-and-now control

- State: P
- Function: regulate the current operating posture of the managed workflow as a whole by applying parent-authored resource/model constraints and workflow intervention policy from aggregated operational evidence.
- Disturbance / variety regulated: excessive cost/LLM/tool use; repeated failures; excessive latency; approval rejections; tool failure accumulation; degraded workflow version behaviour; need to pause/cool down/roll back or narrow an agent's effective operating envelope.
- Decisive decision or feedback right: define which whole-workflow/agent metric conditions warrant a current-control intervention and what intervention follows — including effective model/resource caps and workflow pause/cooldown/version rollback.
- Decision owner: the legitimate self-hosted operator/parent that authors `RuntimePolicy`, `AgentRule` and `WorkflowRule` thresholds/actions/targets. BoundFlow's governor and lifecycle engines enforce/evaluate those selected policies but do not autonomously choose the organizational objective, threshold or target action.
- Supporting / enforcement mechanisms: per-run metric collection; invocation history; workflow version metrics; `AgentGovernor`; `apply_lifecycle_rules()`; backend `LifecyclePolicyEngine.ResolvePolicy()`; scheduler; workflow lifecycle state; durable audit records; policy snapshots and worker-side enforcement.
- Closure path: operations emit cost/call/failure/latency/tool/approval evidence -> BoundFlow stores rolling/version metrics -> the configured lifecycle rule is evaluated -> the parent-selected action changes effective model/caps or workflow state/version -> scheduler/worker subsequent execution uses that returned current-control state.
- Boundary reachability: the documented self-hosted SDK/control-plane API directly exposes `set_agent_runtime_policy`, `set_agent_lifecycle_policy` and `set_workflow_lifecycle_policy`; the backend/worker standard distribution evaluates and enforces those policies in ordinary workflow execution.
- Why this is / is not agent-owned: the runtime has hard authority to block, meter, pause, cool down and change versions, but Methodology 0.3.6 separates enforcement from decision ownership. Counterfactually removing the operator-selected rule while leaving the deterministic evaluator in place removes the reason/action choice; the evaluator cannot independently decide what constitutes unacceptable cost/failure or which target model/version should replace the current one.
- Whole-system current view: workflow lifecycle evaluation consumes rolling metrics and version-level totals for the managed workflow, while agent lifecycle evaluation consumes recent per-agent invocation history inside the same managed workflow. The resulting state is applied at the workflow/agent control boundary rather than as one model's local task observation.
- Current-control decision scope: current constraints and intervention over model selection, maximum calls/cost/tokens, tool limits, workflow pause/cooldown and active workflow version. These affect resource use and whether/how the operational workflow may continue.
- Evidence: [`README.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/README.md); [`sdk/python/boundflow/policies.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/policies.py); [`sdk/python/boundflow/lifecycle.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/lifecycle.py); [`internal/lifecyclepolicy/engine.go`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/internal/lifecyclepolicy/engine.go); [`docs/concepts.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/docs/concepts.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is specifically a parent-governed self-hosted operator mode. A deterministic policy engine is not credited with autonomous S3 ownership, and ordinary per-task human approval is not relied on to establish the whole-system S3 function.

## S3* — Complementary audit

- State: —
- Function: no qualifying complementary and sufficiently independent audit judgment with corrective return is established in the supported runtime.
- Disturbance / variety regulated: BoundFlow records governance decisions and detailed run traces, and it monitors cost/failure/tool metrics, but those evidence surfaces primarily report or enforce the same operational/control paths.
- Decisive decision or feedback right: no separately situated auditor is shown obtaining materially complementary access to operational reality, issuing an independent audit judgment and returning findings that change subsequent operation.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: server-side governance audit log; operation/agent/LLM/tool traces; OpenTelemetry sinks; policy metric counters; approval audit; deterministic lifecycle evaluation; tests.
- Closure path: operational/control decisions -> audit/trace records and metrics; policy evaluation can act on the same recorded operational metrics, but there is no independent audit judgment -> corrective finding -> changed operation loop.
- Why this is / is not agent-owned: logging a policy action or trace, validating limits, or reusing ordinary run metrics for lifecycle control does not create complementary audit independence.
- Evidence: [`README.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/README.md); [`docs/concepts.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/docs/concepts.md); [`sdk/python/boundflow/worker.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/worker.py).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a downstream application could attach an independent reviewer/auditor through tools/workflow code, but generic extensibility does not establish first-party S3*.

### Absence scope

- Surfaces inspected: governance audit log, run traces, metric reporting, lifecycle evaluation, runtime-policy enforcement, approval audit, worker/server separation and tests/examples documenting those paths.
- Plausible first-party paths checked: governance audit as auditor; OTel/run tracing; scheduler as independent monitor; approval decisions; policy-rule evaluation; platform interruption detection.
- Why no material first-party path remains: the audit log and traces are evidence records rather than independent audit judgment, while scheduler/governor/policy checks consume ordinary operational/control evidence and enforce configured constraints. No complementary-access independent corrective auditor is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: no qualifying external-and-prospective intelligence loop that develops and adopts future capability/posture from environmental distinctions is established in the standard runtime.
- Disturbance / variety regulated: prior-run cost/failure/latency/tool/approval metrics can change later operating constraints or active workflow version, but these are inside-and-now operational/control signals rather than an external prospective intelligence process.
- Decisive decision or feedback right: no first-party actor is shown sensing external/future-relevant change, generating alternative capability/strategy options and selecting an adaptation that returns into present capability.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: agent/workflow lifecycle metrics; model switching; version rollback; durable history; operator-updated workflow versions/configuration; external integration support.
- Closure path: prior internal run metrics -> configured lifecycle rule -> current model/cap/version control is S3 parent governance; no external distinction -> prospective adaptation option -> adopted changed capability loop closes.
- Why this is / is not agent-owned: automatic model downgrade or workflow rollback reacts to internal performance under an already-authored rule. It changes current operating posture but does not develop future options from the outside environment. New workflow versions/policies remain developer/operator-authored outside the autonomous runtime.
- Evidence: [`README.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/README.md); [`sdk/python/boundflow/lifecycle.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/lifecycle.py); [`internal/lifecyclepolicy/engine.go`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/internal/lifecyclepolicy/engine.go).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: lifecycle adaptation is intentionally not promoted to S4 merely because it affects future runs; the decisive evidence remains internal operational performance under pre-authored current-control rules.

### Absence scope

- Surfaces inspected: agent/workflow lifecycle policy, version switching, history/metrics, workflow registration/versioning, integrations, approval/input paths, scheduler and documented governance examples.
- Plausible first-party paths checked: model switching as adaptation; automatic rollback; version metrics; approval-rejection response; customer-defined future workflow versions; external input gates.
- Why no material first-party path remains: first-party automatic reactions use internal current-operation metrics and fixed actions. Externally/future-derived option generation and autonomous return into installed capability are not supplied.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy authority is established at the managed-workflow recursion.
- Disturbance / variety regulated: workflow purpose/code, system prompts, tool set, model/provider, runtime/lifecycle policies, version targets, approvals and deployment configuration constrain behavior but are authored by operator/developer/parent rather than decided by a first-party S5 closure.
- Decisive decision or feedback right: define or revise the ultimate purpose/identity/top-level normative policy of the BoundFlow-managed organization itself.
- Decision owner: external operator/developer/configuration; no qualifying first-party S5 closure is established.
- Supporting / enforcement mechanisms: workflow registration/versioning; runtime/lifecycle policy storage and enforcement; API keys/tenant state; approval gates; model/tool configuration; server-side governance audit.
- Closure path: top-level purpose/policy is supplied through workflow code/configuration and then enforced; no identity-level issue -> authoritative S5 judgment -> returned top-level policy -> subsequent organization governed by that decision loop closes inside the harness.
- Why this is / is not agent-owned: BoundFlow can strongly enforce policy without deciding what the organization ultimately is for or which ultimate policy it should adopt. Generic operator configuration and task approvals are explicitly insufficient S5 evidence.
- Evidence: [`README.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/README.md); [`sdk/python/boundflow/policies.py`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/sdk/python/boundflow/policies.py); [`docs/concepts.md`](https://github.com/boundflow/boundflow/blob/15c0b20a3a98d3413956cab7fba2fd77c1fa32e2/docs/concepts.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the S3 parent mode records legitimate operator authority over current control; it does not imply that every operator-authored policy is S5.

### Absence scope

- Surfaces inspected: workflow registration/versioning, runtime/lifecycle policy APIs, approval/input gates, tenant/API-key provisioning, agent definitions/system prompts, scheduler/control-plane state and governance audit.
- Plausible first-party paths checked: operator lifecycle policy as S5; workflow version as identity; tenant/API-key identity; approval gate as ultimate authority; model/tool policy; workflow type/name and system prompt.
- Why no material first-party path remains: these surfaces configure, authorize or enforce operation beneath an externally supplied purpose. No first-party runtime process deliberates and closes identity/ultimate-policy questions for the organization.

## Recursion

The assessed recursion is one BoundFlow-managed workflow organization, including repeated runs and the first-party control plane/SDK worker paths that regulate them. An `AgentDefinition` step is a lower-level operational actor within that workflow. Independent customer applications could compose multiple separately accountable workflows/agents into a higher-recursion organization, but that downstream topology is not imported into the generic BoundFlow assessment.

## Variety and escalation

BoundFlow attenuates task variety through the model/tool S1 loop and operational risk variety through hard runtime caps, durable state, leases/recovery and parent-authored lifecycle policy. Tool/model failures return through the ordinary S1 channel; repeated cost/failure/latency/approval/tool signals can trigger operator-selected S3 interventions such as model-cap changes, pause, cooldown or version rollback. Application code may explicitly escalate to a human through `AwaitApproval`/`AwaitInput`, while platform interruption can disable a workflow for operator resolution. These escalation mechanisms are recorded according to the function they serve and are not promoted to S5 or S3* by their names.

## Evidence gaps

- Structural/static review only; no live BoundFlow deployment or external LLM/tool service was executed during this assessment.
- The repository is explicitly public preview/pre-1.0 at the reviewed ref; the engine is documented/tested but not yet described as production-proven with external users.
- Downstream workflows can compose additional agents, coordination, review and adaptation. Those application-specific organizations are separate systems-in-focus and must not donate S2/S3*/S4/S5 states to generic BoundFlow.
- The parent S3 classification depends on the documented self-hosted operator being the legitimate parent for the managed workflow and on lifecycle policies being intentionally operator-authored whole-workflow current-control decisions; deterministic evaluation/enforcement is not treated as autonomous decision ownership.