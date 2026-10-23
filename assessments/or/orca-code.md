---
harness_id: orca-code
project_name: Orca Code
repository: https://github.com/Nethyric/orca-code
review_ref: 953c73b6d14cf50b2229302acb64df59561c235f
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Orca Code

## Review boundary

- System in focus: Orca Code's first-party Go terminal coding agent at frozen `Nethyric/orca-code@953c73b6d14cf50b2229302acb64df59561c235f` (release 1.0.0).
- Purpose and identity: execute a user coding task against one local working directory through a model-selected sequence of repository file/search/shell/web actions, with approval, undo and context/cost limits.
- Relevant environment: local repository contents, model/provider replies, user prompts, tool execution outcomes, permissions, trust state, external web results and command/file errors.
- Standard-distribution boundary: shipped `cmd/orca` interactive/one-shot CLI, single `internal/agent` model/tool loop, standard-library providers, first-party tool registry, security/permission policy, configuration, JSONL session writing and terminal UI.
- Credited operating / distribution surfaces: `cmd/orca/`, `internal/agent/`, `internal/provider/`, `internal/tools/`, `internal/permissions/`, `internal/security/`, `internal/config/`, `internal/session/` and supported CLI modes.
- Adjacent first-party surfaces excluded from ownership: Go source/unit tests as product-control actors; planned desktop/daemon/event protocol, OS sandbox, MCP, LSP and parallel subagents; product/competitive research documents; external provider hosts, user-written verify commands and upstream maintainer governance.
- Reviewed modes: REPL and one-shot CLI; default, acceptEdits, plan and yolo permissions; project-trusted hooks/verify command; bounded tool/model turns and context compaction.
- Recursion level: one operating Orca coding session with **one** independently deciding model actor; not a future daemon, external editor organization or multiple unrelated terminals.
- License screen: frozen root `LICENSE` contains MIT License text and repository metadata reports MIT; public-source candidate eligible.
- Observation date: 2026-10-23; Profile `0.2.4`; Methodology `0.3.7`.

## Repository architecture

`internal/agent.Agent.Run` implements a first-party provider → tool use → permission check → tool execution → tool-result feedback cycle. The active model independently chooses `read_file`, search, write/edit, shell, web, todo and other registered operations, observes new results and can iterate up to a fixed turn limit. `execTool` checks a policy verdict and obtains human consent if requested; a trusted optional `verify_command` runs after successful file writes and returns any failure to the **same** acting model. Undo groups changes by the current turn, and usage/cost guardrails are deterministic.

The checked-in architecture contract is particularly explicit about implemented versus planned functionality. A future desktop/daemon event bus, local IPC, LSP/MCP, OS-native sandbox and parallel agent population are a **target**, not shipped code. The quality-assurance matrix also lists subagents and Git review UI as roadmap items. The shipped runtime therefore presents one S1 agent and constrained tools, rather than distinct parallel S1s with S2 coordination, a whole-current S3 manager, an independently operated S3* auditor, external/prospective S4, or legitimate ultimate S5.

Frozen sources: [`internal/agent/agent.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/agent/agent.go), [`internal/tools/registry.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/tools/registry.go), [`internal/permissions/permissions.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/permissions/permissions.go), [`internal/config/config.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/config/config.go), [`docs/orca-architecture.md`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/docs/orca-architecture.md), [`docs/qa-matrix.md`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/docs/qa-matrix.md).

## Operational model

The main model adjusts repository work based on tool results (S1=A). Permission enforcement, context pruning, command guardrails and cost/turn caps are constraints on its decisions, not independently autonomous VSM functions. A single sequential model actor has no distinct-S1 coordination disturbance (S2=—), and per-turn interruptions do not entail present whole-cohort management (S3=—). Same-model post-edit verification is ordinary validation, not complementary S3* audit. A future architecture sketch and product research do not count as deployed adaptation (S4=—). Human tool approval and local trust do not close organizational identity policy (S5=—).

## S1 — Operations

