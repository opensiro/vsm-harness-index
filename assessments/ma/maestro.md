---
harness_id: maestro
project_name: Maestro
repository: https://github.com/RunMaestro/Maestro
review_ref: 32ecbc14fe832138e9a7af4f263d1026a8aa8a5b
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.4
profile_version: 0.2.2
assessment_procedure_version: 0.3.4
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Maestro

## Review boundary

- System in focus: Maestro's first-party agent/session orchestration, Auto Run/playbooks, Group Chat moderator, busy-agent coordination, worktrees, queues and resilience at the pinned revision.
- Purpose and identity: orchestrate multiple external coding-agent sessions/projects from one desktop/headless control surface, including unattended task execution and moderated multi-agent discussion.
- Relevant environment: user requests/specifications, local repositories/worktrees, supported coding-agent CLIs/providers, SSH hosts and project state.
- Standard-distribution boundary: Maestro application/runtime, Group Chat moderator contract, Auto Run/playbooks, worktree/session/queue management; Claude Code/Codex/OpenCode/etc. are execution hosts.
- First-party operating / deployment modes considered: interactive sessions, Auto Run, parallel agents, worktree sub-agents, Group Chat with AI moderator, local/remote participants and default “only work with agents that are free”.
- Recursion level: one Maestro Group Chat / coordinated fleet when evaluating S2; individual provider agent sessions are S1 units.
- Reviewed revision: `32ecbc14fe832138e9a7af4f263d1026a8aa8a5b`.
- Observation date: 2026-09-18.
- Generated Profile version: `0.2.2`.
- Generated Methodology version: `0.3.4`.
- Current Profile version: `0.2.2`.
- Current Methodology version: `0.3.4`.

## Repository architecture

Maestro is a pass-through orchestration application for multiple coding-agent providers. Individual agents have isolated contexts/workspaces; Auto Run feeds checklist tasks through fresh sessions; worktree sub-agents isolate parallel file changes. Group Chat runs an AI moderator that receives the user question first, decides how to proceed, @mentions relevant agents, performs multiple rounds and synthesizes results. By default, Group Chat holds requests to busy agents to avoid simultaneous processes editing the same files.

## Operational model

S1 units are model-driven coding-agent sessions doing project work. For Group Chat, a model-driven moderator owns delegation/follow-up/synthesis decisions. The default availability mechanism specifically prevents a documented collision: two processes editing the same files and leaving stale state. The runtime enforces the hold, while the moderator decides which agents and rounds to invoke.

## Primary evidence

