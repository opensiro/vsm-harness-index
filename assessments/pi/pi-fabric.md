---
harness_id: pi-fabric
project_name: Pi Fabric
repository: https://github.com/fabric-runtime/pi-fabric
review_ref: b166b4c72c58c74c7aa8c81aeda46e344d89eb68
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Pi Fabric

## Review boundary

- System in focus: The published Fabric extension installed in a supported Pi session with one Fabric-managed project workflow and its child agents or actors.
- Purpose and identity: Compose coding tools, agents and durable project work under one checked, permissioned runtime.
- Relevant environment: Pi coding host, configured model providers, Git workspace, operator, project mesh and externally configured connectors.
- Standard-distribution boundary: Fabric package, native extension binding, included skills and provider implementations in supported project workflows.
- Credited operating / distribution surfaces: fabric_exec, worker and actor runtime, workflow and mesh providers, installed swarm and spec supervisor templates, Activity/Topology and decision surfaces.
- Adjacent first-party surfaces excluded from ownership: Benchmark agents, proof generators and developer CI, external Foreman project, external application connectors and host policies outside Fabric.
- First-party operating / deployment modes considered: Default Pi with code-mode tool, optional durable actors and user-invoked swarm, workflow and spec supervisor profiles, operator control of active work.
- Recursion level: One Fabric-managed project run with Main and several scoped lower-level agent or actor work units.
- Reviewed revision: b166b4c72c58c74c7aa8c81aeda46e344d89eb68.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Fabric registers a checked code-execution tool in the Pi host. Main's model writes a program using Fabric's execution bridge. Commands resolve into native Pi tools, MCP, documented child runners or durable actors. Agents can expose progress and outcomes, while the project mesh can preserve tasks, claims, events and durable decisions. An active host validates and dispatches tool calls under configured scopes and budgets. The installed skill templates provide optional organization-specific operating routines.

## Operational model

A Pi model and subordinate model sessions choose code and tools and produce workspace, analysis or task artifacts. A Fabric workflow can distribute several operational scopes and revise control as results arrive. The same operator can intervene via the project run display. Compliance actors have separate read-only access and return scoped correction to Main. Static limits and approval machinery enforce choices as they are made.

## S1 — Operations

