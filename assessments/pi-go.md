---
harness_id: pi-go
project_name: pi (Go)
repository: https://github.com/sky-valley/pi
review_ref: 1c1b674f7b7bf18885082e3cf39c29fc56858107
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# pi (Go)

## Review boundary

- System in focus: one first-party `sky-valley/pi` Go coding-agent deployment/session at pinned revision `1c1b674f7b7bf18885082e3cf39c29fc56858107`, including the `agent` loop/state machine, `coding.Session`, built-in coding tools, steering/follow-up queues, automatic context compaction, JSONL persistence/resume, project context/skills loading, SDK facade and `cmd/pi` CLI.
- Purpose and identity: provide a native-Go port of pi's coding-agent harness that turns user coding requests into filesystem/process outcomes through a persistent model/tool feedback loop while preserving pi-compatible session, tool and provider semantics.
- Relevant environment: user prompts, the selected workspace/cwd, local files and commands, configured LLM provider/model, API credentials, persisted session history, trusted project context/skills and tool results.
- Standard-distribution boundary: the root Go module and shipped `pi` CLI/SDK at the frozen ref. The separate `difftest` Go module, `.claude/skills` used to maintain/port the repository, repository tests, parity sweeps, release notes and CI are adjacent development/evaluation surfaces; they may corroborate implementation but do not own runtime organizational functions.
- Credited operating / distribution surfaces: `agent.Agent`, `agent.AgentLoop`, tool execution and queue semantics, `coding.Session`, system-prompt/resource assembly, built-in coding tools, compaction, session persistence/resume, SDK hooks exposed to embedders, and `cmd/pi` print/REPL operation.
- Adjacent first-party surfaces excluded from ownership: `difftest/`, `.claude/skills/*`, test fixtures and `*_test.go`, parity/release/porting documentation, upstream TypeScript pi, repository CI/build/release activity and maintainer porting workflow.
- First-party operating / deployment modes considered: CLI print mode; interactive REPL; SDK embedding through `coding.NewSession`; persisted/resumed sessions; sequential or parallel tool-call execution; steering/follow-up/abort; custom tools and execution hooks; optional trusted project-local skills/context; automatic compaction.
- Recursion level: one pi (Go) agent session. The active model/tool loop is the S1 operational unit. Concurrent tool invocations are action executions inside that unit, not separate S1 organizations merely because goroutines execute them concurrently.
- Reviewed revision: `1c1b674f7b7bf18885082e3cf39c29fc56858107`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The root runtime is a stateful single-agent model/tool loop. `agent.Agent` owns the transcript, active model, tool registry, streaming state and steering/follow-up queues. `runLoop` repeatedly requests a model response, validates and executes requested tools, appends tool results to the same agent context, and returns those observations to later model turns. Tool calls may execute sequentially or concurrently, but they remain calls made by one agent turn against one shared agent context.

`coding.Session` packages that loop as the coding harness: it resolves the built-in/custom tool set, constructs the coding system prompt, exposes model/thinking changes and steering/follow-up/abort, records finalized messages to JSONL, restores prior branches, and optionally compacts long context. The `cmd/pi` CLI wires one session into print or REPL operation and exposes ordinary operator controls such as `/model`, `/think`, `/new`, session listing/resume and system-prompt override.

The extension callbacks (`BeforeToolCall`, `AfterToolCall`, `FinishTurn`, `PrepareRequest`, `PrepareNextTurn`) are SDK composition points supplied by an embedder. They do not, by themselves, instantiate additional first-party organizational actors or a metasystemic function in the standard distribution. Likewise, project skills/context are discovered and inserted as prompt resources when the operator has enabled project trust; the frozen runtime does not autonomously evolve or adopt new skills from environmental analysis.

The repository also contains extensive fidelity machinery, but it sits outside the assessed operating boundary. The README explicitly describes `difftest/` as a separate Go module comparing this port against upstream pi as ground truth, while `.claude/skills` and parity/release documents support repository maintenance. Those surfaces are development/evaluation evidence, not an independent runtime auditor or adaptation authority for a deployed session.

Primary evidence:

