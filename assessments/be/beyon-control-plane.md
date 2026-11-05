---
harness_id: beyon-control-plane
project_name: Beyon Control Plane
repository: https://github.com/Beyon-Digital/control-plane
review_ref: 9dbe4012bdf8b2d2ee333402912b408aadd35e6d
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Beyon Control Plane

## Review boundary

- System in focus: the distributed native Control Plane deployment consisting of one authenticated Rust worker and its connected macOS/iOS native client running the **optional main orchestrator** with model/agent-management permission; existing provider sessions and their events are inside its current operational scope.
- Purpose and identity: supervise coding-agent work on an explicitly selected host/account while keeping distinct provider tasks, execution permissions, session progress, files and Git changes inspectable and revocable.
- Relevant environment: workspace edits, Codex/Claude/Kiro processes, provider failures, interrupted runs, cross-device clients, host/account boundaries, changing task requests and uncertain side effects.
- Standard-distribution boundary: first-party SwiftUI client, Swift model orchestration and tool dispatch, host API, Rust worker, durable SQLite session/event/receipt store, provider adapters and scoped workspace/desktop facilities. Actual coding-agent SDKs/provider inference and ChatGPT account entitlement are external dependencies, not credited as native Beyon policy departments.
- Credited operating / distribution surfaces: [README](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/README.md), [orchestrator](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/apple/Sources/ControlPlaneKit/OrchestratorEngine.swift), [orchestrator deployment and limits](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/orchestrator.md), [architecture](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/architecture.md), [worker event/store](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/crates/host/src/store.rs), [host API](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/crates/host/src/api.rs).
- Adjacent first-party surfaces excluded from ownership: build/release CI and unsigned preview, OS trust chain as an organizational decision-maker, external provider's internal control loops, paid/live account inference tests, and future mobile/production acceptance work.
- Operating modes considered: client without a host (chat only); connected read-only orchestrator; **Allow agent management** with create/prompt/interrupt; direct per-agent sessions; local worker versus brokered OS-account worker; trusted/untrusted task policies and per-session human approvals; restart/uncertain recovery.
- Recursion level: one owner-connected host/account's coding work portfolio under a client-side orchestrator, not the whole Beyon Digital company or a federation of unrelated workers.
- Reviewed revision: `9dbe4012bdf8b2d2ee333402912b408aadd35e6d`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The worker launches and tracks independently selected coding-agent provider sessions under a user OS account. Acceptance, idempotency receipts, audit and event cursors are persisted in SQLite; a disconnected client can later read session states and events. The native orchestrator runs its **own** model inference on the viewing device, enumerates the authenticated worker's host/provider capabilities, session states, individual event streams, files and actual Git diffs, and—if the user enables agent management—can create sessions, send prompts or interrupt a running session through the worker API. Requests are sequential, budgeted and subject to worker role/session/workspace controls. A task acceptance is not a completion claim; worker restart renders running sessions uncertain, without automatic replay. [Orchestrator source](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/apple/Sources/ControlPlaneKit/OrchestratorEngine.swift); [architecture](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/architecture.md).

## Operational model

Operational coding discretion belongs to Codex/Claude/Kiro provider agents in explicit sessions; Beyon's worker exposes and bounds those existing session actions. A separate client-side **main orchestrator** uses model inference and concrete worker tools to decide how to inspect and direct the current session portfolio. Human scope, provider credentials, host/account selection, agent-management toggle and approvals remain external or parent-owned. The assessment credits reachable shipped source wiring—not real provider quota, physical device testing, network latency or signed distributions.

## S1 — Operations

- State: A
- Function: provider coding agents work on repo tasks through native worker session and tool/result feedback.
- Disturbance / variety regulated: unknown code, compilation failures, tool restrictions, interrupted provider processes and changing workspace state.
- Decisive decision or feedback right: each configured provider agent chooses coding actions and follow-up responses in its provider session, limited by its own approval policy and worker exposure; the first-party worker accepts, persists and reports concrete execution events.
- Decision owner: model-backed Codex/Claude/Kiro agent; external provider inference is a runtime dependency, while Beyon owns the adapter, execution and feedback boundary.
- Supporting / enforcement mechanisms: provider stdio/sidecar adapters, scoped session creation, event stream, workspace tools, idempotency receipts, device authorization and abort.
- Closure path: prompt is accepted by worker → provider agent works with permitted tools → worker persists events and file effects → operator/orchestrator reads outcome and can issue follow-up or cancellation.
- Boundary reachability: README documents installed providers and worker start; orchestrator's concrete `create_session` and `prompt_session` routes call authenticated `v1/sessions` endpoints. The provider must separately be installed/authenticated.
- Why this is / is not agent-owned: the provider agent selects how to do coding work rather than simply replaying deterministic scripts; host safety and networking alone are not the autonomous decision.
- Evidence: [run and provider boundary](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/README.md), [provider adapters](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/crates/host/src/providers.rs), [orchestrator session calls](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/apple/Sources/ControlPlaneKit/OrchestratorEngine.swift).
- Basis: source and supported deployment documentation; no live provider inference run.
- Confidence: high for reachability; real account/provider integration is not independently proven.
- Caveats: the external agents' internal organizational functions are not copied into first-party Beyon ownership.

