---
harness_id: agentheim
project_name: Agentheim
repository: https://github.com/heimeshoff/Agentheim
review_ref: 6af21c1cb11ee51d6cbe2305fc537f927b37a2d4
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: P
---

# Agentheim

## Review boundary

- System in focus: installed Agentheim plugin for Claude Code, including its skill/agent definitions, task-board lifecycle helpers, worktree conductor and review/research loops, in one user's project.
- Purpose and identity: convert user-articulated product vision into a modeled, bounded-context task system, run parallel agent workers without destructive overlap, verify changes and govern subsequent execution against the vision.
- Relevant environment: developer/user, code repository and git conflicts, changing project requirements, external documentation via research, Claude Code agent runtime, plugins and operating-system processes.
- Standard-distribution boundary: first-party plugin skills/work, modeling, brainstorm, research, verifier/reviewer definitions and deterministic Node lifecycle helpers as invoked by Claude Code; the provider and its general tools are external execution substrate.
- Credited operating / distribution surfaces: skills/work/SKILL.md, skills/verification-before-completion/SKILL.md, agents/{worker,orchestrator,verifier,researcher,research-reviewer}.md, skills/{research,modeling,brainstorm}/SKILL.md, lib/task-lifecycle-cli.mjs, lib/merge-conflict-ladder.mjs, lib/vision-conformance.mjs.
- Adjacent first-party surfaces excluded from ownership: standalone eval fixtures, README screenshots, repo-development CI, release scripts, VS Code/dashboard display not driving a specific credited decision.
- First-party operating / deployment modes considered: interactive builder-guided brainstorming/modeling, unscoped/scoped work-skill batch with multiple agent workers and default fresh-eyes review, optional research and explicit parent-authorized vision revision; user can opt out of verifier per run.
- Recursion level: one builder-owned software-project lifecycle with Agentheim agent work cells; individual specialized workers are units of S1, not presumed full VSM recursive organizations.
- Reviewed revision: 6af21c1cb11ee51d6cbe2305fc537f927b37a2d4.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Agentheim distributes Claude Code skill definitions and specialist agent prompts backed by Node.js filesystem/task protocol helpers. A builder captures an intended project vision and bounded contexts; modeling converts ideas into versioned task files with dependencies, acceptance criteria, and context references. Work skill reads all ready tasks, creates isolated git worktrees, dispatches independent coding agents, obtains strict RESULT records, runs a separate fresh-context verifier, and merges passing code sequentially into the shared project. Dependencies, exclusive task ownership and cross-worker overlap advisories choose batch order; actual file collisions at merge-back trigger a bounded conflict repair ladder and re-verification. Research skill commissions external web investigation and a different independent source-check reviewer, storing cited reports for subsequent modeling and ADR decisions. The dashboard/VS Code bridge exposes status and launch surfaces, not the credited intelligence itself.

Primary sources: [work conductor](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/work/SKILL.md), [worker](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/agents/worker.md), [verification](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/verification-before-completion/SKILL.md), [research](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/research/SKILL.md), [brainstorm](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/brainstorm/SKILL.md).

## Operational model

S1 cells are task-scoped coding workers with distinct code diff/test outcomes in isolated worktrees. The model-backed work conductor sees the project-wide task/dependency state and chooses dispatch and integration order. Node helpers claim, validate, log and enforce decisions; they do not themselves choose priorities or verify task meaning. Fresh verifier agents separately inspect code/diff, acceptance criteria and runner outcomes and return a veto/rework decision. Research agents provide external knowledge; modeling and builder-approved vision revisions can change future task commitments. Credit applies only when installed plugin skills actually execute in the documented modes, not to generic Claude Code behavior with no plugin.

## S1 — Operations

