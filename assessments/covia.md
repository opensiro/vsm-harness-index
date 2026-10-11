---
harness_id: covia
project_name: Covia
repository: https://github.com/covia-ai/covia
review_ref: 8838132b99e91fc287ac7b2b4b7125c88e7adef2
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Covia

## Review boundary

- System in focus: one self-hosted, first-party Covia venue at the frozen source revision, including its agent execution adapters, venue engine, job lifecycle, scheduler, lattice state, and shipped venue administration operations.
- Purpose and identity: host discoverable AI and agent operations, execute local agent jobs, preserve results and state, and allow explicit invocations across independent venues without transferring governance or data custody automatically.
- Relevant environment: local deployment operator, configured model providers and tools, requesters/credential holders, optionally other independently operated venues, MCP/A2A clients, storage and network.
- Standard-distribution boundary: the deployable Java venue and bundled adapters registered by `Engine`; available configured self-hosted/managed operations count only where actually installed and authorized. External model-service internals, partner venues and caller-authored orchestration/policy do not acquire Covia ownership.
- Credited operating / distribution surfaces: `AgentAdapter` run/wake loop, `LLMAgentAdapter` and `GoalTreeAdapter` agent transitions, `ToolCycleEngine`, built-in `Orchestrator`, `JobManager`, lattice-resident `AgentState`, `Scheduler`, `VenueAdapter` live adapter registry/configuration and authoritatively guarded parent administration.
- Adjacent first-party surfaces excluded from ownership: SDK examples, workbench, developer/CI/test rigs, documentation plans and proposals, mock/provider-specific integration tests, release/governance workflows, independently deployed grid peers and third-party tool/adapter code.
- First-party operating / deployment modes considered: local model-backed agent sessions/tasks with built-in `llmagent` or `goaltree`; grid operation/tool dispatch; built-in DAG orchestration; per-user job pause/cancel/resume; operator-authorized live venue administration. Remote federation remains an external call boundary.
- Recursion level: one venue as an operational organization, with resident agentic task-execution as S1; separate partner venues are not silently nested S1 units.
- Reviewed revision: `8838132b99e91fc287ac7b2b4b7125c88e7adef2` (frozen `develop` revision; not replaced by later default head).
- Observation date: 2026-10-11.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

Covia's `Engine` registers an executable, self-hosted venue with built-in `agent`, `llmagent`, `goaltree`, `orchestrator`, `grid`, messaging, identity/capability and storage adapters. `JobManager` admits invocations under caller and capability constraints, associates execution with durable per-user job records and exposes owner-authorized pause/resume/cancel. The lattice-backed `AgentState` records tasks, sessions and transition state, while `Scheduler` wakes deferred operations with captured caller authority. These are actual runtime paths, not merely abstract protocol declarations.

The agentic operating path is particularly concrete: `AgentAdapter.executeRunLoop` chooses pending task/session inputs and calls a configured transition operation repeatedly. `LLMAgentAdapter.invokeWithToolLoop` sends assembled session observations to the configured model, accepts its discretionary tool-call selection, dispatches tools through `ToolCycleEngine`, commits results, and presents those new observations on later turns. The shipped `GoalTreeAdapter` additionally supports model-driven subgoals and nested frames. External model weights/providers remain dependencies; the first-party venue closes the agent/tool/feedback loop.

`Orchestrator` executes caller-specified DAG steps, waits for dependencies and refuses to release downstream steps after a failed predecessor, recording job status. This is real first-party orchestration, but topology and sequencing alone are not a qualifying inter-S1 conflict-attenuation witness. `VenueAdapter` separately exposes venue-wide effective config, enabled/disabled adapters and loaded modules; holders of explicit venue-rooted management authority can enable/disable/configure adapters, load/unload modules and restart the process. These changes affect live availability. The management API, rather than a pre-installed autonomous supervisory policy, supplies a constructor interface for S3 and a separate authorized parent/operator-controlled mode.

Primary pinned evidence: [`Engine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Engine.java), [`AgentAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/AgentAdapter.java), [`LLMAgentAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/LLMAgentAdapter.java), [`GoalTreeAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/GoalTreeAdapter.java), [`ToolCycleEngine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/ToolCycleEngine.java), [`Orchestrator.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/Orchestrator.java), [`JobManager.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/JobManager.java), [`AgentState.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/AgentState.java), [`Scheduler.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Scheduler.java), [`VenueAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/VenueAdapter.java), [`Audit.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Audit.java), [`CapabilityGate.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/lattice/CapabilityGate.java); [`README.md`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/README.md).

## Operational model

