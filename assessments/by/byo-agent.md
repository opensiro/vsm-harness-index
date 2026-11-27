---
harness_id: byo-agent
project_name: byo-agent
repository: https://github.com/lambeta/byo-agent
review_ref: fde01bea33e93b31ecace32e5f1d656ce454ac25
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# byo-agent

## Review boundary

- System in focus: One installed local byo-agent instance.
- Purpose and identity: A personal assistant that acts on user requests and leaves local artifacts and receipts.
- Relevant environment: A local workspace, one assistant process, configured inference provider and optional external service APIs.
- Standard-distribution boundary: The packaged Python application, command-line and loopback dashboard modes, with first-party tool, memory and trajectory code.
- Credited operating / distribution surfaces: `byo` entry point, CLI/loopback dashboard, Agent, standard tool registry, session/memory and trace paths.
- Adjacent first-party surfaces excluded from ownership: Repository design specs, developer QA/evals and comparison reports. Inference and external services are dependencies.
- First-party operating / deployment modes considered: Interactive CLI and local dashboard, with one model-driven turn operating per assistant request.
- Recursion level: Local assistant instance. Chat sessions are work contexts within that instance.
- Reviewed revision: fde01bea33e93b31ecace32e5f1d656ce454ac25
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The package builds the model adapter, SQLite-backed stores, tool registry and trajectory sink at startup. CLI and dashboard call the same Agent. Each turn binds its starting session, assembles persona/history/recall, runs the provider-neutral tool loop, and records tool decisions, receipt and terminal outcome. A separate consolidation step stores selected conversation facts and episodes. Dashboard endpoints expose history, memory, cost and configuration.

## Operational model

The operational unit is the model-driven assistant performing a user turn over its tool registry. It can deliver a reply, file artifact, calendar entry, stored note or local message draft. It chooses and revises tool actions within the request, while the host enforces tool implementation, workspace restrictions, turn serialization and limits. The user initiates tasks and supplies local settings or preferences.

## S1 — Operations

