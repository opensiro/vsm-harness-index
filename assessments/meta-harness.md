---
harness_id: meta-harness
project_name: Meta-Harness
repository: https://github.com/stanford-iris-lab/meta-harness
review_ref: 0cbc31e97c9e6d24232d1dc754827c02e1ec415c
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Meta-Harness

## Review boundary
Pinned reusable Meta-Harness framework plus its runnable reference evolution loop: proposer-agent invocation, candidate harness generation, validation, benchmark execution, frontier tracking and final held-out evaluation. The generated task-specific harnesses are separate systems-in-focus and are not credited back to Meta-Harness.

Reviewed revision: `0cbc31e97c9e6d24232d1dc754827c02e1ec415c`, which also matched upstream `main` when rechecked on 2026-09-17. Contract: Profile `0.2.1`, Methodology `0.3.1`.

## Primary evidence
- [`README.md`](https://github.com/stanford-iris-lab/meta-harness/blob/0cbc31e97c9e6d24232d1dc754827c02e1ec415c/README.md) — framework purpose, proposer-agent wrapper and reference experiments.
- [`reference_examples/text_classification/meta_harness.py`](https://github.com/stanford-iris-lab/meta-harness/blob/0cbc31e97c9e6d24232d1dc754827c02e1ec415c/reference_examples/text_classification/meta_harness.py) — autonomous propose/validate/benchmark/frontier loop and finalization behavior.

## S1 — Operations
`A`. The system's purpose is automated search over task-specific harnesses. Its supplied loop invokes a proposer agent, validates generated candidates, benchmarks them and iterates against the current frontier without requiring a human decision each iteration. That closed search trajectory is the operational transformation at this boundary. Confidence: high.

## S2 — Coordination
`—`. Candidate systems, proposer calls and benchmark jobs are stages or alternatives inside one search operation. The reviewed framework does not establish two or more operational S1 units plus a concrete mutual-interference regulation loop. Confidence: high.

## S3 — Inside-and-now control
`—`. Frontier bookkeeping, iteration control and candidate validation govern the search procedure itself. They do not establish a distinct metasystem actor with whole-organization current view and authority over shared organizational resources, commitments or priorities. Confidence: high.

## S3* — Complementary audit
`—`. Validation benchmarking is the normal production feedback used by the search. A held-out test path exists, but it is explicitly run only when the evolution run is finalized and frozen against further evolution; its findings therefore do not feed back into subsequent current control within that run. No separate corrective audit closure is established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. The historical positive classified evolutionary harness optimization as S4. Under the function-first criterion, candidate generation and validation against task benchmarks are the primary operation of this meta-harness itself, and the information source is task-internal performance evidence. No separate outside-and-then environmental intelligence function relating future/external change back to present organizational capability was established. Confidence: high.

## S5 — Policy and identity
`—`. Domain specifications, objectives, benchmark configuration and user initiation define the search problem, but no runtime identity/ultimate-policy authority loop is supplied. Confidence: high.

## Recursion, variety, and escalation
Candidate generation amplifies harness-design variety; import checks, validation benchmarks and frontier selection attenuate it. A generated child harness may itself realize VSM functions, but it is a distinct system-in-focus requiring its own evidence.

## Admission conclusion
Canonical vector: `A — — — — —`.

Same-ref correction of the historical chat result `A — — — A —`: autonomous harness search remains S1, while optimization/evolution is no longer promoted to S4 merely because it changes future candidate behavior.