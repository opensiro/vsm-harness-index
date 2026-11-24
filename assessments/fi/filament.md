---
harness_id: filament
project_name: Filament
repository: https://github.com/invertibleMatrix/filament
review_ref: 90cf0c20f3fd2d55a73994963427f2fd2532b970
reviewed_at: 2026-11-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: —
---

# Filament

## Review boundary

- System in focus: one Filament coding session with its graph, delegated workers and beside-team audit, within the installed application.
- Purpose and identity: accomplish the developer's repository work with model-backed coding agents, shared project memory and managed task outcomes.
- Relevant environment: repository/files, developer, models/providers, tools and external events.
- Standard-distribution boundary: shipped loop, task graph, registry, teams, workspace modes, memory and owner UI/API; model services and arbitrary custom extensions excluded.
- Credited operating / distribution surfaces: own agent loop; task graph with isolated workers; model planner and developer graph controls; shipped BugHunters and configured automatic result delivery.
- Adjacent first-party surfaces excluded from ownership: maintainer/release organization, marketing claims, tests as substitutes for runtime, unrelated sessions and device fleet.
- First-party operating / deployment modes considered: agent-led task graph, developer side-run/stop/retry, read-only beside-team with result delivery, optional routines/watchers and memory curator.
- Recursion level: one session and its subordinate work organization, not all independent sessions across a fleet.
- Reviewed revision: 90cf0c20f3fd2d55a73994963427f2fd2532b970.
- Observation date: 2026-11-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The own-agent loop executes a model's tool choices and returns tool results. The persistent task graph records dependencies, writes, worker assignments, reviews, merge state and reported outcomes. Workers may execute in isolated patch/worktree or explicitly shared folder; the graph runner dispatches tasks, returns results and runs checked merges. Separate beside-teams operate in their own chat; the shipped BugHunters can check claims against current code. The owner can intervene from the Plan UI. Memory curates project observations and owner rules, and event-driven routines may deliver guidance. See [docs/architecture/app-agent.md](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/docs/architecture/app-agent.md), [docs/architecture/core.md](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/docs/architecture/core.md), [docs/architecture/services.md](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/docs/architecture/services.md).

## Operational model

The session planner and actual model workers each perform repository operations. The planner allocates dependencies, delegated work, and integration; deterministic graph machinery enforces those choices and reports outcomes. The developer has a separate live graph intervention route. An optional beside-team provides a complementary checking route outside the ordinary worker report.

## S1 — Operations

