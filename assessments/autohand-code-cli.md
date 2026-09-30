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
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# Autohand Code CLI

## Review boundary

- System in focus: Autohand Code CLI's first-party public coding-agent runtime at frozen revision `feaa8df7dcc5ee0152bc0d961bc271759fced45a`, including the primary `AutohandAgent`, model/tool runtime, first-party subagents and built-in agents, team/task orchestration, peer/resource coordination, permissions/modes, sessions/context, skills/learn/auto-skill machinery and supported CLI/headless/RPC/ACP surfaces.
- Purpose and identity: perform repository-facing software-engineering work, including autonomous implementation, delegated specialist work, coordinated multi-agent execution, review and persistent adaptation of project-specific agent capabilities.
- Relevant environment: the selected repository/worktree, user objective, provider/model responses, shell/Git/test evidence, teammates and task/resource state, project dependencies/frameworks/CI shape, community skill registry and operator governance choices.
- Standard-distribution boundary: first-party CLI/runtime code, embedded built-in agents/skills, team/task manager, peer/resource-coordination machinery, permission/mode system and skill-learning surfaces are inside. External model providers, MCP servers, community skills before installation and external-agent definitions remain dependencies/environment. Separately built trace/computer-use companions are outside except for concrete integration behavior exposed by the public CLI boundary.
- Credited operating / distribution surfaces: `README.md`; `docs/teams.md`; `docs/feature_meta_tools.md`; `src/core/agent.ts`; `src/core/agents/SubAgent.ts`; `src/core/toolManager.ts`; `src/core/toolFilter.ts`; `src/core/teams/TaskManager.ts`; `src/core/teams/TeamManager.ts`; `src/core/peerTools.ts`; `src/generated/builtinAssets.ts`; `src/index.ts`; `src/commands/learn.ts`; `src/skills/autoSkill.ts`; directly reachable runtime/configuration paths.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests/governance, design plans not wired into the frozen runtime, later default-branch behavior, and behavior owned by external agents/providers. Current-default-branch code search was used only for path discovery; all credited behavior was re-read at the frozen revision.
- First-party operating / deployment modes considered: normal interactive editing mode; AUTO/autonomous execution; PLAN/YOLO where documented; unrestricted/restricted permission configurations; direct delegation and parallel delegation; team creation/teammates/task control; peer/resource coordination; built-in reviewer delegation; `--auto-skill`; interactive `/learn`; `--learn`; `--learn-update`; RPC/ACP/headless surfaces sharing the same runtime.
- Recursion level: one Autohand coding organization. Teammate processes and delegated `SubAgent` instances are distinct lower-level S1 units because each owns a bounded model/tool execution loop. They are not automatically classified as complete recursively viable systems.
- Reviewed revision: `feaa8df7dcc5ee0152bc0d961bc271759fced45a`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Autohand Code owns a model/tool coding loop through `AutohandAgent` and its first-party tool/execution stack. The same distribution can create delegated `SubAgent` instances with their own `ConversationManager`, provider/model loop and filtered tool set. Built-in agent definitions are embedded into the release through generated assets rather than borrowed from user configuration.

The frozen distribution also contains a persistent team organization. The ordinary interactive session becomes the team lead; teammate processes run their own LLM loops; the lead owns a shared `TaskManager`, task dependency graph and current team state. Teammates report task status/output back through the first-party `TeamManager`, and the lead can create/update/stop tasks, add teammates, inspect team/task state, message workers and shut down the team. Tasks can declare blocking dependencies, and idle workers receive only currently available work.

S2 additionally has a first-party capacity-one `coordinate_resource` protocol with request/grant/release/cancel/controller semantics. It gives coexisting agents a concrete way to attenuate exclusive-resource contention rather than relying only on generic messaging.

For complementary audit, the standard distribution embeds an independent read-only `reviewer` agent. A delegated reviewer runs through the separate `SubAgent` model/tool loop with artifact-inspection/Git tools and an audit-specific system prompt, then returns evidence/findings to the lead rather than editing the target itself.

For adaptation, Autohand ships two related paths. `--auto-skill` analyzes the project, asks a model to generate a tailored skill and persists the new `SKILL.md` under the Autohand skills boundary so later sessions can use it. `/learn` and `--learn` analyze the project, installed skills and an external/community skill registry, audit current capability, recommend matching skills or identify capability gaps, and can generate/install new skills. `/learn update` re-analyzes the changed project and regenerates stale LLM-generated skills using project-hash provenance.

Primary evidence:

