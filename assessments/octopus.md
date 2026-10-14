---
harness_id: octopus
project_name: Octopus
repository: https://github.com/zwpdbh/octopus-in-rust
review_ref: 88695f8e9209c76522d5943a2207751fd382dd43
reviewed_at: 2026-10-11
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

# Octopus

## Review boundary

- System in focus: the installed first-party `octopus-cli` terminal coding agent plus the reusable `agent-core` runtime it actually calls, at one local coding-session/workspace recursion. Native model/tool operations and optional foreground/background spawned `coder`, `explore` and `plan` subagents are examined within that boundary.
- Purpose and identity: carry out a user's repository investigation, edits, command execution and code planning through the Kimi-inspired Rust coding agent, with permission, tools, model feedback and subordinate task sessions.
- Relevant environment: user's repository/filesystem, command outputs, external model API, MCP tool servers, tool approval, session history, running child agents and background shell commands.
- Standard-distribution boundary: the public pinned Cargo workspace's `apps/octopus-cli`, native `crates/agent-core` and `crates/llm-provider` as reached from CLI, including built-in profiles, background task manager, notifications, hooks/approvals and checkpointing. Separately runnable QQ bot, FAF game-companion web/API, ML training, simulation and UI applications in the same monorepo are **distinct deployments**, not automatically native S1 workers or metasystemic governance of the terminal coding agent.
- Credited operating / distribution surfaces: [README.md](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/README.md); [Cargo.toml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/Cargo.toml); [apps/octopus-cli/src/main.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/main.rs); [apps/octopus-cli/src/app.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/app.rs); [apps/octopus-cli/src/soul/agent.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/agent.rs); [apps/octopus-cli/src/soul/kimisoul.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/kimisoul.rs); [apps/octopus-cli/src/soul/brain_bridge.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/brain_bridge.rs); [apps/octopus-cli/src/tools/agent/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/agent/mod.rs); [apps/octopus-cli/src/subagents/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/subagents/mod.rs); [apps/octopus-cli/src/agents/default/agent.yaml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/agents/default/agent.yaml); [apps/octopus-cli/src/background/manager.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/background/manager.rs); [apps/octopus-cli/src/tools/background/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/background/mod.rs); [apps/octopus-cli/src/approval_runtime/runtime.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/approval_runtime/runtime.rs); [apps/octopus-cli/src/notifications/manager.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/notifications/manager.rs); [apps/octopus-cli/src/hooks/engine.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/hooks/engine.rs); [crates/agent-core/src/core/brain.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/brain.rs); [crates/agent-core/src/core/step.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/step.rs); [crates/agent-core/src/core/recovery.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/recovery.rs); [crates/agent-core/src/core/approval.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/approval.rs); [crates/agent-core/src/core/checkpoint.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/checkpoint.rs).
- Adjacent first-party surfaces excluded from ownership: [apps/qqbot-core/src/main.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/qqbot-core/src/main.rs), [apps/fafcn-server/src/main.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/fafcn-server/src/main.rs) and [apps/faf-ml-server/src/main.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/faf-ml-server/src/main.rs) are separate app/deployment organizations even if they consume the same `agent-core`. `apps/fafcn-web`, game simulation, training and [.github/workflows/ci.yml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/.github/workflows/ci.yml) are not the coding-agent's runtime S3*/S4/S5. Maintainer [AGENTS.md](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/AGENTS.md) and [STATUS.md](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/STATUS.md) are contributor governance/status, not executed native system policy.
- First-party operating/deployment modes considered: CLI root `Agent` and `KimiSoul`; streaming model/tool loops, foreground `Agent` subagents, optional `execution_mode=background` native subagents, shared approval source and separate subagent sessions, running process/status registry, approval/notification hooks and code-plan mode, checkpoint and DMail operational recovery, external MCP tools, independently operated application/server binaries.
- Recursion level: one terminal coding session and its subordinate agent tasks at the first-party product boundary. Reuse of `agent-core` by standalone QQ/FAF applications is a library dependency, not evidence of their coordination inside this one agent's organizational recursion.
- Reviewed revision: 88695f8e9209c76522d5943a2207751fd382dd43.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The public Cargo workspace contains over two thousand tracked files and multiple independently launched applications. [README.md](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/README.md) and [Cargo.toml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/Cargo.toml) distinguish the `octopus-cli` terminal agent from QQ group bot, FAF companion, simulations, ML servers and game UI. The assessed terminal agent starts through [apps/octopus-cli/src/main.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/main.rs), constructs the Kimi-inspired session/runtime in [apps/octopus-cli/src/app.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/app.rs) and [apps/octopus-cli/src/soul/agent.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/agent.rs), and bridges it to [crates/agent-core/src/core/brain.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/brain.rs) and tool registry through [apps/octopus-cli/src/soul/brain_bridge.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/brain_bridge.rs). The reusable `Brain` streams tool-call and result events and supports per-step continuation, retries, recovery policy and checkpoint hooks. Native file, shell, plan and MCP tools can alter the coding workspace subject to permissions; [apps/octopus-cli/src/approval_runtime/runtime.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/approval_runtime/runtime.rs) receives human approval decisions with specific task/agent source tags.

