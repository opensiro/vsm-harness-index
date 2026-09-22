---
harness_id: qwenpaw
project_name: QwenPaw
repository: https://github.com/agentscope-ai/QwenPaw
review_ref: 8af8b6e31a837a0e19ee6c9fffaf1c6b44b5f9ec
reviewed_at: 2026-09-22
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-22
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: P
---

# QwenPaw

## Review boundary

- System in focus: one self-hosted QwenPaw installation at pinned revision `8af8b6e31a837a0e19ee6c9fffaf1c6b44b5f9ec`, including QwenPaw-owned agent/runtime wiring, workspace/persona surfaces, scheduling and heartbeat, Hub/model-service quota mediation, governance/tool approvals, proactive helper, channels, skills/plugins and multi-agent management.
- Purpose and identity: provide a local personal-agent operating environment that can answer and act across channels, execute configured work without a fresh user turn, coordinate access to shared model capacity, anticipate future user needs and keep installation identity/control under the self-hosting user.
- Relevant environment: user conversations and behavior, local workspace/persona files, configured agents, scheduled time, external web/desktop evidence, model-provider capacity and responses, tools/channels, persistent memory and the local operator.
- Standard-distribution boundary: QwenPaw-owned Python package and shipped optional/full extras. AgentScope 2.0 and ReMe are separately maintained dependencies; their internal agent/memory decisions are not imported as QwenPaw ownership. External model providers, MCP/A2A/ACP peers/runners, Codex/Qoder and other externally hosted agents remain outside the boundary.
- Credited operating / distribution surfaces: `src/qwenpaw/app/crons/executor.py`; `src/qwenpaw/runtime/tool_guard.py`; `src/qwenpaw/app/routers/agents.py`; `src/qwenpaw/hub/model_service/limiter.py`; `src/qwenpaw/cli/doctor_checks.py`; `src/qwenpaw/cli/doctor_cmd.py`; `src/qwenpaw/agents/memory/proactive/proactive_responder.py`; persona/workspace loading and Console editing surfaces; built-in multi-agent/cron skills and first-party configuration around those paths.
- Adjacent first-party surfaces excluded from ownership: CI/release infrastructure, tests and Creator tooling are corroborative only unless reached by the installed runtime. ReMe auto-dream internals and AgentScope internals are dependency behavior and are not credited as QwenPaw-owned S4/S1 decisions. External coding-agent and peer-agent autonomy is not borrowed through integration.
- First-party operating / deployment modes considered: interactive/channel chat, scheduled agent jobs through CronExecutor, heartbeat/proactive operation, multiple configured QwenPaw agents, Hub/model-service operation, Console/operator administration, `qwenpaw doctor`, persona bootstrap/editing and first-party tool approval modes.
- Recursion level: one QwenPaw installation is the system-in-focus. Configured QwenPaw agents and scheduled autonomous jobs may act as distinct S1 units where they produce separate operational outcomes; external peer agents remain environmental systems.
- Reviewed revision: `8af8b6e31a837a0e19ee6c9fffaf1c6b44b5f9ec`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

QwenPaw is shipped as a self-hosted Python application with a `qwenpaw` CLI and first-party app/runtime modules. The pinned `pyproject.toml` packages `src/qwenpaw`, publishes an explicit `hub` extra, includes that extra in `full`, and registers the CLI. The pinned CLI exposes `qwenpaw hub` and `qwenpaw doctor` as shipped control/diagnostic surfaces, so these paths are part of the supported QwenPaw distribution rather than adjacent repository experiments.

The runtime supports ordinary conversational/channel operation and unattended work. `CronExecutor` creates a QwenPaw request context for an agent job, allocates or reuses a session, invokes the workspace stream query, tracks trace/session state, and delivers the result through QwenPaw channels. That first-party closure establishes autonomous S1 operation without importing autonomy from Codex, Qoder or external peer systems.

QwenPaw also exposes several metasystemic surfaces. Hub's shared limiter protects model-provider quota shared across connections/aliases; Console and APIs expose installation-wide agent state, enablement and approval/control paths to the local operator; `qwenpaw doctor` independently probes underlying installation reality without mutation; the proactive helper derives likely future tasks from recent evidence, gathers fresh evidence and injects a useful proactive result back through QwenPaw; and persona bootstrap/editor paths let the user resolve durable identity and boundary choices that are loaded into later system prompts.

