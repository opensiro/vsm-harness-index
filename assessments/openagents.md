---
harness_id: openagents
project_name: OpenAgents
repository: https://github.com/OpenAgentsInc/openagents
review_ref: a2de475d2ee3a2f00865944c79c15600c1ada45c
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 8f84d05896ef14edee491621bf977ee5315cc8ed
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenAgents

## Review boundary
OpenAgents at the pinned revision as the Agent IDE/control environment around agent engines. Provider loops such as Codex remain worker engines behind the OpenAgents boundary; roadmap/research systems that are explicitly retired or not planned are not counted as current runtime functions.

## Repository architecture
OpenAgents owns durable work around agent engines: conversations, project context, parent/child topology, controls, history, review, recovery and evidence. Its current product framing explicitly puts intent, authority, supervision and acceptance in a human/operator cockpit.

## Primary evidence
- `README.md`: models are workers; OpenAgents owns the working environment around them. The standard supervision surface includes stop, steer, queue, question, approval and refusal, while a human operator supplies goals/boundaries and decides whether the result counts.
- `README.md`: ProductSpec/AssuranceSpec remain underlying authoring/verification tooling; fleet and broader autonomous/network capabilities are explicitly narrowed, closed `not planned`, or require new bounded owner decisions before becoming current product authority.
- `INVARIANTS.md`, `QA Swarm Assurance Execution`: the former Desktop assurance swarm/partitioner was retired and deleted on 2026-08-04; the pinned revision states there is no current Desktop swarm target and no swarm execution path. Remaining QA projections/receipts are evidence machinery and explicitly cannot fabricate or strengthen missing evidence.
- Parent/subagent history, causal activity, cancellation/supervision and bounded evidence are first-party product capabilities, but they remain routing/inspection/operator-control mechanisms at the reviewed boundary.

## Operational model
Connected agent engines execute S1 work. OpenAgents records and supervises the environment around those workers, but decisive acceptance and authority are explicitly owner/operator controlled rather than delegated to an autonomous metasystem.

## S1 — Operations
`A`: connected coding-agent engines autonomously execute bounded model/tool work inside the standard product. Confidence: high.

## S2 — Coordination
`—`: parent/child topology, queues, cancellation and supervised delegation organize work but do not establish a standard autonomous anti-oscillation/shared-resource coordination decision right among peer S1 units.

## S3 — Inside-and-now control
`—`: whole-environment supervision is explicitly an operator control surface. No current autonomous agent owns the superior resource/priority/commitment regulator role.

## S3* — Complementary audit
`—`: OpenAgents has substantial evidence and assurance infrastructure, but the previously autonomous-looking assurance swarm execution path is explicitly retired/deleted at this pinned revision. Current review, receipts and QA projections support human/verifier judgment rather than a standard autonomous complementary-audit agent.

## S4 — Outside-and-then intelligence
`—`: research, Fast Follow and network/product-roadmap material do not establish a standard runtime S4 decision right; several broader directions explicitly require new owner admission before they gain product authority.

## S5 — Policy and identity
`—`: the product deliberately retains ultimate goals, authority, private boundaries and result acceptance with the owner/user.

## Recursion, variety, escalation
OpenAgents records rich parent/child topology and evidence, but subagents are not automatically recursively viable systems and the human owner remains the terminal escalation/acceptance authority.