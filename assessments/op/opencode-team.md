---
harness_id: opencode-team
project_name: OpenCode Team
repository: https://github.com/sametcelikbicak/opencode-team
review_ref: 02f9845682369d3435660bfee8b448168fd83268
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: P
---

# OpenCode Team

## Review boundary

- System in focus: One installed OpenCode Team project with model-driven orchestrator, specialist agent roles, configured stages, project-local run checkpoints and human-approved gates.
- Purpose and identity: Carry a product idea through structured research, requirements, coding, QA/security and launch stages with explicit human acceptance.
- Relevant environment: Project brief and existing files, external market or technology information, tool/provider results, code editing conflicts, testing failures and human stage decisions.
- Standard-distribution boundary: First-party installable role Markdown, team.yaml, slash commands, stage skills and project-local run_state helper, executed in an external OpenCode 2.x agent host.
- Credited operating / distribution surfaces: First-party Orchestrator and FE/BE/QA/security prompt actors installed into OpenCode; file-scope and task delegation rules; actual project state and stage approval helpers.
- Adjacent first-party surfaces excluded from ownership: Installer/validation/CI-only scripts, docs site, static diagrams, third-party OpenCode host as an independently owning system, model provider, unrelated user plugins and speculative external integrations.
- First-party operating / deployment modes considered: Installed default orchestrator, stage-specialist subagents, parallel FE/BE file partition, QA/security review, project-owner approvals, editable project pipeline and durable run state.
- Recursion level: One product project team assembled through the installed agent templates, not a company-wide autonomous organization.
- Reviewed revision: sametcelikbicak/opencode-team@02f9845682369d3435660bfee8b448168fd83268.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

This distribution is a first-party set of agent prompt/configuration artifacts and Python standard-library run checkpoint helper; there is no custom agent model-loop server. The installed external OpenCode host interprets first-party Orchestrator and specialist agents and dispatches subagents. The Orchestrator loads stage-specific skills, reads team.yaml and the full .team/ run state, allocates tasks, including parallel frontend/backend scopes, and requires separate completion reports before declaring a consolidated build. Each stage is gated on human approval tied to artifact content hashes. QA and security roles can independently inspect built project source before later stages. The owner can edit the pipeline declaratively, with symlink installation applying edits immediately. Evidence: [README.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/README.md), [agents/orchestrator.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/orchestrator.md), [team.yaml](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/team.yaml), [skills/team-memory/run_state.py](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/skills/team-memory/run_state.py), [docs/pipeline.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/docs/pipeline.md).

## Operational model

Individual role agents are substantive S1 units; the orchestrator resolves a concrete inter-agent code-scope interference problem during parallel FE/BE work. It has current whole-project status and autonomous within-stage dispatch/hold decisions, while recorded human approval controls stage advancement. QA/security are a constructible independent review route, not a proven running auditor in this static review. External market research and human-adopted pipeline changes influence future product direction, with project owner retaining ultimate policy.

## S1 — Operations

- State: A
- Function: Specialist agent execution for research, design, implementation, tests and project artifacts.
- Disturbance / variety regulated: Changing user task and source content, requirements and acceptance criteria.
- Decisive decision or feedback right: Specialists choose substantive content and code edits for assigned task, then return an artifact/report and later rework.
- Decision owner: First-party agent persona in the installed team, actually executed by OpenCode's agent tool/model runtime.
- Supporting / enforcement mechanisms: Role definitions, stage skills, prompt instructions, subagent tool, project artifact conventions and checkpoints.
- Closure path: Task prompt and skill → model specialist runs in tool-equipped OpenCode host → changed project code or .team/ artifact → orchestrator consumes outputs and status.
- Boundary reachability: Distinct first-party installable agent prompts with actions and task lifecycle; the OpenCode provider is an external execution dependency, not a borrowed autonomous organization.
- Why this is / is not agent-owned: Remove model-bound specialist, the orchestrator and helper cannot generate substantive task outputs.
- Evidence: [agents/orchestrator.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/orchestrator.md), [agents/fe.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/fe.md), [agents/be.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/be.md), [team.yaml](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/team.yaml), [README.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/README.md)
- Basis: structural
- Confidence: moderate
- Caveats: Source/contract evidence at pinned revision; no external OpenCode model session executed during review.


