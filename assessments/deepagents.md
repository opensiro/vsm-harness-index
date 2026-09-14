---
harness_id: deepagents
project_name: Deep Agents
repository: https://github.com/langchain-ai/deepagents
review_ref: 9e7d62ff6e7131505995a706d717e01837aa8617
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Deep Agents

## Review boundary
Deep Agents at the pinned revision as the opinionated LangGraph-based harness; external LangSmith services are not endogenous functions.

## Repository architecture
The harness bundles planning, filesystem/shell, context management, memory, skills, HITL and isolated-context subagents. Subagents receive delegated tasks and custom compiled graphs can also be inserted as subagents.

## Primary evidence
- `README.md`: out-of-box harness; subagent delegation; context/filesystem/memory/skills; HITL and explicit stack boundary.

## Operational model
Principal and subagents are S1 units. The standard subagent mechanism delegates bounded work; LangGraph composition remains developer-provided orchestration.

## S1 — Operations
`A`: the harness autonomously plans/uses tools/manages context toward long-horizon outcomes. Confidence: high.

## S2 — Coordination
`—`: bundled subagents establish delegation, not a specific anti-oscillation/mutual-adjustment function.

## S3 — Inside-and-now control
`?`: principal-agent planning/context management does not prove whole-system resource/accountability authority.

## S3* — Complementary audit
`?`: LangSmith tracing/evaluation is external support and not independent audit inside the assessed harness.

## S4 — Outside-and-then intelligence
`?`: planning/memory are not S4.

## S5 — Policy and identity
`?`: HITL/system prompt remain parent-owned constraints.

## Recursion, variety, escalation
Subagents and CompiledStateGraph nesting are compositional, not automatically recursive viability.