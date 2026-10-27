---
harness_id: swarms-rust
project_name: Swarms Rust
repository: https://github.com/The-Swarm-Corporation/swarms-rs
review_ref: ee1e74cb6e2c94775db88dddb311f2235e3fe9e3
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Swarms Rust

## Review boundary

- System in focus: one user-instantiated multi-agent runtime using the published first-party Rust `swarms-rs` library and its `SwarmsAgent` operating units, optionally configured as concurrent, sequential, graph or rearranged workflows; not the Python `swarms` package or the vendor's organization.
- Purpose and identity: supply model-backed Rust agents with tools, memory and handoff capability, and compose their operating work in reusable swarm workflows.
- Relevant environment: externally hosted model responses, callable Rust/MCP tools, errors and retries, incoming tasks, concurrent agent responses and conditional graph results.
- Standard-distribution boundary: `swarms-rs/src/agent/`, `swarms-rs/src/structs/`, the published Cargo crate and first-party workflow configurations. User-supplied tools/model endpoints are environmental dependencies, not evidence of an internally owned metasystem.
- Credited operating / distribution surfaces: `SwarmsAgent` model/tool loop, sub-agent delegation and handoff, `ConcurrentWorkflow` task re-entrancy guard, `DAGWorkflow` conditional fan-out/join and once-only target claim, `SequentialWorkflow`, `AgentRearrange`, `SwarmRouter` configuration dispatch, conversation and persistence.
- Adjacent first-party surfaces excluded from ownership: the separately assessed Python Swarms implementation, developer README marketing claims of enterprise viability or scale, third-party LLM services and MCP servers, application-specific orchestration the user could write on top, CI/tests, and future roadmap.
- First-party operating/deployment modes considered: direct autonomous `SwarmsAgent`, model-selected agent-to-agent handoff, configured parallel and sequential execution, configured conditional DAG with parallel joins, and router/rearrange modes. `DAGWorkflow` and the direct-agent handoff are not presumed to share a single dynamic director.
- Recursion level: one configured library application/swarm containing operating agent instances; multiple unrelated installations are not one shared viable system.
- Reviewed revision: `ee1e74cb6e2c94775db88dddb311f2235e3fe9e3`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Rust crate implements a concrete model-backed agent. Its `Agent::run` receives a task, optionally constructs a plan, repeatedly sends conversation and tool definitions to a model, calls selected tools, returns their results to later iterations, retries failed completions and supports a task-evaluator completion signal. `add_sub_agent` exposes an operating agent as an LLM-selected tool; `add_handoff` permits a selected transfer of the current task and accumulated conversation. These are operating decisions inside the agent boundary, not a guarantee that the enclosing swarm has a model director.

The library also offers distinct first-party workflows. `ConcurrentWorkflow` rejects a second concurrently active invocation bearing the same task key via `DashSet`, launches configured agent workers concurrently, then collects their outputs. `DAGWorkflow` uses typed graph edges, conditional output filters, an incoming-edge resolution map and a shared atomic `started` set, so concurrent predecessors can contribute to one join without executing the downstream agent twice. This is bounded technical inter-unit disturbance attenuation. `SwarmRouter` is an enum selecting a developer-specified sequential, concurrent or rearranged topology, not a learning or model-deciding policy.

Pinned primary evidence: [README](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/README.md), [agent runtime](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/agent/swarms_agent.rs), [delegation tools](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/agent/delegation.rs), [concurrent workflow](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/concurrent_workflow.rs), [graph workflow](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/graph_workflow.rs), [router](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/swarms_router.rs).

## Operational model

An agent chooses model-generated tool calls or handoff, observes returned text and tool results, and changes its next prompt/action. Multiple such S1 agents can be instantiated in graph or concurrent workflows. The graph join and active-task guards prevent concrete inter-agent races in the reached shipped modes, but workflow topology, timeouts and evaluation do not demonstrate an independently deciding whole-swarm controller. No runtime operator for self-directed future environmental intelligence or ultimate identity policy appears in the inspected library surface.

## S1 — Operations

