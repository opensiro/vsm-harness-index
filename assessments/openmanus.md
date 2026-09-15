---
harness_id: openmanus
project_name: OpenManus
repository: https://github.com/FoundationAgents/OpenManus
review_ref: 3309bf4e416fb1c74b008f3e86494439a31bad53
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenManus

## Review boundary
Deep review of the pinned OpenManus flow implementation, especially planning and agent assignment. Task planning is distinguished from VSM S4, and flow orchestration from S2/S3.

## Repository architecture
OpenManus provides autonomous agents plus planning flows that decompose a user objective into steps and dispatch execution through configured agents. The planning flow tracks plan state/status and selects execution behavior for the current objective. This is task-level operational orchestration rather than a separate organizational metasystem.

## Primary evidence
- `app/flow/planning.py`: creates/updates plans, tracks step status and drives agents through planned task execution.
- `app/flow/`: first-party flow layer composes operational agents around the current task.

## Operational model
A plan is generated for the current objective, steps are selected/executed by agents, and execution state feeds subsequent steps until completion.

## S1 — Operations
`A`: configured agents autonomously execute task steps with tools/model reasoning under the planning flow. Confidence: high.

## S2 — Coordination
`—`: sequencing and assignment of planned steps do not establish a dedicated interference-regulation mechanism among multiple autonomous S1 units.

## S3 — Inside-and-now control
`—`: plan status and agent dispatch manage the current workflow, but no whole-system current-control authority over shared organizational resources/commitments was established.

## S3* — Complementary audit
`—`: plan/status checks are part of normal execution; no independent complementary audit channel with distinct access was found.

## S4 — Outside-and-then intelligence
`—`: the planner reasons about how to accomplish the present task. Under the profile, internal task planning is not S4 without prospective external-environment intelligence that changes system capability/strategy.

## S5 — Policy and identity
`—`: mission, prompts, agents and policies are externally configured; no autonomous ultimate identity/value authority is present.

## Recursion, variety, escalation
Planning creates hierarchical task structure and operational variety but not recursive VSM closure. Escalation/policy remain parent supplied.