---
harness_id: mastra
project_name: Mastra
repository: https://github.com/mastra-ai/mastra
review_ref: 76cec9be889c0a6ae7f51fbf25356d5a06019351
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Mastra

## Review boundary
Mastra at the pinned revision as a TypeScript agent/application framework, including the first-party agent-network/supervisor composition path and task-completion scoring. Offline evals/observability remain support unless closed into runtime control.

## Repository architecture
Mastra agents reason and choose tools. Authored workflows are deterministic control, while the separate agent-network/supervisor path gives an LLM supervisor a set of subagents/workflows/tools plus task history so it can choose which primitive to call, in what order and with what data. The same path can attach independent task-completion scorers that gate whether the supervisor may finish.

## Primary evidence
- `docs/src/content/en/docs/agents/networks.mdx`: a routing agent interprets the request and autonomously selects subagents/workflows/tools and their ordering; memory stores task history and is required for completion determination.
- `docs/src/content/en/reference/migrations/network-to-supervisor.mdx`: the recommended supervisor path retains autonomous delegation/iteration and exposes `isTaskComplete.scorers`; failed completion validation makes the supervisor continue iterating and inserts scorer feedback into conversation context for subsequent work.
- `packages/core/src/loop/network/validation.ts` and the network/supervisor loop integrate completion-scoring results into runtime completion control rather than only offline evaluation.
- Network/supervisor composition is a selectable first-party path rather than the closed behavior of every ordinary Mastra agent.

## Operational model
A normal Mastra agent is S1. Deterministic graph workflows do not create S2/S3. In the optional supervisor path, however, one agent reasons over current task history and dynamically regulates which operational primitives run next until completion. A distinct scorer can independently reject the proposed completion and feed corrective information back into that loop.

## S1 — Operations
`A`: agents autonomously choose tools and iterate toward task completion. Confidence: high.

## S2 — Coordination
`—`: supervisor routing chooses/delegates work but no distinct mutual-adjustment or conflict-dampening relation among autonomous S1s is established.

## S3 — Inside-and-now control
`C`: the first-party supervisor/network path owns current selection and sequencing of subagents/workflows/tools using task history and completion state. That is composable current regulation, but not the default closed path for all agents.

## S3* — Complementary audit
`C`: first-party task-completion scorers separately assess whether the supervisor's current result satisfies completion criteria; a failed verdict blocks completion, adds feedback and causes further iteration. The audit decision right is composable/configured rather than universally enabled.

## S4 — Outside-and-then intelligence
`—`: memory, RAG and planning remain current-task capabilities; no distinct prospective environment-to-S3 loop is established.

## S5 — Policy and identity
`—`: instructions, primitive descriptions, scorers, approvals and workflow/network policy remain developer/user supplied.

## Recursion, variety, escalation
Supervisor/subagent composition increases organizational variety and adds a complementary completion gate, but nesting itself is not recursive viable-system closure.