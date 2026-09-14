---
harness_id: proliferate
project_name: Proliferate
repository: https://github.com/proliferate-ai/proliferate
review_ref: 74e1178cf3ecfbfc3ffeb8321f82c4a9bfce620f
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Proliferate

## Review boundary
Proliferate at the pinned revision as an AI IDE/control plane running native coding-agent harnesses in parallel worktree workspaces.

## Repository architecture
Each task gets an isolated branch/worktree/terminal/conversation/review state. Multiple agents run side by side; subagents receive scoped delegated work and return results; recurring/event-driven workflows launch agent runs.

## Primary evidence
- `README.md`: native harnesses; isolated worktree per task; parallel agents; subagent delegation; recurring/event-driven workflows and self-hosted control plane.

## Operational model
Native coding agents and child agents perform S1 work. Isolation prevents filesystem conflicts mechanically; subagent calls are delegation.

## S1 — Operations
`A`: native agent harnesses autonomously perform coding tasks within the standard product. Confidence: high.

## S2 — Coordination
`—`: parallel isolation and parent→child delegation do not establish agent-owned mutual adjustment among S1 units.

## S3 — Inside-and-now control
`?`: control-plane/workspace scheduling is not verified autonomous S3 regulation.

## S3* — Complementary audit
`?`: per-task review state does not establish independent audit.

## S4 — Outside-and-then intelligence
`?`: event-triggered runs react to current conditions, not prospective adaptation.

## S5 — Policy and identity
`?`: workflow/integration policy remains operator-owned.

## Recursion, variety, escalation
Worktree isolation supports safe parallel operational variety; child agents are not recursive viable systems.