---
harness_id: shannon
project_name: Shannon
repository: https://github.com/Kocoro-lab/Shannon
review_ref: 391b619130281502d227a53dd97238c9791bf174
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Shannon

## Review boundary
Pinned Python LLM service, Go Temporal orchestrator/swarm, budget/backpressure and Rust enforcement gateway.

## Repository architecture
A Swarm Lead coordinates child AgentLoops. Budget manager/preflight/backpressure regulate current resource use; approval middleware can wait on a human Temporal signal.

## Primary evidence
- Pinned deep review established Swarm Lead child coordination, budget/preflight/backpressure and human-signal approval middleware at `review_ref`.

## Operational model
Autonomous workers execute S1 work; lead coordinates them; constructor/runtime resource controls bound operation; human approval retains ultimate authority where required.

## S1 — Operations
`A`: AgentLoops autonomously perform bounded work. Confidence: high.

## S2 — Coordination
`A`: Swarm Lead actively coordinates child AgentLoops. Confidence: high.

## S3 — Inside-and-now control
`C`: budget manager, preflight and backpressure provide constructor-owned current regulation. Confidence: high.

## S3* — Complementary audit
`—`: no independent complementary audit function was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no prospective organizational adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`P`: approval middleware waits on a human Temporal signal, preserving parent authority. Confidence: high.

## Recursion, variety, escalation
Lead/child structure amplifies operational variety; budget/backpressure attenuate load; approval middleware escalates policy decisions.

## Deep-review conclusion
Signature at the pinned revision: `A A C — — P`. Shannon combines autonomous swarm coordination with strong constructor-owned resource regulation.