---
harness_id: agentling
project_name: Agentling
repository: https://github.com/lunarstack-co/agentling
review_ref: 6673e5833d7d9ba69ec33653b7cfed4e8ae9096a
reviewed_at: 2026-11-10
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

# Agentling

## Review boundary

- System in focus: One library-configured `Agentling.AgentSession` executing a model-directed task with caller-supplied tools and a provider-neutral model adapter, including supported resume and optional skill loading. Multiple unrelated sessions of one `Agent` do not automatically form a higher-recursion shared organization.
- Purpose and identity: Provide a small reusable Python agent engine for repeated model → tool → observation work, typed memory, interruption and streaming, leaving applications free to implement surrounding policy and services.
- Relevant environment: User tasks, model responses, tool failures/results, execution limits, interrupted runs, provider errors, caller-defined tools, skills and memory contexts.
- Standard-distribution boundary: The installed `agentling` Python package, configured with a conforming caller-provided `Model.stream` adapter and approved tools, running through `Agent.start()` / `Agent.run()` and `AgentSession.run()` / `resume()`. The library does not itself ship a live provider adapter or generic server/organizational control plane.
- Credited operating / distribution surfaces: [public API and quickstart](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/README.md), [core loop/session implementation](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/agent.py), [tool execution](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/tools.py), [typed memory](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/memory.py), [optional skills](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/skills.py).
- Adjacent first-party surfaces excluded from ownership: `examples/` application-specific tool sets, provider adapter examples, `tests/` and `agentling.testing` conformance fixtures, CI and package release, project security reporting/maintainer governance. They may corroborate the library's public API but do not supply a standing agent-organization metasystem to the installed package.
- First-party operating / deployment modes considered: Fresh one-off `Agent.run()`, retained `AgentSession` multi-turn/resume, optional caller-defined callbacks/context manager and skills loaded on demand. Concurrent sessions are isolated, not a shared multi-agent control mode.
- Recursion level: One agentic task session and its model-directed operational loop; model-requested tool calls are actions of that S1, not separate viable S1 organizations. A developer application hosting multiple sessions is a separate, unassessed recursion.
- Reviewed revision: `lunarstack-co/agentling@6673e5833d7d9ba69ec33653b7cfed4e8ae9096a` (`main`).
- Observation date: 2026-11-10; source and API inspection, no live provider call.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

`Agent` holds a caller-selected model, tools, skills, instructions and run limits; each `AgentSession` owns memory, an interrupt flag and a copied tool registry. `_loop` streams a model turn, reassembles tool calls, validates/executes them, appends results as `ActionStep`, returns observations to the same model and repeats until a text/final-tool answer or step limit. Failures become tool observations; retry logic applies only to provider failures before output. Several calls from one step can run concurrently if each tool declares itself parallel-safe, but the session itself permits only one active run. [`ARCHITECTURE.md`](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/ARCHITECTURE.md), [`agent.py`](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/agent.py).

`Memory` saves typed task/action/final steps and may be serialized to JSON, but persistent storage or context summarization is application-supplied. Skills append a catalog to instructions; model-called `load_skill` imports configured tools for the next turn. Caller callbacks and external model/provider adapters are extension boundaries, not built-in future planning, independent audit or constitutional governance. The project explicitly says it does not sandbox tools or supply tracing beyond events/callbacks. [`memory.py`](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/memory.py), [`skills.py`](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/skills.py), [`SECURITY.md`](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/SECURITY.md).

## Operational model

The model actor chooses tool calls, arguments and subsequent steps from observations; the library supplies the operational iteration and limits while application authors choose tools, provider, initial instructions, retry and context policy. Nothing in the examined standard package establishes shared resource governance or legitimate collective identity authority for independently operating sessions. Isolated concurrency and input/output hooks support application composition without importing that application's organizational functions into Agentling.

## S1 — Operations

