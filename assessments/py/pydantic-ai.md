---
harness_id: pydantic-ai
project_name: Pydantic AI
repository: https://github.com/pydantic/pydantic-ai
review_ref: 5cbacfc8f86d653baa0ca2e31970cbf4f0fcec95
reviewed_at: 2026-09-15
status: included
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 532fb9b98092664c0d59a825de5d986783cae036
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

# Pydantic AI

## Review boundary
Pydantic AI at the pinned revision. The separately packaged Pydantic AI Harness is recognized where this repository explicitly documents it, but distinct Harness implementation is not silently attributed to core.

## Repository architecture
Pydantic AI provides typed autonomous agent loops, tools, durable execution and several multi-agent composition patterns. Its documentation distinguishes agent delegation, programmatic hand-off and graph-based control; Harness `SubAgents` is an external convenience capability.

## Primary evidence
- `docs/multi-agent-applications.md`: delegation calls another agent as a tool and returns control to the parent; programmatic hand-off is application-controlled; graph control is an authored state machine.
- The same document makes shared usage/cancellation limits explicit, including whole-tree cancellation, but those are runtime budget/safety controls rather than an autonomous metasystem.
- Harness `SubAgents` is explicitly referenced as a separately packaged capability and therefore is not counted as core ownership without its own assessed boundary.

## Operational model
An `Agent` is S1. Delegate agents perform bounded operational work for a parent; application code or graph state machines decide programmatic transitions.

## S1 — Operations
`A`: agents autonomously choose tools/actions across iterative runs. Confidence: high.

## S2 — Coordination
`—`: reviewed multi-agent paths are parent delegation, sequential hand-off or authored graph control, not first-party autonomous mutual adjustment among S1 units.

## S3 — Inside-and-now control
`—`: shared usage limits, cancellation trees and durable execution are runtime constraints; no autonomous whole-system commitment/resource regulator is established.

## S3* — Complementary audit
`—`: second opinions or reviewer-like delegates can be constructed, but core does not supply a distinct audit channel with independent corrective authority.

## S4 — Outside-and-then intelligence
`—`: planning, memory, web access and deep-agent composition do not establish a distinct prospective adaptation function coupled to S3.

## S5 — Policy and identity
`—`: instructions, graphs, limits, approvals and policies remain application/developer owned.

## Recursion, variety, escalation
Delegation and graph composition are compositional; they do not by themselves establish recursive viability.
