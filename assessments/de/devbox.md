---
harness_id: devbox
project_name: DevBox
repository: https://github.com/rudderlabs/devbox
review_ref: fc2b4270eb803404281e352bb79394a54d28c723
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# DevBox

## Review boundary

- System in focus: self-hosted DevBox ticket-to-draft-PR system, including first-party Bun/Postgres control plane, one OpenSandbox container per task, Python DeepAgents harness, role-specific planning/implementation/review agents and PR follow-up route.
- Purpose and identity: pick up engineering assignments from CLI/Linear, select repositories, plan multi-repo changes, implement/test, challenge results, distill reusable repo knowledge and open PRs, then respond to review/CI feedback.
- Relevant environment: authorized project repos, tickets and comments, model feedback, cross-repository interfaces, concurrent repo planners, code diffs, CI results, GitHub PR reviews, sandbox crashes, persisted workspaces and durable knowledge.
- Standard-distribution boundary: documented bun run up Docker Compose or Kubernetes setup, control-plane task/inbox/event API, harness daemon handlers and DeepAgents stage agents in sandbox; external LLM endpoint, Linear/GitHub services, OpenSandbox/iron-proxy images, actual user and target repositories remain dependencies/adjacent entities.
- Credited operating / distribution surfaces: harness/src/harness/planning.py, implementation.py, self_review.py, distillation.py, deepagents/agents/*, handlers/assignment.py, followup.py, daemon.py; control-plane task/sandbox/inbox routing and CLI.
- Adjacent first-party surfaces excluded from ownership: maintainer GitHub governance, developer CI tests, marketing claims of internal deployment, review by actual PR author and separate user organization.
- Modes considered: default staged harness with per-repo parallel planning and multi-repo implementation, default enabled adversarial self-review, optional model stage/provider selection, repo knowledge distillation, PR comment/CI follow-up and sandbox-resume. Disabling review/distillation is not credited as a positive audit/adaptation mode.
- Recursion: one engineering assignment over one or more repository-specific S1 agents, with a model-selected cross-repo plan and complementary review cells. Control plane can run multiple independent assignments, but autonomous whole-organization S3/S4/S5 is not inferred from a queue.
- Reviewed ref fc2b4270eb803404281e352bb79394a54d28c723 on 2026-11-02; Profile 0.2.4; Methodology 0.3.7.

## Repository architecture

The control plane accepts task, Linear and GitHub follow-up events, creates a persisted inbox round and starts an isolated task volume/sandbox under a concurrency limit. Its scheduler makes no LLM calls. Within the sandbox, an inbox daemon runs one assignment: orientation model selects relevant checked-out repositories, per-repo planning agents work in parallel, an adversarial plan-review agent judges the composed cross-repo plan (including omitted interfaces/repos), and issues are returned to corresponding planning agents for revision or a newly discovered repo is added. Per-repo implementation agents then change code and run checks. A distinct self-review stage dispatches read-only model lens agents, each in its own thread, then merges findings and routes them to separate per-repo fix agents, iterating until reviewed, explicitly declined or capped; unresolved findings are surfaced in PR metadata. Distillation can promote durable high-signal lesson notes into committed repository knowledge that later tasks read. The system opens a draft PR and returns subsequent comments, submitted reviews or CI failure events as new inbox rounds operating on the same branch and persisted workspace.

Primary sources: [README](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/README.md), [architecture](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/docs/architecture.md), [planning](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/planning.py), [self-review](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/self_review.py), [assignment](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/handlers/assignment.py).

## Operational model

Agent models own substantive workspace code and planning decisions; control-plane scheduling, isolation, schema validation and GitHub transport enforce/route them. Orientation and plan reviewer have a whole-assignment view and can change current repo work allocations. A distinct reviewer model challenges implementation diff evidence and feeds fix agents without inheriting implementation thread. Human PR merge and feedback are external task-level acceptance/requests, not an automatically established parent-governed S3/S5 operating mode.

## S1 — Operations

- State: A
- Function: implement assigned engineering changes in one repository through a model-backed agent using source/test feedback.
- Disturbance / variety regulated: unknown code paths, failed checks, requirements ambiguity, repo-local implementation issues and API/CI tool responses.
- Decisive decision or feedback right: per-repo DeepAgents implementation model selects edits, commands, corrections and structured completion evidence.
- Decision owner: configured implementation model; planning models similarly own local repository plan work.
- Supporting / enforcement mechanisms: DeepAgentSession, repo/tool middleware, stage model routing, persisted thread/checkpointer, sandbox workspace and structured result schema.
- Closure path: assigned repo plan → model code/tool actions → observed results → recorded implementation.json → independent review/fix or PR publication.
- Boundary reachability: normal bun run up + control-plane assignment inbox enters handlers.assignment and constructs per-repo model stage agents.
- Why this is / is not agent-owned: sandbox/inbox scheduler has no model/tool discretion; the implementation agent decides the actual code change and follows test feedback.
- Evidence: [implementation](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/implementation.py), [implementation agent](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/deepagents/agents/implementation.py), [assignment](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/handlers/assignment.py).
- Basis: explicit + structural.
- Confidence: high for installed task-to-model action path; provider task quality not empirically measured.
- Caveats: requires configured LLM keys and external target repos; CI/test results can still fail.

## S2 — Coordination

- State: A
- Function: attenuate concrete cross-repository interface/contract mismatch between distinct concurrently authored repo plans before implementation cells act on incompatible assumptions.
- Disturbance / variety regulated: independently planned repo components can omit or contradict dependencies at cross-repo boundaries or miss a required repository.
- Decisive decision or feedback right: separate plan-review model examines the assembled multi-repo plan for missing cross-repo contracts/interfaces and generates repo-scoped issues; the harness returns those issues to their planning agents or instantiates a missing repo planner for a corrected plan.
- Decision owner: plan-review model judges inter-repo incompatibility; deterministic planning driver performs routing to the affected model S1 planners.
- Supporting / enforcement mechanisms: parallel per-repository PlanningAgent sessions, shared cross_repo_assumptions, PlanReviewAgent output, _issues_by_repo and per-repo revision prompts.
- Closure path: concurrent repo plan outputs → merged plan and cross-repo assumptions → reviewer detects interface gap → issue returned to affected repo planner/new repo → revised plan governs later implementation.
- Boundary reachability: ordinary multi-repo assignment path runs orientation, per-repo parallel planning and plan review; no external plugin mediation needed.
- Why this is / is not agent-owned: reviewer model makes substantive cross-repo compatibility judgment; the Python loop transports that feedback but cannot invent missing interfaces on its own.
- Distinct S1 units: separate model PlanningAgent sessions for independently scoped repositories, followed by distinct implementation agents for each planned repository.
- Inter-S1 disturbance: missing cross-repository contracts and interfaces or omitted collaborating repo in the combined plan, arising from independent repo-level planning assumptions.
- Attenuating coordination relation: explicit whole-plan cross-repository reviewer issues are assigned back to the specific source planner, including a new planner for an omitted repo.
- Feedback into subsequent S1 behaviour: _repo_revision_prompt reruns the affected planner with its issues, and the revised output replaces the earlier plan before implementation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: this path targets incompatibility of the outputs of independent repo units, not just a task queue or passive shared state.
- Evidence: [planning.py](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/planning.py), [plan reviewer](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/deepagents/agents/plan_review.py).
- Basis: explicit + structural.
- Confidence: high for shipped inter-repo feedback path; no live cross-repo incompatibility reproduction performed.
- Caveats: review permits unresolved unscoped issues and bounds revision passes; model can miss interface conflicts. S2 claim is restricted to the cross-repo planning relation, not generic cross-assignment sandbox orchestration.

## S3 — Inside-and-now control

- State: A
- Function: choose and repair the current assignment's whole repository scope and operating commitments before dispatch to implementation.
- Disturbance / variety regulated: new task intent, omitted repos, revised cross-repo obligations and missing validation/implementation scope.
- Decisive decision or feedback right: orientation model selects which repositories/components are in the assignment; whole-plan review model can identify additional repository commitments or force current plan revision, which is returned to the stage dispatcher.
- Decision owner: model orientation/whole-plan review roles, with deterministic stage runner enforcing and composing their selected assignments.
- Supporting / enforcement mechanisms: OrientationAgent, PlanningAgent fanout, PlanReviewAgent, structured PlanRepo/PlanReviewOutput, revision/new-repo dispatch and per-task state.
- Closure path: whole workspace/task view → model scope selection → current multi-repo agents plan → whole-plan model judgment/reallocation → revised repo plan → actual implementation dispatch.
- Boundary reachability: standard multi-repo assignment mode from the first-party inbox handler; no manual synthesis of a higher model required.
- Why this is / is not agent-owned: removing the orientation/whole-plan reviewer models leaves deterministic scripts unable to decide which current repo commitments the assignment needs or when absent work must be added.
- Whole-system current view: orientation sees task and workspace repository inventory; plan reviewer receives whole compiled plan and cross-repository assumptions, not one isolated S1's local output.
- Current-control decision scope: selecting involved repos/components, commissioning added repo planning, revising current task implementation/validation commitments before execution.
- Evidence: [planning.py](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/planning.py), [orientation agent](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/deepagents/agents/orientation.py), [assignment.py](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/handlers/assignment.py).
- Basis: explicit + structural.
- Confidence: medium-high, specifically for the bounded current assignment rather than all organization tasks.
- Caveats: the wider control plane's concurrent sandbox scheduling and budgets are deterministic, not a model-run global S3; the S3 claim is confined to one multi-repository assignment, not whole-company management.

## S3* — Complementary audit

- State: A
- Function: independently challenge plan and code/change claims, generate findings and return them into corrective execution.
- Disturbance / variety regulated: planning omissions, code bugs, failed contracts, implementation bias, ungrounded severity and missed review issues.
- Decisive decision or feedback right: separate PlanReviewAgent adjudicates the draft plan; post-implementation ReviewLensAgent models inspect actual working-tree diffs, emit grounded findings and return those to new ReviewFixAgent sessions.
- Decision owner: model reviewers in distinct read-only sessions/threads, never the implementation author; deterministic harness merges and caps reports but does not choose substantive code findings.
- Supporting / enforcement mechanisms: non-durable adversarial plan reviewer, per-(repo,lens) review thread, code-review/bug-hunter/security lenses, merge-findings agent, run_self_review_loop, per-repo fix sessions and revision/fingerprint checks.
- Closure path: draft plan/diff → independent model judgments → plan-agent revisions or review-fix code actions → reviewed state loop or surfaced unresolved PR warnings.
- Boundary reachability: plan review in standard assignment and self-review enabled by default; no dogfood-only actor.
- Why this is / is not agent-owned: reviewer models independently read source/diffs and choose findings; the executor/controller only routes them. Distinct implementation and reviewer threads protect against self-certification.
- Claim being audited: planning sufficiency and correctness/security of the implementation diff before draft PR publication.
- Ordinary reporting path: planning agents and implementation agents produce plan/implementation artifacts and pass claims.
- Complementary access path: read-only PlanReviewAgent sees workspace and whole plan; separate lens agents read git diff including untracked changes and independently trace code paths.
- Independence boundary: one reviewer thread per repository/lens never inherits implementer or other reviewer thread; fix agent also uses a fresh thread rather than the author's.
- Who acts on findings: plan driver re-dispatches planners; self-review fix agent triages/fixes or records explicit declines, and the harness iterates or annotates unresolved warnings.
- Evidence: [plan reviewer](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/deepagents/agents/plan_review.py), [review lens agent](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/deepagents/agents/review.py), [self-review](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/self_review.py).
- Basis: explicit + structural.
- Confidence: high for independent model sessions and corrective return; live review quality not tested.
- Caveats: review stage is opt-out, missing isolated lens result can degrade to empty unless all fail, and declined/iteration-exhausted findings may be published with warnings rather than stopping all PRs.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate externally/future-grounded organizational option-development loop proven beyond task memory distillation.
- Disturbance / variety regulated: historical project mistakes/feedback inform future code tasks, but no explicit future environmental uncertainty or alternatives are sensed and evaluated for system capability.
- Decisive decision or feedback right: none established for outside-and-then strategic adaptation.
- Decision owner: none established for S4; task distillation model selects high-signal existing notes, not prospective strategy options.
- Supporting / enforcement mechanisms: staged harness memory, DistillationAgent, versioned repository .agents/knowledge files and future-session knowledge middleware.
- Closure path: past-task note → knowledge promotion → later agent context; this learning path lacks an externally grounded prospective choice/return warranting S4.
- Boundary reachability: no positive S4 mode claimed.
- Why this is / is not agent-owned: a model filtering and persisting repository conventions from current implementation evidence is durable memory maintenance, not a demonstrated foresight/adaptation organization.
- Evidence: [distillation](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/distillation.py), [distillation agent](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/harness/src/harness/deepagents/agents/distillation.py), [architecture](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/docs/architecture.md).
- Basis: bounded structural absence.
- Confidence: medium-high.
- Caveats: future task productivity might improve, but this is not evidence that S4 future options are developed and returned to S3.

### Absence scope

- Surfaces inspected: distillation agent scope, knowledge middleware, staged task lifecycle, CI-followup, Linear/GitHub event intake and control-plane configs.
- Plausible first-party paths checked: externally sensed long-term shifts, prospective scenario options, decision authority for new capabilities and adopted change returned to present operations.
- Why no material first-party path remains: evidence supports memory reuse of current task facts, not a separate forward-looking external intelligence decision loop.

## S5 — Policy and identity

- State: —
- Function: no distinct ultimate identity/organizational policy decision-and-return loop established inside the harness.
- Disturbance / variety regulated: repo authorization, credential access, human PR approval and scope changes are execution/task constraints.
- Decisive decision or feedback right: none demonstrated for ultimate identity policy.
- Decision owner: none established for S5; operators select repos, keys and final merges outside the AI harness decision graph.
- Supporting / enforcement mechanisms: repo allowlist and iron-proxy permissions, configuration, per-task sandbox isolation, human PR merge and review API.
- Closure path: no identity-level proposal → legitimate institutional decision → updated ultimate-policy return into ongoing harness.
- Boundary reachability: no positive S5 mode claimed.
- Why this is / is not agent-owned: merge permission, token allowlist and per-PR comments are ordinary operating governance, not a first-party identity-policy body.
- Evidence: [architecture](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/docs/architecture.md), [README](https://github.com/rudderlabs/devbox/blob/fc2b4270eb803404281e352bb79394a54d28c723/README.md), [control plane](https://github.com/rudderlabs/devbox/tree/fc2b4270eb803404281e352bb79394a54d28c723/control-plane).
- Basis: bounded structural absence.
- Confidence: high.
- Caveats: real organizations may operate policy/identity above deployed DevBox, which cannot be inferred from this repository's tasks.

### Absence scope

- Surfaces inspected: credential/repo authorization, stage model routing, assignment/follow-up handlers, PR review interface and config.
- Plausible first-party paths checked: identity-level policy disputes, ultimate legitimate authority, decision record and binding policy return.
- Why no material first-party path remains: current approval/permission events can alter individual PRs and task behavior but do not close ultimate policy at the harness recursion.

## Distributed OSS parent arrangement

RudderStack maintainers can change DevBox releases, and users merge PRs, but the public OSS development workflow is adjacent to this installed harness. No extra organization-wide S3/S4/S5 parent loop is inferred.

## Self-hosted and non-human modes

Docker Compose and Kubernetes run isolated task sandboxes with chosen OpenAI/Anthropic stage models. These do not make the deterministic control plane a whole-company autonomous governor. Human PR review and merge are a normal acceptance mode, not an evidenced parent S3/S5 function.

## Recursion

One multi-repo assignment is the chosen whole: repo-specific model agents supply S1, model cross-repo plan review closes S2 compatibility feedback, model orientation/plan review controls current assignment scope for S3, and separately threaded read-only agents supply S3*. Parallel assignments at control-plane level are separate contexts not automatically joined into another viable recursion.

## Variety and escalation

Plan review returns omitted-contract and missing-repo problems to affected planners. Post-code review returns diff findings to fix agents in bounded iterations. CI/PR comments reenter the same task through inbox rounds; sandbox crashes resume from volumes/checkpoints. Distillation retains code-specific lessons, but no autonomous prospective or ultimate-policy function is credited.

## Evidence gaps

Source-first pinned-revision assessment. No live model-key, Docker/Linear/GitHub task-to-PR end-to-end test was run. The S2 and S3 positive claims are specifically scoped to the model-controlled multi-repo assignment; no general claim of whole-company portfolio governance or flawless peer conflict resolution is made.
