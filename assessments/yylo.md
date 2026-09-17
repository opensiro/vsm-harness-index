---
harness_id: yylo
project_name: YYLO
repository: https://github.com/yylo-dev/yylo
review_ref: 93abebf1a787bd1d6c14677d0766e64361bda1ae
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# YYLO

## Review boundary

- System in focus: the first-party YYLO coding-agent orchestration CLI and repository-local managed runtime at pinned revision `93abebf1a787bd1d6c14677d0766e64361bda1ae`.
- Purpose and identity: orchestrate coding-agent work through explicit task worktrees, bounded parallel execution, validation/evidence, review, and protected native-Git delivery boundaries.
- Relevant environment: target Git repository, external model/provider-backed coding agents, separately installed YYLO Ledger/Benchmark packages, and separately authorized push/release/deploy actors.
- Standard-distribution boundary: first-party CLI, managed scripts, controller instructions, task/worktree lifecycle, managed worker/reviewer launcher, risk/review policy and native delivery adapter. Ledger and Benchmark are separate packages and are not credited as bundled implementations.
- Recursion level: one YYLO-managed repository/task organization containing one or more coding-agent task S1s.
- Reviewed revision: `93abebf1a787bd1d6c14677d0766e64361bda1ae` (2026-09-16).
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Primary evidence

