---
harness_id: flue
project_name: Flue
repository: https://github.com/withastro/flue
review_ref: 6285b0ee89ad8941009ecd0062de11a8cd64c4a3
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Flue

## Review boundary

- System in focus: the first-party Flue agent harness at pinned revision `6285b0ee89ad8941009ecd0062de11a8cd64c4a3`, centered on `@flue/runtime` and its owned agent/session loop, tools, skills, persistent state, subagent/task execution, durability/recovery, sandbox integration contracts, runtime hooks and supported Node/Cloudflare runtime glue.
- Purpose and identity: provide a programmable TypeScript harness in which model-driven agents can maintain durable conversations, choose tools and skills, act through a sandbox, delegate focused work to isolated child sessions, and recover accepted work through interruption.
- Relevant environment: user and application messages, webhook/channel/schedule signals, model-provider responses, tool/API state, sandbox filesystem/process/network state, workspace context and skills, child-agent results, process crashes/redeploys and operator/application configuration.
- Standard-distribution boundary: shipped `@flue/runtime` behavior plus documented first-party Node.js and Cloudflare execution modes, including runtime-owned durability semantics. External model providers, MCP servers, sandbox providers, databases, telemetry backends and workflow engines are environment/substrate. Application-specific callback code supplied through generic hooks remains developer composition unless Flue itself supplies the relevant organizational function.
- Credited operating / distribution surfaces: runtime/session/harness code under `packages/runtime/src/`; documented agent functions and hooks; built-in task/subagent machinery; durable submission/recovery logic; built-in virtual/local sandbox integration; first-party runtime event surfaces; and supported Node/Cloudflare target glue where it implements Flue-owned lifecycle behavior.
- Adjacent first-party surfaces excluded from ownership: `.flue/agents/*` repository dogfood agents, `.github/workflows/*`, contributor/release automation, examples and demo applications, website/blog implementation, tests as independent organizational actors, and blueprints that merely generate application-specific integration code. External workflow engines and observability providers are not imported into the Flue harness boundary.
- First-party operating / deployment modes considered: registered agents driven by CLI, HTTP, `dispatch()` or `start()/init()`; Node and Cloudflare runtime targets; sandboxed and no-sandbox operation; optional skills and subagents; durable recovery when a durable database/target is configured. Generic user-authored workflow code is not treated as a built-in Flue metasystem.
- Recursion level: one deployed Flue harness/application as the system-in-focus. Registered root-agent conversations are operational units. A delegated child session is a bounded nested operational execution capability of its parent, not automatically a viable recursive unit. Runtime attempts/coordinators are execution machinery, not separate S1 units merely because they own a lease.
- Reviewed revision: `6285b0ee89ad8941009ecd0062de11a8cd64c4a3`.
- Stable GitHub repository id: `1152451571`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Flue exposes agents as exported functions whose current render supplies instructions and composes model, sandbox, tools, skills, subagents, persistent state and lifecycle hooks. A registered agent has a durable identity keyed by agent name plus instance/conversation id. Inputs from HTTP, `dispatch()`, channels or schedules are admitted as submissions and enter one durable conversation stream. The model receives instructions and message state, chooses model-visible tool calls, receives their results, and may continue for further turns until the response reaches a would-stop point. `useAgentFinish` is a first-party response-control seam that can append a signal and send the model through another turn when application-defined completion conditions are not met.

Durability is first-party execution infrastructure rather than a separate organizational manager. A submission is durably admitted before model work. Flue processes one submission at a time per conversation, records attempts, preserves committed tool outcomes and persistent-state writes, repairs interrupted tool batches, retries bounded transient failures, and eventually records one terminal settlement. On Node a Flue coordinator uses leases and reconciliation to recover abandoned submissions; on Cloudflare each conversation is structurally hosted in one Durable Object and wake/reconciliation logic resumes unsettled work. These mechanisms keep one operational conversation coherent across failure, but they do not by themselves choose organizational priorities or adaptation policy.

