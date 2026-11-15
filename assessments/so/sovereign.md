---
harness_id: sovereign
project_name: Sovereign
repository: https://github.com/HexaField/sovereign
review_ref: a485bb260556b11140606f6de194459902a9977c
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: P
---

# Sovereign

## Review boundary

- System in focus: A self-hosted Sovereign development operation with one assessed repository work portfolio, agent sessions and the configured Forge work graph.
- Purpose and identity: Carry out development work while keeping worker sessions and external issue and change state coherent.
- Relevant environment: Workspaces, forge repositories, user decisions, supported model services and optional local integrations.
- Standard-distribution boundary: Server and client, installed agent backend, task and Forge services, event bus, worktree tooling and operating configuration.
- Credited operating / distribution surfaces: Native Claude SDK sessions, Forge Rethink, task and workstream services, workspace operator controls and personality compiler.
- Adjacent first-party surfaces excluded from ownership: Repository-maintainer CI, evaluations, design plans without runtime wiring and test fixtures. External forge and model services supply observations or execution infrastructure.
- First-party operating / deployment modes considered: Agent-enabled self-hosting with configured Forge and the operator-driven work graph, ambient presence and scheduled execution.
- Recursion level: One configured development portfolio, its working threads and their subagents. The installation operator owns the parent role.
- Reviewed revision: a485bb260556b11140606f6de194459902a9977c
- Observation date: 2026-11-15
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The [server composition](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/server/src/bootstrap.ts) wires the config store, agent backend, task service and Forge Rethink runner through the event bus. The standard backend runs Claude SDK sessions, with configured alternative backends available. Tasks and workstreams connect to current forge observations and local plans. Rethink receives a scoped digest and sends corrective work to an owning thread. A separate presence module delivers contextual events to an ambient session.

## Operational model

Agent threads and managed subagents investigate, edit and check code and produce a result. The portfolio spans open changes, proposed work and active owners. Rethink's model-backed turn can decide dependency or ownership adjustments and which existing thread should act next. The operator can inspect the same work graph and direct portfolio commitments through its controls.

## S1 — Operations

