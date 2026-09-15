---
harness_id: flowise
project_name: Flowise
repository: https://github.com/FlowiseAI/Flowise
review_ref: 9291856d1ea4a4ceea9f8fef8ce14f4f6c81e8eb
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Flowise

## Review boundary
Flowise at the pinned revision, focusing on first-party Agentflow execution and control primitives rather than the UI, deployment service, or human operator as an autonomous organization.

## Repository architecture
Agentflow supplies operational Agent nodes plus authored routing/control nodes such as Condition, ConditionAgent, ExecuteFlow, HumanInput, Iteration and LLM. The Agent node owns model/tool choices inside one operation; graph nodes determine how that operation is sequenced or routed.

## Primary evidence
- `packages/components/nodes/agentflow/Agent/Agent.ts`: `Agent_Agentflow` is an Agent Flow node whose stated behavior is to dynamically choose and use tools during runtime for multi-step reasoning; its implementation constructs model/tool execution inside the node.
- `packages/components/nodes/agentflow/ConditionAgent/ConditionAgent.ts`: a model classifies the current input into one of authored scenarios and returns a set of fulfilled conditions; those conditions select an outgoing graph path.
- `packages/components/nodes/agentflow/ConditionAgent/matchScenario.ts` and `matchScenario.test.ts`: first-party matching and tests cover scenario-to-output selection rather than mutual regulation among operational units.
- `packages/components/nodes/agentflow/HumanInput/HumanInput.ts`: first-party human-input node provides an explicit external pause/input boundary rather than agent-owned metasystem authority.
- `packages/components/nodes/agentflow/`: the pinned tree exposes Agent, Condition, ConditionAgent, ExecuteFlow, HumanInput, Iteration, LLM and other graph primitives; no separate first-party regulator, complementary audit channel, prospective adaptation loop, or ultimate-policy actor is present in the reviewed Agentflow boundary.

## Operational model
The model/tool Agent node is S1. ConditionAgent can make an agentic routing decision, but the VSM profile explicitly excludes a router or workflow edge from S2 unless it regulates interference among multiple S1 units. The surrounding Agentflow topology remains authored execution structure.

## S1 — Operations
`A`: an Agent node autonomously selects model/tool actions within its configured bounds and produces task outcomes. Confidence: high.

## S2 — Coordination
`—`: Condition/ConditionAgent and graph edges select execution paths; the inspected implementation and tests do not establish mutual adjustment, collision management, reservations, negotiated plans, or another stabilizing channel between multiple S1 units. Confidence: high.

## S3 — Inside-and-now control
`—`: ExecuteFlow/Iteration/runtime execution can drive or repeat work, but no reviewed first-party actor has the required whole-system view plus authority over shared resources, commitments, or constraints across S1s. Confidence: medium-high.

## S3* — Complementary audit
`—`: analytics, node outputs, routing conditions and human-input pauses are normal execution/observability paths. No sufficiently independent path obtains materially different access to operational reality and challenges routine S1–S3 reporting. Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`: agents may call web/data tools and retain conversation state, but the reviewed runtime has no external-and-prospective adaptation loop that develops future options and couples them back to present control. Confidence: high.

## S5 — Policy and identity
`—`: system prompts, scenarios, graph topology and human-input gates are authored constraints. They do not constitute runtime identity-level authority or closure of S3–S4 tension. Confidence: high.

## Recursion, variety, escalation
Nested flows and Agentflow composition increase execution variety but do not prove recursive viable-system closure. HumanInput is an escalation boundary to a parent human, not autonomous S5.