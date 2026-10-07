---
harness_id: einoclaw
project_name: Einoclaw
repository: https://github.com/YellowDusk04/einoclaw
review_ref: f7b790f966487e7b9f8202c9d024f714b3030afb
reviewed_at: 2026-10-07
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Einoclaw

## Review boundary

- System in focus: the shipped/self-hosted Einoclaw CLI coding-agent composition at the frozen revision, including its first-party agent construction, TurnLoop wiring, TUI integration, configured Eino middleware, local session store, and first-party configuration surface.
- Purpose and identity: a CLI coding agent that accepts user coding requests, lets the model select first-party coding tools, consumes tool results, and iterates within a persistent local session.
- Relevant environment: the user's current working directory and host shell/filesystem, configured model provider, local session/memory/configuration directories, and interactive terminal user.
- Standard-distribution boundary: repository code and supported local configuration paths that instantiate Einoclaw. Eino, model providers, Cozeloop, Bubble Tea, external skills, and the host OS are dependencies rather than owners of credited VSM functions.
- Credited operating / distribution surfaces: `main.go`, `handlers.go`, `tui.go`, `init.go`, `config.go`, `example.yaml`, and the shipped README/architecture documentation that describe and wire the local runtime.
- Adjacent first-party surfaces excluded from ownership: explanatory documentation about Eino sub-agent/background-task facilities where no corresponding Einoclaw runtime wiring exists; repository docs/examples that describe framework capabilities but are not registered into the shipped agent; repository maintenance/CI.
- First-party operating / deployment modes considered: local interactive CLI execution with first-party filesystem tools enabled as configured; optional permission middleware on/off; optional summarization/reduction/automemory/skill middleware; session resume; supported model selection.
- Recursion level: one Einoclaw coding-agent session operating on one user-selected working environment. No nested viable first-party operational unit with its own environment and metasystem is established.
- Reviewed revision: `f7b790f966487e7b9f8202c9d024f714b3030afb`.
- Observation date: 2026-10-07.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Einoclaw is a small Go CLI coding agent built on Eino's ADK and Bubble Tea. The repository itself wires a single `TypedChatModelAgent` into an Eino `TurnLoop`, registers first-party-selected middleware, sends user messages into that loop, receives model/tool events, and presents them through the TUI.

The first-party runtime creates one agent with a coding instruction, configured model, middleware stack, and a 50-iteration ceiling. The filesystem middleware can expose list/read/write/edit/search/execute tools according to local configuration. The agent therefore has a repository-wired model → tool-call → tool-result → next-model-decision operational loop. The TurnLoop persists session events to `~/.einoclaw/sessions`; `/resume` reconstructs the message history for a selected session. Optional summarization/reduction middleware manages context, optional automemory persists cross-session memory, and optional skill middleware loads local skill content.

The permission middleware is an execution gate, not a separate operating agent. When enabled, it checks shell commands against a configured blacklist; a matching command interrupts the TurnLoop and asks the user to approve, reject, or reject with a response before execution resumes. This is human-in-the-loop enforcement over a specific tool action rather than a separate S5 policy loop.

The repository also contains explanatory documentation describing Eino sub-agent and background-task features. At the reviewed revision, Einoclaw's runtime construction does not import/register the sub-agent middleware or a background-task manager. Those documentation examples are therefore excluded from the credited operating boundary.

Primary evidence:
- [README at the reviewed revision](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/README.md)
- [agent and TurnLoop wiring](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/main.go)
- [filesystem, memory, context, permission and skill middleware construction](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/handlers.go)
- [interactive message queue, permission response and session resume](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/tui.go)
- [local initialization and session/config directories](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/init.go)
- [shipped configuration template](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/example.yaml)
- [Eino sub-agent/background-task explanatory document](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/docs/%E5%AD%90Agent%E4%B8%8E%E5%90%8E%E5%8F%B0%E4%BB%BB%E5%8A%A1.md)

