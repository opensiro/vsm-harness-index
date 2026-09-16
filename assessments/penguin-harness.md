---
harness_id: penguin-harness
project_name: PenguinHarness
repository: https://github.com/Prism-Shadow/penguin-harness
review_ref: 77c746954f92a588295de1c2dad362b1b8593f19
reviewed_at: 2026-09-16
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: P
---

# PenguinHarness

## Review boundary
Pinned standard distribution including benchmark builder, target agent, evaluators and agent-tuning optimizer.

## Repository architecture
The harness builds/calibrates a benchmark, runs a target agent, evaluates isolated outputs with private rubrics, and feeds scores/traces into an optimizer that can edit durable agent state under bounded acceptance and rollback rules.

## Primary evidence
- Pinned review established benchmark construction/calibration, target-agent execution, isolated evaluators and optimizer-driven state updates at `review_ref`.
- Optimizer acceptance is strict-improvement gated and preserves snapshots/versioning for rollback.

## Operational model
Target execution is the operational S1. Evaluation and optimization form a closed improvement loop around it; benchmark/capability intent remains parent-owned.

## S1 — Operations
`A`: target agent autonomously performs benchmark work. Confidence: high.

## S2 — Coordination
`C`: the distribution supplies composable coordination across target/evaluator/optimizer stages, but constructor configuration determines the concrete organization. Confidence: medium-high.

## S3 — Inside-and-now control
`A`: optimizer regulates current operational state using scores/traces and bounded edits. Confidence: high.

## S3* — Complementary audit
`A`: isolated evaluators with private rubric provide a distinct assessment channel feeding corrective closure. Confidence: high.

## S4 — Outside-and-then intelligence
`A`: evidence-backed optimization produces durable future-facing agent-state adaptation with acceptance/rollback. Confidence: high.

## S5 — Policy and identity
`P`: target capability, benchmark intent and initiation remain parent-owned. Confidence: high.

## Recursion, variety, escalation
Evaluation attenuates result variety; optimizer edits amplify corrective variety. Acceptance and rollback constrain adaptation while parent authority fixes the outer purpose.

## Deep-review conclusion
Signature at the pinned revision: `A C A A A P`. The standard distribution closes operations, audit and durable adaptation while retaining ultimate purpose with the parent.