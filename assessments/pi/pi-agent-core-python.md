---
harness_id: pi-agent-core-python
project_name: pi-agent-core (Python)
repository: https://github.com/Huvinesh-Rajendran-12/pi-agent-core
review_ref: f541b859d4a8e6d1f7415a671024bd4e22b1025d
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

# pi-agent-core (Python)

## Review boundary

- System in focus: the Python pi-agent-core package; an independent Python port, not the external TypeScript pi-mono distribution.
- Purpose and identity: provide a stateful provider-neutral model/tool execution loop.
- Relevant environment: caller tasks and tools, model streams, tool failures, cancellation and queued user messages.
- Standard-distribution boundary: installed src/pi_agent_core modules, including optional Anthropic and SSE proxy transport adapters.
- Credited operating / distribution surfaces: Agent.prompt/continue_, agent_loop and tool-result return; first-party optional stream_anthropic adapter.
- Adjacent first-party surfaces excluded from ownership: tests, development CLAUDE.md, package-maintenance workflow and README illustrative fake stream. External TypeScript predecessor and proxy server are separate systems.
- First-party operating / deployment modes considered: stateful Agent and direct async loop API, optional Anthropic adapter or caller StreamFn/SSE proxy, steering/follow-up queues and abort/reset.
- Recursion level: one configured agent conversation with tool feedback.
- Reviewed revision: `f541b859d4a8e6d1f7415a671024bd4e22b1025d`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Agent wraps an async generator loop, stores messages and pending calls, and emits lifecycle events. The loop streams the assistant response, executes each model-selected tool, records ToolResultMessage and asks the model again until it has no tools or pending messages. A steering queue can skip remaining tool calls and return an instruction to the next turn; follow-up messages start further turns. Agent enforces one active prompt per instance. Host setters configure model, prompt and tools. transform_context and convert_to_llm callbacks process context at the request boundary. The optional Anthropic adapter implements actual model streaming; the proxy is an SSE client, not a first-party server or supervisor. State is in memory; no autonomous fleet, audit or strategic governance service is packaged.

## Operational model

The model-driven conversation is S1: it makes operational tool/answer decisions and receives results. Host code supplies tools, credentials and application instructions; that configuration is not agent-owned governance. The shipped model adapter makes a usable first-party loop reachable without implementing a new organizational actor. Steering is task-local human/application input, not evidence of a whole-system parent metasystem.

## S1 — Operations

