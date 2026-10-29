---
harness_id: opencode-orchestrator
project_name: OpenCode Orchestrator
repository: https://github.com/agnusdei1207/opencode-orchestrator
review_ref: fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OpenCode Orchestrator

## Review boundary

- System in focus: an installed OpenCode 2 plugin managing one project's continuing task mission, Commander model, optional Planner/Worker/Reviewer model sessions and durable verification/mission state.
- Purpose and identity: maintain authorized goal continuity and verify concrete source changes across turns without losing delegated task progress.
- Relevant environment: evolving user request, actual code/test state, interrupted sessions, unfinished mission leaves, concurrency and delegate failures, reviewer findings, tool/provider limits.
- Standard distribution: shipped npm OpenCode plugin entry and registered Commander, optional subagents, delegate_task tools, mission ledger/TODO/verification and persistence hooks; Rust CLI utilities are supportive.
- Credited operating / distribution surfaces: active Commander OpenCode model choices, supported model-backed Worker implementation, mission-wide delegation/replanning authority and separately invoked Reviewer source verification.
- Adjacent first-party surfaces excluded from ownership: repository maintainer governance, npm release process, user-supplied external agents, third-party OpenCode model internals, tests/demos and marketing.
- First-party operating modes considered: ordinary Commander implementation, explicit /task continuing mission, optional Planner/Worker/Reviewer delegation and concurrent worker mode, deterministic mission continuation/verification, human stop/replacement.
- Recursion level: one project mission with task-producing S1 roles and a Commander supervising the whole mission. Subagents alone are not complete viable systems.
- Reviewed revision: agnusdei1207/opencode-orchestrator@fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2, exact local first-party checkout, MIT LICENSE.
- Observation date: 2026-10-29, active Profile 0.2.4 / released Methodology 0.3.7.

## Repository architecture

Commander is a normal model-backed OpenCode agent that may implement directly, create a plan or delegate bounded implementation to Worker, and request a separate Reviewer. It must track its mission TODO, actual tests, dependencies, unfinished work, verification and next steps. Parallel task tools preserve separate session identities and results; run/complete checks guard against equating idle status with verified task output. Deterministic mission-loop hooks inspect completion/checklists and request continuation; they are enforcement, not an autonomous model executive. Sources: https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/commander.ts, https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/prompts/common.ts, https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/tools/parallel/delegate-task.ts, https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/core/loop/mission-loop-handler.ts.

A separate Reviewer role is instructed to inspect assigned results and actual affected interfaces, rerun project checks, and report failures/untested areas into TODO and sync-issues so Commander can repair. This is an optional complementary audit route, not a guarantee of external reviewer independence. Shared task queue and concurrency limits do not by themselves show a concrete collision and corrective inter-S1 feedback loop; cross-task scope assignment is primarily Commander control. Sources: https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/subagents/reviewer.ts, https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/core/loop/verification.ts, https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/core/agents/manager.ts.

## Operational model

Active Commander or Worker model chooses source-specific work. In a mission, Commander observes all delegated tasks, task results, TODO status and verification, and chooses re-plan, new scoped delegation or direct repair to meet the whole user goal. Optional Reviewer checks actual source/test evidence separately. Configured concurrency, task store, loop persistence and guardrails enforce or transport these choices. No source-backed future external-environment adaptation or ultimate policy tribunal is credited.

## S1 — Operations

- State: A
- Function: perform code, test and project changes using an actual OpenCode backend agent.
- Disturbance / variety regulated: changing source, ambiguous instructions, failing tests and tool feedback.
- Decisive decision or feedback right: select which files to inspect/edit, what tests to run and what fix satisfies the task.
- Decision owner: model-backed Commander working directly or separately invoked Worker; plugin only routes tools.
- Supporting / enforcement mechanisms: OpenCode host, tool adapters, session registry, mission memory and verification checklist.
- Closure path: user task → Commander/Worker model tool actions → code/tests/evidence → reviewed mission result.
- Why this is / is not agent-owned: removing the model leaves prompt/routing code but no task-specific implementation choice.
- Evidence: https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/commander.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/subagents/worker.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/tools/parallel/delegate-task.ts
- Basis: shipped model agent definitions and runtime delegation path.
- Confidence: high for supported mode; provider performance unmeasured.
- Caveats: standalone question-only runs do not exhibit a coding operational cell.
- Boundary reachability: published OpenCode 2 plugin adds Commander; Worker is a supported optional delegate.

## S2 — Coordination

