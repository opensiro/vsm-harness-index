---
harness_id: looptroop
project_name: LoopTroop
repository: https://github.com/looptroop-ai/LoopTroop
review_ref: b96f5448251cbe88cd845cd5f262adda02701413
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# LoopTroop

## Review boundary
LoopTroop at the pinned revision as the local ticket-to-PR pipeline using LLM councils, bead executors, auto-fix loops and final verification.

## Repository architecture
Planning interviews produce PRDs/beads; LLM councils help plan; isolated beads execute through repeated fix/test loops in OpenCode worktrees; a final verification/review pass closes the ticket.

## Primary evidence
- `README.md`: planning/execution/shipping layers; LLM councils; isolated bead execution; automated testing/fix loops and final verification.

## Operational model
Bead executors are S1 units. Planning decomposes work into non-overlapping units and worktree isolation prevents mechanical collisions, but that is not agent-owned S2 mutual adjustment.

## S1 — Operations
`A`: executors autonomously implement/fix/test bounded beads. Confidence: high.

## S2 — Coordination
`—`: planned isolation/sequencing is task decomposition and deterministic collision avoidance, not an autonomous coordination role among S1s.

## S3 — Inside-and-now control
`?`: pipeline orchestration does not establish an agent-owned whole-system regulator.

## S3* — Complementary audit
`?`: final verification/review exists, but the reviewed README does not establish sufficient evaluator independence/alternative reality access for `A/C`.

## S4 — Outside-and-then intelligence
`?`: planning is not S4.

## S5 — Policy and identity
`?`: human interview/configuration owns project intent.

## Recursion, variety, escalation
Beads/worktrees are operational partitions, not recursion.