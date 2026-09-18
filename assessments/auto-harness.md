---
harness_id: auto-harness
project_name: Auto Harness
repository: https://github.com/neosigmaai/auto-harness
review_ref: 52360dbbeb8cea8886d90778e634a145c51da735
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Auto Harness

## Review boundary

- System in focus: the first-party self-improving harness-engineering loop defined by `PROGRAM.md`/program templates, benchmark adapters, gating, results/learnings state and target-agent edit protocol at pinned revision `52360dbbeb8cea8886d90778e634a145c51da735`.
- Purpose and identity: autonomously improve a target agent harness against a configured benchmark while protecting prior gains with a maintained regression suite and held-out/full-test gate.
- Relevant environment: the target harness, benchmark tasks/environments, external coding-agent host, model providers, Harbor/tau/BIRD integrations and the human-authored experiment configuration.
- Standard-distribution boundary: Auto Harness program/gating/benchmark/workspace machinery. External coding-agent software and external benchmark runtimes remain dependencies/actors rather than inherited functionality.
- Recursion level: one harness-optimization operation; the target agent is the mutable artifact being optimized, not a child VSM credited back by default.
- Reviewed revision: `52360dbbeb8cea8886d90778e634a145c51da735`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Repository architecture

A coding agent is instructed to run the benchmark, inspect train failures/traces, edit `agent/agent.py`, execute a multi-step gate, record accepted results, append learnings and repeat. The gate rejects unauthorized file edits, requires the regression suite to pass, requires held-out/full-test score to meet the best recorded score, and promotes newly fixed train tasks into the regression suite. Failed hypotheses are reverted; repeated failures cause the agent to abandon the hypothesis.

## Primary evidence

- [`README.md`](https://github.com/neosigmaai/auto-harness/blob/52360dbbeb8cea8886d90778e634a145c51da735/README.md) — system purpose, benchmark adapters, loop, gating, state and human/external-host boundary.
- [`program_templates/base.md`](https://github.com/neosigmaai/auto-harness/blob/52360dbbeb8cea8886d90778e634a145c51da735/program_templates/base.md) — autonomous coding-agent responsibilities, edit rights, gate/record/revert loop and stop condition.

## Operational model

The primary operation is benchmark-driven harness improvement. The externally hosted coding agent is the autonomous actor executing the first-party Auto Harness program: it diagnoses failures, chooses a general change, edits the target harness, interprets gate outcomes and either keeps or reverts the change. Benchmark/gating components enforce the experiment contract but do not become separate organizational owners merely by producing scores.

## S1 — Operations

- State: `A`.
- Function: autonomously transform the target agent harness through repeated diagnose-change-evaluate-keep/revert cycles.
- Disturbance / variety regulated: benchmark failures, trace evidence, regression risk and alternative harness-improvement hypotheses.
- Decisive decision or feedback right: the coding agent selects diagnoses and harness changes and decides the next hypothesis based on gate results within the supplied program.
- Decision owner: autonomous coding-agent actor executing the first-party program.
- Supporting / enforcement mechanisms: benchmark runners, file guard, regression suite, held-out/full-test gate, results ledger and learnings file.
- Closure path: successful changes are committed and become the next harness baseline; failed changes are reverted and the next iteration consumes the recorded outcome.
- Basis / confidence: explicit + structural; high.

## S2 — Coordination

- State: `—`.
- The reviewed optimization loop has one primary coding-agent work cell. Benchmark tasks and runner concurrency are evaluation workload, not multiple organizational S1 units with a mutual-interference regulation loop.
- Confidence: high.

## S3 — Inside-and-now control

- State: `—`.
- Gating, stop conditions, configuration and benchmark execution constrain the primary optimization operation. No distinct first-party actor is established with a current whole-system view and discretionary authority over shared organizational resources, priorities or commitments.
- Runtime enforcement is not promoted to S3 ownership.
- Confidence: high.

## S3* — Complementary audit

- State: `—`.
- Regression and held-out/full-test evaluation are the ordinary acceptance path of the optimization operation. They are intentionally protected against train-trace leakage, but the pinned system does not establish a separate complementary auditor with independent access and a corrective feedback channel beyond that normal production gate.
- Confidence: high.

## S4 — Outside-and-then intelligence

- State: `—`.
- The system learns from benchmark failures and updates the harness, but this is internal task-distribution optimization. No externally and prospectively oriented environment model generates adaptation options and closes them back into current organizational capability.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- Humans choose the benchmark/configuration and can edit the program, but the reviewed distribution does not provide a runtime identity/ultimate-policy issue → parent decision → return-to-operation loop.
- Confidence: high.

## Recursion

The target agent being optimized can itself be assessed separately. Auto Harness does not inherit the target harness's VSM functions.

## Variety and escalation

Failure traces amplify actionable design distinctions; one-change-per-iteration discipline, regression/full-test gates and reversion attenuate unsafe search variety. The program can surface “needs from human,” but this generic assistance path is not classified as S3/S4/S5 parent closure.

## Evidence gaps

External coding-agent host semantics are not inherited; only the autonomy explicitly required by the first-party optimization program is credited.

## Admission conclusion

Canonical vector: `A — — — — —`.
