---
harness_id: super-agent
project_name: super-agent
repository: https://github.com/FedericoCasarella/super-agent
review_ref: afa4850f4cf698db8ce868525c6dad3215a13a6d
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
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# super-agent

## Review boundary

- System in focus: the first-party `super-agent` personal-agent runtime at pinned revision `afa4850f4cf698db8ce868525c6dad3215a13a6d`, including its scheduler, internal-agent registry, persistent second brain, goal/roadmap control surfaces, sub-agent/team lifecycle, connector/MCP bridge, Telegram/web control surfaces and first-party prompts around model execution.
- Purpose and identity: maintain a persistent personal AI organization that can operate through chat, scheduled/background workers, knowledge maintenance, goals, connectors and delegated agents while keeping consequential action under explicit user control.
- Relevant environment: the user and their communication patterns, business goals/KPIs, email/WhatsApp/Instagram/Telegram channels, local files and vaults, GitHub/RSS feeds, external MCP services, model providers and the local host on which Claude Code subprocesses execute.
- Standard-distribution boundary: `super-agent` owns the scheduler, prompts, persistent state, internal-agent definitions, goal/proposal machinery, connector bridge, web/Telegram control surfaces and subprocess lifecycle. Claude Code CLI is a separate reasoning/runtime substrate; its internal organizational functions are not credited merely because `super-agent` launches `claude -p`.
- Credited operating / distribution surfaces: `backend/src/index.ts`; `backend/src/agent/orchestrator.ts`; `backend/src/claude/runner.ts`; `backend/src/scheduler/index.ts`; `backend/src/agents/internal/registry.ts`; `backend/src/agents/internal/goal_pursuit.ts`; `backend/src/agents/internal/goal_steward.ts`; `backend/src/agents/internal/vault_librarian.ts`; `backend/src/agent/tone_mirror.ts`; `backend/src/claude/prompts.ts`; `backend/src/goals/index.ts`; `backend/src/sub_agents/index.ts`; `backend/src/connectors/builtin/agent/index.ts`; `frontend/src/pages/Dashboard.tsx`.
- Adjacent first-party surfaces excluded from ownership: repository-development scripts and CI; generic logs/tool-event traces; brain snapshots/backups; UI naming such as `orchestrator`, `COO`, `steward`, `manager` or `agent` where behavior does not independently establish the corresponding VSM function.
- First-party operating / deployment modes considered: interactive Telegram conversation, scheduled internal-agent operation, proactive reflection, goal pursuit/steward review, approved background sub-agents, custom team tasks, connector/flow automation and authenticated dashboard control.
- Recursion level: one installed `super-agent` user organization, with concurrent scheduled/internal/sub-agent/team executions treated as candidate S1 operating units when they perform distinct work for that user.
- Reviewed revision: `afa4850f4cf698db8ce868525c6dad3215a13a6d`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

`super-agent` wraps Claude Code CLI as its principal model/runtime substrate but keeps substantial organization in first-party TypeScript. The backend starts the interactive orchestrator, scheduler, flow dispatchers, channel bots and recovery loops only after the process successfully owns its listening port. The scheduler then drives proactive reflection, connector ticks, internal agents, snapshots and other maintenance work.

Internal agents are registered as first-party operating roles and have persistent per-user schedules/status. They can read external or operational state, call the model, write the durable vault, update goal state and report through Telegram. Separately, the main interactive path builds a first-party system/turn prompt, executes Claude Code headlessly and closes model/tool results back into persistent state and chat.

The runtime also exposes parent control: the authenticated dashboard aggregates current operational state and active agents, Telegram carries approval keyboards, and goal plans/actions are deliberately staged for user approval before execution.

## Operational model

Interactive work enters through Telegram, is deduplicated/queued per user, receives persistent brain and roadmap context, and is executed through a headless Claude Code subprocess with first-party MCP tools and return handling. Scheduled work enters through `node-cron`: internal agents and reflection cycles are claimed, run and persisted by `super-agent` without a new user message.

Multiple such runs can coexist. `runClaude` therefore owns a global concurrency gate: the repository explicitly records that background/reflection/vault runs previously saturated the machine and produced spawn failures/timeout pile-ups, so excess runs now wait in a first-party queue until a slot is released.

For strategic/current control, the dashboard exposes live activity while goal planning and daily/weekly goal regulation feed proposals back to the user. The parent decides whether staged plans and operational action batches are approved. For adaptation, the nightly Tone Mirror reads that day's user conversation, autonomously revises `meta/user-profile.md`, and subsequent standard turns inject that durable profile into their system context.

