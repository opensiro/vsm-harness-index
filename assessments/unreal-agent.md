---
harness_id: unreal-agent
project_name: Unreal Agent
repository: https://github.com/unreallabsai/unreal-agent
review_ref: b7c9bf1c5c2fa4127255c07727a7c8413e23944a
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Unreal Agent

## Review boundary

- System in focus: one shipped Unreal Agent runtime/session at pinned revision `b7c9bf1c5c2fa4127255c07727a7c8413e23944a`, including the first-party harness library and `unreal-agent-runner`: coordinator/event loop, inbox, context builder, LLM adapter boundary, tool registry/translators, append-only session store, durable operation manager and the standard Bash/ViewImage/SkillUse execution path.
- Purpose and identity: execute a caller-supplied goal as an autonomous asynchronous agent session, allowing the model to choose tool actions, continue from tool feedback, persist/recover session state and stop when the goal-directed loop becomes idle.
- Relevant environment: human or API caller; caller-supplied prompt/messages and system prompt; workspace/filesystem and shell environment; configured model provider; tool/skill inputs; asynchronous operation results; process interruption/restart; optional downstream embeddings of the harness interfaces.
- Standard-distribution boundary: the repository-shipped Go harness packages and executable runner with their normal provider/tool/session wiring. External model providers, caller-owned prompts/workspaces, shell programs and any downstream remote operation executor are dependencies/environment; their internal organizational functions are not inherited.
- Credited operating / distribution surfaces: `README.md`; `cmd/internal/agentrunner/run.go`; `harness/contextbuilder/builder.go`; `harness/contextbuilder/prompts/preamble.md`; `harness/coordinator/coordinator.go`; `harness/coordinator/loop.go`; `harness/sessionstore/sessionstore.go`; `harness/operation/` runtime interfaces/manager.
- Adjacent first-party surfaces excluded from ownership: `benchmarks/harbor` evaluation adapter and benchmark tests; repository CI/release workflows; contributor/release governance; unit/fuzz/smoke tests except as corroboration of the shipped runtime contract.
- First-party operating / deployment modes considered: the standalone `unreal-agent-runner` with local persisted sessions and operation execution; resume of an existing session; session fork support; host-selected model/system-prompt/tool configuration; library composition through the documented swappable component interfaces.
- Recursion level: one running agent session is the system-in-focus. Tool calls and serialized operations are subordinate execution mechanisms inside that session. A fork creates another session-history branch but is not treated as a nested viable organization.
- Reviewed revision: `b7c9bf1c5c2fa4127255c07727a7c8413e23944a`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Unreal Agent is an async-first harness library plus an executable runner. The runner resolves a model/provider, opens or restores an append-only session store, discovers workspace skills, configures the standard Bash/ViewImage/SkillUse tools, creates a local operation manager and inbox, then wires those components into one coordinator. The coordinator owns one session's event loop but does not supply the task-level reasoning: it persists accepted inputs and turns, asks the configured LLM for a response, translates model-produced tool calls into serializable operations, dispatches those operations, records their state and returns completed or still-running tool results into later model context.

The supplied preamble explicitly tells the model to treat the prompt as a goal, keep working until it is met, issue independent tool calls concurrently and use later turns when asynchronous results arrive. Tool concurrency therefore increases the operational repertoire of one agent loop; it does not create multiple independently viable S1 units. Heartbeats wake the same loop when tools run for a long time, while stop controls, idempotent input handling, persisted operations and session recovery preserve execution continuity.

Sessions are append-only histories that can be resumed or forked. The session store records inputs, turns, model responses, tool-call status and operation state. Fork metadata points to a parent session and previous turn. These are state/lifecycle capabilities, not evidence that a child session has its own S2-S5 metasystem or that several session branches are coordinated as one higher-recursion organization.

The repository also contains a Harbor evaluation adapter which runs the shipped runner on external benchmark tasks and exports trajectories. That evaluation surface is first-party but adjacent to the assessed product runtime: it evaluates Unreal Agent rather than participating in the normal session's organizational closure.

## Operational model

A caller submits one or more messages or a prompt to `unreal-agent-runner`. The runner selects the configured provider/model, creates or resumes a session, registers the standard tools and workspace skills, and places external messages into the session inbox. A context builder assembles the model request from the fixed harness preamble, caller-selected system prompt, committed history, pending inputs and tool results.

