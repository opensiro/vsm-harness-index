---
harness_id: peezy
project_name: Peezy
repository: https://github.com/p0systems/peezy-cli
review_ref: 4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Peezy

## Review boundary

- System in focus: the first-party Peezy CLI coding runtime at frozen revision 4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3, including its model/tool agent loop, built-in coding/web/todo tools, approval/confinement policy, context compaction, session persistence/resume, MCP tool registration, TUI and headless runner.
- Purpose and identity: complete repository coding tasks through one model-backed agent loop that may inspect/edit/execute, maintain a visible todo list, use connected tools and persist/resume its conversation.
- Relevant environment: user goal and approvals, repository files, process/tool results, provider/model responses, web/MCP tool results, context pressure, session state and interrupt signals.
- Standard-distribution boundary: shipped Peezy CLI/runtime and bundled first-party modules. Hosted gateway/model services, MCP servers, external providers and the user's repository/toolchain are dependencies and cannot donate VSM functions.
- Credited operating / distribution surfaces: src/core/agent.ts, create-agent.ts, built-in tools, prompt/compaction, session store/resume, TUI approval controls and src/cli/run.ts.
- Adjacent first-party surfaces excluded from ownership: package/release infrastructure, tests, hosted p0 services beyond the CLI-owned invocation boundary, and maintainer workflows.
- First-party operating / deployment modes considered: interactive TUI, headless run/print, approval modes auto/ask/plan/yolo, persisted/resumed sessions, connected MCP tools and supported providers.
- Recursion level: one Peezy coding conversation. No distinct standard operational agent unit is instantiated by the frozen runtime.
- Reviewed revision: 4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Peezy implements one UI-free Agent loop per conversation. The model receives the current message history and ToolRegistry, chooses coding/tool calls, receives results and repeats until it emits a final answer or hits a deterministic request limit. The same core loop is consumed by the TUI and headless runner.

The ToolRegistry includes file read/write/edit, bash, search and a mutable todo list; gateway-backed web/image tools and configured MCP tools can be added. Ask mode routes write/exec calls through a human approval callback; plan mode deterministically rejects mutation. File tools can be confined to the working directory. Session JSONL persists trajectory state for resume, while context compaction summarizes older conversation content through the same provider/model family.

These are useful S1 supports, but no bundled delegation/subagent constructor or distinct operational worker is present. Approval, todo state, context management and MCP extensibility therefore do not establish higher VSM functions by themselves.

## Operational model

