---
harness_id: blades
project_name: Blades
repository: https://github.com/go-kratos/blades
review_ref: b78fec59029d11e02c135ea10da8986ed006521f
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Blades

## Review boundary

- System in focus: One installed first-party Blades Go agent application, including its `Agent.Run`/Runner invocation, per-invocation model-to-tool feedback, optional session/middleware/skills/memory, and packaged `flow` and `graph` composition modes. The operating recursion is the compiled agent application, not the maintainer team or an external collection of users and agent vendors.
- Purpose and identity: Execute current multimodal user/developer tasks using configured models and tools, preserve selected task/session information and compose subagents into reusable programmatic workflows.
- Relevant environment: Input messages, model inference and streaming responses, registered tool side effects/errors, per-session history, graph checkpoints, developer-configured flow choices, user approvals and outside data services.
- Standard-distribution boundary: Go core `Agent`, `Runner`, Tool, Session, flow/graph, `internal/deep`, optional `evaluator`, middleware and skills/memory interfaces at the frozen first-party source. An actual model adapter and custom tools are supplied by configuration; providers' internal organizational control and adopters' custom `Condition`/graph callbacks are **not** silently credited as first-party S2–S5.
- Credited operating / distribution surfaces: [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L193); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L235); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L294); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L315); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L357); [runner.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/runner.go#L71); [flow/routing.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/routing.go#L17); [flow/parallel.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/parallel.go#L12); [flow/deep.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/deep.go#L27); [flow/loop.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/loop.go#L20); [graph/executor.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/graph/executor.go#L42); [evaluator/criteria.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/evaluator/criteria.go#L12); [middleware/confirm.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/middleware/confirm.go#L18); [skills/loader.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/skills/loader.go#L1).
- Adjacent first-party surfaces excluded from ownership: Example applications and sample `flow/evaluator` scenarios, test-only guards, repository CI/release, compiler/toolchain, maintainers, external model/API vendors, third-party MCP implementations, and any adopter-provided scorer, production control plane or parent management. Bundled evaluator library itself is inspected but not assumed to be installed and wired to current control in every app.
- First-party operating / deployment modes considered: Basic `NewAgent` with model/tool options and `NewRunner` (streaming or regular); optional supported `NewDeepAgent` with task/todo tools; `flow.RoutingAgent`, `ParallelAgent`, `LoopAgent`, sequential flows; graph execution/checkpoints; supported optional `evaluator.Criteria`, memory and confirmation middleware; shipped skills loader.
- Recursion level: The one Go runtime application and its model-controlled S1 task execution. Tool-wrapped subagents can be locally nested S1 executors; arbitrary parallel flows or graph nodes do not establish separately viable organizational S1 divisions with a metasystem.
- Reviewed revision: `b78fec59029d11e02c135ea10da8986ed006521f`, frozen row 6 in candidate intake #202 / serial batch #1669. Not current source `main`.
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The public `Agent` interface implements `Run`; `NewAgent` assembles provider, instructions, tools, middleware, iteration bounds and optional skills, while `NewRunner` builds an invocation/session context and consumes `Run` messages. At runtime `agent.Run` resolves the active tools, installs instruction/context and middleware, then calls `handle`. In `handle`, each model `Generate`/stream yields either a final assistant message or a `RoleTool` message. Tool messages pass to `executeTools`, which dispatches requested registered tools and records returned tool responses; the results are appended to session/local invocation history and fed into the next model turn until a final response, tool exit or maximum iteration. These are real first-party execution and feedback rights, though actual tool work/model inference can reside outside the library. [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L126), [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L193), [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L235), [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L315), [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L357), [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L439), [runner.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/runner.go#L71).

Shipped `flow.RoutingAgent` invokes a model-backed router and then a selected named subagent, `ParallelAgent` starts independent subagent calls concurrently and streams their outputs, `LoopAgent` repeats configured subagent executions until a supplied `LoopCondition` or exit signal, and `NewDeepAgent` creates a model-directed parent with todo and task delegation tools. These are substantive supported compositions; none is automatically independent organization-wide coordination or current governance. `graph.Executor` executes developer-compiled graph dependencies and optional checkpoint/resume. [flow/routing.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/routing.go#L17), [flow/routing.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/routing.go#L50), [flow/parallel.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/parallel.go#L12), [flow/parallel.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/parallel.go#L38), [flow/loop.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/loop.go#L20), [flow/loop.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/loop.go#L47), [flow/deep.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/deep.go#L27), [internal/deep/task_tool.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/internal/deep/task_tool.go#L35), [graph/executor.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/graph/executor.go#L42), [graph/executor.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/graph/executor.go#L86).

`evaluator.Criteria` is a genuine optional separately instantiated model-backed evaluator returning structured `Evaluation` (pass, score and feedback). The library entry takes a message and returns the classification; it does **not** by itself install a corrective readback to aggregate current operations. `middleware.Confirm` queries an adopter-provided callback to admit a particular invocation. Sessions/history, skills, graph checkpoints and memory assist continuity and tooling, not automatically S4 reconfiguration or S5 final organizational authority. [evaluator/criteria.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/evaluator/criteria.go#L12), [evaluator/criteria.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/evaluator/criteria.go#L17), [evaluator/criteria.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/evaluator/criteria.go#L33), [evaluator/evaluator.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/evaluator/evaluator.go#L10), [middleware/confirm.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/middleware/confirm.go#L12), [session.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/session.go#L12), [skills/loader.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/skills/loader.go#L1).

## Operational model

The concrete autonomous operation is the configurable single-agent model/tool/result iteration. Tool-wrapped and directly run subagents can each close their own S1 task decision cycles; nested `DeepAgent` uses a tool-selected dispatch under the parent's current request. Routings, graph edges, parallel execution and loops may distribute work and enforce sequencing, but classification of S2–S5 depends on independently evidenced *organizational* disturbance, decisive right, owner and returned adjustment, not package names. Programmatic callbacks provided by adopters can build more elaborate metasystems but are not borrowed as already-owned first-party functions.

## S1 — Operations

- State: A
- Function: Handle current tasks through model-selected operations and tool execution, retaining actual observations for further model decisions and user output.
- Disturbance / variety regulated: Open-ended user prompts, multimodal inputs, changes in tool/API responses, errors, session context and subtasks.
- Decisive decision or feedback right: Within the first-party `agent.handle` loop, the configured model selects tools/parameters or a final message based on prior history; tool execution returns actual observations into the next model request.
- Decision owner: Configured model-directed `Agent` operating within Blades' first-party loop. The remote model host is a provider dependency, while middleware/iteration limits and developer registrations constrain the agent.
- Supporting / enforcement mechanisms: `NewRunner`, Session history, `Invocation` data, Tool handler, middleware, optional skill/tool resolution, maxIterations, message streaming and tool-exit signals.
- Closure path: Input `Runner.Run` → agent `Run`/prepareInvocation → provider `Generate` or `NewStreaming` → `RoleTool` → `executeTools`/actual tool Handle result → session/local message history → next `Generate` or completed assistant answer.
- Boundary reachability: `NewAgent` configures a concrete `Agent.Run`, not just an interface sketch; `Runner` actually calls it, and `handle` executes registered tools and re-enters provider decisions for both stateless and session-history modes. Optional `NewDeepAgent` returns an actual configured `NewAgent` with task/todo tools.
- Why this is / is not agent-owned: Model decides next action from returned tool evidence; the deterministic tool handler, middleware and session are subordinate execution and data mechanisms. This is distinct from a purely prewritten graph sequence.
- Evidence: [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L145); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L193); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L235); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L294); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L315); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L357); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L439); [runner.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/runner.go#L71).
- Basis: Explicit reachable source showing model/tool/observation/next-decision closure.
- Confidence: High for first-party source structure; no external model/provider inference executed.
- Caveats: Actual provider integration, tools and policy are supplied at deployment; task-level autonomy does not imply metasystem autonomy.

## S2 — Coordination

- State: —
- Function: No verified first-party inter-S1 disturbance-specific damping relation with returned mutual adjustment is installed at the declared recursion.
- Disturbance / variety regulated: Parallel subagent contention, inconsistent data writes and competing tool actions could occur; actual inter-unit conflict-response policy is not implemented in the reviewed flow primitives.
- Decisive decision or feedback right: `ParallelAgent` starts and streams peers; `RoutingAgent` selects a named recipient; `LoopAgent` enforces configured iteration/condition. None detects a specific organizational disturbance between independently viable S1 cells and authoritatively attenuates it.
- Decision owner: Task model router, programmatic workflow composer and deterministic Go flow execution; no S2-specific mutual-coordination decision owner evidenced.
- Supporting / enforcement mechanisms: Subagent clone/errgroup, cancellation, HandoffTool routing, loop exit, graph dependency scheduling, Session and nested task tool.
- Closure path: Current task routing/parallel result/loop outputs reach the invoker; missing independent S1 conflict observation → S2-specific stabilization choice → enforced adjustments returned to affected distinct S1 units.
- Why this is / is not agent-owned: Concurrent agents, cancellation and model-chosen handoff are useful orchestration, not automatically S2; no concrete disturbance-specific reciprocal dampening is established.
- Evidence: [flow/parallel.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/parallel.go#L38); [flow/routing.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/routing.go#L50); [flow/loop.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/loop.go#L47); [flow/deep.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/deep.go#L27); [internal/deep/task_tool.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/internal/deep/task_tool.go#L35); [graph/executor.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/graph/executor.go#L42).
- Basis: Bounded negative after explicit inspection of supported first-party flow/graph modes.
- Confidence: Medium-high for source-inspected shipped paths.
- Caveats: An adopter could supply a separate S2 algorithm via callbacks; hypothetical composition does not upgrade shipped framework.

### Absence scope

- Surfaces inspected: First-party core Agent, DeepAgent TaskTool, ParallelAgent, RoutingAgent, LoopAgent, sequential flow, graph execution, tool/session handoff and middleware.
- Plausible first-party paths checked: Parallel conflicting tool calls, cancellation, handoff to specialists, deep-agent todo/task delegation, conditional graph edges and loop conditions.
- Why no material first-party path remains: Flows schedule/delegate/repeat task activity, and graph dependency rules are developer-specified; no first-party function detects and resolves a specific interference/oscillation between separate viable S1 units with reciprocal closed feedback.

## S3 — Inside-and-now control

- State: —
- Function: No app-wide current-control system is evidenced that integrates several S1 operating units and makes binding resource/commitment/priority interventions.
- Disturbance / variety regulated: Potential multiple subagent workloads, resource exhaustion, deadlines and competing workflow commitments; actual aggregate management is not present in the inspected first-party decision path.
- Decisive decision or feedback right: `DeepAgent` can model-select task delegation and update todos *for its current task*; `Runner` runs a root agent, and graph scheduler advances configured tasks. Neither represents a whole-current organizational command right across independent S1 purposes/commitments.
- Decision owner: Task agent, developer-authored graph/flow configuration, deterministic Runner/graph executor. No S3 metasystem owner or legitimate parent return path proven.
- Supporting / enforcement mechanisms: TaskTool, WriteTodos, graph checkpoint/recovery, session tracking, max iterations, parallel cancellation and optional middleware.
- Closure path: Current task → todo/delegation → feedback → task completion; absent whole-system current view → strategic present resource/priority/commitment adjudication → adjustment returned to distinct S1 cells.
- Why this is / is not agent-owned: Parent-subagent dispatch for one goal is S1 decomposition, not necessarily S3 management of an enduring organization; a checkpoint or todo list does not confer a S3 right.
- Evidence: [flow/deep.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/deep.go#L27); [internal/deep/task_tool.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/internal/deep/task_tool.go#L35); [internal/deep/write_todos_tool.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/internal/deep/write_todos_tool.go#L1); [runner.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/runner.go#L43); [graph/executor.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/graph/executor.go#L42); [graph/executor.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/graph/executor.go#L86).
- Basis: Explicit current-work context/graph/delegation inspection; bounded negative.
- Confidence: Medium-high at the declared application recursion.
- Caveats: Complex third-party orchestration applications may themselves own S3; their business governance is outside this source-boundary.

### Absence scope

- Surfaces inspected: Runner and sessions, core/deep model iteration and task delegation, graph dependency/checkpoint, parallel and loop status, error/confirm/retry middleware.
- Plausible first-party paths checked: Root agent as 'supervisor', todo management, cancellation and resumption, dynamic routing, graph current view and developer/operator callback control.
- Why no material first-party path remains: Every reviewed decisive choice is scoped to the current user invocation or developer-defined flow rather than an independent app-wide right controlling priorities, resources and commitments across multiple viable S1 workstreams.

## S3* — Complementary audit

- State: —
- Function: No independent complementary audit of operational reporting is connected by corrective feedback into normal current-control regulation.
- Disturbance / variety regulated: Inaccurate model outputs, weak artifacts or unmet criteria. A real `Criteria` LLM scorer exists for selected messages, but its returned `Evaluation` is not a shipped governance intervention.
- Decisive decision or feedback right: The optional model-backed scorer returns `Pass`, `Score`, `Feedback` to its caller; it does not independently interrogate ordinary multi-unit current control or own a returned corrective/withhold decision.
- Decision owner: Optional scorer agent/model and adopter caller choosing scoring criteria/handling. No separately authorized S3* organizational corrective actor in the normal running app.
- Supporting / enforcement mechanisms: Typed evaluation JSON, model `Run`, optional diagnostics/test code, middleware confirmation and tool errors.
- Closure path: Caller invokes evaluator with message → evaluator model outputs score/feedback → returned to caller; absent independently obtained conflicting operating evidence → S3 challenge → accountable correction/commitment revision returned into S1/S3.
- Why this is / is not agent-owned: LLM judging is genuine model feedback, but optional endpoint called by an adopter is not by itself complementary audit with independent access and enforced correction. Model judge names or scoring output are insufficient.
- Evidence: [evaluator/criteria.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/evaluator/criteria.go#L12); [evaluator/criteria.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/evaluator/criteria.go#L17); [evaluator/criteria.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/evaluator/criteria.go#L33); [evaluator/evaluator.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/evaluator/evaluator.go#L10); [flow/loop.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/flow/loop.go#L47); [middleware/confirm.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/middleware/confirm.go#L18).
- Basis: Source-backed evaluator input/output and separate workflow caller boundary, bounded negative.
- Confidence: Medium; evaluator possibility explicitly inspected rather than dismissed.
- Caveats: Specific external applications may wire evaluation to live corrective loops; outside declared first-party installed mode.

### Absence scope

- Surfaces inspected: Optional evaluator.Criteria, Evaluation/Feedback API, LoopAgent condition callback, graph condition functions, confirm/retry middleware and core session/messages.
- Plausible first-party paths checked: Model scoring, generated feedback, loop until criterion, review/retry tasks, externalized audit hooks and tool-error handling.
- Why no material first-party path remains: Scorer is optional and returns unconsumed typed feedback; `LoopCondition` and graph paths are developer-supplied task-level control, with no first-party independent audit reporting route into current-organizational authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective environmental-intelligence and organizational capability-adaptation decision with accepted return into operating configuration.
- Disturbance / variety regulated: Changing longer-horizon integration/model/tool needs and shifting user tasks; session memory and skills may preserve context, but not select strategic organizational changes.
- Decisive decision or feedback right: Developer configures model, tools, skills, recipe, memory and graph. Runtime can select operations, but no shipped autonomous future capability evaluation/approval/install right is established.
- Decision owner: External developer/operator for configuration, task agent for current decisions, optional model evaluator for individual outputs; no operational S4 owner or legitimate parent-return future adaptation path.
- Supporting / enforcement mechanisms: Skill loader, memory and history, model adapters, configurable ToolResolver, graph checkpoint/replay and Recipe loader.
- Closure path: Current request may read memory/skill instructions and operate within them; absent future environment sensing → alternative capability selection → authorized changed agent/tool topology → subsequent operations reflecting an S4 decision.
- Why this is / is not agent-owned: Pluggable design, tool registration, resumed graph and long-term memory are infrastructure for extensibility, not evidence of prospective system-level intelligence and closure.
- Evidence: [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L76); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L83); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L193); [session.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/session.go#L81); [skills/loader.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/skills/loader.go#L1); [memory/memory.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/memory/memory.go#L1); [recipe/loader.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/recipe/loader.go#L1).
- Basis: Bounded negative of supported dynamic extension/memory/graph mechanisms.
- Confidence: Medium-high for standard first-party modes.
- Caveats: A customized third-party self-improving agent could use these tools as S4, but none is first-party coupled here.

### Absence scope

- Surfaces inspected: Core provider/tool resolver and skill injection, Session memory/compression, recipe loading, graph state/checkpoints, deep task/todo and optional evaluator.
- Plausible first-party paths checked: Model-selected future tool changes, skill auto-creation/installation, persistent experience feedback, changing model/graph configuration, planned longer-horizon adaptation.
- Why no material first-party path remains: Runtime executes injected/configured skills and tools, retains context or replays tasks. The decisive strategy/option evaluation and durable admission into changed capabilities remain developer/user-authored outside the shipped runtime.

## S5 — Policy and identity

- State: —
- Function: No first-party final legitimate values/purpose/organizational identity decision and returned binding policy control path at the application recursion.
- Disturbance / variety regulated: Tool authorization, model/config identity and task-level confirmations, not proven ultimate organizational mission conflicts.
- Decisive decision or feedback right: Developer defines system instructions, model and tool set; optional `ConfirmFunc` allows/denies individual invocation; no function settles legitimate ultimate ethos/purpose for this app.
- Decision owner: Developer/operator who authored application constraints and callback, plus deterministic middleware that enforces tool/invocation admission; none a packaged S5 purpose-governing organ.
- Supporting / enforcement mechanisms: System instruction precedence, ToolResolver, middleware Confirm, stop/exit, session model and custom provider config.
- Closure path: Current invocation → approval callback → allowed/interrupted execution; missing policy-purpose dispute → authorized final organizational judgment → returned revised governing purpose for present operations.
- Why this is / is not agent-owned: A named agent, static instructions or per-tool human confirmation is not automatically ultimate authority over the system's identity and legitimate direction.
- Evidence: [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L27); [agent.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/agent.go#L193); [middleware/confirm.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/middleware/confirm.go#L12); [middleware/confirm.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/middleware/confirm.go#L18); [runner.go](https://github.com/go-kratos/blades/blob/b78fec59029d11e02c135ea10da8986ed006521f/runner.go#L43).
- Basis: Explicit source-control and middleware scope, bounded negative.
- Confidence: Medium-high for shipped first-party API/modes.
- Caveats: An actual adopter organization may supply S5 externally; this is not a packaged Blades owner and no parent-governed return is evidenced.

### Absence scope

- Surfaces inspected: Model/instruction/tool configuration, middleware confirm/retry, Runner and agent identity, session/flows/graph and evaluator.
- Plausible first-party paths checked: Human-in-the-loop approval, runtime safety policy, config mutation, agent naming and decision on a material purpose clash.
- Why no material first-party path remains: No shipped values/identity deliberation right plus authoritative returned future/current policy revision; mechanisms merely authorize or bound a specific run under external developer purpose.


## Distributed OSS parent arrangement

The root Agent, external model provider, user's application operator, skill author, optional evaluator model, remote subagents and Blades maintainers are different decision holders. `ConfirmFunc` and developer-authored workflow/graph callbacks do not establish a first-party parent-controlled S3/S4/S5 mode absent an organization-level view, legitimate parent choice and enforced return into ongoing operations.

## Self-hosted and non-human modes

The Go framework is installable and usable with a configured model/tool provider and optional sessions, flows, memory/skills and graph execution. Its internal S1 loop is active code; actual model inference or API credentials are external prerequisites. There is no claim to have executed live provider, external tool/MCP, custom adopter graph or production orchestration. Source-first evidence is limited to pinned first-party code.

## Recursion

An `agentTool` or `DeepAgent` can encapsulate an additional model/tool operational loop. Parallel and routed agents may themselves be S1 executors in their task recursion. No second viable metasystem with distinct S2–S5 decision closures is inferred from this topology.

## Variety and escalation

Task-level model iteration, tool feedback, middleware guards and optional ContextCompressor attenuate execution variety; graph checkpoint/resume supports individual task recovery, and `LoopAgent` can raise exit/escalation errors. These mechanisms can alert or bound current operations but do not establish additional S functions or an independently accountable algedonic channel.

## Evidence gaps

- The evaluator is a real packaged `Criteria` model judge with structured scored output. No shipped first-party path connects its findings to an independent S3* challenge, corrective S3 intervention and returned altered S1 operation. Source-bounded S3*=— does not deny possible adopter-written review pipelines.
- `ParallelAgent` and `NewDeepAgent` instantiate and invoke actual independent Agent objects, but this alone does not prove S2 conflict-sensitive coordination or S3 whole-application current commitments.
- Skills/memory can inform later runs; no first-party S4 agent selects and admits longer-horizon strategic capability redesign from outside intelligence at this recursion.
- This frozen-source semantic assessment does not attest external model/provider behavior, credentials, end-to-end production operations or full Go test execution. The Index structural/oracle and deterministic generator tests do not make unsupported runtime performance claims.
