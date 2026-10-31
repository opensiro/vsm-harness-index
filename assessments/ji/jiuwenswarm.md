---
harness_id: jiuwenswarm
project_name: JiuwenSwarm
repository: https://github.com/openJiuwen-ai/jiuwenswarm
review_ref: 02b37f47fbefe80a58e4ed88606120818ca44ac3
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# JiuwenSwarm

## Review boundary

- System in focus: the packaged JiuwenSwarm agent/team service, including its explicitly configured openJiuwen runtime composition.
- Purpose and identity: deliver user work through single agents or a persistent Leader/Teammate organization with reusable capabilities.
- Relevant environment: user tasks/corrections, shared artifacts/code, models, tools, channels, skill library and optional distributed hosts.
- Standard-distribution boundary: pip/source installation, web/TUI/IM Agent and Cluster modes. The target pins openjiuwen to b6db2733bb9119f3b2e137969baca18d69b9f4c6 in pyproject.toml; the exact dependency commit was fetched from its public GitHub mirror, not replaced by current dependency main.
- Credited operating / distribution surfaces: TeamManager and declarative spec/providers, normal model-driven members, cooperative workspace coordination, Leader control, opt-in scheduled challenger review and enabled skill evolution.
- Adjacent first-party surfaces excluded from ownership: project-maintainer development/dogfood records, build/release CI, sample expert-group personas, benchmarks and meta-source-change PR acceptance. Auto Harness documentation is inspected, but generic product self-optimization terminology alone supplies no function.
- First-party operating / deployment modes considered: single-agent and local persistent team; autonomous and scheduled dispatch; task verification enabled/disabled; skill evolution enabled with auto_save true/false. Distributed transport and human team contributors are considered without inventing additional ownership.
- Recursion level: one operated JiuwenSwarm team and its capability library, not Huawei/openJiuwen project governance.
- Reviewed revision: `02b37f47fbefe80a58e4ed88606120818ca44ac3`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Python service owns request/session/configuration and builds a concrete model-driven agent/team composition using the version-pinned Agent Core. TeamManager enriches TeamAgentSpec with Swarm providers, binds session identity, mounts skills/permissions/evolution rails and calls the runtime. This is a shipped executable organization rather than an uncomposed generic SDK. Members independently execute work; the Leader regulates the team via task/message/member tools. Core code is cited only along paths actually wired by this target's spec.

The shared workspace has member-selected cooperative locks. Scheduled dispatch can create temporary verifier/inspector/challenger actors with raw filesystem tools and returned rework. Skill evolution separates reusable external-user correction from one-off noise, proposes capability changes and either saves automatically or waits for operator approval; saved experience affects subsequent skill calls. Tool permissions, prompt files, persona labels and ordinary UI stops are separated from organizational ownership. Target LICENSE is Apache-2.0.

## Operational model

The autonomous members own local task transformations; the Leader owns current team direction, member/commitment choices and exceptional intervention. Agent-selected coordination responses are distinct from deterministic lock/database enforcement. A temporary adversarial challenger is distinct from routine verifier QA. Skill adaptation has separate autonomous and operator-governed modes; this does not imply simultaneous final authority.

## S1 — Operations

- State: A
- Function: deliver delegated research/coding/content artifacts in the task environment.
- Disturbance / variety regulated: unknown source/material, tool failures and task-specific alternatives.
- Decisive decision or feedback right: members select methods/tools and revise work from observations.
- Decision owner: model-driven first-party-composed agents.
- Supporting / enforcement mechanisms: pinned DeepAgent/Runner, session/workspace state, tools, permission rails and transport.
- Closure path: task/request → member model actions → environment observations → revised actions and delivered artifacts.
- Boundary reachability: TeamManager.get_swarm_enriched_team_spec calls enrich_team_spec_for_swarm and produces runnable specs for supported Cluster mode; Agent mode is also documented. Dependency membership is established by [pyproject.toml](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/pyproject.toml).
- Why this is / is not agent-owned: removing the model actors leaves transport/enforcement without equivalent task discretion.
- Evidence: [jiuwenswarm/agents/harness/team/team_manager.py](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/agents/harness/team/team_manager.py); [jiuwenswarm/agents/harness/team/config_loader.py](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/agents/harness/team/config_loader.py); [docs/en/AgentTeam.md](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/docs/en/AgentTeam.md); [openjiuwen/agent_teams/prompts/en/teammate_policy.md](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/prompts/en/teammate_policy.md).
- Basis: structural
- Confidence: high
- Caveats: Optional modes are credited only when enabled; source evidence does not prove execution quality or empirical viability.

