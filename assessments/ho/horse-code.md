---
harness_id: horse-code
project_name: Horse Code
repository: https://github.com/hizliemre/horse-code
review_ref: 8e134ac3b2745477940bda5867313d07ae535900
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: P
---

# Horse Code

## Review boundary

- System in focus: the first-party Horse Code terminal coding runtime at frozen revision `8e134ac3b2745477940bda5867313d07ae535900`, including the refine/specify/plan/task pipeline, role-agent loops, board/wave engine, isolated worktrees, review/council/judge paths, post-merge revision, model/skill tuning, memory, constitution and supported TUI/operator controls.
- Purpose and identity: turn a software-development request into reviewed, tested, committed work on an isolated branch/worktree while coordinating multiple role-specialized model actors and preserving explicit user authority over selected runtime and project-governance decisions.
- Relevant environment: user requests and answers, repository/source/build/test state, git branches/worktrees, model/provider availability, project rules/constitution, connected MCP tools, external model catalogs, installed skills, persisted board/session/memory state, review findings and operator interventions.
- Standard-distribution boundary: shipped Horse Code TypeScript runtime, built-in roles/prompts/tools, board/wave/worktree machinery, review and revision loops, constitution handling, memory, project scanning, model-health/tuning and TUI commands. External model providers, MCP servers, Git hosting services and externally installed skill repositories are dependencies and cannot donate ownership.
- Credited operating / distribution surfaces: `README.md`; `src/agent/`; `src/engine/`; `src/board/`; `src/worktree/`; `src/speckit/`; `src/session/`; `src/skills/`; `src/tui/`; `src/config/`; `src/wiring.ts`; `src/cli.ts`; built-in prompts and tools.
- Adjacent first-party surfaces excluded from ownership: repository unit/integration tests, `src/eval/`, CI/release workflows, historical design/planning documents under `docs/superpowers`, maintainer/contributor governance and development-only benchmark/test infrastructure. They may corroborate behavior but are not credited as runtime owners.
- First-party operating / deployment modes considered: interactive TUI coding runs, resumed runs, multi-task wave execution, post-merge revision, direct verify/research/govern lanes, live operator role/model/parallelism control, first-run role bootstrap and explicit `/roles adjust`.
- Recursion level: one Horse Code job/session is the assessed organization. Parallel task implementers operating in isolated task worktrees are distinct S1 units within that organization; reviewer/council/judge roles are metasystem actors, not additional operational S1s for the same coding outcome.
- Reviewed revision: `8e134ac3b2745477940bda5867313d07ae535900`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Horse Code is a role-based TypeScript coding harness. A request is refined and may pass through constitution, brainstorming, specification, clarification, planning and task decomposition before implementation. The project manager turns the approved plan into a persistent board whose cards carry dependencies, acceptance criteria and expected write paths. A team-lead agent audits parallelizable cards for missing semantic dependencies and can add dependency edges before execution.

Implementation cards run as separate role-agent loops in isolated task worktrees. The wave engine starts tasks when their dependencies are merged, respects a live parallelism ceiling and prevents simultaneously running tasks from writing the same declared files. Task attempts escalate across model/role tiers, receive independent code review and acceptance checks, and merge into a session base branch. Merge conflicts have a distinct resolver path and may cause a task to be restarted from a newer base.

Review is multi-layered. Per-task review teams and councils judge individual artifacts; after task work is merged, a separate principal-coder performs a holistic review of the integrated diff. Change requests are handed to a senior-coder revision pass, committed, pushed and reviewed again. This post-merge path can challenge claims that survived local task review.

The TUI exposes current whole-run state and lets the operator alter the running concurrency ceiling through `/parallel N`, cancel a running job and choose specific model chains. Separately, `/roles adjust` reads the currently healthy external model pool and project facts, uses a capable model to assign role model chains and skills, applies those choices to the live registries and persists them for future sessions.

Project governance is represented by a committed constitution. An explicit govern lane carries the user's governance request to the analyst, which establishes or minimally amends the constitution and may ask the user for core-principle decisions. Constitution rules are subsequently selected by scope and injected into the roles they govern.

## Operational model

Operational work is performed by task-specific implementer agents operating over separate worktrees and tool loops. Their output is reviewed, tested and merged into the shared session base. The board is the durable account of current task commitments and outcomes; dependencies and declared file ownership constrain which S1 units can safely operate together.

Agent-owned coordination is separated from deterministic enforcement. The team-lead model decides whether a parallel task relation hides an unstated semantic dependency and writes the accepted edge back to the board; deterministic scheduling then enforces dependency readiness and same-file exclusion. Whole-system current resource control is not credited to that scheduler. The supported parent/operator mode owns live concurrency decisions through the TUI.

