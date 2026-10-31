---
harness_id: openjiuwen-agent-runtime
project_name: openJiuwen Agent Runtime
repository: https://github.com/openJiuwen-ai/agent-runtime
review_ref: 34ed6e86b99fab9b3f07d9f063efc1692ab365d2
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# openJiuwen Agent Runtime

## Review boundary

- System in focus: an installed openJiuwen Agent Runtime deployment including its first-party low-code/IR Agent applications, service wrapper, management service and session pool, not just the deployment REST API in isolation.
- Purpose and identity: publish configured AI agents, instantiate them as callable services, execute model/tool turns, manage service/session lifecycle and isolate concurrent tenant work.
- Relevant environment: Studio-exported agent IR/configuration, end-user queries, model/tool results, tenant/session traffic, resource demand, service crashes, provider/network failures and deployment mode.
- Standard-distribution boundary: first-party `applications/lowcode_agent`, `applications/ir_execution_service`, `service/AgentApp`, `management` session router/instance pool and `server` APIs; process is the default mode, with Docker/Kubernetes strategies also examined.
- Credited operating / distribution surfaces: shipped low-code agent runner and ReAct builder/invoke API, AgentApp query/stream interface, DeploymentManager and ServiceManager dual-queue/affinity/concurrency/scale execution paths; these are source-distributed and documented deployment modes.
- Adjacent first-party surfaces excluded from ownership: example-only simple agents/tests, docs and CI, separate Studio editor/product, external `openjiuwen.core`/`openjiuwen_studio` agent frameworks and cloud model providers. Their discretionary inner loops are not donated as independent first-party modules; only the runtime's configured instantiation/return path is credited.
- Modes considered: exported low-code LLM/Workflow Agent, IR ReAct execution service, service/session API, subprocess, Docker and Kubernetes deployers, multi-tenant and A2A parallel bridge; no live model/deploy E2E executed.
- Recursion level: one operator-configured runtime installation running multiple agent services/session cells; upstream Studio authoring is a parent input and external A2A/VersatileAdapter services are adjacent.
- Reviewed revision: `openJiuwen-ai/agent-runtime@34ed6e86b99fab9b3f07d9f063efc1692ab365d2`, GitHub repository ID 1283876614, frozen #2501 / controller #2502 row 3.
- Observation date: 2026-10-31; active Profile 0.2.4 / released Methodology 0.3.7. Source/contract inspection only.

## Repository architecture

The pinned [README](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/README.md) explicitly separates deployment `management/`, web `service/`, API `server/`, and bundled executable `applications/`. Crucially, the shipped [low-code runner](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/lowcode_agent/openjiuwen_runtime/examples/lowcode_agent/lowcode_agent_runner.py) loads exported agent IR, compiles it with packaged Studio contracts, instantiates `LLMAgent`/`WorkflowAgent`, registers workflows/tools and invokes a streaming `Runner`; the [IR ReAct builder](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/ir_execution_service/ir_execution_service/react_agent_builder.py) and [invoke API](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/ir_execution_service/ir_execution_service/invoke_api.py) similarly construct and run configurable ReAct agents. The [session design](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/DESIGN.md) and [ServiceManager](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/service_manager.py) implement two-level concurrency, service affinity, system-priority queueing and pool lifecycle. The separate [A2A executor](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/a2a_service/orchestrator/executor.py) supports parallel child calls/cancellation but imports an `agents.EDPAgent` actor absent from this pinned source tree; this adjacent integration does not prove a shipped metasystem brain.

## Operational model

Operators/Studio select the agent IR, tools, workflow and deployment resources. Within a deployed runnable agent, the instantiated `openjiuwen.core` model/tool actor makes content-bearing decisions; this repository owns the packaged configuration-to-instantiation-to-service-return path, not the imported agent algorithm in isolation. Management routes and throttles traffic deterministically. Operational capacity decisions, health controls and API permissions are first-party infrastructure support unless they establish a function-specific autonomous right. The product README states it does not embed a model; model access is external and configured.

## S1 — Operations

