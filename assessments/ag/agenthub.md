---
harness_id: agenthub
project_name: AgentHub
repository: https://github.com/hawkingrei/agenthub
review_ref: 7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentHub

## Review boundary

- System in focus: one supported AgentHub Team, including first-party installed coordinator/worker contracts, actor task/mailbox control and provider-backed execution.
- Purpose and identity: deliver engineering work through durable team ownership, local worker discretion and accountable coordinator integration.
- Relevant environment: human requests, project workspaces/source, peer agents, ACP provider runtimes, remote nodes and local persistence.
- Standard-distribution boundary: Rust backend/daemon, Team APIs/actor CLI, compiled default role prompts and managed role skills at the frozen source.
- Credited operating / distribution surfaces: packaged Team roles and their actual task/mailbox/API/ACP delivery paths, not the internal metasystem of external Codex.
- Adjacent first-party surfaces excluded from ownership: repository CI, test-only fixtures, optional developer prompt-review plugin, prospective offline-activation/complete Nowledge Mem design, and unrelated maintainer governance.
- First-party operating / deployment modes considered: existing local/remote-node Team execution, persistent/one-shot roles, canonical task/review lifecycle and operator controls. Pending agent-loop product direction is not assumed implemented.
- Recursion level: one Team with operational worker cells and its coordinator.
- Reviewed revision: `hawkingrei/agenthub@7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7`; immutable intake #2446 / serial controller #2447; historical #201 pin preserved.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/README.md); [Cargo.toml](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/Cargo.toml) distinguish existing runtime from pending offline activation/complete Mem integration. The Rust server, SQLite-backed task/mailbox history, ACP streams and remote node layer provide durable execution support. [crates/agenthub-team-prompts/src/lib.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/crates/agenthub-team-prompts/src/lib.rs); [crates/agenthub-managed-skills/src/lib.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/crates/agenthub-managed-skills/src/lib.rs); [crates/agenthub-acp/src/team_role_skills.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/crates/agenthub-acp/src/team_role_skills.rs); [src/api/teams.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/api/teams.rs) compile/materialize role contracts, install required role skills and select prompts in the supported Team composition. They do not merely expose a generic prompt editor.

[skills/team/team-worker-executor.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-worker-executor.SKILL.md); [skills/team/team-coordinator-orchestrator.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-coordinator-orchestrator.SKILL.md) allocate meaningful local execution and current team-governance discretion. [src/team/manager/task_catalog.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/manager/task_catalog.rs); [src/team/manager/task_updates.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/manager/task_updates.rs) persist ownership, priority, context and status. [src/team/manager/mailbox_threads.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/manager/mailbox_threads.rs); [src/team/manager/mailbox_errors.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/manager/mailbox_errors.rs) enforce a concrete topic-claim conflict and return actionable watch/release/expiry feedback. The coding CLI/provider executes these installed roles; its own reasoning machinery and internal organizational functions are not independently credited. Apache-2.0 applies to this repository.

## Operational model

The worker can investigate, implement, repair and retain evidence within an explicit assignment; coordinator controls canonical Team tasks, ownership, priority, blocking and acceptance. Actor mailbox, task APIs, runtime permission gates and persistence support those decisions. Topic ownership conflict is a concrete inter-worker disturbance with a shipped claim/watch response. A coordinator title alone is not the S3 evidence: current task/worker evidence plus priority/reassignment/status rights and returned operational changes establish the mapping.

## S1 — Operations

- State: A
- Function: Workers deliver assigned engineering outcomes with local initiative and repair.
- Disturbance / variety regulated: Implementation/test failures, new findings and scoped blockers.
- Decisive decision or feedback right: Select local investigation/actions/repair and report evidence rather than wait for coordinator micro-approval.
- Decision owner: Worker agent under the shipped worker execution role.
- Supporting / enforcement mechanisms: ACP provider bridge, role-skill installation, task records, workspace tools and evidence stores.
- Closure path: Task assignment/context reaches worker → agent acts → worker_status/artifact pointers reach coordinator → accepted review or concrete change request drives continued work.
- Boundary reachability: Team creation selects compiled worker prompt and role skill profile; ACP attaches mandatory managed skills before execution. External CLI is execution support, not an unexamined donor of the role’s rights.
- Why this is / is not agent-owned: Worker prompt explicitly gives initiative within its lane. Removing the agent leaves transport/task state without the same implementation decisions.
- Evidence: [skills/team/team-worker-executor.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-worker-executor.SKILL.md); [crates/agenthub-team-prompts/prompts/default_team_worker_prompt.txt](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/crates/agenthub-team-prompts/prompts/default_team_worker_prompt.txt); [crates/agenthub-acp/src/team_role_skills.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/crates/agenthub-acp/src/team_role_skills.rs); [src/api/teams.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/api/teams.rs)
- Basis: structural
- Confidence: high
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

## S2 — Coordination