## S2 — Coordination

- State: A
- Function: attenuate shared-artifact write interference and resolve coordination deadlock among members.
- Disturbance / variety regulated: multiple members writing the same shared deliverable, with lock conflicts and possibly incompatible local choices.
- Decisive decision or feedback right: members acquire/release scopes and negotiate with peers; unresolved directional conflicts go to the Leader.
- Decision owner: member agents, with Leader arbitration for deadlock.
- Supporting / enforcement mechanisms: workspace_meta lock/owner metadata, separate workspaces, message delivery and task state.
- Closure path: before shared write → member requests exclusive lock → conflict names holder → peer negotiation/wait/revised action → unlock and resumed work.
- Boundary reachability: the target builds TeamAgentSpec and workspace tooling through pinned Core; the shipped teammate prompt explicitly requires workspace_meta locks for shared deliverables.
- Why this is / is not agent-owned: locks themselves are deterministic; members choose when/what to lock and how to respond to the other holder.
- Distinct S1 units: two or more independently executing teammates delivering different task outcomes.
- Inter-S1 disturbance: concurrent writes to the same shared artifact, explicitly identified in the teammate collaboration policy and tool's Locked by response.
- Attenuating coordination relation: cooperative exclusive-lock discipline plus lateral messages and deadlock escalation.
- Feedback into subsequent S1 behaviour: lock failure reveals the holder so the agent changes write timing/scope or negotiates; release permits subsequent writes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation targets a concrete shared-write collision rather than treating the mailbox or task DAG itself as coordination.
- Evidence: [openjiuwen/agent_teams/prompts/en/teammate_policy.md](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/prompts/en/teammate_policy.md); [openjiuwen/agent_teams/team_workspace/tools.py](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/team_workspace/tools.py); [docs/en/AgentTeam.md](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/docs/en/AgentTeam.md); [jiuwenswarm/agents/harness/team/team_manager.py](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/agents/harness/team/team_manager.py).
- Caveats: cooperative lock discipline is agent-owned and is not automatic write_file exclusion; no claim that all actual conflicts are prevented.
- Basis: structural
- Confidence: high

## S3 — Inside-and-now control

- State: A
- Function: regulate present whole-team commitments and intervene in stalled or repeatedly rejected work.
- Disturbance / variety regulated: capability mismatch, directional conflict, exhausted review rounds and stalled commitments threatening the team goal.
- Decisive decision or feedback right: reassign, change task constraints/review setup, stop a stalled member or replan current commitments.
- Decision owner: Leader model actor.
- Supporting / enforcement mechanisms: task/member tools, event-driven mailbox/scheduler, snapshot state, permission narrowing and runtime lifecycle controls.
- Closure path: team state/escalation plus assignee account → Leader judgment → update_task/reassign/reviewer/member change → new operational work.
- Boundary reachability: TeamManager constructs the supported team spec; pinned Core supplies Leader policy and scheduled escalation machinery selected by the target's dispatch_mode configuration.
- Why this is / is not agent-owned: the Leader selects the intervention; scheduler limits and shutdown execution enforce rather than originate that judgment.
- Whole-system current view: Leader sees team roster, task graph/status, member reports, directional conflicts and exhausted/stalled review escalations.
- Current-control decision scope: team-wide commitments, task ownership, member capabilities and constraints, not merely the initial task decomposition.
- Evidence: [openjiuwen/agent_teams/prompts/en/leader_policy.md](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/prompts/en/leader_policy.md); [openjiuwen/agent_teams/prompts/en/dispatch_scheduled_leader.md](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/prompts/en/dispatch_scheduled_leader.md); [openjiuwen/agent_teams/agent/scheduling/scheduler.py](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/agent/scheduling/scheduler.py); [jiuwenswarm/agents/harness/team/team_manager.py](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/agents/harness/team/team_manager.py); [jiuwenswarm/agents/harness/team/rails/team_permission_policy_rail.py](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/agents/harness/team/rails/team_permission_policy_rail.py).
- Caveats: generic user pause buttons and fixed token budgets are not credited as parent S3. No distinct parent control mode is claimed.
- Basis: structural
- Confidence: high

## S3* — Complementary audit

