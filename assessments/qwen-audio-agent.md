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

- System in focus: the first-party qwen-audio-agent realtime voice harness at frozen revision `7b5913a05666a6cab9681c301807206ffa66c106`, including the Realtime frontend agent, Gateway, frontend tool registry, Task lifecycle/scheduling/permission runtime, protocol-neutral backend integration, durable conversation/session state, and shipped memory/personalization surfaces where they are reachable in supported deployment modes.
- Purpose and identity: present one continuous conversational assistant that can answer directly, use foreground capabilities, delegate sustained work to one configured backend Agent, track that work, return results into conversation, and preserve supported long-term personalization across sessions.
- Relevant environment: the current user/operator, realtime model provider, configured backend Agent implementation, local files and client environment, MCP/OpenAPI/tool providers, memory/knowledge providers, network services and changing user preferences.
- Standard-distribution boundary: qwen-audio-agent's Gateway, Realtime agent contract, Task/permission lifecycle, backend adapters and memory/personalization modules are inside. The cognition and internal topology of a selected Qwen Code/OpenCode/OpenClaw/other backend, remote A2A implementation, external model/service internals, MCP servers and user/operator judgment remain external actors even when first-party qwen-audio-agent paths transport their decisions.
- Credited operating / distribution surfaces: ordinary Realtime conversation/tool execution; the Gateway `spawn_thinking`/Task path to one configured backend Agent; task status/cancellation/permission closure; the default Markdown personalization/memory implementation; the optional first-party preference-learning mode enabled by `QWEN_AUDIO_PREFERENCE_LEARNING=on`; and the supported local `ASSISTANT.md` identity profile path.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests, contributor/release machinery, roadmap material, diagnostics as development evidence, standalone scenario/example-specific logic such as X-Omni and smart-cockpit behavior, and any subagents/tools/sessions internal to the selected backend Agent. These may corroborate architecture but do not donate VSM ownership to the standard qwen-audio-agent runtime.
- First-party operating / deployment modes considered: frontend-only Realtime mode; ordinary Realtime plus one configured backend Agent; user-supervised backend permissions/cancellation; default explicit personalization/memory; optional preference-learning mode; and local operator-owned assistant-profile configuration. These are supported modes and need not all be enabled simultaneously.
- Recursion level: the assessed whole is one qwen-audio-agent assistant runtime. Its persistent backend coordinator Session and backend-private subagents/sessions are not treated as qwen-audio-agent recursive viable systems merely because they can be nested or delegated to.
- Reviewed revision: `7b5913a05666a6cab9681c301807206ffa66c106`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The product architecture deliberately exposes one assistant while separating a Realtime frontend from one configured backend Agent. The Realtime agent handles full-duplex conversation and may answer directly or invoke available foreground tools. Work requiring sustained execution enters `spawn_thinking`, becomes a Gateway Task, passes through an owner-scoped queue and the protocol-neutral `BackendPort`, and is sent to the configured backend. The backend owns its internal execution strategy; qwen-audio-agent explicitly treats any backend tools, skills, agents or Sessions as backend-private rather than additional qwen-audio-agent layers.

The Gateway owns Task state, scheduling, persistence, recovery, permission routing, result correlation and cancellation. Multiple requests may be queued while conversation continues, but the product uses a fixed backend coordinator Session per owner/backend and serializes writes to that Session. Task records are delivery receipts rather than mirrors of backend-internal task graphs. Progress is explicitly observability rather than control.

Personalization is separated into an instance-wide `ASSISTANT.md` profile, a per-user directive overlay (`USER.md` in the default provider), and factual durable memory (`MEMORY.md`). The optional preference-learning mode observes a narrow set of user traits after a session, requires cross-session confirmation plus structural evidence guards, promotes accepted observations into the observed section of `USER.md`, and intentionally applies them to later sessions. The operator-owned `ASSISTANT.md` controls the assistant instance's default name, personality, relationship stance and expression style and is reloaded for subsequent sessions; the assistant cannot edit that file through its memory path.

