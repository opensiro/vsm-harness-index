---
harness_id: mirothinker
project_name: MiroThinker
repository: https://github.com/MiroMindAI/MiroThinker
review_ref: 1c4253f6774bf40314271a827304b842100e054c
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 1c4253f6774bf40314271a827304b842100e054c
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# MiroThinker

## Review boundary
Deep review of the pinned MiroFlow agent orchestration path, including main/sub-agent execution, duplicate-query rollback and the surrounding research/training framing. Internal loop protection and research breadth are not promoted to metasystem functions without the corresponding organizational responsibility.

## Repository architecture
MiroThinker contains a long-horizon research agent and optional sub-agents exposed as tools to the main agent. `Orchestrator` owns the model/tool turn loop for both main and delegated agents, including tool execution, context management, retry/rollback and duplicate-query suppression. Subagents receive bounded task descriptions and return their final answers to the main trajectory.

## Primary evidence
- `apps/miroflow-agent/src/core/orchestrator.py`: coordinates model calls, tool execution and sub-agent sessions and exposes delegated subagents to the main agent.
- The same orchestrator tracks duplicate queries and repeated format/refusal failures and rolls back the current agent turn when necessary.
- These rollback mechanisms stabilize one operational trajectory/subtask rather than regulate interference among independent S1 units.

## Operational model
The main research agent performs long evidence-gathering tool loops and may invoke specialized sub-agents for bounded subtasks, then integrates their returned results.

## S1 — Operations
`A`: research agents autonomously choose search/tool actions and iterate from evidence/results. Confidence: high.

## S2 — Coordination
`—`: subagents are invoked as operational capabilities and return results to the main agent. Duplicate-query and rollback protections operate inside individual agent loops, not between autonomous S1 units.

## S3 — Inside-and-now control
`—`: orchestration of current turns/subtasks does not establish whole-system regulation of shared resources, capacities or commitments.

## S3* — Complementary audit
`—`: rollback/format checking is ordinary execution control, not a distinct complementary audit channel.

## S4 — Outside-and-then intelligence
`—`: broad external research is performed to answer the current task; post-training/trajectory refinement is not a runtime prospective intelligence function governing future organizational adaptation.

## S5 — Policy and identity
`—`: models, prompts, tools and organizational topology remain externally configured.

## Recursion, variety, escalation
MiroThinker can scale operational research variety through specialist agents and long trajectories, while the reviewed harness remains centered on S1 execution.