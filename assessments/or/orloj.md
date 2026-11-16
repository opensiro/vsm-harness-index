---
harness_id: orloj
project_name: Orloj
repository: https://github.com/OrlojHQ/orloj
review_ref: 43173acfcf777e77c834f0cb87edee53d06f235a
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: P
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: P
---

# Orloj

## Review boundary

- System in focus: One deployed Orloj AgentSystem running tasks through its first-party worker/controller, resources, and operator's control API.
- Purpose and identity: Execute agentic tasks through a policy-governed, observable, declarative multi-agent system with durable task runs.
- Relevant environment: Task requests, tool backends, model services, distributed workers, operators and deployment infrastructure.
- Standard-distribution boundary: Shipped Go controller, HTTP API, configured resource stores, agent worker, task engine, tool runtimes, policy enforcement, approval and task status paths. Only supported self-hosted/operator modes are credited.
- Credited operating / distribution surfaces: `runtime/agent_worker.go`, `runtime/execution_engine.go`, `controllers/task_controller.go`, the AgentSystem and AgentPolicy API resources, and their persistent task/policy state.
- Adjacent first-party surfaces excluded from ownership: Contributor CI/roadmap, standalone conformance/tests/load tests, example blueprints not wired to an assessed run; separately invoked EvalRun benchmarking unless its findings enter the claimed operational control loop. External model/provider tool services do not donate their own higher-order decisions.
- First-party operating / deployment modes considered: Sequential task execution, message-driven agent systems, policy-scoped self-hosted operation, optional approval checkpoint configuration, and separately operated EvalRun.
- Recursion level: One declared AgentSystem composed of autonomous agent workers/tasks under a legitimate deployment operator.
- Reviewed revision: `43173acfcf777e77c834f0cb87edee53d06f235a`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Orloj ships a Go ReAct engine and model/tool-backed worker, declarative AgentSystem graph with routes, delegates and joins, controller-managed Tasks, retry/DeadLetter lifecycle, persistent API resource stores, policies, approvals and an eval subsystem. The operator creates and replaces AgentSystem and AgentPolicy resources through first-party API. `TaskController.executeTask` resolves the system's execution order, applicable policies and token/child limits before running workers. A separate `EvalRunController` starts sample Tasks, scores outputs and stores results; its inclusion in a live control decision must be demonstrated rather than assumed. [`runtime/agent_worker.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/runtime/agent_worker.go#L305-L377), [`controllers/task_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/task_controller.go#L2029-L2090), [`api/server.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/api/server.go#L813-L853), [`controllers/eval_run_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/eval_run_controller.go#L227-L302).

## Operational model

Configured agents receive model prompts, select tools, consume results and terminate or continue. Agents are operational units when running material outcomes, not simply graph nodes. The runtime stores tasks and handles retries and approval checkpoints; these are supporting mechanisms. Human/system operators select agent composition and apply policies, while the model remains the ordinary S1 decision owner. `AgentPolicy` records model/tool restrictions and budgets, but merely enforcing a policy is not ownership of a discretionary S3 or S5 decision.

## S1 — Operations

