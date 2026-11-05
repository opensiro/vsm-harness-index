---
harness_id: meka
project_name: meka
repository: https://github.com/k4yt3x/meka
review_ref: b7c188a831f888e8accecc1bbe7bd95a7a0112c8
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# meka

## Review boundary

- System in focus: one locally hosted meka session, optionally supervising its own bounded family of first-party spawned agent workers, across the shipped CLI, ACP or HTTP host interfaces.
- Purpose and identity: carry out user goals using model-selected tools, memory, scheduled turns and delegated subagents while conserving permission boundaries, scoped file writes and persistent session state.
- Relevant environment: user/editor/API instructions, files and shell, network/MCP tools, filesystem changes made concurrently by parent and workers, provider responses, long-running background jobs, schedule triggers and parent permission changes.
- Standard-distribution boundary: the shipped Rust agent runtime, tool registry, subagent session/permission/inbox lifecycle, file conflict guards and host/session store; external providers, MCP servers, user-defined skills and third-party web frontends are dependency surfaces rather than first-party decision owners.
- Credited operating / distribution surfaces: [agent turn](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/agent/turn.rs), [tool dispatch](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/agent/dispatch.rs), [subagent lifecycle](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/subagent.rs), [file freshness](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/file.rs), [shared file locks](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/workspace.rs), [agent tools guide](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/tools/overview.md).
- Adjacent first-party surfaces excluded from ownership: Rust repository CI/test suites, public website and optional `mekaweb`/`mekabridge` integration repositories, documentation-only examples and OS/provider infrastructure. Source tests corroborate mechanics but do not supply a separate runtime auditor.
- First-party operating / deployment modes considered: interactive CLI, one-shot, ACP and resident HTTP session; one-agent mode; multi-subagent mode with parallel spawn, follow-up/steer/delete; default and optional background jobs, schedule and skills; confined `file_*` versus shell/MCP external mutation paths.
- Recursion level: a parent meka session and its immediate delegated S1 work cells. A nested worker with children constitutes another possible local recursion, but grandchildren are not silently credited to the parent's direct current-view boundary.
- Reviewed revision: `b7c188a831f888e8accecc1bbe7bd95a7a0112c8`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The agent loop obtains model responses, resolves tool schemas, admits calls against a permission ladder, dispatches inline or background and feeds tool results into subsequent rounds. It persists conversations, checklist commitments, scratchpad/memory and project/session records. Optional scheduling creates a prompt that becomes another agent turn (possibly after a cheap gate), not an external planning agent in its own right. The hosted runtime supports multiple model backends and CLI/ACP/HTTP surfaces. [README](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/README.md), [turn implementation](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/agent/turn.rs), [dispatch](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/agent/dispatch.rs), [scheduling guide](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/usage/scheduling.md).

An agent can spawn independent subagents with private conversation and checklist, optionally scope them to different worktrees/directories/tools and later list, follow up, steer or interrupt them. The parent receives worker reports; an explicitly selected direct child can be revised in place. Rights narrow down the tree: persisted spawn specifications, bounded permissions/tools/network/scope and replayed follow-up ceilings prevent privilege escalation. Parent and worker registries share host-wide `WriteLocks` keyed by canonical file path, serializing first-party file edits and returning stale-read failures instead of overwriting a concurrent edit. These protections are not universal: shell commands and MCP servers can write outside the internal file tool's coordination, and a model can explicitly request `force`. [Subagents](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/subagent.rs), [write locks](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/workspace.rs), [file edit](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/file.rs), [permissions](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/usage/permissions.md).

## Operational model

At least one model-backed agent performs bounded work by choosing successive tool calls in response to results. With `agent_spawn`, independently modeled child work cells have private turn/memory/checklist state and shared access to some files, while the parent agent retains a live child roster and the discretion to start, follow up, interrupt/steer or discard its direct reports. The first-party file tool's per-path lock plus fresh-read requirement provides a constructor-owned collision attenuation surface, even when the model's own task planning is imperfect. Distinguish that bounded S2 from a general shared-project conflict resolver. Host permission approval is action-specific, not a legitimate S5 identity-policy decision.

## S1 — Operations

