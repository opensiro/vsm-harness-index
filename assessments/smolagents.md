---
harness_id: smolagents
project_name: smolagents
repository: https://github.com/huggingface/smolagents
review_ref: 30bb1161095dbae2271e6bc3cc4c219cc3897a57
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# smolagents

## Review boundary
smolagents at the pinned revision as a minimal agent library with CodeAgent and tool integrations.

## Repository architecture
`CodeAgent` writes actions as code and executes them through configurable sandboxes/tools. Hub/MCP/LangChain/Space integrations expand the available operational tool set.

## Primary evidence
- `README.md`: runnable agents; first-class CodeAgent; sandbox execution; tool/model/modality integrations; `agent.run()` example.

## Operational model
A CodeAgent is S1. Tool sharing/integrations are capabilities, not peer operational units.

## S1 — Operations
`A`: agents autonomously choose/code actions and use tools toward a task. Confidence: high.

## S2 — Coordination
`—`: no material multi-S1 coordination function established at this boundary.

## S3 — Inside-and-now control
`?`: sandbox/runtime controls are not autonomous whole-system regulation.

## S3* — Complementary audit
`?`: no independent audit function verified.

## S4 — Outside-and-then intelligence
`?`: multimodal/tool access does not establish prospective adaptation.

## S5 — Policy and identity
`?`: instructions/security configuration remain parent-owned.

## Recursion, variety, escalation
Tool/model integrations amplify one S1; no recursion is established.