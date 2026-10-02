---
harness_id: litecode
project_name: LiteCode
repository: https://github.com/itissika/litecode
review_ref: 146a9feff9edee2204138f18473b9bef83c41c5a
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# LiteCode

## Review boundary

- System in focus: one first-party LiteCode-managed coding project/session organization at frozen revision `146a9feff9edee2204138f18473b9bef83c41c5a`, including the selected primary agent, its separately executing child sessions, shared workspace, session/task state, subagent orchestration tools, workspace contract, permissions, context pipeline and supported desktop/browser/headless execution.
- Purpose and identity: perform software-engineering work on a local workspace while allowing a primary coding or orchestrator agent to inspect, edit, run tools, delegate bounded work, manage a subagent team and return completed outcomes to the user.
- Relevant environment: user/operator requests and approvals; target workspace/repository and git state; files, processes, LSP/search engines and test/build results; model/provider responses; optional MCP/custom tools; durable project `CLAUDE.md` contract.
- Standard-distribution boundary: shipped LiteCode Rust core, primary/subagent definitions, runtime/tool/context/session/permission layers, built-in orchestrator/general/explore prompt packs, subagent tool series, process-wide structured-write exclusion, web/desktop control surfaces and workspace contract handling are inside. External model providers, MCP servers, host OS/git, target-project code and third-party commands are dependencies/environment.
- Credited operating / distribution surfaces: `README.md`; `src/agent/`; `src/runtime/`; `src/tool/`; `src/tools/subagent/`; `src/session/`; `src/config/global_db/builtin_prompts.rs`; `src/config/global_db/seed.rs`; `src/context_pipeline/`; `src/knowledge/`; `src/permission/`; `web/src/components/SubagentRosterPanel.tsx`; `web/src/dockview/panels/SubagentReadOnlyPanel.tsx`.
- Adjacent first-party surfaces excluded from ownership: repository CI and release packaging, test fixtures and e2e suites as development evidence, contributor instructions for LiteCode's own repository, and later upstream changes after the frozen review ref.
- First-party operating / deployment modes considered: ordinary primary `default`; shipped primary `orchestrator`; `general` and `explore` child sessions; concurrent background subagents; desktop/browser/server/headless execution; project `CLAUDE.md` contract loading; knowledge/session-search/context-compression paths.
- Recursion level: one project/session organization. The primary model-backed agent and independently running child sessions are S1 cells when they produce repository-facing outcomes. In orchestrator mode, the primary agent also occupies S2/S3 over those children; fresh non-authoring children can occupy S3* when assigned verification.
- Reviewed revision: `146a9feff9edee2204138f18473b9bef83c41c5a`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

LiteCode ships a first-party model/tool loop over durable session rows. Each step builds the current model view, invokes the selected provider, persists the returned items, executes completed tool calls, persists tool results and loops until completion, cancellation or budget termination. Tool results therefore return directly into subsequent model decisions rather than being an external application concern.

The standard seed includes two primary profiles: `default` and `orchestrator`. The orchestrator is explicitly described as managing a team of subagents and owning the user's goal; it can launch the shipped `general` mutation-capable implementer and `explore` read-only investigator. Child sessions are full durable LiteCode sessions with independent turn/context state, may run concurrently, cannot recursively launch their own teams, and remain controllable through parent-only `subagent_list`, `subagent_send`, `subagent_stop` and `subagent_wait` tools.

Two coordination layers matter. First, the orchestrator prompt assigns file/write scopes and requires one writer per file region at a time, so task-specific interference is regulated by an autonomous manager before and during work. Second, structured `write`/`edit` calls use a process-wide file lock across sessions: a conflicting call returns `resource busy: held by session ...` to the blocked S1, supplying deterministic enforcement/feedback without replacing the orchestrator's organizational discretion.

The orchestrator prompt also separates implementation from verification: it states that verification must be performed by someone who did not write the code, and unrelated/verification work should use a new hire/new session. Child completion is routed back to the parent at a safe injection point from the same durable session source of truth.

Project standing authority is separate from the team manager. LiteCode initializes a root `CLAUDE.md` as the workspace contract; every new turn re-reads that file from disk, and the non-hidden system prompt splices its contents as project context. The built-in primary prompt explicitly treats durable `CLAUDE.md` instructions as a source of advance authorization. The project owner therefore retains ultimate authority over that contract.