## Operational model

The operational unit is the single Einoclaw coding agent. The model receives the user's coding request plus the current conversation/tool context, decides whether and how to call enabled tools, receives the results, and iterates until it returns an answer or reaches a stop condition. First-party runtime machinery transports and enforces those decisions; configured providers supply inference but do not become organizational owners.

Operator configuration determines which tool and middleware capabilities are available. A supported local mode can expose write/edit/execute tools while leaving the permission middleware disabled, so the agent can close the coding operation autonomously inside the configured working directory. Another supported mode can enable the permission gate, in which selected shell commands require a human decision before the same operational loop resumes. That human gate limits an S1 action but does not create a higher VSM function by itself.

The TUI may queue additional user messages while the current turn is running. `GenInput` consumes one user item at a time and leaves remaining items for later processing. This is serialization/preemption of inputs to the same S1, not evidence of coordination among distinct S1 units.

## S1 — Operations

- State: A
- Function: perform coding-assistant work by interpreting a coding request, selecting enabled coding/filesystem tools, acting on the working environment, consuming tool results, and iterating toward a response.
- Disturbance / variety regulated: uncertainty in the user's codebase/task, filesystem state, tool results/errors, and evolving conversational context during a coding turn.
- Decisive decision or feedback right: choose the next model response and tool calls, including which enabled coding operation to invoke and how to react to returned tool results.
- Decision owner: the Einoclaw agent/model loop in the autonomous supported mode.
- Supporting / enforcement mechanisms: Eino TurnLoop; filesystem middleware; local backend; session-event persistence; iteration limit; context reduction/summarization; optional deterministic permission gate.
- Closure path: user request → agent/model decision → first-party-wired tool call → tool result/session event → result returned to the agent context → subsequent model decision or terminal response.
- Boundary reachability: `loadAgent()` registers the configured filesystem middleware on the shipped `TypedChatModelAgent`, and `initTurnLoop()` directly runs that agent through the shipped TurnLoop. The configuration schema exposes write/edit/execute tool switches and permission enablement, so the autonomous tool-use path is a first-party supported local mode rather than an adjacent example.
- Why this is / is not agent-owned: in the autonomous mode the agent selects and sequences operational tool calls from model-visible tool definitions and closes the loop from returned results. Runtime code executes/enforces those choices. Optional operator approval can gate selected shell commands in another mode, but it does not remove the separately supported autonomous mode.
- Evidence: [main.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/main.go), [handlers.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/handlers.go), [README.md](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/README.md), [example.yaml](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/example.yaml).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: model inference is externally provided; the optional permission mode can require human authorization for configured shell-command prefixes; tool availability is operator-configured.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at the reviewed boundary.
- Disturbance / variety regulated: not established; the shipped runtime exposes one coding-agent operational unit rather than multiple distinct S1 units whose mutual interference must be attenuated.
- Decisive decision or feedback right: none for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: the TurnLoop input queue, session state, event dispatch, and optional framework middleware serialize/transport work for the same agent.
- Closure path: not applicable.
- Boundary reachability: not applicable; no positive S2 path is claimed.
- Why this is / is not agent-owned: there is no established S2 function to own. Queued user messages and sequential TurnLoop processing are input/runtime mechanics for one S1.
- Evidence: [GenInput and TurnLoop construction in main.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/main.go), [pending-message handling in tui.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/tui.go), [sub-agent explanatory document](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/docs/%E5%AD%90Agent%E4%B8%8E%E5%90%8E%E5%8F%B0%E4%BB%BB%E5%8A%A1.md).
- Basis: structural.
- Confidence: high.
- Caveats: Eino itself supports sub-agent facilities, but documentation of dependency/framework capability is not credited without Einoclaw runtime wiring.

### Absence scope

