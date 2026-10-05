---
harness_id: autohand-code-cli
project_name: Autohand Code CLI
repository: https://github.com/autohandai/code-cli
review_ref: feaa8df7dcc5ee0152bc0d961bc271759fced45a
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# Autohand Code CLI

## Review boundary

- System in focus: Autohand Code CLI's first-party public coding-agent runtime at frozen revision `feaa8df7dcc5ee0152bc0d961bc271759fced45a`, including the primary model/tool runtime, first-party SubAgents and built-in agents, team/task orchestration, peer/resource coordination, permissions/modes, sessions/context, skills/learn/auto-skill machinery and supported CLI/headless/RPC/ACP surfaces.
- Purpose and identity: perform repository-facing software-engineering work, including autonomous implementation, delegated specialist work, coordinated multi-agent execution, review and persistent adaptation of project-specific capabilities.
- Relevant environment: selected repository/worktree, user objective, model/provider responses, shell/Git/test evidence, teammates and task/resource state, project dependencies/frameworks/CI, community skill registry and operator governance choices.
- Standard-distribution boundary: first-party CLI/runtime code, embedded built-in agents/skills, team/task manager, peer/resource coordination, permission/mode system and skill-learning surfaces are inside. External model providers, MCP servers, community skills before installation and external-agent definitions remain dependencies/environment. Separately built trace/computer-use companions are outside except for concrete integration behavior exposed by the public CLI boundary.
- Credited operating / distribution surfaces: `README.md`; `docs/teams.md`; `docs/feature_meta_tools.md`; `src/core/agent.ts`; `src/core/agents/SubAgent.ts`; `src/core/toolManager.ts`; `src/core/toolFilter.ts`; `src/core/teams/TaskManager.ts`; `src/core/teams/TeamManager.ts`; `src/core/peerTools.ts`; `src/generated/builtinAssets.ts`; `src/index.ts`; `src/commands/learn.ts`; `src/skills/autoSkill.ts`.
- Adjacent first-party surfaces excluded from ownership: development CI/tests/governance, design plans not wired into the frozen runtime, later default-branch behavior and behavior owned by external agents/providers. Current-default-branch search was used only for path discovery; credited evidence was re-read at the frozen ref.
- First-party operating / deployment modes considered: normal interactive editing; AUTO/autonomous execution; documented PLAN/YOLO modes; direct/parallel delegation; team creation/teammates/task control; peer/resource coordination; built-in reviewer delegation; `--auto-skill`; interactive `/learn`; `--learn`; `--learn-update`; RPC/ACP/headless surfaces sharing the runtime.
- Recursion level: one Autohand coding organization. Teammate processes and delegated `SubAgent` instances are distinct lower-level S1 units because each owns a bounded model/tool execution loop; they are not automatically classified as complete viable recursions.
- Reviewed revision: `feaa8df7dcc5ee0152bc0d961bc271759fced45a`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Autohand owns its coding model/tool loop and can create delegated `SubAgent` instances with separate conversations, provider/model execution and filtered tool sets. Built-in agents are embedded into the release rather than borrowed from user configuration.

The frozen distribution also contains a persistent team organization. The interactive session becomes the lead; teammate processes run their own LLM loops; the lead owns a shared `TaskManager`, task dependency graph and current team state. Teammates report task status/output through `TeamManager`, while lead tools can create/update/stop tasks, add teammates, inspect team/task state, message workers and shut down the team. Tasks can declare blocking dependencies and idle workers receive only available work.

S2 additionally has a first-party capacity-one `coordinate_resource` protocol with request/grant/release/cancel/controller semantics. For audit, the distribution embeds an independent read-only `reviewer` agent that executes through the separate `SubAgent` loop and returns findings to the lead.

For adaptation, `--auto-skill` analyzes the project, asks a model to generate a tailored skill and persists the resulting `SKILL.md` for later operation. `/learn`/`--learn` combine project analysis, installed skills and an external/community skill registry to audit capability, recommend options and generate/install new skills. `/learn update` re-analyzes project change and regenerates stale LLM-generated skills using project-hash provenance.