- State: A
- Function: adversarial complementary challenge beyond author claims and routine acceptance verification.
- Disturbance / variety regulated: blind spots, faulty assumptions, security risks and blocking failures missed by ordinary production reporting.
- Decisive decision or feedback right: temporary challenger independently inspects the deliverable and casts a blocking pass/fail judgment.
- Decision owner: separate challenger model actor; Leader acts on escalated failures.
- Supporting / enforcement mechanisms: fresh temporary harness, raw filesystem tools, reviewer-scoped verify_task identity, deterministic tally and rework routing.
- Closure path: author submits → separate challenger examines raw deliverable → fail returns feedback and in_progress rework; exhausted rounds escalate to Leader for changed control.
- Boundary reachability: target config_loader passes dispatch_mode and enable_task_verification into TeamAgentSpec. In supported scheduled mode with verification enabled the Leader can select challenger; Core scheduler builds and runs it with the team's filesystem tools.
- Why this is / is not agent-owned: the challenger owns adversarial judgment; vote parsing and state transitions are enforcement. Plain logs, routine verifier checks and the task-level AutoReviewer permission prompt are not the credited audit.
- Claim being audited: the submitted task deliverable is acceptable and free of blocking unconsidered defects.
- Ordinary reporting path: author completion report and routine verifier/acceptance checks.
- Complementary access path: a separate adversarial reviewer reads the deliverable with raw filesystem tools and tests threat scenarios beyond the acceptance rubric.
- Independence boundary: temporary reviewer has its own system prompt/context and reviewer-scoped task manager; the author cannot vote as this reviewer. Shared model infrastructure does not make it the author's self-check.
- Who acts on findings: author receives rework feedback; Leader receives stalled/exhausted review plus assignee summary.
- Evidence: [jiuwenswarm/agents/harness/team/config_loader.py](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/agents/harness/team/config_loader.py); [openjiuwen/agent_teams/agent/scheduling/scheduler.py](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/agent/scheduling/scheduler.py); [openjiuwen/agent_teams/prompts/en/reviewer_challenger.md](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/prompts/en/reviewer_challenger.md); [openjiuwen/agent_teams/prompts/en/dispatch_scheduled_leader.md](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/prompts/en/dispatch_scheduled_leader.md).
- Caveats: verification is disabled by default in the target loader; A describes an explicitly supported enabled mode, not every default run. Routine verifier-only configurations do not establish this S3* witness.
- Basis: structural
- Confidence: high

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: adapt reusable capability to externally supplied corrections and changing recurring task requirements.
- Disturbance / variety regulated: a reusable mismatch between a skill and user/environment requirements, beyond a transient task failure.
- Decisive decision or feedback right: decide which reusable update to retain and apply to future skill use.
- Decision owner: base mode: agent/evolution actor with enabled auto_save; parent mode: local operator approves specific proposed experience records.
- Supporting / enforcement mechanisms: trajectory evidence, evolution review/proposal schema, global skill experience store, approval interruption and future skill loading.
- Closure path: task/user correction → assess reusability → structured skill improvement → auto-save or operator approval → persisted experience loaded on later skill calls.
- Boundary reachability: Swarm evolution providers explicitly construct/register TeamSkillEvolutionRail and EvolutionInterruptRail. Enabled feature and auto_save settings select the complete alternative modes; no custom implementation is required.
- Why this is / is not agent-owned: agent-generated option selection plus automatic retention closes the base mode; when auto_save=false the operator owns the decisive retention judgment, hence separately evidenced parent mode.
- External distinction: user correction or recurring usage requirement that reveals a reusable gap in a skill, explicitly distinguished from personal preference and one-off environment errors.
- Future / prospective distinction: the actor judges applicability to later tasks of the same kind and develops reusable prechecks/fallback/verification guidance.
- Adaptation option generated: structured skill experience proposal naming target/section/reason/content, or a reusable team skill improvement.
- Path back into current capability / S3: approved/saved experience is kept in the shared active skill library and loaded on subsequent skill calls, changing the response repertoire available to the team.
- Evidence: [docs/en/SkillSelfEvolution.md](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/docs/en/SkillSelfEvolution.md); [jiuwenswarm/agents/swarm/providers/evolution_rails.py](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/agents/swarm/providers/evolution_rails.py); [openjiuwen/harness/rails/evolution/skill_evolution_rail.py](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/harness/rails/evolution/skill_evolution_rail.py); [openjiuwen/harness/rails/evolution/evolution_interrupt_rail.py](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/harness/rails/evolution/evolution_interrupt_rail.py).
- Caveats: skill_evolution defaults false; only enabled supported modes are credited. Generic memory or internal retry learning alone is not S4. This is structural capability adaptation, not measured improvement.
- Basis: structural
- Confidence: high

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Agent/evolution actor with auto_save=true | Reusable user/environment correction after task evidence | Validated proposed experience automatically retained and loaded on later skill calls | Swarm evolution providers; Core SkillEvolutionRail; SkillSelfEvolution guide |
| Parent (`P`) | Local harness operator with auto_save=false | Same reusable adaptation proposal presented for approval | Operator selects/approves records; approve_record writes accepted records; later skill execution loads them | EvolutionInterruptRail; SkillEvolutionRail.approve_record; target approval interface |