The LLM decides what response to produce and which available tools to call. A tool translator validates each model tool call and converts it into serializable operations; the operation manager runs them asynchronously. Completed and running results are returned to the same model context, causing later turns until no model call, input or tool/operation work remains. The runner pre-submits `StopWhenIdle`, so an idle completed loop exits. Persisted history and operation snapshots allow recovery after interruption.

The decisive task-level choices are therefore made by the model actor inside a bounded first-party execution relation. The coordinator, session store, operation manager, stop logic and heartbeat machinery transport, persist and enforce those choices but do not become separate organizational decision owners merely because they control execution state.

## S1 — Operations

- State: A
- Function: perform the caller's goal-directed task in the supplied workspace/environment by choosing model responses and tool actions, observing their results and continuing until the session becomes idle.
- Disturbance / variety regulated: uncertainty in the caller's task, workspace/file state, shell/tool outcomes, asynchronous completion order, model/tool errors, new external inputs and recovered prior session state.
- Decisive decision or feedback right: choose the next task-level reasoning/output and which available tool calls to issue in response to the current prompt, history and operation results.
- Decision owner: the configured LLM agent actor reached through the first-party LLM adapter and coordinator loop.
- Supporting / enforcement mechanisms: runner-selected provider/model; caller/system prompt; context builder; tool registry/translators; coordinator persistence/dispatch; operation manager; input idempotency; append-only session history; operation snapshots; stop/cancellation handling; heartbeat wakeups; local session resume.
- Closure path: caller input enters the inbox → coordinator persists it and requests a model response → agent chooses text/tool calls → translators create operations → operation manager executes them asynchronously → results are persisted and returned into model context → agent chooses subsequent actions → the loop exits only when no work remains under `StopWhenIdle` or an explicit stop/cancellation closes it.
- Boundary reachability: this actor relation is wired directly by the shipped `unreal-agent-runner`: it constructs the model client, context builder, tool registry, operation manager, inbox and session store and passes them to `coordinator.New(...).Run(...)`. The standard preamble explicitly instructs the model to keep working toward the prompt goal and use asynchronous tool feedback.
- Why this is / is not agent-owned: the runtime deterministically schedules, stores and executes state transitions, but it does not choose the substantive task solution or model-produced tool actions. Removing the LLM actor while retaining the coordinator/operation machinery removes the discretionary goal-directed operational decision path.
- Evidence: [`README.md`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/README.md); [`cmd/internal/agentrunner/run.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/cmd/internal/agentrunner/run.go); [`harness/contextbuilder/prompts/preamble.md`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/contextbuilder/prompts/preamble.md); [`harness/coordinator/loop.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/coordinator/loop.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-provider internals remain outside the first-party boundary. The positive state credits only the agent decision right that the shipped harness directly invokes and closes through its model/tool loop.

## S2 — Coordination

- State: —
- Function: no separate inter-S1 coordination function is established at the reviewed session boundary.
- Disturbance / variety regulated: multiple asynchronous tool operations can finish in different orders, but they are subordinate actions selected by one agent S1 rather than autonomous operational units whose interaction creates a qualifying inter-S1 disturbance.
- Decisive decision or feedback right: not established for an S2-specific relation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: operation IDs/status, tool-call reconciliation, input deduplication, event-loop sequencing, concurrent asynchronous execution, grace timing and serialized session history coordinate runtime events inside one S1 without constituting S2.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the reviewed standard runner exposes one model-driven operational loop per coordinator/session. No second distinct S1 plus interference/attenuation/feedback relation is supplied to classify.
- Evidence: [`README.md`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/README.md); [`harness/coordinator/coordinator.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/coordinator/coordinator.go); [`harness/coordinator/loop.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/coordinator/loop.go); [`harness/sessionstore/sessionstore.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/sessionstore/sessionstore.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: downstream users can compose the library in broader organizations, but generic composability does not establish an S2 function in this repository's standard distribution.

### Absence scope

- Surfaces inspected: runner wiring; coordinator state/event loop; inbox; operation manager/operation state; tool translation/reconciliation; session persistence/resume/fork; context construction; repository search for subagent/delegation/multi-agent paths.
- Plausible first-party paths checked: concurrent tool operations; multiple tool calls in one turn; operation actors; session forks; persisted sessions; swappable managers/interfaces.
- Why no material first-party path remains: all inspected concurrent work is subordinate to one model-driven session, while forks create separate histories rather than a first-party higher-level organization of simultaneously regulated S1 units. No concrete inter-S1 conflict or oscillation plus attenuation and returned behavioural adjustment is supplied.

## S3 — Inside-and-now control

- State: —
- Function: no distinct metasystemic inside-and-now control function is established above the single operational session.
- Disturbance / variety regulated: the coordinator tracks current inputs, model calls, tool calls and operations and can stop/cancel work, but these are execution/liveness states inside the same S1 rather than whole-system resource/commitment regulation across S1 operations.
- Decisive decision or feedback right: no whole-system current resource, priority, commitment, accountability or synergy decision right is established at the declared recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: coordinator state, hard/idle stops, cancellation, heartbeat timing, provider/model selection, tool availability and operation status provide deterministic execution constraints but do not by themselves own S3 decisions.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the LLM owns task-local S1 choices; the runtime owns deterministic execution state. Neither reviewed path is a separately established S3 current-control conversation at a multi-operation organizational level.
- Evidence: [`harness/coordinator/coordinator.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/coordinator/coordinator.go); [`harness/coordinator/loop.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/coordinator/loop.go); [`cmd/internal/agentrunner/run.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/cmd/internal/agentrunner/run.go).
- Basis: structural negative search.
- Confidence: high.
- Caveats: an embedding application could place the library under an external supervisor, but that parent organization is not part of this standard-distribution assessment.

### Absence scope

- Surfaces inspected: coordinator current state; stop/cancel paths; heartbeat path; operation manager; runner provider/model/tool configuration; session observer/logging; session recovery/fork.
- Plausible first-party paths checked: `Coordinator` naming/central event loop; hard stop and stop-when-idle; operation cancellation; heartbeat wakeups; model/tool selection; host controls.
- Why no material first-party path remains: these paths execute or configure one S1 loop. The reviewed distribution does not expose a higher current-control actor with a whole-system view and discretionary authority over shared S1 resources, commitments, priorities or accountability.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established inside the assessed runtime boundary.
- Disturbance / variety regulated: session history, JSONL observation, operation status and ordinary tool results provide normal execution evidence; the Harbor adapter can evaluate benchmark runs but is an adjacent evaluation system rather than a runtime audit channel feeding current control.
- Decisive decision or feedback right: no independent audit judgment with corrective return is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: persisted history, session observers, logs, fuzz/unit/smoke tests and Harbor trajectories expose or test behavior without constituting an in-boundary complementary audit organization.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: no qualifying S3* function is established, so audit ownership is not classified.
- Evidence: [`README.md`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/README.md); [`benchmarks/harbor/README.md`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/benchmarks/harbor/README.md); [`harness/sessionstore/sessionstore.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/sessionstore/sessionstore.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: Harbor can supply external evaluation evidence in an evaluation recursion, but repository co-location does not make that evaluator part of the shipped session's S3* closure.

### Absence scope

- Surfaces inspected: session observers/logging; append-only session state; operation outputs/status; tests/fuzz tests; Harbor evaluation adapter, trajectories and validation path; coordinator feedback loop.
- Plausible first-party paths checked: ordinary tool-result reconciliation; logs/observers; benchmark trajectories/results; test and smoke validation.
- Why no material first-party path remains: runtime observations travel on the ordinary production path, while the only clearly separate evaluator is the co-located Harbor benchmark system excluded from product ownership. No first-party runtime path independently challenges an operational claim and returns a finding into subsequent current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective adaptation loop is established in the standard distribution.
- Disturbance / variety regulated: sessions can absorb new prompts/tool results and recover historical state, and workspace skills can extend task capability, but these mechanisms serve present execution or caller-supplied configuration rather than sensing future environmental change and developing adaptation options.
- Decisive decision or feedback right: no prospective adaptation judgment that changes present harness capability is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: persisted history, resume/fork, provider configuration, skills discovery, caller-supplied system prompts and tool interfaces provide continuity/extensibility without supplying S4 closure.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the model can reason about the current task, but the reviewed runtime does not assign it a separate environment-modeling/adaptation mandate whose outputs alter current organizational capability.
- Evidence: [`README.md`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/README.md); [`cmd/internal/agentrunner/run.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/cmd/internal/agentrunner/run.go); [`harness/sessionstore/sessionstore.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/sessionstore/sessionstore.go); [`harness/contextbuilder/builder.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/contextbuilder/builder.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: downstream embeddings may add research/adaptation machinery, but those are separate systems-in-focus and require their own evidence.

### Absence scope

- Surfaces inspected: context builder; runtime prompt/preamble; skills discovery; session history/resume/fork; provider/model configuration; tool interfaces; benchmark/evaluation directory; repository search for adaptation/learning/future-oriented paths.
- Plausible first-party paths checked: memory/history reuse; session forks; skills; provider changes; caller settings; benchmark results.
- Why no material first-party path remains: none of the inspected paths closes external/future sensing → adaptation-option generation → return into current capability. Persistence, task reasoning and extensibility remain present-oriented mechanisms until another system composes them into such a loop.

## S5 — Policy and identity

- State: —
- Function: no runtime identity or ultimate-policy closure is established at the assessed session recursion.
- Disturbance / variety regulated: the fixed harness preamble, caller-selected system prompt, model/provider choice and host-selected tool set bound operation, but they are configuration/policy inputs rather than an in-runtime authority that resolves identity-level or ultimate-policy tensions.
- Decisive decision or feedback right: no identity/ultimate-policy decision right is exposed and closed by the shipped runtime.
- Decision owner: not established within the assessed system.
- Supporting / enforcement mechanisms: embedded preamble; caller-supplied system prompt; model/reasoning settings; tool allow/disallow configuration; runner/environment configuration; cancellation/stop behavior.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the model follows supplied instructions but does not own the right to revise or resolve the harness's identity/ultimate policy. The caller/developer chooses configuration before or around operation; generic configuration authority is not itself a function-specific parent S5 loop.
- Evidence: [`harness/contextbuilder/prompts/preamble.md`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/contextbuilder/prompts/preamble.md); [`harness/contextbuilder/builder.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/harness/contextbuilder/builder.go); [`cmd/internal/agentrunner/run.go`](https://github.com/unreallabsai/unreal-agent/blob/b7c9bf1c5c2fa4127255c07727a7c8413e23944a/cmd/internal/agentrunner/run.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream application or human organization can own S5 over an embedded Unreal Agent session. That parent is not supplied as a first-party function-specific governance loop by this repository.

### Absence scope

- Surfaces inspected: built-in preamble; system-prompt assembly; runner request/configuration schema; provider/model/reasoning selection; tool/skill registration; stop/control messages; session persistence and fork semantics.
- Plausible first-party paths checked: fixed prompt identity; caller system prompt; model selection; tool allow/disallow controls; runtime control messages; session branch/fork.
- Why no material first-party path remains: these paths set or enforce operational configuration but do not expose an identity/ultimate-policy issue → legitimate authority → authoritative decision → returned governance loop at the declared recursion.

## Recursion

No positive VSM recursion is established. A coordinator owns one session loop. Serialized operations and tool calls are capabilities/actions, not viable sub-organizations. Session `Fork` records a new history branch with a parent session and previous turn, but the reviewed distribution does not establish that forked sessions become S1 units inside a higher-level Unreal Agent organization with their own required metasystem and parent-level coordination/control channels.

## Variety and escalation

The harness absorbs substantial task/runtime variety at S1: arbitrary caller goals, model output, Bash/ViewImage/skill use, asynchronous operation completion, concurrent independent tool calls, new external inputs, provider errors and restart/recovery state. Input IDs attenuate duplicate delivery; serialization and append-only history preserve replay/recovery distinctions; the context builder transduces persisted state and tool results into model input; the model supplies the main discretionary response repertoire.

Exceptional runtime conditions are handled primarily through process/error/stop paths rather than a higher VSM recursion. Hard stop interrupts the model and cancels outstanding operations; `StopWhenIdle` ends a completed session; long-running tools generate a heartbeat back into the same agent loop; provider/session/runtime errors return to the caller. These channels preserve execution viability but do not by themselves establish S3/S4/S5 ownership.

## Evidence gaps

- The repository is very new at the reviewed revision, so future releases may add first-party multi-agent, supervisory, audit, adaptation or governance paths that are not present here.
- The README encourages alternative component implementations and gives a remote-operation-manager example, but generic extension seams are not credited as constructor states without function-specific organizational paths.
- Downstream users may compose multiple Unreal Agent sessions or independent evaluators around the library; each such composition is a separate system-in-focus and requires separate evidence before S2-S5 or recursion can be credited.
