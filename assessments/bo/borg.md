---
harness_id: borg
project_name: Borg
repository: https://github.com/joydle/borg
review_ref: be9d9cf613a16ef13772c3fc4ddcfae27321579d
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Borg

## Review boundary

- System in focus: Borg's published Rust library crates and documented examples at the frozen repository commit.
- Purpose and identity: Give an embedding Rust application supervised, budgeted and resumable building blocks for model-driven pipelines and actor sessions.
- Relevant environment: Rust/Tokio host, host-provided AgentLlmClient, concrete agent/task definitions, tool policy and optional stores.
- Standard-distribution boundary: The git dependency exports a real executor and agent-loop construction API. Adopters supply a live AgentLlmClient, meaningful agents and the application assembly. Shipped examples use predetermined fake responses.
- Credited operating / distribution surfaces: [`Cargo.toml`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/Cargo.toml), [`README.md`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/README.md), [`crates/borg/src/lib.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/lib.rs), [`crates/borg/src/agent.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/agent.rs), [`crates/borg/src/executor.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/executor.rs), [`crates/borg-loop/src/runtime.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg-loop/src/runtime.rs), [`crates/borg-loop/src/streaming_runtime.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg-loop/src/streaming_runtime.rs)
- Adjacent first-party surfaces excluded from ownership: Examples and testing feature, documentation examples, website, host application and external inference client. Test verdicts demonstrate executor behavior under scripted input.
- First-party operating / deployment modes considered: Embedded composition executor, resumable executions and actor/session library, plus documented deterministic examples.
- Recursion level: One adopter-composed pipeline or actor session is the potential operating unit. The assessment boundary is the supplied library distribution before adopter assembly.
- Reviewed revision: `be9d9cf613a16ef13772c3fc4ddcfae27321579d`, [intake #3059](https://github.com/opensiro/vsm-harness-index/issues/3059) and [controller #3060](https://github.com/opensiro/vsm-harness-index/issues/3060).
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The library implements the agent invocation protocol, verdict extraction and an iterative executor that feeds tool results into later calls. The executor can compose stages, budget concurrent child invocations, checkpoint and route failures. The adopter supplies the live client and task decisions through concrete BorgAgent or actor implementations.
README documents a trait implementation requirement for live inference. The stock end-to-end tool-loop example constructs FakeLlmClient. The default BorgAgent user_prompt returns no task, so the executor and a generic agent trait do not themselves form an operational agent.

## Operational model

Disposition: excluded-no-agentic-vsm. Borg supplies a substantive constructor for a model-tool operation, but at the reviewed first-party distribution the autonomous operational loop depends on adopter-supplied actor and provider implementation. Scripted examples prove the mechanics rather than a live semantic owner.

## S1 — Operations

- State: —
- Function: No complete first-party autonomous operation in the shipped distribution. The executor intentionally supports constructing a task actor.
- Disturbance / variety regulated: Tool errors, task results and token consumption are collected by the runtime.
- Decisive decision or feedback right: Choose meaningful tools and revisions in response to real operational inputs.
- Decision owner: The embedding application must provide a concrete task actor and a live provider client.
- Supporting / enforcement mechanisms: Agent loop, HandoffState, token budget, tool registry and actor snapshots.
- Closure path: With host wiring, verdict → tool → accumulated result → next invocation. Shipped demonstration feeds predetermined verdicts through the same path.
- Boundary reachability: The agent and actor constructors are exported. An out-of-box live client and substantive runnable actor are absent.
- Why this is / is not agent-owned: Removing the adopter implementation leaves generic machinery and fake responses.
- Evidence: [`README.md`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/README.md), [`crates/borg/src/agent.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/agent.rs), [`crates/borg/src/llm.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/llm.rs), [`crates/borg/src/executor.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/executor.rs#L2024-L2086), [`crates/borg/examples/tool_loop.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/examples/tool_loop.rs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Live client trait, default invoke, agent executor and documented tool-loop and actor examples.
- Plausible first-party paths checked: Tool selection through Agent composition and the built-in fake provider.
- Why no material first-party path remains: The library packages the execution path. A real operational actor is still supplied externally in a deployed embedding.

## S2 — Coordination

- State: —
- Function: No first-party inter-S1 coordination mode at this library boundary.
- Disturbance / variety regulated: Possible branch concurrency and contention for finite tokens or provider permits.
- Decisive decision or feedback right: Choose and return a response to interference between independently operating S1s.
- Decision owner: Adopter specifies the composition and budgets. Executor applies scheduling/degradation rules.
- Supporting / enforcement mechanisms: Parallel composition, branch handoff, budget admission and supervised permits.
- Closure path: Configured limits affect branch start and failure transport; adopter would need to establish the actual S1 relationship and response.
- Boundary reachability: Parallel execution is supplied as a composition primitive.
- Why this is / is not agent-owned: The concrete relationships between operating units are specified by the embedding application.
- Evidence: [`crates/borg/src/composition.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/composition.rs), [`crates/borg/src/executor.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/executor.rs#L1284-L1340), [`crates/borg/src/supervisor.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/supervisor.rs), [`crates/borg/src/handoff.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/handoff.rs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Parallel executor, guardrails, handoff and group concurrency.
- Plausible first-party paths checked: Budget-driven degradation and concurrent branch execution.
- Why no material first-party path remains: These mechanisms enforce pipeline and capacity rules on adopter work. No shipped distinct S1 operations with a coordination decision path are bound.

## S3 — Inside-and-now control

- State: —
- Function: No separate current-control owner is established for a whole operating system.
- Disturbance / variety regulated: Child failures, restarts, budget and excess repetitions inside a run.
- Decisive decision or feedback right: Discretionary intervention over current commitments across operations.
- Decision owner: Embedder specifies limits and restart policy, then the executor enforces them.
- Supporting / enforcement mechanisms: Supervisor, circuit breaker, cancellation, guardrails and actor recovery.
- Closure path: Failures trigger bounded retries, cancellation, throttling or stop under configured rules.
- Boundary reachability: The executor uses supervision in parallel branches and optional guardrails in tool loops.
- Why this is / is not agent-owned: Process supervision is implemented. A whole-system discretionary control and return are outside the supplied mode.
- Evidence: [`crates/borg/src/supervisor.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/supervisor.rs), [`crates/borg/src/executor.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/executor.rs), [`crates/borg/src/guardrails.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/guardrails.rs), [`crates/borg-loop/src/runtime.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg-loop/src/runtime.rs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Parallel supervision, budget admission, actor registry and optional guardrails.
- Plausible first-party paths checked: Budget-triggered throttling and intervention through cancellation/approval.
- Why no material first-party path remains: These control execution under previously chosen rules and lack a first-party current-commitment judgment role and return.

## S3* — Complementary audit

- State: —
- Function: No complementary audit of a live operational claim is established.
- Disturbance / variety regulated: A composed agent may give an unreliable result or violate a runtime guardrail.
- Decisive decision or feedback right: Sample operational evidence through a distinct path and return a corrective judgment.
- Decision owner: Testing assertions are defined by developers. A reviewer in a composition must be authored by the embedder.
- Supporting / enforcement mechanisms: Tracing, event recording, scripted evals and configurable guardrails.
- Closure path: Testing compares fake runs with expected events; runtime guardrails use execution signals for enforcement.
- Boundary reachability: The testing feature runs the composition with FakeLlmClient. Review is an illustrative role in the README.
- Why this is / is not agent-owned: Neither the supplied testing path nor the guardrail path implements claim-specific independent operational verification.
- Evidence: [`README.md`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/README.md), [`crates/borg/src/evals.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/evals.rs), [`crates/borg/src/guardrails.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/guardrails.rs), [`crates/borg/src/event_recorder.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/event_recorder.rs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Scripted evals, event recording, guardrails and sample reviewer composition.
- Plausible first-party paths checked: Boundary checks, event inspection and a documented reviewer role.
- Why no material first-party path remains: None supplies distinct primary operational evidence, an audit judgment and a return to a legitimate decision owner in a shipped mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: No outside-and-then adaptation function is established.
- Disturbance / variety regulated: Model availability, retryable errors and actor interruptions affect the current execution.
- Decisive decision or feedback right: Sense a future-relevant environmental change and return a durable capability option.
- Decision owner: Adopter sets model ladder and checkpoint policy.
- Supporting / enforcement mechanisms: Fallback ladders, checkpoint store, restart and context propagation.
- Closure path: Current errors select a preconfigured alternative or restore a prior run.
- Boundary reachability: The executor exposes ladder and resumable paths.
- Why this is / is not agent-owned: Substitution within an authored plan addresses current continuity.
- Evidence: [`crates/borg/src/ladder.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/ladder.rs), [`crates/borg/src/checkpoint.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/checkpoint.rs), [`crates/borg/src/executor.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/executor.rs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Model fallback ladder, actor resume, checkpoint and external client interfaces.
- Plausible first-party paths checked: Model substitution under failure and checkpoint restart.
- Why no material first-party path remains: No shipped environmental sensing and prospective capability decision connects these to changed future operation.

## S5 — Policy and identity

- State: —
- Function: No first-party identity or ultimate-policy decision mode is established.
- Disturbance / variety regulated: An operation may require an approval or a different sandbox policy.
- Decisive decision or feedback right: Resolve an ultimate system mandate issue and return the resulting policy to operations.
- Decision owner: Adopter and operator define task policy and issue per-run decisions.
- Supporting / enforcement mechanisms: Suspend/resume decisions, tool approval and sandbox backend.
- Closure path: Approve, reject or edit returns to the suspended task.
- Boundary reachability: The actor and tool helpers expose a documented human-in-the-loop task mode.
- Why this is / is not agent-owned: An approval within a run leaves the system mandate set by its embedding application.
- Evidence: [`crates/borg-loop/examples/human_in_the_loop.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg-loop/examples/human_in_the_loop.rs), [`crates/borg-loop/src/handle.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg-loop/src/handle.rs), [`crates/borg-tools/src/approval.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg-tools/src/approval.rs), [`crates/borg/src/suspend.rs`](https://github.com/joydle/borg/blob/be9d9cf613a16ef13772c3fc4ddcfae27321579d/crates/borg/src/suspend.rs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Human-in-the-loop example, approval helper, suspension state and public configuration.
- Plausible first-party paths checked: Human approve/reject/edit and developer-selected runtime policy.
- Why no material first-party path remains: None supplies a first-party ultimate-policy issue and corresponding authoritative return across operations.

## Recursion

One adopter-composed pipeline or actor session is the potential operating unit. The assessment boundary is the supplied library distribution before adopter assembly.

## Variety and escalation

The library provides bounded concurrency, event recording, checkpoints, cancellation and configurable guardrails to help an embedding absorb run-level disturbances.

## Evidence gaps

Source-static. No adopter application, live provider, or tool execution was run. An adopter distribution bundling a real actor and live client would be a different assessment boundary.
