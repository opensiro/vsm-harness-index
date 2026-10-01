---
harness_id: zhizhi-agent-runtime
project_name: Zhizhi Agent Runtime
repository: https://github.com/cocoyes/zhizhi-agent-runtime
review_ref: 02465df2afbe6d511d20fa275ccffe0c40b1b31c
reviewed_at: 2026-10-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-01
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Zhizhi Agent Runtime

## Review boundary

- System in focus: one first-party Zhizhi Go `Agent` runtime deployment at pinned revision `02465df2afbe6d511d20fa275ccffe0c40b1b31c`, including its standard simple and complex execution modes, model-backed planning/replanning, bounded ReAct execution, typed tools/MCP integration, checkpoint/resume, failure policy, side-effect controls and observability.
- Purpose and identity: execute user requests through a model-driven agent runtime that can select tools, plan dependency-safe work, act on typed capabilities, recover within bounded execution and return evidence-backed answers.
- Relevant environment: users/callers, caller-configured model/provider, registered tools and MCP servers, external systems affected by tools, runtime deadlines/budgets, checkpoint storage, and optional human confirmation for side effects.
- Standard-distribution boundary: the public `zhizhi` runtime plus its public packages and the `internal/runtime` implementation reached through normal `Agent.Run`/`Stream`/`Resume` use. External model/provider internals, external tool implementations, MCP server internals and caller application code remain separate systems.
- Credited operating / distribution surfaces: `Agent.Run`/`Resume`; simple model-tool execution; complex `ModelPlanner` → compiled scheduler → bounded `ModelReplanner` path; nested agentic plan steps implemented by the private ReAct runner; public policy/checkpoint/route/observe surfaces as wired by the runtime.
- Adjacent first-party surfaces excluded from ownership: `.agents/skills/*` repository-development/authoring artifacts; examples and tests as organizational owners; the caller-facing `eval` helper; CI/release/repository governance; documentation-only claims not wired into runtime operation.
- First-party operating / deployment modes considered: chat/simple agent mode, complex planned execution, tool steps, nested `agentic` steps, failure/replan recovery, confirmation suspend/resume, MCP capability selection, and configured policy/guard paths.
- Recursion level: one deployed Zhizhi `Agent` runtime serving one request/run organization. Nested `agentic` steps are bounded transient task cells inside that run; they are not promoted to separate recursively viable S1 units merely because each can execute a local model-tool loop.
- Reviewed revision: `02465df2afbe6d511d20fa275ccffe0c40b1b31c`.
- Observation date: 2026-10-01.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Zhizhi exposes a public `Agent` facade with `Run`, `Stream`, `Resume`, and `Close`. A run builds an immutable effective tool registry, optionally selects MCP tools, routes the request, and then executes either a simple model-tool loop or complex mode. In simple mode the configured model chooses tool calls from observations until it emits a final answer or reaches bounded termination.

Complex mode adds a model-backed planner that produces a dependency-safe plan, validates and compiles that plan, then executes batches through the internal scheduler. Plan steps may be ordinary tool steps or bounded `agentic` steps. An `agentic` step receives a local goal, success criteria, capability allowlist and tool-call budget, then runs a private ReAct loop using the configured model. If a required complex step fails, the default model-backed replanner may add, replace or remove plan steps subject to compatibility and structural validation; already completed compatible work can be reused. Final composition is again model-backed but constrained to structured execution facts.

The scheduler supplies dependency bindings, conditional execution, bounded parallelism, failure policy, confirmation checkpoints and a write barrier for ordinary tool steps. That barrier serializes write tool steps, but the scheduler enters the `agentic` execution branch before acquiring the barrier, so it is not evidence of inter-agent coordination among nested agentic cells. The runtime also exposes JSONL/event observability and a caller-facing `eval` helper, but these are routine reporting/testing surfaces rather than an independent complementary audit path.

Primary evidence:

