---
harness_id: flujo
project_name: FLUJO
repository: https://github.com/mario-andreschak/FLUJO
review_ref: 968a495afe85ae93f078738812a0985f615dae71
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: P
---

# FLUJO

## Review boundary

- System in focus: One saved local FLUJO agent or its enduring Persona deployment, including Persona Activities, authored Flow steps, goal supervision and experimentally enabled improvement of the same Behavior.
- Purpose and identity: Deliver configured assistant work under durable owner-set scope and tool authority. Adapt the authored instruction layer to later work when the relevant feature is enabled.
- Relevant environment: Workspace owner, incoming messages and triggers, recurring unfamiliar tasks, configured model endpoints and tools, and persistent task/runtime records.
- Standard-distribution boundary: Shipped Flow/Process engine and model/tool adapters, experimental Persona and Harness Lab paths, administrative runtime APIs and UI. Configured providers supply model inference or tool services.
- Credited operating / distribution surfaces: Flow engine and model handler, Persona dispatcher, goal/work-item state, Role and Behavior revision management, Harness Lab worker and version activation.
- Adjacent first-party surfaces excluded from ownership: Product CI, development and demos as organizational actors, other independent workspaces, unrelated flows/Personas and provider internals.
- First-party operating / deployment modes considered: Saved flows in Talk/API/triggers; one enabled Persona with owner goal controls; opt-in Harness Lab adaptive and manual regression/activation paths.
- Recursion level: One local saved agent work cell or enduring Persona with its authored operation graph. Workspace-wide coordination of independent installations and product governance are outside scope.
- Reviewed revision: 968a495afe85ae93f078738812a0985f615dae71.
- Observation date: 2026-11-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The application runs persisted Process/Static/MCP/Subflow graphs. Model adapters run Process decisions and model-requested tool calls inside the FLUJO action/result protocol. A Persona pins a Role and Behavior revision at admission, then calls the same graph engine with identity, task and bounded tool context. Owner commands can pause, stop and restart a committed ongoing goal. The experimental Harness Lab captures completed interactions, uses separately scoped proposer and evaluator calls on replayed evidence, and can activate an immutable instruction revision for subsequent admissions.

Evidence: [README.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/README.md), [PocketflowEngine.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/execution/flow/engine/PocketflowEngine.ts), [ModelHandler.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/execution/flow/handlers/ModelHandler.ts), [personaDispatcher.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/personaDispatcher.ts), [harness-lab.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/features/harness-lab.md).

## Operational model

The saved Process/Persona owns context-sensitive task work once connected to a model and given authorized tools. A durable goal binds current operations across activity intervals. The owner governs interruption and the mission/Role. A prospective instruction update has its own scoped evaluation and admission lifecycle, with an unattended and a separately supported manual choice path.

## S1 — Operations

- State: A
- Function: Perform the configured user or automation task and choose the next action from returned evidence.
- Disturbance / variety regulated: User requests, tool returns and changing workspace context require task-specific choices.
- Decisive decision or feedback right: Choose the next tool, handoff or response and interpret the resulting evidence.
- Decision owner: Model-backed Process actor inside FLUJO’s packaged flow and tool loop.
- Supporting / enforcement mechanisms: Graph executor, tool registry, model route, authorization constraints, conversation history and Persona Activity dispatch.
- Closure path: Tool results and outputs enter the subsequent model/graph state, which governs continuation and task delivery.
- Boundary reachability: The shipped server runs Process work through its own model handler and flow engine; first-party Persona admission reaches the same path.
- Why this is / is not agent-owned: Tool and graph wiring is support. The model actor supplies semantic choice over the offered actions and their results.
- Evidence: [ModelHandler.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/execution/flow/handlers/ModelHandler.ts), [PocketflowEngine.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/execution/flow/engine/PocketflowEngine.ts), [personaDispatcher.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/personaDispatcher.ts), [running-flows.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/features/flows/running-flows.md).
- Basis: structural
- Confidence: high
- Caveats: Model credentials, tools and an authored flow are deployment inputs; performance under any particular configuration was not measured.

## S2 — Coordination

- State: —
- Function: Check whether the assessed single-cell distribution contains a distinct inter-S1 conflict-attenuation loop.
- Disturbance / variety regulated: Subflow handoffs and Persona Activity ordering can collide at shared runtime state boundaries.
- Decisive decision or feedback right: Resolve specific mutual disturbance among distinct operational units and return a corrective coordination decision.
- Decision owner: No function-specific coordinating owner was evidenced at this recursion.
- Supporting / enforcement mechanisms: Graph edges, subflow communication, per-Persona mailbox ordering, task dependencies and lease fencing.
- Closure path: Subflow responses and completed dependencies return into the same operational plan. The examined paths serialize one cell or execute authored dependencies.
- Why this is / is not agent-owned: Deterministic admission avoids state conflicts. These paths do not establish a separate coordination disposition between independently operating S1 units.
- Evidence: [SUBFLOW_COMMUNICATION.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/SUBFLOW_COMMUNICATION.md), [PocketflowEngine.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/execution/flow/engine/PocketflowEngine.ts), [workItems.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/workItems.ts), [activityRuntime.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/activityRuntime.ts).
- Basis: structural
- Confidence: medium
- Caveats: Optional Meetings spans a different multi-agent configuration. Speaker facilitation or graph routing would require its own interference and feedback witness.

