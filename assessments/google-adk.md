---
harness_id: google-adk
project_name: Google Agent Development Kit
repository: https://github.com/google/adk-python
review_ref: 460715b6c62c8e9ab00931c502381ee0364e39b6
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Google Agent Development Kit

## Review boundary
Google ADK Python at the pinned revision, including the graph workflow runtime, Task API and standard multi-agent composition. Vertex/hosted control planes are outside the system-in-focus.

## Repository architecture
ADK 2.0 supplies autonomous agents, a graph workflow runtime with routing/fan-out/fan-in/loops/retry/state/HITL, structured agent-to-agent task delegation, multi-agent hierarchies and tool confirmation.

## Primary evidence
- `README.md`: workflow runtime, Task API, modular multi-agent systems, tools, confirmation and agent/workflow quickstarts.

## Operational model
Agents are S1 units. Workflow edges and Task API delegation structure execution, but the high-level evidence does not establish whether group interactions include the mutual-adjustment/conflict-dampening relation required for S2.

## S1 — Operations
`A`: standard agents autonomously use tools and produce bounded outcomes. Confidence: high.

## S2 — Coordination
`?`: multi-agent hierarchy and collaboration are first-party, but routing/delegation alone is insufficient and no specific anti-oscillation decision right was verified.

## S3 — Inside-and-now control
`?`: workflow control does not prove autonomous whole-system resource/accountability authority.

## S3* — Complementary audit
`?`: development evaluation/debugging is not enough to establish sufficiently independent runtime audit.

## S4 — Outside-and-then intelligence
`?`: dynamic workflows/planning are not prospective environmental adaptation.

## S5 — Policy and identity
`?`: confirmation/instructions remain parent-owned.

## Recursion, variety, escalation
Nested workflows and agent hierarchies are composition, not automatically recursive viability.