- State: A
- Function: implement bounded source/test changes for user-approved project tasks.
- Disturbance / variety regulated: differing task requirements, repository code and tests, unexpected implementation obstacles.
- Decisive decision or feedback right: specialist/coding worker selects code edits and tests to meet one task's acceptance criteria.
- Decision owner: task-scoped Claude Code worker agent under the installed Agentheim worker definition.
- Supporting / enforcement mechanisms: dedicated worktree, preloaded ADR/task context, permitted source/test file scope and strict RESULT sidecar.
- Closure path: agent edits and runs tests in its worktree, returns SUCCESS/BOUNCED/FAILED with evidence to conductor for integration or recovery.
- Boundary reachability: work skill explicitly spawns agentheim:worker in the shipped batch path; worker's instructions and task-scoped input are installed plugin surfaces.
- Why this is / is not agent-owned: choice of implementation and local corrections belongs to the worker model; git worktree and task-lifecycle helpers just isolate and record.
- Evidence: [work skill](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/work/SKILL.md), [worker](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/agents/worker.md).
- Basis: explicit
- Confidence: high for installed provider-backed work mode.
- Caveats: requires Claude Code runtime and user/model access; no paid end-to-end execution was performed.

## S2 — Coordination

- State: A
- Function: prevent and resolve interference between simultaneous coding S1 cells editing overlapping files, without centralizing each worker's code choices.
- Disturbance / variety regulated: two ready workers modify the same code path, making direct simultaneous integration inconsistent or conflict-prone.
- Decisive decision or feedback right: model conductor applies collision advisory, chooses sequential integration, and routes real merge conflicts to a bounded resolution workstream before accepting a revised worker artifact.
- Decision owner: agent executing work conductor for live merge order and conflict-repair decisions; git's three-way merge, conflict parser and worktree locks detect/enforce collisions.
- Supporting / enforcement mechanisms: per-worker worktrees, git conflict markers and merge-back status, source-file overlap advisory, merge-conflict ladder and re-verification guard.
- Closure path: competing workers progress independently; conductor serializes accepted merge-back; actual conflicts cause an agentic resolution dispatch and fresh re-verification, changing the final edits before they reach shared main.
- Boundary reachability: full path is specified in the installed work skill and called as part of ordinary parallel task integration, rather than only a test fixture.
- Why this is / is not agent-owned: the conductor has discretion in order, conflict interpretation and repair dispatch; git alone cannot choose the revised implementation.
- Distinct S1 units: parallel coding workers operating on distinct task IDs and worktrees.
- Inter-S1 disturbance: overlapping source/test changes or noncommutative edits to a common file produce real git merge conflict.
- Attenuating coordination relation: isolated branches plus sequential merge and model-driven bounded conflict resolution.
- Feedback into subsequent S1 behaviour: losing worker receives the conflict note, can revise only allow-listed files, and is re-verified before inclusion.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism responds to a concrete conflict between concurrently operating S1 units and feeds a resolution back, beyond mere task transport.
- Evidence: [work skill conflict ladder](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/work/SKILL.md), [merge helper](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/lib/merge-conflict-ladder.mjs).
- Basis: explicit
- Confidence: high for documented git-based mode.
- Caveats: many order/allow-list constraints are deterministic; agent ownership is limited to discretionary conflict/merge response.

## S3 — Inside-and-now control

- State: A
- Function: manage the current project-wide portfolio of ready/doing tasks and commitments while workers retain local code discretion.
- Disturbance / variety regulated: dependencies, overcommitment, stranded in-progress tasks, worker failure and limited parallel capacity across bounded contexts.
- Decisive decision or feedback right: model-backed conductor prioritizes ready tasks under dependency restrictions, chooses batches/dispatch and re-dispatch/stop dispositions on worker/verifier results.
- Decision owner: installed work-skill conductor agent; external builder approves the work invocation/scope but does not make every live task scheduling or repair choice.
- Supporting / enforcement mechanisms: board files, MAX_PARALLEL, dependency DAG validation, lifecycle locking/claim/complete helpers, worktree ownership and protocol logs.
- Closure path: conductor observes all active/ready work and verifier dispositions; commits verified results, moves lifecycle states, requeues bounced tasks or escalates irrecoverable ones, thereby changing the next available dispatch set.
- Boundary reachability: shipped work skill reads all BC boards, integrates results and loops until the current selected scope is terminal.
- Why this is / is not agent-owned: priority and exception handling are model-driven choices constrained by mechanical checks; static caps do not alone justify A.
- Whole-system current view: cross-BC ready, doing and backlog task inventory plus dependency graph, currently in-flight worktrees and recent protocol.
- Current-control decision scope: dispatch quantity/order, current task commitments, retry/verification escalation and authorized integration.
- Evidence: [work skill](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/work/SKILL.md), [task lifecycle](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/lib/task-lifecycle-cli.mjs).
- Basis: explicit
- Confidence: high for active work batch mode.
- Caveats: no automatic deployment or unlimited authority; a builder invokes or scopes a batch and can stop it.

