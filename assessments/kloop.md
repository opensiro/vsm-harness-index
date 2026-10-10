---
harness_id: kloop
project_name: Kloop
repository: https://github.com/lizc2003/kloop
review_ref: 5dbff2148f30a14737b8f661533b3c921470374e
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Kloop

## Review boundary

- System in focus: first-party Rust Kloop coding-agent runtime, model/tool loop, native coding tools, independent subagent sessions with optional worktree isolation, code-mode Workflow and permissions/session management.
- Purpose and identity: user-directed code changes and investigations on a local project with optional delegated bounded tasks, persistent evidence and safe shell/file operations.
- Relevant environment: local Git project files, source/test output, model provider, command shell, separate child checkout, trusted-project policies and persisted conversation state.
- Standard-distribution boundary: native Kloop Rust executable and shipped CLI/TUI/headless/app-server modes. External provider inference, MCP servers, optional user skill packs and developer benchmark/planning documents do not donate VSM ownership.
- Credited operating / distribution surfaces: rust/crates/core/src/agent.rs, native tool handlers, subagent, worktree, permissions, scheduler, skill/session state; CLI/TUI/server only insofar as wired to core.
- Adjacent first-party surfaces excluded from ownership: docs/plan future design proposals, benchmark fixtures, verifier of an external corpus, build CI/developer governance, third-party provider operations, optional SDK/plugin source.
- First-party operating / deployment modes considered: CLI interactive/headless coding; model-selected file/shell/notebook actions; run_agent synchronized/background real sidechains; explicit run_agent isolation: worktree; code-mode workflow, local agent mailbox, configured agents/hooks and user permission gates.
- Recursion level: user coding project, with primary model-driven coding S1 and distinct bounded coding subagents when dispatched. Mechanical bash/code-mode loops alone are not independently viable operational units.
- Reviewed revision: 5dbff2148f30a14737b8f661533b3c921470374e.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Kloop implements an independent Rust model/tool loop in core/agent.rs and ships native read/edit/write/bash/search/notebook/web and other tools. Provider wire protocols are implemented in its own provider crate. The model chooses tools, receives actual results in message history and continues or finishes; CLI/headless/app-server are entrypoints to the same owned engine.

The model may invoke run_agent to start real child coding/research tasks, synchronous or background, with their own bounded rounds and separate persisted sessions. Explicit isolation: worktree moves one child into a freshly provisioned Git checkout before its tool loop; failed provisioning halts launch instead of silently sharing cwd. The separate checkout dampens actual source-edit interference between sibling/parent coding workers but does not automatically arbitrate semantic merge conflicts. The choice of isolation is configured at dispatch, so a narrow compositional C-level S2 is proposed rather than autonomous full-time coordination.

Workflows, local agent messaging, background jobs, session forks and provider/model selection add useful task infrastructure. They do not prove separately owned whole-current S3 over active commitments or an independent complementary S3* audit loop. A user-created reviewer agent might inspect files in a distinct session, yet the default run_agent contract only returns text rather than requiring an independent diff audit/feedback gate. Project skills and historical sessions inform later operation without establishing prospective external-environment S4 capability renewal; user trust/permission/sandbox is not S5 policy governance.

Primary source evidence: [rust/crates/core/src/agent.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/agent.rs); [rust/crates/core/src/tools/subagent.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/subagent.rs); [rust/crates/core/src/worktree.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/worktree.rs); [rust/crates/core/src/permissions.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/permissions.rs); [rust/crates/core/src/agent_mailbox.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/agent_mailbox.rs).

## Operational model

Native coding S1 turns user goals into executable tool actions with observed feedback. Optional independently operating child model/tool loops can edit separately when worktree isolation is requested. The runtime persists each child session and returns its status/result, but does not by default provide a distinct whole-current priority authority or independent verification with corrective closure.

## S1 — Operations

- State: A
- Function: Autonomous source reads, edits, shell/test execution and tool observations in an operating user project.
- Disturbance / variety regulated: Unfamiliar files, user task requirements, failed commands, edits and changing tests.
- Decisive decision or feedback right: Model chooses source/tool actions and subsequent correction using real tool outputs.
- Decision owner: Native Rust core agent and independent bounded child model/tool sessions when explicitly delegated.
- Supporting / enforcement mechanisms: Provider wire protocols, owned run_turn, native ToolCtx/builtin tools, session history, permissions and sandbox.
- Closure path: Task → model selects file/edit/bash action → first-party tool handler operates on real repository → output enters model history → next action or finish.
- Boundary reachability: Shipped CLI/headless/server enters core run_turn implementation and dispatches source/shell tools; external models supply inference only.
- Why this is / is not agent-owned: The agent exercises ongoing operational discretion; Rust handlers carry out and constrain results.
- Evidence: [rust/crates/core/src/agent.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/agent.rs); [rust/crates/core/src/tools/mod.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/mod.rs); [rust/crates/core/src/tools/builtin.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/builtin.rs); [rust/crates/cli/src/main.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/cli/src/main.rs).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: Platform sandbox and provider endpoints are supporting services; no quality benchmark is inferred..


