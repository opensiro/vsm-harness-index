---
harness_id: michin
project_name: MichiN
repository: https://github.com/rohaquinlop/michin
review_ref: ff001031aad8486583055455989e02d2a88c8518
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# MichiN

## Review boundary

- System in focus: first-party Rust MichiN terminal coding-agent harness with its own streaming model/tool loop, native coding tools, persisted session and context, separate plan/build model settings, and optional Rhai lifecycle/tool hooks.
- Purpose and identity: respond to a user's software development requests through autonomous repository inspection, file modifications and shell commands.
- Relevant environment: source workspace, tool results, model endpoint, user mode/settings, permissions, session memory and human steering.
- Standard-distribution boundary: packaged MichiN TUI, prompt/continue, RPC and Rust agent core. No borrowing model-provider internals, external agents, hypothetical user scripts or repository maintenance workflows.
- Credited operating / distribution surfaces: crates/michin-agent-core for the actual loop and native tool execution; crates/michin executable/CLI/TUI/print/RPC wiring; crates/michin-script callbacks only where loaded and invoked from first-party paths.
- Adjacent first-party surfaces excluded from ownership: test fixtures, development scripts, publishing/CI, demo conversations, future extensions, external provider services and user-created multi-agent organizations.
- First-party operating / deployment modes considered: interactive coding session, print and RPC, model-directed source operations, plan/non-plan model switches, queued steering/follow-ups, allowed Rhai before/after-tool handlers, session replay and compaction.
- Recursion level: single local project coding session with one agent-directed operational cell. Multiple tools or separate plan/build model tracks do not establish distinct S1 agents.
- Reviewed revision: ff001031aad8486583055455989e02d2a88c8518.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

MichiN is an independent Rust coding-agent executable with a first-party agent engine, stream/provider adapters, concrete file/shell tools, terminal/UI and script extension packages. The core's Agent::run_prompt_loop maintains a single session and alternates inference and tool execution. Tool execution may be parallel or sequential according to tool type, but all responses are returned to the same coder and run context, not to separate independently functioning S1 work cells.

The TUI has plan mode and a separate remembered model selection for planning. Plan/non-plan switches affect local tool access and the currently selected coding model; this is not an independently operating long-horizon intelligence organization. Automatic model escalation, command safety, cancellation, repeated-call guards and context compaction support local task viability rather than create new metasystem decision owners.

The optional Rhai extension bridge implements before_tool_call and after_tool_call. A custom script can allow or block a tool; source-native hook failures may be logged while the tool proceeds. Nothing in this interface by itself provides independently owned, source-inspecting complementary audit judgment and correction feedback. The first-party Rust source implements meaningful safety controls but not higher VSM organizational authority by name.

Pinned source: [crates/michin-agent-core/src/agent.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/agent.rs); [crates/michin-agent-core/src/loop_mod.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/loop_mod.rs); [crates/michin-agent-core/src/tools.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/tools.rs); [crates/michin-script/src/hooks.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-script/src/hooks.rs); [crates/michin/src/interactive.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin/src/interactive.rs).

## Operational model

One model-directed S1 agent chooses code operations from actual project observations. Native execution, status and user controls regulate and protect that agent's task. No distinct agent peer, global current-control regulator, independent supplementary audit, strategic environmental capability-renewal actor or ultimate-policy governance actor is established at this selected boundary.

## S1 — Operations

