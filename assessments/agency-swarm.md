---
harness_id: agency-swarm
project_name: Agency Swarm
repository: https://github.com/VRSEN/agency-swarm
review_ref: 853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: C
---

# Agency Swarm

## Review boundary
Pinned agency runtime with first-party Agents, communication topology, SendMessage/handoff, ToolConcurrencyManager and guardrails.

## Repository architecture
Agents operate inside constructor-defined directional communication graphs. Concurrency management attenuates shared-tool interference; executable guardrails can challenge/abort inputs/outputs.

## Primary evidence
- Pinned deep review established directional communication, ToolConcurrencyManager and input/output guardrail execution at `review_ref`.

## Operational model
Agents own local operations; constructor-defined topology, concurrency and guardrail policy close composable metasystem functions.

## S1 — Operations
`A`: agents autonomously execute tool/model work. Confidence: high.

## S2 — Coordination
`C`: concurrency management genuinely attenuates shared-tool interference, while topology remains constructor-owned. Confidence: high.

## S3 — Inside-and-now control
`C`: executable guardrails/concurrency constraints regulate current operations. Confidence: high.

## S3* — Complementary audit
`C`: separate input/output guardrails can challenge and abort work, with constructor-supplied audit policy. Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`: no prospective organizational adaptation function was established. Confidence: high.

## S5 — Policy and identity
`C`: shared instructions, topology and guardrail policy form an executable constructor surface without a required parent-approval path. Confidence: high.

## Recursion, variety, escalation
Topology constrains communication variety; guardrails and concurrency control attenuate unsafe/conflicting action. Nested agencies do not automatically prove recursive viability.

## Deep-review conclusion
Signature at the pinned revision: `A C C C — C`. Agency Swarm exposes unusually broad composable organizational closure.