Subagents are model-selected delegates. A parent exposes a named roster through `useSubagent`; the framework `task` tool lets the parent model send a complete task prompt to a child with fresh context. Multiple task calls in one batch can run concurrently, and child sessions have their own durable records. Only the child's final answer returns as the parent's tool result. Parent and child may share a sandbox, but Flue documents files as a hand-off surface rather than supplying a conflict-resolution protocol among independent children.

Skills and conditional resources make operational capability dynamic. Skills are packaged instructions selected by the model; workspace skills can be discovered from `.agents/skills/`; `useTool`, `useSkill`, `useSubagent` and `useSandbox` can be conditional on persisted state. These mechanisms allow an application or an S1 agent to change its immediately available operational repertoire. They are not, by themselves, an outside-and-then intelligence loop: no standard first-party path was found that senses future/external distinctions, develops adaptation options as an S4 function and returns an autonomous adaptation decision into current capability.

Observability is deliberately non-controlling. The runtime `observe()` API emits typed activity across agents, but subscribers receive detached read-only observations, cannot steer the runtime, and subscriber failure cannot halt an agent. Sentry, Braintrust and OpenTelemetry integrations export those events/spans to external telemetry systems. This supplies operational visibility but not an independent complementary audit actor or corrective feedback owner.

## Operational model

A root agent is rendered before model calls so its current instructions and conditional resources reflect durable state. The model consumes current conversation/workspace context, chooses whether to answer or invoke model-visible tools such as application tools, sandbox operations, skill activation or the framework `task` tool, and receives resulting observations. Tool-call cycles and optional `useAgentFinish` continuation signals can cause further model turns before one durable submission settles.

Durability surrounds this S1 loop. Accepted work is queued per conversation, attempts are claimed and supervised, committed outcomes are replay-safe, and recovery resumes from durable evidence. A crash can therefore cause a new runtime owner to continue the same accepted submission without changing who owns the task-level operational discretion: the model-driven agent remains the actor selecting task actions; the coordinator/lease machinery owns execution safety and recovery transitions.

Subagent delegation creates isolated child work contexts when the parent model chooses a delegate. The child executes to a final answer and the result becomes a tool observation for the parent. Parallel children provide fan-out, but the standard distribution does not add a separate first-party agent that observes interactions among those child S1s and regulates a specific collision/oscillation. External durable workflows can sequence several Flue agents, but the documentation explicitly states that workflows are not a Flue feature per se and recommends Cloudflare Workflows, Inngest, Temporal or ordinary application scripts for durable multi-step orchestration outside the agent.

## S1 — Operations