- State: A
- Function: execute coding work through model-selected tools and iterative observation.
- Disturbance / variety regulated: uncertain repository state, task and tool failures.
- Decisive decision or feedback right: choose actions and adapt subsequent action to results.
- Decision owner: own coding model and delegated model workers.
- Supporting / enforcement mechanisms: agent loop, tool gating, provider execution and tool result handling.
- Closure path: model calls produce tool actions; results enter subsequent model rounds and final task output.
- Boundary reachability: native installed agent loop, not a hypothetical external composition.
- Why this is / is not agent-owned: code executes and gates tools but the model selects discretionary coding actions.
- Evidence: [src/app/agent/loop.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/loop.js#L554-L590), [src/app/agent/loop.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/loop.js#L2450-L2452), [src/app/agent/loop.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/loop.js#L3480-L3505), [src/app/agent/graph-runner.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/graph-runner.js#L911-L926)
- Basis: explicit/structural
- Confidence: high
- Caveats: model/provider credentials and permissions needed; no live call performed.

## S2 — Coordination

- State: A
- Function: attenuate conflicting writes and conflicting task dependencies among independently executing workers.
- Disturbance / variety regulated: concurrently open tasks with overlapping forecast paths or actual overlapping changes.
- Decisive decision or feedback right: planner chooses task needs, writes, worker mode and subsequent conflict response/landing.
- Decision owner: model planner; deterministic runtime computes overlaps and enforces workspace/merge handling.
- Supporting / enforcement mechanisms: graph meetings, workspace modes, task dispatch, serialized checked merges and bounded rework.
- Closure path: overlapping paths are reported to planner, workers execute isolated or sequenced, overlapping changes return for rework or resolution, outcomes wake planner and alter next graph decisions.
- Boundary reachability: first-party tasks tool, graph runner, shipped workspace implementation.
- Why this is / is not agent-owned: planner can change needs and tasks in response to graph information; mechanical isolation alone would not establish A.
- Evidence: [src/core/task-graph.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/core/task-graph.js#L1520-L1605), [src/app/agent/tools.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/tools.js#L161-L204), [src/app/agent/workspace-kind.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/workspace-kind.js#L39-L61), [src/app/agent/graph-runner.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/graph-runner.js#L1182-L1254), [src/app/agent/graph-runner.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/graph-runner.js#L1640-L1665)
- Basis: explicit/structural
- Confidence: high
- Caveats: declared paths are forecasts, not strict locks; shared folder mode can interfere; no universal collision prevention claim.

- Distinct S1 units: separate running model coding workers and planner's own coding work.
- Inter-S1 disturbance: simultaneous independent tasks can write the same files or produce overlapping changes.
- Attenuating coordination relation: dependency choices, overlap feedback and separate workspace with serialized integration/rework.
- Feedback into subsequent S1 behaviour: workers receive rework after conflict and planner receives graph/merge outcome to adjust tasks.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: concrete shared-write interference is identified, returned and handled.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current commitments and worker allocations across the session graph.
- Disturbance / variety regulated: failed/stopped work, limited slots, dependencies and integration failures.
- Decisive decision or feedback right: change/drop/start tasks, allocate worker roles and approve/redirect integration; owner may independently stop/restart and assign side runs.
- Decision owner: model planner or authorized developer in parent mode.
- Supporting / enforcement mechanisms: persisted graph, graph view, job dispatcher, slot constraints, merge/check and wake events.
- Closure path: planner reads graph, changes commitments through tasks/apply, dispatch/merge executes, outcomes are persisted and returned; developer side-run or send-back changes graph and informs planner.
- Boundary reachability: shipped session tools and developer Plan/API controls use the same graph runner.
- Why this is / is not agent-owned: planner decides current work allocation rather than just follows a fixed queue; parent may exercise real allocation/intervention rights.
- Evidence: [src/app/agent/tools.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/tools.js#L161-L204), [src/app/agent/graph-runner.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/graph-runner.js#L660-L675), [src/app/agent/graph-runner.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/graph-runner.js#L829-L943), [src/app/agent/graph-runner.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/graph-runner.js#L1640-L1665), [src/app/agent/graph-runner.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/graph-runner.js#L1856-L1912), [src/app/agent/graph-runner.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/graph-runner.js#L2021-L2029), [src/http/admin/sessions.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/http/admin/sessions.js#L1148-L1224)
- Basis: explicit/structural
- Confidence: high
- Caveats: scope is session graph, not all daemon projects; owner gates can restrict model authority.

- Whole-system current view: persisted session graph, running/waiting/review/merge states, dependencies and outcome feedback.
- Current-control decision scope: choose current work allocation, modify or drop commitments, start/retry delegated work, decide whether to integrate changes.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Session model planner | Graph state and worker outcomes | tasks/apply choices change graph and dispatch; feedback returns | graph-runner.js 660-675, 1640-1665, 2021-2029 |
| Parent (`P`) | Authorized developer | Failed/stopped tasks or desired side allocation | send-back/side-run alters graph and sends notice to planner | graph-runner.js 1856-1912; admin/sessions.js 1148-1224 |

## S3* — Complementary audit

- State: A
- Function: independently challenge claims against code and return findings outside the producing worker's ordinary report.
- Disturbance / variety regulated: incomplete or inaccurate claims of completed coding work.
- Decisive decision or feedback right: separate BugHunters lead/workers select evidence and judge claims; originating model can commission a bug hunt/check, with configured result delivery.
- Decision owner: separate model-backed audit team; authorized owner configures delivery and available teams.
- Supporting / enforcement mechanisms: beside-team isolation, scoped Git change views, read-only claim verification prompt, automatic notification, distinct review worker with diff.
- Closure path: main model sends authorized BugHunters; independent team reads actual code and produces findings; enabled notify returns result to main chat. Separate optional graph review also consumes raw changes and returns requested corrections.
- Boundary reachability: shipped team tool, BugHunters, beside-team execution and notify configuration; no custom auditor required.
- Why this is / is not agent-owned: checking model chooses evidence and verdict independently of producing worker; deterministic delivery and owner configuration do not decide findings.
- Evidence: [src/app/agent/beside-tool.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/beside-tool.js#L1-L40), [src/core/beside.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/core/beside.js#L178-L195), [src/app/teams-beside.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/teams-beside.js#L501-L568), [src/app/teams-beside.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/teams-beside.js#L620-L700), [src/app/teams-beside.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/teams-beside.js#L746-L815), [src/app/agent/graph-runner.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/graph-runner.js#L1122-L1170), [src/core/task-graph.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/core/task-graph.js#L5617-L5648)
- Basis: explicit/structural
- Confidence: medium
- Caveats: enabled team and notification mode required for autonomous return; same model family possible; no claim of mandatory audits or empirically measured independence. Routine task check alone is not credited.

- Claim being audited: earlier coding findings or asserted changes relative to repository evidence.
- Ordinary reporting path: worker/task report and session outcome.
- Complementary access path: separate BugHunters claim check against current code and scoped changes rather than accepting report.
- Independence boundary: distinct beside-team chat and read-only role; team chooses evidence and verdict without producer setting it.
- Who acts on findings: main session receives notification and can revise tasks; developer can also inspect and send findings.

## S4 — Outside-and-then intelligence

- State: ?
- Function: prospective environmental modeling and adaptation at session-work-organization boundary not established.
- Disturbance / variety regulated: changing external conditions and future capability needs.
- Decisive decision or feedback right: unresolved whether a shipped configuration supplies prospective option-generation and returned adaptation decisions beyond generic watcher guidance.
- Decision owner: not established.
- Supporting / enforcement mechanisms: event routines, watcher guidance delivery, cross-session memory curator and configurable tools.
- Closure path: watcher can deliver a note or wake a chat; curator proposes grounded rules for owner approval. Neither examined path itself demonstrates an explicit prospective adaptation decision and return to current control.
- Why this is / is not agent-owned: event reaction, internal learning and general agent discretion alone do not prove S4. The configurable external-event/agent guidance path merits further targeted examination.
- Evidence: [src/app/routines.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/routines.js#L326-L354), [src/app/watchers/guidance.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/watchers/guidance.js#L1-L22), [src/services/memory/curator.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/services/memory/curator.js#L1498-L1516), [src/services/memory/curator.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/services/memory/curator.js#L1561-L1604)
- Basis: structural
- Confidence: medium
- Caveats: unknown rather than absence because optional watcher composition is materially plausible but its S4-specific closure was not established.

## S5 — Policy and identity

- State: —
- Function: no demonstrated identity-level or ultimate-policy arbitration at the assessed session boundary.
- Disturbance / variety regulated: potential disputes over purpose or ultimate policy rather than local instructions.
- Decisive decision or feedback right: no first-party ultimate-policy issue resolution established.
- Decision owner: developer sets task goals, permissions and project rules; not shown as S5 arbitration.
- Supporting / enforcement mechanisms: memory rule proposals, owner confirmation, tool permission rules and task goal.
- Closure path: user can accept learned project rules that affect later work; no demonstrated route escalating ultimate-policy conflict to identity authority and returning that resolution.
- Why this is / is not agent-owned: ordinary project instruction learning, tool permission decisions and task goals are not ultimate policy.
- Evidence: [src/services/memory/curator.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/services/memory/curator.js#L1498-L1516), [src/services/memory/curator.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/services/memory/curator.js#L1561-L1604), [src/http/admin/memory.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/http/admin/memory.js#L420-L436), [src/app/agent/rules.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/rules.js), [src/app/agent/tools.js](https://github.com/invertibleMatrix/filament/blob/90cf0c20f3fd2d55a73994963427f2fd2532b970/src/app/agent/tools.js#L161-L204)
- Basis: structural
- Confidence: medium
- Caveats: external maintainer or business identity governance outside boundary.

### Absence scope

- Surfaces inspected: session task tools, owner control, memory curator's rule adoption, permission rules and memory admin endpoints.
- Plausible first-party paths checked: goal editing, persistent project rules, correction/adoption, permission confirmation and owner intervention.
- Why no material first-party path remains: examined paths govern local commitments, permissions or learned instructions, not resolution of ultimate identity/policy conflict.

## Recursion

A session's workers are operational units with delegated tasks and distinct contexts/workspaces. No full viability vector inferred for every child or across daemon fleet.

## Variety and escalation

Graph dependency and overlap feedback, checked merge, rework, permission gates and owner intervention attenuate operational disturbances. No separate algedonic channel inferred.

## Evidence gaps

Static source review at frozen revision. No live model/provider execution or independent semantic audit. S4 retained as unknown pending a targeted prospective watcher/adaptation trace. No inference of daemon-wide authority from session-level closure.
