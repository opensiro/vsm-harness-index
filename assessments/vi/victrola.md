---
harness_id: victrola
project_name: Victrola
repository: https://github.com/haileyok/victrola
review_ref: 2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: ?
---

# Victrola

## Review boundary

- System in focus: Victrola's first-party single-operator agent runtime with web/Discord/Signal entrypoints, scheduled agent jobs, code execution, memory and tool approval.
- Purpose and identity: complete personal operator tasks through model-generated TypeScript and Python-backed tools.
- Relevant environment: operator chat, scheduled prompts, tool/web observations, transient model failures, concurrent jobs, external services and operator capability approvals.
- Standard-distribution boundary: main.py wiring, src/agent, scheduler, tool/executor/store/memory and supported local web/channel interfaces; configured external model, Deno, MCP and Engram services are dependencies.
- Credited operating / distribution surfaces: Agent.chat/_chat_impl, Deno execute_code feedback, _wire_scheduler and the explicit starvation-attenuating Scheduler path.
- Adjacent first-party surfaces excluded from ownership: unit/integration tests, test_images.py, frontend test fixtures and CI/Docker publication; external MCP servers, Engram Garden service and model-provider governance.
- First-party operating / deployment modes considered: local/web chat and optional Discord/Signal, multiple scheduled tasks with fresh per-run conversations, code/custom tools with operator approval, mutable memory/self note and prompt reload.
- Recursion level: one installed runtime and its persistent scheduled operational task cells/conversations; operator is external deployment parent.
- Reviewed revision: `2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AgentClient adapters implement Anthropic or OpenAI-compatible model calls with bounded retry. Agent.chat preserves caller-owned conversation state, refreshes the system prompt, retrieves RAG memories and runs _chat_impl. The model selects execute_code TypeScript; ToolExecutor runs it under a Deno permission/time/output boundary, mediates Python tool calls and returns results to subsequent model turns. Structured assistant/tool messages are persisted; compaction checkpoints and context repair support continued operation. The summarizer model is a routine tool/context helper, not a separate auditor.

The scheduler persists named recurring prompts and optional approved condition scripts. main._wire_scheduler invokes Agent.chat with a fresh conversation for each fire and stores the transcript under a per-schedule session. Scheduler._tick explicitly fires distinct due jobs concurrently so one slow callback cannot starve the others; _fire enforces per-job timeout/retry and advances each job's next-run basis. This is a concrete coordination path distinct from generic asynchronous messaging.

Custom tools start unapproved, can be tested, and are enabled/revoked by the operator through the web interface. Code/parameter/permission changes reset approval. The prompt advertises a build/test/propose/approve utility workflow, but it supplies no separate externally prospective adaptation mandate. Memory has self/operator/skill/episodic/factual entries. The self entry is explicitly described as identity/personality/behavior and can be edited by the agent via memory.update or operator via web CRUD. main._load_system_prompt reads it, and the agent refreshes it on later turns. The source proves edit and reload reachability; it does not clearly distinguish self-description/effectiveness edits from ultimate-policy authority.

## Operational model

The primary S1 unit is an agent conversation solving an operator task with actual tool observations. Named recurring tasks are durable operational cells: each has its own prompt, recurrence, run state and fresh agent conversation/outcome. Their scheduler relationship prevents one slow cell blocking another. The scheduling policy is developer-selected deterministic control, not autonomous coordination discretion. Tool/condition approval authorizes specific capabilities or scheduled actions; it is not automatically whole-system S3, future-oriented S4 or S5.

## S1 — Operations

- State: A
- Function: perform operator and recurring tasks through a model/code/tool feedback loop.
- Disturbance / variety regulated: external information, code/tool errors, unfinished tasks and changing conversation context.
- Decisive decision or feedback right: generate TypeScript/tool choices, interpret returned observations and decide next action or final answer.
- Decision owner: model-backed agent within first-party Agent.chat.
- Supporting / enforcement mechanisms: provider adapters, Deno sandbox, Python registry, retries, iteration cap, conversation persistence/compaction and optional operator-approved capabilities.
- Closure path: _chat_impl executes model tool_use blocks, appends tool_result messages to the conversation and calls the model again; final response returns to the caller or scheduled job.
- Boundary reachability: main wires Agent to its ToolExecutor and chat/channel/scheduler interfaces; execute_code is the first-party exposed primitive, not an outside coding-agent loop.
- Why this is / is not agent-owned: runtime permission enforcement cannot choose task-dependent code or interpret observations without the model-backed actor.
- Evidence: [src/agent/agent.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/agent/agent.py); [src/tools/executor.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/tools/executor.py); [src/agent/prompt.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/agent/prompt.py); [main.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/main.py); [src/tools/registry.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/tools/registry.py).
- Basis: structural.
- Confidence: high.
- Caveats: Static source evidence only; no live model, Deno/browser, external account or provider E2E execution.

## S2 — Coordination

- State: C
- Function: attenuate starvation between recurring operational task cells sharing one scheduler.
- Disturbance / variety regulated: a slow due task callback would hold up another simultaneously due task if processed serially.
- Decisive decision or feedback right: determine which due cells can progress independently and when each may next fire; the shipped fixed policy uses concurrent firing with per-job timeout/retry.
- Decision owner: developer-selected scheduling policy; no autonomous agent owns coordination discretion.
- Supporting / enforcement mechanisms: asyncio.gather over due _fire calls, per-job wait_for timeout, retry state and persisted last_run.
- Distinct S1 units: distinct named recurring prompts wired by main to fresh Agent.chat conversations and per-schedule transcript sessions, each producing its own operational outcome.
- Inter-S1 disturbance: slow scheduled callback starves another due operational cell; Scheduler._tick documents this exact interference and a dedicated regression witness exercises it.
- Attenuating coordination relation: dispatch all due cells concurrently rather than await one before the others; bound each fire and handle failures independently.
- Feedback into subsequent S1 behaviour: _fire updates each task's last_run/retry state after its own result, determining that cell's subsequent due/retry execution without waiting on a slow peer.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the implementation and test tie concurrency directly to a concrete cross-cell starvation mode; this is not S2 credit merely for a scheduler name or tool batching.
- Closure path: task-local result/timeout updates scheduler state; the next tick schedules each operational cell from that returned state.
- Boundary reachability: main._wire_scheduler installs the real agent callback into the packaged Scheduler; the anti-starvation path is part of normal scheduler execution, not test-only machinery.
- Why this is / is not agent-owned: C records the exposed S2-specific decision/feedback primitive; an autonomous actor/authority for selecting or revising coordination policy still requires developer composition.
- Evidence: [src/scheduler/scheduler.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/scheduler/scheduler.py); [main.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/main.py); [tests/test_pr12_scheduler_retry.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/tests/test_pr12_scheduler_retry.py); [README.md](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: No autonomous S2 policy negotiation or task-quality/throughput claim. Per-session chat serialization and SQL locks alone are not used to justify C.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current resource/commitment regulator is established.
- Disturbance / variety regulated: per-run iteration limits, individual schedules, tool permissions and pending approval counts.
- Decisive decision or feedback right: caller/developer selects run limits; operator approves individual tools/conditions or edits schedules; no shared current-commitment arbitration is shipped.
- Decision owner: operator/developer for configuration and particular authorization; task model for local work.
- Supporting / enforcement mechanisms: iteration cap, Deno limits, status counters, schedule enable/run-now controls and approval/revocation gates.
- Closure path: approved capabilities become callable and schedule edits affect that task, without a first-party whole-system current-control decision path.
- Why this is / is not agent-owned: an operator dashboard and hard enforcement do not by themselves establish S3.
- Evidence: [src/agent/agent.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/agent/agent.py); [src/web/routers/status.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/web/routers/status.py); [src/web/routers/schedules.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/web/routers/schedules.py); [src/web/routers/tools.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/web/routers/tools.py); [src/tools/custom.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/tools/custom.py); [src/scheduler/scheduler.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/scheduler/scheduler.py).
- Basis: structural.
- Confidence: high.
- Caveats: The scheduler S2 witness is specific starvation control, not evidence of whole-system priority/resource bargaining.

### Absence scope

- Surfaces inspected: Full agent loop/limits, scheduler lifecycle, aggregate status endpoint, custom-tool approval manager and web control routes.
- Plausible first-party paths checked: Approval counts, schedule enable/disable/run-now, custom/MCP permissions and failure/time limits.
- Why no material first-party path remains: The status surface counts configured capabilities/tasks; per-item controls and fixed enforcement supply no whole-system current view plus discretionary regulation of shared commitments/resources and returned supervisory control, including a qualifying parent alternative.

## S3* — Complementary audit

- State: —
- Function: no independent complementary operational audit is supplied.
- Disturbance / variety regulated: routine tool results, compaction quality and custom-code validity.
- Decisive decision or feedback right: no first-party independent audit judgment challenging ordinary claims and returning corrective control.
- Decision owner: task model and operator routine code reviewer; no separate audit owner is installed.
- Supporting / enforcement mechanisms: full transcripts, tool events, sub-agent summarizer, code test endpoint and unit tests.
- Closure path: summaries/results feed the production context and code approval enables a capability; no audit-specific findings-to-control channel is wired.
- Why this is / is not agent-owned: a separate summarization model or human tool review is not automatically independent audit.
- Evidence: [src/tools/definitions/summarize.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/tools/definitions/summarize.py); [src/agent/agent.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/agent/agent.py); [src/web/routers/tools.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/web/routers/tools.py); [src/agent/conversation.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/agent/conversation.py).
- Basis: structural.
- Confidence: high.
- Caveats: Stored transcripts are potentially useful audit inputs but do not establish audit ownership.

### Absence scope

- Surfaces inspected: Routine summary/compaction, execution events and transcript persistence, custom-code test/approval and test-directory boundary.
- Plausible first-party paths checked: Alternative model summary, raw scheduled/chat transcripts, operator code testing and approval.
- Why no material first-party path remains: These paths summarize production content or authorize tools; no complementary independent challenge/judgment with returned control is shipped. Generic custom tools/MCPs cannot supply missing audit decision content by expressiveness alone.

## S4 — Outside-and-then intelligence

- State: —
- Function: no function-specific externally prospective adaptation process is supplied.
- Disturbance / variety regulated: current task tool gaps, reusable procedures, operator facts and recurring condition checks.
- Decisive decision or feedback right: agent may build a utility and operator approves its execution, but no shipped future/environment option-selection process governs that workflow.
- Decision owner: agent for task code/proposals; operator for capability permission.
- Supporting / enforcement mechanisms: workspace build/test workflow, pending custom-tool store, approval reset, memory/RAG and scheduler triggers.
- Closure path: approved code appears in later prompts and can run, while memory changes current context; no first-party external/future analysis-to-adaptation-option conversation is established.
- Why this is / is not agent-owned: capability creation, operational sensing, retention and generic approval are insufficient by themselves for S4.
- Evidence: [src/agent/prompt.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/agent/prompt.py); [src/tools/definitions/custom_tools.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/tools/definitions/custom_tools.py); [src/tools/custom.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/tools/custom.py); [src/web/routers/tools.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/web/routers/tools.py); [src/scheduler/scheduler.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/scheduler/scheduler.py); [main.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/main.py).
- Basis: structural.
- Confidence: high.
- Caveats: The complete tool build/test/approval return was inspected; the missing element is the function-specific external-and-prospective adaptation relation, not code installation.

### Absence scope

- Surfaces inspected: Self-improvement prompt workflow, tool creation/update/approval, trigger evaluation, memory/skills and prompt refresh.
- Plausible first-party paths checked: External web/notification sensing, new tools for tasks, skill retention, condition-driven future runs and operator adoption.
- Why no material first-party path remains: The shipped playbook is generic utility engineering and authorization; no specific external/future distinctions generate adaptation options under an established S4 decision/feedback mandate. Recurring event reaction and future tool availability alone do not close S4.

## S5 — Policy and identity

- State: ?
- Function: a plausible runtime identity-maintenance path exists, but S5 ultimate-policy function/ownership is unresolved.
- Disturbance / variety regulated: changes to the editable self note describing identity/personality/task focus and lessons about effectiveness.
- Decisive decision or feedback right: memory.update can replace self-note content and web CRUD can do likewise; the source does not settle which edits constitute legitimate ultimate-policy adjudication versus ordinary descriptive/effectiveness memory.
- Decision owner: agent can edit autonomously; operator can also edit. The intended decisive ultimate authority for identity/policy conflicts is not reconstructed sufficiently.
- Supporting / enforcement mechanisms: typed single self-entry memory, SQLite persistence, prompt templates and automatic per-turn reload.
- Closure path: main._load_system_prompt reads the self entry; _chat_impl refreshes it before the next operator turn. Data-to-instruction return is real; ultimate-policy judgment/authority is the unresolved element.
- Why this is / is not agent-owned: proactive self-note editing shows agent write discretion, but a writable identity-labeled prompt is not by itself enough to establish autonomous ultimate-policy ownership.
- Evidence: [src/agent/prompt.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/agent/prompt.py); [src/tools/definitions/memory.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/tools/definitions/memory.py); [src/memory/store.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/memory/store.py); [src/web/routers/memory.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/web/routers/memory.py); [src/agent/agent.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/src/agent/agent.py); [main.py](https://github.com/haileyok/victrola/blob/2bc6262cc7d12a61b6d8de68f3a16ceaec3ba5d7/main.py).
- Basis: unknown.
- Confidence: medium.
- Caveats: This is a concrete shipped-path uncertainty, not a hypothetical extension or an automatic negative. No P/A/C state is inferred from generic tool approval or the Self Note label.

## Distributed OSS parent arrangement

The operator controls one installed runtime. Repository contributor/maintainer authority is adjacent. No distributed project-recursion parent governance is inferred.

## Self-hosted and non-human modes

Local operator web/chat controls, code approval and editable memory are supported and were inspected. Tool/trigger approvals do not by themselves establish S3/S4/S5 parent modes. The self-note path's actual policy-authority interpretation remains unresolved; no intentionally non-human organization is claimed.

## Recursion

Recurring task cells have local outcomes and context but no established complete local metasystem. The summarizer is a bounded helper, not proof of recursive viability.

## Variety and escalation

Code-mode batches, permission limits, retries, context repair, RAG and per-schedule failure handling manage execution variety. Scheduler anti-starvation is the specific S2 constructor witness. Crash/empty-result notifications and dashboard counters are not themselves an algedonic channel or a higher function.

## Evidence gaps

Source-only review; no provider, external account, browser/Deno or application E2E runs. The S2 finding is structural and supported by a repository-native mocked regression, not measured performance. S5 remains ? because the shipped self-note edit/reload loop is concrete, but its legitimate ultimate-policy decision right and conflict resolution relative to the operator are not established. A documented governance/identity use case or implementation-level authority path could resolve it; neither generic self-writing nor missing documentation alone justifies replacing ? with A or —.