## S3* — Complementary audit

- State: A
- Function: challenge worker self-reports of completion using different access to actual code/diff, task acceptance criteria and test results.
- Disturbance / variety regulated: plausible but incorrect code, incomplete task coverage, scope drift or false worker success.
- Decisive decision or feedback right: fresh-context verifier decides PASS, FAIL or SKIP, independently of the worker's reasoning and with direct read/run tools.
- Decision owner: separate Agentheim verifier model, not the code-writing worker or deterministic result parser.
- Supporting / enforcement mechanisms: diff/test-command snapshot, read-only agent tools, strict verdict protocol, bounded retry and commit gate.
- Closure path: FAIL blocks integration and causes targeted re-dispatch with reasons; PASS allows conductor to materialize bookkeeping and merge; iteration cap escalates rather than silently accepting failure.
- Boundary reachability: the installed work skill calls the fresh-eyes verification gate after each worker SUCCESS by default; no detached development-only test is credited.
- Why this is / is not agent-owned: the verifier independently judges whether the actual diff meets criteria; deterministic parsing merely enforces its verdict.
- Claim being audited: worker reports that a specific task has been completed correctly.
- Ordinary reporting path: worker RESULT block plus own tests/claims.
- Complementary access path: fresh verifier reads task specification and raw git diff/runner output without worker reasoning, then runs checks.
- Independence boundary: distinct agent instance/context, no Write/Edit, separate pass/fail authority and source-facing evidence.
- Who acts on findings: conductor blocks merge, redispatches worker or escalates on verifier failure.
- Evidence: [verification gate](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/verification-before-completion/SKILL.md), [verifier](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/agents/verifier.md), [work flow](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/work/SKILL.md).
- Basis: explicit
- Confidence: high
- Caveats: per-run --no-verify bypass exists; source inspection proves shipped path, not actual live provider independence in this review.

## S4 — Outside-and-then intelligence

- State: C
- Function: investigate external technology/domain changes and formulate prospective design alternatives for future project capabilities, then make those findings available to modeling.
- Disturbance / variety regulated: unknown external libraries, architectural options, market/domain facts or changing technical constraints before implementation.
- Decisive decision or feedback right: research/modeling agent can investigate, compare options and propose model/backlog changes; full adaptation is contingent on builder-sponsored modeling/promotion/work, not an always-on autonomous S4 loop.
- Decision owner: constructor path of researcher → separate research-reviewer → modeling/orchestrator; actual commitment of scope or strategy stays with builder/agentic workflow under task acceptance.
- Supporting / enforcement mechanisms: WebSearch/WebFetch, source-grounded research notes, prior-art linking, ADR/task references and task pipeline.
- Closure path: approved research report enters related_research and task Notes/ADRs; a later modeling decision may change a refined task and downstream work. This is a first-party constructor route, not proof of continuous self-adaptation.
- Boundary reachability: research skill explicitly participates in installed brainstorm/model/work when outside knowledge is insufficient and its reports are wired into modeling records.
- Why this is / is not agent-owned: specialist agents generate and compare future options, but independent external research and task-citation infrastructure alone do not own a complete autonomous decision to change present capability.
- External distinction: alternative external libraries, documented domain constraints or state of the art gathered from primary sources.
- Future / prospective distinction: architectural options for work not yet implemented.
- Adaptation option generated: source-backed report and possible revised backlog/ADR.
- Path back into current capability / S3: user/agent modeling cites report in refined task; the work conductor can then schedule an authorized implementation.
- Evidence: [research skill](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/research/SKILL.md), [modeling](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/modeling/SKILL.md), [researcher](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/agents/researcher.md).
- Basis: structural
- Confidence: medium
- Caveats: no independent autonomous/environment-monitoring daemon; many ordinary product task refinements are not prospective S4. Only external-research-backed constructor route is credited.

