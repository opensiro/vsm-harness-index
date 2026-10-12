---
harness_id: kairocode
project_name: KairoCode
repository: https://github.com/yangf-Veda/KairoCode
review_ref: 018c74035de1354f69a92eda626ddbb210fbebcc
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# KairoCode

## Review boundary

- System in focus: the shipped Python KairoCode terminal coding-agent application, including the model/tool execution loop, tool/permission boundary, first-party subagent execution and the explicitly configured local Team/Coordinator mode.
- Purpose and identity: a local coding agent that reads, edits and tests repository code, delegates bounded work to independent model-driven teammates, keeps task and session state, and in an optional mode leads a team of coding workers.
- Relevant environment: a local Git workspace, configured Anthropic or OpenAI-compatible model provider, first-party filesystem/shell/tools, user permissions, TUI, external MCP servers, optional tmux/iTerm/in-process teammate backends, local project and user memory.
- Standard-distribution boundary: first-party `src/kairocode/` Python package and bundled role prompts/configurations, with the TUI wiring that instantiates `Agent`, `AgentTool`, `TeamSpawner`, shared Team task/store, worktree manager, mailbox and coordinator prompt. Model provider, terminal multiplexers and external MCP services are dependencies, not credited organizational owners.
- Credited operating / distribution surfaces: `src/kairocode/agent/__init__.py`, `agent/agent_tool.py`, `agent/team_mailbox.py`, `agent/team_hook.py`, `team/manager.py`, `team/spawn.py`, `team/tasks/__init__.py`, `team/tools/__init__.py`, `team/mailbox/`, `worktree/`, `coordinator/__init__.py`, `cli.py`, `tui/app.py`, bundled subagent roles, tools and runtime instructions.
- Adjacent first-party surfaces excluded from ownership: offline evaluation suite and reports, test-only fake provider, CI, maintainer roadmaps and design documents, demonstration screenshots, example MCP server, unrelated parent projects in the user's workspace and external custom agent plugins. These corroborate reachability but cannot supply an independent operating function themselves.
- First-party operating / deployment modes considered: default local coding loop and read-only plan mode; foreground/background `Agent` subagents and `SendMessage`; optional enabled Team/Coordinator Mode requiring both configured feature and `KAIROCODE_COORDINATOR_MODE` environment opt-in, including in-process or terminal-backed workers in per-teammate worktrees; memory, sessions, hooks and extensions.
- Recursion level: one top-level KairoCode session and its live subordinate local team; the teammate model loops are the lower-level S1 units. Separate unrelated KairoCode installations are not assumed to form one managed organization.
- Reviewed revision: 018c74035de1354f69a92eda626ddbb210fbebcc.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `Agent` loop streams provider responses, parses requested tool calls, routes each through permission/tool registry enforcement, appends structured results to conversation and iterates toward a final answer or explicit stop. The TUI assembles first-party runtime, permissions, memory, worktree and built-in tools in `cli.py`. Read/write/edit/bash, glob/grep and optionally MCP tools supply local coding operations. Project instructions, JSONL sessions, compaction and model-produced memory updates preserve context but do not alone establish a higher VSM function.

The `Agent` model tool creates an independently executed child agent using a bundled or project-defined definition; it may run as a background task and return observations through `task.Manager`. In Team mode, `TeamSpawner` creates a dedicated Git worktree and session directory, launches an actual subordinate `Agent`, records team membership and exposes mailbox operations. Shared `TaskCreate`, `TaskList`, `TaskGet`, `TaskUpdate` and `SendMessage` tools are wired from `cli.py` into the standard tool registry. Shared task records have assignee/status/dependency fields, readiness recomputed from completed blockers, and file locks for atomic storage. Teammate mailbox messages become a new user-context reminder in the child model loop; lead messages and task changes can therefore change subsequent worker behavior.

The explicitly optional Coordinator mode assigns the top-level model the role of Team Lead and restricts its tool surface to delegate, view status, send messages and perform bounded inspection/acceptance. Its shipped prompt instructs it to divide research/synthesis/implementation/verification work, wait for worker reports, inspect returned work and decide acceptance, providing a first-party current-control route in that mode. The per-worker worktree isolation, shared task dependencies and mailbox mechanics remain supporting paths rather than by themselves S2 conflict control. An optional review-style child or a plan/verification task has no separately established formal audit contract or independent corrective authority at the declared boundary.

