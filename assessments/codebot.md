---
harness_id: codebot
project_name: Codebot
repository: https://github.com/voocel/codebot
review_ref: 098c5f3cf3e8708bd87138d666b08cd7888ec3b1
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Codebot

## Review boundary

- System in focus: Codebot's first-party terminal coding harness at frozen revision `098c5f3cf3e8708bd87138d666b08cd7888ec3b1`, including the product-owned session/runtime layer around `agentcore`, built-in coding tools, team/task/subagent composition, optional teammate worktree isolation, approval/permission modes, persistent sessions/context, goals/plans, Dream auto-memory consolidation, skills/plugins and supported TUI/print/ACP surfaces.
- Purpose and identity: perform repository-facing software-engineering work through a model/tool loop, optionally split work among long-lived teammates/subagents, regulate current team commitments and persist session/memory state across long-running terminal use.
- Relevant environment: user coding goals, repository/workspace state, shell/build/test/tool outcomes, teammate task state and messages, configured models/providers/MCP services, approval decisions, project/user agent definitions, git worktrees and persisted session/memory stores.
- Standard-distribution boundary: Codebot's repository-owned harness/runtime logic is inside. `agentcore` supplies the generic execution kernel/team primitives and remains a dependency; external models, MCP services and Git hosting cannot donate organizational functions not concretely instantiated by Codebot.
- Credited operating / distribution surfaces: ordinary TUI/print/ACP coding sessions; team/task tools; long-lived teammates and subagents; project/user agent definitions including supported `isolation: worktree`; persistent roster/transcripts/sessions; plan/goal modes; approval engine; Dream consolidation; skills/plugins.
- Adjacent first-party surfaces excluded from ownership: repository-development tests/benchmarks, baseline scripts, contributor/release governance and documentation/examples that are not wired into the frozen runtime.
- First-party operating / deployment modes considered: single-agent coding, foreground/background subagents, long-lived teammates with shared task state, optional per-teammate worktree isolation, plan/goal operation, persistent resume/fork/replay, Dream memory consolidation and supported permission modes.
- Recursion level: the Codebot session/team is the focal viable system. The lead and long-lived teammate coding loops count as distinct S1 units when they own separate bounded coding contributions. Task rows, mailboxes, worktrees and validators are mechanisms rather than independent viable systems.
- Reviewed revision: `098c5f3cf3e8708bd87138d666b08cd7888ec3b1`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Codebot explicitly separates the generic `agentcore` execution kernel from a first-party harness layer responsible for prompt/session policy, approval routing, context engineering, persistence, team/task coordination and TUI orchestration. Ordinary coding calls enter a model/tool loop; first-party runtime state then adds persistent tasks, goals, plan mode, compaction, memory and recovery.

A default team exists from session start. The lead model can create/update/list tasks, assign owners, spawn long-lived teammates through the subagent tool, send them messages, receive idle/result messages through the leader inbox pump and dismiss or hard-stop them. Teammates run independent model/tool loops with their own persisted transcripts and may auto-claim unblocked work.

Codebot also ships optional per-agent `isolation: worktree`. When selected, the teammate spawner creates a private git worktree and binds that teammate's tool execution to it so concurrent writers do not clobber one another. Isolation creation is serialized; inability to honor the declared mode fails loudly rather than silently falling back to the shared checkout. On teammate exit, uncommitted/committed surviving work is reported back to the leader.

Dream mode is a restricted background subagent that consolidates auto-memory after session activity: it reads project/session evidence and can only write/edit inside the memory directory. This changes later recalled context but remains retrospective memory consolidation rather than an external/prospective adaptation loop.

## Operational model

A user prompt enters the lead coding actor. The actor chooses tool actions, receives concrete results and revises its work. For larger jobs it can maintain a shared task graph and spawn long-lived teammates. Team messages and task state are injected back into the lead, allowing it to reassign, stop, redirect or add work while teammates continue their own S1 loops.

When an agent definition declares worktree isolation, the runtime places that teammate in a separate checkout before its S1 work begins. The resulting isolation prevents concurrent peer writes from clobbering the same workspace; cleanup reports surviving unmerged/uncommitted work to the lead for subsequent coordination.

