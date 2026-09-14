---
harness_id: deerflow
project_name: DeerFlow
repository: https://github.com/bytedance/deer-flow
review_ref: 6f81daefff2035d76d41e45d021626f022885372
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# DeerFlow

## Review boundary
DeerFlow 2.0 at the pinned revision as the standard super-agent harness; the 1.x deep-research branch is explicitly separate.

## Repository architecture
DeerFlow orchestrates subagents, memory, sandboxes and skills, with session goals, context compaction, scheduled tasks and tracing integrations. A lead/root harness delegates bounded work to subagents.

## Primary evidence
- `README.md`: super-agent harness; subagents/memory/sandbox/skills; session goals, context management, scheduling and tracing; explicit 1.x/2.0 boundary.

## Operational model
Root and subagents perform S1 work. The documented subagent topology is hierarchical delegation and result integration.

## S1 — Operations
`A`: agents autonomously use tools/skills/sandboxes toward outcomes. Confidence: high.

## S2 — Coordination
`—`: subagent orchestration/delegation does not establish peer mutual adjustment or anti-oscillation.

## S3 — Inside-and-now control
`?`: lead/root control does not prove whole-system resource/accountability authority.

## S3* — Complementary audit
`?`: tracing/replay support evidence but are not independent audit.

## S4 — Outside-and-then intelligence
`?`: memory/scheduled work/environment search do not establish prospective adaptation coupled to S3.

## S5 — Policy and identity
`?`: session goals/configuration remain parent-owned.

## Recursion, variety, escalation
Subagents and runtime caps constrain delegated operational variety; hierarchy is not recursion.