- State: A
- Function: complete caller tasks through repeated model/tool decisions.
- Disturbance / variety regulated: intermediate tool observations, missing tools/errors and changing user instructions.
- Decisive decision or feedback right: choose actions/arguments and the next response after returned tool results.
- Decision owner: model-backed agent within the first-party loop.
- Supporting / enforcement mechanisms: Agent state, event streams, schema/message normalization, sequential tool execution and provider transport.
- Closure path: _run_loop appends tool results to current_context.messages, then streams a further assistant response; follow-ups and steering are incorporated before subsequent turns.
- Boundary reachability: Agent.prompt invokes this loop; README documents stream_anthropic as a built-in optional StreamFn. No outside coding-agent harness is credited.
- Why this is / is not agent-owned: without model action selection the runtime only transports messages and invokes already-chosen tools.
- Evidence: [src/pi_agent_core/agent.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent.py); [src/pi_agent_core/agent_loop.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent_loop.py); [src/pi_agent_core/types.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/types.py); [README.md](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Static implementation evidence; no live model/provider execution or competence claim.

## S2 — Coordination

- State: —
- Function: no function-specific inter-S1 coordination is supplied.
- Disturbance / variety regulated: one conversation's queued messages and serial tool calls.
- Decisive decision or feedback right: no cross-unit conflict/oscillation response identified.
- Decision owner: caller controls queue modes; model controls the local task.
- Supporting / enforcement mechanisms: steering/follow-up deques and already-processing prompt guard.
- Closure path: queued messages enter the same S1 context; no separate cross-unit adjustment path.
- Why this is / is not agent-owned: single-instance serialization and generic event subscriptions are not S2.
- Evidence: [src/pi_agent_core/agent.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent.py); [src/pi_agent_core/agent_loop.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent_loop.py); [src/pi_agent_core/types.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/types.py); [README.md](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Applications may create multiple Agents, but must add coordination decision content.

### Absence scope

- Surfaces inspected: Complete package module inventory, Agent queues/prompt guard, loop tool sequencing, types and supported README modes.
- Plausible first-party paths checked: Concurrent prompt rejection, steering-induced skipped calls, follow-up ordering and event callbacks.
- Why no material first-party path remains: No first-party distinct-unit organization, specific inter-unit disturbance and function-specific corrective return is shipped; generic queuing is not an S2 constructor.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system inside-and-now regulator is supplied.
- Disturbance / variety regulated: individual active turns, cancellation and context state.
- Decisive decision or feedback right: host chooses abort, model/tool settings and steering messages; no whole-system allocation/accountability process.
- Decision owner: caller/application for intervention, task agent for operational decisions.
- Supporting / enforcement mechanisms: abort event, wait_for_idle, state setters and request options.
- Closure path: abort stops one loop and steering changes its next turn; neither constitutes whole-system resource/commitment governance.
- Why this is / is not agent-owned: an imperative control API does not install a supervisory decision owner.
- Evidence: [src/pi_agent_core/agent.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent.py); [src/pi_agent_core/agent_loop.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent_loop.py); [src/pi_agent_core/types.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/types.py); [README.md](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: No P state from ordinary user steering or cancellation.

### Absence scope

- Surfaces inspected: Agent control/setter APIs, state/config types, loop and adapter contracts.
- Plausible first-party paths checked: Abort/reset, pending tool visibility, queue steering and thinking/token request options.
- Why no material first-party path remains: These are local execution/host controls; no first-party whole-system view plus shared resources/commitments decision and returned supervisory closure exists.

## S3* — Complementary audit

- State: —
- Function: no complementary independent operational audit is supplied.
- Disturbance / variety regulated: tool exceptions and model stream events are ordinary feedback.
- Decisive decision or feedback right: no independent audit judgment/findings-to-control right identified.
- Decision owner: task agent reads its own tool outcomes; application subscribes to events.
- Supporting / enforcement mechanisms: tool-execution events, is_error messages and adapter usage data.
- Closure path: errors re-enter ordinary task context; event observers have no shipped audit mandate or correction process.
- Why this is / is not agent-owned: the same production trace does not provide complementary independent access.
- Evidence: [src/pi_agent_core/agent_loop.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent_loop.py); [src/pi_agent_core/types.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/types.py); [src/pi_agent_core/proxy.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/proxy.py); [tests/test_agent_loop.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/tests/test_agent_loop.py).
- Basis: structural.
- Confidence: high.
- Caveats: Developer tests/fake providers corroborate loop behavior but are not product auditors.

### Absence scope

- Surfaces inspected: Runtime event subscriptions, tool execution/error return, adapters and package/test separation.
- Plausible first-party paths checked: Subscriber inspection, tool-result validation and fake-provider tests.
- Why no material first-party path remains: No audit-specific independent actor/access/judgment with findings returning to control is packaged; custom listeners are generic extensibility.

## S4 — Outside-and-then intelligence

- State: —
- Function: no outside-and-then capability adaptation loop is supplied.
- Disturbance / variety regulated: current request context and conversation continuity.
- Decisive decision or feedback right: no future/environment distinction-to-adaptation decision is shipped.
- Decision owner: caller selects model/tools/context transforms; model solves the task.
- Supporting / enforcement mechanisms: transform_context, message replacement/continuation and provider selection.
- Closure path: transformed messages affect a current model call, without an adaptation-option adoption loop into capability.
- Why this is / is not agent-owned: context transformation and follow-up prompts are operational extensibility, not prospective S4.
- Evidence: [src/pi_agent_core/agent.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent.py); [src/pi_agent_core/agent_loop.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent_loop.py); [src/pi_agent_core/types.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/types.py); [README.md](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: No inference from the ability to implement a custom research agent.

### Absence scope

- Surfaces inspected: Context/config callbacks, all packaged module roles, model/tool setters, continuation and README modes.
- Plausible first-party paths checked: Context summarization hook, retained messages, changed tools/model and follow-up tasks.
- Why no material first-party path remains: The shipped package has no environmental/future model, adaptation-option generation and acceptance into current capability, nor a complete parent adaptation path.

## S5 — Policy and identity

- State: —
- Function: no identity or ultimate-policy closure is supplied.
- Disturbance / variety regulated: configured system instructions and local task steering.
- Decisive decision or feedback right: set_system_prompt is a setter, not issue-to-authority policy adjudication.
- Decision owner: host/developer supplies instructions and allowed tools.
- Supporting / enforcement mechanisms: AgentState and configuration/message transport.
- Closure path: new configuration is used on later calls, without a shipped identity-level referral and authoritative decision-return process.
- Why this is / is not agent-owned: obeying a prompt or human message does not establish ultimate policy ownership.
- Evidence: [src/pi_agent_core/agent.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent.py); [src/pi_agent_core/agent_loop.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/agent_loop.py); [src/pi_agent_core/types.py](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/src/pi_agent_core/types.py); [README.md](https://github.com/Huvinesh-Rajendran-12/pi-agent-core/blob/f541b859d4a8e6d1f7415a671024bd4e22b1025d/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: A legitimate user can control the application without a function-specific S5 process being exposed.

### Absence scope

- Surfaces inspected: Prompt/model/tool setters, config types, steering paths, adapter boundaries and README supported usage.
- Plausible first-party paths checked: Prompt replacement, user steering and host application authority.
- Why no material first-party path remains: No identity/ultimate-policy matter is routed to an authoritative parent/internal owner and returned as governing policy by this distribution; imperative configuration alone is insufficient.

## Distributed OSS parent arrangement

Maintainer development authority is adjacent to installed agent executions. No project-recursion parent governance is inferred from the upstream port or contributors.

## Self-hosted and non-human modes

Caller-hosted SDK use, optional provider/proxy and local steering were considered. No qualifying S3/S4/S5 parent mode or non-human organization is packaged.

## Recursion

No recursive viable operational organization is supplied. Multiple caller-created instances are not evidence of recursion.

## Variety and escalation

Tool errors, streaming messages, cancellation and queued steering preserve operational feedback. Request transport, callbacks and error/status events do not inherit organizational authority.

## Evidence gaps

Source-only assessment; no live provider or integration tests were executed. Caller-written tools/StreamFn/transform policies and the external proxy server are outside the evidence boundary. The narrow complete package offers no concrete unresolved shipped higher-function path; negatives are bounded to this distribution.
