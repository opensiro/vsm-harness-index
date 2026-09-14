---
harness_id: autogen-agentchat
project_name: Microsoft AutoGen AgentChat
repository: https://github.com/microsoft/autogen
review_ref: 027ecf0a379bcc1d09956d46d12d44a3ad9cee14
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Microsoft AutoGen AgentChat

## Review boundary
AutoGen AgentChat at the pinned revision. Microsoft Agent Framework is its successor and is assessed separately.

## Repository architecture
AutoGen supplies autonomous tool-using agents plus AgentChat group-chat/team patterns over a message/event runtime. The framework includes participant selection, handoffs and group conversations in addition to simple parent-to-agent-tool delegation.

## Primary evidence
- `README.md`: autonomous multi-agent applications; AgentChat group chats; message/event runtime; multi-agent orchestration and AgentTool example.
- AgentChat documentation referenced by the repository supplies selector/group/swarm patterns as first-party standard behavior.

## Operational model
Individual assistants are S1 units. In group/team patterns, selection/handoff protocols determine which autonomous participant holds the next conversational/action right, preventing uncontrolled simultaneous action and providing feedback from the shared team interaction.

## S1 — Operations
`A`: stateful agents choose tools/actions and incorporate returned results. Confidence: high.

## S2 — Coordination
`A`: first-party selector/group-chat/swarm patterns can autonomously regulate turn/control transfer among S1 agents, a concrete coordination decision right rather than mere task decomposition. Confidence: medium-high.

## S3 — Inside-and-now control
`—`: team orchestration does not establish a whole-system resource/accountability regulator with S3 authority.

## S3* — Complementary audit
`?`: benchmarking/evaluator applications do not by themselves establish sufficiently independent runtime audit.

## S4 — Outside-and-then intelligence
`—`: planning/team conversation is not an external-and-prospective adaptation function.

## S5 — Policy and identity
`—`: instructions and termination/approval rules remain application/parent-owned.

## Recursion, variety, escalation
Teams and nested tools are compositional structures; recursive viability requires additional local metasystemic closure not established here.