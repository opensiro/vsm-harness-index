---
harness_id: synth
project_name: synth
repository: https://github.com/aw1875/synth
review_ref: 545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# synth

## Review boundary

- System in focus: the first-party synth terminal coding-agent runtime at frozen revision 545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19, including its Zig model/tool loop, build/plan/review agent modes, read-only task subagents, tool approvals, persisted sessions/todos, context compaction, provider layer, MCP/skills/web tools, lifecycle hooks and interactive/headless surfaces.
- Purpose and identity: perform software-engineering work through one model-backed coding loop that can inspect/edit/run a project, ask the user for approvals, steer an active turn, persist/resume work and delegate bounded read-only research to nested task agents.
- Relevant environment: user goals/steering/approvals, repository files, tool/process/test results, provider/model outputs, read-only child-agent results, persistent session/todo state, MCP/skills/web services, hooks and configuration.
- Standard-distribution boundary: shipped synth binary, repository-owned Zig runtime, built-in tools/agents, subagent runner, TUI/headless hosts, database/session machinery and hook/MCP/skill integration. External model servers/providers, MCP servers, user/project skills and configured hook scripts are dependencies/configuration and cannot donate organizational ownership.
- Credited operating / distribution surfaces: src/agent, src/tools, src/core, src/tui, provider integration, headless execution and the first-party task/subagent bridge.
- Adjacent first-party surfaces excluded from ownership: repository CI/release workflows, tests/examples as development artifacts except where they corroborate wired runtime behavior, and OpenCode UI provenance.
- First-party operating / deployment modes considered: default Build mode; Plan and Review modes; interactive steering/cancellation; headless synth run; read-only task subagents; persistent/resumed sessions; supported MCP/skills/hooks/provider/model configurations.
- Recursion level: one synth coding session. The main build/plan/review loop is the primary viable operational unit. Task subagents are nested read-only research loops whose result is returned as one tool result; they do not write the project and cannot delegate further.
- Reviewed revision: 545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

synth implements one first-party AgentLoop that repeatedly calls the selected provider/model, executes requested tools and feeds tool results back until the model answers in prose or a deterministic safety/limit condition stops the turn. Build mode has the full registered tool surface; Plan and Review are alternative agent records with narrower tool sets and extra instructions.

The task tool creates nested subagent loops in fresh conversations. The built-in task agent is explicitly read-only, receives only read/list/glob/grep/ask_user/skill/todo tools, cannot call task again, and returns one answer to the parent tool call. Multiple tool calls may run concurrently, but task subagents cannot mutate the project. Cancelling the parent turn propagates a give-up flag to children; the TUI can display a live child transcript, but that view is explicitly read-only.

Interactive input entered while a turn is running is stored as steering and injected at the next parent-agent model step. This is current S1 correction, not a separate whole-system supervisor over a portfolio of operational commitments. The Review mode likewise changes the same session's agent configuration to a read/run-only prompt; it does not automatically create an independent author-versus-reviewer loop.

## Operational model

The model-backed main loop owns open-ended coding decisions: what to inspect, edit, execute, verify, delegate and when to finish. The runtime supplies deterministic permission prompts, safe-command classification, hooks, repeat/time/token/stall limits, compaction and persistence.