- [`README.md`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/README.md)
- [`docs/teams.md`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/docs/teams.md)
- [`docs/feature_meta_tools.md`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/docs/feature_meta_tools.md)
- [`src/core/agents/SubAgent.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/agents/SubAgent.ts)
- [`src/core/toolManager.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/toolManager.ts)
- [`src/core/toolFilter.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/toolFilter.ts)
- [`src/core/teams/TaskManager.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/teams/TaskManager.ts)
- [`src/core/teams/TeamManager.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/teams/TeamManager.ts)
- [`src/core/peerTools.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/core/peerTools.ts)
- [`src/generated/builtinAssets.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/generated/builtinAssets.ts)
- [`src/index.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/index.ts)
- [`src/commands/learn.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/commands/learn.ts)
- [`src/skills/autoSkill.ts`](https://github.com/autohandai/code-cli/blob/feaa8df7dcc5ee0152bc0d961bc271759fced45a/src/skills/autoSkill.ts)

## Operational model

A primary Autohand actor can work alone, delegate bounded specialist tasks, or instantiate a longer-lived team. In team mode, the lead has model-facing tools for constructing the team and changing its present commitment structure while teammate processes continue independently. Current state returns through shared team/task state and teammate updates.

Coordination and current control are distinct. S2 regulates interaction among S1s through dependency-aware availability, exclusive task ownership and explicit resource reservation/control. S3 uses the whole team/task state to decide the current population, commitments, dependencies, assignments, interventions and shutdowns on behalf of the whole.

Complementary review is also distinct from ordinary tests or self-review: the embedded `reviewer` is a separate read-only model actor that inspects the actual diff/repository evidence and hands findings back to the lead. Adaptation is distinct again: project/community distinctions are turned into persistent skill capability that changes what later Autohand sessions can do.

## S1 — Operations

- State: A
- Function: perform repository-facing software-engineering transformations by interpreting the objective, selecting permitted tools/actions, observing results and iterating toward the requested working outcome.
- Disturbance / variety regulated: changing code/worktree state, implementation alternatives, provider uncertainty, tool/build/test failures, repository instructions, user constraints and evidence discovered during execution.
- Decisive decision or feedback right: choose the next task-specific repository/tool action and revise it from model/tool/workspace feedback.
- Decision owner: the model-backed Autohand lead or delegated teammate/SubAgent within its bounded local task.
- Supporting / enforcement mechanisms: tool manager/action executor, permission system, conversation/session state, provider adapters, skills, hooks, context controls, run budgets and protocol adapters.
- Closure path: current objective/evidence → model selects tool/action → first-party executor runs it → result returns into conversation → same actor selects another action or completes.
- Boundary reachability: the first-party lead/runtime and delegated SubAgent loops are shipped across supported CLI/headless/protocol modes.
- Why this is / is not agent-owned: removing the model actor leaves tools, permissions and persistence but removes the open-ended coding choice of what to inspect/change/run next; deterministic machinery constrains or executes the choice rather than substituting for it.
- Evidence: `README.md`; `src/core/agent.ts`; `src/core/agents/SubAgent.ts`; `src/core/toolManager.ts` at the frozen revision.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: individual high-risk actions may be operator-governed in interactive permission modes, but first-party autonomous/unrestricted operation is also supported.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among concurrently operating teammate/peer S1 units through dependency-aware work admission, exclusive task ownership and explicit capacity-one resource coordination.
- Disturbance / variety regulated: duplicate ownership of one unit of work, execution of dependent work before prerequisites complete, and simultaneous use of a shared exclusive resource by multiple active agents.
- Distinct S1 units: teammate child processes and delegated SubAgent executions each run independent model/tool loops against the shared organization/workspace.
- Inter-S1 disturbance: two active units can otherwise claim the same current work, consume an exclusive resource simultaneously, or begin a dependent task before another S1 has produced the prerequisite state.
- Attenuating coordination relation: `TaskManager` exposes one owner/status per task, `blockedBy` dependencies and `getAvailableTasks()` that returns only pending work whose dependencies have completed; `TeamManager` assigns available tasks to idle teammates and revises availability from teammate status. Separately, `coordinate_resource` provides capacity-one request/grant/release/cancel/controller semantics for explicitly contested resources.
- Feedback into subsequent S1 behaviour: task completion/status changes unblock later tasks and trigger new assignment; an unavailable dependency prevents assignment; resource grant/release changes whether another peer may proceed. These coordination outcomes therefore alter later S1 execution, not merely record it.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive witness is not the message router or team label. It is the concrete regulation of duplicate/dependency/resource contention among distinct live operational actors and the return of that regulation into which S1 can act next.
- Decisive decision or feedback right: the autonomous lead model decides task decomposition/dependency/assignment interventions through first-party team tools, while teammate/resource protocols feed back availability/contention evidence; deterministic managers enforce the selected dependency/ownership/resource state.
- Decision owner: model-backed team lead for task-specific coordination discretion; resource-controller ownership is explicitly represented by the coordination protocol where used.
- Supporting / enforcement mechanisms: `TaskManager`, `TeamManager`, peer messaging, `coordinate_resource`, team tools and runtime assignment/recovery machinery.
- Closure path: lead/peers establish current work/resource relationship → first-party coordination state accepts/blocks/assigns/grants → workers receive only permitted current work/resource access → completion/release/status changes the coordination state → subsequent S1 behavior changes.
- Boundary reachability: teams, task tools and peer/resource tools are standard first-party runtime surfaces documented and embedded in the frozen CLI product.
- Why this is / is not agent-owned: deterministic task/resource state would not choose the task-specific decomposition, dependencies or intervention if the lead actor were removed; it mainly enforces and transduces the coordination structure chosen through the agentic control path.
- Evidence: `docs/teams.md`; `src/core/teams/TaskManager.ts`; `src/core/teams/TeamManager.ts`; `src/core/peerTools.ts`; `src/core/toolManager.ts` at the frozen revision.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this state does not claim that every shared-filesystem collision is automatically prevented. It is bounded to the explicit dependency/task-ownership/resource-contention disturbances that first-party mechanisms regulate.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current organization-wide team population, work commitments, dependencies, assignments and interventions while teammate S1s continue independently.
- Disturbance / variety regulated: changing team capacity, idle/working/crashed members, blocked/current/completed work, failed or obsolete commitments, dependency changes and cross-unit current priorities that require intervention on behalf of the whole.
- Whole-system current view: the lead owns the active `TeamManager`/`TaskManager` state; first-party `team_status`, `task_list`, `task_get`, `task_output` and live team view expose the active team, member status, complete task list, dependencies, progress and outputs. Teammate task updates flow back through `TeamManager` and update this current state.
- Current-control decision scope: the lead can create/reuse a team, add teammates, create/update tasks and dependencies, inspect current status/output, stop active tasks, send team messages and stop/shut down the team; those actions change current subordinate commitments and their allocation rather than merely one S1's local step.
- Decisive decision or feedback right: choose and revise which current subordinate commitments exist, their dependencies/ownership and when an active task/team must be stopped or redirected.
- Decision owner: the model-backed Autohand team lead in the standard agent-driven team runtime.
- Supporting / enforcement mechanisms: `TeamManager`, `TaskManager`, teammate processes, process leases, message routing, run/cancel wiring, status snapshots and deterministic assignment/recovery machinery.
- Closure path: current team/task/member state → lead model chooses task/team intervention → first-party team tool mutates task/member/team commitment state → teammate process behavior/status changes → updated status/output returns to lead/current team view.
- Boundary reachability: the complete team lifecycle is first-party documented runtime behavior reachable from the standard CLI lead session; no application-authored manager is required.
- Why this is / is not agent-owned: retaining `TaskManager`/`TeamManager` without the lead leaves persistence, availability calculations and fixed lifecycle machinery but removes task-specific whole-team decisions about composition, dependencies, interventions and priority/commitment changes.
- Evidence: `docs/teams.md`; `src/core/toolManager.ts`; `src/core/teams/TaskManager.ts`; `src/core/teams/TeamManager.ts` at the frozen revision.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic auto-assignment chooses an available idle worker mechanically after the lead has defined the current task/dependency structure; that enforcement does not replace the lead's S3 decision right.

## S3* — Complementary audit

- State: A
- Function: independently challenge the ordinary implementation/producer path through a separate read-only reviewer actor that directly inspects repository/change artifacts and returns evidence-based findings to the lead for corrective control.
- Disturbance / variety regulated: defects, regressions, security issues, missing tests, maintainability failures or unsupported completion claims that can survive the producer's ordinary self-reporting and production checks.
- Claim being audited: that the scoped code/change is correct, secure, adequately tested and maintainable enough to proceed.
- Ordinary reporting path: the lead/implementer/teammate performs implementation through its normal coding tool loop and returns its own task status/output/tests.
- Complementary access path: the first-party embedded `reviewer` agent is defined as an independent, read-only reviewer with repository/Git inspection tools and an evidence-led review contract; delegation instantiates it as a separate `SubAgent` with its own conversation/model/tool loop and direct access to the selected repository evidence.
- Independence boundary: the reviewer cannot edit the target through its shipped tool set, has its own conversation/context and receives the review scope rather than merely accepting the producer's summary. It remains inside the same Autohand product/provider environment, so the independence claim is complementary operational independence, not institutional independence.
- Who acts on findings: findings are returned from the reviewer SubAgent to the lead/delegating control path; the lead can then assign/perform corrective edits, tests, another review or other current-control action.
- Decisive decision or feedback right: the reviewer model owns the audit judgment from directly inspected artifacts; the lead owns the corrective operational response after the challenge returns.
- Decision owner: autonomous first-party reviewer actor for audit judgment.
- Supporting / enforcement mechanisms: embedded built-in agent registry/assets; `SubAgent`; read-only reviewer tool set; delegation/team handoff; task/result transport.
- Closure path: lead delegates scoped review → separate read-only reviewer model inspects actual diff/repository evidence → reviewer forms findings with severity/confidence/remediation → findings return to lead → lead changes subsequent implementation/control in response.
- Boundary reachability: the reviewer definition is embedded in the shipped built-in assets and the generic first-party SubAgent path executes built-ins directly; it does not require an external/user-authored reviewer.
- Why this is / is not agent-owned: removing the reviewer model while retaining search/Git tools and transport removes the independent judgment about whether evidence establishes a defect; deterministic components cannot replace that audit discretion.
- Evidence: `src/generated/builtinAssets.ts`; `src/core/agents/SubAgent.ts`; `docs/teams.md` at the frozen revision.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary `code_review` tooling or a self-review skill is not the positive witness; the state rests on the separately instantiated embedded reviewer actor and corrective handoff to the lead.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: model project/external capability conditions, identify future-relevant capability gaps/options and persist selected/generated skills so subsequent Autohand operation has an adapted capability set.
- Disturbance / variety regulated: project languages/frameworks/dependencies/testing/CI and patterns change over time; installed skills can become stale/redundant; external/community capability options may fit or fail to fit the project's emerging needs; missing specialized skill capability can constrain future execution.
- External / future-relevant distinctions: `ProjectAnalyzer` derives project languages, frameworks, patterns, dependencies, platform, Git/tests/CI and package manager; `/learn` also obtains the community skill registry and compares those options with the currently installed capability set; `/learn update` detects project change through stored/current project hashes.
- Adaptation options: model-backed `LearnAdvisor` audits installed skills, ranks community matches, performs gap analysis and can generate a tailored new skill with an allowed-tool capability contract. The auto-skill path likewise generates a project-specific skill directly from project analysis.
- Return into present capability: generated/installed skills are persisted under the project/user Autohand skills boundary and are loaded/available to later lead/subagent sessions; `learn update` can regenerate stale LLM-generated skills after environmental/project change. The adaptation therefore changes the present capability repertoire used by later S1/S3 operation rather than ending as a recommendation document.
- Decisive decision or feedback right: in autonomous auto-skill mode, the model owns the content/adaptation option that becomes the generated persistent skill; in interactive `/learn`, the parent operator owns whether to generate/install the adaptation and its scope after receiving model recommendations/gap analysis.
- Decision owner: model-backed skill generator/advisor in the autonomous base mode; human operator in the separate interactive parent-governed mode.
- Supporting / enforcement mechanisms: `ProjectAnalyzer`; community registry/cache/fetcher; `LearnAdvisor`; generated-skill metadata/project hash; SkillsRegistry; filesystem persistence/loading; learn/update CLI routing.
- Closure path: project/environment/capability distinctions → model develops skill recommendation/generated adaptation → autonomous save or parent selection/install → persistent skill enters Autohand registry/capability → subsequent sessions/agents can use the adapted skill → later project change can trigger re-analysis/regeneration.
- Boundary reachability: `--auto-skill`, `/learn`, `--learn` and `--learn-update` are shipped first-party CLI/runtime surfaces at the frozen revision; no developer-authored adaptation controller is required.
- Why this is / is not agent-owned: the model materially determines the generated specialized skill/capability in the autonomous path; deterministic analyzers/storage record and install that decision. The interactive advisor path deliberately moves the decisive adoption/generation choice to the parent operator and returns that choice into the same persistent capability store.
- Evidence: `README.md`; `src/index.ts`; `src/commands/learn.ts`; `src/skills/autoSkill.ts`; `docs/feature_meta_tools.md` at the frozen revision.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic skill extensibility or agent-defined meta-tools alone would not establish S4. The positive state rests specifically on environment/project analysis, capability-gap/option development and persistent adaptation returned into future operation.

### S4 mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed Autohand skill generator/advisor | Operator starts supported autonomous `--auto-skill`; the runtime analyzes the selected project and calls the model to produce a tailored capability | Project distinctions → model-generated skill → first-party persistence under Autohand skills → capability available to subsequent sessions; generated metadata supports later re-analysis/update | `src/index.ts`; `src/skills/autoSkill.ts`; README |
| Parent (`P`) | Human operator | Interactive `/learn` presents project/community analysis, recommendations/gaps and a generation/install decision | Advisor develops adaptation options → parent chooses generation/install and scope → selected/generated skill is persisted → subsequent Autohand operation can use the changed capability set | `src/commands/learn.ts`; README |

The parent row is a genuine S4 ownership mode rather than generic human configuration because the operator's decision selects a future-oriented capability adaptation developed from current project/external capability distinctions and that decision returns into subsequent operation through the persistent skill registry.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: permission modes, policy rules, project/user configuration, built-in role prompts, team limits, tool restrictions and persisted capabilities constrain or shape operation, but they do not constitute an identity/ultimate-policy adjudication path.
- Decisive decision or feedback right: not established for S5-level identity or ultimate policy.
- Decision owner: not established at S5; operator/developer configuration supplies top-level constraints outside a qualifying runtime identity closure.
- Supporting / enforcement mechanisms: permission manager/CLI policy, restricted/unrestricted modes, tool filters, agent/skill definitions, team/task limits, hooks/configuration, persisted meta-tools and skills.
- Closure path: absent at S5 level; no identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned policy governing subsequent runtime operation path was found.
- Why this is / is not agent-owned: Autohand agents can create capabilities and regulate current work, but that does not grant legitimate authority to redefine the organization's ultimate identity/purpose/policy. Human approval of an operational action or capability install is likewise not automatically S5.
- Evidence: `README.md`; `src/core/toolFilter.ts`; configuration/permission/team surfaces at the frozen revision.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository maintainers decide future releases and operators can rewrite configuration, but adjacent development/administrative authority is not imported into the running product as S5.

### Absence scope

- Surfaces inspected: permission/restricted/unrestricted controls; team/lead limits; agent/skill/meta-tool creation; project/user configuration; hooks; provider/model configuration; current team control; adaptation/learn surfaces; repository governance adjacency.
- Plausible first-party paths checked: runtime constitutional or identity revision; agent-owned ultimate-policy adjudication; explicit parent escalation of identity/purpose conflicts; durable identity/policy decisions returned to govern all subsequent operation; maintainer/release governance as a possible distributed parent closure.
- Why no material first-party path remains: the inspected mechanisms either enforce externally authored operational constraints, change task capability, or govern present work. None exposes a boundary-reachable identity/ultimate-policy issue and legitimate final authority with return-to-operation closure at the assessed runtime recursion.

## Recursion

Teammate processes and delegated SubAgents have their own bounded objective, local model/tool loop, context and operational environment, so they are distinct S1 units for S2/S3 analysis. The frozen evidence does not establish that each child also contains the full S2/S3/S3*/S4/S5 organization required for a stronger full-recursion claim; spawning a capable coding child therefore remains operational nesting rather than proof of complete recursive viability.

## Variety and escalation

Autohand attenuates variety through permissions, tool filtering, task dependencies/ownership, explicit resource coordination, team-size/run budgets and bounded child roles. It amplifies capability through specialist agents, teams, persistent skills/meta-tools, MCP and project/community skill discovery.

Current-operation escalation is concrete: teammate status/output enters the lead's team/task view, and the lead can change tasks/dependencies, stop work or shut down the team. Audit escalation is separate: a read-only reviewer challenges producer evidence and returns findings to the lead. Prospective adaptation is separate again: project/external capability distinctions can result in a new or regenerated persistent skill used by later operation.

## Evidence gaps

- The S2 mapping is intentionally bounded to explicit task/dependency/resource-contention regulation; the review does not claim that the shared filesystem is globally conflict-free.
- S3* relies on the embedded read-only reviewer actor executed through the first-party SubAgent/delegation path; generic `code_review` tooling is not treated as an independent auditor.
- S4=A(P) distinguishes autonomous generation from interactive parent-governed adoption; ordinary manual skill installation by itself would not establish the positive function.
- No runtime identity/ultimate-policy closure was found for S5.
