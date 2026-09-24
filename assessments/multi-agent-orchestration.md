---
harness_id: multi-agent-orchestration
project_name: Multi-Agent Orchestration Engine
repository: https://github.com/Vinay-veeragani/Multi-Agent-Orchestration
review_ref: e6c34462af045d7e53d383103346362351c96353
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Multi-Agent Orchestration Engine

## Review boundary

- System in focus: one first-party Multi-Agent Orchestration Engine execution at pinned revision `e6c34462af045d7e53d383103346362351c96353`, including the registered task agents, shared agent reason/act runtime, autonomous supervisor, dynamic/static workflow execution, routing validation/fallback, budgets/tool policy, approvals and execution/checkpoint state.
- Purpose and identity: execute a user objective through one or more autonomous task agents while a first-party supervisor can dynamically allocate current work, retry/replan failed work, fan out parallel work, request action-scoped approval and decide when the execution can finalize or fail.
- Relevant environment: user objectives, model providers, external tools/services, PostgreSQL/Redis infrastructure, filesystem/network resources reached by tools and operator approval decisions.
- Standard-distribution boundary: repository-owned Python runtime under `src/orchestration`, including agent definitions/runtime, supervisor, workflow/dynamic orchestration, policy/budget/approval plumbing, state/checkpoint/event storage interfaces and built-in tool surfaces. External model/provider internals, PostgreSQL/Redis implementations and downstream services/tools remain environmental dependencies.
- Credited operating / distribution surfaces: `README.md`; `src/orchestration/agents/runtime.py`; `src/orchestration/supervisor/supervisor.py`; `docs/supervisor-and-routing.md`; `docs/dynamic-orchestration.md`; `docs/workflow-engine.md`; `src/orchestration/coordination/redis.py`; `docs/budget-and-policies.md`; `docs/human-in-the-loop.md`; standard runtime paths reached by those modules.
- Adjacent first-party surfaces excluded from ownership: `benchmarks/`, benchmark result artifacts, repository tests, CI/release/contributor governance, architecture-audit documents used only to validate/develop the project and examples that are not wired into the standard runtime. They may corroborate reachability but do not donate VSM ownership to the assessed execution.
- First-party operating / deployment modes considered: standard dynamic execution driven by `ExecutionOrchestrator` + `Supervisor`; standard static `WorkflowExecutor` path where relevant to supporting execution; optional action/tool approval gates. Benchmark-only arm selection is excluded from ownership classification.
- Recursion level: one orchestration execution is the system-in-focus. Autonomous registered task-agent invocations are operational units. The autonomous supervisor plus execution machinery forms the run-level metasystem for current control.
- Reviewed revision: `e6c34462af045d7e53d383103346362351c96353`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The standard agent runtime supplies a reusable autonomous reason/act loop. An `AgentDefinition` selects prompt, tool allowlist, model criteria and limits; `AgentRuntime` iterates model reasoning, authorised tool execution and tool-result feedback until the agent returns a validated output or reaches its iteration ceiling.

Dynamic orchestration places an autonomous supervisor above those task agents. `ExecutionOrchestrator` repeatedly supplies live `ExecutionState` to `Supervisor.decide()`. The supervisor model emits a typed `RoutingDecision`; allowed actions include `delegate`, `parallel_delegate`, `retry`, `replan`, `request_human_approval`, `respond_directly`, `finalize` and `fail`. Schema and semantic validators reject impossible decisions, with a deterministic `HeuristicRouter` fallback when the autonomous supervisor cannot produce a usable one. Valid decisions are compiled into the workflow/execution engine, whose scheduler, budgets, policy engine, checkpoints and approval service enforce/transport the selected action.

The repository also provides DAG joins, local/distributed concurrency primitives, retries, durable checkpoints, action-scoped approvals, evaluation infrastructure and a deterministic orchestration benchmark. These are separated below from the organizational decision rights they support.

## S1 — Operations

