---
harness_id: semantic-kernel
project_name: Semantic Kernel
repository: https://github.com/microsoft/semantic-kernel
review_ref: ca40aa7226531d28a721d0ca0e451d0aaf86dafc
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Semantic Kernel

## Review boundary
Semantic Kernel at the pinned revision. Microsoft Agent Framework is identified as its successor but is a separate repository/system and is assessed independently later in the cohort.

## Repository architecture
Semantic Kernel is a model-agnostic SDK for agents and multi-agent systems, with plugins/tools, memory/planning capabilities, multi-agent workflows and a process framework. It can orchestrate collaborating specialist agents across Python/.NET/Java applications.

## Primary evidence
- `README.md`: agent framework, tools/plugins and planning; explicit multi-agent systems and structured process framework; successor boundary to Microsoft Agent Framework.

## Operational model
Tool-using ChatCompletionAgent-like actors are S1. Multi-agent/process primitives can structure collaboration, but the reviewed high-level evidence does not establish that coordination specifically damps interference among autonomous S1s.

## S1 — Operations
`A`: agents own bounded model/tool decisions and produce outcomes. Confidence: high.

## S2 — Coordination
`?`: collaborating-agent orchestration is first-party, but S2 cannot be inferred from the orchestration label without evidence of the required coordination relation.

## S3 — Inside-and-now control
`?`: process control/supervision is not enough to prove autonomous whole-system regulatory authority.

## S3* — Complementary audit
`?`: no sufficiently independent audit path verified.

## S4 — Outside-and-then intelligence
`?`: planning and plugin-based environment access do not prove outside-and-then adaptation.

## S5 — Policy and identity
`?`: agent instructions and application policy are parent-supplied rather than verified runtime policy closure.

## Recursion, variety, escalation
Multi-agent composition is present, but nested agents/processes are not automatically recursive viable systems.