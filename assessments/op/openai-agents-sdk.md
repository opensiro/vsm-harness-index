---
harness_id: openai-agents-sdk
project_name: OpenAI Agents SDK
repository: https://github.com/openai/openai-agents-python
review_ref: fbd2dbcaaf74a2c447c6d3fa9d5645d83fd7e292
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 5f9899d584c5cfc879d3579352eb929fd4b34756
last_checked_at: 2026-09-16
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

# OpenAI Agents SDK

## Review boundary
Deep review of the pinned first-party multi-agent documentation and its manager, handoff and evaluator-loop patterns. Pattern names are not mapped to VSM functions unless the required organizational responsibility is present.

## Repository architecture
The Agents SDK supports autonomous tool-using agents, agents-as-tools (manager-style orchestration), handoffs that transfer control, and code-driven orchestration including evaluator loops. These are expressive composition patterns. In the reviewed distribution, however, they remain application-built operational flows rather than built-in organizational control functions.

## Primary evidence
- `docs/multi_agent.md`: distinguishes manager/agents-as-tools, handoffs and code orchestration; the application chooses the topology and control flow.
- `docs/multi_agent.md`: evaluator-loop examples place evaluation/retry in the same application workflow around a produced result.

## Operational model
An agent autonomously performs task work with tools. Applications may delegate to specialist agents, transfer the active conversation through handoffs, or implement deterministic/LLM-driven orchestration and evaluation loops.

## S1 — Operations
`A`: first-party agents autonomously select tools/actions and execute task work within application-defined bounds. Confidence: high.

## S2 — Coordination
`—`: handoffs and manager-to-specialist calls transfer/delegate work, but the SDK does not itself provide a function whose responsibility is regulating interference or shared constraints among multiple autonomous S1 units. The earlier `S2=C` interpretation is removed.

## S3 — Inside-and-now control
`—`: a manager agent or code orchestrator assigns operational work but is not, by that fact, a whole-system current-control authority for resources/capacity/commitments.

## S3* — Complementary audit
`—`: evaluator loops are ordinary application composition over the same work product. No built-in independent/complementary audit channel with distinct organizational access/authority is established; the earlier `S3*=C` interpretation is therefore removed.

## S4 — Outside-and-then intelligence
`—`: routing and orchestration concern current task execution, not a distinct prospective environmental intelligence function.

## S5 — Policy and identity
`—`: instructions, guardrails, handoff topology and application policy are developer-owned; the SDK does not supply autonomous ultimate policy/identity authority.

## Recursion, variety, escalation
The SDK is highly composable and can be used to build VSM-like organizations, but the reviewed SDK does not close those functions out of the box.