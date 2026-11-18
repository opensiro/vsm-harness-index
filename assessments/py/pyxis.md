---
harness_id: pyxis
project_name: Pyxis
repository: https://github.com/arthjean/pyxis
review_ref: 690665d686a1f6a44d4281b360a965ac338deffb
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Pyxis

## Review boundary

- System in focus: The shipped native Pyxis CLI and agent runtime at the parent thread with children it owns.
- Purpose and identity: Execute coding tasks across model-mediated workspace operations, optionally delegating to managed subagents.
- Relevant environment: Tasks and follow-up steering, workspace state, configured model APIs, tool outputs, child-run events and MCP endpoints.
- Standard-distribution boundary: First-party Rust core, CLI, app server, provider adapters and child supervisor. External providers, MCP tool implementations and the internals of external child processes are dependencies.
- Credited operating / distribution surfaces: [Cargo.toml](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/Cargo.toml), [README.md](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/README.md), [crates/agent-cli/src/main.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/main.rs), [crates/agent-core/src/agent.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-core/src/agent.rs), [crates/agent-runtime/src/thread.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/thread.rs), [crates/agent-runtime/src/supervisor.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/supervisor.rs), [crates/agent-tools/src/agent.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-tools/src/agent.rs)
- Adjacent first-party surfaces excluded from ownership: Development-fixture and live-parity suites, release work and roadmap. Notice documents reused Codex components; ownership claims require their operation in Pyxis itself.
- First-party operating / deployment modes considered: CLI/headless and app-server-facing architecture, session forks/resume, capability-gated native child tools, optional external child provider, scheduled reminders and tool approval.
- Recursion level: One Pyxis operational team: the primary thread and its directly managed child runs.
- Reviewed revision: `690665d686a1f6a44d4281b360a965ac338deffb`
- Observation date: 2026-11-18
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Pyxis separates a streamed tool-using loop from terminal rendering, providers and durable task state. The runtime thread actor owns queue and lifecycle transitions; the supervisor attaches first-party child agent handles to the current thread. Configured models can see agent management tools, while job and timer facilities provide operational inputs and completion events.

## Operational model

The model asks for workspace actions and sees their results. In a supported child-tool mode the parent model can allocate work, inspect its distinct live children, redirect a target and collect the returned result. Runtime gates and cancellation arbitrate whether a requested action is accepted.

## S1 — Operations

