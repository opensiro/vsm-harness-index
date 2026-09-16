---
harness_id: openai-agents-js
project_name: OpenAI Agents SDK for JavaScript
repository: https://github.com/openai/openai-agents-js
review_ref: 8831eae9d34365f9a397cbd52ae0366f304e1a96
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 58844c7fbcee33e4cf404bbd18350f30627b07e1
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

# OpenAI Agents SDK for JavaScript

## Review boundary
Deep review of the pinned JavaScript SDK handoff/composition model. Handoffs, managers, guardrails and evaluator-style application patterns are not mapped to VSM functions unless the SDK itself supplies the relevant organizational responsibility.

## Repository architecture
The JavaScript Agents SDK provides autonomous tool-using agents, handoffs, agents-as-tools, sessions, guardrails and related runtime primitives. Its handoff guide explicitly defines handoffs as delegation/transfer of control to a specialist within the same run; manager-style composition keeps specialists behind the calling agent. These are application composition patterns, not built-in interference regulation or whole-system control.

## Primary evidence
- `docs/src/content/docs/guides/handoffs.mdx`: states that handoffs let an agent delegate part of a conversation to another agent and transfer control to the configured destination.
- Handoffs stay within a single run; destination choice, authorization, filtering and topology remain application-defined.
- The guide distinguishes handoffs from agents-as-tools/manager-style composition, confirming that these abstractions organize operational delegation rather than supplying an organizational metasystem.

## Operational model
A JavaScript agent performs tool-using work and can either invoke specialists as tools or transfer the active run to a specialist via a handoff. Application code configures destinations, filters, guardrails and authority boundaries.

## S1 — Operations
`A`: agents autonomously choose tools/actions and execute text/voice tasks within configured run boundaries. Confidence: high.

## S2 — Coordination
`—`: handoffs transfer control and agents-as-tools delegate work; neither mechanism by itself regulates interference, oscillation or shared constraints among multiple autonomous S1 units. The shallow `S2=C` interpretation is removed.

## S3 — Inside-and-now control
`—`: manager-style composition remains task orchestration and does not establish whole-system authority over shared resources/capacity/commitments.

## S3* — Complementary audit
`—`: evaluator/guardrail patterns require application-defined placement and authority and, in the reviewed SDK boundary, are normal validation/composition rather than a supplied complementary audit channel. The shallow `S3*=C` interpretation is removed.

## S4 — Outside-and-then intelligence
`—`: routing, session state and current-run orchestration do not provide a distinct prospective environment-intelligence function.

## S5 — Policy and identity
`—`: instructions, guardrails, handoff topology and application policy remain developer-owned.

## Recursion, variety, escalation
The SDK can be used to construct richer organizations, but its first-party primitives do not close S2–S5 out of the box.