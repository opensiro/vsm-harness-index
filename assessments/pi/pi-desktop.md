---
harness_id: pi-desktop
project_name: PI-Desktop
repository: https://github.com/vastsa/PI-Desktop
review_ref: 5aa253883c4e34fd65d31c434256d424c352bf0b
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# PI-Desktop

## Review boundary

- System in focus: the first-party PI-Desktop installed local desktop/host and Pi agent runtime, its persistent sessions/Agent–Plan–Goal operating modes, permission and plugin boundaries, and the shipped host session-collaboration infrastructure for worker sessions.
- Purpose and identity: provide a local-first workspace in which model-backed agents plan and perform file/tool-based work, save projects/sessions and optionally delegate to other durable model-agent sessions under host permissions.
- Relevant environment: user requests, local project files, model provider APIs, command/tool/plugin results, explicit human approvals, independent worker sessions, persistent turn state, and installed plugin capabilities.
- Standard-distribution boundary: packages `agent-runtime`, `agent-host`, `host-runtime`, `shared`, desktop/Electron Main and Rust `host-core`, plus first-party supported session-collaboration API. External models/providers, hosted marketplace review/operations and the separately delivered Session Orchestrator plugin are dependencies/adjacent products, not silently packaged owners.
- Credited operating / distribution surfaces: [native Pi session](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/agent-runtime/src/native-pi-session.ts), [Agent Host](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/agent-host/src/agent-host.ts), [host runtime](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/host-runtime/src/runtime-service.ts), [Rust session collaboration](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/crates/host-core/src/session_collaboration/mod.rs), [desktop session-collaboration service](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/apps/desktop/electron/main/services/session-collaboration.ts), and reviewed plugin/permission invocation surfaces.
- Adjacent first-party surfaces excluded from ownership: separate plugin-center server/review process, marketplace-published official Session Orchestrator code not contained in the pinned checkout, docs/spec future plans, sample voice agents, development/E2E fixture runs, CI/release and repository maintainer governance. Accepted design documents are evidence of supported composition, not proof a remote service/plugin runtime is installed.
- First-party operating / deployment modes considered: single user-driven `Agent` model session with tool calls; Plan with durable user approval; Goal with model task execution; local project/sessions; optional subagents and host-owned session-collaboration API invoked through a permitted installed plugin; read-only UI/work-panel and user interruption; bundled plugin/permission host controls.
- Recursion level: one local PI-Desktop instance with its optional parent-plus-worker session team. Separate end-user organizations and all marketplace installations do not become one shared VSM by distribution.
- Reviewed revision: `5aa253883c4e34fd65d31c434256d424c352bf0b`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/README.md) advertises Agent, Plan and Goal modes, model/tool selection, persistent project sessions, subagents and full worker sessions. The decisive runtime is not the promotional feature list: [`native-pi-session.ts`](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/agent-runtime/src/native-pi-session.ts) invokes Pi's `createAgentSession`, operates a model-driven session and integrates project instructions/tool calls. [`AgentHost`](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/agent-host/src/agent-host.ts) owns turn admission, queue, state/snapshots and approval brokerage; [`RuntimeService`](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/host-runtime/src/runtime-service.ts) sends turns to the Pi sidecar and preserves finalization/provenance. The [sidecar bridge](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/host-runtime/src/agent-sidecar.ts) allow-lists sensitive host RPC methods.

Plan/Goal are operating modes of a model agent, not evidence of a second autonomous manager. Host-owned plan approvals constrain when a model's proposed work may execute; a deterministic policy/permission gate transports the human decision but does not own that decision. User sessions and tool plugins can be composed for tasks without creating organizational S5 by name. [`LiveWorkCoordinator`](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/host-runtime/src/live-work/coordinator.ts) explicitly describes call-scoped intent routing rather than an Agent runtime; its deduplication, stop barriers and status feedback regulate request delivery, not whole-business strategy.