- State: A
- Function: complete a user's coding/research/general assistant task, or a delegated task in a scoped subagent, through model-selected tool actions and observations.
- Disturbance / variety regulated: changing user needs, unpredictable shell/file/web/MCP observations, incomplete memory, tool errors and subtask requirements.
- Decisive decision or feedback right: each model decides whether to use shell, file, memory, research, scheduling, subagent or other admitted tools and chooses its subsequent course after results.
- Decision owner: each active meka model-backed session/worker in the first-party agent turn loop.
- Supporting / enforcement mechanisms: provider adapters, registry/tool discovery, tool dispatch and results, persistent sessions, skills, memory, checklist, permission levels and optional scheduled/background turns.
- Closure path: user/scheduled/background/parent prompt → provider response with selected tool calls → `dispatch` gated execution → result blocks returned to the same agent → model revision or answer.
- Boundary reachability: shipped CLI/ACP/HTTP use the same agent core; `agent_spawn` builds a real narrowed worker and calls the agent turn loop, so multi-worker S1 is not a mere README topology.
- Why this is / is not agent-owned: model selects operational actions and revises them under observations; scheduled triggers, scope admission, memory persistence and fallback enforcement are supporting mechanics.
- Evidence: [turn code](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/agent/turn.rs), [dispatch](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/agent/dispatch.rs), [subagent spawn](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/subagent.rs), [README](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/README.md).
- Basis: frozen implementation and shipped user/tool contracts.
- Confidence: high structurally; no paid provider E2E executed in this review.
- Caveats: the model's tool rights depend on runtime permission, optional settings and host credentials. Subagents can be disabled; that removes multi-unit positive modes without removing single-agent S1.

## S2 — Coordination

- State: C
- Function: attenuate concurrent edit interference between independent parent/child or sibling agent work cells using shared first-party file tools.
- Disturbance / variety regulated: two separate agent sessions attempt to edit the same disk/editor file based on stale or concurrently changing contents, risking lost updates.
- Decisive decision or feedback right: host-scoped file guard serializes one path's read/check/edit/write, refuses stale changes, and forces a later agent/tool call to re-read or explicitly override.
- Decision owner: constructor-owned `WriteLocks` and `ReadTracker`/`stale_read_complaint` logic; the model/caller must choose follow-up conflict resolution.
- Supporting / enforcement mechanisms: canonical path keys, shared per-host async mutex, per-agent read stamp, compare against disk/editor buffer, conflict error tool result and direct-child workspace bounds.
- Closure path: agent A reads/writes a file → agent B's older stamped edit arrives → same-path lock plus freshness check rejects B's stale write → error returns to B's model, which can re-read/re-plan; non-conflicting paths proceed.
- Boundary reachability: `SessionMaterials` carries one shared host-wide `WriteLocks` to parent and worker registry scopes, and first-party `file_edit` takes `scope.lock_path` over the read-modify-write step; a specific source-level cross-registry collision hazard is documented and tested.
- Why this is / is not agent-owned: conflict detection/serialization is deterministic constructor ownership (`C`), not negotiated by an autonomous S2 model. The agent may respond, but the first-party regulator specifically targets cross-cell interference.
- Distinct S1 units: concurrently active parent and spawned child or two sibling subagents, each with independent model turn and local read history.
- Inter-S1 disturbance: a shared workspace file is modified after another S1's read, or simultaneous file edits would overwrite one another.
- Attenuating coordination relation: host-shared canonical-path lock and version/freshness validation establish write serialization and refuse stale intent.
- Feedback into subsequent S1 behaviour: returned `changed on disk/editor` error instructs re-read; the worker model sees the refusal and can adjust its next file operation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the first-party mechanism is explicitly shared **across separate agent registries** to resolve an actual write/write race and provide corrective feedback, not merely to queue one conversation's calls.
- Evidence: [WriteLocks rationale](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/workspace.rs), [file edit lock/freshness](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/file.rs), [background concurrency guide](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/usage/background.md).
- Basis: first-party source mechanism plus source tests for stale-read rejection, bounded positive.
- Confidence: medium-high for `file_*` paths, not for arbitrary shell/MCP operations.
- Caveats: the guide correctly warns no **universal** coordination: shell writes and external tools can bypass these guards, and `force` can override freshness. This is a bounded constructor path, not end-to-end team settlement.

## S3 — Inside-and-now control