Actual first-party child agents exist: [apps/octopus-cli/src/tools/agent/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/agent/mod.rs) implements `Agent` tool calls in foreground and background. The foreground awaits a child `KimiSoul`'s run; the background spawns `tokio::spawn` with an independently model-directed agent session and logs completion/failure. [apps/octopus-cli/src/subagents/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/subagents/mod.rs) exposes a `LaborMarket` of `coder/explore/plan` built-ins, with `SubagentStore` tracking `Running/Completed/Failed` and a result string for each child. [apps/octopus-cli/src/agents/default/agent.yaml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/agents/default/agent.yaml) registers `Agent`, planning, shell, file and background-task tools and built-in role specifications. Subagent task sessions and separate prompt/tool choices qualify as operational subunits under S1, including while a background worker overlaps the parent. However, a status registry plus dispatch does not establish dedicated conflict regulation across simultaneous child operations.

The source supplies richer local runtime infrastructure: [apps/octopus-cli/src/background/manager.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/background/manager.rs) starts/monitors/kills shell tasks; [apps/octopus-cli/src/tools/background/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/background/mod.rs) returns their output. [apps/octopus-cli/src/notifications/manager.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/notifications/manager.rs) and [apps/octopus-cli/src/approval_runtime/runtime.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/approval_runtime/runtime.rs) route status or per-tool consent. [apps/octopus-cli/src/soul/agent.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/agent.rs) persists conversation checkpoint identifiers, and [apps/octopus-cli/src/tools/dmail/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/dmail/mod.rs) can request a rollback-with-message to an earlier single-agent checkpoint; these are operative correction/memory tools, not future intelligence or audit. The default `explore` and `plan` subagent roles are task functions; no source-backed separate raw-artifact audit mandate and control-return was observed. Hook events and plugin tool interfaces extend execution but do not inherit decisions from external modules that are not first-party shipped.

## Operational model

One root model-driven coding agent can delegate first-party bounded tasks to additional model-driven child agents. Some children may run asynchronously and share a workspace, session-derived permissions and status store, while a root tool call may obtain a child report in foreground. Root-level task splitting, a centralized permit queue and background process status constitute orchestration/support but do **not by themselves** establish a specific S2 mechanism detecting/attenuating *cross-S1 collisions* or S3 management of the whole-current organization. The chosen recursion has no demonstrated shared-workflow task-ownership arbitration, current-team resource reprioritization based on a governed global view, independent complementary audit of producer claims, prospective environmental strategy loop or ultimate identity/policy return.

## S1 — Operations

- State: A
- Function: pursue user-specified coding outcomes and focused subagent investigations/edits using model-chosen tools and first-party execution-feedback loops.
- Disturbance / variety regulated: repository uncertainty, failing tools, changing source/workspace state, subtask results, interruptions, provider and permission errors, and needed plan adjustments.
- Decisive decision or feedback right: root or child model selects the next code-reading, editing, command, plan, search or delegated task and adapts after actual returned result.
- Decision owner: first-party `octopus-cli` `KimiSoul` model and child `Agent` sessions; the external model provider performs inference but native `Brain` and agent tools own the workflow and action routing.
- Supporting / enforcement mechanisms: `agent-core` streaming Brain, KimiSoul toolset, tool registry, prompt profiles, hooks, permissions, checkpoints, background task manager and child status store.
- Closure path: user task → native coding-agent model/tool call → approval and real tool/subagent execution → observation or child report → same model's next coding decision or terminal response.
- Boundary reachability: [apps/octopus-cli/src/agents/default/agent.yaml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/agents/default/agent.yaml) registers the native `Agent` tool; [apps/octopus-cli/src/tools/agent/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/agent/mod.rs) creates and runs named child sessions with own model/tool loop, while [crates/agent-core/src/core/brain.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/brain.rs) implements executable streamed tool/result turns for the native root runtime.
- Why this is / is not agent-owned: without model-selected actions and interpretation of tool/subagent outcomes, file/LLM transports and status stores cannot choose what work to do next.
- Evidence: [apps/octopus-cli/src/soul/agent.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/agent.rs); [apps/octopus-cli/src/soul/kimisoul.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/kimisoul.rs); [apps/octopus-cli/src/soul/brain_bridge.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/brain_bridge.rs); [apps/octopus-cli/src/tools/agent/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/agent/mod.rs); [crates/agent-core/src/core/brain.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/brain.rs); [apps/octopus-cli/src/agents/default/agent.yaml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/agents/default/agent.yaml).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: this demonstrates first-party operational model rights, not success in any live programming benchmark or all model settings.

