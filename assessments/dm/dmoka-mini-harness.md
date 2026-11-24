---
harness_id: dmoka-mini-harness
project_name: mini-harness
repository: https://github.com/dmoka/mini-harness
review_ref: 4563935c87c4e22514a6ee3842fc51fc34ebe2fb
reviewed_at: 2026-11-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# mini-harness

## Review boundary

- System in focus: local Python coding-agent runtime, including its child sessions/worktrees, memory maintenance and configured lifecycle hooks.
- Purpose and identity: transform user coding tasks into repository investigation, changes, command results and completion reports.
- Relevant environment: local repository/Git state, user requests and approvals, model responses, shell and configuration.
- Standard-distribution boundary: agent.py, claude_cli.py and documented direct CLI entrypoints; model service and external Claude CLI internals excluded.
- Credited operating / distribution surfaces: SDK and Claude-CLI backends, act/chat/plan modes, isolated subagent/worktree paths, memory consolidation and configured permissions/hooks.
- Adjacent first-party surfaces excluded from ownership: tutorial/article, illustrations, fake-model tests, repository-development and release governance.
- First-party operating / deployment modes considered: act and chat, plan then human approval, parallel context-only or worktree children, automatic/manual memory consolidation, optional hooks and permissions.
- Recursion level: local coding session with parent coding agent and concurrent operational children where selected, not project-maintainer organization.
- Reviewed revision: 4563935c87c4e22514a6ee3842fc51fc34ebe2fb.
- Observation date: 2026-11-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Session holds conversation, active tools, mode and rules. The runtime repeatedly sends model-selected tool calls through dispatch, returns results and stops on the model's completion. Both SDK and one-turn Claude CLI use the same first-party loop. Plan mode blocks write tools until approval. Context rules, memory and compaction maintain local knowledge. Worktree children execute separate tasks in distinct checkouts and return branch/report pairs. Permission matching and optional shell hooks gate operations. Fake-model tests corroborate paths, not separate shipped owners.