- State: A
- Function: interpret a software-engineering request and select coding-tool actions until completion or bounded stop.
- Disturbance / variety regulated: changing files, unknown code structure, ambiguous user requests, tool failures, model/provider uncertainty and validation errors.
- Decisive decision or feedback right: the model chooses tool names/arguments and subsequent steps after each file, command, web or verification result.
- Decision owner: one first-party model-backed Orca session actor.
- Supporting / enforcement mechanisms: provider adapters, tool registry and run functions, permission requester, working-directory guard, user prompt, session JSONL, undo, token/cost limits and compaction.
- Closure path: user task → model response/tool uses → permission and tool execution → tool result returned to model → revised tool choice or final answer.
- Boundary reachability: the supported Go CLI/REPL constructs `Agent` with real provider, tool context, permissions and UI; `Run` enacts the full loop in the default distribution.
- Why this is / is not agent-owned: the model decides what to inspect/change/test in response to fresh outcomes; the Go execution loop alone does not supply those task-level judgments.
- Evidence: [`internal/agent/agent.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/agent/agent.go), [`internal/tools/registry.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/tools/registry.go), [`cmd/orca/main.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/cmd/orca/main.go).
- Basis: frozen source and deterministic first-party Go tests, no live LLM agent execution.
- Confidence: high for the shipped operational loop, not a measure of task success.
- Caveats: third-party model providers are required to make actual coding decisions; source-only tests do not establish field effectiveness.

## S2 — Coordination

- State: —
- Function: no interference-damping relationship among distinct independently deciding S1 operations is shipped at this session boundary.
- Disturbance / variety regulated: parallel agents might collide in hypothetical future deployments, but the frozen product does not instantiate a parallel population.
- Decisive decision or feedback right: the main agent chooses tools sequentially; a deterministic `for` loop executes returned tool uses and the tool registry contains no built-in delegated independent actor.
- Decision owner: no first-party S2 owner established.
- Supporting / enforcement mechanisms: sequential tool results, todo text, turn limit, single process permissions and tool confinement.
- Closure path: model-generated tool uses are executed serially and reported to the same model; there is no second S1 whose interference requires coordination.
- Why this is / is not agent-owned: sequencing actions of a single model is not conflict attenuation among independent operational actors; planned parallel agents cannot be credited.
- Evidence: [`internal/agent/agent.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/agent/agent.go), [`docs/orca-architecture.md`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/docs/orca-architecture.md).
- Basis: direct source and explicitly segregated product roadmap.
- Confidence: high.
- Caveats: tools can perform process-level work, but subprocesses are not separate autonomous S1 actors.

### Absence scope

- Surfaces inspected: core model/tool loop, complete tool registry, CLI mode construction, todo, session, permissions and future architecture.
- Plausible first-party paths checked: parallel returned tool calls, shell subprocesses as S1s, queue/loop as coordination, future multi-agent architecture and planned daemon.
- Why no material first-party path remains: no separately model-backed child runtime or cross-worker interference detection/attenuation is instantiated at the frozen source.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current control over a population of active independently operating units with resource/priority/commitment intervention rights is demonstrated.
- Disturbance / variety regulated: token/cost growth, editing risk or a bad command affects one task stream, but no current multi-unit portfolio is managed.
- Decisive decision or feedback right: humans allow/deny individual tools; deterministic limits stop the current loop. No controller reallocates resources or selectively revises commitments among multiple S1s.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: usage counters, cost estimate, `MaxTurns`, mode flags, per-tool approvals and UI warnings.
- Closure path: fixed cost/turn checks can end one execution; no current whole-system view → chosen cross-unit intervention → changed subsequent S1 operations path exists.
- Why this is / is not agent-owned: cost caps and tool veto are enforcement on a single S1 session, not a current metasystemic management actor.
- Evidence: [`internal/agent/agent.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/agent/agent.go), [`internal/permissions/permissions.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/permissions/permissions.go).
- Basis: bounded negative structural review.
- Confidence: high at one-session recursion.
- Caveats: the user could supervise multiple independently launched sessions externally; this is not first-party S3.

### Absence scope

- Surfaces inspected: command/turn caps, cost/usage, permission UI, session JSONL, CLI/one-shot operation and future daemon plan.
- Plausible first-party paths checked: cost limit as resource control, permission modal as S3, single-session todos as current portfolio, planned daemon as live manager.
- Why no material first-party path remains: no roster of simultaneous S1 commitments, dynamic resource bargaining or selectable cohort-level intervention with returned operating change.

## S3* — Complementary audit

- State: —
- Function: no independent complementary access to code-action claims with findings returned into a distinct accountable current-control decision path.
- Disturbance / variety regulated: bad edits or unsupported success claims can occur, but an ordinary verify command does not create independent audit ownership.
- Decisive decision or feedback right: optional trusted `verify_command` runs after an edit and reports failures to the **same** model; unit tests and prospective Git review features do not alter this fact.
- Decision owner: same S1 agent handles routine verification; no S3* auditor established.
- Supporting / enforcement mechanisms: trusted project hook, command stdout/stderr return, session JSONL and ordinary test/build commands.
- Closure path: edit → configured verification command → failure text appended to the producer's tool result → same producer chooses a repair; no complementary independent auditor → S3 corrective control.
- Why this is / is not agent-owned: the verify command is a fixed user-configured checker, not an independently deciding reviewer with alternate operational access.
- Evidence: [`internal/agent/agent.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/agent/agent.go), [`internal/config/config.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/config/config.go), [`docs/qa-matrix.md`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/docs/qa-matrix.md).
- Basis: frozen runtime and roadmap/feature contrast.
- Confidence: high.
- Caveats: a GitHub action or separate reviewer outside this source could independently audit Orca output, but its judgment and closure are not shipped in the assessed harness.

### Absence scope

