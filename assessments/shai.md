---
harness_id: shai
project_name: SHAI
repository: https://github.com/ovh/shai
review_ref: f076f6128a826a96a28e47d0d674284b1552905e
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SHAI

## Review boundary

- System in focus: SHAI's first-party coding-agent runtime at frozen revision `f076f6128a826a96a28e47d0d674284b1552905e`, including the core agent state machine, coder runner, built-in filesystem/shell/fetch/todo tools, claim/permission handling, project-context loading, custom-agent configuration, CLI/headless/HTTP entry surfaces and HTTP session persistence.
- Purpose and identity: act as a terminal or service-hosted coding assistant that can autonomously inspect and modify a project, execute commands and continue from tool results while remaining externally controllable.
- Relevant environment: user coding requests, repository/filesystem state, shell/build/runtime output, configured LLM providers, MCP services, project `SHAI.md` context and optional HTTP clients.
- Standard-distribution boundary: repository-owned SHAI core/CLI/HTTP composition is inside. LLM providers and MCP servers are dependencies and cannot donate organizational functions. Repository-development CI/tests and maintainer governance are adjacent.
- Credited operating / distribution surfaces: interactive CLI, headless stdin mode, persistent/ephemeral HTTP sessions, coder runner, built-in tools, claim/permission path, custom-agent configuration and project-context loading.
- Adjacent first-party surfaces excluded from ownership: repository-development tests/CI, contributor/release governance, examples, and shell/client code that merely invokes the same focal agent without adding a distinct organizational function.
- First-party operating / deployment modes considered: interactive terminal coding, headless coding, OpenAI-compatible HTTP service with persistent or ephemeral sessions, and custom configured agent instances.
- Recursion level: one SHAI agent session is the focal S1 operational unit. Tool coroutines, HTTP requests and configured provider/MCP adapters are mechanisms or dependencies, not separate S1 units by themselves.
- Reviewed revision: `f076f6128a826a96a28e47d0d674284b1552905e`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

SHAI exposes one model-driven agent core with an asynchronous state machine. The Brain chooses whether to continue reasoning, invoke tools or pause for external input; the tool layer executes filesystem, shell, fetch, todo and optional MCP actions and returns their results to the same trace. The controller protocol can cancel, query state, provide user input and participate in permission handling.

The coder runner packages that core for software-engineering work. CLI and headless modes invoke the same underlying agent, while the HTTP service can host multiple persistent or ephemeral sessions. Session persistence serializes conversation traces and can restore a later session, but the manager's `max_sessions` check is a static admission cap rather than a distinct discretionary whole-system current-control loop.

## Operational model

A user request enters one SHAI agent. The model receives the current trace and available tools, selects the next action, observes concrete tool results, and continues until the state machine reaches a terminal or externally paused condition. External controllers can inject input, grant permissions or cancel the run. Persistent HTTP mode can reload an earlier trace into a new agent instance.

## S1 — Operations

- State: A
- Function: autonomously perform coding work by selecting and revising model/tool actions against the live project environment.
- Disturbance / variety regulated: unfamiliar codebases, changing file state, command failures, incomplete context, model/tool errors, permission requirements and user corrections.
- Decisive decision or feedback right: choose the next reasoning/tool action, interpret returned evidence, continue or pause, and revise subsequent work until the coding request is complete or terminated.
- Decision owner: the active model-backed SHAI Brain.
- Supporting / enforcement mechanisms: agent state machine, coder prompt/runner, filesystem/shell/fetch/todo/MCP tools, claim manager, controller protocol, project-context loading and provider adapters.
- Closure path: user/project context → model chooses action/tool → tool or environment returns evidence → evidence is appended to the trace → model chooses the next action until terminal completion, pause or cancellation.
- Boundary reachability: interactive CLI, headless mode and HTTP sessions all instantiate the repository-owned agent core/coder runner directly; no adjacent development workflow is required.
- Why this is / is not agent-owned: removing the model actor leaves the state machine, tools and controller but removes the open-ended coding decisions that turn observations into subsequent actions.
- Evidence: README; `shai-core/src/agent/README.md`; `shai-core/src/agent/agent.rs`; `shai-core/src/agent/brain.rs`; `shai-core/src/runners/coder/coder.rs`; built-in tool implementations.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external providers supply inference and MCP services may add tools, but their internal behavior is not credited to SHAI.