- State: A
- Function: perform assigned operational task work through autonomous agent reason/act loops that can choose tool use and produce task outputs.
- Disturbance / variety regulated: task uncertainty, model/tool feedback, external data returned by allowed tools and local decisions required to satisfy each delegated instruction.
- Decisive decision or feedback right: choose task-local reasoning steps, permitted tool calls and when to return the assigned result.
- Decision owner: the autonomous model actor inside each first-party `AgentRuntime` invocation.
- Supporting / enforcement mechanisms: `AgentDefinition`, model routing, tool schemas, policy authoriser, budget checks, iteration limits, tool execution and output validation.
- Closure path: supervisor/workflow assigns a node instruction → `AgentRuntime` builds the agent context → autonomous model reasons and requests permitted tools → tool results feed back into the same loop → the agent returns a validated `AgentOutput` into execution state.
- Boundary reachability: the shared `AgentRuntime` is the standard execution path for registered agents, including dynamically delegated nodes; it is not a benchmark-only or development-only actor.
- Why this is / is not agent-owned: deterministic runtime code limits and transports the loop, but substantive task-local reasoning/tool choices are made by the model actor.
- Evidence: [`src/orchestration/agents/runtime.py`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/src/orchestration/agents/runtime.py); [`README.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider/model internals are environmental; ownership is credited only to the autonomous role reached through the first-party runtime.

## S2 — Coordination

- State: —
- Function: no material first-party run-level S2 coordination function is established at the reviewed boundary.
- Disturbance / variety regulated: the runtime contains parallel execution, joins, locks, semaphores and dependency scheduling, but the inspected standard paths do not establish a specific inter-S1 interference/conflict/oscillation together with a function-specific coordination decision/feedback path that changes subsequent autonomous agent behavior.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: workflow edges and join policies sequence/aggregate work; `max_concurrent_nodes` limits parallel execution; Redis locks/semaphores protect process-level mutual exclusion and capacity; supervisor delegation controls current work allocation. These are not promoted to S2 merely because they coordinate execution machinery.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the reviewed runtime has generic scheduling, synchronization and current-control mechanisms, but no evidenced S2-specific autonomous coordination discretion over a reconstructed inter-S1 disturbance.
- Evidence: [`docs/workflow-engine.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/workflow-engine.md); [`src/orchestration/coordination/redis.py`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/src/orchestration/coordination/redis.py); [`docs/dynamic-orchestration.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/dynamic-orchestration.md).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: a downstream workflow can use the supplied synchronization primitives to construct stronger coordination behavior; general framework expressiveness is not sufficient for `S2=C`.

### Absence scope

- Surfaces inspected: agent runtime/definitions, dynamic orchestration, static workflow scheduling, join/retry behavior, Redis locks/semaphores, supervisor routing and benchmark-adjacent coordination descriptions.
- Plausible first-party paths checked: parallel delegation/fan-out, DAG joins/dependencies, max-concurrency scheduling, Redis mutual exclusion/semaphores and supervisor rerouting/replanning.
- Why no material first-party path remains: these paths allocate, serialize, gate or aggregate work but the reviewed standard distribution does not tie them to a specific interaction-generated inconsistency/oscillation among distinct operational agents plus an S2-specific feedback relation into their later behavior. The supervisor's discretionary allocation/retry/replan role maps to S3 rather than being relabeled S2.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current execution as a whole by observing live run state and deciding which agents/work should run next, when failed work should retry or be replanned, when parallel work should be introduced, and when the run should finalize or fail.
- Disturbance / variety regulated: incomplete or failed work, changing execution progress, unsuitable delegation, exhausted/invalid routes, current resource/budget constraints, blocked work and uncertainty about whether more operational work is required.
- Decisive decision or feedback right: choose a `RoutingDecision` over `delegate`, `parallel_delegate`, `retry`, `replan`, `request_human_approval`, `respond_directly`, `finalize` or `fail` against the current `ExecutionState`.
- Decision owner: the autonomous supervisor model actor in the standard dynamic-orchestration mode.
- Supporting / enforcement mechanisms: typed routing schema, semantic validation, agent registry, deterministic fallback, `ExecutionOrchestrator`, workflow compilation/execution, budget meter, policy engine, checkpoint/event persistence and cancel token.
- Closure path: current execution/node state is supplied to `Supervisor.decide()` → autonomous supervisor selects a current-control action → first-party schema/semantic validators accept or degrade it → `ExecutionOrchestrator` compiles/applies the valid action → agents/nodes execute under that decision → resulting node state/output returns to the next supervisor turn.
- Boundary reachability: `ExecutionOrchestrator` explicitly calls the first-party `Supervisor` each turn in the supported dynamic execution path; this is the ordinary runtime design rather than an evaluator-only layer.
- Why this is / is not agent-owned: the supervisor model owns the discretionary current-control choice when it produces a valid decision. Deterministic validators, schedulers, budgets and policy gates enforce feasibility/constraints without inheriting the decision right. The heuristic fallback is a degraded deterministic mode rather than the basis for `A`.
- Evidence: [`src/orchestration/supervisor/supervisor.py`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/src/orchestration/supervisor/supervisor.py); [`docs/supervisor-and-routing.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/supervisor-and-routing.md); [`docs/dynamic-orchestration.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/dynamic-orchestration.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: static user-authored workflows and deterministic heuristic fallback are separate supported control paths; the `A` finding is specifically grounded in the standard autonomous dynamic-supervisor mode. Action-scoped human approval does not by itself establish an S3 parent mode.
- Whole-system current view: the supervisor prompt is built from current `ExecutionState`, registered agent summaries, tool surface and optional budget/workflow state; it can validate retries/replans against actual node status and current graph state.
- Current-control decision scope: delegation/allocation, parallel fan-out, retry, graph replan, approval escalation, direct response, finalization and failure of the current execution.

## S3* — Complementary audit

- State: —
- Function: no materially distinct complementary audit path over operational S1 reality is established in the reviewed standard distribution.
- Disturbance / variety regulated: routing/schema/policy validators can reject invalid decisions or calls, but they inspect conformance of the same control/tool path rather than independently challenge operational claims/results against alternative evidence.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Pydantic/schema validation, `Supervisor.validate_decision()`, policy checks, output validation, checkpoint consistency and benchmark/evaluation code provide correctness/enforcement surfaces but do not become S3* by label or verification vocabulary.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the reviewed validators are in-line deterministic gates around ordinary operation/current control; no separate autonomous or constructor audit actor with complementary access and corrective feedback into the same run was found.
- Evidence: [`src/orchestration/supervisor/supervisor.py`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/src/orchestration/supervisor/supervisor.py); [`docs/supervisor-and-routing.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/supervisor-and-routing.md); [`src/orchestration/agents/runtime.py`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/src/orchestration/agents/runtime.py).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: repository evaluation/benchmark infrastructure is adjacent first-party evidence and was excluded from runtime ownership under Methodology `0.3.6` boundary rules.