The [Rust collaboration ledger](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/crates/host-core/src/session_collaboration/mod.rs) allows an authenticated model-session tool to spawn durable worker sessions (capped in number), send task/message inputs, receive real terminal results and cancel deliveries with original permissions. The [desktop service](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/apps/desktop/electron/main/services/session-collaboration.ts) bridges durable queued collaboration deliveries into actual Agent Host turns. The [session collaboration API contract](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/docs/spec/07-plugins/03-plugin-api.md) describes supported spawn/send/list/status/result/cancel operations requiring a plugin's active Agent tool invocation. The accepted [orchestrator ADR](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/docs/adr/0237-session-orchestrator-as-a-plugin.md) places the supervisor composition in a distinct marketplace plugin, not in host-core. The later [session-message ADR](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/docs/adr/0239-session-collaboration-messages.md) describes host-enforced provenance, worker return messages and bounded autonomous hops.

## Operational model

In ordinary Agent mode the integrated Pi model chooses task actions against user/project context and executes configured tools under permission checks. In Plan mode the user may authorize a proposed plan before a new Agent turn; in Goal mode the model determines the path to an operator-given outcome. If an operator installs an authorized session collaboration plugin, parent and worker sessions become independently running first-party Pi agent loops while the host supplies bounded session creation, status/result observation, messages and cancellation. PI-Desktop itself exposes a current-supervision construction surface, but the separate plugin/model manager must choose interventions and establish authority; the deterministic host ledger is not that owner.

**Proposed disposition: included**, vector `A — C — — —`. First-party model-execution and tool-feedback closes S1. A function-specific S3 worker-team current-control path is constructed by shipped host APIs but is not autonomously closed by the host without a separately installed deciding manager. Other functions are bounded to in-repository supplied modes.

## S1 — Operations

- State: A
- Function: fulfill user coding/workspace tasks via model-selected reads, edits, tools, subagent operations and iterative response to execution observations.
- Disturbance / variety regulated: evolving task requirements, codebase state, provider outputs, failures, permission limits, test results and changing tool context.
- Decisive decision or feedback right: model chooses what action/tool/repair or result to produce on each turn within permissions; a delegated worker similarly chooses its next task step.
- Decision owner: actual model-backed Pi agent in `native-pi-session` / its worker sessions, with the user setting goals and the host controlling allowed tool execution.
- Supporting / enforcement mechanisms: `AgentHost` turn state, `RuntimeService` sidecar, persistent session file and model configuration, prompt/tool lifecycle, plugin tool adapters and local permission broker.
- Closure path: user/session input → Pi model → selected permitted tool or code action → host executes/records result → model consumes output and continues or returns a report.
- Boundary reachability: `packages/agent-runtime/src/native-pi-session.ts` calls `createAgentSession` from Pi in the shipped runtime; Electron host starts the sidecar and `RuntimeService` binds the model turn to durable host state. This is not merely a third-party agent icon or test fixture.
- Why this is / is not agent-owned: without the model, the desktop still displays sessions and enforces permissions, but it no longer chooses task-specific code changes or adaptive next actions. Human approval restricts agency rather than replacing its ordinary S1 decision right.
- Evidence: [native Pi integration](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/agent-runtime/src/native-pi-session.ts), [runtime service](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/host-runtime/src/runtime-service.ts), [agent host](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/agent-host/src/agent-host.ts), [README operating modes](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/README.md).
- Basis: executable first-party runtime integration; no new provider/live-task measurement.
- Confidence: high for structural reachability.
- Caveats: an actual provider model, credentials and permissions are required; external plugin functions do not automatically become part of every standard installation.

## S2 — Coordination

