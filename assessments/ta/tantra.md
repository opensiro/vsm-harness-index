---
harness_id: tantra
project_name: tantra
repository: https://github.com/malayh/tantra
review_ref: 779bf82b073bc5121bb70f45b36dab1ae1c05fd8
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# tantra

## Review boundary

- System in focus: tantra-harness core durable actor runtime, not a custom application organization or the Sarathi research product.
- Purpose and identity: host persistent model/tool agent turns, child actors and reconnectable execution through local APIs or ACP.
- Relevant environment: application-defined Agent/tool declarations, configured provider, storage, ACP clients and human tool-approval responses.
- Standard-distribution boundary: packages/tantra core Runtime/TurnEngine, built-in framework/memory/skill tools, stores, compactor, provider adapter and ACP support.
- Credited operating / distribution surfaces: Runtime.create/connect/actor drain to supplied TurnEngine model/tool loop and built-in spawn/send/status/cancel child tools.
- Adjacent first-party surfaces excluded from ownership: Sarathi demo application, stress/e2e fixtures, FakeProvider tests, website/design notes and CI/development agents. They inform boundary and API behavior without supplying core metasystem owners.
- First-party operating / deployment modes considered: in-process runtime with supported stores, optional PostgresCoordinator for ownership/fencing, ACP stdio/WebSocket serving, root human asks and reusable child actors.
- Recursion level: one runtime/application agent tree; named parent-child edges do not establish recursive viable systems.
- Reviewed revision: `779bf82b073bc5121bb70f45b36dab1ae1c05fd8`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[runtime.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/runtime.py) stores agent/session headers, queues commands idempotently, drains each actor serially and creates [loop.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/loop.py) for the next turn. The model chooses tools or final/structured output; completed tool events rebuild subsequent context. Optional child actors have independent journals; terminal replies are durably delivered to the parent as new input, and send only crosses direct parent-child edges. [coordinator.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/coordinator.py) controls execution ownership, fenced writes, forwarding, writer claims and process recovery. These are runtime correctness roles, not autonomous organizational judgment. Agent declarations supply model/prompt/tools/max_steps; permissions and [hooks.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/hooks.py) can deny or escalate a tool action. Root asks may await a human; children cannot ask humans directly. [memory.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/memory.py) supports explicit memory writes/recall; compaction manages context and optional summaries. ACP transports commands, observations, writer transitions and model settings. Sarathi is separately documented as a demo app.

## Operational model

Configured agents own task-specific model/tool choices. The reusable core supplies an executable loop rather than merely recommending an external agent CLI. Developers supply ordinary Agent declarations and tools; runtime stores, permission enforcement and lease machinery do not inherit the agent's discretion. Parent-child management remains operational delegation at this evidence boundary.

## S1 — Operations

- State: A
- Function: Model-backed task operations in durable actors.
- Disturbance / variety regulated: User input, tool failures, changing task evidence and asynchronous child replies.
- Decisive decision or feedback right: Choose next tool/arguments, child task/message or final result from the current journal context.
- Decision owner: Configured model-backed agent actor.
- Supporting / enforcement mechanisms: TurnEngine, provider transport, schema/permission gates, durable store, inbox drain and retry/step limits.
- Closure path: TurnEngine._drive constructs request from history, samples the model, executes tools and persists completion; results and child replies enter later model turns.
- Boundary reachability: Runtime._drain directly instantiates the shipped TurnEngine using registered Agent/provider/tools; no new agent-control implementation is needed for declared modes.
- Why this is / is not agent-owned: Removing the model leaves queueing/replay and fixed checks, but not task-specific tool selection and response judgment.
- Evidence: [runtime.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/runtime.py); [loop.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/loop.py); [agent.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/agent.py); [README](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/README.md)
- Basis: structural
- Confidence: high for supported source paths
- Caveats: No live provider run or operational performance witness; default model/tools remain application-selected.

## S2 — Coordination

- State: —
- Function: Inter-S1 interference regulation is not established at the core-runtime boundary.
- Disturbance / variety regulated: Actor mailboxes, root locks, command identity and leases suppress duplicate execution and concurrent writers for the same actor/tree. They do not establish a regulated conflict between distinct operational work units.
- Decisive decision or feedback right: No shipped function-specific decisive regulation/return path identified.
- Decision owner: No credited owner; application developers/operators configure constraints.
- Supporting / enforcement mechanisms: Durable events, inboxes, leases, permissions, hooks, retry and cancellation.
- Closure path: No qualifying metasystem feedback beyond the operational turn protocol.
- Why this is / is not agent-owned: Actor mailboxes, root locks, command identity and leases suppress duplicate execution and concurrent writers for the same actor/tree. They do not establish a regulated conflict between distinct operational work units.
- Evidence: [runtime.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/runtime.py); [coordinator.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/coordinator.py)
- Basis: structural
- Confidence: high within the declared standard distribution
- Caveats: Applications may compose stronger organization; generic APIs are not that composition.