- State: A
- Function: Deliver code and investigation results from workspace assignments.
- Disturbance / variety regulated: Variability in repository state, tool output and work context.
- Decisive decision or feedback right: Select current tool actions and edits and return a reasoned outcome.
- Decision owner: The running SDK agent in a working thread or subagent session.
- Supporting / enforcement mechanisms: The native SDK loop, context and tool setup, durable per-session state and worker result delivery.
- Closure path: A task or event reaches a session, the agent acts on workspace evidence and the turn or subagent outcome returns to the calling thread and UI.
- Boundary reachability: The self-hosted composition supplies the SDK backend and standard worker spawn path with the configured account.
- Why this is / is not agent-owned: The agent chooses workspace actions and responds to actual tool results.
- Evidence: [Backend selection](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/agent-backend/src/wiring.ts#L374-L437), [SDK session setup](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/agent-backend/src/claude-code/claude-code.ts#L1397-L1461), [worker lifecycle](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/agent-backend/src/claude-code/claude-code.ts#L2897-L2958).
- Basis: Pinned source.
- Confidence: High.
- Caveats: A supported model backend is needed for this mode.

## S2 — Coordination

- State: A
- Function: Attenuate conflicting or duplicate work across separate portfolio owners.
- Disturbance / variety regulated: A stacked change can advance before its prerequisite, and one thread can reopen work another thread already covers.
- Decisive decision or feedback right: Decide which live changes must wait for another and whether an opened change supersedes a planned assignment.
- Decision owner: The installed Rethink agent in its configured Forge mode.
- Supporting / enforcement mechanisms: Work graph digest, ownership overlays, dependency edges with cycle checks, supersede action and blocked-state projection.
- Closure path: Forge and local task observations reach Rethink. It records or removes a dependency and can cancel superseded planned work. Updated blocked, cancelled and ownership states feed later task selection.
- Boundary reachability: The server creates the Rethink runner and exposes the scoped tools to its dedicated agent thread.
- Distinct S1 units: Separate owning threads working on repository items across the assessed portfolio.
- Inter-S1 disturbance: Cross-thread dependency interference and duplicated planned and active work.
- Attenuating coordination relation: Agent-selected wait-for relations and retirement of planned items already covered by a live change.
- Feedback into subsequent S1 behaviour: Later portfolio work uses the accepted dependency and supersession state when selecting tasks and routing them to owners.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Dependency and supersession operations act on identified clashes between independently owned work.
- Why this is / is not agent-owned: The Rethink agent judges whether a specific dependency or duplicate exists and applies the graph action.
- Evidence: [Rethink intervention instructions](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/rethink.ts#L146-L223), [dependency updates](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/rethink.ts#L983-L1007), [blocked projection](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/tree.ts#L22-L58).
- Basis: Pinned source, installed prompt and persisted graph transitions.
- Confidence: Medium.
- Caveats: The dependency projection informs coordination. A universal worker-level lock is outside this witness.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate current portfolio ownership, active commitments and corrective work.
- Disturbance / variety regulated: Failing checks, blocked agents, ownerless work, and priorities changing in the current portfolio.
- Decisive decision or feedback right: Choose interventions and commit in-scope worker capacity, or change current assignments and stream state as an operator.
- Decision owner: The Rethink agent in the activated mode. The installation operator in manual Forge operation.
- Supporting / enforcement mechanisms: Work graph, portfolio digest, current owner overlays, dispatch limits, assignment tools, pause and progress state.
- Closure path: Rethink sends a corrective prompt to an owner or starts an eligible change's owning thread. The reports and task-state changes return to the next view. In manual mode the operator changes assignment and stream or item state through the same operational service.
- Boundary reachability: The server binds both the Rethink thread and the operator graph routes to the running Forge service.
- Whole-system current view: The configured portfolio's workstreams, planned items, current ownership, active changes and newly significant events.
- Current-control decision scope: Decide which work receives an owner or an intervention, and which current items or workstreams pause or resume.
- Why this is / is not agent-owned: The Rethink agent chooses the portfolio intervention in its mode. The operator exercises current-control discretion through the manual work graph.
- Evidence: [Runtime binding](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/server/src/bootstrap.ts#L977-L1084), [returned dispatch](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/rethink.ts#L780-L855), [manual routes](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/routes.ts), [assignment state and prompt return](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/service.ts#L1370-L1400).
- Basis: Source-backed decision and return paths.
- Confidence: Medium.
- Caveats: The result is relative to the configured scoped portfolio. Per-run limits constrain agent discretion.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Forge Rethink agent | New unresolved portfolio events reach the configured digest | Agent decides what to dispatch, resolve or escalate. The receiver starts or redirects work and the report becomes part of the portfolio state. | [Digest prompt and action rules](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/rethink.ts#L146-L223) |
| Parent (`P`) | Work portfolio operator | Live graph or unresolved decision calls for changed commitments | Operator assigns work to a thread or pauses a stream or item. The resulting state governs dispatch and the graph shown to the team. | [Assignment and pause operation](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/service.ts#L1370-L1400), [pause return](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/service.ts#L1456-L1466) |

## S3* — Complementary audit

- State: ?
- Function: Independently inspect the evidence behind an operational claim and return the result to current control.
- Disturbance / variety regulated: A change's reported state can diverge from actual checks or code evidence.
- Decisive decision or feedback right: Sample independent evidence, form an audit judgment and return that judgment to the portfolio owner.
- Decision owner: Unresolved for a first-party audit mode.
- Supporting / enforcement mechanisms: Forge CI and review inputs, review cache, raw check lookups and a distinct Rethink session that may dispatch corrections.
- Closure path: Current forge observations demonstrably return to operations. A specific complementary claim-and-verdict audit path requires further evidence.
- Why this is / is not agent-owned: Rethink selects responses to review and check evidence. The source reconstruction leaves uncertain whether it closes an audit function beyond routine reactive control.
- Evidence: [Forge observation and work graph](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/service.ts), [Rethink evidence inputs and actions](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/rethink.ts#L167-L223).
- Basis: Review of the strongest shipped review and check paths.
- Confidence: Medium.
- Caveats: A separate SDK session alone does not establish a complementary audit.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Convert anticipated external change into durable changes in capabilities or strategy.
- Disturbance / variety regulated: Changing project conditions or external demands can alter the portfolio's future capabilities.
- Decisive decision or feedback right: Choose a prospective adaptation and return it to the operating portfolio.
- Decision owner: Unresolved in the assessed mode.
- Supporting / enforcement mechanisms: Forge event sensing and categorization, editable future epics, ambient external input and persistent user instructions.
- Closure path: Epic and context changes can persist. The assessed sources leave open whether a supported mode uses prospective sensing to choose and return a capability adaptation.
- Why this is / is not agent-owned: Rethink can change planned streams and react to current external events. The link to a prospective adaptation decision remains unresolved.
- Evidence: [Epic refinement input and durable actions](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/rethink.ts#L284-L310), [refinement session dispatch](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/work-graph/src/rethink.ts#L1067-L1075), [ambient operating mode](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/presence/src/module.ts).
- Basis: Comparison of prospective and current operating paths.
- Confidence: Medium.
- Caveats: Hardware/service scheduling and periodic PR polling are ordinary operational support.

## S5 — Policy and identity

- State: P
- Function: Set and return the enduring identity and instruction boundary of the deployed agent operation.
- Disturbance / variety regulated: The operator may revise the deployment's persistent intent and instruction sources as the work portfolio changes.
- Decisive decision or feedback right: Choose the governing files and contents for the installation's agent identity, and set the configuration that binds them to future work.
- Decision owner: The operator maintaining the deployment's personality and scoped context.
- Supporting / enforcement mechanisms: Runtime configuration, manifest watcher, compiler and SDK session context loader.
- Closure path: Operator-selected identity and instruction files compile into the persistent personality. Later main agent sessions read and apply the resulting context.
- Boundary reachability: The server initializes and watches the compiler, and the standard SDK backend reads its output when opening an agent session.
- Identity / ultimate-policy issue: Which enduring operational identity and instruction sources govern the installed agent across assignments.
- Ultimate authority in each claimed mode: The installation operator owns the governing source files and manifest.
- Return-to-operation path: Configuration and source changes trigger recompilation into the prompt that subsequent parent sessions receive.
- Why this is / is not agent-owned: Compiler and loader apply the operator's identity decision. Agent turns operate under the resulting prompt.
- Evidence: [Operator personality compilation and watch](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/server/src/bootstrap.ts#L351-L377), [configuration write route](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/config/src/routes.ts#L49-L57), [operating prompt binding](https://github.com/HexaField/sovereign/blob/a485bb260556b11140606f6de194459902a9977c/packages/agent-backend/src/claude-code/claude-code.ts#L1397-L1424).
- Basis: Pinned source showing the operator-to-runtime return.
- Confidence: Medium.
- Caveats: SDK subagents receive their specific subagent and repository instructions. This witness concerns enduring identity in the controlling workspace agent.

## Recursion

The assessed portfolio contains separate working threads and delegated worker sessions. Rethink sees the joined state within a configured scope. The deployment operator sets binding identity and intervenes on work portfolios through the available controls.

## Variety and escalation

The event digest filters a changing flow of work and updates. Rethink has bounded dispatch and a user decision path for items requiring parent judgement.

## Evidence gaps

The assessment reconstructs paths from the pinned source. It does not depend on a live model run. Complementary audit under the external review modes and a prospective environment-to-capability feedback loop remain open evidence questions.
