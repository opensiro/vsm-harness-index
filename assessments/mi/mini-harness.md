---
harness_id: mini-harness
project_name: mini-harness
repository: https://github.com/mini-harness/mini-harness
review_ref: 340d2d9f1bcc833483d2924770448fcf4ef788be
reviewed_at: 2026-09-17
profile_version: 0.2.2
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

# mini-harness

## Review boundary
Pinned first-party mini-harness coding-agent runtime at `340d2d9f1bcc833483d2924770448fcf4ef788be`, including its interactive/task execution modes, tool loop, session state, retries and context compaction. Harbor/SWE-bench scorers remain outside the harness system-in-focus.

Contract: Profile `0.2.2`, Methodology `0.3.1`. Generation provenance is not backfilled because the pre-admission proposal did not record it.

## Primary evidence
- [`README.md`](https://github.com/mini-harness/mini-harness/blob/340d2d9f1bcc833483d2924770448fcf4ef788be/README.md) — stated harness boundary, tools, compaction, retries and benchmark adapters.
- [`src/mini_harness/agent.py`](https://github.com/mini-harness/mini-harness/blob/340d2d9f1bcc833483d2924770448fcf4ef788be/src/mini_harness/agent.py) — model/tool iteration, result feedback, execution bounds and interactive approval path.

## Repository architecture
The runtime wraps a model-driven coding agent with typed workspace tools, session history, context compaction, request retries and finite turn/wall-clock limits. Interactive execution can request permission before selected tool calls; task execution can run with an allow policy. Benchmark adapters invoke the same operational agent and hand results to external evaluation rather than supplying an internal metasystem.

## Operational model
One coding-agent S1 transforms the target workspace. Retries, compaction, limits and permissions bound that operation but do not create additional organizational functions.

## S1 — Operations
`A`. The model-driven agent chooses successive tool actions and incorporates tool results into later turns until completion or an execution bound is reached. The decisive operational action right is agent-owned within configured limits. Confidence: high.

## S2 — Coordination
`—`. No distinct peer S1 units plus a specific inter-S1 interference/conflict/oscillation and an attenuation loop are established. Sequencing tools inside one agent is not S2. Confidence: high.

## S3 — Inside-and-now control
`—`. Turn limits, wall-clock limits, retries and permission enforcement constrain one operation. They do not establish a separate whole-system current view with discretionary authority over organizational resources, commitments or priorities. Confidence: high.

## S3* — Complementary audit
`—`. Harbor/SWE-bench verification belongs to the external evaluation membrane. No first-party independent audit judgment with corrective closure back into the running organization is established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. Context compaction, retry and session persistence react to current execution. No external-and-prospective adaptation loop generates options and returns them into present capability. Confidence: high.

## S5 — Policy and identity
`—`. User permission prompts, provider/model selection and supplied task/policy constraints do not establish a runtime identity or ultimate-policy tension-resolution loop. The earlier proposal over-promoted generic human approval to `P`. Confidence: high.

## Recursion, variety, and escalation
Model/tool choice amplifies operational variety; typed tools, compaction, retries and finite budgets attenuate it. Interactive approval can escalate an individual tool call to the user, but that local permission path is not S5.

## Admission conclusion
Canonical vector: `A — — — — —`.

Pre-admission correction from the stale proposal `A — — — — P`: generic parent configuration/approval is not sufficient evidence of S5 under the current function-first contract.