- [`README.md`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/README.md) — stated system boundary, agent/task/workflow/validation/native-delivery surfaces, and separation from Ledger/Benchmark.
- [`capabilities.json`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/capabilities.json) — evidence-backed capability boundary: autonomous agent runs, task worktrees, parallel execution, exact-input evidence, native delivery, and explicit separation of tests/reviews from merge.
- [`src/templates/scripts/parallel_runner.sh`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/src/templates/scripts/parallel_runner.sh) — bounded parallel dispatch of multiple agent/task executions.
- [`src/templates/scripts/merge_queue.py`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/src/templates/scripts/merge_queue.py) — one-task native-Git composition, conflict preservation, expected-old target updates, explicit `CONFLICT`/`TARGET_MOVED` feedback and retry/recomposition path.
- [`src/templates/controller-agent/AGENTS.md`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/src/templates/controller-agent/AGENTS.md) — controller/task/delivery ownership boundaries and explicit statement that native delivery does not choose reviewers or own repair.
- [`src/templates/wiki/controller/task_dependency_hydration.md`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/src/templates/wiki/controller/task_dependency_hydration.md) — exact-base per-task worktree preparation and fail-closed readiness isolation.
- [`src/templates/wiki/controller/parallel_runner_and_spec_review.md`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/src/templates/wiki/controller/parallel_runner_and_spec_review.md) — independent semantic-review boundary, frozen candidate, distinct reviewer/repair roles and returned findings.
- [`src/templates/scripts/managed_agent_runner.py`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/src/templates/scripts/managed_agent_runner.py) — separate managed reviewer process, exact candidate/policy binding, bounded structured findings and `pass|findings` verdict.
- [`src/templates/scripts/risk_policy.py`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/src/templates/scripts/risk_policy.py) — deterministic risk/reviewer policy and evidence binding.
- [`src/templates/prompts/review_commit_parallel_runner.md`](https://github.com/yylo-dev/yylo/blob/93abebf1a787bd1d6c14677d0766e64361bda1ae/src/templates/prompts/review_commit_parallel_runner.md) — reviewer independence, full-candidate scope, structured findings and separation from repair/mutation.

## Repository architecture

YYLO wraps external coding-agent backends in a local orchestration/control plane. Agent tasks execute in explicit task worktrees, can be dispatched in bounded parallel batches, and move through typed task state before one selected immutable task is composed into the protected target by native Git. The native delivery adapter deliberately performs no model calls, reviewer selection or test scheduling. Separately, the repository ships managed reviewer machinery: a fresh read-only reviewer is bound to an exact frozen candidate and policy identity, emits a bounded structured verdict/findings object, and is kept separate from the actor that repairs findings.

The distinction matters for classification: the task/worktree/native-Git layer supplies deterministic coordination structure, while semantic review is a supplied composable organizational path whose activation and final repair disposition remain project/workflow-owned.

## Operational model

Coding-agent processes are the S1 units: they autonomously implement or analyze assigned work through the selected backend. YYLO can run several task S1s concurrently while isolating their mutable repository state in task worktrees. Native delivery later composes one immutable task source against the current target and returns explicit conflict/target-movement state when independently developed work cannot be safely composed.

## S1 — Operations

- State: `A`.
- Function: autonomous coding/analysis execution through a selected external agent backend under YYLO invocation/session/task boundaries.
- Disturbance / variety regulated: repository/task uncertainty, tool results and evolving implementation state.
- Decisive right / owner: the model-driven coding agent selects operational actions inside its task/worktree boundary.
- Supporting mechanisms: sessions, task worktrees, bounded command/workflow runners, validation/evidence surfaces.
- Closure: agent actions change task-local repository state and subsequent agent turns consume those results.
- Evidence / basis: README/capabilities plus managed agent and parallel-runner surfaces; explicit/structural.
- Confidence: high.

## S2 — Coordination

- State: `C`.
- Function: attenuate interference among independently executing task S1s at the shared repository/delivery boundary.
- Concrete disturbance: parallel task S1s may produce overlapping/divergent Git changes or attempt composition after the protected target moves.
- Detection / attenuation: task worktrees isolate mutable execution; native delivery composes exactly one immutable task source, detects Git conflicts, refuses stale expected-target updates and records `CONFLICT` or `TARGET_MOVED` instead of silently overwriting shared state.
- Feedback closure: conflict state, preserved candidate worktree/receipt and explicit recomposition/continue command return the disturbance to the task/delivery path before a later landing attempt.
- Decisive right / owner: deterministic first-party Git/task machinery supplies this regulation; it is therefore Constructor-owned rather than agent-owned.
- Why not S3: selecting/serializing one task and enforcing safe composition does not itself create a whole-system discretionary current-regulation actor.
- Confidence: high.

## S3 — Inside-and-now control

- State: `—`.
- The repository exposes controller metadata, task/Kanban state, bounded parallel dispatch, status surfaces and an authorized target-owner delivery path, but the reviewed first-party path does not establish a distinct actor with both a whole-system current view and discretionary authority to reallocate priorities/resources/commitments across the live task organization.
- `controller`, `coordinator`, queue/task state and merge ownership are therefore not promoted by name. Native delivery is explicitly non-model-driven and owns no reviewer/repair loop.
- Confidence: medium-high.

## S3* — Complementary audit

- State: `C`.
- Function: independently challenge a frozen implementation candidate against explicit requirements and supported behavior.
- Independence: the managed reviewer runs in a fresh `yy pi` context, is bound to the exact candidate/policy/reviewer sequence, and is explicitly forbidden to edit, commit, update Kanban, mutate refs/worktrees, launch another reviewer or repair its own findings.
- Evidence / judgment: it must inspect the complete frozen candidate and emit a bounded structured `pass|findings` verdict with cited contract, paths/symbols, evidence, impact, failure condition and acceptance condition. High-risk policy can require two sequential independent reviewers against the same frozen candidate.
- Corrective closure: findings return to the project review/orchestrator path; the review contract assigns repair to a separate repair owner, after which validation/review can be rerun against the replacement candidate. Replacement tips invalidate prior review evidence.
- Decisive right / owner: YYLO supplies the independent reviewer launcher, schema, binding and review/repair protocol, but review activation and final disposition are project/workflow policy choices rather than an always-closed autonomous harness owner. This is therefore `C`, not `A`.
- Confidence: high.

## S4 — Outside-and-then intelligence

- State: `—`.
- Workflow evidence reuse, risk classification, sessions, project discovery and validation react to current repository/workflow state. No first-party loop was established that senses the external future environment, generates prospective adaptation options and returns them into present organizational capability.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- Risk policy, provider/model allowlists, task requirements, human target-owner authority and separate push/release/deploy authorization constrain execution. They do not establish an operationally closed identity/ultimate-policy tension-resolution function. Generic human authorization is not `P`.
- Confidence: high.

## Recursion, variety, and escalation

Parallel Runner and managed agents amplify operational variety by allowing several coding/review actors. Per-task worktrees, exact-base hydration, typed lifecycle state and native-Git composition attenuate shared-state variety. Conflicts/target movement are escalated as explicit task/delivery state rather than silently resolved. Semantic-review findings travel through an intentionally separate audit-to-repair path. Spawning or batching agents is not itself counted as VSM recursion.

## Admission conclusion

Canonical vector: `A C — C — —`.

The two positive metasystem states rest on different evidence boundaries: S2 is deterministic constructor-owned repository-interference regulation; S3* is a supplied composable independent semantic-review channel. Controller naming, generic orchestration, validation, learning-like evidence reuse and parent authority are not promoted to S3/S4/S5.