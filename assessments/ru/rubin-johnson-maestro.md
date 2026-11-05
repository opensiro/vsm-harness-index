---
harness_id: rubin-johnson-maestro
project_name: Maestro
repository: https://github.com/rubin-johnson/maestro
review_ref: 0589ff3b2b0d25baabff196a1dd64c2147048b8e
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Maestro

## Review boundary

- System in focus: One installed Maestro Python/tmux coding-work-unit orchestration and its bounded local workflow of model-driven implementer/reviewer subprocesses; not the user organization, model vendors or remote GitHub CI.
- Purpose and identity: Crash-resumable multi-model implementation loop with tests, cross-model adversarial review and controlled commit.
- Relevant environment: Work-unit specification/DoD, repository files/diffs, test command outcomes, CLI agent process status, model failures, dependency DAG, escalation tier and SQLite state.
- Standard-distribution boundary: `src/maestro/{cli,orchestrator,orchestrator_review,reviewer,validators,tmux_manager,parallel_executor,decomposer,escalation,db,git_ops}.py` and shipped supported work-unit CLI, excluding third-party coding CLIs' own internal harnesses.
- Credited operating / distribution surfaces: [orchestrator](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator.py), [review orchestration](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator_review.py), [reviewer evidence prompt](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/reviewer.py), [validators](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/validators.py), [tmux manager](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/tmux_manager.py).
- Adjacent first-party surfaces excluded from ownership: External Claude/Codex/Gemini/OpenCode internal loops, optional provider accounts, upstream CI, planned knowledge base, operator-authored work-unit specifications, tests and static default policy as autonomous governing bodies.
- First-party modes inspected: `maestro execute`, work-unit and DAG workflow execution, implementation in isolated tmux windows, independent local tests and file checks, fresh cross-model review, revision/escalation and commit, SQLite recovery, opt-in model backends.
- Recursion level: A bounded local work-unit execution group, possibly multiple ready work units across waves; no general-purpose self-governing enterprise established.
- Reviewed revision: `rubin-johnson/maestro@0589ff3b2b0d25baabff196a1dd64c2147048b8e` (first-party MIT source).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`WorkUnitOrchestrator.execute_work_unit` runs an implement/validate/review/commit state machine and persists status through `MaestroDB`. An implementation agent launched by tmux writes to a real local repository; validators independently execute commands and inspect files, rather than trust completion text. `orchestrator_review` spawns fresh reviewer agents with a non-colliding model type and independent tool access to code/spec, inspects staged files or `git diff` and parses verdicts. Failing tests and `NEEDS_REVISION` return work to another implementation attempt or stronger provider tier; a passed result can commit. `execute_workflow` runs a user-specified dependency DAG in up to four parallel ready work units, marking blocked dependents explicitly. Its scheduling and escalation are primarily fixed program rules rather than a model-held portfolio mandate. [orchestration](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator.py), [review](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator_review.py), [DAG executor](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/parallel_executor.py).

## Operational model

Individual model-backed implementation agents choose their coding actions through externally installed CLIs under Maestro's first-party task composition. Static orchestration routes actual failure/review evidence to corrective work. The separate reviewer has fresh instructions and direct code inspection, a materially complementary evidence path relative to an implementer's self-report. Those strengths are bounded to local work-unit acceptance: they are not by themselves autonomous coordination, organizational resource choice or future policy creation.

## S1 — Operations

- State: A
- Function: Code-changing task agents implement specified work units and respond to source/tool feedback.
- Disturbance / variety regulated: Requirements, repository state, build/test failures, model response and review-requested revisions.
- Decisive decision or feedback right: Implementation CLI-backed model selects coding steps and edits; revision requests lead to a new model-driven implementation attempt.
- Decision owner: Launched model-driven implementer for local coding decisions, installed into Maestro's first-party work-unit execution route.
- Supporting / enforcement mechanisms: tmux isolation, explicit work-unit spec/DoD, task limits, SQLite persistence, CLI backends and escalation.
- Closure path: User work unit→Maestro spawns implementer→model edits repo files→tests/review results→model revision or final accepted code.
- Boundary reachability: `execute` CLI and orchestrator instantiate real tmux coding agents with configured backends, not just mock or planned actors.
- Why this is / is not agent-owned: Model actor exercises task-level file-change choice; Maestro's fixed phase machine supplies gates, not coding autonomy. External vendor CLI internals are not separately credited.
- Evidence: [orchestrator](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator.py), [tmux manager](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/tmux_manager.py), [CLI](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/cli.py).
- Basis: Shipped runnable model-directed coding process with corrective feedback into implementation.
- Confidence: Medium-high for first-party route; provider runtime effectiveness not independently replayed.
- Caveats: Actual model steps run in separately installed CLI products; first-party evidence is their orchestration contract and returned status, not vendor-harness architecture.

## S2 — Coordination