## S2 — Coordination

- State: —
- Function: no distinct inter-S1 coordination function is established.
- Disturbance / variety regulated: concurrent tool calls and multiple HTTP sessions exist, but they are not evidenced as distinct S1 units whose mutual interference is regulated through a coordination loop.
- Decisive decision or feedback right: no S2-specific decision over a concrete inter-S1 conflict or oscillation was found.
- Decision owner: not established at S2 level.
- Supporting / enforcement mechanisms: async tool aggregation, per-session controller locking, session IDs and request serialization.
- Closure path: these mechanisms serialize or isolate work inside individual sessions; they do not close a peer coordination relation among distinct operational units.
- Why this is / is not agent-owned: concurrency and session isolation are implementation mechanisms, not evidence of S2 by themselves.
- Evidence: agent architecture README; `shai-core/src/agent/agent.rs`; `shai-http/src/session/session.rs`; `shai-http/src/session/manager.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: separately launched SHAI agents could be composed externally, but no first-party coordination relation among them is supplied in the frozen standard distribution.

### Absence scope

- Surfaces inspected: agent state machine, concurrent tool execution, CLI/headless paths, HTTP session manager, persistent sessions, custom-agent configuration and MCP integration.
- Plausible first-party paths checked: concurrent tools as peer S1 units; multiple HTTP sessions as S1 peers; controller locking as S2; MCP/custom agents as coordination.
- Why no material first-party path remains: the reviewed runtime isolates or serializes sessions and tools but does not expose a specific peer interference/attenuation/feedback path at the declared recursion.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established.
- Disturbance / variety regulated: session cancellation, permission handling and a configured maximum session count constrain current execution, but they do not provide substantive whole-system resource/commitment management.
- Decisive decision or feedback right: no separate actor observes the whole set of current operations and makes discretionary choices over shared priorities, resources, commitments or interventions on behalf of the whole.
- Decision owner: not established at S3 level.
- Supporting / enforcement mechanisms: HTTP session map, static `max_sessions` limit, per-session controller lock, cancel/state protocol and permission handling.
- Closure path: the session manager deterministically accepts a new session when below a configured count and rejects it when full; session-local controller actions affect only the focal agent.
- Why this is / is not agent-owned: the hard concurrency cap enforces a configured limit but does not supply the whole-current decision authority required for S3.
- Evidence: `shai-http/src/session/manager.rs`; `shai-http/src/session/session.rs`; `shai-core/src/agent/protocol.rs`; `shai-core/src/agent/claims.rs`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an external service operator may choose configuration and terminate sessions, but generic operational administration is not a first-party S3 closure at this boundary.

### Absence scope

- Surfaces inspected: session manager and lifecycle, static session-cap configuration, agent controller protocol, permissions/claims, HTTP cancellation, CLI/TUI control surfaces and provider/custom-agent configuration.
- Plausible first-party paths checked: `SessionManager` as S3; `max_sessions` as resource admission; external controller as parent S3; permission manager as current-control authority.
- Why no material first-party path remains: the only cross-session view is a count/map used for static admission and lifecycle bookkeeping; there is no substantive whole-system current view plus discretionary control over shared current commitments/resources.

## S3* — Complementary audit

- State: —
- Function: no complementary audit path distinct from ordinary production feedback is established.
- Disturbance / variety regulated: shell output, tool results, traces and repository tests can reveal mistakes, but the same coding agent consumes these as ordinary operational evidence.
- Decisive decision or feedback right: no separate auditor owns an independent claim-checking judgment that returns findings into current control.
- Decision owner: not established at S3* level.
- Supporting / enforcement mechanisms: tool result events, trace logging, shell/build execution, repository tests and HTTP event streams.
- Closure path: execution evidence returns directly into the same agent trace or external client; no separate complementary-access audit loop is supplied.
- Why this is / is not agent-owned: routine self-checking and observability do not establish S3*.
- Evidence: `shai-core/src/agent/events.rs`; built-in tools; agent output/logging; repository tests; HTTP event logging.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: users may independently inspect results, but no first-party reviewer/evaluator runtime closes that path.

### Absence scope

- Surfaces inspected: agent events/logging, shell/file tools, coder runner, HTTP session/event surfaces, repository tests and trace output.
- Plausible first-party paths checked: trace replay as audit; shell/build results as verifier; repository tests as reviewer; HTTP observers as complementary access.
- Why no material first-party path remains: each path is routine production evidence, observability or adjacent development testing rather than a distinct sufficiently independent audit relation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop is established.
- Disturbance / variety regulated: persistent traces, project `SHAI.md`, custom agent configs, provider selection and MCP configuration can influence later sessions.
- Decisive decision or feedback right: no first-party process senses future/external change, develops adaptation options for SHAI and returns a selected option into current organizational capability.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: session persistence, project context files, custom-agent configuration, provider/model selection and MCP configuration.
- Closure path: stored traces/configuration are replayed or loaded into later operational runs; they do not form an external-and-prospective adaptation conversation.
- Why this is / is not agent-owned: persistence and extensibility change context/capabilities only when supplied by users/configuration and do not autonomously generate future-oriented adaptation options.
- Evidence: README; `SHAI.md`; `shai-http/src/session/persist.rs`; `shai-core/src/config/agent.rs`; MCP configuration.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external operators can create new agent configurations, but generic configurability is not S4.

### Absence scope

- Surfaces inspected: persistent sessions, custom-agent configs, project context, provider/model configuration, MCP integration, shell assistant and HTTP service modes.
- Plausible first-party paths checked: trace persistence as learning; custom agents as adaptation; MCP/provider changes as environmental intelligence; shell-error analysis as S4.
- Why no material first-party path remains: inspected paths reuse current/history context or operator-specified configuration and do not generate/close prospective adaptation options for the harness.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level closure is established.
- Disturbance / variety regulated: tool claims, sudo mode, permission requests, agent configuration and external controller commands constrain ordinary task execution.
- Decisive decision or feedback right: no identity/ultimate-policy issue is routed to legitimate ultimate authority and returned as a durable governing decision for SHAI.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: `ClaimManager`, sudo/no-sudo mode, permission protocol, custom-agent config and user/project context.
- Closure path: permissions and controller commands allow or deny current actions, but do not settle identity-level policy questions for subsequent system operation.
- Why this is / is not agent-owned: guardrails and ordinary approval are execution constraints, not S5.
- Evidence: `shai-core/src/agent/claims.rs`; `shai-core/src/agent/agent.rs`; protocol/configuration surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: maintainers and service operators have governance authority outside the focal runtime, but that adjacent authority is not an operational S5 loop.

### Absence scope

- Surfaces inspected: claims/permissions, sudo mode, protocol commands, custom-agent config, project context, HTTP administration and repository governance.
- Plausible first-party paths checked: permission approval as S5; sudo mode as policy; agent config as identity; service operator cancellation as ultimate authority; maintainer governance as runtime S5.
- Why no material first-party path remains: these mechanisms bound ordinary operations/configuration or belong to adjacent development/service governance; no identity-policy issue/authority/return loop is present.

## Recursion

The reviewed standard distribution contains one focal model/tool agent per session. Multiple sessions may coexist, but coexistence alone does not establish a higher viable-system recursion, and no first-party cross-session metasystem is evidenced.

## Variety and escalation

SHAI absorbs task variety through model/tool iteration, user input, provider/MCP tools and project context. Permission-requiring actions can pause for external approval, and the controller can cancel a run. These are operational escalation paths rather than separate S3–S5 functions.

## Evidence gaps

No `?` state is required. The frozen repository exposes the complete focal agent loop, controller/permissions, serving/session lifecycle and configuration surfaces broadly enough to support S1 and the negative higher-function findings.

## Assessment summary

SHAI closes autonomous S1 through its first-party model/tool coding loop. Concurrent tools and sessions do not establish S2; static session admission and local control do not form S3; traces/tests are not complementary S3*; persistence/configuration do not provide S4; and permissions/sudo/configuration do not close S5.

**Vector:** A · — · — · — · — · —
