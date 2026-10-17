---
harness_id: microsoft-agent-framework-for-go
project_name: Microsoft Agent Framework for Go
repository: https://github.com/microsoft/agent-framework-go
review_ref: f66340335e973986cbb8e9a1ae95e23596e4dc3d
reviewed_at: 2026-10-18
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

# Microsoft Agent Framework for Go

## Review boundary

- System in focus: The separately shipped **Go** implementation of Microsoft Agent Framework: the first-party agent wrapper, supported automatic tool-call middleware and loop harness, runtime state/session/context, workflow graph/agentworkflow combinators, GroupChat host, checkpoint, HITL request/approval and skill interfaces. Not Microsoft Agent Framework .NET/Python or externally hosted Foundry/Copilot agent service.
- Purpose and identity: A reusable Go package for developers to run model-powered agents and composed, recoverable and potentially human-approved task workflows. At the reviewed recursion, the organization under test is a configured Go agent/workflow application, not Microsoft's business organization or an adopter institution.
- Relevant environment: User/task requests, actual tool results and failures, provider streaming responses, message histories, workflow participant output, optional operator approval responses, checkpoint/resume and model-provider/platform events.
- Standard-distribution boundary: `agent`, `agent/harness/toolautocall`, `agent/harness/loop`, `agent/harness/toolapproval`, `agent/harness/agentmode`, `workflow`, `workflow/agentworkflow` and `agent/skills` at the pinned source. Provider adapters are accepted only as first-party integration surfaces, not as evidence of internals of remote Foundation-model/Foundry agent organizations. Constructor/wiring is credited where supported by Go package, not invented as default when an optional middleware must be selected.
- Credited operating / distribution surfaces: [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L109), [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L177), [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L269), [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L283), [agent/harness/toolautocall/autocall.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/toolautocall/autocall.go#L38), [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L39), [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L152), [agent/harness/loop/evaluators.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/evaluators.go#L26), [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L39), [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L86), [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L319), [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L359), [workflow/agentworkflow/concurrent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/concurrent.go#L1), [workflow/checkpoint/manager.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/checkpoint/manager.go#L1), [agent/harness/agentmode/agentmode.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/agentmode/agentmode.go#L1).
- Adjacent first-party surfaces excluded from ownership: Sample applications under `examples/`, `cmd/verifyexamples` and other contributor CI tools, documentation of .NET/Python behavior and external hosted Foundry governance. Adopter-defined arbitrary `GroupChatManager.SelectNextAgent/ShouldTerminate/UpdateHistory`, `loop.EvaluatorFunc`, custom graph/conditions, tool approval callbacks, policies, prompt templates, and human/institutional decisions are only credited as externally furnished rights unless shipped Go first-party closure is independently shown.
- First-party operating / deployment modes considered: Core `agent.New` wrapping a provider `Run` with middleware, sessions and history; installed tool-autocall for model-selected multi-turn tool use; optional `harness/loop` evaluator feedback/rerun; sequential and concurrent agent workflows; GroupChat with packaged RoundRobinGroupChatManager or custom manager callbacks; checkpoint/restore and in-process graph runtime; human input/approval, skills and plan/execute agent-mode context provider.
- Recursion level: One Go agent workflow/deployment, with model-directed current task operation and optional agent participants. Collaborating `agent.Agent` participants are potential S1 tasks but a graph or turn-taking protocol alone is not an independently viable parent organizational recursion.
- Reviewed revision: `f66340335e973986cbb8e9a1ae95e23596e4dc3d` frozen in Index intake #202 and serial batch #1669, not the moving upstream default branch.
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`agent.New` takes a `ProviderConfig` with a provider `Run` function and configures independent provider/agent middleware chains, tool options, context providers, and session history. `Agent.Run` invokes the pipeline and captures emitted updates into session/history/continuation, but **the base wrapper alone is a provider invocation**; model-selected, first-party repeated tool execution is specifically supplied by the supported opt-in `agent/harness/toolautocall` middleware. That middleware detects function-call content, resolves locally registered tools, invokes them, constructs function-result messages, binds approval requests when enabled, sends returned observations to the provider and repeats until a final model result, approval pause, error cap or iteration bound. This is a real reachable operational mode and the grounds for S1 autonomy, not a claim that every configuration automatically invokes tools. [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L109), [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L269), [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L283), [agent/harness/toolautocall/autocall.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/toolautocall/autocall.go#L38), [agent/harness/toolautocall/autocall.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/toolautocall/autocall.go#L146).

`agent/harness/loop` is another supported middleware: it executes an agent, gathers `LastResponse` and calls configured evaluators. `Continue(feedback)` or `ContinueWithMessages` can re-invoke the agent, optionally with a fresh session snapshot. The **bundled** `CompletionMarkerEvaluator` searches for a completion marker in the last agent response and supplies another message if absent. It is not independent access to a governed work system or independent verification of ordinary management reports. An adopter could install a more substantive evaluator callback; custom private/business evaluator internals cannot be borrowed into this first-party assessment. [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L39), [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L96), [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L116), [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L146), [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L152), [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L270), [agent/harness/loop/evaluators.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/evaluators.go#L26), [agent/harness/loop/evaluators.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/evaluators.go#L49).

The package builds sequential, concurrent, and GroupChat multi-agent workflows. In packaged GroupChat, the host retains chat history, updates/broadcasts messages, asks `GroupChatManager.SelectNextAgent` to choose the next participant, handles termination and persists manager state. The **shipped** `NewRoundRobinGroupChatManager` rotates speakers and uses an iteration cap. Other manager policies are caller-supplied function fields, not demonstrated first-party interference-governance rules. The graph execution runtime supports request ports/conditional routes, checkpoints, restarts and HITL waits. Model/provider adapters, memory/context providers, tool-approval and agentmode interfaces extend the developer's choices but do not by themselves settle system-wide purpose, portfolio governance or future organizational viability. [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L39), [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L86), [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L319), [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L359), [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L408), [workflow/checkpoint/manager.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/checkpoint/manager.go#L1), [workflow/requestport.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/requestport.go#L1), [agent/harness/agentmode/agentmode.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/agentmode/agentmode.go#L1).

## Operational model

The S1 operating unit is the configured model-directed Go agent with tool-autocall installed. The model chooses a registered callable using task context and previous results; the harness executes or stages approval and returns actual tool outcomes for further model decisions. Composed agent workflows hand off messages or issue concurrent requests. The reviewed Go package manages task progression, session state and backpressure, but the decisive metasystem thresholds are independent of product terms such as *group collaboration*, *group manager*, *approval*, *evaluation*, or *agent mode*.

## S1 — Operations

- State: A
- Function: Model-directed current task execution with first-party tool-call authorization/execution and returned environment observations in the supported tool-autocall mode.
- Disturbance / variety regulated: Unstructured requests, model-chosen tool sequences, API/tool outcome differences, errors and approval responses, stored multi-turn context and partner messages.
- Decisive decision or feedback right: Within configured `toolautocall`, each provider model response can select registered tools and arguments; the first-party middleware actually executes eligible tool calls and returns result/error messages into another model request. A provider-generated final answer or stop condition terminates the request.
- Decision owner: The installed model-guided Go agent operating through first-party automatic tool calling. The external model provides semantic choice; first-party Go tool registry, human approval options and middleware constrain what can execute.
- Supporting / enforcement mechanisms: ProviderConfig.Run, `Agent.Run` pipeline, request tool declaration/lookup, session/history and continuation, optional human approval binding, iteration/error limits and observability.
- Closure path: User/input → configured Go agent/provider → model-emitted function call → tool-autocall lookup and local invocation → actual tool result or governed approval → result to provider in continuing loop → next model decision or final user-facing response.
- Boundary reachability: The public Go `toolautocall.New` middleware can be configured into `agent.Config.Middlewares` and is actually called by the `agent.New` run pipeline, not merely a standalone example. Its run loop invokes model/provider again after dispatched tool results. Base `agent.New` **without** installed auto-call remains provider wrapper and is not independently represented as this positive loop.
- Why this is / is not agent-owned: There is a model-selected, evidence-returning operational decision loop with registered tool effects. A bare `Agent.Run` provider call or deterministic sequential workflow is not the positive witness.
- Evidence: [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L55); [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L109); [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L269); [agent/harness/toolautocall/autocall.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/toolautocall/autocall.go#L38); [agent/harness/toolautocall/autocall.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/toolautocall/autocall.go#L146); [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L283).
- Basis: First-party shipped middleware and actual provider/tool/result/reinvocation closure at pinned Go source.
- Confidence: High structural evidence, not an external provider or end-to-end inference claim.
- Caveats: This S1=A exists in the explicitly supported installed auto-call mode. Go client does not guarantee autonomous choices if middleware/model/tool support is absent.

## S2 — Coordination

- State: —
- Function: No demonstrated interference-specific feedback control among independently viable S1 units at this declared application recursion.
- Disturbance / variety regulated: Competing agent turns, concurrent work, inconsistent outputs and interaction conflicts could exist; the shipped multi-agent patterns do not identify and regulate a concrete inter-S1 oscillation or resource interference.
- Decisive decision or feedback right: `NewRoundRobinGroupChatManager` rotates turn index, host broadcasts messages and enforces turn/termination; caller-injected SelectNextAgent/UpdateHistory may implement custom policies, but first-party does not choose an interference-specific stabilizing policy.
- Decision owner: Deterministic group host and round-robin algorithm or adopter-provided callback. The Go package owns turn scheduling, not a separate active S2 disturbance-adjustment judgment.
- Supporting / enforcement mechanisms: Graph edges/turn tokens, concurrent fan-out, group history broadcast and manager checkpoints, sequential agents, request ports and termination guard.
- Closure path: Agent output → GroupChat host updates shared history/broadcast/next turn → other agent invocation. This provides messaging and turn-taking, but lacks sensed inter-unit conflict → damping decision → adjustment fed back to multiple operating S1s.
- Why this is / is not agent-owned: Selecting which model agent speaks next is agent routing/turn sequencing; without an evidenced inter-S1 disturbance it does not become Viable System S2.
- Evidence: [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L39); [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L86); [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L109); [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L319); [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L359); [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L408); [workflow/agentworkflow/concurrent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/concurrent.go#L1).
- Basis: Direct first-party manager and host path review, bounded negative.
- Confidence: Medium-high for packaged managers and workflow modes.
- Caveats: Applications can supply a custom manager with S2-specific rules; the interface alone does not establish shipped S2 ownership.

### Absence scope

- Surfaces inspected: GroupChatManager and shipped round-robin manager, host turn/termination/broadcast, sequential/concurrent workflows, graph routes/requests, tool-autocall and agentmode.
- Plausible first-party paths checked: Shared conversation history, distributed participant turns, concurrent fan-out, custom manager callbacks, graph dependency and tool approval.
- Why no material first-party path remains: First-party mechanisms route/serialize/broadcast or cap turns. There is no configured default or code-reachable S2-specific active comparator/adjudicator of disruptive cross-unit operations with returned mutual stabilization. Custom callbacks are externally authored.

## S3 — Inside-and-now control

- State: —
- Function: No distinct closed whole-current organizational manager governs multiple operational units' commitments, priorities, shared resources and interventions.
- Disturbance / variety regulated: Competing running workflows, participant task conflicts, resource availability, constraints and obligations could require system-level current governance; no such integrated control decision was shown.
- Decisive decision or feedback right: Group host chooses next chat participant and terminates a dialogue; graph checkpoint/restart and request port wake tasks. These do not decide present system-wide portfolio/resource commitments or accountability across independently purposed S1 units.
- Decision owner: Per-request agent provider, developer-selected GroupChatManager or deterministic workflow runtime; no first-party accountable whole-current owner with an enforced return to separate S1 workstreams.
- Supporting / enforcement mechanisms: Host message history, manager turn state, workflow graph, checkpoints and resumption, loop evaluator iteration budget, approval pause, plan/execute mode under explicit user permission.
- Closure path: Single workflow updates/broadcasts/terminates; missing aggregate operational view → current inter-unit allocation/priority/commitment choice → binding adjustment to governed S1 units.
- Why this is / is not agent-owned: A group conversation 'manager' is a turn controller, not a manager of organizational survival/resource priorities. Human approval of a tool run or switching local plan/execute mode is not parent S3.
- Evidence: [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L319); [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L359); [workflow/agentworkflow/groupchat.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/agentworkflow/groupchat.go#L390); [workflow/checkpoint/manager.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/checkpoint/manager.go#L1); [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L152); [agent/harness/agentmode/agentmode.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/agentmode/agentmode.go#L1).
- Basis: Source-bound current-control vs task control distinction, bounded negative.
- Confidence: Medium-high at app recursion.
- Caveats: An adopter may implement independent S3 policy via manager callbacks/workflow, but none established in the default Go package.

### Absence scope

- Surfaces inspected: GroupChatManager and host, workflow/inproc execution, checkpoints, request port, agentmode, loop harness, tool approval and agent session state.
- Plausible first-party paths checked: Group host as overarching supervisor, persisted management state, plan/execute permission, parallel queue capacity and human control via HITL.
- Why no material first-party path remains: All shipped decisive control manages this workflow/turn/request lifecycle or accepts external callback choices; none claims, owns and feeds back decisions over independent whole-system current obligations.

## S3* — Complementary audit

- State: —
- Function: No independent complementary access path challenges normal current-control claims and returns corrective enforcement across S3/S1 operation.
- Disturbance / variety regulated: Unfinished or low-quality model replies, unknown tool outcomes and false assertions of completion. The loop can request another response, but is a task-level feedback guard.
- Decisive decision or feedback right: Installed `loop.Evaluator` can return Continue(feedback) and rerun, yet packaged `CompletionMarkerEvaluator` inspects only last model response text. Separate audit evidence and an independent corrective-management right are not present.
- Decision owner: The configured evaluator callback / completion-string matcher within the same request loop; adopter would own any separately engineered verifier, not first-party default S3*.
- Supporting / enforcement mechanisms: Evaluation structs, LastResponse/Feedback, session snapshot restart, iteration ceilings, tool-error/approval handling, tracing and workflow checkpoints.
- Closure path: Agent response → completion-marker check or supplied evaluator callback → task iteration and new prompt. Lacks independent access to operating facts → challenge of S3 reporting → autonomous/legitimate corrective order into live S1 work.
- Why this is / is not agent-owned: A feedback-triggered rerun **is real**, but neither checking a completion marker nor replaying one's task constitutes independently corrective complementary audit of a viable organization's current performance.
- Evidence: [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L39); [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L96); [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L116); [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L152); [agent/harness/loop/loop.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/loop.go#L270); [agent/harness/loop/evaluators.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/evaluators.go#L26); [agent/harness/loop/evaluators.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/loop/evaluators.go#L49).
- Basis: Positive test of actual built-in evaluator feedback and negative of independence/organizational audit closure.
- Confidence: Medium-high at shipped first-party boundary.
- Caveats: A substantive separately deployed evaluator wired through the public callback interface could create a different application-specific audit, not established here.

### Absence scope

- Surfaces inspected: Loop middleware evaluator interface, feedback and rerun path, shipped CompletionMarkerEvaluator, tool approval, model/tool traces, checkpoints/observability and workflow request ports.
- Plausible first-party paths checked: Evaluator as verifier, completion-marker feedback into rerun, independent provider/agent-as-reviewer, HITL review and watchdog-like checkpoint monitoring.
- Why no material first-party path remains: Built-in evaluator has only the last response/marker and returns into the same request. Other verification judgment must be explicitly supplied by adopter; there is no shipped distinct S3* evidence path with corrective control authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: No demonstrated first-party prospective environmental intelligence generating and legitimately adopting system capability/reconfiguration choices.
- Disturbance / variety regulated: Longer-horizon model/provider/tool changes, emerging external requirements and failure patterns. Session context/skills can help current tasks but no packaged future intelligence decision is closed.
- Decisive decision or feedback right: Developer supplies tools, skills, models and GroupChatManager/workflow design. `agentmode` supports a plan/execute permission switch explicitly directed by user rather than assessing future environment and admitting changed organization capabilities.
- Decision owner: External application developer/operator for future configuration; per-request model and user for immediate plans/mode consent; no supported future capability authority returned to the runtime.
- Supporting / enforcement mechanisms: History/context providers, skills, plan/execute mode state, continuation, workflow checkpoint/replay, externally selected model and tool adapter.
- Closure path: Configuration and session state affect present/future calls; missing environment sensing/strategic future options → authorized viability judgement → modified available capabilities/organizational configuration adopted into subsequent S1.
- Why this is / is not agent-owned: Memory, installed skills and the name 'plan' concern current requested work, not selection and deployment of a new sustainable organizational capability.
- Evidence: [agent/harness/agentmode/agentmode.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/agentmode/agentmode.go#L1); [agent/harness/agentmode/agentmode.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/agentmode/agentmode.go#L39); [agent/history.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/history.go#L1); [agent/skills/skills.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/skills/skills.go#L1); [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L55); [workflow/checkpoint/manager.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/checkpoint/manager.go#L1).
- Basis: Bounded negative after testing mode switching/skills/session and workflow evolution alternatives.
- Confidence: Medium-high for pinned Go package modes.
- Caveats: Third-party self-modifying tools or business innovation workflows are outside assessed shipped closure.

### Absence scope

- Surfaces inspected: Agent mode provider, skills, context/history, tool options/provider adaptation, workflow graph/checkpoint, loop feedback and continuation.
- Plausible first-party paths checked: Mode-based autonomous planning, persistent learning/capability change, policy/skill selection, loop-judged improvement and externally observed future alternatives.
- Why no material first-party path remains: Mode switching is directed by user permission, skills and tools are developer-provisioned, and evaluator feedback addresses this task. No distinct first-party future intelligence organization receives and implements accepted capability decisions.

## S5 — Policy and identity

- State: —
- Function: No owner of final legitimate organizational policy and purpose/identity disputes is closed within the first-party Go agent application.
- Disturbance / variety regulated: Tool policy, approval requirements, agent IDs/instructions and session modes do not establish ultimate organizational ethos or binding purpose disputes.
- Decisive decision or feedback right: Human/toolapproval can permit an individual tool invocation; agentmode can switch task mode after explicit user instruction; developer registers agent Name/Description and provider config. No first-party ultimate identity arbitration is returned.
- Decision owner: Adopter's human/operator and static configuration for their local tasks; not a shipped legitimate S5 governing body with durable organization-wide policy return.
- Supporting / enforcement mechanisms: Agent configuration ID/instructions, approval-request binding, plan/execute mode permission, HITL request port and provider/tool scope.
- Closure path: Current tool approval/mode/config → immediate allowed/blocked request, but absent final organizational purpose decision → authorized identity/policy change → return into system-wide governing objectives.
- Why this is / is not agent-owned: Operational permission and contributor/host authority are not evidence of final policy identity or resolution of irreconcilable organizational aims.
- Evidence: [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L55); [agent/agent.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/agent.go#L109); [agent/harness/toolapproval/toolapproval.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/toolapproval/toolapproval.go#L1); [agent/harness/agentmode/agentmode.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/agent/harness/agentmode/agentmode.go#L1); [workflow/requestport.go](https://github.com/microsoft/agent-framework-go/blob/f66340335e973986cbb8e9a1ae95e23596e4dc3d/workflow/requestport.go#L1).
- Basis: Shipped identity and permission surfaces reviewed, bounded negative.
- Confidence: Medium-high for declared first-party boundary.
- Caveats: External Microsoft organization, hosted Foundry service or an adopter's business may have S5, but they are not the assessed Go runtime's S5.

### Absence scope

- Surfaces inspected: Agent ID/Name/Description and tools, HITL request/approval, mode permissions and workflow request ports, provider authentication/host boundary, contributor governance as explicitly excluded.
- Plausible first-party paths checked: Human tool approval as parent, mode change as policy, agent instructions and GroupChat management as ultimate authority.
- Why no material first-party path remains: All these rights are run-level authorizations/configurations governed by external actors; no first-party final purpose-adjudication and returned binding policy loop exists at the app recursion.

## Distributed OSS parent arrangement

Microsoft maintainers, an adopter's business/operator, model providers, separately hosted Foundry Agents, custom GroupChatManager callbacks and an instantiated Go workflow are distinct decision domains. A parent operator's HITL tool approval or user-requested plan/execute mode change does **not** establish `S3=P`, `S4=P` or `S5=P` without an organizational-level decision right and a governed return. Do not inherit the broader .NET/Python features into this Go-specific repository.

## Self-hosted and non-human modes

The Go package supports local/in-process agent middleware, session, conditional workflow execution and persistent checkpoints. Provider inference/tool operations may require external configuration, remote services or credentials. The first-party automatic tool-calling loop and GroupChat host are code paths at frozen source, not proof of live credentials or a deployed Foundry environment. No external cloud model inference or live multi-agent E2E was performed.

## Recursion

Group chat participants and sequential/concurrent workflow nodes can contain their own model-directed S1 operations. The GroupChat host provides turn dispatch and a shared conversation; those alone do not establish S2 to S5 at a higher recursively viable organization. Classify each higher function only when an actual corresponding right, owner, affected unit, and returned closure are shown.

## Variety and escalation

Tool-call iteration/error limits, approval pauses, context/history, group turn caps, checkpoints and loop evaluator feedback bound or restore current work. External human approval, loop continuation, errors and interruption can be useful escalation surfaces but they do not automatically supply an independent algedonic channel or whole-current/ultimate metasystem ownership.

## Evidence gaps

- The Go `agent.New` constructor wraps provider functions; first-party tool-autocall is **optional**, so positive `S1=A` is source-backed only for the supported installed multi-turn tool mode. External model/provider behavior and effective permissions were not E2E exercised.
- The packaged evaluator feedback path really **does** rerun the agent. Only a completion-marker evaluator is supplied in the inspected first-party path; a separately implemented independent verifier with S3 corrective power was not shown. Bounded S3*=— does not preclude future/adopter-specific verifier integrations.
- Custom GroupChatManager hooks admit sophisticated policies, but the shipped RoundRobinGroupChatManager rotates speakers and caps turns; no first-party adaptive conflict-specific inter-S1 or whole-current control was evidenced.
- The Go implementation explicitly differs from .NET/Python; framework product positioning, examples and remote Foundry integrations are not credited as current operational ownership.
- Source-first frozen semantic review only; no live provider, credentials, external A2A/Foundry/AG-UI or production workflow replay claimed. Index checkers/tests validate assessment materialization and structural contract, not inference performance.