## S1 — Operations

- State: A
- Function: autonomously perform coding and repository work through a model-driven tool feedback loop.
- Disturbance / variety regulated: unfamiliar codebases, changing file state, shell/build/test failures, tool/provider errors, context limits, long-running goals, user constraints and delegated subtask uncertainty.
- Decisive decision or feedback right: choose the next coding/investigation/tool action, revise work from concrete observations, delegate bounded work when useful and decide when an operational contribution is complete.
- Decision owner: the active Codebot lead or teammate model-backed coding actor.
- Supporting / enforcement mechanisms: `agentcore` loop instantiated by Codebot, first-party tools, session runtime, persistent context/compaction, plans/goals, skills, approval engine, task runtime and teammate/subagent launchers.
- Closure path: user/task context → model selects action/tool/delegation → workspace/tool result returns → result enters the same actor's subsequent context → later coding behavior changes until completion, stop or failure.
- Boundary reachability: normal TUI/print/ACP session bootstrap constructs the first-party harness around the execution kernel and directly exposes the credited coding path.
- Why this is / is not agent-owned: removing the model actor leaves tools, persistence and policy machinery but removes the open-ended decisions that transform repository evidence into subsequent coding actions.
- Evidence: README; `internal/agent/session_runtime.go`; `internal/bootstrap/assemble_session.go`; `internal/bootstrap/tools.go`; `internal/bootstrap/subagents.go`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic loop mechanics come from `agentcore`, but Codebot concretely instantiates and surrounds them with the reviewed harness behavior.

## S2 — Coordination

- State: C
- Function: provide a concrete coordination constructor that attenuates write interference among distinct teammate S1 units through per-teammate git-worktree isolation and controlled handoff of surviving work.
- Disturbance / variety regulated: concurrent coding teammates may otherwise edit the same files/checkouts and clobber peer changes; concurrent worktree creation itself can contend on the repository index lock.
- Decisive decision or feedback right: the runtime deterministically enforces the selected first-party isolation declaration; no autonomous metasystem actor chooses the collision policy at runtime.
- Decision owner: constructor/runtime policy configured through first-party agent definitions (`isolation: worktree`), enforced by the teammate spawner and worktree lifecycle.
- Supporting / enforcement mechanisms: `Isolation` agent-type map, serialized worktree creation, per-teammate cwd binding, fail-loud non-fallback behavior, cleanup preservation, branch/worktree retention and leader notifications.
- Closure path: distinct teammate S1s are spawned for concurrent work → an isolated agent type receives a private checkout → its subsequent writes occur outside peer workspaces → on exit, surviving changes/branch state are reported to the lead → later team decisions can integrate or inspect that work without silent clobbering.
- Boundary reachability: `isolation: worktree` is a supported project/user agent-definition field wired by `buildSubAgents` into the shipped teammate spawner; no custom runtime code is required.
- Why this is / is not agent-owned: removing the models does not remove the isolation/serialization policy once configured; the decisive anti-collision relation is therefore constructor-owned rather than autonomous.
- Evidence: `internal/agent/agent_definition.go`; `internal/agent/agent_loader.go`; `internal/bootstrap/subagents.go`; `internal/team/spawn.go`; worktree lifecycle.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: default teammates can still share the leader workspace; the positive state describes the shipped first-party isolation constructor mode, not every team configuration.

