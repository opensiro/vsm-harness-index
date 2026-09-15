---
harness_id: claude-agent-sdk
project_name: Claude Agent SDK
repository: https://github.com/anthropics/claude-agent-sdk-python
review_ref: 37a52c9fb3f0271de017911914b0d42efea6267e
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Claude Agent SDK

## Review boundary
Deep review of the pinned Python SDK's agent definitions, hooks, permissions, MCP integration and subagent/session surfaces. Configurable callbacks and delegated specialists are not promoted to metasystem functions unless the SDK supplies the corresponding organizational responsibility.

## Repository architecture
Claude Agent SDK exposes long-running Claude Code agent sessions with built-in/MCP tools, inline or filesystem agent definitions, permissions and lifecycle/tool hooks. Subagents have distinct transcripts and configured agent definitions, while hooks can block execution or add feedback. These are strong application control primitives around operational agents, but the reviewed SDK does not itself create a coordination, whole-system regulation or independent audit function.

## Primary evidence
- `src/claude_agent_sdk/types.py`: hook outputs can continue/stop/block execution and return tool-specific permission decisions or context.
- `src/claude_agent_sdk/types.py` / SDK agent-definition surface: applications define specialist agents and their tool/instruction boundaries.
- Subagent/session support preserves separate subagent transcripts, but delegation and transcript separation do not themselves regulate interference among autonomous S1 units.

## Operational model
A configured Claude agent receives a task, selects tools, acts through Claude Code/MCP capabilities and iterates. Applications may provide specialist agents and callbacks that constrain or observe execution.

## S1 — Operations
`A`: the normal SDK session supports autonomous tool selection/action over long-running coding or general tasks. Confidence: high.

## S2 — Coordination
`—`: specialist/subagent invocation is delegation. No first-party mechanism was established whose responsibility is regulating interference, oscillation or shared constraints among multiple autonomous S1 units.

## S3 — Inside-and-now control
`—`: permissions, hooks and parent/subagent lifecycle controls constrain execution but do not constitute whole-system current authority over multiple S1 resources, priorities and commitments.

## S3* — Complementary audit
`—`: hooks can observe or block operational events, but the hook callbacks and their authority are application-supplied. No autonomous, organizationally separate complementary audit channel is included by default.

## S4 — Outside-and-then intelligence
`—`: session state, hooks and specialist delegation concern current operation; no separate prospective environment-intelligence function that adapts future system capability was established.

## S5 — Policy and identity
`—`: instructions, permissions, hooks and agent definitions remain developer/user-owned rather than an autonomous ultimate policy/identity authority.

## Recursion, variety, escalation
The SDK supplies primitives from which richer organizations can be composed, while leaving S2–S5 closure to the application.