---
harness_id: langgraph
project_name: LangGraph
repository: https://github.com/langchain-ai/langgraph
review_ref: e539ac122f4126f6dd850581c1494948cf620e31
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# LangGraph

## Review boundary
LangGraph at the pinned revision as a low-level stateful-agent orchestration runtime. Deep Agents, LangSmith, and applications composed on top are separate systems.

## Repository architecture
LangGraph supplies durable execution, state/memory, graph transitions, interrupts and supporting infrastructure for long-running agent workflows. It deliberately presents itself as low-level infrastructure; higher-level planning and subagent behavior is delegated to Deep Agents.

## Primary evidence
- `README.md`: low-level orchestration framework; durable execution; human-in-the-loop interrupts; memory; explicit boundary to Deep Agents/LangSmith.

## Operational model
Agent nodes can be S1 units. Graph edges, state and Commands route execution but are generic workflow mechanisms, not by themselves Beer-style S2.

## S1 — Operations
`A`: agent nodes can own model/tool action loops against durable state. Confidence: high.

## S2 — Coordination
`—`: the standard graph/runtime primitives do not specifically establish an autonomous anti-oscillation decision right among S1 units; developers can compose such a relation, but generic graph expressivity is insufficient for `C`.

## S3 — Inside-and-now control
`—`: no first-party autonomous whole-system regulator with resource/commitment authority is supplied at this boundary.

## S3* — Complementary audit
`?`: tracing/debugging and state inspection are not independent audit by themselves; applications may compose evaluators externally.

## S4 — Outside-and-then intelligence
`—`: planning and persistent state do not establish an external/prospective adaptation function.

## S5 — Policy and identity
`—`: interrupts return control to a parent/human, but a generic interrupt is not specifically runtime identity or ultimate-policy closure.

## Recursion, variety, escalation
Subgraphs and nested agents are not automatically recursive viable systems. Durable state and interrupts attenuate execution variety without creating metasystemic autonomy.