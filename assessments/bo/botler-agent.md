---
harness_id: botler-agent
project_name: botler-agent
repository: https://github.com/crossoverJie/botler-agent
review_ref: 6dd4986fd236f75053f15905f66adcb0df9a8431
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# botler-agent

## Review boundary

- System in focus: the shipped Go personal task agent, model/tool execution, dispatch chain, recurring scheduler and optional local WebUI control of active/scheduled tasks.
- Purpose and identity: handle small user messages and reminders against isolated, user-described data subprojects with bounded file/script/schedule actions.
- Relevant environment: Telegram/Feishu/WeChat requests, subproject conventions and JSON files, competing inbound tasks, scheduled commitments, model/API failures and local host availability.
- Standard-distribution boundary: built `botler` executable or published container with first-party `internal/agentrt`, `runner`, `dispatch`, `tools`, `scheduler`, `safety`, task logs, WebUI and monitor; external model provider and messaging networks provide endpoints.
- Credited operating / distribution surfaces: model-driven Go task runtime, dispatch serialization/recovery, shared DATA_ROOT, optional scheduler task agents and WebUI schedule overview, run histories and user task-commitment updates.
- Adjacent first-party surfaces excluded from ownership: test-only fake runtime and parity drivers, TypeScript predecessor/reference implementation, repository CI/release scripts, sample data-template submodule, external platform accounts, and ordinary maintainer governance.
- First-party operating / deployment modes considered: CLI one-shot, persistent messaging, `SCHEDULER_ENABLED=1` recurring jobs, optional `WEBUI_ENABLED=1` operator-supervised schedule and run portfolio, local/Docker data mounts.
- Recursion level: distinct short-lived model-governed task executions in a shared personal DATA_ROOT, with an optional user-controlled scheduled-task portfolio; each request is not a separate full viable organization.
- Reviewed revision: `6dd4986fd236f75053f15905f66adcb0df9a8431`.
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

`cmd/botler` configures the agent runtime and channel/scheduler/web services. The `runner` uses a model routing decision to choose data subprojects, assembles their `AGENTS.md` conventions and invokes `agentrt.Loop`: model → allowlisted read/write/edit/run/schedule tools → observed outputs → further model decisions. Each message is a fresh bounded agent, optionally with recent conversation memory. `dispatch` processes inbox and scheduled tasks through a single serialized chain; after execution it checks actual JSON state, may attempt a model self-heal, and commits changed data. The scheduler can trigger model tasks or deterministic scripts. The optional WebUI exposes task logs, schedule overview/history and update APIs to an operator, with saves waking the scheduler. These are actual packaged runtime surfaces, unlike the nearby parity driver and TS migration reference. [runtime](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/agentrt/loop.go), [runner](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/runner/runner.go), [dispatch](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/dispatch/dispatch.go), [WebUI schedules](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/webui/wire.go).

## Operational model

The model decides each task's data project and ordinary tool actions; the runtime enforces directory/scripts limits and serializes competing tasks. Distinct short-lived task agents may be enqueued from multiple channels and the scheduler. The lock specifically prevents simultaneous mutation of a shared data root, but coordination discretion is fixed by framework construction, not owned by an agent. In the optional WebUI mode the human operator sees schedules and outcomes across this bounded portfolio and can authoritatively change queued/future recurring commitments; deterministic scheduler reload applies those changes. Syntax checks/self-heal are routine task validation, not a sufficiently independent complementary auditor; schedules are execution timing, not prospective environmental adaptation.

## S1 — Operations

- State: A
- Function: autonomous local data maintenance and short-scoped user-task execution via model-selected first-party file, script and scheduling tools.
- Disturbance / variety regulated: varied incoming requests, ambiguous project scope, changing files, failed tools and short conversation history.
- Decisive decision or feedback right: model routes a request to a project and then chooses subsequent available tools and arguments against observations.
- Decision owner: provider-backed model reached through first-party `agentrt.Runtime` and `Loop`; developer/user supplies fixed limits and initial task.
- Supporting / enforcement mechanisms: bounded tool turns, controlled `DATA_ROOT` paths, recent-context loading, provider adapter, per-project instructions and post-write validation.
- Closure path: inbound message or scheduler reminder → model routing → model/tool cycle → returned tool observations → next model turn or final result/changed data.
- Boundary reachability: the documented CLI, channels and scheduled message mode invoke `runner.RunTask` and the bundled Go `agentrt.Loop`; no external coding-agent harness is required.
- Why this is / is not agent-owned: the model has discretionary route, action and continuation choices while tool restrictions and validation enforce developer/user limits.
- Evidence: [two-phase routing and execution](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/runner/runner.go), [loop and tool-call feedback](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/agentrt/loop.go), [supported user operation](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/README.md).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: no configured provider credential or live IM delivery was exercised; source reaches the loop in supported modes.

## S2 — Coordination