## S2 — Coordination

- State: A
- Function: Prevent FE and BE specialist code-scope interference during parallel build stage.
- Disturbance / variety regulated: Both S1 implementing agents may write shared source, contracts and generated types, overwriting or conflicting.
- Decisive decision or feedback right: Orchestrator chooses disjoint per-agent file ownership, assigns shared contracts and types to one owner, and dispatches explicit scoped tasks; waits for both reports before accepting build.
- Decision owner: First-party configured model Orchestrator in supported installed pipeline.
- Supporting / enforcement mechanisms: Parallel build team.yaml stage, orchestrator contract, subagent task prompts, separate FE/BE reports and build-consolidation gate.
- Closure path: Potential overlapping file edits → orchestrator divides work and sets single-owner shared contract → sends role-specific scope to FE/BE → independently produced reports → consolidates only after each succeeds.
- Boundary reachability: This is a shipped installed first-party role/command mode under a user-configured external OpenCode 2.x host.
- Why this is / is not agent-owned: Unlike generic sequencing, this explicitly attenuates shared-file ownership conflict between distinct live implementation S1 units.
- Evidence: [agents/orchestrator.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/orchestrator.md), [team.yaml](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/team.yaml), [docs/pipeline.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/docs/pipeline.md)
- Basis: structural
- Confidence: moderate
- Caveats: Source/contract evidence at pinned revision; no external OpenCode model session executed during review.
- Distinct S1 units: Frontend (fe) and backend (be) implementation subagents running concurrently.
- Inter-S1 disturbance: Both agents editing shared interfaces, generated types or the same project files.
- Attenuating coordination relation: Orchestrator allocates disjoint edit scopes and assigns a single owner for shared contracts/types.
- Feedback into subsequent S1 behaviour: Scope restrictions are sent in each subagent task prompt; reports must be returned and reconciled before consolidated completion.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It directly regulates a file-ownership conflict among two S1 writers, not just start order.


## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate current project-stage commitments, outstanding task attempts, blockers and legitimate continuation.
- Disturbance / variety regulated: Incomplete subagent work, changed artifacts invalidating approvals, cancellation, conflicting current stage progress and uncertainty after compaction.
- Decisive decision or feedback right: Orchestrator decides which specialist to dispatch/retry and when stage output is incomplete; human alone approves completed stage advancement. These are separate present-control modes.
- Decision owner: Configured model Orchestrator for actual task allocation/stop and readiness (base A); human owner at approval/checkpoint gates (parent P).
- Supporting / enforcement mechanisms: Project-wide .team/ output view, run_state.py status/start-task/finish-task/retry/approve, active stage configuration and explicit human gate.
- Closure path: Orchestrator reads run status and artifacts, allocates/checks attempts, records success/blocked work and requests approval; user approval records artifact hash, then subsequent stage can run; stale approval is rejected.
- Boundary reachability: This is a shipped installed first-party role/command mode under a user-configured external OpenCode 2.x host.
- Why this is / is not agent-owned: Agent makes whole-project current task/commitment dispositions within a stage, while the owner makes binding progression decisions; checkpoint and stage gate are enforcers, not owners.
- Evidence: [agents/orchestrator.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/orchestrator.md), [skills/team-memory/run_state.py](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/skills/team-memory/run_state.py), [commands/team-status.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/commands/team-status.md), [commands/team-approve.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/commands/team-approve.md)
- Basis: structural
- Confidence: moderate
- Caveats: Source/contract evidence at pinned revision; no external OpenCode model session executed during review.
- Whole-system current view: Orchestrator reads full project .team/ artifacts, active team.yaml stage, run attempts, stage approvals, warnings and pending next actions.
- Current-control decision scope: Dispatch allocation, incomplete-stage hold, task retry/reconciliation, user-approved stage progression and rework.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Configured model Orchestrator | Incomplete/current specialist tasks, stage readiness, restart uncertainty | Routes scoped work, marks attempts and retains incomplete state until accepted report | [agents/orchestrator.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/orchestrator.md) |
| Parent (`P`) | Human project owner | Stage output and pending approval, or stale artifact revision | Human-approved artifact hash recorded by run_state.py; orchestrator can proceed to the next configured stage | [skills/team-memory/run_state.py](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/skills/team-memory/run_state.py) |


