---
harness_id: microsoft-agent-framework
project_name: Microsoft Agent Framework
repository: https://github.com/microsoft/agent-framework
review_ref: c030fa3582b1d2971488645fa03ec65bffab8617
reviewed_at: 2026-09-16
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: c030fa3582b1d2971488645fa03ec65bffab8617
last_checked_at: 2026-09-16
assessment_changed_at: 2026-09-16
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Microsoft Agent Framework

## Review boundary
Microsoft Agent Framework at the checked revision, focusing on the first-party orchestration package and especially Magentic manager behavior plus its optional human plan-review mode. Generic graph workflows, approval hooks, and manager naming are not sufficient for a VSM mapping; the positive classifications below come from explicit whole-team current-control decision rights.

## Repository architecture
Microsoft Agent Framework provides stateful operational agents and several orchestration patterns. The Magentic implementation is materially stronger than ordinary workflow routing: a manager maintains team-level facts, plan and progress, selects the next worker, detects lack of progress/repetitive behavior, and can reset/replan the team execution. In the standard autonomous mode that closes agent-owned S3. The first-party plan-review mode additionally pauses before execution of each Magentic plan and lets a human approve it or return revision feedback; revision is fed back into the same workflow so the manager replans and execution resumes.

## Primary evidence
- `python/packages/orchestrations/agent_framework_orchestrations/_magentic.py`: manager state includes whole-team facts, plan and progress; the manager selects the next participant/action, monitors execution, detects stalls and can reset/replan current commitments.
- `python/samples/03-workflows/orchestrations/magentic_human_plan_review.py` at `c030fa3582b1d2971488645fa03ec65bffab8617`: `enable_plan_review=True` requests human approval or revision before executing each generated plan; the review request exposes the current progress ledger and proposed plan; `approve()` continues while `revise(feedback)` returns human feedback into the workflow; responses are supplied back until execution completes.
- `dotnet/src/Microsoft.Agents.AI.Workflows/MagenticWorkflowBuilder.cs`: the first-party builder documents `RequirePlanSignoff` as review and approve/revise of plans before execution, separately from participant tool-call approval.
- `dotnet/tests/Microsoft.Agents.AI.Workflows.UnitTests/MagenticOrchestrationTests.cs`: plan-review tests cover human revision triggering a replan rather than merely gating one participant tool call.

## Operational model
Specialist agents perform operational work while an autonomous manager repeatedly interprets whole-team progress, regulates who acts next, and revises the current plan when execution fails to converge. With plan review disabled, that S3 loop is agent-owned. With first-party plan review enabled, a human parent can exercise the decisive approve/revise right over the whole-team current plan before it is executed; revision returns through the Magentic manager into replanning and continued operation.

## S1 — Operations
`A`: specialist agents autonomously perform bounded tool/model work and return operational outcomes. Confidence: high.

## S2 — Coordination
`A`: the Magentic manager actively detects loop/stall/no-progress conditions and changes team execution to restore convergence. This is agent-owned regulation of instability among operational units, not static graph topology. Confidence: high.

## S3 — Inside-and-now control
`A(P)`: the default Magentic manager owns a whole-team current-state ledger of facts/plan/progress, chooses who acts next, and has reset/replan authority over current commitments, establishing an autonomous S3 mode. The first-party plan-review option establishes a second parent-governed mode over the same S3 function: before a plan executes, a human sees the current progress ledger and proposed whole-team plan and may approve it or require revision; revision is returned to the manager, which replans before work continues. This is materially different from participant tool-call approval because it controls the team's current plan itself. Confidence: high.

## S3* — Complementary audit
`—`: the same manager that regulates current work observes progress; no organizationally distinct complementary audit channel with independent access/authority was established.

## S4 — Outside-and-then intelligence
`—`: replanning responds to current execution failure. The reviewed implementation does not establish a separate prospective external-environment intelligence function that adapts future system capability/strategy.

## S5 — Policy and identity
`—`: goals, participants, instructions and orchestration policy remain application-defined. Human signoff on a current Magentic plan is S3 current-control authority, not by itself ultimate organizational identity or policy closure.

## Recursion, variety, escalation
Magentic closes more of the metasystem than ordinary agent frameworks: S2 and autonomous S3 are agent-owned around multiple S1s, while optional human plan review supplies a parent-owned S3 mode. It still lacks evidenced S3*, S4 and S5 closure.