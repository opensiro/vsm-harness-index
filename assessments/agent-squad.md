---
harness_id: agent-squad
project_name: Agent Squad
repository: https://github.com/2FastLabs/agent-squad
review_ref: 31eccfeb0d546262d1d0ec2e2e5239186f8d2954
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Agent Squad

## Review boundary
Agent Squad at the pinned revision across its multi-agent routing/orchestration runtime and SupervisorAgent pattern.

## Repository architecture
A classifier selects the most suitable specialized agent for each user turn while preserving conversation context. SupervisorAgent can delegate parallel subtasks and synthesize one response; GroundedAgent separates gatherer and presenter roles.

## Primary evidence
- `README.md`: classifier routing; context across agents; supervisor parallel delegation/shared context; grounded gatherer→presenter separation.

## Operational model
Specialized agents are S1. Classifier/supervisor mechanisms distribute work, but routing/delegation is not automatically S2.

## S1 — Operations
`A`: specialized agents independently process routed tasks with tools. Confidence: high.

## S2 — Coordination
`?`: shared context and supervisor/classifier topology provide coordination infrastructure, but evidence does not show a distinct mutual-adjustment/conflict-regulation decision right among S1s.

## S3 — Inside-and-now control
`?`: supervisor synthesis/routing does not establish whole-system resource/accountability authority.

## S3* — Complementary audit
`?`: GroundedAgent presenter isolation constrains generation but is normal production composition, not complementary audit.

## S4 — Outside-and-then intelligence
`?`: no prospective adaptation function verified.

## S5 — Policy and identity
`?`: roles/routing policies are application-configured.

## Recursion, variety, escalation
Hierarchical teams-of-teams are technically composable, but hierarchy alone is not recursive viability.