## Operational model

A user, channel, timer or proactive trigger reaches a configured QwenPaw workspace/agent. QwenPaw assembles context, applies tool/governance policy, invokes the configured model/runtime path, records session/trace state and routes resulting output. Scheduled agent jobs therefore can execute and deliver without a contemporaneous user message.

When multiple QwenPaw operations consume a shared Hub model-service quota, the first-party `SharedLimiter` aggregates the shared quota scope, tracks concurrent activity and per-minute starts, and attenuates overload by admitting, rejecting with `429`, or applying cooldown. This is a constructor coordination mechanism: the repository supplies the S2-specific relation and enforcement, but no autonomous coordinator owns a discretionary S2 judgment.

The self-hosting user remains the installation-wide parent controller and ultimate identity authority. QwenPaw supplies current-state/control surfaces and asks for approval where policy requires it, while the user decides current enablement, approvals and durable persona/boundary choices. A separate read-only diagnostic plane can challenge nominal health/configuration claims and return findings to that parent control layer.

## S1 — Operations

- State: A
- Function: autonomously execute configured conversational or scheduled objectives and close their outputs through QwenPaw-owned session, trace and delivery paths.
- Disturbance / variety regulated: heterogeneous user/channel requests, scheduled objectives, changing workspace/memory context, tool/model responses and delivery conditions.
- Decisive decision or feedback right: choose the substantive response/action sequence for an admitted objective under the configured model, context and tools.
- Decision owner: the model actor reached through the QwenPaw workspace/runtime for the active configured agent.
- Supporting / enforcement mechanisms: CronExecutor, workspace `stream_query`, session allocation, trace collection, tool guard, channel manager, scheduler/heartbeat plumbing and persistent workspace/context state.
- Closure path: user/channel/timer trigger → QwenPaw request/session/context → model-owned operational decision → tool/response execution → trace/session persistence and channel delivery → later operation can consume the resulting state.
- Boundary reachability: scheduled `task_type=agent` jobs are an ordinary first-party CronExecutor path and invoke the same QwenPaw workspace runtime without a fresh user turn.
- Why this is / is not agent-owned: the model actor makes the material operational choice; QwenPaw owns the trigger, context, governance and delivery closure. No external coding-agent or peer-agent autonomy is needed for the positive claim.
- Evidence: `src/qwenpaw/app/crons/executor.py`; first-party workspace/runtime invocation reached by that executor; channel/session/trace closure in the same path.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: some configured backends or integrations can delegate externally; only QwenPaw-owned runtime closure is credited here.

## S2 — Coordination

- State: C
- Function: attenuate interference among distinct QwenPaw S1 operations that share a constrained upstream model-service quota.
- Disturbance / variety regulated: concurrent and high-rate model starts across configured agents/connections/aliases that share one supplier quota and can saturate that common resource.
- Decisive decision or feedback right: admit a start now, reject/ask it to retry later, or hold the shared scope in cooldown according to the aggregated quota state.
- Decision owner: constructor-level first-party coordination mechanism (`SharedLimiter`); no autonomous coordinator owns discretionary S2 policy at this boundary.
- Supporting / enforcement mechanisms: shared quota-scope aggregation, active-count tracking, per-minute start history, strictest shared limit selection, `429` busy responses, retry metadata and cooldown after upstream overload.
- Closure path: sibling S1 operations contend for a shared model-service quota → Hub observes shared active/rate state → limiter attenuates starts/rejects/cooldown → subsequent S1 calls are admitted only under the returned coordination state.
- Boundary reachability: the frozen package ships the Hub as a `qwenpaw` CLI subcommand; `pyproject.toml` publishes the `hub` extra and includes it in the supported `full` installation, while `src/qwenpaw/hub/model_service/limiter.py` provides the shared limiter.
- Distinct S1 units: concurrently operating configured QwenPaw agents/jobs whose model starts traverse the same shipped Hub quota scope.
- Inter-S1 disturbance: sibling operations can concurrently consume the same constrained upstream model-service quota, producing a structurally evidenced shared-capacity collision and upstream overload/429 pressure.
- Attenuating coordination relation: `SharedLimiter` aggregates the shared quota scope, tracks active/rate state, applies the strictest shared limit and admits, rejects or cools down starts.
- Feedback into subsequent S1 behaviour: rejected starts receive retry/cooldown state, and later sibling starts are admitted only after the shared limiter state permits them.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping is tied to attenuation of a specific inter-S1 shared-resource interference class; generic sub-agent messaging, routing and delegation are not used as evidence.
- Why this is / is not agent-owned: QwenPaw owns a concrete coordination construction tied to a real shared-resource interference class, but the admission decision is deterministic host enforcement rather than an autonomous agent's coordination judgment. This supports `C`, not `A`.
- Evidence: `src/qwenpaw/hub/model_service/limiter.py`; `src/qwenpaw/cli/main.py`; `pyproject.toml`; multi-agent management surfaces establishing plural configured QwenPaw agents.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: generic sub-agent delegation and background queues are not used as S2 evidence. The positive mapping relies specifically on shared quota interference and its first-party attenuation loop.