- State: A
- Function: autonomously transform task and environment state through a model-driven decision/action/observation loop until a bounded response or durable terminal outcome is produced.
- Disturbance / variety regulated: heterogeneous user/application goals, evolving conversation state, workspace and sandbox contents, tool/API results, model outputs/errors, conditional capability availability and interrupted work that require context-sensitive next actions.
- Decisive decision or feedback right: choose the next model-directed action — answer, activate expertise, invoke a tool/sandbox action, delegate to a child, or continue after observations — and decide task-level next steps from returned results.
- Decision owner: the active Flue root-agent model actor in the registered agent conversation; delegated child model actors own the bounded operational choices inside their delegated tasks.
- Supporting / enforcement mechanisms: agent-function rendering, model/provider adapter, tool execution, sandbox adapters, skills, persistent state, session/conversation records, submission queue, retry/timeout limits, `useAgentFinish` control seam and durability/recovery machinery.
- Closure path: admitted message/signal + durable conversation/environment state → model chooses action/tool/delegation → Flue executes it → result/observation returns to model-visible context → model chooses another action or produces the response → submission settles durably.
- Boundary reachability: registered agents, their model/tool loop, skills, sandbox and task delegation are documented standard runtime surfaces available through `@flue/runtime` on supported deployment modes, not repository dogfood or test-only actors.
- Why this is / is not agent-owned: removing the model-driven agent while leaving submission queues, leases, persistence, sandboxes and tool executors intact removes the context-sensitive task decisions. Deterministic runtime machinery transports, constrains and recovers those decisions rather than replacing them.
- Evidence: [`README.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/README.md), [`building-agents.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/building-agents.md), [`use-agent-finish.ts`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/packages/runtime/src/hooks/use-agent-finish.ts), [`durability.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/durability.md).
- Basis: structural
- Confidence: high
- Caveats: model inference and external tools/providers remain substrate. Durability can resume the loop after interruption, but recovery ownership is not being counted as an additional VSM function.

## S2 — Coordination

- State: —
- Function: no material first-party S2-specific path was established that regulates a concrete interference/conflict/oscillation among distinct S1 operational units at the declared Flue-application recursion.
- Disturbance / variety regulated: candidate disturbances inspected included parallel child tasks sharing a sandbox, duplicate/retried execution, multiple registered agent conversations and concurrent runtime ownership; none is paired in the standard boundary with an S2-specific autonomous coordination decision path among distinct S1 units.
- Decisive decision or feedback right: no qualifying inter-S1 coordination right is supplied by Flue itself; developers may impose sequencing or coordination in application/workflow code, while per-conversation queues and leases deterministically protect one conversation's execution semantics.
- Decision owner: none established for S2 in the standard distribution.
- Supporting / enforcement mechanisms: per-conversation submission ordering, one-live-owner constraints, attempt leases/recovery, parallel `task` execution, child final-result handoff, shared sandbox, generic `dispatch()` and external workflow composition.
- Closure path: no S2-specific autonomous closure was found. Delegated child results return to the parent as ordinary tool outcomes, and queue/lease mechanisms regulate execution ownership rather than a cross-S1 organizational disturbance.
- Why this is / is not agent-owned: a parent model may choose delegates and synthesize their outputs, but delegation, fan-out and result collection do not establish S2 without a concrete inter-S1 disturbance plus a coordination relation aimed at attenuating it. Flue does not supply such an agent-owned relation as a standard organizational function.
- Evidence: [`subagents.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/subagents.md), [`durability.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/durability.md), [`workflows.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/workflows.md).
- Basis: structural
- Confidence: high
- Caveats: an application built on Flue can compose explicit S2 behavior, and shared sandbox state can create real collisions, but generic framework expressiveness is not enough for `C`; no first-party S2-specific construction path was established.

### Absence scope

- Surfaces inspected: root-agent/session semantics, `useSubagent`/`task` delegation, parent/child sandbox sharing, per-conversation submission queue and lease recovery, `dispatch()`, workflow guidance, runtime hooks and dynamic-resource behavior.
- Plausible first-party paths checked: child-task parallelism, shared workspace handoff, per-conversation serialization, duplicate/recovery fencing, multi-agent dispatch and workflow orchestration.
- Why no material first-party path remains: the inspected primitives either delegate/sequence work, protect one conversation's execution ownership, or expose generic application composition. None is tied to a specific cross-S1 interference witness with an S2-specific decision/feedback path that changes subsequent behavior of multiple S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current-control function was established over the set of operational agent conversations at the declared recursion.
- Disturbance / variety regulated: candidate current-control disturbances included running/failed submissions, timeouts, provider failures, concurrent ownership and multiple child tasks; Flue regulates these as local execution/reliability conditions rather than whole-system commitments, priorities, resources or synergy.
- Decisive decision or feedback right: no agent or first-party parent mode was found with a whole-harness view and discretionary authority to rebalance current work, resources, priorities or commitments across S1 units.
- Decision owner: none established for S3. Runtime coordinators deterministically claim/recover attempts according to configured durability rules; application developers or external workflow engines own any higher-level scheduling/prioritization they compose.
- Supporting / enforcement mechanisms: submission queues, attempt leases, startup reconciliation, wake scans, timeout/abort signals, retry budgets, conditional resources, `useAgentFinish` callbacks and external workflow integration.
- Closure path: local reliability transitions return into the same conversation's execution, but no whole-system S3 decision loop across current operations was found.
- Why this is / is not agent-owned: the Node coordinator and Cloudflare Durable Object supervision have enforcement authority over attempt ownership and recovery, not discretionary organizational authority over current operational commitments. `useAgentFinish` is a generic application-authored callback seam, not a built-in whole-system controller.
- Evidence: [`durability.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/durability.md), [`use-agent-finish.ts`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/packages/runtime/src/hooks/use-agent-finish.ts), [`workflows.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/workflows.md).
- Basis: structural
- Confidence: high
- Caveats: a developer can build S3 in surrounding application/workflow code; this assessment does not promote generic control hooks, schedulers or recovery coordinators to `C` without an established S3 function.