Evidence: [loop](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L71-L163), [memory](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L297-L429), [children and hooks](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L491-L609), [CLI](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L620-L648), [backend](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/claude_cli.py#L45-L83).

## Operational model

Main agent owns task-local investigation, editing and completion. Worktree children own their individual task execution, have their own checkout and return branch/report deliverables. Parent chooses isolated execution to avoid concurrent edits to one checkout. Plan and command approvals constrain local action, not automatically S3/S5. No live model call made in this assessment.

## S1 — Operations

- State: A
- Function: produce requested repository investigation and changes.
- Disturbance / variety regulated: uncertain repository content, tool errors and incomplete changes.
- Decisive decision or feedback right: select and revise tool actions, decide task completion.
- Decision owner: model-backed coding agent.
- Supporting / enforcement mechanisms: Session, tools, permissions, hooks, transport and shell.
- Closure path: results/errors and optional stop-hook rejection enter the next model turn; agent continues or reports completion.
- Boundary reachability: main creates Session and calls run_loop; both backends return model-selected actions to the same dispatcher.
- Why this is / is not agent-owned: removing the model leaves execution machinery but no discretionary action selection or completion.
- Evidence: [loop](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L85-L148), [file tools](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L210-L252), [shell](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L289-L294), [entrypoint](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L620-L648).
- Basis: explicit.
- Confidence: high.
- Caveats: plan mode and restricted commands can require human approval; Stop retries are bounded. No performance claim.

## S2 — Coordination

- State: A
- Function: attenuate concurrent coding-cell interference through selectable isolated writable checkouts and joined branch outcomes.
- Disturbance / variety regulated: concurrent editing children modifying overlapping files or Git working state.
- Decisive decision or feedback right: calling model chooses whether each child gets its own worktree and receives the resulting branch report for subsequent handling.
- Decision owner: parent coding agent, while children retain local task discretion.
- Supporting / enforcement mechanisms: run_subagent worktree parameter, parallel executor, unique Git branch/worktree creation, child process cwd and join.
- Closure path: chosen isolated checkout becomes the child's operational environment; separate writes avoid same-checkout overwrite; branch/report returns to the parent's next turn. The isolation loop itself does not require branch merge.
- Boundary reachability: run_subagent is a default core tool; model directly chooses worktree=true; concurrent calls launch separate children with selected checkouts.
- Why this is / is not agent-owned: the model chooses when to invoke isolation; runtime implements the choice rather than deciding which tasks need it.
- Distinct S1 units: concurrent task-specific coding children with own loop, checkout and branch/report deliverable.
- Inter-S1 disturbance: editing agents otherwise share a repository working copy and may interfere through concurrent writes.
- Attenuating coordination relation: selectable per-child unique Git worktree separates writes while work continues.
- Feedback into subsequent S1 behaviour: each child executes in its selected cwd; branch/report returns to next parent turn for further work without concurrent shared-file edits.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the choice explicitly changes concurrent editing cells' environment to isolate writes.
- Evidence: [fork/join](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L112-L122), [subagent and worktree](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L510-L545), [default tools](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L552-L553), [tests](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/tests/test_agent.py#L182-L205).
- Basis: structural.
- Confidence: medium.
- Caveats: isolation, not proven conflict-free merge or distributed locking. Git merge may require human permission; child commit failure is not fully checked. Context-only mode does not sandbox arbitrary shell commands.

## S3 — Inside-and-now control

- State: —
- Function: no supplied whole-system current-control loop at the local multi-cell boundary.
- Disturbance / variety regulated: potential competition for shared commitments/resources.
- Decisive decision or feedback right: not established beyond task-local actions and delegation.
- Decision owner: no evidenced S3 owner; human approves specific plans/commands, developer defines static permissions.
- Supporting / enforcement mechanisms: tool lists, plan gate, permissions, fork/join and scope.
- Closure path: no whole-system current-state intervention over resources/commitments.
- Why this is / is not agent-owned: parent receives completed reports and selects subtasks, not whole-system resource bargaining or intervention over active cells; plan approval is task-local.
- Evidence: [session and join](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L71-L122), [plan](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L491-L503), [worktrees](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L524-L545), [permissions](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L566-L609).
- Basis: structural.
- Confidence: medium.
- Caveats: ordinary task management and integration do exist.

### Absence scope

- Surfaces inspected: complete agent.py, Claude backend, CLI modes, README, plan/worktree/permission tests.
- Plausible first-party paths checked: parent delegation and joined reports, resource/permission configuration, plan approval and stop-hook intervention, memory maintenance.
- Why no material first-party path remains: no whole-system current view plus shared resource/commitment regulation, including parent mode or specific S3 constructor.

## S3* — Complementary audit

- State: —
- Function: no supplied complementary audit loop distinct from ordinary investigation/verification.
- Disturbance / variety regulated: potentially unreliable routine coding reports.
- Decisive decision or feedback right: no specific independent audit judgment path.
- Decision owner: no evidenced S3* owner.
- Supporting / enforcement mechanisms: generic fresh-context subagent, file tools, configurable hooks and ordinary tests.
- Closure path: subtask reports and configured hook failures return to ordinary task loop; no dedicated complementary challenge is wired.
- Why this is / is not agent-owned: generic subagent prompt supplies arbitrary investigation, not complementary audit relation; generic hooks require external audit composition.
- Evidence: [subagent](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L506-L521), [fresh-context test](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/tests/test_agent.py#L167-L179), [loop](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L95-L107), [hooks](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L594-L609), [stop test](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/tests/test_agent.py#L257-L265).
- Basis: structural.
- Confidence: medium.
- Caveats: caller could request audit, or configure external verifier; not a shipped function-specific loop.

### Absence scope

- Surfaces inspected: complete runtime, subagent/tool code, hook runner, README, backend, subagent and stop tests.
- Plausible first-party paths checked: separate-context file investigation, stop gates, shell tests, memory cleanup, external hook configuration.
- Why no material first-party path remains: no shipped audit-specific claim, independent access/judgment arrangement and return into control; generic extension alone does not establish S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective external adaptation loop.
- Disturbance / variety regulated: potential future changes in harness capability/environment.
- Decisive decision or feedback right: no future-facing harness adaptation right established.
- Decision owner: no evidenced S4 owner.
- Supporting / enforcement mechanisms: memory, compaction, planning, model fallback and shell/tools.
- Closure path: internal facts/summaries return into later prompts, not external prospective options into capability.
- Why this is / is not agent-owned: memory cleanup merges internal notes; fallback and coding the user's target do not establish harness adaptation.
- Evidence: [prompt](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L313-L326), [memory](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L356-L429), [compaction](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L435-L469), [plan](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L491-L503).
- Basis: structural.
- Confidence: high.
- Caveats: no inference about maintainer roadmap or hypothetical self-editing.

### Absence scope

- Surfaces inspected: complete runtime, both backends, README, memory/compaction/plan tests.
- Plausible first-party paths checked: memory capture/cleanup, summarization, planning, model fallback, shell access.
- Why no material first-party path remains: local operational knowledge and current tasks do not supply prospective external modeling, options and returned capability decisions, including parent mode.

## S5 — Policy and identity

- State: —
- Function: no runtime ultimate-policy or identity-resolution path.
- Disturbance / variety regulated: potential conflict over ultimate policy/identity.
- Decisive decision or feedback right: no evidenced identity-level decision path.
- Decision owner: static developer/user configuration and task-local human permission, not established S5.
- Supporting / enforcement mechanisms: BASE_PROMPT, AGENTS.md, settings.json, ask_human and plan gate.
- Closure path: rules enter prompts and approval changes command/mode, not an ultimate-policy issue returned into operations.
- Why this is / is not agent-owned: no concrete identity-level issue reaches an agent or legitimate parent through a shipped closure loop.
- Evidence: [base prompt](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L25-L36), [rules](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L297-L326), [human input](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L159-L163), [plan](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L491-L503), [settings](https://github.com/dmoka/mini-harness/blob/4563935c87c4e22514a6ee3842fc51fc34ebe2fb/agent.py#L566-L609).
- Basis: structural.
- Confidence: high.
- Caveats: configuration ownership exists, but no S5 loop; maintainer governance outside recursion.

### Absence scope

- Surfaces inspected: complete runtime, both backends, README, permission/plan/hook tests.
- Plausible first-party paths checked: instruction files, user plan/command approval, permissions, refusal/errors, external hooks.
- Why no material first-party path remains: none routes an ultimate-policy issue to authority and returns policy into operations, including parent mode.

## Recursion

Worktree coding cells have their own task, environment and local agency. No claim that a child contains all metasystemic functions.

## Variety and escalation

Tool results, exceptions, rules, compaction, isolation and retries absorb local variety. Human prompts preserve bounded rights. No distinct algedonic channel established.

## Evidence gaps

Static source assessment at pinned ref, not live SDK/Claude execution or independent audit. S2 limited to selectable same-checkout interference avoidance; merge conflicts, shell containment and commit failure recovery not established. No positive claim relies on adjacent development/test actors.