The active model owns open-ended engineering actions and completion. The runtime owns deterministic transport/enforcement: tool lookup, path confinement, approval gating, request caps, session recording and context compaction. A human in ask mode approves or denies risky S1 actions, but the approval is local execution permission rather than a whole-system current-control function.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify a software project using model-selected coding/tool actions.
- Disturbance / variety regulated: unfamiliar repository state, implementation choices, tool/process failures, context pressure, provider behavior and denied actions.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret their outcomes, adapt after failures/denials and decide when the task is complete.
- Decision owner: the active model-backed Peezy agent.
- Supporting / enforcement mechanisms: ToolRegistry, gateway streaming, approvals, path confinement, todo state, compaction, session persistence/resume, MCP registration and interrupt handling.
- Closure path: user objective → model selects tool/coding action → runtime executes or returns denial/error → result re-enters model history → model revises work → final answer closes the turn.
- Boundary reachability: both interactive and headless entry points construct the same first-party Agent and tool registry; headless changes approval handling without replacing the core decision loop.
- Why this is / is not agent-owned: runtime code enforces permissions and transports tool results, but the model owns the open-ended coding decisions and evidence interpretation.
- Evidence: [README.md](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/README.md); [src/core/agent.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/agent.ts); [src/core/create-agent.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/create-agent.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ask/plan modes can constrain execution, but that does not transfer the coding decision itself away from the model.

## S2 — Coordination

- State: —
- Function: no material inter-S1 coordination function is established.
- Disturbance / variety regulated: none at the declared recursion because the standard runtime does not instantiate distinct concurrent operational agents.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: todo sequencing, MCP tool registration and tool execution order remain inside one S1 loop.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: generic task ordering/tool extensibility is not peer interference attenuation.
- Evidence: [src/core/agent.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/agent.ts); [src/core/tools/todo.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/tools/todo.ts); [src/core/mcp/manager.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/mcp/manager.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: connected MCP servers may themselves contain agents, but external systems cannot donate S2 to Peezy.

### Absence scope

- Surfaces inspected: agent loop, tool registry, todo tool, MCP manager, TUI/headless entry points and repository tree for delegation/subagent surfaces.
- Plausible first-party paths checked: peer workers, parallel task agents, worktrees, shared task arbitration and inter-agent conflict feedback.
- Why no material first-party path remains: no distinct S1 units or S2-specific constructor is supplied by the frozen CLI.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established.
- Disturbance / variety regulated: no portfolio of distinct current operational commitments exists under a separate controller.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: approval prompts, request caps, abort signals, plan-mode mutation rejection and todo visibility constrain one S1 turn.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: human approval is action-local permission and interrupt is termination enforcement; neither provides a whole-system current view plus substantive control over resources/commitments.
- Evidence: [src/core/agent.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/agent.ts); [src/core/tools/safety.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/tools/safety.ts); [README.md](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: generic approval or stop controls are explicitly insufficient for S3 under Methodology 0.3.6.

### Absence scope

- Surfaces inspected: approval modes, TUI status/interrupts, todo state, request cap, session state and headless behavior.
- Plausible first-party paths checked: worker portfolio view, resource/priority reallocation, selective live intervention and autonomous or parent supervisor loop.
- Why no material first-party path remains: all located controls apply to one coding loop or individual actions.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is established.
- Disturbance / variety regulated: no separate actor independently challenges an operational claim using a complementary evidence path.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: the same coding agent may run tests, inspect diffs or use read tools; plan mode and todo tracking do not create independent review.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: no fresh reviewer/verifier role or separate evidence channel is wired into the standard distribution.
- Evidence: [src/core/prompt/system.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/prompt/system.ts); [src/core/agent.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/agent.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a user can ask the same agent or an external MCP tool to review; generic composition is not a first-party independent audit loop.

### Absence scope

- Surfaces inspected: system prompt, tool registry, todo, approval modes, session history, MCP integration and tests.
- Plausible first-party paths checked: dedicated reviewer role, second model, fresh context, independent test/evidence reader and corrective audit gate.
- Why no material first-party path remains: verification remains ordinary S1 work or external composition.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no future/external distinction is transformed into an adaptation option that changes current organizational capability.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: session resume, compaction, provider/model configuration, live MCP changes and project instructions preserve/reconfigure context but do not themselves close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: compaction summarizes prior context and configuration selects tools/models; neither is an autonomous prospective adaptation owner.
- Evidence: [src/core/prompt/compaction.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/prompt/compaction.ts); [src/core/session/store.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/session/store.ts); [src/core/create-agent.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/create-agent.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: persistent experience can inform later S1 turns, but persistence/context reuse is insufficient S4.

### Absence scope

- Surfaces inspected: compaction, session resume, provider catalog, MCP lifecycle, project instructions and configuration.
- Plausible first-party paths checked: environment scanning, learned strategy update, autonomous capability/model/tool selection from future-facing evidence and returned adaptation options.
- Why no material first-party path remains: inspected mechanisms persist or externally configure current execution rather than close a prospective adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level policy matter is routed to an authoritative owner and returned as governing runtime policy.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: compiled system prompt, approval modes, path confinement, project instructions and provider/tool configuration constrain operations.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: Peezy operates within user/developer-authored rules and has no authority to redefine its identity or ultimate policy.
- Evidence: [src/core/prompt/system.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/prompt/system.ts); [src/core/agent.ts](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/src/core/agent.ts); [README.md](https://github.com/p0systems/peezy-cli/blob/4abb65bb3e8c9f6c4cdd42c22d29b61531bffad3/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: action approvals are not identity governance.

### Absence scope

- Surfaces inspected: system prompt, approval/confinement modes, project instructions, provider/model config, MCP controls and CLI/TUI commands.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity governance and authoritative policy-return loop.
- Why no material first-party path remains: located policy surfaces are static/external operating constraints.

## Distributed OSS parent arrangement

The assessed organization is the running Peezy CLI session, not the p0 GitHub project or hosted service organization. Maintainer/company governance is not imported as runtime S3/S4/S5 ownership.

## Self-hosted and non-human modes

Peezy can use local/custom providers and has a headless mode. S1 remains model-owned across these modes. Ask mode adds human action approval but does not close a higher parent function.

## Recursion

One model-backed coding conversation is the viable-unit candidate. Built-in tools, todo state, compaction, sessions and connected MCP tools are components/supporting capabilities rather than separate operational organizations.

## Variety and escalation

S1 absorbs coding/tool variety. Deterministic request limits, approval/confinement, compaction and session persistence bound operation. No separate S2/S3/S3*/S4/S5 loop is established.

## Evidence gaps

No ? state is required. The frozen runtime exposes the full agent loop, tools, approval/confinement, session, compaction and integration boundaries needed for these bounded conclusions.