- [`README.md`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/README.md) — documented lifecycle, complex planning, bounded replanning, side-effect controls, checkpoints and observability.
- [`docs/architecture.md`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/docs/architecture.md) — public package boundary and internal runtime split.
- [`agent.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/agent.go) — standard run modes, model-tool loop, complex planner/scheduler/replanner closure, agentic-step executor and checkpoint/resume behavior.
- [`internal/runtime/react/react.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/internal/runtime/react/react.go) — bounded local model-tool feedback loop used by agentic steps.
- [`plan/plan.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/plan/plan.go) — task-plan step model, dependency graph and `agentic` step contract.
- [`plan/planner.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/plan/planner.go) and [`plan/replan.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/plan/replan.go) — model-driven task decomposition and failure-local plan repair.
- [`internal/runtime/exec/scheduler.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/internal/runtime/exec/scheduler.go) — dependency batches, parallel execution, ordinary-tool write barrier, confirmations and result propagation.
- [`policy/policy.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/policy/policy.go) — deterministic failure classification/retry/fallback policy.
- [`eval/eval.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/eval/eval.go) — caller-facing scenario evaluation helper inspected for S3* and excluded from runtime ownership.

## Operational model

The runtime's primary transformation is one request-to-answer execution loop. In simple mode, the model chooses substantive tool actions from current observations; tool results feed subsequent model calls until a final answer. In complex mode, the same configured model may first decide a task plan and later repair that task plan after a required step failure. The scheduler and policy machinery enforce dependency, budget, retry, confirmation and side-effect constraints around those model decisions.

Nested `agentic` plan steps have local autonomous model-tool choice, but at the reviewed recursion they are transient decomposition cells created to complete one parent request. They have no independently evidenced durable contribution/identity/local environment/metasystem establishing recursive viability. Consequently, task dependencies, batch scheduling and replanning are analyzed as S1-internal task regulation rather than automatically promoted to S2/S3.

## S1 — Operations