- State: A
- Function: Carry out task requests by dynamically selecting model and tool actions.
- Disturbance / variety regulated: Unknown inputs and tool responses, provider failures and changing local task context.
- Decisive decision or feedback right: Select model next step and tools based on observed model/tool history.
- Decision owner: The running model-backed AgentWorker; the external model provider supplies inference, not Orloj's independent metasystem ownership.
- Supporting / enforcement mechanisms: ReAct execution engine, tool runtime, configured model gateway, bounded steps, checkpoint and task-controller lifecycle.
- Closure path: Model response selects tool calls; tool results/errors enter worker history and can shape subsequent model choices; completion returns to the task controller.
- Why this is / is not agent-owned: Removing the agent model removes the discretion to choose task actions; deterministic controller/queue alone cannot carry out diverse tasks.
- Evidence: [`runtime/agent_worker.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/runtime/agent_worker.go#L305-L377); [`runtime/agent_worker.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/runtime/agent_worker.go#L528-L615); [`runtime/execution_engine.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/runtime/execution_engine.go#L73-L151); [`controllers/task_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/task_controller.go#L2208-L2225).
- Basis: structural
- Confidence: High for first-party reachable execution organization.
- Caveats: No live model-provider execution was performed for this assessment.
- Boundary reachability: The shipped TaskController resolves agents and invokes the bundled first-party TaskExecutor/ReAct worker under configured policies.

## S2 — Coordination

- State: ?
- Function: Possible regulation of interference among parallel delegated workers, beyond ordinary graph sequencing.
- Disturbance / variety regulated: Parallel agent outputs can be incomplete or incompatible, and dependent agents might need a stable coordinated view.
- Decisive decision or feedback right: Choose/resolve a response to materially conflicting operational contributions and return the resolution to affected agents.
- Decision owner: Unresolved. Declarative graph joins have configured deterministic wait/quorum/failure policies, but no verified distinct-agent conflict judgment owner.
- Supporting / enforcement mechanisms: `GraphEdge.Delegates`, `GraphJoin` wait/quorum semantics, agent message bus, task lifecycle and retries.
- Closure path: Graph routes and joins deliver outputs toward successor/delegate review. Whether this path detects specific competing commitments and changes subsequent S1 behavior to attenuate actual interference remains unverified.
- Why this is / is not agent-owned: The executor's join/retry logic applies developer-set policy; mere fan-in, routing and serialization do not prove model-owned inter-S1 coordination.
- Evidence: [`resources/resource_types.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/resources/resource_types.go#L39-L81); [`resources/graph.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/resources/graph.go#L283-L316); [`controllers/task_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/task_controller.go#L1445-L1469).
- Basis: structural; unresolved functional witness
- Confidence: Low for any positive S2 claim.
- Caveats: A verified exact-mode delegate re-execution resolving competing branches could change this result; do not infer S2 from a graph alone.

## S3 — Inside-and-now control

- State: P
- Function: Parent-controlled regulation of the current AgentSystem's permissible resources, models and task commitments.
- Disturbance / variety regulated: Current tasks and agents compete for budgets and available tools; failures, blocked tasks and overspend threaten system operations.
- Decisive decision or feedback right: The deployment operator chooses cross-agent policies and current run constraints, including scoped/global allowed models and token/child budgets.
- Decision owner: Legitimate parent operator in the shipped HTTP API and policy management mode, not the deterministic policy enforcement loop.
- Supporting / enforcement mechanisms: AgentPolicy store, API create/update, resource controllers, TaskController match/limit enforcement, task status/trace.
- Closure path: The accepted operator AgentPolicy is stored, matched to live Task/AgentSystem, and enforced before later agent execution, changing the allowable actions and resources of subsequent operations.
- Why this is / is not agent-owned: The worker may choose task tools, but cannot set the global/current portfolio constraints that the controller enforces.
- Evidence: [`api/server.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/api/server.go#L1629-L1669); [`api/server.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/api/server.go#L1721-L1767); [`controllers/task_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/task_controller.go#L2029-L2089); [`runtime/policy_enforcement.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/runtime/policy_enforcement.go#L10-L35).
- Basis: structural
- Confidence: Moderate; supported policy-operator loop observed in first-party code.
- Caveats: Policy controller itself simply reconciles Ready state; it is not an autonomous S3 owner.
- Boundary reachability: The public supported API persists global/scoped policy, and each packaged TaskController path reads matching policies during task execution.
- Whole-system current view: Task and AgentSystem endpoints show the configured system plus current task phases, logs and trace; the operator chooses policy against that bounded task organization, not all unrelated deployments.
- Current-control decision scope: Cross-agent model allowlist, blocked tools, token budget, child-depth/task limits; enforcement is not credited as autonomous policy selection.

## S3* — Complementary audit

- State: ?
- Function: Possible independently judged assessment of actual task outcomes through the separately shipped EvalRun mode.
- Disturbance / variety regulated: Ordinary task success reporting can omit quality failures; an external/scored sample may contradict an agent's apparent success.
- Decisive decision or feedback right: Independent judgment and corrective return to current controller for findings on operational reality.
- Decision owner: Unresolved. EvalScorer can compute exact-match or separate model-judge scores; no proven feedback from EvalRun decision back into the currently assessed operational control path.
- Supporting / enforcement mechanisms: EvalDataset sample tasks, EvalScorer and EvalRun result/summary store, completion review checkpoints.
- Closure path: EvalRun reads finished sample Task outputs and stores pass/fail and reasoning; whether an independent audit verdict affects later run control is not evidenced by the inspected path.
- Why this is / is not agent-owned: A separate judge/model could own audit judgment, but independent provider identity and returned corrective feedback to S3 were not established.
- Evidence: [`controllers/eval_run_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/eval_run_controller.go#L98-L176); [`controllers/eval_run_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/eval_run_controller.go#L227-L302); [`runtime/eval_scorer.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/runtime/eval_scorer.go#L21-L45); [`runtime/eval_scorer.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/runtime/eval_scorer.go#L79-L145).
- Basis: structural; unresolved audit boundary
- Confidence: Low for S3* positive classification.
- Caveats: An explicit supported integration from evaluation results into ordinary operating control is required; evaluation/samples alone are not S3*.
- Claim being audited: Whether a completed task output satisfies expected sample properties.
- Ordinary reporting path: Task status/output and worker traces.
- Complementary access path: Separate EvalDataset sample expectations or LLM-judge rubric.
- Independence boundary: Separate scorer component exists, but judge-provider independence and operational feedback/closure were not verified.
- Who acts on findings: EvalRun stores status/scores; no established automatic or legitimate parent corrective S3 action linked to those findings.

## S4 — Outside-and-then intelligence

- State: —
- Function: No established shipped externally informed, future-oriented adaptation loop in the bounded runtime organization.
- Disturbance / variety regulated: Evolving model/tool availability and future task requirements would require prospective capability choices.
- Decisive decision or feedback right: No integrated prospective environment-sensing and capability-adaptation decision found.
- Decision owner: None established for S4. Operators may change manifests; agents may retain memory, but these mechanisms do not by themselves own future adaptation.
- Supporting / enforcement mechanisms: Configurable AgentSystem/AgentPolicy, model gateways, memory manager, scheduler, EvalRuns and status telemetry.
- Closure path: No first-party path was established in which external/prospective intelligence generates options and returns an adaptation decision into current capability/S3.
- Why this is / is not agent-owned: Neither the agent model loop nor manifest editing is evidence of organizational outside-and-then judgment.
- Evidence: [`resources/resource_types.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/resources/resource_types.go#L30-L45); [`controllers/eval_run_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/eval_run_controller.go#L227-L302); [`api/server.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/api/server.go#L813-L853); [`runtime/policy_enforcement.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/runtime/policy_enforcement.go#L10-L47).
- Basis: structural
- Confidence: Moderate, bounded to reviewed shipped controllers, policy, eval, runtime and operator surfaces.
- Caveats: Not a claim that applications built with Orloj cannot implement adaptation.

### Absence scope

- Surfaces inspected: AgentSystem manifest/API, model/tool runtime, control policies, EvalRun scoring, task schedule/retry and worker memory.
- Plausible first-party paths checked: Model switching/fallback, operator manifest changes, memory persistence, evaluation scoring and scheduled tasks.
- Why no material first-party path remains: The reviewed modes choose or enforce current run configuration, report historical performance or maintain state; no linked external-and-future sensing → option judgment → adopted capability/S3 loop was shown in standard distribution.

## S5 — Policy and identity

- State: P
- Function: Human-owned ultimate identity and policy for the deployed AgentSystem and its permissible operational membership.
- Disturbance / variety regulated: Addition/removal of agent units and policy changes affect which organizational functions constitute the system and what actions are permissible.
- Decisive decision or feedback right: Set or replace the AgentSystem's authoritative list of agents/graph and the global operating policy that governs admitted workers.
- Decision owner: Legitimate deployment/operator authority through first-party AgentSystem and AgentPolicy endpoints; no first-party autonomous identity-governance loop established.
- Supporting / enforcement mechanisms: AgentSystem resource schema, API authorization/resource store, AgentPolicy resources, controller generation reconciliation, per-agent enforce step.
- Closure path: Operator-defined AgentSystem and global policy are persisted, loaded by TaskController, and govern which agents run and which model/tools they may use on subsequent tasks.
- Why this is / is not agent-owned: Model agents decide within the declared system; they do not autonomously own authority to redefine system membership and ultimate policy.
- Evidence: [`resources/resource_types.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/resources/resource_types.go#L30-L45); [`resources/resource_types.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/resources/resource_types.go#L867-L885); [`api/server.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/api/server.go#L813-L853); [`api/server.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/api/server.go#L1629-L1669); [`controllers/task_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/task_controller.go#L2029-L2063).
- Basis: structural
- Confidence: Moderate.
- Caveats: ToolApproval for one tool call is not S5; the claim is limited to constitution of the deployed system and organization-wide model/tool policy.
- Boundary reachability: API-created system/policy resources are first-party deployed resources and used in the controller that starts agent work.
- Identity / ultimate-policy issue: Which agents and graph constitute the AgentSystem, and which global model/tool restrictions bind its current and future operating units.
- Ultimate authority in each claimed mode: External legitimate operator; no autonomous internal identity authority verified.
- Return-to-operation path: Persisted manifest/policy → next task resolution/match → worker membership, resource and tool restrictions.

## Distributed OSS parent arrangement

This assessment concerns one deployed Orloj AgentSystem and its operator, not multiple GitHub contributors. Maintainer PR governance and repository CI are adjacent and are not used to manufacture an organizational parent mode.

## Self-hosted and non-human modes

Supported self-hosted policy/operator control is first-party. S3 and S5 parent rights are reported as `P`, without claiming independent agent-owned S3/S5 or that all runtime guardrails establish governance. A fully non-human application constructed with the framework may differ and requires a separately declared boundary.

## Recursion

Multiple Agent workers are S1 cells inside a configured AgentSystem. A graph of agents or agent-generated child tasks does not automatically create a higher-recursion VSM organization.

## Variety and escalation

Failures can return to retries/DeadLetter and task output review can pause for human decision, while policy denials prevent prohibited tools/models. These paths are current control or operational safety, not automatically new functions. [`controllers/task_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/task_controller.go#L1582-L1665), [`controllers/task_controller.go`](https://github.com/OrlojHQ/orloj/blob/43173acfcf777e77c834f0cb87edee53d06f235a/controllers/task_controller.go#L997-L1045).

## Evidence gaps

- S2: Inspect an exact supported concurrent delegate/fan-in configuration to establish whether its join/review closes specific inter-S1 interference, rather than merely waiting for responses.
- S3*: Trace evaluation results into a live or deliberately parent-controlled corrective action at the same operational recursion and prove independent access/judgment.
- Do not import eval benchmark fixtures, contributor CI, provider internals or external application policies as Orloj-owned decision makers.
- A source inspection and package wiring review were completed; live model provider traces were not executed.