## S5 — Policy and identity

- State: —
- Function: no closed identity/ultimate-policy adjudication path established.
- Disturbance / variety regulated: persona, tool permissions and member authority limits are configured constraints rather than demonstrated ultimate-policy disputes.
- Decisive decision or feedback right: persona editing, tool approval and skill adaptation are not by themselves identity-level adjudication.
- Decision owner: operators/developers configure boundaries; Leader owns bounded current operations, not demonstrated ultimate authority.
- Supporting / enforcement mechanisms: IDENTITY/SOUL templates, AvatarPromptRail, permission narrowing and approval rails.
- Closure path: ordinary configuration/approvals return to execution, but no identity/ultimate-policy matter-to-authority-to-return loop is reconstructed.
- Why this is / is not agent-owned: a prompt called identity and a human approval mechanism do not establish S5.
- Evidence: [jiuwenswarm/resources/agent/workspace/IDENTITY_EN.md](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/resources/agent/workspace/IDENTITY_EN.md); [jiuwenswarm/resources/agent/workspace/SOUL_EN.md](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/resources/agent/workspace/SOUL_EN.md); [jiuwenswarm/agents/harness/common/rails/avatar_rail.py](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/agents/harness/common/rails/avatar_rail.py); [jiuwenswarm/agents/harness/team/rails/team_permission_policy_rail.py](https://github.com/openJiuwen-ai/jiuwenswarm/blob/02b37f47fbefe80a58e4ed88606120818ca44ac3/jiuwenswarm/agents/harness/team/rails/team_permission_policy_rail.py); [openjiuwen/agent_teams/prompts/en/leader_policy.md](https://github.com/openJiuwen-ai/agent-core/blob/b6db2733bb9119f3b2e137969baca18d69b9f4c6/openjiuwen/agent_teams/prompts/en/leader_policy.md).
- Caveats: bounded absence at the operated-harness recursion; contributor governance and a user's broader institutional authority are outside.
- Basis: structural
- Confidence: high

### Absence scope

- Surfaces inspected: persona templates, avatar identity injection/commitment guard, team policy/narrowing, Leader decision policy, skill approval and configuration.
- Plausible first-party paths checked: first-conversation identity fields, evolvable SOUL text, avatar principal authorization, human team/task approval and skill mutation approval.
- Why no material first-party path remains: the supplied paths personalize behavior or authorize bounded actions/capability changes; none exposes an identity/ultimate-policy issue adjudication with legitimate authority and returned policy closure. Generic file editing cannot fill that missing organizational path.

## Distributed OSS parent arrangement

The upstream contributors and development/dogfood organization are not the operated team. The S4 parent is the local operator of the skill library; no project-wide parent modifier is inferred from multiple contributors.

## Self-hosted and non-human modes

Both autonomous and operator-approved skill retention are shipped options. Team permission approvals and human participants do not automatically add parent S3 or S5. Without enabled evolution/verification those optional positive witnesses do not run.

## Recursion

Leader/Teammate hierarchy and subagent spawning establish decomposition and bounded operational discretion, not complete recursive viability of each member.

## Variety and escalation

Peers manage shared-write interference; directional deadlock and repeated review failures reach the Leader. Deterministic limits, transport recovery and session pause/stop support these paths without owning the associated judgments.

## Evidence gaps

No live-model execution, measured reliability, adaptation benefit or universal viability claim. Source dependencies were examined at the exact target-pinned Core b6db2733bb9119f3b2e137969baca18d69b9f4c6; newer dependency features are excluded. Findings distinguish shipped optional modes, ordinary QA and development-only surfaces.
