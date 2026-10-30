---
harness_id: agentlane
project_name: AgentLane
repository: https://github.com/yasik/agentlane
review_ref: 66ff002432a41cd2b952d8963e1a4fbe6650d183
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentLane

## Review boundary

- System in focus: installed Python AgentLane runtime and its first-party `DefaultAgent`/`Runner` model/tool feedback loop, with optional addressed-distributed execution. Not downstream clinical business applications or independently supplied model-provider policy systems.
- Purpose and identity: make model-driven agents persistently addressable with identity, tool execution, conversation state, messages and transport-independent execution.
- Relevant environment: model providers, user tasks, files/tool outputs, user-authored agent definitions, addressable workers, message delivery, host processes and persistent state stores.
- Standard-distribution boundary: first-party `src/agentlane/harness`, messaging and runtime implementations; `DefaultAgent.from_markdown` uses a bundled actual model loop. A model client and user instruction are configured inputs, not a developer-implemented substitute agent.
- Credited operating / distribution surfaces: `DefaultAgent`, `RunLoop`, tool call execution, `AgentTool` handoff, persisted `RunState`, built-in local/distributed runtime and message delivery.
- Adjacent first-party surfaces excluded from ownership: example domain applications, clinical inbox demo agents and reviewer roles, tests/CI/roadmap, independently supplied agents on the same messaging fabric, downstream integrations and model providers' organizations.
- Operating modes considered: single-agent local `run`/`run_stream`, model tool use, markdown-defined subagents, optional distributed runtimes with stateful/stateless subscriptions, persistence across runs/processes and caller-controlled tools/permissions.
- Recursion level: one AgentLane harness session or composed addressed agent workgroup with first-party model actors; default provider keys/model content must be supplied at run time.
- Frozen revision: `66ff002432a41cd2b952d8963e1a4fbe6650d183`, reviewed 2026-10-29. Generated/current Profile 0.2.4, Skills Methodology 0.3.7.

## Repository architecture

`DefaultAgent` provisions an actual local runtime/runner, or attaches to a supplied distributed runtime, and saves `RunState`. `RunLoop._run_turns` repeatedly prepares an inference request, receives model-selected tool calls, invokes matching handlers/delegated agents, adds tool outputs to conversation history and asks the model again. `run` serializes calls against the same agent's persisted state; `fork` branches from a snapshot without committing to the primary conversation. `AgentTool` transfers a subagent's result through the parent tool/continuation path. The messaging layer gives stable `AgentId`, topic routing, optional stateful affinity, FIFO per recipient and delivery outcomes; a separate worker host can move addressed agents across processes. Those are strong S1 and transport capabilities, not automatically a completed S2/S3/S3*/S4/S5 organizational loop.

Primary sources at the exact SHA:

