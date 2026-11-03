---
harness_id: opengent
project_name: OpenGent
repository: https://github.com/samkerrcode/opengent
review_ref: f981d42614d49bda064c474587095a49a0c2bb28
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenGent

## Review boundary

- System in focus: OpenGent's shipped local desktop agent application and Rust agent-core runtime, not its contributor organization.
- Purpose and identity: Complete user-configured model/tool tasks with transparent progress and per-tool authority boundaries.
- Relevant environment: User, local files and MCP tools, OpenAI-compatible hosted/local model endpoint, desktop OS and persistent agent configuration.
- Standard-distribution boundary: Tauri desktop application, Rust `agent-core` coordinator, provider adapter, MCP manager, persisted chat/agent/schedule state and permission prompts.
- Credited operating / distribution surfaces: [agent/coordinator.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/coordinator.rs), [agent/tools.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/tools.rs), [mcp/manager.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/mcp/manager.rs), [agents/schedule.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agents/schedule.rs), [README](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/README.md).
- Adjacent first-party surfaces excluded from ownership: Cargo/desktop build tests and CI, product roadmap, mock provider tests and maintainer review are corroboration/development rather than runtime governance actors.
- First-party operating / deployment modes considered: Local desktop chats with user-selected providers/tools/permission modes; saved agents; scheduled runs after application restart. No independent cloud organization is supplied.
- Recursion level: One OpenGent-hosted application with individual task/chat runs as S1 units.
- Reviewed revision: `f981d42614d49bda064c474587095a49a0c2bb28`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`RunCoordinator` owns cancellation and per-chat run slots; its asynchronous loop streams provider responses, extracts tool calls, dispatches through a `ToolHost`, waits for individual user approval when policy requires, reinserts tool results and continues model turns. `McpManager` maintains real stdio/HTTP MCP connections and tool policies, including reapproval after a tool definition changes. SQLite stores chats, user-defined agents and schedule state; schedule catch-up/skip rules remain operator-selected. A simulated provider is included for tests, not counted as an autonomous operational actor. [coordinator.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/coordinator.rs#L305); [mcp/manager.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/mcp/manager.rs); [storage/agents.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/storage/agents.rs).

## Operational model

An individual chat/scheduled run transforms a user task into model-chosen tool actions and a terminal answer. The model makes the local task-dependent choice; the Rust runtime validates/blocks/executes, stores and returns observations. The human configures tools, agents and schedules and may approve a particular action, but is not replaced by a separate autonomous cross-run regulator. Multiple chat runs do not imply separate metasystem functions.

## S1 — Operations

- State: A
- Function: Model-led local task execution with tool-result feedback.
- Disturbance / variety regulated: Tool failures, unanticipated responses, model/provider errors, incomplete tasks and user-selected access constraints.
- Decisive decision or feedback right: Choose the next tool/action or conclude the task after seeing prior results.
- Decision owner: Configured model-driven chat agent, with human ownership of optional individual approvals.
- Supporting / enforcement mechanisms: Rust `RunCoordinator`, MCP tool catalog, dispatch policy, approval timeouts, cancellation, context limits and SQLite persistence.
- Closure path: Executed/denied tool results enter the conversation and can change the next model step; completed turn reaches a terminal response.
- Boundary reachability: Shipped `RunCoordinator::start` and `run_loop` wire provider stream into actual `execute_call`/tool results; this is not a test-only mocked workflow.
- Why this is / is not agent-owned: Without model discretion the host still enforces policies but cannot choose the task-sensitive sequence of actions.
- Evidence: [coordinator.rs#L305](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/coordinator.rs#L305), [coordinator.rs#L491](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/coordinator.rs#L491), [agent/mod.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/mod.rs).
- Basis: structural
- Confidence: high for the source-visible model/tool loop, not live task success.
- Caveats: A real provider and user-authorized MCP tools must be supplied; no provider task run was executed for this review.

## S2 — Coordination

- State: —
- Function: Regulation of interference between distinct S1 operational units.
- Disturbance / variety regulated: Potential simultaneous runs/shared tools and per-chat overlap checked within the desktop boundary.
- Decisive decision or feedback right: No separate inter-S1 conflict-adjustment decision was found.
- Decision owner: No S2-specific agent/constructor; host serialization and user configuration remain mechanisms.
- Supporting / enforcement mechanisms: Per-chat exclusivity slots, cancellation and stored scheduled jobs.
- Closure path: No demonstrated feedback relating one S1's interference to adjustments in another S1's subsequent behavior.
- Why this is / is not agent-owned: A mutex on the same chat and a schedule queue do not make a multi-unit conflict regulator.
- Evidence: [coordinator.rs#L78](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/coordinator.rs#L78), [schedule.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agents/schedule.rs).
- Basis: structural
- Confidence: medium-high for the reviewed distribution.
- Caveats: External users can coordinate multiple chat agents themselves.

### Absence scope

- Surfaces inspected: Coordinator per-chat slots and concurrency tests, agent schedules/storage, MCP manager and public desktop modes.
- Plausible first-party paths checked: Concurrent chats, scheduled agents, shared tool sessions, waiting/termination and operator intervention.
- Why no material first-party path remains: Those paths serialize execution or carry individual approvals; none supplies a function-specific inter-unit interference assessment and returned coordination choice.

## S3 — Inside-and-now control

- State: —
- Function: Current whole-application allocation/commitment regulation.
- Disturbance / variety regulated: Concurrent workload, model fallback, timeouts and permission limits.
- Decisive decision or feedback right: No shipped whole-system discretionary prioritization or corrective commitment right evidenced.
- Decision owner: User-selected schedule/configuration and deterministic local run controller, not a dedicated S3 agent or parent loop.
- Supporting / enforcement mechanisms: Run slots, fallback on provider error, step caps, per-tool approval and stored schedules.
- Closure path: Individual run enforcement/fallback closes locally without an app-wide view→decision→reallocation return.
- Why this is / is not agent-owned: Hard limits and operator-set priorities do not exercise whole-system managerial discretion.
- Evidence: [coordinator.rs#L305](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/coordinator.rs#L305), [storage/agents.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/storage/agents.rs).
- Basis: structural
- Confidence: medium-high.
- Caveats: Human management outside the app is not a first-party closed S3 parent mode.

### Absence scope

- Surfaces inspected: Agent run coordinator, schedules, persisted agents, tool access policy and application README.
- Plausible first-party paths checked: Per-chat contention, missed-job scheduling, failure fallback, human approval, user configurable budget and operator controls.
- Why no material first-party path remains: No operative cross-run current state and adaptive resource/commitment decision loop closes at application recursion; the shipped paths implement prior configuration or local recovery.

## S3* — Complementary audit

- State: —
- Function: Independent challenge to routine operational claims using complementary access.
- Disturbance / variety regulated: Incorrect but convincing agent outputs.
- Decisive decision or feedback right: No independent audit judgment with returned corrective authority is shipped.
- Decision owner: User can inspect visible traces; ordinary runtime records events, but neither is an independent S3* actor.
- Supporting / enforcement mechanisms: Streamed tool events, persisted transcripts, simulated-provider/CI tests and user approval cards.
- Closure path: No alternate outcome evidence→independent verdict→control correction path beyond the same run.
- Why this is / is not agent-owned: Transparent traces and routine tool-result checking repeat ordinary reporting, not independent audit.
- Evidence: [agent/recorder.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/recorder.rs), [domain/events.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/domain/events.rs), [README](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/README.md).
- Basis: structural
- Confidence: medium-high.
- Caveats: A downstream reviewer can audit exports, but no first-party independent corrective path was established.

### Absence scope

- Surfaces inspected: Recorder/event types, transcript storage, run coordinator, documented transparency UI, tests and policy grants.
- Plausible first-party paths checked: Tool-result observation, UI trace inspection, verification tests and permission challenges.
- Why no material first-party path remains: These are production observations, static enforcement or development validation; no protected separate inspection/judgment channel drives current-control correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: External/future-oriented adaptation of the harness's own capabilities.
- Disturbance / variety regulated: Provider/tool evolution, changing user needs and future capabilities.
- Decisive decision or feedback right: No first-party prospective adaptation decision returned to current capability.
- Decision owner: Developer/desktop user configures providers/tools and roadmap; task agent does not own capability evolution.
- Supporting / enforcement mechanisms: Provider registry, saved agents, on-demand MCP discovery, fallback models and schedules.
- Closure path: Configuration changes require user/developer selection; local task feedback does not establish prospective organizational adaptation.
- Why this is / is not agent-owned: Selecting a tool for the current task differs from researching future environment changes and installing a revised repertoire.
- Evidence: [providers/registry.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/providers/registry.rs), [agent/tools.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/tools.rs), [README](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/README.md).
- Basis: structural
- Confidence: medium-high.
- Caveats: A future plugin/application could add adaptation, outside the reviewed distribution.

### Absence scope

- Surfaces inspected: Provider registry, agent definitions, scheduler, MCP tool discovery and product roadmap.
- Plausible first-party paths checked: Model fallback, saved agent modification, tool-definition reapproval, tool search and maintainer planned adapters.
- Why no material first-party path remains: Runtime changes to current tool use and human edits are not a closed external-and-prospective option→capability loop.

## S5 — Policy and identity

- State: —
- Function: Identity and ultimate-policy resolution for the application.
- Disturbance / variety regulated: Potential changes to the product's governing purpose versus ordinary tool risk.
- Decisive decision or feedback right: No identity-level matter→legitimate decision→returned policy closure is implemented.
- Decision owner: Maintainer and desktop user set policies outside an S5 runtime path; tool approval is task-local.
- Supporting / enforcement mechanisms: Tool policy modes, per-call approval, secrets, static product configuration and user-defined agent instructions.
- Closure path: Tool grants/denials feed one tool request or persistent access settings, not a returned identity-level decision.
- Why this is / is not agent-owned: Even hard permission enforcement cannot determine the identity/ultimate policy of the system.
- Evidence: [mcp/permissions.rs](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/mcp/permissions.rs), [coordinator.rs#L587](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/crates/agent-core/src/agent/coordinator.rs#L587), [README](https://github.com/samkerrcode/opengent/blob/f981d42614d49bda064c474587095a49a0c2bb28/README.md).
- Basis: structural
- Confidence: medium-high.
- Caveats: The repository may have human maintainer governance, distinct from the installed app recursion.

### Absence scope

- Surfaces inspected: Product configuration, agents/settings, MCP policies, approval call handling and documented UI modes.
- Plausible first-party paths checked: Human approval and persistent grants, instructions, risk gating, project roadmap and maintainer contribution authority.
- Why no material first-party path remains: None routes an actual identity/ultimate-policy question to legitimate authority and returns a governing resolution into subsequent application operation.

## Recursion

Saved agents and chat runs may have durable tasks, but no complete lower-level metasystem or higher-level self-governed viability is established merely by their multiplicity.

## Variety and escalation

Provider/tool errors feed the local model loop, while policy denial and approval timeout safely attenuate tool-action variety. Human approval is an ordinary action-level return; stop/cancel and scheduler state are not independently algedonic or S5 evidence.

## Evidence gaps

This is pinned-source structural review, not live execution of a paid/local model or a macOS/Windows installer. It cannot establish model output quality, operational reliability or a separate organization-wide governance process beyond the shipped application.

## Verdict

**Included.** A reachable autonomous S1 model→tool→feedback loop is present. Additional VSM functions were not established at the reviewed first-party application boundary; human configuration and deterministic enforcement are not credited as autonomous management or ultimate-policy authority.