- State: —
- Function: No separate agent-owned regulation of specifically observed contention between parallel S1 implementation units.
- Disturbance / variety regulated: Dependency readiness, parallel-file collisions and worker resource contention can occur across work units.
- Decisive decision or feedback right: DAG dependency checks and `max_concurrent=4` semaphore select ready waves, but are deterministic ordering, not balancing of detected competing goals.
- Decision owner: Operator for work-unit DAG; Python scheduler for static ordering and concurrency gates.
- Supporting / enforcement mechanisms: Dependency graph, parallel executor, work-unit status, file scope checks and tmux windows.
- Closure path: Predeclared dependency→ready/blocked status; parallel work-unit results→output records, not peer contention evidence→autonomous S2 arbitration→returned adjustments.
- Why this is / is not agent-owned: A queue, DAG and semaphore are supporting coordination machinery but no distinct real-time S2 balancing authority is installed.
- Evidence: [workflow executor](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator.py), [parallel executor](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/parallel_executor.py).
- Basis: Bounded absence despite distinct simultaneous work units.
- Confidence: Medium-high.
- Caveats: Operator can encode dependencies to avoid conflict; not a self-sensing inter-S1 balancing loop.

### Absence scope

- Surfaces inspected: Workflow dependency waves, parallel execution, file scopes and review outcomes.
- Plausible first-party paths checked: DAG as conflict attenuation, concurrency limit as S2, file-scope review as inter-worker arbitration, work-unit split as coordination.
- Why no material first-party path remains: No shipped actor detects inter-S1 disturbance and sends revised shared commitments or attenuation decisions back to the contending units.

## S3 — Inside-and-now control

- State: —
- Function: No model/agent-owned discretionary whole-system management of current operating commitments and resources beyond the authored work-unit sequence.
- Disturbance / variety regulated: Failed unit, bad test result, model timeout, context exhaustion and blocked dependencies.
- Decisive decision or feedback right: Fixed phase gates and escalation ladder retry/fail/advance per unit; code selects ready waves. Model-assisted decomposition serves task shaping, not a portfolio manager with authority over organizational tradeoffs.
- Decision owner: User defines work-unit specs/priority/dependencies; deterministic orchestrator follows configured rules.
- Supporting / enforcement mechanisms: Validator gates, model-tier escalation, retry budget, SQLite status, DAG and GitOps.
- Closure path: Unit failure→preset retry/tier escalation; DAG dependency blocking→recorded status. No autonomous whole-portfolio capacity/priority/commitment renegotiation.
- Why this is / is not agent-owned: Enforceable resource and quality gates are not an independent S3 deciding strategic current tradeoffs; reviewers judge claims, they do not manage fleet priorities.
- Evidence: [phase and escalation machine](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator.py), [escalation rules](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/escalation.py), [decomposition](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/decomposer.py).
- Basis: Bounded absence after testing source-backed execution governance against S3 discretion threshold.
- Confidence: Medium-high.
- Caveats: A future user/controller could wrap Maestro in a portfolio S3, but the standard execution mode owns only per-unit rule machinery.

### Absence scope

- Surfaces inspected: Workflow/parallel DAG, model-tier escalation and work-unit decomposition, validators, SQLite accounting and task CLI.
- Plausible first-party paths checked: Orchestrator as S3 from its name, failure escalation as S3 reallocation, model-assisted decomposition as S3 priority setting, tests as management choice.
- Why no material first-party path remains: The shipped decision rights are static per-unit rules or implementer task judgments, not an independent authority revising whole-system current commitments.

## S3* — Complementary audit

- State: A
- Function: Bounded independent code/spec reality check of implementation claims with a returned review verdict and enforced rework.
- Claim being audited: Implementer asserts its work unit meets the original spec and Definition of Done and presents changed files/output.
- Ordinary reporting path: Implementer process completion text, status, staged changes and routine command/test output feed the orchestrator.
- Complementary access path: Fresh cross-model reviewer agents receive the original spec/DoD and are asked to inspect actual code files and Git diff independently; deterministic validator directly executes source/test checks rather than trust self-report.
- Independence boundary: Reviewer runs in a distinct tmux agent session and model type selected to avoid collision with implementer, but uses the same local repo and is orchestrated by Maestro; no external institution or externally verified truth guarantee.
- Who acts on findings: Orchestrator parses `NEEDS_REVISION` and validation failure, blocks commit and re-enters implementation or escalates model tier; positive evidence can advance to commit.
- Disturbance / variety regulated: Hallucinated completion, incomplete DoD, out-of-scope file changes, security/code-quality defects and misleading model claims.
- Decisive decision or feedback right: Reviewer may reject implementation with file:line evidence, while independent validator can fail executable checks; orchestrator enforces corrective loop.
- Decision owner: Distinct reviewer model owns evidence-based audit judgment; deterministic validator owns command-based test gate; orchestrator routes returned finding.
- Supporting / enforcement mechanisms: Fresh reviewer prompt, different agent type, direct source access, `git diff`, file-scope manifest, test execution, verdict parser and retry/escalation.
- Closure path: Implementer completion claim→fresh independent reviewer reads code/spec (plus test execution/diff)→verdict→orchestrator rejects/requests revision or accepts/commits→new implementation attempt.
- Boundary reachability: The shipped review phase spawns its own tmux reviewer, sends actual work-unit spec/diff/file-scope instructions and persists result; source tests cover review/revision behavior.
- Why this is / is not agent-owned: The reviewer challenges original operational claims with a separately acquired direct file view, not just repackaged implementer prose. The static accept/deny state machine is an enforcement channel.
- Evidence: [review creation and non-colliding model selection](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator_review.py), [reviewer instruction](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/reviewer.py), [orchestrator revision path](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator.py), [validators](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/validators.py).
- Basis: Source-traced alternative direct-code reality access, distinct judgment owner and closed returned correction in normal work-unit mode.
- Confidence: Medium-high for implemented bounded audit route.
- Caveats: Reviewers can err, share upstream tool vulnerabilities or be manipulated by inputs; using a different model does not alone prove independence, and this is not certified external audit.

