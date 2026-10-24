---
harness_id: langflow
project_name: Langflow
repository: https://github.com/langflow-ai/langflow
review_ref: 595cd72a2b2021f2375fa31109af02d20bb17648
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 5621dcfd84e11108e4cc1ecb0c51f41053c4211c
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Langflow

## Review boundary
Langflow OSS at the pinned revision, focusing on deployed agent components, graph execution and first-party agent-to-agent composition. The previous stored SHA was not resolvable upstream; this deep review explicitly repins the assessment to the current reproducible `main` HEAD shown above.

## Repository architecture
Langflow supplies a visual/runtime graph for agents and tools. `AgentComponent` creates a tool-calling agent with model-call limits, retries, optional human tool approval and memory. `A2AAgentComponent` is a first-party Agent-to-Agent client that sends a message to another A2A agent and returns its reply.

## Primary evidence
- `src/lfx/src/lfx/components/models_and_agents/agent.py`: `AgentComponent` wraps `create_agent`, tool retry, model-call limits, memory and optional human approval around one agent loop.
- `src/lfx/src/lfx/components/models_and_agents/a2a_agent.py`: module docstring defines it as an A2A client that sends a message to a remote agent and returns its reply; runtime validates the card/endpoint, sends the message and returns the remote result.
- `src/lfx/tests/unit/components/models_and_agents/test_a2a_agent.py` and backend A2A tests exercise that first-party RPC/delegation path.

## Operational model
Each tool-calling agent can be an S1. A flow can invoke another agent through A2A or connect multiple components through an authored graph, but the standard relation evidenced here is request→remote-agent→reply or deterministic graph composition.

## S1 — Operations
`A`: the first-party Agent component owns model/tool decisions and iterates toward a task outcome. Confidence: high.

## S2 — Coordination
`—`: A2A is a callable remote-agent relation and visual graph edges are authored routing. Neither supplies a material first-party mechanism for mutual adjustment, collision regulation or anti-oscillation among autonomous peer S1s. Confidence: high.

## S3 — Inside-and-now control
`?`: runtime/graph execution and call limits constrain work, but this pass did not establish an agent-owned whole-system regulator with authority over shared commitments/resources.

## S3* — Complementary audit
`?`: human tool approval, retries and observability are support mechanisms, not sufficient evidence of an independent audit actor with corrective closure.

## S4 — Outside-and-then intelligence
`?`: connected tools/retrieval expose environment information but do not by themselves establish a distinct prospective adaptation function coupled to S3.

## S5 — Policy and identity
`?`: system prompts, approval configuration and flow topology remain builder/parent-authored.

## Recursion, variety, escalation
A2A and flow nesting expand operational variety but do not imply recursive viability.

## Deep-review result
`S2` resolves from `?` to `—`; the remaining unknowns stay unresolved pending stronger function-specific evidence.