### Absence scope

- Surfaces inspected: Structural and detached subflow paths, one Persona’s mailbox, goal task dependencies and described multi-agent facilitation mode.
- Plausible first-party paths checked: Conflicting live work, handoffs, duplicate task admission, dependency readiness and cross-flow returns.
- Why no material first-party path remains: Scoped paths route a child result, protect one Persona’s state or enforce already authored order. None of the inspected single-cell paths supplies a material coordination judgment between persistent independent operating units.

## S3 — Inside-and-now control

- State: P
- Function: Regulate the current whole Persona goal across ongoing work sessions.
- Disturbance / variety regulated: A stale, blocked or incompatible commitment can continue consuming resources after owner priorities change.
- Decisive decision or feedback right: An authorized owner decides whether the whole ongoing commitment should pause, stop or retry based on its current runtime view.
- Decision owner: Local owner of the assessed Persona.
- Supporting / enforcement mechanisms: Goal/runtime read, visible activity states, version-fenced actions, runtime lock, cancel/reconcile and scheduling.
- Closure path: A persisted version-bound owner decision changes admission, execution or retry of the current goal and later work rounds.
- Boundary reachability: The enabled Persona desk and strict-local control service expose these supported controls to the owning workspace.
- Why this is / is not agent-owned: Routine model reporting and goal task execution provide operational evidence. The operator owns the separately returned supervisory decision.
- Whole-system current view: The goal desk/read path exposes owned goal progress, pending control, active work and associated tasks for the one Persona commitment.
- Current-control decision scope: Interrupt, terminate or re-admit the currently committed goal after inspecting the active work and state.
- Evidence: [persona.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/journeys/persona.md), [persona-goal-control-version.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/persona-goal-control-version.md), [goalRuntimeRead.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/goalRuntimeRead.ts), [goalRuntime.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/goalRuntime.ts), [workItems.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/workItems.ts).
- Basis: structural
- Confidence: medium
- Caveats: A control acknowledgment records intent. Only runtime follow-through proves actual pause/termination. This is not management of all Personas in a workspace.

## S3* — Complementary audit

- State: —
- Function: Test for a complementary first-party check of current Persona operating reports with corrective return.
- Disturbance / variety regulated: A Persona can report success while an outcome or pending goal differs materially.
- Decisive decision or feedback right: Independently inspect the underlying live result, adjudicate the reporting claim and correct current operation.
- Decision owner: No dedicated in-boundary complementary audit actor or constructor was established in the inspected live mode.
- Supporting / enforcement mechanisms: Activity reports, traces, outcome counters, operator views and prospective replay assessment.
- Closure path: Reporting feeds current execution state, and regression metrics can later revert a Behavior. Metrics fold existing Activity outcomes rather than independently verifying their success claims.
- Why this is / is not agent-owned: Source replay judges candidate instructions for prospective activation. Routine instrumentation and count-based aggregation do not independently adjudicate a present operational report.
- Evidence: [personaTools.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/execution/flow/handlers/personaTools.ts), [behaviorOutcome.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/behaviorOutcome.ts), [goalRuntime.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/goalRuntime.ts), [harness-lab.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/features/harness-lab.md), [persona.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/journeys/persona.md).
- Basis: structural
- Confidence: medium
- Caveats: An owner can manually inspect work; the identified built-in evaluator serves prospective changes and is credited under S4.

### Absence scope

