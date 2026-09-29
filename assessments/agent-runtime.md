---
harness_id: agent-runtime
project_name: agent-runtime
repository: https://github.com/tsharp/agent-runtime
review_ref: 07ebca8ec36d15eae2d264d4998fa6857f9e0b51
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# agent-runtime

## Review boundary

- System in focus: the first-party Rust `tsharp/agent-runtime` library/runtime at frozen revision `07ebca8ec36d15eae2d264d4998fa6857f9e0b51`, including `Agent`/`Runtime`, provider clients, native/MCP tools, workflow-step machinery, retry/timeout behavior, context strategies, event stream and tool-loop prevention.
- Purpose and identity: a reusable Rust framework for executing tool-using LLM agents and caller-authored sequential/conditional/nested workflows.
- Relevant environment: callers/applications, external LLM providers, MCP servers and other resources reached through registered tools.
- Standard-distribution boundary: first-party `src/agent`, `src/runtime`, `src/workflow`, `src/context`, `src/event`, `src/llm`, `src/tools`, configuration and shared types are inside. External model cognition, external MCP servers and caller application logic remain environmental. The `crates/agent-discourse` multi-agent demo may corroborate composability but does not transfer its application-authored organizational decisions into the core runtime.
- Credited operating / distribution surfaces: the native `Agent` model/tool/result loop; caller-authored `Workflow` execution including agent, transform, conditional and sub-workflow steps; retry/timeout/context/event/tool-loop support.
- Adjacent first-party surfaces excluded from ownership: tests/benchmarks/CI, repository governance and the `agent-discourse` demo's scenario-specific role/topology decisions.
- First-party operating / deployment modes considered: direct `Agent` execution and `Runtime::execute` over workflows assembled from the shipped step types, with native or MCP-backed tools and supported provider clients.
- Recursion level: one agent loop is the operational S1. A workflow may sequence several `AgentStep`s, but the frozen core runtime provides deterministic caller-authored composition rather than an autonomous higher-recursion metasystem.
- Reviewed revision: `07ebca8ec36d15eae2d264d4998fa6857f9e0b51`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`src/agent/mod.rs` owns a complete first-party model/tool execution loop. It builds the chat request, calls the configured model client, receives model-selected tool calls, executes them through the first-party `ToolRegistry`, appends tool results to the conversation, and calls the model again until a terminal response or bounded stop. Repeated identical tool calls can be detected and replaced with a first-party feedback message, which the next model turn observes.

`src/runtime/executor.rs` is a workflow executor rather than a supervisory agent. It iterates through the caller-supplied workflow step list, constructs step input, invokes each step, records output/events, and feeds output deterministically to the next step. `ConditionalStep` evaluates a caller-supplied Rust `Fn(&Value) -> bool`; nested workflows similarly execute an already-authored sub-workflow. Retry, timeout and event machinery bound/observe execution but do not acquire discretion over organizational commitments.

`WorkflowContext` and its pruning strategies preserve and compress conversation state within a workflow. Context forking gives sub-workflows isolated copies and configurable merge behavior, but no first-party prospective learning/adaptation loop was found. The README labels `crates/agent-discourse` a multi-agent demo; its application-authored composition is not imported as core-runtime S2/S3/S3*/S4/S5 ownership.

Primary evidence:

- [`README.md`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/README.md) — supported runtime features, workflow composition and module boundaries; explicitly describes `agent-discourse` as a multi-agent demo.
- [`src/agent/mod.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/agent/mod.rs) — model/tool/result continuation loop, tool execution and repeated-tool-loop feedback.
- [`src/runtime/executor.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/runtime/executor.rs) — deterministic sequential workflow execution and event/history capture.
- [`src/workflow/steps/conditional.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/workflow/steps/conditional.rs) — caller-supplied deterministic conditional branch selection.
- [`src/context/mod.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/context/mod.rs) — workflow-local chat history, context forking and merge/pruning interfaces.

## Operational model

A caller configures an `Agent` with a system prompt, model client and optional tools. During execution, the model chooses substantive tool actions; the runtime executes them, returns observations and continues the model loop. A caller may instead assemble a `Workflow` with one or more agent/transform/conditional/sub-workflow steps. The workflow runtime follows that authored structure and emits lifecycle events; its branching, retries, timeouts and context policies are runtime mechanisms rather than autonomous metasystem decision owners.

## S1 — Operations