## S3 — Inside-and-now control

- State: P
- Function: keep the current QwenPaw installation's active agent population, automation and risky tool execution within the operator's present-time control.
- Disturbance / variety regulated: agents that should be enabled/disabled, scheduled/heartbeat work, pending risky actions, backend/model state and current runtime conditions that require operator intervention.
- Decisive decision or feedback right: enable or disable configured agents, approve or deny gated actions, alter/stop current automation and choose current installation controls exposed through first-party Console/API/CLI surfaces.
- Decision owner: the local self-hosting user/operator as legitimate parent actor.
- Supporting / enforcement mechanisms: agent inventory/status/toggle API, Console controls, cron/heartbeat administration, tool-guard approval queue, runtime/session status and deterministic enforcement of returned decisions.
- Closure path: QwenPaw exposes current installation/agent/action state → parent operator decides a control intervention or approval → first-party API/runtime applies it → subsequent agent/tool operation proceeds under the changed current-control state.
- Boundary reachability: `src/qwenpaw/app/routers/agents.py` exposes configured agents with enabled/startup/backend/model state and mutation paths; first-party control surfaces apply parent changes to the managed installation.
- Why this is / is not agent-owned: QwenPaw supplies the installation-wide visibility and control surface but does not replace the parent with an autonomous whole-system controller. The decisive current-control rights remain with the operator, so the state is `P`.
- Evidence: `src/qwenpaw/app/routers/agents.py`; runtime/tool approval and cron/heartbeat administration paths.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: isolated settings or an approval prompt alone would not establish S3; the positive claim is the parent control relation spanning the active agent population and current automation/action state.
- Whole-system current view: the first-party management plane exposes all configured agents and their enabled/startup/backend/model state alongside automation and approval/runtime controls for the installation.
- Current-control decision scope: parent intervention over which agents/automations may run now and whether gated actions may proceed.

## S3* — Complementary audit

