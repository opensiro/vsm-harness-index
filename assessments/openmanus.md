---
harness_id: openmanus
project_name: OpenManus
repository: https://github.com/FoundationAgents/OpenManus
review_ref: 3309bf4e416fb1c74b008f3e86494439a31bad53
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# OpenManus

## Review boundary
OpenManus at the pinned revision using its standard single-agent runtime. The README labels `run_flow.py` multi-agent mode unstable, so it is not promoted into out-of-box metasystem classification.

## Repository architecture
OpenManus runs a general-purpose agent with LLM configuration and browser/MCP tools. Browser Use is started as a default MCP server; an unstable multi-agent flow is separately available.

## Primary evidence
- `README.md`: standard `python main.py` agent path; default Browser Use MCP tools; explicit “unstable multi-agent version” boundary.

## Operational model
The standard OpenManus agent is S1. Experimental multi-agent flow is outside the standard documented distribution used for autonomy states.

## S1 — Operations
`A`: standard agent autonomously uses tools/environment toward supplied tasks. Confidence: high.

## S2 — Coordination
`—`: no standard-distribution multi-S1 coordination function; unstable flow is not counted.

## S3 — Inside-and-now control
`?`: no autonomous whole-system regulator verified.

## S3* — Complementary audit
`?`: no independent audit function verified.

## S4 — Outside-and-then intelligence
`?`: browser/web access serves current tasks, not prospective adaptation.

## S5 — Policy and identity
`?`: model/task/configuration remain parent-owned.

## Recursion, variety, escalation
External MCP tools expand one S1's variety; experimental multi-agent composition is not recursion.