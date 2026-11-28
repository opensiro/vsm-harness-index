---
harness_id: jucode-cli
project_name: JuCode CLI
repository: https://github.com/luo-ca/JuCode-CLI-OSS
review_ref: c012eb09d7ebee3fd0d7536330052e86c2c2193e
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# JuCode CLI

## Review boundary

- System in focus: One JuCode CLI session, its persistent objective and native child runs.
- Purpose and identity: Carry out model-directed code work in the user's workspace.
- Relevant environment: A local repository, a configured model provider and the operator or supported client.
- Standard-distribution boundary: Rust agent core, TUI, headless and ACP entry points, native tool and subagent runtime.
- Credited operating / distribution surfaces: Native CLI session, supported client/daemon access to the native engine, permissions and goal controls.
- Adjacent first-party surfaces excluded from ownership: External Claude and Codex engine internals, external model services, source-development tests and maintainers.
- First-party operating / deployment modes considered: TUI, headless and ACP native execution. The daemon can host sessions. External daemon engines are not credited as JuCode agent logic.
- Recursion level: One session with nested subagent operations.
- Reviewed revision: c012eb09d7ebee3fd0d7536330052e86c2c2193e
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The Rust core owns persisted sessions, the request worker, tool calls, permissions, a goal record and a subagent registry. TUI and headless modes expose the model-directed agent with different approval settings. The session scheduler can start a follow-up turn for an active goal after a turn has ended.

## Operational model

The main model selects investigation and edit operations and can delegate bounded results to child loops. The objective may survive many worker turns. The user can explicitly pause or replace it, reprioritize an incoming request or stop the active turn and its child work.

## S1 — Operations

- State: A
- Function: Investigate or change a workspace and deliver a task result.
- Disturbance / variety regulated: Tool failures, changing files and heterogeneous code tasks.
- Decisive decision or feedback right: Choose and repeat workspace actions from task context and observations.
- Decision owner: The model in the shipped agent core.
- Supporting / enforcement mechanisms: TUI or headless transport, tool registry, tool approval policy and workspace constraints.
- Closure path: Provider replies choose calls. Tool results enter the session and subsequent model turns until a final response or runtime interruption.
- Boundary reachability: The documented CLI and ACP supply the native loop and tools. A configured compatible provider exercises the actor without developer composition.
- Why this is / is not agent-owned: The host can protect files and execute a selected action, while the next task action and response depend on model judgment.
- Evidence: [README.md](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/README.md#L139-L150), [README.md](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/README.md#L186-L212), [README.md](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/README.md#L232-L256), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L651-L695), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L1646-L1665)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Manual headless mode can deny mutating tools. An explicitly supported approval mode allows agent closure.

## S2 — Coordination

- State: —
- Function: Interference regulation was sought among main and child execution loops.
- Disturbance / variety regulated: Concurrent workspace edits or overlapping delegated tasks can interfere.
- Decisive decision or feedback right: No distinct first-party decision relation selects or returns inter-worker conflict resolution.
- Decision owner: A model may construct a coordination convention via generic messaging.
- Supporting / enforcement mechanisms: Spawn and wait tools, child routing, message queues and worktree support.
- Closure path: Messages enter subsequent child requests and completed results return to the requester, with no native interference-specific disposition.
- Why this is / is not agent-owned: Message delivery and waiting implement communication and delegation. The supplied runtime does not decide what should change when workers overlap.
- Evidence: [README.md](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/README.md#L249-L257), [crates/agent-core/src/subagents.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/subagents.rs#L399-L426), [crates/agent-core/src/subagents.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/subagents.rs#L518-L547), [crates/agent-core/src/llm.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/llm.rs#L1570-L1602)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: A custom prompt might coordinate task overlap.

### Absence scope

- Surfaces inspected: Native registry, wait and send controls, child context return, worktree handling and TUI controls.
- Plausible first-party paths checked: Change conflict/reassignment feedback, concurrent workspace ownership and negotiated edits between active S1 units.
- Why no material first-party path remains: The code transports arbitrary messages and tracks execution. It supplies no function-specific interference signal with a return that revises both operations.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate whether the session's current objective continues across worker turns and which queued commitment runs next under supervision.
- Disturbance / variety regulated: A completed turn can leave a live session objective unfinished, blocked or superseded by a higher-priority request.
- Decisive decision or feedback right: Decide whether the persisted objective remains active or should stop. The operator can pause, resume, replace or explicitly supersede it.
- Decision owner: Main-session model for autonomous goal disposition. User for parent-owned goal and queue overrides.
- Supporting / enforcement mechanisms: Goal state, budget accounting, queue events, turn interruption and follow-up worker start.
- Closure path: The goal state controls subsequent turns beyond the ordinary turn finish. The user can also return a changed commitment or stop the current turn and start queued work.
- Boundary reachability: The supplied core exposes the goal tools in the main session and the TUI goal and steering commands. The follow-up turn uses current session state.
- Why this is / is not agent-owned: A worker turn ending does not itself close the encompassing commitment. The goal owner separately selects complete or blocked, and the returned state controls future execution.
- Whole-system current view: Current persisted objective, goal status and usage, queued input and session transcript give the relevant current session view.
- Current-control decision scope: Retain or close the persistent objective across turns. In parent mode, pause or replace it, or preempt it with a selected queued request.
- Evidence: [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L1765-L1797), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L2480-L2502), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L3063-L3108), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L4127-L4158), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L753-L782)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The goal tool marks the model's disposition. It does not independently prove the work was correctly verified.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Main-session model | An active goal remains after a turn | The model marks complete or blocked; goal status controls whether another turn is scheduled | [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L1784-L1796), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L2480-L2502), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L3075-L3105) |
| Parent (`P`) | Session operator | The active objective or queue no longer reflects the user's priority | Goal status or objective changes persist. Interrupt-and-send stops the current turn and starts the selected commitment | [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L753-L782), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L4127-L4158) |

