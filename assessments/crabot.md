---
harness_id: crabot
project_name: Crabot
repository: https://github.com/J-F-Liu/crabot
review_ref: 09324dba3036f9033bb8a7dc5b88cc62959db8a2
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Crabot

## Review boundary

- System in focus: one first-party Crabot coding workspace/session organization at frozen revision `09324dba3036f9033bb8a7dc5b88cc62959db8a2`, including the active model/tool loop, task-spawned child sessions, multi-tab GUI, session persistence, tool execution, project prompt components and supported interactive/ACP surfaces.
- Purpose and identity: perform software-engineering work in a local workspace while keeping model choice, work mode, tools, project instructions, sessions and human intervention explicit in a native GUI.
- Relevant environment: user/operator prompts and approvals; target workspace/repository; files, shell/process state and build/test results; external model providers; web pages; optional MCP/custom tools; project `AGENTS.md`.
- Standard-distribution boundary: shipped Crabot Rust binary/library, GUI/session runtime, model/tool loop, built-in task/review/testing modes, context-prompt assembly, session tabs, snapshots/revert, custom/MCP tool adapters and ACP bridge are inside. External model providers, MCP servers, host OS/git and target-project code are dependencies/environment.
- Credited operating / distribution surfaces: `README.md`; `src/llm/`; `src/tools/`; `src/tools/builtin/task.rs`; `src/app/session_state.rs`; `src/app/conversation.rs`; `src/app.rs`; `src/views/center_pane.rs`; `src/views/session_tabs.rs`; `src/app/prompt.rs`; `assets/preamble/`.
- Adjacent first-party surfaces excluded from ownership: repository CI/release workflows, integration tests as development evidence, Crabot's own contributor `AGENTS.md` except as evidence of what the supported AGENTS surface represents, and any source changes after the frozen ref.
- First-party operating / deployment modes considered: ordinary GUI coding session; multiple concurrent user/task tabs; task modes `explore`, `planning`, `coding`, `review`, `testing`; nested task delegation; user stop/cancel controls; project AGENTS.md enabled/disabled per workspace; ACP exposure.
- Recursion level: one local coding workspace organization. The parent coding model and task-spawned model-backed child sessions are S1 cells when they act on project outcomes. The GUI operator is treated as a parent recursion only where the first-party current-control or standing-policy return path is explicitly closed.
- Reviewed revision: `09324dba3036f9033bb8a7dc5b88cc62959db8a2`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Crabot ships an iterative model/tool coding loop with a visible, configurable context. Model responses may contain several independent tool calls; read-like calls can execute in parallel while interactive/mutating tools are serial barriers inside one session. Completed tool results are appended to the session and returned to later model requests. Sessions persist incrementally as JSONL, and write/edit operations receive per-session pre-images for GUI revert.

The `task` tool creates a separate background session in the same workspace. The child receives a self-contained prompt and a mode-specific preamble; its final assistant message is delivered verbatim back to the originating parent tool call. Multiple `task` calls in one model response are emitted before waiting, so child sessions can execute concurrently. The parent model, however, remains blocked in the tool batch until their reports arrive and receives no first-party child list/message/stop/status tool.

Crabot exposes several shipped child roles. `coding` may mutate and self-test; `explore` is read-only; `review` is explicitly read-only and reports bugs/edge cases/performance/style/maintainability findings with exact evidence; `testing` can create/run/fix tests. These are separate sessions and may recursively delegate further tasks.

The GUI remains human-in-the-loop above all tabs. Session tabs display running/terminal state and parent provenance; the status line names background running sessions. The operator can switch to any running child and press Stop, cancelling that session. A cancelled child returns `Subtask was cancelled.` through the same task-report channel to the parent model.

Project standing instructions are an optional first-party prompt component. Crabot scans root `AGENTS.md`, defaults its workspace preference to enabled when present, persists that preference per recent workspace and includes the file content in the assembled system prompt. New sessions re-scan the workspace surface.

## Operational model

A user submits a task to a selected model/session. The model chooses coding/tool actions and receives their results back until it finishes. It may synchronously delegate one or several self-contained subtasks; those run as independent background session tabs and return terminal reports into the parent's pending tool-call batch.