- [README and standard entry modes](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/README.md).
- [DefaultAgent persistent execution/fork](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/src/agentlane/harness/agents/_default_agent.py).
- [Model/response/tool cycle](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/src/agentlane/harness/_run_loop.py).
- [Runner bridge](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/src/agentlane/harness/_runner.py); [agent handoff](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/src/agentlane/harness/_handoff.py).
- [Routing engine](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/src/agentlane/messaging/_routing.py) and [routing policy](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/src/agentlane/messaging/_routing_policy.py).
- [High-level agent documentation](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/docs/harness/default-agents.md).
- [Distributed worker composition and example boundary](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/docs/harness/distributed-agents.md).
- [Messaging and delivery semantics](https://github.com/yasik/agentlane/blob/66ff002432a41cd2b952d8963e1a4fbe6650d183/docs/messaging/routing-and-delivery.md).

## S1 — Operations

- State: A
- Function: model-driven local or addressable agents absorb open-ended task variety and produce outcomes through selected tools/subagent handoffs, responses and resumed state.
- Disturbance / variety regulated: changing user goals, tool returns/errors, uncertain task completion and conversations lasting across independent processes or model providers.
- Decisive decision or feedback right: choose substantive next tool/handoff and whether to continue or finish after observing tool results.
- Decision owner: first-party wired model actor in `DefaultAgent`/`RunLoop`, with supplied provider client performing inference; host runner enforces tool contracts/limits.
- Supporting / enforcement mechanisms: `AgentDescriptor`, `Runner`, `Tools`, serialization, agent identity, mailbox, persisted state and step-limit enforcement.
- Closure path: agent input + durable history → model response with tool call(s) → `RunLoop._execute_tool_calls`/`AgentTool` → tool messages appended to history → next model turn / final result; repeated runs preserve state.
- Why this is / is not agent-owned: model selects tools and next actions from feedback, not a pre-scripted graph; provider adapter and delivery runtime transport and enforce the model's decisions.
- Evidence: `_run_loop.py`, `agents/_default_agent.py`, `_runner.py`, `_handoff.py`, README (links above).
- Basis: explicit documentation plus first-party source control flow.
- Confidence: high.
- Caveats: `DefaultAgent` needs a supplied model configuration; absent credentials/model no inference occurs. A downstream app's independently authored specialized role is not credited as a separate first-party higher VSM function.
- Boundary reachability: one markdown agent with `model=` uses built-in `DefaultAgent.run`, local runtime and `RunLoop`; returned tool results re-enter the same stream without a downstream agent-loop implementation.

## S2 — Coordination

- State: —
- Function: no specific shipped S2 attenuation loop between **distinct** autonomous S1 agents is evidenced from identity, routing and delivery guarantees alone.
- Disturbance / variety regulated: duplicate messages, same-recipient concurrent calls and state races are technical consistency concerns; no concrete cross-agent operational conflict with corrective mutual adjustment is shown.
- Decisive decision or feedback right: select a remedy to inter-S1 collision/oscillation and return that coordination decision to both/affected operating agents.
- Decision owner: not established. `RoutingPolicy`, FIFO and `DefaultAgent._run_lock` enforce deterministic delivery/state consistency; downstream applications may choose coordination policy.
- Supporting / enforcement mechanisms: recipient IDs, publish/subscription, route-key affinity, idempotency keys, direct RPC outcomes, run serialization, distributed host.
- Closure path: send/publish → recipient routing and FIFO processing → terminal delivery/ack; no specific identified interference between autonomous operational units is resolved into changed subsequent agent behavior.
- Why this is / is not agent-owned: a stable mailbox and FIFO are transport; serializing **two calls to the same agent** is not S2 between two independently operating S1 units.
- Evidence: `messaging/_routing.py`, `messaging/_routing_policy.py`, `agents/_default_agent.py`, docs/messaging and docs/harness/distributed-agents (links above).
- Basis: bounded structural negative review.
- Confidence: high.
- Caveats: a custom distributed workflow may build task ownership, negotiation or mutual-exclusion coordination atop AgentLane; that composition requires its own concrete evidence.

### Absence scope

- Surfaces inspected: addressing/subscriptions, deterministic routing, idempotency, FIFO, local run lock, subagent handoff, distributed host and example application wiring.
- Plausible first-party paths checked: multi-agent by topology as S2, stateful affinity as conflict attenuation, same-agent serialization as inter-S1 S2, fan-out/fan-in as coordination.
- Why no material first-party path remains: no distinct agent-pair operational collision and returned remedy is established; consistency and transport mechanisms are not S2-specific by themselves.

## S3 — Inside-and-now control

- State: —
- Function: no first-party autonomous or constructor-closed whole-workgroup current control over commitments/priorities beyond per-agent tool loops and host placement.
- Disturbance / variety regulated: worker lifecycle, per-agent limits, stale instances and message failure are transport/execution concerns.
- Decisive decision or feedback right: review all current S1 commitments and change resource allocation, priorities or interventions on behalf of their whole organization.
- Decision owner: downstream application/controller or user; the bundled lead agent can delegate a subtask but is not shown assessing global commitments and revising whole-workgroup allocations.
- Supporting / enforcement mechanisms: `WorkerAgentRuntimeHost`, per-agent `Runner`, delivery outcomes, tracing and parent-agent subagent handoff.
- Closure path: parent delegates → worker result returns as tool output; this is task decomposition, not a whole-system current-control loop with independent commitments and corrective supervision.
- Why this is / is not agent-owned: giving an agent a tool to spawn/call a specialist is not enough for a distinct S3 resource/commitment decision path.
- Evidence: `docs/harness/distributed-agents.md`, `_run_loop.py`, `_runner.py`, messaging docs.
- Basis: bounded negative review.
- Confidence: medium-high.
- Caveats: a custom lead role with explicit status/reassignment/priority powers can instantiate S3 but is not inherent in the stock runtime.

### Absence scope

- Surfaces inspected: `DefaultAgent` run lifecycle, runtime host worker placement, subagent handoff, runner limits, messaging results and distributed examples.
- Plausible first-party paths checked: parent agent as manager; worker host as S3; task delivery and executor supervision as whole current control.
- Why no material first-party path remains: model-level task selection/delegation and deterministic host deployment do not establish a whole-system view and discretionary cross-S1 resource/priority closure.

## S3* — Complementary audit

- State: —
- Function: no automatically supplied complementary, sufficiently independent audit of an agent's operational claims returns findings into control.
- Disturbance / variety regulated: tracing/metrics/reviewer examples can help check results but are ordinary observability and composed workflow surfaces.
- Decisive decision or feedback right: independently sample operational reality, challenge a claim and feed a corrective finding back to the managing actor.
- Decision owner: external evaluator/application or optional user-authored reviewer; no default independent audit actor is packaged.
- Supporting / enforcement mechanisms: message trace/span IDs, model/tool event streams, optional reviewer pattern and final `RunResult`.
- Closure path: first-party logs/results → downstream consumer; no first-party independent observation → audit judgment → corrective return.
- Why this is / is not agent-owned: instrumentation and a role named reviewer in an application example are not an independent audit with different reality access.
- Evidence: `src/agentlane/tracing`, docs/tracing, docs/harness/distributed-agents and `_run_loop.py`.
- Basis: bounded negative review.
- Confidence: high.
- Caveats: independently grounded evaluation can be constructed with external tools and separate agent roles.

### Absence scope

- Surfaces inspected: trace/metrics, event hooks, tool results, distributed clinical review example, agent roles and external integrations.
- Plausible first-party paths checked: trace as audit, task reviewer as S3*, multiple subagents as independent review, test suite as deployed audit.
- Why no material first-party path remains: no packaged auditor selects claims, obtains a materially independent reality view and returns corrective judgments to current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no built-in outside-and-future adaptation loop develops options and changes present harness capability.
- Disturbance / variety regulated: conversation continuity, changing model providers, new plugins/workers and long-running background activity are extensibility inputs, not future strategy by themselves.
- Decisive decision or feedback right: interpret external/future changes and select a capability adaptation returned to present operations.
- Decision owner: downstream user/developer/operator; the shipped agent handles current tasks, not an independent future-facing environment model.
- Supporting / enforcement mechanisms: state snapshots, persisted conversation, model swaps, task/worker definitions, distributed runtime and extension interfaces.
- Closure path: human/app configuration changes → new runtime state/provider/worker; no model-generated prospective option evaluated and installed into whole present capability.
- Why this is / is not agent-owned: durable memory and infrastructure scaling cannot substitute for S4's external/prospective two-way conversation with S3.
- Evidence: `agents/_default_agent.py`, docs/harness/default-agents, docs/harness/distributed-agents, README.
- Basis: bounded negative review.
- Confidence: high.
- Caveats: AgentLane is a substrate for downstream long-horizon or adaptive applications, which need separate boundary evidence.

### Absence scope

- Surfaces inspected: run-state persistence, provider swapping, markdown roles, agent definition reloading, distributed placement and docs/examples.
- Plausible first-party paths checked: persistent memory as learning, agent replacement as S4 adaptation, tooling extensibility as future capability planning.
- Why no material first-party path remains: all change capability via caller/developer intent, without a first-party prospective sensing/option/return loop.

## S5 — Policy and identity

- State: —
- Function: stable agent address/persona and tool permission gates do not form an ultimate-policy/identity adjudication loop.
- Disturbance / variety regulated: identity persistence, tool access, model selection, task-specific approvals and runner limits.
- Decisive decision or feedback right: decide ultimate organizational values/identity or settle an S3–S4 policy conflict and return governing changes to operation.
- Decision owner: user/app developer specifies agent descriptor, prompt and permissions; no first-party legitimate higher authority deciding such issues is wired.
- Supporting / enforcement mechanisms: `AgentId`, descriptor instructions, persistent `StateStore`, tool permission checks and approval APIs.
- Closure path: external authored descriptor/policy → runner execution bounded by checks; no identity-level matter → authority decision → returned constitutional update.
- Why this is / is not agent-owned: preserving an address across model swaps is durable operational identity, not S5 ultimate identity-policy governance.
- Evidence: `agents/_default_agent.py`, `messaging/_identity.py`, docs/harness/default-agents, docs/harness/tools/permissions.md and README.
- Basis: bounded negative review.
- Confidence: high.
- Caveats: human control/organizational policy may exist around a particular deployment, but is outside this generic harness boundary.

### Absence scope

- Surfaces inspected: identity and state stores, role descriptor, permission tools, caller approvals, handoff and distributed host policy.
- Plausible first-party paths checked: stable address as constitutional identity, human approval as S5, system instructions as policy and model switching as identity closure.
- Why no material first-party path remains: these preserve or constrain task operations, without a first-party identity-policy decision process or parent-authority return.

## Recursion, variety and escalation

Addressable workers and fan-out work can form distinct S1 cells, but the default transport and worker identity do not establish recursively viable meta-organizations. Tool failure, timeout and failed message delivery return task-level signals to the agent/caller; they are not automatically algedonic S3/S5 governance.

## Evidence gaps

- Static source-first review of frozen SHA; no external model/provider-backed E2E, networked host soak test or live downstream clinical scenario.
- Some user-supplied workflow may have stronger multi-agent coordination, audit or control; it is not credited to generic `DefaultAgent` and messaging at this source boundary.
- No automatically spawned independent reviewer was executed; S3* is assessed structurally and negative at this boundary.

## Assessment summary

**Proposed disposition: `included`.** AgentLane ships a genuine first-party model/tool/result S1 loop with durable identity and state (S1=A). Messaging, distributed execution, delegation, FIFO and permission primitives are substantial but do not alone establish the function-specific S2/S3/S3*/S4/S5 closure demanded by Profile 0.2.4. Vector: **A · — · — · — · — · —**.
