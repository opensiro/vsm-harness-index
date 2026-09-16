---
harness_id: agentbox
project_name: AgentBox
repository: https://github.com/madarco/agentbox
review_ref: 463a6a0a20176147f0b0dbfa8a261aba5e43cbd6
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: C
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# AgentBox

## Review boundary
Pinned hub/runtime with isolated boxes, workspace/task store, manager sessions and assignment lifecycle; external agents provide cognition.

## Repository architecture
AgentBox owns task states (`todo`, `in_progress`, `blocked`, `done`), assignments, assignment healing, manager sessions and timeline state across isolated boxes.

## Primary evidence
- Pinned deep review established shared task/assignment state, healing, manager sessions and timeline at `review_ref`.

## Operational model
External agents execute S1 work while AgentBox provides persistent shared operational state and constructor-owned control primitives.

## S1 — Operations
`C`: external agents supply operational cognition. Confidence: high.

## S2 — Coordination
`C`: shared tasks, assignments and healing provide composable coordination. Confidence: high.

## S3 — Inside-and-now control
`C`: authoritative current task/assignment state and manager-session controls provide current regulation. Confidence: high.

## S3* — Complementary audit
`—`: no independent audit channel with corrective closure was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective organizational adaptation function was established. Confidence: high.

## S5 — Policy and identity
`P`: outer objectives/authority remain parent-owned. Confidence: high.

## Recursion, variety, escalation
Isolation and explicit blocked states attenuate operational interference; the autonomous-manager brief remained planned rather than standard at the pin.

## Deep-review conclusion
Signature at the pinned revision: `C C C — — P`. AgentBox is a composable current-control substrate around externally intelligent agents.