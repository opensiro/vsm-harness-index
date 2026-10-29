---
harness_id: tardigrade
project_name: Tardigrade
repository: https://github.com/clavia-labs/tardigrade
review_ref: 9ba13979e251f338a0f6c7baaf29f4f2d67a34d5
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

# Tardigrade

## Review boundary

- System in focus: the first-party TypeScript Tardigrade/Tardie agent actor runtime and its supported host wiring, not the whole Tardigrade contributor organization or any particular customer's agent deployment.
- Purpose and identity: execute model-directed tasks through durable actor turns, tools, recorded observations and retried/reactivated event-log state.
- Relevant environment: incoming operator turns, model responses, external API/workspace/tool outcomes, child-agent results, failing effects, context limits, permissions and host-provided credentials.
- Standard-distribution boundary: `packages/agent/src` default `createActor`, its inference/tools/trajectory/permissions/budget atoms, `packages/libraries/src/agents.ts`, supported `assistantRuntime` host and first-party Bun/Cloudflare actor/platform binding. The selected model and external systems remain supplied by an installer/host.
- Credited operating / distribution surfaces: model-to-tool-to-event-to-model recurrence in `createActor` and host's effect services, with optional child actor delegation and durable parent notifications.
- Adjacent first-party surfaces excluded from ownership: deprecated `apps/server` assembly, quickstart/demo-specific weather example, repository tests, TLA specifications, CI, SDK documentation and developer/maintainer releases. These show construction/test patterns but do not become governing runtime units.
- First-party modes considered: one configured actor thread; default model, permission and tool policy; local child-agent calls through the exported agents library and `assistantRuntime(maxChildDepth)`; independently persisted Bun/Cloudflare threads. An app's custom actor definition or external evaluator is not presumed installed.
- Recursion level: one first-party deployed agent runtime including its optional child actor threads as supported by the stock host, with the installer/operator as external parent. A supervisor thread directory is not automatically a VSM metasystem.
- Reviewed revision: `9ba13979e251f338a0f6c7baaf29f4f2d67a34d5`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The public README describes composable Effect-TS agent actors with durable atoms and immutable event logs. The shipped `createActor` actually composes `tools`, `permissions`, `toolBudget`, `compact(messages)`, `infer(...)` and `agentMethods`. An external `agentMethods.message` call records `TurnRequested`; `infer` uses a host model service and records `ModelCalled`/`ModelReturned`. Model tool calls are queued in `pendingTools`; permission/budget wrappers constrain `tools` proposals, and successful/failed execution records `ToolReturned`. `inferenceState` clears outstanding calls and exposes `needsReply`; the model can then see projected assistant/tool messages and choose further work or settle a terminal turn. This is an actual first-party actor/action/observation loop even without a live provider execution in this assessment.

The default optional `agents` library exports `delegate_task` and `cancel_agent`, returning a durable child execution handle. `assistantRuntime` configures a bounded-depth local child runtime, forwards child requests/messages to the parent as data, waits for child settlement, and cancels pending child work on interruption. The Bun and Cloudflare platforms persist separate thread logs and parent/child identity. These are substantial execution, recovery and supervision mechanisms, but the code does not itself demonstrate a particular conflict between two autonomous task cells, an agent-selected resolution of that conflict, or a whole-system resource bargaining policy.

Tool budgets and permissions are real: `withBudget` and `withPermissions` can prevent a tool from running, and events retain grants/denials. `parentBudgetRequests`, `grantBudget` and `askBudget` are exported construction elements, but a search of the reviewed standard-distribution references finds no callsite wiring them together into the default `assistantRuntime` services/tool catalog. The default child agent is given a static per-turn tool-call cap. No richer resource governor or ultimate organizational identity adjudicator is inferred from extensible APIs.

Primary pinned source evidence:

- [README](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/README.md) and [default agent actor](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/agent.ts) — composition/primary first-party task mode.
- [inference effect](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/infer.ts), [durable inference reducer](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/durable/inference.ts) and [actor message method](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/actor/methods.ts) — generated actions, outstanding-tool wait and terminal return.
- [pending tool queue](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/durable/tools.ts), [tool execution/permissions/budget wrappers](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/tools.ts) and [trajectory projection](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/durable/trajectory.ts) — observation returning to subsequent model input.
- [child-agent tools](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/libraries/src/agents.ts), [assistant runtime/host](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/services/runtime.ts) and [thread topology](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/docs/explanations/threads.md) — child delegation, parent messages and recovery/placement identity.
- [budget request atom](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/budget-request.ts), [budget/permission service constructors](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/services/decisions.ts) and [permission atom](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/permission-request.ts) — constrain execution, not proof of broader S3/S5 decision ownership.