## S2 — Coordination

- State: —
- Function: no evidenced *inter-S1 conflict-specific* reciprocal attenuation loop between independently acting coding agents.
- Disturbance / variety regulated: independent sessions could edit shared files or compete for worker resources, but the reviewed implementation does not show a first-party overlap analyzer and corrective return to the competing operational units.
- Decisive decision or feedback right: the orchestrator's tool calls are sequential and worker policies bound sessions/concurrency; neither explicitly identifies contested S1 obligations and reconciles them with collision feedback.
- Decision owner: no distinct inter-S1 coordination owner established; session limits are deterministic worker enforcement.
- Supporting / enforcement mechanisms: sequential model calls, per-account isolation, role grants, session ownership, worker quotas, Git conditional saves and separate worktrees.
- Closure path: requests are authenticated and serialized locally where required; a resource denial returns an error, not an evidenced negotiation/adjustment between multiple S1 agents.
- Boundary reachability: concurrency and host/account controls are shipped but do not themselves prove inter-S1 regulatory coordination.
- Why this is / is not agent-owned: having many sessions, a central orchestrator and an action cap is insufficient without identified actual collisions and a feedback relation specifically resolving those collisions.
- Evidence: [orchestrator tool loop](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/apple/Sources/ControlPlaneKit/OrchestratorEngine.swift), [worker controls](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/architecture.md), [workspace operations](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/crates/host/src/workspace.rs).
- Basis: bounded first-party negative inspection.
- Confidence: medium; a model might manually notice a conflict, but a reproducible supported collision workflow is not demonstrated.
- Caveats: explicit separate worktrees reduce collision probability; they do not automatically constitute S2.

### Absence scope

- Surfaces inspected: Swift orchestrator dispatcher, worker sessions and concurrency limits, auth/account separation, workspace/Git conditional operations and documented deployments.
- Plausible first-party paths checked: two agents editing the same file, cross-client session actions, per-worker quotas, concurrent prompt requests, sequential tool dispatch and isolation by worktree.
- Why no material first-party path remains: observed mechanisms isolate, order or reject requests, without a distinct conflict-aware inter-agent feedback/adjustment cycle and reciprocal S1 return.

## S3 — Inside-and-now control

- State: A(P)
- Function: a client-side main orchestrator can inspect the **present portfolio** of installed agents, active sessions, progress and host account capabilities, and direct current coding work.
- Disturbance / variety regulated: tasks accepted but not completed, unavailable providers, failed/uncertain sessions, unexpected file effects, new user priorities and permission changes.
- Decisive decision or feedback right: when management is enabled, the main model can select a provider, create sessions, prompt them and interrupt a live run after querying `host_info`, `list_sessions`, `session_events`, `workspace_diff` and other evidence. Human retains scope and approval rights.
- Decision owner: separate model-backed first-party `OrchestratorEngine` for operational session-portfolio decisions; human owner supplies binding agent-management permission, host/account selection and provider/tool approvals.
- Supporting / enforcement mechanisms: scoped API client, model tool catalog/dispatcher allowlist, per-turn 10-round/40-call budget, user toggle, persistent worker session events and host access checks.
- Closure path: current host/session/workspace evidence → orchestrator chooses create/prompt/interrupt or wait/inspect → worker accepts/rejects → event states return to subsequent model judgment and user UI.
- Boundary reachability: `OrchestratorEngine.run` calls configured model inference and `OrchestratorTools.execute` implements actual endpoints, available from the native Orchestrator screen; read-only mode removes management calls.
- Why this is / is not agent-owned: current portfolio management is an explicit model decision layer distinct from a worker's deterministic dispatch; notation includes `(P)` because the user holds the management enablement and unapproved tool authority.
- Whole-system current view: worker host/provider discovery, per-session states/events, files and Git state across the connected account.
- Current-control decision scope: creation, follow-up prompting, interruption and current inspection; not identity policy, user consent overrides or provider permission approval.
- Evidence: [executable tool catalog and dispatch](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/apple/Sources/ControlPlaneKit/OrchestratorEngine.swift), [orchestrator limits and scope](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/orchestrator.md).
- Basis: first-party model loop and scoped live API wiring; not a successful real model-provider performance claim.
- Confidence: medium-high for implemented mode, with uncertainty about account entitlement and real deployment operation.
- Caveats: without a connected worker or with management disabled, this S3 agent's action right is absent; these modes are not silently credited with full orchestration.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Native main-orchestrator model | Session roster, host state and prompt outcomes require present-work decisions | query connected worker → choose session creation, prompt or interruption → worker state/events return to next model turn | [orchestrator source](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/apple/Sources/ControlPlaneKit/OrchestratorEngine.swift) |
| Parent (`P`) | Host/account human operator | Model-management toggle, new permissions or a current run requiring intervention | enable/disable management, grant/deny a provider action or stop a session → worker/dispatcher enforces the new scope | [orchestrator scope](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/orchestrator.md) |