## Operational model

A user selects a primary agent and submits a coding task. The model receives the current LiteCode system prompt plus project contract and session context, chooses tool actions, and reacts to persisted results. In orchestrator mode the primary model may define a team structure, allocate write scopes, launch independent child sessions, inspect the current roster, send correction/continuation work, stop bad work and synthesize results.

Child completions are lifecycle facts reconstructed from durable session data and delivered back to the parent. The human UI exposes child roster/status and read-only child transcripts, but the child panel intentionally has no composer or child-control surface; the credited autonomous S3 therefore remains with the orchestrator model rather than being marked with a separate parent mode.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work on the selected workspace through open-ended model/tool action.
- Disturbance / variety regulated: heterogeneous repository structure, incomplete requirements, implementation alternatives, file contents, command/build/test/LSP results, tool/permission failures, context limits and changing workspace state encountered while completing coding work.
- Decisive decision or feedback right: choose which project evidence to inspect, which offered tool/action to invoke, what implementation or command to attempt, how to respond to returned evidence and when the assigned operational outcome is complete.
- Decision owner: the model-backed LiteCode primary agent for ordinary work and each separately instantiated model-backed child session for its delegated bounded outcome.
- Supporting / enforcement mechanisms: agent profiles/tool bindings, model adapters, context pipeline, permission engine, durable session store, snapshots/revert, LSP/search engines, tool pipeline, cancellation and step limits.
- Closure path: task plus current workspace/session context → model selects a tool/action → LiteCode executes or rejects it → tool/environment result is persisted into the same session → the model receives the returned evidence and selects the next action or final response.
- Boundary reachability: ordinary CLI/server/web/desktop turns instantiate the shipped first-party loop directly; child sessions use the same first-party session/turn primitives rather than an adopter-authored agent runtime.
- Why this is / is not agent-owned: removing the model-backed actor while retaining tools, state and permission machinery removes the open-ended task-specific software-engineering judgment.
- Evidence: [`README.md`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/README.md); [`src/agent/core.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/agent/core.rs); [`src/runtime/mod.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/runtime/mod.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external; the assessment credits LiteCode's first-party role/tool/feedback composition, not provider internals.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among concurrently executing child coding S1 cells by autonomously assigning non-overlapping write responsibility and reacting when a worker crosses or collides with that boundary.
- Disturbance / variety regulated: multiple mutation-capable child sessions can operate concurrently on one workspace and otherwise overwrite the same files/regions, act on stale overlapping assumptions or create incoherent parallel changes.
- Distinct S1 units: separately instantiated `general` (and user-defined permitted) child sessions, each with its own durable session/context/turn and independent model/tool execution.
- Inter-S1 disturbance: concurrent mutation-capable children share the project workspace; overlapping writes or ownership scopes can make one worker invalidate another's work.
- Attenuating coordination relation: the shipped orchestrator prompt requires the manager to choose team structure, who touches which files, who is read-only/writable and to maintain “one writer per file region at a time”; assignments carry explicit constraints/write scope to each child. Process-wide file locks additionally reject simultaneous structured writes/edits to the same file across sessions.
- Feedback into subsequent S1 behaviour: the orchestrator's assignment changes the concrete file scope a child is instructed to touch; live corrections can be sent or the child stopped. If two sessions nevertheless collide through structured write/edit, the blocked tool result names the holder session and tells the affected child to retry after the other writer, so later S1 action changes under the coordination result.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping is tied to an explicit shared-file writer-interference problem and a first-party manager policy plus cross-session exclusion specifically aimed at that interference, not to the mere existence of child sessions, queues or messages.
- Decisive decision or feedback right: decide the live team/write-scope partition—who may write which region and when a running worker must be corrected or stopped to preserve that partition.
- Decision owner: the model-backed shipped `orchestrator` primary agent.
- Supporting / enforcement mechanisms: `subagent_launch` responsibility/prompt contract; orchestrator board/write-scope guidance; child role/tool ceilings; process-wide `WorkspaceWriteLock`; structured resource keys; completion/status/message/stop paths.
- Closure path: orchestrator identifies parallel work and interference risk → assigns distinct roles/write scopes in child prompts/board → children act under those scopes → current status/results or a write-lock conflict returns → orchestrator sends correction/stops/reassigns as needed → subsequent child behavior follows the revised coordination.
- Boundary reachability: `orchestrator` is a seeded first-party primary profile with `general` and `explore` in its allowed-subagent set and the full subagent tool series bound through the standard runtime; no consumer-authored coordinator is required.
- Why this is / is not agent-owned: the process lock is deterministic enforcement, but removing the orchestrator model removes the task-specific decision of how to partition real work/file responsibility and how to revise that relation as current team state changes.
- Evidence: [`src/config/global_db/builtin_prompts.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/config/global_db/builtin_prompts.rs); [`src/config/global_db/seed.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/config/global_db/seed.rs); [`src/tools/subagent/launch.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tools/subagent/launch.rs); [`src/tool/write_lock.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tool/write_lock.rs); [`src/tool/executor.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tool/executor.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the hard file lock covers structured `write`/`edit`, not arbitrary shell-side mutation; S2=A therefore rests on the autonomous orchestrator's explicit write-scope/interference policy, with the lock as additional enforcement rather than sole evidence.

## S3 — Inside-and-now control

- State: A
- Function: regulate current team commitments and interventions across the active child-session population on behalf of the user's present project goal.
- Disturbance / variety regulated: children may be running, idle, stopping, completed, failed, blocked, working on obsolete scope or returning evidence that changes which commitment should continue next.
- Whole-system current view: `subagent_list` enumerates every descendant session visible to the primary with agent identity, responsibility, latest assignment preview, raw current session state, running turn age/step and terminal reason; child completions are also injected into the parent through the shared lifecycle source.
- Current-control decision scope: choose team size/roles, launch work, inspect the current roster, continue an idle child with a new fitting assignment, send corrections, wait on a fixed result set, stop stuck/known-wrong work and synthesize/reallocate current commitments.
- Decisive decision or feedback right: decide which current child commitments should exist, continue, be corrected, be stopped or be replaced as the user's active goal evolves.
- Decision owner: the model-backed shipped `orchestrator` primary agent.
- Supporting / enforcement mechanisms: `subagent_list`, `subagent_send`, `subagent_stop`, `subagent_wait`, durable child-session metadata/status, lifecycle completion router, todo/plan/board files and cancellation.
- Closure path: current roster/completion state returns to orchestrator → orchestrator judges current allocation/intervention → launch/send/stop/wait/reassignment action changes active child commitments → later child operation/results reflect that decision and return to the manager.
- Boundary reachability: the seeded orchestrator has the standard primary tool bindings and allowed `general`/`explore` children. Its shipped system prompt explicitly names team management, roster inspection, continuation and stopping as manager duties.
- Why this is / is not agent-owned: session state, lifecycle routing and cancellation only expose/enforce facts. Removing the orchestrator model removes the semantic decision of which current commitments to create, continue, redirect or stop.
- Evidence: [`src/config/global_db/builtin_prompts.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/config/global_db/builtin_prompts.rs); [`src/tools/subagent/list.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tools/subagent/list.rs); [`src/tools/subagent/send.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tools/subagent/send.rs); [`src/tools/subagent/stop.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tools/subagent/stop.rs); [`src/tools/subagent/hub.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tools/subagent/hub.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the human Workers roster is an observation/navigation surface and child panels are deliberately read-only, so no separate parent-governed S3 mode is credited from the UI.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation work through a fresh non-authoring child session assigned to verify specified claims/evidence, then return that verifier's result to current control.
- Disturbance / variety regulated: an implementation child can report completion while its own assumptions/tests miss defects, or while the manager lacks independent evidence that the delivered change satisfies done criteria.
- Claim being audited: that another child/main implementation satisfies the specified coding requirement and verification criteria in the actual workspace.
- Ordinary reporting path: the implementing child returns its own conclusion/tests/evidence through its normal durable child turn result.
- Complementary access path: the shipped orchestrator policy explicitly requires verification to be “someone who did not write that code” and states that verification/unrelated work should use a new hire/new session; the orchestrator can launch a fresh `general` child with direct repository/test tools or a fresh read-only `explore` child for independent inspection.
- Independence boundary: the verifier has a separate child session, fresh conversation/context and separately assigned responsibility rather than continuing the implementer's session. Provider family may be the same, so independence is contextual/access-path rather than model-provider diversity.
- Who acts on findings: the orchestrator receives the verifier completion through the parent completion router/durable turn result and can accept, send corrective work, stop/replace a bad implementation path or launch another bounded fix before reporting completion.
- Decisive decision or feedback right: make the semantic verification judgment from a fresh, non-authoring model context examining the actual project evidence requested by the manager.
- Decision owner: the model-backed fresh verifier child selected/assigned by the autonomous orchestrator.
- Supporting / enforcement mechanisms: shipped orchestrator verification rule; seeded `general`/`explore` roles; new child-session creation; responsibility/done-criteria prompts; direct read/search/bash/test tool access as role permits; completion routing.
- Closure path: implementation result returns → orchestrator assigns explicit proof criteria to a fresh non-authoring child → verifier inspects/runs the relevant evidence and returns judgment → orchestrator uses that finding to accept or change current implementation work → subsequent operation changes accordingly.
- Boundary reachability: the verifier is constructed from seeded first-party subagent roles via the ordinary `subagent_launch` path, and the requirement for independent authorship is part of the shipped orchestrator prompt rather than consumer-authored coordination code.
- Why this is / is not agent-owned: deterministic session plumbing cannot decide whether arbitrary implementation evidence proves the requirement; removing the fresh verifier model removes the complementary semantic audit judgment.
- Evidence: [`src/config/global_db/builtin_prompts.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/config/global_db/builtin_prompts.rs); [`src/config/global_db/seed.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/config/global_db/seed.rs); [`src/tools/subagent/launch.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tools/subagent/launch.rs); [`src/tools/subagent/hub.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tools/subagent/hub.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: verification is manager-chosen rather than a mandatory gate on every code change; the positive state relies on the explicit non-authoring/fresh-session rule and corrective return, not merely on generic subagent availability.

## S4 — Intelligence / adaptation

- State: —
- Function: no material first-party outside-and-then loop was established that senses external/future-relevant change, develops adaptation options and returns a selected option into LiteCode's present organizational capability.
- Disturbance / variety regulated: session search, context compaction, web-capable explore workers, hot-plug provider/tool configuration, workspace engines and the persistent knowledge base expose information or preserve useful state, but none closes the required prospective organizational adaptation loop in the standard distribution.
- Decisive decision or feedback right: none established for S4.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: `session_search`; websearch/webfetch on explore; project knowledge tool/files; workspace drift reminder; provider/model/agent settings; MCP/custom-tool definitions; code search/LSP readiness; context compaction.
- Closure path: not applicable; no first-party external/future distinction → adaptation-option formation → selected persistent capability/strategy change → return into current S3/capability loop was found.
- Why this is / is not agent-owned: persistent knowledge is explicitly described as human-owned; agent-created knowledge nodes begin `pending` and a person enables them. The drift detector tells the agent to notify/ask the user before organizing stale knowledge. Web exploration and session retrieval answer present work rather than autonomously adapting the organization for future environmental change.
- Evidence: [`src/tools/knowledge.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/tools/knowledge.rs); [`src/knowledge/reminder.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/knowledge/reminder.rs); [`src/config/global_db/builtin_prompts.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/config/global_db/builtin_prompts.rs); [`README.md`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a user can compose research, knowledge and settings into an adaptation process, but generic composability/current-task research does not donate S4 ownership to the frozen standard distribution.

### Absence scope

- Surfaces inspected: session search/history; context compaction; explore web research; knowledge creation/status/reminders/drift; provider/model hot-switching; editable agent definitions; MCP/custom-tool definitions; LSP/code-search engine readiness; workspace config and current orchestration.
- Plausible first-party paths checked: persistent knowledge as learning; workspace-drift reminder as adaptation trigger; explore web research as external intelligence; hot-plug tools/models as capability adaptation; agent-profile editing as organizational redesign; session memory as learning.
- Why no material first-party path remains: the located features either serve present S1/S3 work, preserve/retrieve history, or expose operator-controlled configuration. The one durable knowledge path explicitly reserves activation/maintenance authority to a person and lacks a shipped external/prospective option-selection loop returning into S3.

## S5 — Identity / ultimate policy

- State: P
- Function: establish and preserve the durable workspace contract that defines project-level standing instructions and advance authorization governing later LiteCode coding behavior.
- Disturbance / variety regulated: inconsistent project rules, missing durable authorization, divergent coding conventions and later agent behavior that no longer reflects the legitimate project owner's standing constraints.
- Identity / ultimate-policy issue: what persistent project instructions, boundaries and authorization should govern LiteCode agents working in this workspace.
- Ultimate authority in each claimed mode: Parent (`P`) — the legitimate project owner/operator owns the authoritative `CLAUDE.md` workspace contract. No separate first-party autonomous S5 policy-authoring mode is established.
- Return-to-operation path: LiteCode initializes/recognizes root `CLAUDE.md`; each new turn re-reads it from disk through `contract_snapshot_for_turn`; `build_system_prompt` splices the contract into every non-hidden agent's system prompt; later model/tool behavior is therefore governed by the returned owner-selected policy.
- Decisive decision or feedback right: decide the semantic content of the durable workspace contract, including project instructions and advance authorization boundaries.
- Decision owner: the legitimate project owner/operator at the parent recursion.
- Supporting / enforcement mechanisms: workspace initialization shell; workspace editor/file persistence; per-turn contract snapshot; system-prompt splicing; permission engine and built-in prompts that explicitly honor durable `CLAUDE.md` authorization.
- Closure path: project policy/authorization issue → owner writes/edits root `CLAUDE.md` → file persists → the next turn re-reads the fresh contract → LiteCode injects it into the model's system context → subsequent operation follows that returned standing policy.
- Boundary reachability: workspace initialization creates the contract surface in ordinary projects; the standard runtime re-reads it for every turn and the desktop/browser product includes direct workspace editing. No external governance adapter is required for the parent decision to return into operation.
- Why this is / is not agent-owned: ordinary agents can technically edit files, but the shipped prompt treats `CLAUDE.md` as durable user/project authorization rather than an agent-owned self-authorization channel. The decisive ultimate-policy right therefore remains with the legitimate project owner.
- Evidence: [`src/config/workspace.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/config/workspace.rs); [`src/context_pipeline/env.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/context_pipeline/env.rs); [`src/context_pipeline/system.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/context_pipeline/system.rs); [`src/runtime/mod.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/runtime/mod.rs); [`src/config/global_db/builtin_prompts.rs`](https://github.com/itissika/litecode/blob/146a9feff9edee2204138f18473b9bef83c41c5a/src/config/global_db/builtin_prompts.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is project-recursion S5, not ownership of LiteCode's product-level safety model or provider configuration. A user asking an agent to edit the contract does not by itself transfer ultimate authority away from the user.

## Distributed OSS parent arrangement

LiteCode's public repository maintainers govern the LiteCode software project, but that development governance is outside the local project/session organization assessed here. The credited S5 parent is the local project's legitimate owner/operator whose workspace contract is consumed by the running harness.

## Self-hosted and non-human modes

S1/S2/S3/S3* can operate without continuous human decisions once the orchestrator task and configured authority are supplied. Human approval/permission prompts constrain risky operations but are not promoted into S3. The explicit human-owned organizational function is S5 through the durable project contract; human-owned knowledge activation does not by itself establish S4.

## Recursion

At the selected project/session recursion, primary and child model-backed coding sessions are S1 cells. The orchestrator coordinates their write scopes as S2, manages their current commitments as S3, and can instantiate a fresh non-authoring child as S3*. The project owner remains at the parent recursion for S5 through the workspace contract.

## Variety and escalation

Local coding variety is handled within each S1. Shared-write interference escalates to orchestrator scope and is additionally blocked by process-wide structured-write exclusion. Child state/completions return to the orchestrator for current intervention. Verification findings return from a fresh child before acceptance. Project-level standing-policy changes return on the next turn through the contract snapshot. No S4 adaptation escalation path is established.

## Evidence gaps

No evidence gap requires `?`. The multi-agent positive claims are tied to the shipped orchestrator mode and frozen implementation paths; S4 is supported by an explicit absence review, and S5 is limited to the parent-owned workspace contract rather than generic settings.

## Assessment summary

LiteCode closes autonomous coding S1, autonomous inter-S1 coordination through the shipped orchestrator's explicit write-scope policy, autonomous whole-team current control through live child management, and autonomous complementary audit through fresh non-authoring verifier sessions. Persistent research/memory/configuration features do not close outside-and-then S4. Project-level ultimate policy remains parent-owned through the root `CLAUDE.md` workspace contract that LiteCode re-reads and injects into subsequent turns.

Proposed vector: **`A · A · A · A · — · P`**.