- State: A
- Function: Execute first-party model-selected source and shell tools for project coding work.
- Disturbance / variety regulated: Changing user requirements, source state, compile errors, returned tool failures and environmental constraints.
- Decisive decision or feedback right: Select contingent source-edit/read/search/bash actions and decide subsequent work after observing outcomes.
- Decision owner: The coding LLM operating through MichiN's own Agent/loop, with action rights bounded by native tool/policy enforcement.
- Supporting / enforcement mechanisms: Provider streaming, native tool dispatcher, guardrails, context history, session state and user approval/mode choices.
- Closure path: User coding request → inference chooses tool action → first-party native tool executes on workspace → returned result enters core state → model chooses next corrective action or finishes.
- Boundary reachability: The shipped CLI, TUI, prompt and RPC operation call the first-party Rust agent core and first-party concrete tools. External providers supply inference only, not an external coding harness.
- Why this is / is not agent-owned: The model decides how to absorb local coding variety; native tools and policies enforce its chosen bounded work.
- Evidence: [crates/michin-agent-core/src/agent.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/agent.rs); [crates/michin-agent-core/src/loop_mod.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/loop_mod.rs); [crates/michin-agent-core/src/tools.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/tools.rs); [crates/michin/src/tools/write.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin/src/tools/write.rs); [crates/michin/src/tools/bash.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin/src/tools/bash.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: This is evidence of operative autonomy, not a measured benchmark-quality claim.

## S2 — Coordination

- State: —
- Function: No first-party organizational coordination loop across two independently functioning operational S1 cells.
- Disturbance / variety regulated: Concurrent tool execution may affect one active coding session, but does not evidence competing autonomous work units whose variety must be mutually stabilized.
- Decisive decision or feedback right: None across distinct S1 units; generic tool execution mode is selected/obeyed inside the single coder.
- Decision owner: No separate S2 authority.
- Supporting / enforcement mechanisms: Parallel or sequential native tool execution, queued user messages, session-level cancellation.
- Closure path: Tool output returns to the one model/agent; no inter-S1 interference detection and feedback to another S1 is seen.
- Why this is / is not agent-owned: Parallel file reads, serialized edit calls, model switching and queueing do not constitute an inter-agent coordination relationship.
- Evidence: [crates/michin-agent-core/src/tools.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/tools.rs); [crates/michin-agent-core/src/agent.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/agent.rs); [crates/michin-agent-core/src/loop_mod.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/loop_mod.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Separately running MichiN processes would need a separately established first-party organizational connection.

### Absence scope

- Surfaces inspected: Native loop, tool types and dispatcher, TUI modes, queues, session state, hooks and coding tools.
- Plausible first-party paths checked: Independent child coding loops, inter-agent file claims, collision detection, arbitration/negotiation and conflict-return to S1.
- Why no material first-party path remains: Reviewed distributed runtime has one agent decision cell; concurrency is among tools in that cell, not independently acting code workers.

## S3 — Inside-and-now control

- State: —
- Function: No separately owned whole-current regulator that supervises and reallocates work across multiple operational units.
- Disturbance / variety regulated: Run interruption, latency, current budget, repeated model/tool requests and execution errors.
- Decisive decision or feedback right: User steers or cancels; native runtime enforces timeout/repetition bounds and local safety policy.
- Decision owner: Deterministic single-session runtime and human task operator, not an S3 actor with discretionary whole-current view.
- Supporting / enforcement mechanisms: Active-run mutex, cancellation tokens, run reports, tool watchdog, turn termination statuses and model escalation.
- Closure path: Stop/steer/escalate changes this agent's present tool turn, without manager-mediated system-wide current allocation across multiple S1 units.
- Why this is / is not agent-owned: Status reports, execution ceilings and individual agent control do not transfer broader managerial judgment to the model.
- Evidence: [crates/michin-agent-core/src/agent.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/agent.rs); [crates/michin-agent-core/src/events.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/events.rs); [crates/michin-agent-core/src/loop_mod.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/loop_mod.rs); [crates/michin-agent-core/src/command_policy.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/command_policy.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: External human management of a coding team lies outside this packaged local session.

### Absence scope

- Surfaces inspected: Run lifecycle, status reports, task bounds, tool policy, model escalation and TUI controls.
- Plausible first-party paths checked: Whole-current model-owned manager, multi-S1 resource trade-offs, priority changes and closed managerial return to ongoing operations.
- Why no material first-party path remains: Every control path changes the one coding session's local execution; no independent overarching decision-maker or whole-current loop is wired.

## S3* — Complementary audit

- State: —
- Function: No material independent operational-audit owner with corrective return to coding S1.
- Disturbance / variety regulated: Unsafe commands and possibly defective code require checks, but safety enforcement does not itself establish complementary audit.
- Decisive decision or feedback right: Deterministic command safety rejects destructive actions; optional Rhai scripts can pre-block or post-observe tools, not act as a separately autonomous supplementary auditor by default.
- Decision owner: Static runtime policy and user-configured scripts; original coder retains responsibility for correction.
- Supporting / enforcement mechanisms: Before/after tool hooks, Rhai executor, command policy engine and tool result events.
- Closure path: Hook/policy may block one tool, or script observes a result; errors return to original coding context. No separate source-reading auditor returns independent defect judgment as binding corrective work.
- Why this is / is not agent-owned: Custom hooks, a second plan model and tool guards are not automatically complementary audit actors.
- Evidence: [crates/michin-agent-core/src/hooks.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/hooks.rs); [crates/michin-script/src/hooks.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-script/src/hooks.rs); [crates/michin-agent-core/src/command_policy.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/command_policy.rs); [crates/michin-agent-core/src/tools.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/tools.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: A separately supplied Rhai extension might implement richer audit logic, but its hypothetical behavior cannot be borrowed as default first-party capability.

### Absence scope

- Surfaces inspected: Hook contract, script bridge, command-policy path, tool dispatcher, agent turns and coding tests.
- Plausible first-party paths checked: Independently tasked reviewer, supplementary source evidence, explicit audit decision ownership and corrective feedback reaching a subsequent coder.
- Why no material first-party path remains: Source provides generic action hooks/guards without an installed independent audit-and-repair organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective environment analysis and strategic organizational capability renewal authority.
- Disturbance / variety regulated: Long-horizon external requirements and future tool/provider evolution are not addressed by one-session task planning.
- Decisive decision or feedback right: User selects model/plan track, preserves skills and restores sessions; the single coding agent performs local plans.
- Decision owner: No first-party prospective S4 decision owner.
- Supporting / enforcement mechanisms: Plan and build model tracks, context compaction, persistent session forks, resources and skills.
- Closure path: Settings and notes guide later coding turns, but no future-environment options are examined and accepted into organizational capabilities by a strategic owner.
- Why this is / is not agent-owned: Memory, switching to a better model and proposing a coding plan are not standalone future-environment intelligence.
- Evidence: [crates/michin/src/settings.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin/src/settings.rs); [crates/michin-agent-core/src/agent.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/agent.rs); [crates/michin-agent-core/src/compact.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/compact.rs); [crates/michin/src/skills.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin/src/skills.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Maintainer research/roadmap decisions are outside installed runtime ownership.

### Absence scope

- Surfaces inspected: Plan-mode model selection, sessions, skill loading, compaction, configuration and agent state.
- Plausible first-party paths checked: Prospective environmental scan, strategic option judgment, binding capability-development decision and later operational closure.
- Why no material first-party path remains: Only task-directed planning and preserved context are wired; there is no strategic decision/return organization.

## S5 — Policy and identity

- State: —
- Function: No constitutive identity/ultimate-purpose policy authority with organizational return.
- Disturbance / variety regulated: Permission risk and destructive commands are local execution safety matters, not highest-order identity/policy conflicts.
- Decisive decision or feedback right: User configures policies and model mode; runtime follows explicit forbidden-command constraints.
- Decision owner: Human operator for task settings and deterministic guard for enforcement; no legitimate highest-level first-party actor.
- Supporting / enforcement mechanisms: Command policy, strict safety flags, Rhai allow/block callbacks and plan-mode mutation gate.
- Closure path: Tool permitted/refused or model track changed; no ultimate organizational identity-policy decision returns to regulate the whole operation.
- Why this is / is not agent-owned: Constraints and human approvals do not establish an autonomous S5 decision right.
- Evidence: [crates/michin-agent-core/src/command_policy.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/command_policy.rs); [crates/michin-agent-core/src/hooks.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin-agent-core/src/hooks.rs); [crates/michin/src/config.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin/src/config.rs); [crates/michin/src/settings.rs](https://github.com/rohaquinlop/michin/blob/ff001031aad8486583055455989e02d2a88c8518/crates/michin/src/settings.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: OSS repository governance, licensing and developer policy are adjacent to user coding session.

### Absence scope

- Surfaces inspected: Safety policy, configuration, tool guards, plan mode and Rhai hooks.
- Plausible first-party paths checked: Highest-purpose deliberation, legitimate ultimate policy owner, ratification and binding policy return to operations.
- Why no material first-party path remains: All wired controls govern immediate code/tool permissions rather than an organization's identity or constitutive policy decisions.

## Distributed OSS parent arrangement

Repository maintainers, GitHub CI and release machinery are separate from installed user coding sessions and cannot donate S3/S4/S5. Provider services or user-authored extension systems cannot automatically be counted as first-party owners.

## Self-hosted and non-human modes

MichiN can operate with different model providers and a saved plan-mode model while the underlying code/tool loop remains first-party. Model switching changes inference choice rather than creating separate operating systems.

## Recursion

At the reviewed coding-session recursion one model-directed operating unit acts through native tools. Multi-tool calls, CLI/TUI modes, optional script callbacks and separate model profiles remain supporting surfaces, not independently viable S1 cells.

## Variety and escalation

Tool outcomes and user steering can alter coding choices; command policy and timeout paths can block unsafe or prolonged actions. No structural code review here establishes benchmark performance or independent metasystem ownership.

## Evidence gaps

- Negative findings are scoped to this frozen source and the packaged local coding runtime; custom user-hosted multi-agent systems may differ.
- No measured benchmark capability is inferred from repo tests or promotional descriptions.
- Richer custom script audit flows would require concrete first-party enabled evidence before scoring them positively.
