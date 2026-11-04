---
harness_id: orchestragent-orch
project_name: orch
repository: https://github.com/Orchestragent/orchestragent
review_ref: 533d06b440654e0f9c9654c80945a751796747e5
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-04
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# orch

## Review boundary

- System in focus: The installed `orch` CLI and first-party Python orchestrator executing one user specification as a planned, independently test-gated set of coding tasks.
- Purpose and identity: Coordinate model-generated plans, test design, parallel code generation, reviews and integration into a demonstrably test-passing branch.
- Relevant environment: A local Git repository, model providers or coding CLIs, frozen tests, dependency and file conflicts, sandbox/pytest execution, provider rate limits and failures.
- Standard-distribution boundary: The shipped `orchestragent` Python package, planner, task builder, deterministic scheduler, review and rule stores, integration worktrees, and supported provider adapters. External models answer bounded calls; they are not themselves first-party orchestration.
- Credited operating surfaces: [orchestrator](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py), [model decisions](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_ladder.py), [rules](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_rules.py), [reviews](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_review.py).
- Adjacent surfaces excluded: Maintainers' development, test fixtures and benchmark outcomes, user-authored policy, provider internals, externally deployed organizational supervisors.
- Modes considered: Standard plan/execute, concurrent generation, distributed/resumable planning, model-mediated exception review, learned-rule trial; frozen policy mode restricts some automatic adaptation and does not substitute for an S5 parent.
- Recursion level: A complete `orch` specification run containing multiple bounded code-building S1 tasks; no claim that every task is an independently viable organizational recursion.
- Reviewed revision: `533d06b440654e0f9c9654c80945a751796747e5` on 2026-11-04; generated and current Profile 0.2.4 / Methodology 0.3.7.

## Repository architecture

