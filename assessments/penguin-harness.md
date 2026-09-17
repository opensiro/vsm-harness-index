---
harness_id: penguin-harness
project_name: PenguinHarness
repository: https://github.com/Prism-Shadow/penguin-harness
review_ref: 77c746954f92a588295de1c2dad362b1b8593f19
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# PenguinHarness

## Review boundary
Pinned first-party PenguinHarness standard distribution at `77c746954f92a588295de1c2dad362b1b8593f19`, focusing on target-agent execution plus the agent-tuning evaluator/optimizer loop. Generated downstream applications are separate systems-in-focus and are not automatically credited back to the platform.

Contract: Profile `0.2.1`, Methodology `0.3.1`. Current upstream was inspected for drift; the candidate pin is preserved rather than silently advanced.

## Primary evidence
- [`README.md`](https://github.com/Prism-Shadow/penguin-harness/blob/77c746954f92a588295de1c2dad362b1b8593f19/README.md) — target-agent lifecycle and self-evolution surface.
- [`plugins/agent-tuning/skills/agent-evaluation/SKILL.md`](https://github.com/Prism-Shadow/penguin-harness/blob/77c746954f92a588295de1c2dad362b1b8593f19/plugins/agent-tuning/skills/agent-evaluation/SKILL.md) — isolated Test Agent workspace, hidden rubric, trace binding and evaluator-owned scoring.
- [`plugins/agent-tuning/skills/agent-optimization/SKILL.md`](https://github.com/Prism-Shadow/penguin-harness/blob/77c746954f92a588295de1c2dad362b1b8593f19/plugins/agent-tuning/skills/agent-optimization/SKILL.md) — evidence/hypothesis/candidate/evaluation loop with strict improvement, snapshots and rollback.

## S1 — Operations
`A`. A configured target agent autonomously performs task work through the Penguin runtime. Its model/tool loop owns the next operational action inside the configured task boundary. Confidence: high.

## S2 — Coordination
`—`. Target, evaluator and optimizer are stages in an evaluation/optimization pipeline, not multiple operational S1 units whose mutual interference is regulated by an S2 function. Parallel evaluation cells and subagent calls are execution structure, not sufficient evidence of S2. Confidence: high.

## S3 — Inside-and-now control
`—`. The optimizer changes durable future Agent State after evaluations. That is not a separate whole-system current regulator with authority over shared organizational resources, commitments, priorities or constraints. The historical `A` promoted optimization authority into S3. Confidence: high.

## S3* — Complementary audit
`A`. The evaluator is deliberately separated from the target's normal production path: the target receives the public Statement but cannot access the private Rubric/Gold/scoring rules, while the evaluator later inspects the isolated workspace, bound root/child traces and the private Rubric to make its own score judgment. That score enters the optimizer's accept-or-rollback decision, changing subsequent retained Agent State. This establishes a first-party complementary audit channel with autonomous evaluator ownership. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. The optimizer searches improvements against a frozen benchmark using scores and traces from the target's own task executions. Durable self-improvement is real, but the reviewed path does not establish the required outside-and-then environmental intelligence relation; optimization/learning alone is not S4. Confidence: high.

## S5 — Policy and identity
`—`. The target purpose, benchmark, desired score and optimization initiation are parent-authored constraints. They do not form a runtime identity/ultimate-policy tension-resolution loop with legitimate S5 authority. Parent configuration therefore does not imply `P`. Confidence: high.

## Recursion, variety, and escalation
Evaluation isolates evidence variety from the target; candidate generation amplifies possible future operational variety; strict score improvement, snapshots and rollback attenuate it. Generated agents or applications are separate recursion-level systems and require independent assessment.

## Admission conclusion
Canonical vector: `A — — A — —`.

Same-ref correction of historical `A C A A A P`: the isolated private-rubric evaluator remains a strong autonomous S3* witness; pipeline composition, optimizer control, self-evolution and parent-authored goals no longer stand in for S2, S3, S4 or S5.