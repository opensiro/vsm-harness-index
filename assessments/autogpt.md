---
harness_id: autogpt
project_name: AutoGPT
repository: https://github.com/Significant-Gravitas/AutoGPT
review_ref: 98381ab27f733468bfe1f9c4f4942b4b416d9a8b
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: ?
---

# AutoGPT

## Review boundary
AutoGPT repository at the pinned revision, focusing on the open-source builder/runtime rather than the vendor organization. The previous stored SHA was not resolvable upstream; this deep review explicitly repins the assessment to the current reproducible default-branch HEAD shown above.

## Repository architecture
The platform executes visual block graphs on demand, schedules or triggers. Runtime execution/scheduling is deterministic infrastructure around agent/model blocks. The repository also contains a `dream` memory-maintenance pipeline that consolidates, recombines and sanitizes recent memory before applying updates.

## Primary evidence
- `autogpt_platform/backend/backend/executor/scheduler.py`: schedules recurring graph execution and creates graph runs.
- `autogpt_platform/backend/backend/data/execution.py` and executor utilities: maintain node execution state/queues for graph execution.
- `autogpt_platform/backend/backend/copilot/dream/orchestrator.py`: explicitly describes a three-phase `consolidate → recombine → sanitize` pass over a user's recent memory window and applies resulting memory operations.
- Builder/agent-generation guidance requires authored input/trigger/output blocks, confirming graph topology and triggers are application-defined runtime structure.

## Operational model
An executing agent/workflow is the S1. Scheduler, graph executor and monitoring are runtime infrastructure. The dream pass changes internal memory representations from prior interaction history rather than maintaining a separate external/future intelligence role.

## S1 — Operations
`A`: model/tool blocks execute outcome-oriented workflows within bounded graph runs. Confidence: high.

## S2 — Coordination
`—`: graph branching, node scheduling and deterministic execution do not establish mutual adjustment among autonomous operational S1 units. Confidence: high.

## S3 — Inside-and-now control
`?`: run state, queues, scheduling and monitoring regulate execution infrastructure, but this pass did not establish agent-owned whole-system current authority over shared operational commitments/resources.

## S3* — Complementary audit
`?`: monitoring/run visibility can detect failures, but no sufficiently independent agent-owned audit path with corrective closure was established.

## S4 — Outside-and-then intelligence
`—`: schedules/triggers are reactive execution mechanisms, while the `dream` pipeline is internal memory consolidation/recombination. Neither is the required distinct external-and-prospective intelligence function that generates adaptation options and couples them back through S3. Confidence: high.

## S5 — Policy and identity
`?`: goals, graph topology, credentials and permissions remain parent/application-authored; no runtime ultimate-policy closure was established.

## Recursion, variety, escalation
Graph composition expands operational variety but does not imply recursive viability.

## Deep-review result
`S4` resolves from `?` to `—`; the rest of the vector remains `A — ? ? — ?`.