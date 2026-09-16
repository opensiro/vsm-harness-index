---
harness_id: claw-code-agent
project_name: Claw Code Agent
repository: https://github.com/HarnessLab/claw-code-agent
review_ref: 167571da895b2a1a9e36ecfae2876984cef65e0d
reviewed_at: 2026-09-16
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Claw Code Agent

## Review boundary
The system-in-focus is the first-party Python coding-agent runtime plus bundled delegation, task, team, policy, workflow and interaction runtimes. Child `LocalCodingAgent` instances count as operational S1 units; external providers and the human operator are outside the autonomous boundary.

## Repository architecture
`LocalCodingAgent` owns the model/tool loop and can instantiate bounded child agents. Delegation supports dependency graphs, topological batches, failure limits, child permissions and resumable sessions. Runtime task state blocks unresolved dependencies and releases dependents after completion. Hook policy supplies deterministic tool/budget enforcement; ask-user can synchronously obtain a parent decision.

## Primary evidence
- [`src/agent_runtime.py`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_runtime.py#L2160-L2535): constructs child agents, narrows permissions, checks dependencies and enforces failure limits.
- [`src/agent_runtime.py`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_runtime.py#L2705-L2770): dependency-aware topological batching admits only ready subtasks.
- [`src/agent_tools.py`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_tools.py#L960-L1015): dependency-sensitive task transitions release dependents after completion.
- [`src/hook_policy.py`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/hook_policy.py#L20-L116): constructor-authored policy/budget/tool-denial surface.
- [`src/ask_user_runtime.py`](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/ask_user_runtime.py#L90-L205): queued or synchronous human answers return into execution.

## Operational model
A model-driven parent chooses coding actions and may create child S1s. The constructor determines delegation strategy, dependencies, budgets and permissions; runtime enforces them. Topological batching/task state regulate when operations proceed, while human decisions can re-enter through ask-user.

## S1 — Operations
`A`: first-party `LocalCodingAgent` instances independently perform coding/tool work. Proof: [child-agent execution](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_runtime.py#L2160-L2535). Confidence: high.

## S2 — Coordination
`C`: constructor-declared dependencies become enforced topological batches; unresolved children do not run and task completion releases dependents. Proof: [topological batching](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_runtime.py#L2705-L2770), [task dependencies](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_tools.py#L960-L1015). Confidence: high.

## S3 — Inside-and-now control
`C`: child permissions, failure limits and executable policy/budget gates regulate current operational continuation under constructor-owned rules. Proof: [delegation control](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_runtime.py#L2160-L2535), [policy surface](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/hook_policy.py#L20-L116). Confidence: high.

## S3* — Complementary audit
`—`: inspected verification/regression/history paths do not establish a structurally independent audit channel with corrective/escalation closure. Proof: [ordinary child construction](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_runtime.py#L2160-L2245). Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`: plans, compaction, resume and persistence concern current/continued execution, not a distinct prospective environment-facing adaptation loop. Proof: [execution-state management](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/agent_runtime.py#L1650-L1805). Confidence: high.

## S5 — Policy and identity
`P`: `ask_user_question` can synchronously obtain a human response and return it into execution, preserving parent authority for escalated decisions. Proof: [parent interaction runtime](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/src/ask_user_runtime.py#L90-L205). Confidence: medium-high.

## Recursion, variety, escalation
Children are bounded operational units and cannot recursively spawn indefinitely. Dependencies, permissions and failure limits attenuate variety; ask-user returns unresolved legitimate decisions to the parent.

## Deep-review conclusion
Signature at the pinned revision: `A C C — — P`. This same-ref reassessment strengthens S3 from `—` to `C` and S5 from `—` to `P` based on executable runtime paths while preserving S2 as constructor-owned.