- State: —
- Function: no evidenced first-party regulation of a specified inter-S1 collision, oscillation or conflict across independent worker operations.
- Disturbance / variety regulated: simultaneous worker message traffic, target inbox pressure, parallel session interactions and inconsistent task outputs.
- Decisive decision or feedback right: detect an interference between identified sibling operational units and choose a reciprocal coordination adjustment affecting their subsequent work.
- Decision owner: request/inbox/permission code deterministically admits messages and rejects conflicts; a parent agent may direct subagents as task work but no S2-specific conflict adjudicator is supplied.
- Supporting / enforcement mechanisms: delivery idempotency, inbox size ceiling, no self-message, `remaining_hops`, session permission inheritance, source-linked callbacks and result projections.
- Closure path: permitted message or result arrives at another session/parent; it does not itself detect and attenuate identified inter-S1 interference.
- Why this is / is not agent-owned: bounded intersession communication and generic routing can support future S2, but no first-party S2-specific disturbance/decision/returned coordination witness is established.
- Evidence: [collaboration ledger](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/crates/host-core/src/session_collaboration/mod.rs), [message ADR](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/docs/adr/0239-session-collaboration-messages.md), [turn queue](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/agent-host/src/turn-queue.ts).
- Basis: bounded source-negative.
- Confidence: medium-high.
- Caveats: downstream plugins may implement collision-specific mediation, but a generic platform capability alone does not meet `S2=C`.

### Absence scope

- Surfaces inspected: collaboration Rust ledger/schema/projections, desktop delivery service, Agent Host queue, orchestration API/ADR, plugin message bus and subagent/worker modes.
- Plausible first-party paths checked: inbox overflow as inter-S1 conflict, guaranteed callbacks as coordination, parent worker supervision as S2, permission inheritance as inter-unit interference attenuation.
- Why no material first-party path remains: these guard message admission and progress flow or manage assignments; none reconstructs a specific ongoing two-S1 collision and bilateral adjustment/closure.

## S3 — Inside-and-now control

- State: C
- Function: provide a bounded current view and decisive intervention endpoints for a parent agent to supervise its portfolio of live durable worker sessions.
- Disturbance / variety regulated: busy/stalled worker turns, outdated assignments, cancelable queued deliveries, excess parallel workers and failed or incomplete worker tasks.
- Decisive decision or feedback right: after reviewing the current worker/session states and results, choose new task delegation, follow-up instructions, cancellation or intervention that changes the currently executing team.
- Decision owner: an explicitly installed plugin's main model agent or user must compose and own that discretionary supervisor judgment. Host core is authoritative for session identity/provenance/permission, but does not autonomously choose managerial priorities or guarantee a legitimate parent-governed S3(P) loop.
- Supporting / enforcement mechanisms: `session.collaboration.list/status/result`, durable turn ledger and actual completion callbacks, `spawn/send/cancel`, Agent Host queue/abort and permission ceiling, UI session state.
- Closure path: parent/manager obtains bounded worker state/results → decides who should work, stop, or receive changed instructions → host validates and dispatches `spawn`/`send`/`cancel` → durable worker Agent turn starts/stops/responds → updated state and result return to parent.
- Boundary reachability: first-party Rust `session_collaboration` implements and validates the exact collaboration operations; desktop `createSessionCollaborationService` binds delivery into real Agent Host turns. The API is a shipped supported plugin-host integration, though a separately delivered plugin/manager is required to compose discretionary S3.
- Why this is / is not agent-owned: actual workers are model agents, yet the host simply records, gates and transports their work. Full current-worker control functions are specifically exposed, not autonomously chosen by the host, so `C` rather than `A`; human UI stop alone is not automatically S3(P).
- Whole-system current view: for the parent-plus-worker session team, the host `list/status/result` projections identify active/queued/terminal worker execution and bounded outcomes without reading full transcripts.
- Current-control decision scope: current assignment of up to the supported worker cap, follow-up direction, session task cancellation, and reallocation of active work; not finance/strategy of all PI-Desktop users.
- Evidence: [collaboration core](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/crates/host-core/src/session_collaboration/mod.rs), [status projections](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/crates/host-core/src/session_collaboration/projections.rs), [desktop dispatch](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/apps/desktop/electron/main/services/session-collaboration.ts), [plugin API control contract](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/docs/spec/07-plugins/03-plugin-api.md).
- Basis: first-party function-specific S3 constructor; external manager composition required.
- Confidence: medium for classification, high for host control/return implementation.
- Caveats: the official marketplace plugin is separate from the pinned checkout, hence not credited as autonomous S3 owner. `LiveWorkCoordinator` and turn queues alone are task-delivery plumbing and do not change this ownership conclusion.

