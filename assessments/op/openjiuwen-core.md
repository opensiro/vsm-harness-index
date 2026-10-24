---
harness_id: openjiuwen-core
project_name: openJiuwen Core
repository: https://github.com/openJiuwen-ai/agent-core
review_ref: e23806c1073275780dced2b71ddd592ffb0a21fd
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: ?
---

# openJiuwen Core

## Review boundary

- System in focus: first-party openJiuwen Core Python SDK, including its directly callable ReAct, workflow, BaseTeam, and packaged optional TeamAgent leader/member modes reached through Runner. The assessment is not of the entire openJiuwen organization or JiuwenSwarm.
- Purpose and identity: configurable agent/tool/task runtime supporting individual and team execution, checkpointing, supervision, evaluation, and optional Skill evolution.
- Relevant environment: user demands and acceptance criteria, provider/model responses, external tool/file outcomes, simultaneous teammate task claims, review findings, and reusable Skill requirements.
- Standard-distribution boundary: first-party code at pinned Index #238 revision; supported SDK entry points and wired optional modes, excluding imagined application compositions.
- Credited operating / distribution surfaces: [README.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/README.md); [openjiuwen/core/single_agent/agents/react_agent.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/single_agent/agents/react_agent.py); [openjiuwen/core/runner/team_runner.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/runner/team_runner.py); [openjiuwen/core/multi_agent/team.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/multi_agent/team.py); [openjiuwen/core/multi_agent/teams/hierarchical_msgbus/supervisor_agent.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/multi_agent/teams/hierarchical_msgbus/supervisor_agent.py); [openjiuwen/agent_teams/agent/team_agent.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/team_agent.py); [openjiuwen/agent_teams/agent/coordination/kernel.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/coordination/kernel.py); [openjiuwen/agent_teams/agent/scheduling/scheduler.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/scheduling/scheduler.py); [openjiuwen/agent_teams/tools/task_manager.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/tools/task_manager.py); [openjiuwen/harness/rails/evolution/team_skill_evolution_rail.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/harness/rails/evolution/team_skill_evolution_rail.py).
- Adjacent first-party surfaces excluded from ownership: separate `openJiuwen-ai/jiuwenswarm` repository (Index #238 row 8), other openJiuwen repositories, contributor/dogfood/CI/test organizations, unmounted optimizer/trainers and research examples; provider internals and user-authored application controllers.
- First-party operating / deployment modes considered: ReActAgent; WorkflowAgent; HierarchicalTeam with LLM SupervisorAgent; TeamAgent autonomous and scheduled leader/member dispatch; optional task-verification reviewers; optional mounted team Skill evolution in auto-save or approval-required mode.
- Recursion level: one instantiated SDK Agent/Team application and its component workers, not project-wide openJiuwen governance.
- Reviewed revision: `e23806c1073275780dced2b71ddd592ffb0a21fd`.
- Observation date: 2026-10-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The SDK ships a model/tool ReAct loop and a separate developer-configured workflow graph, with Runner session, streaming and checkpoint services ([README.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/README.md); [openjiuwen/core/runner/runner.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/runner/runner.py)). The public Runner team route activates packaged TeamAgent objects with leader/member roles, rather than merely describing an example multi-agent topology ([openjiuwen/core/runner/team_runner.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/runner/team_runner.py)). The leader can construct and change a team task DAG, staff specialist workers, approve plans, arbitrate conflicts and send constraints through first-party tools ([openjiuwen/agent_teams/prompts/en/leader_policy.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/prompts/en/leader_policy.md); [openjiuwen/agent_teams/tools/AGENTS.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/tools/AGENTS.md)).

In the scheduled variant the leader's CoordinationKernel instantiates a deterministic TeamScheduler. Its reconciliations start pending work for idle members, settle review votes and route failure/rework/escalations. It manages task state, but is not credited as an agentic owner of model-decided task scope and priorities ([openjiuwen/agent_teams/agent/coordination/kernel.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/coordination/kernel.py); [openjiuwen/agent_teams/agent/scheduling/scheduler.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/scheduling/scheduler.py)).

Optional reviewer agents directly inspect work artifacts; their independently formed judgments are combined by host vote logic. Optional reviewer-feedback Skill evolution takes failure observations, builds reusable adaptation candidates, and either automatically admits them in explicit auto-save mode or returns a pending decision to the operator ([openjiuwen/agent_teams/prompts/en/reviewer_verifier.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/prompts/en/reviewer_verifier.md); [openjiuwen/agent_teams/agent/scheduling/review_feedback_evolution.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/scheduling/review_feedback_evolution.py); [openjiuwen/agent_evolving/experience/AGENTS.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_evolving/experience/AGENTS.md)).

## Operational model

An individually running ReActAgent is an operational unit producing task outcomes with model-selected actions. In TeamAgent mode, independently active teammates are separate S1 units. The team leader's shared view covers task, roster and member events; its decisions go back through task and communication tools. Deterministic task transitions, runtime wakeups, review vote tally and storage enforce or convey those decisions rather than independently deciding whole-system strategy. Higher-function claims apply only to their declared first-party optional modes.

## S1 — Operations

- State: A
- Function: outcome-producing iterative agent execution with model-chosen tool use and feedback.
- Disturbance / variety regulated: user intent variation, external responses, tool results, run errors and incomplete work.
- Decisive decision or feedback right: select next model/tool action and continue or finish.
- Decision owner: instantiated model-backed ReActAgent.
- Supporting / enforcement mechanisms: model adapter, context, sessions, tool executor, iteration limits, interruption/resume.
- Closure path: user task → model decision/tool act → observed result → next model turn or completion.
- Boundary reachability: first-party ReActAgent and Runner.run_agent are callable SDK implementations.
- Why this is / is not agent-owned: model owns context-sensitive operating choices; runtime merely invokes and bounds them.
- Evidence: [openjiuwen/core/single_agent/agents/react_agent.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/single_agent/agents/react_agent.py); [openjiuwen/core/runner/runner.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/runner/runner.py).
- Basis: structural
- Confidence: high
- Caveats: source inspection, no live provider-backed run performed.

## S2 — Coordination

- State: C
- Function: attenuate contention and competing ownership for operational tasks across teammates.
- Distinct S1 units: independently acting team members that claim/receive team task assignments.
- Inter-S1 disturbance: competing claims for the same pending task and overlapping pending work for an already-occupied member.
- Attenuating coordination relation: authoritative claim/start transitions, current active-task inspection, role-targeted task-update notification; scheduled mode starts only the earliest startable assigned task for each idle member.
- Feedback into subsequent S1 behaviour: rejected claims cannot be acted upon as owned work; accepted owner/start/cancel/reassignment updates reach member task board and wake/steer paths.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a concrete cross-member double-claim and busy-member contention is controlled by a shared admissibility gate and returned changed task ownership, beyond mere message forwarding.
- Disturbance / variety regulated: duplicate work, race conditions and inconsistent teammate commitments.
- Decisive decision or feedback right: admit or deny exclusive task ownership/start for a particular member/task.
- Decision owner: first-party deterministic task-state and scheduled-dispatch controller; function-specific construction/control path (`C`), not autonomous coordination discretion credited to an LLM.
- Supporting / enforcement mechanisms: task DB/CAS, event bus, mailbox and leader scheduler.
- Closure path: competing work intent → authoritative claim/start decision → returned board/event → altered teammate execution.
- Boundary reachability: TeamAgent team/task tools and leader scheduler are wired to the shipped runtime and reachable through Runner.
- Why this is / is not agent-owned: agents choose tasks/assignments, but the cited collision resolution is deterministic, and does not prove autonomous S2 ownership.
- Evidence: [openjiuwen/agent_teams/tools/task_manager.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/tools/task_manager.py); [openjiuwen/agent_teams/agent/scheduling/scheduler.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/scheduling/scheduler.py); [openjiuwen/agent_teams/agent/coordination/handlers/AGENTS.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/coordination/handlers/AGENTS.md).
- Basis: structural
- Confidence: medium
- Caveats: limited to specific task ownership/busy-member interference, not general conflict resolution between reasoning agents.

## S3 — Inside-and-now control

- State: A
- Function: supervise present team commitments, staffing, shared priorities and interventions across executing teammates.
- Disturbance / variety regulated: diverging progress, task dependencies, new constraints, stalled or unsuitable members, inconsistent deliveries.
- Decisive decision or feedback right: create/revise a task DAG, allocate specialists, change constraints, approve plans, reassign or escalate active work.
- Decision owner: model-backed TeamAgent leader in the packaged autonomous team configuration.
- Supporting / enforcement mechanisms: task/roster DB, leader tools, status reporting, schedulers and interrupts.
- Whole-system current view: task board, roster, worker reports/completions and exceptions for the current team.
- Current-control decision scope: bounded team task/resource allocations, commitments and criteria; not organization-wide policy.
- Closure path: leader chooses current team change → writes board/messages via tools → members receive amended commitment → results inform the leader's subsequent decisions.
- Boundary reachability: TeamAgent is activated by the published Runner team interface; the leader policy and tools are first-party runtime surfaces.
- Why this is / is not agent-owned: an LLM leader selects discretionary allocation and intervention; deterministic scheduled dispatch only executes preselected policy.
- Evidence: [openjiuwen/core/runner/team_runner.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/runner/team_runner.py); [openjiuwen/agent_teams/prompts/en/leader_policy.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/prompts/en/leader_policy.md); [openjiuwen/agent_teams/agent/team_agent.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/team_agent.py); [openjiuwen/agent_teams/tools/AGENTS.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/tools/AGENTS.md).
- Basis: structural
- Confidence: medium
- Caveats: optional team topology; bare ReAct/WorkflowAgent modes do not establish S3.

## S3* — Complementary audit

- State: A
- Function: independently challenge worker completion statements by inspecting actual deliverables and returning corrective judgments.
- Disturbance / variety regulated: inaccurate completion reports, faulty artifacts and overlooked acceptance criteria.
- Claim being audited: an operating teammate's statement that its deliverable satisfies the task.
- Ordinary reporting path: teammate's own completion/result and submitted-review status.
- Complementary access path: in scheduled mode, the runtime constructs a separately assigned one-shot reviewer with reviewer-scoped task identity and a copy of the configured base-agent tool set, plus `view_task` and `verify_task`. Its first-party verifier prompt directs it to locate deliverable paths and inspect files with `list_files`/`read_file` (and test code with `bash`) when those capabilities are available; a reviewer name or vote alone is not counted as independent inspection.
- Independence boundary: independent actor and primary artifact/tool observations at the bounded team level; distinct persona or LLM instance alone is not sufficient. Not an attestation of external institutional independence.
- Who acts on findings: first-party scheduled review settlement returns failure/rework to assignee or verification; stalled rounds escalate to the leader.
- Decisive decision or feedback right: assess the independently inspected artifacts and cast a reasoned pass/fail or scored judgment.
- Decision owner: configured model-backed reviewer; deterministic tally does not own the factual audit judgment.
- Supporting / enforcement mechanisms: reviewer prompts, file-reading/tests, verify_task tool, vote aggregation, task transition CAS.
- Closure path: submitted worker output → direct reviewer inspection → vote → settled rework/verified task → subsequent worker/leader operation.
- Boundary reachability: `TeamAgentSpec.dispatch_mode="scheduled"` activates `TeamScheduler`; with task reviewers configured, `_spawn_temp_reviewer` builds a fresh reviewer harness and runs it, `verify_task` attributes the vote to the reviewer, and failed rounds return to the assignee as rework. Artifact access is inherited from the supplied agent spec and remains a condition of the credited mode, not a default guarantee.
- Why this is / is not agent-owned: reviewer chooses the substantive judgment using its own observation, while settlement applies vote policy.
- Evidence: [openjiuwen/agent_teams/prompts/en/reviewer_verifier.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/prompts/en/reviewer_verifier.md); [openjiuwen/agent_teams/prompts/en/reviewer_inspector.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/prompts/en/reviewer_inspector.md); [openjiuwen/agent_teams/prompts/en/reviewer_challenger.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/prompts/en/reviewer_challenger.md); [openjiuwen/agent_teams/agent/scheduling/scheduler.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/scheduling/scheduler.py); [openjiuwen/agent_teams/agent/scheduling/verdict.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/scheduling/verdict.py).
- Basis: structural
- Confidence: medium
- Caveats: `enable_task_verification` defaults to false and the leader may assign zero reviewers; inherited filesystem/test abilities and readable shared artifacts must be present. Source code and prompts establish a supported conditional audit path, not attestation that a reviewer actually inspected a specific artifact in a model-backed run.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: optional reviewer-feedback-driven adaptation of reusable team Skill experience to later task environments.
- Disturbance / variety regulated: repeated failure modes and changing external user task/acceptance demands beyond the current task.
- External distinction: user acceptance criteria, review/evaluation feedback and observed delivered artifacts.
- Future / prospective distinction: aggregate failures across tasks into reusable experience available to subsequent team runs.
- Adaptation option generated: model-attributed evolution signals, optimized Skill experience records or reusable new Skill patterns.
- Path back into current capability / S3: settled review feedback → enabled mounted `TeamSkillEvolutionRail` → attribution/aggregation → accepted record in `EvolutionStore` → regenerated `SKILL.md` experience index/details. Subsequent operational use requires the same Skill library to be visible to a `SkillUseRail`/`TeamSkillUseRail` consumer and the relevant experience to be selected/read; persistence alone does not prove a later model used the record.
- Decisive decision or feedback right: form future capability update and approve its durable admission.
- Decision owner: model-based optimizer in explicit auto-save configuration; legitimate operator/parent makes the admission decision in approval-required mode.
- Supporting / enforcement mechanisms: optional coordinator, confidence/repetition checks, pending snapshots and persistent Skill store.
- Closure path: external review feedback → model adaptation proposal → explicit auto-save or returned parent approval decision → durable Skill record/projection → available input for later Skill-based work, subject to shared-library binding, visibility and actual retrieval. No end-to-end later-run reuse is claimed.
- Boundary reachability: the supported optional mode mounts `TeamSkillEvolutionRail`, explicitly calls `configure_review_feedback_evolution(...)`, and uses scheduled TeamAgent review feedback; the scheduler only finds Rails with `review_feedback_evolution_enabled`. The shipped Rail offers `auto_save=True` and the separate default `auto_save=False` approval mode. A future read path is supplied by first-party Skill-use Rails, but requires a matching library/visibility setup.
- Why this is / is not agent-owned: autonomous mode grants model-generated adaptation decisive write-through; in the parent mode the operator controls approval. A task planner or log alone would be insufficient.
- Evidence: [openjiuwen/agent_teams/agent/scheduling/review_feedback_evolution.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/scheduling/review_feedback_evolution.py); [openjiuwen/harness/rails/evolution/team_skill_evolution_rail.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/harness/rails/evolution/team_skill_evolution_rail.py); [openjiuwen/agent_evolving/experience/AGENTS.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_evolving/experience/AGENTS.md); [openjiuwen/agent_teams/agent/scheduling/scheduler.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/scheduling/scheduler.py); [openjiuwen/agent_teams/rails/team_skill_use_rail.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/rails/team_skill_use_rail.py); [openjiuwen/harness/rails/skills/skill_use_rail.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/harness/rails/skills/skill_use_rail.py).
- Basis: structural
- Confidence: medium
- Caveats: optional, explicitly configured and mounted; `auto_save` is not default. `DESCRIPTION` experience injection needs a bound `evolution_store`; `BODY` experience requires progressive Skill index/detail reading. The source establishes storage and consumption interfaces, not a witnessed update-and-reuse execution or continuous self-adaptation by every SDK application.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-based Skill updater in explicit auto-save mode | Attributed, aggregated reviewer failures or signals | Accepted experience persists in the Skill store and is projected for later eligible reads (not guaranteed later consumption) | [openjiuwen/agent_teams/agent/scheduling/review_feedback_evolution.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/scheduling/review_feedback_evolution.py); [openjiuwen/harness/rails/evolution/team_skill_evolution_rail.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/harness/rails/evolution/team_skill_evolution_rail.py) |
| Parent (`P`) | User/operator approves or rejects staged adaptation | Pending evolution approval request in default approval-required mode | approve_record persists accepted records; reject_record discards them | [openjiuwen/harness/rails/evolution/team_skill_evolution_rail.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/harness/rails/evolution/team_skill_evolution_rail.py); [openjiuwen/agent_evolving/experience/AGENTS.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_evolving/experience/AGENTS.md) |

## S5 — Policy and identity

- State: ?
- Function: ultimate team identity and purpose policy are not decisively mapped from inspected runtime paths.
- Disturbance / variety regulated: durable identity or ultimate-policy disputes rather than ordinary plan or tool approval.
- Decisive decision or feedback right: not established: a specific identity/policy issue must reach legitimate authority and return to govern execution.
- Decision owner: unresolved; application author can set initial configuration, but initial configuration alone is not function closure.
- Supporting / enforcement mechanisms: role/system prompts, agent specifications, guardrails, approval rails.
- Closure path: no verified identity-level proposal → legitimate policy adjudication → returned changed operational constraint in this declared mode.
- Why this is / is not agent-owned: no positive ultimate-policy decision or autonomous owner established by static constraints.
- Evidence: [openjiuwen/agent_teams/prompts/en/leader_policy.md](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/prompts/en/leader_policy.md); [openjiuwen/agent_teams/agent/team_agent.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/agent_teams/agent/team_agent.py); [openjiuwen/core/security/guardrail/guardrail.py](https://github.com/openJiuwen-ai/agent-core/blob/e23806c1073275780dced2b71ddd592ffb0a21fd/openjiuwen/core/security/guardrail/guardrail.py).
- Basis: unknown
- Confidence: low
- Caveats: uninspected human-agent/guardrail policy interfaces could hide a material shipped return path; use `?`, not unjustified `P` or `—`.

## Recursion

The member agents have their own model/tool loops but team-member nesting and hierarchical supervisor dispatch do not alone prove autonomous metasystem closure at a separately viable child recursion.

## Variety and escalation

ReAct absorbs task/tool variety; task-start/claim gates attenuate inter-member ownership contention; a model-led team owner can adapt current priorities using a shared board. Reviewer inspection supplies complementary operational evidence and the scheduler handles verified/rework states. The optional mounted Skill Rail permits prospective adaptation; unmounted optimizers are not S4 evidence. A task status, queue, enforcement gate, or routine escalation is not automatically an algedonic signal or S5 authority.

## Evidence gaps

1. No upstream runtime tests, live model/provider run, or direct reviewer artifact-inspection trace were performed. S3* is a conditional supported structural path: verify an actual reviewer's inherited file/test tools and distinct observations if stronger assurance is needed; no universal model-backed execution requirement is imposed by the assessment Methodology.
2. Source inspection finds `auto_save` and approval paths plus Skill-use consumers, but no end-to-end witness of the same mounted Skill library across persist → later selected/read experience. Reviewer-feedback evolution also requires explicit coordinator configuration (`configure_review_feedback_evolution`) and sufficiently attributed feedback. Verify those bindings for a concrete deployment before claiming observed later-run adaptation; do not equate durable projection with record consumption.
3. Inspect specific shipped human-agent/guardrail governance integrations before resolving S5 as absent or any positive state.
4. JiuwenSwarm and adjacent openJiuwen projects require separate frozen-ref assessment; no organizational functions are borrowed from them.