- State: A
- Function: individually model-directed agent execution of tasks, including tool use, feedback-contingent continuation and optional peer-agent delegation.
- Disturbance / variety regulated: unknown task subtasks, model/tool errors, new tool outputs, incomplete task-evaluator feedback and provider failures.
- Decisive decision or feedback right: choose tool/agent operations and subsequent task steps from model replies; continue, hand off or finish as new results arrive.
- Decision owner: the invoked `SwarmsAgent` model-backed loop within one operational agent, using externally supplied LLM completion but first-party loop and tools.
- Supporting / enforcement mechanisms: `SwarmsAgentBuilder`, tool registration, `chat`, `Agent::run`, `task_evaluator`, retry and max-loop settings, `SubAgentTool` and `HandoffTool`.
- Closure path: user task → model completion and tool/delegation choice → executed tool/child result → saved conversation and new agent prompt → next action or completion.
- Boundary reachability: README shows actual builder/use of `SwarmsAgent` through the published crate; `Agent::run` calls the loop, while opt-in first-party builder methods register handoff/subagent tools in the model-visible tool set.
- Why this is / is not agent-owned: model choice determines which operation is taken in response to the task, while fixed retry counters and memory only bound it.
- Evidence: [run loop](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/agent/swarms_agent.rs), [delegation implementation](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/agent/delegation.rs), [README quickstart](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/README.md).
- Basis: structural and documented.
- Confidence: high on static source architecture.
- Caveats: agent action success and reasoning quality require a live configured provider; this review executed no paid/model-dependent task.

## S2 — Coordination

- State: C
- Function: bounded attenuation of concurrent operating-unit interference when multiple independently executing Rust agents feed a common graph join or two invocations contend over the same concurrent-workflow task key.
- Distinct S1 units: separately invoked `Agent` workers in a configured `DAGWorkflow` graph, or two concurrently initiated operations of the same `ConcurrentWorkflow` instance.
- Inter-S1 disturbance: independent predecessor branches resolve concurrently and might start the same downstream worker more than once; duplicate active task runs might overwrite or intermingle their task-specific shared conversation.
- Attenuating coordination relation: graph incoming-edge resolution waits for all predecessor decisions, aggregates accepted outputs, and atomically claims each target using `DashSet::insert`; concurrent workflow's task-level `DashSet` denies duplicate in-flight same-key runs, released when the run exits.
- Feedback into subsequent S1 behaviour: a downstream agent only receives resolved, accepted upstream inputs and starts once, or does not run when all edges are skipped; a duplicate workflow invocation is rejected before it launches an interfering set of agents.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the claim rests narrowly on actual collision-prevention and concurrent fan-in resolution, not on the mere presence of graph edges, router names, parallel execution or conversation history.
- Disturbance / variety regulated: simultaneous predecessor completions, skipped/error predecessor branches, fan-in duplicate launch races and same-task concurrent invocation.
- Decisive decision or feedback right: enforce a single downstream start after incoming-branch resolution and reject a second active run of the same task key.
- Decision owner: deterministic first-party graph/workflow concurrency gates, hence `C` rather than an autonomous S2 model owner.
- Supporting / enforcement mechanisms: `DAGWorkflow::execute_workflow`, `execute_node_tracked`, `propagate`, `edge_tracker`, `started`; `ConcurrentWorkflow::run` and `RunningTask` guard.
- Closure path: parallel operating outputs or contending invocation → first-party graph/task key gate → joined accepted input, skipped downstream work or explicit duplicate error → bounded later agent execution.
- Boundary reachability: `execute_workflow` calls `execute_node_tracked` and `propagate` on the published first-party graph type; `ConcurrentWorkflow::run` enforces the task gate on the documented direct run method.
- Why this is / is not agent-owned: collision and launch grants are fixed Rust concurrency decisions, not model-authored coordination rules.
- Evidence: [graph join and atomic claim](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/graph_workflow.rs), [duplicate-task guard](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/concurrent_workflow.rs).
- Basis: structural.
- Confidence: medium-high for these narrow modes.
- Caveats: no global scheduling or shared-resource arbitration across unrelated swarm instances; graph joins and task guards do not prove resource-level coordination for arbitrary side effects.

## S3 — Inside-and-now control

