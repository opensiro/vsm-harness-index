---
harness_id: qwen-code
project_name: Qwen Code
repository: https://github.com/QwenLM/qwen-code
review_ref: 01aa4f267fd4f76a47a391a858f86c855aceb0ba
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Qwen Code

## Review boundary
Deep review of the pinned coding-agent runtime with special attention to first-party Agent Teams. The positive S2/S3 classifications come from actual team decision rights and shared coordination state, not from subagent terminology alone.

## Repository architecture
Qwen Code ships a terminal coding agent, isolated subagents and a richer Agent Teams subsystem. A model-driven team lead can create the team and task board, spawn teammates, create and assign tasks, receive reports, reassign ownership and shut down workers. Teammates share the task board, can claim newly available work, create tasks, update ownership/status and directly message peers. `TeamManager` maintains the runtime substrate—mail delivery, idle detection, lifecycle and automatic claiming—around those agent-owned decisions.

## Primary evidence
- `packages/core/src/tools/team-create.ts`: the lead agent is instructed to create teams/tasks, spawn teammates, assign work, receive reports and shut the team down.
- `packages/core/src/tools/team-create.ts`: teammates are instructed to inspect the shared task list, claim unassigned/unblocked work, create new tasks, mark completion and communicate with peers/team lead.
- `packages/core/src/agents/team/tasks.ts`: persistent shared task board supports ownership, task claiming, dependencies/blocking and concurrency-safe updates; ownership conflicts are actively rejected.
- `packages/core/src/agents/team/TeamManager.ts`: central runtime bridges team events, priority messages, idle state and auto-claim while preserving the agent-driven task/message control surface.

## Operational model
The lead agent decomposes project work into shared commitments and delegates to autonomous teammates. Teammates mutually adjust through peer messages, task ownership, dependency state and claiming. The lead can reshape current team commitments through assignments/reassignments and team lifecycle decisions.

## S1 — Operations
`A`: individual coding agents autonomously select tools/actions and perform useful workspace work. Confidence: high.

## S2 — Coordination
`A`: teammates have first-party peer communication plus a shared dependency/ownership task board and can autonomously claim/update work. These mechanisms explicitly manage cross-agent dependencies, ownership conflicts and blocked/unblocked work rather than merely fan out tasks. Confidence: high.

## S3 — Inside-and-now control
`A`: the autonomous team lead owns the current team task structure, creates and assigns commitments, can change ownership, receives team-wide progress/reports and controls teammate lifecycle. This provides whole-team current regulation over operational commitments. Confidence: high.

## S3* — Complementary audit
`—`: read-only/review-capable teammates can be configured, but no default independent complementary audit channel with distinct authority is established.

## S4 — Outside-and-then intelligence
`—`: Auto-Memory/Auto-Skills and task planning may improve future operation, but the reviewed team/runtime boundary does not establish a separate prospective environmental-intelligence function responsible for adapting system strategy/capability.

## S5 — Policy and identity
`—`: team mission, policies, permissions, agent definitions and ultimate authority remain externally supplied.

## Recursion, variety, escalation
Qwen Code closes S2 and S3 around multiple coding S1s out of the box. It therefore belongs with the strongest current metasystem implementations in the reviewed cohort, while S3*, S4 and S5 remain open.