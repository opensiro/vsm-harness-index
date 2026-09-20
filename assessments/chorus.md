---
harness_id: chorus
project_name: Chorus
repository: https://github.com/Chorus-AIDLC/Chorus
review_ref: 148b7928b99773f7fbdf61080940bd6995b06934
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Chorus

## Review boundary

- System in focus: one Chorus AI-DLC project using first-party project/idea/proposal/task state, agent permissions, plugin skills, daemon/session dispatch, worker/reviewer spawning protocol, acceptance criteria, comments/verdicts, and the shipped full-auto `$yolo` orchestration path.
- Purpose and identity: coordinate a team of autonomous coding agents plus optional human participants from idea and proposal through task execution, independent verification, rework, and completion.
- Relevant environment: user product intent, target source repository and project rules, coding-agent/model runtimes, test/build results, task/proposal artifacts, failures and review findings.
- Standard-distribution boundary: first-party Chorus server/state/API/MCP surfaces, shipped Chorus plugin/skills and reviewer definitions, daemon/session lifecycle, permissions, and standard agent integrations. Claude Code, Codex, Kiro, OpenClaw, Pi, dsh and model providers are external execution substrates; they are not credited for organizational functions that Chorus does not first-party structure and close.
- Credited operating / distribution surfaces: AI-DLC project state and task DAG, `$yolo` and related proposal/develop/review skills, first-party proposal/task reviewer definitions, Chorus MCP state transitions and admin operations, agent permissions, daemon/session wake/dispatch and persisted project/task/comment state.
- Adjacent first-party surfaces excluded from ownership: Chorus contributor/CI/release machinery, OpenSpec change archives as development history, tests/examples, website/landing presentation, and repository-development governance not participating in a running Chorus project.
- First-party operating / deployment modes considered: supported agent-driven Chorus operation including the shipped `$yolo` full-auto mode and standard plugin-driven proposal/develop/review flows; human interaction was inspected only for possible parent ownership and is not inferred from a permission or approval hook alone.
- Recursion level: one Chorus project as the viable system; autonomous task-development sessions are the principal S1 operational units, with the orchestrating agent acting across the project.
- Reviewed revision: `148b7928b99773f7fbdf61080940bd6995b06934`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Chorus describes itself as a harness one level above coding-agent harnesses: it persists Ideas, Proposals, Documents and Tasks, exposes fine-grained permissions, tracks sessions and task state, and connects external coding-agent runtimes into one AI-DLC pipeline. The shipped `$yolo` skill provides an autonomous end-to-end operating mode. It creates/chooses a project, creates and elaborates an Idea, creates and validates a Proposal with a task DAG, runs an independent proposal-review loop, approves the proposal, dispatches dependency-ready tasks in waves to worker agents, independently reviews each submitted task, reopens failed tasks and continues until work is complete or escalation is required.

The decisive project-control and audit rights are model-driven in `$yolo`; Chorus state and MCP operations enforce those decisions. Proposal and task reviewers are deliberately separate, read-only adversarial roles. Their verdicts are persisted as comments, and the orchestrator must read the current round's verdict before advancing. A proposal FAIL causes reject/revise/resubmit; a task FAIL causes reopen/rework. This provides a complementary audit path with explicit return into subsequent operation.

Primary evidence:

