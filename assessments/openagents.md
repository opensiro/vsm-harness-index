---
harness_id: openagents
project_name: OpenAgents
repository: https://github.com/OpenAgentsInc/openagents
review_ref: a2de475d2ee3a2f00865944c79c15600c1ada45c
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: —
---

# OpenAgents

## Review boundary
OpenAgents at the pinned revision as the Agent IDE/control environment around agent engines. Provider agent loops such as Codex remain distinct workers behind the OpenAgents boundary.

## Repository architecture
OpenAgents owns durable conversations, project context, agent/subagent topology, supervision, review, recovery and evidence around model-owned execution loops. Human/operator authority is explicit: stop, steer, approve/refuse, review and decide whether outcomes count.

## Primary evidence
- `README.md`: typed agent turns/tools/plans; parent/child topology; supervision controls; review/evidence; durable history/recovery; explicit human authority and provider-worker boundary.

## Operational model
Agent engines perform S1 work. OpenAgents coordinates/supervises their environment, but much of the decisive authority is explicitly human/user-owned rather than autonomous-agent-owned.

## S1 — Operations
`A`: connected agent engines execute autonomous coding/tool work within the standard product. Confidence: high.

## S2 — Coordination
`?`: parent/child topology and queued/supervised work provide coordination infrastructure, but reviewed evidence does not establish an autonomous S2 decision right distinct from human control/delegation.

## S3 — Inside-and-now control
`—`: whole-environment supervision is explicitly a human/operator control surface, not an autonomous S3 agent.

## S3* — Complementary audit
`?`: evidence/review are strong audit-support mechanisms, but human review and normal receipts are not sufficient autonomous complementary audit.

## S4 — Outside-and-then intelligence
`?`: network/product-roadmap adaptation is organizational/product intent, not a runtime S4 agent function.

## S5 — Policy and identity
`—`: ultimate authority and acceptance remain explicitly owner/user-controlled.

## Recursion, variety, escalation
Parent/child topology is recorded and bounded, but subagents are not automatically recursively viable systems.