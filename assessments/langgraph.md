---
harness_id: langgraph
project_name: LangGraph
repository: https://github.com/langchain-ai/langgraph
review_ref: e539ac122f4126f6dd850581c1494948cf620e31
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# LangGraph

## Review boundary
LangGraph at the pinned revision as a low-level stateful-agent orchestration runtime. Deep Agents, LangSmith and applications composed on top are separate systems.

## Repository architecture
LangGraph supplies durable execution, state/memory, graph transitions, interrupts and supporting infrastructure for long-running agent workflows. The pinned tree does not itself contain the higher-level `supervisor`, `swarm` or handoff packages/patterns that are often discussed in the surrounding LangChain ecosystem.

## Primary evidence
- `README.md`: low-level orchestration framework; durable execution; human-in-the-loop interrupts; memory; explicit boundary to higher-level agent products.
- `libs/langgraph/langgraph/types.py`: `interrupt()` pauses the current graph task, surfaces a value to the client and resumes when the caller supplies a `Command`; this is a runtime/HITL control primitive, not an autonomous audit function.
- Pinned implementation/test tree around Pregel/checkpoint execution: checkpoint/resume and state inspection remain properties of the same workflow execution path rather than a distinct reviewing subsystem.

## Operational model
Agent nodes can be S1 units. Graph edges, state, checkpoints and Commands route or persist execution, but generic workflow expressivity does not itself allocate any Beer-style metasystemic decision right.

## S1 — Operations
`A`: agent nodes can own model/tool action loops against durable state. Confidence: high.

## S2 — Coordination
`—`: the standard graph/runtime primitives do not specifically establish autonomous anti-oscillation or shared-resource regulation among two or more S1 units. A developer can author such a graph, but generic routing is not enough for `C`.

## S3 — Inside-and-now control
`—`: no first-party autonomous whole-system regulator with current resource, priority or commitment authority is supplied at this boundary.

## S3* — Complementary audit
`—`: interrupts, checkpoint inspection, tracing hooks and resume are execution/debug/HITL mechanisms on the operational path. No distinct first-party reviewer independently compares operational claims with evidence and feeds corrective findings back into the system.

## S4 — Outside-and-then intelligence
`—`: planning, persistence and arbitrary graph composition do not establish a prospective external-intelligence function coupled back to S3.

## S5 — Policy and identity
`—`: interrupts return authority to a parent/human and application configuration remains parent-owned; the runtime does not close mission, identity or ultimate policy.

## Recursion, variety, escalation
Subgraphs and nested agents are not automatically recursive viable systems. Durable state and interrupts attenuate execution variety without creating metasystemic autonomy.