Primary evidence:

- [`README.md`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/README.md)
- [`docs/teams.md`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/docs/teams.md)
- [`docs/feature_meta_tools.md`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/docs/feature_meta_tools.md)
- [`src/core/agents/SubAgent.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/agents/SubAgent.ts)
- [`src/core/toolManager.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/toolManager.ts)
- [`src/core/teams/TaskManager.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/teams/TaskManager.ts)
- [`src/core/teams/TeamManager.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/teams/TeamManager.ts)
- [`src/core/peerTools.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/peerTools.ts)
- [`src/generated/builtinAssets.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/generated/builtinAssets.ts)
- [`src/index.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/index.ts)
- [`src/commands/learn.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/commands/learn.ts)
- [`src/skills/autoSkill.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/skills/autoSkill.ts)

## Operational model

A primary Autohand actor can work alone, delegate bounded specialist tasks, or instantiate a longer-lived team. In team mode, the lead has model-facing tools for constructing the team and changing its present commitment structure while teammate processes continue independently. Current state returns through team/task state and teammate updates.

Coordination and current control are distinct. S2 regulates interaction among S1s through dependency-aware availability, exclusive task ownership and explicit resource reservation. S3 uses whole team/task state to decide current population, commitments, dependencies, assignments, interventions and shutdowns. Complementary review is separate again: the embedded reviewer directly inspects artifacts and hands findings back to lead control. S4 turns project/external capability distinctions into persistent skill capability used by later operation.

## S1 — Operations

- State: A
- Function: perform repository-facing engineering transformations by interpreting the objective, selecting permitted tools/actions, observing results and iterating toward the requested outcome.
- Disturbance / variety regulated: changing code/worktree state, implementation alternatives, provider uncertainty, tool/build/test failures, repository instructions and evidence discovered during execution.
- Decisive decision or feedback right: choose the next task-specific repository/tool action and revise it from returned evidence.
- Decision owner: the model-backed Autohand lead or delegated teammate/SubAgent within its bounded task.
- Supporting / enforcement mechanisms: tool manager/action executor, permissions, conversation/session state, provider adapters, skills, hooks, context controls and run budgets.
- Closure path: objective/evidence → model selects action → first-party executor runs it → result returns into conversation → same actor selects another action or completes.
- Boundary reachability: first-party lead and delegated SubAgent loops are shipped across supported CLI/headless/protocol modes.
- Why this is / is not agent-owned: removing the model actor leaves tools, permissions and persistence but removes open-ended task-specific coding discretion.
- Evidence: `README.md`; `src/core/agent.ts`; `src/core/agents/SubAgent.ts`; `src/core/toolManager.ts` at the frozen revision.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: high-risk actions can be operator-governed in some interactive permission modes, but first-party autonomous operation is also supported.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among concurrently operating teammate/peer S1 units through dependency-aware work admission, exclusive task ownership and explicit capacity-one resource coordination.
- Disturbance / variety regulated: duplicate ownership of current work, execution before prerequisites complete, and simultaneous use of a shared exclusive resource by multiple active agents.
- Distinct S1 units: teammate child processes and delegated SubAgent executions each run independent model/tool loops against the shared organization/workspace.
- Inter-S1 disturbance: active units can otherwise claim the same work, consume one exclusive resource simultaneously, or begin a dependent task before another S1 has produced prerequisite state.
- Attenuating coordination relation: `TaskManager` exposes one owner/status per task, `blockedBy` dependencies and availability only after dependencies complete; `TeamManager` assigns available tasks to idle teammates. `coordinate_resource` adds capacity-one request/grant/release/cancel/controller semantics for contested resources.
- Feedback into subsequent S1 behaviour: task completion/status unblocks later tasks and triggers assignment; blocked work is withheld; resource grant/release changes whether another peer may proceed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive witness is concrete duplicate/dependency/resource contention among live S1s and a first-party relation that changes which S1 may act next.
- Decisive decision or feedback right: the autonomous lead decides task decomposition/dependency/assignment interventions through team tools while task/resource protocols return contention and availability feedback.
- Decision owner: model-backed team lead for task-specific coordination discretion; first-party managers enforce selected dependency/ownership/resource state.
- Supporting / enforcement mechanisms: `TaskManager`, `TeamManager`, peer messaging, `coordinate_resource`, team tools and assignment/recovery machinery.
- Closure path: lead/peers establish work/resource relation → coordination state accepts/blocks/assigns/grants → workers receive permitted work/resource access → completion/release/status changes coordination state → subsequent S1 behavior changes.
- Boundary reachability: teams, task tools and peer/resource tools are standard first-party runtime surfaces at the frozen ref.
- Why this is / is not agent-owned: deterministic state does not choose task-specific decomposition, dependencies or interventions if the lead actor is removed.
- Evidence: `docs/teams.md`; `src/core/teams/TaskManager.ts`; `src/core/teams/TeamManager.ts`; `src/core/peerTools.ts`; `src/core/toolManager.ts`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the positive state is bounded to explicit task/dependency/resource-contention regulation, not a claim that every filesystem collision is prevented.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current organization-wide team population, work commitments, dependencies, assignments and interventions while teammate S1s continue independently.
- Disturbance / variety regulated: changing team capacity, idle/working/crashed members, blocked/current/completed work, failed or obsolete commitments, dependency changes and cross-unit current priorities.
- Whole-system current view: the lead owns active `TeamManager`/`TaskManager` state; `team_status`, `task_list`, `task_get`, `task_output` and team view expose the active team, member status, task list, dependencies, progress and outputs. Teammate updates return into this state.
- Current-control decision scope: the lead can create/reuse a team, add teammates, create/update tasks/dependencies, inspect current status/output, stop active tasks, send team messages and stop/shut down the team; these actions change current subordinate commitments and allocation.
- Decisive decision or feedback right: choose and revise which current subordinate commitments exist, their dependencies/ownership and when active work/team must be stopped or redirected.
- Decision owner: model-backed Autohand team lead.
- Supporting / enforcement mechanisms: `TeamManager`, `TaskManager`, teammate processes, process leases, message routing, run/cancel wiring, status snapshots and assignment/recovery machinery.
- Closure path: current team/task/member state → lead model chooses intervention → first-party team tool mutates commitment state → teammate behavior/status changes → updated status/output returns to whole-system view.
- Boundary reachability: the complete team lifecycle is first-party documented runtime behavior reachable from the standard CLI lead session.
- Why this is / is not agent-owned: without the lead, managers retain persistence/availability calculations but not task-specific whole-team composition, dependency, intervention and commitment decisions.
- Evidence: `docs/teams.md`; `src/core/toolManager.ts`; `src/core/teams/TaskManager.ts`; `src/core/teams/TeamManager.ts`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic auto-assignment enforces available work after the lead defines task/dependency structure; it does not replace the lead's S3 decision right.

## S3* — Complementary audit

- State: A
- Function: independently challenge the ordinary implementation path through a separate read-only reviewer that directly inspects repository/change artifacts and returns evidence-based findings to the lead for corrective control.
- Disturbance / variety regulated: defects, regressions, security issues, missing tests, maintainability failures or unsupported completion claims that can survive producer self-reporting and ordinary checks.
- Claim being audited: that the scoped code/change is correct, secure, adequately tested and maintainable enough to proceed.
- Ordinary reporting path: lead/implementer/teammate performs implementation through its normal coding loop and returns task status/output/tests.
- Complementary access path: the embedded `reviewer` is an independent read-only reviewer with repository/Git tools and an evidence-led contract; delegation instantiates it as a separate `SubAgent` with its own conversation/model/tool loop and direct repository access.
- Independence boundary: the reviewer cannot edit through its shipped tool set, has separate context and receives review scope rather than merely accepting the producer summary.
- Who acts on findings: findings return from reviewer to lead/delegating control; the lead can then assign/perform corrective edits, tests, another review or other current-control action.
- Decisive decision or feedback right: reviewer model owns audit judgment; lead owns corrective operational response.
- Decision owner: autonomous first-party reviewer actor for audit judgment.
- Supporting / enforcement mechanisms: embedded built-in registry/assets; `SubAgent`; read-only reviewer tools; delegation/team handoff; result transport.
- Closure path: lead delegates review → separate reviewer inspects actual diff/repository evidence → reviewer forms findings → findings return to lead → lead changes subsequent implementation/control.
- Boundary reachability: reviewer definition is embedded in shipped built-in assets and the generic first-party SubAgent path executes built-ins directly.
- Why this is / is not agent-owned: removing reviewer model while retaining tools/transport removes independent audit judgment.
- Evidence: `src/generated/builtinAssets.ts`; `src/core/agents/SubAgent.ts`; `docs/teams.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic `code_review` tooling is not the witness; the state rests on the separately instantiated embedded reviewer actor and corrective handoff.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: model project/external capability conditions, identify future-relevant capability gaps/options and persist selected/generated skills so subsequent Autohand operation has an adapted capability set.
- Disturbance / variety regulated: project languages/frameworks/dependencies/testing/CI and patterns change; installed skills can become stale/redundant; external/community options may fit or fail; missing specialized capability can constrain future execution.
- External distinction: `ProjectAnalyzer` distinguishes the current project's languages, frameworks, dependencies, patterns, platform, Git/tests/CI and package manager; `/learn` additionally obtains a community skill registry and compares external capability options with the installed set.
- Future / prospective distinction: generated skills are explicitly intended for later agent runs, while `/learn update` detects project evolution using stored/current project hashes and decides whether previously generated capability has become stale relative to the new project state.
- Adaptation option generated: model-backed `LearnAdvisor` audits installed skills, ranks community matches, performs capability-gap analysis and can generate a tailored new skill; `--auto-skill` likewise generates a project-specific skill directly from analyzed project distinctions.
- Path back into current capability / S3: selected/generated skills are persisted under Autohand's skills boundary and loaded/available to later lead/SubAgent operation; `learn update` can regenerate stale LLM-generated skills, changing the capability repertoire available to current/future S1 and lead control.
- Decisive decision or feedback right: in autonomous auto-skill mode the model owns the generated adaptation content that becomes persistent capability; in interactive `/learn`, the parent operator owns whether to generate/install the adaptation and its scope after model recommendations/gap analysis.
- Decision owner: model-backed skill generator/advisor in autonomous base mode; human operator in the distinct parent-governed mode.
- Supporting / enforcement mechanisms: `ProjectAnalyzer`; community registry/cache/fetcher; `LearnAdvisor`; generated-skill metadata/project hash; SkillsRegistry; filesystem persistence/loading; learn/update CLI routing.
- Closure path: project/external capability distinctions → model develops adaptation option → autonomous save or parent selection/install → persistent skill enters Autohand registry → subsequent sessions/agents use adapted capability → later project change can trigger re-analysis/regeneration.
- Boundary reachability: `--auto-skill`, `/learn`, `--learn`, `--learn-update` are shipped first-party surfaces at the frozen revision.
- Why this is / is not agent-owned: the model materially determines the generated specialized capability in the autonomous path; deterministic analyzers/storage record and install the decision. The interactive path moves decisive adoption/generation to the parent and returns that choice into the same persistent capability store.
- Evidence: `README.md`; `src/index.ts`; `src/commands/learn.ts`; `src/skills/autoSkill.ts`; `docs/feature_meta_tools.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic skill extensibility or meta-tool creation alone would not establish S4; the positive state rests on project/external distinctions, capability-option development and persistent adaptation returned into later operation.

### S4 mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed Autohand skill generator/advisor | Supported autonomous `--auto-skill` analyzes the selected project and asks the model for a tailored capability | Project distinctions → model-generated skill → first-party persistence → capability available to subsequent sessions; metadata supports later re-analysis/update | `src/index.ts`; `src/skills/autoSkill.ts`; README |
| Parent (`P`) | Human operator | Interactive `/learn` presents project/community analysis, recommendations/gaps and generation/install choice | Advisor develops adaptation options → parent chooses generation/install and scope → skill is persisted → subsequent operation uses changed capability | `src/commands/learn.ts`; README |

The parent row is genuine S4 governance rather than generic configuration because the operator selects a future-oriented capability adaptation developed from project/external distinctions and the decision returns into subsequent operation through the persistent skill registry.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: permission modes, policy rules, project/user configuration, role prompts, team limits, tool restrictions and persisted capabilities constrain operation but do not constitute identity/ultimate-policy adjudication.
- Decisive decision or feedback right: not established for S5-level identity or ultimate policy.
- Decision owner: not established at S5; operator/developer configuration supplies top-level constraints outside a qualifying runtime identity closure.
- Supporting / enforcement mechanisms: permission manager/CLI policy, restricted/unrestricted modes, tool filters, agent/skill definitions, team/task limits, hooks/configuration and persisted tools/skills.
- Closure path: absent at S5 level; no identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned policy governing subsequent runtime operation path was found.
- Why this is / is not agent-owned: agents can create capabilities and regulate current work, but that does not grant legitimate authority to redefine organizational identity/purpose/ultimate policy; ordinary action/capability approval is not S5.
- Evidence: `README.md`; `src/core/toolFilter.ts`; configuration/permission/team surfaces at the frozen revision.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: maintainers decide future releases and operators can rewrite configuration, but adjacent development/administrative authority is not imported as runtime S5.

### Absence scope

- Surfaces inspected: permission/restricted/unrestricted controls; team/lead limits; agent/skill/meta-tool creation; project/user configuration; hooks; provider/model configuration; team control; adaptation/learn surfaces; repository governance adjacency.
- Plausible first-party paths checked: runtime constitution/identity revision; agent-owned ultimate-policy adjudication; parent escalation of identity/purpose conflicts; durable identity/policy decisions returned to govern all operation; maintainer/release governance as distributed parent closure.
- Why no material first-party path remains: inspected mechanisms enforce externally authored operational constraints, change task capability or govern present work. None exposes a boundary-reachable identity/ultimate-policy issue and legitimate final authority with return-to-operation closure.

## Recursion

Teammate processes and delegated SubAgents have their own bounded objective, model/tool loop, context and operational environment, so they are distinct S1 units for S2/S3 analysis. The frozen evidence does not establish that each child also contains the full metasystemic organization required for a stronger full-recursion claim.

## Variety and escalation

Autohand attenuates variety through permissions, tool filtering, task dependencies/ownership, explicit resource coordination, team-size/run budgets and bounded child roles. It amplifies capability through specialist agents, teams, persistent skills/meta-tools, MCP and project/community skill discovery.

Current-operation escalation is concrete: teammate status/output enters the lead's team/task view, and the lead can change tasks/dependencies, stop work or shut down the team. Audit escalation is separate: a read-only reviewer challenges producer evidence and returns findings to the lead. Prospective adaptation is separate again: project/external capability distinctions can result in a new or regenerated persistent skill used by later operation.

## Evidence gaps

- S2 is intentionally bounded to explicit task/dependency/resource-contention regulation; the review does not claim that the shared filesystem is globally conflict-free.
- S3* relies on the embedded read-only reviewer actor executed through the first-party SubAgent/delegation path; generic review tooling is not treated as an independent auditor.
- S4=A(P) distinguishes autonomous generation from interactive parent-governed adoption; ordinary manual skill installation alone would not establish the positive function.
- No runtime identity/ultimate-policy closure was found for S5.
