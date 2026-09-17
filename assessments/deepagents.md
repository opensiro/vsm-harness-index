---
harness_id: deepagents
project_name: DeepAgents
repository: https://github.com/langchain-ai/deepagents
review_ref: f86b4e9abef7620b63a7258bc9fab0ccd83de8a4
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: f86b4e9abef7620b63a7258bc9fab0ccd83de8a4
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# DeepAgents

## Review boundary
DeepAgents at the pinned current `main` revision, including the reusable deep-agent runtime, synchronous and async subagent middleware, the model-facing async task-control tools, and the rubric grader as wired by the first-party `dcode` runtime. Optional middleware/configuration is not classified as Constructor merely because it must be enabled; ownership is determined after the function is established.

## Repository architecture
DeepAgents supplies autonomous tool-using agents plus synchronous and remote asynchronous subagents. `AsyncSubAgentMiddleware` exposes `start_async_task`, `check_async_task`, `update_async_task`, `cancel_async_task` and `list_async_tasks` directly to the main agent. The runtime persists the full set of tracked tasks and executes the agent's selected intervention against the remote subagent thread/run.

A separate `RubricMiddleware` intercepts a would-be terminal response and invokes a distinct grader agent. The grader can return `needs_revision`, causing structured feedback to be injected into the primary loop and work to resume. In the current first-party `dcode` server wiring, rubric graders receive explicitly selected read-only external-context tools, so the grader can independently inspect evidence rather than relying only on the primary agent's normal report/transcript.

## Primary evidence
- [`libs/deepagents/deepagents/middleware/async_subagents.py`](https://github.com/langchain-ai/deepagents/blob/f86b4e9abef7620b63a7258bc9fab0ccd83de8a4/libs/deepagents/deepagents/middleware/async_subagents.py): model-facing start/check/update/cancel/list controls over persisted concurrent async-subagent tasks; updates can interrupt a running subagent and continue the same thread.
- [`libs/deepagents/deepagents/middleware/rubric.py`](https://github.com/langchain-ai/deepagents/blob/f86b4e9abef7620b63a7258bc9fab0ccd83de8a4/libs/deepagents/deepagents/middleware/rubric.py): separate grader agent evaluates the terminal candidate, may use verification tools, emits structured criteria verdicts and loops `needs_revision` findings back into the primary agent.
- [`libs/code/deepagents_code/server_graph.py`](https://github.com/langchain-ai/deepagents/blob/f86b4e9abef7620b63a7258bc9fab0ccd83de8a4/libs/code/deepagents_code/server_graph.py): constructs the exact read-only context-tool set and passes it as `rubric_grader_tools`, giving the first-party grader complementary access to repository/external evidence.

## Operational model
The main agent performs S1 work and may create multiple background subagent commitments. It can inspect all tracked async tasks and autonomously update or cancel them. On configured rubric runs, a separate grader independently challenges completion and can force another primary iteration.

## S1 — Operations
`A`: the primary and delegated agents autonomously perform model/tool work. Confidence: high.

## S2 — Coordination
`—`: concurrent async tasks, isolation and lifecycle APIs establish multiple S1 units but no specific first-party inter-S1 interference/oscillation plus attenuation relation. Start/update/cancel/list are hierarchical current-control rights, not mutual-adjustment evidence by themselves. Confidence: high.

## S3 — Inside-and-now control
`A`: the main agent has a live view of its tracked background commitments and model-facing authority to start, inspect, redirect/interupt, cancel and list those commitments. The decisive intervention is chosen by the autonomous main agent; SDK/LangGraph machinery transports and enforces it. This closes a current whole-subagent-set regulation loop without a developer having to supply another control actor. Confidence: high.

## S3* — Complementary audit
`A`: a separate rubric grader challenges a candidate completion and can independently gather read-only evidence through the first-party `dcode` wiring. `needs_revision` findings are returned into the primary loop and cause further work. This is materially complementary access plus autonomous audit judgment and feedback closure, rather than ordinary inline QA. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: rubric iteration, memory, skills and task updates concern present execution/quality. No separate prospective environment-facing loop that changes future organizational capability/strategy was established. Confidence: high.

## S5 — Policy and identity
`—`: HITL/`interrupt_on`, rubrics and runtime options can gate operational actions or define acceptance criteria, but they do not establish identity/ultimate-policy closure. Generic human interruption is therefore not `S5=P`. Confidence: high.

## Recursion, variety, escalation
Subagents amplify operational variety and the main agent can regulate the current set through explicit lifecycle interventions. Rubric grading provides a distinct challenge/escalation path with complementary read-only evidence. Neither mechanism establishes S4/S5 at this boundary.

## Admission conclusion
Canonical vector at the pinned revision: `A — A A — —`. Relative to the proposal, generic coexistence is removed from S2, model-owned async-task regulation upgrades S3 from `C` to `A`, the now-evidenced first-party read-only grader upgrades S3* from `C` to `A`, and generic HITL is removed from S5.