- State: A
- Function: Operational task execution
- Disturbance / variety regulated: Operator instructions, workspace observations and tool success/failure
- Decisive decision or feedback right: Choose task actions, follow-ups and turn completion
- Decision owner: The model-backed Pyxis agent
- Supporting / enforcement mechanisms: Typed transitions, I/O dependency injection, approved tool dispatch and runtime turn persistence
- Closure path: Tool responses and accepted new inputs return to later model requests
- Boundary reachability: The headless or interactive CLI builds the first-party tool registry and calls the runtime, which runs the same agent core.
- Why this is / is not agent-owned: The actor selecting the requested tool and next turn is the model using the shipped agent runtime.
- Evidence: [crates/agent-cli/src/main.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/main.rs), [crates/agent-cli/src/headless.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/headless.rs), [crates/agent-core/src/agent.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-core/src/agent.rs), [crates/agent-runtime/src/runner.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/runner.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

## S2 — Coordination

- State: —
- Function: Attenuation of interference between distinct S1 units
- Disturbance / variety regulated: Potential duplicate child work or contested workspace effects between separate model agents
- Decisive decision or feedback right: No supplied conflict-specific attenuation relation at this recursion
- Decision owner: Parent can dispatch and send generic corrections. No established function-specific cross-agent coordination actor
- Supporting / enforcement mechanisms: Child registry, message delivery, queue serialization and read-only child boundaries
- Closure path: Children can receive new instructions and report outcomes
- Why this is / is not agent-owned: Per-thread queue arbitration settles races inside the runtime. Generic child steering alone leaves the detection and regulation of specific inter-S1 interference unestablished.
- Evidence: [crates/agent-runtime/src/supervisor.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/supervisor.rs), [crates/agent-runtime/src/thread.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/thread.rs), [crates/agent-tools/src/agent.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-tools/src/agent.rs), [crates/agent-cli/src/subagents/mod.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/subagents/mod.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [crates/agent-runtime/src/supervisor.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/supervisor.rs), [crates/agent-runtime/src/thread.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/thread.rs), [crates/agent-tools/src/agent.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-tools/src/agent.rs), [crates/agent-cli/src/subagents/mod.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/subagents/mod.rs)
- Plausible first-party paths checked: Trace native child tool addressing, per-turn serialization, boundary restrictions and child follow-up delivery for cross-child interference remedies.
- Why no material first-party path remains: The first-party mechanisms manage or transport thread-level work and constraints without a specific inter-S1 interference decision and return.

## S3 — Inside-and-now control

- State: A
- Function: Whole-system current direction and resource or commitment intervention
- Disturbance / variety regulated: Pending, failed or stalled commitments across the operational children managed by one parent thread
- Decisive decision or feedback right: Reallocate work by selecting child scopes and sending revised tasks, or interrupt a specifically identified active commitment
- Decision owner: The parent Pyxis model in the shipped child-management mode
- Supporting / enforcement mechanisms: Supervisor graph and list/wait snapshots, child permissions, message and follow-up dispatch, interrupt enforcement
- Closure path: The parent model sees child state or results, selects a follow-up or interrupt, and the supervisor applies it to the identified child thread
- Boundary reachability: The CLI registers SpawnAgent, ListAgents, WaitAgent, FollowupTask and InterruptAgent against the runtime supervisor. The model catalog controls exposure per step.
- Why this is / is not agent-owned: The parent model chooses which active commitment to redirect or interrupt based on the team view. The supervisor executes that selection.
- Evidence: [crates/agent-cli/src/main.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/main.rs), [crates/agent-tools/src/agent.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-tools/src/agent.rs), [crates/agent-runtime/src/supervisor.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/supervisor.rs), [crates/agent-runtime/src/thread.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/thread.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Requires a model/mode with the child tools exposed and a spawner supporting the requested operation. TUI cancellation of a single turn is not the basis for the grade.

- Whole-system current view: In the assessed parent-owned team, list and wait expose current child identities, lifecycle and results to the parent that maintains its own task context.
- Current-control decision scope: Create, redirect or interrupt operating commitments across that parent's children; the state excludes independent external teams and provider internals.

## S3* — Complementary audit

- State: —
- Function: Complementary independent operational audit with corrective return
- Disturbance / variety regulated: A child reports a completed change while operating reality differs
- Decisive decision or feedback right: No supplied audit-specific independent judgment and corrective return
- Decision owner: Working agents can inspect files or request a child. Operator can read the transcript
- Supporting / enforcement mechanisms: Read-only child, diff and logs, transcript replay and external tests
- Closure path: Read outputs or child reports can return to the requester
- Why this is / is not agent-owned: The packaged audit-adjacent surfaces expose operating data and generic delegation without a configured independent authority that challenges sample claims and governs corrective follow-up.
- Evidence: [crates/agent-tools/src/agent.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-tools/src/agent.rs), [crates/agent-tools/src/turn_diff.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-tools/src/turn_diff.rs), [crates/agent-cli/src/transcript/replay.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/transcript/replay.rs), [crates/agent-cli/src/subagents/mod.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/subagents/mod.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [crates/agent-tools/src/agent.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-tools/src/agent.rs), [crates/agent-tools/src/turn_diff.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-tools/src/turn_diff.rs), [crates/agent-cli/src/transcript/replay.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/transcript/replay.rs), [crates/agent-cli/src/subagents/mod.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/subagents/mod.rs)
- Plausible first-party paths checked: Inspect read-only worker defaults, diffs, tool histories and test replay for a shipped complementary sampling or judgment path.
- Why no material first-party path remains: Transcript replay is a development/diagnostic path and native child tools are general-purpose. An independent auditor would require a new operating composition.

## S4 — Outside-and-then intelligence

- State: —
- Function: External, prospective intelligence and adopted capability adaptation
- Disturbance / variety regulated: Future changes in tasks, tool availability or model/provider conditions
- Decisive decision or feedback right: No packaged external prospective sensing-and-adopt capability decision
- Decision owner: Operator configures model and connection options; the agent can schedule reminders
- Supporting / enforcement mechanisms: Provider abstraction and fallback, live session settings, reminders, contextual compaction
- Closure path: These paths modify ordinary configuration or deliver a reminder/result to the ongoing thread
- Why this is / is not agent-owned: The shipped scheduler brings inputs to an identified thread. Provider choice and fallback do not explore and adopt options for changed future demands.
- Evidence: [crates/agent-runtime/src/schedule.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/schedule.rs), [crates/agent-runtime/src/thread.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/thread.rs), [crates/agent-cli/src/interactive/commands.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/interactive/commands.rs), [crates/agent-cli/src/runtime.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/runtime.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [crates/agent-runtime/src/schedule.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/schedule.rs), [crates/agent-runtime/src/thread.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/thread.rs), [crates/agent-cli/src/interactive/commands.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/interactive/commands.rs), [crates/agent-cli/src/runtime.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/runtime.rs)
- Plausible first-party paths checked: Inspect scheduled wakeup, runtime switches, fallback provider and turn goals as possible adaptation paths.
- Why no material first-party path remains: No first-party transition from external future-relevant analysis to adopted capability is defined by these surfaces.

## S5 — Policy and identity

- State: —
- Function: Resolution and return of ultimate identity or policy decisions
- Disturbance / variety regulated: Potential disagreement over the installed organization's enduring purpose and binding policy
- Decisive decision or feedback right: No constitutional decision loop reaches and returns from a legitimate authority
- Decision owner: Operator chooses session goals and permitted effects; maintainers establish defaults
- Supporting / enforcement mechanisms: Goal persistence, permission gate and configured runtime boundaries
- Closure path: The current goal or approval constrains the thread's next work
- Why this is / is not agent-owned: A durable task objective can steer the agent while leaving the system's ultimate purpose and policy outside its runtime decision loop.
- Evidence: [crates/agent-cli/src/interactive/commands.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/interactive/commands.rs), [crates/agent-cli/src/settings.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/settings.rs), [crates/agent-cli/src/approver.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/approver.rs), [crates/agent-runtime/src/supervisor.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/supervisor.rs)
- Basis: Bounded inspection of pinned shipped implementation, manifests and operating instructions.
- Confidence: Medium-high within this boundary.
- Caveats: Source-only review of the declared operating surface.

### Absence scope

- Surfaces inspected: [crates/agent-cli/src/interactive/commands.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/interactive/commands.rs), [crates/agent-cli/src/settings.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/settings.rs), [crates/agent-cli/src/approver.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-cli/src/approver.rs), [crates/agent-runtime/src/supervisor.rs](https://github.com/arthjean/pyxis/blob/690665d686a1f6a44d4281b360a965ac338deffb/crates/agent-runtime/src/supervisor.rs)
- Plausible first-party paths checked: Check /goal, stored thread context, operator permissions and inherited subagent authority.
- Why no material first-party path remains: These paths apply a task objective or enforce action rights. None receives, resolves and reapplies a higher-order identity issue.

## Recursion

Child sessions are separately operating model-backed cells with constrained authority. The observed supervisor sits at the parent thread's team boundary; no complete repeated VSM at every child follows.

## Variety and escalation

Tool permission gates, child authority ceilings, bounded queues, steering and interrupt provide reaction to current operating variance. Child outcomes return through the supervisor.

## Evidence gaps

No live provider or tool run. Source establishes native code paths conditional on model/tool configuration. No external provider, MCP service or Codex child internals are credited.