## S4 — Outside-and-then intelligence

- State: —
- Function: No autonomous future-environment sensing and strategic organizational change loop.
- Disturbance / variety regulated: Changing model quality/prices, future source architecture, toolchain updates and novel task types.
- Decisive decision or feedback right: Operators configure ladder/backend; predictive risk, preflight and dynamic decomposition serve a current task's execution, not future organizational strategy.
- Decision owner: External developer/operator for long-horizon capability changes; per-unit implementer/reviewer for present work.
- Supporting / enforcement mechanisms: Provider ladder, cost tier, prediction, knowledge-base roadmap and context-budget monitoring.
- Closure path: Failure→current retry with a stronger model; offline future development remains manual. No external scanning→future options→policy/operational mandate adjustment.
- Why this is / is not agent-owned: Changing model tier in response to immediate test failures is operational retry, not adaptive prospective environmental intelligence.
- Evidence: [model escalation](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/escalation.py), [prediction](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/predictor.py), [orchestrator](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator.py).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: User can ask Maestro to implement a future plan, which is task-level S1 rather than its organizational S4.

### Absence scope

- Surfaces inspected: Prediction, model tier/escalation, context management, research CLI and proposed knowledge-base feature.
- Plausible first-party paths checked: Prediction as future scanning, model choice as strategic adaptation, research mode as outside intelligence, future knowledge-base roadmap as shipped S4.
- Why no material first-party path remains: No independent prospective organization-level environmental model and adopted strategy feedback path is installed.

## S5 — Policy and identity

- State: —
- Function: No legitimate ultimate identity-policy governing body or returned parent-assisted mandate.
- Disturbance / variety regulated: Unsafe code changes, permission policy, task scope and model/provider credentials.
- Decisive decision or feedback right: User authors work spec/DoD, mode, policies and credentials; validator/reviewer enforce work acceptance rather than determine organizational identity.
- Decision owner: Operator/developer for legitimate policy; deterministic gates and reviewer for local task acceptance.
- Supporting / enforcement mechanisms: Manifest scope, approval mode, preflight DoD quality, explicit backend configuration and commit gate.
- Closure path: User spec/config→bounded operational checks; no identity-level conflict→legitimate charter deliberation→binding mandate into S3/S4.
- Why this is / is not agent-owned: Security and acceptance criteria around a work unit do not constitute self-directed ultimate governance.
- Evidence: [preflight](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/preflight.py), [review](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/orchestrator_review.py), [config](https://github.com/rubin-johnson/maestro/blob/0589ff3b2b0d25baabff196a1dd64c2147048b8e/src/maestro/escalation.py).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: A human owner may be S5 of a deploying team, but not installed as an autonomous or parent-governed Maestro role.

### Absence scope

- Surfaces inspected: Work-unit spec, DoD, permissions, preflight, reviewer conditions, config and safety scope.
- Plausible first-party paths checked: Work spec as charter, adversarial reviewer as S5 policy, model-tier escalation as ultimate authority, fixed manifest as identity control.
- Why no material first-party path remains: These constrain and verify current task output; none owns identity-level mandate decisions with legitimacy and returned lasting authority.

## Recursion

Multiple separate model-backed implementer/reviewer roles and DAG work units do not by themselves imply a recursively viable enterprise. The independent S3* auditor is bounded to work-unit correctness, and the installed scheduler is not a discretionary S3 owner.

## Variety and escalation

Model-provider selection, work-unit decomposition and multiple tmux agents supply task variety. Preflight, executable validation, independent reviewer and scoped commit gate attenuate error. Test/review rejection returns to implementation as corrective feedback; model tier escalation is reactive at the present work-unit horizon, not future-strategy S4.

## Evidence gaps

- Source review and bundled tests cover wiring; live provider-backed tmux agent execution was not replayed here.
- The strongest S3 candidate is the orchestrator's workflow manager, but its demonstrated decisions are largely deterministic DAG/phase/ladder gates rather than discretionary whole-portfolio authority.
- Cross-model reviewer can independently inspect code via tools but still shares local deployment and potential model/provider failure; no institutional independent audit quality claim.
