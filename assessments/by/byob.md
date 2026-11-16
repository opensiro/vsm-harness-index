---
harness_id: byob
project_name: byob
repository: https://github.com/Scronkfinkle/byob
review_ref: f32aa7a31bdf696e8ab1dbb686db151ba402738b
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# byob

## Review boundary

- System in focus: One byob engine serving a workspace and its attached desktop/browser chat clients.
- Purpose and identity: Local-first tool-using coworker organized around workspaces and an operator-selected model endpoint.
- Relevant environment: Operator goals, local files and environment, inference capacity, and workspace-provided extensions.
- Standard-distribution boundary: Installed byob application, headless engine, desktop/browser modes and bundled plugin/toolset interfaces.
- Credited operating / distribution surfaces: Normal chat and subagent turn loops, applicable endpoint slot leases, user-managed authoring and workspace plugin policy.
- Adjacent first-party surfaces excluded from ownership: Contributor and build workflows, example plugins and test fixtures. External model endpoints supply inference.
- First-party operating / deployment modes considered: Native desktop, browser/headless client attachment, bundled subagents, and retained workspace/global plugins.
- Recursion level: One workspace in the byob engine. Its chat turns and delegated tasks act as operational units.
- Reviewed revision: `f32aa7a31bdf696e8ab1dbb686db151ba402738b`
- Observation date: 2026-11-16
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

One engine owns chat sessions, permissions and runtime extensions. Client front ends attach over the product protocol. Worker turns apply model choices to a composed tool registry, while the engine maintains journals and allows optional child turns and plugin reloads.

## Operational model

A chat receives a goal and can select, run and revise admitted operations. Caller-specific tools and child prompts are assembled inside the workspace's policy. The model can author a candidate extension, while durable plugin scope and external workspace trust have operator decision paths.

## S1 — Operations

