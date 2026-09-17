---
harness_id: vibe-kanban
project_name: Vibe Kanban
repository: https://github.com/BloopAI/vibe-kanban
review_ref: 735654971bd396aa97b65166955678e4c34f8bf8
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Vibe Kanban

## Review boundary
Pinned Vibe Kanban coding-agent workspace/control-plane distribution: supported autonomous coding-agent executions, isolated workspaces, workspace-global concurrency exclusion, execution/follow-up lifecycle and operator review/PR surfaces. Deterministic lifecycle management and human merge authority are not promoted into higher VSM functions without function-specific closure.

Reviewed revision: `735654971bd396aa97b65166955678e4c34f8bf8`. Contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`crates/db/src/models/execution_process.rs`](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/db/src/models/execution_process.rs) — workspace-global active execution lookup used to exclude incompatible concurrent work.
- [`crates/local-deployment/src/container.rs`](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/local-deployment/src/container.rs) — coding-agent execution, follow-up queuing and success/failure lifecycle.

## S1 — Operations
`A`. Supported coding agents autonomously modify repositories inside Vibe Kanban-managed executions/workspaces. Confidence: high.

## S2 — Coordination
`C`. The runtime structurally excludes conflicting concurrent active execution in a workspace, attenuating the concrete disturbance of simultaneous mutation of the same operational workspace. This is deterministic/runtime-owned coordination rather than an autonomous S2 actor. Confidence: medium-high.

## S3 — Inside-and-now control
`—`. Execution status, follow-ups and lifecycle transitions supervise individual runs but do not establish a separate whole-organization regulator owning shared current priorities/resources/commitments. Confidence: high.

## S3* — Complementary audit
`—`. Review/diff surfaces and human feedback are useful inspection mechanisms, but no materially independent first-party audit channel with autonomous corrective closure was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. No prospective environment-facing adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`. Human review, PR creation and merge authority are task acceptance/control surfaces, not an organizational identity/ultimate-policy loop. Confidence: high.

## Recursion, variety, and escalation
Multiple coding-agent sessions amplify execution variety. Workspace separation/concurrency exclusion attenuates collision risk; follow-ups and operator intervention provide execution escalation without closing S3/S5.

## Admission conclusion
Canonical vector: `A C — — — —`.

The earlier stale proposal `A C C — — P` over-promoted deterministic lifecycle supervision into S3 and human PR/merge authority into S5.