- State: A
- Function: satisfy heterogeneous user queries and run exported ReAct/LLM/Workflow Agent tasks through the source-distributed application services.
- Disturbance / variety regulated: prompt/task variation, tool/provider responses, workflow branches, errors and per-session context.
- Decisive decision or feedback right: the instantiated model-driven agent selects substantive reasoning and tool/workflow actions; first-party application adapters launch and return that sequence.
- Decision owner: the configured application-level Agent instance under the bundled low-code/IR service path, with its inner `openjiuwen.core` implementation as a declared dependency and user-authored configuration as parent constraint.
- Supporting / enforcement mechanisms: `AgentApp`, REST/stream response conversion, Runner startup, tenant sessions, process/container management, model SDK/Studio compiler, DB and network.
- Closure path: Studio-exported IR and incoming `/query` → AgentCompiler/ReAct builder → `Runner.run_agent` or streaming agent execution → tool/model feedback → agent result returned over service API.
- Boundary reachability: README presents `applications/` as concrete deployed agent implementations, and both [low-code runner](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/lowcode_agent/openjiuwen_runtime/examples/lowcode_agent/lowcode_agent_runner.py) and [invoke API](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/ir_execution_service/ir_execution_service/invoke_api.py) call actual agent runners, beyond toy samples.
- Why this is / is not agent-owned: removing the deployed model-driven actor leaves agent hosting and HTTP routing, but no autonomous semantic resolution of queries; fixed infrastructure does not acquire S1 credit.
- Evidence: [README](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/README.md); [lowcode_agent_runner.py](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/lowcode_agent/openjiuwen_runtime/examples/lowcode_agent/lowcode_agent_runner.py); [react_agent_builder.py](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/ir_execution_service/ir_execution_service/react_agent_builder.py); [invoke_api.py](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/ir_execution_service/ir_execution_service/invoke_api.py); [AgentApp](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/service/openjiuwen_runtime/service/app/agent_app.py).
- Basis: structural
- Confidence: medium
- Caveats: native source composes imported same-ecosystem agent implementation; no direct model/provider trace or full dependency installation was performed.

## S2 — Coordination

- State: C
- Function: attenuate capacity and session-context interference among concurrently served agent execution cells sharing a multi-instance service pool.
- Distinct S1 units: independently active agent-service instances and their session-scoped execution cells that contend for pooled service slots/channels and tenant session continuity.
- Inter-S1 disturbance: shared service capacity exhaustion, cross-session answer interleaving, reassignment to a wrong stateful instance, and processing system reclaim while a cell still owns an active session.
- Attenuating coordination relation: `ServiceManager` chooses an available existing instance with session affinity, creates a fresh one only within the pool cap, otherwise returns an explicit capacity error; service-level and session-level semaphores constrain competing requests, and `request_id` demultiplexes streaming returns.
- Feedback into subsequent S1 behaviour: accepted requests wait on service/session slots and remain sticky to the correct agent context; saturated requests fail explicitly instead of corrupting a peer's turn; completion callbacks release slots and may permit later work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the combination specifically prevents observed structural interference of stateful concurrent agent invocations against finite shared execution slots; ordinary HTTP routing alone would not preserve session/slot ownership.
- Disturbance / variety regulated: colliding stateful traffic and worker-pool capacity contention.
- Decisive decision or feedback right: resolve instance affinity/admission and release slots so later agent cells can continue safely; higher-level cross-agent priority judgments are not autonomous.
- Decision owner: deterministic first-party session capacity/affinity constructor, with configuration authored by operator; an autonomous multi-agent coordinator still has to be composed for broader discretion.
- Supporting / enforcement mechanisms: dual system/user queues, bounded semaphores, `ServiceRouter`, `SessionHandler`, `WSServiceMessageChannel`, timeouts and idle TTL.
- Closure path: simultaneous tenant/agent requests → affinity/capacity check → accepted/sticky dispatch or explicit overload response → request completion callback/slot release → subsequent cell admission.
- Boundary reachability: documented [Session design](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/DESIGN.md) corresponds to shipped [ServiceManager](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/service_manager.py), [SessionHandler](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/session_handler.py), [router](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/router.py) and [tests](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/tests/unit_tests/management_session/test_session_concurrency_interleave.py).
- Why this is / is not agent-owned: constructor enforces a concrete S2-specific inter-cell interference rule; it does not independently decide organizational trade-offs, so `C`, not `A`.
- Evidence: [session DESIGN](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/DESIGN.md); [service_manager.py](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/service_manager.py); [service_handler.py](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/service_handler.py).
- Basis: structural
- Confidence: medium-low
- Caveats: this is narrow S2 capacity/session interference at the agent pool, not proof of model-selected conflict arbitration between business goals or collaboration among all deployed agents.

## S3 — Inside-and-now control