## S3* — Complementary audit

- State: —
- Function: no established independent operational-reality audit that challenges parent management's ordinary status/report and returns corrective S3 findings.
- Disturbance / variety regulated: incomplete or misleading worker reports, plugin safety defects, inaccurate task completion and policy bypasses.
- Decisive decision or feedback right: use an independent source of operational truth to judge system operations and feed a corrective management conclusion back into S3.
- Decision owner: Rust host truth and audit/provenance are deterministic infrastructure; reviews/approvals of plans/plugins are task/security gates, not a separately constituted operational auditor at this recursion.
- Supporting / enforcement mechanisms: session transcripts, turn-bound result ledger, plugin permissions, hard admission checks, E2E tests and user-inspectable reviews.
- Closure path: host terminal outcomes feed ordinary worker status and user report; no separate audit actor brings independently obtained operational evidence to correct supervisory authority.
- Why this is / is not agent-owned: persisted truth and provenance can improve integrity, but data availability without independent audit judgment/return does not establish S3*.
- Evidence: [collaboration provenance](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/crates/host-core/src/session_collaboration/provenance.rs), [turn settlement](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/crates/host-core/src/session_collaboration/settlement.rs), [plugin security](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/docs/spec/07-plugins/04-plugin-security.md).
- Basis: bounded source-negative.
- Confidence: medium-high.
- Caveats: a dedicated independently mandated review plugin with direct external observations may add complementary audit in a later adopter configuration.

### Absence scope

- Surfaces inspected: collaboration records and turn provenance, host-result reports, plugin permission/marketplace documentation, plan approval and test/review modes.
- Plausible first-party paths checked: durable transcript as independent reality audit, plan user approval as S3*, plugin/security review as complementary management inspection.
- Why no material first-party path remains: ordinary session status is the same management information path, task approvals and plugin policy are safety controls, and no independent operational-reality audit actor/return is provided by these supported modes.

## S4 — Outside-and-then intelligence

- State: —
- Function: no established prospective external-scanning/adaptation-choice loop returning system capability changes to present management.
- Disturbance / variety regulated: new project/user goals, provider availability, plugin marketplace options, future development practices and work-context changes.
- Decisive decision or feedback right: scan outside/future environment, compare strategic capability options and return chosen adaptation into the team's present S3 operating structure.
- Decision owner: user configures models/plugins and future goals; an Agent/Goal model chooses the next path for an immediate task, not a standing environment-intelligence strategy.
- Supporting / enforcement mechanisms: Goal/Plan modes, provider catalog/import, plugin marketplace selection, persistent sessions, Work/LiveWork intent routing.
- Closure path: a new goal or plugin is applied to a task/configuration; no enduring external/future options appraisal and decision return to current S3 is demonstrated.
- Why this is / is not agent-owned: the model selecting a plan for a goal is operational S1 planning; available plugin/provider catalogs do not turn into S4 until a legitimate prospective choice updates organizational capability.
- Evidence: [README Goal/Plan modes](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/README.md), [LiveWork intent routing](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/host-runtime/src/live-work/coordinator.ts), [provider configuration](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/shared/src/provider-presets.ts).
- Basis: bounded source-negative, including parent-mode check.
- Confidence: medium-high.
- Caveats: self-hosted long-term strategy plugins are possible, but only their actual credited loops could establish S4.

### Absence scope

- Surfaces inspected: Agent/Plan/Goal modes, provider/plugin settings, LiveWork coordinator, session memory and official plugin integration contract.
- Plausible first-party paths checked: Goal planning as S4; changing provider as future adaptation; plugin marketplace as outside intelligence; user config updates as S4(P).
- Why no material first-party path remains: these are current task goals and operator configuration without an evidenced future-sensing, option-selection and closed management return cycle.

## S5 — Policy and identity

