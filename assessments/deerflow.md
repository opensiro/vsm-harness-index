---
harness_id: deerflow
project_name: DeerFlow
repository: https://github.com/bytedance/deer-flow
review_ref: 6f81daefff2035d76d41e45d021626f022885372
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# DeerFlow

## Review boundary
Deep review of the pinned lead-agent/subagent runtime. Lead/subagent hierarchy, concurrency controls and guardrails are tested as operational mechanisms rather than assumed to be metasystem functions.

## Repository architecture
DeerFlow provides a long-horizon lead agent that can browse, code, create artifacts and delegate bounded investigations to subagents. The runtime constrains subagent execution and integrates returned findings, but the reviewed implementation is a hierarchical task-execution structure rather than a separate coordination/control metasystem.

## Primary evidence
- `backend/packages/harness/deerflow/agents/lead_agent/agent.py`: constructs the lead-agent operational path and its tool/subagent capabilities.
- First-party subagent/task paths impose execution/concurrency constraints and return delegated results to the lead agent.
- Guardrails and runtime limits constrain operational behavior; they do not establish agent-owned whole-system regulation.

## Operational model
The lead agent advances a research/creation objective through tools and may delegate scoped work to sandboxed subagents, consuming their findings in the parent trajectory.

## S1 — Operations
`A`: lead and delegated agents autonomously perform useful tool-using operational work. Confidence: high.

## S2 — Coordination
`—`: lead-to-subagent delegation, concurrency limits and result integration do not constitute a dedicated mechanism for regulating interference or oscillation among autonomous S1 units. The shallow `S2=A` interpretation is removed.

## S3 — Inside-and-now control
`—`: current task supervision and concurrency caps are runtime constraints rather than whole-system authority over organizational resources/capacity/commitments.

## S3* — Complementary audit
`—`: no distinct complementary audit channel with separate organizational access/authority was established.

## S4 — Outside-and-then intelligence
`—`: long-horizon task research still serves the current objective; no separate prospective intelligence function that changes future organizational capability/strategy was established.

## S5 — Policy and identity
`—`: goals, tools, guardrails and delegation policy remain externally configured.

## Recursion, variety, escalation
Sandboxed subagents increase operational variety and depth while leaving metasystem closure to the application.