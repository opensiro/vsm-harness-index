---
harness_id: omnigent
project_name: Omnigent
repository: https://github.com/omnigent-ai/omnigent
review_ref: 4d963a360e798f076d4fdbd4665e7188e4da05df
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: P
---

# Omnigent

## Review boundary
Pinned meta-harness with first-party YAML agents, heterogeneous external backends, policy layers and bundled Polly orchestrator/reviewer.

## Repository architecture
Policies exist at server/agent/session levels with ALLOW/DENY/ASK, budgets, tool limits and sandboxing. Polly provides cross-vendor orchestration and a separate reviewer over diffs/contracts.

## Primary evidence
- Pinned review established layered ALLOW/DENY/ASK policy, budgets/tool limits/sandbox and Polly orchestrator/reviewer at `review_ref`.

## Operational model
First-party agents can act autonomously while deployment-defined policy and orchestration primitives regulate execution; reviewer output does not itself merge changes.

## S1 — Operations
`A`: first-party agents autonomously perform model/tool work. Confidence: high.

## S2 — Coordination
`C`: orchestration primitives coordinate heterogeneous agents under constructor-defined topology. Confidence: high.

## S3 — Inside-and-now control
`C`: executable policy/budget/tool/sandbox controls regulate current operation. Confidence: high.

## S3* — Complementary audit
`C`: separate reviewer machinery challenges worker output against diff/contract evidence, but constructor configuration owns the closure and reviewer does not merge. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no distinct prospective adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`P`: ASK and outer deployment policy preserve parent authority. Confidence: high.

## Recursion, variety, escalation
Multiple backends amplify operational variety; policy layers attenuate it and ASK escalates unresolved authority to the parent.

## Deep-review conclusion
Signature at the pinned revision: `A C C C — P`. Omnigent provides broad composable metasystem controls around autonomous agents while retaining ultimate policy with the parent.