- State: C
- Function: challenge ordinary runtime and configuration-health claims through a complementary read-only diagnostic path that probes actual filesystem, process, provider, channel, workspace, skill, cron, memory and security state.
- Disturbance / variety regulated: latent divergence between what ordinary runtime/configuration surfaces imply and what the installation can actually read, reach, load or execute.
- Decisive decision or feedback right: produce an audit finding from raw diagnostic probes and expose concrete failure/hint information for corrective current control.
- Decision owner: constructor-level first-party diagnostic mechanism; QwenPaw supplies deterministic audit judgments and complementary access, but no autonomous auditor owns discretionary S3* judgment.
- Supporting / enforcement mechanisms: `qwenpaw doctor`, read-only `doctor_checks`, runtime health/API probes, raw config and workspace checks, provider/model connectivity checks, channel connectivity checks, skill/cron/memory/security diagnostics, and the separately invoked `doctor fix` repair path.
- Closure path: ordinary operation/configuration claims a usable installation → `qwenpaw doctor` independently probes underlying runtime/filesystem/connectivity state → failures and actionable hints are surfaced → operator/current-control paths can repair, reconfigure or restart → subsequent operation reflects the correction.
- Boundary reachability: `qwenpaw doctor` is a shipped first-party CLI command at the frozen revision; its checks explicitly run read-only against installed QwenPaw state and do not require an external evaluator or development-only actor.
- Why this is / is not agent-owned: the complementary diagnostic relation is real and specifically packaged, but the audit judgment is deterministic code and corrective authority remains outside an autonomous auditor. That establishes `C`, not `A`; Methodology 0.3.x does not publish a parent modifier for S3*.
- Evidence: `src/qwenpaw/cli/doctor_checks.py`; `src/qwenpaw/cli/doctor_cmd.py`; `src/qwenpaw/cli/doctor_connectivity.py`; separate repair path in `src/qwenpaw/cli/doctor_fix_runner.py`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary governance logs, traces and status endpoints are not themselves counted as S3*. The positive claim is limited to the deliberately read-only complementary `doctor` path; an autonomous independent auditor is not supplied.
- Claim being audited: that the configured QwenPaw installation and its agents/providers/channels/skills/cron/memory/security/runtime dependencies are actually healthy and usable, rather than merely configured or nominally running.
- Ordinary reporting path: normal agent/runtime status, configuration, traces, governance logs and service operation report the primary execution path.
- Complementary access path: `doctor` reads raw configuration/workspace/filesystem state, probes the running HTTP service and Python environment, checks provider/model reachability and inspects channel, skill, cron, memory and security conditions without mutating them.
- Independence boundary: the diagnostic CLI/check functions are outside the conversational model decision path and explicitly read-only; they access underlying operating reality directly, although they remain first-party deterministic QwenPaw code rather than a separate autonomous actor.
- Who acts on findings: the self-hosting operator/current-control layer uses reported FAIL/hint output and may invoke the separate `doctor fix` path, reconfigure the installation or restart affected components.

## S4 — Outside-and-then intelligence

- State: A
- Function: anticipate likely future user needs from recent operating evidence, gather fresh external/local evidence for those needs and return a useful intervention into later QwenPaw operation.
- Disturbance / variety regulated: changing recent user interests/work, likely near-future goals, stale knowledge and external/local conditions that could make a proactive intervention useful or irrelevant.
- Decisive decision or feedback right: infer and rank likely future tasks/queries from recent memory context, choose which candidate to investigate, determine whether newly gathered evidence is sufficient and decide whether to send a proactive result or remain silent.
- Decision owner: the first-party proactive model actor instantiated by QwenPaw's proactive responder.
- Supporting / enforcement mechanisms: recent-memory context builder, optional desktop evidence, task extraction, web/file/shell/browser retrieval tools, activity-abort checks, success/failure self-check and proactive Console delivery.
- Closure path: recent user/operating evidence → model derives likely future tasks → QwenPaw gathers fresh evidence/executes a candidate → model/runtime checks usefulness/completion → successful proactive message is posted into QwenPaw Console/chat → subsequent user/agent operation receives the prospective intervention.
- Boundary reachability: `generate_proactive_response` is first-party QwenPaw code reached by the supported proactive feature/background loop; it creates the proactive assistant, derives tasks and closes successful output through QwenPaw's own Console chat API.
- Why this is / is not agent-owned: enabling proactive mode is parent consent/configuration, but the substantive prospective judgment — what future need is likely, what to investigate and whether to speak — is made by the model actor. ReMe's separate auto-dream internals are not needed for this positive mapping.
- Evidence: `src/qwenpaw/agents/memory/proactive/proactive_responder.py`; proactive feature documentation at the reviewed revision.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ReMe-backed memory context is input evidence only; its internal memory-evolution algorithm is not credited to QwenPaw ownership.
- External distinction: the proactive path reads evidence beyond the current inside-and-now control state — recent user behavior plus optional desktop state and fresh web/file/tool evidence.
- Future / prospective distinction: the model infers likely next needs and investigates candidate work before a new user request requires that work.
- Adaptation option generated: choose and rank a likely future task/query, gather supporting evidence and decide whether a proactive intervention is useful enough to surface or should remain silent.
- Path back into current capability / S3: a successful prospective result is injected into first-party QwenPaw Console/chat for subsequent user/agent operation; activity-abort checks suppress stale interventions before delivery.

