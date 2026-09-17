---
harness_id: gemini-cli
project_name: Gemini CLI
repository: https://github.com/google-gemini/gemini-cli
review_ref: 6a466a7e2fe2b1255752c1e74f69b31f0216084d
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 6a466a7e2fe2b1255752c1e74f69b31f0216084d
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Gemini CLI

## Review boundary
Gemini CLI at the pinned current `main` revision, including the primary coding-agent loop, local agent executor, per-agent tool scheduler, agent registry and tool-confirmation path. The review distinguishes execution topology and tool scheduling from organizational coordination/current-control functions.

## Repository architecture
Gemini CLI provides an autonomous terminal/coding agent and first-party local agents. `LocalAgentExecutor` creates a separate tool/prompt/resource registry for each local agent and explicitly prevents an agent tool from being registered inside another local agent, so local-agent execution is bounded parent-to-child delegation rather than an recursively coordinating peer organization. Each agent's model-selected tool calls are handed to an event-driven `Scheduler`; that scheduler executes and confirms a batch of tool calls for that agent rather than regulating multiple S1 units on behalf of a whole organization.

## Primary evidence
- [`packages/core/src/agents/local-executor.ts`](https://github.com/google-gemini/gemini-cli/blob/6a466a7e2fe2b1255752c1e74f69b31f0216084d/packages/core/src/agents/local-executor.ts): constructs the autonomous local-agent loop, isolated registries and the explicit rule that agents cannot call other agents.
- [`packages/core/src/agents/agent-scheduler.ts`](https://github.com/google-gemini/gemini-cli/blob/6a466a7e2fe2b1255752c1e74f69b31f0216084d/packages/core/src/agents/agent-scheduler.ts): schedules a batch of tool calls for one agent and surfaces tool confirmation state.

## Operational model
The primary agent and any invoked local agent independently perform model/tool work. The runtime supplies bounded execution, registries, scheduling and confirmation around those S1 trajectories.

## S1 — Operations
`A`: the coding agent autonomously selects tools/actions and iterates from tool/environment feedback inside configured bounds. Confidence: high.

## S2 — Coordination
`—`: the reviewed first-party boundary supplies parent-to-child local-agent invocation and per-agent tool scheduling, but no specific inter-S1 interference/oscillation plus attenuation relation. The previous proposal promoted orchestration/scheduling vocabulary without the required S2 witness. Confidence: high.

## S3 — Inside-and-now control
`—`: `Scheduler` regulates execution of one agent's requested tool calls. It does not establish a whole-system view plus authority over resources, commitments, priorities or interventions across multiple S1 units. Tool confirmation is likewise local execution gating rather than S3 closure. Confidence: high.

## S3* — Complementary audit
`—`: no separate complementary audit actor/path with materially different access to operational reality and feedback into control was established. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: no separate prospective environment-facing adaptation loop was established. Confidence: high.

## S5 — Policy and identity
`—`: tool confirmation/approval concerns individual operational actions. It does not establish an identity/ultimate-policy matter, legitimate ultimate authority, and return-to-operation loop. The previous proposed `P` therefore does not satisfy the current S5 parent-mode threshold. Confidence: high.

## Recursion, variety, escalation
Local agents increase operational variety through bounded specialization. Separate registries and scheduler/confirmation machinery constrain execution, but the reviewed standard distribution does not close a metasystem function above S1.

## Admission conclusion
Canonical vector at the pinned revision: `A — — — — —`. The prior `A C C — — P` proposal conflated execution topology/tool gating with S2, S3 and S5 functions.