- Distinct S1 units: separate long-lived teammate model/tool coding loops with independent task ownership/transcripts.
- Inter-S1 disturbance: simultaneous peers writing the same checkout can overwrite or clobber each other's changes; concurrent sandbox creation can also contend on the same git index.
- Attenuating coordination relation: configured teammate types are placed in separate git worktrees, with creation serialized and silent fallback to the shared workspace forbidden.
- Feedback into subsequent S1 behaviour: the selected isolation changes every later filesystem/tool action by binding that teammate to its private cwd, while cleanup messages return surviving work/branch state to the leader for later integration decisions.
- Why S2-specific rather than generic communication/routing/sequencing/shared state/delegation: this path exists specifically to attenuate concrete write interference between distinct operational coding peers, not merely to pass messages or order tasks.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current team as a whole by observing shared task/member state and changing current assignments, dependencies and teammate lifecycle.
- Disturbance / variety regulated: multiple current tasks can be pending, blocked, in progress or reassigned; teammates can become idle, finish, crash, leave residual work or need to be redirected/stopped.
- Decisive decision or feedback right: the lead model can create tasks, inspect the whole task list, update status/dependencies/owners, assign work, message teammates, spawn additional teammates, gracefully dismiss them or hard-stop their task when necessary.
- Decision owner: the model-backed team lead.
- Supporting / enforcement mechanisms: shared `TaskStore`, `task_create/get/list/update`, assignment notifier, team registry/mailboxes, leader inbox pump, `send_message`, `team_create`, `team_dismiss`, teammate roster/transcript persistence and task/runtime stop paths.
- Closure path: current task/member/output state → lead model receives task snapshots and teammate messages → lead changes task ownership/dependencies/status or teammate lifecycle/messages → runtime enforces those changes → subsequent teammate state/results return through the same team surfaces.
- Boundary reachability: team/task tools are first-party runtime tools available in normal sessions; long-lived teammate spawns share the same registry/task surface and require no external orchestrator.
- Why this is / is not agent-owned: deterministic stores/mailboxes can preserve and route an existing plan but cannot decide what new tasks to create, who should own them, when to stop a peer or how to redirect current work when evidence changes.
- Evidence: `internal/tools/task.go`; `internal/tools/team_create.go`; `internal/tools/team_dismiss.go`; `internal/tools/send_message.go`; `internal/team/inbox.go`; `internal/team/protocol.go`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: task sorting/auto-claim/dependency checks are deterministic support; autonomous ownership rests on the lead model's whole-team tool rights and response to returned state.

- Whole-system current view: `task_list` summarizes all task statuses, owners and dependencies, while leader inbox/team registry expose current teammate outputs/availability.
- Current-control decision scope: create, assign, reassign, block/unblock through dependencies, update/stop tasks, message or dismiss teammates and spawn additional current capacity.

## S3* — Complementary audit

- State: —
- Function: no distinct complementary operational audit path is established.
- Disturbance / variety regulated: Codebot includes a bundled `review` skill, tests/tool results, worktree review wording, audit logs and optional read-only custom agents, but none is a separately wired first-party reviewer that independently challenges producer claims and closes findings back into current control.
- Decisive decision or feedback right: no distinct auditor owns an independent semantic acceptance/rejection judgment in the standard runtime.
- Decision owner: not established at S3* level.
- Supporting / enforcement mechanisms: bundled review skill, ordinary test/build commands, permission audit log, snapshots/diff/worktree inspection and generic subagent support.
- Closure path: these surfaces remain ordinary producer self-review, user-requested inspection, observability or generic composition capability; no standard complementary audit loop is closed.
- Why this is / is not agent-owned: the same coding actor can invoke review instructions or users may define reviewer agents, but uninstantiated generic reviewer capability is not a first-party S3* relation.
- Evidence: `internal/agent/skill/bundled/review.md`; skill tooling; worktree UI/lifecycle; permission audit surfaces; agent definition system.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a project can author a reviewer agent, but the assessment does not credit user-created compositions that are not a shipped Codebot audit path.

### Absence scope