- Surfaces inspected: README; `main.go`; `handlers.go`; `tui.go`; configuration/init surfaces; architecture and sub-agent/background-task documentation.
- Plausible first-party paths checked: TurnLoop input queue/preemption, multiple middleware, session handling, skill loading, and documented Eino sub-agent/background-task facilities.
- Why no material first-party path remains: the shipped agent construction registers no sub-agent middleware or background-task manager, and the queue serializes user inputs to the same operational agent. No distinct first-party S1 units plus interference/attenuation/feedback relation is wired.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current first-party control function over multiple operational units/resources/commitments is established.
- Disturbance / variety regulated: not established as an S3 disturbance at this recursion.
- Decisive decision or feedback right: none for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: iteration limit, tool enable/disable configuration, model selection, permission gate, token display, session stop/resume.
- Closure path: not applicable.
- Boundary reachability: not applicable; no positive S3 path is claimed.
- Why this is / is not agent-owned: the agent controls its own next operational action, but the reviewed boundary does not expose a separate whole-system current view plus authority over shared resources, commitments, priorities, constraints, accountability, synergy, or intervention.
- Evidence: [main.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/main.go), [tui.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/tui.go), [example.yaml](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/example.yaml).
- Basis: structural.
- Confidence: high.
- Caveats: single-session operational control is part of S1 here and must not be promoted into S3 merely because it has stop, queue, token, or permission controls.

### Absence scope

- Surfaces inspected: runtime construction, TUI/status controls, middleware/configuration, session lifecycle, README/architecture docs, documented background-task/sub-agent capabilities.
- Plausible first-party paths checked: current token/status bar, model switching, interrupt/permission handling, TurnLoop stop/resume, queues, iteration limit, background/sub-agent documentation.
- Why no material first-party path remains: no credited runtime path observes a plurality of S1 units as a whole and exercises current-control decisions over their shared resources/commitments. Deterministic limits and operator tool configuration are enforcement/configuration rather than S3 ownership.

## S3* — Complementary audit

- State: —
- Function: no complementary, sufficiently independent first-party audit function with corrective closure is established.
- Disturbance / variety regulated: not established as S3*.
- Decisive decision or feedback right: none for S3*.
- Decision owner: none established.
- Supporting / enforcement mechanisms: session event logging, optional Cozeloop tracing, tool-call error wrapping, permission checks, and ordinary tool-result feedback.
- Closure path: not applicable.
- Boundary reachability: not applicable; no positive S3* path is claimed.
- Why this is / is not agent-owned: logging/telemetry and routine execution checks observe the same operational path; they do not constitute an independent complementary access path that audits an operational claim and returns corrective findings.
- Evidence: [README observability/session description](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/README.md), [handlers.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/handlers.go), [main.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/main.go).
- Basis: structural.
- Confidence: high.
- Caveats: external observability products may support later human inspection, but they are external dependencies and no first-party audit-judgment/closure loop is supplied here.

### Absence scope

- Surfaces inspected: session/event persistence, optional Cozeloop integration described by the repository, error middleware, permission gate, TUI event rendering, architecture documentation.
- Plausible first-party paths checked: tracing, session logs, tool results/errors, permission decisions, and any verifier/reviewer/audit-labelled runtime path.
- Why no material first-party path remains: no independent complementary evidence acquisition plus audit judgment and return-to-operation corrective loop is wired. Routine tool feedback and tracing remain part of ordinary operation/observability.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: not established as S4.
- Decisive decision or feedback right: none for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent automemory, session resume, context summarization/reduction, local skill loading, and manual model selection.
- Closure path: not applicable.
- Boundary reachability: not applicable; no positive S4 path is claimed.
- Why this is / is not agent-owned: memory and summarization retain/compress prior operational context; they do not scan an external/future environment, generate adaptation options, decide an adaptation, and return it into current capability. Skills/models are selected from operator configuration rather than by a first-party adaptation loop.
- Evidence: [handlers.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/handlers.go), [README context/memory/skill description](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/README.md), [tui.go model/session controls](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/tui.go).
- Basis: structural.
- Confidence: high.
- Caveats: externally authored skills can change capabilities when the operator installs/enables them, but their authorship/selection is outside the first-party autonomous adaptation loop assessed here.

