---
harness_id: deepagents
project_name: DeepAgents
repository: https://github.com/langchain-ai/deepagents
review_ref: 7f9e8ed3a555933902045792da9bb184950ee7b2
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# DeepAgents

## Review boundary
Pinned middleware harness including blocking/async subagents, persistent background task lifecycle, HITL and rubric middleware.

## Repository architecture
SubAgentMiddleware and AsyncSubAgentMiddleware manage delegated/background agents. Background identities/lifecycle/update/cancel/check regulate coexistence. RubricMiddleware grades after natural stop and can jump execution back to the model for correction.

## Primary evidence
- Pinned deep review established background task lifecycle, declarative subagent overrides, HITL interrupts and rubric correction loop at `review_ref`.

## Operational model
Primary/subagents perform S1 work; middleware supplies constructor-owned coordination/current control and optional post-stop audit/correction; HITL preserves parent authority.

## S1 — Operations
`A`: agents autonomously execute model/tool work. Confidence: high.

## S2 — Coordination
`C`: background identities/lifecycle/isolation/update/cancel/check regulate coexistence beyond delegation, but no autonomous coordinator owns the function. Confidence: high.

## S3 — Inside-and-now control
`C`: permissions/interrupts/state repair/background lifecycle provide constructor-owned current regulation. Confidence: high.

## S3* — Complementary audit
`C`: RubricMiddleware runs after natural stop and a structured grader can jump back to the model for correction. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective environment-facing organizational adaptation function was established. Confidence: high.

## S5 — Policy and identity
`P`: `interrupt_on` injects human approval into selected decisions. Confidence: high.

## Recursion, variety, escalation
Background subagents amplify parallel variety; lifecycle controls attenuate it; rubric correction and HITL create distinct escalation paths.

## Deep-review conclusion
Signature at the pinned revision: `A C C C — P`. DeepAgents supplies substantial composable metasystem closure around autonomous agents.