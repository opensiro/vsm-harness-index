---
harness_id: deepagents
project_name: Deep Agents
repository: https://github.com/langchain-ai/deepagents
review_ref: 9e7d62ff6e7131505995a706d717e01837aa8617
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Deep Agents

## Review boundary
Deep review of the pinned core subagent middleware and long-horizon agent stack. Isolated/forked subagents are evaluated as delegation unless a separate cross-S1 regulation function is present.

## Repository architecture
Deep Agents layers planning, filesystem/shell access, summarization, skills, memory and subagents onto an autonomous agent. Its core `task` middleware exposes declarative or compiled subagents. By default a subagent receives only the delegated task; optional fork mode continues parent context. The parent selects a specialist and consumes its result. This is intentionally context-isolated task decomposition, not mutual coordination among peer S1s.

## Primary evidence
- `libs/deepagents/deepagents/middleware/subagents.py`: defines isolated/forked subagents exposed to the main agent through a `task` tool.
- Subagent results are returned to the parent as a tool result/structured response; recursive delegation is explicitly bounded.
- Tools, permissions, middleware, skills and HITL can differ per subagent but remain application-defined execution boundaries.

## Operational model
A main long-horizon agent plans and acts through tools, delegating bounded tasks to specialist subagents when useful and incorporating their returned results into the parent trajectory.

## S1 — Operations
`A`: agents autonomously choose tools/actions and perform filesystem/shell or other application work. Confidence: high.

## S2 — Coordination
`—`: isolated/forked `task` calls implement parent-to-child delegation and result return. No mechanism was established for regulating interference, oscillation or shared constraints among multiple autonomous S1 units. The shallow `S2=A` interpretation is removed.

## S3 — Inside-and-now control
`—`: parent delegation and middleware policy do not constitute whole-system current authority over multiple operational resources/capacity/commitments.

## S3* — Complementary audit
`—`: no first-party independent complementary audit channel with distinct authority was established.

## S4 — Outside-and-then intelligence
`—`: planning, memory, summarization and skills improve current/recurring task execution but do not establish a distinct prospective environmental-intelligence function.

## S5 — Policy and identity
`—`: prompts, tools, skills, permissions and HITL remain application/developer supplied.

## Recursion, variety, escalation
Deep Agents provides strong recursive decomposition and context isolation while leaving metasystem closure outside the core harness.