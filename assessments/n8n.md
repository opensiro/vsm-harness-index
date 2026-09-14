---
harness_id: n8n
project_name: n8n
repository: https://github.com/n8n-io/n8n
review_ref: 4169b55bf3b3e6c255d7361642bc5243bd04345a
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# n8n

## Review boundary
n8n at the pinned revision, focusing on the first-party AI Agent node, Agent Tool, fallback-model and Guardrails surfaces. Generic deterministic workflow automation is supporting infrastructure unless an autonomous actor owns the organizational decision right.

## Repository architecture
The AI Agent generates an action plan, executes it and uses connected tools/model/memory/output-parser subnodes. AI Agent Tool exposes the same plan-and-execute behavior as a callable tool for an orchestrator pattern. One agent can also have a primary and fallback model. The separate Guardrails node validates/sanitizes text against builder-configured policies and thresholds.

## Primary evidence
- `packages/@n8n/nodes-langchain/nodes/agents/Agent/Agent.node.ts`: plan-and-execute agent, external tools and explicit Agent Tool relation for an orchestrator pattern.
- `packages/@n8n/nodes-langchain/nodes/agents/Agent/Agent.node.ts`: fallback-model example explicitly remains one agent; the second model is a retry provider, not another agent.
- `packages/@n8n/nodes-langchain/nodes/agents/Agent/AgentTool.node.ts`: callable child agent retains the same plan-and-execute behavior.
- `packages/@n8n/nodes-langchain/nodes/Guardrails/description.ts`: policy checks/sanitization for jailbreak, NSFW, PII, secrets, topical alignment and URLs are configured by the workflow builder.

## Operational model
An AI Agent node is one S1. Agent Tool permits parent→child task delegation. Workflow edges, guardrails and fallback providers constrain or route operation but do not become autonomous metasystem actors.

## S1 — Operations
`A`: the AI Agent owns bounded planning/action/tool selection and incorporates returned results. Confidence: high.

## S2 — Coordination
`—`: Agent Tool and orchestrator patterns assign/delegate bounded work; deterministic workflow routing and model fallback do not regulate interference among peer autonomous S1s. Confidence: high.

## S3 — Inside-and-now control
`—`: workflow execution controls and guardrails do not provide an autonomous actor with a whole-system current view and authority over shared resources, commitments and priorities. Confidence: high.

## S3* — Complementary audit
`—`: Guardrails validate configured text policies on the normal workflow path; execution records/tests are diagnostics. No separate independent audit actor with complementary reality access and corrective closure is supplied. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: planning, model selection/fallback and ordinary workflow reactions do not establish a distinct external-and-prospective intelligence function coupled to S3. Confidence: high.

## S5 — Policy and identity
`—`: system prompts, workflow topology, guardrail rules/thresholds and permissions are parent-authored configuration, not agent-owned ultimate policy. Confidence: high.

## Recursion, variety, escalation
An agent exposed as a tool is nested operational delegation, not recursive viability. Guardrails attenuate input/output variety and fallback models improve S1 reliability without creating metasystem closure.