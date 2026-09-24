---
harness_id: cascaide-ts
project_name: cascaide-ts
repository: https://github.com/Airavat-Research/cascaide-ts
review_ref: 08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7
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

# cascaide-ts

## Review boundary

- System in focus: one first-party Cascaide cascade/workflow organization at pinned revision `08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7`, including the reusable `@cascaide-ts/core` graph executor and the shipped `@cascaide-ts/helpers` agent factories that directly instantiate model/tool agent loops on that executor.
- Purpose and identity: execute agent and application workflows as observable, optionally durable graphs that can cross client/server execution boundaries while preserving cascade state, node lifecycle and model/tool feedback.
- Relevant environment: user/application objectives; external model-provider endpoints; application-supplied tools and business systems; client/UI nodes; optional persistence/database infrastructure; and application code that defines the concrete graph and node semantics.
- Standard-distribution boundary: first-party core workflow state, server/client listener middleware, controller, persistence/hydration hooks, provider-stream normalization and official helper agent factories are inside. External model APIs, application tools, application-authored graph semantics and database services remain dependencies or downstream specialization and do not donate organizational functions.
- Credited operating / distribution surfaces: `packages/core/src/controller.ts`; `packages/core/src/middlewares/serverWorkflowListenerMiddleware.ts`; `packages/core/src/middlewares/clientWorkflowListenerMiddleware.ts`; `packages/core/src/middlewares/serverPersistenceMiddleware.ts`; `packages/core/src/middlewares/serverHydrationMiddleware.ts`; `packages/core/src/workflowSlice.ts`; `packages/core/src/types.ts`; `packages/helpers/src/agent/createAgent.ts`; `packages/helpers/src/agent/types.ts`.
- Adjacent first-party surfaces excluded from ownership: CLI-generated/scaffolded demo applications and their domain-specific graphs/HITL flows; repository-development CI/release/contributor activity; framework presentation adapters except where they corroborate the standard execution boundary; documentation and examples used only as supporting evidence.
- First-party operating / deployment modes considered: standard ReAct agent factory; recursive ReAct self-delegation; named-sub-agent Supervisor and recursive Supervisor factories; custom graph nodes executing through the same core listener; client/UI node handoff; durable claim/finalize/context persistence, cold-start hydration and cascade fork/time-travel primitives.
- Recursion level: one Cascaide cascade is the primary system-in-focus. Model-driven agent instances or delegated child cascades may be operational S1 units when they directly perform the cascade's work. Recursive graph/subcascade topology is not treated as recursive viability by itself.
- Reviewed revision: `08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Cascaide describes itself as a distributed, observable, durable graph executor. The core runtime keeps workflow context, active-node state, history and errors in a Redux-style store. `setupServerWorkflowListener()` reacts to an active node by resolving its graph definition, running `prep` → `exec` → `post`, persisting context updates, spawning returned follow-on nodes, handling streaming provider output, recording error/completion state and handing execution across the client/server boundary when needed. The controller exposes generic state/read/write primitives such as `spawn`, `updateContext`, `waitUntil`, `getCascadeState`, `getCascadeNodes` and `fork`.

The official helpers package supplies the first-party autonomous operating loop. `createReactAgent()` and its variants build an agent node plus a tool node. The agent node invokes the configured model provider with current history and declared tools. If the model returns tool calls, the post step spawns the tool node; the tool node executes those tools, records results and spawns the agent node again so the returned observations enter the next model decision. Recursive and Supervisor variants add model-visible delegation tools. `delegateToSubAgents()` spawns child cascades, waits for them to complete and returns their final outputs as tool results to the parent model.

Those delegation surfaces do not, by themselves, establish higher VSM functions. The recursive helper tells the model to use self-delegation for independent subtasks, and the Supervisor turns named sub-agents into tools, but the reusable runtime does not identify a concrete inter-S1 conflict/oscillation or return a coordination decision specifically aimed at attenuating one. Likewise, the Supervisor receives completed child outputs rather than a packaged whole-cascade current-control view; task assignment and sequential delegation remain task decomposition unless downstream code adds stronger organizational semantics.

Durability and observability are substantial. The persistence middleware claims node execution, finalizes nodes, records context events and errors, while hydration can restore or fork a cascade at a selected function id. These mechanisms preserve and replay operational state. They do not provide an independent audit judgment, an external/future adaptation loop or an identity/ultimate-policy authority merely because they make history inspectable or forkable.

Primary evidence:

- [`packages/core/src/middlewares/serverWorkflowListenerMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/serverWorkflowListenerMiddleware.ts) — first-party node execution, streaming, state update, spawning, completion/error and checkpoint handoff.
- [`packages/core/src/controller.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/controller.ts) — generic cascade control/read surface.
- [`packages/helpers/src/agent/createAgent.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/helpers/src/agent/createAgent.ts) — packaged ReAct model/tool loop, recursive delegation and Supervisor variants.
- [`packages/helpers/src/agent/types.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/helpers/src/agent/types.ts) — model/system/tool/sub-agent configuration and helper factory boundary.
- [`packages/core/src/middlewares/serverPersistenceMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/serverPersistenceMiddleware.ts) — durable node claims, completion, error and context-event persistence.
- [`packages/core/src/middlewares/serverHydrationMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/serverHydrationMiddleware.ts) — cold-start restore and fork/hydrate path.
- [`packages/core/src/workflowSlice.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/workflowSlice.ts) — current context, active-node, history and error state.
- [`README.md`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/README.md) and [`packages/core/README.md`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/README.md) — supported runtime, helper and durability boundaries.

