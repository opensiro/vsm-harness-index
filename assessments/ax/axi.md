---
harness_id: axi
project_name: Axi
repository: https://github.com/devsohm/axi
review_ref: b1d0fe007535f1c59d08c1f06e014c4558a4862d
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

# Axi

## Review boundary

- System in focus: The packaged Axi Durable Harness and its first-party model and tool adapters.
- Purpose and identity: Run a model-driven conversation and its tasks across tool calls, asynchronous work, state commits and process restarts.
- Relevant environment: An embedding JavaScript application, a supported model endpoint, configurable registered tools and a Durable storage backend.
- Standard-distribution boundary: The release packages supply Harness, the generation/tool feedback loop, live model protocols, built-in tool factories and storage. A host wires these components and supplies task input and credentials. The host's application-specific extensions are outside the assessed distribution.
- Credited operating / distribution surfaces: [`README.md`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/README.md), [`packages/durable/README.md`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/README.md), [`packages/durable/docs/tutorial.md`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/docs/tutorial.md), [`packages/durable/src/harness/harness.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/harness.ts), [`packages/durable/src/harness/generation.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/generation.ts), [`packages/durable/src/harness/tool.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/tool.ts), [`packages/durable/src/tools/index.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/tools/index.ts), [`packages/ai/src/api/openai-responses.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/ai/src/api/openai-responses.ts)
- Adjacent first-party surfaces excluded from ownership: Standalone model catalog maintenance, package tests, codemode demonstrations, arbitrary adopter extensions and UI applications do not add scored actors.
- First-party operating / deployment modes considered: Embedded Harness conversation with scripted or packaged live provider, registered built-in or host tools, and memory or persistent storage. The CLI supplied by the AI package is not the assessed loop.
- Recursion level: A conversation runs an S1 model-tool feedback loop. Root and child conversation and task ownership form a lifecycle hierarchy within one embedded Harness.
- Reviewed revision: `b1d0fe007535f1c59d08c1f06e014c4558a4862d`, [intake #3059](https://github.com/opensiro/vsm-harness-index/issues/3059) and [controller #3060](https://github.com/opensiro/vsm-harness-index/issues/3060).
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Harness.open binds models, storage, registry and scheduler. Submission initiates a GenerationTask, which resolves the selected model and prompt, persists streamed output and classifies tool calls. ToolTask records arguments and results. The generation phase consumes results and starts the next request or commits the answer.
The same scheduler handles checkpointed tasks, context compaction and interrupted work. First-party live model adapters and built-in tool factories can replace tutorial fixtures with configuration. A provider supplies inference and the host determines which tools are exposed.

## Operational model

The operator supplies a task to a conversation. The model selects tools or a response; the scheduler persists each phase and appends tool results to the conversation. Recovery respects the recorded and current replay policy.

## S1 — Operations

- State: A
- Function: Complete a submitted task through model-selected actions and committed feedback.
- Disturbance / variety regulated: Tool outcomes, model errors, context limits, interruptions and partially complete work.
- Decisive decision or feedback right: Select the next supported tool and its arguments, revise the action after tool observations, or return an answer.
- Decision owner: The model bound to the packaged GenerationTask owns semantic choices. The harness owns phase execution and persistence.
- Supporting / enforcement mechanisms: Model collection, first-party provider adapters, ToolTask, registered tool factories, scheduler, views and checkpointed storage.
- Closure path: Conversation submit → GenerationTask selects request → model calls a tool → ToolTask records result → next generation consumes result or commits completion.
- Boundary reachability: Harness.open, root submission, GenerationTask and ToolTask are public supported distribution paths. The shipped provider can be configured in place of the tutorial faux provider.
- Why this is / is not agent-owned: The host selects provider and tool policy. The model makes per-task decisions through the supplied standard executor without a host-authored control loop.
- Evidence: [`packages/durable/docs/tutorial.md`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/docs/tutorial.md), [`packages/durable/src/harness/harness.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/harness.ts), [`packages/durable/src/harness/generation.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/generation.ts#L632-L674), [`packages/durable/src/harness/generation.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/generation.ts#L867-L916), [`packages/durable/src/tools/index.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/tools/index.ts), [`packages/ai/src/api/openai-responses.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/ai/src/api/openai-responses.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

## S2 — Coordination

- State: —
- Function: No autonomous coordination between distinct S1 units is established.
- Disturbance / variety regulated: Parallel conversations and file mutations can share resources.
- Decisive decision or feedback right: Resolve inter-conversation interference and change subsequent operating choices across the units.
- Decision owner: Scheduler and mutation queue serialize work under fixed rules. The host defines any inter-conversation policy.
- Supporting / enforcement mechanisms: Ownership graph, task scheduler, document transactions and canonical-file mutation queue.
- Closure path: Locks and task ordering regulate writes and resource access. Results return to the originating tool or conversation.
- Boundary reachability: Child conversations, task ownership and file tools are present.
- Why this is / is not agent-owned: The implemented lifecycle and write serialization do not expose a distinct cross-S1 decision/feedback role.
- Evidence: [`packages/durable/src/harness/scheduler.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/scheduler.ts), [`packages/durable/src/harness/ownership.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/ownership.ts), [`packages/durable/src/tools/file-mutation-queue.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/tools/file-mutation-queue.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Conversation and task ownership, scheduler, transaction publication and shared file queues.
- Plausible first-party paths checked: Multiple conversations, per-file write conflicts, cancellation and task dependencies.
- Why no material first-party path remains: The runtime manages mechanical contention and ownership. It does not bind an inter-S1 coordination actor or function-specific discretionary feedback path.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control decision mode is established.
- Disturbance / variety regulated: Live tasks, stalled phases, conversation usage and cancellation requests.
- Decisive decision or feedback right: Reallocate or change whole-system operating commitments with returned discretionary intervention.
- Decision owner: The app chooses configuration. The scheduler manages present phases under fixed lifecycle rules.
- Supporting / enforcement mechanisms: Task graph, views, checkpoints, metadata telemetry and cancellation.
- Closure path: Current statuses drive scheduling, restart and cancellation within the lifecycle contract.
- Boundary reachability: The public Harness exposes task inspection and conversation control primitives.
- Why this is / is not agent-owned: Observations and isolated operator controls leave the whole-system judgment and return to adopter code.
- Evidence: [`packages/durable/src/harness/harness.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/harness.ts), [`packages/durable/src/harness/scheduler.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/scheduler.ts), [`packages/durable/src/harness/task-graph.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/task-graph.ts), [`packages/durable/src/harness/view.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/view.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Scheduler, public views, ownership graph, telemetry hooks and conversation configuration.
- Plausible first-party paths checked: Lifecycle recovery, parent cancellation and present-state inspection by host.
- Why no material first-party path remains: No included actor or parent supervision mode joins a whole-current operational view with a discretionary commitment-level action and subsequent feedback.

## S3* — Complementary audit

- State: —
- Function: No complementary operational audit is established.
- Disturbance / variety regulated: An agent response or tool outcome may disagree with task reality.
- Decisive decision or feedback right: Inspect alternative evidence and return a claim-specific corrective judgment.
- Decision owner: Producing conversation receives committed tool results. Hosts own any telemetry or extra hook logic.
- Supporting / enforcement mechanisms: Recorded tool phases, transcript, durable telemetry and development test fixtures.
- Closure path: Runtime records return to the same conversation or host subscribers. There is no audit verdict in standard generation settlement.
- Boundary reachability: Packaged telemetry and task views expose event observations.
- Why this is / is not agent-owned: Neither a hook nor a second arbitrary conversation carries audit-specific independence and return by default.
- Evidence: [`packages/durable/src/harness/generation.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/generation.ts), [`packages/durable/src/harness/telemetry.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/telemetry.ts), [`packages/durable/src/harness/registry.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/registry.ts), [`packages/durable/README.md`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/README.md)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Before and after hooks, GenerationTask settlement, ToolTask records and telemetry.
- Plausible first-party paths checked: Custom registry extensions, transcript views and testing helpers.
- Why no material first-party path remains: No packaged alternative operational evidence path with an independent assessment judgment and corrective return is wired to the shipped conversation.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective adaptation loop is established.
- Disturbance / variety regulated: Changes in model catalogs, context length or available extensions may affect future tasks.
- Decisive decision or feedback right: Sense outside change, judge a future capability option and feed it into present operations.
- Decision owner: Host selects model configuration and extensions. Compaction maintains the active conversation context.
- Supporting / enforcement mechanisms: Model catalogs, compaction tasks, configuration and persisted context boundaries.
- Closure path: The compaction output changes the next prompt. It does not commit a prospective capability adaptation.
- Boundary reachability: Compaction is a supported conversation function. Catalog tooling belongs to model package maintenance.
- Why this is / is not agent-owned: Selecting or summarizing context for current work does not assign outside-and-then ownership.
- Evidence: [`packages/durable/src/harness/compaction.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/compaction.ts), [`packages/durable/src/harness/agent.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/agent.ts), [`packages/ai/src/model-catalog.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/ai/src/model-catalog.ts), [`packages/durable/docs/spec.md`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/docs/spec.md)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Context compaction, model/provider selection, registry configuration and catalog maintenance.
- Plausible first-party paths checked: Compaction after overflow and application-driven configuration changes.
- Why no material first-party path remains: The paths regulate the current session or are host-selected inputs, without an external-future signal to adaptation decision and capability return.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/policy decision process is established.
- Disturbance / variety regulated: Host policy, request identity overrides and conversation-level settings.
- Decisive decision or feedback right: Resolve an identity-level dispute and apply the authoritative result to future operation.
- Decision owner: The embedding application supplies policy and identity fields. Harness applies runtime configuration.
- Supporting / enforcement mechanisms: Request identity, extension registry, AgentDoc settings and ownership checks.
- Closure path: Configured identity and tool policy influence requests and run admission under predefined rules.
- Boundary reachability: Harness.open and conversation configure are supported configuration paths.
- Why this is / is not agent-owned: An attribution string, permission boundary or configuration override does not substantiate ultimate authority arbitration.
- Evidence: [`packages/durable/README.md`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/README.md), [`packages/durable/src/harness/harness.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/harness.ts), [`packages/durable/src/harness/agent.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/agent.ts), [`packages/durable/src/harness/ownership.ts`](https://github.com/devsohm/axi/blob/b1d0fe007535f1c59d08c1f06e014c4558a4862d/packages/durable/src/harness/ownership.ts)
- Basis: Pinned first-party source and declared distribution.
- Confidence: High for the bounded structural finding.
- Caveats: Source-static assessment. Provider behavior and real-world quality were not tested.

### Absence scope

- Surfaces inspected: Harness identity settings, configurable AgentDoc, registry and task ownership.
- Plausible first-party paths checked: Host-owned settings, task abort and request identity override.
- Why no material first-party path remains: No standard first-party decision or parent return addresses a genuinely ultimate identity/policy issue.

## Recursion

A conversation runs an S1 model-tool feedback loop. Root and child conversation and task ownership form a lifecycle hierarchy within one embedded Harness.

## Variety and escalation

Persistent phase receipts, tool result replay policy, queued inputs, model request retry, compaction and cancellation regulate disturbances within the conversation.

## Evidence gaps

No live provider or installed package archive was executed. The tutorial uses a scripted provider. The live adapter, built-in tool path and generation feedback were reconstructed from the pinned implementation.