- Surfaces inspected: Activity outcome model tool, Behavior regression folding, Goal reconciliation, runtime/tracing views, Harness Lab isolation and demonstrated review.
- Plausible first-party paths checked: Independent check of reported success, automatic rollback and replayed baseline/candidate evaluation.
- Why no material first-party path remains: The regression path relies on reported or terminal Activity records, and held-out replay evaluates potential future instructions. Neither path supplies complementary access and separate adjudication of the current work evidence at this boundary.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: Generate and install future behavior changes from new real tasks and comparative testing.
- Disturbance / variety regulated: The next set of incoming tasks and tool contexts can expose failures of previous authored instructions.
- Decisive decision or feedback right: Generate candidate revisions and judge paired performance, selecting qualified prospective instructions automatically; in a separate supported mode, the owner chooses which eligible evaluated revision to activate or retain.
- Decision owner: Bundled proposer/evaluator actors under configured unattended policy; legitimate Persona/flow owner in the separate manual activation mode.
- Supporting / enforcement mechanisms: Distinct train and held-out inputs, replay isolation, scoring and deterministic eligibility gate, durable versions and compare-and-swap activation.
- Closure path: A passing selected revision replaces the active instruction version for future admissions. Manual activation or rollback updates the same active binding and pauses automation.
- Boundary reachability: The documented, opt-in Harness Lab worker observes deployed conversations/Activities and calls the shipped promotion path. The UI also exposes owner activation and rollback.
- Why this is / is not agent-owned: The proposer/evaluator supply task-sensitive judgments and options under the existing policy. Deterministic gating binds the result. The owner’s manual selection is a distinct binding decision.
- External distinction: Fresh distinct incoming tasks, observed tool states and the workspace contexts that actually occurred.
- Future / prospective distinction: Test a changed instruction template on held-out previously unconsumed cases for better future operational coverage.
- Adaptation option generated: Retain existing instructions or activate a bounded revised prompt as an immutable profile and Behavior version.
- Path back into current capability / S3: Worker or owner version activation moves the live binding. Later admissions pin and use the new version, which can be assessed or rolled back from later evidence.
- Evidence: [harness-lab.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/features/harness-lab.md), [worker.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/harness/worker.ts), [service.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/harness/service.ts), [profiles.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/harness/profiles.ts).
- Basis: structural
- Confidence: medium
- Caveats: Experimental and disabled by default. Probe replay prevents live external effects and does not certify live provider results or general improvement.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Installed model-backed proposer and evaluator under configured policy | New observed distinct tasks and a qualified comparison | Worker activates the eligible version and future dispatch uses it | [worker.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/harness/worker.ts), [service.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/harness/service.ts). |
| Parent (`P`) | Authorized local owner | Owner examines candidate comparisons, release conditions or a problematic active version | Manual activation or rollback writes the binding and changes future admitted work | [harness-lab.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/features/harness-lab.md), [profiles.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/harness/profiles.ts). |

## S5 — Policy and identity

- State: P
- Function: Preserve or revise the Persona’s enduring mission, Role and standing autonomy under human authority.
- Disturbance / variety regulated: New task pressure or adaptive prompts could conflict with the governing scope and identity.
- Decisive decision or feedback right: Determine the durable mission, pin a new Role and revise autonomy/authorization policy for the commissioned cell.
- Decision owner: Authorized Persona owner through the idle-only settings/Role path.
- Supporting / enforcement mechanisms: Workspace ownership checks, version-bound admin mutations, immutable Role and Behavior revisions, pinned dispatch identity, and projection of granted tools.
- Closure path: Owner-approved Role/mission settings and permission context are projected at the next Activity admission and govern subsequent task work.
- Boundary reachability: The shipped Persona desk and update path allow the operator to bind a RoleVersion and update mission/autonomy. Runtime consumes that trusted identity context.
- Why this is / is not agent-owned: Experimental improvement is scoped to authored instructions; the owner's path controls the underlying mission and authority rules.
- Identity / ultimate-policy issue: Decide which long-lived purpose, Role/mission and autonomy envelope the Persona should serve.
- Ultimate authority in each claimed mode: The owner who commissions and controls the Persona.
- Return-to-operation path: Owner update changes durable Role and mission binding; future Persona Activites assemble the pinned instructions and authority when they execute.
- Evidence: [personaAdmin.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/personaAdmin.ts), [personaDispatcher.ts](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/src/backend/services/enduringAgents/personaDispatcher.ts), [enduring-agent-foundation-contracts.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/architecture/enduring-agent-foundation-contracts.md), [harness-lab.md](https://github.com/mario-andreschak/FLUJO/blob/968a495afe85ae93f078738812a0985f615dae71/docs/features/harness-lab.md).
- Basis: structural
- Confidence: medium
- Caveats: A per-tool approval or one process instruction alone is not credited as ultimate policy.

## Distributed OSS parent arrangement

The Persona owner governs the local cell. Project contributors, feature development, release CI and product policy operate at an adjacent recursion.

## Self-hosted and non-human modes

The base Flow loop is shipped. Enduring Personas, goals and Harness Lab require feature enablement and supported connections. The automatic adaptation mode and the informed operator-chosen activation mode share versioning while differing in who selects the change.

## Recursion

The observed level is the single saved agent or Persona. Nested graph actions and externally connected resources are credited only where they close the Persona’s own work.

## Variety and escalation

Runtime scopes tools and admissions, maintains versioned commitments, and returns several types of blockers to the owner. Replay isolates experimental evaluation from real external action while previewing a proposed instruction change.

## Evidence gaps

Read pinned source and tested the assessment artifact only. No deployment, native model execution, longitudinal Persona endurance, live side effects or performance-benefit experiment was independently reproduced. Inter-Persona workspace coordination is outside the declared recursion.