- State: —
- Function: no independently evidenced controller regulating the present whole-swarm operating commitments based on a comprehensive status view.
- Disturbance / variety regulated: uneven worker progress, partial failures and changing priority could require adaptive whole-team direction, but the inspected shipped topology instead follows configured steps and predetermined graph edges.
- Decisive decision or feedback right: `SwarmRouter` selects a preconfigured variant at construction; graph branches are configured functions; local LLM delegation only chooses a child's task within one operating agent.
- Decision owner: application author and deterministic workflow/router for whole-application topology; individual model agents own their own S1 actions.
- Supporting / enforcement mechanisms: router enum dispatch, graph edge functions, rearrange text flow, concurrent and sequential workflow loops, task-evaluator inside the individual agent.
- Closure path: returned agent results can feed another preconfigured step, but no evidence that a model or other distinct function sees the whole current swarm and revises global allocations/controls on result feedback.
- Whole-system current view: graph execution results and shared conversation are accumulated by orchestration code; no separate whole-swarm supervisory interpretation/choice found.
- Current-control decision scope: graph/router/rearrange schedule is operator-defined, while handoff is agent-local; neither was elevated to whole-system governance.
- Boundary reachability: published workflow API is reachable; its reachable paths are deterministic dispatch/conditions, not a full S3 controller.
- Why this is / is not agent-owned: model-selected `add_handoff` transfers one task, and model tool choices remain operating-level; they do not prove a distinct supervisor regulating all worker commitments.
- Evidence: [router dispatch](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/swarms_router.rs), [flow execution](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/rearrange.rs), [DAG execution](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/graph_workflow.rs), [handoff](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/agent/swarms_agent.rs).
- Basis: structural bounded absence.
- Confidence: medium.
- Caveats: downstream users can author their own supervisor using this general-purpose library; an unobserved custom application is not part of the shipped assessed system.

### Absence scope

- Surfaces inspected: router config, sequential/concurrent/graph/rearrange workflows, model agent loop, subagent and handoff facilities, state/conversation and error handling.
- Plausible first-party paths checked: `SwarmRouter::inner_run`, DAG condition/transform, `AgentRearrange::run_internal`, `SwarmsAgent::run_handoff` and built-in task evaluator.
- Why no material first-party path remains: each candidate chooses a fixed configured route, protects concurrency or acts within one agent's task; none closes a first-party whole-swarm adaptive current-control loop.

## S3* — Complementary audit

- State: —
- Function: no independent complementary sampling of operational truth against ordinary producer reporting established for the installed Rust swarm.
- Disturbance / variety regulated: potentially false or incomplete agent output and hidden failures.
- Decisive decision or feedback right: task evaluator and downstream agents may reconsider production output, but the evaluator receives same agent-local context and is part of the normal work loop.
- Decision owner: producing operating agent and ordinary application workflow; no distinct audit owner is evidenced.
- Supporting / enforcement mechanisms: local `task_evaluator` tool, graph error/timeout reporting, per-agent logs, result persistence and general tests.
- Closure path: evaluator feedback can prompt another loop of the producing agent; an independent observation/audit finding with a separate corrective authority is not shown.
- Why this is / is not agent-owned: a model reporting its own task completion or downstream summarization is ordinary operating QA, not independent complementary S3* inspection.
- Evidence: [task-evaluator implementation](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/agent/swarms_agent.rs), [graph result/error handling](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/graph_workflow.rs).
- Basis: structural bounded absence.
- Confidence: medium.
- Caveats: an external observer could audit application effects, but none is installed as a first-party alternative access channel here.

### Absence scope

- Surfaces inspected: agent evaluator, external tool result feeding, graph stored results and execution errors, workflow metadata and logging, repository tests.
- Plausible first-party paths checked: evaluator tool's completeness verdict, graph timeout paths, consumer-agent downstream review and logging/telemetry.
- Why no material first-party path remains: these mechanisms are in the normal production path or code testing, without separately controlled direct-source verification plus a corrective audit return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped function prospectively sensing external change and steering future capabilities of the Rust swarm itself.
- Disturbance / variety regulated: changing model availability, new task domains, tool ecosystems and operational threats might require strategic changes.
- Decisive decision or feedback right: model/tool/provider, flow configuration and future crate upgrades are chosen by an external application author or developer, not by an in-scope S4 agent.
- Decision owner: users/developers of host applications and package maintainers outside this runtime.
- Supporting / enforcement mechanisms: extensible model/tool interfaces, optional external MCP servers, configurable prompts and runtime state.
- Closure path: model tools may answer a user's research question as an operating task; no environmental scan → durable future-system option → current-control implementation loop for the swarm is established.
- Why this is / is not agent-owned: general ability to ask an LLM for plans or research does not assign it ongoing prospective adaptation authority over this runtime.
- Evidence: [agent builder and model/tool interfaces](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/agent/swarms_agent.rs), [runtime router configuration](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/swarms_router.rs).
- Basis: structural bounded absence.
- Confidence: medium.
- Caveats: application-specific model research or strategy could be built by adopters; no such in-boundary policy feed was demonstrated.