## S3* — Complementary audit

- State: —
- Function: Complementary checking of the producing model's work and completion claim was sought.
- Disturbance / variety regulated: A task model can assert completion without sufficient artifact evidence.
- Decisive decision or feedback right: No shipped auditor is commissioned to access operational evidence and return a completion disposition.
- Decision owner: The session agent selects checks as part of its task work.
- Supporting / enforcement mechanisms: Shell checks, diff previews, child-agent requests, approvals and goal status.
- Closure path: The model can reason about test output. Pending plan and tool review gate proposed actions, and goal completion can be set by the producer.
- Why this is / is not agent-owned: A generic child can receive a review request through delegation. It has no supplied independent mandate or mandatory return into completed-task adjudication.
- Evidence: [README.md](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/README.md#L114-L127), [README.md](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/README.md#L236-L258), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L2531-L2578), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L3085-L3105)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Provider-side risk approval and pre-execution approvals are present.

### Absence scope

- Surfaces inspected: Model tool list, subagent registry, plan approval, tool approval receiver and goal completion dispatch.
- Plausible first-party paths checked: Separate verification role, direct evidence on claimed completion and findings that reopen or stop the relevant goal.
- Why no material first-party path remains: The supplied verification prompt remains with the producer. Risk and policy approve an intended action and do not audit delivered outcome evidence.

## S4 — Outside-and-then intelligence

- State: —
- Function: Future-facing capability adaptation was sought across sessions and tool configuration.
- Disturbance / variety regulated: Shifts in model, task or tool demands across future sessions.
- Decisive decision or feedback right: No supported judgment loop selects a new capability from those external changes.
- Decision owner: Operators select configured resources and releases; helpers react to immediate context.
- Supporting / enforcement mechanisms: Update check, provider configuration, context compaction and lifecycle-managed skills.
- Closure path: Current context changes the next request. Update and configuration surfaces do not connect prospective evidence to a runtime capability decision.
- Why this is / is not agent-owned: Persistence and compaction carry task evidence. Updating a package or editing model settings follows a supplied choice.
- Evidence: [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L485-L489), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L1204-L1222), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L2395-L2430), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L1765-L1782), [README.md](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/README.md#L51-L60)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Operators can change models, tools or installed versions between runs.

### Absence scope

- Surfaces inspected: Update and model settings, skill lifecycle, session summaries, and maintained output projection.
- Plausible first-party paths checked: Automatic learning from cross-session results, scenario comparison, and governed capability return.
- Why no material first-party path remains: The active supplied flows maintain information or apply settings. No prospective option evaluation and returned decision is evidenced.

## S5 — Policy and identity

- State: —
- Function: Ultimate policy and identity governance was sought at session level.
- Disturbance / variety regulated: The user's task priorities or tool constraints can conflict.
- Decisive decision or feedback right: No installed identity-level matter is admitted and authoritatively resolved as an operating policy change.
- Decision owner: Users choose goals and permissions. The system prompt and runtime constrain execution.
- Supporting / enforcement mechanisms: Approval modes, sandbox enforcement, config files and session goal commands.
- Closure path: Session settings affect tasks and tool calls, without a supplied policy arbitration path.
- Why this is / is not agent-owned: A task objective or approval choice operates within the installed harness's purpose. The actor is not supplied as an owner of ultimate identity or policy.
- Evidence: [README.md](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/README.md#L67-L90), [README.md](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/README.md#L114-L127), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L2531-L2578), [crates/agent-core/src/core.rs](https://github.com/luo-ca/JuCode-CLI-OSS/blob/c012eb09d7ebee3fd0d7536330052e86c2c2193e/crates/agent-core/src/core.rs#L4127-L4158)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: OSS maintainer governance and external backend policy are outside the session boundary.

### Absence scope

- Surfaces inspected: User goal/permission controls, runtime config and agent tool allow/deny paths.
- Plausible first-party paths checked: Mission conflict resolution, delegated policy adoption and return of an identity ruling.
- Why no material first-party path remains: The session uses policy settings and goal controls to execute work. It does not raise and resolve ultimate-policy matters.

## Recursion

Child runs execute delegated operations within the session. The persistent objective is assessed at the enclosing session boundary, above the work done by an individual turn.

## Variety and escalation

Approvals, bounded working directories, message queues, context compaction and goal status manage immediate variety. A blocked goal or approval can return to the operator, with no claim of a separate algedonic channel.

## Evidence gaps

Public Rust source only. No provider run, daemon engine interoperability, inter-agent collision test or live approval trace was executed. Actual correctness of agent-selected goal closure is unevaluated.
