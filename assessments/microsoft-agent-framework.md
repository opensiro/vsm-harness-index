---
harness_id: microsoft-agent-framework
project_name: Microsoft Agent Framework
repository: https://github.com/microsoft/agent-framework
review_ref: 1cd06c5a2058a172eebadf5d9d7c3fa45c519520
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Microsoft Agent Framework

## Review boundary
Microsoft Agent Framework at the pinned revision across its production agent and multi-agent workflow APIs. Foundry hosting is infrastructure, not silently treated as a VSM actor.

## Repository architecture
MAF supports agents plus graph workflows with sequential, concurrent, handoff and group-collaboration patterns, checkpointing, HITL, time travel, middleware and observability.

## Primary evidence
- `README.md`: production multi-agent framework, graph orchestration patterns, HITL/checkpointing/time travel, observability and hosting boundaries.

## Operational model
Agents are S1 units. Workflow/group-collaboration primitives can organize multiple S1s, but the reviewed high-level evidence does not establish a specific anti-oscillation decision right separate from routing/handoff.

## S1 — Operations
`A`: standard agents autonomously perform model/tool work. Confidence: high.

## S2 — Coordination
`?`: first-party group collaboration exists, but Beer-style mutual adjustment/conflict regulation is not sufficiently demonstrated for `A/C`.

## S3 — Inside-and-now control
`?`: workflow/governance infrastructure does not prove agent-owned whole-system regulatory authority.

## S3* — Complementary audit
`?`: observability and labs/evaluation do not by themselves establish independent complementary audit.

## S4 — Outside-and-then intelligence
`?`: RL/research labs and workflow planning do not establish standard-distribution S4.

## S5 — Policy and identity
`?`: HITL/governance remain parent-controlled constraints.

## Recursion, variety, escalation
Nested/group workflows are not automatically recursive viable systems.