## S3* — Complementary audit

- State: C
- Function: Independent QA/security inspection of implementer outputs with returned release/rework evidence.
- Disturbance / variety regulated: False completion, untested or vulnerable code emitted by FE/BE.
- Decisive decision or feedback right: Separately configured QA and security model roles can inspect project source rather than only trusting builders, produce finding/verification artifacts and cause owner to withhold gate until addressed.
- Decision owner: Constructed distinct QA/security reviewers, with project owner acting on evidence; review agent is not the builder.
- Supporting / enforcement mechanisms: Default team.yaml distinct QA/security stages, separate agent persona/tool access, test/security skill protocols and artifact approval gates.
- Closure path: FE/BE implementation → independent QA/security reads source and runs authorized checks → review artifacts → owner/orchestrator gates rework or continuation.
- Boundary reachability: This is a shipped installed first-party role/command mode under a user-configured external OpenCode 2.x host.
- Why this is / is not agent-owned: Separate role definitions and source access are shipped, but model provider actual isolation and audit execution is external OpenCode configuration; C, not automatically independent A.
- Evidence: [team.yaml](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/team.yaml), [agents/qa.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/qa.md), [agents/security.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/security.md), [skills/team-qa/SKILL.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/skills/team-qa/SKILL.md), [skills/team-security-review/SKILL.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/skills/team-security-review/SKILL.md)
- Basis: structural
- Confidence: moderate
- Caveats: Source/contract evidence at pinned revision; no external OpenCode model session executed during review.
- Claim being audited: Implementation agent asserts a build meets acceptance and security requirements.
- Ordinary reporting path: FE/BE build reports and orchestrator consolidated build artifact.
- Complementary access path: Distinct QA/security roles can read actual source and run tests or audit checks, producing own stage artifacts.
- Independence boundary: Separate configured role/model session and source inspection, not an author-generated summary alone.
- Who acts on findings: Orchestrator and human owner inspect review artifacts; owner may withhold stage approval or require rework.


## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt the future product delivery workflow and output based on newly researched external requirements.
- Disturbance / variety regulated: New market findings, updated requirements, changed technology or operator-requested new stages.
- Decisive decision or feedback right: User reviews research/PRD/design output and may adjust goals, role/stage ordering or stage parameters via team.yaml and project instructions.
- Decision owner: Legitimate human project owner; role analysts propose but do not autonomously adopt lasting operating goals or pipeline revision.
- Supporting / enforcement mechanisms: Market research/analyst agent, PRD stages, human approval gates, editable team.yaml, symlink installation where file changes take effect.
- Closure path: Research/new constraint → human evaluates proposal → revises project direction or stage configuration → saved change is loaded into later orchestrator stage dispatch → subsequent implementation changes.
- Boundary reachability: First-party prompt orchestrator and editable team.yaml are deployed via symlinks/copy into configured OpenCode; user must actually activate changes.
- Why this is / is not agent-owned: Human can change future working capability by editing first-party declarative team.yaml, which the shipped orchestrator explicitly reads before dispatch; not just a maintainer issue.
- Evidence: [agents/analyst.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/analyst.md), [skills/team-market-research/SKILL.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/skills/team-market-research/SKILL.md), [docs/customization.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/docs/customization.md), [agents/orchestrator.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/orchestrator.md), [README.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/README.md)
- Basis: structural
- Confidence: moderate
- Caveats: Source/contract evidence at pinned revision; no external OpenCode model session executed during review.
- External distinction: Market research, user-supplied new market/technical requirement or new product finding.
- Future / prospective distinction: Changes later project roadmap/agent pipeline behavior rather than correcting only the current failed task.
- Adaptation option generated: Analyst/architect output or owner-customized pipeline configuration and task goals.
- Path back into current capability / S3: Persistent team.yaml/project decisions feed orchestrator next stage selection and subsequent specialist tasks.