### Absence scope

- Surfaces inspected: durability coordinator/recovery paths, per-conversation queues, timeout/retry configuration, agent lifecycle hooks, subagent runtime, dispatch/init APIs, workflow documentation and supported Node/Cloudflare deployment semantics.
- Plausible first-party paths checked: coordinator ownership, lease recovery, one-live-owner constraint, `useAgentFinish` continuation, dynamic resource switching and external durable workflows.
- Why no material first-party path remains: these surfaces regulate local execution/recovery or expose generic developer composition. They do not provide a first-party whole-system current view plus discretionary authority over shared resources, priorities, commitments or interventions across the harness's operational units.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit path was established that challenges ordinary operational claims and returns findings into subsequent control.
- Disturbance / variety regulated: candidate audit concerns included failed model turns, tool errors, traces, token/cost accounting, child-task outcomes and final-response completion checks.
- Decisive decision or feedback right: no first-party independent auditor owns a judgment over operational truth with corrective return. Runtime observers receive telemetry; application-authored finish hooks may enforce developer-defined completion rules but remain in the ordinary response path and are not independently supplied auditors.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: `observe()` runtime event stream, conversation history, logs, traces, Sentry/Braintrust/OpenTelemetry adapters, `useAgentFinish`, settlement records and durable child transcripts.
- Closure path: telemetry may be exported for external analysis, but Flue's observer contract is read-only and live-only; no standard audit finding is routed back as a corrective organizational decision.
- Why this is / is not agent-owned: observers cannot steer execution and their failures are contained. A developer can attach an evaluator or write a finish hook, but generic hooks and external telemetry do not establish a first-party independent audit actor or judgment.
- Evidence: [`observability.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/observability.md), [`use-agent-finish.ts`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/packages/runtime/src/hooks/use-agent-finish.ts).
- Basis: explicit
- Confidence: high
- Caveats: Braintrust can be used by an application for evaluation, and custom observers can feed other systems, but those external/application-specific arrangements are not first-party S3* closure in the assessed distribution.

### Absence scope

- Surfaces inspected: runtime `observe()` semantics, conversation/runtime event separation, telemetry integrations, trace/log exports, settlement events, `useAgentFinish` control hooks and durable transcripts.
- Plausible first-party paths checked: global runtime observer, Braintrust/Sentry/OTel integrations, final-response enforcement callbacks, child transcript inspection and failure/settlement diagnostics.
- Why no material first-party path remains: the observer is explicitly detached/read-only and cannot alter execution; integrations export telemetry to external systems; finish hooks are application-defined ordinary-path controls. No independent complementary access + audit judgment + corrective feedback closure is supplied as a standard first-party function.

## S4 — Outside-and-then intelligence

- State: —
- Function: no standard first-party outside-and-then intelligence loop was established that senses external/future-relevant distinctions, develops adaptation options and returns an adaptation decision into current Flue capability.
- Disturbance / variety regulated: candidate adaptation inputs included new messages/signals, changing workspace skills, persistent state, resource availability, sandbox changes and provider/tool failures.
- Decisive decision or feedback right: no S4-specific autonomous adaptation judgment is supplied. Agent models can make task-local choices and application code can conditionally add/remove resources; developers or external systems decide the adaptation logic they compose.
- Decision owner: none established for S4 in the standard distribution.
- Supporting / enforcement mechanisms: persistent state, conditional `useTool`/`useSkill`/`useSubagent`/`useSandbox`, workspace-skill discovery, dynamic resource signals, editable workspace files, lifecycle hooks and application dispatch of external signals.
- Closure path: state can change resources at later turn boundaries, but the standard runtime does not itself form prospective adaptation options from external intelligence and choose which capability change should be adopted as an S4 function.
- Why this is / is not agent-owned: an S1 agent may operationally call a tool that flips state and thereby gain a sandbox or skill, but that is immediate task-level regulation unless evidence ties it to external/prospective adaptation. Generic dynamic-resource primitives are not an S4-specific constructor under Methodology 0.3.5.
- Evidence: [`skills.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/skills.md), [`sandboxes.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/sandboxes.md), [`building-agents.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/building-agents.md).
- Basis: structural
- Confidence: high
- Caveats: Flue is expressive enough to host a custom self-improvement/adaptation design; that possibility is deliberately not published as `C` without a first-party S4-specific decision/feedback path.

