---
harness_id: rexmod
project_name: rexmod
repository: https://github.com/alpcanaydin/rexmod
review_ref: fd0580e6a8648f7b62b4da81cb16be6b32835d52
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# rexmod

## Review boundary

- System in focus: the installed rexmod layer around a coding agent running in a Rex pane: Go hook/CLI, turn snapshots, macOS Changes panel, Neovim reviewer and agent-specific feedback integration.
- Purpose and identity: make coding-agent changes visible per turn, let the user inspect exact source diffs and deliver line-specific corrective review back into the same active coding agent.
- Relevant environment: a user's Git worktree, Rex terminal panes, installed Claude Code/Codex/OpenCode/Pi agent, Neovim editor, Git state, comments and process/pane metadata.
- Standard-distribution boundary: macOS 15+ Apple silicon, installed and opened Rex, rexmod's patch/hook integration, built-in `rexmod` CLI/panel, and **one of** the supported external coding-agent runtimes. The coding model/tool loop belongs to that live dependency; rexmod adds its delivered feedback to that agent's next turn.
- Credited operating / distribution surfaces: [shipped loop and prerequisites](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/README.md), [hook/feedback bridge](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/main.go#L495-L676), [turn snapshots and changes](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/git.go), [pane identity and ambiguity controls](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/rex.go), [panel review/switching](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/panel/Views.swift).
- Adjacent first-party surfaces excluded from ownership: upstream Rex app internals and agent vendor/model organizations, tests and dev-only editor previews, release updater and installer checks (distribution maintenance, not an agent governance loop), Homebrew package manager and author contribution process. Rex and external agents supply execution; they are not silently credited as independent rexmod organizational policy.
- First-party operating / deployment modes considered: Claude Code and Codex `UserPromptSubmit`/`Stop` hooks, OpenCode server/TUI plugin, Pi extension, Last Turn/Uncommitted/Branch diff views, Neovim source review, automatic next-message review delivery and immediate Send, multiple agent panes in one Rex window, ambiguous same-repo Codex panes.
- Recursion level: one user's Rex window and its integrated coding agents working in Git projects; the panel follows one active target at a time while listing other local agent panes.
- Reviewed revision: `fd0580e6a8648f7b62b4da81cb16be6b32835d52`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Installer hooks one of the user's live coding agents and patches Rex with a Swift Changes panel. At `prompt`, the Go `rexmod hook` captures a working-tree snapshot with a disposable Git index, resolves agent/pane identity and supplies pending code-review notes to that agent's next prompt. At `stop`, it captures the end-of-turn snapshot. The panel shows Last Turn, Uncommitted, Branch, Files and Info; a Neovim editor supports line/range comments with code snippets. Comments store a target pane, drift detection and sent/resolved state under worktree-local Git metadata. An explicit Send action pastes comments into the correct agent pane immediately; otherwise the prompt hook attaches them next turn. There is no model inference inside the rexmod binary itself. [Architecture and supported agents](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/README.md#L17-L71); [hook routine](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/main.go#L577-L672); [comment store](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/comments.go).

## Operational model

A human sends a task to an already running coding agent. That model selects code/edit/test actions using the external host, while rexmod records a before/after Git worktree snapshot and gives the operator actual file/line changes in a parallel editor. The human can add source-based corrections to an agent-specific review queue; hooks return those comments (including stale/changed-line warnings) as fresh instruction to the model. The panel also shows other agent panes for current attention switching. The system is dependent on first-party hooks being installed/trusted and on a live coding-agent runtime; a bare `rexmod` binary without an agent is a UI/instrumentation utility, not an autonomous S1. No shipped inter-agent conflict arbiter or prospective capability-upgrade decision loop follows from this code. [Agent call and review loop](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/README.md#L20-L61); [immediate/next-prompt comment paths](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/main.go#L495-L672).

## S1 — Operations

- State: A
- Function: an integrated coding model performs user-requested repository changes and responds to source-specific review corrections in subsequent turns.
- Disturbance / variety regulated: repository bugs/requirements, live tool results, changing code and human review notes that identify wrong or incomplete edits.
- Decisive decision or feedback right: model decides how to edit/test/respond to original tasks and returned line-specific comments; rexmod only transports and displays the corrections.
- Decision owner: the live installed Claude Code/Codex/OpenCode/Pi coding agent selected in a Rex pane, not the rexmod Go CLI or Swift panel.
- Supporting / enforcement mechanisms: installed prompt/stop hooks or plugin/extension, `rexmod comments`, agent pane resolution, Git turn snapshot, editor target and prompt-bridge comment context.
- Closure path: user prompt → agent model/tool actions → changed repo and Stop snapshot → optional direct source-review comments → next prompt/explicit Send → agent model receives corrections and acts in its next turn.
- Boundary reachability: installation hooks supported live coding agents and the panel feeds those same agents; the README explicitly requires one running agent and notes Codex hook trust and OpenCode server restart. Standalone Rex or rexmod without such a host does not supply S1 inference.
- Why this is / is not agent-owned: the external model agent owns the operative code changes; first-party rexmod closes an additional feedback path into that exact agent but has no independent model loop. It is credited only for the documented integrated distribution mode, not for a bare editor.
- Evidence: [installed four-agent integration](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/README.md#L48-L95), [hook passes review to model](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/main.go#L577-L672), [OpenCode prompt insertion](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/agents/opencode-rexmod.js), [Pi extension](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/agents/pi-rexmod.ts).
- Basis: source-level integration and shipped documented mode; no macOS agent runtime executed in this assessment.
- Confidence: medium-high for integrated mode and return path.
- Caveats: model reasoning/tool abilities are provided by the external agent, and rexmod does not autonomously begin a model run. In unsupported/no-hooks mode S1 ownership cannot be attributed to rexmod alone.

## S2 — Coordination

- State: —
- Function: no shipped inter-S1 disturbance resolution/control loop among distinct coding agents, despite multi-agent pane awareness.
- Disturbance / variety regulated: simultaneous agents on overlapping worktrees can overwrite files or misreceive comments; multiple Codex panes in one repository are explicitly ambiguous.
- Decisive decision or feedback right: source code targets comments to the right pane or withholds them if ambiguous; it does not detect and resolve competing agents' edits/claims or negotiate work partitioning.
- Decision owner: not established; user selects target pane and agents remain independently responsible for their code.
- Supporting / enforcement mechanisms: `Target.Agents`, `TargetBlock`, `rememberAgent`, pane scoring, conservative ambiguity refusal, comment flock and per-worktree state.
- Closure path: a comment is delivered only to its selected agent or held for manual Send when attribution is ambiguous; that protects feedback routing, not an interaction-level cross-agent work-conflict correction.
- Why this is / is not agent-owned: multiple panes and accurate message routing are generic communication/identity support; git file diff is a single-agent review instrument, with no stock inter-agent scheduling, arbitration or rebasing loop.
- Evidence: [multiple agents and same-repo Codex limitation](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/README.md#L41-L49), [ambiguous target deliberately withheld](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/rex.go#L190-L257), [per-pane comment ownership](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/comments.go#L60-L76).
- Basis: bounded negative-state structural review.
- Confidence: high for no stock agent-work conflict reconciliation.
- Caveats: a human can tell agents to use separate worktrees, but rexmod does not supply that S2 decision as a shipped agent-function closure.

### Absence scope

- Surfaces inspected: agent-pane resolution and switching, hook delivery, Git snapshots/diffs, comment storage/locking, panel Info and installer integrations.
- Plausible first-party paths checked: cross-agent pane list, targeted notes, ambiguous Codex attribution refusal, worktree Git context and review drift detection.
- Why no material first-party path remains: none observes two S1 outputs as competing work and returns a corrective inter-agent work-allocation/settlement decision; refusal to guess a message recipient is routing safety, not S2 coordination.

## S3 — Inside-and-now control

- State: P
- Function: the installed human operator sees current work across the Rex window's agent panes and decides which one to inspect and redirect now.
- Disturbance / variety regulated: several running/blocked/idle agents, changed code needing attention, unresolved review notes, process/port state and risk of sending feedback to the wrong agent.
- Decisive decision or feedback right: select/follow a live agent pane, inspect current status/changes and choose which agent receives corrective comments immediately or on its next prompt.
- Decision owner: human using the bundled Rex panel and editor, not an autonomous supervisory model.
- Supporting / enforcement mechanisms: `resolveTarget` enumerates `Agents`, `cmdFollow` focuses selected block, Info tab displays agent status, work process and session/ports, Changes tab shows per-agent active work, pending notes and Send.
- Closure path: live pane list/status/diff → operator chooses an agent and code review priority → focus, direct Send or next-prompt comment delivery → targeted agent's ongoing task receives the new instruction and later updated turn change set.
- Boundary reachability: installed panel and Rex pane integration provide this on supported macOS installations with one or more live agents; scope is current Rex window, not all separate installations/remote sessions.
- Why this is / is not agent-owned: supervisor choice and review decisions are human; pane selection and source snapshots are deterministic mechanisms. No unsupervised global task-priority model is credited.
- Whole-system current view: the `Target.Agents` enumeration/Info view lists every agent pane in the active window, with selected agent `working`/`blocked`/`idle` status, processes/ports and per-target diff/notes.
- Current-control decision scope: selecting which current agent receives attention and feedback, changing that agent's immediate task instructions and requesting corrections, within one tab/window's integrated operation.
- Evidence: [agent list and followed target](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/rex.go#L340-L456), [focus agent](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/main.go#L119-L140), [Info status/process/ports](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/info.go#L14-L115), [panel controls](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/panel/Views.swift#L1379-L1450).
- Basis: structural, human-controlled installed mode.
- Confidence: medium; current-view and actuation path are explicit but local/single-window bounded.
- Caveats: not a machine-wide cross-workspace dashboard or independent team coordinator; the panel tracks the chosen agent's files, not a fused synthesis of all work.

## S3* — Complementary audit

- State: C
- Function: a separate human source-review path independently inspects actual Git changes made by the coding model and returns file/line findings for repair.
- Disturbance / variety regulated: an agent may claim task completion while its working tree contains wrong, missing or unsafe changes that its own response did not disclose.
- Decisive decision or feedback right: preserve a per-turn worktree comparison, expose source code and diagnostics to the human, create drift-aware review annotations and feed corrections to the responsible agent.
- Decision owner: human reviewer supplies inspection judgment; rexmod implements artifact capture, provenance/identity and correction return, not a separate autonomous auditor.
- Supporting / enforcement mechanisms: Git disposable-index start/stop snapshots, Last Turn/Uncommitted/Branch diffs, Neovim changed-line jump and LSP diagnostics, source/snippet-matched `Comment`, `checkDrift`, hook `additionalContext` and direct Send.
- Closure path: agent finishes a turn → independent Git snapshot diff and current source in editor → human identifies a defect and attaches exact code comment → rexmod validates current drift and routes it to agent prompt/terminal → producing model can revise code and later resolve the review ID.
- Boundary reachability: installed hook takes both before/after snapshots and the shipped Neovim/panel allows inspection and comment delivery; no second model is required, but a human must actually review for the audit judgment to occur.
- Why this is / is not agent-owned: the complementary artifact and returned findings are first-party integrated, but a human rather than an autonomous review model judges the discrepancy; rated `C` only for a bounded constructed review/audit path, not `A` or a parent modifier.
- Claim being audited: the coding agent's stated changes satisfy the current request, without omitted or defective edits.
- Ordinary reporting path: the model's own completion message, transcript and tool narrative within its terminal pane.
- Complementary access path: a separate Git worktree snapshot/diff, actual file content and editor diagnostics, rather than the authoring agent's own text report.
- Independence boundary: source reviewer reads code outside the model's reasoning transcript through rexmod's Git/editor integration; comments are authored by the human and stored with target and reviewed snippet.
- Who acts on findings: human decides to send/queue corrections; next model turn receives them and can edit the files, with the following snapshot showing subsequent effects.
- Evidence: [Git change capture and disposable index](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/git.go#L74-L116), [turn boundaries](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/git.go#L475-L512), [snippet/drift aware source review](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/comments.go#L183-L266), [feedback return and resolution](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/main.go#L495-L672), [review UI](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/panel/Views.swift#L1320-L1378).
- Basis: structural integrated review path conditional on human inspection.
- Confidence: medium; complementary evidence and feedback are explicit, not observed with a live macOS agent during this review.
- Caveats: no automatic independent judgment, mandatory approval gate or enforcement that each comment was fixed; a human may miss defects or skip review. It is not an autonomous `S3* A` auditor and does not claim security certification.

## S4 — Outside-and-then intelligence

- State: —
- Function: no installed proactive outside/future environmental interpretation and subsequent strategic change of the harness's capabilities.
- Disturbance / variety regulated: agent changes, new language servers, upstream Rex updates and user project demands can prompt maintenance.
- Decisive decision or feedback right: no first-party model or parent loop interprets prospective external conditions and selects adaptive operating policies for future work.
- Decision owner: not established; installer/updater and language-server provisioning are deterministic or operator-initiated.
- Supporting / enforcement mechanisms: update/repatch LaunchAgent, on-demand parser/LSP installs, model vendor extension compatibility and hook configuration.
- Closure path: updater detects upstream app release and reapplies a patch; editor installs a language server based on opened file. These are environment maintenance reactions, not prospective strategic sensing/adaptation.
- Why this is / is not agent-owned: compatibility automation changes software support, not a function-specific outside-and-then intelligence owner that anticipates future work.
- Evidence: [installation/update behavior](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/README.md#L75-L108), [language server on demand](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/README.md#L37-L47), [update process](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/scripts/update.sh).
- Basis: bounded negative-state structural review.
- Confidence: high for stock modes.
- Caveats: upstream agents may have their own planning or adaptation skills; those are not a rexmod-level S4 loop.

### Absence scope

- Surfaces inspected: release/patch watcher, hook installer, agent plugins, panel overview, LSP provisioning, bundled skill and README maintenance modes.
- Plausible first-party paths checked: tracking Rex releases, automatic re-patch, opportunistic language servers, new supported-agent hooks and future coding tasks.
- Why no material first-party path remains: the paths handle present/retrospective compatibility and current user instruction; none links an external/future distinction to a selected strategic capability change and return.

## S5 — Policy and identity

- State: —
- Function: no installed ultimate-policy/identity-level authority is shown settling and revising the agent organization's purpose with a completed feedback return.
- Disturbance / variety regulated: which agents can run, how their duties differ and who has ultimate project authority are governed by external agent host and user's machine, not rexmod policy.
- Decisive decision or feedback right: the user can install/uninstall rexmod, select a pane and comment, but no shipped charter/membership/mission policy deliberation and enforcement loop follows.
- Decision owner: not established inside the rexmod layer; external user/agent host retains the binding policy.
- Supporting / enforcement mechanisms: install/remove hooks, Rex patch, pane identity, comments and per-worktree review metadata.
- Closure path: hook install/disable and current-task review change integration but do not adjudicate ultimate organizational identity and return a revised mission/authority to all agents.
- Why this is / is not agent-owned: the model is not authorized to define its organizational purpose and rexmod's human review comments control a task, not the whole agent organization's ultimate policy.
- Evidence: [install/uninstall scope](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/README.md#L73-L108), [agent pane targeting](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/cmd/rexmod/rex.go), [bundled task-level skill](https://github.com/alpcanaydin/rexmod/blob/fd0580e6a8648f7b62b4da81cb16be6b32835d52/skills/rexmod/SKILL.md).
- Basis: bounded negative-state structural review.
- Confidence: medium-high for absence at this layer.
- Caveats: the local human/operator unquestionably controls the machine but that general fact alone does not demonstrate an S5 identity-policy loop in rexmod.

### Absence scope

- Surfaces inspected: plugin/hook installation, user comments, agent pane selection, bundled skill and update/uninstall logic.
- Plausible first-party paths checked: named agent recognition, targeted reviewer notes, user-controlled patch lifecycle and operational switches.
- Why no material first-party path remains: each is compatibility, task feedback or UI configuration without a continuing identity-level policy decision/enforcement return.

## Distributed OSS parent arrangement

The upstream repo's maintainer/releases and downstream Claude Code/Codex/OpenCode/Pi organizations are distinct. rexmod's patch is explicitly unofficial relative to Rex; neither external vendor policy nor the upstream GitHub contributor workflow is imputed to the installed harness. Human S3 refers strictly to the current Rex window; the auditor constructor requires an active human source reviewer, not a provider-owned independent model.

## Self-hosted and non-human modes

The usable distribution is macOS + Rex + a supported coding agent with trusted hooks/plugins and optionally the patched panel. `--no-hooks`/no agent removes the model feedback path and cannot inherit S1 or audited returned corrections. A user can use the direct CLI even with panel hidden; standard code review still needs a human. Same-repository Codex pane ambiguity intentionally leaves comments pending, not guessed. No running agent or installed Rex was exercised on this non-macOS analysis host.

## Recursion

Multiple active panes are distinct coding S1 systems under the same local reviewer; a switched panel follows one at a time. A note's agent-specific TargetBlock is a feedback identity, not a rule that makes all panes one jointly autonomous team. The local machine owner has current-control rights within a Rex window; vendor processes and repo maintainer governance are outside the recursion.

## Variety and escalation

Model hosts amplify coding operations; Git snapshot/diff and editor diagnostics expose otherwise hidden errors. Code-review notes carry file/line snippets, drift warnings and resolution IDs; user can send immediately or defer until next prompt. Target ambiguity attenuates wrong-agent feedback but does not coordinate competing edits. Human reviewer and external agent host determine whether a finding is corrected; no policy governance, future capability scan or global autonomous auditor is inferred.

## Evidence gaps

- Source-only assessment without a macOS/Rex/agent execution; hook registration and UI feedback are code/documentation evidence, not a claim of live observed completion.
- The S1 model belongs to a separately installed supported coding agent; a rexmod-only installation without that host cannot be scored as agent-owned S1.
- `S3* C` is contingent on a human using the source comparison and forwarding findings; no independent model reviewer, enforced defect closure or mandatory signoff is present.
- The multi-pane view is bounded by the current Rex window; inter-agent work conflict resolution and organization-wide authority are not demonstrated.