Source evidence:
- [Agent model/tool feedback loop](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/agent/__init__.py)
- [Tool-based subagent dispatch](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/agent/agent_tool.py)
- [Team spawner and dedicated child worktree](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/team/spawn.py)
- [Team tool implementations](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/team/tools/__init__.py)
- [Shared task readiness and update locking](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/team/tasks/__init__.py)
- [Mailbox ingestion into child conversation](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/agent/team_mailbox.py)
- [Coordinator gating, tool allowlist and team-lead prompt](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/coordinator/__init__.py)
- [CLI tool registry wiring](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/cli.py)
- [TUI coordinator and team-spawner runtime wiring](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/tui/app.py)
- [Worktree lifecycle and cleanup](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/worktree/lifecycle.py)
- [Architecture and distributed boundary cautions](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/docs/architecture.md)

## Operational model

The default session autonomously selects coding actions and observes direct tool/test feedback. In opt-in Coordinator mode, the model changes organizational role: a team lead chooses which active worker receives which current task, uses first-party status and mailbox information to alter assignments, requests follow-ups, then inspects/accepts work. Workers have their own model loops and worktrees. Human permission enforcement and runtime persistence constrain those decisions; neither is itself the model's organizational discretion.

## S1 — Operations

- State: A
- Function: execute requested local coding and repository inspection/modification tasks through model-selected first-party tools, with ongoing observation and repair.
- Disturbance / variety regulated: user coding requirements, repository content, tool failures, permission denials, shell/test outputs, provider responses and newly discovered file context.
- Decisive decision or feedback right: model chooses read/edit/shell/tool and successor steps, responds to returned results, delegates a subtask or terminates task work.
- Decision owner: top-level coding model; in Team mode, delegated teammate models own their bounded coding work.
- Supporting / enforcement mechanisms: Python `Agent` loop, tool registry, permission engine, provider streaming, session, compaction, worktree/child-task facilities.
- Closure path: request → model tool selection → first-party execution/denial → structured returned result → next model action, correction or final answer.
- Boundary reachability: normal `kairocode` CLI/TUI instantiates the model loop and tools; teammate loops are reachable when the optional team path is chosen.
- Why this is / is not agent-owned: runtime enforces permissions and transport; the model determines task-specific operations and responds to results.
- Evidence: [agent loop](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/agent/__init__.py), [CLI](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/cli.py), [architecture](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the source review does not imply production-grade sandboxing or uninterrupted provider availability.

## S2 — Coordination

- State: —
- Function: no sufficiently evidenced first-party *inter-S1 interference-specific* attenuation with returned correction of subsequent S1 behavior, as distinct from generic routing and work isolation.
- Disturbance / variety regulated: separate workers might contend for shared files or task prerequisites, but a first-party post-integration conflict-detection/negotiation-and-return path was not established.
- Decisive decision or feedback right: not established for S2-specific interference resolution.
- Decision owner: not established.
- Supporting / enforcement mechanisms: per-worker Git worktrees, team task dependency readiness, JSON file lock, mailbox communications and lead's generic task routing.
- Closure path: no verified disturbance-specific inter-worker regulation cycle; per-worker isolation and task readiness are support for general delegation.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: worktree separation can prevent direct file overwrites, but without evidence of live inter-worker incompatible edit detection, integration arbitration or feedback, it is not enough to credit the stronger organizational coordination claim. Generic readiness and mailbox messages are not S2 by themselves.
- Evidence: [worktree manager](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/worktree/manager.py), [team spawn](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/team/spawn.py), [tasks store](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/team/tasks/__init__.py), [worktree lifecycle](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/worktree/lifecycle.py).
- Basis: structural.
- Confidence: medium.
- Caveats: reviewer should challenge whether independent worktrees and explicit task blockers amount to an eligible S2 constructor; do not infer cross-worker conflict closure merely from Git isolation.

### Absence scope

- Surfaces inspected: team spawner, worktree management/create/lifecycle, task dependencies, teammate mailbox, coordinator prompt, shared task storage and lock implementation.
- Plausible first-party paths checked: per-teammate worktree isolation, `blocked_by` and readiness computation, atomic JSON writes, shared mailbox and model lead's explicit follow-up instructions.
- Why no material first-party path remains: the inspected shipped mechanisms are task decomposition, avoidance and storage integrity; no concrete detected inter-S1 incompatibility, attenuation decision and returned worker correction was established in these paths. This conclusion is bounded by the inspected supported runtime, not a claim that future modules cannot implement S2.

## S3 — Inside-and-now control

- State: A
- Function: in opt-in Coordinator mode, direct and regulate present commitments of subordinate coding agents across one live local team.
- Disturbance / variety regulated: changing worker availability, completion/error state, current assignments, task dependencies and unmet acceptance requirements.
- Decisive decision or feedback right: team lead model decides decomposition and assignment, dispatches subordinate coding agents, reads member/task status and reports, sends instructions, updates ownership/status and accepts or redirects work.
- Decision owner: top-level autonomous model in the explicitly enabled Coordinator mode.
- Supporting / enforcement mechanisms: first-party `TeamCreate` / `Agent` / `TaskList` / `TaskUpdate` / `SendMessage`, team registry and shared task store, mailbox delivery, worktree creation, coordinator tool allowlist.
- Closure path: model lead sees shared task/member results → chooses next priority, assignment or corrective instruction → model tool call updates shared team/task/mailbox state → teammate receives message/new task and performs subsequent action → updated status/report returns to lead for redecision.
- Boundary reachability: `coordinator.is_enabled` is gated by shipped `features.coordinator_mode` AND `KAIROCODE_COORDINATOR_MODE`; `cli.py` registers team management tools, and `tui/app.py` applies coordinator prompt/tool allowlist and installs `TeamSpawner` on the active `Agent` tool.
- Why this is / is not agent-owned: persistence and task readiness are deterministic; the model team lead interprets current reports and owns substantive decision over current commitments.
- Whole-system current view: current team members, worker status and shared task board plus returned mailbox reports under one named local team; not claimed to manage all independent KairoCode installations.
- Current-control decision scope: assignments, subordinate task state, delegation, follow-up messages and acceptance, not merely a technical concurrency cap.
- Evidence: [coordinator implementation](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/coordinator/__init__.py), [tool registration](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/cli.py), [TUI wiring](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/tui/app.py), [team tools](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/team/tools/__init__.py), [team mailbox](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/agent/team_mailbox.py).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this claim is local-team/optional mode only. It does not establish distributed organizational governance, nor imply that merely enabling arbitrary subagents without Coordinator wiring closes S3.

## S3* — Complementary audit

- State: ?
- Function: a distinct child could be asked to inspect actual code/tests separately from an implementing worker; a qualifying built-in *complementary audit* with correction/independence remains unresolved.
- Disturbance / variety regulated: potentially defects or discrepancies in implementing-agent evidence versus operational artifact.
- Decisive decision or feedback right: unknown; an independent child with direct file tools might issue findings, but no distinct standard audit authority and binding correction loop has been demonstrated.
- Decision owner: unresolved; coordinator's stated Verification phase and generic subagent are not automatically an independently entrusted reviewer.
- Supporting / enforcement mechanisms: independent child `Agent` loops, read-only `explore` and `plan` roles, first-party file/bash tools, parent/lead message acceptance and Team task feedback.
- Closure path: potential implementation → independently tasked child reads actual files/tests → returns defect findings to lead → reassigns change; shipped audit-specific guarantees and concrete standard trigger not sufficiently traced.
- Boundary reachability: no positive path credited; actual child tooling and coordinator Verification phase are supported, but their audit-specific independence/return need source adjudication.
- Why this is / is not agent-owned: choosing a generic verification task does not by itself create a complementary audit with accountable authority; detached test/evaluation suite is development evidence only.
- Evidence: [coordinator stages](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/coordinator/__init__.py), [subagent dispatch](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/agent/agent_tool.py), [roles](https://github.com/yangf-Veda/KairoCode/tree/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/subagent/builtin), [team mailbox](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/agent/team_mailbox.py).
- Basis: structural + unknown.
- Confidence: low.
- Caveats: no independent S3* human reviewer was executed; the question concerns the harness architecture, not the independence of this Index assessment.

## S4 — Outside-and-then intelligence

- State: —
- Function: no materially closed future-directed outside-intelligence capability-adaptation loop is established within the assessed shipped session/team.
- Disturbance / variety regulated: user requests, persistent knowledge and provider outcomes affect current/local task behavior but are not shown as external-future strategic alternatives.
- Decisive decision or feedback right: not established for future organizational capability adaptation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: asynchronous LLM memory update, project/user Markdown memory index, instruction loading, skills/hooks, roadmap and external MCP interfaces.
- Closure path: memory may be written and retrieved in later tasks, but no identified outside-prospective distinction → adaptation option → authorized/operational capability-change decision exists in the shipped loop.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: the model can produce memory notes, but persistence of past experience is not by itself ownership of future-oriented organizational intelligence.
- Evidence: [memory manager](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/memory/manager.py), [memory store](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/memory/store.py), [architecture](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/docs/architecture.md), [skills](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/skills/executor.py).
- Basis: structural.
- Confidence: medium.
- Caveats: model-mediated persistent notes may influence future sessions, but prospective external discrimination and capability change were not separately established.

### Absence scope

- Surfaces inspected: model-based memory updates, project/user memory store and prompt injection, skills/hooks, context compaction, provider/MCP integration, coordinator's current planning mode and adjacent roadmap.
- Plausible first-party paths checked: post-turn notes, cross-session recall, external provider and tool observations, project instructions and future feature plan.
- Why no material first-party path remains: these support current task/reuse or static extensions; they do not close a prospective environment-intelligence decision into materially changed organizational capability at the reviewed boundary.

## S5 — Policy and identity

- State: —
- Function: no evidenced whole-system ultimate-purpose or identity-policy arbiter with an authoritative returned policy decision at the declared team/session recursion.
- Disturbance / variety regulated: tool permissions, agent roles and team membership limit operations, but do not decide constitutional identity or ultimate purpose.
- Decisive decision or feedback right: no qualifying ultimate-policy decision established.
- Decision owner: not established for S5; users configure modes/permissions, not a legitimate S5 parent decision cycle.
- Supporting / enforcement mechanisms: static system prompt, coordinator role switch, project instructions, owner permissions, tool blacklist and sandbox, approvals.
- Closure path: operator approvals can change one tool call, but no identity-policy matter reaches a legitimate ultimate authority and returns to govern the system's constitutional identity.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: if model is removed, static control rules remain, but no model-owned ultimate purpose decision remains; human approval alone is not the parent S5 loop.
- Evidence: [coordinator policy](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/coordinator/__init__.py), [permissions](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/permission/engine.py), [instructions](https://github.com/yangf-Veda/KairoCode/blob/018c74035de1354f69a92eda626ddbb210fbebcc/src/kairocode/instructions/loader.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a human-founded open-source project's external governance is not silently imported as a first-party S5 parent for local KairoCode runs.

### Absence scope

- Surfaces inspected: `coordinator` role/flag, permission/approval modes, task/team registry, memory/project instructions and prompt/hook loading.
- Plausible first-party paths checked: top-level owner configuring Coordinator mode, human approvals, editable policy files, team creation and agent-generated runtime instructions.
- Why no material first-party path remains: reviewed paths configure task/authority limits without deciding and returning ultimate organizational purpose/identity policy at the session/team recursion.

## Recursion

One local coding session constitutes the assessed parent operational organization. With Team mode enabled, several independently model-driven child S1 units appear under its coordinator. This is a local team recursion: it does not turn separate users, remote providers, repository contributors or external terminal backends into a proven larger VSM.

## Variety and escalation

Coding disturbances are handled through iterative tool feedback. Permission exceptions are escalated to the user. Tasks may block on explicit dependencies and subordinate reports can be returned through the team mailbox. The optional model-led Coordinator changes current team commitments, but no separately established inter-worker interference controller is credited. Model-written memory persists contextual information but not a demonstrated prospective S4 adaptation policy. Tool, status and error signals are not themselves an algedonic channel or another VSM function.

## Evidence gaps

- S2: source-first reviewer should independently test whether worktree isolation and task dependency signals establish a specific S2 constructor rather than ordinary multi-agent scheduling. No conflict-detect/integration-feedback close was observed in reviewed first-party worktree and team logic.
- S3*: coordinator prompt names Verification and independent child sessions can read artifacts; shipped audit independence, audit-specific authority and feedback to corrective intervention remain unclear. Retain `?` rather than awarding S3* from role naming.
- S3: optional Coordinator reachability requires explicit feature/environment enablement and a working model/team backend, and should not be generalized to default solo operation.
- No provider-backed end-to-end live run was performed; verdict is bounded to frozen source and documented first-party runtime wiring.