- State: —
- Function: no concrete first-party cross-operational conflict resolution circuit was established for parallel workers.
- Disturbance / variety regulated: independent worker file edits or interface changes may be incompatible when merged.
- Decisive decision or feedback right: Commander assigns scopes/dependencies and can review results; no specific inter-S1 clash signal/repair relation shown.
- Decision owner: Commander for current task delegation rather than a demonstrated S2-specific conflict decision.
- Supporting / enforcement mechanisms: parallel task manager, agentConcurrency, task result tool, scoped worker prompts and session IDs.
- Closure path: workers report results to Commander but a collision-specific balancing signal and returned repair are not evidenced.
- Why this is / is not agent-owned: file ownership guidance and queue limits prevent some overlap but delegation alone is not specific inter-S1 oscillation regulation.
- Evidence: https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/commander.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/core/agents/manager.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/tools/parallel/delegate-task.ts
- Basis: bounded negative on parallel task lifecycle and Commander scope/dep guidance.
- Confidence: medium; a real Commander could notice conflicts not proven as a repeatable shipped circuit.
- Caveats: S3 whole-mission corrective work and S3* Reviewer findings are not automatically S2.

### Absence scope

- Surfaces inspected: parallel launcher, session/task result store, agentConcurrency, Worker scope and Commander dependency instructions
- Plausible first-party paths checked: file ownership, sequential dependent work, optional reviewer, task result pickup
- Why no material first-party path remains: no concrete source-level inter-S1 interference and correction return was established beyond generic task delegation and review.

## S3 — Inside-and-now control

- State: A
- Function: direct a whole currently active project mission, allocate scoped model work and intervene when delegated commitments or verification stall.
- Disturbance / variety regulated: unfinished TODO leaves, dependencies, failed delegates, stagnant iterations and incomplete verification of overall goal.
- Decisive decision or feedback right: Commander selects task decomposition, model delegation, dependency ordering, replanning, repair or final acceptance.
- Decision owner: model-backed Commander with whole-mission goal and result view, not the mission-loop continuation hook.
- Supporting / enforcement mechanisms: mission TODO/status/sync issues, parallel task list/results, progress/stagnation guard, checklist and durable ledger.
- Closure path: whole mission evidence and delegated status → Commander reassigns/replans or repairs → worker next action and updated TODO/verified completion.
- Why this is / is not agent-owned: the model chooses revised work and scope; deterministic retry/verification cannot produce design-specific corrective decisions.
- Evidence: https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/commander.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/core/loop/mission-loop-handler.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/prompts/common.ts
- Basis: first-party model role and continuing mission control feedback.
- Confidence: medium-high for selected active mission mode.
- Caveats: a trivial question or single direct edit has no multi-cell S3 demonstrated; budget/loop enforcement alone is not ownership.
- Whole-system current view: Commander sees entire user goal, all mission TODO leaves, child task status/results and aggregate verification requirements.
- Current-control decision scope: assign Workers/Planner/Reviewer, choose serial dependency order, take over blocked work, re-plan and decide evidence-backed completion.
- Boundary reachability: normal Commander and /task mode with optional delegate_task, task-list and result tools.

## S3* — Complementary audit

- State: A
- Function: independently challenge a Worker/Commander completion claim by checking actual project files and tests.
- Disturbance / variety regulated: false success, broken interface contracts, untested regressions and incomplete TODO verification.
- Decisive decision or feedback right: dedicated Reviewer model decides which checks to rerun and what findings block completion.
- Decision owner: fresh role-specific Reviewer agent, not original implementer or deterministic checklist parser.
- Supporting / enforcement mechanisms: Reviewer prompt and scope, actual source/tests, mission checklist, sync-issues and returned task result.
- Closure path: implementation result → Reviewer source/test checks → evidenced pass/fail/uncovered area → Commander repair or verified TODO completion.
- Why this is / is not agent-owned: Reviewer makes code-specific fault judgments rather than only checking a manifest flag.
- Evidence: https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/subagents/reviewer.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/prompts/common.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/core/loop/verification.ts
- Basis: supported optional role-separated reviewer and executable evidence-return contract.
- Confidence: medium-high for configured review; no paid model E2E validation.
- Caveats: optional delegation, possibly same provider and no external institutional independence.
- Claim being audited: Worker or Commander claims an implementation is complete and matches acceptance checks.
- Ordinary reporting path: implementer result, task status and self-reported tests.
- Complementary access path: separate Reviewer reads actual affected files, interfaces and executes project checks independently.
- Independence boundary: distinct Reviewer invocation and independent direct source/tests, not a separate organization.
- Who acts on findings: Commander updates scope or repairs; Reviewer may mark only verified assigned checklist leaves and log integration issues.
- Boundary reachability: published plugin optional Reviewer subagent available via delegate_task.