- [`README.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/README.md) — project boundary, AI-DLC stages, permissions, agent integrations, task/session lifecycle and human/agent operating model.
- [`plugins/chorus/skills/yolo/SKILL.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/yolo/SKILL.md) — complete autonomous project workflow, proposal review loop, dependency-wave dispatch, task review/reopen loop and escalation behavior.
- [`plugins/chorus/skills/chorus-proposal-reviewer/SKILL.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/chorus-proposal-reviewer/SKILL.md) — read-only adversarial proposal reviewer and structured verdict contract.
- [`plugins/chorus/skills/chorus-task-reviewer/SKILL.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/chorus-task-reviewer/SKILL.md) — independent implementation/AC/test review and read-only evidence access.
- [`docs/DAEMON.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/docs/DAEMON.md) — first-party daemon path that wakes configured coding agents on dispatched work.

## Operational model

Task workers autonomously perform bounded software-engineering work under Chorus task/proposal context and return implementation evidence for verification. The `$yolo` orchestrator holds the project-level current-control role: it inspects task readiness and status, selects dependency-ready work, starts worker waves, waits for results, interprets review outcomes, reopens failed work and decides whether the project can advance or must escalate. Deterministic task states, permissions and API transitions support this loop but do not own the project-level discretion.

Review is separated from production. A task reviewer receives task acceptance criteria, proposal documents, project constraints and the implementation filesystem/test surface with read-only permissions; it independently posts a structured verdict. The orchestrator then changes task state and subsequent work based on that verdict.

## S1 — Operations

- State: A
- Function: autonomously implement bounded Chorus tasks and produce software changes/evidence under the task's acceptance criteria and project context.
- Disturbance / variety regulated: repository state, implementation choices, failures, tests, project constraints and task-specific ambiguity encountered while completing assigned work.
- Decisive decision or feedback right: choose substantive coding/tool/debugging actions needed to satisfy an assigned task and decide when work is ready to submit for verification.
- Decision owner: the autonomous task worker agent launched under the shipped Chorus develop/worker protocol.
- Supporting / enforcement mechanisms: task/proposal state, acceptance criteria, permissions, session/daemon dispatch, agent integration adapters, Chorus MCP tools and persisted work reports.
- Closure path: orchestrator dispatches an unblocked task → worker reads Chorus context and executes autonomously in the target repository → worker reports work/self-check and submits for verification → resulting state/evidence returns to Chorus for audit/control.
- Boundary reachability: Chorus ships the worker/develop skill contracts and supported adapters/daemon paths that launch autonomous coding-agent sessions as the standard operating surface; the external coding harness supplies execution capabilities but the Chorus project/task contract and return path are first-party.
- Why this is / is not agent-owned: the task contract constrains scope, while the running worker agent chooses the substantive implementation sequence and tool actions rather than Chorus deterministically prescribing them.
- Evidence: [`README.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/README.md), [`$yolo` task execution](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/yolo/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: S1 autonomy is credited to the running task-agent role reachable through Chorus's first-party integration surfaces, not to deterministic task-state machinery or to undocumented behavior of any particular external coding harness.

## S2 — Coordination

- State: —
- Function: no material S2-specific regulation of a demonstrated interference/oscillation among distinct S1 workers is established at the declared project recursion.
- Disturbance / variety regulated: not established as an S2 disturbance.
- Decisive decision or feedback right: not established as S2.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: task DAG dependencies, unblocked-task queries, dependency-ordered waves, project/task state, comments and worker isolation organize and sequence work but do not by themselves establish an inter-S1 conflict/oscillation witness.
- Closure path: dependency completion changes which tasks become runnable, but this is task sequencing/current control rather than evidence of a separate S2 attenuation loop.
- Why this is / is not agent-owned: multiple workers and a DAG are insufficient under the Profile; the reviewed evidence does not identify a concrete recurring interference between S1 units and a distinct coordination relation targeted at attenuating that interference.
- Evidence: [`$yolo` wave execution](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/yolo/SKILL.md), [`README.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: dependency ordering can prevent invalid execution order, but no separate S2-specific interference/attenuation relation is evidenced strongly enough to publish a positive state.

### Absence scope

- Surfaces inspected: AI-DLC workflow, project/task DAG, unblocked-task selection, worker waves, comments, permissions, daemon/session dispatch and review/rework paths.
- Plausible first-party paths checked: dependency edges, parallel wave scheduling, task assignment, project shared state, agent handoff and review comments.
- Why no material first-party path remains: the inspected paths establish dependency management, dispatch, sequencing and reporting; they do not establish a specific inter-S1 conflict or oscillation plus a dedicated attenuation relation feeding back into the affected workers.

## S3 — Inside-and-now control

- State: A
- Function: maintain a project-wide current operational view and decide which commitments start, wait, reopen, advance or escalate.
- Disturbance / variety regulated: incomplete dependencies, failed or missing worker submissions, task-review failures, proposal-review failures, stuck work, exhausted review rounds and changing readiness across the task DAG.
- Decisive decision or feedback right: select the next dependency-ready task wave, dispatch workers, decide how to handle non-ready/failed results, reopen failed tasks, advance verified tasks and stop/escalate when the project cannot progress.
- Decision owner: the model-driven orchestrating agent executing the first-party `$yolo` workflow.
- Supporting / enforcement mechanisms: persistent project/proposal/task state, `chorus_get_unblocked_tasks`, status transitions, acceptance criteria, admin transition APIs, reviewer comments, permissions and daemon/session lifecycle.
- Closure path: orchestrator reads current project/task/review state → chooses wave/advance/reopen/escalate action → Chorus state/API transitions and worker dispatch implement it → changed task states alter subsequent readiness and execution → refreshed project state returns to the orchestrator.
- Boundary reachability: `$yolo` is a shipped first-party Chorus skill and explicitly provides a complete autonomous mode using Chorus MCP/project state; its current-control decisions are not borrowed from repository CI or human project administration.
- Why this is / is not agent-owned: task-state and dependency code enforce constraints, but the orchestrating agent chooses the current portfolio action, handles exceptional results and decides whether to continue, rework or escalate.
- Whole-system current view: project, proposal, task DAG, unblocked tasks, task statuses, review comments/verdicts and completion state across the Chorus project.
- Current-control decision scope: current worker commitments, wave dispatch, rework/reopen, progression after review, and escalation when progress conditions cannot be satisfied.
- Evidence: [`plugins/chorus/skills/yolo/SKILL.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/yolo/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: server-side validation, permission checks and dependency computation are enforcement/support. S3 credit comes from the orchestrating agent's evidenced project-wide current-control choices.

## S3* — Complementary audit

- State: A
- Function: independently challenge proposal and implementation completion claims through separate read-only reviewer agents and return blocking findings into corrective project operation.
- Disturbance / variety regulated: missing requirements, weak acceptance criteria, dependency/design errors, implementation drift, circular or inadequate self-tests, build/test failure and developer self-verification blind spots.
- Decisive decision or feedback right: inspect evidence independently, classify findings as blocking/non-blocking and issue the current round's `VERDICT` that determines whether the orchestrator advances or returns the work for correction.
- Decision owner: the separate proposal-reviewer or task-reviewer agent for the corresponding audit stage.
- Supporting / enforcement mechanisms: read-only reviewer permissions, proposal/task/Idea/comment APIs, filesystem/test/build inspection, structured verdict format, persisted comments, review-round limits and admin state-transition APIs.
- Closure path: producer submits proposal/task → distinct reviewer gathers complementary evidence and posts current-round verdict → orchestrator reads that verdict → FAIL causes reject/revise/resubmit or reopen/rework → the corrected artifact is reviewed again before advancement.
- Boundary reachability: both reviewer definitions and the orchestration that invokes/consumes them are shipped first-party Chorus plugin surfaces in the standard autonomous workflow.
- Why this is / is not agent-owned: reviewers make substantive adversarial judgments from separate evidence and are prevented from editing the work under review; deterministic state transitions only enforce the downstream response selected from the verdict.
- Claim being audited: proposal completeness/alignment before implementation and task implementation/acceptance correctness before verification/completion.
- Ordinary reporting path: PM/developer agents create proposal drafts or implementation, self-check/report work and submit it through ordinary Chorus state transitions.
- Complementary access path: reviewer agents separately fetch originating Idea/proposal/task/AC/comments and inspect project files, diffs, tests/builds or proposal dependency coverage under read-only constraints.
- Independence boundary: reviewer roles are separate spawned agents with explicit read-only restrictions and distinct reviewer contracts; they do not author the proposal/code they evaluate during the review pass.
- Who acts on findings: the `$yolo` orchestrator reads the current verdict and rejects/reopens or approves/verifies accordingly, causing the affected planning/development agents to perform subsequent correction.
- Evidence: [`proposal reviewer`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/chorus-proposal-reviewer/SKILL.md), [`task reviewer`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/chorus-task-reviewer/SKILL.md), [`$yolo` review loops](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/yolo/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: reviewer verdict strings are not credited merely because they are called review; the positive state rests on separate evidence access, read-only independence and an explicit findings-to-rework closure.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then adaptation loop is established at the Chorus-project recursion.
- Disturbance / variety regulated: not established at S4 scope.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: project search, Idea elaboration, proposal generation, repository/context inspection, persistent reports and reviewer feedback improve current project execution but do not establish prospective environment sensing that changes the harness/project's future capability program.
- Closure path: current-project information feeds current planning and rework; no separate future-facing adaptation selection/return loop was established.
- Why this is / is not agent-owned: planning future tasks inside the current product request and learning from current review are not sufficient to map S4 without an environment-facing prospective adaptation loop.
- Evidence: [`$yolo` planning/review workflow](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/yolo/SKILL.md), [`README.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: Chorus can be extended and its agents can research externally, but generic agent capability or project planning does not establish S4 ownership for the harness at this boundary.

### Absence scope

- Surfaces inspected: Idea elaboration, proposal generation, project/repository search, reports, reviewer loops, plugin skills, project state and daemon/session operation.
- Plausible first-party paths checked: elaboration, project discovery, proposal planning, persisted reports/comments, reviewer feedback and reuse of project artifacts.
- Why no material first-party path remains: these paths close current-project planning, execution and correction; none establishes a distinct prospective environment-sensing → adaptation-option → returned capability/program-change loop at the assessed recursion.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the Chorus-project recursion.
- Disturbance / variety regulated: not established at S5 scope.
- Decisive decision or feedback right: not established as identity/ultimate policy.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: user prompt/Idea intent, API-key permissions, admin approval/verification rights, project settings and review-round limits constrain operation but are operational/task policy rather than an evidenced S5 identity loop.
- Closure path: permissions and approvals affect allowed current actions, but no disputed identity/ultimate-policy matter is routed to an authoritative S5 actor and returned as governing identity policy.
- Why this is / is not agent-owned: a user origin, admin permission or approval gate is not automatically S5; the reviewed project boundary does not expose an identity-level policy negotiation/closure path.
- Evidence: [`README.md`](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/README.md), [`$yolo` prerequisite/admin flow](https://github.com/Chorus-AIDLC/Chorus/blob/148b7928b99773f7fbdf61080940bd6995b06934/plugins/chorus/skills/yolo/SKILL.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: humans can operate/administer Chorus and configure permissions, but those facts alone do not establish a parent-governed S5 function under Methodology 0.3.5.

### Absence scope

- Surfaces inspected: project/Idea creation, permissions, admin proposal/task transitions, plugin configuration, review escalation and user/agent participation model.
- Plausible first-party paths checked: human verification philosophy, admin permissions, proposal approval, task verification, Idea intent and review escalation.
- Why no material first-party path remains: the identified authority concerns operational authorization and task/project intent, not a reconstructable identity/ultimate-policy issue → authoritative decision → return-to-operation loop.

## Distributed OSS parent arrangement

The open-source project has maintainers/contributors, but repository development governance is outside the running Chorus-project boundary. No organization-level parent modifier is inferred from OSS maintenance. Within a running Chorus project, humans may hold permissions and approvals, but the reviewed evidence does not establish a distinct qualifying parent-owned S3/S4/S5 mode rather than ordinary operational administration.

## Self-hosted and non-human modes

Chorus is self-hostable and supports mixed human/agent operation. The credited S3 mode is the shipped autonomous `$yolo` path. Optional human approvals, permissions and operator intervention do not add `(P)` without a function-specific parent-control closure. The autonomous mode can therefore be assessed independently of whether a deployment also chooses human gates.

## Recursion

This assessment fixes recursion at one Chorus project. Individual worker sessions are S1 units within that project; the `$yolo` orchestrator acts across their current project state. The assessment does not import the internal organization of Claude Code/Codex/etc. as a deeper Chorus recursion, and it does not treat Chorus's own OSS development organization as the same system.

## Variety and escalation

Chorus absorbs operational variety through task decomposition, dependency readiness, independent reviewers and repeated rework rounds. Review silence has a bounded retry/fallback contract; explicit reviewer refusal or exhausted review rounds stops autonomous progression and escalates rather than treating absence as PASS. These escalation paths support S3/S3* closure but do not create S5 by themselves.

## Evidence gaps

The repository supplies strong primary evidence for the autonomous `$yolo`, worker and reviewer paths. No positive S2, S4 or S5 path was found in the reviewed standard distribution. A future reassessment should revisit those states if Chorus adds explicit inter-worker conflict attenuation, environment-facing adaptation of future project capability, or identity-level governance modes.