## S3* — Complementary audit

- State: C
- Function: provide evidence independent of coding-agent prose about actual session acceptance/completion, worker state and Git working-tree differences, enabling a corrective decision.
- Disturbance / variety regulated: a coding agent can claim a task is done when a prompt was only accepted or its changes are missing; client state can be stale after disconnect/restart.
- Decisive decision or feedback right: orchestrator/human can query durable worker `session_events`, `list_sessions` and raw `workspace_diff`, compare to the coding agent's story and then change follow-up or interrupt; the alternative evidence path itself is deterministic rather than a dedicated autonomous auditor.
- Decision owner: independent first-party worker event/actual-file evidence constructor (`C`); model orchestrator or human interprets it, but the code does not guarantee a distinct adversarial auditing-model verdict.
- Supporting / enforcement mechanisms: durable SQLite events and receipts, restart `uncertain` rather than success/replay, actual workspace Git diff endpoint, clear prompt acceptance semantics.
- Closure path: provider report/accepted prompt → fresh worker events and raw Git diff challenge the claimed state → main orchestrator/user can send a correction or halt a session → next provider action and events reflect the adjustment.
- Boundary reachability: model tool catalog includes these live read-only tools, backed by worker API and stored events; the docs explicitly instruct inspection rather than treating acceptance as completion.
- Why this is / is not agent-owned: these observations do not originate in the coding agent's natural-language assertion, yet no separate reviewer model automatically produces a verdict; hence a complementary **constructor**, not S3* A.
- Claim being audited: the provider agent actually completed requested work and current workspace effects match its claimed progress.
- Ordinary reporting path: provider messages, prompt-accepted notifications and local client conversation state.
- Complementary access path: persisted host event cursor/status and independent Git filesystem diff read through the authenticated worker.
- Independence boundary: coding agents can change workspace files and might manipulate their own outputs; the event store is separately maintained by the worker, but does not prove correctness, and actual Git diff alone cannot validate tests.
- Who acts on findings: parent human or client-side orchestrator issues a new prompt, pauses, or explicitly declines completion claims.
- Evidence: [orchestrator independent read tools](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/apple/Sources/ControlPlaneKit/OrchestratorEngine.swift), [durable events and restart semantics](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/architecture.md), [worker store](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/crates/host/src/store.rs).
- Basis: first-party separate observation and optional corrective return, not an observed independent semantic audit.
- Confidence: medium: robust source separation, discretionary rather than mandatory corrective use.
- Caveats: an orchestrator can choose not to inspect, and a diff can miss semantics; no guaranteed code-review safety threshold is inferred.

## S4 — Outside-and-then intelligence

- State: —
- Function: no packaged externally prospective scenario/option selection feeding durable changes to future operating capabilities.
- Disturbance / variety regulated: future agent/provider availability, model eligibility, host topology and longer-term developer workflows may shift.
- Decisive decision or feedback right: humans select current model profiles/endpoints, connect hosts and install workers; model discovery and account authorization are present-day capability choices, not a strategic outside-and-then return loop.
- Decision owner: developer/operator configuration; no distinct first-party S4 intelligence decision owner.
- Supporting / enforcement mechanisms: model profiles and discovery, platform release/updater, host management, installation and verification guides.
- Closure path: a user can switch a model or host and run the current orchestrator, but there is no shown future environment options assessment that binds a changed long-term operating capability through S3.
- Why this is / is not agent-owned: discovering current models and installing signed updates are not VSM S4 merely because they concern technological change.
- Evidence: [model setup](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/orchestrator.md), [architecture and update trust](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/architecture.md).
- Basis: bounded negative review of shipped model/settings, current orchestrator and future release modes.
- Confidence: medium-high at declared host/account recursion.
- Caveats: developer roadmap and update mechanisms can evolve without proving a deployed prospective adaptation regulator.

### Absence scope