## S4 — Outside-and-then intelligence

- State: —
- Function: no future external-environment adaptation loop into mission capability control was proven.
- Disturbance / variety regulated: provider changes, future market/user requirements and long-term technical alternatives.
- Decisive decision or feedback right: Planner and Commander choose current technical steps, not enduring environmental adaptation options.
- Decision owner: user/project leadership for long-horizon adaptation outside plugin.
- Supporting / enforcement mechanisms: Planner, mission memory, persistent TODO and model tools.
- Closure path: current planning updates task implementation but no external future options negotiation with S3 is evidenced.
- Why this is / is not agent-owned: an implementation plan or research tool call alone is not future-facing S4.
- Evidence: https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/subagents/planner.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/core/knowledge/mission-memory.ts
- Basis: negative path review of Planner, mission continuation and memory.
- Confidence: medium-high at package boundary.
- Caveats: a user can prompt strategic research, which does not demonstrate shipped S4 governance.

### Absence scope

- Surfaces inspected: Planner, mission memory, TODO, model backends, session continuation and verification
- Plausible first-party paths checked: planning, remembered lessons, user-driven research and re-planning
- Why no material first-party path remains: all inspected loops address present mission execution without external prospective adaptation options and returned S3 capability change.

## S5 — Policy and identity

- State: —
- Function: no legitimate identity-level policy decision loop is wired into the packaged OpenCode mission plugin.
- Disturbance / variety regulated: user permission, mission replacement, project policy and final action boundaries.
- Decisive decision or feedback right: human sets goals, stops or replaces missions, and approves operations as needed.
- Decision owner: user/deployment parent for policy; plugin only enforces selected task permissions and state.
- Supporting / enforcement mechanisms: stop/cancel commands, prompts, bounded concurrency, session replacement and verification gates.
- Closure path: human can cancel or redirect a mission, but an identity-level exception is not routed to ultimate authority and returned as governance.
- Why this is / is not agent-owned: system prompt constraints and user approvals over coding steps are not S5 identity closure.
- Evidence: https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/agents/commander.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/src/core/loop/mission-loop.ts; https://github.com/agnusdei1207/opencode-orchestrator/blob/fdba1b1eea1e78d27aa733a421beaa61ad0bb8a2/README.md
- Basis: bounded negative across commands, safety, mission replacement, prompts and user rights.
- Confidence: medium-high for installed plugin.
- Caveats: maintainer governance or an external company policy engine is outside the system-in-focus.

### Absence scope

- Surfaces inspected: Commander instructions, human /task and /stop, session authority, mission replacement and verification
- Plausible first-party paths checked: operator stop/approval, policy-like agent prompt and issue escalation
- Why no material first-party path remains: no observed identity-level matter with legitimate final authority and returned ruling into subsequent project operations.

## Distributed OSS parent arrangement

Public maintainers develop the plugin; they are not the deployed mission's first-party policy parent. No S4/S5 parent-mode function is borrowed from project release governance.

## Self-hosted and non-human modes

OpenCode model-backed Commander and optional Worker/Reviewer supply the credited A decisions; deterministic loops, Rust tools and queues support those choices. In direct Commander-only mode, distinct delegated S1 cells and independent Reviewer may be absent; positives are selected available modes.

## Recursion

A Worker is bounded by one task and may report back to Commander; it does not automatically include its own S2/S3/S4/S5. The mission is the evaluated recursion for Commander S3, with source-verifying Reviewer as a complementary role.

## Variety and escalation

Mission TODO, checklist, stagnation counts and child session results compress current failures; Commander chooses a revised plan or exact blocker. Reviewer returns independent source/test findings for repair. User stop and scope change govern authorized execution but are not automatically S5.

## Evidence gaps

- No paid external OpenCode provider run. Source and first-party tests establish supported closure, not empirical reliability.
- S3 and S3* claims require the active mission and optional role invocation, respectively; neither is forced on ordinary chat.
- File-scope instructions and concurrency caps are not scored S2 without a concrete inter-S1 interference correction witness.
- Current re-planning, memory, and human mission authorization do not establish S4 future intelligence or S5 identity governance.
