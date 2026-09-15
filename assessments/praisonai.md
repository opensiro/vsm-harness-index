---
harness_id: praisonai
project_name: PraisonAI
repository: https://github.com/MervinPraison/PraisonAI
review_ref: 43a106db26d399d312370f8eeca949a5ba135c5b
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# PraisonAI

## Review boundary
PraisonAI at the pinned revision as an agent/multi-agent framework with autonomous agents, `AgentTeam`, AgentFlow, and selectable team execution modes.

## Repository architecture
PraisonAI provides autonomous agents, tools/MCP, guardrails, approval/hooks/sandbox, AgentFlow graph primitives, and multi-agent team execution. The TypeScript team runtime exposes sequential/parallel execution plus an optional `hierarchical` process backed by a synthetic Manager agent.

## Primary evidence
- `src/praisonai-ts/src/agent/team.ts`: `AgentTeam` dispatches team execution and reaches the hierarchical manager path when `process: 'hierarchical'` is selected.
- `src/praisonai-ts/src/agent/team-manager.ts`: the Manager receives the status of every real task, chooses the next task and assignee, can re-delegate failed work, and can stop the team run.
- Python parity is implemented by `src/praisonai-agents/praisonaiagents/process/process.py::Process.hierarchical` at the reviewed product boundary.

## Operational model
Individual agents are S1. Sequential, parallel, route, loop, and graph primitives structure execution but are not themselves Beer-style coordination. The optional hierarchical Manager is stronger: it reasons over current team-wide task state and owns assignment/reassignment and completion decisions.

## S1 — Operations
`A`: agents autonomously reason, choose tools and execute bounded tasks. Confidence: high.

## S2 — Coordination
`—`: reviewed team modes route/delegate work; no distinct mutual-adjustment or conflict-dampening function among autonomous S1 units is established.

## S3 — Inside-and-now control
`C`: the first-party hierarchical Manager sees all task statuses, selects work/assignees, re-delegates failures and may terminate the team run. That is current whole-team regulation, but it is an explicitly selected process rather than closed/default ownership.

## S3* — Complementary audit
`—`: verification/reflection/self-correction paths are normal production checking and do not establish a distinct complementary audit channel with independent corrective authority.

## S4 — Outside-and-then intelligence
`—`: reflection, planning and self-improvement language remains current-task/internal adaptation; no distinct prospective environment-to-S3 intelligence loop is established.

## S5 — Policy and identity
`—`: guardrails, prompts, approvals, process mode and team policy remain developer/user supplied.

## Recursion, variety, escalation
Team nesting and graph composition increase operational variety; they do not independently establish recursive viable systems.