- State: A
- Function: Prevent competing agents from simultaneously owning the same actionable mailbox topic and reconcile ownership/dependency conflicts.
- Disturbance / variety regulated: Multiple workers can claim one topic or conflicting assignments; claim rejection identifies the active owner.
- Decisive decision or feedback right: Agent chooses claim, watch/wait, release or peer/coordinator adjustment after concrete ownership feedback.
- Decision owner: Participating Team agents; coordinator resolves cross-worker ambiguity when needed.
- Supporting / enforcement mechanisms: SQLite topic claim/lease transaction, stable topic keys, mailbox error/status feedback and shipped mailbox discipline.
- Closure path: A live conflicting claim returns ThreadClaimConflict/owner; losing agent switches to watch/wait rather than executing as a second owner; release/expiry enables later accepted work.
- Boundary reachability: Both worker/coordinator ACP roles require the actor-mailbox skill. The shipped actor triage path invokes the same claim transaction and exposes its concrete conflict recovery; custom coordination code is not required.
- Why this is / is not agent-owned: SQL exclusion only enforces the selected claim. The mandatory agent mailbox contract supplies the behavior-changing triage response; a bare mailbox would not suffice.
- Evidence: [skills/team/team-actor-mailbox.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-actor-mailbox.SKILL.md); [src/team/manager/mailbox_threads.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/manager/mailbox_threads.rs); [src/team/manager/mailbox_errors.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/manager/mailbox_errors.rs); [crates/agenthub-acp/src/team_role_skills.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/crates/agenthub-acp/src/team_role_skills.rs)
- Basis: structural
- Confidence: medium
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.
- Distinct S1 units: separate worker agents with assigned outcomes and local implementation discretion in the same Team.
- Inter-S1 disturbance: competing active ownership of one topic/task-related thread, not merely two agents exchanging messages.
- Attenuating coordination relation: claim ownership plus agent watch/wait/release and explicit handoff.
- Feedback into subsequent S1 behaviour: conflict response names owner and instructs loser to watch/release/wait, withholding duplicate execution until ownership permits it.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: source implements and the installed skill handles an actual exclusive-ownership collision, beyond message delivery.

## S3 — Inside-and-now control

- State: A
- Function: Maintain cohesion of current Team work through explicit ownership, priority, accountability and intervention.
- Disturbance / variety regulated: Stale/duplicated tasks, blocked workers, ownership mismatch, competing priorities and unsupported completion claims.
- Decisive decision or feedback right: Choose/revise canonical assignee/priority and current task commitments, park blocked work, accept/reopen based on evidence.
- Decision owner: Coordinator agent in the installed Team mode.
- Supporting / enforcement mechanisms: Actor task create/list/update tools, task journals, execution context, mailbox evidence, role/permission gates and runtime views.
- Closure path: Coordinator reads current task/member evidence → prioritizes or reassigns/changes state with journal reason → persisted canonical task/actor message changes worker’s next lane → returned evidence is reconciled again.
- Boundary reachability: Compiled coordinator prompt and mandatory role skills explicitly route to task governance/lifecycle; supported actor/API tools persist chosen priorities and assignees. No adjacent contributor-management agent is borrowed.
- Why this is / is not agent-owned: This extends beyond decomposing one prompt: the role deliberately reconciles ongoing task truth, stale duplicates, ownership drift, waiting commitments and evidence freshness. Runtime SQL/permissions execute rather than choose these decisions.
- Evidence: [skills/team/team-coordinator-orchestrator.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-coordinator-orchestrator.SKILL.md); [skills/team/team-task-governance.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-task-governance.SKILL.md); [skills/team/team-task-lifecycle.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-task-lifecycle.SKILL.md); [src/team/manager/task_catalog.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/manager/task_catalog.rs); [src/team/manager/task_updates.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/manager/task_updates.rs); [src/api/teams.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/api/teams.rs)
- Basis: structural
- Confidence: medium
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.
- Whole-system current view: Team task set/Kanban, member identity cards and checkpoints, blockers, notes and mailbox evidence.
- Current-control decision scope: owner/priority/replanning, task commitment/acceptance and block/unblock intervention across the current Team.

## S3* — Complementary audit

