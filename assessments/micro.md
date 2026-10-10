---
harness_id: micro
project_name: Micro
repository: https://github.com/rmonvfer/micro
review_ref: 563dc1e6a6957cefbcfdd503fc5c4b754dfc5240
reviewed_at: 2026-10-10
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

# Micro

## Review boundary

- System in focus: first-party native Rust terminal coding agent, its model-selected repository tools, OS-sandboxed shell, session/ledger, optional confined extension host, interactive/headless local or RPC control.
- Purpose and identity: carry out software coding requests in a user project with explicit permission and inspectable execution.
- Relevant environment: source workspace, terminal command outcomes, model provider, application extension callbacks, user approval and persistent local session history.
- Standard-distribution boundary: shipped Micro CLI and agent. The Codex-derived OS sandbox is a supporting borrowed implementation, not an imported model-driven coding loop or metasystem decision owner; optional external extensions and provider internals are not counted.
- Credited operating / distribution surfaces: crates/micro-agent, crates/micro-tools, crates/micro-cli and its runtime wiring, crates/micro-session and first-party sandbox/capability broker.
- Adjacent first-party surfaces excluded from ownership: released installer/update checking, GitHub CI, user scripts in examples, external provider decisions, README descriptions without runtime linkage, unrelated independently started Micro sessions.
- First-party operating / deployment modes considered: CLI interactive and --print headless coding, session continuation/fork, source/shell tool actions, default workspace-write sandbox, optional confined TypeScript extension process, locally exposed remote control.
- Recursion level: a local coding session with one model-directed operational S1. RPC clients, tools, session branches, extension workers and detached OS shell processes are not second code-owning autonomous S1 cells.
- Reviewed revision: 563dc1e6a6957cefbcfdd503fc5c4b754dfc5240.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Micro's first-party Rust core owns its own streaming model/tool loop: request provider inference, execute native read/write/search/bash tools, return outcomes into conversation, and continue until tool calls stop. A session carries history and may enforce a dollar-denominated spend ceiling; append-only records preserve request/tool/policy evidence, including hashed provider request content. Persistent session forks preserve prior history but do not launch multiple active independent agents.

The default command sandbox combines host OS confinement with built-in file and protected path guards. External TypeScript extensions are isolated in a confined Bun process and use a capability broker that enforces host approval and sandbox restrictions. The repository includes examples with hooks and custom policies, but these are optional scripts and cannot be assumed to supply a packaged independent audit, policy or coordination organization. Source code implementing a sandbox partly derived from Codex is a supporting subsystem; the agent itself executes its own native first-party tool loop.

Multi-tool execution modes or many remote-connected sessions do not prove first-party inter-S1 coordination, and ordinary session-level spending and safety gates do not provide an autonomous whole-current regulatory actor. Likewise a rich policy/event ledger supports traceability without owning audit decisions. Persistent memory/compaction and version update checking do not create prospective S4 strategic authority.

Primary source evidence: [crates/micro-agent/src/lib.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-agent/src/lib.rs); [crates/micro-tools/src/files.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-tools/src/files.rs); [crates/micro-tools/src/bash.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-tools/src/bash.rs); [crates/micro-session/src/tree.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-session/src/tree.rs); [crates/micro-cli/src/main.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-cli/src/main.rs).

## Operational model

Model decisions drive real coding operations. Sandboxed tools and extension capabilities constrain action rights while the session log records their outcomes. No second separately owning coding S1, autonomous inside/current manager, independent complementary auditor, future-environment strategy owner or ultimate policy governance actor is verified for the packaged local session.

## S1 — Operations

