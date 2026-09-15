---
harness_id: looptroop
project_name: LoopTroop
repository: https://github.com/looptroop-ai/LoopTroop
review_ref: b96f5448251cbe88cd845cd5f262adda02701413
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# LoopTroop

## Review boundary
LoopTroop at the pinned revision as the local ticket-to-PR pipeline using LLM councils, bead executors, auto-fix loops and final verification.

## Repository architecture
Planning interviews produce PRDs/beads; LLM councils help plan; isolated beads execute through repeated fix/test loops in OpenCode worktrees; a final verification/review phase can generate fresh ticket-level tests and persist verification artifacts.

## Primary evidence
- `README.md`: planning/execution/shipping layers; LLM councils; isolated bead execution; automated testing/fix loops and final verification.
- `server/workflow/phases/verificationPhase.ts`: verification is a distinct post-execution phase that generates/executes final-test artifacts, captures file effects and persists verification evidence rather than relying only on bead-worker self-report.
- `server/prompts/index.ts`: the final-test prompt explicitly asks for a comprehensive test/suite validating the whole ticket and requires re-reading ticket/PRD/bead artifacts, providing a constructor path to complementary evidence.

## Operational model
Bead executors are S1 units. Planning decomposes work into non-overlapping units and worktree isolation prevents mechanical collisions, but that is not agent-owned S2 mutual adjustment. Final ticket verification adds an alternative evidence path after implementation, while its closure remains pipeline-composed.

## S1 — Operations
`A`: executors autonomously implement/fix/test bounded beads. Confidence: high.

## S2 — Coordination
`—`: planned isolation/sequencing is task decomposition and deterministic collision avoidance, not an autonomous coordination role among S1s.

## S3 — Inside-and-now control
`—`: the workflow engine sequences phases and recovery mechanically; councils plan and bead agents execute, but no autonomous actor is shown with a whole-system current view and authority over shared operational resources/commitments.

## S3* — Complementary audit
`C`: the standard pipeline supplies a distinct final-test/review path that can generate fresh ticket-level tests and inspect persisted implementation artifacts after bead execution, providing materially different evidence from worker self-report. It is still a pipeline-composed verification mechanism rather than a clearly independent autonomous audit authority, so it is constructor-level rather than `A`. Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`: councils, PRD refinement and implementation planning concern the current ticket; no external-and-prospective environment model develops organizational adaptation options coupled to S3.

## S5 — Policy and identity
`—`: ticket intent, interview answers, approvals and workflow configuration remain human/application owned; no agent has legitimate ultimate-policy closure.

## Recursion, variety, escalation
Beads/worktrees are operational partitions, not recursion.