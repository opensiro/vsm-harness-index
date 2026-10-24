---
harness_id: kode-sdk
project_name: KODE SDK
repository: https://github.com/shareAI-lab/kode-agent-sdk
review_ref: 2596118805d8968c7e33cc437e440721833e9689
reviewed_at: 2026-10-25
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

# KODE SDK

## Review boundary

- System in focus: The distributable TypeScript KODE SDK for model-backed persistent agents and optional multi-agent composition, not the company/community maintaining it or an embedding application's entire organization.
- Purpose and identity: Execute user- or application-supplied tasks through model-selected tool actions and preserve agent state across interaction and restart; support developers composing multiple task actors.
- Relevant environment: Variable tasks, model answers, tool failures, sandbox contents, permission responses, agent messages, persistence/recovery events and provider availability. External market, governance and future capability signals are not modeled by a first-party strategic controller.
- Standard-distribution boundary: Shipped `src/` exports with registered templates, dependency-injected external model provider, store, tool registry and sandbox; `Agent`, `AgentPool`, `Room`, `task_run`, events, hooks, skills and permissions. The developer supplies credentials, tasks, templates and optionally a team topology.
- Credited operating / distribution surfaces: [SDK exports](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/index.ts), [Agent model/tool loop](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts), [AgentPool](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/pool.ts), [Room](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/room.ts), [delegation tool](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/tools/task_run/index.ts), [Scheduler](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/scheduler.ts), [permission manager](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent/permission-manager.ts), [skills runtime](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/skills/manager.ts).
- Adjacent first-party surfaces excluded from ownership: `examples/` example teams, user-provided coordinator prompts and workflows, integration/developer tests, benchmark claims, repository contributors/releases/CI, external LLM provider and any independently written application-level S2–S5 regulator. The separately exported skill file-management service explicitly does not participate in Agent runtime.
- First-party operating / deployment modes considered: Single `Agent` chat/complete/stream backed by a model; multiple distinct `Agent` instances in `AgentPool` with `Room` directed/broadcast messaging; opt-in `task_run` or `spawnSubAgent` delegation; operator/API `decide` approvals; persistent JSON/SQL store and restart; dynamic skill loading, step scheduler, self-hosted sandbox and third-party provider. No live model or agent was run.
- Recursion level: One installed SDK-composed task execution with autonomous model-backed S1 work cells; a parent-to-child task call is not automatically a separate viable organizational recursion.
- Reviewed revision: `2596118805d8968c7e33cc437e440721833e9689`, frozen in [discovery #2024](https://github.com/opensiro/vsm-harness-index/issues/2024) and [serial control #2025](https://github.com/opensiro/vsm-harness-index/issues/2025).
- Observation date: 2026-10-25.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Agent` is the concrete model-backed work unit. Its shipped `runStep` flushes pending messages, may compress context, streams a request with tool schemas through `this.model.stream`, collects chosen tool calls, executes them, persists tool responses as new context and schedules another step. The SDK provides sandbox/tool runners, approval pause/resume, event streams, checkpoints, stores and a step-triggered scheduler. `AgentPool` creates/resumes/deletes agents and handles capacity and graceful shutdown. `Room` sends text to named peers or broadcasts it by calling `agent.complete`; `task_run` delegates one model-chosen template task to a new child agent and returns the result. [agent core](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts#L961-L1246), [pool lifecycle](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/pool.ts#L38-L126), [room message delivery](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/room.ts#L8-L57), [delegate implementation](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts#L661-L756).

The standard library exposes building blocks for a containing organization's coordination, audit, adaptation and policy, but the bundled examples' coordinator prompt, a user-chosen cap of 50 agents, file-based skill installation, SDK lifecycle administration and human tool approvals do not themselves implement those higher-order functions. The different `SkillsManagementManager` service states explicitly that it is separate from the running agent's skill loader. Tests and documentation support implementation analysis, not live outcome/effectiveness claims.

## Operational model

An integrating operator registers a model, templates and tools, then sends a task. A model-backed `Agent` autonomously chooses among available next tool calls and a final response; the SDK feeds observations back for another decision, with specified permission gates. Applications can launch several S1 units and choose to use a pool, room, or agent-triggered subtask. The SDK does not supply a default model-backed manager with a whole-current view and power to revise peer commitments, a dispute-resolving inter-S1 protocol, an independent audit owner, or a prospective adaptation/identity feedback circuit. The model owns within-task tool choices; the developer/operator owns the wider composition and operating constraints.

## S1 — Operations

- State: A
- Function: Execute a supplied task through an autonomous model-backed operational actor using offered tools and feedback from their effects.
- Disturbance / variety regulated: Unpredictable user input, sandbox contents, tool errors, permission outcomes and intermediate model responses require choosing what to do next.
- Decisive decision or feedback right: The external model selects a next tool call or content response using the context and advertised schemas; subsequent tool observations influence the next model request.
- Decision owner: Configured model-backed `Agent` operational work cell. The model provider supplies inference; first-party SDK code deliberately constructs and closes its model/tool/observation loop.
- Supporting / enforcement mechanisms: Tool registry/runner, `PermissionManager`, sandbox, context compression, stores, message queue, hooks, events, scheduling and operator-configured limits.
- Closure path: `Agent.complete`/`chat` → queued prompt → `runStep` → `model.stream` → tool-use selection → `executeTools` → tool outcomes appended as user messages → `ensureProcessing`/next model turn or completed answer.
- Boundary reachability: `Agent` is a public SDK export and its normal `complete` mode directly invokes the agent loop; no example-only controller or evaluation job is needed to receive and act on model-chosen tool calls.
- Why this is / is not agent-owned: Without model discretion, the existing deterministic transport, retries, approvals and tool runner cannot decide which task-specific tool to invoke next. The model's tool selection is operational ownership, not merely its ability to produce text.
- Evidence: [public Agent export](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/index.ts#L1-L17); [complete and send](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts#L458-L518); [stream and closure](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts#L1012-L1211); [delegated actor completion](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts#L702-L753).
- Basis: Structural first-party runtime call path and published API.
- Confidence: High for implemented autonomous decision/feedback; no empirical claim of effectiveness or safety.
- Caveats: The SDK requires external model credentials/dependencies and user-provided task/template. A child `Agent` is a bounded operational unit, not automatic proof of recursive viability.

## S2 — Coordination

- State: —
- Function: No first-party coordination circuit specifically attenuating interference, collision or oscillation *between* two distinct S1 work cells is evidenced in the standard distribution.
- Disturbance / variety regulated: Separate agents could potentially disagree, duplicate edits or collide in one sandbox, but the SDK does not represent a concrete shared-work conflict and a conflict-specific response.
- Distinct S1 units: `AgentPool` holds multiple independent model-backed `Agent` instances, and `Room` delivers messages to selected members; this establishes multiplicity, not S2 closure.
- Inter-S1 disturbance: No collision detection, reservation ownership, contradictory-output reconciliation, conflict arbitration or feedback from a detected peer disturbance is represented in the reviewed multi-agent primitives.
- Attenuating coordination relation: `Room.say` transfers text to one or more peers; `task_run` serially delegates a parent task to a child. Neither checks or dampens any particular inter-agent interference.
- Feedback into subsequent S1 behaviour: Recipient models may condition their next output on delivered messages, but there is no *coordination result* from an inter-S1 instability being fed back under a first-party S2 protocol.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The functions inspected are precisely ordinary transport, pool lifecycle and delegation. An embedding app could add a dispute procedure, but none is installed by KODE SDK itself.
- Decisive decision or feedback right: Developers/operators decide topology and communication content; no first-party S2 response-selection or conflict-resolution owner is established.
- Decision owner: No qualifying S2 owner inside this boundary.
- Supporting / enforcement mechanisms: Room membership map, mentions/broadcast, pool capacity checks, subagent depth/template restrictions, caller-defined coordinator system prompt.
- Closure path: Parent invokes child and awaits result, or `Room.say` calls peer `complete`; neither closes a specifically evidenced conflict → mitigation → revised S1 behavior relation.
- Why this is / is not agent-owned: Agent-originated task messages may be discretionary, but autonomy of message content does not make generic delivery an S2 function.
- Evidence: [Room](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/room.ts#L8-L57); [pool](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/pool.ts#L38-L126); [task_run tool](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/tools/task_run/index.ts#L10-L83); [documented pattern is user-authored](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/docs/en/advanced/multi-agent.md#L246-L289).
- Basis: Bounded negative on shipped first-party multi-agent path.
- Confidence: Medium-high.
- Caveats: An application's own scripted negotiation, locking or conflict-aware shared-work layer would move the assessed boundary; no such application is included here.

### Absence scope

- Surfaces inspected: `AgentPool`, `Room`, `task_run`, `Agent.spawnSubAgent`/`delegateTask`, scheduler, multi-agent guide and first-party coordinator example descriptions.
- Plausible first-party paths checked: Mention/broadcast messaging, child-task results returned to parent, pool membership and fixed capacity, template/depth guards and shared sandbox.
- Why no material first-party path remains: Multiplicity and message return exist, but a specific inter-S1 disturbance, its attenuator and a qualifying feedback closure are absent from these standard distributed primitives; there is no unresolved candidate S2-specific code path.

## S3 — Inside-and-now control

- State: —
- Function: No bundled whole-current regulation of the active agent population's conflicting commitments, shared-resource allocation or accountability is established.
- Disturbance / variety regulated: Agents could exhaust concurrent capacity, exceed context limits or produce weak work, but the SDK exposes fixed caps and local agent processes, not a controller that evaluates and revises the whole's priorities.
- Decisive decision or feedback right: The embedding developer chooses which agents to create and how to distribute tasks; `AgentPool.maxAgents` is a configured guard, not a model-owned or constructor-managed choice among current commitments.
- Decision owner: External embedding application/developer for population design; the SDK has no qualified S3 owner or parent-return circuit.
- Supporting / enforcement mechanisms: Pool `maxAgents`, task delegation, per-agent todos, context compression, step scheduler, event monitor, graceful shutdown and resume.
- Closure path: Fixed configured limits reject additional creations; shutdown persists/interrupts operations; subagent results return to their parent task. No whole-population appraisal → discretionary resource/priorities revision → changed S1 operations exists.
- Why this is / is not agent-owned: A coordinator-like prompt in docs may choose delegates inside its own task; without an installed whole-current view and authority over the other S1 units, delegation is S1 decomposition rather than S3. Hard-coded capacity cannot own choices about commitments.
- Evidence: [pool create and maxAgents](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/pool.ts#L38-L100); [pool shutdown](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/pool.ts#L137-L253); [local scheduler](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/scheduler.ts#L19-L85); [parent task delegation](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts#L702-L755).
- Basis: Bounded negative after checking S3 constructor and parent possibilities.
- Confidence: Medium-high.
- Caveats: A self-hosted app could place an autonomous manager over this SDK; that manager is not a first-party supported control mode established in the package.

### Absence scope

- Surfaces inspected: `AgentPool` create/list/status/shutdown/recovery, parent task delegation, todos, event streams, model loop, scheduler, README and multi-agent reference.
- Plausible first-party paths checked: Agent cap, pool status snapshots, operator-applied interrupts, task template selection, token/context compression, local step callbacks and caller-supplied coordinator prompt.
- Why no material first-party path remains: Each is capacity enforcement, per-task work, reporting or developer-defined wiring; none chooses or revises shared commitments/priorities from a whole-current operating view or closes an S3 parent-control return.

## S3* — Complementary audit

- State: —
- Function: No sufficiently independent inspection of claims by operating agents beyond their ordinary output/tool/event stream is part of this SDK's working governance loop.
- Disturbance / variety regulated: Agent results might be inaccurate, unauthorized or misleading; permission checks and event logs are local execution governance rather than independent raw-reality audit.
- Decisive decision or feedback right: No separately authorized audit finding about operational reports is made from complementary evidence and fed into current-control decisions.
- Decision owner: Operator may inspect events or build a reviewer agent in an application; the SDK itself does not construct independent audit ownership.
- Supporting / enforcement mechanisms: Progress/control/monitor event channels, approval decisions, tool-result records, generic reviewer template documented in examples, snapshot/replay facilities.
- Closure path: Tool results reenter the same producer's model context; event subscribers and human approvals can affect routine work but have no independent audit judgment returning to an S3 regulator.
- Why this is / is not agent-owned: A second model named `reviewer` in a user template is normal production QA until the independently sourced evidence, auditor ownership and return to separate control are demonstrated.
- Evidence: [agent event and tool-result path](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts#L1190-L1247); [event bus](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/events.ts); [optional reviewer example](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/docs/en/advanced/multi-agent.md#L162-L184).
- Basis: Bounded negative standard-distribution review.
- Confidence: Medium-high.
- Caveats: Independent tests or reviewers implemented by a downstream application can change the result at that application's boundary; such a mode is not credited here.

### Absence scope

- Surfaces inspected: Event bus, agent progress/control/monitor reporting, tool records, persistence, optional reviewer template and permission interfaces.
- Plausible first-party paths checked: Event subscriptions, tool-result observation, replay/snapshot, reviewer subagent and permission gate.
- Why no material first-party path remains: These paths reuse production artifacts or govern execution; none demonstrates independent evidence access, audit-specific judgment and corrective feedback into separate whole-current regulation.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party future-oriented external-environment sensing → adaptation option → adoption into current operating capability circuit is demonstrated.
- Disturbance / variety regulated: Future shifts in models, tools or workloads might require adaptation, but the shipping runtime handles current conversations and lets an operator manage skills and templates.
- Decisive decision or feedback right: The SDK does not choose and adopt future capability alternatives from external intelligence; operators/developers install skills and update model/templates outside a closed agentic S4 loop.
- Decision owner: Developer/operator for versions, providers and skill sets; per-task agent/tool choices remain S1.
- Supporting / enforcement mechanisms: Hot skill scanning, `SkillsManagementManager` import/archive/export, model provider configuration, context compression, hooks and lifecycle events.
- Closure path: Changed skill files may become visible on the next scan, but no controller has sensed a prospective environmental need, compared adaptation options and returned a chosen capability change to current work.
- Why this is / is not agent-owned: Skill file CRUD and hot reload are mechanisms for carrying a user-selected change. Tool learning/context management during a present task is not a prospective organizational adaptation loop.
- Evidence: [skill runtime scan](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/skills/manager.ts#L1-L150); [separate skill-management service and explicit no-runtime scope](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/skills/management-manager.ts#L1-L59); [agent context compression](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts#L1012-L1068).
- Basis: Bounded negative with developer-managed future adaptation possibility distinguished from shipped S4.
- Confidence: Medium-high.
- Caveats: An external agent using SDK tools to research future providers and update skills could create an S4 path in a larger system, but no such first-party feedback circuit is wired into this standard runtime.

### Absence scope

- Surfaces inspected: Skill loader, separate skill management service, provider abstraction, hooks, agent loop, docs/guides and scheduler.
- Plausible first-party paths checked: Dynamic file scan, manually installed skills, provider/model selection, context summarization, step callbacks and self-authored tools within a task.
- Why no material first-party path remains: The components either implement current S1 work or expose developer-facing capability management without prospective external sensing and an adoption-return loop.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/purpose-policy deliberation with legitimate returned binding governance is evidenced for the installed agent organization.
- Disturbance / variety regulated: Tool safety and permission conflicts are handled as routine task-level policy constraints, not identity-level disputes between present execution and future adaptation.
- Decisive decision or feedback right: A developer sets permission mode and allowed tools; an external user can approve/deny a pending tool call through `agent.decide`. Neither is a runtime ultimate-policy question with organizational deliberation and returned identity governance.
- Decision owner: Developer/application operator for configured constraints and individual API approval; no qualified first-party S5 agent or parent identity authority.
- Supporting / enforcement mechanisms: `PermissionManager` allow/deny/ask, mode handlers, system prompt, `agent.decide`, sandbox configuration, tool registration and agent template.
- Closure path: Pending tool request → ordinary user/API permission decision → resume or deny the tool. This closes a single operational authorization, not a policy/identity issue with legitimate parent decision and return.
- Why this is / is not agent-owned: The model must obey runtime permission decisions, but these are preconfigured or call-by-call; a restrictive system prompt or human approval does not itself implement S5.
- Evidence: [permission evaluation](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent/permission-manager.ts#L1-L35); [API permission resolution](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/agent.ts#L547-L567); [template-based constraints](https://github.com/shareAI-lab/kode-agent-sdk/blob/2596118805d8968c7e33cc437e440721833e9689/src/core/template.ts).
- Basis: Bounded negative after checking parent-governed and autonomous S5 paths.
- Confidence: Medium-high.
- Caveats: The external hosting application's human owner may legitimately supply S5 in a broader organization, but that application's identity-policy escalation and return are not installed with the SDK.

### Absence scope

- Surfaces inspected: Permission manager/modes, `agent.decide`, agent templates/system prompts, sandbox settings, tool registry and API docs.
- Plausible first-party paths checked: Individual tool approvals, static allow/deny rules, configured prompt governance, manual skill/provider changes and runtime monitoring.
- Why no material first-party path remains: No identity-level issue is escalated to legitimate ultimate authority and returned as an enacted binding organizational decision; the evidenced circuits concern local operational permissions.

## Distributed OSS parent arrangement

The people maintaining this library and the developers using it do not form one installed runtime organization. Contributor governance, repository review and releasing packages cannot be substituted for parent S3/S4/S5 modes. The SDK exposes an API for user-managed authorization but not a whole-system identity-policy return.

## Self-hosted and non-human modes

Self-hosted sandboxes, SQL/JSON persistence and API/provider adapters give an operator deployment choices. Non-human `Agent` actors choose model/tool action during individual tasks; using `Room` or a coordinator template does not supply an independent S2/S3 metasystem. No first-party multi-agent, no-human policy mode has been shown to close S3, S4 or S5.

## Recursion

An `Agent` instance performs a locally bounded task and may spawn nested agents; the code enforces a recursion-depth limit but does not establish each child as a viable organization with its own independent metasystemic control. This assessment keeps the SDK composed execution as system-in-focus and does not elevate tool calls or nesting depth into VSM recursions.

## Variety and escalation

The model/tool/observation loop absorbs task variety. `monitor` error/timeout and `control` permission events inform the host and can cause task-level pause/retry/deny. Such event channels are not evidence by themselves of an exceptional algedonic escalation to independent organizational S3/S4/S5 authority, or a collective intervention returning to affected S1 units.

## Evidence gaps

- Source structure and documented installed SDK APIs were inspected at the exact frozen revision. No live LLM, model provider, benchmark or multi-agent tool run was performed; effectiveness and actual absence of deployed downstream control are not inferred.
- The assessment intentionally excludes an embedding application's own coordinator, independent verification, conflict arbiter, strategic skill updater and identity governance. These could change vectors only under a separately declared installed system boundary and first-party evidence.
- Negative states mean no material qualifying path in this standard distribution after inspecting plausible shipped surfaces, not universal impossibility. Provider behavior and user-written prompt content cannot be credited as first-party S2–S5 ownership.
