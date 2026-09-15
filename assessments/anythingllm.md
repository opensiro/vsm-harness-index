---
harness_id: anythingllm
project_name: AnythingLLM
repository: https://github.com/Mintplex-Labs/anything-llm
review_ref: 3a85d3e75490f09453de7e8c440b9463f4a82019
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AnythingLLM

## Review boundary
AnythingLLM at the pinned revision, focusing on built-in workspace agents and the first-party no-code Agent Flow runtime. Multi-user permissioning and application administration are support infrastructure, not agent-owned organizational functions.

## Repository architecture
Workspace agents use retrieval and tools toward user tasks. Agent Flows are stored builder-authored step lists loaded and executed through `FlowExecutor`; the reviewed vocabulary includes start-variable initialization, API calls, LLM instructions and web scraping. Flows can be exposed back to an agent as callable tools.

## Primary evidence
- `server/utils/agentFlows/index.js`: loads stored flow definitions, exposes them as agent-callable plugins and invokes `FlowExecutor` with caller variables.
- `server/utils/agentFlows/executor.js`: executes authored flow steps and propagates variables/results through the flow runtime.
- `server/utils/agentFlows/flowTypes.js`: defines concrete `start`, `apiCall`, `llmInstruction` and `webScraping` steps rather than an autonomous multi-S1 coordination protocol.
- `server/__tests__/utils/agentFlows/index.test.js`: verifies flow definitions are loaded as tools, variables are filtered/merged and configured steps execute, confirming builder-defined semantics.

## Operational model
Workspace agents are S1. Agent Flows amplify an S1 with reusable deterministic/LLM-backed procedures, but authored step execution does not itself create several autonomous operational units or a metasystem.

## S1 — Operations
`A`: workspace agents autonomously choose available skills/tools toward user tasks. Confidence: high.

## S2 — Coordination
`—`: Agent Flow sequences authored blocks/procedures; it does not evidence a coordination problem among multiple S1 units or regulation of their interference. Confidence: high.

## S3 — Inside-and-now control
`—`: flow execution, workspace administration and permissions do not supply an agent-owned whole-system view with authority over shared current commitments/resources. Confidence: high.

## S3* — Complementary audit
`—`: no distinct sufficiently independent path inspects operational reality outside the normal flow and challenges routine claims. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: web access, schedules and memory extend operational reach, but the reviewed runtime does not establish an external-and-prospective adaptation loop coupled to current control. Confidence: high.

## S5 — Policy and identity
`—`: flow definitions, workspace configuration, permissions and agent setup are user/platform authored rather than an agent-owned ultimate policy function. Confidence: high.

## Recursion, variety, escalation
Flows can enter an agent's tool repertoire, but technical composition is not recursive viability. Variable schemas and step definitions attenuate execution variety at the application boundary.

## Deep-review result
`S2`, `S3`, `S3*`, `S4` and `S5` resolve from `?` to `—`; `S1 A` is confirmed with implementation and tests.