While the model is waiting, the human operator can observe all running tabs, inspect a child and cancel it. This is credited only as parent current-control; Crabot does not promote generic multi-tab existence into autonomous coordination or management.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work through open-ended model/tool interaction with the selected workspace.
- Disturbance / variety regulated: heterogeneous repository contents, incomplete requirements, implementation alternatives, file/search/shell/process results, model/tool failures, tests/build output, context limits and user feedback encountered while completing coding work.
- Decisive decision or feedback right: choose what evidence to inspect, which enabled tool/action to invoke, what project change to attempt, how to react to returned evidence and when the assigned coding outcome is complete.
- Decision owner: the model-backed Crabot session actor, including task-spawned child actors for their delegated outcomes.
- Supporting / enforcement mechanisms: tool registry, work modes, provider adapters, cancellation/retries, session JSONL, snapshots/revert, process management, explicit context components and per-session tool configuration.
- Closure path: user/delegated task plus current context → model chooses action/tool → Crabot executes or rejects it → result is appended to session history → the same model receives it and chooses the next action or final response.
- Boundary reachability: ordinary Crabot GUI sessions and task-spawned children directly instantiate the first-party loop without consumer-authored orchestration code.
- Why this is / is not agent-owned: removing the model actor while retaining UI, tools and persistence removes the open-ended task-specific coding judgment.
- Evidence: [`README.md`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/README.md); [`src/llm/tool_call.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/llm/tool_call.rs); [`src/app/session_state.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/app/session_state.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference remains an external dependency; the assessment credits Crabot's first-party loop/tool composition rather than provider internals.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established for concurrently mutating Crabot child sessions at the selected recursion.
- Disturbance / variety regulated: concurrent `coding`/user sessions can share one workspace and can therefore overwrite, invalidate or observe one another's mutable file state, but Crabot does not package a task-specific interference-attenuation relation across those sessions.
- Distinct S1 units: independently running parent/task child sessions, each with its own model context and tool execution.
- Inter-S1 disturbance: structurally possible shared-workspace write/write or write/read interference when concurrent sessions touch overlapping files.
- Attenuating coordination relation: none established. Serial tool barriers apply within one session only; session snapshots support later revert; exact-match `edit` validation detects local stale/missing text but does not assign or arbitrate ownership across sibling S1s.
- Feedback into subsequent S1 behaviour: no S2-specific cross-session coordination result is returned. A child may observe ordinary filesystem/tool failure, but Crabot supplies no first-party relation that maps sibling interference into changed task scope/order/ownership.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: multiple background sessions, parent IDs, task-report routing and a generic “not alone in the codebase” prompt do not by themselves attenuate a concrete inter-S1 interference relation.
- Decisive decision or feedback right: none established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: within-session serial barriers; exact-text edit validation; per-session snapshots/revert; task parent IDs and terminal-report routing.
- Closure path: not applicable; no distinct-S1 interference → coordination decision/relation → changed subsequent S1 behavior loop is packaged in the reviewed distribution.
- Why this is / is not agent-owned: the parent model can choose self-contained task prompts, but generic delegation is not a concrete S2 interference decision and the parent has no sibling-scope arbitration surface after launch.
- Evidence: [`src/llm/tool_call.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/llm/tool_call.rs); [`src/tools/builtin/task.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/tools/builtin/task.rs); [`src/tools/builtin/edit.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/tools/builtin/edit.rs); [`src/app/snapshot.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/app/snapshot.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a parent model can manually choose non-overlapping task prompts, but the Methodology does not credit generic task decomposition without an evidenced interference-specific coordination path.

### Absence scope

- Surfaces inspected: task spawning/report routing; parallel tool batching; parent/child session metadata; write/edit execution; snapshots/revert; session tabs/status; default/coding/review/testing/explore preambles.
- Plausible first-party paths checked: automatic worktree/session isolation; cross-session file locks; sibling write ownership; parent-selected non-overlap; optimistic edit conflict as S2; task nesting/sequencing; human multi-tab oversight.
- Why no material first-party path remains: task children intentionally share the workspace, `write` overwrites directly, edit checks are intra-call file validation, and snapshots are recovery artifacts. No first-party S2-specific ownership/ordering/isolation decision closes across sibling operations.

## S3 — Inside-and-now control

- State: P
- Function: provide the human operator a whole-window view of current sessions and a first-party intervention path to terminate an active child/current commitment.
- Disturbance / variety regulated: several parent/task/user sessions may be running concurrently, including a delegated child that is stuck, wrong, expensive or no longer wanted while its parent model remains blocked waiting for its report.
- Whole-system current view: the tab bar presents all open sessions with running/terminal status and task-session parent provenance; the status line additionally identifies background running tab numbers.
- Current-control decision scope: select any current running session, inspect its live conversation/tool state and stop the stream; after cancellation the same tab remains available for later user-directed continuation.
- Decisive decision or feedback right: decide whether a currently running session commitment should continue or be cancelled.
- Decision owner: the human/operator at the parent recursion.
- Supporting / enforcement mechanisms: multi-tab GUI; running status indicators; per-tab cancellation token; Stop button; session parent/task path metadata; task-report channel.
- Closure path: operator observes current session fleet → selects a running child and presses Stop → Crabot cancels that session → terminal cancellation is delivered as an error result for the originating `task` call → the parent model later receives that returned intervention outcome and revises subsequent operation.
- Boundary reachability: multi-tab session visibility and Stop controls are standard first-party GUI behavior; task-spawned children are visible/clickable tabs rather than hidden external workers.
- Why this is / is not agent-owned: the autonomous parent model is blocked while task children are in flight and has no child list/message/stop/status tool. The current-control decision credited here is therefore parent-owned, not agent-owned.
- Evidence: [`src/views/session_tabs.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/views/session_tabs.rs); [`src/views/center_pane.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/views/center_pane.rs); [`src/app/session_state.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/app/session_state.rs); [`src/app/conversation.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/app/conversation.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the parent current-control path is intentionally narrow: it is operator supervision/cancellation, not an autonomous scheduler or rich agent-fleet manager.

## S3* — Complementary audit

- State: A
- Function: independently review implementation/code through a separate read-only model-backed session and return actionable findings to the parent coding actor.
- Disturbance / variety regulated: the implementing session may miss bugs, logic/edge-case problems, performance/style/maintainability issues or test gaps because it evaluates its own work through the same context and assumptions.
- Claim being audited: that the specified code/change is correct and acceptable beyond the implementer's own completion report.
- Ordinary reporting path: the implementing parent/coding child reports its own modifications and verification through its normal session/tool result path.
- Complementary access path: a `task` call with `mode: review` spawns a distinct session with the shipped read-only review preamble, direct read/find/search and inspect-only bash access, and explicit instructions to reference exact paths/lines and actionable issues.
- Independence boundary: the reviewer is a separate session that receives only a self-contained delegated prompt and does not inherit the parent conversation; its role prohibits file modification. Independence is context/access-path based rather than provider-family diversity.
- Who acts on findings: the parent model receives the reviewer's final message verbatim as the `task` tool result and can then edit code, delegate a corrective coding/testing task or report unresolved issues.
- Decisive decision or feedback right: make the semantic audit judgment about defects/risks from the separate reviewer context and repository evidence.
- Decision owner: the model-backed review child.
- Supporting / enforcement mechanisms: `review.md` preamble; task mode dispatch; separate background session; read-only role instructions; terminal report routing tagged by tool call ID.
- Closure path: parent selects review scope → Crabot launches separate review session → reviewer inspects actual code and returns findings → report becomes parent tool result → parent coding model reacts with correction/acceptance in subsequent operation.
- Boundary reachability: `review` is one of the shipped `TASK_MODES` and its preamble is bundled with the standard distribution; no application-authored reviewer loop is required.
- Why this is / is not agent-owned: deterministic task/report plumbing cannot judge arbitrary code quality; removing the reviewer model removes the complementary semantic audit.
- Evidence: [`assets/preamble/review.md`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/assets/preamble/review.md); [`src/tools/builtin/task.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/tools/builtin/task.rs); [`src/llm/tool_call.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/llm/tool_call.rs); [`src/app/session_state.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/app/session_state.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: review is a parent/model-chosen path rather than a mandatory gate on every mutation, and the same provider/model family may be selected for reviewer and implementer.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-then loop was established that converts external/future-relevant distinctions into persistent organizational adaptation.
- Disturbance / variety regulated: web fetch/explore, prompt skills, model/tool configuration, durable sessions, context renewal and testing/review can improve current-task execution, but no supported loop turns prospective environmental intelligence into a selected durable capability/strategy change.
- Decisive decision or feedback right: none established for S4.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: `fetch`; explore/planning task modes; configurable preambles/skills/tools/MCP; model selection; JSONL sessions; `renew` relay/context summarization; custom tools.
- Closure path: not applicable; no external/future distinction → adaptation option → persistent capability/strategy change → return into current organizational control was found.
- Why this is / is not agent-owned: `renew` preserves a long current task in a fresh session, while web/review/testing modes gather evidence for present work. User-editable skills/tool/model settings are configuration surfaces, not an autonomous adaptation loop.
- Evidence: [`README.md`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/README.md); [`src/tools/builtin/renew.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/tools/builtin/renew.rs); [`assets/preamble/explore.md`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/assets/preamble/explore.md); [`src/views/system_prompt.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/views/system_prompt.rs).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an operator can manually evolve Crabot's configuration or prompt assets, but operator configuration alone does not establish the Profile S4 intelligence/adaptation loop.

### Absence scope

- Surfaces inspected: web/explore task mode; planning/testing/review modes; renew/context handoff; session persistence; preamble/skill selection; custom tools; MCP; model configuration; workspace/project context.
- Plausible first-party paths checked: web research as prospective intelligence; renew as learning; persistent sessions as organizational memory; skills/custom tools as capability adaptation; model switching as adaptation; review/testing feedback as S4.
- Why no material first-party path remains: all identified loops either regulate a current coding task, preserve its context/evidence, or expose externally selected configuration. No shipped prospective sensing/option-selection loop persists an adaptation and returns it into later current control.

## S5 — Identity / ultimate policy

- State: P
- Function: apply the legitimate project owner's durable repository-level instructions as standing policy for Crabot agents in that workspace.
- Disturbance / variety regulated: later coding sessions can diverge from project architecture, conventions, safety/working rules or other durable owner instructions unless the project policy layer is carried into agent context.
- Identity / ultimate-policy issue: what repository-level rules and standing instructions should govern AI coding behavior in the selected project.
- Ultimate authority in each claimed mode: Parent (`P`) — the legitimate project owner/editor owns root `AGENTS.md` content and whether that project instruction component is enabled for the workspace. No first-party autonomous S5 authoring mode is established.
- Return-to-operation path: Crabot scans the workspace root for `AGENTS.md`, restores the workspace's enabled preference, stores the content in prompt state and includes it in the assembled system prompt; fresh sessions re-scan the workspace so owner policy changes govern later model operation.
- Decisive decision or feedback right: decide the durable project instruction content and whether Crabot should apply that project-policy component.
- Decision owner: the human/project owner at the parent recursion.
- Supporting / enforcement mechanisms: workspace scan; per-workspace AGENTS preference; explicit AGENTS checkbox; system-prompt composition; fresh-session refresh.
- Closure path: project-level policy/instruction issue → owner edits root `AGENTS.md` and/or enables its first-party prompt component → Crabot scans and composes it into session system context → subsequent agent work follows the returned standing project policy.
- Boundary reachability: AGENTS.md detection/toggle is a standard GUI workspace feature documented in the README, and task child system prompts are composed through the same project-context surface with their role preamble.
- Why this is / is not agent-owned: ordinary coding agents may have file-write capability, but Crabot does not package a self-policy authoring/legitimation loop; authoritative project rules remain owner-supplied and owner-toggleable.
- Evidence: [`README.md`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/README.md); [`src/app/prompt.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/app/prompt.rs); [`src/app.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/app.rs); [`src/views/system_prompt.rs`](https://github.com/J-F-Liu/crabot/blob/09324dba3036f9033bb8a7dc5b88cc62959db8a2/src/views/system_prompt.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is project-recursion S5; it does not imply human ownership of every operational approval or Crabot product-level development decision.

## Distributed OSS parent arrangement

Crabot's repository maintainers govern the Crabot software project outside a local coding workspace. The parent modes credited here are narrower: the local GUI operator owns current session intervention for S3 and the legitimate target-project owner owns project AGENTS.md policy for S5.

## Self-hosted and non-human modes

S1 and optional S3* can operate through model decisions after the task and configured authority are supplied. Concurrent delegated children can run without continuous human decisions, but Crabot does not package autonomous S2 or S3 over them. Human/operator presence is structurally meaningful through GUI current-control and project-policy selection.

## Recursion

At the selected workspace recursion, parent and task child sessions are S1 units. A review child can act as S3*. The human GUI operator sits at a parent recursion for current session intervention, and the project owner supplies ultimate project policy through AGENTS.md. Tool calls/processes are mechanisms rather than additional S1s.

## Variety and escalation

Coding variety is handled within each S1. A parent model can fan out independent subtasks and receive terminal reports, but no S2-specific shared-write coordination or autonomous live S3 loop is supplied. Running-session problems can escalate to the human operator for cancellation, and cancellation returns through the task tool. Review findings return to the parent model. Project policy returns through AGENTS.md. No S4 adaptation loop is established.

## Evidence gaps

No reviewed evidence gap requires `?`. S2 and S4 negatives are supported by dedicated absence reviews; S3 is intentionally limited to the human GUI intervention path rather than inferred from delegation itself.

## Assessment summary

Crabot closes autonomous coding S1 and autonomous complementary S3* through its shipped read-only review sub-agent mode. Concurrent task sessions share the workspace without a material first-party S2 coordination relation, and the parent model blocks while children run rather than managing them live. The standard GUI does close a parent S3 path because the operator sees running session tabs, can cancel an active child and that cancellation returns into the parent's task result. Current-task research/context/configuration do not establish S4. Project-level S5 remains parent-owned through the AGENTS.md instruction component returned into later session prompts.

Proposed vector: **`A · — · P · A · — · P`**.
