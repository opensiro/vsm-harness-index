---
harness_id: humanlayer-agent-control-plane
project_name: Agent Control Plane
repository: https://github.com/humanlayer/agentcontrolplane
review_ref: eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad
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

# Agent Control Plane

## Review boundary

- System in focus: one first-party `humanlayer/agentcontrolplane` installation at pinned revision `eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad`, including the shipped Kubernetes operator/controller manager, Agent/LLM/Task/ToolCall/MCPServer/ContactChannel resources, first-party task and tool-call state machines, LLM clients, MCP execution, sub-agent delegation and HumanLayer-backed human interaction paths.
- Purpose and identity: run durable long-lived outer-loop agents whose task conversation state, model turns, asynchronous tool calls, sub-agent calls and human interactions survive controller reconciliation and are represented as first-party resources.
- Relevant environment: external model-provider APIs and credentials; MCP servers/tools; humans reached through contact channels/HumanLayer; Kubernetes as substrate; users/operators creating and updating Agent/Task resources.
- Standard-distribution boundary: ACP's controller manager, CRDs, reconcilers/state machines, LLM client integration, tool adapters/executors and REST/API resource surfaces are inside. External LLM inference services, MCP-server implementations and humans are dependencies/environmental actors; their internal functions are not inherited.
- Credited operating / distribution surfaces: `README.md`; `acp/cmd/main.go`; `acp/api/v1alpha1/agent_types.go`; `acp/api/v1alpha1/task_types.go`; `acp/internal/controller/task/task_controller.go`; `acp/internal/controller/task/state_machine.go`; `acp/internal/controller/toolcall/state_machine.go`; `acp/internal/controller/toolcall/executor.go`; `acp/internal/server/server.go`.
- Adjacent first-party surfaces excluded from ownership: `hack/` prompts and repository-development review helpers; tests/examples except as corroboration; Kubernetes controller-runtime leader election/replica coordination where it only protects duplicate reconciliation; project contribution/release work; external HumanLayer service implementation beyond the first-party integration contract.
- First-party operating / deployment modes considered: normal Kubernetes controller-manager deployment with Task and ToolCall controllers; MCP tool use; configured sub-agent delegation; optional human-contact tools; optional per-MCP-server human approval before a selected tool call executes; REST/Kubernetes resource creation and observation.
- Recursion level: one ACP installation running one or more Agent/Task operational loops. A child Agent invoked through the built-in delegation tool is another S1 work unit inside the same installation, but topology/delegation alone is not treated as proof of S2 or S3.
- Reviewed revision: `eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

ACP is not merely a Kubernetes wrapper around an external agent process. The frozen source implements the substantive outer agent loop itself as first-party controller logic. A `Task` persists the conversation context and phase. `TaskReconciler` is wired into the shipped controller manager, obtains the configured Agent and LLM, collects MCP, human-contact and sub-agent tools, sends the current context to the model, and converts model-selected tool calls into first-party `ToolCall` resources. `ToolCallReconciler` executes or waits on those calls. When every call in the model turn completes, their results are appended to the parent Task's context window and the Task is returned to `ReadyForLLM`, causing the next model turn. A final textual response terminates the loop.

This establishes a first-party autonomous S1 actor even though model inference and tool implementations are external dependencies. ACP owns the durable decision/observation loop, action vocabulary, continuation state and return of observations into subsequent model decisions.

ACP can also expose another configured Agent as a tool. A model-selected `delegate_to_agent__<name>` call causes first-party code to create a child Task bound to the referenced Agent. The ToolCall then waits for that child Task and returns the child output or failure into the parent loop. This is real recursive/delegated operation, but the frozen runtime does not establish a function-specific inter-S1 disturbance that this relationship attenuates. The delegation relation is therefore not promoted to S2 merely because multiple agents can run.

Current-control mechanisms likewise remain narrower than S3 at this system boundary. Per-Task mutexes and Kubernetes Leases prevent duplicate concurrent model requests for the same Task across controller replicas; they protect execution consistency rather than allocating or regulating the whole population of operational units. Human approval can hold or reject a configured MCP ToolCall, but this is a local action gate over one S1 decision. The reviewed Task schema contains no first-party whole-fleet priority/quota/resource-allocation contract, and the operator-facing REST surface lists/creates Tasks and manages Agent definitions without establishing an autonomous or parent-owned whole-system current-management decision loop.

No materially independent runtime audit organization is established. Events, traces, status validation and human approval observe or gate the ordinary execution path; no separate reviewer/auditor actor obtains complementary evidence, challenges an operational claim and returns corrective findings through an independent S3* loop. Repository `hack/` review material is development tooling and is outside the product-runtime boundary.

No shipped prospective adaptation loop is established. Persistent Task context is operational memory, not S4. MCP discovery, agent validation and retry/reconciliation react to present runtime state. External human contact can provide task-level information, but the frozen organization does not transform outside/future distinctions into a prospective change to its own capability, organization or strategy and then return that adaptation into present operation.

Finally, system prompts, Agent definitions, contact-channel approval configuration and Kubernetes/API authority configure or constrain operation but do not close an identity/ultimate-policy issue through legitimate ultimate authority and return that decision as S5. They are not promoted from configuration/approval to S5 by importance or naming.

Primary evidence:

- [`README.md`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/README.md) — declared outer-loop architecture, first-party Task context loop, MCP/sub-agent/human interaction surfaces and deployment model.
- [`acp/cmd/main.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/cmd/main.go) — standard manager composition wiring Task and ToolCall reconcilers with the shared MCP manager.
- [`acp/internal/controller/task/task_controller.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/task/task_controller.go) — production Task reconciler, default LLM/tool adapters and manager registration.
- [`acp/internal/controller/task/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/task/state_machine.go) — durable model/tool continuation loop, per-Task lease, result return and next-turn progression.
- [`acp/internal/controller/toolcall/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/toolcall/state_machine.go) — asynchronous tool execution, approval wait, sub-agent wait and human-input wait paths.
- [`acp/internal/controller/toolcall/executor.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/toolcall/executor.go) — MCP execution, child Task creation for delegation and human approval/contact integration.
- [`acp/api/v1alpha1/task_types.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/api/v1alpha1/task_types.go) and [`acp/api/v1alpha1/agent_types.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/api/v1alpha1/agent_types.go) — first-party operational state, context, tool-call phase and Agent capability/delegation definitions.
- [`acp/internal/server/server.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/server/server.go) — standard REST surfaces for Task/Agent lifecycle and operator configuration.

## Operational model

A Task is ACP's durable operational unit. Its status carries the context window and phase. The controller validates the configured Agent, obtains the Agent's LLM and tools, sends the context through ACP's first-party LLM client, and interprets the result as either a final answer or one or more asynchronous ToolCall resources. ToolCall controllers execute MCP actions or mediate delegated Agent/Human interactions. Completed results are added to the Task's context as tool messages and re-enter the Task controller for another model turn.

The model is therefore a dependency that supplies semantic choice, while ACP supplies and owns the surrounding operational closure. Removing the external inference provider breaks cognition, as it would in many agent runtimes, but leaving only a raw model call would not recreate ACP's durable goal-directed tool loop. Conversely, the first-party controllers determine what observations return to the model, when another turn occurs and when the Task becomes terminal.

Sub-agent Tasks are ordinary ACP Tasks created by a model-selected delegation tool. The parent ToolCall polls the child state and returns the child output into the parent context. This creates nested operations but does not establish a separate coordination or management function without evidence of the relevant disturbance/current-control right.

## S1 — Operations

- State: A
- Function: perform a durable goal-directed agent task through repeated model decisions and asynchronous tool/environment interactions until a final answer or terminal failure.
- Disturbance / variety regulated: task/user objective, changing context window, available MCP/human/sub-agent tools, model-selected tool calls, asynchronous tool outcomes, transient model/tool failures and child/human completion latency.
- Decisive decision or feedback right: choose the next substantive answer/tool action from the current Task context, then incorporate returned tool observations into the next semantic decision.
- Decision owner: the configured ACP Agent's model-driven Task loop implemented by first-party Task/ToolCall controllers.
- Supporting / enforcement mechanisms: durable Task/ToolCall CRDs, phase state machines, first-party LLM client factory, tool adapters/executor, per-Task mutex/Lease, controller-runtime reconciliation, context persistence, retries and terminal-state handling.
- Closure path: Task objective/context → first-party Task controller sends context/tools to configured model → model chooses final content or tool calls → ACP creates first-party ToolCall resources → MCP/sub-agent/human path returns results → ACP appends tool messages to Task context → Task returns to `ReadyForLLM` → next model decision or final answer.
- Boundary reachability: `acp/cmd/main.go` registers both Task and ToolCall reconcilers in the standard controller manager; `TaskReconciler.SetupWithManager` binds the Task CRD and initializes the production state machine.
- Why this is / is not agent-owned: deterministic controllers enforce durable progression, but substantive next-action selection comes from the Agent's configured model over first-party-maintained context and tool choices. Human approval is optional for configured MCP tools and does not remove the standard autonomous operation path.
- Evidence: [`acp/cmd/main.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/cmd/main.go); [`acp/internal/controller/task/task_controller.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/task/task_controller.go); [`acp/internal/controller/task/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/task/state_machine.go); [`acp/internal/controller/toolcall/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/toolcall/state_machine.go); [`acp/internal/controller/toolcall/executor.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/toolcall/executor.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model inference, MCP servers and humans are dependencies. Their internal functions are not inherited; the positive S1 claim rests on ACP's first-party ownership of the iterative operational closure around them.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes regulation of a concrete disturbance between distinct ACP S1 operational units with feedback that changes their subsequent mutual behaviour.
- Disturbance / variety regulated: ACP supports multiple Agents/Tasks and parent-to-child delegation, but the frozen standard distribution does not identify a specific inter-S1 collision, contention, contradictory commitment or shared-resource disturbance whose attenuation forms a closed coordination relation.
- Decisive decision or feedback right: not established as a distinct S2 right.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: child Task creation, parent/child labels, child-result polling, Task-specific mutexes and Kubernetes Leases.
- Closure path: delegation closes parent operation → child Task → child result → parent operation, which is task decomposition/recursion. The Task Lease closes duplicate controller execution for one Task. Neither path demonstrates inter-S1 disturbance → attenuation → feedback into multiple S1 units.
- Boundary reachability: delegation and Task leases are standard-runtime code, but their organizational function is not S2 under the Profile criteria.
- Why this is / is not agent-owned: multiple agents and delegation are topology. A controller lease is infrastructure consistency. Neither supplies the required coordination function merely because it affects concurrency.
- Evidence: [`acp/internal/controller/toolcall/executor.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/toolcall/executor.go); [`acp/internal/controller/toolcall/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/toolcall/state_machine.go); [`acp/internal/controller/task/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/task/state_machine.go); [`acp/api/v1alpha1/agent_types.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/api/v1alpha1/agent_types.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: an adopter can define interacting Agents/tools whose domain creates coordination needs. Such an instantiated organization would require separate evidence; ACP's generic delegation mechanism does not itself close S2.
- Distinct S1 units checked: parent and child ACP Tasks/Agents created through the built-in delegation tool.
- Inter-S1 disturbance checked: no first-party contract was found for branch/resource collision, contradictory shared commitments, rate/resource interference or another disturbance between those Tasks.
- Why generic communication/routing/delegation is insufficient: the child result is simply returned as the result of the parent's selected tool call; no function-specific attenuation of mutual disturbance is established.

### Absence scope

- Surfaces inspected: Task/ToolCall state machines, child-task creation/waiting, Task distributed lease, Agent sub-agent configuration and standard controller composition.
- Plausible first-party paths checked: sub-agent delegation as S2; multiple ToolCalls as coordination; Task lease as S2; Kubernetes leader/controller scheduling as S2.
- Why no material first-party path remains: each path is delegation, one-task execution consistency or infrastructure-level duplicate suppression rather than coordination among viable operational units.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system present-management loop is established across the running Agent/Task population.
- Disturbance / variety regulated: individual Tasks are durably progressed and individual ToolCalls can be gated, retried or rejected; these controls do not provide a whole-current view with authority to allocate/reallocate resources or intervene across the operational organization as S3.
- Decisive decision or feedback right: no first-party actor is shown receiving a whole-system current state and deciding present resource/work allocation or cross-unit intervention for the installation.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: per-Task reconciler state, Task mutex/Lease, ToolCall approval, Agent/Task REST CRUD/list surfaces and Kubernetes controller manager.
- Closure path: local Task state drives local reconciliation; configured human approval can decide whether one MCP call proceeds. No whole-system current-state → management judgment → intervention → changed organization-wide operation loop is established.
- Boundary reachability: the cited local controls are standard runtime. Their presence is insufficient to change their organizational function into S3.
- Why this is / is not agent-owned: durable supervision, retries, distributed locking and action approval are enforcement/operational mechanisms. No autonomous or parent current manager owns a whole-system S3 decision right at this boundary.
- Evidence: [`acp/internal/controller/task/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/task/state_machine.go); [`acp/internal/controller/toolcall/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/toolcall/state_machine.go); [`acp/api/v1alpha1/task_types.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/api/v1alpha1/task_types.go); [`acp/internal/server/server.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/server/server.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a user/operator can create, update or delete Agent definitions through API/Kubernetes surfaces, but generic administrative CRUD is not by itself a whole-current S3 function.
- Whole-system current view checked: REST listing and Kubernetes resource observation expose state but no first-party current-management decision loop is bound to that view.
- Current-control scope checked: no task priority, fleet quota, work reallocation or comparable whole-population management right was established in the reviewed Task/Agent contracts.

### Absence scope

- Surfaces inspected: Task/Agent schemas, Task reconciliation and distributed locking, ToolCall approval, standard REST Task/Agent APIs and controller-manager composition.
- Plausible first-party paths checked: Task controller as manager; Kubernetes controller manager as S3; human ToolCall approval as parent S3; sub-agent delegation as S3; REST list/update APIs as whole-current control.
- Why no material first-party path remains: the paths either maintain one resource's desired state, gate one action, expose generic administration or decompose work without a whole-system present-management decision right.

## S3* — Complementary audit

- State: —
- Function: no material runtime path establishes an independent complementary audit of S1 operation with corrective return.
- Disturbance / variety regulated: ACP records Kubernetes events/traces, validates resource dependencies and can require a human to approve a selected MCP call; these mechanisms observe or constrain the ordinary path but do not form a separate audit organization.
- Decisive decision or feedback right: no independent auditor is shown judging operational claims/outcomes from materially complementary evidence and returning a corrective finding into subsequent operation.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: status/events, OpenTelemetry spans, validation, human approval and repository-development review helpers outside the runtime boundary.
- Closure path: runtime events/status support observability and approval may allow/reject a proposed tool call, but there is no independent audit finding → corrective action → re-observation loop over completed/ongoing work.
- Boundary reachability: observability and approval are shipped; repository `hack/` reviewer prompts are adjacent development material and excluded from runtime ownership.
- Why this is / is not agent-owned: approval before an action executes is not complementary audit of operational reality, and telemetry does not own audit judgment merely because it records evidence.
- Evidence: [`acp/internal/controller/toolcall/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/toolcall/state_machine.go); [`acp/internal/controller/task/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/task/state_machine.go); [`acp/cmd/main.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/cmd/main.go).
- Basis: structural negative search.
- Confidence: high.
- Caveats: an Agent may be configured by an adopter to act as a reviewer, but role/prompt configuration does not establish a standard-distribution S3* function without evidence of independence and corrective closure.

### Absence scope

- Surfaces inspected: Task and ToolCall runtime paths, status/events/tracing, human approvals, controller composition and repository reviewer-related search surfaces.
- Plausible first-party paths checked: human approval as S3*; event/trace history as audit; validation as audit; sub-agent configured as reviewer; repository `hack/` code-review helpers as runtime audit.
- Why no material first-party path remains: no materially independent product-runtime audit actor/decision loop is wired over operational outcomes.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective adaptation loop is established in the shipped runtime.
- Disturbance / variety regulated: ACP reacts to current model/tool errors, dependency readiness, human responses and child-task results, but those are present operational observations rather than outside/future intelligence that changes the organization's future capability or strategy.
- Decisive decision or feedback right: no runtime owner is shown generating/evaluating a prospective adaptation option and returning the chosen change into current organizational capability.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: durable context window, retries, MCP discovery, Agent validation, human-contact tools and external model/tool inputs.
- Closure path: not established. Current observations return to the same Task loop as operational context; they do not become an organization-level prospective adaptation that changes how ACP subsequently operates.
- Boundary reachability: reviewed first-party runtime code contains adapters and reactive controllers but no separate learning/adaptation owner/path.
- Why this is / is not agent-owned: memory/context persistence and access to humans/external tools can support S1 cognition without constituting S4. Future-facing function must be proven separately.
- Evidence: [`acp/internal/controller/task/state_machine.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/task/state_machine.go); [`acp/api/v1alpha1/task_types.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/api/v1alpha1/task_types.go); [`acp/api/v1alpha1/agent_types.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/api/v1alpha1/agent_types.go).
- Basis: structural negative search.
- Confidence: high.
- Caveats: an application built on ACP can create a research/adaptation Agent organization. That downstream composition is a separate system-in-focus.

### Absence scope

- Surfaces inspected: Task context lifecycle, Agent definitions, MCP discovery, human contact, retry/reconciliation paths and first-party runtime source searches for learning/adaptation machinery.
- Plausible first-party paths checked: persistent context as S4; human contact as environmental intelligence; sub-agent research as S4; MCP discovery as environmental sensing; retry/reconciliation as adaptation.
- Why no material first-party path remains: all identified paths serve current task execution or dependency validation and do not close prospective organization/capability adaptation.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the ACP installation recursion.
- Disturbance / variety regulated: Agent system prompts, model/tool configuration, sub-agent lists and MCP approval settings constrain operational behaviour, while users/operators can create/update resources; none is shown recognizing and resolving an organizational identity/ultimate-policy issue as S5.
- Decisive decision or feedback right: no first-party path establishes identity/policy issue → legitimate ultimate authority → authoritative decision → return governing subsequent operation.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: Agent `system` prompt, Agent/LLM/MCP resource configuration, optional approval contact channel, Kubernetes/API administration and human contact paths.
- Closure path: configuration enters normal operation directly; configured approvals decide concrete ToolCalls. No distinct ultimate-policy feedback loop is established.
- Boundary reachability: these configuration and approval surfaces are shipped and reachable, but their organizational function remains setup/action gating rather than S5 identity governance.
- Why this is / is not agent-owned: system prompts and approval authority are not S5 by vocabulary or importance. The required identity/ultimate-policy closure is absent.
- Evidence: [`acp/api/v1alpha1/agent_types.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/api/v1alpha1/agent_types.go); [`acp/internal/controller/toolcall/executor.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/controller/toolcall/executor.go); [`acp/internal/server/server.go`](https://github.com/humanlayer/agentcontrolplane/blob/eaa2a7ed1d9cb4e13dc53defaf420e36f481dcad/acp/internal/server/server.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: external Kubernetes administrators or application owners can act as ultimate authority in a wider organization, but generic platform administration is not automatically parent-owned S5 for ACP standalone.

### Absence scope

- Surfaces inspected: Agent/System/LLM/MCP configuration, approval channels, REST/Kubernetes administration, human-contact paths and runtime source searches for explicit policy/identity machinery.
- Plausible first-party paths checked: system prompt as S5; Agent configuration as constitution; human approval as ultimate policy; Kubernetes owner/admin as parent S5; contact channels as escalation-to-S5.
- Why no material first-party path remains: each path configures/gates lower-level operation or belongs to a wider deployment authority without a first-party identity/ultimate-policy closure loop.

## Distributed OSS parent arrangement

Repository maintainers are not treated as the parent of a running ACP installation merely because they publish its code. A cluster/application operator can configure Agents and approval channels, but those generic administrative rights are not published as S3 or S5 without the function-specific closure required by the Profile.

## Self-hosted and non-human modes

ACP's autonomous S1 does not depend on a human being present: an Agent using MCP/sub-agent tools without configured human approval/contact can run through repeated model/tool turns to completion. Configuring HumanLayer approval or contact introduces a parent/environmental decision inside particular S1 tool paths, but it does not by itself reclassify S1 as parent-owned or create a metasystem function.

## Recursion

Sub-agent delegation can create a nested ACP Task whose own Agent runs the same first-party S1 loop. The parent sees that child as a delegated tool and receives the child output. This demonstrates operational recursion/decomposition, but each additional VSM function still requires its own evidence. In particular, parent/child topology alone does not establish S2 or S3.

## Variety and escalation

ACP attenuates operational variety through durable phase machines, Task-specific locking, validation, retries, explicit ToolCall resources and optional human approval. It amplifies operational capacity by exposing MCP tools, child Agents and human contact as model-visible tools. Escalation can suspend a selected MCP action for human approval or suspend a Task waiting for human input, then return the response to the ongoing S1 loop. These are genuine S1 support/parent mechanisms; they are not promoted to S3*/S5 without the corresponding organizational function.

## Evidence gaps

- No concrete first-party inter-S1 disturbance/feedback relation was established beyond delegation and one-Task controller locking; therefore S2 remains `—`.
- No whole-system present-management decision loop was established over the Task/Agent population; local reconciliation and action approval remain below the S3 threshold.
- No independent runtime audit actor with complementary evidence and corrective return was established; telemetry/approval are insufficient for S3*.
- No deployed outside/future adaptation or identity/ultimate-policy closure was established for S4/S5.
- A downstream ACP application can instantiate richer organizational semantics through prompts/tools/Agent graphs, but each such composition is a separate system-in-focus and cannot be credited to the generic standalone distribution without evidence.
