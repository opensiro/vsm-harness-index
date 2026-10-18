---
harness_id: browser-use
project_name: Browser Use
repository: https://github.com/browser-use/browser-use
review_ref: 50f205533fe10ba35b553d2a3689c77b87bd5d0a
reviewed_at: 2026-09-15
status: included
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: d8110c5ff87ccba887aaa726cdb780f2f84bef8d
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

# Browser Use

## Review boundary
Deep review of the pinned Browser Use agent service and its first-party planning/judge hooks. The assessment distinguishes an evaluator inside one agent loop from a complementary S3* audit function.

## Repository architecture
Browser Use provides an autonomous browser agent with model-driven action selection, browser/tool execution, state/history, callbacks, optional planning and optional judging. The reviewed architecture is centered on one operational agent loop rather than a multi-S1 organizational control layer.

## Primary evidence
- `browser_use/agent/service.py`: owns the agent lifecycle, browser/tool execution, model calls, state/history and step callbacks.
- `browser_use/agent/service.py`: exposes planning and `use_judge`/judge-model configuration as parts of the operational run.

## Operational model
The agent observes browser state, asks the model for the next action, executes browser/tools and iterates. Optional planning and judging enrich or validate that same task trajectory.

## S1 — Operations
`A`: the standard agent autonomously chooses browser/tool actions and continues from environment feedback. Confidence: high.

## S2 — Coordination
`—`: no distinct mechanism was found for regulating interference among multiple autonomous S1 units. A single browser-agent loop with callbacks is not S2.

## S3 — Inside-and-now control
`—`: run state, history and task-level planning manage one operational process; there is no whole-system current-control authority over multiple S1 commitments/resources.

## S3* — Complementary audit
`—`: the optional judge evaluates the operational trajectory/output inside the normal run. It is not evidenced as an organizationally independent or complementary audit channel with distinct access/authority.

## S4 — Outside-and-then intelligence
`—`: task planning predicts next actions for the current browser objective. No separate environment-scanning function that changes system capability or strategy over a longer horizon was established.

## S5 — Policy and identity
`—`: tool permissions, task goals, prompts and approval/configuration remain externally supplied rather than owned by an autonomous policy/identity function.

## Recursion, variety, escalation
The harness has substantial operational variety through browser tools, planning and judging, but these remain internal features of S1 rather than recursively closed S2–S5 functions.

## R2 result
Checked through `d8110c5ff87ccba887aaa726cdb780f2f84bef8d`. The 16-commit delta is confined to provider/model documentation, examples and a small model adapter change; no assessed agent, planner or judge ownership path changes. Outcome: `no-material-change`; accepted `review_ref` remains unchanged.