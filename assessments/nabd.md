---
harness_id: nabd
project_name: Nabd
repository: https://github.com/amiraq1/Nabd
review_ref: 1b7c36a5d79a20c055e688474b0ebc9fd916b7b3
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Nabd

## Review boundary

- System in focus: the first-party Nabd terminal coding runtime at frozen revision `1b7c36a5d79a20c055e688474b0ebc9fd916b7b3`, including the `internal/agent` model/tool loop, built-in coding tools, provider/router layer, permission gate, append-only event journal, compaction/budget logic, shadow snapshots and undo/rewind, resumable interactive/headless sessions and supported configuration/provider commands.
- Purpose and identity: turn a user engineering request into repository inspection, code/file/process actions and a final model response while preserving explicit permission, audit and recovery boundaries in one local coding session.
- Relevant environment: user requests and approval decisions, working-tree contents, file/process/tool results, provider/model responses and rate limits, provider route availability, context pressure, session journal/history, shadow snapshots, configuration and credentials.
- Standard-distribution boundary: the shipped `nabd` Go binary and its first-party agent, provider, tool, permission, storage, snapshot/recovery, configuration and UI/headless wiring. External model/provider endpoints, OS shell programs, Git hosting and repository content are dependencies and cannot donate ownership.
- Credited operating / distribution surfaces: `README.md`; `cmd/ag/`; `internal/agent/`; `internal/provider/`; `internal/tools/`; `internal/perm/`; `internal/store/`; `internal/snap/`; `internal/config/`; supported interactive/headless execution and resume/replay surfaces.
- Adjacent first-party surfaces excluded from ownership: repository CI/build gates, release process, test/replay corpora, security review reports and maintainer development decisions. `docs/GOAL_MODE.md` is considered as design evidence but its user-facing integration steps are incomplete at the frozen ref and are not credited as a distinct runtime owner.
- First-party operating / deployment modes considered: interactive Feed/legacy chat sessions, headless `-p` execution, resumed sessions, permission modes `deny`/`allow-reads`/`ask`/`plan`, provider-router fallback, compaction, rewind, file undo and configured provider/model selection.
- Recursion level: one Nabd coding session over one working tree is the assessed organization. The active model/tool loop is the sole material operational S1; providers, tools, permission/journal/snapshot machinery and the human approver are supporting actors or environmental/parent constraints rather than peer operational S1 units.
- Reviewed revision: `1b7c36a5d79a20c055e688474b0ebc9fd916b7b3`.
- Observation date: 2026-10-06.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Nabd is a Go terminal coding agent built around one event-producing model/tool loop. `internal/agent.Loop` turns one user message into a settled conversation by streaming a provider turn, executing model-requested tools, returning tool outcomes and repeating until the model stops asking. The first-party registry supplies repository reads/search, writes/edits and bash; permission classification occurs before sensitive execution and denied calls return into the ordinary loop as evidence rather than becoming a parallel actor.

The session is journaled as append-only JSONL. Resume, replay, compaction and rewind operate over the same event/history contract. File mutations may be backed by a content-addressed shadow store so `/undo` can restore tracked edits independently of Git. These are persistence, recovery and variety-management mechanisms around the same operational coding loop.

The provider layer can route sequentially across configured provider/model routes before semantic output commits. It includes retry/fallback, rate-limit handling and a route-local circuit breaker. This is deterministic transport resilience for the same S1 request: routes are not peer coding operations and the router does not become a metasystem owner merely by choosing the first available configured route.

Interactive and headless modes share the same operational boundary while changing permission behavior and presentation. Configuration and provider commands let the operator select credentials/routes/models. Context pressure can trigger warning/compaction behavior, including model-assisted compaction with deterministic fallback, but it does not create a separate prospective-intelligence owner.

## Operational model

The material operation is repository-level coding work performed by one model-backed agent. It chooses what to inspect, which coding tool/process action to request, how to interpret the returned result and whether further work is required. First-party policies constrain tool classes, route providers, cap reads/turns/spend, preserve the audit log and support recovery.

The human may approve or deny particular actions and may choose static modes/providers. Those decisions constrain the operation but do not form a separate whole-system current-control, prospective adaptation or identity-governance loop under Methodology 0.3.6.

## S1 — Operations