## S5 — Policy and identity

- State: P
- Function: Maintain binding project purpose, role permissions, stage sequence and approval authority.
- Disturbance / variety regulated: Unapproved changes to project identity, role boundaries, artifact policy and release scope.
- Decisive decision or feedback right: Human owner sets mission and per-stage authorizations, chooses agent roles/pipeline config, and can refuse any gate.
- Decision owner: Human project owner retains ultimate authority; Orchestrator is subordinate to team.yaml and required approval gates.
- Supporting / enforcement mechanisms: team.yaml, agent permissions, user commands, recorded stage approvals with artifact hashes and configured project memory.
- Closure path: Owner purpose/permissions → persisted team config and explicit approval → orchestrator reads and enforces stage policies on later agent calls.
- Boundary reachability: This is a shipped installed first-party role/command mode under a user-configured external OpenCode 2.x host.
- Why this is / is not agent-owned: No shipped actor may autonomously waive user approval or change binding mandate; default model agent cannot bypass human gate just because it is orchestrator.
- Evidence: [agents/orchestrator.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/agents/orchestrator.md), [team.yaml](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/team.yaml), [skills/team-memory/run_state.py](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/skills/team-memory/run_state.py), [README.md](https://github.com/sametcelikbicak/opencode-team/blob/02f9845682369d3435660bfee8b448168fd83268/README.md)
- Basis: structural
- Confidence: moderate
- Caveats: Source/contract evidence at pinned revision; no external OpenCode model session executed during review.
- Identity / ultimate-policy issue: What goal and stage/role/permission boundaries this product team serves and who may approve stage completion.
- Ultimate authority in each claimed mode: Legitimate human project owner; no autonomous policy-changing S5 mode is substantiated.
- Return-to-operation path: Saved team.yaml and artifact-linked approval records change what stages and roles the installed agent can run next.


## Distributed OSS parent arrangement

Many independent users install the same open source template, but each has separate project goals and approvals. Human parent modes are local to one installed product team. The upstream maintainers are not assumed to supervise runtime projects.

## Self-hosted and non-human modes

OpenCode Team contains installable role agents and operational instructions; they require external OpenCode 2.x and configured model runtime. S1, S2 and S3=A describe those first-party roles acting when properly installed and activated, not a zero-dependency native server. Human stage approvals remain mandatory; there is no evidenced standalone non-human ultimate policy mode.

## Recursion

One configured product-project delivery process with specialist agent work, file conflict coordination and orchestrator current-stage control. External host, model inference, third-party deploy tools and upstream community do not automatically own functions in this recursion.

## Variety and escalation

Specialist roles attenuate diverse tasks; file ownership rules resolve simultaneous edits; task attempt states prevent repeating work on compaction and invalidated artifact hashes fail approval; human gate blocks unapproved progression. These effects do not prove broader enterprise governance or guarantee exactly-once external side effects.

## Evidence gaps

Static pinned-source assessment, no external OpenCode process/model session operated. Source directly instructs disjoint file assignment, scoped FE/BE messages, task checkpoints and human approval, but actual policy compliance varies with host/model. A separate QA/security reviewer is constructible; no independently recorded external audit execution was verified. Parent adaptation is limited to an owner-controlled project pipeline, not a continuous autonomous environmental intelligence service.