## S1 — Operations

- State: A
- Function: autonomously implement software-development tasks through model-selected repository/tool actions until reviewed work is ready to merge.
- Disturbance / variety regulated: unfamiliar codebases, implementation choices, repository constraints, build/test failures, review feedback, tool/model failures and merge-local changes.
- Decisive decision or feedback right: choose concrete code changes and tool actions, interpret returned repository/test evidence, revise the implementation and decide when a task attempt is ready for review.
- Decision owner: the active Horse Code implementer role agent (for example coder, designer, senior-coder or principal-coder depending on the stage).
- Supporting / enforcement mechanisms: role registries, tool permissions, isolated worktrees, board state, model fallbacks, turn budgets, automatic checkpoints, code-review/acceptance gates and git merge machinery.
- Closure path: task + project context → implementer chooses tool/code actions → worktree produces concrete results → review/test feedback returns → implementer/revision actor changes work → accepted work merges into the session base.
- Boundary reachability: standard feature/bugfix jobs construct role agents and task worktrees through the shipped `job`, `wave-task`, `task-cycle` and agent-loop paths.
- Why this is / is not agent-owned: deterministic worktree, board and git machinery transports and constrains the attempt, but removing the role model removes the discretionary coding choices that create the implementation.
- Evidence: [README.md](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/README.md); [src/engine/task-cycle.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/task-cycle.ts); [src/engine/wave-task.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/wave-task.ts); [src/agent/loop.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/agent/loop.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: role/model routing and runtime guards can change which agent serves an attempt, but they do not replace the implementer's open-ended operational decision right.

## S2 — Coordination

- State: A
- Function: attenuate interference among parallel implementer S1 units before and during concurrent work.
- Disturbance / variety regulated: two operational task agents may be scheduled together despite an unstated semantic dependency or may attempt to write overlapping files, causing stale assumptions, failed downstream tasks or merge conflicts.
- Decisive decision or feedback right: judge whether candidate parallel tasks have a missing dependency that makes simultaneous execution unsafe and add the dependency edge that changes their subsequent scheduling.
- Decision owner: the model-backed `team-lead` role for semantic dependency coordination.
- Supporting / enforcement mechanisms: project-manager file/dependency declarations, deterministic `computeWaves`, `splitFileConflicts`, live busy-file exclusion, dependency-ready scheduling, isolated worktrees and serialized merge sections.
- Closure path: board exposes candidate parallel tasks/dependencies/write paths → team-lead audits the interaction → accepted missing dependency is added to the board → wave computation/scheduler observes the new edge → affected implementer S1s no longer run in the conflicting relation.
- Boundary reachability: team-lead audit is invoked by the standard board/wave pipeline before parallel implementation and writes directly to the first-party Board consumed by execution.
- Why this is / is not agent-owned: the scheduler and file exclusion deterministically enforce already-known relations; the semantic decision that a task actually needs another task's output is produced by the team-lead agent.
- Evidence: [src/engine/project-manager.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/project-manager.ts); [src/engine/team-lead.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/team-lead.ts); [src/engine/waves.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/waves.ts); [src/engine/wave-engine.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/wave-engine.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: same-file exclusion is deterministic support and is not used by itself to claim agent ownership.
- Distinct S1 units: parallel coder/designer/other implementer agents executing different board cards in separate task worktrees.
- Inter-S1 disturbance: missing semantic dependencies and overlapping write sets can make concurrently executing cards interfere, consume stale state or collide at merge.
- Attenuating coordination relation: team-lead adds missing task dependencies; deterministic wave/file-clash machinery then serializes the affected relationship.
- Feedback into subsequent S1 behaviour: the changed Board dependencies and busy-file relation alter eligibility, so an affected implementer starts later against merged predecessor state instead of continuing in the unsafe parallel relation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited path is tied to a concrete interaction disturbance between distinct parallel operational units and changes their interaction topology; generic board storage and role routing are not the positive witness.

## S3 — Inside-and-now control

- State: P
- Function: regulate current whole-job resource pressure by changing how many operational task agents may run concurrently.
- Disturbance / variety regulated: a job can expose more runnable cards than the available machine/model/provider capacity can safely support, producing heap pressure, rate limits and a larger unfinished tail.
- Decisive decision or feedback right: choose the live maximum number of task agents allowed in flight for the current/future scheduling passes of the running job.
- Decision owner: the human operator in the supported interactive TUI mode.
- Supporting / enforcement mechanisms: TUI board/running-agent display, `/parallel N`, the mutable `parallelRef`, persisted `maxParallel`, wave-engine slot accounting and the scheduler's live `ceiling()` getter.
- Closure path: current run exposes active agents/board state → operator chooses a new concurrency ceiling → `setParallel` updates the live value → the scheduler rereads that ceiling on subsequent passes → current task admission/resource usage changes.
- Boundary reachability: `/parallel` is a shipped TUI command explicitly documented to take effect on the running job.
- Why this is / is not agent-owned: deterministic scheduling enforces the ceiling, but the discretionary whole-run resource choice belongs to the operator. No first-party autonomous actor was established that owns an equivalent whole-system current resource/commitment judgment.
- Evidence: [README.md](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/README.md); [src/tui/commands.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/tui/commands.ts); [src/tui/app.tsx](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/tui/app.tsx); [src/engine/wave-engine.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/wave-engine.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: team-lead dependency repair is credited to S2, while deterministic park/wake/retry, model-health and slot machinery support present operations without owning S3 discretion.
- Whole-system current view: the TUI surfaces the persistent board and currently running agents/models for the job while the operator can issue run-control commands.
- Current-control decision scope: the operator changes the global in-flight task ceiling that governs resource allocation across the job, with immediate effect on later scheduling passes.

## S3* — Complementary audit

- State: A
- Function: independently challenge the integrated result after local task review and return whole-diff findings into corrective work.
- Disturbance / variety regulated: locally reviewed task outputs can each look acceptable while their merged combination still contains cross-task defects, deferred review concerns or integrated-surface problems.
- Decisive decision or feedback right: inspect the merged base diff holistically and decide approve versus request-changes; after bounded revision rounds, decide whether remaining findings are acceptable or require a human decision.
- Decision owner: the separate model-backed `principal-coder` reviewer.
- Supporting / enforcement mechanisms: read-only reviewer tools, merged/base diff construction, persisted revision card, PR review comments/threads, senior-coder revision loop, commit/push and repeat review.
- Closure path: task-level work merges → principal-coder receives the integrated diff plus deferred findings → autonomous audit verdict/comments → senior-coder applies changes → changes are committed/refreshed → principal re-reviews or makes a bounded final audit decision.
- Boundary reachability: the standard job path invokes the PR revision pass whenever merged work exists, even on partial jobs.
- Why this is / is not agent-owned: the principal-coder is a distinct read-only judgment role from the operational implementers and from the senior-coder that applies corrections; git/thread machinery only records and transports its findings.
- Evidence: [src/engine/job.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/job.ts); [src/engine/revision.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/revision.ts); [src/engine/reviewer.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/reviewer.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary per-task code review and acceptance gates are not independently sufficient for S3*. The positive witness is the additional integrated post-merge audit over the combined result.
- Claim being audited: that the merged job result, not merely each individual task, is coherent and ready to ship.
- Ordinary reporting path: task implementers plus per-task code review/acceptance report individual card outcomes and merge them into the base.
- Complementary access path: the principal-coder later reads the combined base/PR diff holistically, including deferred local findings.
- Independence boundary: principal-coder is a separate read-only reviewer from the task implementers and the senior-coder revision actor, and it observes the integrated artifact after local review/merge.
- Who acts on findings: senior-coder applies requested corrections; the principal-coder then re-audits the changed integrated result, with unresolved ownership decisions eventually reaching the user.

## S4 — Outside-and-then intelligence

- State: A
- Function: adapt Horse Code's future role capability to changing external model availability/capability and project-specific skill needs.
- Disturbance / variety regulated: connected model sources change availability, quota, cost/capability and source diversity; projects differ in whether skills such as testing or UI guidance are appropriate.
- Decisive decision or feedback right: choose model chains for all roles from the currently healthy external model pool and choose which installed skills should become durable role capabilities for the scanned project.
- Decision owner: the model-backed tuner used by `/roles adjust` (with a separate model-backed skill tuner for skill assignment).
- Supporting / enforcement mechanisms: model-source discovery, model-health quarantine/probing, capability/source heuristics, project factual scan, assignment validation, role registries and config persistence.
- Closure path: current external model pool + project facts → tuner reasons over role requirements and adaptation choices → validated model/skill assignments are applied to live role registries → saved configuration changes future sessions and later S1/S2/S3* operation.
- Boundary reachability: `/roles adjust` is a shipped TUI path; it calls the first-party tuners, applies their returned chains/skills and persists them.
- Why this is / is not agent-owned: deterministic validators constrain invalid or unsafe assignments, but the role-to-model and role-to-skill selection is produced by model reasoning rather than fixed configuration or the operator choosing each assignment.
- Evidence: [src/tui/app.tsx](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/tui/app.tsx); [src/engine/role-tuner.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/role-tuner.ts); [src/engine/skill-tuner.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/skill-tuner.ts); [src/engine/project-scan.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/project-scan.ts); [src/engine/model-health.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/model-health.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the operator explicitly invokes `/roles adjust`; that trigger is not the decisive adaptation judgment. Manual `/roles setmodel` and config edits are not separately promoted to a parent S4 mode here.
- External distinction: which connected/provider-backed models are currently healthy/routable and what installed capability/skill inventory is available.
- Future / prospective distinction: which role-capability allocation will better survive later workload, rate-limit/source failures and project-specific task demands.
- Adaptation option generated: a validated three-model chain per role plus project-appropriate skill assignments.
- Path back into current capability / S3: assignments are applied to live role registries and persisted, altering the agents/resources available to later operational, coordination, review and control activity.

## S5 — Policy and identity

- State: P
- Function: establish or amend the project's standing constitution so later Horse Code roles are governed by the returned project-level principles.
- Disturbance / variety regulated: a project may need new or revised standing principles, coding/governance rules or identity-level constraints that ordinary task execution should not decide locally.
- Decisive decision or feedback right: determine the requested project-governance/constitutional direction and any core-principle choices that the analyst cannot legitimately infer.
- Decision owner: the human user/operator as legitimate parent project authority in the supported govern path.
- Supporting / enforcement mechanisms: intent classification to `govern`, analyst constitution phase, `ask_user`, committed constitution artifact, constitution parsing/scoping/caching and rule injection into role prompts.
- Closure path: user raises a governance/constitution matter → analyst carries that request and asks the parent when core principle decisions are needed → constitution is established/minimally amended → subsequent role prompts receive the applicable rules → later operation is governed by the returned project policy.
- Boundary reachability: the `govern` intent and constitution phase are shipped first-party lanes, and ordinary feature runs also load the same constitution into governed role prompts.
- Why this is / is not agent-owned: the analyst authors and operationalizes the document, but the legitimate ultimate authority for project principles remains the user; automatic initial constitution authoring is not treated as evidence that the analyst has acquired ultimate project identity authority.
- Evidence: [src/engine/upstream.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/upstream.ts); [src/speckit/phases.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/speckit/phases.ts); [src/engine/constitution.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/constitution.ts); [src/engine/constitution-store.ts](https://github.com/hizliemre/horse-code/blob/8e134ac3b2745477940bda5867313d07ae535900/src/engine/constitution-store.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: a static constitution file alone would not establish S5. The positive path is the supported parent governance lane plus return of the authoritative result into later runtime prompts.
- Identity / ultimate-policy issue: establishment or amendment of the project's own standing principles and governing rules rather than an ordinary implementation choice.
- Ultimate authority in each claimed mode: the human project user/operator is the ultimate authority in the claimed parent-governed mode; no separate autonomous S5 base mode is claimed.
- Return-to-operation path: the resulting constitution is stored in the project, scoped into applicable rules and injected into later agent prompts so subsequent work is governed by that decision.

## Distributed OSS parent arrangement

The positive parent claims are local to an operated project/session, not inferred from Horse Code repository maintainers or distributed OSS contributors. S3 and S5 parent authority belongs to the user operating the assessed job/project.

## Self-hosted and non-human modes

Horse Code is self-hosted. The reviewed TUI exposes direct parent control over current concurrency and project governance while operational, coordination, audit and adaptation decisions can remain agent-owned in their credited modes. Generic model/configuration controls are not promoted beyond the function-specific loops described above.

## Recursion

The parent viable unit is one Horse Code job/session. Parallel task implementers are the operative S1 population: each has its own task commitment, model/tool loop and isolated worktree, while their outputs contribute to the shared delivered branch. Reviewers, councilors and the principal reviewer provide metasystem judgment over those operations rather than becoming additional operational S1s for the same coding task.

## Variety and escalation

Operational variety is distributed across task agents and model fallbacks. Inter-task dependency and file-write variety is attenuated by agentic team-lead coordination plus deterministic wave/file controls. Failed task attempts escalate through stronger roles/council paths; non-converging review reaches judge/human seams; integrated output receives a separate principal audit. Model-source degradation can trigger quarantine/re-chaining, while explicit role tuning adapts future capability from the available external pool.

## Evidence gaps

No `?` state is required. The frozen source exposes the standard job composition, S1 task loops, inter-S1 dependency repair, live operator resource control, integrated post-merge audit, role/skill adaptation and project constitution path sufficiently to classify all six functions without relying on adjacent CI/test/governance surfaces.

## Assessment summary

Horse Code establishes autonomous S1 through task implementers, autonomous S2 through model-backed dependency coordination among parallel task agents, parent-governed S3 through live whole-job concurrency control, autonomous S3* through a distinct post-merge principal audit, autonomous S4 through external model/project capability tuning, and parent-governed S5 through the project constitution/governance return path.