### Absence scope

- Surfaces inspected: agent planner and memory, MCP tool integration, provider wrappers, router/graph/configuration, docs, examples and workflow persistence.
- Plausible first-party paths checked: planning prompts, arbitrary external-tool access, persistence and model-provider configuration.
- Why no material first-party path remains: these enable present operating action or manual extensibility, not a designated self-adaptive prospective function with a durable return to system policy/capability.

## S5 — Policy and identity

- State: —
- Function: no established ultimate identity/policy-setting authority inside one runtime swarm as distinguished from ordinary developer configuration.
- Disturbance / variety regulated: conflicts over ultimate purposes or legitimate authority for changing swarm identity would require policy adjudication.
- Decisive decision or feedback right: builder-provided instructions/rules define ordinary task constraints, but no in-runtime purpose dispute is routed to a recognized policy owner and returned as governing charter.
- Decision owner: application author/configurator or package maintainers outside the assessed operating instance.
- Supporting / enforcement mechanisms: `system_prompt`, builder settings, flow rules, agent handoff and stop conditions.
- Closure path: configuration is read and enforced during tasks; no identity-level challenge → legitimate policy judgment → binding change to subsequent operation is documented.
- Why this is / is not agent-owned: static initial rules and human ownership of source code are not automatic evidence of S5 ownership in this recursion.
- Evidence: [builder/prompt and handoff configuration](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/agent/swarms_agent.rs), [rearrange rules](https://github.com/The-Swarm-Corporation/swarms-rs/blob/ee1e74cb6e2c94775db88dddb311f2235e3fe9e3/swarms-rs/src/structs/rearrange.rs).
- Basis: structural bounded absence.
- Confidence: medium.
- Caveats: organizational policies governing the vendor or adopter are different recursion levels and are not imported.

### Absence scope

- Surfaces inspected: builder/system prompts, flow rules, handoff, stop/evaluator semantics, model provider setup, docs and repository governance surfaces.
- Plausible first-party paths checked: user-defined agent identity, rules injected into task conversation, API/tool permissions and publisher-level project governance.
- Why no material first-party path remains: these mechanisms configure/limit execution or govern software contributions; none supplies a separate legitimate internal identity-policy loop for the running swarm.

## Distributed OSS parent arrangement

The public Rust library has maintainers and Cargo packaging; neither creates a runtime S3–S5 parent spanning all users' independently configured swarms. Its relationship to the vendor's Python Swarms is a project adjacency, not evidence transferable across language implementations. Provider models and host applications are dependencies/parents only within the precise authority they actually exercise.

## Self-hosted and non-human modes

The crate runs inside a Rust process and calls configured hosted/provider LLM services. No cloud vendor service is required for its Rust orchestration logic, but autonomous S1 actions still need configured model completion. Parallel agent operations and deterministic graph gates are reachable in the first-party crate; this review does not infer production-scale robustness from README promotion.

## Recursion

Each model-backed `SwarmsAgent` may be an operating S1 unit inside one workflow. A sub-agent or handoff target receiving a task is not therefore a viable organization with its own proven full metasystem. A host application may form a larger recursive viable system, but its governance must be evidenced separately.

## Variety and escalation

Tool/evaluator outcomes change local next actions; retries and stop limits bound individual agent variety. The graph attenuates concurrent branch ambiguity through join/skip/once-only admission and per-task active-run gates; observed errors return to callers or logs. Neither these mechanisms nor externally injected rules constitute an algedonic S5 channel or independent S3* audit.

## Evidence gaps

- Pinned first-party Rust code and docs were inspected statically; no external LLM/API execution or independent quality benchmark was performed. `cargo` is unavailable in the inspection environment, so native Rust tests were not executed.
- S2 `C` is deliberately limited to published graph fan-in and active-task races, not general resource management or global scheduling.
- No model-led whole-swarm control was shown in configured router, graph, or rearrange modes; model-directed one-task handoffs remain S1.
- No first-party independent complementary audit, prospective self-adaptation or ultimate policy-decision loop was established in this recursion.