- State: —
- Function: No additional materially independent complementary operational-audit path established.
- Disturbance / variety regulated: Misleading execution or management claims.
- Decisive decision or feedback right: A separately authoritative audit judgment and corrective control return.
- Decision owner: Coordinator reviews ordinary worker evidence; permission reviewer decides narrower execution permission.
- Supporting / enforcement mechanisms: ACP event history, task review, permissions and developer prompt-review plugin.
- Closure path: Task in_review returns requested changes to worker, but this is the normal delivery/acceptance path; no separate complementary organizational-audit mode is supplied.
- Why this is / is not agent-owned: Architect/reviewer naming and raw logs alone do not turn normal coordinator acceptance into S3*.
- Evidence: [skills/team/team-task-lifecycle.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-task-lifecycle.SKILL.md); [src/team/permission_review/dispatcher.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/permission_review/dispatcher.rs); [src/team/permission_review/selection.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/permission_review/selection.rs); [plugins/agenthub-prompt-engineering/skills/agenthub-team-prompt-review/SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/plugins/agenthub-prompt-engineering/skills/agenthub-team-prompt-review/SKILL.md)
- Basis: structural
- Confidence: medium
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Task lifecycle/role contracts, ACP permission-review routing, event views and optional prompt-review plugin scope.
- Plausible first-party paths checked: Coordinator code review, automated permission-review peer routing and repository prompt-review tooling.
- Why no material first-party path remains: The first is routine operational acceptance, the second reviews action permissions rather than an operational truth claim, and the developer plugin is adjacent; no additional audit-specific complementary access/return is wired into this Team.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective environmental adaptation loop established.
- Disturbance / variety regulated: Future capability/environment change beyond current task learning.
- Decisive decision or feedback right: Develop/admit prospective organizational capability options from external distinctions.
- Decision owner: Agents retain project lessons and may patch their own profile; user controls broader product evolution.
- Supporting / enforcement mechanisms: Workspace memory, profile_patch_proposal, timed follow-ups and runtime recovery spine.
- Closure path: Selected notes/profile changes inform later tasks, without an established external/future option-to-capability regulatory conversation.
- Why this is / is not agent-owned: Self-profile drift repair and durable lessons do not alone establish S4; planned Mem/activation design cannot supply current closure.
- Evidence: [docs/features/team-workspace-memory-contract.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/docs/features/team-workspace-memory-contract.md); [src/api/teams.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/api/teams.rs); [skills/team/team-worker-executor.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-worker-executor.SKILL.md); [README.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/README.md)
- Basis: structural
- Confidence: medium
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Workspace-memory contract, implemented profile patch API, role lessons/follow-ups and README implementation limits.
- Plausible first-party paths checked: Durable notes, self-profile patches, coordinator research/option comparison and proposed new activation/Mem architecture.
- Why no material first-party path remains: Research serves current delegated task planning; profiles preserve local role fit; no shipped prospective organizational sensing/options/adoption loop or qualifying parent adaptation return is established.

## S5 — Policy and identity

- State: —
- Function: No legitimate ultimate-policy/identity adjudication loop at Team recursion established.
- Disturbance / variety regulated: Purpose/ultimate-policy tension, beyond member identity metadata and execution risk.
- Decisive decision or feedback right: Return an authoritative ultimate-purpose/policy decision into subsequent Team operation.
- Decision owner: User configures Team; agents own only scoped self-profile proposals and operational commitments.
- Supporting / enforcement mechanisms: Agent cards, role skill restrictions, profile patches and permission approvals.
- Closure path: Description/prompt changes update local role metadata; ACP approvals permit scoped commands. Neither is an evidenced ultimate-policy decision.
- Why this is / is not agent-owned: The word identity in Agent Cards does not make role-metadata editing S5.
- Evidence: [src/api/teams.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/api/teams.rs); [skills/team/TEAM_AGENTS.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/TEAM_AGENTS.md); [skills/team/team-task-governance.SKILL.md](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/skills/team/team-task-governance.SKILL.md); [src/team/permission_review/dispatcher.rs](https://github.com/hawkingrei/agenthub/blob/7f1f0450ebb58b3cb77b75c9669b4ad1ab8309f7/src/team/permission_review/dispatcher.rs)
- Basis: structural
- Confidence: medium
- Caveats: Source-based boundary judgment; no live model or production effectiveness claim.

### Absence scope

- Surfaces inspected: Team profile-patch validation/application, role authority, human input/permission routing and Agent Cards.
- Plausible first-party paths checked: Durable team/run prompt patches, user scope correction, role policy and ACP approvals.
- Why no material first-party path remains: No identity-level dispute reaching legitimate ultimate authority and returning as governing system policy is supplied; ordinary current planning and least-privilege permission decisions retain their own function.

## Distributed OSS parent arrangement

User/operator input is supported, but no organization-wide OSS parent arrangement is inferred from maintainers or multiple private agent sessions. Generic Team steering does not establish an extra S3/S4/S5 parent mode.

## Self-hosted and non-human modes

Local self-hosted Team and optional remote execution are supported. Persistent and one-shot role contracts retain the same scoped rights. External Codex must be installed/configured; offline durable-activation and full Mem features remain pending at this ref.

## Recursion

Worker cells have outcome/environment and local discretion, but a complete recursively viable worker metasystem is not established merely by separate ACP sessions.

## Variety and escalation

Mailbox/topic claims attenuate conflicting ownership; coordinator prioritizes current commitments and workers absorb task-local variety. Waiting/in_review and permission escalation provide inspectable return paths without automatically becoming algedonic functions.

## Evidence gaps

No live ACP/Codex invocation, remote-node deployment or full Rust build/test run claimed. Rust toolchain was unavailable in the assessment environment. Source tests corroborate intended behavior but are not reported as executed. S2/S3 conclusions depend on installed role adherence and API wiring, not empirical model reliability.
