---
harness_id: ruflo
project_name: Ruflo
repository: https://github.com/ruvnet/ruflo
review_ref: 2602b642d92234c710ffbe96bfb33007d481ceab
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: C
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: C
autonomy_s5: —
---

# Ruflo

## Review boundary
Pinned modular meta-harness/orchestration distribution, treating deployment-supplied agents and policies as constructor-owned where the runtime only provides primitives.

## Repository architecture
Ruflo supplies swarm coordination, lifecycle and consensus/collective-intelligence primitives plus adaptive control surfaces. Concrete operational roles, authority and policy are assembled by the deployment.

## Primary evidence
- Pinned review established swarm coordination, lifecycle, consensus and adaptive primitives at `review_ref`.

## Operational model
The repository is primarily a constructor/meta-harness: it provides executable organizational mechanisms but generally does not itself choose the deployed organization's decisions.

## S1 — Operations
`C`: operational agents are instantiated/configured through supplied primitives. Confidence: high.

## S2 — Coordination
`C`: swarm coordination and consensus mechanisms provide composable mutual-adjustment closure. Confidence: high.

## S3 — Inside-and-now control
`C`: lifecycle/control primitives can regulate current swarm operation when configured. Confidence: medium-high.

## S3* — Complementary audit
`—`: no sufficiently independent standard audit channel with corrective closure was established. Confidence: high.

## S4 — Outside-and-then intelligence
`C`: adaptive/collective-intelligence primitives can be composed into prospective adaptation, but deployment owns the concrete decision right. Confidence: medium-high.

## S5 — Policy and identity
`—`: ultimate identity/policy remains external to the standard runtime. Confidence: high.

## Recursion, variety, escalation
The framework can express nested/swarm structures, but recursion depends on configured viable closure at each level.

## Deep-review conclusion
Signature at the pinned revision: `C C C — C —`. Ruflo is best read as a broad organizational constructor rather than a fixed autonomous organization.