- State: A
- Function: Perform one user-specified task through a repeated model-directed tool/action loop until an answer or bounded stop.
- Disturbance / variety regulated: Changing user instructions, tool output, invalid calls, tool errors, unexpected provider responses and interrupted work.
- Decisive decision or feedback right: Choose the next tool, arguments, iterative response and final content based on task and observations.
- Decision owner: The configured model-backed agent actor; the caller supplies an adapter and permitted tool repertoire but does not select each ordinary tool action in the supported loop.
- Supporting / enforcement mechanisms: `_loop`, argument validation, `Tool.call`, `RetryPolicy`, typed step memory, step limit, `FinalAnswerTool`, interrupt flag and optional callbacks.
- Closure path: User task → model stream → tool calls → first-party tool execution and result/error → memory-rendered next model turn → further action or final answer.
- Boundary reachability: `Agent.run` creates a session, `AgentSession._run_stream` enters `_loop` and executes the model/tool cycle with the public `Model` protocol; the scripted no-key example confirms that the library itself owns the cycle, while a real provider adapter remains caller-supplied.
- Why this is / is not agent-owned: Removing the model leaves validation/iteration machinery without a discretionary choice of next task action; the model's calls are the decisive operational choices.
- Evidence: [`agent.py` session and `_loop`](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/agent.py), [memory-to-model feedback](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/memory.py), [public quickstart](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/README.md#quickstart).
- Basis: structural; a complete first-party control loop is directly implemented.
- Confidence: High for source-level wiring, without measuring real-provider task success.
- Caveats: The package supplies no live model adapter or task-specific actions by default; a consumer must bind a compliant model and tools. Scripted examples are not evidence of universal deployed efficacy.

## S2 — Coordination

- State: —
- Function: Would dampen concrete interference or oscillation among distinct task-producing S1 agents in an integrated organization.
- Disturbance / variety regulated: Potential conflicting actions/commitments among independently operating agents, not merely concurrent calls to tools within one model turn.
- Decisive decision or feedback right: No first-party inter-S1 conflict-specific coordination discretion or closure is supplied for isolated sessions.
- Decision owner: No established S2 owner at the declared session recursion; application authors would have to define joint operations and coordination policy.
- Supporting / enforcement mechanisms: `parallel_tools`, tool-level `parallel_safe`, single-session `_running` guard and isolated per-session memory/tool tables.
- Closure path: The local guard prevents simultaneous reuse of one session and can serialize tool calls, but no result is returned as an inter-agent conflict attenuation decision to multiple S1 units.
- Why this is / is not agent-owned: Serial tool execution is not an S2 decision between operational units; two independent `AgentSession` instances have no shared decision/feedback channel.
- Evidence: [agent/session isolation and parallel tool execution](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/agent.py), [concurrency trust model](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/SECURITY.md#concurrency), [documented scope](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/ARCHITECTURE.md#what-it-doesnt-do).
- Basis: structural bounded absence.
- Confidence: High at the single-session boundary.
- Caveats: A higher-recursion developer application may coordinate several sessions; that is not shipped as an Agentling coordination relation.

### Absence scope

- Surfaces inspected: `Agent`, `AgentSession`, parallel tool scheduling, session concurrency guard, memory, tool/session extension APIs and documented architecture/security boundaries.
- Plausible first-party paths checked: Competing tool calls, parallel sessions, shared memory, cross-agent messaging/negotiation, collision decisions and return into each S1's future actions.
- Why no material first-party path remains: The only specific concurrency safeguards operate inside one session or isolate sessions; no distinct S1 collision, S2-specific attenuation choice and returned multi-unit feedback path is packaged.

## S3 — Inside-and-now control

- State: —
- Function: Would govern current aggregate operational commitments, resource bargaining and interventions on behalf of a whole comprising multiple S1 units.
- Disturbance / variety regulated: Conflicting resource demands, priorities and live commitments across a multi-unit task organization.
- Decisive decision or feedback right: No actor with a whole-system current view selects or revises shared commitments; session limits are caller-chosen runtime settings.
- Decision owner: Application developer/caller sets model, permitted tools, maximum steps, timeouts and interruption; deterministic Agentling runtime enforces those inputs.
- Supporting / enforcement mechanisms: Step limit, timeouts, retry, interruption, per-session state, `step_callbacks` and events.
- Closure path: A timeout or step limit changes one session's immediate continuation, without a whole-system resource/priority judgment over distinct S1s or parent returned current-control decision.
- Why this is / is not agent-owned: The model directs its own S1 actions but does not receive a system-wide commitments view or discretionary authority to redistribute shared capacity through this package.
- Evidence: [`Agent` configuration and session boundary](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/agent.py), [public settings reference](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/REFERENCE.md#agent), [step-limit behavior](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/ARCHITECTURE.md#the-loop).
- Basis: structural bounded absence.
- Confidence: High.
- Caveats: Per-session runtime governance is real but does not establish current-control authority at a multi-unit VSM recursion.

### Absence scope

- Surfaces inspected: Agent constructor, session API and loop, callbacks, tool concurrency controls, interrupt/retry mechanisms and public reference.
- Plausible first-party paths checked: Shared ongoing operational portfolio, capacity/priority bargaining, autonomous or parent current-control decision and returned cross-unit intervention.
- Why no material first-party path remains: Inspected shipped controls are local execution limits and observer hooks, not a whole-current S3 decision and subsequent organization-wide closure.

## S3* — Complementary audit

- State: —
- Function: Would use a sufficiently independent alternative view of operational reality to challenge the normal agent's success claims and return audit findings into control.
- Disturbance / variety regulated: Incorrect tool/answer claims or omitted operational evidence that ordinary same-loop reporting could fail to reveal.
- Decisive decision or feedback right: The installed package has no complementary audit judgment about a run's substantive outcome; callbacks and model-adapter conformance fixtures observe ordinary execution.
- Decision owner: No shipped S3* actor; an application developer may arrange external evaluators separately.
- Supporting / enforcement mechanisms: Typed step log, event stream, `step_callbacks`, `agentling.testing.check_model` and test fixture recorder.
- Closure path: Events and saved actions can be inspected by an external consumer, but there is no first-party independent audit finding returned to alter task commitments/control.
- Why this is / is not agent-owned: The producing session records its own tool execution; recorded trace access is not an independent, claim-relative audit decision.
- Evidence: [events and callbacks](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/ARCHITECTURE.md#events), [testing API is an adapter checker](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/REFERENCE.md#agentlingtesting), [typed memory](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/memory.py).
- Basis: structural bounded absence.
- Confidence: High.
- Caveats: A consumer can build a separate validator using the event stream, but it cannot donate S3* ownership to the installed library.

### Absence scope

- Surfaces inspected: `events.py`, `memory.py`, `testing.py`, `step_callbacks`, the loop's ordinary tool-error correction and conformance tests.
- Plausible first-party paths checked: Independent sampled replay, alternate direct-artifact inspection, audit-specific model/judge, authority over audit verdict and returned corrective S3 effect.
- Why no material first-party path remains: First-party diagnostics describe/validate the producer or adapter path and do not establish an independent operational-evidence judgment with actionable returned findings.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would sense relevant external/future changes, develop prospective adaptation options and return them into present agent capability or S3.
- Disturbance / variety regulated: New tasks, tools, providers, threats and opportunities requiring durable future-oriented changes, as distinct from a current user's prompt.
- Decisive decision or feedback right: Model may select present tools/skills and respond to errors, but no shipped prospective environment-assessment or capability-change judgment path is established.
- Decision owner: The developer supplies and may update tools, provider, prompt and context-management policy; the model selects only among currently exposed options.
- Supporting / enforcement mechanisms: On-demand `load_skill`, dynamic per-session `add_tools`, `context_manager`, memory JSON and tool-error feedback.
- Closure path: Loading a configured skill changes current tools for the next turn, but does not evaluate an outside-and-then opportunity and durably select future organizational capability.
- Why this is / is not agent-owned: Immediate reactive tool selection or optional skill loading is current S1 adaptation to the task, not an independent prospective S4 loop.
- Evidence: [skill loader and explicit developer configuration](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/agent.py), [skill file loading](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/skills.py), [documented architecture limits](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/ARCHITECTURE.md).
- Basis: structural bounded absence.
- Confidence: Medium-high.
- Caveats: A configured skill can direct future-facing research, but a particular caller-authored skill is not an included first-party standing S4 function.

### Absence scope

- Surfaces inspected: Skills, dynamic tool management, context manager, typed memory, default instructions, examples and core iteration.
- Plausible first-party paths checked: Future/outside sensing, alternative capability generation, selection/authorization, durability and return into current agent capacity or multi-unit control.
- Why no material first-party path remains: The package exposes immediate reactive/compositional primitives with no installed externally prospective judgment/commitment path.

## S5 — Policy and identity

- State: —
- Function: Would resolve a legitimate ultimate identity or constitutional policy matter and return the authoritative decision to govern subsequent operation.
- Disturbance / variety regulated: Conflicts over the enduring purpose, legitimacy and ultimate policy of the agent's operating organization.
- Decisive decision or feedback right: A caller selects the system instructions, permitted tools and trust boundaries; there is no first-party ultimate-policy deliberation or adjudication that an agent or legitimate parent closes.
- Decision owner: External application/user authors static instructions and privileges; runtime simply applies them to each model turn.
- Supporting / enforcement mechanisms: `Agent.instructions`, skill catalog, registered tools, argument validation and `SECURITY.md` trust guidance.
- Closure path: A caller can construct a different `Agent` or change its configuration before a run, but this is external setup, not a shipped identity/policy question → legitimate decision → authoritative returned operating rule cycle.
- Why this is / is not agent-owned: The model can act within instructions but cannot decide the legitimate identity or ultimate authority behind them in a first-party package-supported mode.
- Evidence: [agent construction and instructions](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/src/agentling/agent.py), [security trust boundary](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/SECURITY.md), [public configuration reference](https://github.com/lunarstack-co/agentling/blob/6673e5833d7d9ba69ec33653b7cfed4e8ae9096a/REFERENCE.md).
- Basis: structural bounded absence.
- Confidence: High at the declared library/session boundary.
- Caveats: External applications or maintainers may have legitimate policy authority over their own organizations; that governance is outside this installed runtime.

### Absence scope

- Surfaces inspected: Agent configuration/instructions, dynamic skill/tool options, session loop, security and contributor documentation.
- Plausible first-party paths checked: Agent or parent ultimate-policy proposal, legitimacy adjudication, authoritative policy update and returned continued operation at the declared recursion.
- Why no material first-party path remains: Only external initial configuration and ordinary execution safety/settings are shipped, with no first-party identity-level decision/return loop.

## Distributed OSS parent arrangement

The upstream project's maintainer, release and security-reporting processes govern Agentling development, not a user's installed `AgentSession`. Independent users can instantiate the library without any common operating authority; the source repository's maintainers therefore do not supply a parent S3/S4/S5 return path at the assessed session boundary.

## Self-hosted and non-human modes

All observed sessions are locally instantiated with caller-supplied model and tools. The model-backed execution path supplies S1=A; optional callbacks, operator interruption and per-session tools do not form independent parent-governed S3/S4/S5 modes. There is no claimed all-agent shared autonomous metasystem.

## Recursion

Individual tools are operational actions, not separate viable systems; different sessions have separate memory and no shipped common collective management. A developer-built multi-agent service could be a higher recursion, requiring its own declared boundary and new evidence.

## Variety and escalation

Task and tool variation reach the model through typed observations, while deterministic validation, timeouts, retries and step limits attenuate error/loop variety. A tool failure is returned as a new observation, not silently graded as independent audit. The caller must manage secret exposure, prompt-injection risk, tool trust and external organizational escalation. An interrupt ends a resumable local run; it is not by itself an algedonic metasystem path.

## Evidence gaps

- Static source review of the pinned package, docs and tests; no live paid-model/provider task run or deployment capability benchmarking.
- The public `Model` interface is caller-provided, so concrete application-level organization, optional plugins and custom model adapters are outside the credited boundary.
- A different higher-recursion system integrating several Agentling sessions may establish S2/S3/S3*/S4/S5, but no such consumer is part of this assessment.