- State: A
- Function: Carry out a personal-assistant request through workspace and service operations, returning a reply or local artifact.
- Disturbance / variety regulated: Variable user requests, tool results, missing inputs, provider failures and iteration limits.
- Decisive decision or feedback right: Select and revise tool actions from returned results, then produce the terminal result.
- Decision owner: The configured model-backed byo agent owns task-specific tool and answer decisions inside the runtime contract.
- Supporting / enforcement mechanisms: Tool registry, run-loop bounds, workspace tools, recorded results and provider adapters.
- Closure path: Model selects calls; the loop dispatches them and appends tool observations for the next model iteration; the runtime records and returns the final reply and turn state.
- Boundary reachability: The standard CLI/dashboard construct Agent with a concrete registry and adapter, then call the shipped run_loop. The owner does not have to implement a separate agent loop.
- Why this is / is not agent-owned: The model makes the operational choices after observing the effects of its calls. Deterministic tool and limit enforcement bounds those choices.
- Evidence: [byo/app.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/app.py#L50-L101), [byo/app.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/app.py#L152-L189), [byo/loop/agent.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/loop/agent.py#L113-L187), [byo/ops/dashboard.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/ops/dashboard.py#L643-L665)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Configured provider credentials and permissions are prerequisites. A message draft is a local outbox artifact.

## S2 — Coordination

- State: —
- Function: No distinct inter-S1 coordination function is supplied at the installed local-instance boundary.
- Disturbance / variety regulated: Concurrent dashboard requests and a new chat arriving while a turn is active are handled locally.
- Decisive decision or feedback right: No coordination decision across independent operational units was reconstructed.
- Decision owner: Dashboard request lock and session binding maintain consistency for one agent.
- Supporting / enforcement mechanisms: A nonblocking dashboard lock rejects overlapping turns and session capture keeps an in-flight turn attached to its originating chat.
- Closure path: A busy request returns HTTP 409 or a running turn completes in its original session.
- Why this is / is not agent-owned: These mechanisms serialize entry into the same agent and protect its state.
- Evidence: [byo/ops/dashboard.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/ops/dashboard.py#L643-L666), [byo/app.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/app.py#L90-L127), [byo/loop/agent.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/loop/agent.py#L159-L182)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Multiple chats or model calls are present within a local agent instance.

### Absence scope

- Surfaces inspected: CLI/dashboard turn paths, run loop, registry and session switching.
- Plausible first-party paths checked: Separate operational agents, dashboard locking, serial tool calls, and simultaneous session creation.
- Why no material first-party path remains: The shipped path regulates admission to one agent and its state, with no distinct operational work units returning coordination feedback.

## S3 — Inside-and-now control

- State: —
- Function: No whole-current resource or commitment control function was established.
- Disturbance / variety regulated: Turn limits, provider choice, service failures and live task visibility.
- Decisive decision or feedback right: No actor decides a portfolio of live obligations, resources or priorities from a whole-current view.
- Decision owner: Runtime limits bound one turn, and the local operator can save provider configuration.
- Supporting / enforcement mechanisms: Iteration cap, dashboard status, session binding, dotenv settings and turn receipts.
- Closure path: Settings may affect a later launch and limits return a turn outcome.
- Why this is / is not agent-owned: Individual turn intervention and settings lack a current resource or commitment control loop at this recursion.
- Evidence: [byo/app.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/app.py#L163-L189), [byo/app.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/app.py#L203-L237), [byo/ops/dashboard.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/ops/dashboard.py#L469-L484), [byo/ops/dashboard.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/ops/dashboard.py#L643-L666)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: The dashboard is an operator surface for the local agent.

### Absence scope

- Surfaces inspected: Agent respond, dashboard live/chat/settings, single-turn loop and receipts.
- Plausible first-party paths checked: Current supervisor/portfolio path, busy-turn enforcement, and human resource or priority intervention.
- Why no material first-party path remains: Available intervention and budget signals remain at turn or configuration level. No operating portfolio decision is fed back.

## S3* — Complementary audit

- State: —
- Function: No complementary audit function was established.
- Disturbance / variety regulated: The local operator can examine model and tool histories, costs, and memory outcomes.
- Decisive decision or feedback right: No independent operating-evidence query and returned intervention path over a current-control representation is supplied.
- Decision owner: The turn and tooling produce the events that the dashboard summarizes.
- Supporting / enforcement mechanisms: The JSONL trajectory, receipt, observability projection and memory change log.
- Closure path: Events can be read in the dashboard, with the underlying event source shared across views.
- Why this is / is not agent-owned: The observation paths report the same operating stream. No separate decision authority checks an operational management claim.
- Evidence: [byo/app.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/app.py#L121-L149), [byo/app.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/app.py#L175-L189), [byo/ops/trajectory.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/ops/trajectory.py#L74-L125), [byo/ops/observability.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/ops/observability.py#L34-L108), [byo/ops/dashboard.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/ops/dashboard.py#L197-L204)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Deterministic evals are development evidence.

### Absence scope

- Surfaces inspected: Live dashboard, turn details, receipt events, memory curation and packaged deterministic eval surfaces.
- Plausible first-party paths checked: Independent access to outcomes, off-channel audit authority and corrective return into current control.
- Why no material first-party path remains: The available read paths expose the same in-turn event stream or directly edit facts. Neither supplies complementary operational audit.

## S4 — Outside-and-then intelligence

- State: —
- Function: No outside-and-then intelligence function was established.
- Disturbance / variety regulated: New external query facts, growing dialogue history and changed owner preferences.
- Decisive decision or feedback right: No owner compares prospective capabilities against environmental change and adopts a corresponding operating change.
- Decision owner: The active agent searches within a request, memory summarizes prior transcripts, and the operator can edit facts/settings.
- Supporting / enforcement mechanisms: Web search, semantic/episodic memory consolidation and persistent persona.
- Closure path: Facts and persona may shape future turns as operating context.
- Why this is / is not agent-owned: These paths retrieve information, preserve memory and carry preferences forward within the established assistant capability.
- Evidence: [byo/app.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/app.py#L59-L100), [byo/app.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/app.py#L191-L219), [byo/memory/consolidation.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/memory/consolidation.py#L62-L116), [byo/runtime/session.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/runtime/session.py#L71-L96), [byo/tools/memory_admin.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/tools/memory_admin.py#L51-L71)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Persisted memory can materially affect replies.

### Absence scope

- Surfaces inspected: Search wiring, memory retrieval/consolidation, dashboard settings and the persona tool.
- Plausible first-party paths checked: Environmental intelligence, future options, human-adopted capability changes and prospective feedback.
- Why no material first-party path remains: Search is request-bound and configuration or memory updates have no prospective evaluation and adoption loop for capability strategy.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity or policy settlement loop was established at the installed-instance recursion.
- Disturbance / variety regulated: The user's standing preferences and the default personal-assistant behavior can differ.
- Decisive decision or feedback right: The shipped persona tool replaces text; it does not decide constitutional authority or settle ultimate policy conflicts.
- Decision owner: The local owner may specify standing instructions and the agent may apply the text write. Fixed runtime rules remain separately injected.
- Supporting / enforcement mechanisms: PERSONA.md, backup on updates, and system-prompt assembly.
- Closure path: Persona replacement changes the next turn's context while the shipped rule layer remains in the prompt.
- Why this is / is not agent-owned: Persistent instructions are an operating configuration surface. No recognized policy adjudication and return is supplied for conflicts over the assistant's purpose or ultimate authority.
- Evidence: [byo/config.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/config.py#L135-L137), [byo/runtime/session.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/runtime/session.py#L22-L53), [byo/runtime/session.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/runtime/session.py#L71-L96), [byo/tools/memory_admin.py](https://github.com/lambeta/byo-agent/blob/fde01bea33e93b31ecace32e5f1d656ce454ac25/byo/tools/memory_admin.py#L51-L71)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: A human can configure the instance independently of repo maintainers.

### Absence scope

- Surfaces inspected: Default and persistent persona, owner-directed installation settings, and the persona update tool.
- Plausible first-party paths checked: Agent or parent resolution of identity/policy issues, including the closest persistent-persona path.
- Why no material first-party path remains: Prompt replacement is a configuration action under the same runtime constraints. The shipped path confers no decisive identity/policy adjudication right.

## Recursion

User requests and tool actions are internal steps of one local assistant arrangement. CLI and dashboard are entry points. Provider and service dependencies are outside that operating recursion.

## Variety and escalation

Tool errors and outputs re-enter the turn, and model failure or a bounded stop returns a visible outcome. The dashboard discloses turn cost and traces. No exceptional signal that bypasses an organizational hierarchy is evidenced.

## Evidence gaps

Source review only. Provider sessions and external tools were not run. No claim is made about performance, safe handling of arbitrary tool input, or instances composed outside the shipped modes.
