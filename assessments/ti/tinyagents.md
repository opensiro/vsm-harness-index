---
harness_id: tinyagents
project_name: TinyAgents
repository: https://github.com/tinyhumansai/tinyagents
review_ref: 39e5835ddd2cf77830e68438135b251eb904438f
reviewed_at: 2026-10-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TinyAgents

## Review boundary

- System in focus: Published first-party **TinyAgents Rust agent harness** comprising the model/tool operating loop, admission and result feedback, with host-neutral session and subagent lifecycle composition. The analyzed recursion is one user-task-facing operating agent (which can delegate children), **not** a host's surrounding enterprise or an automatic viable federation of independent business agents.
- Purpose and identity: Provide typed model calls, tool execution, middleware, budget enforcement and terminal outcomes; optionally persist conversation/session and run child jobs durably, using host-chosen identity, credentials, prompts and policy.
- Relevant environment: Unknown tasks and model responses, changing tool results/errors, provider failures and cancellations, concurrent tool effects, detached child completion or restart, high context cost, model/tool formatting failures and host-defined approval boundaries.
- First-party distribution: Rust `crates/tinyagents-harness` (core and adapter), `tinyagents-runtime` (Session), `tinyagents-orchestration` (subagents/teams/workflows), `tinyagents-tasks` (durable task lifecycle and parent completion delivery), `tinyagents-graph` (checkpoint/interrupt/replay) and `tinyagents-definition` (host-owned agent definitions). The actual `tinyinference` model implementation is an **external dependency**, not imported as a separate organizational metasystem.
- Credited operating / distribution surfaces: [README.md#L5](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/README.md#L5), [README.md#L160](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/README.md#L160), [crates/tinyagents-harness/src/runtime/agent.rs#L657](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/runtime/agent.rs#L657), [crates/tinyagents-harness/src/agent_loop/run_loop.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/run_loop.rs#L1), [crates/tinyagents-harness/src/agent_loop/run_loop.rs#L910](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/run_loop.rs#L910), [crates/tinyagents-harness/src/agent_loop/tools.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/tools.rs#L1), [crates/tinyagents-harness/src/agent_loop/model_call.rs#L182](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/model_call.rs#L182), [crates/tinyagents-orchestration/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-orchestration/src/lib.rs#L1), [crates/tinyagents-runtime/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-runtime/src/lib.rs#L1).
- Adjacent first-party surfaces excluded from ownership: Downstream host task/organizational policy, authorization and credentials; external `tinyinference-llm` providers and remote LLM services, Claude Code CLI implementation/permissions, tool servers and workspace operators; repository maintenance/release/test harness and example graph business tasks. Their independent organizational rights cannot be credited to TinyAgents.
- Operating modes considered: Public `AgentHarness::invoke_agent` and `invoke_default`, regular and streaming model/tool operation with typed tools/middleware, optional Claude Code CLI adapter, registered-model switching, live provider tool admission, host-neutral durable Session driver/record, nested tool invocation, `SubAgentTool` inline/background and durable parent completion routing, graph checkpointing, teams/workflows, and host-supplied `AgentDefinition` and policy.
- Recursion: Model-selected task-facing work is the only evidenced first-party **S1 operating unit**. Direct children may perform scoped subtasks and return results; durable job stores are transport/restart mechanisms, not autonomous organizational managers. Separate host deployments might form a viable multi-S1 system but this code alone does not prove that.
- Frozen source: `tinyhumansai/tinyagents@39e5835ddd2cf77830e68438135b251eb904438f`, GitHub repository ID **1283610217**, public GPL-3.0, source Git tree `673d9cc5bfa9036702c172bcd239afc17d9ce43d`, batch [#1756](https://github.com/opensiro/vsm-harness-index/issues/1756). Reviewed 2026-10-19; generation contract Profile 0.2.4 / Skills Methodology 0.3.7.

## Repository architecture

The public `AgentHarness` routes registered provider models and typed tool definitions through a concrete model–tool feedback loop. `AgentHarness::invoke_agent` enters its runtime, `run_loop` calls `invoke_model_resolving` / model dispatch and inspects the actual `response.tool_calls()`, then admits and executes authorized named tools with before/after middleware. Execution results and tool errors are returned to the working transcript before the next model call; a terminal provider response, run limit or cancellation closes the cycle. Parallel tool execution is bounded and results are folded in call order; the general `AgentHarness` inner loop is first-party, not an unimplemented provider trait. [crates/tinyagents-harness/src/runtime/agent.rs#L657](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/runtime/agent.rs#L657); [crates/tinyagents-harness/src/agent_loop/run_loop.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/run_loop.rs#L1); [crates/tinyagents-harness/src/agent_loop/run_loop.rs#L934](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/run_loop.rs#L934); [crates/tinyagents-harness/src/agent_loop/run_loop.rs#L1159](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/run_loop.rs#L1159); [crates/tinyagents-harness/src/agent_loop/model_call.rs#L598](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/model_call.rs#L598); [crates/tinyagents-harness/src/agent_loop/tools.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/tools.rs#L1).

`tinyagents-runtime::Session` retains conversation and tool outcomes, but the host supplies actual model/tool execution via a driver, prompt, authorization and durable codec. `tinyagents-orchestration` supports child invocation, background jobs, parent messaging, pause/resume and persistence, while `tinyagents-tasks` can reconcile detached tasks after a restart and redeliver a child completion. `tinyagents-graph` offers typed state DAGs, checkpoints, interrupts, replay and time travel. These are real first-party infrastructure routes but, without a substantive inter-S1 conflict owner, current portfolio decision owner, independent S3 correction mandate or prospective strategy author, do not prove S2/S3/S3*/S4/S5. [crates/tinyagents-runtime/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-runtime/src/lib.rs#L1); [crates/tinyagents-orchestration/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-orchestration/src/lib.rs#L1); [crates/tinyagents-orchestration/src/subagent/mod.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-orchestration/src/subagent/mod.rs#L1); [crates/tinyagents-tasks/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-tasks/src/lib.rs#L1); [crates/tinyagents-graph/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-graph/src/lib.rs#L1).

`tinyagents-definition` explicitly declares that organizational identity, prompt construction and authorization are owned by the **host**; registered agent tiers and tool grants do not confer ultimate mission-setting authority on this harness. Host-controlled middleware, model policies, budgets and replay help an external owner regulate execution, but are not independent VSM metasystem decisions in the assessed first-party recursion. [crates/tinyagents-definition/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-definition/src/lib.rs#L1); [crates/tinyagents-harness/src/agent_loop/tools.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/tools.rs#L1); [crates/tinyagents-harness/src/cost/model_budget.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/cost/model_budget.rs#L1).

## Operational model

A user-authorized task reaches the model with available tools and context. The model may select one or several typed tools; admission/middleware applies host-provided constraints, first-party dispatch invokes them, and observations flow to the same model until completion. Child tasks and replay preserve operating continuity. An independent, model-owned future organization redesign or constitutional escalation has not been shown in the published supported operating modes.

## S1 — Operations

- State: A
- Function: Use model-selected actions and tool-result feedback to execute a goal-facing agent task under defined limits.
- Disturbance / variety regulated: Novel task requirements, dynamic tool results, failing provider/tool calls, unparseable tool arguments, large conversation context, unexpected child task output and limits.
- Decisive decision or feedback right: A configured model via the first-party runtime selects tool names/arguments or a final response after receiving actual tool-result and error observations. Tool admission can deny unsafe effects, but it does not select the model's next substantive task action.
- Decision owner: Model behind the registered `tinyinference` provider reached via first-party `AgentHarness::invoke_agent` / `run_loop`; host grants tools and policy, model owns immediate task selection.
- Supporting / enforcement mechanisms: Typed tool registry/validation, admission and folding, lifecycle/tool-wrap middleware, tool concurrency and run limits, streamed provider tokens, reusable session transcript, failure and cancellation reporting.
- Closure path: Goal → current context and available tools → provider/model completion with tool calls → admission and first-party tool execution → result/error ToolMessages in transcript → model next step → completed/paused/failed terminal outcome.
- Boundary reachability: The public harness example and `invoke_agent` path invoke concrete `run_loop`, which calls model via `model_call.rs`, inspects `response.tool_calls()` and calls `execute_tools_with_promotions`, then feeds tool results into the same `messages` vector before looping. No downstream application needs to implement this inner loop.
- Why this is / is not agent-owned: Without the provider model, the harness could admit tools and record transcripts but cannot choose task-specific tools and responses from new observations. The supported first-party integration exercises the model decision right despite external provider ownership.
- Evidence: [README.md#L165](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/README.md#L165), [crates/tinyagents-harness/src/runtime/agent.rs#L657](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/runtime/agent.rs#L657), [crates/tinyagents-harness/src/agent_loop/run_loop.rs#L900](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/run_loop.rs#L900), [crates/tinyagents-harness/src/agent_loop/run_loop.rs#L934](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/run_loop.rs#L934), [crates/tinyagents-harness/src/agent_loop/run_loop.rs#L1159](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/run_loop.rs#L1159), [crates/tinyagents-harness/src/agent_loop/model_call.rs#L598](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/model_call.rs#L598).
- Basis: Supported source-connected model/tool feedback loop, not an empirically measured provider result.
- Confidence: High for structural S1 composition, medium for runnable deployment in this environment.
- Caveats: No live model inference was performed, and external `tinyinference` provider stability or model output quality is unverified.

## S2 — Coordination

- State: —
- Function: No separately owned regulator was evidenced that senses **mutual interference between independently viable S1 departments** and returns revised mutual operating commitments to those departments.
- Disturbance / variety regulated: Concurrent tool calls and background subagents may compete for resources or change a shared workspace. Task queues can lose progress or deliver late results unless reconciled. These are current task/delegation and transport disturbances, not a demonstrated independent operating-division coordination relationship.
- Decisive decision or feedback right: The calling task agent can spawn/steer/cancel children under host policy; the queue and task stores route completion. Deterministic admission and concurrent-safe middleware suppress individual tool races, not organizational interference between viable S1 lines.
- Decision owner: Parent task model and host policy for delegation, mechanical queue/registry and scheduler for transport and safety.
- Supporting / enforcement mechanisms: Child session/tool registry, `spawn/await/cancel/steer`, detached task store, restart reconciliation, durable completion routing, graph fanout and reducer channels, bounded tool concurrency.
- Closure path: Parent task delegates → child executes/finishes → durable completion reaches parent → parent continues; no observable independent-S1 interference → specialized S2 regulator → changed ongoing obligations of both separate operating units.
- Why this is / is not agent-owned: Parent task steering is an S1 operational right; message transport/locking between subtasks is not a separate independently owned S2 system.
- Evidence: [README.md#L35](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/README.md#L35), [README.md#L182](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/README.md#L182), [crates/tinyagents-orchestration/src/subagent/mod.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-orchestration/src/subagent/mod.rs#L1), [crates/tinyagents-tasks/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-tasks/src/lib.rs#L1), [crates/tinyagents-harness/src/agent_loop/tools.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/tools.rs#L1).
- Basis: Bounded negative after checking direct/background child, durable task/router, graph and concurrent tool modes.
- Confidence: Medium-high at the bounded one-goal operating recursion.
- Caveats: A host could deploy independent ongoing departments using these components and implement its own inter-S1 regulator; such a host is outside this first-party assessment.

### Absence scope

- Surfaces inspected: Subagent orchestration, teams/workflows, durable task and completion router, graph fanout, concurrent tool executor and shared context.
- Plausible first-party paths checked: Shared workspace conflicts, duplicate child completions, tool contention, multiple independent worker agents and possible priority/routing conflict.
- Why no material first-party path remains: No first-party independent inter-division conflict-damping decision and reciprocal adjustment of at least two viable operating S1 departments is evidenced; these surfaces are generalized task/delegation and delivery infrastructure.



## S3 — Inside-and-now control

- State: —
- Function: No independent whole-current executive manager owns discretionary resource/priorities/obligations across a portfolio of independently viable S1 divisions and returns binding adjustments.
- Disturbance / variety regulated: Run-cost overages, stuck tool loops, provider timeouts, abandoned child jobs, restart discontinuity and cancellation may require recovery or admission decisions for individual tasks.
- Decisive decision or feedback right: Hosts choose budgets, prompt, tool grants, subagent definitions and authorization. Middleware and run limits enforce those settings, while the task model chooses actions. No separate model/agent manager decides whole-current cross-S1 commitments.
- Decision owner: Host for present constraints and scope, deterministic first-party limits and drivers for per-run admission and task recovery.
- Supporting / enforcement mechanisms: `RunLimits`, model budgets, `TurnPolicy`, middleware, typed task statuses, SessionDriver, durable run ledger and orchestration lifecycle driver.
- Closure path: Task action/child recovery → configured policy and limit check → same operation continues, pauses or fails; no S3 executive state/negotiation → portfolio reprioritization/resource decision → returned separate S1 adjustment.
- Why this is / is not agent-owned: A host-neutral session driver and task-store status are useful operations machinery, not autonomous management mandates for an independently viable department portfolio.
- Evidence: [crates/tinyagents-runtime/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-runtime/src/lib.rs#L1), [crates/tinyagents-harness/src/agent_loop/run_loop.rs#L190](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/run_loop.rs#L190), [crates/tinyagents-harness/src/cost/model_budget.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/cost/model_budget.rs#L1), [crates/tinyagents-orchestration/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-orchestration/src/lib.rs#L1).
- Basis: Source-bounded negative including policy/quotas and orchestration modes.
- Confidence: Medium-high.
- Caveats: Human/host organization may constitute S3 externally, but the first-party harness does not define its authority.

### Absence scope

- Surfaces inspected: Runtime Session/Driver, budget/limits, subagent durable lifecycle, agent definitions and host-scoped admission rules.
- Plausible first-party paths checked: Current cross-agent allocation, stalled jobs, retry or cancellation, model changes and permissions for resource management.
- Why no material first-party path remains: The shipped controls govern one task or enforce host decisions; no first-party discretionary whole-current portfolio manager has a distinct mandate and binding return to separately viable S1 operations.



## S3* — Complementary audit

- State: —
- Function: No independently mandated reality audit can inspect normal S1/S3 operational claims and return corrections to an S3 current-management owner in the assessed first-party mode.
- Disturbance / variety regulated: Misreported tool executions, missing transcripts, replay gaps, malformed outputs and cost-accounting errors can threaten confidence in individual runs.
- Decisive decision or feedback right: The harness records provider/tool lifecycle events, tool receipts and transcripts; testkit and deterministic validators can reject invalid tool requests, and graph replay exposes state. None has an independent corrective audit mandate into a distinct S3.
- Decision owner: Host-configured tracing/validation and deterministic run/instrumentation code, not a separate S3* auditor.
- Supporting / enforcement mechanisms: Append-only session transcript, typed tool execution receipts, trace and usage records, graph replay/checkpoint, tool schema validators, host callback hooks and integration tests.
- Closure path: Tool result/trace → current task/transcript/host observability; no independent reality-sampling → challenged managerial picture → source-backed S3 correction → changed whole-current control.
- Why this is / is not agent-owned: Stored evidence makes independent review possible but does not implement a first-party authorized auditor with a feedback right over an S3 manager.
- Evidence: [crates/tinyagents-session/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-session/src/lib.rs#L1), [crates/tinyagents-graph/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-graph/src/lib.rs#L1), [crates/tinyagents-harness/src/agent_loop/tools.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/tools.rs#L1), [crates/tinyagents-runtime/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-runtime/src/lib.rs#L1).
- Basis: Negative after examining monitoring/history, model/tool errors and replay.
- Confidence: Medium-high.
- Caveats: External compliance systems may consume these receipts, but their owners are not part of this shipped harness.

### Absence scope

- Surfaces inspected: Transcript storage and spend provenance, graph checkpoint/replay, model/tool lifecycle events, typed validation and integration-test evidence.
- Plausible first-party paths checked: False tool-operation claims, missing/reordered result records, checks against independent execution reality and return to a manager.
- Why no material first-party path remains: No first-party independent operational-reality audit ownership and corrective decision return to a separate S3 current-control authority is present; the paths are telemetry, correctness checks and host-accessible records.



## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped model-owned external prospective sensing, future capability redesign option **and** accepted changed operating configuration returned to later independent task runs was established.
- Disturbance / variety regulated: Changing model outputs, high token costs, expanding transcript and session continuation are operating context disturbances, not necessarily future environment and strategy questions.
- Decisive decision or feedback right: Hosts select models, tools, policies, definition sets and session continuity; model can decide a current task's next tool, but there is no first-party model mechanism authorized to formulate/adopt a future skill/strategy/tool change for the operating cell as an enduring artifact.
- Decision owner: Host developer/application for future harness capabilities; first-party model's discretion stays in the current S1 task path.
- Supporting / enforcement mechanisms: Durable transcript, model-switching, tool-surface refresh, agent-definition vocabulary, graph interrupt/replay and caching/memory middleware.
- Closure path: Prior session/transcript or replay → rehydration and present context/middleware → current task continues with host-configured tool/model behavior; no evidence→prospective model option→selection/admission→durable changed future operating capability loop.
- Why this is / is not agent-owned: Recording prior reasoning and replaying a DAG do not grant prospective strategic option or adoption rights. Dynamic tool registration is host-supplied and not a model-authored improvement admitted for future tasks.
- Evidence: [README.md#L35](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/README.md#L35), [crates/tinyagents-harness/src/agent_loop/model_switch.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-harness/src/agent_loop/model_switch.rs#L1), [crates/tinyagents-runtime/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-runtime/src/lib.rs#L1), [crates/tinyagents-definition/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-definition/src/lib.rs#L1), [crates/tinyagents-graph/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-graph/src/lib.rs#L1).
- Basis: Bounded negative after inspecting future-looking memory/replay and tool/model adaptation possibilities.
- Confidence: Medium-high at the first-party reviewed boundary.
- Caveats: A downstream host could implement a reflective skill optimizer using the programmable model/tool loop, but it is not a credited shipped first-party S4 integration.

### Absence scope

- Surfaces inspected: Model-switch/registry, persistent sessions, graph replay and time travel, optional memory middleware, host-owned agent definitions and tool-surface refresh.
- Plausible first-party paths checked: Reusable new skills, model-guided prospective strategy formation, versioned future operating instructions or policy and next independent run adoption.
- Why no material first-party path remains: Shipped APIs persist or replay existing state, or defer configuration/approval to a host; no model-authored prospective option and first-party admitted durable capability-return path has been established.



## S5 — Policy and identity

- State: —
- Function: No first-party legitimate decision-making authority for fundamental organizational identity/purpose questions and enduring constitutional policy return is demonstrated.
- Disturbance / variety regulated: Unsafe actions, unauthorized tool use, cost budget violations and child-agent delegation scopes require binding permission limits, but these are delegated operating constraints rather than ultimate purpose disputes.
- Decisive decision or feedback right: Host explicitly owns agent definitions, prompt/identity, tool authorization, credentials and product policy. Rust harness enforces chosen bounds; model chooses within them.
- Decision owner: External application host, not a first-party constitutional agent/board with final mission decision rights.
- Supporting / enforcement mechanisms: `tinyagents-definition` host-owned identity, `ToolAdmission`, `RunLimits`, middleware, `SubAgentPolicy` and host auth callbacks.
- Closure path: Proposed tool/child action → configured policy admission/deny/stop → current run changes state; no contested ultimate-purpose issue → authorized S5 judgment → binding identity-level policy returned to future S1 operations.
- Why this is / is not agent-owned: An agent tier declaration, tool permission or durable transcript cannot legitimately determine organization-wide constitutional priorities by itself.
- Evidence: [crates/tinyagents-definition/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-definition/src/lib.rs#L1), [crates/tinyagents-runtime/src/lib.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-runtime/src/lib.rs#L1), [crates/tinyagents-orchestration/src/subagent/mod.rs#L1](https://github.com/tinyhumansai/tinyagents/blob/39e5835ddd2cf77830e68438135b251eb904438f/crates/tinyagents-orchestration/src/subagent/mod.rs#L1).
- Basis: First-party boundary source-explicitly defers ultimate host authority.
- Confidence: High for the ownership boundary.
- Caveats: In a larger integrated product, legitimate human or agent-owned S5 may exist, but must be assessed at that different organizational recursion.

### Absence scope

- Surfaces inspected: AgentDefinition host vocabulary, tool admission, SubAgentPolicy, session/graph policy hooks and configurable model/provider permissions.
- Plausible first-party paths checked: Host or end-user legitimacy, task stop/grant exceptions, permanent mission identity decisions and future binding governance.
- Why no material first-party path remains: The repository explicitly keeps identity, authorization, prompt and policy with external hosts, and provides no internally legitimate first-party S5 intake/decision/constitutional return.



## Recursion

One registered model-backed agent harness is the operating S1; subagent jobs are delegated tasks. Durable graphs and teams increase programmability and reliability, but an independent viable multi-S1 enterprise authority cannot be credited from library composition alone. Host-managed policy, identity and durable dialect conversion are explicitly excluded.

## Variety and escalation

Model tool selection and returned results regulate immediate operating variety. Typed admission and running limits attenuate dangerous actions, while task/job durable delivery prevents some lost work after restart. Observability and graph replay give potential evidence for external governance; a cancelled child, timeout, trace record or failed replay is not automatically an algedonic signal to a distinct first-party S3/S4/S5 owner.

## Evidence gaps

- Source-only frozen Rust assessment; `cargo` is absent from the isolated Linux review runner, so full upstream Rust tests, live model calls, cross-crate provider drivers and empirical agent performance have **not** been independently executed here. This is not a claim of upstream failure.
- The package embeds a model/tool loop and optional provider/Claude Code adapters, but underlying `tinyinference` implementation and user product's agent organization are external; this analysis does not borrow their S2–S5 rights.
- The host-neutral orchestration/graph/session packages implement persistent execution, **not** independently demonstrated model-owned future strategic improvement, organizational portfolio management or constitutional authority. A host can add such functions only with new evidence.
- Proposed assessment does not participate in canonical catalog/signature/rankings until a separate reviewed and CI-backed admission.
