---
harness_id: autoharness
project_name: AutoHarness
repository: https://github.com/aiming-lab/AutoHarness
review_ref: 3561e468f9ca9f9bf282512e695bd32e4e90fef4
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 3561e468f9ca9f9bf282512e695bd32e4e90fef4
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# AutoHarness

## Review boundary
AutoHarness at the pinned revision as a governance wrapper/full agent loop with deterministic risk/permission/output/audit pipeline and first-party multi-agent orchestration primitives.

## Repository architecture
Every tool call passes parse/validate, risk classification, permission check, execution, output sanitization and audit logging. Enhanced mode adds turn governor, failure hooks, fork/background execution, a mailbox-based swarm mode, coordinator mode and built-in specialist agents including an adversarial Verification agent. Constitution, budgets and permissions are explicit parent configuration.

## Primary evidence
- `README.md`: governance modes/pipeline, risk classifier, permission checks, JSONL audit, trace diagnostics, multi-agent profiles and constitution.
- `docs/features.md`: Enhanced mode ships Fork, Background, Swarm with JSONL mailbox, Coordinator delegated execution, and built-in Explore/Plan/Verification/General agent types.
- `docs/concepts/agents.md`: swarm agents communicate through shared mailboxes; shutdown uses a request/response handshake; coordinator mode dispatches all work to typed workers.
- `autoharness/agents/swarm.py`: first-party `TeamMailbox` plus `message`, `broadcast`, `shutdown_request`, `shutdown_response`, and `plan_approval_response` protocol messages.
- `docs/guides/multi-agent.md`: documented pattern for forking a Verification agent after implementation and for coordinator workflows that sequence exploration, implementation and verification.
- `autoharness/agents/builtin.py`: the built-in Verification agent is explicitly adversarial, runs build/tests/lint/type checks and edge-case probes, records observed outputs, and returns PASS/FAIL/PARTIAL.

## Operational model
The model-driven AgentLoop is S1. The deterministic governance pipeline constrains operational variety but is not itself an autonomous metasystem. Separately, the standard distribution exposes cross-agent mailbox/protocol primitives and an explicit adversarial verifier role. Those are specific constructor paths toward S2 and S3*, but they still require the application/coordinator to compose the authority and closure loop.

## S1 — Operations
`A`: full AgentLoop autonomously reasons/uses tools under governance. Confidence: high.

## S2 — Coordination
`C`: swarm mode supplies a first-party inter-agent mailbox and explicit coordination protocol messages, including plan-approval and shutdown handshakes. These are more than parent→child delegation, but the repository does not provide a general out-of-box agent-owned policy that resolves interference/oscillation across arbitrary S1s; the developer/coordinator still composes that closure. Confidence: high.

## S3 — Inside-and-now control
`—`: the turn governor, budgets and Coordinator pattern regulate or route execution, but the standard evidence shows delegated workflow composition rather than an autonomous whole-system current regulator bargaining resources/priorities across independent S1s.

## S3* — Complementary audit
`C`: AutoHarness ships a dedicated adversarial Verification agent with direct workspace/tool access and a documented post-implementation verification pattern. It can obtain complementary evidence by executing builds, tests, linters and adversarial probes rather than relying on the worker's report. However, invoking it and closing FAIL/PARTIAL results back into corrective execution remain application/coordinator-composed rather than an always-on independent audit loop. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: model routing, diagnostics, hooks and adaptation-related mechanisms do not establish an externally and prospectively oriented intelligence function coupled back to present operational control.

## S5 — Policy and identity
`—`: the YAML constitution and permission/risk policy are explicitly parent-authored deterministic constraints, not agent-owned policy closure.

## Recursion, variety, escalation
Governance attenuates S1 variety. Fork/background/swarm workers are operational agents; their existence does not establish recursive viability without their own metasystemic closure.