- State: A
- Function: autonomously execute a coding request through model-selected repository/tool actions and iterate on returned evidence until the session settles.
- Disturbance / variety regulated: unfamiliar repository state, implementation choices, read/write/process outcomes, provider failures/rate limits, permission refusals, context pressure, malformed tool calls and ordinary coding/test feedback.
- Decisive decision or feedback right: choose substantive repository/tool actions, interpret their outcomes, revise the implementation or plan and decide when the coding response is complete.
- Decision owner: the active model-backed Nabd agent in `internal/agent.Loop`.
- Supporting / enforcement mechanisms: tool registry, permission gate, provider/router transport, turn/spend/context budgets, journal, tool-call repair, snapshot/undo, rewind, redaction and recovery machinery.
- Closure path: user request → model chooses a tool/code action → first-party permission/tool layer executes or refuses it → structured result is returned to the same model conversation → the model chooses the next action or final response.
- Boundary reachability: the shipped interactive and headless command paths construct the same first-party session/agent composition; resume restores persisted history into that loop rather than substituting an external executor.
- Why this is / is not agent-owned: deterministic gates, storage and routing constrain/transport work, but the model owns the open-ended coding judgments; removing it removes the decision process that selects implementation actions.
- Evidence: [README.md](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/README.md); [internal/agent/loop.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/agent/loop.go); [cmd/ag/session.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/cmd/ag/session.go); [cmd/ag/headless.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/cmd/ag/headless.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: execution permissions can remain human-governed, especially for bash/mutation classes, but the approval decision controls whether a proposed action may run rather than supplying the substantive coding choice.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at the reviewed session boundary.
- Disturbance / variety regulated: not applicable because the shipped coding session does not construct multiple operational coding S1 units whose interactions must be attenuated.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: sequential provider fallback, tool serialization, journal ordering and permission enforcement coordinate components of one operation but do not regulate interference among distinct S1 units.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: the active organization contains one coding agent; configured provider routes are alternate transports for that agent, not separate operational units with independently owned work commitments.
- Evidence: [internal/agent/loop.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/agent/loop.go); [internal/provider/router.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/provider/router.go); [README.md](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: fallback routing and tool ordering provide resilience/sequencing but do not create the distinct-S1 disturbance/feedback relation required for S2.

### Absence scope

- Surfaces inspected: core agent loop, provider router, tool registry, interactive/headless wiring, journal/history, compaction and recovery paths.
- Plausible first-party paths checked: provider-route fan-out/fallback, multiple tools, replay/resume branches, Goal Mode design and any agent delegation/multi-worker path.
- Why no material first-party path remains: all live coding paths converge on one model-backed agent and one session commitment; no peer coding S1 population or inter-S1 interference loop is constructed.

## S3 — Inside-and-now control

- State: —
- Function: no material separate whole-system current-control function is established at the declared recursion.
- Disturbance / variety regulated: current turn/context/rate-limit/tool pressures are handled by local budgets, deterministic policies and operator permission/cancellation rather than a metasystem actor deciding whole-session resources or commitments.
- Decisive decision or feedback right: none established for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: max-turn/rate-limit/spend/context budgets, provider fallback, circuit breaker, permission modes, cancellation, journal state and compaction thresholds.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: these mechanisms bound or retry one S1 operation. No distinct actor receives a whole-system current view and owns cross-operation resource allocation, prioritization or commitment regulation.
- Evidence: [internal/agent/budget.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/agent/budget.go); [internal/provider/router.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/provider/router.go); [internal/perm/policy.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/perm/policy.go); [cmd/ag/session.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/cmd/ag/session.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: provider route selection is current transport resilience and human approvals are local execution gates; neither establishes the Methodology's whole-system current-control loop.

### Absence scope

- Surfaces inspected: turn/spend/context/rate-limit budgets, provider router/circuit breaker, permission policies, UI status/cancellation, session state, compaction and recovery.
- Plausible first-party paths checked: dynamic route choice, current budget pressure, permission-mode changes, cancellation, active history mutation and headless exit-state logic.
- Why no material first-party path remains: the inspected paths enforce fixed/local policies around one S1; none assigns a separate whole-organization decision right for current resource/commitment/prioritization control.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is established in the shipped coding runtime.
- Disturbance / variety regulated: no separate first-party reviewer independently challenges the ordinary coding agent's completion/result and returns findings into corrective operation.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: read/process/tool results, loop detection, permission checks, journal/replay and recovery evidence can expose failures to the same operational loop but are not an independent complementary auditor.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: verification/tool evidence is consumed through the ordinary S1 observation path. Goal Mode documents a fresh-verification requirement, but its user-facing integration is incomplete at the frozen ref and it still dispatches the ordinary runner rather than a separate independent audit actor.
- Evidence: [internal/agent/loop.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/agent/loop.go); [docs/GOAL_MODE.md](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/docs/GOAL_MODE.md); [internal/store/jsonl.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/store/jsonl.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: auditability and verification instructions are valuable but do not satisfy S3* independence by themselves.

### Absence scope

- Surfaces inspected: agent/tool feedback path, Goal Mode contract/design, journal/replay, loop detection, permission gate, recovery/snapshot surfaces and repository test/security-review material.
- Plausible first-party paths checked: separate reviewer/verifier agent, independent replay auditor, verification gate, Goal Mode fresh verification, security/runtime policy checks and CI.
- Why no material first-party path remains: no shipped session constructs a distinct auditor with an independent access path whose findings return into S1 correction; adjacent tests/reports are outside the runtime boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective adaptation loop is established in the live runtime.
- Disturbance / variety regulated: provider/model availability, context pressure and future configuration needs are handled through configured routes, live listing and deterministic/local fallback rather than a separate actor interpreting outside/future evidence to adapt future organizational capability.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: `/models`, provider registry/configuration, route fallback/circuit breaker, compaction and context calibration expose or respond to operating conditions but do not autonomously decide a future capability redesign.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: the router selects among already configured routes for the current request, and the operator chooses configuration/model settings. No first-party actor converts external/future evidence into persisted adaptation of subsequent organizational capability.
- Evidence: [README.md](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/README.md); [internal/provider/router.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/provider/router.go); [internal/agent/compact.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/agent/compact.go); [cmd/ag/provider_commands.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/cmd/ag/provider_commands.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: provider discovery and fallback are environment-sensitive, but current-route resilience is not the outside-and-then adaptation function required for S4.

### Absence scope

- Surfaces inspected: provider discovery/router, route circuit breaker/retry, configuration, context calibration/compaction, persisted session state, skills and Goal Mode design.
- Plausible first-party paths checked: autonomous model/provider switching for future sessions, learned route/configuration updates, skill evolution, persistent policy tuning and model-assisted compaction.
- Why no material first-party path remains: observed external conditions affect the current request or inform human configuration; they are not turned by a first-party adaptation owner into a persisted future-capability change.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established at the reviewed runtime boundary.
- Disturbance / variety regulated: runtime safety and permission concerns are governed by static developer-authored policy plus operator approval, not by an in-boundary authority deciding the system's identity or ultimate principles.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes/policy, threat-model invariants, endpoint/config restrictions, system prompt, journal/security handling and explicit operator approvals.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent must operate inside the shipped permission/security rules and cannot authoritatively redefine them. Individual operator approvals and provider/config choices govern local actions, not the organization's identity/ultimate policy.
- Evidence: [internal/perm/policy.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/perm/policy.go); [docs/THREAT_MODEL.md](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/docs/THREAT_MODEL.md); [internal/agent/prompt.go](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/internal/agent/prompt.go); [README.md](https://github.com/amiraq1/Nabd/blob/1b7c36a5d79a20c055e688474b0ebc9fd916b7b3/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a human user legitimately controls individual execution permissions, but that parent seam does not close an identity/ultimate-policy feedback loop and is not promoted to P.

### Absence scope

- Surfaces inspected: permission policy/modes, threat model, prompt/configuration, endpoint restrictions, provider setup, journal/redaction and session commands.
- Plausible first-party paths checked: autonomous policy revision, parent constitution/governance path, durable identity artifact, operator mode as parent S5 and maintainer governance.
- Why no material first-party path remains: the rules are static inputs or local approvals; no runtime path establishes/revises identity-level policy and returns that authoritative decision into subsequent operation.

## Distributed OSS parent arrangement

The assessed organization is a local Nabd coding session, not the repository maintainer/contributor organization. Maintainers and distributed contributors are therefore not imported as parent S3/S4/S5 owners. The local operator controls permissions and configuration but does not close the function-specific parent loops required for a positive parent state.

## Self-hosted and non-human modes

Nabd can use configured hosted/provider routes and exposes headless operation that fails closed instead of reading a TTY for permission. Alternate permission modes, provider routes and resumed sessions preserve the same single-agent organization. They alter constraints/transport but do not establish additional VSM-function ownership.

## Recursion

One Nabd coding session is the viable-unit candidate. The active model-backed coding loop is the single material S1. Tools, providers, permission gate, event journal, shadow store, router and UI are supporting components. The human operator is an environmental/parent actor for individual permissions and static configuration, not a positive higher-function owner at this recursion.

## Variety and escalation

Operational variety is absorbed through model/tool iteration, bounded reads, tool repair, provider fallback, rate-limit budgets, permission refusal feedback, context compaction, recovery snapshots and rewind/undo. Router failure, budget exhaustion, denied actions and interruption can fail closed or return evidence to the same operational loop. These mechanisms improve resilience and recoverability without creating separate S2/S3/S3*/S4/S5 ownership.

## Evidence gaps

No `?` state is required. The frozen source exposes the core single-agent loop, provider routing, permission policy, journal/recovery architecture, interactive/headless wiring and documented Goal Mode integration state sufficiently to classify S1 positively and to establish no material first-party path for S2, S3, S3*, S4 or S5.
