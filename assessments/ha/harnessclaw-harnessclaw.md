---
harness_id: harnessclaw-harnessclaw
project_name: harnessclaw/harnessclaw
repository: https://github.com/harnessclaw/harnessclaw
review_ref: 44d01c1fa2193d1d4f479327cc15cf1bec09851c
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# harnessclaw/harnessclaw

## Review boundary

- System in focus: a desktop Harnessclaw application connected to its supported bundled Harnessclaw Engine and a configured LLM provider, running a user's agent session; not the maintainers' issue/reward organization.
- Purpose and identity: user-operated desktop AI-agent workspace for chat, tools, skills and session history, with interactive permissions and agent delegation.
- Relevant environment: user requests, model/tool output, browser and local file/command interactions, agent/subagent failures, provider configuration, interrupts and UI reconnects.
- Standard-distribution boundary: Electron main process, renderer and WebSocket client plus the separately published first-party `harnessclaw-engine` native runtime that the release build downloads and bundles. Engine source is in a *separate* public repository; this front-end frozen revision does **not** pin the released engine asset to an immutable SHA.
- Credited operating / distribution surfaces: `src/main/index.ts`, `src/main/harnessclaw.ts`, `src/main/browser-agent-session.ts`, main IPC and renderer agent/session UI, and packaged engine launch from `resources/bin` as specified by first-party release scripts. The observed public engine release `v0.0.22` (`a9d4b481e7af27a3d7c111d9e01629426fff1aba`) is supporting source evidence only, not a frozen-engine identity guarantee for every desktop build.
- Adjacent first-party surfaces excluded from ownership: Electron distribution/reward CI, release-change notes, design proposals, diagnostics/tests, agent team UI mockups, contributor governance and external browser-agent executable/provider internals. Engine release pipeline is a dependency, not credited as a live metasystem decision owner.
- First-party operating / deployment modes considered: packaged desktop app spawning native engine with config, WebSocket agent sessions, streamed tool/card events, user permissions/questions, optional subagent task dispatch and plan/step review prompts. At observed engine source the plan-coordinator tool mode explicitly fails during scheduler refactor.
- Recursion level: one configured desktop agent session and its supported delegated work; distinct higher-level multiple-user organizations or maintainers are outside scope.
- Reviewed revision: `harnessclaw/harnessclaw@44d01c1fa2193d1d4f479327cc15cf1bec09851c` (frontend) and explicitly identified public engine release `v0.0.22` as a conditional composed-mode witness, not silently repinned into the intake record.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Electron starts a platform-specific bundled native engine binary with a generated configuration and connects to its WebSocket endpoint. `HarnessclawClient` stores session card forests, streams main/subagent tool and text events, forwards user approval/plan/step responses and maps events into the React interface. Release preparation fetches platform engine runtime assets from the `harnessclaw/harnessclaw-engine` releases; binaries are not committed to this frontend checkout. At the observed engine tag, Go query-loop/provider/tool architecture implements task-specific model/tool interaction with subagent dispatch. The scheduler's `plan` mode explicitly returns an unavailable error in this tag, so UI prompt handlers are not enough to assert a functioning plan-coordinator owner. [App engine spawn](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/index.ts#L1000-L1046), [client session/card state](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/harnessclaw.ts#L94-L125), [runtime download](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/scripts/download-harnessclaw-runtime-release.cjs#L138-L160), [engine query-loop design at observed tag](https://github.com/harnessclaw/harnessclaw-engine/blob/a9d4b481e7af27a3d7c111d9e01629426fff1aba/README.md#L10-L49).

## Operational model

The human selects settings, provider, an agent and task. The native engine's model decides which tools and subagents to call and returns events over WebSocket; the desktop app hosts local tool/permission interaction and persistent UI. This supports one composed S1 agent runtime, not autonomous coordination/policy merely from dashboard, scheduler name or plan-review card. The current download selector may use latest release when an engine version is not explicitly set, so the positive finding is bounded to the observed supported engine composition.

## S1 — Operations

