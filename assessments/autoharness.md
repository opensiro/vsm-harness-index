---
harness_id: autoharness
project_name: AutoHarness
repository: https://github.com/aiming-lab/AutoHarness
review_ref: 3561e468f9ca9f9bf282512e695bd32e4e90fef4
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: —
---

# AutoHarness

## Review boundary
AutoHarness at the pinned revision as a governance wrapper/full agent loop with deterministic risk/permission/output/audit pipeline and multi-agent profiles.

## Repository architecture
Every tool call passes parse/validate, risk classification, permission check, execution, output sanitization and audit logging. Enhanced mode adds turn governor, failure hooks and fork/swarm/background profiles. Constitution, budgets and permissions are explicit configuration.

## Primary evidence
- `README.md`: governance modes/pipeline, risk classifier, permission checks, JSONL audit, trace diagnostics, multi-agent profiles and constitution.

## Operational model
The model-driven AgentLoop is S1. The governance pipeline constrains it deterministically. Multi-agent profiles expose topology, but details are insufficient to prove S2.

## S1 — Operations
`A`: full AgentLoop autonomously reasons/uses tools under governance. Confidence: high.

## S2 — Coordination
`?`: fork/swarm/background multi-agent profiles exist but the reviewed evidence does not establish mutual-adjustment semantics.

## S3 — Inside-and-now control
`?`: turn governor/budgets are deterministic governance, not autonomous S3 enactment.

## S3* — Complementary audit
`?`: audit logs and trace diagnostics record/inspect the normal governance path; no sufficiently independent evaluator with alternative access and corrective authority is supplied.

## S4 — Outside-and-then intelligence
`?`: no prospective adaptation function verified.

## S5 — Policy and identity
`—`: the YAML constitution and permission/risk policy are explicitly parent-authored deterministic constraints, not agent-owned policy closure.

## Recursion, variety, escalation
Governance attenuates S1 variety; multi-agent profiles do not automatically establish recursion.