- State: —
- Function: no whole-runtime discretionary current-control owner and returned intervention loop established beyond configured deployment and resource management.
- Whole-system current view: lifecycle/health and pool metrics exist; they show infrastructure state, not a model-owned consolidated mission/commitment picture across independent agents.
- Current-control decision scope: deterministic admission, scaling, idle reclaim and deployment actions, not semantic reprioritization of the installation's current operational purposes.
- Disturbance / variety regulated: service exhaustion, health and failed deployments are handled mechanically within preselected limits.
- Decisive decision or feedback right: no qualifying discretionary whole-system resource/commitment priority right was evidenced in the first-party runtime actor.
- Decision owner: deployment operator chooses policy/config; ServiceManager and DeploymentManager deterministically enforce it.
- Supporting / enforcement mechanisms: health endpoints, instance pool, autoscale loop, session TTL, management REST and DB records.
- Closure path: health/load → fixed policy scaling/routing returns to service availability; this is not an independent organization-level S3 decision/feedback closure.
- Why this is / is not agent-owned: more pod/instance controllers and telemetry do not establish discretionary current mission management at the declared recursion.
- Evidence: [README](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/README.md); [service_manager.py](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/service_manager.py); [manager.py](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/manager.py).
- Basis: structural
- Confidence: medium-low
- Caveats: a custom external coordinator might supply S3 but is not first-party shipped ownership at this runtime boundary.

### Absence scope — S3

- Surfaces inspected: deployment/server management APIs, instance health/scale/session routes, low-code and IR agent application adapters, A2A parallel executor and repository docs.
- Plausible first-party paths checked: autoscale current-control, deployment manager, exported agent workflows, A2A orchestration and Studio operations.
- Why no material first-party path remains: these perform deterministic lifecycle control or individual agent tasks. The A2A `agent_stream` decision owner is an absent external/imported actor; an installation-wide discretionary supervisor with returned priorities/interventions is not established by this source.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary independent challenger to an agent's ordinary outcome with consequential corrective return was found.
- Claim being audited: a deployed agent's answer/workflow report should be correct and justified by independent evidence.
- Ordinary reporting path: `AgentApp` and IR/A2A execution return model/workflow answer and status to caller; management records lifecycle.
- Complementary access path: tests and health checks are development/infrastructure surfaces; no supported separate runtime verifier with independent evidence access is wired to a deployed agent's answer.
- Independence boundary: no distinct reviewer authority/actor and non-self-report evidence channel required for ordinary agent decisions.
- Who acts on findings: failures/status may return to caller; there is no independent critique → corrective agent path.
- Disturbance / variety regulated: hallucinated/incorrect outputs and unjustified task claims are not governed by a packaged complementary audit organ.
- Decisive decision or feedback right: none shown beyond ordinary runtime errors and caller handling.
- Decision owner: no first-party audit decision owner established.
- Supporting / enforcement mechanisms: health checks, schema conversion, terminal event handling, tests, logs and session history.
- Closure path: current execution status → HTTP/stream output; no independent challenge and remediation cycle.
- Boundary reachability: no reviewer path in documented standard application/service/management deployment modes.
- Why this is / is not agent-owned: error/status validation and CI tests do not provide a separate evidence-owning S3* reviewer.
- Evidence: [README](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/README.md); [AgentApp](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/service/openjiuwen_runtime/service/app/agent_app.py); [A2A executor](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/a2a_service/orchestrator/executor.py).
- Basis: structural
- Confidence: medium-low
- Caveats: bounded standard-distribution absence; user-added auditors in compiled workflows are outside the evidenced first-party return path.

### Absence scope — S3*

- Surfaces inspected: agent service responses, IR/lowcode execution, A2A aggregator and status/cancel handling, session and deployment management, documented application entry points.
- Plausible first-party paths checked: separate reviewer agent, independent evaluation/traces, QA validation, health probes, A2A child tests and runtime error schemas.
- Why no material first-party path remains: these are ordinary task logic, health/error checks or offline tests; none installs an independent operational reviewer that can challenge and return an authoritative correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: no independent future-facing intelligence/adaptation owner identified for the runtime's evolving operating capability.
- Disturbance / variety regulated: future model/provider changes, demand trends and shifting workflow requirements were considered.
- Decisive decision or feedback right: no model/human parent loop turns prospective environmental intelligence into selected strategic changes returned to runtime capability.
- Decision owner: operator/Studio authors agent IR, image and deployment settings; autoscaler follows fixed current-demand policy.
- Supporting / enforcement mechanisms: workflow IR config, context/memory adapter, deployment strategies, service scaling and versioned publishing.
- Closure path: exported changes can alter later behavior, but repository evidence does not tie them to a first-party prospective sense → adaptation-choice → future-effectiveness feedback loop.
- Why this is / is not agent-owned: agent memory, prompt reuse and immediate autoscaling are not, alone, a system-level S4.
- Evidence: [README](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/README.md); [react_agent_builder.py](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/applications/ir_execution_service/ir_execution_service/react_agent_builder.py); [session DESIGN](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/session/DESIGN.md).
- Basis: structural
- Confidence: medium-low
- Caveats: other openJiuwen products may implement adaptation, but their modes are not donated to this pinned Runtime.