## S2 — Coordination

- State: —
- Function: no implemented native inter-S1 interference/oscillation attenuation relation is demonstrated for the concurrently runnable coding subagents at this recursion.
- Disturbance / variety regulated: overlapping parent/child or child/child actions could contend for the same files, task responsibility or tool permissions; the source provides child launch/status and user-approved tool execution but not collision-specific conflict detection and feedback.
- Decisive decision or feedback right: no established native mutually-exclusive work claim, inter-agent dependency arbitration, shared write conflict adjudication or returned attenuation to conflicting S1s. Approval is about user permission for each requested tool action, not collision between peer commitments.
- Decision owner: root model for delegation and standard permission/runtime for operation gating; no observed distinct S2 coordination decision.
- Supporting / enforcement mechanisms: `LaborMarket` for task role selection, `SubagentStore` for running/completed/error status, shared approval callback with source IDs, background shell task controls and notification broker.
- Closure path: a delegated child runs its own task and may complete asynchronously; shared registry and approvals track each task, but no conflict-specific outcome is returned to *multiple* S1s to attenuate their interference.
- Why this is / is not agent-owned: concurrent spawning and monitoring is not itself collision arbitration; agent roles, status messages, and one approval queue do not demonstrate cross-agent conflict regulation.
- Evidence: [apps/octopus-cli/src/tools/agent/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/agent/mod.rs); [apps/octopus-cli/src/subagents/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/subagents/mod.rs); [apps/octopus-cli/src/approval_runtime/runtime.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/approval_runtime/runtime.rs); [apps/octopus-cli/src/background/manager.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/background/manager.rs); [apps/octopus-cli/src/tools/background/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/background/mod.rs); [apps/octopus-cli/src/notifications/manager.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/notifications/manager.rs).
- Basis: structural.
- Confidence: medium.
- Caveats: native background child tasks can genuinely run in parallel; their concurrency is acknowledged rather than denied. The negative is the absence of a demonstrated collision-specific *coordination relation*, not absence of multiple active agents.

### Absence scope

- Surfaces inspected: foreground/background subagent spawn and status, approval source tagging and queue, runtime tool dispatch and hooks, background shell task management, default agent role specs, shared workspace, notifications and nested agent capabilities.
- Plausible first-party paths checked: two simultaneously active independently operating children contending for one work item/file; reservation, lock, arbitration or feedback to both; priority/dependency conflict detection distinct from ordinary user tool permission; coordination via broker or shared task store.
- Why no material first-party path remains: reviewed machinery registers child identities, reports completion/failure, approves individual tool actions and monitors processes, but no collision-aware rule/decision and consequential inter-agent S2 return was established.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current organization management owner with an evidenced global resource/commitment judgment returned to several simultaneously operating S1s was found.
- Disturbance / variety regulated: task decomposition, background children and tool failures are handled as the root coding request. A list of running subagents exists but no first-party portfolio status→reassignment/control loop spanning current commitments was demonstrated.
- Decisive decision or feedback right: the root chooses to spawn a requested child, tool approvals constrain execution and subagent records can be queried in code; neither establishes whole-current reprioritization of a team/work portfolio.
- Decision owner: root coding agent for task delegation and human user for tool consent, not an evidenced S3 controller of all current operative units.
- Supporting / enforcement mechanisms: typed `Agent` tool and task/result store, per-child approval source and session, local background task manager, notifications, prompt role policies and UI event streams.
- Closure path: child tool results may return to the root for further coding, or background completion is recorded/logged; no whole-current status view with an owned global management decision and returned commitment change to multiple active workers is established.
- Why this is / is not agent-owned: choosing individual delegates and checking status is operational orchestration for the current request. A native parent model would need a demonstrated distinct global/current management right and closed corrective return to justify S3, not just tool access to async children.
- Evidence: [apps/octopus-cli/src/tools/agent/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/agent/mod.rs); [apps/octopus-cli/src/subagents/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/subagents/mod.rs); [apps/octopus-cli/src/soul/agent.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/agent.rs); [apps/octopus-cli/src/notifications/manager.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/notifications/manager.rs); [crates/agent-core/src/control.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/control.rs).
- Basis: structural.
- Confidence: medium.
- Caveats: other standalone bot/web service deployments may have their own operational oversight; those different recursions are not imported as terminal coding S3 owners.

