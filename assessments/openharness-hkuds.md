---
harness_id: openharness-hkuds
project_name: OpenHarness HKUDS
repository: https://github.com/HKUDS/OpenHarness
review_ref: 9b2efd795c6aa09f88b0c257d269a9e518da6ae7
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# OpenHarness HKUDS

## Review boundary
HKUDS/OpenHarness at the pinned revision, including core agent loop, governance and standard swarm/team primitives; roadmap-only ClawTeam integration is excluded.

## Repository architecture
OpenHarness supplies a streaming tool-call agent loop, memory/context, permissions/hooks, and “Swarm Coordination”: subagent spawning/delegation, team registry/task management and background lifecycle. Later changelog entries describe stabilized subprocess teammates/polling.

## Primary evidence
- `README.md`: agent loop, governance, Swarm Coordination table, team/task lifecycle, changelog and explicit roadmap marker.

## Operational model
Agents/teammates perform S1 work. First-party team/task structures exist, but the evidence does not show enough about autonomous mutual adjustment versus delegation/task management to assign positive S2.

## S1 — Operations
`A`: the harness supplies a ready autonomous tool-using agent loop. Confidence: high.

## S2 — Coordination
`?`: team registry/task management and teammates are first-party, but a specific anti-oscillation decision right/feedback closure is not established.

## S3 — Inside-and-now control
`?`: budgets/governance/task lifecycle are predominantly runtime policy mechanisms, not verified autonomous S3.

## S3* — Complementary audit
`?`: hooks/audit-style instrumentation do not establish independent complementary audit.

## S4 — Outside-and-then intelligence
`?`: memory/context and hooks do not establish prospective adaptation.

## S5 — Policy and identity
`?`: permission modes/rules/approvals are parent-configured.

## Recursion, variety, escalation
Subprocess teammates and background tasks do not automatically establish recursive viability.