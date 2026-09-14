---
harness_id: langchain
project_name: LangChain
repository: https://github.com/langchain-ai/langchain
review_ref: 348c9dc572599947d2d7d33d6a5b8b936e92a1d4
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# LangChain

## Review boundary
LangChain at the pinned revision. LangGraph, Deep Agents, LangSmith, and hosted deployment products are separate systems and are not silently imported into this assessment.

## Repository architecture
The core repository is a component framework for agents and LLM applications: models, tools/integrations, retrieval and agent abstractions. Its README explicitly points advanced agent orchestration to LangGraph and higher-level planning/subagent behavior to Deep Agents.

## Primary evidence
- `README.md`: LangChain as an agent/application framework; third-party tools/integrations; advanced orchestration delegated to LangGraph; Deep Agents listed as a separate higher-level package.

## Operational model
A LangChain tool-using agent is the S1 unit. Composition primitives and integrations support its work, but the reviewed repository boundary does not itself establish a distinct multi-S1 coordination layer.

## S1 — Operations
`A`: agent loops can choose tools/integrations and produce bounded application outcomes. Confidence: high.

## S2 — Coordination
`—`: advanced orchestration is explicitly directed to a separate LangGraph system; generic chaining/components do not establish S2.

## S3 — Inside-and-now control
`?`: no verified autonomous whole-system current regulator within this boundary.

## S3* — Complementary audit
`?`: evaluation/observability references point outside the assessed repository and do not establish independent audit here.

## S4 — Outside-and-then intelligence
`?`: flexible integrations and model swapping are developer capabilities, not agent-owned future/environment intelligence.

## S5 — Policy and identity
`?`: prompts/configuration do not prove legitimate runtime policy closure.

## Recursion, variety, escalation
The framework amplifies S1 variety through interchangeable tools/models. External orchestration packages must be assessed separately rather than treated as recursion inside LangChain.