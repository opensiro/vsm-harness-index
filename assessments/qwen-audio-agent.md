---
harness_id: qwen-audio-agent
project_name: Qwen Audio Agent
repository: https://github.com/QwenAudio/qwen-audio-agent
review_ref: 7b5913a05666a6cab9681c301807206ffa66c106
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: P
---

# Qwen Audio Agent

## Review boundary

- System in focus: the first-party `qwen-audio-agent` Realtime Gateway / frontend-assistant harness at frozen revision `7b5913a05666a6cab9681c301807206ffa66c106`, including the shipped Realtime frontend prompt/tool contract, Gateway task lifecycle, backend-port/adapters, durable conversation/session state, personalization/memory and optional preference-learning pipeline.
- Purpose and identity: keep one realtime assistant continuously present in conversation while it directly answers or uses frontend tools and, when configured, delegates sustained environment work through one backend Agent without blocking the conversation; preserve bounded user personalization across sessions.
- Relevant environment: the current user/operator, Realtime model/provider, configured backend Agent/harness, tools/MCP and retrieval providers, clients/OS, local files and external services.
- Standard-distribution boundary: first-party Gateway, frontend instructions/tools, task/session/delivery machinery, backend integration contract, memory/personalization and preference-learning machinery are inside. External model-provider internals, configured backend Agent implementations and their private subagents/Sessions, external MCP/services and client environment are external actors even when reached through first-party adapters.
- Credited operating / distribution surfaces: standard Gateway with Realtime frontend model and tool registry; frontend-only and configured-backend product modes; TaskManager/task queue and BackendPort integration; default Markdown memory/personalization; optional documented `QWEN_AUDIO_PREFERENCE_LEARNING=on` mode; local operator-controlled `ASSISTANT.md` identity profile.
- Adjacent first-party surfaces excluded from ownership: repository tests/CI/release machinery, roadmap-only target architecture, contributor/governance workflows, benchmark/development surfaces and standalone scenario examples such as X-Omni except as corroboration of framework reachability.
- First-party operating / deployment modes considered: frontend-only realtime assistant; realtime assistant plus one configured backend Agent; optional cross-session preference learning; explicit user preference edit; local operator edit of instance-wide assistant profile. These are supported modes and are not assumed to be simultaneously active.
- Recursion level: the assessed whole is the qwen-audio-agent product runtime. The Realtime frontend model is the credited operational agent actor. A configured backend Agent is an adjacent integrated system; backend-private tools, agents and Sessions are not promoted into qwen-audio-agent VSM organs merely because the adapter can reach them.
- Reviewed revision: `7b5913a05666a6cab9681c301807206ffa66c106`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The public architecture defines one user-visible assistant with two product layers: a Realtime frontend for full-duplex conversation and bounded frontend tools, plus at most one configured backend Agent for sustained environment work. `spawn_thinking` accepts work asynchronously; the Gateway owns Task identity, FIFO/admission, lifecycle, persistence, permissions, progress projection, cancellation, result correlation and safe delivery back into conversation. The backend Agent owns its own execution strategy. Backend-internal tools, subagents and Sessions remain implementation details of that backend rather than extra qwen-audio-agent layers.

The Realtime model receives a first-party prompt and a dynamically available tool registry. It decides whether to answer directly, use a specialized frontend tool, or submit a background objective through `spawn_thinking`; it later consumes Gateway-provided results, pending input and permission requests. The architecture deliberately prevents the Realtime layer from choosing backend Sessions, execution modes, strategies, tools, Agents or subagents. Task status/progress is observable through Gateway records but ordinary progress is explicitly not control.

Personalization is separated into core policy, instance identity/persona, per-user preferences and durable facts. `ASSISTANT.md` is the operator-editable instance-wide default identity/personality/relationship/expression profile and is reloaded for later voice sessions. `USER.md` is a per-user personalization overlay; it cannot override task, permission or safety policy. Optional preference learning runs after sessions: a model-driven observer proposes bounded user traits from actual user utterances, candidates require cross-session confirmation and structural guards, a promoter writes accepted observations into `USER.md`, and later sessions receive those preferences in frontend context. Explicit user preferences use a distinct direct path and outrank inferred observations.