Primary evidence:

- [`README.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/README.md)
- [`docs/architecture/deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md)
- [`config/frontend-agent/PROMPT.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/config/frontend-agent/PROMPT.md)
- [`server/src/frontend/tools/agent-task-runtime.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/frontend/tools/agent-task-runtime.mjs)
- [`server/src/task/task-manager.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/task/task-manager.mjs)
- [`server/src/task/permission-policy.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/task/permission-policy.mjs)
- [`docs/reference/personalization.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/personalization.md)
- [`docs/reference/preference-learning.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/preference-learning.md)
- [`server/src/memory/learning/profile-observer.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/learning/profile-observer.mjs)
- [`server/src/memory/learning/preference-promoter.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/learning/preference-promoter.mjs)
- [`server/src/memory/context.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/context.mjs)

## Operational model

A live user turn is interpreted by the Realtime agent under the fixed frontend contract. The model can answer directly, choose a currently exposed foreground tool, or create a backend Task when sustained work is needed. The Gateway validates tool availability, persists and schedules Task state, enforces permission/cancellation semantics, and returns observations/results that can affect later agent responses. A configured backend can perform substantial work, but its private subagents and internal strategy are not credited to qwen-audio-agent itself.

Durable personalization supplies two materially different organizational paths. In explicit mode, the user/operator directly establishes persistent preferences or instance identity. In optional preference-learning mode, an LLM observer proposes inferred user traits from actual user utterances, while deterministic evidence guards and a cross-session promotion threshold constrain whether those adaptation options become durable. Promoted preferences are injected into later Realtime contexts and therefore alter subsequent behavior.

## S1 — Operations

- State: A
- Function: carry out the assistant's user-facing operation by interpreting a live request, choosing a direct conversational response or reachable tool/delegation action, observing returned state/results and continuing the interaction toward an outcome.
- Disturbance / variety regulated: changing user intents, conversational context, available tool capabilities, local/remote execution requirements, task progress/results, permission/input requests and interruption or cancellation.
- Decisive decision or feedback right: choose whether to answer directly, invoke an exposed foreground capability, or submit sustained work through `spawn_thinking`, and choose subsequent conversational/tool actions from returned observations.
- Decision owner: the configured Realtime model acting through the first-party frontend-agent contract.
- Supporting / enforcement mechanisms: Gateway tool availability checks, TaskManager, BackendPort/adapters, transcript/context assembly, permission policy, result delivery, cancellation and client protocol.
- Closure path: user turn → Realtime model choice → direct response or first-party tool/Task submission → tool/task observation or backend result → updated Realtime context → subsequent agent response/action.
- Boundary reachability: the frontend-agent prompt and tool registry are core shipped runtime surfaces; the positive path does not depend on repository examples, benchmarks or a backend's private multi-agent topology.
- Why this is / is not agent-owned: removing the Realtime model's discretionary routing/tool/response choice while retaining Gateway queues and enforcement would not preserve materially the same operational decision. The runtime constrains and executes the choice but does not select the substantive conversational/action path itself.
- Evidence: [`config/frontend-agent/PROMPT.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/config/frontend-agent/PROMPT.md); [`docs/architecture/deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md); [`server/src/frontend/tools/agent-task-runtime.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/frontend/tools/agent-task-runtime.mjs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: work performed inside a selected backend Agent may have additional autonomous structure, but that backend-private autonomy is excluded from this S1 ownership claim.

## S2 — Coordination

- State: —
- Function: no material function-specific coordination relation among multiple distinct qwen-audio-agent S1 operational units was established at the reviewed boundary.
- Disturbance / variety regulated: the candidate S2 variety would be concrete oscillation, collision or destructive interference among distinct operational units; the reviewed queue/serialization mechanisms instead regulate concurrent requests entering one backend execution lane.
- Distinct S1 units: the standard architecture exposes one unified Realtime assistant plus one configured backend action Agent; backend-private subagents/Sessions are explicitly not additional qwen-audio-agent layers, and Task records are explicitly delivery receipts rather than operational units.
- Inter-S1 disturbance: no specific disturbance among multiple distinct qwen-audio-agent S1 units was established. Concurrent writes racing inside the one persistent backend Session are a request-serialization hazard, not an evidenced conflict among separate S1 units.
- Attenuating coordination relation: owner FIFO queue, lane limit and ACP write serialization prevent concurrent requests from racing inside the backend Session, but these are sequencing/concurrency controls for one execution path rather than an S2 mutual-adjustment relation among S1 units.
- Feedback into subsequent S1 behaviour: Task/result delivery changes later assistant behavior, but no S2-specific coordination result between distinct S1 units is returned.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is not S2-specific; the relevant mechanisms are routing, FIFO sequencing, session serialization and delegation.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: `TaskScheduler`, owner lane limit, backend Session serialization, delegation/result correlation and task-state persistence.
- Closure path: no S2 closure established.
- Why this is / is not agent-owned: the Realtime model may decide to delegate work, but delegation and choosing when to use a backend do not establish regulation of a concrete inter-S1 interference relation.
- Evidence: [`docs/architecture/deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md); [`server/src/task/task-manager.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/task/task-manager.mjs); [`server/src/frontend/tools/agent-task-runtime.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/frontend/tools/agent-task-runtime.mjs).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: a selected backend harness may itself coordinate multiple agents, but its internal S2 belongs to that adjacent system and is not inherited by qwen-audio-agent.

### Absence scope

- Surfaces inspected: architecture-defined Realtime/backend boundary, Task queue/scheduler, fixed backend coordinator Session, ACP delegation/session tools, result correlation, cancellation, permission policy and backend-private capability boundary.
- Plausible first-party paths checked: concurrent Task scheduling, multiple queued requests, frontend/backend handoff, delegated target Sessions, backend MCP Session tools, write serialization and shared Task state.
- Why no material first-party path remains: reviewed mechanisms either sequence requests through one backend lane, transport/delegate work, or expose backend-private coordination. No reviewed standard-distribution path establishes multiple distinct qwen-audio-agent S1 units plus a specific inter-unit disturbance, attenuation relation and returned coordination feedback.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control function was established that discretionarily regulates shared resources, commitments, priorities or accountability across qwen-audio-agent operational units.
- Disturbance / variety regulated: active Task lifecycle, concurrency, pending permissions and cancellations are regulated, but the reviewed boundary does not show whole-system organizational commitment/resource variety being discretionarily balanced on behalf of the whole.
- Whole-system current view: Task status can list recent work and expose active state, but it is a bounded work-status surface rather than a demonstrated whole-system operational view spanning the assistant's operations and external backend internals.
- Current-control decision scope: users can cancel one/series/all current-session Tasks and approve/reject pending operations; the Gateway also enforces concurrency and lifecycle rules. These are task-local or preconfigured supervisory controls, not an evidenced S3 bargaining/prioritization loop over shared operational commitments.
- Decisive decision or feedback right: not established at the S3 function threshold.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: TaskManager repository/status view, owner/session filters, scheduler limits, cancellation, permission grants, recovery and backend abort/correlation.
- Closure path: individual task cancellation and permission decisions do return to execution, but no whole-system S3 closure was established.
- Why this is / is not agent-owned: the Realtime model is explicitly forbidden from inventing permission decisions or controlling backend execution strategy; it relays user decisions. Deterministic Task machinery enforces lifecycle/concurrency rules selected in advance. Neither surface demonstrates autonomous S3 ownership.
- Evidence: [`server/src/frontend/tools/agent-task-runtime.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/frontend/tools/agent-task-runtime.mjs); [`server/src/task/task-manager.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/task/task-manager.mjs); [`server/src/task/permission-policy.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/task/permission-policy.mjs); [`config/frontend-agent/PROMPT.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/config/frontend-agent/PROMPT.md).
- Basis: explicit + structural negative finding.
- Confidence: medium-high.
- Caveats: the task-control surface is materially stronger than a passive UI, but Methodology 0.3.6 requires whole-system current regulation rather than treating cancellation, permission approval or deterministic concurrency enforcement as S3 by themselves.

### Absence scope

- Surfaces inspected: TaskManager/scheduler, status listing, all/single/series cancellation, permission-policy session/task grants, backend execution/cancellation, progress projections, persistent task recovery and frontend control instructions.
- Plausible first-party paths checked: Realtime agent as supervisor, user as parent supervisor, TaskManager as control plane, session-wide permission mode, all-task cancellation, concurrency gates and backend lifecycle ownership.
- Why no material first-party path remains: the first-party runtime exposes observation and intervention over individual/current-session work plus deterministic limits, but not a reconstructable whole-system S3 loop with discretionary authority over shared operational resources/commitments/priorities across distinct operations.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path was established beyond ordinary runtime validation, lifecycle correlation, logs and diagnostics.
- Disturbance / variety regulated: the candidate S3* disturbance would be uncertainty that ordinary Task/backend reporting reflects operational reality; reviewed checks validate the same protocol/runtime path rather than obtain materially independent access to reality.
- Claim being audited: task progress/completion, permission state, backend result correlation and runtime health can all be inspected or validated.
- Ordinary reporting path: Gateway Task state, adapter events, backend result correlation, structured progress and client-facing status.
- Complementary access path: not established. `doctor`, logs, memory audit and protocol validation inspect first-party runtime records or the same underlying provider/session surfaces.
- Independence boundary: no materially separate auditor, replay/ground-truth path or alternative access channel was found that can independently challenge the ordinary operational claims.
- Who acts on findings: users/operators and ordinary runtime code can respond to errors/status, but no complementary-audit judgment/feedback owner is established.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: validated delegation IDs, exact target-Session correlation, completion-state checks, structured logs, read-only diagnostics, memory audit records and cancellation confirmation.
- Closure path: ordinary runtime validation can fail/cancel a task, but no independent S3* finding-to-control closure exists.
- Why this is / is not agent-owned: no independent agent auditor is part of the supported standard boundary; normal Realtime/backend actors and deterministic validators remain inside the production path being observed.
- Evidence: [`docs/architecture/deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md); [`docs/configuration/advanced.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/configuration/advanced.md); [`server/src/frontend/tools/agent-task-runtime.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/frontend/tools/agent-task-runtime.mjs).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: repository tests may independently test implementation claims, but CI/test infrastructure is adjacent development evidence rather than an operational S3* path in the assessed assistant runtime.

### Absence scope

- Surfaces inspected: backend completion/delegation correlation, Task status/progress, logs, `doctor` diagnostics, permission records, memory audit, recovery and cancellation confirmation.
- Plausible first-party paths checked: independent verifier/auditor, replay or raw-artifact inspection path, diagnostics as complementary reality access, memory-learning audit and protocol-level cross-checks.
- Why no material first-party path remains: every reviewed operational check is part of the same production/runtime state path or a read-only diagnostic projection of it; no sufficiently independent complementary access plus returned audit judgment into subsequent control was established.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: adapt future assistant behavior to durable externally observed user characteristics/preferences by generating a bounded adaptation option, validating it across sessions and returning the accepted change into later Realtime capability; a distinct supported parent mode lets the user/operator directly choose long-term adaptation instead.
- Disturbance / variety regulated: stable changes or previously unknown distinctions in the user's occupation, skills and desired response length/style that should alter later interaction behavior without treating every transient utterance as a permanent preference.
- External distinction: evidence comes from the user's utterances, an environment external to the assistant runtime; the observer accepts only user-turn evidence and structurally rejects fabricated or unsupported quotations/inferences.
- Future / prospective distinction: inferred traits must persist across at least two distinct sessions before promotion, and promoted preferences intentionally take effect in later/new sessions rather than merely repairing the current turn.
- Adaptation option generated: the preference-observer model proposes a field/value/relation/basis for a bounded user-profile trait; in parent mode, the user/operator directly specifies the durable personalization change.
- Path back into current capability / S3: accepted observations enter the candidate pool → cross-session promotion writes the observed section of `USER.md` → `buildMemoryContext` injects it as `<user_preferences>` → the frontend prompt gives those long-term preferences precedence over instance defaults in later operation. Explicit parent/user preferences enter the same directive layer with higher authority than inferred observations.
- Decisive decision or feedback right: in the autonomous mode, the observer model decides what semantic user trait/adaptation option is supported by the external evidence; deterministic guards, promotion thresholds and write mechanics decide admissibility/stability but do not independently invent the adaptation content. In parent mode, the user/operator directly chooses the durable preference/default-behavior change.
- Decision owner: base mode — the first-party preference-observer LLM for the adaptation judgment, constrained by deterministic validation/promotion. Parent mode — the legitimate local user/operator governing the deployed personal assistant's durable personalization.
- Supporting / enforcement mechanisms: user-turn-only transcript construction, quote/value guards, sensitive-content rejection, candidate pool, confirmation count/session threshold, promoter, memory provider revisions, explicit-vs-observed precedence and memory-context assembly.
- Closure path: repeated user evidence → model-generated adaptation candidate → deterministic validation and cross-session confirmation → successful promotion to `USER.md` → preference context in a later Realtime session → subsequent responses governed by the accepted preference. Parent mode closes through explicit long-term user setting/direct edit → `USER.md` → subsequent context/behavior.
- Boundary reachability: both paths are shipped first-party surfaces. The autonomous base mode is optional but explicitly supported via `QWEN_AUDIO_PREFERENCE_LEARNING=on`; the parent explicit-preference path is part of the default personalization contract. Neither path borrows learning behavior from a selected backend Agent.
- Why this is / is not agent-owned: counterfactually removing the observer model while retaining the gates/pool/promoter leaves no actor able to infer the semantic adaptation option from conversation evidence; the deterministic machinery can only validate, count and persist options already proposed. Conversely, removing deterministic gates would weaken safety/stability but would not supply an equivalent semantic adaptation judgment. The base adaptation decision is therefore agent-owned with deterministic enforcement/support.
- Evidence: [`docs/reference/preference-learning.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/preference-learning.md); [`server/src/memory/learning/profile-observer.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/learning/profile-observer.mjs); [`server/src/memory/learning/preference-promoter.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/learning/preference-promoter.mjs); [`server/src/memory/context.mjs`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/server/src/memory/context.mjs); [`docs/reference/personalization.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/personalization.md); [`config/frontend-agent/PROMPT.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/config/frontend-agent/PROMPT.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: preference learning is off by default because it incurs an additional model call; `A(P)` records supported first-party ownership modes rather than claiming autonomous learning is active in every deployment. Generic factual memory consolidation is not used as S4 evidence.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Preference-observer LLM | Session-close observation when optional preference learning is enabled and enough user evidence is present | model candidate → structural guards/candidate pool → cross-session promotion → `USER.md` → later Realtime preference context | `preference-learning.md`; `profile-observer.mjs`; `preference-promoter.mjs`; `context.mjs` |
| Parent (`P`) | Local user/operator | Explicit durable personalization instruction or supported direct preference edit | explicit preference → `USER.md` directive layer → later/current supported context → subsequent assistant behavior | `personalization.md`; `PROMPT.md`; `context.mjs` |

## S5 — Policy and identity

- State: P
- Function: close the assistant instance's default identity at the local deployment recursion through a legitimate operator-owned profile whose decision is loaded back into subsequent operation.
- Disturbance / variety regulated: changes in the deployed assistant's intended default name, personality, relationship stance and expression style, while preventing user memory/personalization from rewriting core task, permission and safety protocol.
- Identity / ultimate-policy issue: the supported `ASSISTANT.md` profile defines the instance-wide default assistant identity/personality/relationship/expression stance; this is distinct from transient conversation state and per-user factual memory.
- Ultimate authority in each claimed mode: parent mode only — the local deployment owner/operator who edits the copied `ASSISTANT.md` or selects the supported assistant-profile path. The Realtime agent and memory learner are explicitly denied authority to modify this instance-wide profile through memory.
- Return-to-operation path: operator identity decision → local `ASSISTANT.md` / configured profile path → profile reloaded for the next voice session as the assistant-profile context → frontend instruction hierarchy applies it as the instance default → subsequent assistant operation follows that identity subject to higher-priority current/per-user overrides and immutable core protocol boundaries.
- Decisive decision or feedback right: choose the instance-wide default identity/personality/relationship/expression stance for the deployed assistant.
- Decision owner: legitimate local parent/operator; no autonomous S5 owner is established.
- Supporting / enforcement mechanisms: first-launch template copy, profile-path configuration, session context composition and fixed `PROMPT.md` hierarchy that constrains what the profile may override.
- Closure path: identity edit/configuration → next-session profile load → operative assistant-profile context → subsequent Realtime behavior.
- Boundary reachability: the local assistant profile is a documented shipped configuration surface used by ordinary Gateway sessions; the closure does not rely on contributor governance or repository-maintainer policy.
- Why this is / is not agent-owned: the assistant is explicitly unable to edit `ASSISTANT.md` through memory. Removing the human/operator authority leaves no first-party autonomous actor with the same legitimate instance-identity decision right; runtime code only loads and bounds the selected profile.
- Evidence: [`docs/reference/personalization.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/reference/personalization.md); [`docs/architecture/deep-dive.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/docs/architecture/deep-dive.md); [`config/frontend-agent/PROMPT.md`](https://github.com/QwenAudio/qwen-audio-agent/blob/7b5913a05666a6cab9681c301807206ffa66c106/config/frontend-agent/PROMPT.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this finding credits an explicit parent-governed identity loop, not the mere existence of a static prompt. Core tool/permission/safety policy remains fixed by the packaged prompt and is not claimed as autonomously governed S5.

## Recursion

The product deliberately maintains one qwen-audio assistant boundary. The configured backend has one persistent coordinator Session per owner/backend, and may internally use tools, skills, agents or target Sessions, but the architecture explicitly treats those as backend-private implementation details. Task IDs, delegated Sessions and spawned work therefore do not establish recursive qwen-audio-agent viable systems. A selected backend harness may independently deserve its own VSM assessment at its own boundary.

## Variety and escalation

Realtime attenuates conversational variety by choosing between direct handling, bounded foreground tools and backend delegation. The Gateway preserves structured Task identity/lifecycle and prevents model-authored lookalikes from becoming authoritative events. Backend permission and input requests escalate unresolved execution variety to the current user, whose response can return to the same Task; cancellation can stop queued/running/delegated work through confirmed runtime paths. These are important channels and constraints but are not promoted to S2/S3/S3* without their function-specific evidence.

The optional preference-learning path amplifies future regulatory capacity by turning repeatedly evidenced external user distinctions into durable personalization while structurally limiting unsupported inferences. Instance identity changes escalate to the local operator-owned profile rather than being delegated to the assistant itself.

## Evidence gaps

- The frozen review does not classify the VSM structure of Qwen Code, OpenCode, OpenClaw or any other selectable backend; their internal agents/Sessions remain adjacent systems.
- Optional preference learning is a supported first-party mode but is disabled by default. The `A(P)` state therefore denotes available ownership configurations, not a claim that every ordinary installation learns preferences autonomously.
- No first-party operational complementary-audit channel meeting S3* independence requirements was found; repository tests/CI remain adjacent development evidence.
- X-Omni and other scenario examples can add observation/scheduling behavior but are not used to upgrade the standard-distribution assessment.