## Primary evidence

- [`README.md`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/README.md) — product/runtime boundary, Claude Code substrate, scheduled internal agents, approval model, connectors, teams and dashboard.
- [`backend/src/index.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/index.ts) — standard boot wiring for orchestrator, scheduler, flows, channel bots and recovery.
- [`backend/src/agent/orchestrator.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/agent/orchestrator.ts) — first-party interactive queue/dedupe, prompt construction, Claude execution and return path.
- [`backend/src/claude/runner.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/claude/runner.ts) — Claude subprocess boundary, tool/runtime wrapping and global concurrency queue built in response to concrete host saturation.
- [`backend/src/agents/internal/registry.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/agents/internal/registry.ts) — first-party internal-agent registry, scheduling, atomic due-run claims, persistence and notification closure.
- [`backend/src/agents/internal/goal_pursuit.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/agents/internal/goal_pursuit.ts) — autonomous goal-state analysis and strategy-correction reasoning, with operational action batches deliberately gated by parent approval.
- [`backend/src/agents/internal/goal_steward.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/agents/internal/goal_steward.ts) — weekly KPI/outcome review and user-approved next-action proposals.
- [`backend/src/goals/index.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/goals/index.ts) — staged goal-plan generation/revision, explicit user approval and returned activation/action proposal path.
- [`backend/src/sub_agents/index.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/sub_agents/index.ts) — user approval/denial of proposed work and first-party background execution lifecycle.
- [`frontend/src/pages/Dashboard.tsx`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/frontend/src/pages/Dashboard.tsx) — current-state aggregation of agent state, active agents, messages, tool activity and live operational indicators plus wake control.
- [`backend/src/connectors/builtin/agent/index.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/connectors/builtin/agent/index.ts) — first-party parent controls for quiet/sleep/wake, roadmap/strategy/KPI manipulation, team/sub-agent operations and related management paths.
- [`backend/src/agent/tone_mirror.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/agent/tone_mirror.ts) — nightly autonomous adaptation of durable user behavioral/tone profile from current user interaction evidence.
- [`backend/src/claude/prompts.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/claude/prompts.ts) — standard future-turn injection of the Tone Mirror profile and the hard-coded runtime identity/policy framing inspected for S5.
- [`backend/src/agents/internal/vault_librarian.ts`](https://github.com/FedericoCasarella/super-agent/blob/afa4850f4cf698db8ce868525c6dad3215a13a6d/backend/src/agents/internal/vault_librarian.ts) — additional external RSS/GitHub sensing and durable curation; corroborating S4 evidence but not used alone as adaptation closure.

## S1 — Operations

- State: A
- Function: perform user-facing and background personal-agent work through interactive turns, scheduled internal agents, persistent knowledge maintenance, goal work and approved delegated executions.
- Disturbance / variety regulated: open-ended user requests, external communications, changing vault/goal state, scheduled maintenance needs, information intake and task-specific tool results.
- Decisive decision or feedback right: within an admitted operating run, choose how to interpret evidence, what knowledge/action output to produce, which tool/path to use and how to close the assigned outcome within first-party prompts and permissions.
- Decision owner: model-driven operating actors invoked by the first-party orchestrator/internal-agent/task definitions.
- Supporting / enforcement mechanisms: Telegram ingestion queue, scheduler and atomic claims, `runClaude`, MCP bridge, connector tools, vault persistence, run status, retries/timeouts and approval gates around consequential delegated actions.
- Closure path: user/schedule/environment trigger → first-party operating prompt/agent role → model decision/tool use → changed vault/goal/channel/task state or produced result → persisted status/output and subsequent operation/user notification.
- Boundary reachability: standard backend startup directly enables the interactive orchestrator and scheduler; the internal-agent registry is started by `startScheduler`, while approved sub-agent/team work is reachable from standard Telegram/web/MCP surfaces.
- Why this is / is not agent-owned: `super-agent` defines the operating roles, prompts, triggers, state and closure paths, while the model actor supplies material discretion inside those paths. Claude Code is the execution substrate, but no internal Claude organizational functions are imported as evidence.
- Evidence: `backend/src/index.ts`; `backend/src/agent/orchestrator.ts`; `backend/src/agents/internal/registry.ts`; internal-agent implementations; `backend/src/sub_agents/index.ts`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: not every spawned Claude process is automatically a distinct viable S1; the positive claim concerns first-party operating loops that produce durable/user-relevant outcomes.

## S2 — Coordination

- State: C
- Function: attenuate destructive host-resource interference among concurrent model-driven S1 runs by preventing unbounded simultaneous Claude subprocess execution.
- Disturbance / variety regulated: concurrent chat, reflection, proactive, vault/internal-agent and sub-agent runs can accumulate long-running Claude subprocesses, saturate the host, cause OS spawn refusal and create timeout pile-ups.
- Decisive decision or feedback right: apply a shared concurrency ceiling and queue excess runs until capacity is released.
- Decision owner: first-party deterministic runtime policy in `runClaude`; the limit can be configured by environment, but no autonomous coordinator chooses/revises the response from observed competing S1 needs.
- Supporting / enforcement mechanisms: `MAX_CONCURRENT_CLAUDE`, `activeClaude`, `claudeWaitQueue`, `acquireClaudeSlot()` and `releaseClaudeSlot()`.
- Closure path: S1 run requests Claude capacity → gate admits it or places it in the wait queue → completion releases/passes the slot → waiting run proceeds later rather than competing simultaneously for the same saturated host capacity.
- Why this is / is not agent-owned: the repository documents the concrete interference and ships a disturbance-specific attenuation loop, but the coordination decision is deterministic host enforcement rather than autonomous S2 discretion. That supports constructor state `C`, not `A`.
- Evidence: `backend/src/claude/runner.ts`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: agent-to-agent networking, team delegation, queues and orchestration are not separately counted as S2 without an evidenced inter-S1 disturbance.
- Distinct S1 units: interactive chat turns, proactive/reflection/internal-agent runs and approved background sub-agent runs may concurrently execute distinct user outcomes through separate Claude subprocesses.
- Inter-S1 disturbance: the runner source explicitly records that concurrent background/reflection/vault work saturated the machine, produced `posix_spawnp`/PTY failures and caused timeout accumulation.
- Attenuating coordination relation: the shared first-party concurrency semaphore queues runs over the configured ceiling instead of allowing them to consume host execution capacity simultaneously.
- Feedback into subsequent S1 behaviour: a blocked run does not spawn its Claude subprocess until `releaseClaudeSlot()` transfers/frees capacity, directly changing the timing of later S1 execution.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the queue is explicitly tied to a concrete cross-run host-capacity interference mode and exists to damp that instability, rather than merely ordering work for convenience.
- Boundary reachability: every first-party path that calls `runClaude` passes through this concurrency gate in the shipped runtime.

## S3 — Inside-and-now control

- State: P
- Function: provide a whole-installation current view and parent intervention over running work, agent activity, pauses/quiet state, approved plans and consequential delegated commitments.
- Disturbance / variety regulated: simultaneous current agent runs, queued/background commitments, stalled or unwanted work, timing/notification state and proposed goal/sub-agent actions that may need to be admitted, stopped or deferred for the organization as a whole.
- Decisive decision or feedback right: decide whether staged plans/actions become active commitments and whether current agent operation is woken, paused/quieted, approved, denied or otherwise intervened upon across the installation.
- Decision owner: the authenticated human user/owner through first-party dashboard/Telegram/control-tool surfaces.
- Supporting / enforcement mechanisms: dashboard state aggregation, active-agent/run persistence, internal-agent enable/schedule state, quiet/sleep/wake settings, goal `pending_plan`, proposal keyboards, proposal status and sub-agent/task lifecycle enforcement.
- Closure path: first-party surfaces aggregate current installation state or surface a pending commitment → user decides wake/quiet/approve/deny/plan activation or related intervention → backend persists/enforces the decision → subsequent current S1 scheduling/execution changes.
- Why this is / is not agent-owned: goal agents may analyze current KPIs and recommend/correct strategy notes, but they intentionally do not deploy consequential action batches or activate a pending goal plan without the user. The parent owns the decisive cross-operation commitment/control right.
- Evidence: `frontend/src/pages/Dashboard.tsx`; `backend/src/connectors/builtin/agent/index.ts`; `backend/src/goals/index.ts`; `backend/src/sub_agents/index.ts`; `backend/src/agents/internal/goal_pursuit.ts`; `backend/src/agents/internal/goal_steward.ts`.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: naming `goal_steward` a COO and calling the main path an orchestrator are not used as S3 evidence; the positive mapping is the parent's actual whole-installation control path.
- Whole-system current view: the dashboard combines agent sleep/quiet/working state, active/pending background agents, recent messages/tool activity and live KPI/status feeds, while related first-party pages expose internal agents, teams, tasks, flows, goals and logs.
- Current-control decision scope: wake/quiet/sleep regulation; enable/schedule choices; approval or denial of proposed sub-agent batches; approval/rejection of generated goal plans and resulting active commitments; intervention in current delegated work through first-party task/agent controls.
- Boundary reachability: dashboard and Telegram approval surfaces are ordinary authenticated product paths, and the returned decisions are persisted by the same backend that schedules/executes subsequent work.

## S3* — Complementary audit

- State: —
- Function: no qualifying complementary independent audit function is established at the declared installed-runtime boundary.
- Disturbance / variety regulated: the review looked for operational claims or conditions checked through a materially different access path capable of challenging ordinary S1/S3 reporting.
- Decisive decision or feedback right: no first-party independent audit judgment was found that compares an ordinary operational claim with complementary reality and returns a finding into current control.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: persisted agent runs, tool-call traces, logs, status pages, brain snapshots, watchdogs and recovery/reaper loops provide observability, durability or deterministic recovery rather than complementary audit ownership.
- Closure path: logs/status can be inspected and watchdogs can detect narrow runtime conditions, but no distinct ordinary-report claim → independent evidence path → audit judgment → returned S3 corrective loop is established.
- Why this is / is not agent-owned: tracing is emitted by the same runtime path whose behavior it records; snapshots copy first-party state; watchdogs/reapers enforce known runtime conditions. None supplies sufficiently independent audit access and judgment over operational claims.
- Evidence: dashboard/log surfaces; scheduler watchdog/recovery paths; run/tool persistence; snapshot paths inspected alongside primary runtime files.
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: rich observability and deterministic health recovery are useful control infrastructure but are not automatically S3*.

### Absence scope

- Surfaces inspected: dashboard/tool events, agent-run records, scheduler watchdogs/reapers, brain snapshots, connector status checks, goal reports and normal model/tool result paths.
- Plausible first-party paths checked: runtime health checks, stale-run recovery, raw tool traces, snapshot comparisons/backup surfaces, current KPI reports and user-visible logs.
- Why no material first-party path remains: these paths observe, copy or enforce state produced by the same operating organization; none establishes a sufficiently independent complementary reality check with an audit judgment that feeds current control.

## S4 — Outside-and-then intelligence

- State: A
- Function: adapt future personal-agent interaction behavior from changing user-environment evidence by autonomously revising a durable behavioral profile that standard future turns consume.
- Disturbance / variety regulated: the user's communication style can change over time — vocabulary, formality, message length, punctuation, energy, slang/irony and interaction preferences — making the current response style progressively less fitted to its user environment.
- Decisive decision or feedback right: infer which durable tone/profile changes are warranted from the day's conversation and rewrite the corresponding `meta/user-profile.md` adaptation for future operation.
- Decision owner: the model actor invoked by the first-party nightly Tone Mirror routine; it analyzes user evidence and chooses the content of the revised profile without an approval step.
- Supporting / enforcement mechanisms: nightly scheduler, daily-message query, minimum-signal threshold, vault read/write access and `buildSystemContext()` loading of the resulting profile.
- Closure path: changing user communication evidence → nightly model analysis → autonomous rewrite/refinement of `meta/user-profile.md` → later `buildSystemContext()` reads `LIVE USER BEHAVIORAL PROFILE` → subsequent standard model turns are instructed to mirror the adapted profile.
- Boundary reachability: `startScheduler()` installs Tone Mirror as a standard nightly task, and every ordinary interactive turn builds system context through `buildSystemContext()`, which reads the same durable profile file when present.
- Why this is / is not agent-owned: fixed scheduling and minimum-message thresholds only trigger/enforce the cycle. The model actor decides what the environmental evidence means and what behavioral adaptation to encode, and the first-party runtime closes that choice into later operation without parent approval.
- Evidence: `backend/src/agent/tone_mirror.ts`; `backend/src/scheduler/index.ts`; `backend/src/claude/prompts.ts`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `Vault Librarian` provides additional external RSS/GitHub intelligence, but generic information ingestion is not relied on to establish S4. The positive mapping uses the stronger Tone Mirror adaptation/return loop.
- External distinction: observed user communication behavior from the current day is treated as environmental evidence about how the system should interact with its user.
- Future / prospective distinction: the routine asks whether the durable behavioral/tone profile should be refined so later responses better fit the user's evolving communication style.
- Adaptation option generated: a model-selected update/refinement to the `Tone of voice` and related durable behavioral profile content in `meta/user-profile.md`.
- Path back into current capability / S3: the updated profile is read into the standard system context for subsequent interactive operation, materially changing the instructions governing future S1 responses; the parent can still intervene through the S3 control surfaces if current behavior is unwanted.

## S5 — Policy and identity

- State: —
- Function: no distinct runtime identity/ultimate-policy closure is established at the declared installation recursion.
- Disturbance / variety regulated: the review looked for an identity-level or ultimate-policy issue that can be raised, decided by legitimate authority and returned to govern subsequent `super-agent` operation.
- Decisive decision or feedback right: no separate first-party path was found that closes ultimate identity/policy questions for the installed organization.
- Decision owner: none established for qualifying S5 at this recursion.
- Supporting / enforcement mechanisms: the runtime contains hard-coded conductor/purpose instructions, user/profile/business settings, roadmap vision/mission/pillars/bets, goal-plan approvals, permission/approval gates and configurable agent/team prompts.
- Closure path: ordinary strategy, task, goal and permission choices can return to operation, but the evidence does not establish a distinct identity/ultimate-policy issue → legitimate authority decision → returned organization-wide identity closure path.
- Why this is / is not agent-owned: the base system context includes durable first-party identity/purpose language such as the personal-advisor/conductor framing and `YOUR ONE JOB: improve user's business outcomes`; user roadmap strategy and approvals regulate work but are not shown to hold authority over that ultimate runtime identity. A system prompt or generic human final say is not sufficient S5 evidence.
- Evidence: `backend/src/claude/prompts.ts`; `backend/src/roadmap/index.ts`; `backend/src/connectors/builtin/agent/index.ts`; `backend/src/goals/index.ts`; onboarding/settings surfaces inspected in the standard distribution.
- Basis: explicit + structural absence.
- Confidence: medium-high.
- Caveats: this does not say the user lacks product control. It says the reviewed controls do not prove S5 closure under the Profile's stricter identity/ultimate-policy test.

### Absence scope

- Surfaces inspected: hard-coded system context, onboarding profile/business state, roadmap v2 strategy (`vision`, `mission`, `pillars`, `bets`), goal creation/plan approval, quiet/sleep/push settings, custom agent/team prompts and general approval/permission surfaces.
- Plausible first-party paths checked: direct strategy editing, goal-plan revision/approval, runtime behavior calibration and user authority over consequential actions.
- Why no material first-party path remains: those paths alter strategy, configuration or ordinary commitments, while the installation's ultimate personal-advisor/conductor identity remains first-party prompt policy; no explicit identity-level escalation/decision/return mechanism at the installation boundary is evidenced.

## Recursion

The assessed boundary is one installed `super-agent` organization for one user. Internal agents, interactive turns, sub-agents and team members are operating units only where they perform distinct durable/user-relevant work; their names or process count do not prove lower-level viability. External Claude Code and MCP services remain substrates/environment unless a separate boundary-specific assessment establishes their own VSM organization.

## Variety and escalation

`super-agent` attenuates operational variety through per-user message dedupe/debounce, the global Claude concurrency queue, atomic scheduler claims, quiet/sleep modes, proposal deduplication, approval gates, retries and reapers. It amplifies operational repertoire through connectors, MCP tools, internal agents, teams and external information sensing. Current commitments and consequential action batches escalate to the parent user, supporting `S3=P`. Tone Mirror turns changing user-environment evidence into autonomous future behavioral adaptation, supporting `S4=A`. No reviewed path turns roadmap or generic approvals into installation-level S5 identity closure.

## Evidence gaps

- The S2 constructor classification is deliberately narrow: it is the evidenced host-capacity interference/queue loop, not agent plurality or task routing.
- S3 remains parent-governed because goal-analysis agents propose consequential work but the shipped paths reserve activation/approval of those commitments to the user.
- S3* is not inferred from rich logs, snapshots or watchdogs because those lack a sufficiently independent complementary audit judgment.
- S4 is credited specifically to the Tone Mirror environmental adaptation loop; external news/library ingestion alone would not satisfy the Profile's return-to-capability requirement.
- Claude Code CLI is excluded from first-party ownership; its internal planning, tool policy or autonomy is not transferred to `super-agent`.

## Admission conclusion

Standalone vector at the pinned revision: `A C P — A —`.
