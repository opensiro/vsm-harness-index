---
harness_id: hivemind
project_name: Hivemind
repository: https://github.com/Emiyaaaaa/HiveMind
review_ref: 05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: P
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: P
---

# Hivemind

## Review boundary

- System in focus: One deployed Hivemind tenant's runtime organization of first-party LangGraph-backed agents and their ongoing Runs, under an authorized operator/admin.
- Purpose and identity: Carry out arbitrary agentic tasks while providing persistent execution, streaming events, operator control, versioned agent definitions, retries, checkpoints and multi-agent orchestration adapters.
- Relevant environment: User task requests, configured model services/tools, external MCP integrations, competing tenant/project resource usage, task errors, approval events, authorization and human operators.
- Standard-distribution boundary: Shipped Java/Spring Boot HTTP administration API, Python worker/adapter runtime, PostgreSQL run/agent definitions, Redis queue/cancellation/events, and first-party shipped `LangGraphAdapter` with model/tool feedback. Only supported installed paths counted.
- Credited operating / distribution surfaces: First-party Python LangGraph ReAct node and tool execution, RunService and worker status, tenant-scoped quota and run operator interfaces, administrative agent definitions/versions and shipped regression comparison capability.
- Adjacent first-party surfaces excluded from ownership: External LangGraph, model provider, AutoGen/CrewAI and plugin author internals; frontend presentation without runtime decision ownership; CI/OSS maintainer policies and developer roadmap; standalone benchmark fixtures and tests rather than installed execution.
- First-party operating / deployment modes considered: Python inline or queue worker, Java API with backend workers (documented deployment), default model-backed LangGraph adapter, optional external orchestrator adapters and manually triggered regression comparisons.
- Recursion level: One tenant organization containing multiple independent model-backed agent Runs as S1 operational units; Python agent graph nodes are subordinate run-internal work units and not all higher-recursion VSM organizations.
- Reviewed revision: `05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The documented production topology has a Java REST/SSE console API, Redis job/events transport, Python workers, PostgreSQL durable state and an adapter registry. A first-party LangGraph adapter constructs a graph from an Agent config, invokes the model, calls configured tools in a bounded ReAct loop, returns tool results to model messages, emits events/checkpoints and persists the run. External PydanticAI/AutoGen and other adapters are optional, not needed to establish this first-party S1. RunService and worker implement retry/resume/cancel and state transitions. Operator/admin APIs expose current runs, tenant quotas, agent manifests, version snapshots and regression replay/compare. [`backend/app/adapters/langgraph_adapter.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/adapters/langgraph_adapter.py#L325-L434); [`backend/app/adapters/langgraph_adapter.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/adapters/langgraph_adapter.py#L614-L812); [`backend/app/services/run_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/run_service.py#L123-L205); [`backend-java/src/main/java/io/agentflow/api/controller/RunsController.java`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend-java/src/main/java/io/agentflow/api/controller/RunsController.java#L24-L100); [`backend-java/src/main/java/io/agentflow/api/controller/AgentsController.java`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend-java/src/main/java/io/agentflow/api/controller/AgentsController.java#L25-L100); [`docs/architecture.md`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/docs/architecture.md).

## Operational model

An authorized user starts a run against a persisted agent definition. The worker consumes it, and the first-party LangGraph agent node makes model-dependent tool decisions. Tool observations are returned to the model, and the run's state/trace become visible through the persistent API. Human operators can cancel, retry from checkpoint or resume paused work and may revise agent definitions. Tenant/project quotas constrain new runs and account for subsequent usage. A regression API can replay baseline inputs against a pinned candidate agent version and compare result fields, but its role as a functionally independent, corrective S3* loop is not yet proved. Episode memory stores past runs for later S1 context and is not itself organizational future intelligence.

## S1 — Operations