- State: —
- Function: no autonomous or operationally closed parent-mode ultimate identity/policy deliberation for the local agent organization.
- Disturbance / variety regulated: risky filesystem/tool actions, permission escalation, approved plans, model capability selection and plugin trust.
- Decisive decision or feedback right: resolve a genuinely ultimate identity/policy matter through legitimate authority and return a binding governance decision into subsequent organization operation.
- Decision owner: user/operator owns permission and plan approvals; Rust host validates and enforces current constraints. The model can submit a plan or ask for consent but cannot independently adjudicate the system's ultimate purpose.
- Supporting / enforcement mechanisms: plan approval record and durable authorization, plugin capability grants, model `availableForSubagents` opt-in, host-enforced permission ceilings and policy service.
- Closure path: an ordinary requested operation may be permitted/denied and execution proceeds/stops, but no first-party runtime identity-level issue → legitimate parent debate/decision → returned constitutional rule is evidenced.
- Why this is / is not agent-owned: strong permissions and user plan approval are important safety controls, but do not themselves define the S5 identity/ultimate-policy function.
- Evidence: [host approvals](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/packages/agent-host/src/approvals.ts), [Rust permission policy](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/crates/host-core/src/permissions.rs), [session collaboration permissions](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/crates/host-core/src/session_collaboration/permissions.rs), [current plugin permissions matrix](https://github.com/vastsa/PI-Desktop/blob/5aa253883c4e34fd65d31c434256d424c352bf0b/docs/spec/07-plugins/13-plugin-permissions-matrix.md).
- Basis: bounded source-negative, parent mode checked.
- Confidence: medium-high.
- Caveats: a user's enterprise identity and policy can exist outside the platform, not borrowed into this one local agent runtime merely by hosting its approvals.

### Absence scope

- Surfaces inspected: Plan/Goal authority, host plan approvals, plugin install/update permissions, worker inherited permission ceilings and session host policy.
- Plausible first-party paths checked: user Plan approval as S5(P); permission escalation/deny as ultimate-policy decision; plugin marketplace trust as application identity policy.
- Why no material first-party path remains: these settle bounded action/config permissions, and the external plugin-center review is adjacent; no first-party identity/ultimate-policy dispute/legitimate authoritative-return loop closes at this recursion.

## Distributed OSS parent arrangement

An individual PI-Desktop installation has local user authorization and private session data. Independent operators and marketplace plugin publishers do not form one shared organization for Index classification. Open-source project maintainers control repository releases, but their CI/PR process is adjacent to the installed desktop Agent's operational decision ownership.

## Self-hosted and non-human modes

The desktop can run a model-driven task with no human within every intermediate tool turn, while enforcing permissions and optional human Plan acceptance. A separately installed Agent-facing collaboration plugin may allow a parent model to inspect and redirect durable workers, but the checked-in host provides the current-control constructor only. The record does not upgrade this to `S3=A(P)` or `P` without separately showing each function-specific legitimate decisive owner/return mode.

## Recursion

A local parent Session and durable Worker Sessions form a plausible higher-level work team with multiple operational model-backed cells; a worker remains a fully inspectable lower-recursion agent. The app's own project→session→agent→work hierarchy is an object model, not a proof of full viable S1–S5 recursions at every nesting level. Current-control construction is bounded to a parent/worker portfolio in one installation.

## Variety and escalation

Model/tool/planning freedoms amplify task variety. Host-origin-signed messages, per-turn idempotency, user permission ceiling, Plan approval, resource limits, bounded callback hops and plugin manifests constrain unsafe action and infinite delegation. Queue fullness, failed turns and permission denials return concrete errors to the active task or user; none automatically establishes a distinct algedonic path to S4/S5. The S3 constructor supports supervisory correction of current worker commitments when a deciding dispatcher is composed.

## Evidence gaps

This review fixes the public upstream Git commit and shipped code/API boundary. It does not claim live external model/provider performance, a real marketplace plugin installed, or multiworker throughput tests. Source `scripts/e2e-session-collaboration.mjs` passed `node --check`; Python scripts compiled. A targeted JavaScript UI collaboration test could not load in this checkout because npm package `i18next` was absent, and Rust `cargo` was unavailable; no false green upstream integration run is claimed. The separate official Session Orchestrator implementation was not credited as part of the pinned repository, which limits the S3 result to the first-party construction path.
