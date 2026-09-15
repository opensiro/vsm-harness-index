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
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Mastra

## Review boundary
Mastra at the pinned revision as a TypeScript agent/application framework, including the first-party agent-network/supervisor composition path. Evals/observability remain support unless closed into an autonomous organizational role.

## Repository architecture
Mastra agents reason and choose tools. Authored workflows are deterministic control, while the separate agent-network path gives an LLM routing agent a set of subagents/workflows/tools plus memory so it can choose which primitive to call, in what order, with what data, and determine task completion.

## Primary evidence
- `docs/src/content/en/docs/agents/networks.mdx`: a routing agent interprets the request and autonomously selects subagents/workflows/tools and their ordering; memory stores task history and is required for completion determination.
- The same first-party path supports suspension/resume and approval snapshots, which remain parent/runtime controls rather than additional VSM functions.
- Network mode is explicitly a composable/deprecated path being replaced by supervisor agents, not the default behavior of every Mastra agent.

## Operational model
A normal Mastra agent is S1. Deterministic graph workflows do not create S2/S3. The optional routing-agent network, however, reasons over current task history and dynamically regulates which operational units run next until completion.

## S1 — Operations
`A`: agents autonomously choose tools and iterate toward task completion. Confidence: high.

## S2 — Coordination
`—`: network routing chooses/delegates work but no distinct mutual-adjustment or conflict-dampening relation among autonomous S1s is established.

## S3 — Inside-and-now control
`C`: the first-party routing/supervisor pattern owns current selection and sequencing of subagents/workflows/tools using task history and completion state. That is composable current regulation, but not the default closed path for all agents.

## S3* — Complementary audit
`—`: evals, structured output and approval/suspension mechanisms support checking/control but do not establish a distinct autonomous audit channel with corrective authority.

## S4 — Outside-and-then intelligence
`—`: memory, RAG and planning remain current-task capabilities; no distinct prospective environment-to-S3 loop is established.

## S5 — Policy and identity
`—`: instructions, primitive descriptions, approvals and workflow/network policy remain developer/user supplied.

## Recursion, variety, escalation
Networks/supervisors increase organizational composition, but nesting itself is not recursive viable-system closure.