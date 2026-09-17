---
harness_id: roo-code
project_name: Roo Code
repository: https://github.com/RooCodeInc/Roo-Code
review_ref: b867ec9145750d0ae1ff7f02d35406e9bf2a0b16
reviewed_at: 2026-09-15
status: included
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: b867ec9145750d0ae1ff7f02d35406e9bf2a0b16
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Roo Code

## Review boundary
Deep review of Roo Code at the pinned revision, including its first-party child-task mechanism. Delegation is evaluated separately from S2 coordination and S3 control.

## Repository architecture
Roo Code is an autonomous coding harness with modes, tools and explicit task delegation. `NewTaskTool` creates a child task in a selected mode and links it to the parent task so work can be decomposed and later returned. That is a genuine hierarchical execution primitive, but no separate metasystem function is evidenced for regulating interference among multiple autonomous S1 units.

## Primary evidence
- `src/core/tools/NewTaskTool.ts`: creates delegated child tasks/modes, establishes the parent-child relationship and transfers scoped work into the child execution context.
- `README.md`: documents autonomous coding/tool use and configurable modes that bound agent behavior.

## Operational model
A coding agent performs task work through tools and can split selected work into a child task running under another mode. The parent-child relationship structures decomposition and return of work.

## S1 — Operations
`A`: the normal coding agent autonomously selects/executes tools and reacts to results inside configured permissions. Confidence: high.

## S2 — Coordination
`—`: `new_task` is parent-to-child delegation. The reviewed implementation does not show a distinct function that regulates conflicts, oscillation or shared constraints between multiple autonomous S1 units.

## S3 — Inside-and-now control
`—`: parent task ownership and child-task lifecycle do not establish whole-system current authority over resources/commitments across multiple S1 units.

## S3* — Complementary audit
`—`: no independent/complementary audit path distinct from the normal operational hierarchy was established.

## S4 — Outside-and-then intelligence
`—`: mode selection and task decomposition are current-task planning, not a separate prospective environment-intelligence/adaptation function.

## S5 — Policy and identity
`—`: modes, permissions, rules and task goals are configured by the user/developer. No autonomous ultimate policy/identity authority is present.

## Recursion, variety, escalation
Child tasks provide recursive operational decomposition and can specialize behavior by mode. Under the profile this is not enough to infer any metasystem function.