- State: C
- Function: prevent conflicting independent short-lived task agents from mutating shared `DATA_ROOT` concurrently.
- Disturbance / variety regulated: competing IM, CLI and scheduler arrivals could overlap writes/JSON commits in the same data subproject and corrupt each other's task output.
- Decisive decision or feedback right: first-party `dispatch.chain` grants only one task permission to enter the mutation/validation/commit section; a waiting task starts only after release.
- Decision owner: fixed developer-designed serialization rule, **not** a model-selected S2 coordinator; a different conflict policy would need an explicitly composed agentic coordination owner.
- Supporting / enforcement mechanisms: buffered one-token channel, `acquire`/`release` for both model and scheduled-script dispatch, deduplication and scoped validation.
- Closure path: competing task arrivals → all mutation-capable tasks acquire the same token → previous task commits/releases → next agent task starts against settled data.
- Boundary reachability: shipped `Dispatch` and `DispatchScriptedTask` share the chain in the supported channel/scheduler/CLI operating path, so collision attenuation is not a developer-only example.
- Why this is / is not agent-owned: the interference and damping relation are structurally explicit, but deterministic lock ownership provides no autonomous negotiation or policy choice; hence constructor `C`, not `A`.
- Distinct S1 units: separately enqueued model task agents from independent message/channel/scheduler requests, including independently routed project contexts.
- Inter-S1 disturbance: overlapping writes to the same shared data root and validation/commit sequence could destroy another task's data consistency.
- Attenuating coordination relation: common dispatch token serializes every task capable of shared writes, including direct scheduled scripts.
- Feedback into subsequent S1 behaviour: release after validation/commit unblocks the next queued agent to read and act on the post-task file state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the lock is deliberately attached to the shared-data mutation boundary to prevent competing autonomous task writers from overlapping; it is not merely selecting which model receives a message.
- Evidence: [explicit shared-write exclusion and serial queue](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/dispatch/dispatch.go), [fresh task-agent creation](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/runner/runner.go), [scheduler reuses dispatch](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/scheduler/engine.go).
- Basis: structural, specific collision/attenuation witness.
- Confidence: medium.
- Caveats: a series of ephemeral agents is weaker evidence for stable simultaneous S1 identities than a multi-agent team; the symbol claims the supplied S2-specific serialization constructor, not a deployed agent-owned coordinating intelligence.

## S3 — Inside-and-now control

- State: P
- Function: let the personal operator inspect a whole schedule/task-run portfolio and revise which recurring commitments are active and when they execute.
- Disturbance / variety regulated: failures, obsolete reminders, clashing recurrent workload expectations and unintended outstanding task commitments across projects.
- Decisive decision or feedback right: user/operator reviews schedule overview, task histories and run statistics and saves updated enabled/disabled tasks, timing or assignments in the first-party WebUI.
- Decision owner: legitimate parent human operating this personal assistant in optional WebUI/scheduler mode; the model's `schedule` tool is ordinary S1 execution, and the scheduler enforces the chosen plan.
- Supporting / enforcement mechanisms: WebUI schedule overview, schedule history/stats, config save endpoint, persistent `schedules.json`, scheduler `Reload` and task logs/health metrics.
- Closure path: current schedule/run evidence → operator revises shared future/current task commitments in WebUI → validated schedule save and scheduler wake/reload → changed triggering or suppression of subsequent agent tasks.
- Boundary reachability: optional WebUI+Scheduler is a documented first-party local/container mode, and `webui/wire.go` connects schedule Save/Overview/History to the active scheduler store, not a separate external service.
- Why this is / is not agent-owned: the choice over which commitments remain enabled belongs to the human; automated polling and queue ordering cannot own this current-control right.
- Whole-system current view: WebUI provides task-log list, schedule overview, per-schedule run histories/stats and monitoring across the bounded personal assistant deployment.
- Current-control decision scope: save/replace global schedule entries and immediately reload the live scheduler, changing execution priority/time and active commitments in subsequent runs.
- Evidence: [WebUI run and schedule endpoints](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/webui/server.go), [wired schedule save/reload and overview](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/webui/wire.go), [scheduler live reload and fire](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/scheduler/engine.go), [documented optional WebUI/scheduler mode](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/README.md).
- Basis: structural optional parent operating mode.
- Confidence: medium.
- Caveats: this is a narrow schedule/commitment control plane, not a general dynamic resource allocator; no autonomous whole-system S3 mode was established, so standalone `P` is used.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary operational audit/feedback channel beyond routine task validation is established.
- Disturbance / variety regulated: malformed JSON or unsafe writes trigger `ValidateState` and a bounded same-agent repair attempt; the check does not independently verify requested goal truth.
- Decisive decision or feedback right: deterministic JSON parser detects malformed files; original model is re-invoked with a fix prompt, not an independent audit decision owner.
- Decision owner: routine dispatcher and same provider-backed task agent, with no separate complementary auditor.
- Supporting / enforcement mechanisms: `safety.ValidateState`, tool restrictions, self-heal retry, task logs and WebUI monitoring.
- Closure path: post-task parse failure → original agent repair request → revalidation/commit or reported failure; ordinary validation inside the same task lifecycle.
- Why this is / is not agent-owned: filesystem reading is real evidence but routine syntax validation and same-agent self-heal are not an independent S3* challenge to ordinary S1 results.
- Evidence: [dispatch revalidation and same-agent repair](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/dispatch/dispatch.go), [JSON syntax gate](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/safety/validate.go).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: manual WebUI review can disclose failures but no independent corrective audit authority is attached.

