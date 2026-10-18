---
harness_id: ruflo
project_name: Ruflo
repository: https://github.com/ruvnet/ruflo
review_ref: 2602b642d92234c710ffbe96bfb33007d481ceab
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Ruflo

## Review boundary
Pinned Ruflo meta-harness/orchestration distribution, including the documented Codex execution mode, swarm coordinator, dependency/worktree controls, policy envelope, and learning bridge. Deployment-authored domain roles and ultimate organizational policy are not credited merely because Ruflo can host them.

Reviewed revision: `2602b642d92234c710ffbe96bfb33007d481ceab`. Contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`README.md`](https://github.com/ruvnet/ruflo/blob/2602b642d92234c710ffbe96bfb33007d481ceab/README.md) — swarm/meta-harness boundary and supported execution surfaces.
- [`v3/@claude-flow/codex/README.md`](https://github.com/ruvnet/ruflo/blob/2602b642d92234c710ffbe96bfb33007d481ceab/v3/%40claude-flow/codex/README.md) — standard `init --codex` mode, with Ruflo as orchestrator and Codex as autonomous executor.
- [`v3/@claude-flow/swarm/src/unified-coordinator.ts`](https://github.com/ruvnet/ruflo/blob/2602b642d92234c710ffbe96bfb33007d481ceab/v3/%40claude-flow/swarm/src/unified-coordinator.ts) — whole-swarm assignment, topology, health, recovery and resource-control primitives.
- [`v3/docs/adr/ADR-324-agentic-policy-engine-codex-swarm.md`](https://github.com/ruvnet/ruflo/blob/2602b642d92234c710ffbe96bfb33007d481ceab/v3/docs/adr/ADR-324-agentic-policy-engine-codex-swarm.md) — dependency-ordered work, isolated writer worktrees, designated integration ownership, policy and budget controls.
- [`v3/@claude-flow/memory/src/learning-bridge.ts`](https://github.com/ruvnet/ruflo/blob/2602b642d92234c710ffbe96bfb33007d481ceab/v3/%40claude-flow/memory/src/learning-bridge.ts) — retrospective trajectory/reward consolidation used to test the old S4 claim.

## S1 — Operations
`A`. In the documented Codex mode, autonomous Codex workers perform the operational coding/tool-execution loop while Ruflo supplies the surrounding orchestration. This is a supported standard-distribution path rather than a developer-only constructor hook. Confidence: high.

## S2 — Coordination
`C`. Ruflo supplies a concrete inter-worker coordination membrane beyond generic messaging: dependency ordering, isolated writer worktrees, designated ownership of shared integration files, topology/consensus primitives, and failure/recovery routing constrain concurrent-worker interference. The decisive organizational coordination policy remains a constructor/configuration surface rather than a demonstrated autonomous S2 actor, so the path is composable rather than `A`. Confidence: medium-high.

## S3 — Inside-and-now control
`C`. The unified coordinator maintains current swarm state and exposes assignment/reassignment, health/recovery, topology, concurrency/budget and policy-envelope controls over the whole active swarm. These are genuine current-regulation decision rights, but the reviewed standard path does not establish an autonomous agent as the owner of those whole-system decisions. Confidence: medium-high.

## S3* — Complementary audit
`—`. Validation, consensus, security and monitoring paths were not shown to provide materially independent access to operational reality with complementary corrective closure. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. The learning bridge consolidates internal trajectories, rewards, confidence and memory. That is retrospective self-improvement inside the operating history, not evidence of an outside-looking prospective intelligence loop that adapts the organization to a changing external environment. Confidence: high.

## S5 — Policy and identity
`—`. Deterministic policy rules, approval gates and deployment configuration constrain operation but do not establish a first-party identity/ultimate-policy tension-and-resolution loop. Confidence: high.

## Recursion, variety, and escalation
Swarm topology, domain pools and nested workers amplify operational variety; dependency/worktree controls, budgets and recovery paths attenuate it. The framework can host recursive organizations, but viable closure at each recursion level remains deployment-specific.

## Admission conclusion
Canonical vector: `A C C — — —`.

Same-ref correction of historical `C C C — C —`: S1 is autonomous in the supported Codex execution mode, while internal learning no longer counts as S4 under the current function-first test.