- State: A
- Function: perform model-selected tool and delegation actions to address user tasks within a supported desktop agent session.
- Disturbance / variety regulated: changing user task instructions, tool/browser/file outputs and provider or subagent responses.
- Decisive decision or feedback right: the native engine's LLM loop selects tool calls and continuation; desktop user gates particular actions.
- Decision owner: model-driven Harnessclaw Engine agent within the first-party distributed desktop/runtime composition.
- Supporting / enforcement mechanisms: spawned native engine, WebSocket session/card transport, permission requests, tool-result return, persisted session forest and provider configuration.
- Closure path: user/session message → engine model/tool cycle → tool or delegated result → engine continuation/finish → streamed cards and session result into desktop UI.
- Boundary reachability: release workflow bundles a real platform engine binary, Electron resolves and spawns it, and client starts authenticated sessions; engine tag v0.0.22 provides first-party source evidence for the observed distribution path. Frontend shell alone is not the claimed agent.
- Why this is / is not agent-owned: engine model/tool selection is discretionary, unlike static WebSocket card parsing or Electron launch code.
- Evidence: [packaged binary resolution and process](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/index.ts#L435-L440), [process spawn](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/index.ts#L1000-L1046), [engine query-loop README](https://github.com/harnessclaw/harnessclaw-engine/blob/a9d4b481e7af27a3d7c111d9e01629426fff1aba/README.md#L10-L50).
- Basis: structural supported packaged-mode wiring and a named observed engine release; not a live provider execution.
- Confidence: medium for stable source-to-binary correspondence given frontend's non-pinned runtime selector; high that a supported installed agentic mode is intentionally shipped.
- Caveats: do not generalize to unknown future engine assets, or treat mock/demo/event translation as a substitute for actual agent execution.

## S2 — Coordination

- State: —
- Function: no first-party S2-specific inter-S1 disturbance attenuation and returned adjustment is evidenced in the bounded available runtime path.
- Disturbance / variety regulated: subagent scheduling, card visibility and ordered task dispatch are generic work management until a concrete cross-worker collision/relation is established.
- Decisive decision or feedback right: agent may dispatch subagents; deterministic scheduler selects sync/async execution strategy, but does not demonstrate an inter-unit conflict resolution decision.
- Decision owner: native parent agent for delegation, scheduler for dispatch, not a distinct S2 attenuation actor.
- Supporting / enforcement mechanisms: subagent cards, event streams, scheduler `Dispatch`/`Subscribe`, tool permissions.
- Closure path: subagent tool requests and results return to the parent agent; no evidenced collision signal changes a second worker's subsequent operating conduct.
- Why this is / is not agent-owned: multiple workers and ordering are not, by themselves, viable inter-S1 coordination.
- Evidence: [client subagent event handling](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/harnessclaw.ts#L1235-L1261), [engine scheduler contract](https://github.com/harnessclaw/harnessclaw-engine/blob/a9d4b481e7af27a3d7c111d9e01629426fff1aba/internal/engine/scheduler/scheduler.go#L1-L29).
- Basis: reviewed supported frontend and tagged runtime source.
- Confidence: medium; current release selection is not immutable in this frontend ref.
- Caveats: a future coordinator with concrete inter-S1 collision control would need a new evidence-specific assessment.

### Absence scope

- Surfaces inspected: client card forest/agent trees, engine scheduler API and dispatch, plan/step prompt wiring and README.
- Plausible first-party paths checked: subagent task flow, sync/async scheduler, plan steps, browser tool serialization and session fan-out.
- Why no material first-party path remains: found delegation and event grouping but not a specified inter-agent disturbance, distinct attenuation decision and feedback into another worker at this tagged supported mode.

## S3 — Inside-and-now control

- State: —
- Function: no proven whole-system current resource/commitment control loop beyond user configuration, individual approvals and delegated task management.
- Disturbance / variety regulated: tool permissions, session failures, step retry/replan budgets, runtime restart and task progress.
- Decisive decision or feedback right: user can approve a local tool or answer a plan/step prompt; engine controls per-turn limits and task dispatch.
- Decision owner: user for local approvals, native model for operational task decisions, static engine for dispatch/limits.
- Supporting / enforcement mechanisms: permissions, step-decision WebSocket bookkeeping, session reconnect, scheduler tool.
- Closure path: UI replies unblock a pending individual tool/step; no demonstrated view/regulation of shared current whole-system commitments with a legitimate parent S3 decision loop. Tagged runtime's plan-coordinator tool mode returns unavailable.
- Why this is / is not agent-owned: an 'agent team' UI and a human gate are insufficient without a whole-system current-control decision owner and returned resource intervention.
- Evidence: [step/plan UI response](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/harnessclaw.ts#L2326-L2462), [runtime explicit unavailable plan mode](https://github.com/harnessclaw/harnessclaw-engine/blob/a9d4b481e7af27a3d7c111d9e01629426fff1aba/internal/tools/builtin/scheduler/scheduler.go#L133-L149).
- Basis: structural, release-bounded.
- Confidence: medium.
- Caveats: re-evaluate after engine coordinator restoration and explicit version pin.

### Absence scope

- Surfaces inspected: native engine scheduler tool, desktop plan/step responses, permission handling and session state.
- Plausible first-party paths checked: plan approval/retry/cancel gates, delegated task dispatch, tool allow/deny, engine hot reload and status UI.
- Why no material first-party path remains: these are task-level gates or unavailable plan orchestration, not demonstrated whole-system current-control closure.

## S3* — Complementary audit

- State: —
- Function: no independently owned complementary operational check of agent results is established.
- Disturbance / variety regulated: emitted tool/card summaries, developer diagnostics and prompt validation.
- Decisive decision or feedback right: same runtime emits progress; user may inspect outcomes; no distinct audit owner with alternative access channel.
- Decision owner: none in the installed task operation.
- Supporting / enforcement mechanisms: event log, card forest, error reports and tests.
- Closure path: ordinary execution telemetry is displayed but independent findings are not returned into a corrective management decision.
- Why this is / is not agent-owned: event viewing and user approvals lack a separate auditor and independent evidentiary path.
- Evidence: [stream/card conversion](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/harnessclaw.ts#L1136-L1259), [session logs](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/harnessclaw.ts#L166-L220).
- Basis: structural.
- Confidence: medium for observed runtime.
- Caveats: manual inspection by user is not credited as independent S3* agent authority.

### Absence scope

- Surfaces inspected: engine/browser-agent event frames, UI session history, permission prompts, tests and telemetry.
- Plausible first-party paths checked: subagent event reports, plan cards, tool logs, app diagnostics, release tests.
- Why no material first-party path remains: all surfaced paths are ordinary execution/diagnostics or adjacent developer tests; no distinct operational truth-checking actor closes correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective environment-scanning and capability-adaptation loop beyond model task planning or maintainer releases.
- Disturbance / variety regulated: new skills/models/providers, application updates and future tools.
- Decisive decision or feedback right: users/maintainers install skills, configure model settings and ship releases.
- Decision owner: adjacent human user/developer, not a first-party future-intelligence actor.
- Supporting / enforcement mechanisms: skills market, engine config, updater, release pipeline.
- Closure path: configuration/release can change future sessions; no autonomous outside-and-then option-development decision visibly returns to current operations.
- Why this is / is not agent-owned: planning an assigned coding task is S1; installing a skill is a user action, not system-level S4.
- Evidence: [skills market](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/skills-market.ts), [runtime and update code](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/updater.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: a later engine release may add such a loop; the front-end selector is not pinned.

### Absence scope

- Surfaces inspected: skills market, models/settings, updater, tagged engine prompt and scheduler code.
- Plausible first-party paths checked: skill discovery, model switching, task planning, updates and future coordinator notes.
- Why no material first-party path remains: choices are user-maintainer-driven or within task execution, not first-party S4 adaptation closure.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate-purpose or organizational identity decision loop at one desktop agent-session recursion.
- Disturbance / variety regulated: permission modes, tool allow/deny, user questions and agent personas.
- Decisive decision or feedback right: user sets tool permissions and responds to individual approvals; engine applies rules.
- Decision owner: task user and deterministic enforcement, not a designated S5 ultimate-authority mode.
- Supporting / enforcement mechanisms: tool allow/deny, session user prompts, profile/skill settings.
- Closure path: decisions unlock specific tool or conversation operations; no identity-policy dispute returns to govern S3/S4.
- Why this is / is not agent-owned: permission is operational risk control, not identity-level policy/constitutional legitimacy.
- Evidence: [permission client](https://github.com/harnessclaw/harnessclaw/blob/44d01c1fa2193d1d4f479327cc15cf1bec09851c/src/main/harnessclaw.ts#L2835-L2874), [permissions at engine tag](https://github.com/harnessclaw/harnessclaw-engine/blob/a9d4b481e7af27a3d7c111d9e01629426fff1aba/README.md#L35-L45).
- Basis: structural.
- Confidence: medium.
- Caveats: software community governance is outside this one-session system boundary.

### Absence scope

- Surfaces inspected: tool permission rules, user-request prompts, engine config and frontend agent settings.
- Plausible first-party paths checked: high-risk tool approvals, plan review, agent identity/persona configuration and maintainer governance.
- Why no material first-party path remains: no supported identity-level issue is decided by a legitimate ultimate authority with returned organizational control.

## Distributed OSS parent arrangement

Maintainer release and community reward workflows alter software distribution, not the governance of a user's live agent session. The separately maintained public engine source is first-party runtime dependency only when included in a supported packaged mode.

## Self-hosted and non-human modes

The desktop client uses a local engine with configurable provider; a public engine release is bundled in installed builds. Its release selector is version-optional, so source of a future downloaded engine cannot be inferred from the frontend SHA. No autonomous higher-parent mode is credited from this dynamic release channel.

## Recursion

One desktop engine session can delegate work to subagents. The scheduler and UI surface their results to its parent agent; multiple agent cards do not alone establish independently viable recursive units with S2–S5 authority.

## Variety and escalation

Tool permissions, session state/replay, retry limits and user prompts bound local risks. UI plan/step decision gates can represent exceptional task events, but without a reachable whole-system receiving authority and closed regulator path they do not establish S3/S4/S5 or a formal algedonic channel.

## Evidence gaps

- Live provider, browser and native-engine execution was not performed. Positive S1 rests on source and supported packaged-mode integration; task quality is unmeasured.
- Engine binary identity is not pinned by the frontend `review_ref`; the public `v0.0.22` tag is an explicitly dated supporting witness, not a commitment that all releases or installs use that commit.
- The tagged engine disables `plan` coordinator mode during refactor; do not infer active S2/S3 control from frontend plan-card and step-decision types alone. Later engine changes would require a new bounded review.
