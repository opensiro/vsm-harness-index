---
harness_id: inhuman
project_name: inhuman
repository: https://github.com/here-build/inhuman-harness
review_ref: 01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# inhuman

## Review boundary

- System in focus: the installable `inhuman` local agent workspace, its background kernel/project/session daemons, and bundled browser/terminal clients, not the public source repository's contributor organization.
- Purpose and identity: run persistent model-directed tool sessions for one machine's operator, optionally with named worker bots and scheduled/reactive Scheme jobs.
- Relevant environment: local user projects, files and commands, model connections, installed tools/plugins, project sessions, permission approvals and optional experimental remote relay.
- Standard-distribution boundary: the shipped `packages/inhuman` CLI, `packages/harness` daemon and agent runtime, first-party bundled web/TUI, built-in named-agent and Scheme tools. Optional plugin installations are not presumed active.
- Credited operating / distribution surfaces: [installation and daemon lifecycle](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/usage.md), [session orchestrator](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/session/SessionOrchestrator.ts), [agent-call host](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/session/agent-runtime.ts), [all-project session rail](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness-web-app/src/shell/rail-sessions.tsx), [live bot overlays](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/project/ProjectDaemon.ts).
- Adjacent first-party surfaces excluded from ownership: source tests/stories, uninstalled plugin packages, proposed remote-access architecture, contributor CI, external model providers, WorkOS relay and upstream GitHub governance. Test fixtures corroborate but do not enact operating control.
- First-party operating / deployment modes considered: `npx inhuman` terminal, `npx inhuman web` background daemon/browser, manual/auto/yolo permission modes, installed global/project bot recipes and `bot/send`/`agent/call`, `scheme_repl`/`scheme_watch`, experimental remote client.
- Recursion level: one operator's installed local kernel spanning registered projects and distinct agent sessions; disposable worker calls are subordinate S1 activity.
- Reviewed revision: `01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI attaches to a machine-local daemon rather than owning session execution. A kernel maintains configuration, model connections and project/session summary documents. Project daemons own tools, sessions and project bot overlays. Session orchestration enters model turns, admits tool calls and handles permission waits; agent calls can dispatch to named or disposable child worker sessions, with callback/settlement recorded in session documents. The web app displays an all-project inventory as well as project-specific sessions, while the TUI attaches to the same daemon. Scheme REPL/watch adds programmable tool sequences and periodic/reactive activity, but installation of a capability is not proof that its operator is an independent VSM function. [Usage](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/usage.md); [kernel worker dispatch](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/kernel/KernelDaemon.ts#L1499-L1515); [Scheme tools](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/scheme-repl/README.md).

## Operational model

Each agent session receives user/model messages, selects tools and can be paused for authorization; a requested child may continue as a separate session and report back. The daemon persists session state independently of the UI, which makes current multi-session oversight possible. Distinct worker processes can have overlapping project scope, but message routing, named-agent callbacks, permissions, a generic job queue and the author's prompt suggestions to divide file ownership do not demonstrate a shipped S2 decision loop that detects and resolves interference between those workers. The operator can inspect running/blocked sessions, intervene in current work and edit authoritative bot recipes/policies that are reloaded into ongoing sessions. [Usage and permission modes](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/usage.md); [session orchestration](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/session/SessionOrchestrator.ts#L476-L570); [project bot watcher](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/project/ProjectDaemon.ts#L235-L265).

## S1 — Operations

- State: A
- Function: model-directed sessions perform requested development/information operations by choosing tools and reacting to results.
- Disturbance / variety regulated: varied requests, project files, model/tool failures, environmental outputs, concurrent worker observations and permission holds.
- Decisive decision or feedback right: select action/tool arguments, inspect tool outcomes, continue a model turn, ask a named worker or terminate with an answer.
- Decision owner: the configured LLM-backed session/worker, bounded by operator-selected tools, permissions and model connections.
- Supporting / enforcement mechanisms: `SessionOrchestrator` model-turn resolver, per-project `toolCalls.admit`, persisted sessions, agent-call worker/callback lifetime, TUI/web client and permission desk.
- Closure path: request → model turn → admitted tool/agent call → execution result or worker callback → resumed model decision and response.
- Boundary reachability: standard CLI/web start uses the kernel and project/session daemons; a model connection and selected model are required for inference; worker dispatch is shipped with the built-in named-agent tooling.
- Why this is / is not agent-owned: the model chooses work and next-step responses; the daemon, tool executor and permission rules enforce rather than determine those choices.
- Evidence: [installation and first turn](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/usage.md#L1-L44), [model turn and tool admission](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/session/SessionOrchestrator.ts#L476-L570), [worker session calls](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/session/agent-runtime.ts#L359-L460).
- Basis: first-party code and documented installed path; no live model inference was run by this assessment.
- Confidence: high for reachable model/tool ownership.
- Caveats: `yolo` is a permission mode, not independent authority; plugins and remote mode are optional.

## S2 — Coordination

- State: —
- Function: a function-specific inter-S1 disturbance attenuation and return loop is not established at the installed multi-session boundary.
- Disturbance / variety regulated: concurrent sessions and named/disposable child agents can touch the same project files, contend for tools and produce incompatible changes.
- Decisive decision or feedback right: no observed shipped owner that detects cross-agent file/goal conflicts, allocates shared work according to them and returns enforceable corrections to both affected S1 cells.
- Decision owner: not established; the caller/model or human may choose who to message and which work to merge.
- Supporting / enforcement mechanisms: named bot catalog, `agent/call`/`agent/ask`/`bot/send`, callbacks, worker tool grants and generic per-session admission.
- Closure path: worker replies return to the caller, and permissions can block tools; these are delegation/authorization closures rather than a demonstrated inter-S1 coordination correction.
- Why this is / is not agent-owned: distinct agents and messages exist, but the observed behavior is dispatch/response without explicit mutual-disturbance regulation; workspace isolation is not implied by a suggested division of file scope.
- Evidence: [agent call worker host](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/session/agent-runtime.ts#L70-L148), [named worker dispatch](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/kernel/KernelDaemon.ts#L1499-L1515), [Scheme agent-call surface](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/scheme-repl/README.md).
- Basis: bounded negative-state structural review.
- Confidence: medium; no complete conflict-attenuation relation was found in the reviewed stock modes.
- Caveats: a human could author a custom coordination bot or watcher; that possibility is not an implemented first-party inter-S1 loop.

### Absence scope

- Surfaces inspected: named-agent dispatch and callback lifecycle, project/session daemons, Scheme REPL/watch, runtime permissions and bundled multi-session UI.
- Plausible first-party paths checked: independent worker replies, `bot/send` message handling, shared project sessions, scheduled watchers, tool admission and human-authored agent instructions suggesting non-overlapping file scopes.
- Why no material first-party path remains: the shipped evidence closes individual calls or exposes multiple sessions; none demonstrates recognition of inter-S1 interference followed by a function-specific decision and feedback across affected workers.

## S3 — Inside-and-now control

- State: P
- Function: an installed operator oversees current work across their projects and can alter active session execution or authorizations.
- Disturbance / variety regulated: simultaneous running/idle/waiting sessions, approval bottlenecks, stalled activity and task attention priority.
- Decisive decision or feedback right: choose which active session needs attention, enter it to continue/steer or stop work, and approve or reject tool execution.
- Decision owner: the machine's human operator through the bundled web/TUI, not a global autonomous supervisor model.
- Supporting / enforcement mechanisms: kernel/project session summaries, all-project rail with attention-aware ordering and search, shared session attach, explicit daemon stop, permission desk and saved per-session states.
- Closure path: all-project live inventory/attention light → operator selects a session and sends/approves/cancels/stops → its ongoing model/tool execution or permission state changes; updated kernel summary is displayed.
- Boundary reachability: `npx inhuman web` launches the shipped local browser front end against the daemon; terminal client can attach to a specific session; a running machine and valid local access are required.
- Why this is / is not agent-owned: human current-control rights are visible and exercised via the installed clients; prioritization in the UI and default policies are not counted as agent-owned S3.
- Whole-system current view: `OverviewSessions` traverses registered projects, joins their session summaries and sorts by `waiting-for-you`/`running` attention lights, presenting an overview of the local kernel's sessions.
- Current-control decision scope: session selection, work continuation/steering, permission approval and daemon/session interruption within this one local installation, not control of upstream providers or other installations.
- Evidence: [all-project attention inventory](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness-web-app/src/shell/rail-sessions.tsx#L59-L146), [client attachment and daemon stop](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/usage.md#L45-L88), [operator approval modes](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/usage.md#L90-L104).
- Basis: structural parent-owned installed mode.
- Confidence: medium-high for human current control; no autonomous agent-wide control asserted.
- Caveats: the inventory is attached-project scoped; remote client is experimental and no stronger role isolation is inferred.

## S3* — Complementary audit

- State: —
- Function: no separate installed inspection owner independently challenges an S1 completion claim through complementary evidence and closes corrective findings.
- Disturbance / variety regulated: tool/model mistakes and untrue completion claims would require an independent check beyond the authoring agent's own results.
- Decisive decision or feedback right: no shipped distinct auditor/gate with enforced findings was identified.
- Decision owner: not established; the user can review output and may install a custom reviewer bot.
- Supporting / enforcement mechanisms: tool-result traces, saved transcripts, permission desk, callable named agents, Scheme watchers and UI file review.
- Closure path: these surfaces can show or relay observations, but a first-party independent claim → complementary inspection → correction/hold loop is not established.
- Why this is / is not agent-owned: a caller asking another agent to review, or viewing a trace, does not automatically constitute a separate, independently enforced audit function.
- Evidence: [generic named agent host](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/session/agent-runtime.ts), [Scheme watchers](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/scheme-repl/README.md), [permissions](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/usage.md#L90-L104).
- Basis: bounded negative-state structural review.
- Confidence: medium.
- Caveats: optional user-authored review bot or external CI may add review outside the credited stock mode.

### Absence scope

- Surfaces inspected: bundled named-agent catalog, session tool approval, watch scheduling, stored tool/session evidence and web UI.
- Plausible first-party paths checked: reviewer-named worker invocations, self/notify watches, manual tool approval and UI inspection; none guarantees independent direct evidence for completion claims.
- Why no material first-party path remains: the paths inspected provide ordinary process visibility, generic additional workers or permission authorization; none ships an independent audit-feedback owner at this recursion.

## S4 — Outside-and-then intelligence

- State: —
- Function: no installed function-specific loop prospectively interprets a future external change and changes the system's long-term capabilities.
- Disturbance / variety regulated: future provider, repository and workflow requirements could demand changed tools, policy or mode.
- Decisive decision or feedback right: no shipped external-prospective assessment and capability-adaptation decision with a returned deployment is established.
- Decision owner: not established; users and maintainers can separately update tools, models and plugins.
- Supporting / enforcement mechanisms: periodic/reactive Scheme watcher, configurable model/plugin catalog, persistent memory and bot recipe updates.
- Closure path: scheduled watches may launch present operations and notify an agent; user-installed/configured plugins can change capabilities, but the source does not join these into a prospective adaptation decision/return loop.
- Why this is / is not agent-owned: event reaction and retrospective state are not evidence of future-environment intelligence; operator authoring is an external parent change.
- Evidence: [watcher and run limits](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/scheme-repl/README.md), [installable plugins and connections](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/docs/usage.md#L110-L135), [bot overlay loading](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/bots/merge.ts).
- Basis: bounded negative-state structural review.
- Confidence: medium-high at standard-installation boundary.
- Caveats: a particular user's own monitoring/upgrade policy may supply S4 outside this shipped harness; not presumed here.

### Absence scope

- Surfaces inspected: Scheme reactivity/watch, model selection, plugin installs, bot recipe reload and released client documentation.
- Plausible first-party paths checked: scheduled external probes, reactive agents, persistent sessions and live tool/bot changes.
- Why no material first-party path remains: triggering current tasks and making operator-directed edits do not establish an owned external/future distinction, chosen prospective adaptation and return to deployed capacity.

## S5 — Policy and identity

- State: P
- Function: an installed user's authoritative bot identity, operational mission and permission boundaries are defined and revised by the human operator.
- Disturbance / variety regulated: which named agents legitimately exist, which instructions/tools they carry, and what permission mode may apply to each bot as local work changes.
- Decisive decision or feedback right: create/replace/remove global or project bot recipes and pin or change permission modes; a bot definition cannot itself set its own authorization mode.
- Decision owner: the local operator who controls configuration and bot recipe files, subject to ordinary filesystem trust; no autonomous ultimate-policy model is credited.
- Supporting / enforcement mechanisms: `~/.inhuman/bots/*.md`, project bot overlay watcher, recipe validation/catalog replacement/change notice, kernel config `authorization.botModes`, permission enforcement.
- Closure path: operator writes an authoritative bot recipe or permission pin → kernel/project watcher reloads and validates recipes or config → updated bot catalog and active-session notices/permission checks govern later agent invocations.
- Boundary reachability: global and project bot watches are installed in `KernelDaemon`/`ProjectDaemon`, not merely exposed as an extension API; the per-bot permission pin is explicitly reserved to the user.
- Why this is / is not agent-owned: ultimate identity and allowed authority are outside the agent's remit; model-chosen tools run within that operator-selected framework.
- Identity / ultimate-policy issue: the continuing identity, charter/tool delegation and privilege ceiling for a named worker, as opposed to a one-off user prompt.
- Ultimate authority in each claimed mode: local filesystem/configuration owner in the global/project bot modes; the same operator holds permission decisions in manual/auto/yolo modes, with different routine enforcement.
- Return-to-operation path: bot file/config change → watcher/parse/recipe replacement and mode selection → subsequent worker session creation and tool authorization use new authoritative instructions and permissions.
- Evidence: [operator-only permission pin](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/bots/bot-mode.ts#L1-L16), [recipe overlay and admission](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/bots/merge.ts), [kernel global hot reload](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/kernel/KernelDaemon.ts#L797-L834), [project hot reload](https://github.com/here-build/inhuman-harness/blob/01a9ceafbb17eb98ef16c0ea863d97cdf2b58f67/packages/harness/src/server/daemon/project/ProjectDaemon.ts#L235-L265).
- Basis: structural installed parent-owned governance loop.
- Confidence: medium-high for the locally enforceable return path.
- Caveats: local file owners with machine access can also alter the system, and remote access presently has no role/method restriction; a single approved tool call alone would not justify this S5 rating.

## Distributed OSS parent arrangement

The upstream repository's maintainers, tests and release process are not credited as governing a deployed machine. Independent installations and plugin developers do not share one accountable S5. S3 and S5 here are explicitly **P**, exercised by the local human who holds the workspace and its authoritative bot/policy files.

## Self-hosted and non-human modes

The supported stock path is local self-hosting on the user's machine. The background daemon can persist without either client but depends on the running host; `auto` employs a judge model for individual tool permissions, not automatic ultimate-policy transfer. `yolo` reduces routine approvals but retains hard blocks. Remote access is experimental and its documented absence of roles/method allowlists prevents treating it as stronger organizational governance. No default autonomous S2/S3*/S4 owner is credited from optional custom watchers, bots or plugins.

## Recursion

Individual sessions, named bot workers and disposable call children are subordinate S1 cells of one local kernel. Separate registered projects are distinct work contexts under the same local operator; a project session or worker does not automatically inherit an organizational S3–S5 loop. Other users' kernels and external providers are separate organizations outside the reviewed system.

## Variety and escalation

Model/tool calls amplify the operational repertoire; per-tool permission modes and worker grant ceilings attenuate risk. Agent calls return a result to their caller; that is not by itself coordination of competing S1 cells. Pending approvals and session status surface through the all-project view, allowing human current intervention. Human-authored bot and authorization changes alter later operative bounds. Prospective scan and independent completion-audit closures remain unproven.

## Evidence gaps

- Source-level assessment only: no provider credentials or live remote relay were exercised, no independent multiagent conflict experiment was run.
- No supplied evidence that the shipped named-agent workflows implement conflict arbitration beyond routing, messaging, callbacks and operator-authored instructions.
- No stock separate reviewer with independent direct claim evidence and correction authority was found; plugins and user-authored processes could change a deployment-specific assessment.
- Parent S3 and S5 depend on the local operator remaining a legitimate, secure authority; the repository expressly warns that remote access has no roles/method allowlist.
