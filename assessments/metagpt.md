---
harness_id: metagpt
project_name: MetaGPT
repository: https://github.com/FoundationAgents/MetaGPT
review_ref: 11cdf466d042aece04fc6cfd13b28e1a70341b1f
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 11cdf466d042aece04fc6cfd13b28e1a70341b1f
last_checked_at: 2026-09-16
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# MetaGPT

## Review boundary
MetaGPT at the pinned revision, focusing on the first-party software-company/MGX team runtime rather than the company metaphor or role names. The mapping is based on default TeamLeader behavior, shared team environment and current-plan regulation.

## Repository architecture
MetaGPT runs specialized role agents in a shared environment. In MGX, ordinary team communication is routed through a `TeamLeader`. The leader can assign role work, receive results, inspect team information and maintain/update the current plan. The default software-company entry point instantiates `TeamLeader` with product, architecture, engineering and data-analysis roles.

## Primary evidence
- `metagpt/software_company.py`: default MGX path hires `TeamLeader`, `ProductManager`, `Architect`, `Engineer2` and `DataAnalyst` before running the team.
- `metagpt/environment/mgx/mgx_env.py`: ordinary member messages are handed to TeamLeader, while TeamLeader publications are routed to intended recipients.
- `metagpt/roles/di/team_leader.py` and `metagpt/prompts/di/team_leader.py`: leader assigns work by expertise, tracks progress from feedback, finishes current tasks, resets/replaces plans and waits for prerequisite outputs.
- `metagpt/strategy/planner.py`: `Planner` holds structured current/finished task state, validates plan updates, records progress and can regenerate the plan from feedback.
- `tests/metagpt/roles/di/test_team_leader.py`: exercises requirement routing, result-driven specialist handoff, plan/progress updates and team-status responses.
- `metagpt/team.py` and `metagpt/environment/base_env.py`: define the shared operational boundary, role registry, message delivery and concurrent role execution.

## Operational model
Specialist roles are S1 units. The TeamLeader's assignment path is not counted as S2 merely because it moves work. Its stronger mapping is S3: it has a team-wide current plan/status view and agent-owned authority to regulate current commitments by assigning, finishing, resetting and replacing team work as results arrive.

## S1 — Operations
`A`: specialized role agents autonomously produce requirements, designs, code, analyses and other operational artifacts. Confidence: high.

## S2 — Coordination
`—`: the reviewed leader/SOP path primarily assigns and sequences work. No separate evidence shows a function that dampens destructive interference or oscillation among autonomous S1 units without centralizing their decisions. Confidence: medium-high.

## S3 — Inside-and-now control
`A`: the default TeamLeader has a whole-team current view through team information, routed feedback and a structured plan; it can regulate current commitments by assigning specialists, closing tasks, changing/resetting the plan and gating downstream work on prerequisite results. This goes beyond worker selection alone and is exercised by an autonomous shipped role. Parent-authored roles, SOPs, prompts, budget and team composition constrain this loop but do not provide a separate first-party human/operator decision path over the same current whole-team commitments, so no `(P)` mode is published. Confidence: high.

## S3* — Complementary audit
`—`: review/testing inside the normal software-production path does not provide a materially independent alternative access channel to operational reality. Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`: planning, product/competitive artifacts and replanning are project work; the reviewed runtime does not establish a distinct external-and-prospective adaptation loop in two-way conversation with S3. Confidence: medium-high.

## S5 — Policy and identity
`—`: role definitions, SOP, prompts, budget and team composition are parent/developer authored. No runtime agent holds legitimate ultimate identity/policy closure for the system-in-focus. Confidence: high.

## Recursion, variety, escalation
Specialized roles increase operational variety, but the software-company hierarchy does not by itself prove recursive viable systems. TeamLeader routing amplifies current regulatory capacity while centralizing cross-role commitments.

## Deep-review result
`S2` resolves from `?` to `—`; `S3` resolves from `?` to `A`; `S3*`, `S4` and `S5` resolve from `?` to `—`; `S1 A` is confirmed. The key correction is function placement: centralized task routing is not S2, while whole-team current-plan authority satisfies S3.