### Absence scope

- Surfaces inspected: Runtime actor activation/drain/framework tools and lifecycle return; TurnEngine drive/preflight/batch; coordinator ownership/writer contracts; Agent declarations, hooks, permissions, memory/skills/compaction; README, Sarathi deployment scope and test inventory.
- Plausible first-party paths checked: spawn/send/lifecycle replies, per-actor FIFO, root execution leases, writer fencing and concurrent tool batches
- Why no material first-party path remains: The reviewed core ships task messaging and duplicate-writer correctness, not a specific inter-S1 interference-response-feedback relation. Same-actor replicas and client writers are not distinct S1 units.

## S3 — Inside-and-now control

- State: —
- Function: Whole-system current control is not established at the core-runtime boundary.
- Disturbance / variety regulated: Child status/cancel and tree status expose task lifecycle; fixed max_steps, permission inheritance and process ownership do not supply a whole-current discretionary regulator.
- Decisive decision or feedback right: No shipped function-specific decisive regulation/return path identified.
- Decision owner: No credited owner; application developers/operators configure constraints.
- Supporting / enforcement mechanisms: Durable events, inboxes, leases, permissions, hooks, retry and cancellation.
- Closure path: No qualifying metasystem feedback beyond the operational turn protocol.
- Why this is / is not agent-owned: Child status/cancel and tree status expose task lifecycle; fixed max_steps, permission inheritance and process ownership do not supply a whole-current discretionary regulator.
- Evidence: [runtime.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/runtime.py); [loop.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/loop.py); [agent.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/agent.py)
- Basis: structural
- Confidence: high within the declared standard distribution
- Caveats: Applications may compose stronger organization; generic APIs are not that composition.

### Absence scope

- Surfaces inspected: Runtime actor activation/drain/framework tools and lifecycle return; TurnEngine drive/preflight/batch; coordinator ownership/writer contracts; Agent declarations, hooks, permissions, memory/skills/compaction; README, Sarathi deployment scope and test inventory.
- Plausible first-party paths checked: tree_status/watch_tree, parent child cancellation, max_depth/max_steps, ACP model selection, coordinator recovery and root operator intervention
- Why no material first-party path remains: Delegation/cancellation is scoped to current task execution; generic observation and API controls do not compose a current whole-system resource/commitment decision and returned regulatory closure.

## S3* — Complementary audit

- State: —
- Function: Complementary audit is not established at the core-runtime boundary.
- Disturbance / variety regulated: Tracing, persisted journals, hook callbacks and test providers record/check ordinary execution; no shipped independent source-of-truth audit judgment acts on an operational claim.
- Decisive decision or feedback right: No shipped function-specific decisive regulation/return path identified.
- Decision owner: No credited owner; application developers/operators configure constraints.
- Supporting / enforcement mechanisms: Durable events, inboxes, leases, permissions, hooks, retry and cancellation.
- Closure path: No qualifying metasystem feedback beyond the operational turn protocol.
- Why this is / is not agent-owned: Tracing, persisted journals, hook callbacks and test providers record/check ordinary execution; no shipped independent source-of-truth audit judgment acts on an operational claim.
- Evidence: [tracing.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/tracing.py); [hooks.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/hooks.py); [runtime.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/runtime.py)
- Basis: structural
- Confidence: high within the declared standard distribution
- Caveats: Applications may compose stronger organization; generic APIs are not that composition.

### Absence scope

