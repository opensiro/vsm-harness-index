---
harness_id: langflow
project_name: Langflow
repository: https://github.com/langflow-ai/langflow
review_ref: 595cd72a2b2021f2375fa31109af02d20bb17648
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Langflow

## Review boundary
Langflow OSS at the pinned revision, focusing on deployed agent components and multi-agent flows. External observability services are not treated as endogenous VSM functions.

## Repository architecture
Langflow is a visual platform for building/deploying agents and workflows. It includes agent/tool components, conversation management, retrieval, a visual flow graph, APIs and MCP exposure, and explicitly advertises multi-agent orchestration.

## Primary evidence
- `README.md`: visual agent/workflow builder; agent/tool ecosystem; multi-agent orchestration with conversation management and retrieval; API/MCP deployment.

## Operational model
Agent components can be S1 units. The authored graph and conversation machinery constrain their interaction, but a graph edge or deterministic flow is not itself agentic S2.

## S1 — Operations
`A`: deployed agent components perform model-driven tool work inside flows. Confidence: high.

## S2 — Coordination
`?`: multi-agent orchestration is a first-party capability, but the reviewed primary evidence does not show enough about mutual adjustment/collision regulation to distinguish S2 from authored routing.

## S3 — Inside-and-now control
`?`: flow execution/control does not establish an autonomous whole-system regulator.

## S3* — Complementary audit
`?`: observability integrations and playground inspection do not establish sufficiently independent audit.

## S4 — Outside-and-then intelligence
`?`: retrieval and connected tools provide environment access but not a proven prospective adaptation loop.

## S5 — Policy and identity
`?`: builder configuration and system instructions are not runtime ultimate policy.

## Recursion, variety, escalation
Flows can compose agents and expose flows as tools, but composition/nesting is not automatically recursive viability.