A task subagent can investigate a focused question independently in its own context, but its tool surface is intentionally non-mutating. Its lifecycle is subordinate to the waiting task tool and the parent turn's cancellation state. No separate first-party peer-work coordination or current portfolio controller is established by this nested research mechanism.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify, execute and verify software in response to a coding objective.
- Disturbance / variety regulated: unfamiliar repository state, implementation choices, build/test/tool failures, provider/model variation, context pressure, permission decisions and focused research questions.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret returned evidence, decide when read-only subagent research is useful and decide when the requested work is complete.
- Decision owner: the active model-backed synth agent in the selected Build/Plan/Review mode; Build mode owns project-changing software-engineering outcomes.
- Supporting / enforcement mechanisms: built-in file/bash/web/MCP/skill/todo tools, approval gate, safety classifier, hooks, provider adapters, steering, persistence, compaction, cancellation and turn limits.
- Closure path: user request → model selects coding/tool/research action → first-party runtime executes or delegates a read-only task → evidence returns into the same parent loop → model revises or completes the objective.
- Boundary reachability: the shipped TUI and synth run headless path instantiate the same AgentLoop/tool/provider machinery; Build is the default selectable agent mode.
- Why this is / is not agent-owned: deterministic code executes, constrains and persists work, but the model makes the open-ended engineering choices and interprets the evidence.
- Evidence: [README.md](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/README.md); [src/agent/loop.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/loop.zig); [src/agent/agent.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/agent.zig); [src/agent/prompt.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/prompt.zig).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Build-mode write/command calls may require human approval; approval constrains execution rather than supplying the substantive coding decision.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination loop is established.
- Disturbance / variety regulated: no concrete interference among distinct concurrently project-mutating S1 units is placed under a dedicated attenuation/feedback relation.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: task subagents have independent nested loops and tool calls may execute concurrently, but the built-in task-agent capability is read-only and cannot create file-write conflicts with the parent or peers.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: concurrency and nested agents are present, but the shipped multi-agent path deliberately removes project mutation from children; no function-specific peer-interference control loop is needed or instantiated.
- Evidence: [src/agent/agent.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/agent.zig); [src/agent/subagent.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/subagent.zig); [src/tools/task.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/tools/task.zig).
- Basis: structural absence review.
- Confidence: high.
- Caveats: shared provider/backend and tool scheduling are execution plumbing, not S2 without a concrete distinct-S1 interference witness.

### Absence scope