## S2 — Coordination

- State: C
- Function: Prevent actual file-write collisions between separately operating parent/child or sibling coding S1 sessions by independent Git worktrees.
- Disturbance / variety regulated: Two concurrently executing coding agents in one checkout can race when editing overlapping source files, corrupting or losing changes.
- Decisive decision or feedback right: The model/operator selects isolation: worktree for a child run; first-party runtime provisions independent branch/cwd before child actions and fails closed on errors.
- Decision owner: Composed parent/child task configuration and native worktree enforcement; not independently proven to be an autonomous inter-S1 conflict-negotiating regulator.
- Supporting / enforcement mechanisms: Validated Worktree API, per-child EffectiveWorkspace cwd, unique agent ids, scoped permissions and session logs.
- Closure path: Parent dispatches separate coding agent with worktree isolation → native tool creates separate checkout before spawn → child edits away from parent/siblings → output and workspace state return to parent for optional explicit integration.
- Boundary reachability: Builtin run_agent tool offers and actually implements isolation: worktree, used in the packaged agent loop; parent can launch several distinct coding task sessions.
- Why this is / is not agent-owned: Actual source-write interference is physically damped, not simply re-ordered or labeled. Agent/human composition plus deterministic provisioning justifies a bounded C reading.
- Evidence: [rust/crates/core/src/tools/subagent.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/subagent.rs); [rust/crates/core/src/tools/worktree_tool.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/worktree_tool.rs); [rust/crates/core/src/worktree.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/worktree.rs); [rust/crates/core/src/agent_mailbox.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/agent_mailbox.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Isolation is optional (default shared). No semantic merge conflict arbitration, review gate or adaptive negotiation is claimed..

- Distinct S1 units: Independent parent and real tool-using child coding agents with separate model turns/history and file-edit discretion.
- Inter-S1 disturbance: Simultaneous source writes in one checkout would overwrite or invalidate one worker's operating context.
- Attenuating coordination relation: Explicitly selected isolation: worktree makes the first-party launcher create a separate branch and working directory before the child loop; failure to create the worktree blocks launch.
- Feedback into subsequent S1 behaviour: The child edits only its isolated project copy and returns its bounded work report; parent can inspect or merge intentionally without inheriting surprise writes, changing subsequent operating choices.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Concrete cross-agent file mutation interference is structurally prevented by changed execution environments, not merely by message passing or dispatch labels.


## S3 — Inside-and-now control

- State: ?
- Function: Parent can launch/stop workers, receive messages and observe execution but no separate whole-current current-control owner is conclusively shown.
- Disturbance / variety regulated: Parallel children and background jobs can fail, consume budget, block others and compete for attention.
- Decisive decision or feedback right: Subagent spawn/stop and scheduler states are exposed; no clear source-wired discretionary aggregate resource reallocation or priority adjudication across active S1 units.
- Decision owner: Possible parent coding model and task launcher, backed by fixed scheduler/agent mailbox; organizational S3 judgment unresolved.
- Supporting / enforcement mechanisms: Background agent sessions, mailbox with caps, scheduler execution records and stop controls.
- Closure path: A child result or error returns to parent conversation; that permits task follow-up but does not independently demonstrate whole-current multi-unit regulatory decisions.
- Why this is / is not agent-owned: Tool orchestration, queues, worker directories, status and cancellation are supports, not S3 by name.
- Evidence: [rust/crates/core/src/tools/subagent.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/subagent.rs); [rust/crates/core/src/agent_mailbox.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/agent_mailbox.rs); [rust/crates/core/src/scheduler.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/scheduler.rs); [rust/crates/core/src/tools/workflow.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/workflow.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: A user can assemble a broader run structure, but it is not automatically the system-in-focus..


## S3* — Complementary audit

- State: ?
- Function: Separate child agent/persona may review source and return a report, but first-party mandatory independent evidence-acquisition → corrective-code loop is not demonstrated.
- Disturbance / variety regulated: Agent may incorrectly conclude the edit solved the requested coding problem.
- Decisive decision or feedback right: Generic run_agent can dispatch a custom reviewer role or workflow, but its source/evidence policy and own return to repair are user/model supplied.
- Decision owner: Potential child reviewer selected by parent; separate model/tool context is possible, but auditor-owned corrective closure not established as a stock mode.
- Supporting / enforcement mechanisms: Agent-type prompts/tool allowlists, session lineage, optional hooks and permission gates.
- Closure path: Child reviewer text returns as one tool result; parent may choose to fix but there is no source-proven independent review receipt gating completion and driving automatic corrective action.
- Why this is / is not agent-owned: A second model, LLM evaluation, hook or persona is not sufficient without an independent complementary source and binding audit feedback loop.
- Evidence: [rust/crates/core/src/tools/subagent.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/subagent.rs); [rust/crates/core/src/agent_type.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/agent_type.rs); [rust/crates/core/src/hooks.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/hooks.rs); [rust/crates/core/src/tools/workflow.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/workflow.rs).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: This is unresolved rather than a strong absence because configured reviewer agents could be substantial in particular deployments..


## S4 — Outside-and-then intelligence

- State: —
- Function: No native prospective external intelligence and capability-renewal decision path established.
- Disturbance / variety regulated: Future ecosystem changes and shifts in user-project needs require anticipation and strategic adaptation beyond task notes.
- Decisive decision or feedback right: Skills/config/session context can change subsequent prompts but do not autonomously decide future operational capability renewal.
- Decision owner: No evidenced first-party S4 owner.
- Supporting / enforcement mechanisms: Project skill loading, session forks, model presets, context compaction, project instruction files.
- Closure path: Past context is saved and may be restored; no source-native external-future sensing, options appraisal, decision and capability change returned to operation.
- Why this is / is not agent-owned: Historic memory, skills and model selection are not strategic intelligence by persistence alone.
- Evidence: [rust/crates/core/src/skills.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/skills.rs); [rust/crates/core/src/context.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/context.rs); [rust/crates/core/src/session_store.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/session_store.rs); [rust/crates/core/src/config.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/config.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: Developer version upgrades and user-authored skill packs are adjacent, not autonomous organizational intelligence..

### Absence scope

- Surfaces inspected: Core skills/config/project instructions, sessions/forks, compaction and model routing.
- Plausible first-party paths checked: Skill loading, prompt reuse, provider changes, saved session branches and scheduled tasks.
- Why no material first-party path remains: No packaged model-owned prospective environmental scan/options/decision loop autonomously closes a capability renewal into current agent operations.


## S5 — Policy and identity

- State: —
- Function: No independent ultimate-policy/identity governance right with authoritative binding return at this coding-session recursion.
- Disturbance / variety regulated: Tool approvals, project trust and sandbox restrictions are operational authority decisions, not foundational purpose disputes.
- Decisive decision or feedback right: User selects trust/permission policy; deterministic code enforces without S5 constitutional deliberation.
- Decision owner: Human user and configured local rules for individual operations; no first-party S5 decision actor.
- Supporting / enforcement mechanisms: Central permission gate, OS sandbox, trusted project, tool approval and agent tool allowlists.
- Closure path: Permit/deny operational tools or choose a project trust scope; no highest-purpose identity/policy decision governs all future operating arrangements.
- Why this is / is not agent-owned: Static safety and human approval do not by themselves establish S5.
- Evidence: [rust/crates/core/src/permissions.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/permissions.rs); [rust/crates/cli/src/trust.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/cli/src/trust.rs); [rust/crates/core/src/agent_type.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/agent_type.rs); [rust/crates/core/src/tools/mod.rs](https://github.com/lizc2003/kloop/blob/5dbff2148f30a14737b8f661533b3c921470374e/rust/crates/core/src/tools/mod.rs).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: The human/developer governance of the public repository is outside the selected system-in-focus..

### Absence scope

- Surfaces inspected: Workspace trust, permission gate, sandbox, agent allowlist, plan/read-only mode and user config.
- Plausible first-party paths checked: Operator approvals, command policy, project trust, provider mode and manual resume/fork choice.
- Why no material first-party path remains: No shipped legitimate identity/ultimate-policy authority, constitutional issue/decision and binding organizational policy-return path is present in the inspected coding-session runtime.


## Distributed OSS parent arrangement

Public Kloop maintainers and source design references to other products are not part of the deployed coding-session decision hierarchy. External providers, MCP services and user skill packs supply capabilities or context only when actually integrated.

## Self-hosted and non-human modes

Different provider wires and a configured local/remote inference model use the same first-party Rust coding tool path. An explicitly isolated worktree child changes source safety but is optional; no positive S2 claim is made about default shared-cwd children.

## Recursion

Main and delegated agent sessions each have a distinct model/tool operating loop and local task variety. The actual coordination mechanism credited is isolated execution between those coding cells, not simply the existence of several agents or tool calls.

## Variety and escalation

Tool errors and test output return to the model; permissions may deny unsafe file/shell calls. Background child results arrive through inbox and can influence later main-agent tasks. Worktree creation fails closed, avoiding cross-worker overwrites. These are execution and coordination paths, not an automatic whole-current or ultimate-policy authority.

## Evidence gaps

- S2 C applies to explicit worktree-isolated run_agent child tasks only. Non-isolated default children do not gain conflict safety.
- S3 unresolved: scheduler/mailbox states and parent delegation do not conclusively show independently owned whole-current resource intervention.
- S3* unresolved: optional generic reviewer sidechain without compulsory complementary source access and corrective return cannot be promoted to A.
- No performance/benchmark claims imported from tests, taskground or README.