- Surfaces inspected: bundled review skill, built-in subagent definitions, custom-agent loader, task completion hints, worktree cleanup/review wording, tests/build usage, approval audit logging, snapshots/diff and team messaging.
- Plausible first-party paths checked: bundled review skill as S3*; read-only `plan/explore` agents as reviewers; task completion verification hint as audit; worktree review flow as independent audit; permission audit log as S3*.
- Why no material first-party path remains: these mechanisms either use the producer actor, are generic read-only roles without a wired claim-checking relation, or provide evidence/observability without an independent audit judgment and corrective return path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented organizational adaptation loop is established.
- Disturbance / variety regulated: persistent memories, Dream consolidation, session history, skills/plugins, web access and provider/MCP configuration influence current or later work.
- Decisive decision or feedback right: no first-party path models future/external environmental change, develops adaptation options for Codebot's capability and closes a selected adaptation into later operation.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: Dream restricted memory-consolidation subagent, lexical memory recall, skill catalog/usage, plugins, session persistence, web search/fetch and provider/MCP settings.
- Closure path: Dream rewrites internal memory from prior session evidence and later recall injects that memory into prompts; this is retrospective memory maintenance, not a distinct outside-and-then adaptation conversation.
- Why this is / is not agent-owned: persistence, memory summarization and plugin/config extensibility are insufficient for S4 without an external/prospective distinction and adaptation-option loop.
- Evidence: `internal/dream/agent.go`; `internal/dream/lock.go`; `internal/dream/watcher.go`; session memory recall; skill/plugin surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: Dream is agent-owned memory consolidation, but the Methodology does not treat internal memory maintenance alone as S4.

### Absence scope

- Surfaces inspected: Dream triggers/lock/restricted agent, memory recall, persistent sessions, skills/plugins, provider/MCP configuration, web tools, goals/plans and runtime compaction.
- Plausible first-party paths checked: Dream as S4; memory recall as adaptation; plugin lifecycle as capability evolution; web search as external intelligence; provider switching as strategic adaptation.
- Why no material first-party path remains: inspected paths reuse internal history, perform current-task research or apply operator-selected configuration; none forms external/future sensing → adaptation-option generation → durable return into organizational capability.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy-level closure is established.
- Disturbance / variety regulated: permission modes, plan mode, dangerous-path prompts, workspace roots, stored approvals, plugin trust and user/project configuration constrain ordinary operation.
- Decisive decision or feedback right: no identity/ultimate-policy matter is routed to a legitimate ultimate authority and returned as a durable governing identity decision for the harness.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: approval engine, strict/balanced/accept-edits/trust modes, dangerous-path force-ask, plan approval, filesystem roots, plugin trust/enable state and settings.
- Closure path: users approve or configure ordinary tool/capability actions; these decisions constrain execution but do not close identity-level policy questions.
- Why this is / is not agent-owned: security and configuration mechanisms enforce selected limits rather than supplying S5.
- Evidence: README; `internal/approval/engine.go`; approval gate/rules; plugin/configuration surfaces.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: maintainers and operators retain real governance outside the run, but repository/deployment authority is adjacent absent a first-party identity-policy return loop.

### Absence scope

- Surfaces inspected: approval modes, plan exit approval, dangerous-path policy, stored approvals, workspace roots, plugin trust, model/provider/MCP settings, goals/plans and repository governance.
- Plausible first-party paths checked: permission modes as S5; plan approval as ultimate authority; plugin trust as identity governance; project/user configuration as constitution; maintainer governance as runtime S5.
- Why no material first-party path remains: these paths govern ordinary execution, access or configuration below identity/ultimate-policy level, while development governance is outside the operating harness boundary.

## Recursion

Long-lived teammates have independent model/tool loops, bounded task ownership and durable transcripts, so they can be treated as operational S1 units for team-level S2/S3 analysis. This does not imply that each teammate independently contains a complete S1–S5 viable-system stack.

## Variety and escalation

Each coding actor absorbs local variety through model/tool iteration, compaction, plans/goals, skills and memory. Team-level variety returns to the lead through task snapshots and teammate messages. Concrete write-conflict variety can be attenuated structurally by worktree-isolated teammate definitions. Approval/security violations escalate to the human user, while Dream processes stale/redundant internal memory in the background.

## Evidence gaps

No `?` state is required. The frozen repository exposes the team/task paths, optional worktree isolation, approval runtime, Dream mode and supported entry surfaces sufficiently to establish S1/S2/S3 and negative S3*/S4/S5 conclusions.

## Assessment summary

Codebot closes autonomous S1 through its model/tool coding loop, provides constructor S2 through first-party teammate worktree isolation against peer write clobbering, and closes autonomous S3 through lead-owned current team/task control. Its review surfaces do not establish an independent S3* path; Dream and persistent memory remain retrospective internal consolidation rather than S4; permissions/configuration do not close S5.

**Vector:** A · C · A · — · — · —