- State: A
- Function: Model-selected coding actions on real source files and shell tasks.
- Disturbance / variety regulated: Changing user requirements, source observations and tool/test errors.
- Decisive decision or feedback right: Model chooses next tool operation or finish from observed results.
- Decision owner: First-party micro-agent runtime with provider-backed model.
- Supporting / enforcement mechanisms: Native Rust tools, provider streaming, file/search/bash tool set and prompt context.
- Closure path: Prompt → model response with tool calls → native executable tool → result stored in conversation → model continues or finishes.
- Boundary reachability: The installed CLI/headless runtime calls first-party micro-agent's model/tool loop, dispatching native tools inside the selected sandbox.
- Why this is / is not agent-owned: Model selects bounded coding work; sandbox is the enforcement surface.
- Evidence: [crates/micro-agent/src/lib.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-agent/src/lib.rs); [crates/micro-tools/src/files.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-tools/src/files.rs); [crates/micro-tools/src/bash.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-tools/src/bash.rs); [crates/micro-cli/src/main.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-cli/src/main.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Findings are scoped to installed first-party coding runtime rather than external user-built workgroups.

## S2 — Coordination

- State: —
- Function: No shipped coordination decision across two separately operating S1 units at the selected local coding-session recursion.
- Disturbance / variety regulated: Multiple ordinary file/shell tools and session forks do not equal active independent operational cells.
- Decisive decision or feedback right: No inter-S1 collision judgment or active corrective coordination choice.
- Decision owner: Absent in standard single-agent execution.
- Supporting / enforcement mechanisms: Parallel/sequential tool modes, message/session tree, protected file access and extension event hooks.
- Closure path: Concurrent tool requests return to the same agent turn; no first-party cross-agent interference feedback exists.
- Why this is / is not agent-owned: Tool scheduling, branchable history and external RPC sessions do not create a first-party coordinated fleet.
- Evidence: [crates/micro-agent/src/lib.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-agent/src/lib.rs); [crates/micro-session/src/tree.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-session/src/tree.rs); [crates/micro-tools/src/lib.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-tools/src/lib.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Findings are scoped to installed first-party coding runtime rather than external user-built workgroups.

### Absence scope

- Surfaces inspected: Native agent loop, file/shell tools, sessions, extension capability broker, provider configuration, OS sandbox and operational policy/ledger.
- Plausible first-party paths checked: A distinct owner making S2-specific discretionary decisions, with independently gathered evidence and a feedback return into operational coding at this selected recursion.
- Why no material first-party path remains: Actual mechanisms are local single-agent task feedback, deterministic guardrails, persisted traces or user-directed settings rather than a complete separately deciding organizational function.

## S3 — Inside-and-now control

- State: —
- Function: No separately owned inside-and-now management of multiple coding S1 units.
- Disturbance / variety regulated: Task budget, tool timeouts and session health are local execution disturbances.
- Decisive decision or feedback right: Runtime enforces individual budget/sandbox/permissions; operator may intervene.
- Decision owner: Human plus deterministic limits, not separate current-control actor.
- Supporting / enforcement mechanisms: Session-level spending limit, tool completion, cancellation, run state and log.
- Closure path: Budget/timeouts stop the same single-agent loop, without governing a distinct set of active S1 commitments.
- Why this is / is not agent-owned: Observability and spending controls do not prove whole-current decision ownership.
- Evidence: [crates/micro-agent/src/lib.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-agent/src/lib.rs); [crates/micro-cli/src/main.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-cli/src/main.rs); [crates/micro-session/src/lib.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-session/src/lib.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Findings are scoped to installed first-party coding runtime rather than external user-built workgroups.

### Absence scope

- Surfaces inspected: Native agent loop, file/shell tools, sessions, extension capability broker, provider configuration, OS sandbox and operational policy/ledger.
- Plausible first-party paths checked: A distinct owner making S3-specific discretionary decisions, with independently gathered evidence and a feedback return into operational coding at this selected recursion.
- Why no material first-party path remains: Actual mechanisms are local single-agent task feedback, deterministic guardrails, persisted traces or user-directed settings rather than a complete separately deciding organizational function.

## S3* — Complementary audit

- State: —
- Function: No independent complementary review of the coding agent's operating evidence followed by a corrective directive.
- Disturbance / variety regulated: Source edits can introduce defects; sandbox refusals and checks serve operational safety rather than independent audit.
- Decisive decision or feedback right: Policy/sandbox guards and optional extension callbacks deny/observe particular actions, without auditor judgment.
- Decision owner: First-party deterministic guards and user-supplied extensions; coder owns task corrections.
- Supporting / enforcement mechanisms: Sandbox guard/command admission, ledger, extension broker and system/tool results.
- Closure path: Policy denial/extension result enters the existing coding conversation; no separate auditor independently scrutinizes source and assigns repair.
- Why this is / is not agent-owned: Inspectable evidence logs and sandbox policy are not a reviewer with independent source evidence and closed feedback.
- Evidence: [crates/micro-tools/src/guard.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-tools/src/guard.rs); [crates/micro-tools/src/access.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-tools/src/access.rs); [crates/micro-cli/src/extensions.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-cli/src/extensions.rs); [crates/micro-agent/src/lib.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-agent/src/lib.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Findings are scoped to installed first-party coding runtime rather than external user-built workgroups.

### Absence scope

- Surfaces inspected: Native agent loop, file/shell tools, sessions, extension capability broker, provider configuration, OS sandbox and operational policy/ledger.
- Plausible first-party paths checked: A distinct owner making S3*-specific discretionary decisions, with independently gathered evidence and a feedback return into operational coding at this selected recursion.
- Why no material first-party path remains: Actual mechanisms are local single-agent task feedback, deterministic guardrails, persisted traces or user-directed settings rather than a complete separately deciding organizational function.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective environmental intelligence leading to first-party strategic capability renewal.
- Disturbance / variety regulated: Future provider/runtime changes and evolving software environment require strategy decisions beyond one present coding task.
- Decisive decision or feedback right: User selects providers/extensions; update checker informs installation state, not agent-owned strategy.
- Decision owner: No independent S4 owner.
- Supporting / enforcement mechanisms: Model/provider selection, compaction, skills/project prompts, installer update check.
- Closure path: Configuration/notes influence later turns, but no autonomous environmental options decision alters organization capabilities.
- Why this is / is not agent-owned: Historical memory, context and extension support do not constitute a complete outside-and-then system.
- Evidence: [crates/micro-cli/src/main.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-cli/src/main.rs); [crates/micro-agent/src/summarizer.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-agent/src/summarizer.rs); [crates/micro-config/src/lib.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-config/src/lib.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Findings are scoped to installed first-party coding runtime rather than external user-built workgroups.

### Absence scope

- Surfaces inspected: Native agent loop, file/shell tools, sessions, extension capability broker, provider configuration, OS sandbox and operational policy/ledger.
- Plausible first-party paths checked: A distinct owner making S4-specific discretionary decisions, with independently gathered evidence and a feedback return into operational coding at this selected recursion.
- Why no material first-party path remains: Actual mechanisms are local single-agent task feedback, deterministic guardrails, persisted traces or user-directed settings rather than a complete separately deciding organizational function.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/purpose policy decision with binding organizational return.
- Disturbance / variety regulated: Sandbox restrictions, workspace trust and capabilities concern present command safety.
- Decisive decision or feedback right: Human/trust configuration and deterministic capability/sandbox checks allow/deny tasks.
- Decision owner: Human operator controls action policy, not a native autonomous S5.
- Supporting / enforcement mechanisms: OS sandbox, capability broker, protected paths, persisted policy entries.
- Closure path: Refuse/allow risky operation or change settings; no constitutive policy adjudication across an autonomous organization.
- Why this is / is not agent-owned: An append-only policy ledger records decisions but does not itself own constitutional policy choice.
- Evidence: [crates/micro-tools/src/access.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-tools/src/access.rs); [crates/micro-cli/src/main.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-cli/src/main.rs); [crates/micro-sandbox/src/lib.rs](https://github.com/rmonvfer/micro/blob/563dc1e6a6957cefbcfdd503fc5c4b754dfc5240/crates/micro-sandbox/src/lib.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Findings are scoped to installed first-party coding runtime rather than external user-built workgroups.

### Absence scope

- Surfaces inspected: Native agent loop, file/shell tools, sessions, extension capability broker, provider configuration, OS sandbox and operational policy/ledger.
- Plausible first-party paths checked: A distinct owner making S5-specific discretionary decisions, with independently gathered evidence and a feedback return into operational coding at this selected recursion.
- Why no material first-party path remains: Actual mechanisms are local single-agent task feedback, deterministic guardrails, persisted traces or user-directed settings rather than a complete separately deciding organizational function.

## Distributed OSS parent arrangement

GitHub issue reviews/CI and the OSS maintainer organization are external to users' first-party coding sessions. They do not donate independently owned VSM functions to the local terminal execution model.

## Self-hosted and non-human modes

Micro's headless coding uses its Rust-owned loop, with provider inference treated as a dependency. Remote RPC can direct a saved session, but transport and detached clients do not establish a coordinating metasystem without an attached real operating decision right.

## Recursion

The system-in-focus is one active terminal coding session. Model-selected file/shell tools form its operating means; sandbox, ledger, extension callback host and session persistence are support mechanisms.

## Variety and escalation

Tool errors and sandbox refusals return local evidence to the coding loop, bounded by permissions and budget. The original agent chooses subsequent actions; no independent auditor or policy actor has been demonstrated.

## Evidence gaps

- No performance or correctness claim is inferred from repository tests, documentation promises or an append-only record's presence.
- Negative states are scoped to first-party built-in modes at frozen revision; arbitrary custom extension implementations and human teams would require new direct evidence.