### Absence scope

- Surfaces inspected: automemory, summarization/reduction, skill loading, session resume, model switching, README/docs, runtime/configuration.
- Plausible first-party paths checked: cross-session memory, context compression, dynamic skill loading, provider/model selection, and documented sub-agent/background-task features.
- Why no material first-party path remains: none closes the required external distinction + future/prospective distinction + adaptation-option generation + decision + return into current capability. Retention and manual extensibility are not S4.

## S5 — Policy and identity

- State: —
- Function: no runtime first-party identity/ultimate-policy governance loop is established at the assessed recursion.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: none for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: hard-coded agent instruction, local YAML configuration, tool enable/disable switches, optional shell-command blacklist, and human approval/rejection of matched commands.
- Closure path: not applicable.
- Boundary reachability: not applicable; no positive S5 path is claimed.
- Why this is / is not agent-owned: the instruction/configuration constrain the operational agent but do not implement a runtime decision over organizational identity or ultimate policy. The permission dialog decides whether a particular shell action proceeds; generic action approval is not S5.
- Evidence: [agent instruction and permission resume path in main.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/main.go), [permission gate in handlers.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/handlers.go), [permission UI in tui.go](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/tui.go), [configuration template](https://github.com/YellowDusk04/einoclaw/blob/f7b790f966487e7b9f8202c9d024f714b3030afb/example.yaml).
- Basis: structural.
- Confidence: high.
- Caveats: a human/operator remains the external authority who configures the local tool/policy envelope, but Methodology 0.3.x does not turn ordinary configuration or command approval into a positive S5 parent mode.

### Absence scope

- Surfaces inspected: agent instruction, runtime/configuration, permission middleware/UI, model selection, skill configuration, session lifecycle, README/docs.
- Plausible first-party paths checked: static system instruction, YAML policy/configuration, human command approval, model selection, skill loading, and any runtime governance/policy mechanism.
- Why no material first-party path remains: no first-party path frames an identity/ultimate-policy issue, routes it to a legitimate S5 authority, returns an authoritative policy/identity decision, and governs subsequent operation through that decision.

## Distributed OSS parent arrangement

The public repository has ordinary maintainer/contributor governance, but that governance is outside the assessed local coding-agent runtime. The reviewed distribution does not route S3/S4/S5 matters from an operating Einoclaw session into project-level OSS governance and return a decision into that same runtime. No organization-level parent-mode notation is therefore inferred.

## Self-hosted and non-human modes

Einoclaw is self-hosted locally. The operator can choose models, enable/disable tools and middleware, and optionally require approval for configured shell-command prefixes. These operator controls bound or interrupt S1 operations; none establishes a complete S3, S4, or S5 parent-governed loop at the reviewed recursion.

## Recursion

One operational coding agent is established. The repository does not wire multiple recursively viable child systems. Framework documentation about sub-agents is not credited because the reviewed Einoclaw runtime does not instantiate that path.

## Variety and escalation

The agent absorbs coding-task variety through model reasoning and enabled filesystem/shell tools. Session persistence, reduction/summarization, and optional automemory reduce context-loss pressure. Tool errors are returned into the model loop. When permission middleware is enabled and a shell command matches the blacklist, execution is interrupted and escalated to the local user for approve/reject/respond, after which the TurnLoop resumes or blocks that action. This is bounded operational escalation, not by itself evidence of S3/S4/S5.

## Evidence gaps

No material unresolved evidence gap changes the published vector at the frozen revision. The principal boundary risk was framework-capability leakage: Eino documentation in the repository describes sub-agents/background tasks, but the reviewed first-party runtime files do not wire those mechanisms into Einoclaw. Those documented facilities are therefore excluded rather than classified as latent S2/S3 evidence.