- [`README.md`](https://github.com/RunMaestro/Maestro/blob/32ecbc14fe832138e9a7af4f263d1026a8aa8a5b/README.md) — fleet orchestration, Auto Run, worktrees, Group Chat, queues and resilience.
- [`docs/group-chat.md`](https://github.com/RunMaestro/Maestro/blob/32ecbc14fe832138e9a7af4f263d1026a8aa8a5b/docs/group-chat.md) — moderator ownership, multi-round routing and explicit busy-agent edit-collision behavior.
- [`src/main/group-chat/group-chat-moderator.ts`](https://github.com/RunMaestro/Maestro/blob/32ecbc14fe832138e9a7af4f263d1026a8aa8a5b/src/main/group-chat/group-chat-moderator.ts) — first-party moderator implementation.
- [`src/main/group-chat/group-chat-router.ts`](https://github.com/RunMaestro/Maestro/blob/32ecbc14fe832138e9a7af4f263d1026a8aa8a5b/src/main/group-chat/group-chat-router.ts) — first-party group routing/availability machinery.
- [`ARCHITECTURE.md`](https://github.com/RunMaestro/Maestro/blob/32ecbc14fe832138e9a7af4f263d1026a8aa8a5b/ARCHITECTURE.md) — application/module architecture including Group Chat and worktrees.

## S1 — Operations

- State: A
- Function: autonomously execute project/coding tasks inside individual provider-agent sessions controlled through Maestro.
- Disturbance / variety regulated: open-ended codebase state, implementation uncertainty, tool output, tests and task-specific context.
- Decisive decision or feedback right: choose substantive coding/research/tool actions needed to complete the assigned prompt/task.
- Decision owner: the model-driven supported coding agent running as a Maestro session.
- Supporting / enforcement mechanisms: session spawning/resume, project cwd, provider CLI integration, Auto Run task feeding, worktrees and message transport.
- Closure path: Maestro sends a task/prompt to an agent session; the agent performs work and returns output/state; Maestro records and can feed the next task/turn.
- Why this is / is not agent-owned: provider models own operational action choices; Maestro supplies the first-party harness that invokes and preserves their sessions.
- Evidence: README, Group Chat docs and provider/session architecture.
- Basis: explicit + structural
- Confidence: high
- Caveats: Maestro itself is a pass-through to provider agents; classification credits the organizational right exercised through its standard supported runtime.

## S2 — Coordination

- State: A
- Function: coordinate multiple agent sessions so work is routed to suitable agents while avoiding concurrent edit interference and stale shared-project state.
- Disturbance / variety regulated: two agent processes can edit the same files simultaneously, overwrite each other and continue from stale state; multi-agent questions can also require selective delegation/follow-up across project contexts.
- Decisive decision or feedback right: choose which agents to involve and whether more rounds are needed; standard availability policy holds a request when the selected agent is already busy.
- Decision owner: the model-driven Group Chat moderator owns agent/round selection; deterministic Maestro availability machinery enforces the selected coordination safely.
- Supporting / enforcement mechanisms: “Only work with agents that are free” default, busy-state detection/holding, per-agent process/workdir, @mention routing, isolated worktrees and group message queue.
- Closure path: moderator selects agents; Maestro delays any busy conflicting target until free while other agents proceed; returned responses go back to the moderator, which follows up or synthesizes before returning to the user.
- Why this is / is not agent-owned: the runtime's busy check is enforcement, not the organizational owner; the autonomous moderator decides participant selection and continuation, with the safety relation altering when chosen S1 work actually runs.
- Evidence: `docs/group-chat.md`, README and Group Chat source modules.
- Basis: explicit + structural
- Confidence: high
- Caveats: worktrees/queues alone would not establish S2; the positive mapping relies on the documented same-file concurrency disturbance plus moderator/availability feedback loop.
- Distinct S1 units: separate local or remote provider-agent processes, each in its own agent/project context.
- Inter-S1 disturbance: concurrent processes editing the same files can overwrite one another and leave both conversations acting on stale state.
- Attenuating coordination relation: the moderator routes work while the default availability policy holds requests to busy agents; separate worktrees can additionally isolate intentionally parallel writes.
- Feedback into subsequent S1 behaviour: busy/free state delays or releases the requested invocation, and member responses return to the moderator for follow-up/delegation/synthesis.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the cited first-party behavior exists specifically to attenuate a concrete interaction hazard among distinct active agent processes, not merely to pass messages.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established beyond task/session orchestration.
- Disturbance / variety regulated: provider errors, cost/usage, session state and playbook progress are monitored, but no separate whole-fleet current-control owner with organizational discretion is established.
- Decisive decision or feedback right: no material first-party owner was found that sees the whole system and reallocates current resources/commitments/priorities on behalf of the whole.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: usage dashboard, Auto Run tracking, resilience/failover, queues, session discovery and remote control.
- Closure path: no qualifying distinct S3 loop was found.
- Why this is / is not agent-owned: moderator routing is counted as S2; dashboards, retries and failover are observation/runtime recovery rather than a demonstrated agent-owned S3 decision right.
- Evidence: README, Group Chat docs and architecture.
- Basis: structural
- Confidence: high
- Caveats: the human operator can manage many sessions, but generic manual fleet control is not enough for a canonical parent S3 state without a function-specific closed parent mode.

### Absence scope

- Surfaces inspected: Group Chat, Auto Run/playbooks, worktrees, resilience/failover, queues, remote control, usage dashboard and session management.
- Plausible first-party paths checked: moderator, Auto Run scheduler, provider failover, cost dashboard and human remote controls.
- Why no material first-party path remains: no separate agent-owned whole-system current view plus discretionary authority over fleet resources/commitments/priorities and a returned control loop was established.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit loop is established by the standard distribution.
- Disturbance / variety regulated: code diffs, agent output filtering and moderator follow-up were inspected, but they do not constitute independent organizational audit.
- Decisive decision or feedback right: no distinct reviewer/auditor right with complementary evidence access and corrective return was found.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: diff viewer, logs/history, moderator synthesis/follow-up and provider-native tests/tools.
- Closure path: no first-party independent audit finding → correction/reassignment loop is established.
- Why this is / is not agent-owned: a moderator asking for more information or a human inspecting diffs is part of normal operation/review, not an evidenced independent S3* channel.
- Evidence: README, Group Chat docs and architecture.
- Basis: structural
- Confidence: medium-high
- Caveats: users can configure coding agents that perform reviews, but that external composition is not a standard independent audit role supplied by Maestro.

### Absence scope

- Surfaces inspected: Group Chat moderator, diff/history UI, Auto Run, worktree flows, output filtering, tests/docs and resilience.
- Plausible first-party paths checked: moderator follow-up, cross-agent discussion, diff inspection and possible review-agent use.
- Why no material first-party path remains: no standard first-party complementary evidence path with enforced reviewer independence and returned corrective authority was found.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate external/prospective adaptation loop is established for the Maestro fleet.
- Disturbance / variety regulated: changing provider availability and future project needs were inspected, but existing resilience is operational recovery.
- Decisive decision or feedback right: no material first-party owner was found that senses external/future distinctions, develops adaptation options and returns a selected option into present capability/S3.
- Decision owner: none established for qualifying S4.
- Supporting / enforcement mechanisms: provider resilience/failover, documentation graph, usage analytics and user-authored playbooks.
- Closure path: failover/retry restores current operation; it does not close an outside-and-then capability adaptation loop.
- Why this is / is not agent-owned: recovery from overload/quota and analytics are S1/support mechanisms unless connected to prospective option generation and capability change.
- Evidence: README features and architecture/docs.
- Basis: structural
- Confidence: high
- Caveats: agents can be asked to research future designs as user work, but that is S1 task execution unless organizational adaptation closure is separately established.

### Absence scope

- Surfaces inspected: resilience/failover, analytics, Auto Run/playbooks, document graph, Group Chat and provider/session configuration.
- Plausible first-party paths checked: backup endpoint failover, usage analysis, cross-project architecture discussion and agent research.
- Why no material first-party path remains: these paths recover or perform current user-requested work; no first-party external/future sensing → adaptation option → capability/S3 return loop is established.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy governance loop is established for the Maestro fleet.
- Disturbance / variety regulated: user specifications, playbooks and app settings constrain tasks but do not establish organizational identity authority.
- Decisive decision or feedback right: no material first-party ultimate-policy decision path with legitimate authority and return was found.
- Decision owner: none established for qualifying S5.
- Supporting / enforcement mechanisms: user prompts/specs, playbooks, moderator settings, agent/provider configuration and read-only mode.
- Closure path: configuration and prompts affect tasks directly; no identity-level authority closure is established.
- Why this is / is not agent-owned: a user being able to configure agents or choose a moderator is not sufficient for VSM S5.
- Evidence: README, Group Chat management docs and application configuration surfaces.
- Basis: structural
- Confidence: high
- Caveats: a larger development organization can supply S5 outside Maestro.

### Absence scope

- Surfaces inspected: Group Chat configuration, Auto Run/playbooks, agent settings, remote controls, prompts/specifications and application configuration.
- Plausible first-party paths checked: choosing moderator/provider, editing playbooks, read-only mode and project specifications.
- Why no material first-party path remains: no identity/ultimate-policy issue is routed to a legitimate ultimate authority and returned as an authoritative organizational policy that governs the fleet.

## Recursion

Maestro can coordinate agents across projects and machines, but the pinned evidence does not establish nested full viable organizations. The assessment therefore treats the coordinated fleet/Group Chat as one system in focus.

## Variety and escalation

Maestro attenuates concurrency variety through busy-agent holding and worktree isolation, while the moderator iterates until the group question is sufficiently answered. Provider failures trigger bounded retry/wait/failover behavior, which is operational resilience rather than S4.

## Evidence gaps

No separate S3/S3*/S4/S5 closure was established after checking the principal fleet-management and group-control surfaces. The S2 claim is strong because the documentation states the exact same-file collision and the default first-party attenuation mechanism.
