---
harness_id: synapscli
project_name: SynapsCLI
repository: https://github.com/HaseebKhalid1507/SynapsCLI
review_ref: 62853b06777fcc16db4b142d535a99e23da4b207
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SynapsCLI

## Review boundary

- System in focus: installed SynapsCLI terminal-native Rust agent runtime and its bundled agent actors, model/tool feedback loop, subagent orchestration, optional unattended watcher and session daemon, at the frozen revision.
- Purpose and identity: conduct open-ended user/automated tasks with an LLM choosing tools and follow-on actions, optionally through multiple model-driven subagents.
- Relevant environment: user workspaces, local files/processes, configured model endpoints, tools/plugins/MCP servers, daemon clients and task feedback.
- Standard-distribution boundary: `synaps` chat/TUI/RPC/daemon/watcher plus first-party `agent-engine`, `agent-core`, tool and subagent implementations. Actual model service and task content are runtime inputs, not separately owned organizational units.
- Credited operating / distribution surfaces: provider-round/tool-result engine, foreground model actor, independently driven subagents, scope-aware orchestration registry, model-visible subagent tools and host-enforced write/completion gates; watcher mode is considered without inheriting its external configuration.
- Adjacent first-party surfaces excluded from ownership: upstream models' internal training/policy organizations, plugin implementations authored by downstream users, developer CI/benchmarks, repository release workflow and test agents.
- Modes considered: direct interactive and headless chat, daemon/RPC clients, model-driven parallel delegation with read-only/isolated/nonoverlapping write scopes, unattended watcher and autonomous session driver, optional user steering.
- Recursion level: one SynapsCLI agent session with an optional multi-agent workgroup; watcher manages sessions at a wider operations boundary, not an automatic S3/S4/S5 owner.
- Reviewed revision: `62853b06777fcc16db4b142d535a99e23da4b207`.
- Observation date: 2026-10-29.
- Generated Profile/Methodology: 0.2.4 / 0.3.7; current Profile/Methodology: 0.2.4 / 0.3.7.

## Repository architecture

The engine's `run_stream_internal` retains conversation history and repeatedly calls the provider, dispatches model-requested tools, appends tool results and continues until completion, stop or budget. The model is the task-level actor; the Rust engine is its tool, model, event and history substrate. `subagent_start` spawns another configured model-driven runtime with its own task/prompt; `subagent_status`, `subagent_steer`, `subagent_collect` and `subagent_resume` expose current work to the foreground agent. The first-party orchestration policy tracks worker state, allowed models, write scopes, concurrency and completion/reconciliation. A foreground model may choose a worker's role/write policy, inspect results and revise current work, while deterministic host enforcement blocks overlapping writes and unreconciled completion.

Primary source at exact frozen ref:

- [README and operating modes](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/README.md).
- [LLM/tool feedback cycle](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/crates/agent-engine/src/runtime/stream.rs).
- [Subagent launch, task/model/role/write scope](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/crates/agent-engine/src/tools/subagent/start.rs).
- [Terminal result and reconciliation](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/crates/agent-engine/src/tools/subagent/collect.rs).
- [Policy, scope overlap, supervision lifecycle](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/crates/agent-core/src/orchestration.rs).
- [Runtime orchestration/handle mapping](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/crates/agent-engine/src/orchestration.rs).
- [Foreground write enforcement](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/crates/agent-engine/src/tools/write.rs) and [edit enforcement](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/crates/agent-engine/src/tools/edit.rs).
- [Bundled foreground supervision instruction](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/crates/agent-core/src/builtin_prompts/codex_subagent_supervision.md).
- [Unattended watcher session budgets/handoff](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/src/watcher_session.rs) and [watcher supervisor](https://github.com/HaseebKhalid1507/SynapsCLI/blob/62853b06777fcc16db4b142d535a99e23da4b207/src/watcher/supervisor.rs).

## Operational model

User or watcher supplies a goal. The foreground LLM reads observations and chooses a next tool, delegates a bounded subtask, or finishes. An agent worker receives its own prompt/history and can independently carry out model-selected operations. Progress, cancellation, tool results and terminal worker output re-enter the foreground's context. Scope declarations permit parallel work while host gates prevent a foreground edit from colliding with an active worker's declared file scope; the returned rejection or reconciliation drives a revised decision. Model-driven supervision can steer or resume drifted workers, then collect their output and reconcile commitments before completion.

## S1 — Operations

- State: A
- Function: foreground and optionally spawned worker agents absorb open-ended coding/terminal task variety through repeated model decisions, tool execution and observed results.
- Disturbance / variety regulated: uncertain file/process/tool results, task decomposition and changing intermediate evidence in each worker's environment.
- Decisive decision or feedback right: choose model-requested tools and follow-on tasks from returned observations, including whether to continue or finish.
- Decision owner: model-driven foreground/worker agent inside the shipped runtime; an external model endpoint supplies inference but the tool-action loop is first-party wired.
- Supporting / enforcement mechanisms: provider adapters, tool registry, stream events, sessions, budgets, daemon, context checkpointing and cancellation.
- Closure path: goal/history → LLM tool choice → first-party tool execution → tool result added to history → next provider round / final response.
- Why this is / is not agent-owned: tool choice and next action are not prewritten as a deterministic workflow; the model acts on feedback, including inside subagent runtime.
- Evidence: `crates/agent-engine/src/runtime/stream.rs`, `tools/subagent/start.rs` and README (pinned links above).
- Basis: direct source-first control-flow inspection.
- Confidence: high.
- Caveats: task correctness depends on the selected model, tools and user permissions; a model-less session does not exercise S1.
- Boundary reachability: shipped chat/TUI/RPC foreground stream and spawned subagent stream, using the standard bundled tool registry.

### Boundary reachability

- Mode and entry: shipped `synaps chat`/TUI/RPC uses first-party engine; foreground can invoke bundled subagent tools.
- Reachable owner: configured model makes provider-round/tool calls and separate worker models execute their own streams without a downstream developer supplying an agent implementation.
- Closed return: tool results and worker outputs are sent back into conversational context before subsequent decisions.

## S2 — Coordination

- State: A
- Function: attenuate concrete file-write interference between concurrently active autonomous work units within a shared workgroup.
- Disturbance / variety regulated: concurrent foreground/worker modifications to the same file/path, plus worker output arriving after foreground completion.
- Decisive decision or feedback right: choose worker isolation/write scopes and adjust work after a collision/reconciliation signal; worker-collect/reconcile is a separate foreground coordination act.
- Decision owner: foreground LLM when it selects `write_policy` for `subagent_start`, steers/rescopes work and decides what to reconcile; host registry enforces matching scopes and returns a refusal. This does **not** credit deterministic scope matching itself as autonomous judgment.
- Supporting / enforcement mechanisms: `WorkerWritePolicy`, `check_foreground_write`, overlap predicate, `write`/`edit` rejection and subagent completion gate.
- Closure path: foreground chooses nonoverlapping scopes → concurrent agent work → overlapping foreground write is rejected with a concrete error → model receives that result and must avoid/reconcile the collision before continuing; terminal worker result is collected and reconciled before completion.
- Why this is / is not agent-owned: unlike mere subagent delegation, the scope choice and handling of a concrete collision remain in the model's next-action loop; host rejection is evidence of an actual structurally implemented inter-S1 interference path.
- Evidence: `tools/subagent/start.rs`, `agent-core/src/orchestration.rs`, `tools/write.rs`, `tools/edit.rs`, `tools/subagent/collect.rs` (pinned links above).
- Basis: source-structural coordination witness, without an observed live multi-agent collision.
- Confidence: medium-high.
- Caveats: isolated worktree/read-only modes avoid the collision structurally, and incorrect agent scope declarations may fail to protect files outside their scope.
- Distinct S1 units: an autonomous foreground model loop and an independently streamed subagent model loop share a task workspace; further workers may run concurrently.
- Inter-S1 disturbance: foreground `write`/`edit` can target paths that a still-running worker declares writable, risking simultaneous edits to one work product.
- Attenuating coordination relation: model-chosen `write_policy` scope/isolation and registry's active-worker overlap check block a colliding foreground write.
- Feedback into subsequent S1 behaviour: the foreground receives the failed write as a tool result and can steer, collect or reconcile worker work before retrying or rescoping.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the exact overlap predicate and file-write rejection regulate concurrent operational interference, beyond mere messaging or dispatch.
- Boundary reachability: bundled subagent dispatch and file-write tools use the same orchestration policy at runtime, without a plugin or downstream workflow definition.

### Boundary reachability

- Mode and entry: bundled `subagent_start` exposes `write_policy` and permits at least two live S1 loops; `write`/`edit` consult the shared orchestration instance.
- Reachable owner: the foreground model chooses tool parameters and responds to the error; no custom extension is required.
- Closed return: denied write surfaces as a tool error in the agent loop; collect/reconcile changes subsequent allowed completion.

## S3 — Inside-and-now control

- State: A
- Function: regulate current commitments and accountability across active subagent work on behalf of the whole foreground task.
- Disturbance / variety regulated: slow/stalled or diverging workers, exhausted concurrency/total-worker capacity, finished-but-unreconciled work and conflicting current implementation responsibilities.
- Decisive decision or feedback right: inspect worker statuses and partial output, steer or resume a worker, decide which work to dispatch and whether results are reconciled with the foreground objective.
- Decision owner: foreground model exercising bundled `subagent_status`/`steer`/`collect`/`resume` tools; user may intervene, while the registry only tracks/enforces quotas and completion.
- Supporting / enforcement mechanisms: model catalog/authorization, typed worker roles, worker status telemetry, runtime handle registry, budget/worker-count gates and prompt supervision guidance.
- Closure path: model dispatches several current commitments → reads status/progress/completion → chooses steering/resumption or integration → collected result updates current task context and explicit reconciliation releases completion gate.
- Why this is / is not agent-owned: host logic does not choose which task is off-track or how to revise it; the foreground actor observes all subagents and has real steer/dispatch/collect authority over their current work.
- Evidence: `tools/subagent/start.rs`, `tools/subagent/collect.rs`, `agent-engine/src/orchestration.rs`, `agent-core/src/orchestration.rs`, bundled supervision prompt and stream completion gate (pinned links above).
- Basis: reachable first-party orchestration tools and feedback path.
- Confidence: medium-high.
- Caveats: foreground supervision is prompt-guided and optional in single-agent mode; watcher restart/budget enforcement alone is not S3 agent ownership.
- Whole-system current view: foreground can inspect all of its active worker handles, states, partial outputs and collected results through the shipped orchestration tools.
- Current-control decision scope: model can dispatch, set role/write policy, steer, resume and reconcile current work against the foreground outcome; host applies hard budget/limit gates.
- Boundary reachability: standard foreground tool registry wires subagent supervision and orchestration, and feedback returns into the same model stream.

### Boundary reachability

- Mode and entry: ordinary foreground runtime ships the subagent status/steer/collect/resume tool suite and shared orchestration; no external supervisor implementation is required.
- Reachable owner: the model can issue new guidance to a running worker based on its partial work and can accept/reconcile its terminal output.
- Closed return: steering enters the worker stream, terminal output enters the foreground stream and the host completion gate is released on reconciliation.

## S3* — Complementary audit

- State: —
- Function: no standard-distribution independent complementary access that challenges an S1 claim and returns audit findings into control is established.
- Disturbance / variety regulated: runtime traces, status and optional reviewer subagents can reveal errors, but are ordinary task/supervision paths.
- Decisive decision or feedback right: independently select an operational claim, inspect distinct evidence and return a corrective finding to current control.
- Decision owner: not supplied by the standard distribution; a foreground agent/user may request an optional reviewer, without a guaranteed independent challenge channel.
- Supporting / enforcement mechanisms: subagent `reviewer` role, partial-output/status reads, telemetry, tool events and debug logs.
- Closure path: ordinary worker report → foreground inspection or optional prompted review; no dedicated independent audit access and controlled corrective return is evidenced.
- Why this is / is not agent-owned: typed reviewer capability and logs do not establish S3* independence or a different view of operational reality.
- Evidence: `tools/subagent/start.rs`, `tools/subagent/collect.rs`, `agent-engine/src/orchestration.rs`, README.
- Basis: bounded structural negative review.
- Confidence: medium-high.
- Caveats: a specifically designed downstream reviewer workgroup may establish S3* and requires separate source evidence.

### Absence scope

- Surfaces inspected: subagent reviewer role, worker state/history, event/status telemetry, runtime feedback and watcher.
- Plausible first-party paths checked: reviewer label as independent auditor; separate subagent as alternate inspection; watcher healthchecks as audit.
- Why no material first-party path remains: these expose the normal worker/host path or programmable review primitives, not an independent claim-to-artifact challenge loop automatically reachable in this product mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: no packaged external/future sensing → adaptation option → operational capability-change loop is established.
- Disturbance / variety regulated: models/providers, task feedback, package/plugin capabilities and crash recovery are present-task or maintenance concerns.
- Decisive decision or feedback right: judge future environmental differences and revise the agent system's future capabilities in conversation with S3.
- Decision owner: user/operator/plugin author or downstream agent application; not a first-party S4 role.
- Supporting / enforcement mechanisms: provider catalog, plugins/extensions, MCP, watcher config reload, memory/compaction and project prompts.
- Closure path: tools/model/config can change on external instruction, but the repository does not ship a prospective model of environment and a dedicated adaptation option-to-present-control return.
- Why this is / is not agent-owned: context persistence, plugin extensibility, task planning and deterministic config reload are not prospective organizational intelligence by themselves.
- Evidence: README, `src/watcher/supervisor.rs`, `crates/agent-engine/src/runtime/stream.rs`.
- Basis: bounded structural negative review.
- Confidence: medium-high.
- Caveats: some specific user-created long-running watchers might implement future adaptation; not inferred from runtime generality.

### Absence scope

- Surfaces inspected: runtime tool/model loop, session memory/compaction, watcher reload/trigger, extension/plugin mechanisms and README modes.
- Plausible first-party paths checked: memory/self-improvement, provider selection, plugin installation, unattended watcher decisions and external event handling.
- Why no material first-party path remains: these paths do not themselves select future-directed adaptation options and return them to present capability governance.

## S5 — Policy and identity

- State: —
- Function: no identity- or ultimate-policy decision path with legitimate authority and returned governing closure is established.
- Disturbance / variety regulated: model eligibility, session budgets, credential scope, system prompts, tool confirmations and worker write rules constrain operations.
- Decisive decision or feedback right: decide the identity, legitimate authority boundaries and ultimate policy if operational/future tensions require resolution.
- Decision owner: user/operator/configurator at a wider boundary; runtime enforces predefined limits and explicit session grants.
- Supporting / enforcement mechanisms: `DelegationPolicy`, `CrossProviderGrant`, `EnforcementMode`, credential broker, user approval, prompt and role budgets.
- Closure path: user-supplied settings/grants → deterministic enforcement → agent operation; no identity-level issue is routed to ultimate authority and returned as a revised policy decision in the shipped workflow.
- Why this is / is not agent-owned: policy text and runtime authorization cannot be promoted to S5 merely because they constrain agent autonomy.
- Evidence: `agent-core/src/orchestration.rs`, README, `src/watcher_session.rs`.
- Basis: bounded structural negative review.
- Confidence: high.
- Caveats: parent organizations may impose real S5 through an embedding deployment, outside the frozen standard-distribution boundary.

### Absence scope

- Surfaces inspected: delegation grants, policy authorization, model/worker catalogs, system prompt, user approval, credential broker, watcher budgets.
- Plausible first-party paths checked: static identity prompt as policy, user model grant as ultimate-policy return, worker quotas as governance and watcher limit enforcement as S5.
- Why no material first-party path remains: all are task-level operating constraints and authority supplied outside the harness, not a durable identity-level decision and closure channel.

## Recursion

Subagents can be locally autonomous S1 units inside the foreground workgroup, but worker role labels, recursive spawning and provider selection do not establish an independently viable six-function organization at each recursion level.

## Variety and escalation

Model choice attenuates open-ended task variety into tool calls; scoped parallel work and explicit collection attenuate collisions and unfinished commitments. Quota exhaustion, denied writes, worker failures and budget stops return control signals to the foreground or user. These signals are not automatically algedonic/identity-level channels.

## Evidence gaps

- Static inspection at the frozen SHA; no paid-provider, live multi-agent conflict or external process/daemon E2E run. The S2 interference relation is structurally explicit in code.
- Provider selection, local tools, dangerous process paths and plugin commands vary by configuration. Actual performance and policy safety are not established by this structural VSM mapping.
- The S3* negative is about the standard supplied composition, not a prohibition on constructing a separate independent reviewer via the available agent tools.

## Assessment summary

**Proposed disposition: `included`.** SynapsCLI packages a first-party, model-driven task/tool feedback loop and a reachable multi-agent operating mode with concrete overlap attenuation and foreground current-control powers. Bounded six-function vector: **A · A · A · — · — · —**. The S2/S3 claims credit model-level scope/supervision decisions while distinguishing deterministic runtime enforcement; no packaged independent complementary audit, prospective adaptation or ultimate identity-policy closure is shown.
