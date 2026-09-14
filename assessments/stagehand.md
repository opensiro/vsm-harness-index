---
harness_id: stagehand
project_name: Stagehand
repository: https://github.com/browserbase/stagehand
review_ref: b771930d2b4d858e5bd9670203c66260b385a8fa
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Stagehand

## Review boundary
Stagehand at the pinned revision as the browser-agent SDK and execution environment, not Browserbase as an organization.

## Repository architecture
Stagehand exposes agent-optimized browser observation/action/extraction, self-healing primitives, context reduction and autonomous goal execution through its agent/session surface. It adapts browser actions when sites change.

## Primary evidence
- `README.md`: SDK for browser agents; agent-optimized context; self-healing `act/observe/extract`; browser automation/runtime behavior.
- First-party SDK/docs expose autonomous goal execution that navigates/clicks/types until the browser goal is completed.

## Operational model
A browser agent executing a goal is S1. Self-healing and DOM/context mechanisms support that one operation rather than coordinate multiple S1 units.

## S1 — Operations
`A`: a standard browser agent autonomously chooses browser actions toward a goal. Confidence: high.

## S2 — Coordination
`—`: no material multi-S1 coordination path is supplied at this boundary.

## S3 — Inside-and-now control
`?`: execution/security controls are runtime mechanisms, not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: observability is not independent audit.

## S4 — Outside-and-then intelligence
`?`: self-healing reacts to changed pages locally; it does not establish future-oriented environmental adaptation coupled to S3.

## S5 — Policy and identity
`?`: policy/security configuration remains parent-owned.

## Recursion, variety, escalation
Browser context and self-healing amplify one S1's environmental variety; no recursion is established.