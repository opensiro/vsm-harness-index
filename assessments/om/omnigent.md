---
harness_id: omnigent
project_name: Omnigent
repository: https://github.com/omnigent-ai/omnigent
review_ref: 4d963a360e798f076d4fdbd4665e7188e4da05df
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Omnigent

## Review boundary
Pinned Omnigent meta-harness, including first-party autonomous agents, heterogeneous coding-agent backends, the bundled Polly orchestration example, policy layers, isolated worktrees and the separate cross-vendor reviewer. Static deployment policy and ordinary human approval are not promoted into VSM functions without the required closure.

Reviewed revision: `4d963a360e798f076d4fdbd4665e7188e4da05df`. Contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`README.md`](https://github.com/omnigent-ai/omnigent/blob/4d963a360e798f076d4fdbd4665e7188e4da05df/README.md) — meta-harness boundary, autonomous agent execution, interchangeable backends, sandboxing and policy surfaces.
- [`examples/polly/config.yaml`](https://github.com/omnigent-ai/omnigent/blob/4d963a360e798f076d4fdbd4665e7188e4da05df/examples/polly/config.yaml) — autonomous orchestrator, goal decomposition, worker selection, isolated worktrees, task registry, monitoring/re-dispatch, independent reviewer and review-failure fix tasks.
- [`omnigent/runner/policy.py`](https://github.com/omnigent-ai/omnigent/blob/4d963a360e798f076d4fdbd4665e7188e4da05df/omnigent/runner/policy.py) — ALLOW/DENY/ASK policy enforcement and escalation behavior.

## S1 — Operations
`A`. First-party agents and supported external coding-agent backends autonomously perform model/tool work inside Omnigent sessions. Confidence: high.

## S2 — Coordination
`A`. Polly closes a concrete coordination loop across parallel workers: it decomposes work, assigns independent worktrees, tracks task dependencies/results, reacts to failures and re-dispatches work. Worktree isolation attenuates file collisions while task-state feedback changes later worker behavior. Confidence: high.

## S3 — Inside-and-now control
`A`. The autonomous Polly orchestrator has a whole-run view and authority over assignment, worker/model selection, cancellation, failure recovery and re-dispatch. It therefore regulates current team commitments rather than merely forwarding tasks. Confidence: high.

## S3* — Complementary audit
`A`. A separate cross-vendor reviewer receives the implementation diff and contract rather than the implementer's working context, independently judges the result, and blocking findings are converted automatically into corrective fix tasks before human merge. This supplies complementary access plus closed corrective feedback. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. No distinct outside-looking prospective adaptation loop that develops future organizational capability was established. Confidence: high.

## S5 — Policy and identity
`—`. ALLOW/DENY/ASK, budgets, sandbox rules and human escalation constrain execution. They do not establish an identity/ultimate-policy tension resolved by legitimate S5 authority and returned as changed organizational policy. Confidence: high.

## Recursion, variety, and escalation
Heterogeneous workers and models amplify operational variety; worktree separation, task registry, policy layers and Polly's current regulation attenuate it. Reviewer failures escalate into new corrective work; ASK escalates ordinary execution authority to the parent without becoming S5.

## Admission conclusion
Canonical vector: `A A A A — —`.

Same-ref correction of historical `A C C C — P`: the bundled Polly path demonstrates autonomous ownership of S2/S3/S3*, while ASK/outer policy is execution governance rather than S5 identity closure.