- State: A
- Function: Complete requested work in model-backed chat turns.
- Disturbance / variety regulated: Tool failures, intermediate output and differing workspace tasks.
- Decisive decision or feedback right: Choose admitted tools, steer subsequent calls using results and finish the turn.
- Decision owner: The model-backed chat or delegated child actor.
- Supporting / enforcement mechanisms: Typed registries, client approvals, context and call limits, execution journal.
- Closure path: A tool response or error enters the next model message; the engine publishes and persists progress and outcome.
- Why this is / is not agent-owned: The actor selects calls and responses while the host enforces permissions.
- Evidence: [crates/agent/src/lib.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/lib.rs#L1-L14), [crates/agent/src/turn.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/turn.rs#L447-L503), [crates/agent/src/delegate.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/delegate.rs#L1-L20).
- Basis: Shipped worker turn and engine wiring.
- Confidence: High.
- Caveats: Provider inference is separable from the bundled execution and feedback loop.
- Boundary reachability: Desktop and browser clients connect to the same installed engine. The engine runs worker turns against registered tools; the enabled bundled subagents plugin can start the same bounded loop for children.

## S2 — Coordination

- State: C
- Function: Attenuate contention for a shared inference endpoint among parent chats and concurrent delegated operations.
- Disturbance / variety regulated: A child request can take a waiting parent's llama.cpp cache slot; multiple children can consume endpoint capacity.
- Decisive decision or feedback right: Bind parent and child operations to available slots and control child concurrency at the endpoint.
- Decision owner: The first-party lease and semaphore implement the arbitration; effective endpoint and parallelism are composed through configuration.
- Supporting / enforcement mechanisms: Endpoint capability probe, parent-sticky lease preference, model cap and child queue.
- Closure path: Lease and capacity admissions affect actual subsequent model requests. Dropping a lease or guard opens capacity for peers.
- Why this is / is not agent-owned: The configured runtime relation chooses slots and releases capacity. Delegating model actors do not own the allocator.
- Evidence: [crates/agent/src/slot_leases.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/slot_leases.rs#L1-L15), [crates/agent/src/slot_leases.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/slot_leases.rs#L56-L94), [crates/agent/src/delegate.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/delegate.rs#L85-L147), [crates/agent/src/delegate.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/delegate.rs#L626-L699).
- Basis: Dedicated first-party interference countermeasure with explicit capacity/configuration and later request feedback.
- Confidence: Medium.
- Caveats: The lease applies to endpoints with supported slot probing. Saturation can fall back to the endpoint's own choice, and hosted endpoints may use only the concurrency bounds.
- Boundary reachability: Main and child turns request slots from the installed engine's shared table. The bundled delegate path takes the endpoint and selected model's configured capacity into account.
- Distinct S1 units: Distinct chat turns and delegated child tool loops with separate contexts and ongoing work on the same endpoint.
- Inter-S1 disturbance: Using the same inference slot can evict a paused chat's prompt cache, and concurrent children consume slots needed by peers.
- Attenuating coordination relation: Retain a chat's sticky preference, avoid assigning actively leased slots, and limit child launch against shared/model capacity.
- Feedback into subsequent S1 behaviour: The selected slot becomes a model request input; release updates shared availability and lets waiting work proceed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The lease reacts to other operations' current claims and adjusts actual request placement to protect them. The result changes the following inference requests.

## S3 — Inside-and-now control

- State: —
- Function: Choose whole-workspace current commitments, constraints or priorities.
- Disturbance / variety regulated: Competing active chats, resources and changes to live work.
- Decisive decision or feedback right: Use a whole-current view to redirect or reallocate workspace operations.
- Decision owner: No source-backed discretionary whole-workspace controller at this recursion.
- Supporting / enforcement mechanisms: Per-chat queue, current status, stop and approval paths, fixed shared capacity.
- Closure path: Queue progress and turn control affect the selected chat; leases and limits supply endpoint coordination.
- Why this is / is not agent-owned: The parent model can select child tools and models for delegated tasks. The reviewed paths do not give it a current workspace portfolio mandate.
- Evidence: [crates/agent/src/lib.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/lib.rs#L1-L14), [crates/agent/src/queue.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/queue.rs#L1-L18), [crates/agent/src/workspaces.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/workspaces.rs#L1-L10), [crates/agent/src/delegate.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/delegate.rs#L375-L462), [crates/agent/src/hooks.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/hooks.rs#L352-L425).
- Basis: Engine, queue, workspace setting and child launch code.
- Confidence: Medium.
- Caveats: The operator can make local changes, including stopping individual work.

### Absence scope

- Surfaces inspected: Engine view and per-chat controls, queued follow-ups, settings scopes, model selection for a child, and turn hooks.
- Plausible first-party paths checked: Operator chat monitoring and intervention, agent delegation/control and a configurable tool-call hook.
- Why no material first-party path remains: The ordinary views and controls are per chat; delegation binds one new operation. Turn hooks see prompt/request/tool events and lack a whole-workspace current-state and resource-decision contract.

## S3* — Complementary audit

- State: —
- Function: Independently verify operational claims through a complementary path.
- Disturbance / variety regulated: Difference between a chat or child's report and actual workspace effects.
- Decisive decision or feedback right: Inspect primary evidence independently and return a corrective judgment to a control owner.
- Decision owner: No dedicated first-party operational audit witness.
- Supporting / enforcement mechanisms: Fresh child contexts, configurable tools and hooks, turn/effect journaling, plugin tests.
- Closure path: A child result returns as normal delegation output; journals and tests serve routine operation and authoring.
- Why this is / is not agent-owned: The installed generic child tool can be used as a reviewer by a caller, but the shipped path itself does not establish a function-specific complementary audit role.
- Evidence: [crates/agent/src/delegate.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/delegate.rs#L1-L20), [crates/agent/src/delegate.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/delegate.rs#L429-L493), [crates/agent/src/turn.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/turn.rs#L410-L443), [crates/agent/src/authoring.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/authoring.rs#L344-L396), [crates/agent/src/hooks.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/hooks.rs#L425-L474).
- Basis: Generic delegation and plugin authoring/reload pipeline.
- Confidence: Medium.
- Caveats: Caller-defined audit plugins could supply additional evidence under another boundary.

### Absence scope

- Surfaces inspected: Child construction and return, tool and turn hooks, journals, and plugin quick tests.
- Plausible first-party paths checked: A fresh child as auditor, post-tool reporting as a second channel, and authoring tests as checks of operations.
- Why no material first-party path remains: Fresh context permits an independent role to be composed but supplies no audit mandate or returned corrective decision by itself. The other paths check the producing workflow's own effects.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt future workspace or installation capability by adopting a tool/plugin produced for a recurring need.
- Disturbance / variety regulated: An encountered workflow needs a capability that existing tools do not supply.
- Decisive decision or feedback right: Select a durable scope and authorize adoption so other or later chats receive a new tool.
- Decision owner: The workspace or installation operator for durable plugin adoption.
- Supporting / enforcement mechanisms: Model-side plugin authoring with reload and test feedback, scoped confirmation, copy and registry refresh.
- Closure path: The model authors a candidate; the authoring path returns load status or tool results; the operator decides on promotion and the engine loads the retained tool for subsequent chats.
- Why this is / is not agent-owned: The model designs and revises the capability. Durable plugin adoption through the cited keep path is operator-controlled.
- Evidence: [crates/agent/src/authoring.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/authoring.rs#L1-L8), [crates/agent/src/authoring.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/authoring.rs#L302-L396), [crates/agent/src/authoring.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/authoring.rs#L1052-L1098), [crates/agent/src/authoring.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/authoring.rs#L1163-L1229), [crates/agent/src/plugin_authoring.md](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/plugin_authoring.md#L5-L19).
- Basis: Bundled make_tool and keep_plugin, with explicit workspace/global persistence and refresh.
- Confidence: High.
- Caveats: A chat's scratch tool can be made available in the next round. This assessment credits a change at workspace/installation scope, where keep changes later operations.
- Boundary reachability: The installed authoring tools request engine reload; kept workspace/global plugins are resolved into subsequent chat registries by the installed plugin loader.
- External distinction: The user's workplace task or recurring workflow reveals an unmet capability in the current tool environment.
- Future / prospective distinction: The promotion card asks whether to make the tool available beyond the producing turn/chat.
- Adaptation option generated: A concrete new tool/plugin, with generated schema, load diagnostics and optional test result available before retention.
- Path back into current capability / S3: The authorized keep writes into the selected workspace/global plugin directory, reloads the available tools, and makes them available to later operational chats.

## S5 — Policy and identity

- State: P
- Function: Set the standing scope of authority for executable plugins discovered in a workspace.
- Disturbance / variety regulated: A folder can include externally authored plugins with tools or running backends.
- Decisive decision or feedback right: Admit or reject such plugins as part of the workspace's standing operating boundary.
- Decision owner: The workspace operator responding through the authenticated/attached product client.
- Supporting / enforcement mechanisms: Undecided-plugin review, workspace trust records, backend stop, and extension refresh.
- Closure path: The operator chooses trust or decline; the engine persists the choice per workspace, refreshes extensions and can stop a declined backend.
- Why this is / is not agent-owned: The agent can propose a plugin or use tools in policy. It does not own the decision to admit third-party plugins found with the workspace.
- Evidence: [crates/agent/src/plugins.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/plugins.rs#L618-L675), [crates/agent/src/turn.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/turn.rs#L447-L460), [crates/agent/src/workspaces.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/workspaces.rs#L1-L10), [crates/agent/src/permissions.rs](https://github.com/Scronkfinkle/byob/blob/f32aa7a31bdf696e8ab1dbb686db151ba402738b/crates/agent/src/permissions.rs#L32-L87).
- Basis: First-party trust and reload path restricting future workspace operation.
- Confidence: High.
- Caveats: This is a standing policy decision about available capabilities; per-call approvals are a separate gate.
- Boundary reachability: The installed engine exposes TrustPlugins for workspace plugins with no saved trust decision. A first-party turn can raise the prompt before running.
- Identity / ultimate-policy issue: Which external executable extensions may become part of the workspace's trusted operating scope.
- Ultimate authority in each claimed mode: The workspace operator, with the engine enforcing the saved decision and execution policy.
- Return-to-operation path: Saved trust affects subsequent extension composition in that workspace; declining a plugin stops its backend and refreshes available extensions.

## Distributed OSS parent arrangement

The workspace/installation operator owns the deployment decisions assessed here. Upstream repository maintainer governance is outside the runtime boundary.

## Recursion

A parent turn can create fresh, bounded child operations. The children share workspace authority and inference capacity. Child delegation stops at depth one.

## Variety and escalation

Tool errors return to the model, permission checks return denials or approvals, parallel inference waits on capacity, and stop or failure pauses a per-chat queue.

## Evidence gaps

This is a static assessment at the frozen commit. It does not measure endpoint contention, inspect arbitrary user plugins, or run a model. The coordination finding is scoped to first-party capacity/lease paths.