- State: A
- Function: regulate the *current* direct-child task portfolio when an agent has actually spawned subagents and is responsible for the joint user goal.
- Disturbance / variety regulated: evolving subtasks, incomplete/late child reports, need to redirect a running worker, redundant continuation and parent/worker permission changes.
- Decisive decision or feedback right: parent model decides which independent tasks to delegate, what rights/scope each gets, whether to follow up or steer/interrupt a running child, and when to discard an obsolete worker.
- Decision owner: parent meka model with the shipped `agent_spawn`, `agent_list`, `agent_followup`, `agent_steer`, `agent_delete` tools; Rust enforces membership and scope ceilings.
- Supporting / enforcement mechanisms: persisted session parent-child rows, child reports, `agent_list` direct-child roster and activity, in-flight interrupt/steer inbox, conversation lookup, parent checklist and bounded recursion.
- Closure path: parent sees its task commitments and child reports/roster → model selects new assignment/follow-up/steer/interrupt/delete → first-party child session receives revised work or termination → next child report returns to parent.
- Boundary reachability: multi-subagent mode is built into the default tool registry (when depth permits); `agent_list` loads actual direct-child session rows, `agent_steer` writes the child's inbox, `agent_followup` resumes persisted child under recorded grants. No external orchestrator plugin is required.
- Why this is / is not agent-owned: the *decision* to change child commitments belongs to the model parent; direct-child membership, permission and inbox delivery are deterministic enforcement. The single-agent mode does not by itself supply this S3.
- Whole-system current view: parent session's current task/checklist plus directly spawned child identifiers, directories, turn/activity records, reports and accessible child conversations at this explicitly bounded recursion.
- Current-control decision scope: initiate/reallocate subtask effort among children, change a running child's instructions, interrupt superseded work, resume or delete child resources under the owner's chosen parent goal.
- Evidence: [subagent lifecycle and model tools](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/subagent.rs), [subagents guide](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/tools/overview.md), [checklist](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/usage/checklist.md).
- Basis: frozen implemented optional multi-worker mode with explicit current-control rights.
- Confidence: medium; closure is source-reachable, no actual multi-agent model-run transcript inspected.
- Caveats: direct-child visibility is bounded, not a global entire-installation fleet control; ordinary one-off delegation without reassessment/steer would remain task-level routing and should not be used alone as S3 evidence.

## S3* — Complementary audit

- State: —
- Function: no independent authority checks live agent completion claims against a separate evidentiary path and returns a veto to S3.
- Disturbance / variety regulated: a child may submit inaccurate final reports or a parent may declare an unchecked task complete.
- Decisive decision or feedback right: checklist nudges stop an agent with its **own** open commitments, while parent can read child conversations; neither is an automatically independent outcome audit.
- Decision owner: same parent/child model and deterministic checklist; no separately commissioned auditor with distinct reality access.
- Supporting / enforcement mechanisms: list states, bounded completion nudges, status/turn logs, child reports and persistent inbox.
- Closure path: checklist can force same agent to continue/cancel/defer; parent can manually inspect another session's transcript, but no shipped complementary inspector/adjudicator returns a finding to whole-system control.
- Why this is / is not agent-owned: same-agent task assertions and log replay do not independently verify raw artifacts or challenge their meaning.
- Evidence: [checklist guide](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/usage/checklist.md), [subagent tools](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/subagent.rs), [README](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/README.md).
- Basis: frozen source and scoped negative.
- Confidence: medium-high.
- Caveats: a parent may deliberately spawn an independent test agent with raw artifact access, but generic worker creation plus task wording alone does not establish a supplied independent audit mode.

### Absence scope

- Surfaces inspected: checklist/turn completion enforcement, child result/report pipeline, session conversation tools, background and schedule reporting.
- Plausible first-party paths checked: fresh independent reviewer, raw-file diff/test audit, independent verifier gates, parent reading child transcripts and independent veto/correction return.
- Why no material first-party path remains: no first-party complementary evidentiary audit owner and closed findings-to-control loop is established beyond ordinary reports and self-commitments.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future/environment sensing and resulting capability adaptation decision loop.
- Disturbance / variety regulated: changing web/MCP data, future time triggers, new tools and user-created skills; each can be observed on demand or scheduled.
- Decisive decision or feedback right: model can schedule future ordinary tasks, call web tools, write configured skills or switch provider profiles; no shipped prospective option assessment owns adaptation and returns a capability change.
- Decision owner: task agent/operator acting through general tools, not a distinct future-facing intelligence function at this boundary.
- Supporting / enforcement mechanisms: `schedule_create` with a predicate gate, web_fetch, tool discovery, optional agent-managed `skill_*` and profile selection.
- Closure path: scheduled observation → new regular S1 turn; skill write may change an operator-configured instruction package, but no first-party prospective environmental model/options/consequence/decision return is specified.
- Why this is / is not agent-owned: self-scheduling or researching today's environment extends S1 operations without a closed external-and-future S4 adaptive right.
- Evidence: [scheduling guide](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/usage/scheduling.md), [skills guide](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/usage/skills.md), [registry](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/registry.rs).
- Basis: frozen source, scoped negative.
- Confidence: medium-high.
- Caveats: external agents can build such a workflow using meka primitives, but this assessment does not credit hypothetical composition.

