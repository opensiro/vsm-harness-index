---
harness_id: claw-code-agent
project_name: claw-code-agent
repository: https://github.com/HarnessLab/claw-code-agent
review_ref: 167571da895b2a1a9e36ecfae2876984cef65e0d
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# claw-code-agent

## Review boundary
Claw Code Agent at the pinned revision as a local-model reimplementation of a coding-agent harness with nested delegation, persistent teams/messages and dependency-aware task execution.

## Repository architecture
The harness has a full coding loop, child agents, Agent Manager lineage/groups, dependency-aware topological batching, persistent task/plan runtime, Team Runtime with message history/handoff notes, budgets/policies and many developer/runtime surfaces.

## Primary evidence
- `README.md`: nested agent delegation, dependency-aware batching, Agent Manager, Team Runtime messaging/collaboration metadata, task/plan runtime and budgets.

## Operational model
Coding/child agents are S1. Delegation alone is operational decomposition, but team messaging plus dependency-aware task state exposes a first-party path by which multiple S1s can exchange coordination information and avoid invalid ordering.

## S1 — Operations
`A`: agents autonomously perform coding/tool tasks. Confidence: high.

## S2 — Coordination
`C`: team message/handoff tools and dependency-aware task state specifically expose a coordination path among workers, but a general agent-owned mutual-adjustment policy still must be composed/configured. Confidence: medium.

## S3 — Inside-and-now control
`?`: Agent Manager/budgets/task runtime do not establish autonomous whole-system resource/accountability authority.

## S3* — Complementary audit
`?`: diagnostics/history/testing are not sufficiently independent audit.

## S4 — Outside-and-then intelligence
`?`: remote triggers/search/planning are not S4.

## S5 — Policy and identity
`?`: policy/budgets remain parent-authored.

## Recursion, variety, escalation
Lineage/nested agents are explicitly tracked, but children do not demonstrate their own metasystemic closure.