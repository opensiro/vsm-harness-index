---
harness_id: ruhui-agent
project_name: RuHui Agent
repository: https://github.com/Andy1890/ruhui-agent
review_ref: 4bbff9f3094f5024edb7e25ba36b4c31d55df7d6
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# RuHui Agent

## Review boundary

- System in focus: RuHui's first-party Node CLI and embeddable Agent SDK at the pinned repository revision.
- Purpose and identity: Translate a user task into a bounded, recoverable local model-tool turn.
- Relevant environment: One local workspace and runtime home, user-supplied instructions and limits, and a scripted or OpenAI-compatible model provider.
- Standard-distribution boundary: The shipped Node CLI and same-process SDK bind a provider, tool executor, context and JSONL rollout to the same first-party core loop. Model inference is supplied by the configured endpoint.
- Credited operating / distribution surfaces: [`README.md`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/README.md), [`packages/cli/ruhui.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/cli/ruhui.mjs), [`packages/sdk/agent-node.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/sdk/agent-node.mjs), [`packages/core/src/loop.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/core/src/loop.ts), [`packages/tools/src/runtime.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/tools/src/runtime.ts), [`packages/providers/openai-node.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/providers/openai-node.mjs)
- Adjacent first-party surfaces excluded from ownership: Offline meeting-notes and walking-skeleton examples, scripted responses, CI and development evals illustrate or check the runtime. They are not extra operating actors.
- First-party operating / deployment modes considered: CLI run/resume/doctor and embeddable Agent run/stream. A scripted provider supports offline demonstration, while the configurable OpenAI-compatible adapter supplies the decision-making mode.
- Recursion level: A single task turn within one local session is the S1 unit. The CLI and SDK are entrypoints to the same unit, and separate sessions do not constitute a coordinated portfolio in this distribution.
- Reviewed revision: `4bbff9f3094f5024edb7e25ba36b4c31d55df7d6`, [intake #3059](https://github.com/opensiro/vsm-harness-index/issues/3059) and [controller #3060](https://github.com/opensiro/vsm-harness-index/issues/3060).
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The SDK execution path assembles workspace context, chooses the configured provider, opens the rollout, binds local handlers and invokes runLoop. The loop processes model events, validates calls, sends them to the tool executor, appends tool results and corrective hints to the message history, and requests the next model decision.
The core records start, tool and completion events. SDK resume uses persisted rollout state to resume a local task. Policy denies tools by mode, while budget and repeated failure checks constrain the current turn.

## Operational model

The model selects steps within a user task using file, command and plan tools made available by the host. The runtime returns success, tool failure or policy denial to that turn and can surface a waiting-user result. Scripted examples exercise the same structure with predetermined outputs.

## S1 — Operations

- State: A
- Function: Carry out a local user task through iterative model-selected tool actions.
- Disturbance / variety regulated: Tool failures, malformed output, incomplete workspace information and consumption limits.
- Decisive decision or feedback right: Choose the next supported tool and its arguments, revise after observations, or finish with text.
- Decision owner: The model actor bound to the first-party CLI/SDK turn owns the semantic choices. The runtime owns dispatch and fixed limits.
- Supporting / enforcement mechanisms: Provider adapter, context assembly, tool mode policy, local handlers, rollout and budget checks.
- Closure path: Task → provider response → tool call → local observation or corrective hint → next provider step → completion or bounded stop.
- Boundary reachability: CLI delegates to the SDK and the SDK binds the configured provider and executor before calling the core loop. The OpenAI-compatible adapter is an implemented mode.
- Why this is / is not agent-owned: The semantic action is selected from task and results by the model. The scripted provider is a fixture mode and does not substantiate agent ownership by itself.
- Evidence: [`packages/cli/ruhui.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/cli/ruhui.mjs), [`packages/sdk/agent-node.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/sdk/agent-node.mjs), [`packages/core/src/loop.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/core/src/loop.ts), [`packages/providers/openai-node.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/providers/openai-node.mjs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

## S2 — Coordination

- State: —
- Function: No distinct S1 coordination is established in the local turn boundary.
- Disturbance / variety regulated: Tool order and per-workspace state can affect the current task.
- Decisive decision or feedback right: An inter-operation conflict judgment would require independently operating S1 units sharing a relevant disturbance.
- Decision owner: The active turn owns its tool decisions. The runtime sequences calls and keeps session state.
- Supporting / enforcement mechanisms: Serial tool dispatch, tool-batch concurrency flags and local rollout/session boundaries.
- Closure path: Tool results return to the same turn. No lateral conflict signal is returned between S1s.
- Boundary reachability: The CLI and SDK bind the same single-turn execution path.
- Why this is / is not agent-owned: Ordering tools issued by one model is internal to S1.
- Evidence: [`packages/core/src/loop.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/core/src/loop.ts), [`packages/tools/src/runtime.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/tools/src/runtime.ts), [`packages/sdk/agent-node.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/sdk/agent-node.mjs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Core call handling, tool batching and SDK session/turn construction.
- Plausible first-party paths checked: Parallel/serial tool modes and multiple separately invokable Agent objects.
- Why no material first-party path remains: The tool work belongs to one current turn. Independently created SDK objects have no shipped coordination relation.

## S3 — Inside-and-now control

- State: —
- Function: No separate current-control process over whole-system commitments is established.
- Disturbance / variety regulated: Current turn cost, time and repeated tool failures.
- Decisive decision or feedback right: A portfolio-level intervention would require a current view and discretion over commitments beyond the turn.
- Decision owner: The local constructor defines budgets and stopping rules. The user initiates or resumes work.
- Supporting / enforcement mechanisms: Consumption counters, failure caps, exit states and the CLI doctor.
- Closure path: Counters and observations produce fixed continuation or stopping behavior for the current turn.
- Boundary reachability: SDK run/resume and doctor are reachable. Their current scope is local session execution and readiness.
- Why this is / is not agent-owned: Local budget guards execute configured rules inside S1.
- Evidence: [`packages/core/src/loop.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/core/src/loop.ts), [`packages/core/src/budget.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/core/src/budget.ts), [`packages/sdk/agent-node.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/sdk/agent-node.mjs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Budget handling, CLI doctor, SDK run/resume and tool approval requests.
- Plausible first-party paths checked: Budget finalization prompt, user interruption and user-input stop.
- Why no material first-party path remains: Each acts on the immediate task. There is no separate whole-current view and discretionary intervention return.

## S3* — Complementary audit

- State: —
- Function: No complementary operational audit is established.
- Disturbance / variety regulated: Potential disagreement between a task claim and actual workspace or tool outcomes.
- Decisive decision or feedback right: Independently sample evidence for the claim and return a corrective judgment.
- Decision owner: The producing turn receives its own tool results. Development checks are maintained separately from task operation.
- Supporting / enforcement mechanisms: Rollout events, deterministic rollout checks and eval fixtures.
- Closure path: Runtime feedback goes back to the original model. Offline checks have no first-party return into current task control.
- Boundary reachability: The product exposes its own event stream. The evaluation scripts are repository development commands.
- Why this is / is not agent-owned: Observation and deterministic checking do not establish a separate claim-specific challenge and return in the shipped operating mode.
- Evidence: [`packages/core/src/loop.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/core/src/loop.ts), [`packages/sdk/agent-node.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/sdk/agent-node.mjs), [`scripts/eval.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/scripts/eval.mjs), [`scripts/data/rollout.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/scripts/data/rollout.mjs)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Tool result feedback, SDK stream, rollout replay/validation and development eval.
- Plausible first-party paths checked: Separate inspection of logs and deterministic fixture checks.
- Why no material first-party path remains: No distinct operational audit actor or audit-specific constructor with a returned finding is wired into the runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective capability adaptation is established.
- Disturbance / variety regulated: Workspace context and immediate changes to task inputs.
- Decisive decision or feedback right: Observe external change, generate a future option and return it into current capability.
- Decision owner: The user chooses workspace instructions and configuration. The active model addresses the current task.
- Supporting / enforcement mechanisms: Context discovery, configuration loading and session continuation.
- Closure path: The context is assembled for the next local turn without an outside-and-then adaptation path.
- Boundary reachability: Workspace and home configuration are loaded in supported modes.
- Why this is / is not agent-owned: Task plan updates and context assembly do not govern future capability.
- Evidence: [`packages/core/src/context.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/core/src/context.ts), [`packages/sdk/agent-node.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/sdk/agent-node.mjs), [`packages/tools/src/plan.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/tools/src/plan.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Instruction discovery, plan tool, provider configuration and resumed sessions.
- Plausible first-party paths checked: Changed instructions, generated plans and persisted task state.
- Why no material first-party path remains: No first-party prospective sensing or capability-option return is present in the shipped CLI or SDK.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity or policy arbitration process is established.
- Disturbance / variety regulated: Local tool permission and instruction constraints.
- Decisive decision or feedback right: Resolve a conflict in governing identity or ultimate policy and change operating commitments.
- Decision owner: The embedding caller or user configures the runtime, and deterministic tool policy applies the selected mode.
- Supporting / enforcement mechanisms: Tool policy, local configuration, user-input result and sandboxed workspace helpers.
- Closure path: Configured rules gate the current tool invocation. No first-party identity arbitration precedes those constraints.
- Boundary reachability: The first-party dispatcher applies mode policy. The user can respond to task-level requests.
- Why this is / is not agent-owned: Per-action permission and external configuration do not constitute a sourced ultimate-policy decision mode.
- Evidence: [`packages/tools/src/policy.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/tools/src/policy.ts), [`packages/tools/src/runtime.ts`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/tools/src/runtime.ts), [`packages/sdk/agent-node.mjs`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/packages/sdk/agent-node.mjs), [`schema/config.schema.json`](https://github.com/Andy1890/ruhui-agent/blob/4bbff9f3094f5024edb7e25ba36b4c31d55df7d6/schema/config.schema.json)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Tool-mode policy, CLI and SDK configuration, user-input path and package boundary.
- Plausible first-party paths checked: Human tool permission, model instructions and configured workspace rules.
- Why no material first-party path remains: These constrain individual turns. No policy identity issue, legitimate deciding role and operational return are composed.

## Recursion

A single task turn within one local session is the S1 unit. The CLI and SDK are entrypoints to the same unit, and separate sessions do not constitute a coordinated portfolio in this distribution.

## Variety and escalation

The turn absorbs malformed outputs and tool errors through feedback, caps repetitive failure, and returns a bounded stop when interrupted, out of budget or waiting for input.

## Evidence gaps

The assessment is source-static. No model endpoint, local tool action or installed npm distribution was exercised. The repository documents source execution and describes npm publication as pending.
