---
harness_id: actweave
project_name: ActWeave
repository: https://github.com/chenow9/act-weave
review_ref: ea0451acc090977c14c1c8d9d0b4d2bee5df4238
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ActWeave

## Review boundary

- System in focus: one public OSS ActWeave installation at pinned revision `ea0451acc090977c14c1c8d9d0b4d2bee5df4238`, including its first-party control plane, AgentRun/Agentic runtime, Tool and Workflow runtime surfaces, in-workspace Agent delegation, AAP runtime API, A2A gateway and trace/audit services.
- Purpose and identity: configure, publish and run hosted Agents, Workflows and business Tools behind first-party runtime-access boundaries, with durable run state and optional collaboration with other Agents.
- Relevant environment: external model-provider APIs; enterprise HTTP services reached through Provider/Connection; AAP business applications; external A2A agents; console operators; infrastructure such as PostgreSQL, Redis and MinIO.
- Standard-distribution boundary: ActWeave's own Go backend, runtime/control services and shipped configuration/governance machinery are inside. Model endpoints, enterprise APIs and remote A2A agents are dependencies and do not donate autonomy.
- Credited operating / distribution surfaces: `backend/internal/agentrun/runtime.go`; `backend/internal/einoruntime/agentic_engine.go`; `backend/internal/einoruntime/agentic_agent_builder.go`; `backend/internal/agentdelegation/`; `backend/internal/agentaudit/`; documented Workflow/Tool/AAP/A2A runtime paths.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/docs, operator choices made outside the runtime, configuration objects without a closed organizational decision loop, and external Agents/services whose internal decision rights are not owned by ActWeave.
- First-party operating / deployment modes considered: Agentic model/tool execution; async AgentRun start/cancel/continue-after-confirmation; in-workspace INLINE/TASK delegation; root-shared delegation budgets; deterministic Workflow graph execution; Tool publishing/testing; AAP conversations/runs/interactions; configured A2A inbound/outbound paths; trace/audit query UI.
- Recursion level: one ActWeave installation. Hosted Agents are operational units. Delegated child Agents and Workflow nodes can form lower-level task organizations, but plurality/topology does not itself establish installation-level metasystem functions.
- Reviewed revision: `ea0451acc090977c14c1c8d9d0b4d2bee5df4238`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

ActWeave explicitly separates a management/control plane from a runtime plane while assembling both in the same backend. The management plane owns Workspace/RBAC, Agent/model/capability configuration, Tool and Workflow lifecycle, AAP clients/grants and audit access. The runtime plane is reached through AAP or configured A2A exposure and executes frozen Agent/model/capability state, Workflows and Tools while persisting Run/step/event/audit facts.

The positive S1 claim comes from the owned Agentic runtime rather than from those surrounding control-plane objects. `AgenticEngine.Run` validates the conversation, allocates a stable checkpoint and drives a typed agent runner; `Resume` continues an interrupted run from explicit HITL targets. `BuildAgenticAgent` wires a model, executable Tool catalog, bounded Tool disclosure, run-local invocation budget, sequential Tool execution and an iteration cap into the first-party agent. The model therefore makes contextual next-action choices while ActWeave owns the loop that exposes capabilities, executes selected Tools, feeds results back and terminates or interrupts the run.

Agent-to-Agent delegation is substantial but remains task decomposition rather than automatically S2. A frozen directed binding can invoke another Agent INLINE or create an independent TASK child run. A root-shared `Budget` atomically limits depth, total delegations and per-binding dispatches across the call tree, while durable delegation rows record lifecycle and attempts. Those mechanisms constrain recursion/runaway dispatch and preserve evidence; they do not detect a concrete conflict, oscillation or incompatible commitment between distinct S1 units and feed a resolution back into their operation.

The repository's audit surface is likewise functionally narrower than S3*. `agentaudit.Service` is explicitly a workspace-scoped trace loader for the platform-admin audit UI. It lists/aggregates Run facts, steps, statuses, success/failure rates and trace detail. Delegation itself also requires fail-closed audit prewrite/finalization. This is strong provenance/observability, but no materially independent challenge actor, complementary evidence judgment and corrective return loop is established by the standard path.

Workflow drafts, compilation, trial runs and publishing; Tool tests/publishing; Agent prompt/model/capability configuration; RBAC; AAP grants; and security/publish controls provide important governance mechanisms. The reviewed standard distribution does not, however, close S3 current-management judgment over the installation, an outside/future S4 adaptation loop, or an S5 identity/ultimate-policy loop. Those controls are configured or invoked by operators and enforce local/runtime constraints rather than supplying the missing organizational decision rights themselves.

