---
harness_id: agentbox
project_name: AgentBox
repository: https://github.com/madarco/agentbox
review_ref: 463a6a0a20176147f0b0dbfa8a261aba5e43cbd6
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentBox

## Review boundary
Pinned AgentBox workspace/runtime manager at `463a6a0a20176147f0b0dbfa8a261aba5e43cbd6`: isolated boxes, supported coding-agent executions, workspace/task storage, manager-session lifecycle, assignment and timeline APIs. Cognition supplied by supported Claude/Codex/other agent backends is counted as operational S1 inside the assembled AgentBox execution boundary; planned autonomous-manager behavior is not.

Contract: Profile `0.2.2`, Methodology `0.3.1`. Generation provenance is not backfilled because the pre-admission proposal did not record it.

## Primary evidence
- [`README.md`](https://github.com/madarco/agentbox/blob/463a6a0a20176147f0b0dbfa8a261aba5e43cbd6/README.md) — isolated coding-agent boxes/runtime surface.
- [`docs/workspaces-tasks-manager-plan.md`](https://github.com/madarco/agentbox/blob/463a6a0a20176147f0b0dbfa8a261aba5e43cbd6/docs/workspaces-tasks-manager-plan.md) — implemented workspace/task/manager infrastructure and explicit boundary between current infrastructure and the planned manager brief.

## Repository architecture
AgentBox runs supported autonomous coding agents in isolated boxes and maintains persistent workspace/task/manager state. It implements task states, assignment reconciliation, manager-session registration/lifecycle and timeline surfaces. The pinned design document explicitly says deciding what each box should do and preventing two boxes from fighting over the same files is still manual; the manager instructions that would group overlapping tasks, create boxes and follow PRs are Phase 4 and planned.

## Operational model
Supported coding agents autonomously execute repository work inside AgentBox-managed environments. AgentBox supplies persistent operational infrastructure around them. At this pin, the organizational choices needed for cross-box coordination/current regulation are not yet implemented as a first-party autonomous or constructor-specific VSM function.

## S1 — Operations
`A`. Supported coding agents autonomously perform coding work inside AgentBox-managed boxes. As with other coding-agent control planes in the Index, external model/backend cognition does not turn the assembled harness operation into `C` when the standard distribution runs autonomous S1 executions. Confidence: high.

## S2 — Coordination
`—`. The design document explicitly states that preventing boxes from fighting over the same files is manual at the pin. Shared task records, assignment fields, isolated boxes and reconciliation are useful infrastructure, but no implemented S2-specific path is shown that detects/attenuates a concrete inter-S1 collision or dependency disturbance and feeds the result back into subsequent box behavior. Confidence: high.

## S3 — Inside-and-now control
`—`. Manager sessions, authoritative task state and lifecycle APIs expose current information/control mechanisms, but the manager's own brief is explicitly planned and absent. The pinned system therefore does not establish a first-party actor with whole-system current view plus discretionary authority over priorities/resources/commitments. Confidence: high.

## S3* — Complementary audit
`—`. Timeline and PR observation surfaces do not establish a sufficiently independent first-party audit judgment with corrective closure. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. No external-and-prospective organizational intelligence/adaptation loop is implemented at the reviewed boundary. Confidence: high.

## S5 — Policy and identity
`—`. User objectives, task creation, approval surfaces and external authority are not themselves a runtime identity/ultimate-policy closure loop. The earlier proposal over-promoted outer human authority to `P`. Confidence: high.

## Recursion, variety, and escalation
Parallel isolated boxes amplify execution variety while process/workspace isolation attenuates some technical collision risk. However isolation is not the missing organizational S2 decision loop: the repository explicitly records cross-box file-overlap grouping as future manager behavior. Manager sessions provide an escalation/control surface without yet closing S3.

## Admission conclusion
Canonical vector: `A — — — — —`.

Pre-admission correction of the stale proposal `C C C — — P`: autonomous supported coding-agent execution establishes S1; generic task/manager primitives do not establish S2/S3; and generic parent authority does not establish S5.