- Surfaces inspected: post-edit verification, hooks, session events, test suite, permissions and roadmap Git review UI.
- Plausible first-party paths checked: verify-command failures, event JSONL as audit path, Go tests, user approval, future Git review interface.
- Why no material first-party path remains: these paths are ordinary producing-agent validation or unimplemented proposals, with no distinct audit access, owner or control return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped future-facing sensing and capability-redesign loop through present management is identified.
- Disturbance / variety regulated: external developer trends, changing APIs and future product opportunities appear in repository research documents but not in an operating adaptation process.
- Decisive decision or feedback right: the model can fetch web pages for current coding tasks; future architecture and competitive positioning are decisions of maintainers outside the runtime boundary.
- Decision owner: none established for prospective S4.
- Supporting / enforcement mechanisms: web tool, project context, competitive research Markdown and target-architecture roadmap.
- Closure path: current web observations inform current task actions; no external/future modeling → adaptation options → present capability redesign dialogue with S3 is wired.
- Why this is / is not agent-owned: a research document and generic browsing do not create an operating strategic-intelligence organization.
- Evidence: [`docs/orca-competitive-research.md`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/docs/orca-competitive-research.md), [`docs/orca-architecture.md`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/docs/orca-architecture.md), [`internal/tools/web.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/tools/web.go).
- Basis: bounded source/document review.
- Confidence: high for non-shipped planning distinction.
- Caveats: documentation may guide future maintainer development but is not autonomous S4 in a user coding session.

### Absence scope

- Surfaces inspected: current web/search tools, competitive research, roadmap, planned protocol and current session/tool context.
- Plausible first-party paths checked: general web fetch as external horizon scan, roadmap as S4, provider support as strategic choice, compaction as learning.
- Why no material first-party path remains: none shows a prospective adaptation-option process with a return that changes live harness capability through current management.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate system-identity policy decision coupled to operating management/intelligence is shown.
- Disturbance / variety regulated: malicious files, unsafe shell commands and untrusted project hooks need tactical restrictions, not constitutional S5 decisions.
- Decisive decision or feedback right: the operator selects modes, approves commands and explicitly trusts a repository; static guard rules gate files/processes. No in-session actor deliberates identity/purpose or an S3/S4 balance.
- Decision owner: none established for S5 at the chosen recursion.
- Supporting / enforcement mechanisms: project trust flag, path/SSRF/command guards, permission rules, `plan`/`yolo` modes, key store.
- Closure path: requested operation → configured guard or human consent → allowed/denied effect; no identity proposal → legitimate ultimate authority → durable organizational return is implemented.
- Why this is / is not agent-owned: trust and per-tool approval are granular operational safety constraints, not organizational purpose/identity governance.
- Evidence: [`internal/permissions/permissions.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/permissions/permissions.go), [`internal/security/paths.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/security/paths.go), [`internal/config/config.go`](https://github.com/Nethyric/orca-code/blob/953c73b6d14cf50b2229302acb64df59561c235f/internal/config/config.go).
- Basis: first-party static policy path versus absent identity decision closure.
- Confidence: medium-high.
- Caveats: upstream maintainers determine future Orca releases; their policies are not operating-session S5.

### Absence scope

- Surfaces inspected: all four permission modes, repository trust, guard functions, key store, session logging and future protocol statements.
- Plausible first-party paths checked: human approval as S5, threat-model policy as identity, roadmap values as top policy, maintainer governance as embedded runtime S5.
- Why no material first-party path remains: operating controls authorize individual actions and configuration only, without legitimate ultimate identity arbitration and an S3/S4 return.

## Distributed OSS parent arrangement

Orca maintainers may plan desktop/MCP/sandbox functionality and publish product research, but those actions are not an evidenced first-party parent metasystem coupled into a current operator session. No future module or separate process is credited before it exists and has an operating control return.

## Self-hosted and non-human modes

Both interactive and one-shot modes instantiate one model/tool S1 loop. A project trust gate determines whether post-edit command hooks are applied. Plan/yolo vary action permissions rather than ownership of higher VSM functions. A daemon protocol, parallel agent swarm and independent review interface are future architecture only.

## Recursion

One Orca runtime agent acts as S1 at the assessed task/session recursion. The repository, OS shell processes, provider endpoints and speculative future daemon are not nested independent viable subsystems in this frozen implementation.

## Variety and escalation

Tool errors, failed verify hooks and cost warnings return to the producing model or human consent gate. No distinct operational-unit contention is damped through S2, and no whole-cohort live control, complementary audit, prospective capability negotiation or identity-policy channel is wired.

## Evidence gaps

- No live LLM agents were tested: **deterministic Go tests only**. First-party `go test ./...` passes with local loopback available for provider test-server fixtures; this is not a model task-effectiveness measure.
- Planned desktop/daemon/IPC, MCP/LSP, OS sandbox, subagents and Git-review UI cannot be promoted into current VSM functions.
- The optional trusted verification hook is ordinary same-agent validation, not a mandatory independent reviewer.
