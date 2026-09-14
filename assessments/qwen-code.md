---
harness_id: qwen-code
project_name: Qwen Code
repository: https://github.com/QwenLM/qwen-code
review_ref: 01aa4f267fd4f76a47a391a858f86c855aceb0ba
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Qwen Code

## Review boundary
Qwen Code at the pinned revision across its terminal/editor/SDK agent harness and standard SubAgents/Agent Teams features.

## Repository architecture
Qwen Code ships an autonomous coding agent with auto-memory, skills, subagents, agent teams, dynamic workflows, hooks, MCP, sandbox/worktrees and headless operation. It also provides built-in review/batch/loop/bugfix skills and an evaluation harness.

## Primary evidence
- `README.md`: agentic out of the box; SubAgents/Agent Teams/Dynamic Workflows; hooks/skills/sandbox; headless mode; evaluation section.

## Operational model
Coding agents/subagents perform S1 work. The README establishes team topology but does not specify a concrete Beer-style coordination decision right distinct from delegation/workflow control.

## S1 — Operations
`A`: standard agents autonomously act on code/tools with optional unattended mode. Confidence: high.

## S2 — Coordination
`?`: Agent Teams are first-party, but evidence is insufficient to distinguish mutual adjustment/conflict regulation from delegation/dynamic workflow routing.

## S3 — Inside-and-now control
`?`: team/workflow control does not prove whole-system resource/accountability authority.

## S3* — Complementary audit
`?`: `/review` and evaluation are operational/developer evaluation paths; sufficient independence and corrective authority are not established.

## S4 — Outside-and-then intelligence
`?`: auto-memory/skills and self-iteration do not by themselves establish S4.

## S5 — Policy and identity
`?`: hooks/rules/permissions remain configured constraints.

## Recursion, variety, escalation
Subagents/teams are composition and do not automatically establish recursive viability.