### Absence scope

- Surfaces inspected: skill packaging/activation/workspace discovery, persistent state, conditional resources and environment switching, lifecycle hooks, message/signal ingress, model/provider recovery and workflow guidance.
- Plausible first-party paths checked: runtime resource changes, workspace-skill edits, external signals, context compaction/recovery and generic agent-authored capability changes.
- Why no material first-party path remains: the surfaces enable immediate operational reconfiguration or developer composition but do not supply a first-party external/prospective sensing → option-generation → adaptation-decision → return-to-current-capability loop.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy escalation-decision-return loop was established at the Flue-application recursion.
- Disturbance / variety regulated: candidate identity/policy matters included agent instructions and names, sandbox/network/credential boundaries, caller authorization, tool/skill composition, durability limits and developer configuration.
- Decisive decision or feedback right: no first-party S5 authority receives identity-level disputes/proposals, decides them and returns the decision to govern later operation. Developers/application owners author instructions, middleware, resources and configuration outside the autonomous runtime decision loop.
- Decision owner: none established as an operationally closed S5 function within Flue's standard distribution.
- Supporting / enforcement mechanisms: agent instructions/system prompt, static agent identity, sandbox capability boundaries, network allowlists, explicit environment-variable injection, application middleware for conversation access, configuration and hook/resource declarations.
- Closure path: configuration and application code constrain subsequent execution once changed, but no first-party runtime path carries an identity/ultimate-policy issue to legitimate authority and returns its decision.
- Why this is / is not agent-owned: static instructions, environment restrictions and application-owned authentication are constraints selected outside the agent. They do not become S5 merely because the runtime enforces them, and no autonomous agent is shown owning ultimate-policy authority.
- Evidence: [`building-agents.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/building-agents.md), [`sandboxes.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/apps/docs/src/content/docs/guide/sandboxes.md), [`README.md`](https://github.com/withastro/flue/blob/6285b0ee89ad8941009ecd0062de11a8cd64c4a3/README.md).
- Basis: structural
- Confidence: high
- Caveats: the host application or organization can supply policy/identity governance around Flue; that parent system is not automatically part of the assessed harness boundary.

### Absence scope

- Surfaces inspected: agent identity/instructions, HTTP exposure and authorization guidance, sandbox/network/credential controls, tool/skill/resource configuration, lifecycle hooks, durability configuration and repository governance surfaces.
- Plausible first-party paths checked: system instructions, middleware/auth guidance, sandbox capability policy, environment allowlists, configuration changes and repository-level governance.
- Why no material first-party path remains: these are static/developer-owned constraints or adjacent governance mechanisms. No first-party standard runtime path closes an identity- or ultimate-policy-level issue through authoritative decision and return to subsequent operation.

## Recursion, variety, and escalation

Flue strongly supports operational recursion-like composition without proving VSM recursion: a parent can launch nested child sessions, but delegates are intentionally not registered durable agents with their own address/persistent state and therefore are not counted as viable recursive systems solely because they can nest. At the declared recursion, root-agent conversations absorb task variety locally; durability attenuates crash/provider/runtime failure variety so accepted work can continue without escalating every interruption to an operator.

The runtime also provides useful escalation primitives — failed settlements, durable errors, signals, application hooks and externally consumed telemetry — but these are channels/mechanisms. This assessment does not assign S3/S3*/S4/S5 merely because an external application could attach an appropriate organizational actor to them.

## Final vector

`A — — — — —`