- State: A
- Function: transform a user request into an answer and/or tool-mediated outcome through autonomous model decisions grounded in returned tool evidence.
- Disturbance / variety regulated: ambiguous user intent, changing model/tool observations, tool failures, conditional evidence, capability availability, side-effect uncertainty and bounded execution constraints.
- Decisive decision or feedback right: choose the substantive next tool/action or final answer in simple mode; in complex mode, choose the executable task plan and bounded failure repair while local agentic steps choose actions within their allowed capabilities.
- Decision owner: the configured model actor operating through first-party Zhizhi loops; deterministic runtime machinery validates, schedules, executes and constrains its choices.
- Supporting / enforcement mechanisms: tool registry and schemas, route selection, planner/replanner structured-output validation, scheduler, ReAct runner, policy retry/fallback, guards, confirmations, checkpoints, evidence records, budgets and final composer.
- Closure path: request + current evidence → model selects tool/action/plan → first-party runtime validates and applies the choice → tool/execution evidence returns to the model or replanner → model revises behavior or emits the final response.
- Boundary reachability: `Agent.Run` is the standard public entry point and directly wires the configured model into simple execution or the built-in complex planner/replanner/runtime path; no repository-development actor is borrowed to close S1.
- Why this is / is not agent-owned: removing the configured model actor while leaving deterministic runtime machinery in place removes the semantic action selection, plan choice, replan choice and final composition; materially the same discretionary operation no longer occurs.
- Evidence: [`agent.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/agent.go); [`internal/runtime/react/react.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/internal/runtime/react/react.go); [`plan/planner.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/plan/planner.go); [`plan/replan.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/plan/replan.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: model inference is caller-configured/external, but the first-party distribution supplies and closes the model-driven control/feedback organization around it.

## S2 — Coordination

- State: —
- Function: no material inter-S1 conflict/oscillation attenuation path is established at the declared runtime recursion.
- Disturbance / variety regulated: dependency ordering and ordinary write serialization regulate task execution hazards, but no specific conflict among distinct recursively meaningful S1 operational units is established.
- Decisive decision or feedback right: no qualifying S2 decision right is established.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: dependency DAG, batch scheduler, bounded concurrency, evidence bindings and an ordinary-tool write barrier.
- Closure path: dependency/batch results affect later task steps, but this is parent-task sequencing/state propagation rather than an evidenced inter-S1 coordination loop.
- Boundary reachability: the inspected scheduling mechanisms are reachable in complex mode, but the S2 organizational function is not established.
- Distinct S1 units: one deployed request/run is the S1 unit at the declared recursion; nested `agentic` steps are transient task cells and are not independently evidenced as recursively viable operational units.
- Inter-S1 disturbance: none established between qualifying S1 units.
- Attenuating coordination relation: no qualifying relation. The scheduler's write barrier applies to ordinary tool steps; the `agentic` branch returns before that barrier is acquired.
- Feedback into subsequent S1 behaviour: dependency evidence changes later task execution, but without distinct qualifying S1 units and an inter-S1 disturbance this remains S1-local workflow feedback.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not; the reviewed positive-looking mechanisms are dependency sequencing, bounded parallel execution and shared task evidence, which the Profile explicitly does not treat as S2 without the missing inter-S1 conflict witness.
- Why this is / is not agent-owned: function absent at this recursion, so ownership is not assigned.
- Evidence: [`plan/plan.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/plan/plan.go); [`internal/runtime/exec/scheduler.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/internal/runtime/exec/scheduler.go); [`agent.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/agent.go).
- Basis: structural absence review
- Confidence: high
- Caveats: a downstream application could compose multiple durable Zhizhi agents and add coordination; that larger organization is outside this runtime boundary.

### Absence scope

- Surfaces inspected: task-plan model, agentic-step contract, scheduler batches/concurrency/write barrier, result bindings, routing, runtime run/complex paths and nested ReAct execution.
- Plausible first-party paths checked: dependency ordering, batch parallelism, write serialization, agentic-step concurrency and evidence propagation.
- Why no material first-party path remains: the runtime does not establish multiple qualifying S1 units at the assessed recursion plus a concrete inter-unit disturbance and function-specific attenuation loop; the apparent coordination surfaces are task decomposition/execution mechanisms.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control function above the declared S1 operation is established.
- Disturbance / variety regulated: required step failure, execution budgets, deadlines, retries, confirmations and plan inconsistency are regulated inside the current request execution.
- Decisive decision or feedback right: the model-backed replanner can add/replace/remove steps after a required task step fails, but that right repairs one parent task plan rather than governing a set of current operational units on behalf of a larger whole.
- Decision owner: no separate S3 owner established; the model's replan discretion is part of S1 task execution at this recursion.
- Supporting / enforcement mechanisms: scheduler, budgets, failure policy, replanner patch validation, successful-step reuse, checkpoints, guard/confirmation gates and final structured evidence.
- Closure path: failure → model-generated task-plan patch → validation → subsequent task execution changes. This is a closed recovery path, but its organizational function is task-local S1 regulation rather than whole-system S3.
- Boundary reachability: the recovery path is directly reachable in standard complex mode, but reachability alone does not change its function into S3.
- Whole-system current view: the replanner receives the current task plan, failure description and tool catalog, not a separately evidenced whole-organization current operations view across durable S1 units.
- Current-control decision scope: add/replace/remove task steps and preserve reusable completed work within the same request.
- Why this is / is not agent-owned: the model owns the discretionary repair choice, but ownership is assigned only after the organizational function is established; here the qualifying S3 function is absent.
- Evidence: [`agent.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/agent.go); [`plan/replan.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/plan/replan.go); [`internal/runtime/exec/scheduler.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/internal/runtime/exec/scheduler.go); [`policy/policy.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/policy/policy.go).
- Basis: structural absence review
- Confidence: high
- Caveats: the runtime is deliberately rich in current-task control; the negative state reflects the Profile distinction between task decomposition/recovery and metasystemic whole-system S3.

### Absence scope

- Surfaces inspected: planner/replanner, semantic plan/patch model, scheduler, budgets, retry/fallback policy, checkpoint/resume, guard/confirmation paths, routing and final composition.
- Plausible first-party paths checked: model replanning after failures, scheduler control over batches/concurrency, budget enforcement, confirmation suspension/resumption and retry/fallback decisions.
- Why no material first-party path remains: every reviewed current-control mechanism regulates the same request/task execution; no separate metasystemic current view and authority over multiple durable S1 operations is established.

## S3* — Complementary audit

- State: —
- Function: no material complementary sufficiently independent audit path is established in the operating runtime.
- Disturbance / variety regulated: traces, evidence records and scenario evaluation make execution inspectable, but they do not independently challenge ordinary operational claims and return findings into control.
- Decisive decision or feedback right: no independent audit judgment with a corrective return path is established.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: JSONL/events, execution evidence/action receipts, structured final-composer facts, and the caller-facing `eval` scenario helper.
- Closure path: ordinary runtime evidence feeds normal task composition/reporting; `eval` invokes the same public agent and checks configured limits externally to the run. Neither supplies a complementary independent audit-and-return loop.
- Boundary reachability: observability is reachable in the standard runtime; `eval` is an adjacent caller-facing testing utility explicitly separated from runtime implementation in the architecture documentation.
- Claim being audited: no qualifying claim/audit relation established.
- Ordinary reporting path: normal `Response`, `Evidence`, `Actions`, warnings/statistics and observer events.
- Complementary access path: none established; scenario evaluation consumes the same run response rather than materially independent operational reality.
- Independence boundary: no separate auditor/ground-truth/replay path with sufficient independence is wired into the standard run.
- Who acts on findings: no first-party runtime controller is shown consuming complementary audit findings.
- Why this is / is not agent-owned: function absent; the README adjective "auditable" describes inspectability rather than autonomous S3* ownership.
- Evidence: [`README.md`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/README.md); [`docs/architecture.md`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/docs/architecture.md); [`eval/eval.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/eval/eval.go); [`agent.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/agent.go).
- Basis: structural absence review
- Confidence: high
- Caveats: downstream users can independently evaluate traces/results, but that external organization is not a first-party closed S3* runtime path.

### Absence scope

- Surfaces inspected: observer/events, execution evidence, warnings/actions/statistics, final structured-evidence composition, public `eval` package, README/architecture auditability claims and repository `.agents` development artifacts.
- Plausible first-party paths checked: trace inspection, scenario limits, evidence records, final-composer grounding and repository-local authoring/review helpers.
- Why no material first-party path remains: standard operation has routine reporting/evidence only; adjacent development/eval surfaces are not wired as a complementary independent audit authority with feedback into the running organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective capability-adaptation loop is established.
- Disturbance / variety regulated: current request context, tool availability, failures and execution evidence can change the task plan, but they do not produce future-facing organizational adaptation options.
- Decisive decision or feedback right: no first-party path develops prospective environmental options and returns an adaptation decision into current runtime capability.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: model planner/replanner, MCP capability selection/refresh, routing, task evidence and failure recovery.
- Closure path: replanning changes the current task after an actual failure; MCP/catalog refresh changes available current tools. Neither closes external/future distinction → adaptation option → present capability change.
- Boundary reachability: the inspected planning/replanning and capability-selection paths are reachable, but the S4 organizational function is absent.
- External distinction: tools/MCP and their failures provide current external evidence.
- Future / prospective distinction: no separate prospective environmental model/forecast/opportunity-threat distinction was found.
- Adaptation option generated: no qualifying future-oriented capability/policy adaptation option is generated.
- Path back into current capability / S3: task replanning returns to current execution, not to organizational capability adaptation.
- Why this is / is not agent-owned: model planning and replanning are task-local; the Profile explicitly excludes internal task planning from S4 without the missing external/prospective adaptation loop.
- Evidence: [`README.md`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/README.md); [`plan/planner.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/plan/planner.go); [`plan/replan.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/plan/replan.go); [`agent.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/agent.go).
- Basis: structural absence review
- Confidence: high
- Caveats: downstream applications could persist trends and use them to change runtime capabilities, but no such standard first-party loop is established here.

### Absence scope

- Surfaces inspected: planner/replanner, routing, MCP capability selection/refresh, tool catalog, execution evidence/observability, failure recovery and checkpoint/resume.
- Plausible first-party paths checked: current-environment tool discovery, model task planning, failure-driven replanning, refreshed MCP catalogs and reuse of execution evidence.
- Why no material first-party path remains: all reviewed adaptation-like behavior is reactive/current-task execution; none develops future-oriented environmental distinctions into options that alter present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy decision-and-return loop is established.
- Disturbance / variety regulated: guards, confirmation requirements, allowlists, budgets, retry classes, side-effect metadata and checkpoint approval constrain execution, but these are operational safety/configuration decisions.
- Decisive decision or feedback right: no runtime path receives an identity/ultimate-policy issue, reaches legitimate ultimate authority, and returns a newly authoritative identity/policy decision into operation.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: caller-supplied guard and confirmation functions, tool risk/side-effect metadata, retry/fallback policy, budgets, capability allowlists and resume approval.
- Closure path: confirmation can suspend a particular side effect and caller approval/rejection changes that task's execution; this closes operational authorization, not identity/ultimate-policy governance.
- Boundary reachability: safety/policy mechanisms are standard reachable configuration surfaces, but the S5 organizational function is absent.
- Identity / ultimate-policy issue: none shown as a runtime decision object.
- Ultimate authority in each claimed mode: no positive S5 mode claimed.
- Return-to-operation path: task-level confirmation and configured constraints affect execution, but no newly decided ultimate policy/identity returns from legitimate S5 authority.
- Why this is / is not agent-owned: neither the model nor deterministic policy engine is shown owning identity/ultimate-policy authority; static/configured constraints do not become S5 by enforcement.
- Evidence: [`agent.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/agent.go); [`policy/policy.go`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/policy/policy.go); [`README.md`](https://github.com/cocoyes/zhizhi-agent-runtime/blob/02465df2afbe6d511d20fa275ccffe0c40b1b31c/README.md).
- Basis: structural absence review
- Confidence: high
- Caveats: caller institutions may hold ultimate policy externally; that parent organization is not operationally closed as a first-party S5 mode by this runtime.

### Absence scope

- Surfaces inspected: guards, confirmation/resume, side-effect and risk metadata, budgets, policy retry/fallback, capability allowlists, system prompt/configuration and MCP trust controls.
- Plausible first-party paths checked: human confirmation, caller guard decisions, configuration selection, retry policy, model planning constraints and resume approval.
- Why no material first-party path remains: these mechanisms authorize/constrain ordinary task execution; none represents an identity/ultimate-policy issue and legitimate ultimate-authority return loop at the assessed recursion.

## Distributed OSS parent arrangement

Repository maintainers govern development of the Go library, while `.agents/skills/*` contains repository/development authoring machinery. Those surfaces are adjacent to the shipped runtime purpose and are not used to infer product S3/S4/S5 ownership.

## Self-hosted and non-human modes

Zhizhi is self-hostable and model-agnostic. A caller can replace model, planner, replanner, router, guards, confirmation and persistence components, but configurability does not by itself add positive VSM functions. The published vector reflects the first-party runtime organization reachable without importing a downstream organizational wrapper.

## Recursion

The deployed Agent/run is the assessed S1. A complex plan can create nested `agentic` steps, each with a local goal, allowlisted capabilities, success criteria and bounded ReAct loop. These are meaningful autonomous task cells but, at the reviewed evidence boundary, they remain transient decomposition of one parent request rather than separate recursive viable systems: no durable parent contribution, independent identity/environment or local metasystem is established. Spawning/nesting therefore does not change the declared recursion.

## Variety and escalation

The model absorbs semantic task variety; typed schemas, dependency validation and capability allowlists attenuate execution variety; retry/fallback, replanning and confirmation/resume handle bounded exceptions. Required-step failure can escalate into the model replanner, and risky side effects can suspend for caller confirmation. These are exception paths inside S1 task execution at this recursion, not evidence by themselves of separate S3/S4/S5 functions.

## Evidence gaps

No unresolved evidence gap requires `?` for the published vector. Reassessment would be warranted if a standard first-party mode introduced durable multiple-agent operational units with explicit conflict attenuation, a metasystemic whole-current controller, an independent audit-and-return path, a prospective environment-to-capability adaptation loop, or runtime identity/ultimate-policy authority.