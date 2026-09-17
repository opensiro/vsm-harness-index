---
harness_id: beeai-framework
project_name: BeeAI Framework
repository: https://github.com/i-am-bee/beeai-framework
review_ref: 6a8b28f54073790f9a8135320a0e9ed1d4cef602
reviewed_at: 2026-09-15
status: included
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 50bb05be270f681c0375c232792079287f1888b1
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

# BeeAI Framework

## Review boundary
BeeAI Framework at the pinned revision across Python/TypeScript agent and workflow primitives.

## Repository architecture
BeeAI supplies autonomous agents, tools, memory, RAG, persistence, workflows and handoff tools. The documented multi-agent pattern uses a main agent that invokes specialized agents through `HandoffTool` and receives their results; `RequirementAgent` enforces configured requirements around one agent loop.

## Primary evidence
- `docs/src/content/docs/modules/agents.mdx`: first-party examples compose a `RequirementAgent` with `HandoffTool` specialists.
- `docs/src/content/docs/introduction/tour.mdx`: the main agent consults specialized agents through handoff tools and integrates their outputs.
- Python implementation/changelog at the pinned ref shows handoff and requirement behavior as ordinary agent/tool composition rather than a separate organizational control plane.

## Operational model
Specialist agents are S1. The main agent's handoff is delegation/consultation; workflows and requirements constrain execution without establishing separate metasystemic decision rights.

## S1 — Operations
`A`: agents independently reason and use tools toward outcomes. Confidence: high.

## S2 — Coordination
`—`: first-party handoff/workflow mechanisms decompose or route work rather than provide mutual adjustment/collision regulation among autonomous S1 units.

## S3 — Inside-and-now control
`—`: the main agent chooses specialists during its own task but no whole-system current commitment/resource regulator is established.

## S3* — Complementary audit
`—`: observability, middleware and requirement checking do not instantiate a distinct independent audit channel with corrective authority.

R2 compatibility note: the checked delta adds an optional HOL Guard middleware example. It invokes a separately installed external `hol-guard` process before one tool executes and fails closed on a non-allow decision. This is a configured execution gate around S1 behavior, not a first-party complementary-audit organization with independent access and corrective closure.

## S4 — Outside-and-then intelligence
`—`: memory, RAG and environment tools serve current-task reasoning rather than a prospective intelligence loop coupled back to S3.

## S5 — Policy and identity
`—`: RequirementAgent rules, tools, prompts and workflow policy are configured constraints, not autonomous ultimate-policy closure.

## Recursion, variety, escalation
Handoff hierarchies and workflows are compositional; they do not by themselves establish recursive viable systems.

## R2 result
Checked through `50bb05be270f681c0375c232792079287f1888b1`. The 10-commit delta changes adapters, serving/auth/tool behavior and examples without changing the assessed organizational vector. Outcome: `no-material-change`; accepted `review_ref` remains unchanged.