## Operational model

A Cascaide application adds an active node with context. The core listener resolves that node's first-party graph definition and executes its `prep`, `exec` and `post` stages. Post results can update cascade context and spawn additional nodes, while active-node state determines when the stream/run is complete. In durable mode, node claims, context events, completion and errors are persisted so later execution can hydrate prior state or fork from a prior function boundary.

For a helper-built ReAct agent, the active node invokes a model provider with conversation history and model-visible tools. A terminal model answer completes the agent path. A tool decision instead spawns the paired tool node; direct tools or delegated sub-cascades execute, their results are added to history, and the paired agent node is spawned again. The same first-party graph executor therefore closes the model → action/delegation → observation → next-model-turn loop.

## S1 — Operations

- State: A
- Function: perform goal-directed agent work through repeated model decisions, tool/delegation actions and returned observations within a Cascaide cascade.
- Disturbance / variety regulated: user/application requests, evolving conversation history, model uncertainty, tool/sub-agent outputs and errors, provider responses and the local state needed to decide whether to act again or complete.
- Decisive decision or feedback right: choose the next substantive answer, direct tool call, self-delegation or named-sub-agent delegation from the current model-visible context and incorporate returned results into the next turn.
- Decision owner: the model-driven agent actor invoked through the first-party helper-built agent node.
- Supporting / enforcement mechanisms: core node lifecycle, workflow context, provider adapters, tool-node execution, child-cascade spawning/waiting, recursion depth guard, streaming normalization, active-node tracking, optional persistence/hydration and client/server relay.
- Closure path: cascade input/history → helper agent node → provider-backed model decision → answer or Tool/delegation call → first-party tool node executes the selected action/subcascade → tool result is appended to cascade history → helper respawns the agent node → model receives the observation and decides again or terminates.
- Boundary reachability: `@cascaide-ts/helpers` is a shipped package explicitly documented as providing `createReactAgent`, `createRecursiveReactAgent`, `createSupervisorAgent` and `createRecursiveSupervisorAgent`; those generated nodes execute directly through the documented `@cascaide-ts/core` engine rather than through a repository-development example path.
- Why this is / is not agent-owned: Cascaide's deterministic graph executor transports, persists and bounds the loop, while the model actor chooses substantive next actions from the current history and declared capabilities. External providers supply inference but are directly invoked as the actor in the first-party operating path.
- Evidence: [`createAgent.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/helpers/src/agent/createAgent.ts); [`serverWorkflowListenerMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/serverWorkflowListenerMiddleware.ts); [`packages/helpers/README.md`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/helpers/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the application chooses the model, system prompt, direct tools and optional sub-agent catalog. Those constructor inputs bound S1 but do not move the turn-level action decision out of the model actor once the standard helper runtime is executing.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination function is established at the declared cascade recursion.
- Disturbance / variety regulated: parallel or delegated S1 units could in principle overlap, conflict or oscillate, but the reviewed standard distribution does not identify a concrete sibling-interference mode and close a response specifically intended to damp it.
- Decisive decision or feedback right: none established for inter-S1 conflict/oscillation attenuation.
- Decision owner: none established.
- Supporting / enforcement mechanisms: `delegateToSubAgents()` can spawn several child cascades and wait for them; recursive delegation is described for independent subtasks; `activeNodes` tracks concurrent work; persistence claims prevent duplicate execution of a node instance.
- Closure path: no first-party disturbance-specific coordination judgment was found that returns a conflict/oscillation attenuation decision into subsequent behavior of multiple S1 units.
- Why this is / is not agent-owned: the parent model may choose subtasks or named sub-agents, but delegation and task decomposition are not S2 by themselves. `spawn`, `waitUntil`, active-node bookkeeping and node claiming transport/order execution without selecting a coordination response to a evidenced inter-S1 disturbance.
- Evidence: [`createAgent.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/helpers/src/agent/createAgent.ts); [`controller.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/controller.ts); [`serverPersistenceMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/serverPersistenceMiddleware.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: downstream graph/node code could use the generic controller to implement a domain-specific coordination mechanism, but a universal extension surface is not itself an S2 constructor path without function-specific interference and closure evidence.

### Absence scope

- Surfaces inspected: recursive ReAct delegation, Supervisor/named-sub-agent delegation, `CascadeController.spawn`/`waitUntil`, active-node state, server/client workflow listeners and persistence node claiming.
- Plausible first-party paths checked: parent decomposition into concurrent subtasks; parallel sub-cascade execution; generic graph sequencing; duplicate-node execution prevention; client/server execution handoff.
- Why no material first-party path remains: these mechanisms create or transport plurality and ordering, but none is tied to a concrete inter-S1 conflict/oscillation with an organizational coordination decision that changes later sibling behavior.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-cascade current-control function with agent-owned authority is established.
- Disturbance / variety regulated: current whole-cascade commitments, competing priorities, resource constraints or local-vs-global operational exceptions would require a metasystemic current view and intervention right, but the packaged agent paths do not provide that relation.
- Decisive decision or feedback right: none established over current resources, commitments, priorities or constraints for the cascade as a whole.
- Decision owner: none established.
- Supporting / enforcement mechanisms: `WorkflowState` exposes context/active nodes/history/errors; `CascadeController` can read state, spawn nodes, wait and fork; the Supervisor model can delegate to configured sub-agents and receives their completed outputs as tool results; execution-time buffering can checkpoint remaining graph work.
- Closure path: no packaged path was found in which an agent receives a whole-cascade current operational view, chooses a current-control intervention over the organization as a whole and returns that decision into runtime state.
- Why this is / is not agent-owned: Supervisor delegation remains task allocation. The standard Supervisor receives completed child results, not a first-party live whole-system current-control view. Generic controller state/read/write methods are handed to node/tool implementation code and can support downstream specialization, but they do not define or own an S3-specific decision right.
- Evidence: [`createAgent.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/helpers/src/agent/createAgent.ts); [`controller.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/controller.ts); [`workflowSlice.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/workflowSlice.ts); [`serverWorkflowListenerMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/serverWorkflowListenerMiddleware.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: an application may deliberately expose controller state and intervention tools to a model or human manager, but that would be a separate downstream organization requiring its own evidence rather than an inherited S3 state for the reusable base runtime.

### Absence scope

- Surfaces inspected: Supervisor and recursive Supervisor factories; workflow context/active-node/history/error state; controller read/write/spawn/wait/fork methods; time-buffer checkpoint handoff; persistence lifecycle.
- Plausible first-party paths checked: named-sub-agent routing; model-selected delegation; global state getters; active-node completion tracking; node failure state; durable execution continuation.
- Why no material first-party path remains: no standard metasystem actor is wired to a whole-system current view with authority to revise resource/commitment/priority decisions; the exposed controller is generic application infrastructure and delegation remains task decomposition.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit function is established.
- Disturbance / variety regulated: operational claims could require evidence beyond ordinary agent output/history, but the standard runtime does not add an independent challenge path over those claims.
- Decisive decision or feedback right: none established for independent audit judgment.
- Decision owner: none established.
- Supporting / enforcement mechanisms: durable context events, node history/errors, full audit trails described for durable mode, provider-stream canonicalization, cascade hydration and fork/time-travel.
- Closure path: no first-party path was found from complementary evidence or independent challenge → audit finding → downstream corrective current control.
- Why this is / is not agent-owned: persistence and replay improve observability and reconstructability, but they record the ordinary execution path. Forking a prior state permits alternative execution but supplies no independent auditor, distinct evidence channel or corrective audit authority by itself.
- Evidence: [`serverPersistenceMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/serverPersistenceMiddleware.ts); [`serverHydrationMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/serverHydrationMiddleware.ts); [`persistence.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/persistence.ts); [`README.md`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: downstream applications can build reviewers or validators as ordinary graph nodes, but no packaged independent audit relation with complementary access and corrective closure is owned by the reusable runtime.

### Absence scope

- Surfaces inspected: persistence claims/events/history/errors, hydration, cascade forking, durable audit-log claims, graph history and client/server canonical/UI state separation.
- Plausible first-party paths checked: replay/time travel; recorded node outputs; errors; forked execution; UI filtering versus canonical history.
- Why no material first-party path remains: all inspected evidence remains ordinary execution provenance or replay machinery; no independent challenge path with materially different access to operational reality and a correction loop is wired into the standard runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-future adaptation function is established.
- Disturbance / variety regulated: changing external conditions, opportunities, threats or future capability needs are not modeled by a packaged prospective adaptation loop.
- Decisive decision or feedback right: none established for generating and selecting future-oriented adaptation options from external distinctions.
- Decision owner: none established.
- Supporting / enforcement mechanisms: cascade history/context persistence, hydration, forking/time travel, recursive delegation and application-definable graph transitions.
- Closure path: no first-party external/future sensing → adaptation-option generation → return into current capability/control path was found.
- Why this is / is not agent-owned: durable state and forkable histories concern preservation/replay of current or past execution. Recursive delegation and graph evolution during a task remain operational/current regulation unless evidence establishes prospective environmental modeling and capability adaptation.
- Evidence: [`serverHydrationMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/serverHydrationMiddleware.ts); [`controller.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/controller.ts); [`workflowSlice.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/workflowSlice.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: the generic graph can host research/adaptation agents supplied by an application, but those are downstream semantics rather than a first-party S4 constructor relation in the reviewed base distribution.

### Absence scope

- Surfaces inspected: durable context/history, fork and hydrate, recursive agent helpers, generic graph/node extension API and provider/model interfaces.
- Plausible first-party paths checked: time travel/counterfactual fork; recursive self-delegation; persisted learning-like state; dynamic follow-on node spawning.
- Why no material first-party path remains: none combines external/future-relevant distinctions with development of adaptation options and a return path into current capability; persistence and runtime replanning-by-graph are not sufficient by themselves.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the cascade recursion.
- Disturbance / variety regulated: identity-level conflicts or unresolved S3–S4 policy tensions have no packaged escalation/decision path in the reusable runtime.
- Decisive decision or feedback right: none established for legitimate ultimate-policy or identity decisions.
- Decision owner: none established.
- Supporting / enforcement mechanisms: application-provided `systemPrompt`, model/tool/sub-agent configuration, UI-node/HITL construction capability, provider filters and generic graph controls.
- Closure path: no identity/policy issue → legitimate ultimate authority → decision → subsequent-operation governance path was found.
- Why this is / is not agent-owned: prompts and configuration constrain behavior but do not themselves exercise runtime identity authority. Human interaction can be implemented as a client/UI node, including in scaffolded applications, but generic task-level HITL does not establish S5 and the reusable base does not define an ultimate-policy escalation relation.
- Evidence: [`packages/helpers/src/agent/types.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/helpers/src/agent/types.ts); [`clientWorkflowListenerMiddleware.ts`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/packages/core/src/middlewares/clientWorkflowListenerMiddleware.ts); [`README.md`](https://github.com/Airavat-Research/cascaide-ts/blob/08fc10fcd58ecf729b9b0c5c1f0c135f7bb723f7/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a downstream application may define identity/policy-specific human or agent nodes. Such a specialization is a separate system-in-focus and cannot donate S5 to the reusable Cascaide constructor/runtime.

### Absence scope

- Surfaces inspected: helper `systemPrompt` and agent configuration; model/tool/sub-agent declarations; client/UI node dispatch; README-described HITL scaffold; controller/runtime lifecycle.
- Plausible first-party paths checked: human UI nodes; tool/sub-agent configuration; system prompts; application-defined workflow gates.
- Why no material first-party path remains: the standard distribution provides mechanisms for constraints and human interaction but no identity/ultimate-policy issue classification, legitimate ultimate authority or return-to-operation policy closure.