One deployed venue can own multiple agent tasks, but resident agent transitions, scheduler firings and DAG nodes are not automatically independent VSM-recursive organizations. For S1, the configured model selects task-specific next actions from newly observed state and available tools; first-party job and session machinery enforces and returns results. For S3, `venue/adapters` and `venue/show-config` expose venue-wide current deployment capability and `venue/adapter/*` operations can change it. A separate deployment-authorized operator decides when and how to intervene; ordinary caller job controls are more narrowly scoped.

## S1 — Operations

- State: A
- Function: Transform authorized agent tasks into model-chosen tool actions and completed task results through a live venue execution loop.
- Disturbance / variety regulated: Uncertain task inputs, tool availability, model responses, failures, concurrency, session history and changing tool observations.
- Decisive decision or feedback right: Select the next model-directed task/tool action or goal decomposition in response to current task, conversation and tool results.
- Decision owner: Model-backed agent invoked via first-party `llmagent` / `goaltree` transition, rather than deterministic job scheduling.
- Supporting / enforcement mechanisms: `AgentAdapter` wake/CAS/transition loop, `ToolCycleEngine` tool registry and barriers, `JobManager` admission, durable session and tool-event store, iterations/cancellation.
- Closure path: Task/session observation → assembled model inference → discretionary tool calls/subgoals → venue-executed operations → persisted results and changed observations → next model-directed turn or task completion.
- Boundary reachability: `Engine` installs `AgentAdapter`, `LLMAgentAdapter` and `GoalTreeAdapter` as bundled operations and the public README documents locally hosted agent adapters, not a test-only extension.
- Why this is / is not agent-owned: Removing model decision output while leaving the engine, DAG runner and job persistence in place removes the task-specific next-tool/subgoal discretion; those deterministic mechanisms do not supply an equivalent task policy.
- Evidence: [`Engine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Engine.java), [`AgentAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/AgentAdapter.java), [`LLMAgentAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/LLMAgentAdapter.java), [`GoalTreeAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/GoalTreeAdapter.java), [`ToolCycleEngine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/ToolCycleEngine.java), [`JobManager.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/JobManager.java)
- Basis: explicit + structural
- Confidence: high
- Caveats: A hosted external model is a dependency, not a donated foreign organizational S1; credit is for the first-party wired decision/tool/feedback composition, not benchmark performance.

## S2 — Coordination