- State: A
- Function: Execute a coding or analysis task over selected tool and worker capabilities.
- Disturbance / variety regulated: New user objectives, workspace observations, tool failures and output shape require different control flow and next actions.
- Decisive decision or feedback right: Author and revise a Fabric program that chooses Pi tools, worker calls, branches and follow-up observations.
- Decision owner: The Pi model in the host session, and model-backed workers for assigned subprocess outcomes.
- Supporting / enforcement mechanisms: Tool registration, checked guest programs, host validation, tool dispatch, resource and approval policies.
- Closure path: The program's selected calls run on the workspace or participant and return results to the same model for further action.
- Boundary reachability: The installed extension registers fabric_exec in native Pi and documents a standard model-authored execution path.
- Why this is / is not agent-owned: The runtime checks and dispatches the program. The model chooses its content and concrete actions.
- Evidence: [standard entry](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/README.md#how-it-works), [extension registration](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/src/extension.ts), [tool definition](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/src/fabric-exec-tool.ts)
- Basis: structural
- Confidence: High
- Caveats: Provider-backed path reviewed from source. No model run was made.

## S2 — Coordination

- State: A
- Function: Coordinate independently working persistent agents around conflicting task claims and dependencies.
- Disturbance / variety regulated: Two actors may choose the same apparently ready task, or start a dependent task before its predecessor is completed.
- Decisive decision or feedback right: Choose acceptable role-matching work, claim it atomically, withdraw on conflict, and unblock downstream work only when prerequisites are complete.
- Decision owner: Persistent role agents in the first-party swarm recipe, acting on versioned task state.
- Supporting / enforcement mechanisms: Mesh compare-and-swap, task states, dependencies, path partition and actor mailboxes.
- Closure path: A stale claim causes the losing actor to stop work. A completed prerequisite publishes new state and an eligible actor reconsiders ready work. Claimed work is executed only by its current owner.
- Boundary reachability: The user-invoked shipped swarm skill explicitly binds these rules to standard agents and mesh operations.
- Why this is / is not agent-owned: The store enforces the numbered precondition. Role agents choose what to claim and act on conflicts and completed dependencies.
- Evidence: [swarm instructions and program](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/skillsets/typescript/fabric-swarm/SKILL.md), [mesh store](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/src/mesh/store.ts), [mesh calls](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/src/providers/mesh-provider.ts)
- Basis: structural
- Confidence: High
- Caveats: Requires the supported mesh and user-invoked swarm mode. Basic independent worker fan-out alone carries no claim.
- Distinct S1 units: Persistent model workers with separate identities executing assigned project tasks.
- Inter-S1 disturbance: Duplicate claims and overlapping ownership under simultaneous reads, plus downstream jobs crossing unfinished dependencies.
- Attenuating coordination relation: Versioned claim arbitration, predecessor verification and path scope limit each worker's interference.
- Feedback into subsequent S1 behaviour: Losing claimants stop or select a different task; dependency completion makes downstream work eligible.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The installed protocol requires concrete claim-loss and dependency-conditioned actions by independent workers.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate active commitments and interventions across one managed Fabric workflow.
- Disturbance / variety regulated: Partial or all-worker failure, blocked work, progress divergence and shared execution ceilings call for continuation, a different allocation or cessation.
- Decisive decision or feedback right: Determine which scoped work to start, continue or hold in response to the whole run, or choose an operator override of currently active work and assignments.
- Decision owner: Main's model for the authored workflow and its corrective instructions. The legitimate interactive project operator owns the separate live intervention path.
- Supporting / enforcement mechanisms: Workflow phase/item state, worker outcomes, completion inbox, topology activity, work budget observations and dispatched steer/stop controls.
- Closure path: Model-authored programs use returned results to proceed, halt, verify or issue revised work. Operator steering, follow-up or stop decisions return to selected actors or tasks and change their next activity.
- Boundary reachability: The packaged workflow template and observable run controls are available under the same Pi extension. The operator can inspect the active tree and send targeted input.
- Why this is / is not agent-owned: The model decides the live workflow and its conditional response within preset ceilings. In the operator mode the project operator decides binding interventions using the activity and topology evidence.
- Evidence: [workflow and result decisions](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/skillsets/typescript/fabric-workflow/SKILL.md), [runtime visibility and steering](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/agents.md#unified-participants-and-steering), [operator intervention surface](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/interface.md), [topology control](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/src/topology/control-plane.ts)
- Basis: structural
- Confidence: Medium
- Caveats: Scope is one managed project run. Fixed budgets and a Foreman hint alone do not establish discretionary S3.
- Whole-system current view: The assessed workflow's phases, child outcomes and active tree including Main, agents, actors and background tasks, with spend and status.
- Current-control decision scope: Authorize or withhold further work, start verification or repair, direct particular active participants, and halt tasks in the current project run.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Main's model | New worker outcome or active-run disturbance | Sets and changes run commitments through dispatched work, steering, termination or verification. | [workflow and result decisions](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/skillsets/typescript/fabric-workflow/SKILL.md) |
| Parent (`P`) | Legitimate local operator | Active tree reveals a blocked or misdirected participant or task. | Operator submits steering or stop through Fabric, and the addressed work continues under the new commitment or ends. | [project operator interface](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/interface.md) |

## S3* — Complementary audit

- State: A
- Function: Independently inspect task evidence against acceptance requirements and send an actionable correction.
- Disturbance / variety regulated: Main's transcript may claim compliance even when artifacts or test evidence fall short.
- Decisive decision or feedback right: Judge which acceptance item is unverified and decide whether an independent read calls for a correction, silence or completion.
- Decision owner: A dedicated model-backed, read-only spec supervisor actor.
- Supporting / enforcement mechanisms: Explicit acceptance ledger, idle/error subscriptions, bounded transcript, direct read/grep/find/ls, directive delivery with wake enabled.
- Closure path: The reviewer compares the spec with primary code or test evidence. Material findings return to Main through steering and can trigger a corrective turn.
- Boundary reachability: The published spec supervisor skill instantiates a dedicated Fabric actor through the standard ambient setup with read-only tools and explicit event selection.
- Why this is / is not agent-owned: The separate actor evaluates the evidence and chooses the directive. Deterministic delivery controls return it to Main without owning the judgment.
- Evidence: [spec supervisor profile](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/skillsets/typescript/fabric-spec/SKILL.md), [read-only actor setup and live steering](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/skillsets/typescript/fabric-ambient/references/setup.md), [actor delivery](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/agents.md#persistent-actors)
- Basis: structural
- Confidence: High
- Caveats: The supported witness uses an explicitly invoked supervisor. Council vote or trace visibility alone was not used.
- Claim being audited: Main's reported implementation satisfies all feature-spec acceptance conditions.
- Ordinary reporting path: Main and worker outcomes and tool output in the normal run transcript.
- Complementary access path: Fresh actor with read-only source and file discovery can check artifacts against the full named spec.
- Independence boundary: Separate actor and mandate, read-only artifact inspection, no implementation ownership.
- Who acts on findings: Main receives a targeted corrective directive and can resume work.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense an external strategic or future constraint and generate an adapted capability that enters later operations.
- Disturbance / variety regulated: External provider, component and model changes can create future tool or plan gaps.
- Decisive decision or feedback right: No reviewed built-in mode turns externally sensed future options into a selected ongoing capability adaptation.
- Decision owner: Operators or application extensions decide prospective component and policy changes.
- Supporting / enforcement mechanisms: Capability registration and reconciliation, component plan/apply, model guidance selection and tool entropy compilation.
- Closure path: Provider changes can resolve declared commitments and explicit replacement can change future calls. Entropy compiles representation improvements from observed action friction within existing capability.
- Why this is / is not agent-owned: The fixed normal-form compiler and component apply mechanisms do not own an externally grounded adaptation choice.
- Evidence: [normal forms and preservation](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/entropy.md), [component plans and external discovery](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/components.md#live-configuration-control), [role guidance](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/components.md#model-facing-guidance-components)
- Basis: structural
- Confidence: Medium
- Caveats: User-directed research or future connector composition is possible and its decisive loop was not attributed to this shipped boundary.

### Absence scope

- Surfaces inspected: Tool entropy and plan activation, component discovery and plan/apply, role and skill workflows, model dispatch and adapters.
- Plausible first-party paths checked: Background work observing activity, external component generation changes and prospective capability-replacement decisions.
- Why no material first-party path remains: Shipped optimization stays inside existing invocation capability. Component plans reconcile supplied definitions and requests. Reviewed standard workflows do not assemble outside intelligence, alternatives and autonomous or parent-led adoption.

## S5 — Policy and identity

- State: —
- Function: Adjudicate a change of project identity or ultimate policy through a legitimate authority and apply it to future operation.
- Disturbance / variety regulated: Conflicting project identities or standing tool-policy commitments may require authority above current task decisions.
- Decisive decision or feedback right: No first-party identity or ultimate-policy decision loop was identified.
- Decision owner: An operator can set configuration and approve particular calls. External host and project authority remain outside the described Fabric policy path.
- Supporting / enforcement mechanisms: Risk gates, project trust, scope, actor instruction or tool restrictions and durable decision routing.
- Closure path: Approval answers can permit or deny a pending call and operator settings govern subsequent execution. No shipped identity-policy issue, decision owner and governing return is bound as one loop.
- Why this is / is not agent-owned: Deterministic enforcement and generic approval transport do not adjudicate a new standing goal or ultimate policy.
- Evidence: [approval configuration](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/configuration.md#approvals), [durable decisions](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/decisions.md), [component and actor commitment enforcement](https://github.com/fabric-runtime/pi-fabric/blob/b166b4c72c58c74c7aa8c81aeda46e344d89eb68/docs/components.md#actor-commitments)
- Basis: structural
- Confidence: Medium
- Caveats: An application can build its own policy authority on the generic durable decision mechanism.

### Absence scope

- Surfaces inspected: Default and session policies; durable question, approval and escalation routing; actor scope and component commitment rules.
- Plausible first-party paths checked: Whole-run policy revision versus one-action approval; persisted settings; a legitimate constrained escalation to an owner.
- Why no material first-party path remains: The latter only attaches to user-defined generic decisions or the execution of approved actions. No installed identity or policy authority loop was verified.

## Recursion

Main spans one project workflow. Agents and actors are lower operational units with scoped autonomy. Nested execution, residency and tool recursion do not establish an additional viable organization.

## Variety and escalation

Checked programs and capability limits constrain tool variety. Atomic task state coordinates workers. The bundled spec reviewer can direct correction, while operator controls return current intervention at the managed project boundary.

## Evidence gaps

Pinned source-only assessment. No model calls, external connectors, hosted deployment or separate Index audit were executed. Positive states apply to the specific documented first-party operating modes above.
