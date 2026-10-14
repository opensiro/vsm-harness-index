---
harness_id: pythinker-code
project_name: Pythinker Code
repository: https://github.com/PyModel/pythinker-code
review_ref: 5c5a2053116c1e18c7e1e22710d846fc27945f08
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Pythinker Code

## Review boundary

- System in focus: the first-party Pythinker Code installable coding-agent runtime at frozen `5c5a2053116c1e18c7e1e22710d846fc27945f08`, including its Agent Core v2 model/tool loop, session subagent runs, and the first-party explicitly opt-in experimental Tower orchestration mode.
- Purpose and identity: execute user-requested local coding tasks with autonomous model/tool feedback, and in the supported Tower mode decompose a shared objective into scoped independently worked missions subject to a review and merge protocol.
- Relevant environment: source files, build/test outputs, developer objectives, concurrent role-agent changes, git worktrees and branches, review verdicts and shifting model/tool observations.
- Standard-distribution boundary: the shipped CLI/Desktop/ACP-facing first-party runtime, locally instantiated model-backed main and subagents, bundled Tower feature and its backed `TowerStore` protocol, task/session/permission/goal systems. External provider inference, external MCP servers, project-specific skills/agents, operators' git repositories and upstream CI/contributor governance are dependencies or adjacent arrangements, not credited first-party owners.
- Credited operating / distribution surfaces: `apps/pythinker-code/src/cli/`, `packages/agent-core-v2/src/agent/loop/`, `packages/agent-core-v2/src/session/subagent/`, `packages/agent-core-v2/src/agent/toolExecutor/`, `packages/agent-core-v2/src/features/tower/`, `packages/agent-core-v2/src/features/goal/`, `packages/agent-core-v2/src/agent/permissionPolicy/` and the packaged agent tools.
- Adjacent first-party surfaces excluded from ownership: upstream developer governance, release workflows, doc site, tests, project-local user plugins and arbitrary external agents. A skill named “review” is not by itself an S3* auditor.
- First-party operating / deployment modes considered: ordinary local coding session with or without bounded background subagent tasks; opt-in `PYTHINKER_CODE_EXPERIMENTAL_TOWER` feature with `/tower`, TowerInit/Plan/Spawn/Mission/Review/Merge and separate worktree worker/reviewer agents; user permission and goal modes. The Tower feature is compiled and registered first-party but is disabled by default, so no Tower ownership is asserted for ordinary unenabled sessions.
- Recursion level: one local project/multi-agent Tower operating organization with leader and mission-scoped model workers/reviewers; unconnected user sessions or multi-device views are not automatically a larger viable system.
- Reviewed revision: `5c5a2053116c1e18c7e1e22710d846fc27945f08` (immutable from intake #898; not repinned to current upstream).
- Observation date: 2026-10-15.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The first-party Agent Core v2 loop maintains a bounded turn with model requests, model-selected tools, tool execution and results returned to the conversation. The `Agent` tool can instantiate a first-party `SessionSubagentService` agent using a bounded prompt/profile/model, independently running a turn; background tasks expose task-wait/output/stop controls. This supplies concrete model-led operational S1 units, not automatically a metasystem. In normal mode permissions, sessions and persisted goals constrain this work without establishing all higher VSM functions.

The optional `TowerFeature` registers dedicated tools and a worker profile when its experimental flag is enabled. `TowerPlan` generates mission definitions with branch, task criteria, scope and dependencies; `TowerStore.plan` rejects overlapping live build-mission scope stems and colliding branch identities. `TowerSpawn` wires an actual background worker or a distinct reviewer, assigns mission worktrees/branch identity and provides mission briefings. Workers may edit only their declared mission scope and report completion into durable Tower protocol files. `TowerMerge` runs through `TowerStore.merge`: it refuses unreviewed, non-clean, changed-since-review and out-of-scope branches, and merges a clean current-reviewed branch back to the declared base. The merge step also identifies potential conflicts with unmerged overlapping branch changes and returns them for subsequent instructions to affected workers. These are concrete constructor interference checks, distinct from the model-led leader's discretionary planning.

A separate model reviewer spawned for a branch uses its own source context and `TowerReview` to submit a semantic verdict against the mission's tasks and changed code. `TowerStore.submitReview` accepts reviews only from the tower or *assigned reviewers* for that target, stamps the exact reviewed commit, persists findings, and resets a completed mission to active upon a non-clean verdict. The mandatory `TowerStore.merge` gate refuses to admit a branch without a latest `clean` review on the actual current tip; non-clean review calls instruct renewed worker fixing/re-review. This forms the complementary source-audit decision/return under the enabled Tower mode. The gate does **not** independently verify every model-generated finding or test run; the semantic audit right belongs to a separate reviewer model, and deterministic merge admission only enforces its recorded verdict.

Primary evidence: [`README.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/README.md); [`packages/agent-core-v2/src/agent/loop/loop.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/agent/loop/loop.ts); [`packages/agent-core-v2/src/agent/loop/machine/engine.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/agent/loop/machine/engine.ts); [`packages/agent-core-v2/src/agent/tools/agent/agent.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/agent/tools/agent/agent.ts); [`packages/agent-core-v2/src/session/subagent/subagent.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/session/subagent/subagent.ts); [`packages/agent-core-v2/src/features/tower/flag.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/flag.ts); [`packages/agent-core-v2/src/features/tower/towerFeature.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/towerFeature.ts); [`packages/agent-core-v2/src/features/tower/tools/plan/plan.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/plan/plan.md); [`packages/agent-core-v2/src/features/tower/tools/spawn/spawn.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/spawn/spawn.md); [`packages/agent-core-v2/src/features/tower/tools/review/review.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/review/review.md); [`packages/agent-core-v2/src/features/tower/tools/merge/mergeTool.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/merge/mergeTool.ts); [`packages/agent-core-v2/src/features/tower/protocol/store.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/protocol/store.ts).

## Operational model

Single-run coding is S1. When Tower is enabled, each separately running model agent executes an operational coding or inspection mission; an agent-led tower planner/controller exercises distinct whole-current mission oversight. The constructor attenuates concrete inter-worker edit interference through scope exclusion, isolated worktrees and merge conflict checks; a separate model reviewer challenges branch outcomes through mandatory, commit-bound source review and returns failed work for correction before merge. This mode is first-party but explicitly experimental and opt-in; its evidence is source-level reachability, not a production reliability or quality certification.

## S1 — Operations

- State: A
- Function: turn an uncertain coding objective into environment-responsive file inspection, edits, command execution and task results.
- Disturbance / variety regulated: unknown source state, compiler/test errors, tool failures and unexpected repository conditions.
- Decisive decision or feedback right: select coding/investigation tools, modify source and change next steps after observing returned results; in Tower mode individual model workers own bounded mission execution.
- Decision owner: first-party main and child model-directed Agent Core runs. External LLM transport supplies inference but not a separate borrowed coding-agent executable.
- Supporting / enforcement mechanisms: loop machine/tool scheduler, tool registry, permissions, model adapter, context and session history, optional subagent profiles.
- Closure path: user's goal/mission and observed workspace state → model-chosen tool action → first-party executor with authorization → tool result/error returned into the subsequent model turn → revised action or completion.
- Boundary reachability: shipped main runtime runs the agent loop, and `SessionSubagentService` instantiates first-party background and foreground agent runs. Tower workers use this shipped subagent path.
- Why this is / is not agent-owned: removing model-led action selection leaves deterministic tools and scheduling, but no equivalent coding decisions.
- Evidence: [`packages/agent-core-v2/src/agent/loop/machine/engine.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/agent/loop/machine/engine.ts); [`packages/agent-core-v2/src/agent/toolExecutor/toolExecutor.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/agent/toolExecutor/toolExecutor.ts); [`packages/agent-core-v2/src/session/subagent/subagent.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/session/subagent/subagent.ts); [`packages/agent-core-v2/src/agent/tools/agent/agent.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/agent/tools/agent/agent.ts); [`README.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: does not assert correctness or model-provider ownership.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference between distinct concurrently tasked, first-party coding workers in one shared repository under enabled Tower mode.
- Disturbance / variety regulated: two workers taking overlapping writable scope, git branch identity collisions, and incompatible commits/files being integrated into the same base.
- Decisive decision or feedback right: deterministic mission admission rejects pairwise conflicting scopes; isolated branch/worktree allocation constrains writes; merge admission refuses out-of-scope changes and reports actual overlap with other unmerged branches. Leader/worker receives the specific constraint or conflict for reallocation/rebase.
- Decision owner: first-party `TowerStore` and worktree/merge protocol as **constructor**, with agent tower leader owning discretionary redesign of missions. No claim that the deterministic scope match or git conflict test is model-owned.
- Supporting / enforcement mechanisms: mission scope stems and dependency graph, unique branch identifiers, worktree creation, `assertScopesDisjoint`, git diffs, branch merge checks, protocol results.
- Closure path: proposed mission overlaps another S1's scope → rejected allocation requiring the tower to revise mission ownership; or child branch changes → merge checks/report → conflicting worker is instructed to rebase/resolve and re-review before successful integration.
- Boundary reachability: flagged first-party TowerFeature registers `TowerPlan`/`TowerSpawn`/`TowerMerge` and these operations invoke `TowerStore` on actual git worktrees.
- Why this is / is not agent-owned: model may plan better scopes, but source-specific anti-interference controls and gates are deterministic and remain if the planner's discretion is removed; classify as `C`, not `A`.
- Distinct S1 units: model-backed Tower worker agents with separate missions, prompts, worktrees and changed-file outputs.
- Inter-S1 disturbance: overlapping or incompatible writes competing for one project/base branch.
- Attenuating coordination relation: pairwise scope exclusivity plus worktree isolation and conflict-scoped merge admission.
- Feedback into subsequent S1 behaviour: failed mission scope admission and merge conflict details flow back into tower control, which can redefine ownership, ask rebases or hold the merge.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: scope collision and merge interference are keyed to the cross-worker conflict itself; they are not just a message bus or a sequential task queue.
- Evidence: [`packages/agent-core-v2/src/features/tower/protocol/store.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/protocol/store.ts); [`packages/agent-core-v2/src/features/tower/tools/plan/plan.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/plan/plan.md); [`packages/agent-core-v2/src/features/tower/tools/spawn/spawn.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/spawn/spawn.md); [`packages/agent-core-v2/src/features/tower/tools/merge/mergeTool.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/merge/mergeTool.ts).
- Basis: explicit + structural
- Confidence: high (for enabled Tower mode)
- Caveats: overlap detection of declared patterns uses scope stems rather than formal all-glob intersection; does not claim absolute prevention of every edit conflict. The feature is opt-in and marked experimental.

## S3 — Inside-and-now control

- State: A
- Function: regulate the whole set of current Tower missions and role agents with assignment, priority/dependency control, rework and base-merge decisions at the shared objective boundary.
- Disturbance / variety regulated: incomplete missions, diverging child outcomes, blocked dependencies, unreviewed branches, failed audits and conflicting current commitments.
- Decisive decision or feedback right: the model-led main Tower agent chooses the plan/decomposition of the shared goal, worker/reviewer assignment, review/rework routing and whether to request a merge when prerequisites are met.
- Decision owner: model-directed Tower lead on the main-agent session, not the deterministic protocol store. Store and gates enforce the leader's permissible moves and track roster/status.
- Supporting / enforcement mechanisms: TowerInit/Plan/Spawn/Mission/Status/Inbox/Send/Review/Merge, mission index, dependency/scope records, agent task/background tools and merge gate.
- Closure path: current mission/worker/review statuses → tower model replans/assigns/reviews/escalates → worker instructions or held/merged branches → updated shared mission state and subsequent tower decisions.
- Boundary reachability: `TowerFeature` bundles tools and exposes them to the model in an explicitly enabled shipped mode; `TowerStore` persists live cross-mission scope, owner, status and reviews; `TowerMergeTool` is main-agent-only.
- Why this is / is not agent-owned: without tower lead model choices, the protocol can reject bad calls but cannot choose appropriate decomposition, worker targets or corrective task allocation. The positive autonomy is the agent's current fleet decision, not the presence of a dashboard.
- Whole-system current view: all active Tower mission scopes, agents, review rounds, dependencies, blockers and integration states for the shared project.
- Current-control decision scope: plan or revise mission set, assign workers/reviewers, handle blocked/current work, instruct rework and select eligible merges/abandonments.
- Evidence: [`packages/agent-core-v2/src/features/tower/towerFeature.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/towerFeature.ts); [`packages/agent-core-v2/src/features/tower/tools/plan/plan.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/plan/plan.md); [`packages/agent-core-v2/src/features/tower/tools/mission/missionTool.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/mission/missionTool.ts); [`packages/agent-core-v2/src/features/tower/tools/status/statusTool.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/status/statusTool.ts); [`packages/agent-core-v2/src/features/tower/tools/spawn/spawn.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/spawn/spawn.md); [`packages/agent-core-v2/src/features/tower/protocol/store.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/protocol/store.ts).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: enabled Tower project scope only. Ordinary background subagent delegation without Tower is not enough for S3. No separate parent-owned `(P)` state is proven.

## S3* — Complementary audit

- State: A
- Function: challenge a worker's claimed completed branch against independently inspected changed code, mission scope and acceptance tasks, with a mandatory corrective return before integration.
- Disturbance / variety regulated: missed task criteria, code defects, unsupported “done” claims and post-review branch mutation.
- Claim being audited: a mission owner claims its branch has implemented the assigned tasks within scope and is ready for integration into the shared base.
- Ordinary reporting path: the coding worker marks mission tasks complete and requests review; ordinary worker files, commits and task progress originate from the actor performing implementation.
- Complementary access path: TowerSpawn review_target creates a separately running reviewer-role agent with the mission task list and reviewed branch/diff; its TowerReview result is bound to the observed git commit and written as an independent review record.
- Independence boundary: an assigned reviewer identity is distinct from the assigned worker and must be registered against that target; TowerStore.submitReview rejects review submissions by other non-tower actors. No assertion is made that this source review provides external independent organization-level GitHub approval.
- Who acts on findings: non-clean TowerReview reactivates a completed mission; the tower leader routes evidence back to its owner or a replacement and the merge gate forbids incorporation until a newer clean verdict on the latest branch tip.
- Decisive decision or feedback right: a separately spawned reviewer model can issue `clean` versus defect/hold verdict with findings through `TowerReview`; the actual latest review status and commit identity determine admission to the base.
- Decision owner: dedicated model-running reviewer agent for semantic source inspection and critique, separate from the coding worker. Deterministic TowerStore enforces eligibility and exact-tip freshness, and lead model/worker subsequently owns repairs.
- Supporting / enforcement mechanisms: `TowerSpawn(review_target)` independent briefing with authored mission/tasks, reviewer-only `TowerStore.submitReview` permission, persistent review file including target/reviewer/tip, `MAX_REVIEW_ROUNDS` and merge hard gate.
- Closure path: model worker completes branch → separate assigned reviewer reads branch/diff and submits evidence/critique → non-clean review reactivates completed mission and prevents merge → main tower routes findings to original/replacement worker → changed branch must be re-reviewed at its new tip → clean verdict enables merge.
- Boundary reachability: reviewer spawning and review/merge tools are bundled within the same first-party TowerFeature; `TowerStore.submitReview` checks reviewer assignment and `TowerStore.merge` rejects absent/non-clean/stale review before git integration.
- Why this is / is not agent-owned: the reviewer model decides semantic defect severity and claims, while the store merely enforces that a recorded `clean` review from assigned actor is fresh. Removing reviewer discretion leaves no comparable real source-specific quality judgment, even though deterministic gate persists.
- Evidence: [`packages/agent-core-v2/src/features/tower/tools/spawn/spawn.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/spawn/spawn.md); [`packages/agent-core-v2/src/features/tower/tools/review/review.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/review/review.md); [`packages/agent-core-v2/src/features/tower/tools/review/reviewTool.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/review/reviewTool.ts); [`packages/agent-core-v2/src/features/tower/protocol/store.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/protocol/store.ts); [`packages/agent-core-v2/src/features/tower/tools/merge/mergeTool.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/tools/merge/mergeTool.ts).
- Basis: explicit + structural
- Confidence: medium-high (for enabled Tower mode)
- Caveats: the source verifies a reviewer identity and a submitted verdict, not the accuracy of all reviewer claims. Tower itself can also submit a review; this positive independent-actor claim refers specifically to first-party assigned reviewer-subagent mode rather than self-review by tower. It does not imply external organizational independent-review gate.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct shipped prospective outside-environment sensing → future capability options → adoption into current organizational capability has been established for the assessed organization.
- Disturbance / variety regulated: future tool/method changes, emerging project needs and external constraints, beyond the present operator-authored coding mission.
- Decisive decision or feedback right: agents can research a present coding task, the operator can configure providers, plugins and future goals, but no first-party S4 owner of system-level prospective adaptation choice is identified.
- Decision owner: no qualifying S4-specific decision owner on the inspected first-party standard path.
- Supporting / enforcement mechanisms: goal mode, cron, sessions/compaction, user/project skills, plugins, external web tools and long-running task loops.
- Closure path: task information affects current coding actions or a user-supplied later goal; no separate outside/future options/adoption decision circuit is demonstrated as a system-owned return to current Tower management.
- Why this is / is not agent-owned: sustained task execution and session memory are still S1/current task support. Goal deadlines and timers do not choose a prospectively adaptive capability portfolio.
- Evidence: [`packages/agent-core-v2/src/features/goal/goalOps.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/goal/goalOps.ts); [`packages/agent-core-v2/src/features/goal/goalDeadlineScheduler.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/goal/goalDeadlineScheduler.ts); [`packages/agent-core-v2/src/features/skill/skillOps.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/skill/skillOps.ts); [`packages/agent-core-v2/src/agent/contextMemory/contextMemory.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/agent/contextMemory/contextMemory.ts); [`README.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/README.md).
- Basis: structural
- Confidence: medium
- Caveats: this is a bounded absence for the first-party shipped modes, not universal impossibility of future/externally constructed adaptive arrangements.

### Absence scope

- Surfaces inspected: agent loop, goals/deadlines, skill discovery, plugins, context memory, Tower plan/mission controls and README.
- Plausible first-party paths checked: task research vs future-environment analysis, operator-provided standing goals, automatic adaptation of role capabilities, organization-level prospective option creation/adoption, and return to ongoing metasystem authority.
- Why no material first-party path remains: inspected modes plan/execute current user-supplied coding work and optionally load new user-configured tools, but do not own a distinct external-future adaptation-selection feedback circuit with organizational capability return.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime constitutional identity or ultimate-purpose dispute → legitimate authority decision → returned ongoing policy-governance loop is established.
- Disturbance / variety regulated: dangerous commands, permission policies, privacy and user-requested objectives can create authorization problems but do not necessarily concern ultimate mission/identity.
- Decisive decision or feedback right: operator/permission policy approves or blocks actions; Tower lead can change mission scope or abandon one, not authoritatively redefine the organization's ultimate purpose/identity under a legitimate parent resolution.
- Decision owner: user and local tool-permission policy for individual actions; none identified for a first-party S5-specific ultimate identity decision/return.
- Supporting / enforcement mechanisms: tool approval, permission modes, model instructions, project-scoped tools/skills, Tower ownership limits and safety prompts.
- Closure path: permission decisions affect tool execution and Tower decisions affect work planning, but no actual identity-level issue has a first-party legitimate authority and returned constitutional rule governing later operation.
- Why this is / is not agent-owned: the presence of human confirmation or authorized Tower lead discretion does not transfer constitutional policy rights to the model or a deterministic gate.
- Evidence: [`packages/agent-core-v2/src/agent/permissionPolicy/permissionPolicy.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/agent/permissionPolicy/permissionPolicy.ts); [`packages/agent-core-v2/src/agent/interaction/approval.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/agent/interaction/approval.ts); [`packages/agent-core-v2/src/features/tower/protocol/store.ts`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/packages/agent-core-v2/src/features/tower/protocol/store.ts); [`README.md`](https://github.com/PyModel/pythinker-code/blob/5c5a2053116c1e18c7e1e22710d846fc27945f08/README.md).
- Basis: structural
- Confidence: medium-high
- Caveats: developer/maintainer governance and an operator's longer-lived project policies belong to an external organizational boundary.

### Absence scope

- Surfaces inspected: user/tool permission rules, approve/ask modes, Tower mission/branch permissions, goals, project instruction skills and external contributor governance.
- Plausible first-party paths checked: policy change vs tool authorization, human/Tower escalation, durable ultimate-mission identity adjudication and returned cross-operations constitutional governance.
- Why no material first-party path remains: decisions concern operational permission and bounded user task priorities, not a material first-party identity-policy issue resolved by legitimate ultimate authority and fed back into subsequent organizational governance.

## Distributed OSS parent arrangement

The public GitHub organization/maintainers own the upstream product, not a combined first-party parent supervising a consumer's live Pythinker installation. Separate user projects or editors using ACP do not thereby share ultimate identity authority.

## Self-hosted and non-human modes

The shipped coding agent is locally installed, can use configured inference providers and run in terminal/desktop/editor or headless contexts. Tool approvals are operator governed. The experimental Tower feature can be independently enabled and provides agent-owned S1/S3/S3* and constructor S2, but this is not a parent `(P)` state; no `A(P)`/`C(P)` is asserted.

## Recursion

Tower has several autonomous coding units and a real current-management/audit level. A forked Agent alone does not form a nested viable system; a complete recursively viable metasystem for each branch/mission is not demonstrated at the pinned source.

## Variety and escalation

The main/child model and tool feedback absorb coding variety. Tower's scope/worktree/merge rules attenuate inter-worker conflict; review audits produce a distinct challenge and enforce held merges until corrected. Permission escalation governs tool safety, while missed review/blocked mission is ordinary corrective work signaling, not automatically a separate algedonic function or S5 matter.

## Evidence gaps

- Tower experimental default is **off**; every S2/S3/S3* positive finding is mode-scoped to the first-party enabled feature. The source does not prove default customer use or empirical efficacy.
- Reviewer findings are self-reported by a distinct model; the store enforces reviewer assignment, freshness, scope and status, not substantive correctness of the LLM reviewer. Independent execution benchmarking or human audit is not included.
- S2 conflict prevention is bounded by declared scopes, concrete git integration and returned conflicts; no universal glob-collision completeness guarantee or autonomous worker-to-worker bargaining is claimed.
- This is source-first static assessment on exactly the pinned commit; no model-backed task evaluation was performed here.
