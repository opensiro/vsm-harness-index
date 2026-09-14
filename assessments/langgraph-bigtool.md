---
harness_id: langgraph-bigtool
project_name: LangGraph BigTool
repository: https://github.com/langchain-ai/langgraph-bigtool
review_ref: 0bb7f9227d349afa4d4207c6630e800658c80894
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# LangGraph BigTool

## Review boundary
langgraph-bigtool at the pinned revision as a LangGraph agent pattern for dynamically retrieving from large tool registries.

## Repository architecture
The library indexes tool metadata in a LangGraph store and gives an agent a retrieval tool that selects a small relevant subset before action. Streaming/memory/HITL are inherited support from LangGraph.

## Primary evidence
- `README.md`: scalable dynamic tool retrieval; `create_agent`; agent retrieves relevant tools then calls them; persistence integration.

## Operational model
The compiled bigtool agent is one S1. The tool registry/retrieval mechanism attenuates tool-choice variety inside it.

## S1 — Operations
`A`: the agent autonomously retrieves/selects and executes task-relevant tools. Confidence: high.

## S2 — Coordination
`—`: no multi-S1 coordination relation is supplied.

## S3 — Inside-and-now control
`?`: tool-registry control is not whole-system regulation.

## S3* — Complementary audit
`?`: no independent audit path verified.

## S4 — Outside-and-then intelligence
`?`: semantic tool retrieval is current-task capability selection, not S4.

## S5 — Policy and identity
`?`: registry/configuration is parent-owned.

## Recursion, variety, escalation
BigTool is a variety attenuation mechanism for one S1, not a metasystem or recursion.