## S5 — Policy and identity

- State: P
- Function: establish and revise the QwenPaw agent's durable identity, behavioral principles, boundaries and user relationship that constrain future operation.
- Disturbance / variety regulated: ambiguity or drift about who the agent is, how it should behave, its style/tone, user preferences and durable behavioral boundaries.
- Decisive decision or feedback right: choose the durable identity/profile/boundary content and whether persona files participate in future system prompts.
- Decision owner: the local self-hosting user as legitimate parent actor.
- Supporting / enforcement mechanisms: `BOOTSTRAP.md`, `SOUL.md`, `PROFILE.md`, `AGENTS.md`, Console persona editor, enable/disable/reorder controls and hot-reload/system-prompt loading.
- Closure path: identity/boundary issue or initial bootstrap → parent conversation/editor resolves name/nature/style/preferences/boundaries → QwenPaw persists persona files/configuration → those files are loaded into later system prompts → subsequent S1/S4 behavior occurs under the returned identity policy.
- Boundary reachability: the persona system is documented as a standard workspace feature; bootstrap explicitly asks the user to resolve identity/preferences/boundaries and writes durable `PROFILE.md`/`SOUL.md`, while Console editing/hot reload changes later prompts.
- Why this is / is not agent-owned: QwenPaw supplies the identity-construction mechanism and can help elicit the choices, but the ultimate durable identity/boundary authority remains with the user. This is parent-governed S5, not autonomous S5.
- Evidence: `website/public/docs/persona.en.md`; shipped workspace persona files and Console persona editing/loading paths.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary system prompts or model settings are not counted by themselves; the positive mapping relies on the explicit parent identity/boundary resolution and durable return into future operation.
- Identity / ultimate-policy issue: agent name/nature/style, behavioral principles, relationship to the user, preferences and boundaries that should persist across future sessions.
- Ultimate authority in each claimed mode: in the claimed parent-governed mode, the self-hosting user can create, edit, enable, disable and reorder the durable persona surfaces and therefore retains ultimate identity authority.
- Return-to-operation path: saved persona files are hot-reloaded/loaded into subsequent system prompts and therefore constrain later operation.

## Recursion

QwenPaw can host multiple configured agents and can connect to external peer/sub-agent systems. This assessment treats one self-hosted installation as the system-in-focus and credits a configured QwenPaw agent or scheduled job as an S1 unit only where QwenPaw closes its operational outcome. External ACP/A2A/MCP/Codex/Qoder actors do not become QwenPaw-owned simply because the installation can route to them.

## Variety and escalation

QwenPaw has broad first-party variety across channels, scheduled work, tools, multiple agents, model backends, Hub quotas, persona, diagnostics and proactive behavior. Parent escalation appears in policy approvals and installation controls; these are classified by the function they close rather than treated as a separate VSM function. `qwenpaw doctor` adds a complementary read-only diagnostic path but remains constructor-level because no autonomous auditor owns its judgment.

## Evidence gaps

- S2 confidence depends on the credited Hub deployment mode. Its reachability is explicit in the pinned package/CLI, but installations that do not enable Hub simply do not exercise that S2 constructor path.
- S3* is constructor-level only: the shipped `doctor` path provides complementary read-only access and diagnostic judgments, but autonomous audit ownership is not established.
- S4 is based on QwenPaw's own proactive responder, avoiding a false transfer of ownership from ReMe's separately maintained memory-evolution internals.
- `SOUL.md` invites identity evolution, but runtime guidance and Console/bootstrap ownership keep the decisive ultimate-identity right with the parent user in the evidenced standard mode; autonomous S5 is therefore not claimed.

## Summary

QwenPaw provides autonomous S1 through first-party scheduled/workspace execution, constructor S2 through shipped Hub shared-quota attenuation, parent-governed S3 through installation-wide operator controls, constructor S3* through the shipped read-only `doctor` diagnostic plane, autonomous S4 through prospective proactive task inference/retrieval/return, and parent-governed S5 through durable persona identity and boundary closure.