Primary evidence:

- [`backend/internal/agentrun/runtime.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentrun/runtime.go) — production AgentRun facade for asynchronous execution, cancellation and durable continue-after-confirmation scheduling.
- [`backend/internal/einoruntime/agentic_engine.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/einoruntime/agentic_engine.go) — first-party typed Agentic run/resume boundary, checkpoints, streaming events, HITL interrupts and fail-closed terminal handling.
- [`backend/internal/einoruntime/agentic_agent_builder.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/einoruntime/agentic_agent_builder.go) — model/Tool assembly, Tool disclosure, invocation/iteration budgets and sequential Tool execution for the production Agentic path.
- [`backend/internal/agentdelegation/agent_tool.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentdelegation/agent_tool.go) — audited Agent-to-Agent invocation, child TASK runs, frozen binding identity and root-call-tree context.
- [`backend/internal/agentdelegation/models.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentdelegation/models.go) — explicit bindings, immutable graph snapshots and root-shared depth/total/per-binding delegation budgets.
- [`backend/internal/agentaudit/service.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentaudit/service.go) — admin trace query/aggregation over runs, steps, statuses and statistics.
- [`docs/architecture.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/architecture.md) — explicit management/runtime-plane boundary and shipped control/runtime responsibilities.
- [`docs/concepts.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/concepts.md) — first-party Agent dynamic-choice semantics, deterministic Workflow semantics, Tool test/publish lifecycle and AAP/A2A boundary.

## Operational model

A hosted Agent run is created through the runtime plane and executed asynchronously. The Agentic builder freezes the executable capability surface and constructs the model-driven Agent. The engine then owns the run/checkpoint stream: the model sees current context and available capabilities, can select a Tool or delegated Agent action, and first-party runtime machinery executes that action and returns the observation into the continuing run. Human-confirmation interrupts can pause the run and resume it later from persisted checkpoint/targets; cancellation terminates an active job.

Delegation can create nested operational units with immutable binding snapshots and shared limits. The budget and audit layers make nested execution bounded, reproducible and inspectable. Workflow execution supplies a separate deterministic graph path. These mechanisms are valuable operating controls, but VSM metasystem states are credited only where a distinct organizational function and decision/feedback right closes at the declared installation boundary.

## S1 — Operations

