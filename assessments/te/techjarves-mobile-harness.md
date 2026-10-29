---
harness_id: techjarves-mobile-harness
project_name: techjarves/Mobile-Harness
repository: https://github.com/techjarves/Mobile-Harness
review_ref: 96b1da08d03af4f2d63970a3794c7fda068948c4
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# techjarves/Mobile-Harness

## Review boundary

- System in focus: one installed Android Mobile Harness workspace with a user-selected Claude Code, DeepSeek Harness or Antigravity coding-agent runtime operating on a project; not all external model providers or the developer's release organization.
- Purpose and identity: let a phone user delegate project development to an installed coding agent, inspect its actions and files, and work in a local Linux toolchain.
- Relevant environment: project file changes, interactive tool approvals, agent and API-provider failures, Android background-process restrictions, user turns, build/terminal contention and toolchain installation state.
- Standard-distribution boundary: Android application/Compose UI, `MainViewModel`, first-party `AgentRegistry`, runtime bridges, PRoot workspace, session event handling and user-control/checkpoint hooks together with explicitly installed supported external agent CLIs.
- Credited operating / distribution surfaces: `app/src/main/java/com/jarves/mh/ui/MainViewModel.kt`, `runtime/AgentDriver.kt`, `runtime/RuntimeBridge.kt`, `runtime/ClaudeRuntimeBridge.kt`, `runtime/DshRuntimeBridge.kt`, `runtime/AntigravityRuntimeBridge.kt`, `runtime/WorkspaceCheckpoints.kt` and the documented installed Android distribution.
- Adjacent first-party surfaces excluded from ownership: Gradle/CI packaging, release scripts, `scripts/runtime-bundles/` builders, app unit tests, example screenshots, website/demo, maintainer roadmap and Android runtime bundle construction; external Claude/DeepSeek/Antigravity CLI model logic is credited only through the supported composed runtime mode, not as authored here.
- First-party operating / deployment modes considered: on-device PRoot Linux runtime with user-selected agent/provider, guided setup, explicit per-agent driver selection, resumable chats, optional API gateways, terminal/Android build, queued follow-ups, user approvals and undo/keep changes.
- Recursion level: a user-owned Android project agent workspace as operating cell, with the selected native coding agent's tool decisions furnishing S1; externally managed parallel projects and developer governance are outside this cell.
- Reviewed revision: `techjarves/Mobile-Harness@96b1da08d03af4f2d63970a3794c7fda068948c4`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Compose application selects one of three declared `AgentDriver`s and stores a project/chat/provider context. `MainViewModel.sendPrompt` validates state, queues user follow-ups while an agent or build is running, persists messages and calls the selected `RuntimeBridge.startSession`. The Claude bridge builds a provider environment, starts an installed `claude` executable in a PRoot workspace, consumes stream events and tool approvals, captures changed files, emits completion/failure, and exposes user stop/undo/keep actions. DeepSeek and Antigravity have separate bridges and native CLI dependencies. The installed native coding agent, not UI dispatch, chooses coding-task actions. [Driver registry](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/runtime/AgentDriver.kt#L1-L86), [prompt/queue/session](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/ui/MainViewModel.kt#L4661-L4798), [native process/events](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/runtime/ClaudeRuntimeBridge.kt#L96-L282), [README capabilities](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/README.md#L91-L136).

## Operational model

The Android user chooses project, coding agent, prompt and credentials. The external installed coding-agent CLI conducts its own model/tool cycle inside the app-provided workspace. First-party bridges provide I/O, process lifetime, checkpoints, UI and explicit user controls. A queue of follow-up prompts on the same agent session is not a second independent S1; neither UI routing nor the bundled model gateway is itself an agentic strategic manager.

## S1 — Operations

- State: A
- Function: execute a user-delegated development task via a supported installed autonomous coding agent and return code/tool outcomes in the Android workspace.
- Disturbance / variety regulated: changing project state, build errors, command/tool feedback, user prompt and local file artifacts.
- Decisive decision or feedback right: the selected native agent decides concrete reasoning, file edits, tool uses and subsequent actions; the user selects task and authorization envelope.
- Decision owner: Claude Code, DeepSeek Harness or Antigravity installed agent, according to chosen supported mode, within the composed Android operating cell.
- Supporting / enforcement mechanisms: `AgentRegistry`, stream-event bridge, PRoot workspace, tool approval dispatch, checkpoints and changed-file reports.
- Closure path: `sendPrompt` → selected `startSession` → native agent CLI/model decides tool actions against workspace → stream events and changed files → `SessionCompleted`/`SessionFailed` in UI.
- Boundary reachability: drivers explicitly register all three built-ins and the app's `activeRuntime().startSession` connects to the installed native CLI via first-party bridges; not merely screenshots or unreached example code.
- Why this is / is not agent-owned: without the selected coding agent's discretionary model/tool cycle, Android prompt transport and Linux process launch alone cannot select task-specific code changes.
- Evidence: [registry and capabilities](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/runtime/AgentDriver.kt#L26-L85), [VM invocation](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/ui/MainViewModel.kt#L4727-L4785), [CLI launch](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/runtime/ClaudeRuntimeBridge.kt#L151-L193).
- Basis: structural supported installed-mode wiring, not a live agent run.
- Confidence: medium-high for a reachable agentic mode; no claim about quality or Android device compatibility.
- Caveats: bare Android UI/terminal alone is not autonomous; the third-party native agent and configured model/provider must actually be present.

## S2 — Coordination

- State: —
- Function: no first-party loop coordinates a pair of distinct S1 operations against an inter-S1 disturbance inside the declared project cell.
- Disturbance / variety regulated: the prompt queue and active terminal/build exclusion avoid concurrent local tool use, not interference between distinct autonomous S1 units.
- Decisive decision or feedback right: user can reorder and interrupt follow-ups on a single selected agent; ViewModel applies predetermined queue/runtime gates.
- Decision owner: human project user for steering, deterministic ViewModel for execution; no S2-specific autonomous owner or constructed inter-unit control.
- Supporting / enforcement mechanisms: `pendingFollowUps`, `steerQueuedFollowUp`, `stopActiveSession`, terminal/build running flags.
- Closure path: follow-ups are held or moved and the single current session stops; no two autonomous workers' competing activity is jointly regulated.
- Why this is / is not agent-owned: agent-kind choices are alternatives, not simultaneously coordinated operational units; sequencing user prompts is not inter-S1 attenuation.
- Evidence: [queue/steer](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/ui/MainViewModel.kt#L4661-L4730), [runtime selection](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/runtime/AgentDriver.kt#L26-L85).
- Basis: source inspection of standard deployed project UI.
- Confidence: medium-high.
- Caveats: external multi-agent compositions are not credited without an explicit supported shared-control pathway.

### Absence scope

- Surfaces inspected: agent registry, MainViewModel queue/steer/runtime selection, three runtime bridges and README.
- Plausible first-party paths checked: competing selected agents, queued follow-ups, terminal/build conflict gates, resumable chats.
- Why no material first-party path remains: only one selected agent is active at a time, while scheduling gates do not report inter-agent interference or implement S2-specific return to a distinct competing S1.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current control over a portfolio of operating commitments is evidenced at the selected project-agent recursion.
- Disturbance / variety regulated: current session faults, tool-approval requests, queued follow-ups, build/terminal availability and altered files.
- Decisive decision or feedback right: the user may approve/deny a tool, stop the agent, move a queued prompt or keep/undo files; preset state guards avoid simultaneous processes.
- Decision owner: user for local task interventions, native agent for task work, static ViewModel logic for queue and process guards.
- Supporting / enforcement mechanisms: `answerApproval`, `stopTask`, `steerQueuedFollowUp`, `undoLastChanges`, runtime completion/failure flags.
- Closure path: particular requests and interrupts change the current tool/session; a discretionary common current-resource/priorities judgment over the whole system is not shipped or entrusted to a supported parent-level authority loop.
- Why this is / is not agent-owned: UI control of one live job and local file approval are not, without a shared current-system view and broader resource/commitment bargaining, S3 autonomy or a proven S3 parent mode.
- Evidence: [user controls](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/ui/MainViewModel.kt#L4695-L4835), [runtime stop](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/runtime/ClaudeRuntimeBridge.kt#L348-L365).
- Basis: structural; tested local controls are not presumed higher-recursion governance.
- Confidence: medium.
- Caveats: a separately defined project portfolio with an operator-governed S3 could exist outside the reviewed cell.

### Absence scope

- Surfaces inspected: MainViewModel active-project/session view, queue/steering, checkpoints, bridge stop/approval, README workspace.
- Plausible first-party paths checked: user steering of queued tasks, app foreground supervision, permissions, provider retry, build/terminal contention.
- Why no material first-party path remains: all identified decisions target one task/session or preconfigured process gates, without a first-party whole-of-system regulatory decision and returned shared operating commitments.

## S3* — Complementary audit

- State: —
- Function: no independent second access channel and audit owner check the correctness of agent work against operational reality.
- Disturbance / variety regulated: file changes, process errors, approval requests and agent event stream.
- Decisive decision or feedback right: user reviews changed files and can accept/undo; the bridge reports agent process/file telemetry.
- Decision owner: external human reviewing local edits, not an independently executing first-party auditor.
- Supporting / enforcement mechanisms: workspace snapshots/checkpoints, changed-file diffs, event logs and local tests.
- Closure path: changed files are surfaced for human decision; no complementary evidentiary source independently assesses agent claims and returns a corrective finding into agent control.
- Why this is / is not agent-owned: a checkpoint can support inspection but is not autonomous, complementary operational audit.
- Evidence: [snapshot and change events](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/runtime/ClaudeRuntimeBridge.kt#L140-L260), [undo/keep](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/ui/MainViewModel.kt#L4814-L4840).
- Basis: source-first.
- Confidence: medium-high.
- Caveats: a human may manually inspect work; that is not an independent S3* finding established in this assessment.

### Absence scope

- Surfaces inspected: bridge event parsing, checkpoints, pending changes, UI user decisions, tests and README.
- Plausible first-party paths checked: workspace snapshots, diff inspection, developer diagnostics, runtime error detection, user review.
- Why no material first-party path remains: no distinct auditor has independent access, evaluative authority and a correction return path; developer tests are not deployed as a second operational reviewer.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future/environment sensing and option-development actor revises system-level capability from prospective feedback.
- Disturbance / variety regulated: provider changes, new toolchains, incompatible Android runtime and potential updates.
- Decisive decision or feedback right: user selects providers/toolchains; maintainers release updates; current agent reasons about its assigned coding task.
- Decision owner: adjacent human user and developer, not an in-boundary S4 owner.
- Supporting / enforcement mechanisms: runtime installers, provider profiles, capability registry and update notices.
- Closure path: manual setup/release changes the available modes but no first-party prospective strategy loop develops options and returns a new system-wide operating regime.
- Why this is / is not agent-owned: agent task planning is S1, while plugin/toolchain additions are developer or operator configuration.
- Evidence: [capability registry](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/runtime/AgentDriver.kt#L1-L86), [runtime setup](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/ui/MainViewModel.kt#L2098-L2140).
- Basis: structural.
- Confidence: medium-high.
- Caveats: maintainers may actively evolve the product; this is outside the selected runtime recursion.

### Absence scope

- Surfaces inspected: runtime installer/setup, agent registry, provider selection, update code and README architecture.
- Plausible first-party paths checked: model/provider switching, update checks, toolchain installation, task-level agent exploration.
- Why no material first-party path remains: these paths implement chosen configuration or delivery updates; none closes a first-party future-oriented intelligence decision into revised whole-system operation.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/constitutional-policy dispute and legitimate closure at this project agent recursion.
- Disturbance / variety regulated: API credentials, Android sandbox permissions, native tool approvals and user task instructions.
- Decisive decision or feedback right: user consents to concrete tool/file/session operations; application enforces stored settings and agent-specific capabilities.
- Decision owner: the user for local permissions and developer for app policy, not a shipped S5 ultimate-identity authority for the assembled cell.
- Supporting / enforcement mechanisms: Android Keystore, permission requests, driver capability flags, user settings.
- Closure path: approval modifies individual tool execution or configuration; no identity-level decision flows through a legitimate parent into renewed S3/S4 direction.
- Why this is / is not agent-owned: authorization to execute a shell command and credential handling protect local work, not the system's ultimate purpose and legitimacy.
- Evidence: [approval callback](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/ui/MainViewModel.kt#L4782-L4793), [runtime approvals](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/app/src/main/java/com/jarves/mh/runtime/ClaudeRuntimeBridge.kt#L348-L355), [documented security](https://github.com/techjarves/Mobile-Harness/blob/96b1da08d03af4f2d63970a3794c7fda068948c4/README.md#L42-L136).
- Basis: structural.
- Confidence: medium-high.
- Caveats: an enterprise's parent governance of installed devices would require a different system-in-focus.

### Absence scope

- Surfaces inspected: UI permissions, key vault, runtime tool approvals, app preferences, documentation and project lifecycle.
- Plausible first-party paths checked: user consent, developer safety notices, provider selection, login/credential policy and agent-model instructions.
- Why no material first-party path remains: they concern local task safety and user-supplied operating constraints rather than a reachable ultimate identity-policy judgment and returned legitimate policy control.

## Distributed OSS parent arrangement

The upstream project's maintainers choose releases, native integrations and supported Android operating modes. Their software-maintenance organization is adjacent to a user's installed project-agent runtime and is not silently counted as first-party S3/S4/S5 authority over the user's live tasks.

## Self-hosted and non-human modes

The app can use configured custom/local API providers, but the installed native coding-agent CLI still owns task decisions. No self-hosted model endpoint alone supplies a metasystem. Human tool approvals and project steering remain explicit supported controls.

## Recursion

The native coding agent runs inside an Android project cell. The UI holds several projects/chats and user-scheduled prompts, but a parent portfolio of independently viable S1 units and its shared S2/S3/S4/S5 decisions are not established by the one-active-agent mode.

## Variety and escalation

Provider choices, bounded context, project selection and terminal/build gates attenuate operating variety. Agent/provider errors become session failure/UI signals; the user may retry, switch, interrupt or change credentials. This is a useful exception-report and local intervention path, not by itself evidence of autonomous S3/S4/S5 or a formal algedonic channel with an ultimate-response owner.

## Evidence gaps

- No Android ARM64 runtime/device or paid/live LLM agent execution was performed. The positive S1 state is an evidence-bounded supported composition, not validated task performance.
- External native coding agent internals were not separately audited or credited as authorship of Mobile Harness.
- Operator steering and diagnostics may be substantial for usability but did not establish whole-system parent current control or independent S3* operational audit at the chosen single-project recursion.