- Surfaces inspected: model configuration, endpoint model discovery, README deployment matrix, orchestrator scopes, update/release architecture and verification status.
- Plausible first-party paths checked: provider migration, external eligibility, future host fleets, model selection strategy, signed upgrades and knowledge of platform limitations.
- Why no material first-party path remains: paths are present-day operator setup, provider credential refresh, or maintainer build/release work; none closes a first-party option→future capability→current S3 return.

## S5 — Policy and identity

- State: —
- Function: no evidenced ultimate identity/purpose policy conflict adjudicated by a legitimate organizational authority and returned to runtime commitments.
- Disturbance / variety regulated: conflicting device trust, human permission and long-term assistant identity may require parent policy, but runtime currently applies already configured controls.
- Decisive decision or feedback right: administrators enroll/revoke devices and grant roles; the user enables agent management, accepts provider permissions and can emergency-stop. These are scoped operational/security rights, not identity-policy adjudication.
- Decision owner: outside human user/account administrator and project governance; no shipped distinct S5 decision loop with a charter-level return.
- Supporting / enforcement mechanisms: TLS device identity, role/session ACL, certificate renewal, worker privilege boundaries, explicit trusted mode and emergency stop.
- Closure path: permission changes apply to future API calls and revoke streams, without a witnessed foundational identity dispute being raised, decided and returned as ultimate policy across the organization.
- Why this is / is not agent-owned: revocation and human override are genuine safeguards but not sufficient S5 closure; no autonomous S5 is inferred from a secure product name or operator veto.
- Evidence: [trust model and deployment limits](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/architecture.md), [human agent-management bounds](https://github.com/Beyon-Digital/control-plane/blob/9dbe4012bdf8b2d2ee333402912b408aadd35e6d/docs/orchestrator.md).
- Basis: bounded negative inspection of actual governance/permissions rather than contributor organization.
- Confidence: medium-high.
- Caveats: multi-user administrators can govern security policies, but that is not an evidenced question-to-legitimate-S5-to-binding-operational-return loop at this boundary.

### Absence scope

- Surfaces inspected: worker role/member/device policy, broker account isolation, orchestrator user instruction/tool allowlist, trust docs, updater and release authority.
- Plausible first-party paths checked: account revocation, new team member rights, agent approval policy, emergency-stop authority, model endpoint switching and update trust.
- Why no material first-party path remains: these are present safety/security authorization and product maintenance, without a first-party identity dispute or charter decision returned to all operating departments.

## Distributed OSS parent arrangement

The Beyon maintainers and user organizations may exercise their own policy governance, but no organizational S5 is borrowed from the first-party source repository, TLS broker or package name. Parent human controls the selected worker/account and whether model-led management is enabled.

## Self-hosted and non-human modes

The Rust worker and broker can be self-hosted, including isolated OS-user accounts; inference and secrets for the main orchestrator stay on the viewing device. A valid connected worker and explicitly enabled model management are required for S3 A(P). In a read-only or no-host chat mode, no coding-agent portfolio control is credited. The README warns that production/platform acceptance and eligible ChatGPT plan inference still need external validation.

## Recursion

Several provider sessions may form multiple S1 work cells under a client-side meta-orchestrator. Worker/account isolation is an implementation trust boundary, not an automatic next-level VSM federation. No autonomous inter-S1 S2, prospective S4 or identity S5 is inferred merely from device/session scale.

## Variety and escalation

Provider adapters and a capable main model amplify coding and task-routing variety. Explicit host/account scope, sequential calls, bounded rounds/call counts, request receipts, optimistic file writes, worker ACLs, permission handling and interruption attenuate mistakes. A failed or canceled orchestrator turn does not undo accepted provider actions; users are warned to inspect the durable records before retrying.

## Evidence gaps

- First-party source paths and operating documents were inspected at the frozen SHA, but no live provider inference, real macOS/iOS host, external ChatGPT entitlement or production release acceptance was run. Local Rust tests could not run because the `cargo` executable is not installed.
- Model-orchestrator S3 A(P) is reachable only on a connected host with provider and explicit agent-management enablement. No assertion is made that each supported provider/account works end-to-end.
- S3* C credits independent worker events and actual-file access, not a guaranteed independent adversarial code review, quality verdict or human inspection on every task.
- Session quotas and serial tool calls do not show an inter-S1 collision-specific S2 correction loop. External model discovery and updates do not demonstrate prospective S4; permissions and trust enforcement do not establish S5.
- The batch CLI preflight hit unauthenticated GitHub HTTP 403 on comments; frozen row, current board, current main and controller comments were instead inspected via the authenticated GitHub connector. No collision was observed on that alternate read; the failed CLI check is not reported as a PASS.