Primary evidence:

- [`README.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/README.md)
- [`docs/architecture/deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md)
- [`config/frontend-agent/PROMPT.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/config/frontend-agent/PROMPT.md)
- [`server/src/frontend/frontend-tools.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/frontend/frontend-tools.mjs)
- [`server/src/task/task-manager.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/task/task-manager.mjs)
- [`docs/reference/personalization.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/personalization.md)
- [`docs/reference/preference-learning.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/preference-learning.md)
- [`server/src/memory/module.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/module.mjs)
- [`server/src/memory/session-observer.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/session-observer.mjs)
- [`server/src/memory/learning/profile-observer.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/learning/profile-observer.mjs)
- [`server/src/memory/learning/preference-promoter.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/learning/preference-promoter.mjs)

## Operational model

A user turn reaches the Realtime frontend model with current conversation/runtime context, instance profile, user preferences and only the tools actually available in that deployment. The model chooses a direct conversational response or a concrete frontend tool action. Sustained work can be submitted to the Gateway as a self-contained objective for the configured backend Agent; task progress, required input, permissions, cancellation and final results return through structured Gateway state rather than model-authored lifecycle claims. The external backend controls how it performs that work, so backend-internal organizational functions are not borrowed into this assessment.

The same product also supports bounded adaptation and identity control across sessions. Optional preference learning autonomously infers a narrow user profile from completed conversations and applies only cross-session-confirmed observations to future frontend context. Separately, explicit user preferences and the operator-owned instance profile provide parent-governed adaptation and identity modes.

## S1 — Operations

- State: A
- Function: conduct realtime user-facing assistance by interpreting current conversation/context, choosing a substantive response or available frontend action, and incorporating returned tool/task results into later responses.
- Disturbance / variety regulated: changing user intent, conversational context, available capabilities, tool/retrieval results, task status/results, pending clarification/permission state, attachments and persistent personalization.
- Decisive decision or feedback right: choose whether to answer directly, invoke an available specialized frontend tool, submit sustained work through `spawn_thinking`, ask a necessary question, or incorporate a returned result into the next response.
- Decision owner: the configured Realtime model acting as the frontend agent under the shipped first-party prompt/tool contract.
- Supporting / enforcement mechanisms: Gateway Realtime transport, frontend tool registry, capability gating, task/status/permission envelopes, conversation/session persistence, memory context and deterministic tool execution.
- Closure path: user/context input → Realtime model selects response/tool action → first-party Gateway executes or routes the action → result/state returns into model context → later model response/action.
- Boundary reachability: the Realtime frontend and tool registry are the standard shipped user-facing runtime and remain operational even in frontend-only mode; no backend-private agent or repository-development actor is needed for this S1 path.
- Why this is / is not agent-owned: removing model discretion while retaining the Gateway/tool machinery eliminates the substantive choice among direct response, tool use and delegation; deterministic runtime code validates, routes and executes the selected action rather than making an equivalent conversational/task decision itself.
- Evidence: [`PROMPT.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/config/frontend-agent/PROMPT.md); [`frontend-tools.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/frontend/frontend-tools.mjs); [`deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model-provider cognition is outside the repository implementation boundary; the credited autonomy is the supported first-party model/context/tool feedback loop around that agent actor. Backend Agent work is not needed to establish S1 and its internal autonomy is not imported.

## S2 — Coordination

- State: —
- Function: no material first-party coordination function was established that attenuates a specific interference/oscillation among distinct credited S1 operational units.
- Disturbance / variety regulated: the candidate S2 disturbance would be destructive interference among multiple autonomous operational units; the reviewed first-party product boundary instead exposes one credited Realtime S1 and one optionally integrated external backend system.
- Distinct S1 units: multiple Task records, queued requests and backend Sessions are not automatically S1 units. Backend-private subagents/Sessions belong to the configured external backend unless independently brought inside the declared boundary.
- Inter-S1 disturbance: no specific first-party disturbance among two or more credited qwen-audio-agent S1 units was established.
- Attenuating coordination relation: owner FIFO scheduling, backend write serialization, task claims and delivery deduplication regulate runtime races and lifecycle ordering but are generic infrastructure mechanisms rather than an established inter-S1 coordination relation.
- Feedback into subsequent S1 behaviour: no function-specific S2 mutual-adjustment closure was established.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the repository explicitly uses queues, Session correlation and delegation to move/order work; Methodology 0.3.6 does not treat those surfaces as S2 without distinct S1 units plus a concrete cross-unit interference witness.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: TaskScheduler, per-owner FIFO queue, backend serialization lock, renewable delivery claims, Task registry and delegation correlation.
- Closure path: not established for an S2 function.
- Boundary reachability: not applicable because no positive S2 function is published.
- Why this is / is not agent-owned: the frontend can delegate work and the external backend can create private Sessions, but task decomposition/routing does not by itself regulate a specific disturbance among qwen-audio-agent operational units.
- Evidence: [`deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md); [`task-manager.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/task/task-manager.mjs).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: a configured backend may internally contain multiple coordinated agents; those backend-private arrangements are not first-party qwen-audio-agent S2 evidence.

### Absence scope

- Surfaces inspected: product architecture, Realtime/backend boundary, TaskManager/scheduling, backend Session/delegation contract, task claims/result delivery, cancellation/permission flow and documented backend-internal coordination tools.
- Plausible first-party paths checked: foreground-vs-background execution, multiple queued Tasks, per-owner serialization, delegated backend Sessions, coordinator Session tools, result claims/deduplication and backend write locks.
- Why no material first-party path remains: every reviewed mechanism is routing, task lifecycle, race prevention, delivery ownership or integration with an adjacent backend. No concrete interference among distinct credited qwen-audio-agent S1 units plus returned mutual-adjustment path is established.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control function was established over multiple operational units' shared resources, commitments, priorities, accountability or synergy.
- Disturbance / variety regulated: the Gateway tracks task lifecycle, capacity and permissions, but these do not establish discretionary whole-system regulation of current operations at the assessed recursion.
- Whole-system current view: TaskManager can enumerate and persist current Tasks, and the Realtime frontend can query task status, but the architecture intentionally withholds backend Session topology, execution strategy, tools, Agents and subagents from the frontend control surface.
- Current-control decision scope: users/models can query or cancel a selected Task and relay explicit permission/input responses; static schedulers enforce capacity. No first-party actor is shown bargaining/revising whole-system resources, priorities or commitments across autonomous operational units.
- Decisive decision or feedback right: not established for S3.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: TaskManager, TaskScheduler, cancellation state machine, permission policy, progress/status projection, backend locks and restart recovery.
- Closure path: no S3-level whole-system control loop established.
- Boundary reachability: not applicable because no positive S3 function is published.
- Why this is / is not agent-owned: the Realtime model can request status/cancellation but explicitly cannot select/create/continue/cancel backend Sessions, choose execution mode/strategy, or select backend tools/Agents/subagents. Deterministic Gateway controls enforce lifecycle rather than exercise organizational S3 discretion.
- Evidence: [`deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md); [`PROMPT.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/config/frontend-agent/PROMPT.md); [`task-manager.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/task/task-manager.mjs).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: current-task cancellation and permission approval are real control actions but remain below the S3 threshold because they do not reconstruct a whole-system current-control function at this boundary.

### Absence scope

- Surfaces inspected: frontend prompt/tools, TaskManager/TaskScheduler, task status/cancellation, permission policy, backend coordinator/Session tools, progress projection, recovery and client commands.
- Plausible first-party paths checked: Realtime assistant as manager, Gateway task controller, user/operator cancellation, permission decisions, backend coordinator Session management and static concurrency limits.
- Why no material first-party path remains: the reviewed paths regulate individual task lifecycle or enforce predetermined limits; none combines a whole-system present view with discretionary authority over shared operational commitments/resources on behalf of the whole.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path was established that challenges ordinary operational claims and returns findings into subsequent control.
- Disturbance / variety regulated: the candidate S3* disturbance would be uncertainty that ordinary task/model reporting matches actual operational reality; first-party validation focuses on normal lifecycle integrity rather than a separate complementary audit function.
- Claim being audited: Task completion, delegation correlation, permissions, memory-learning evidence and delivery state all receive deterministic validation, but these are ordinary execution/data-integrity claims in their primary paths.
- Ordinary reporting path: backend protocol events, Gateway Task records, frontend tool results, model/user conversation and memory-learning observations.
- Complementary access path: not established. Exact delegation/result correlation, `stopReason` completion gating, audit logs and structural preference guards inspect the same operational path or provide diagnostics rather than an independent alternative view of reality.
- Independence boundary: no first-party auditor with materially different access from the producing operational path was found in the credited distribution.
- Who acts on findings: routine runtime code rejects invalid/stale lifecycle or learning inputs; diagnostic audit records can be inspected by an operator, but no complementary-audit finding loop into S3 is established.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: delegation correlation, completion-state validation, memory-audit log, sensitive-content/evidence guards, delivery claims and protocol validation.
- Closure path: no complementary S3* closure established.
- Boundary reachability: not applicable because no positive S3* function is published.
- Why this is / is not agent-owned: model- or runtime-based checks inside the normal production/learning path do not become S3* merely because they reject bad state; materially independent access and audit feedback are missing.
- Evidence: [`deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md); [`profile-observer.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/learning/profile-observer.mjs); [`preference-learning.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/preference-learning.md).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: repository tests and scenario validation are adjacent development/evaluation surfaces and are not borrowed as runtime S3*.

### Absence scope

- Surfaces inspected: Task lifecycle/correlation, backend completion handling, permission/input validation, result claims, memory audit, preference-learning structural guards, tests/docs describing validation and progress observability.
- Plausible first-party paths checked: independent task verifier, audit-log feedback, protocol reconciliation, preference evidence validation, scenario observation and repository test/evaluation surfaces.
- Why no material first-party path remains: reviewed runtime checks are ordinary in-path integrity gates or diagnostics; adjacent test/example surfaces do not supply an operationally reachable complementary auditor whose findings regulate subsequent current operation.

## S4 — Intelligence / adaptation

- State: A(P)
- Function: adapt future assistant behaviour to stable user characteristics and long-term interaction preferences learned or explicitly selected across sessions.
- Disturbance / variety regulated: user characteristics and preferred interaction style can remain unknown, change, or differ from the instance-wide default; blindly carrying one fixed persona/reply strategy across future sessions would lose environment-relevant variety.
- External distinction: the evidence comes from the external user/environment — user utterances and explicit preference settings — rather than from internal task-planning state alone.
- Future / prospective distinction: accepted observations/preferences are persisted specifically to influence later interactions; inferred promotions are not injected back into the just-ended session, and direct profile edits are documented to apply to subsequent voice sessions.
- Adaptation option generated: in autonomous mode, `ProfileObserver` uses a text-model call to infer bounded candidate values for occupation, special skills, response length and response style from actual user utterances; candidates are cross-session-confirmed and promoted into the observed section of `USER.md`. In parent mode, the user/operator explicitly selects a durable personalization change such as preferred name/language/reply style/default behavior.
- Path back into current capability / S3: promoted or explicit `USER.md` content is composed into later frontend instructions as `<user_preferences>` and has higher personalization precedence than the default assistant profile, changing later Realtime model behaviour; explicit tool writes can update the active preference context while direct file edits apply on later sessions.
- Decisive decision or feedback right: base mode — the observer model makes the substantive semantic inference from user evidence, while deterministic quote/field guards and multi-session promotion thresholds validate/enforce when that option may become durable. Parent mode — the legitimate user/operator directly decides the long-term personalization setting/correction and first-party memory machinery returns it into future frontend context.
- Decision owner: base mode — model-driven `ProfileObserver`; parent mode — current user/operator for their durable personalization overlay.
- Supporting / enforcement mechanisms: candidate pool/store, evidence anchoring guards, ≥2-confirmation/≥2-session promotion gate, `PreferencePromoter`, owner-serialized memory writes, `USER.md`, memory provider/runtime and frontend context composition.
- Closure path: completed sessions → model observer infers candidate from user evidence → candidate accumulates independent cross-session confirmations → promoter persists accepted preference → later frontend context loads preference → subsequent agent responses operate under the adapted preference. Parent mode: explicit durable preference/correction → memory tool/API/direct edit → persisted `USER.md` → subsequent frontend context/behaviour.
- Boundary reachability: both paths are first-party documented product modes at the frozen revision. Autonomous preference learning is optional/off by default but enabled through the supported `QWEN_AUDIO_PREFERENCE_LEARNING=on` configuration; explicit long-term personalization is part of the standard conversational/product interface.
- Why this is / is not agent-owned: in the autonomous mode, removing the observer model while leaving storage, guards and thresholds intact eliminates the substantive inference that proposes what environmental/user distinction should change future behaviour; deterministic machinery validates and promotes that model-generated option rather than inventing an equivalent preference itself. The distinct parent mode intentionally gives that adaptation judgment to the user/operator.
- Evidence: [`preference-learning.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/preference-learning.md); [`personalization.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/personalization.md); [`profile-observer.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/learning/profile-observer.mjs); [`preference-promoter.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/learning/preference-promoter.mjs); [`session-observer.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/session-observer.mjs); [`module.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/module.mjs); [`frontend-tools.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/frontend/frontend-tools.mjs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: autonomous learning is deliberately narrow, optional and limited to four user-trait fields; this state does not claim general self-modification, model training, tool evolution or strategic environmental research.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | model-driven `ProfileObserver` | supported preference-learning mode after a completed session with enough user evidence | inferred candidate → structural validation/cross-session confirmation → automatic promotion to `USER.md` → later frontend context changes behaviour | `profile-observer.mjs`, `preference-promoter.mjs`, `session-observer.mjs`, `preference-learning.md` |
| Parent (`P`) | current user/operator | explicit long-term personalization setting or correction | explicit preference → first-party memory write/edit → persisted `USER.md` → current/subsequent frontend context follows returned setting | `personalization.md`, `PROMPT.md`, `module.mjs`, `frontend-tools.mjs` |

## S5 — Policy and identity

- State: P
- Function: maintain the assistant instance's default identity/persona at the assessed product recursion.
- Disturbance / variety regulated: the deployment may require a different stable assistant name, personality, relationship stance or expression style while preserving one coherent instance-wide default across sessions and users' overlays.
- Identity / ultimate-policy issue: what default assistant identity/personality/relationship stance/expression style this deployed qwen-audio-agent instance presents when not superseded by a legitimate per-user personalization override.
- Ultimate authority in each claimed mode: the deployment user/operator controlling the local `ASSISTANT.md` (or configured assistant-profile path) is the parent authority for this identity surface. No autonomous first-party S5 owner is claimed.
- Return-to-operation path: first launch materializes the packaged assistant-profile template; the parent edits the local profile; qwen-audio-agent preserves it across upgrades and loads it into `<assistant_profile>` for later voice sessions; the first-party instruction hierarchy then makes that profile govern default identity/persona while keeping core tool/permission/safety/task policy non-overridable by persona or memory.
- Disturbance / variety regulated: identity/persona changes are separated from per-user memory and from core operational policy so a deployment-level identity decision can persist without being confused with task permissions or transient conversation state.
- Decisive decision or feedback right: choose the instance-wide default assistant identity/personality/relationship/expression profile that subsequent sessions receive.
- Decision owner: parent deployment user/operator.
- Supporting / enforcement mechanisms: local `ASSISTANT.md`, configurable profile path, template-on-first-launch behavior, upgrade preservation, `resolveAssistantProfile`/frontend context composition and prompt authority hierarchy.
- Closure path: identity/persona decision → parent edits supported local profile → runtime reloads profile on subsequent session → Realtime frontend receives it as authoritative persona-default context → subsequent behaviour reflects returned identity decision.
- Boundary reachability: `ASSISTANT.md` is a documented standard local configuration surface at the frozen revision, not a repository-maintainer/development-only file; the normal frontend instruction builder loads the resolved assistant profile into operating sessions.
- Why this is / is not agent-owned: the runtime and model consume/enforce the selected profile but do not hold the ultimate right to change the instance-wide profile through the memory/learning path. Documentation explicitly prevents memory from editing `ASSISTANT.md`; the decisive identity choice remains with the parent operator.
- Evidence: [`personalization.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/personalization.md); [`deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md); [`frontend-tools.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/frontend/frontend-tools.mjs); [`PROMPT.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/config/frontend-agent/PROMPT.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this S5 credit is intentionally limited to instance identity/persona. Ordinary backend permission approval, task cancellation, static core prompt text and per-user preferences are not used as S5 witnesses.

## Distributed OSS parent arrangement

Repository maintainers and contributors are not imported into the runtime S3/S4/S5 boundary merely because they develop the project. The positive parent modes here are local to a supported deployed assistant: the current user/operator owns their durable personalization (S4 parent mode) and the deployment operator owns the instance-wide assistant profile (S5). This does not claim organization-level governance over the upstream OSS project.

## Self-hosted and non-human modes

The standard self-hosted/local distribution can run without a backend Agent and still retains the Realtime S1. Preference learning is an optional supported mode rather than a requirement for every deployment. A deployment may omit the parent customization paths by never editing durable preferences/profile, but their supported reachability is sufficient to publish the first-party parent modes. No non-human S5 mode was established.

## Recursion

Backend Agents may internally create tools, Agents or Sessions, and the first-party adapter can correlate delegated target Sessions. The architecture explicitly treats those as backend-private implementation details rather than additional qwen-audio-agent layers. No child unit was shown to contain its own complete VSM metasystem at the assessed boundary, so spawning/delegation is not published as VSM recursion.

## Variety and escalation

The product attenuates user/runtime variety through capability-gated tools, one stable user-facing assistant, structured Task records, bounded permission/input channels, deterministic lifecycle validation, per-owner scheduling, persistence/recovery, result claims and strict separation between persona, user preferences, memory and core policy. It amplifies response capacity through optional retrieval/tools and a configured backend Agent while preserving the backend boundary.

Escalation paths include sustained work from Realtime to the configured backend, backend clarification/input back to the user, explicit permission requests to the user, and cancellation/status control. These channels transport variety; they are not promoted to S2/S3/S5 unless the corresponding function-specific closure is independently established.

## Evidence gaps

- Proposed vector: `S1=A / S2=— / S3=— / S3*=— / S4=A(P) / S5=P`.
- S1 is bounded to the first-party Realtime frontend agent loop; configured backend-harness autonomy is not imported.
- S2 remains negative despite queues/locks/delegation because no concrete interference among distinct credited qwen-audio-agent S1 units was established.
- S3 remains negative despite status/cancel/permission controls because the frontend lacks whole-system operational authority and Gateway scheduling is deterministic enforcement.
- S3* remains negative because lifecycle validation/audit logs are ordinary in-path integrity/diagnostic mechanisms rather than a complementary independent audit loop.
- S4 credit is specifically the optional cross-session preference-learning loop plus a distinct explicit-user parent adaptation path, not generic memory persistence.
- S5 credit is specifically the parent-owned instance identity/persona loop through `ASSISTANT.md`; task permissions and ordinary personalization do not establish S5.