### Absence scope

- Surfaces inspected: root tool availability, role/child registration, status/result storage, notification and approval paths, current shell/agent tasks, external service applications, overall CLI runtime.
- Plausible first-party paths checked: global current view of independently active S1s and dependencies, parent budget/resource/priority judgment, subordinate reallocation or suspension on cross-work conflict, intervention notification and returned changed current obligations.
- Why no material first-party path remains: the CLI exposes delegation and status machinery but not a closed metasystemic global decision with consequential commitments returned to several operational units; other workspace binaries are separate products.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary audit with sufficiently independent raw-evidence access, separate judgment and consequential return to present organizational control was demonstrated.
- Disturbance / variety regulated: code may be wrong, shell may fail, model summaries may be overconfident; standard tool results, build CI or self-requested exploration may expose errors but are routine task feedback.
- Decisive decision or feedback right: no separate audit selector/mandate distinct from the producing model and current task role that probes alternative primary evidence and makes an accountable audit judgment for current management.
- Decision owner: root or child executing tasks, user for approval and maintainer CI for external development checks; no native S3* auditor/manager identified at this recursion.
- Supporting / enforcement mechanisms: file/command result logs, hooks on tool use/failure, status notifications, `explore` role with read-only prompt policy, checkpoint/rollback DMail, developer workflows.
- Closure path: tool outcomes, hook events and reports return to the same task loop or user; no independent adversarial audit → findings → distinct current control decision → corrected operational follow-up is wired.
- Why this is / is not agent-owned: a model with read-only tools or separate session can perform code search, but a generic `explore` subtask and hook are not independently commissioned risk-based audit/alternate truth with returned S3* authority.
- Evidence: [apps/octopus-cli/src/agents/default/agent.yaml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/agents/default/agent.yaml); [apps/octopus-cli/src/agents/default/explore.yaml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/agents/default/explore.yaml); [apps/octopus-cli/src/tools/agent/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/agent/mod.rs); [apps/octopus-cli/src/hooks/engine.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/hooks/engine.rs); [crates/agent-core/src/hooks/policy.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/hooks/policy.rs); [apps/octopus-cli/src/soul/brain_bridge.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/brain_bridge.rs); [.github/workflows/ci.yml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/.github/workflows/ci.yml).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a user might compose an external auditor using generic tools, but no specific shipped independent complementary audit mode is shown here.

### Absence scope

- Surfaces inspected: native subagent role specifications and tool policies, first-party hook engine and callback policy, logs, checkpoints, status notifications, user approvals, maintainer CI, external web/QQ bot contexts.
- Plausible first-party paths checked: independent source sampling or replay, dedicated adversarial verifier with operationally distinct evidence, audit findings returned to a whole-current S3 owner, reinspection/reaction affecting subordinate operation.
- Why no material first-party path remains: code supports generic child exploratory tasks and routine production hooks, not a separable complementary audit mandate/judgment/returned control loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective external environment modelling with adaptation options returned into present managerial capability choices was established at the coding-agent recursion.
- Disturbance / variety regulated: provider errors, new user tasks, changing source files, plugin availability, background task events and prompt context are operational disturbances, not forecast-driven future capability management.
- Decisive decision or feedback right: runtime retries/recovery rules and model-guided coding/plans govern current operations; no future-facing option generator and S4→S3 returned tradeoff decision is implemented.
- Decision owner: current operative agent for task steps; developer/user for plugin/provider/tool configurations, not an evidenced native S4 intelligence authority.
- Supporting / enforcement mechanisms: retry/backoff, recovery policy, compaction, prompt injection, plugin discovery, session state and task planning.
- Closure path: new tool or source information informs current model context and retries; no externally prospective sensing → tested adaptation alternatives → current organization management conversation → new capability commitment cycle.
- Why this is / is not agent-owned: memory, planning, checkpoint rollback and newly available plugins aid current task execution but do not meet the future-oriented organizational adaptation criterion.
- Evidence: [crates/agent-core/src/core/retry.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/retry.rs); [crates/agent-core/src/core/recovery.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/recovery.rs); [crates/agent-core/src/session/compaction.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/session/compaction.rs); [apps/octopus-cli/src/soul/dynamic_injection.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/dynamic_injection.rs); [apps/octopus-cli/src/plugin/discovery.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/plugin/discovery.rs); [apps/octopus-cli/src/tools/plan/mod.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/tools/plan/mod.rs).
- Basis: structural.
- Confidence: medium-high.
- Caveats: the same monorepo hosts external-facing applications with their own changing market/user contexts; they are separate from the specified installed coding agent.