The planner asks a model for task/dependency and test designs and rejects invalid plans using lint and sandbox probes. The scheduler dispatches ready tasks to bounded model-backed builders; each receives file ownership, interface context and tests fixed before implementation. Per-task working-tree commits enter an integration branch only after dependent and frozen-test gates. Failure triggers structured diagnosis, autonomous model exception review, bounded replanning or parking. The system records decisions and test outcomes, and can promote candidate planner/builder lessons from controlled trials for future runs. The API/CLI entry points and persistent stores make these operating loops first-party rather than documentation examples. [README](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/README.md), [orch_run.py#L715-L885](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L715-L885), [orch_run.py#L2170-L2240](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L2170-L2240), [orch_run.py#L3848-L3905](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L3848-L3905).

## Operational model

One planner and a team of temporary task-building model calls operate within a spec run. Model discretion selects plan content, code, exception diagnosis and corrective alternatives, but ownership of dispatch, shared quotas, integration and admission gates remains in deterministic code. Consequently an operating S1 `A` and complementary review `A` need not imply autonomous S2/S3. Rule-generated future adaptation is distinct from current task retry.

## S1 — Operations

- State: A
- Function: Generate and repair code in response to scoped user specification and feedback from tests and model calls.
- Disturbance / variety regulated: Unfamiliar source, incomplete interfaces, implementation errors, rejected model outputs and failing frozen tests.
- Decisive decision or feedback right: Choose a task solution/patch from specification, context and feedback, including changed implementation on failure.
- Decision owner: Model-backed planner and builder calls in the installed run; deterministic code enforces schema, attempts and test acceptance.
- Supporting / enforcement mechanisms: Worktrees, `context_pack`, prompt budgets, frozen tests, provider adaptors, retry ladder.
- Closure path: Model plan → task/test contracts → model patch → sandbox test → accept or issue failure feedback → reattempt/replan/park.
- Boundary reachability: `plan` and `execute` are first-party orchestrator operations reachable through supported CLI.
- Why this is / is not agent-owned: The planner and code model choose substantive task decomposition and edits; the scheduler does not author those solutions.
- Evidence: [orch_run.py#L715-L885](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L715-L885), [orch_run.py#L3247-L3477](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L3247-L3477), [orch_run.py#L3848-L3905](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L3848-L3905).
- Basis: structural
- Confidence: high for a reachable source-level loop; no provider-run success reproduced.
- Caveats: The normal run requires configured model inference and an executable project environment.

## S2 — Coordination

- State: C
- Function: Attenuate interference between parallel code-building units in a shared integration branch.
- Disturbance / variety regulated: File ownership overlap, incompatible dependency interfaces, parallel Git conflicts and tests broken by another worker's merge.
- Decisive decision or feedback right: Coordinate dependency/ownership and merge order, reject a conflicting commit and route the affected task back for a refreshed build.
- Decision owner: Deterministic DAG scheduler, interface and file gates and integration merge lock; no separate autonomous coordination actor owns the arbitration policy.
- Supporting / enforcement mechanisms: Planned dependency edges, serialized integration, affected-test gate, rebase count and changed-worktree tests.
- Closure path: Concurrent task outputs → merge collision/affected tests → reject/rebase/retry of specific task → next task execution on updated integration state.
- Boundary reachability: `execute`, `_ready`, `_merge` are standard paths for concurrent task runs.
- Why this is / is not agent-owned: The collision/feedback witness is function-specific and shipped, but the coordinator's decisive scheduling/merge arbitration is hard-coded; agent-owned S2 would need composition.
- Evidence: [orch_run.py#L2170-L2257](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L2170-L2257), [orch_run.py#L2420-L2475](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L2420-L2475), [orch_run.py#L3848-L3910](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L3848-L3910).
- Basis: structural
- Confidence: medium-high.
- Caveats: Mere DAG edges would not establish S2 without the identified collision-response/return path.

## S3 — Inside-and-now control

- State: C
- Function: Control the complete current spec-run portfolio's admissions, throughput, resource limits and stalled tasks.
- Disturbance / variety regulated: Provider rate-limit pressure, too many active model calls, spend caps, blocked dependencies and repeating module failures.
- Decisive decision or feedback right: Change current concurrency, dispatch priority and task admissions or park a failed module based on observed whole-run state.
- Decision owner: Deterministic scheduler (`_drain`, `_room`, `_throttle`, `_breaker`); models generate tasks but do not autonomously decide whole-system resource intervention.
- Supporting / enforcement mechanisms: AIMD limit, token/cache policies, dependency depth sorting, persistent state, failure counts.
- Closure path: Ready/in-flight state and failure signals → scheduler resource/priority intervention → changed dispatch and retry conditions for multiple tasks.
- Boundary reachability: Standard execution uses `_drain` and applies current `max_jobs`/`max_verify_jobs`, rate and spend gates.
- Why this is / is not agent-owned: A whole-run feedback and resource-decision path exists, but its discretionary control policy is fixed in code, leaving agent ownership uncomposed.
- Evidence: [orch_run.py#L2170-L2294](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L2170-L2294), [orch_run.py#L2451-L2490](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L2451-L2490).
- Basis: structural
- Confidence: medium; no autonomous allocator or qualified human parent mode evidenced.
- Caveats: Ordinary user-set quotas do not independently establish `P` parent governance.

## S3* — Complementary audit

- State: A
- Function: Independently challenge the frozen test contract against the original user specification when task failures indicate a test dispute.
- Disturbance / variety regulated: Wrong or over-constraining tests drafted before implementation, misleading failure attribution and builder attempts to relax constraints.
- Decisive decision or feedback right: An exception-review model independently returns `tests_correct` or `tests_wrong`, with an explanation and guarded test edits; a wrong-test verdict can authorize corrective test revision.
- Decision owner: Separate Claude review invocation using original specification, protected from the builder's own test-edit decision; deterministic code validates the verdict and safe application.
- Supporting / enforcement mechanisms: Immutable review inputs, durable review store, assertion-count no-weakening gate and regression check of already merged tasks.
- Closure path: Failed worker/test dispute → independent review → validated finding → corrected frozen tests or rejection → saved candidate reverified / task retried.
- Boundary reachability: `_review` and `_fix_tests` are first-party retry-ladder operations; their execution is conditional, not an asserted always-on audit.
- Why this is / is not agent-owned: The reviewer has the substantive adjudication right; the builder cannot directly alter the pre-frozen test contract, while code checks and transports the verdict.
- Evidence: [orch_run.py#L3010-L3140](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L3010-L3140), [orch_review.py](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_review.py).
- Basis: structural
- Confidence: medium-high for the dispute-triggered complementary path.
- Caveats: Independence is functional/prompt-and-role separation, not a demonstrated separate provider organization; ordinary final pytest gates alone would not establish `A`.

## S4 — Outside-and-then intelligence

- State: A
- Function: Learn prospective planning/building-rule changes from accumulated cross-run failures and outcomes, and return successful changes into future model prompts.
- Disturbance / variety regulated: Repeating planning defects, weak tests, recurring builder mistakes and the possibility that a proxy for eventual success becomes misleading.
- Decisive decision or feedback right: Model review/replanning/build attempts formulate generalizable lessons; A/B evidence evaluates whether a candidate helps, with checkpoint promotion and subsequent prompt influence.
- Decision owner: Autonomous models propose the adaptive rule content from task observations; deterministic promotion statistics retain activation veto, so the agent does not own final promotion discretion in isolation.
- Supporting / enforcement mechanisms: `Rule` store, paired trials and replay, proxy-vs-real Spearman trust test, lifecycle `candidate → active → retired` and prompt layer budget.
- Closure path: Outcomes and model lessons from earlier runs → candidate rule → with/without evaluation → promote/retire at checkpoint → altered next-plan/builder instruction.
- Boundary reachability: `_learn`, `evolve`, `_settle_planner_rules` and builder rule trials are first-party modes (automatic rule learning disabled in frozen-policy modes).
- Why this is / is not agent-owned: Autonomous models originate strategic adaptation content, not merely execute a preselected fixed retry; promotion is a statistical safeguard rather than a model-authored option.
- Evidence: [orch_run.py#L1570-L1775](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L1570-L1775), [orch_run.py#L3888-L3925](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L3888-L3925), [orch_rules.py#L1-L125](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_rules.py#L1-L125).
- Basis: structural
- Confidence: medium for prospectively reusable operating-policy learning; causal effectiveness not independently reproduced.
- Caveats: Feedback comes chiefly from past run/task outcomes, not market sensing. If an evaluator requires a wholly independent outside-environment sensor rather than cross-run experience, S4 should be revisited; the observed loop is durable future capability change, not just current repair.

## S5 — Policy and identity

- State: —
- Function: No first-party whole-system identity or ultimate-policy dispute and legitimate-authority closure is evidenced for a spec-run organization.
- Disturbance / variety regulated: Unsafe workspace edits, mismatched model routes, insufficient budgets and altered test contracts are addressed as operational guardrails.
- Decisive decision or feedback right: Bind an ultimate policy/identity judgment to later operations; no such accountable agent or legitimate parent governance loop is shipped.
- Decision owner: User chooses configuration and optional frozen policy; model reviews resolve tests and task strategy, not organizational identity.
- Supporting / enforcement mechanisms: Policy store, sandbox boundary, explicit model settings, pinned planning inputs, cancel/park limits and review gate.
- Closure path: Configuration and safety gates constrain a run; no S5-level issue/appeal → authoritative decision → returned binding identity policy.
- Why this is / is not agent-owned: Guarded model choices and an immutable execution policy are not themselves an S5 constitutional decision.
- Evidence: [orch_policy.py](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_policy.py), [orch_run.py#L715-L815](https://github.com/Orchestragent/orchestragent/blob/533d06b440654e0f9c9654c80945a751796747e5/src/orchestragent/orch_run.py#L715-L815).
- Basis: structural
- Confidence: medium-high.
- Caveats: Maintainer policy and a human's optional local run selection are outside this selected recursion.

### Absence scope

- Surfaces inspected: Policy store, CLI/planning overrides, pinned inputs, run state, audit/review and model escalation ladder.
- Plausible first-party paths checked: Frozen policy, user-supplied limits, Claude exception review, sandbox permissions and project-maintainer rules.
- Why no material first-party path remains: Each path selects/enforces task constraints or resolves test/plan failures, without an explicitly identity-level decision returned by a legitimate ultimate authority.

## Distributed OSS parent arrangement

Repository maintainers and local operators can change runtime policy but no public first-party organization-level S3/S4/S5 parent governance mode for this individual `orch` spec run was inferred merely from development or installation rights.

## Self-hosted and non-human modes

Local model/CLI adapters and provider services supply planning/building/review cognition. Neither those external providers nor their infrastructure is credited as an additional VSM system; pinned-policy modes disable some automatic learning.

## Recursion

The whole specification run owns a portfolio of S1 building tasks. Each task is a bounded model operating cell, not automatically a viable suborganization; the agent-written plan is not itself an S5 constitution.

## Variety and escalation

Planner samples, model builders and bounded retry tiers amplify implementation variety. Frozen tests, isolated worktrees, ownership constraints, merge gates and rate/spend caps attenuate it. When a test contract is challenged, the independent review path returns a corrective verdict; sustained provider failures park work instead of inventing success.

## Evidence gaps

- No paid-provider end-to-end run, statistical learning gain or actual S3* adjudication was reproduced; autonomy states describe wired source-level decisions, not effectiveness.
- The future-facing learning loop uses past internal run results, with conditional promotion; its external environmental reach and realized generalization remain unvalidated.