### Absence scope

- Surfaces inspected: schedule/gate, web, memory, skills, profile and MCP tools, subagent delegation.
- Plausible first-party paths checked: recurring horizon scans, automatic skill changes, future planning, architectural adaptation options and return into current capabilities.
- Why no material first-party path remains: the distributed primitives can support custom prospective work but do not ship a material S4-specific model/options/adaptation feedback path.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate-policy/identity authority with a returned governance decision for this local agent organization.
- Disturbance / variety regulated: user permission levels, tool approvals, model/skill choices and persisted capability restrictions, not contests over institutional identity or ultimate purpose.
- Decisive decision or feedback right: user/operator grants read/workspace/unrestricted authority or approves individual tool calls; subagent grants may only narrow and never widen past parent.
- Decision owner: human operator for runtime permissions and parent-supplied goal, not a first-party S5 identity/policy deliberator.
- Supporting / enforcement mechanisms: permission ladder, approval callbacks, follow-up scope clamp, `ToolScope` filters and sandboxing.
- Closure path: a tool call may be permitted/refused, and a later parent permission change limits children; no policy-identity issue is escalated for legitimate collective authority and returned as a standing new organizational purpose.
- Why this is / is not agent-owned: action-level consent and fixed safety limits remain bounded runtime authorization, not the S5 viability policy function.
- Evidence: [permission guide](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/docs/book/src/usage/permissions.md), [subagent grant replay](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/tools/subagent.rs), [dispatch approval](https://github.com/k4yt3x/meka/blob/b7c188a831f888e8accecc1bbe7bd95a7a0112c8/src/agent/dispatch.rs).
- Basis: frozen source, scoped negative.
- Confidence: high.
- Caveats: a parent institution could use meka as a tool while retaining S5 outside this software; such external governance is not imported.

### Absence scope

- Surfaces inspected: permission/approval dispatch, config and profile, subagent scope inheritance, host APIs and top-level user instructions.
- Plausible first-party paths checked: enduring identity-policy revision, institutional arbitration, human parent decision followed by returned new policy/mission, retained S5 mandates.
- Why no material first-party path remains: all reviewed authority checks are input/tool capability gates or external user objectives, not a shipped ultimate-policy governance closure.

## Recursion

Each spawned worker has independent model/conversation/checklist and may itself spawn children within depth caps. Its parent observes only direct children and may choose to steer or interrupt them; a descendant's own task organization is a different bounded recursion. `WriteLocks` is host-scoped and serves all such cells when they choose first-party file tools; it is not a cross-host distributed regulator.

## Variety and escalation

Memory, tool discovery, context compaction and scheduled triggers handle task/temporal variety. Parent/child scopes attenuate authorization variety, shared path locks and stale-read refusals attenuate bounded file collisions, and parent model can intervene on an ongoing child through an explicit inbox. Checklist nudges enforce completion honesty within the same actor, not an independent audit escalation.

## Evidence gaps

- Review uses frozen first-party Rust source, public book and tests; no live provider, MCP or resident multi-agent E2E was executed.
- S2 positive is explicitly bounded to `file_*` operations inside a shared host; direct shell/MCP writes or `force` can bypass and should not be represented as guaranteed isolation.
- S3 positive applies only when a model actively manages an actual direct-child portfolio. `agent_spawn` alone is not evidence of a current-control decision; `agent_list`/report/steer/followup/interrupt closure supplies the distinct right.
- No actual independent source-artifact audit or prospective adaptation decision path is part of the standard distribution under this reviewed boundary.