### Absence scope

- Surfaces inspected: state validator, same-run heal, task logs, WebUI histories, runtime model feedback and acceptance/parity test drivers.
- Plausible first-party paths checked: independent post-write JSON parse, model retry with a fix, health monitor and task history inspection.
- Why no material first-party path remains: checks are routine operational validity gates or passive displays; they do not independently challenge agent achievement and return an auditor-owned corrective decision to current control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally prospective environment modeling with adaptation-option feedback into current capability is shipped.
- Disturbance / variety regulated: new messages and calendar changes are immediate tasks; optional holiday-calendar updates change fixed scheduled firing times.
- Decisive decision or feedback right: model solves a current reminder/task; configured scheduler computes triggers, while no actor decides strategic future system capability from external opportunities.
- Decision owner: task model and deterministic schedule system, not a prospective adaptation owner.
- Supporting / enforcement mechanisms: recent conversation context, externalized project instructions, holiday refresh and editable schedules.
- Closure path: observed dates/messages alter current task execution or next scheduled fire, without S4 future-option development and return to S3 capability.
- Why this is / is not agent-owned: recording future execution time is scheduling, not external-and-future organizational intelligence.
- Evidence: [schedule semantics and calendar refresh](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/scheduler/engine.go), [model task pipeline](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/runner/runner.go).
- Basis: bounded negative.
- Confidence: high.
- Caveats: the user can externally rethink project conventions based on experience; no first-party S4 closure is credited.

### Absence scope

- Surfaces inspected: scheduler/holiday updates, project prompt, conversation context, tool list, model routing, monitor and documentation.
- Plausible first-party paths checked: periodic task scheduling, external calendar lookup, data project self-description, adaptive model routing and error retries.
- Why no material first-party path remains: all affect current/known tasks, without a future-environment distinction → option evaluation → changed organizational capability loop.

## S5 — Policy and identity

- State: —
- Function: no ultimate purpose/identity decision path with legitimate authority and returned policy closure is established.
- Disturbance / variety regulated: file/path restrictions, project conventions, trusted scripts, and channel credentials are tool safety and scope constraints.
- Decisive decision or feedback right: user edits `.env`, project `AGENTS.md` and standing schedule permissions; routine tool refusal or config edit is not an identity-level adjudication.
- Decision owner: developer or personal user for static setup and normal task mandates, not an evidenced S5 organizational policy tribunal.
- Supporting / enforcement mechanisms: data allowlists, restricted script runner, per-project instructions, JSON validator and config.
- Closure path: forbidden tool actions fail and prompts constrain behavior; no genuine identity-policy conflict is escalated to an ultimate authority and returned as changed policy to subsequent runs.
- Why this is / is not agent-owned: broad human control rights and natural-language project files are not sufficient for S5 without a function-specific decision and return.
- Evidence: [README security/design boundaries](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/README.md), [restricted tools](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/tools/index.go), [project selection/prompt](https://github.com/crossoverJie/botler-agent/blob/6dd4986fd236f75053f15905f66adcb0df9a8431/internal/runner/runner.go).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: external owner can replace the whole assistant purpose, but the shipped runtime has no dedicated identity-governance feedback loop.

### Absence scope

- Surfaces inspected: user prompts, project rules, config/WebUI, tool restrictions, scheduler and model run lifecycle.
- Plausible first-party paths checked: project instructions, task routing changes, approval/config edits, schedule authority and model self-heal.
- Why no material first-party path remains: each observed decision concerns task execution, permissions or current commitments rather than identity/ultimate-policy adjudication with returned governing decision.

## Distributed OSS parent arrangement

Maintainers and external users operate independent DATA_ROOT installations with no shared organization-level task/control plane. The `S3=P` claim is explicitly local to one operator-controlled installation and its schedule portfolio, not OpenSiro-like distributed OSS governance.

## Self-hosted and non-human modes

CLI and channel-only deployments retain model-owned S1 plus deterministic task serialization; optional installed WebUI/scheduler supplies the parent S3 oversight mode. No autonomous S3 mode, outside-and-then S4, or ultimate-policy S5 actor was identified. Containerized scheduling is not an autonomous governing parent.

## Recursion

Each new task uses a fresh agent over one selected data project. Shared serialization relates these operational cells, but there is no evidence that each cell contains its own full VSM or that the messaging platforms are subsidiary organizations.

## Variety and escalation

Model errors, tool-turn cap, JSON-invalid state and process panic receive bounded fallback/retry/repair handling. Persistent task logs allow local operator attention; no separate algedonic channel is inferred solely from health metrics or status transitions.

## Evidence gaps

Source inspection establishes the optional WebUI/scheduler wiring but not a field observation of a user changing commitments; the narrow S3 parent claim is therefore medium-confidence. The S2 constructor claim depends on treating distinct queued short-lived task agents as S1 units and records that limit explicitly. No provider or IM E2E test was run.
