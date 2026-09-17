---
harness_id: opencode
project_name: OpenCode
repository: https://github.com/anomalyco/opencode
review_ref: 95daf90670b7c039c436c85537da5fbfe2205b41
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 5a8335857b0ebec44ef6aa1d52b339cf25c329ca
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenCode

## Review boundary
Deep review of the pinned built-in task/subagent mechanism and coding-agent runtime. Delegation to a general subagent is not mapped to S2 without a distinct coordination responsibility.

## Repository architecture
OpenCode provides autonomous coding agents and a built-in task tool that invokes a selected subagent in a child session for scoped work. The parent supplies the task, the child executes in its own agent context, and the result returns to the caller. This is hierarchical operational decomposition rather than peer coordination.

## Primary evidence
- `packages/opencode/src/tool/task.ts`: selects a subagent, creates/uses a child session, passes the delegated description/context and returns the subagent result to the parent execution.
- The task tool structures delegation but does not implement interference regulation across autonomous operational units.

## Operational model
A primary coding agent executes repository work through tools and can delegate bounded exploration or multistep work to a specialist/general subagent before resuming from the returned result.

## S1 — Operations
`A`: coding agents autonomously choose tools/actions and iterate against repository/tool feedback. Confidence: high.

## S2 — Coordination
`—`: the task/subagent primitive is parent-to-child delegation. No first-party mechanism was found whose responsibility is regulating interference, oscillation or shared constraints among multiple autonomous S1 units. The shallow `S2=A` interpretation is removed.

## S3 — Inside-and-now control
`—`: parent session control over delegated work is not whole-system current regulation of shared organizational resources/capacity/commitments.

## S3* — Complementary audit
`—`: no distinct complementary audit channel was established.

## S4 — Outside-and-then intelligence
`—`: exploration/planning is directed at the present coding objective rather than prospective environment intelligence.

## S5 — Policy and identity
`—`: agents, modes, tools and policies remain user/developer configured.

## Recursion, variety, escalation
Child sessions and subagents provide recursive specialization without supplying S2–S5 organizational closure.