### Absence scope

- Surfaces inspected: model/provider selection, retry/recovery and DMail, prompt/history, plugins and background tools, plan mode, session/notification services, other workspace apps.
- Plausible first-party paths checked: proactive future environmental distinctions, generated comparative capability adaptation options, tests or feedback on alternatives, two-way option/constraint conversation with whole-current control and operationally enacted future adaptation.
- Why no material first-party path remains: all inspected first-party coding paths respond to current requests/errors or fixed configuration; no native prospective intelligence closure is supplied.

## S5 — Policy and identity

- State: —
- Function: no first-party highest-level identity/ultimate-policy decision authority and returned binding governance path is established for this terminal coding agent.
- Disturbance / variety regulated: tool execution safety, human approvals, read-only exploration, model settings and plugin permissions concern immediate technical boundaries, not competing identity/mission claims.
- Decisive decision or feedback right: users approve/deny particular operations, runtime applies approved/denied tool modes; maintainer AGENTS.md defines contribution rules but not executable legitimate first-party ultimate-policy arbitration.
- Decision owner: operator for local consent and developer for static tool policies, not a verified S5 actor resolving current/future whole-system identity conflicts.
- Supporting / enforcement mechanisms: tool approval, per-subagent approval source/queue, default role tool policy, security hooks and provider configurations.
- Closure path: unsafe tool request is denied or allowed, which affects the current task; no durable supreme identity/ethos decision returns to S3/S4 governance of subsequent operations.
- Why this is / is not agent-owned: ordinary human permission decisions or source policy text do not create a genuine highest-authority organizational policy loop.
- Evidence: [apps/octopus-cli/src/approval_runtime/runtime.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/approval_runtime/runtime.rs); [crates/agent-core/src/core/approval.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/crates/agent-core/src/core/approval.rs); [apps/octopus-cli/src/soul/approval.rs](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/soul/approval.rs); [apps/octopus-cli/src/agents/default/agent.yaml](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/apps/octopus-cli/src/agents/default/agent.yaml); [AGENTS.md](https://github.com/zwpdbh/octopus-in-rust/blob/88695f8e9209c76522d5943a2207751fd382dd43/AGENTS.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: user organization, project maintainers or app-specific human policies may exercise legitimate governance externally, not as first-party native S5 for this coding agent.

### Absence scope

- Surfaces inspected: permission prompts/runtime, subagent approval source, tool/prompt role restrictions, maintainer docs, planning and plugin config, shared library/application boundary.
- Plausible first-party paths checked: ultimate identity conflict detection/escalation, legitimate policy authority beyond task consent, binding decision reconciling future/current organizational objectives and policy return to a native whole-current parent.
- Why no material first-party path remains: the native mechanisms authorize operations and enforce role-specific tool restrictions, without an implemented supreme-policy decision-and-return loop.

## Recursion

`octopus-cli` is the evaluated first-party coding installation with native operational child agents. Distinct `qqbot-core` and `fafcn-server` processes may reuse the same `agent-core` crate but are independent deployment organizations; their presence in one Cargo workspace does not establish that CLI has team-wide S3 or S5 authority over them. Background child agents can be simultaneous S1s but there is no observed inter-worker S2 arbitration. Checkpoints, DMail and hooks are task-operational support, not evidence that the full multi-application ecosystem has been integrated under native management at this recursion.

## Variety and escalation

Changes in source and user request drive the root coding loop, and subordinate agents amplify work variety through specialized independent model/tool sessions. Background agent/tool status and centralized approval capture operational events and constrain allowed actions. Failed shell/tool outcomes and hook events may trigger S1 corrective decisions; status logging is not collision regulation, and role-specific agents do not inherit independent audit authority. Retry/compaction and conversation rollback maintain task progress but do not create forward-facing S4. Local permission approval does not constitute identity S5.

## Evidence gaps

This is bounded source-first review of the pinned public revision and actual first-party installed CLI paths; no cargo build, external provider-backed run or performance result was claimed. The monorepo has other executable services and many non-agent media/data assets; they are explicitly excluded from the chosen coding-agent recursion, rather than silently graded. The native code demonstrates concurrently runnable subordinate S1 agents but the inspected shared store, status, approval, hooks and notification paths do not demonstrate an S2 collision-feedback regulation loop. The `—` states follow source-bound negative calibration and do not preclude user-composed orchestration, future versions, or independently governed deployments.