## S5 — Policy and identity

- State: P
- Function: preserve or consciously revise the builder's project identity, success criteria and non-goals across future work.
- Disturbance / variety regulated: a proposed product direction or shipped work diverges from the project vision/ultimate constraints.
- Decisive decision or feedback right: builder/user alone legitimizes a vision creation, revision, extension, or rejection; the plugin prompts for confirmation and persists the selected policy.
- Decision owner: human builder parent at the project recursion, not a model simply obeying an initial system prompt.
- Supporting / enforcement mechanisms: brainstorm's vision/non-goal conversation, persisted vision.md, work's vision-conformance advisory, model/worker task-context preloading and scope/acceptance gates.
- Closure path: current work's vision-conformance flag is surfaced to the builder; builder can expressly revise/extend or retain the project vision through brainstorm; updated vision.md becomes governing context for subsequent modeling, task formation and work acceptance.
- Boundary reachability: initial and revision modes are shipped plugin skills; work itself reads the persisted vision and emits a post-work conformance result, and brainstorm writes approved revisions into the same project record.
- Why this is / is not agent-owned: the model can challenge or summarize options, but only the user decides the project's ultimate identity; the returning record guides later work.
- Identity / ultimate-policy issue: whether proposed work remains within the project's declared success criteria, non-goals and product purpose.
- Ultimate authority in each claimed mode: builder parent in interactive brainstorm/vision revision mode; no autonomous S5 mode claimed.
- Return-to-operation path: revised/confirmed vision.md and task priorities/acceptance context read by future modeling/work sessions.
- Evidence: [brainstorm](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/brainstorm/SKILL.md), [vision conformance in work](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/work/SKILL.md), [modeling](https://github.com/heimeshoff/Agentheim/blob/6af21c1cb11ee51d6cbe2305fc537f927b37a2d4/skills/modeling/SKILL.md).
- Basis: structural
- Confidence: medium
- Caveats: the conformance signal is deliberately advisory, not an automatic work veto; S5 depends on an active parent/user decision and re-entry through the first-party revision procedure.

## Distributed OSS parent arrangement

The assessed identity recursion is a single builder's project, not Agentheim's own contributor organization. Its user-approved vision mode is local P only; a plugin development GitHub team does not become an S5 organization for every downstream installed project.

## Recursion

Bounded contexts and git worktrees delimit task cells; neither worktree nor specialist spawn automatically creates a viable nested VSM. Recursion beyond the local project/workers remains unproven.

## Variety and escalation

Dependencies and MAX_PARALLEL attenuate simultaneous task variety; scoped worker contexts amplify implementation variety; fresh verifier introduces complementary checks; conflict notes and bounded retries preserve specific failed distinctions rather than only reporting green status. Worker BOUNCED/FAILED and exhausted verification receive tracked dispositions and possible builder escalation. These are operational exception paths, not automatically separate algedonic S-functions.

## Evidence gaps

- Source/prompt/Node helper inspection; no external paid Claude Code work session was executed in this assessment.
- S4 C is a deliberately limited constructor path; no proof of a continuous autonomous future-sensing loop.
- S5 P is builder-local and interactive, not Agentheim-maintainer organization governance.
- Actual tool access and successful web/researcher/verifier integration depend on the host Claude Code distribution; isolated eval fixtures and CI were not credited as live operational witnesses.