- Surfaces inspected: Runtime actor activation/drain/framework tools and lifecycle return; TurnEngine drive/preflight/batch; coordinator ownership/writer contracts; Agent declarations, hooks, permissions, memory/skills/compaction; README, Sarathi deployment scope and test inventory.
- Plausible first-party paths checked: event/history access, telemetry/tracing, hook after_turn, structured-output validation and FakeProvider tests
- Why no material first-party path remains: The core supplies observability and extensibility, with no independently judging complementary audit actor/path and corrective return wired into supported operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: External/prospective adaptation is not established at the core-runtime boundary.
- Disturbance / variety regulated: Web tools answer task research, memory stores recalled records and compaction accommodates context size. These do not produce and select future capability options from environmental modelling.
- Decisive decision or feedback right: No shipped function-specific decisive regulation/return path identified.
- Decision owner: No credited owner; application developers/operators configure constraints.
- Supporting / enforcement mechanisms: Durable events, inboxes, leases, permissions, hooks, retry and cancellation.
- Closure path: No qualifying metasystem feedback beyond the operational turn protocol.
- Why this is / is not agent-owned: Web tools answer task research, memory stores recalled records and compaction accommodates context size. These do not produce and select future capability options from environmental modelling.
- Evidence: [memory.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/memory.py); [compaction.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/compaction.py); [skills.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/skills.py)
- Basis: structural
- Confidence: high within the declared standard distribution
- Caveats: Applications may compose stronger organization; generic APIs are not that composition.

### Absence scope

- Surfaces inspected: Runtime actor activation/drain/framework tools and lifecycle return; TurnEngine drive/preflight/batch; coordinator ownership/writer contracts; Agent declarations, hooks, permissions, memory/skills/compaction; README, Sarathi deployment scope and test inventory.
- Plausible first-party paths checked: memory recall/write/supersede, dynamic prompt/model params, provider context-limit recovery, web tools, skill loading and model updates
- Why no material first-party path remains: The supplied core closes operational context/storage management; no external-and-prospective adaptation conversation returns a selected change to present organizational capability. Sarathi research content is an S1 application output.

## S5 — Policy and identity

- State: —
- Function: Identity/ultimate-policy closure is not established at the core-runtime boundary.
- Disturbance / variety regulated: Permission rules and root Approval/Question asks address individual tool calls; application access policies and writer/model settings do not establish identity-level resolution.
- Decisive decision or feedback right: No shipped function-specific decisive regulation/return path identified.
- Decision owner: No credited owner; application developers/operators configure constraints.
- Supporting / enforcement mechanisms: Durable events, inboxes, leases, permissions, hooks, retry and cancellation.
- Closure path: No qualifying metasystem feedback beyond the operational turn protocol.
- Why this is / is not agent-owned: Permission rules and root Approval/Question asks address individual tool calls; application access policies and writer/model settings do not establish identity-level resolution.
- Evidence: [permissions.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/permissions.py); [ask.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/ask.py); [loop.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/loop.py); [acp/server.py](https://github.com/malayh/tantra/blob/779bf82b073bc5121bb70f45b36dab1ae1c05fd8/packages/tantra/src/tantra/acp/server.py)
- Basis: structural
- Confidence: high within the declared standard distribution
- Caveats: Applications may compose stronger organization; generic APIs are not that composition.

### Absence scope

- Surfaces inspected: Runtime actor activation/drain/framework tools and lifecycle return; TurnEngine drive/preflight/batch; coordinator ownership/writer contracts; Agent declarations, hooks, permissions, memory/skills/compaction; README, Sarathi deployment scope and test inventory.
- Plausible first-party paths checked: agent prompt/permission chain, hook Denial/Escalation, root ask/answer, ACP access policy, writer claim and configuration
- Why no material first-party path remains: No runtime identity/ultimate-policy issue is routed to a legitimate authority and returned as governing policy. Generic human consent and app-defined policy callbacks are not a positive parent S5 mode.

## Distributed OSS parent arrangement

Apache-2.0 development and repository governance remain outside the core runtime. Multi-user app deployment does not itself establish organization-level parent ownership.

## Self-hosted and non-human modes

Local stores and optional multi-process PostgreSQL coordination change durability/ownership enforcement. Human root tool approvals do not establish function-specific parent S3/S4/S5; no autonomous non-human metasystem mode is supplied.

## Recursion

Agents can declare/spawn child types and retain reusable actors. Their journals and task environments do not supply the child's metasystemic viability; no VSM recursion is inferred.

## Variety and escalation

Permission denials, root human asks, retries, durable cancel and interrupted-turn recovery regulate operational failures. The Escalation type raises ordinary tool permission to ask; its name is not proof of an algedonic authority path.

## Evidence gaps

Static source review only. The package requires Python >=3.13; available runtime is Python 3.12 and no Python 3.13/uv/pytest binary is available, so native suite was not run. PostgreSQL/ACP deployment and live provider behavior were not exercised. No environmental adaptation/audit organization is borrowed from the separately scoped Sarathi demo or tests.
