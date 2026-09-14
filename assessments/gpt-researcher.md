---
harness_id: gpt-researcher
project_name: GPT Researcher
repository: https://github.com/assafelovic/gpt-researcher
review_ref: 6f998577d547b1e54ec662dac63583aa11e3b84b
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# GPT Researcher

## Review boundary
GPT Researcher at the pinned revision, covering the planner/execution/publisher research architecture.

## Repository architecture
A planner generates research questions, multiple execution/crawler agents gather and summarize sources, and a publisher aggregates findings into a cited report. Work is parallelized for speed and breadth.

## Primary evidence
- `README.md`: planner and execution agents; question generation; crawler per question; source tracking; filter/aggregate into final report; parallelized agent work.

## Operational model
Research/crawler agents perform outcome-producing S1 work. Planner fan-out and publisher fan-in assign/decompose/aggregate work but do not by themselves regulate oscillation or conflict among S1 units.

## S1 — Operations
`A`: execution agents autonomously gather evidence and produce bounded research results. Confidence: high.

## S2 — Coordination
`—`: the reviewed planner→workers→publisher path is task decomposition/aggregation, not evidence of agent-owned anti-oscillation or mutual adjustment.

## S3 — Inside-and-now control
`?`: planner/publisher titles do not prove whole-system resource/accountability authority.

## S3* — Complementary audit
`?`: source tracking/filtering is part of normal production, not sufficiently independent audit.

## S4 — Outside-and-then intelligence
`?`: web research senses the external environment for the current task but does not establish a future/adaptation function coupled to S3.

## S5 — Policy and identity
`?`: the research query/objective remains parent-supplied.

## Recursion, variety, escalation
Parallel workers amplify evidence-gathering variety; fan-out/fan-in is not recursion.