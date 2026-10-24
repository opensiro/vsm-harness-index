---
harness_id: shannon
project_name: Shannon
repository: https://github.com/Kocoro-lab/Shannon
review_ref: 391b619130281502d227a53dd97238c9791bf174
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Shannon

## Review boundary
Pinned first-party Shannon runtime: autonomous AgentLoops, swarm/lead orchestration, Temporal workflow control, budget/preflight/backpressure, sandbox/policy enforcement, and approval middleware. Application-authored organization is outside the credited boundary.

Reviewed revision: `391b619130281502d227a53dd97238c9791bf174`. Current Index contract: Profile `0.2.1`, Methodology `0.3.1`. The candidate pin is preserved; upstream drift was checked separately.

## Primary evidence
- [`README.md`](https://github.com/Kocoro-lab/Shannon/blob/391b619130281502d227a53dd97238c9791bf174/README.md)
- [`docs/multi-agent-workflow-architecture.md`](https://github.com/Kocoro-lab/Shannon/blob/391b619130281502d227a53dd97238c9791bf174/docs/multi-agent-workflow-architecture.md)
- Historical deep review at the same pin for budget/backpressure and durable approval paths.

## S1 — Operations
`A`. AgentLoops perform bounded model/tool work and adapt subsequent actions from observations. The agent actor owns the next operational action within configured limits. Confidence: high.

## S2 — Coordination
`—`. Swarm Lead decomposition, delegation, result collection and convergence do not establish a separate first-party mechanism regulating a concrete inter-S1 interference/conflict/oscillation. The historical `A` promoted orchestration into S2 without the required disturbance/regulation witness. Confidence: medium-high.

## S3 — Inside-and-now control
`C`. Budget management, preflight checks and backpressure regulate shared current execution capacity across the running system. The runtime supplies and enforces this whole-system resource-control path; applications configure its bounds. Confidence: high.

## S3* — Complementary audit
`—`. No materially different access path to operational reality was established. Validation, sandbox and policy checks remain controls on ordinary execution. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. No first-party outside-and-then loop converts external/future environmental information into organizational adaptation and returns it to current capability. Confidence: high.

## S5 — Policy and identity
`—`. Durable human approval gates ordinary risky/current actions. It does not establish a function-specific identity/ultimate-policy issue reaching legitimate S5 authority and returning as organizational policy. OPA/configuration surfaces likewise do not themselves close S5. Confidence: high.

## Recursion, variety, and escalation
Child AgentLoops amplify operational variety; budgets, preflight, backpressure and sandbox/policy enforcement attenuate it. Lead/child hierarchy and Temporal durability support orchestration and escalation but do not by themselves establish recursive viability.

## Admission conclusion
Canonical vector: `A — C — — —`.

Same-ref correction of historical `A A C — — P`: S3 remains supported by shared current resource regulation; S2 and S5 are removed under the current function-first criteria.