## Operational model

The first-party agent thread is an S1 operation: a model chooses an action in the external environment, gets durable tool/child results, and re-enters inference until `TurnSettled`. Its host and durable atoms provide reliable effect delivery and context. A child thread can itself be an S1 at a nested recursion, but a default `delegate_task` handle and returned answer are not evidence of conflict-dampening S2. Developer/operator configuration and permission/budget services govern how a task may proceed; this does not automatically form the VSM whole-system supervisory, audit, prospective or ultimate-policy functions.

## S1 — Operations

- State: A
- Function: autonomous first-party model-directed task execution through durable agent turns, real tools and observed results.
- Disturbance / variety regulated: unpredictable operator requests, web/workspace/tool results, model continuations and errors, child results, interrupted effects and bounded context.
- Decisive decision or feedback right: select tool calls from current model context, interpret returned observations, initiate subsequent action/continuation or produce the terminal answer; optionally choose a child delegation.
- Decision owner: model-backed Tardigrade agent actor in `infer`, not the actor directory, event store or platform driver.
- Supporting / enforcement mechanisms: `defineActor`, `agentMethods`, model provider adapters, queued tool execution, durable trajectory, permissions, per-turn budgets, compaction, host effect execution and child threading.
- Closure path: `TurnRequested` leads to `ModelReturned`; queued tool calls produce `ToolReturned`, the trajectory adds tool content to the next model context, and `inferState` updates `needsReply` until a no-tool model answer permits `TurnSettled` and `agentReply` returns it.
- Boundary reachability: the stock `createActor` and `assistantRuntime` directly instantiate the mechanism; the Bun example and Cloudflare host API expose it to callers. No custom downstream agent logic is needed to establish this S1 implementation.
- Why this is / is not agent-owned: the model chooses task-sensitive work and interprets feedback; deterministic reducers, budget policy, replay and permissions gate or deliver that work but do not replace the agent's substantive decisions.
- Evidence: [agent.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/agent.ts); [infer.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/infer.ts); [inference reducer](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/durable/inference.ts); [tools.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/tools.ts); [trajectory.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/durable/trajectory.ts); [methods.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/actor/methods.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Source-defined first-party path, not an observed live provider/session; no task-quality or deployment uptime claim.

## S2 — Coordination

- State: —
- Function: no demonstrated coordination relation specifically attenuating inter-S1 interference at the chosen actor-runtime recursion.
- Disturbance / variety regulated: child request/result routing, possible concurrent threads, separate logs, pending tool queues and naming/placement; no concrete shared operational-task conflict with a corrective return is shown.
- Decisive decision or feedback right: model can delegate/cancel a child; host allocates unique thread state, queues effects and transports notifications. No distinct S2 adjustment decision for a specific interference is wired.
- Decision owner: parent task actor for delegation, deterministic host/runtime for identity, storage and scheduling. No qualifying S2 coordinator identified.
- Supporting / enforcement mechanisms: `localActors`, `agents.run/cancel`, parent `onRequest/onReply/onMessage`, durable per-thread databases, execution handles and serial per-thread tool queue.
- Closure path: child completion returns task data to its parent, and actor directories preserve lifecycle. This is work delivery/recovery, not a demonstrated interference-damping feedback to multiple S1 units.
- Why this is / is not agent-owned: generic agent-to-agent messaging, task decomposition, thread isolation and process-level serialization do not meet Profile's specific S2 disturbance/attenuation/return requirement.
- Evidence: [agents library](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/libraries/src/agents.ts); [runtime.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/services/runtime.ts); [threads.md](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/docs/explanations/threads.md); [tool queue](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/durable/tools.ts).
- Basis: structural.
- Confidence: high.
- Caveats: A specific downstream actor may compose an S2 mechanism; none is imported without a first-party wired collision witness.

### Absence scope

- Surfaces inspected: bundled default agent and child-agent tools, assistant runtime callbacks, thread topology/identity and durable tool queue.
- Plausible first-party paths checked: concurrent children, shared parent inbox, cancel handles, isolation of SQLite thread logs and queued tool calls.
- Why no material first-party path remains: these address routing, local execution, lifecycle or general resource segregation; they do not identify a concrete interaction between two S1 task cells and a coordination result changing their subsequent behavior.

## S3 — Inside-and-now control

- State: —
- Function: no active whole-system regulator of present resource/commitment conflict beyond local limits and externally configured permission decisions.
- Disturbance / variety regulated: child/individual-turn tool-call consumption, per-tool authorization, model/tool failures and default maximum child depth.
- Decisive decision or feedback right: configured host or parent sets individual permission/budget caps; `withPermissions`/`withBudget` enforce decisions. No first-party whole-system view revises multiple operational commitments or shared priorities in response to actual contention.
- Decision owner: installer/host's configured permission and model services, parent task actor for requesting/delegating; deterministic counters/gates for enforcement.
- Supporting / enforcement mechanisms: `BudgetConfigured/Resolved`, `PermissionConfigured/Resolved`, child depth limit and cancellation; exported `parentBudgetRequests` and `grantBudget` constructor APIs exist but are not composed in the default runtime.
- Closure path: grants or denials change whether the individual pending tool executes and how its turn resumes. No returned whole-system bargaining/reprioritization path is supplied by the stock distribution.
- Why this is / is not agent-owned: `grantBudget` could be used by a custom supervisory actor, but is not itself a wired, whole-system S3 decision; static caps and per-action approval are insufficient.
- Evidence: [budget-request.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/budget-request.ts); [tools.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/tools.ts); [decisions.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/services/decisions.ts); [runtime.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/services/runtime.ts).
- Basis: structural.
- Confidence: high.
- Caveats: Constructor potential is separated from reachability in the stock operating boundary; task budget adjustment is not automatically S3.

### Absence scope

- Surfaces inspected: default actor composition, host child services and tool catalog, budget/permission policies, grant-budget construction functions and depth cancellation.
- Plausible first-party paths checked: parent receives child requests, budget grant service, per-agent reservations and host enforcement of policy.
- Why no material first-party path remains: the potential parent-budget negotiation helpers are not wired to the default host model/tool services, and no operating whole-system current-state arbitration and returned commitment adjustment is evidenced.

## S3* — Complementary audit

- State: —
- Function: no independent alternative operational audit challenging normal actor claims and returning findings to control.
- Disturbance / variety regulated: logged model/tool outcomes, runtime effect errors, actor state and test/formal-model validity.
- Decisive decision or feedback right: no separate qualified auditor with alternative access and control-return decision in the stock agent runtime.
- Decision owner: operational agent for its model/tool loop, host for journaling and exception handling, developers for tests/TLA specs; no independent S3* owner.
- Supporting / enforcement mechanisms: immutable event logs, trajectory projection, replay, unit/integration tests and TLA models in adjacent repository testing/constructor surface.
- Closure path: event results re-enter normal model context and hosts can retry/replay, while tests inform repository maintainers; no complementary audit finding is routed into a distinct runtime regulator.
- Why this is / is not agent-owned: event sourcing and test suites permit future auditing but do not themselves constitute an independent check on operational assertions.
- Evidence: [trajectory.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/durable/trajectory.ts); [inference.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/durable/inference.ts); [TLA durable execution model](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/platform/cloudflare/tla/DurableExecution.tla); [runtime.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/services/runtime.ts).
- Basis: structural.
- Confidence: high.
- Caveats: No runtime sampling, audit experiment or independent evaluator was executed or credited.

### Absence scope

- Surfaces inspected: event reducers/projections, normal result channels, host retry/recovery, tests and Cloudflare TLA formal specifications.
- Plausible first-party paths checked: raw-event inspection, test replay, formal verification, external audit via exported host hooks.
- Why no material first-party path remains: data/logs and adjacent design-time verification do not provide an independent running audit owner or audit-specific findings-to-control return path in the standard agent system.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/future-directed modeling-and-adaptation loop returning options to present S3 capability.
- Disturbance / variety regulated: context-window pressure, incoming external data, tool failure and optional child assistance.
- Decisive decision or feedback right: the task model selects current tool calls; `compact` invokes a summarizer for context retention. No shipped prospective intelligence owner forms and approves options from externally changing conditions.
- Decision owner: task model for immediate work, deterministic compaction threshold rules and external developer/operator for future feature/policy changes.
- Supporting / enforcement mechanisms: compaction context summaries, durable memory, HTTP tool and child delegation, host model selection.
- Closure path: summaries and observations improve the next task prompt, but no external-prospective option-development path negotiates a change in current organizational capability.
- Why this is / is not agent-owned: a research-capable tool and memory update remain task operations until a specific future-directed adaptation relation is implemented.
- Evidence: [compact.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/compact.ts); [infer.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/infer.ts); [agent.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/agent.ts); [runtime.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/services/runtime.ts).
- Basis: structural.
- Confidence: high.
- Caveats: No future-oriented app-specific composition is presumed merely from general-purpose agent programmability.

### Absence scope

- Surfaces inspected: model/compaction atoms, tool catalog, child services and standard agent entrypoints.
- Plausible first-party paths checked: summarizing accumulated observations, fetching external data, asking subagents to research and invoking tooling over time.
- Why no material first-party path remains: these paths close current work and context, not an identified external-and-prospective adaptation option with two-way S3/current-capability feedback.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy adjudication and return to future operations is supplied within the standard runtime.
- Disturbance / variety regulated: configurable system prompt, permissions, model credentials and task-limit policies.
- Decisive decision or feedback right: installer/host supplies system instructions and permission decisions; ordinary tool approvals and budget settings do not involve a documented identity-level issue/ultimate authority decision.
- Decision owner: external developer/operator for policies and prompt identity, operational model for tasks; no first-party S5 authority path established.
- Supporting / enforcement mechanisms: `systemPrompt` atom, permission policy events, budget/child caps and host injection of model services.
- Closure path: the configured policies affect later tool execution or prompts, without a shipped path that detects an identity/future-versus-present conflict, reaches legitimate ultimate authority and returns its adjudication to govern operations.
- Why this is / is not agent-owned: a configurable system prompt or caller decision over an individual tool is a constraint, not evidence of VSM S5 policy closure.
- Evidence: [agent.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/agent.ts); [system.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/system.ts); [permission-request.ts](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/permission-request.ts); [permissions reducer](https://github.com/clavia-labs/tardigrade/blob/9ba13979e251f338a0f6c7baaf29f4f2d67a34d5/packages/agent/src/atoms/durable/permissions.ts).
- Basis: structural.
- Confidence: high.
- Caveats: An adopter can supply organizational policy governance; no claim is made about all possible applications built with this framework.

### Absence scope

- Surfaces inspected: default system prompt, permission policy/configuration, budget decisions, host/external model services, thread and parent callback boundaries.
- Plausible first-party paths checked: operator approval, prompt updates, child escalation requests and the actor's own model choice.
- Why no material first-party path remains: all shown decisions concern ordinary task/action authorization and externally configured constraints; no first-party identity/ultimate-policy conflict and legitimate adjudication-return route is implemented.

## Distributed OSS parent arrangement

The framework developer, application integrator and deployment operator are distinct parent/constructor roles. External model/provider organizations and downstream user agents are not silently absorbed into the Tardigrade runtime's VSM function ownership. Public repository governance is not a proven policy controller of any deployed agent thread.

## Self-hosted and non-human modes

The documented Bun and Cloudflare host modes can run with configured model and tool providers, with optional non-human child actors. Permissions and budgets remain host/composer choices. No independent non-human organizational S3/S4/S5 governance is shown by the runtime alone.

## Recursion

Each child thread has its own log, workspace, effect lifecycle, environment-facing model/tools and potential independent S1 work. The parent/child relation supplies durable delegation and cancellation; the presence of nested agent actors does not establish a complete nested VSM or automatically credit parent metasystem functions.

## Variety and escalation

Durable journal replay, `ToolReturned` feedback, permission gates, per-turn tool-call caps, child depth ceilings, cancellation and compaction attenuate operational variety. `onRequest`/`onMessage` can transport unusual child conditions to the parent as task data, but no exceptional signal interpretation coupled to the relevant S3/S4/S5 authority and closure is evidenced; it is not promoted to an algedonic channel.

## Evidence gaps

- Source-first review of the pinned TypeScript distribution; no live provider calls, deployed Cloudflare actor, third-party API/task execution or E2E agent benchmark was performed.
- Runtime budgets/permissions and child actors are real shipped paths, but a particular multi-agent collision-resolution policy or whole-system resource negotiation was not found in the default wiring. `parentBudgetRequests`/`grantBudget` are compositional extension points, not automatically executed S3 decisions.
- Tests and TLA specifications are adjacent quality evidence for durable execution, not a second operational reality-check authority. No unverified downstream use of the framework can be imported to fill S2/S3/S3*/S4/S5.
- A future deployment-specific assessment may find additional VSM functions when its actual actor composition, operators and governance are pinned and made reachable.

## Assessment summary

The shipped Tardigrade actor actually owns a model/tool/observation loop with durable local state: `S1=A`. Delegation, parent notifications, permission controls, budget caps, compaction and formal runtime tests are important supporting machinery, but do not meet the specific evidence/ownership/closure requirements for S2, S3, S3*, S4 or S5 at the declared default-runtime boundary. The canonical included vector is **`A / — / — / — / — / —`**.