- State: A
- Function: perform open-ended task work through a model-driven decision/action/observation loop.
- Disturbance / variety regulated: user/task inputs, changing external/tool state, tool results/errors, provider outputs, repeated-action loops and bounded runtime/context conditions encountered during a trajectory.
- Decisive decision or feedback right: choose the next substantive response or registered tool call after observing the current conversation and prior tool results.
- Decision owner: the autonomous model-driven `Agent` actor.
- Supporting / enforcement mechanisms: `Agent::execute_with_events`, provider `LlmClient`, `ToolRegistry`, tool-loop detection/tracker, iteration bounds, event stream and error handling.
- Closure path: task input → model request → model-selected tool call → first-party tool execution → tool result appended to chat request → next model turn observes result/loop feedback and revises or continues → final response or bounded stop.
- Boundary reachability: this is the core shipped `Agent` path and does not require the `agent-discourse` demo or another orchestration package; only the configured external model/provider and tool environment remain dependencies.
- Why this is / is not agent-owned: deterministic Rust code validates, executes and bounds actions, but the model owns the substantive next-action choice. Without that actor the host machinery does not decide how to pursue the task.
- Evidence: [`src/agent/mod.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/agent/mod.rs); [`README.md`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external provider cognition is outside the repository boundary; credit rests on the first-party operational loop and action/observation closure around it.

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 disturbance-attenuation function is established at the reviewed core-runtime boundary.
- Disturbance / variety regulated: no packaged cross-agent conflict/oscillation is identified and attenuated by a first-party coordination relation.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: sequential workflow ordering, conditional steps, nested sub-workflows, shared/forked workflow context and application-defined multi-agent composition.
- Closure path: the runtime executes caller-authored steps and context rules, but no core path reconstructs distinct S1 units → concrete inter-S1 interference → first-party attenuation → feedback that changes later S1 behavior.
- Why this is / is not agent-owned: sequencing and conditional routing are authored/enforced structure rather than an autonomous coordination decision. Context fork/merge is a compositional primitive without an identified cross-S1 disturbance owner.
- Evidence: [`src/runtime/executor.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/runtime/executor.rs); [`src/workflow/steps/conditional.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/workflow/steps/conditional.rs); [`src/context/mod.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/context/mod.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `crates/agent-discourse` demonstrates that applications can compose several agents, but its scenario-specific organization is not core-runtime S2 ownership.

### Absence scope

- Surfaces inspected: workflow executor, sequential/conditional/sub-workflow steps, workflow context fork/merge, event stream, runtime configuration and `agent-discourse` demo boundary.
- Plausible first-party paths checked: multi-agent workflow sequencing as S2; context isolation as conflict attenuation; conditional routing as coordination; the demo's plurality as core-runtime coordination.
- Why no material first-party path remains: the core runtime exposes composition/enforcement primitives but does not itself identify a concrete inter-S1 disturbance and own the response that attenuates it.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous whole-system current-control function is established above operational agent/workflow execution.
- Disturbance / variety regulated: individual steps may fail, time out or retry, but the runtime has no autonomous portfolio view of several current S1 commitments/resources from which to reprioritize, reallocate or intervene.
- Decisive decision or feedback right: not established for S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: step lifecycle state/events, retry/timeout wrappers, workflow state/history, deterministic conditional routing and configured iteration/context limits.
- Closure path: failures and limits can deterministically stop/retry a step or workflow, but no whole-system current view → discretionary current-control judgment → changed allocation/commitment/intervention → returned operational state loop is packaged.
- Why this is / is not agent-owned: runtime limits, retries and events are monitoring/enforcement support. The workflow structure and conditions are supplied by callers rather than decided by a first-party supervisory agent.
- Evidence: [`src/runtime/executor.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/runtime/executor.rs); [`README.md`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: applications may build supervisors from the framework; generic composability does not transfer their current-control decisions into this standalone assessment.

### Absence scope

- Surfaces inspected: runtime executor, event model, retry/timeout behavior, workflow state/history, conditional branches, agent iteration limits and configuration.
- Plausible first-party paths checked: event observability as S3 view; retry/timeout as intervention; workflow conditional routing as prioritization; multiple AgentSteps as managed commitments.
- Why no material first-party path remains: current state is observable and bounded but no first-party actor owns a whole-system discretionary control loop over multiple operational commitments.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit path is established in the core runtime.
- Disturbance / variety regulated: an agent may produce an incorrect answer or tool-mediated result, but the standard runtime does not introduce a separate auditor with materially independent reality access and corrective return.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: event history, tool results, errors, retries, tests/benchmarks and caller-composable additional AgentSteps.
- Closure path: ordinary tool observations and errors return to the same producing S1; workflow history records execution. No producer claim → complementary evidence path → independent audit judgment → corrective feedback loop is supplied by the core runtime.
- Why this is / is not agent-owned: a caller can add another agent step or evaluator in an application, but that is a generic composition possibility, not a first-party complementary-audit constructor with fixed independence semantics.
- Evidence: [`src/agent/mod.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/agent/mod.rs); [`src/runtime/executor.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/runtime/executor.rs); [`README.md`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: repository tests and examples are development/demo evidence and are not runtime audit actors.

### Absence scope

- Surfaces inspected: agent tool feedback, workflow events/history, retry/error handling, tests/benchmarks and multi-agent demo/application composition.
- Plausible first-party paths checked: event log as audit; retry as corrective audit; second AgentStep as reviewer; development tests as S3*.
- Why no material first-party path remains: none provides a packaged independent evidence channel plus audit judgment and corrective return distinct from ordinary S1 reporting.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective adaptation loop is established.
- Disturbance / variety regulated: the runtime manages context pressure and same-workflow history but does not identify an external/future-relevant distinction, generate an adaptation option and return it into later organizational capability.
- Decisive decision or feedback right: not established for S4.
- Decision owner: not established.
- Supporting / enforcement mechanisms: sliding/token/summarization context strategies, workflow history, context fork/merge and caller-defined transforms.
- Closure path: context pruning/summarization changes working history for continuation of the current workflow; fork/merge controls propagation within nested execution. No future-oriented learned option is durably constructed and automatically reused to change later capability.
- Why this is / is not agent-owned: context management regulates current execution capacity rather than owning a prospective adaptation decision. Caller-authored transforms/config are pre-specified construction, not runtime learning.
- Evidence: [`src/context/mod.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/context/mod.rs); [`README.md`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: summarization can preserve information, but preservation within a workflow is not sufficient for S4 without prospective adaptation closure.

### Absence scope

- Surfaces inspected: workflow context/history, context managers, summarization/pruning, nested context fork/merge, configuration and caller-defined transform steps.
- Plausible first-party paths checked: summarization as learning; workflow metadata as durable adaptation; context merge as future capability change; configurable strategies as prospective planning.
- Why no material first-party path remains: all inspected paths maintain or reshape current workflow state; no autonomous future-facing adaptation option is constructed and fed into later organizational capability.

## S5 — Policy / identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established.
- Disturbance / variety regulated: system prompts, configuration, tool registration, workflow definitions and runtime bounds constrain execution but do not create a first-party identity-level governance decision loop.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `AgentConfig.system_prompt`, tool registry/configuration, YAML/TOML runtime config, caller-authored workflows and runtime limits.
- Closure path: caller-supplied policy/configuration enters execution as static constraints; no identity/ultimate-policy matter is deliberated by an authoritative S5 actor and returned as organization-wide governing policy.
- Why this is / is not agent-owned: following a system prompt or enforcing caller configuration is compliance/enforcement, not ownership of the ultimate-policy function.
- Evidence: [`src/agent/mod.rs`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/src/agent/mod.rs); [`README.md`](https://github.com/tsharp/agent-runtime/blob/07ebca8ec36d15eae2d264d4998fa6857f9e0b51/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: an embedding application can impose higher-level governance, but it remains outside this repository-relative core-runtime boundary.

### Absence scope

- Surfaces inspected: system prompts, agent/runtime configuration, tool registration, workflow construction, error/timeout/retry policy and multi-agent demo configuration.
- Plausible first-party paths checked: system prompt as identity; configuration as constitution; tool allowlist/registry as ultimate policy; workflow authoring as S5 authority.
- Why no material first-party path remains: each path supplies or enforces externally authored constraints and lacks an authoritative runtime identity/ultimate-policy decision closure.

## Recursion

The core runtime supports composition of multiple `AgentStep`s and nested workflows, but this does not by itself create a higher-recursion viable organization. At the credited recursion the `Agent` is S1. Higher-order coordination/control/audit/adaptation/policy functions may be authored by applications on top of the framework, including the repository's `agent-discourse` demo, but those application-specific decisions are not imported into the standalone runtime assessment.

## Variety and escalation

Operational variety is handled through model-selected tools, observation feedback, repeated-tool-loop interruption, retry/timeout behavior and bounded context management. Workflow-level variety is handled through caller-authored sequencing, condition functions, transforms and nested execution. Errors can stop or retry execution according to configured mechanics; they do not escalate to a first-party autonomous metasystem.

## Evidence gaps

- The `agent-discourse` crate was treated as a multi-agent demo/application surface, consistent with the frozen intake boundary; it can demonstrate composition but does not transfer application-authored organization into core-runtime S2-S5 ownership.
- Conditional and nested workflows are supported, but conditional decisions are caller-provided Rust functions and the executor follows the authored step graph deterministically.
- Event streams, retries, timeouts, loop prevention and context management are substantial control mechanisms but are not promoted to S3/S3*/S4 without the missing function-specific decision/feedback closure.
- External model-provider cognition and external MCP server behavior are not imported into first-party ownership claims.
