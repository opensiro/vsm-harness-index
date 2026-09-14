---
harness_id: n8n
project_name: n8n
repository: https://github.com/n8n-io/n8n
review_ref: 4169b55bf3b3e6c255d7361642bc5243bd04345a
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# n8n

## Review boundary
n8n at the pinned revision, focusing on its first-party AI Agent node and agent-as-tool orchestration path inside a workflow. Generic workflow automation outside the agent loop is supporting infrastructure.

## Repository architecture
The `AI Agent` node is documented in source as generating an action plan, executing it, and using external tools. It accepts model, memory, tools, and output-parser subnodes. `AI Agent Tool` exposes an agent as a tool for an orchestrator pattern, allowing a parent operational agent to delegate bounded work.

## Primary evidence
- `packages/@n8n/nodes-langchain/nodes/agents/Agent/Agent.node.ts`: AI Agent description, external tools, model/memory/tool inputs, and orchestrator-pattern relation to Agent Tool.
- `packages/@n8n/nodes-langchain/nodes/agents/Agent/AgentTool.node.ts`: first-party AI Agent Tool with the same plan-and-execute agent behavior.
All evidence is read at the pinned `review_ref`.

## Operational model
An AI Agent node is an S1 unit: it plans and acts with tools inside a workflow. An Agent Tool can be invoked by a parent agent, but parent→child delegation is task decomposition unless an additional mechanism regulates interference among autonomous operational units.

## S1 — Operations
`A`: the AI Agent owns bounded plan/action/tool selection and executes against workflow inputs and returned tool results. Basis: explicit/structural. Confidence: high.

## S2 — Coordination
`—`: Agent Tool delegation and workflow routing assign or sequence work but do not establish anti-oscillation or conflict regulation among autonomous S1 units. Basis: structural. Confidence: medium.

## S3 — Inside-and-now control
`?`: workflow/runtime controls exist, but no verified autonomous whole-system regulator with authority over shared resources, commitments, or priorities is established.

## S3* — Complementary audit
`?`: validation, execution records, and workflow diagnostics are not enough to establish an independent complementary audit function.

## S4 — Outside-and-then intelligence
`?`: agent planning and workflow adaptation do not by themselves establish an external-and-prospective intelligence loop.

## S5 — Policy and identity
`?`: system messages, workflow configuration, permissions, and parent-agent instructions constrain operation without proving runtime identity or ultimate-policy closure.

## Recursion, variety, escalation
An agent exposed as a tool is nested delegation, not automatically a recursive viable system. Tools amplify local action variety while workflow configuration and subnode contracts attenuate it.
