---
harness_id: vibe-kanban
project_name: Vibe Kanban
repository: https://github.com/BloopAI/vibe-kanban
review_ref: 735654971bd396aa97b65166955678e4c34f8bf8
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Vibe Kanban

## Review boundary
The system-in-focus is Vibe Kanban's first-party execution/session/workspace control plane around supported coding-agent executors. External coding agents supply S1 cognition; Vibe Kanban-owned sessions, workspaces, process admission, chained actions, queues and lifecycle control are included. The user/operator owns task initiation, review/PR and interruption decisions.

## Repository architecture
Vibe Kanban persists workspaces, sessions, coding-agent turns and execution processes. Successful executions can trigger constructor-defined next actions or queued user follow-ups; failed/killed runs terminate continuation. Across sessions sharing a workspace, non-dev execution is mutually excluded. Review is another user-started coding-agent execution rather than an independently authoritative audit subsystem.

## Primary evidence
- [`crates/server/src/routes/sessions/mod.rs`](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/server/src/routes/sessions/mod.rs#L105-L225): creates/resumes coding-agent execution bound to workspace/session.
- [`crates/db/src/models/execution_process.rs`](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/db/src/models/execution_process.rs#L290-L315): detects running non-dev processes across sessions in a workspace.
- [`crates/server/src/routes/sessions/review.rs`](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/server/src/routes/sessions/review.rs#L35-L125): review admission excludes concurrent work and launches an ordinary coding-agent execution.
- [`crates/local-deployment/src/container.rs`](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/local-deployment/src/container.rs#L560-L675): success triggers commit/next action/follow-up; failure/kill finalizes without continuation.
- [`crates/server/src/routes/workspaces/pr.rs`](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/server/src/routes/workspaces/pr.rs#L145-L300): PR creation is an explicit parent-facing action.

## Operational model
The parent creates work and chooses an executor. An autonomous coding agent performs the task. Vibe Kanban regulates workspace concurrency, process lifecycle and deterministic continuation. Review is available on demand but has no separate gating/corrective authority over the original S1.

## S1 — Operations
`A`: configured coding agents execute substantive coding work autonomously and may continue an existing session. Proof: [session execution](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/server/src/routes/sessions/mod.rs#L105-L225). Confidence: high.

## S2 — Coordination
`C`: runtime enforces workspace-wide mutual exclusion across operational sessions, preventing concurrent non-dev processes from mutating the same workspace. Proof: [workspace exclusion](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/db/src/models/execution_process.rs#L290-L315), [review admission](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/server/src/routes/sessions/review.rs#L35-L60). Confidence: high.

## S3 — Inside-and-now control
`C`: admission, execution state, success/failure continuation and queued follow-up rules regulate current operation under constructor/runtime policy. Proof: [continuation/failure gating](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/local-deployment/src/container.rs#L560-L675), [execution exclusion](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/db/src/models/execution_process.rs#L290-L315). Confidence: high.

## S3* — Complementary audit
`—`: review is parent-invoked and launched as another coding-agent execution; no separate decision is shown gating/correcting/escalating original work. Proof: [review launch](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/server/src/routes/sessions/review.rs#L35-L125). Confidence: high.

## S4 — Outside-and-then intelligence
`—`: follow-ups, resume, chained actions, review and recovery operate on current work/continuity rather than prospective organizational adaptation. Proof: [current continuation](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/local-deployment/src/container.rs#L560-L675). Confidence: high.

## S5 — Policy and identity
`P`: the parent explicitly initiates review and PR creation; autonomous completion does not establish approval/merge authority. Proof: [parent review](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/server/src/routes/sessions/review.rs#L35-L125), [PR action](https://github.com/BloopAI/vibe-kanban/blob/735654971bd396aa97b65166955678e4c34f8bf8/crates/server/src/routes/workspaces/pr.rs#L145-L300). Confidence: high.

## Recursion, variety, escalation
Workspace isolation/exclusion serialize conflicting mutation. Sessions preserve independent operational contexts; failure/kill stops queued progression. Review and PR decisions return higher-level authority to the parent. Multiple sessions do not imply recursive VSM closure.

## Deep-review conclusion
Signature at the pinned revision: `A C C — — P`. Vibe Kanban closes genuine workspace-level S2 and deterministic S3, while its named review facility does not meet independent S3* criteria.