- State: A
- Function: perform a goal-directed hosted Agent run through repeated contextual model decisions and first-party Tool/delegation execution until completion, interruption, cancellation or bounded failure.
- Disturbance / variety regulated: user/application objective, model outputs, available capability catalog, Tool/delegation results, Tool errors, confirmation state, run continuation state and bounded iteration/invocation pressure.
- Decisive decision or feedback right: choose the next substantive answer or callable action from current context and use returned observations to choose subsequent behavior.
- Decision owner: the model-driven Agent assembled and driven by ActWeave's first-party Agentic runtime.
- Supporting / enforcement mechanisms: typed runner/checkpoint store, Tool catalog validation/disclosure, Tool invocation and iteration budgets, sequential execution, async AgentRun lifecycle, cancel/continue hooks, durable run facts and trace projection.
- Closure path: runtime request/context → Agentic model turn → model-selected Tool/delegation or answer → first-party action execution → result/event returned into Agentic context → next model turn or terminal/interrupted state.
- Boundary reachability: `AgenticEngine` and `BuildAgenticAgent` are documented production-target paths; `agentrun.Runtime` is the production facade used by runtime callers.
- Why this is / is not agent-owned: deterministic machinery constrains and transports the loop, while semantic next-action choice is made by the model-driven Agent over first-party-maintained context/capabilities. No external Agent or business service is used to establish the decision right.
- Evidence: [`agentic_engine.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/einoruntime/agentic_engine.go); [`agentic_agent_builder.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/einoruntime/agentic_agent_builder.go); [`runtime.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentrun/runtime.go); [`concepts.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/concepts.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model/provider endpoints remain environmental dependencies; their internal capabilities are not credited separately.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes disturbance-specific coordination among distinct ActWeave S1 units.
- Disturbance / variety regulated: the runtime constrains delegation depth/count/per-binding use and moves tasks/results through directed Agent bindings, but this regulates call-tree growth and execution safety rather than a demonstrated inter-S1 conflict or oscillation.
- Decisive decision or feedback right: no S2-specific conflict detection/resolution right is established.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: INLINE/TASK delegation bindings, immutable graph snapshots, root-shared delegation budget, sequential Tool execution, Workflow graph dependencies and A2A task exchange.
- Closure path: parent Agent selects a delegation → first-party runtime dispatches the configured child → child result returns to the parent; budget checks may reject a dispatch when static limits are exceeded. No cross-S1 disturbance is sensed, resolved and returned as a coordination decision.
- Boundary reachability: delegation and budget paths are shipped and reachable; the negative classification is functional, not due to absence of multi-agent machinery.
- Why this is / is not agent-owned: delegation, routing and static capacity limits do not by themselves damp oscillation, reconcile incompatible assumptions or resolve contention between viable units.
- Evidence: [`agent_tool.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentdelegation/agent_tool.go); [`models.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentdelegation/models.go); [`concepts.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/concepts.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream deployment could use these constructor mechanisms to instantiate real S2; that organization requires its own evidence.
- Distinct S1 units checked: caller and target hosted Agents connected by an in-workspace binding, including TASK child runs.
- Inter-S1 disturbance checked: runaway recursion/count is a call-tree safety condition, not evidence of mutual operational interference between the Agents.
- Why generic communication/routing/delegation is insufficient: the parent already decides to delegate and the child returns task output; the runtime does not independently coordinate a conflict between their operations.

### Absence scope

- Surfaces inspected: Agent delegation, graph snapshots, root budgets, Workflow composition, A2A task exchange and Tool execution ordering.
- Plausible first-party paths checked: delegation as S2; shared budget as S2; Workflow dependencies as S2; A2A collaboration as S2.
- Why no material first-party path remains: all identified paths perform composition, transport or bounded execution without the required disturbance-specific coordination witness.

## S3 — Inside-and-now control

- State: —
- Function: no material installation-level present-management function is established.
- Disturbance / variety regulated: AgentRun cancellation/continuation, static Tool/delegation budgets, published configuration and deterministic Workflow state constrain individual executions but do not create a whole-installation management judgment over competing operations.
- Decisive decision or feedback right: no first-party actor is shown receiving a current whole-system view and deciding priorities, resource allocation, commitments, accountability or intervention among operating Agents.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: management-plane configuration, published Agent/Tool/Workflow versions, run cancellation, continuation leases, runtime budgets, Workspace/RBAC and deterministic Workflow execution.
- Closure path: operators/configuration establish permitted resources and callers can cancel/continue particular runs; runtime enforces those choices locally. No installation-wide current-management assessment → intervention → operational feedback loop closes autonomously.
- Boundary reachability: these controls are shipped first-party surfaces; they are classified by function rather than by naming.
- Why this is / is not agent-owned: current-control decisions remain local execution rules or operator/API decisions, not a distinct S3 decision owner within the harness.
- Evidence: [`runtime.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentrun/runtime.go); [`architecture.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/architecture.md); [`concepts.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/concepts.md).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: an operator can exercise management through the control plane, but generic human administration is not automatically parent-governed S3 without a reconstructed VSM control closure.

### Absence scope

- Surfaces inspected: management/runtime split, run lifecycle, Workflow/runtime controls, delegation budgets, RBAC and publishing controls.
- Plausible first-party paths checked: control plane as S3; run cancel/continue as S3; delegation budget as S3; Workflow runtime as S3.
- Why no material first-party path remains: each path governs one resource/run/topology or enforces configured limits rather than managing the present organization as a whole.

## S3* — Audit

- State: —
- Function: no material first-party independent complementary audit/challenge function with corrective closure is established.
- Disturbance / variety regulated: ActWeave records and exposes extensive Run, step, Tool, model and delegation evidence, but the shipped audit service queries and presents those facts rather than independently challenging operations and returning correction.
- Decisive decision or feedback right: no independent auditor is shown deciding that an operational claim/result deviates and forcing or returning a corrective intervention.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: fail-closed delegation audit rows, trace timelines, status/statistics aggregation, admin audit UI, Tool tests/trials and retained run evidence.
- Closure path: operations write evidence → audit service loads/aggregates evidence → admin can inspect/export it. The first-party path stops before independent challenge → corrective feedback closure.
- Boundary reachability: audit query and delegation evidence are concrete shipped code paths.
- Why this is / is not agent-owned: logging, trace aggregation and pre-dispatch evidence requirements make behavior inspectable but do not supply the independent semantic audit right required by S3*.
- Evidence: [`agentaudit/service.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentaudit/service.go); [`agentdelegation/agent_tool.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/agentdelegation/agent_tool.go); [`architecture.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/architecture.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: Tool testing and Workflow trials can validate configured artifacts before publishing, but development-time tests do not automatically constitute independent audit of live S1 operations.

### Absence scope

- Surfaces inspected: admin trace/audit service, delegation audit lifecycle, Tool tests, Workflow trials/publishing and runtime evidence.
- Plausible first-party paths checked: `agentaudit` as S3*; mandatory delegation audit as S3*; Tool test/Workflow trial as S3*.
- Why no material first-party path remains: evidence capture/query and predeployment validation lack the materially independent live challenge plus corrective-return relation required by S3*.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-then prospective adaptation loop is established.
- Disturbance / variety regulated: operators can draft/revise/test/publish Agents, Tools and Workflows, and the runtime can persist context/checkpoints; these mechanisms change or preserve configured capability but do not themselves sense an external/future condition and select an organizational adaptation.
- Decisive decision or feedback right: no standard first-party actor is shown developing and selecting future-facing change from environmental intelligence and returning it into current operating capability.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: Agent prompt/model/capability configuration, Workflow drafts/revisions/trials/publishing, Tool test/publish lifecycle, durable run/context state and external service/model configuration.
- Closure path: human/operator configuration → trial/test/publish → later runtime use. The missing segment is a first-party prospective intelligence/adaptation decision that closes the loop without inheriting the operator's external judgment.
- Boundary reachability: configuration and publishing surfaces are shipped; their function remains lifecycle management rather than S4.
- Why this is / is not agent-owned: persistence, revisions and publishing provide memory/change mechanisms but no autonomous outside/future sensing and adaptation selection.
- Evidence: [`architecture.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/architecture.md); [`concepts.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/concepts.md); [`agentic_engine.go`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/backend/internal/einoruntime/agentic_engine.go).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: generated Workflow drafts or downstream automation could be incorporated into an adaptive organization, but the standard installation does not prove that closure.

### Absence scope

- Surfaces inspected: Workflow/Tool lifecycle, Agent revisions/configuration, runtime context/checkpoints, external Provider/Connection configuration and documented management plane.
- Plausible first-party paths checked: revisions/publishing as S4; trials/tests as S4; persisted context as S4; model-driven generation as S4.
- Why no material first-party path remains: the repository supplies mechanisms for change and current contextual operation, not a closed prospective organizational adaptation function.

## S5 — Policy / identity

- State: —
- Function: no material first-party recursive identity/ultimate-policy closure is established at the installation boundary.
- Disturbance / variety regulated: Workspace membership/RBAC, publish state, AAP grants/scopes, Agent capability bindings, A2A exposure/auth and runtime flags define permissions and configuration, but they do not decide what the organization is or resolve identity-level policy conflicts through a legitimate ultimate authority loop.
- Decisive decision or feedback right: no standard first-party actor receives identity/policy issues and returns a governing organizational identity or ultimate-policy decision.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: Workspace/RBAC, platform-administrator permissions, Agent/Tool/Workflow configuration and publishing, AAP credentials/grants/scopes, A2A exposure/auth policy and runtime feature flags.
- Closure path: operators configure policy-like objects → first-party runtime enforces them. The repository does not establish identity-level issue → legitimate ultimate authority → returned governing policy closure.
- Boundary reachability: access and governance objects are shipped and documented; negative classification follows the Profile's distinction between enforcement/configuration and S5 ownership.
- Why this is / is not agent-owned: the system enforces configured permissions and published versions but does not itself own ultimate identity/policy judgment.
- Evidence: [`architecture.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/architecture.md); [`concepts.md`](https://github.com/chenow9/act-weave/blob/ea0451acc090977c14c1c8d9d0b4d2bee5df4238/docs/concepts.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream organization may assign ultimate authority through ActWeave's configuration surfaces; that would be a separate system-in-focus and must be assessed from its own evidence.

### Absence scope

- Surfaces inspected: Workspace/RBAC, Agent/Tool/Workflow publishing, AAP grants/scopes, A2A exposure/auth and runtime flags.
- Plausible first-party paths checked: RBAC as S5; publishing governance as S5; Agent prompt/config identity as S5; AAP/A2A security policy as S5.
- Why no material first-party path remains: these paths constrain or authorize lower-level activity but do not close recursive identity/ultimate-policy governance.

## Overall assessment

ActWeave establishes a substantive autonomous S1 through its owned Agentic model/Tool/delegation loop and durable AgentRun lifecycle. Its multi-agent delegation, Workflow execution, budgets, traces, testing/publishing and access-governance machinery are significant constructor/enforcement mechanisms, but the pinned standard distribution does not close separate S2, S3, S3*, S4 or S5 organizational functions at the installation boundary.

Standalone vector:

```text
S1=A / S2=— / S3=— / S3*=— / S4=— / S5=—
```