- [`README.md`](https://github.com/sky-valley/pi/blob/1c1b674f7b7bf18885082e3cf39c29fc56858107/README.md) — shipped package layout, runtime/session/tool capabilities, SDK surface, persistence, compaction and explicit separation of `difftest` from the runtime module.
- [`agent/agent.go`](https://github.com/sky-valley/pi/blob/1c1b674f7b7bf18885082e3cf39c29fc56858107/agent/agent.go) — single stateful Agent, transcript/tool state, steering/follow-up queues, run ownership, abort/reset and loop configuration.
- [`agent/loop.go`](https://github.com/sky-valley/pi/blob/1c1b674f7b7bf18885082e3cf39c29fc56858107/agent/loop.go) — repeated model request, tool execution, result feedback and subsequent-turn closure.
- [`agent/types.go`](https://github.com/sky-valley/pi/blob/1c1b674f7b7bf18885082e3cf39c29fc56858107/agent/types.go) — tool execution modes and SDK hook contracts; parallel mode executes allowed tool calls concurrently rather than creating distinct agents.
- [`coding/session.go`](https://github.com/sky-valley/pi/blob/1c1b674f7b7bf18885082e3cf39c29fc56858107/coding/session.go) — coding-session composition, tool selection, persistence/resume, operator/SDK controls and optional compaction wiring.
- [`coding/systemprompt.go`](https://github.com/sky-valley/pi/blob/1c1b674f7b7bf18885082e3cf39c29fc56858107/coding/systemprompt.go) — static/configurable system-prompt assembly, project context and skills exposure.
- [`coding/compaction.go`](https://github.com/sky-valley/pi/blob/1c1b674f7b7bf18885082e3cf39c29fc56858107/coding/compaction.go) — context-window summarization/compaction machinery.
- [`cmd/pi/main.go`](https://github.com/sky-valley/pi/blob/1c1b674f7b7bf18885082e3cf39c29fc56858107/cmd/pi/main.go) — standard CLI composition and operator controls.

## Operational model

One model actor performs the substantive coding work. It chooses tool calls and arguments from the currently exposed tool set; the host executes or blocks those calls; resulting evidence is appended to the same transcript; and the next model turn revises action from that evidence. Steering and follow-up inject additional user/embedder messages into this same S1 loop. Persistence and compaction preserve/manage its context across turns and restarts.

The repository does not establish a separate operational-agent population in the assessed mode. Parallel tool calls are concurrent effects initiated by the same agent, while custom tools/hooks are constructor interfaces whose downstream implementations are not borrowed as first-party organizational owners. This boundary is decisive for the negative S2/S3 findings.

## S1 — Operations

- State: A
- Function: perform user-directed coding and workspace work through repeated model-selected tool calls and returned environmental feedback.
- Disturbance / variety regulated: heterogeneous user requests, changing workspace/files/process state, provider responses, tool outputs/errors, context pressure, queued steering/follow-up messages and resumed session state.
- Decisive decision or feedback right: choose the next substantive tool/action and its task-specific arguments, interpret returned results, and decide whether another model/tool turn is needed or the task can conclude.
- Decision owner: the active configured model actor inside the `Agent` loop.
- Supporting / enforcement mechanisms: tool schemas/executors, sequential/parallel tool scheduler, before/after hooks, provider adapters, transcript state, persistence, retry/cancellation, compaction and CLI/SDK surfaces.
- Closure path: user/session context → model response/tool calls → runtime validates and executes tools → tool-result messages are appended to the agent context → later model request observes them and selects the next action or final response.
- Boundary reachability: `agent.Agent`/`AgentLoop` are the shipped core used directly by `coding.Session`, and `cmd/pi` constructs that session for both print and interactive modes; no development-only surface is needed for the loop.
- Why this is / is not agent-owned: removing the model removes the task-specific selection of substantive actions, arguments and stopping point. Deterministic runtime code executes, orders and constrains those choices but does not make materially equivalent coding decisions on its own.
- Evidence: `agent/agent.go`, `agent/loop.go`, `coding/session.go`, `cmd/pi/main.go`.
- Basis: explicit + structural
- Confidence: high
- Caveats: operator configuration chooses the model/tool envelope and may inject steering, but ordinary within-run task action remains model-owned.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at this session boundary.
- Disturbance / variety regulated: concurrent tool effects can require execution ordering or safety handling, but the frozen standard runtime does not establish interference among distinct S1 operational units.
- Decisive decision or feedback right: not established for inter-S1 coordination.
- Decision owner: none established for S2 at this boundary.
- Supporting / enforcement mechanisms: sequential/parallel tool execution modes, per-tool execution mode, steering/follow-up queues and host-side tool hooks regulate actions inside one Agent rather than relationships among distinct S1s.
- Closure path: not applicable; tool results close back into the same S1 model loop.
- Why this is / is not agent-owned: there is no qualifying S2 function to classify. Parallel goroutines do not turn tool invocations into autonomous operational units.
- Evidence: `agent/types.go`, `agent/loop.go`, `agent/agent.go`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: SDK consumers could compose multiple sessions or custom tools externally, but downstream composition is outside this standalone repository assessment.

### Absence scope

- Surfaces inspected: `agent` runtime/state/queue/tool execution, `coding.Session`, built-in/custom tool composition, CLI modes, persistence/compaction, README package boundary and repository tree for delegation/subagent surfaces.
- Plausible first-party paths checked: parallel tool batches, steering/follow-up queues, SDK hooks/custom tools, session persistence/resume and any built-in subagent/delegation/spawn path.
- Why no material first-party path remains: the shipped organization contains one model/tool S1; searches and runtime APIs expose no first-party child-agent/delegation population, and concurrency is explicitly tool-call concurrency inside that same S1.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function over multiple operational units is established.
- Disturbance / variety regulated: the runtime tracks one Agent's streaming/tool state and permits user/embedder abort, steering, model changes and reset, but these are controls of one S1/session rather than regulation of a current operational portfolio.
- Decisive decision or feedback right: not established for whole-system resources, commitments, priorities or interventions across distinct S1 units.
- Decision owner: none established for S3 at the declared recursion.
- Supporting / enforcement mechanisms: `AgentState`, `Abort`, queue state, CLI `/model`/`/think`/`/new`, persistence and execution hooks.
- Closure path: not applicable for S3; these surfaces alter or observe the single operational loop directly.
- Why this is / is not agent-owned: lifecycle visibility and operator controls do not create the whole-system current view plus discretionary cross-unit authority required for S3.
- Evidence: `agent/agent.go`, `coding/session.go`, `cmd/pi/main.go`.
- Basis: explicit + structural
- Confidence: high
- Caveats: an external application may use the SDK to supervise multiple sessions, but that parent organization is not supplied by this repository's standard runtime.

### Absence scope

- Surfaces inspected: Agent state/lifecycle APIs, steering/follow-up/abort, session and CLI controls, hooks, persistence and tool scheduling.
- Plausible first-party paths checked: live Agent state, operator slash commands, queue management, tool parallelism, SDK hooks and any multi-session manager/controller surface.
- Why no material first-party path remains: available controls target one session/S1 and no shipped controller receives a whole-system view of multiple S1 commitments with discretionary authority to reallocate or steer them as an organization.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary operational-audit path is established in the shipped runtime.
- Disturbance / variety regulated: ordinary tool/schema validation and hooks can reject or rewrite calls/results, but no sufficiently independent channel re-observes operational reality to challenge the Agent's routine reporting or completion claim.
- Decisive decision or feedback right: not established for an independent audit verdict.
- Decision owner: none established for S3* at this boundary.
- Supporting / enforcement mechanisms: tool validation, `BeforeToolCall`/`AfterToolCall` hooks, tests and differential parity checks exist but do not supply a runtime independent-audit function.
- Closure path: not applicable for S3*.
- Why this is / is not agent-owned: the relevant runtime hooks sit directly in the normal execution path, while `difftest` and repository tests are adjacent development/evaluation systems rather than a complementary operating channel.
- Evidence: `agent/types.go`, `README.md`, repository `difftest/` separation.
- Basis: explicit + structural
- Confidence: high
- Caveats: an embedder could implement a reviewer through custom hooks/tools, but that downstream actor is not credited as first-party runtime audit.

### Absence scope

- Surfaces inspected: tool-call hooks, tool result processing, agent transcript/state, CLI/SDK, `difftest` boundary, repository tests and maintenance skills.
- Plausible first-party paths checked: before/after tool hooks, finish/prepare hooks, parity differential harness, tests/fixtures and any built-in reviewer/auditor command or second model scene.
- Why no material first-party path remains: runtime verification is in-band enforcement around the same operational path; the only materially separate verification surfaces are development/evaluation artifacts excluded from operating ownership, and no built-in runtime reviewer closes findings back into operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective organizational adaptation loop is established.
- Disturbance / variety regulated: context growth, provider/model choice and available project resources are managed, but the runtime does not generate and adopt prospective organizational/capability changes from external environmental analysis.
- Decisive decision or feedback right: not established for choosing a future adaptation and changing present capability on that basis.
- Decision owner: none established for S4 at the assessed boundary.
- Supporting / enforcement mechanisms: automatic compaction, manual model/thinking changes, static project-context/skill discovery, provider catalog and custom tool/hooks configuration.
- Closure path: not applicable for S4; compaction returns a shorter representation of existing conversation context, while model/skill/tool changes are operator/embedder configuration rather than a closed prospective adaptation cycle.
- Why this is / is not agent-owned: the model can solve current tasks and use already exposed skills/tools, but no first-party process gives it or another internal actor the decisive right to alter future organizational capability from environmental intelligence.
- Evidence: `coding/compaction.go`, `coding/session.go`, `coding/systemprompt.go`, `cmd/pi/main.go`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: repository maintainers continuously port upstream features, but that development process is outside the deployed-session boundary and cannot donate S4.

### Absence scope

- Surfaces inspected: compaction, model selection, provider catalog, project context/skills, custom tools/hooks, persistence/resume, CLI controls, release/parity development surfaces.
- Plausible first-party paths checked: automatic summarization/compaction, runtime model switching, trusted skill loading, external/provider access, self-extension claims and maintainer upstream-port workflow.
- Why no material first-party path remains: these paths manage current context/capability or require operator/developer configuration; none closes external/prospective analysis → adaptation option → authoritative adoption → changed present capability inside the assessed runtime.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at runtime.
- Disturbance / variety regulated: the harness constrains prompt/tool availability, project trust, model/provider choice and execution hooks, but those mechanisms do not resolve identity or ultimate-policy issues through a legitimate S5 authority loop.
- Decisive decision or feedback right: not established for runtime identity/ultimate organizational policy.
- Decision owner: none established for S5 at this boundary.
- Supporting / enforcement mechanisms: default/custom/forced system prompt, `--system`, project trust flag, tool allow/deny selection, model/thinking controls and SDK policy-like hooks.
- Closure path: not applicable for S5; configuration is applied directly to the session without a distinct identity/policy issue path and authoritative return loop.
- Why this is / is not agent-owned: prompts and guards state or enforce constraints, but the active Agent does not own a separate ultimate-policy decision right, and generic operator configuration is not promoted to parent S5.
- Evidence: `coding/systemprompt.go`, `coding/session.go`, `cmd/pi/main.go`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: the project has a clear product identity and upstream-parity policy at repository-development level, but those maintainer decisions are outside the assessed deployed session organization.

### Absence scope

- Surfaces inspected: system-prompt assembly/override, project trust, tool selection, model/thinking controls, SDK hooks, CLI commands, session persistence and repository maintenance/parity documentation.
- Plausible first-party paths checked: static/default identity text, custom/forced prompts, human/system override, trust gating, tool admission, model selection and maintainer parity policy.
- Why no material first-party path remains: all discovered mechanisms directly configure or constrain the session; none establishes runtime identity/ultimate-policy issue detection, legitimate S5 authority, authoritative decision and return-to-operation closure at the declared recursion.

## Recursion

The assessed recursion is one pi (Go) session. The model/tool loop is one operational S1. Tools and concurrent tool calls are lower-level action mechanisms, not separately evidenced viable operational organizations. External applications may compose multiple `Session` values, but such composition defines a new system-in-focus and is not inferred here.

## Variety and escalation

Operational variety is handled by the model, tool set, provider/model selection, persisted context, steering/follow-up messages, retries/cancellation and compaction. Tool failures return to the same model loop; user/embedder messages can steer or abort. These are useful escalation/control surfaces for the single S1 but do not, without function-specific evidence, establish S2-S5.

## Evidence gaps

No material unresolved evidence gap requires `?` at the frozen ref. The runtime/package boundary is explicit and broad enough to support the scoped negative findings. Downstream SDK compositions can add organizational actors, reviewers, adaptation or governance, but each such composition would require its own assessment boundary and evidence.