### Absence scope — S4

- Surfaces inspected: exported agent builder, workflows and memory config, deployment version management, session autoscale/reclaim, A2A delegation.
- Plausible first-party paths checked: memory learning, Studio republishing, future-provider selection, rolling deployment, ongoing adaptive resource planning and A2A agent strategy.
- Why no material first-party path remains: inspected paths are authoring inputs, ordinary session memory or current-demand reactions, without a distinct prospective organizational adaptation decision and later effectiveness return.

## S5 — Policy and identity

- State: —
- Function: no distinct ultimate-identity/policy dispute and authoritative decision-return loop within the installed runtime.
- Disturbance / variety regulated: tenant isolation, service authorization, deployment modes and user/agent roles are fixed constraints, not open identity choices.
- Decisive decision or feedback right: no first-party agent or parent S5 authority to resolve what this running organization ultimately is or may become.
- Decision owner: operator/Studio chooses tenant, agent definition, tools and permissions; management middleware enforces those decisions.
- Supporting / enforcement mechanisms: tenant middleware, configuration, auth, service access, role metadata, sandbox and deploy strategies.
- Closure path: config/policy alters later allowed execution; no unresolved ultimate identity issue is adjudicated and returned through a distinct governance organ.
- Why this is / is not agent-owned: agent labels/roles, tenant management and contributor governance are not S5.
- Evidence: [README](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/README.md); [tenant middleware](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/server/openjiuwen_runtime/server/middleware/tenant.py); [manager.py](https://github.com/openJiuwen-ai/agent-runtime/blob/34ed6e86b99fab9b3f07d9f063efc1692ab365d2/management/openjiuwen_runtime/management/manager.py).
- Basis: structural
- Confidence: medium-low
- Caveats: bounded absence for an installation, not a claim about Huawei/openJiuwen institutional policy.

### Absence scope — S5

- Surfaces inspected: runtime API/middleware, deployment config, tenant/session ownership, lowcode agent roles, README and contributor/organizational surfaces.
- Plausible first-party paths checked: tenant policy updates, Studio agent definition, access control, deploy approval, provider compliance notice and upstream governance.
- Why no material first-party path remains: these paths are fixed config/support or external institutions, not a first-party adjudication of ultimate purpose/identity with return to operation.

## Distributed OSS parent arrangement

The runtime's operator and upstream Huawei/openJiuwen contributors are not conflated. Studio can author agent IR and a user can deploy it; this is ordinary S1 configuration, not an evidenced S4/S5 parent function. Upstream project decisions do not become installed-runtime identity policy.

## Self-hosted and non-human modes

Self-hosted subprocess, Docker and Kubernetes variants share a configured service/agent boundary; the model/tool actor is supplied through declared dependencies and credentials, not native embedded model weights. Scaling/tenant control is deterministic and does not grant organizational discretion.

## Recursion

Each deployed agent instance is an operational S1 cell. The session pool attenuates shared execution contention (narrow S2=C), but neither hierarchy names nor A2A subtask counts alone demonstrate autonomous S3 through S5.

## Variety and escalation

Queue priority, two-level bounded semaphores, affinity, timeout, recovery, deploy health and explicit capacity errors regulate runtime traffic. These are enforcement and delivery mechanics, not agent-owned choices over strategic or policy direction. Failed agent work returns to caller; no packaged complementary auditor is evidenced.

## Evidence gaps

No model, Studio, Docker or Kubernetes end-to-end run; source and test definitions inspected structurally. Imported `openjiuwen.core` and Studio packages are required for S1; their internal autonomy is not separately assessed here. The A2A service references missing `agents.EDPAgent` source, so it is not promoted into autonomous whole-runtime S3 or S3* just because it exposes parallel coordination events. Supported first-party runtime/session interference is narrower than arbitrary multi-agent mission management.
