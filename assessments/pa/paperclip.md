---
harness_id: paperclip
project_name: Paperclip
repository: https://github.com/paperclipai/paperclip
review_ref: 7f9867895c4e7e9589b233a93aa9efceb0c992d0
reviewed_at: 2026-11-17
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.4
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Paperclip

## Review boundary

- System in focus: one Paperclip company containing its first-party goals, org chart, autonomous agent heartbeats, tasks/dependencies, budgets, management hierarchy, execution policies, board approvals and governance at the pinned revision.
- Purpose and identity: operate a persistent AI-agent organization that decomposes company goals into accountable work while preserving budgets, reporting lines, review and board authority.
- Relevant environment: company goals and board instructions, repositories/workspaces, external agent runtimes, provider/model services, integrations, customers/market context supplied through tasks and human oversight.
- Standard-distribution boundary: Paperclip server/UI/CLI, bundled Paperclip agent skill, company/agent/task/goal state, execution-policy and budget/governance machinery; provider-native agents are hosts whose organizational rights count only through Paperclip's first-party contract.
- Credited operating / distribution surfaces: first-party Paperclip server, UI, API, agent heartbeat skill, CEO/manager instructions, persistent tasks and blocker/checkout rules, optional runtime-enforced reviewer stages, board goals/strategy approvals and operator overrides.
- Adjacent first-party surfaces excluded from ownership: maintainer CI/release/dogfood organization, documentation plans and roadmap items, test/benchmark/Storybook fixtures, unmerged source PRs, uninstalled third-party tools and the private Cloud routing plugin. A provider's external capabilities are not Paperclip company actors.
- First-party operating / deployment modes considered: autonomous CEO/manager/report heartbeats, structured review stages, board strategy/hire approval, user overrides and self-hosted company operation.
- Recursion level: one Paperclip company. Manager subtrees are internal organizational subdivisions; this assessment does not assume every reporting subtree independently satisfies a full viable recursion.
- Reviewed revision: `7f9867895c4e7e9589b233a93aa9efceb0c992d0`.
- Observation date: 2026-11-17.
- Generated Profile version: `0.2.2`.
- Generated Methodology version: `0.3.4`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.8`.

## Repository architecture

Paperclip is a first-party Node.js/React control plane for heterogeneous agents with runtime-registered plugin and connection interfaces. The current supported distribution additionally exposes evaluation/feedback, versioned skills, routines, optional external memory connections and opt-in model/account routing; these do not independently establish a future-oriented S4 adaptation decision loop. Paperclip is a persistent control plane for heterogeneous agents. Agents wake in bounded heartbeats, inspect assigned work and organizational context, checkout issues, execute, report and exit. Goals, org charts and reporting lines provide purpose/context; tasks carry dependencies and atomic checkout; budgets cap spend; CEO/managers decompose and assign work; execution policies route completed work to distinct reviewers/approvers; board users retain strategy, hiring, override and company-goal authority.

## Operational model

Operational S1 units are autonomous report agents working assigned company tasks. The CEO and managers own model-driven partitioning, assignment, monitoring and unblock/escalation decisions, while Paperclip's runtime enforces leases, budget and workflow invariants. Review stages can appoint a separate agent and explicitly exclude the executor. The board establishes company goals and approves or revises strategy, providing an explicit parent S5 closure and a parent S3 mode for current supervisory intervention.

## Primary evidence

- [`README.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/README.md) — company boundary, agents, goals, budgets, atomic task execution and governance.
- [`docs/guides/board-operator/delegation.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/docs/guides/board-operator/delegation.md) — board/CEO lifecycle, autonomous decomposition/assignment/monitoring and parent approvals.
- [`docs/guides/execution-policy.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/docs/guides/execution-policy.md) — enforced separate review/approval stages, executor exclusion, change requests and re-review.
- [`skills/paperclip/SKILL.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/skills/paperclip/SKILL.md) — heartbeat work contract, task checkout, chain of command, delegation, dependencies and escalation.
- [`docs/start/core-concepts.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/docs/start/core-concepts.md) — company agents/checkout and board approvals/overrides.
- [`server/src/services/issues.ts`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/server/src/services/issues.ts), [`server/src/services/heartbeat.ts`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/server/src/services/heartbeat.ts) — actual task/wake mechanisms.
- [`server/src/services/issue-execution-policy.ts`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/server/src/services/issue-execution-policy.ts) — review-stage participant selection and return path.
- [`server/src/routes/approvals.ts`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/server/src/routes/approvals.ts), [`docs/guides/board-operator/approvals.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/docs/guides/board-operator/approvals.md) — board approval decisions and return-to-work.
- [`server/src/onboarding-assets/ceo/HEARTBEAT.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/server/src/onboarding-assets/ceo/HEARTBEAT.md), [`ROADMAP.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/ROADMAP.md) — shipped CEO work protocol versus planned organizational learning.
- [`doc/connections/MEMORY.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/doc/connections/MEMORY.md), [`doc/connections/AI-CONNECTION-ROUTERS.md`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/doc/connections/AI-CONNECTION-ROUTERS.md), [`server/src/services/ai-connection-router.ts`](https://github.com/paperclipai/paperclip/blob/7f9867895c4e7e9589b233a93aa9efceb0c992d0/server/src/services/ai-connection-router.ts) — optional memory and resource routing, not automatic external adaptation.

## S1 — Operations

- State: A
- Function: autonomous agents execute outcome-bearing company work in bounded heartbeats and return durable task results.
- Disturbance / variety regulated: task uncertainty, repository/workspace state, tool/model observations, blockers and acceptance criteria within each assigned work item.
- Decisive decision or feedback right: choose the concrete actions needed to advance an assigned task and decide what result/evidence to report.
- Decision owner: the assigned model-driven report/worker agent.
- Supporting / enforcement mechanisms: issue checkout, run-scoped credentials, workspace resolution, skills/context injection, heartbeat scheduling, budget checks and durable comments/status.
- Closure path: the agent checks out work, executes it, records progress/result and status, and later heartbeats/managers consume the updated task state.
- Boundary reachability: The bundled agent heartbeat contract and real company issue checkout/update endpoints run in the supported server/agent mode, independent of contributor CI.
- Why this is / is not agent-owned: the model-driven worker chooses the operational solution; Paperclip's runtime constrains execution but does not choose the substantive task outcome.
- Evidence: `skills/paperclip/SKILL.md`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: provider runtimes are external hosts, but Paperclip supplies the first-party operating contract that turns them into company S1 units.

## S2 — Coordination

- State: A
- Function: attenuate duplicate/conflicting work and dependency interference among multiple autonomous report agents.
- Disturbance / variety regulated: double-work on the same task, dependency-invalid execution, conflicting work allocation and capacity/role mismatches across reports.
- Decisive decision or feedback right: partition company work into tasks/subtasks, choose assignees based on role/capability, sequence blocked work and reassign/unblock work when the initial allocation fails.
- Decision owner: autonomous CEO and manager agents within their first-party management heartbeat contracts.
- Supporting / enforcement mechanisms: atomic task checkout, blocker relationships, one-active-run constraints, org chart/reporting lines and assignment-triggered heartbeats.
- Closure path: CEO/managers create and assign a non-overlapping/dependency-aware work structure; runtime prevents duplicate checkout and blocked work from proceeding; status/blocker feedback returns to managers, who reassign, unblock or escalate before subsequent S1 work.
- Boundary reachability: Two or more report agents are active S1 units; CEO/manager task assignment and blocker feedback run through their bundled heartbeat contract and server checkout/dependency controls into later agent wakes.
- Why this is / is not agent-owned: deterministic checkout enforces the selected coordination boundary, but model-driven CEO/managers own decomposition, assignee and unblock/reassignment judgments that change later worker behavior.
- Evidence: `docs/guides/board-operator/delegation.md`, `skills/paperclip/SKILL.md`, `README.md`.
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: simple delegation alone would not establish S2; the positive mapping depends on the concrete double-work/dependency disturbance plus the management feedback path.
- Distinct S1 units: two or more report agents executing separate company tasks/subtasks under the CEO/manager hierarchy.
- Inter-S1 disturbance: without coordination, agents can duplicate ownership of work, proceed despite unresolved dependencies or receive incompatible/overlapping assignments.
- Attenuating coordination relation: CEO/managers decompose and allocate work while blocker/checkout invariants enforce dependency and single-owner boundaries.
- Feedback into subsequent S1 behaviour: task status, blockers and report updates trigger manager monitoring, reassignment/unblocking/escalation; subsequent agents receive changed assignments and cannot concurrently checkout the same work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the cited mechanisms explicitly regulate double-work and dependency/assignment interference across multiple autonomous workers rather than merely passing messages.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current company-wide commitments, priorities, capacity, budgets and blocked work while preserving board supervisory intervention.
- Disturbance / variety regulated: stalled tasks, changing priorities, insufficient capacity, budget pressure, approval waits, agent error/paused state and current goal execution drift.
- Decisive decision or feedback right: autonomous mode — monitor company progress, choose task priorities/assignment/unblocking/hiring escalation and current managerial intervention; parent mode — board users override agent decisions, reassign/change priorities/budgets and pause or terminate agents.
- Decision owner: base mode — autonomous CEO/manager agents; parent mode — legitimate board user/operator.
- Supporting / enforcement mechanisms: dashboard/activity state, goal/task hierarchy, chain of command, budgets/hard stops, agent status, approvals and heartbeat scheduling.
- Closure path: CEO/manager decisions rewrite assignments/priorities/subtasks or escalate; board decisions directly change current task/agent/budget state; later heartbeats execute under that returned state.
- Boundary reachability: Agent managers have first-party company/issue/goal state and can change assignments; the distinct supported board/operator mode changes priorities, budgets, assignments or agent pause status that later runs obey.
- Why this is / is not agent-owned: model-driven managers own current-control discretion in the base mode; deterministic budget/checkout enforcement only implements constraints. A distinct board mode can supersede those decisions.
- Evidence: `docs/guides/board-operator/delegation.md`, `docs/start/core-concepts.md`, `README.md`, `skills/paperclip/SKILL.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: board strategy approval also participates in S5; S3 classification uses only current-operation rights such as priority, budget, reassignment and intervention.
- Whole-system current view: CEO/management heartbeats consume company goals, task/status hierarchy, reports, blockers, budgets, agent states and pending approvals across the governed company.
- Current-control decision scope: current decomposition/assignment, priorities, unblocking/reassignment, capacity/hiring escalation, budget-sensitive work focus and operator intervention.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | CEO / manager agent | heartbeat sees current goals, reports, blockers, capacity or budget pressure | agent changes tasks, assignments, priorities/unblocking or escalates; reports wake and operate under the updated state | `docs/guides/board-operator/delegation.md`, `skills/paperclip/SKILL.md` |
| Parent (`P`) | board user/operator | operator detects stalled/misaligned current operation or chooses an override | reassign/priority/budget/pause/terminate decision is persisted in Paperclip and governs later heartbeats | `docs/start/core-concepts.md`, `README.md` |

## S3* — Complementary audit

- State: A
- Function: independently review a worker's completion claim and return approval or required changes before final completion.
- Disturbance / variety regulated: incorrect, low-quality or non-compliant completion claims that the producing agent could otherwise self-accept.
- Decisive decision or feedback right: approve the submitted work or request changes with an explicit review decision.
- Decision owner: a distinct model-driven agent selected as the active review-stage participant.
- Supporting / enforcement mechanisms: execution-policy stages, runtime participant routing, executor exclusion, decision audit records and return-assignee state.
- Closure path: executor completion is intercepted into `in_review`; reviewer approval advances/finalizes, while change request returns the task to the executor and subsequent resubmission routes back to the same review stage.
- Boundary reachability: Optional execution-policy review is an actual first-party task mode: the runtime excludes the executor from review participant selection, another agent judges the submitted work, and approval or change request changes the next task stage.
- Why this is / is not agent-owned: the reviewer agent owns the review judgment; Paperclip enforces participant identity and stage transitions without deciding quality itself.
- Evidence: `docs/guides/execution-policy.md`, `skills/paperclip/SKILL.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: review stages are optional per issue, so S3* is a supported first-party mode rather than a mandatory path for every task.
- Claim being audited: that the executor's task result is correct/acceptable and ready to advance.
- Ordinary reporting path: the executor marks work complete and supplies the required comment/result.
- Complementary access path: runtime intercepts completion and assigns a distinct eligible reviewer agent, excluding the original executor.
- Independence boundary: reviewer identity is a separate execution-policy participant; the runtime excludes the original executor from reviewer selection.
- Who acts on findings: Paperclip returns changes to the original executor or advances the issue, thereby altering subsequent execution.

## S4 — Outside-and-then intelligence

- State: —
- Function: no independently established first-party external-and-prospective organizational adaptation loop in the reviewed standard Paperclip company distribution.
- Disturbance / variety regulated: future market/model/provider changes, new environment opportunities and evolving company capabilities; the runtime exposes current-work and learning support but no supported closed organization-level adaptation cycle.
- Decisive decision or feedback right: no qualified first-party actor or function-specific constructor was evidenced that converts future-oriented external distinctions into adaptation options and returns an authorized selection to change future company capability.
- Decision owner: none established for a qualifying S4 loop. A board user can direct future research or change company strategy, but company S5 authority or an ordinary assigned research task alone is not a separate first-party S4 function.
- Supporting / enforcement mechanisms: saved agent evals and feedback, skill-version rollback, routines, memory/provider connectors, experimental account routing, goals/strategy, and generic research tasks.
- Closure path: no evidenced supported external/future observation → contrasting adaptation options → qualified choice → first-party change of subsequent company capability/S3.
- Why this is / is not agent-owned: agents may research or learn within task work, but optional memory, routing, versioned skills, planning and generic task/goal changes cannot be credited as a distinct organization-level future adaptation owner without that closed path.
- Evidence: `ROADMAP.md`, `doc/connections/MEMORY.md`, `doc/connections/AI-CONNECTION-ROUTERS.md`, `server/src/services/ai-connection-router.ts`, `server/src/routes/routines.ts`, `server/src/onboarding-assets/ceo/HEARTBEAT.md`, `docs/start/core-concepts.md`, `doc/plugins/PLUGIN_SPEC.md`.
- Basis: explicit + structural (bounded negative finding).
- Confidence: medium-high.
- Caveats: Paperclip marks Self-Organization and Automatic Organizational Learning as planned; the self-hosted connection router defaults off and substantive Cloud routing policy belongs to a private plugin. An installed specialized external plugin or future merged code could require another review, but is not credited as the default first-party company mode.

### Absence scope

- Surfaces inspected: pinned README/ROADMAP, CEO heartbeat/strategy, shipped issue/approval/review/routine service and API surfaces, first-party evaluation/skill and memory descriptions, plugin-spec boundary, experimental AI connection router host and runtime.
- Plausible first-party paths checked: manager resource balancing, board strategy, generic agent research tasks, evals and skills, memory connectors, scheduled routines and AI account/model routing; related original issues/PRs remain proposals, not shipped S4 evidence.
- Why no material first-party path remains: reviewed shipped mechanisms store, enforce, schedule, report or route the present work and may support future development, but no specifically evidenced external/future sensing and authorized adaptation-option decision feeds changed company capability back into ongoing operations. Planned automatic learning/self-organization and optional private or uninstalled plugin policy are outside the supported default closure.

## S5 — Policy and identity

- State: P
- Function: maintain company purpose and ultimate policy through board-owned company goals and strategy authority.
- Disturbance / variety regulated: ambiguity or disagreement over what the company is trying to achieve, which strategy is legitimate and whether organization-level hires/changes are acceptable.
- Decisive decision or feedback right: establish company goals and approve, reject or request revision of the CEO's proposed strategy and organization-level hire requests.
- Decision owner: legitimate board user/operator.
- Supporting / enforcement mechanisms: company goals, strategy approval queue, hire approvals, org chart and persistent task/goal hierarchy.
- Closure path: board sets the company goal; CEO proposes strategy; board authoritatively approves/rejects/revises; approved direction returns to Paperclip and the CEO decomposes it into tasks/assignments that govern later operation.
- Boundary reachability: The Paperclip company goal and CEO strategy approval are first-party board controls; a submitted strategy reaches legitimate user authority and the returned decision gates subsequent company task/agent execution.
- Why this is / is not agent-owned: the CEO proposes and operationalizes strategy, but the first-party lifecycle explicitly reserves ultimate company-goal/strategy acceptance to the board; no autonomous internal ultimate-authority mode is established.
- Evidence: `docs/guides/board-operator/delegation.md`, `README.md`, `docs/start/core-concepts.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary task approvals are not counted as S5; the positive mapping uses company-goal and strategy-level authority.
- Identity / ultimate-policy issue: company goal/purpose and the strategy/organizational composition authorized to pursue it.
- Ultimate authority in each claimed mode: parent mode only — the board user/operator.
- Return-to-operation path: board-approved goal/strategy/hire decision persists in Paperclip; CEO/managers create and assign work under it; subsequent heartbeats inherit that goal ancestry and organization.

## Recursion

Paperclip supports multi-level reporting hierarchies, but this assessment declares one company as the system in focus. Manager subtrees can coordinate work without being assumed to satisfy a complete recursive VSM organization.

## Variety and escalation

Variety is attenuated through task decomposition, role-based assignment, blockers, atomic checkout, budgets and review stages. Unresolved budget, approval and strategic ambiguity escalate through the chain of command to the board rather than being silently settled by lower-level agents.

## Evidence gaps

Source-only review, not a live agent integration benchmark. Manager delegation and optional reviewer stages are supported first-party paths, not necessarily exercised in every company. Installed third-party plugins may implement other modes but are not credited as default shipped S4. The pinned source demonstrates no sufficient outside-and-prospective adaptation closure; reopen this conclusion when a concrete supported S4-specific path ships.

## New-ref reassessment disposition

- Index task: https://github.com/opensiro/vsm-harness-index/issues/3230
- Accepted one-off review event: S3230 in data/reassessment-history.psv (Index PR #3235), distinct from frozen reassessment rounds; no synthetic round freshness is claimed.
- Independent S4 source audit: [Index issue #3242](https://github.com/opensiro/vsm-harness-index/issues/3242), OPEN/PENDING. The 2026-11-17 review is source-based by one executor; its negative S4 classification has not yet received independently reproduced agreement.
- Historical accepted review: `352153b5edf02ff4262210c7bd5bfa94bcf37c7c` on 2026-09-18 (Profile 0.2.2 / Methodology 0.3.4).
- New inspected boundary: `7f9867895c4e7e9589b233a93aa9efceb0c992d0` on 2026-11-17; comparison: https://github.com/paperclipai/paperclip/compare/352153b5edf02ff4262210c7bd5bfa94bcf37c7c...7f9867895c4e7e9589b233a93aa9efceb0c992d0
- Profile 0.2.4 / Methodology 0.3.8 conclusion: **S1=A, S2=A, S3=A(P), S3*=A, S4=—, S5=P**; function states unchanged while source pin, documentation and current semantic provenance are refreshed. Immutable generation provenance and original material classification-change date remain unchanged.
- Evidence method: pinned public implementation plus first-party runtime/docs/issue-policy/approval/CEO and optional connection surfaces; no live runtime test or independent reviewer result is claimed. Roadmap proposals and external issues are not positive Index witnesses.
