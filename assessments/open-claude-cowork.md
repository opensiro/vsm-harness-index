---
harness_id: open-claude-cowork
project_name: Open Claude Cowork
repository: https://github.com/DevAgentForge/Open-Claude-Cowork
review_ref: 7a9f99f32431115008c95ccce9da5bfbda5115f3
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Open Claude Cowork

## Review boundary

- System in focus: the first-party Open Claude Cowork desktop application at frozen revision `7a9f99f32431115008c95ccce9da5bfbda5115f3`, including Electron IPC, session persistence, streamed-event UI, permission prompts, API/model configuration and its Claude Agent SDK runner.
- Purpose and identity: provide a persistent visual desktop client for Claude Code/Claude Agent SDK sessions, with task/session management and inspection of tool activity.
- Relevant environment: user prompts, local working directories/files, Claude Code executable, Anthropic-compatible provider/model configuration, tool permission requests and persisted session history.
- Standard-distribution boundary: Open Claude Cowork Electron/UI/session/configuration code is inside. The model-backed open-ended agent loop implemented by `@anthropic-ai/claude-agent-sdk` / Claude Code is an external runtime dependency and does not donate autonomous ownership to the desktop client.
- Credited operating / distribution surfaces: README.md; package.json; `src/electron/libs/runner.ts`; `src/electron/ipc-handlers.ts`; `src/electron/libs/session-store.ts`; `src/electron/libs/util.ts`; UI permission/event surfaces.
- Adjacent first-party surfaces excluded from ownership: repository-development tooling/tests/assets and any cognition/tool-selection logic contained inside the Anthropic SDK/Claude Code runtime rather than this repository's own code.
- First-party operating / deployment modes considered: new/resumed Claude sessions, persistent local session history, user-question permission handling, alternate API/provider configuration and packaged/development Claude Code executable resolution.
- Recursion level: one Open Claude Cowork-managed desktop collaboration/session shell around a Claude Code agent runtime.
- Reviewed revision: `7a9f99f32431115008c95ccce9da5bfbda5115f3`.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The frozen README positions Open Claude Cowork as a desktop collaboration partner that makes Claude Code sessions visual and persistent. The implementation confirms a client/runtime boundary rather than a first-party semantic agent loop.

`src/electron/libs/runner.ts` imports `query` from `@anthropic-ai/claude-agent-sdk` and passes the user prompt, working directory, resume id, environment, the resolved Claude Code executable path and permission callback directly into that SDK query. Open Claude Cowork then iterates SDK messages, persists the Claude session id, forwards messages to the UI and updates session status. Its own permission callback special-cases `AskUserQuestion` for a human response and automatically allows other requested tools; it does not select the task-specific tools or decide the next semantic action.

`ipc-handlers.ts` owns session start/continue/stop/delete and permission-response routing. `session-store.ts` persists session/message metadata. `util.ts` also uses the Claude Agent SDK for title generation. None of these first-party surfaces replaces the Claude runtime's objective→action→observation loop.

Counterfactual owner test: remove the Claude Agent SDK/Claude Code runtime while leaving the Electron app, session DB, IPC, permission panel and provider configuration. The application can store and display sessions but cannot interpret an open-ended task, choose semantic file/tool actions from observations and continue until completion. First-party S1 therefore does not close.

Primary evidence:

- [README.md](https://github.com/DevAgentForge/Open-Claude-Cowork/blob/7a9f99f32431115008c95ccce9da5bfbda5115f3/README.md)
- [package.json](https://github.com/DevAgentForge/Open-Claude-Cowork/blob/7a9f99f32431115008c95ccce9da5bfbda5115f3/package.json)
- [runner.ts](https://github.com/DevAgentForge/Open-Claude-Cowork/blob/7a9f99f32431115008c95ccce9da5bfbda5115f3/src/electron/libs/runner.ts)
- [ipc-handlers.ts](https://github.com/DevAgentForge/Open-Claude-Cowork/blob/7a9f99f32431115008c95ccce9da5bfbda5115f3/src/electron/ipc-handlers.ts)
- [session-store.ts](https://github.com/DevAgentForge/Open-Claude-Cowork/blob/7a9f99f32431115008c95ccce9da5bfbda5115f3/src/electron/libs/session-store.ts)
- [util.ts](https://github.com/DevAgentForge/Open-Claude-Cowork/blob/7a9f99f32431115008c95ccce9da5bfbda5115f3/src/electron/libs/util.ts)

## Operational model

A user starts or resumes a session. Open Claude Cowork creates/loads local session state and calls Claude Agent SDK `query(...)` with the prompt and Claude Code executable. Claude Code/SDK performs the model/tool loop and yields SDK messages. Open Claude Cowork records and renders those messages, surfaces `AskUserQuestion` to the user, relays the answer, and provides abort/session controls.

## S1 — Operations

- State: —
- Function: no first-party Open Claude Cowork-owned autonomous open-ended operational loop is established.
- Disturbance / variety regulated: first-party code regulates session persistence, runtime configuration, message streaming and permission/user-question transport; semantic task variety is absorbed by Claude Code.
- Decisive decision or feedback right: interpret the open-ended objective, choose task-specific file/tool actions, evaluate tool observations and decide the next semantic action or completion.
- Decision owner: Claude Agent SDK / Claude Code runtime.
- Supporting / enforcement mechanisms: Electron IPC, session DB, SDK query invocation, environment/provider configuration, abort control, UI event streaming and permission callback.
- Closure path: user task → Open Claude Cowork SDK call → Claude Code model/tool loop → tool/file observation → Claude Code next decision/completion → SDK messages → Open Claude Cowork persistence/UI.
- Why this is / is not agent-owned: the first-party client transports the prompt, tools' permission responses and resulting events, but does not own the task-semantic action selection.
- Evidence: README.md; package.json; `src/electron/libs/runner.ts`; `src/electron/ipc-handlers.ts`.
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: packaging the SDK and resolving its Claude Code executable makes the runtime readily reachable, but dependency bundling does not transfer decision ownership.

### Absence scope

- Surfaces inspected: README/build dependencies, SDK runner, IPC/session lifecycle, persistent session store, provider/Claude executable configuration, permission UI and title-generation utility.
- Plausible first-party paths checked: `runClaude`; session start/resume; permission callback; persisted conversation state; provider/model configuration.
- Why no material first-party path remains: all ordinary open-ended task reasoning and tool selection enter through Claude Agent SDK `query`; first-party code only configures, transports, records and controls that external runtime.

## S2 — Coordination

- State: —
- Function: multiple persistent sessions can coexist, but no first-party inter-S1 interference attenuation loop is established.
- Disturbance / variety regulated: sessions have separate ids/history/cwd and can be individually started, resumed, stopped or deleted.
- Decisive decision or feedback right: identify an interference/conflict among distinct operational S1 units and choose a coordination response that alters their subsequent behaviour.
- Decision owner: not established in first-party Open Claude Cowork code.
- Supporting / enforcement mechanisms: per-session records, runner-handle map, independent abort controls and UI session list.
- Closure path: no interference-specific coordination judgment → changed S1 behaviour path is established.
- Why this is / is not agent-owned: session plurality/isolation and lifecycle routing do not by themselves establish S2.
- Evidence: `src/electron/ipc-handlers.ts`; `src/electron/libs/session-store.ts`.
- Basis: structural absence review.
- Confidence: high.
- Caveats: Claude Code may internally use subagents or other coordination features, but those belong to the external runtime.

### Absence scope

- Surfaces inspected: session store, IPC handlers, runner handles, UI/session management and SDK stream routing.
- Plausible first-party paths checked: concurrent sessions; shared message/event bus; stop/delete controls; per-session permission maps.
- Why no material first-party path remains: no specific first-party relation senses and attenuates inter-agent interference among distinct Open Claude Cowork-owned S1 units.

## S3 — Inside-and-now control

- State: —
- Function: session status/lifecycle and abort controls exist without a first-party autonomous whole-system current-control judgment.
- Disturbance / variety regulated: running/idle/error/completed states, session existence, pending user questions and process abortion.
- Decisive decision or feedback right: discretionary allocation/prioritization/intervention over a whole current operational population.
- Decision owner: user for stop/delete/question answers; Claude runtime for task-level choices; deterministic Open Claude Cowork code enforces lifecycle commands.
- Supporting / enforcement mechanisms: status persistence, runner-handle map, abort controller, IPC commands and session history.
- Closure path: user/runtime event → deterministic session mutation or abort → later runtime/session state.
- Why this is / is not agent-owned: lifecycle controls and current-status views are support/enforcement surfaces, not autonomous S3 discretion.
- Evidence: `src/electron/ipc-handlers.ts`; `src/electron/libs/session-store.ts`.
- Basis: structural absence review.
- Confidence: high.
- Caveats: the ability to stop a session is not by itself a parent-governed S3 mode because no whole-system current-control function is established.

### Absence scope

- Surfaces inspected: session status, start/continue/stop/delete, runner handles, persistence and permission responses.
- Plausible first-party paths checked: desktop as supervisor; session list/status; abort path; resume path.
- Why no material first-party path remains: no first-party actor constructs a whole-system current picture and makes allocation/prioritization/commitment decisions across operations.

## S3* — Complementary audit

- State: —
- Function: streamed tool activity and messages are visible, but no independent first-party semantic reviewer/auditor is packaged.
- Disturbance / variety regulated: users can inspect Claude messages/tool activity and answer explicit questions.
- Decisive decision or feedback right: independently judge an operational claim/result from complementary access and return corrective findings into subsequent operation.
- Decision owner: user if they choose to review; no autonomous first-party Open Claude Cowork auditor.
- Supporting / enforcement mechanisms: event rendering, persisted messages, permission/question panel and session history.
- Closure path: Claude runtime event → UI visibility → optional human follow-up.
- Why this is / is not agent-owned: observation/presentation of another agent's activity is not independent semantic audit ownership.
- Evidence: README.md; `src/electron/ipc-handlers.ts`; UI SDK-message/permission surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: Claude's own self-checks remain inside the same external operational runtime and are not imported.

### Absence scope

- Surfaces inspected: streamed event UI, message history, permission panel, SDK event forwarding and session persistence.
- Plausible first-party paths checked: tool-output inspection; user approval/questions; persisted transcript; session review.
- Why no material first-party path remains: no separately instantiated first-party reviewer with complementary evidence access and corrective-return authority is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: persistent sessions and configurable provider/model/runtime settings do not establish a prospective adaptation loop.
- Disturbance / variety regulated: provider/model/API settings and session continuation can change how later Claude runs execute.
- Decisive decision or feedback right: interpret external/future-relevant evidence, develop adaptation options and select a durable capability/organizational change.
- Decision owner: user/operator for configuration; Claude runtime for task reasoning.
- Supporting / enforcement mechanisms: provider/API configuration, model selection, environment construction, persisted sessions and Claude settings reuse.
- Closure path: externally selected configuration → later SDK invocation uses it.
- Why this is / is not agent-owned: configuration persistence does not supply first-party prospective adaptation judgment.
- Evidence: README.md; package.json; runner/configuration surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: session history supports continuity, not by itself outside-and-then adaptation.

### Absence scope

- Surfaces inspected: API/provider/model configuration, `~/.claude/settings.json` reuse, session persistence and runner environment setup.
- Plausible first-party paths checked: model switching; persisted session memory; runtime configuration; future-session reuse.
- Why no material first-party path remains: durable changes are operator-selected and no first-party actor senses external/future change and selects capability adaptation.

## S5 — Policy and identity

- State: —
- Function: permission handling and runtime/provider configuration constrain execution without autonomous identity/ultimate-policy resolution.
- Disturbance / variety regulated: tool permission prompts, runtime configuration and provider credentials.
- Decisive decision or feedback right: resolve organization-level identity/ultimate-policy tensions and return the authoritative decision into operation.
- Decision owner: user/operator or externally configured Claude policy.
- Supporting / enforcement mechanisms: `canUseTool`, AskUserQuestion relay, configuration files and API/provider credentials.
- Closure path: externally established policy/user answer → Open Claude Cowork callback/configuration → Claude runtime operation.
- Why this is / is not agent-owned: first-party code enforces/transports policy but does not autonomously resolve ultimate policy.
- Evidence: `src/electron/libs/runner.ts`; README.md.
- Basis: structural absence review.
- Confidence: high.
- Caveats: the runner auto-allows ordinary SDK-requested tools, but that is a fixed enforcement choice rather than an autonomous S5 decision loop.

### Absence scope

- Surfaces inspected: permission callback, AskUserQuestion response path, provider/API configuration, session controls and README-described settings reuse.
- Plausible first-party paths checked: tool permissions; user-question policy; runtime configuration; desktop collaboration identity.
- Why no material first-party path remains: no first-party identity/ultimate-policy matter is autonomously adjudicated and returned into operation.

## Recursion

Open Claude Cowork is assessed as a desktop session/control shell around one or more Claude Code sessions. Claude Code's internal organizational functions remain external to this repository-relative assessment.

## Variety and escalation

Open Claude Cowork attenuates integration and interaction variety through persistent sessions, message history, provider/runtime configuration, streamed UI and human-question handling. Open-ended semantic task variety escalates into Claude Code; explicit user questions escalate back to the person through the desktop UI.

## Evidence gaps

- Frozen revision only.
- Anthropic SDK/Claude Code internals are not imported into the repository-relative first-party boundary.
- Hosted/provider behavior not represented in this repository is not credited.

## Assessment summary

At the frozen revision, Open Claude Cowork is a first-party desktop client and session shell around the Claude Agent SDK/Claude Code runtime. Its code owns persistence, configuration, event presentation and user-question transport, while the external Claude runtime owns the open-ended semantic model/tool loop. First-party S1 therefore does not close. Proposed terminal disposition: excluded-no-agentic-vsm.

**Vector:** — · — · — · — · — · —