- State: —
- Function: No first-party S2-specific attenuation relation among separately established S1 operational units is demonstrated at the venue recursion.
- Disturbance / variety regulated: A qualifying inter-S1 interference or oscillation is not identified; tool overlap and dependency ordering are not sufficient.
- Decisive decision or feedback right: No evidenced decision regulating an identified conflict between distinct operational S1 units.
- Decision owner: No S2 owner established.
- Supporting / enforcement mechanisms: DAG dependency barriers, per-user job limits, scheduler invocation, agent messaging and parallel tool batches.
- Closure path: No distinct S2 coordination-and-return loop; dependency release/stop is part of caller-defined execution constraints.
- Why this is / is not agent-owned: Orchestration and messaging route or serialize work, while cross-venue federation links independently governed organizations; none supplies the required concrete inter-S1 disturbance → attenuation → changed subsequent S1 behavior at this declared recursion.
- Evidence: [`Orchestrator.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/Orchestrator.java), [`ToolCycleEngine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/ToolCycleEngine.java), [`JobManager.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/JobManager.java), [`Scheduler.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Scheduler.java), [`AgentAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/AgentAdapter.java)
- Basis: structural
- Confidence: medium-high
- Caveats: A user could compose multiple agents into an organization with additional coordination policy, but that user-supplied composition is not itself a built-in first-party S2 owner.

### Absence scope

- Surfaces inspected: Bundled DAG orchestrator, agent messaging/run loop, tool batching, job concurrency, venue scheduler and grid federation documentation.
- Plausible first-party paths checked: Multi-agent DAG dispatch, shared operation/resource access, messaging, dependency failure handling and remote-venue execution boundaries.
- Why no material first-party path remains: Observed safeguards enforce execution order and task/job admission, without a shipped relation that identifies and corrects inter-S1 interference among distinct first-party operating units.

## S3 — Inside-and-now control

- State: C(P)
- Function: Expose the current whole-venue operational composition and change the live shared adapter/module capacity and availability.
- Disturbance / variety regulated: Shared operation availability, effective adapter configuration, runtime module state and deployment-wide service constraints.
- Decisive decision or feedback right: Decide which non-kernel adapters/modules are enabled, disabled, reconfigured or loaded and whether to restart the current venue process.
- Decision owner: Base constructor mode: an application-author must supply an S3-specific decision actor using the first-party management interface. Shipped parent mode: holder of legitimate venue-rooted management/restart delegation (operator/parent authority) chooses the intervention.
- Supporting / enforcement mechanisms: `VenueAdapter` registry and effective configuration views, `Engine` enable/disable/configure/restart mutations, venue-rooted `adapter/manage` and `venue/restart` capability gates, optional audit log.
- Closure path: Venue-wide current adapter/module/effective-setting view → controller/operator decision → capability-checked `venue/adapter/*`, module or restart invocation → live registry and operation dispatch change → subsequent jobs observe the changed available capability.
- Boundary reachability: `Engine` registers the `VenueAdapter` in the deployed venue; the adapter publishes discovery/configuration and mutation operations with explicit authority checks; changes are applied to the active engine, not only tests or documentation.
- Whole-system current view: `venue/adapters` lists all active/disabled venue adapters plus modules, and `venue/show-config` returns current effective agent/job/storage/access/protocol/limit settings and the active adapter set; it is a whole-venue *capability/configuration* view, not full agent-queue telemetry.
- Current-control decision scope: Site-wide removal/restoration or reconfiguration of offered operations, module membership and runtime process, which controls concurrent services' current capability rather than deciding one task outcome.
- Why this is / is not agent-owned: No standard-distribution autonomous supervisor is wired to consume the entire venue view and make live management decisions. Unlike per-task scheduling, the shipped management path is S3-specific; the first-party operator mode closes the decision, while a constructor must add a different decision owner for base mode.
- Evidence: [`VenueAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/VenueAdapter.java), [`Engine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Engine.java), [`JobManager.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/JobManager.java), [`Audit.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Audit.java)
- Basis: explicit + structural
- Confidence: medium
- Caveats: Operator parent mode depends on explicit venue-rooted delegation, not arbitrary anonymous access. Changes are live-only and reset to operator config after restart. This is current service control, not long-horizon adaptation or identity/ultimate-policy judgment.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | Deployment/application-supplied controller not bundled | Whole-venue adapter/config state and service-control need | First-party `venue/adapters` + management commands expose a specific whole-venue S3 path for composed controller; no autonomous controller shipped | [`VenueAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/VenueAdapter.java), [`Engine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Engine.java) |
| Parent (`P`) | Legitimate venue-rooted management authority/operator | Operator inspects current service composition and decides intervention | Authorized `adapter/manage` or `venue/restart` operation mutates current venue execution/available adapters | [`VenueAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/VenueAdapter.java), [`Engine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Engine.java) |

## S3* — Complementary audit

- State: —
- Function: No independently judged complementary audit with returned corrective regulation is established for the operational venue as a whole.
- Disturbance / variety regulated: Job failures, provider/tool errors, identity abuse and security events are observable, but the separate complementary-control relation is not established.
- Decisive decision or feedback right: No first-party independent auditor with authority to turn a separately obtained finding into corrective current operation.
- Decision owner: No S3* owner established.
- Supporting / enforcement mechanisms: Optional security `Audit` event logger, persisted job results and errors, provider/tool results, capability gates, ordinary status/test/diagnostic infrastructure.
- Closure path: No independent operational audit finding → corrective S3 return loop; event records are emitted, not judged and acted upon by a shipped complementary auditor.
- Why this is / is not agent-owned: The security log records outcomes after events, and validators/tool-result handling are in-path execution feedback. Neither supplies organizationally complementary, independently accessed audit judgment with correction.
- Evidence: [`Audit.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Audit.java), [`VenueAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/VenueAdapter.java), [`JobManager.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/JobManager.java), [`ToolCycleEngine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/ToolCycleEngine.java), [`CapabilityGate.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/lattice/CapabilityGate.java)
- Basis: explicit + structural
- Confidence: high
- Caveats: An external operator or security tool may inspect logs; that unshipped auditor's discretionary closure is not credited to Covia.

### Absence scope

- Surfaces inspected: Security event logger, venue administration audit hooks, job status/failure records, task/tool validation and available test/CI surfaces.
- Plausible first-party paths checked: Independent raw evidence collection, security anomaly audit, model-output verification, corrective intervention by a separately tasked auditor.
- Why no material first-party path remains: No first-party complementary judgment/feedback actor connected to the live S3 decision cycle was found; logs and ordinary execution validation remain support or out-of-band observation.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped organization-level future/environment sensing → capability adaptation option → adopted change loop is established.
- Disturbance / variety regulated: New external provider offerings, future task needs and environmental changes are not evaluated by an S4 organizational process in the deployed venue.
- Decisive decision or feedback right: No first-party prospective strategy/adaptation judgment identified.
- Decision owner: No S4 owner established.
- Supporting / enforcement mechanisms: Session memory and context tools, model-driven subgoal decomposition, scheduled jobs, runtime module loading and live config controls, developer roadmap.
- Closure path: No evidence of prospectively evaluated adaptation options being returned into current capability under a dedicated S4 loop.
- Why this is / is not agent-owned: An agent can adapt its steps within one task and load relevant context; an authorized operator can change today's adapters. Neither entails external/future intelligence creating and returning an organizational adaptation option.
- Evidence: [`GoalTreeAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/GoalTreeAdapter.java), [`LLMAgentAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/agent/LLMAgentAdapter.java), [`AgentAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/AgentAdapter.java), [`VenueAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/VenueAdapter.java), [`Scheduler.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Scheduler.java)
- Basis: structural
- Confidence: medium-high
- Caveats: Module extensibility and prospective R&D may permit later constructed S4 processes but no live first-party closed S4 path is credited.

### Absence scope

- Surfaces inspected: Goal-tree/LLM agent prompts and memory, scheduler, adapter/module reconfiguration, repository plans and deployment documentation.
- Plausible first-party paths checked: Autonomous learning or tool evolution, proposed cross-environment adaptation, forecast-driven strategy, external evaluation → adopted runtime change, operator parent-owned adaptation.
- Why no material first-party path remains: Inspected shipped mechanisms manage present task/context or immediate service availability; the prospective distinction/option-generation/adoption cycle is missing at deployment recursion.

## S5 — Policy and identity

- State: —
- Function: No decisive identity/ultimate-policy deliberation and returned governance loop is established at the deployed venue recursion.
- Disturbance / variety regulated: Principal identities, capabilities, credentials, access grants and effective security settings constrain usage but do not alone resolve identity-level organizational policy.
- Decisive decision or feedback right: No in-boundary ultimate-purpose/identity judgment over competing S3/S4 directions.
- Decision owner: No S5 owner established.
- Supporting / enforcement mechanisms: Venue DID, UCAN/capability delegation, privileged adapter/restart gates, managed user and authentication settings and operator configuration.
- Closure path: No first-party identity/ultimate-policy issue → legitimate deciding authority → resulting doctrine/policy returned to govern later operation is documented.
- Why this is / is not agent-owned: Signing a venue identity and enforcing capabilities proves authentication and policy enforcement; neither is a function-specific ultimate-policy decision. The venue operator's current service controls qualify for S3 only.
- Evidence: [`VenueAdapter.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/adapter/VenueAdapter.java), [`CapabilityGate.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/lattice/CapabilityGate.java), [`Engine.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Engine.java), [`Audit.java`](https://github.com/covia-ai/covia/blob/8838132b99e91fc287ac7b2b4b7125c88e7adef2/venue/src/main/java/covia/venue/Audit.java)
- Basis: structural
- Confidence: medium-high
- Caveats: A real organization's external identity governance could supervise a Covia deployment, but it is not part of the first-party supported operating closure assessed here.

### Absence scope

- Surfaces inspected: Venue DID/authentication, capability/UCAN enforcement, operator-management permissions, runtime config, adjacent project governance.
- Plausible first-party paths checked: Runtime identity decisions, parent ultimate-policy approval and return, S3/S4 conflict adjudication, persistent first-party venue policy adoption.
- Why no material first-party path remains: Credited paths handle authentication/authorization or immediate service controls; a venue-level legitimate ultimate-policy decision with feedback is not implemented in the standard runtime.

## Recursion

Assessment recursion is one self-hosted Covia venue. Shipped resident model-backed agents are operational S1 units for tasks. Independent external grid venues have their own authority and do not donate operating or metasystem decisions to this venue. Nested goal frames, parallel tool calls, DAG nodes and per-user jobs are not independently viable recursive systems merely by topology.

## Variety and escalation

Task variety is absorbed by the model-selected tool/goal loop, constrained by scoped capabilities, job limits, durable lifecycle and fail-fast execution barriers. A venue-authorized parent can review the full adapter/module setting and change current offered capability through the S3 administration channel. Failures/status/security logs remain observability unless a complementary corrective-audit actor is actually evidenced.

## Evidence gaps

This is a source-based, repository-relative classification, not a live benchmark or certification of any deployed grid. Specific future external-S4 programs, complementary external audit programs and project-level governance may exist outside the frozen first-party deployment boundary; hypothetical third-party compositions do not convert bounded absence into `?`. The S3 constructor/parent distinction has medium confidence because its whole-current view focuses on venue-wide capabilities and configuration rather than all in-flight jobs; independent review should specifically challenge whether that scope is enough for S3 at this recursion.