- Surfaces inspected: task agent tool allowlist, nested loop construction, parallel tool execution, project-root sharing, cancellation propagation, provider spawning and parent/child result delivery.
- Plausible first-party paths checked: write-capable peer workers, file/path leases, worktree isolation, peer conflict detector, shared mutation arbiter, merge controller and coordination feedback into child behavior.
- Why no material first-party path remains: standard child agents are explicitly read-only and non-recursive, while the main coding agent is the sole first-party project-mutating operational owner.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established above the active coding loop.
- Disturbance / variety regulated: no portfolio of independently controlled current S1 commitments/resources is exposed to a separate actor with substantive allocation/intervention authority.
- Decisive decision or feedback right: none established for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: mid-turn steering, cancel/timeout/token/repeat limits, live read-only subagent transcript viewing and parent-turn cancellation propagation alter or terminate one current S1 turn but do not create a whole-system controller.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the parent model may choose to call task, but each task call waits for a bounded read-only child result; there is no model-owned live worker portfolio with selective reassignment/retry/resource control. User steering is injected into the same parent loop at its next model step.
- Evidence: [src/agent/loop.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/loop.zig); [src/agent/subagent.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/subagent.zig); [src/tui/model.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/tui/model.zig); [README.md](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: generic stop/cancel, mode switching, todo state and direct steering of one operational loop do not satisfy the Methodology 0.3.6 whole-current threshold.

### Absence scope

- Surfaces inspected: task lifecycle, child status/transcript viewing, parent cancellation, steering queue, todos, mode switching, approval UI and turn resource limits.
- Plausible first-party paths checked: selective child kill/retry/reallocation, whole-current dashboard with decision authority, supervisor agent, live worker reprioritization and resource allocation.
- Why no material first-party path remains: observed controls either regulate the same S1 loop, display child evidence without intervention rights, or cascade a generic parent-turn stop.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit loop is established.
- Disturbance / variety regulated: no first-party path automatically assigns a coding claim to an independently instantiated reviewer and returns an audit judgment into corrective operation.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Review mode provides read/run-only tools and explicit review instructions, and generic task subagents can gather evidence, but these are user-selected modes/tools inside the same session rather than an independent review constructor.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: switching the same session/model loop from Build to Review changes its capability/prompt but does not create an independent author-reviewer boundary; task subagents are generic read-only researchers, not a dedicated audit verdict path.
- Evidence: [src/agent/agent.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/agent.zig); [src/agent/loop.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/loop.zig); [src/agent/subagent.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/subagent.zig); [README.md](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a person can manually use Review mode after a Build turn, but generic human sequencing of the same loop is not a standard independent S3* function.

### Absence scope

- Surfaces inspected: Build/Plan/Review agent definitions, session agent switching, task subagents, tests/bash access in Review mode, persisted sessions and normal verification instructions.
- Plausible first-party paths checked: fresh-context reviewer, second-model critique, authorship-independent evidence access, automatic review gate, audit verdict parser and corrective return.
- Why no material first-party path remains: the dedicated Review configuration is an alternate mode of the same session loop, and generic task subagents lack a standard audit claim/verdict/correction contract.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no changing external/future condition is transformed by an adaptation owner into options that modify later organizational capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent sessions/todos, transcript search, context compaction, skills, web tools, provider/model switching, MCP and user-configured lifecycle hooks supply information or configuration but do not close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: retained sessions and skills can inform later work, and hooks can deterministically block/transform operations, but no first-party actor is shown developing prospective adaptation options from outside/future evidence and returning them into current capability.
- Evidence: [README.md](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/README.md); [src/core/conversation.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/core/conversation.zig); [src/agent/context.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/context.zig); [src/core/hooks.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/core/hooks.zig).
- Basis: structural absence review.
- Confidence: high.
- Caveats: external web/MCP content and persisted context are evidence/capability inputs, not S4 ownership by themselves.

### Absence scope

- Surfaces inspected: sessions/search/todos, compaction, skills, web/MCP, provider/model switching, hook events, config and subagent research.
- Plausible first-party paths checked: durable learned strategy update, future environment scan, autonomous model/tool/skill reconfiguration and prospective option-generation feedback.
- Why no material first-party path remains: inspected mechanisms store/retrieve evidence or apply externally selected configuration/policy; no external-and-prospective adaptation conversation is closed.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level or ultimate-policy conflict is routed to an authoritative owner and returned as governing runtime policy.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: approvals, safe-command rules, user-configured blocking hooks, agent-mode tool allowlists, system prompt replacement and provider/MCP configuration constrain operation but do not establish S5.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent follows developer/user-authored policy and cannot authoritatively redefine synth's identity or ultimate operating principles.
- Evidence: [src/agent/safety.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/safety.zig); [src/agent/agent.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/agent/agent.zig); [src/core/hooks.zig](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/src/core/hooks.zig); [README.md](https://github.com/aw1875/synth/blob/545f1c2dbef396a2a693fd3a6c7f11ea4d00ce19/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a blocking hook may encode a strong local policy, but the hook is externally configured deterministic enforcement rather than a first-party identity-governance owner.

### Absence scope

- Surfaces inspected: system prompt/config replacement, mode capability lists, approval persistence, safe-command classification, blocking hooks, provider/MCP configuration and user steering.
- Plausible first-party paths checked: autonomous constitution/policy revision, parent identity governance, agent-authored permission policy and authoritative identity-level return loop.
- Why no material first-party path remains: all identified policy surfaces are developer/user-defined execution constraints or configuration.

## Distributed OSS parent arrangement

The assessed organization is the running synth coding session, not the GitHub maintainer project. Repository contribution/release governance is not imported as runtime S3/S4/S5 ownership.

## Self-hosted and non-human modes

synth supports local and hosted providers plus headless execution. The positive S1 claim is provider-neutral. User approvals/steering and configured hooks are optional constraints around S1, not evidence of autonomous higher-function ownership.

## Recursion

The declared viable-unit boundary is one synth coding session. The main model-backed loop is S1. Nested task agents are bounded read-only research units whose answer is consumed as a tool result; their presence does not instantiate peer operational coordination or a higher current-control system.

## Variety and escalation

Ordinary coding and verification variety stays in S1. The main agent can delegate research to read-only children. Deterministic approvals, safety rules, hooks, turn limits, compaction, steering and cancellation constrain the loop but do not close S2/S3/S3*/S4/S5.

## Evidence gaps

No ? state is required. The frozen repository exposes the complete agent-mode definitions, task/subagent construction, steering/cancellation, persistence, hooks and capability restrictions needed to support the positive S1 and bounded negative conclusions.