### Absence scope

- Surfaces inspected: supervisor schema/semantic validation, agent output validation, tool/policy gates, workflow failure handling, checkpoints, observability and benchmark/evaluation surfaces.
- Plausible first-party paths checked: semantic validation of supervisor decisions, validation of agent outputs/tool calls, benchmark scoring and failure/retry handling.
- Why no material first-party path remains: all inspected runtime checks are ordinary in-line validation/enforcement or current-control feedback. Benchmark/evaluation code is not wired as an independent production audit actor. No reviewed standard path independently observes operational reality, compares it with an S1 claim and returns a complementary audit judgment into corrective current control.

## S4 — Outside-and-then adaptation

- State: —
- Function: no external-and-prospective organizational adaptation loop is established in the reviewed standard distribution.
- Disturbance / variety regulated: retry/replan/model routing respond to the current task/run, and checkpoints preserve current execution state, but none establishes a separate outside/future sensing → adaptation option → returned capability change loop.
- Decisive decision or feedback right: not established for S4.
- Decision owner: not established.
- Supporting / enforcement mechanisms: supervisor `replan`, node retry policies, model routing, durable checkpoints/resume, configuration and benchmark/evaluation infrastructure support current execution/recovery without establishing prospective adaptation.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: current-run replanning is S3/current-control behavior; no first-party actor is evidenced as changing persistent organizational capability from external/future distinctions.
- Evidence: [`docs/dynamic-orchestration.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/dynamic-orchestration.md); [`docs/checkpointing-and-resume.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/checkpointing-and-resume.md); [`docs/evaluation-benchmark.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/evaluation-benchmark.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: retries, replanning and benchmark-driven development may improve the project in practice; they are not automatically run-level S4.

### Absence scope

- Surfaces inspected: dynamic supervisor loop, retry/replan, model routing, checkpoints/resume, persistent execution state, configuration, observability and benchmark/evaluation paths.
- Plausible first-party paths checked: supervisor replan, retry recovery, model selection, checkpointed history and benchmark feedback.
- Why no material first-party path remains: the reviewed mechanisms restore or alter the current execution but do not autonomously sense external/future-relevant change and persistently revise the organization's capability/repertoire for subsequent operation.

## S5 — Identity / ultimate policy

- State: —
- Function: no runtime identity/ultimate-policy governance loop is established at the assessed execution boundary.
- Disturbance / variety regulated: configured budgets, tool permissions, risk rules and approval gates constrain operation, but they are pre-existing operational policy/enforcement rather than an authoritative decision over organizational identity or ultimate policy.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deny-by-default tool policy, hard budgets, risk-level approval requirements, operator-supplied configuration and action-scoped human approvals.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the runtime enforces configured rules and can pause for action-specific approval, but no first-party standard mode was found in which an autonomous or parent authority adjudicates an identity/ultimate-policy question and returns a newly decided policy into subsequent organization-wide operation.
- Evidence: [`docs/budget-and-policies.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/budget-and-policies.md); [`docs/human-in-the-loop.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/docs/human-in-the-loop.md); [`README.md`](https://github.com/Vinay-veeragani/Multi-Agent-Orchestration/blob/e6c34462af045d7e53d383103346362351c96353/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a human may approve or modify one risky tool action; Methodology `0.3.6` explicitly does not promote generic operational approval to S5 parent governance.

### Absence scope

- Surfaces inspected: budgets, tool permissions/policy engine, human approval/resume, configuration, supervisor finalization and deployment docs.
- Plausible first-party paths checked: action approval, risk policy, operator configuration, budget tightening and supervisor final authority over a run.
- Why no material first-party path remains: inspected authority remains task-operational, safety/policy enforcement or current-control authority. No identity/ultimate-policy matter reaches a legitimate authority that decides and installs a changed governing policy for subsequent operation.