- State: A
- Function: Perform open-ended user tasks with a model-selected action/tool loop in a shipped first-party adapter.
- Disturbance / variety regulated: Varying prompts, tool outputs, provider responses, recoverable tool errors and evolving task context.
- Decisive decision or feedback right: Select next tool calls or final answer in response to observed tool returns and model history.
- Decision owner: The first-party LangGraphAdapter's model-backed ReAct agent node. LangGraph provides execution machinery and the external provider inference; the task-specific node loop and tool feedback handling are first-party.
- Supporting / enforcement mechanisms: `LangGraphAdapter._agent_node`, `AdapterToolSurface`, model routing, worker `RunExecutor`, run state/checkpoints and durable events.
- Closure path: Model response includes tool calls; Hivemind executes them, records/serializes outcomes into `messages`, and iterates to another model request until a final answer; completed state and checkpoints are stored.
- Why this is / is not agent-owned: A scripted queue/adapter would not choose arbitrary tool actions; the model-backed agent decision at each round is necessary.
- Evidence: [`backend/app/adapters/langgraph_adapter.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/adapters/langgraph_adapter.py#L614-L680); [`backend/app/adapters/langgraph_adapter.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/adapters/langgraph_adapter.py#L681-L753); [`backend/app/adapters/langgraph_adapter.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/adapters/langgraph_adapter.py#L764-L812); [`backend/app/worker/executor.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/worker/executor.py#L68-L175).
- Basis: structural
- Confidence: High for the first-party configured LangGraph adapter.
- Caveats: No live provider invocation in this review; optional external adapters are dependencies and do not supply hidden metasystem rights.
- Boundary reachability: Documented default agent `adapter=langgraph` is submitted to the Java API and run by the packaged Python worker; the adapter explicitly builds a graph and invokes Hivemind's model/tool handlers.

## S2 — Coordination

- State: ?
- Function: Plausible constructor-owned regulation of resource conflicts among concurrent independent tenant/project Runs has not been shown to meet the full inter-S1 coordination standard.
- Disturbance / variety regulated: Multiple autonomous Runs can compete for shared tenant/project token, cost and worker capacity.
- Decisive decision or feedback right: Detect and attenuate a concrete competing commitment/resource clash among distinct S1 units and return the disposition to their subsequent operation.
- Decision owner: Unresolved. `QuotaService` and Redis queue enforce host-configured constraints, but no specific inter-run conflict arbitration path and returned behavioral feedback has been reconstructed.
- Supporting / enforcement mechanisms: Tenant/project/agent quota rows, row locking when checking usage, run accounting, Redis consumer leases/ack/DLQ, batch launches.
- Closure path: New run admission may be blocked when aggregate usage exceeds configured quota; consumed jobs get ack/retry. Whether this closes *inter-S1* interference rather than admission/budget enforcement alone remains uncertain.
- Why this is / is not agent-owned: An agent does not negotiate tenant budgets; deterministic queue and quotas alone are not automatic evidence of operational S2.
- Evidence: [`backend/app/services/quota_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/quota_service.py#L114-L161); [`backend/app/services/run_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/run_service.py#L123-L195); [`backend/app/worker/queue.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/worker/queue.py#L321-L365); [`backend/app/worker/queue.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/worker/queue.py#L454-L540).
- Basis: structural; unresolved function-specific interference witness
- Confidence: Low for positive S2.
- Caveats: A verified same-tenant concurrent-Run interference case with a feedback relation to affected Runs is needed before promoting to `C`; avoid re-labeling generic queue serialization as S2.

## S3 — Inside-and-now control

- State: P
- Function: Human operator current-control over the tenant's operating Run population and live task commitments.
- Disturbance / variety regulated: Failed, paused or unwanted concurrent executions, resource allocation and changing operator priorities across the deployed tenant's active workload.
- Decisive decision or feedback right: Inspect run portfolio, cancel an active/pending run, retry a failure at a checkpoint, or resume a paused run with new human input; change current run commitments.
- Decision owner: Legitimate operator in the deployed API's current-run management mode; neither a queue worker nor per-run model owns this whole-team current-control decision.
- Supporting / enforcement mechanisms: Tenant-scoped run list/status/stream, operator role, run-state transitions, Redis cancellation signal, worker cancel watcher and checkpoint-resume metadata.
- Closure path: Operator acts through documented API; RunService persists the decision and sends cancel/retry/resume to live worker or queue, changing subsequent work and status.
- Why this is / is not agent-owned: The model executes task actions but lacks the tenant-level authority to change the whole portfolio of runs; administrator/operator possesses the decisive control right.
- Evidence: [`backend-java/src/main/java/io/agentflow/api/controller/RunsController.java`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend-java/src/main/java/io/agentflow/api/controller/RunsController.java#L25-L105); [`backend/app/api/v1/runs.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/api/v1/runs.py#L92-L207); [`backend/app/services/run_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/run_service.py#L246-L415); [`backend/app/worker/executor.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/worker/executor.py#L267-L337).
- Basis: structural and explicit authorization
- Confidence: Moderate to high for supported operator path.
- Caveats: Current control is parent-owned `P`, not `A(P)`; run-status visibility alone is not credited without the stop/retry/resume decision/return.
- Boundary reachability: Production Java REST endpoints dispatch to RunService and Redis cancel/jobs; the shipped Python worker observes cancellation/replay and finalizes its states.
- Whole-system current view: Tenant-scoped Run list, status and cross-run quotas, with tenant/project/agent RBAC visibility.
- Current-control decision scope: Active run cancellation, failed-run retry, waiting-human continuation and intervention in current work, bounded to the legitimate tenant operator.

## S3* — Complementary audit

- State: ?
- Function: Possible complementary comparison of baseline and candidate agent operation by the first-party regression execution service remains unresolved as closed S3*.
- Disturbance / variety regulated: A modified agent definition could produce worse outputs or operational failure compared with historical runs even if ordinary status reports appear plausible.
- Decisive decision or feedback right: Independently compare observed candidate behavior against a relevant baseline and return a corrective finding to whole-system S3 control.
- Decision owner: Unresolved. `RegressionExecutionService` generates pinned candidate Runs and a comparison result, but the same runtime powers both sides; no independent complementary evidence authority or returned controller action has been established.
- Supporting / enforcement mechanisms: Operator-triggered baseline replay under pinned candidate agent version, `RunComparisonService.preview`, per-case pass/fail results, Run audit records and execution traces.
- Closure path: Result comparison is obtainable through the regression API; no established first-party automatic or legitimate parent decision that consumes these findings and changes subsequent current operating commitments was traced.
- Why this is / is not agent-owned: Replay and status/output comparisons offer useful inspection but do not alone prove an independent auditor or S3* decision/feedback closure.
- Evidence: [`backend-java/src/main/java/io/agentflow/api/service/RegressionExecutionService.java`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend-java/src/main/java/io/agentflow/api/service/RegressionExecutionService.java#L56-L98); [`backend-java/src/main/java/io/agentflow/api/service/RegressionExecutionService.java`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend-java/src/main/java/io/agentflow/api/service/RegressionExecutionService.java#L104-L133); [`backend-java/src/main/java/io/agentflow/api/service/RunComparisonService.java`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend-java/src/main/java/io/agentflow/api/service/RunComparisonService.java#L20-L82); [`backend/app/services/run_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/run_service.py#L417-L464).
- Basis: structural, unresolved auditor/feedback ownership
- Confidence: Low for positive S3*.
- Caveats: A future source-verified audit-to-corrective-action integration could change classification; do not claim this regression comparison is an independent S3* reviewer already.
- Claim being audited: Candidate agent/version preserves expected operational outcomes against a baseline.
- Ordinary reporting path: Agent Run status, output, messages and tool events.
- Complementary access path: Explicit pinned previous version/run inputs and replay comparison service, with shared runtime infrastructure.
- Independence boundary: Regression comparison executes separately, but independence of evidence and judgment from ordinary runtime is unproven.
- Who acts on findings: The operator may inspect the returned result, but a concrete first-party correction intake and authority loop have not been verified.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party future-facing environment sensing, option evaluation and adoption of new organizational capabilities was established.
- Disturbance / variety regulated: Future tool/model ecosystem shifts and changes in task distribution could demand strategic capability adaptation, but these are not the runtime's shown function.
- Decisive decision or feedback right: Judge prospective options from environmental evidence and adopt an organizational change that returns to current S3.
- Decision owner: None established. Agent-specific episode recall reuses past task evidence; administrators may manually edit definitions, not a documented S4 intelligence loop.
- Supporting / enforcement mechanisms: EpisodeService ingestion/recall, memory-window trimming, retry/resume history, comparison of past/candidate runs, version snapshot/restore.
- Closure path: Past episodes can be recalled and injected as contextual support to S1; no decision and return path was shown that evaluates future alternatives and changes the system's organization-level capability.
- Why this is / is not agent-owned: Past experience reused by an executing model is not automatically VSM S4, and an admin restoring a version need not be making a prospective environmental adaptation decision.
- Evidence: [`backend/app/services/episode_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/episode_service.py#L78-L128); [`backend/app/services/episode_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/episode_service.py#L234-L275); [`backend/app/services/agent_versions.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/agent_versions.py#L42-L84); [`backend-java/src/main/java/io/agentflow/api/service/RegressionExecutionService.java`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend-java/src/main/java/io/agentflow/api/service/RegressionExecutionService.java#L56-L98).
- Basis: structural
- Confidence: Moderate within the shipped multi-API/worker boundary.
- Caveats: New external-intelligence plugins may be authored by consumers; no prospective decision owner is credited from an unspecified plugin.

### Absence scope

- Surfaces inspected: Episode ingestion/recall, memory window, model routing, agent versioning/rollback, regression baseline/candidate comparison, scheduling, adapter extension and operator state.
- Plausible first-party paths checked: Retrospective episode memory, model routing fallback under provider errors, regression replay of prior inputs, human version restore and configuration changes.
- Why no material first-party path remains: Each supported path is task memory, current contingency handling or explicit operator configuration; none independently owns an outside-and-then sensing → prospective choice → adopted capability returned to S3 loop at the claimed tenant recursion.

## S5 — Policy and identity

- State: P
- Function: Parent-admin governance of the tenant's agent identity, adapter/config definitions, authorized roles and legitimate organization membership.
- Disturbance / variety regulated: Which named agents, adapters and definition versions are legitimately in operation, and which tenants/roles may create and revise them.
- Decisive decision or feedback right: Authorized administrator creates or changes an Agent definition, including its model/adapter/tools configuration, and may restore a previous version; current Run creation consumes that approved definition.
- Decision owner: Legitimate tenant/project ADMIN role exposed in first-party API and enforced by auth middleware; the agent model lacks authority to rewrite its own ultimate identity and organization definitions in this mode.
- Supporting / enforcement mechanisms: Admin role authorization, tenant/project scope, version snapshots, agent registry, RunService agent resolution, persistent version metadata and worker adapter selection.
- Closure path: Admin-defined agent is committed to persistence; authorized Run requests resolve it and the worker executes the selected adapter/config. Restore/version changes affect subsequently launched work.
- Why this is / is not agent-owned: A runtime tool call or checkpoint approval is not the ultimate identity decision; the administrator setting which agent definition is legitimate does own that higher-order right.
- Evidence: [`backend/app/api/v1/agents.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/api/v1/agents.py#L41-L77); [`backend/app/api/v1/agents.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/api/v1/agents.py#L114-L165); [`backend/app/api/v1/agents.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/api/v1/agents.py#L221-L250); [`backend/app/services/run_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/run_service.py#L123-L167); [`backend-java/src/main/java/io/agentflow/api/controller/AgentsController.java`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend-java/src/main/java/io/agentflow/api/controller/AgentsController.java#L25-L100).
- Basis: structural / explicit RBAC
- Confidence: Moderate to high for supported admin-created agent definitions.
- Caveats: This is bounded to declared tenant/project identity and authoritative agent configuration, not a claim that every human tool permission step equals S5.
- Boundary reachability: The supported Java API and equivalent Python API persist versions and agent definitions; the RunService loads the definitions and the first-party worker dispatches agent adapters accordingly.
- Identity / ultimate-policy issue: Which named agents with which adapters and instructions constitute the legitimate agent organization and who may change that definition.
- Ultimate authority in each claimed mode: Authenticated tenant/project administrator; no autonomous first-party agent-governed identity mode established.
- Return-to-operation path: Authorized create/update/restore → durable agent/version state → subsequent Run creation resolves the definition → execution using the chosen model/adapter/config.

## Distributed OSS parent arrangement

This is a deployed tenant's legitimate operator/admin, not the GitHub contributor or maintainer institution. No pull-request review or CI status is imported as proof of the running organization's S3* or S5. External orchestrator frameworks and models remain dependencies.

## Self-hosted and non-human modes

A self-hosted Java/Python/Redis/Postgres mode is explicitly documented. The tenant operator/admin can exercise S3/S5 parent decisions through shipped APIs. Autonomy of this deployed *agent* resides in the first-party LangGraph ReAct loop (S1), not the operator interfaces. A separately built fully agent-owned current-control or identity governor is not automatically attributed to Hivemind.

## Recursion

Tenant organization contains multiple independently dispatched model-backed agent Runs. A LangGraph node and an optional external orchestration plugin may contain other subagents, but their internal VSM organization is not imported into the tenant's top-level functions without its own first-party evidence.

## Variety and escalation

Failed runs may retry from a checkpoint; waiting-human runs can be resumed with operator input; quota exhaustion can reject a new Run. Regression testing offers another observation about versions but not a proven independent audit path. These status/exception flows are not automatically new S3, S3* or S5 functions. [`backend/app/services/run_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/run_service.py#L246-L415); [`backend/app/services/quota_service.py`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend/app/services/quota_service.py#L114-L161); [`backend-java/src/main/java/io/agentflow/api/service/RegressionExecutionService.java`](https://github.com/Emiyaaaaa/HiveMind/blob/05f7d3e79cd24f75b432bcddfe5aa0877eb5a64b/backend-java/src/main/java/io/agentflow/api/service/RegressionExecutionService.java#L104-L133).

## Evidence gaps

- For S2, verify whether scoped quotas or worker lease coordination actually resolve an inter-S1 disturbance among independent concurrent agents and return corrective feedback, rather than merely gating task admission and serializing queue work.
- For S3*, trace regression comparisons into an independent judgment source plus actionable corrective intervention in current whole-tenant regulation; different run IDs and deterministic field comparisons alone do not prove the function.
- No live model provider, database or hosted app deployment was executed for this assessment. Claims follow first-party source and shipped operational entry points at the frozen revision.
- Separate external AutoGen/PydanticAI plugins can add advanced capabilities but were excluded as borrowed third-party function owners; the native LangGraph agent loop is sufficient for S1.
