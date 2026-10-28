---
harness_id: openorc
project_name: OpenOrc
repository: https://github.com/davejj1530/openorc
review_ref: 85bf1c5e4c81000911d8a5a90e23dbb7cf869283
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: A(P)
---

# OpenOrc

## Review boundary

- System in focus: supported OpenOrc desktop/core runtime, including optional team execution, independent review and persistent Orcling modes; one local user-operated project/team organization.
- Purpose and identity: produce software/project outcomes through registered coding-agent actors, coordinated workspaces and explicit owner-selected permissions/identities.
- Relevant environment: user projects/Git, installed authenticated coding CLIs, shared files, agent results, pull requests and local operator decisions.
- Standard-distribution boundary: Electron desktop assembles core workflows, vendor adapters, local MCP tools, SQLite journals, Git workspaces, review and Orcling identity services.
- Credited operating / distribution surfaces: packages/core run/team/review/orcling services, packages/agents adapters, packages/mcp tools and packaged desktop composition; first-party role instructions/actions are included.
- Adjacent first-party surfaces excluded from ownership: scripted test providers, website demos/screenshots, benchmark/CI/release automation and maintainer development governance. External CLI internal organization is not assessed.
- First-party operating / deployment modes considered: single threads/tasks; shipped Beta shared-workspace teams and isolated assignments; selected PR review; Orcling Allow versus Approve/Plan and user profile editing/restoration.
- Recursion level: one local project/team with operative member cells and optional persistent identity actors. Company governance and recursive viability are not inferred.
- Reviewed revision: `85bf1c5e4c81000911d8a5a90e23dbb7cf869283`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

OpenOrc is a Node/Electron workspace with a utility-process core. The run layer composes first-party task/team prompts, model choice, scoped MCP endpoint and permissions into vendor CLI sessions, normalizes their events, persists a ledger and resumes actors from new messages/results. TeamCoordinator journals actors/attempts/messages/claims; assignments receive isolated workspaces or share a claimed workspace. Model members select assignments, file claims, messages, wait/completion and corrections through explicit tools. Scheduler/capacity/deadline enforcement is deterministic. Review creates a separate Plan-mode conversation on a detached PR checkout, records model-authored draft findings and permits later re-review of changed code. Orclings add versioned persistent instructions, local user identity/permission settings and agent instruction-edit tools. Optional memory retains context; it is not automatically prospective adaptation. All cognitive actors still use external installed CLIs, whose unrelated internal capabilities are not borrowed.

## Operational model

The first-party runtime is more than a passive terminal: it assembles role-specific decision contexts and a durable tool/action/feedback protocol around coding-agent processes. Agent actors produce code and task results and can coordinate competing work. Human current-team control remains a distinct mode; the scheduler does not own its resource decisions. Review judgment is model-owned while posting/implementation selections can remain human control. Orcling self-instruction Allow mode and parent-edited/approved mode are separate identity arrangements.

## S1 — Operations

- State: A
- Function: produce software/task results with durable first-party role/action/feedback composition.
- Disturbance / variety regulated: heterogeneous tasks, code/tool failures, delegation outcomes and changing user direction.
- Decisive decision or feedback right: model members choose edits, delegated work, messages and terminal results through scoped MCP tools.
- Decision owner: installed Codex/Claude/OpenCode actors explicitly assembled into first-party run/team roles; external CLI internals are not separately credited.
- Supporting / enforcement mechanisms: provider adapters, RunHandle, task briefs, MCP scope, worktrees, snapshots, journals and settlement/recovery.
- Closure path: user/task brief → provider model action → local tools/files/child result → resumed model turn → captured result and reported completion.
- Why this is / is not agent-owned: substantive work choices come from model actors; host state transitions only transport/enforce them.
- Caveats: requires installed authenticated CLI; source topology is not live model quality.
- Boundary reachability: desktop/core constructs provider adapters and the scoped MCP server; team instructions are injected into actual actor turns, whose tool calls mutate the same live journal and return results.
- Evidence: [packages/core/src/services/run-launch.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/run-launch.ts); [packages/core/src/services/run-turns.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/run-turns.ts); [packages/core/src/services/team-instructions.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-instructions.ts); [packages/core/src/services/team-assignments.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-assignments.ts); [packages/core/src/openorc.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/openorc.ts).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

## S2 — Coordination

- State: A
- Function: attenuate shared-file and assignment interference through agent-owned claim negotiation and returned correction.
- Disturbance / variety regulated: independent coding members may edit the same shared file, duplicate ownership or apply incompatible user direction.
- Decisive decision or feedback right: members choose file ownership/release, alternative work or directed negotiation; lead/members relay concrete corrections to affected workers.
- Decision owner: model-backed team members/lead own coordination choices; journal claims and refusal are enforcement.
- Supporting / enforcement mechanisms: team_claim, team_say/team_message, active claims, role boundaries, captured changed files and isolated assignment integration.
- Closure path: claim conflict returns holder/file → model asks colleague or selects other work → colleague releases/revises scope → later claim/work proceeds; affected active workers receive new direction.
- Why this is / is not agent-owned: the model chooses the conflict response; a fixed refusal alone is not the credited autonomous owner.
- Caveats: claims are advisory and depend on model compliance; not an OS-level write sandbox, and live effectiveness is unmeasured.
- Boundary reachability: Beta team execution exposes team_claim and chat tools to running members, with conflict text returned directly to the requesting model.
- Distinct S1 units: distinct coding members/contribution actors producing changes in a common project workspace or isolated child assignments.
- Inter-S1 disturbance: overlapping file ownership and incompatible concurrent edits/direction, explicitly addressed by first-party shared-workspace instructions and held-path refusal.
- Attenuating coordination relation: claim before editing; on collision ask current holder in chat or choose another file; release claims and deliver scoped corrections to affected members.
- Feedback into subsequent S1 behaviour: holder/conflict data and chat are included in subsequent actor turns, changing who edits which files and under which direction.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: this witness names the shared-file collision, actor-selected response and resumed work; the generic message bus and hierarchy alone are not counted.
- Evidence: [packages/core/src/services/team-instructions.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-instructions.ts); [packages/core/src/services/team-chat.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-chat.ts); [packages/core/src/services/team-delivery.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-delivery.ts); [packages/core/src/mcp-host/team.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/mcp-host/team.ts).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

## S3 — Inside-and-now control

- State: P
- Function: parent current-control over the whole active local team execution and its operational commitments.
- Disturbance / variety regulated: active assignments may need stopping/recovery, changed direction or intervention after conflicting/failed integration.
- Decisive decision or feedback right: operator inspects whole-team runtime and selects scoped direction, stop, actor retry, Plan/Act implementation and retained integration recovery.
- Decision owner: legitimate local desktop user owns this supervisory current-control mode; lead performs delegated work coordination; fixed scheduler does not own resource discretion.
- Supporting / enforcement mechanisms: runtime actor/attempt/task view, ownership checks, direction/admission keys, scoped delivery, stop/retry and guarded recovery receipts.
- Closure path: whole-team runtime → operator intervention/direction → coordinator fences/stops/retries or delivers changed direction → actors resume or withhold work under the returned decision.
- Why this is / is not agent-owned: P is based on the combined team-wide view and applied intervention path, not a generic stop button or the class name TeamCoordinator. No autonomous whole-system S3 choice is established.
- Caveats: scope is one local team/project execution, not all organizations or a global fleet. User must exercise the supported control; source establishes capability, not observed intervention history.
- Boundary reachability: desktop orchestration RPC exposes current team runtime and guarded send/stop/retry/implementPlan/recovery methods; they act on the owned execution journal rather than an adjacent dashboard.
- Whole-system current view: team conversation runtime includes pinned team revision, execution actors/attempts, retained work/results and recovery state across active member cells.
- Current-control decision scope: current team commitment/direction, withholding or restarting affected actors, moving planning to implementation and applying retained integration recovery; scheduler limits only enforce the selected envelope.
- Evidence: [packages/core/src/services/team-conversation.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-conversation.ts); [packages/core/src/services/team-coordinator.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-coordinator.ts); [packages/core/src/services/team-attempt-recovery.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-attempt-recovery.ts); [packages/core/src/handlers/orchestration.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/handlers/orchestration.ts).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

## S3* — Complementary audit

- State: A
- Function: independent source-backed model review challenges proposed code before user publication or corrective implementation.
- Disturbance / variety regulated: unsupported completion claims and defects in proposed PR code; previous findings may remain after revision.
- Decisive decision or feedback right: separate review model chooses findings and summary against raw checkout/diff; user retains posting and follow-through selection.
- Decision owner: dedicated review conversation/model owns audit judgment; Git checkout/draft parser and human publication are distinct support/control.
- Supporting / enforcement mechanisms: detached PR checkout, Plan-mode review, scoped finding/summary tools, exact-commit drafts and re-review after head change.
- Closure path: raw PR code/diff → separate reviewer model findings → draft visible to operator/control; selected findings can be sent into task/team implementation and later review checks whether addressed.
- Why this is / is not agent-owned: audit judgment is model-authored, not the coder completion narrative or deterministic Git diff. Human ownership of external posting does not author the audit conclusion.
- Caveats: not independent provider validation or measured detection efficacy; arbitrary team member named reviewer alone is not credited.
- Boundary reachability: the shipped PR-review service creates the dedicated conversation/checkout, injects review-only instructions and exposes draft finding tools; normal task/team review selections have first-party return paths.
- Claim being audited: proposed source changes are correct and prior findings have been addressed.
- Ordinary reporting path: implementation conversation, task result and PR description.
- Complementary access path: detached current-head source checkout plus direct diff, with subsequent reviews comparing changed commits rather than merely repeating author reports.
- Independence boundary: separate review conversation in Plan mode with explicit prohibition on implementation, file changes, push and posting; isolated from the author workspace.
- Who acts on findings: operator sees/selects draft findings; task/team review-send paths return selected corrections to implementation; subsequent model review checks retained findings against new code.
- Evidence: [packages/core/src/services/pull-requests.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/pull-requests.ts); [packages/core/src/services/pull-request-checkout.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/pull-request-checkout.ts); [packages/core/src/services/review.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/review.ts); [packages/core/src/services/team-tasks.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-tasks.ts).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

## S4 — Outside-and-then intelligence

- State: —
- Function: no outside-and-future adaptation loop into OpenOrc current capability established.
- Disturbance / variety regulated: new task context, project lessons, user preferences and updated software versions.
- Decisive decision or feedback right: memory extraction and instruction changes retain collaboration context; updater checks releases.
- Decision owner: task/Orcling agents own local content changes; operator and maintainers own externally selected capability/product evolution.
- Supporting / enforcement mechanisms: project memory/retrieval, Orcling histories/instructions, model selection and release updater.
- Closure path: past work/user preference is reused or a released app is updated; no prospective environmental model develops adaptation options and returns a capability decision into current control.
- Why this is / is not agent-owned: memory, self-instruction edits and update notification do not by themselves satisfy S4.
- Caveats: does not rule out a larger organization using outputs for strategy.
- Evidence: [packages/core/src/services/memory.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/memory.ts); [packages/core/src/services/orcling-briefs.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/orcling-briefs.ts); [packages/core/src/services/orclings.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/orclings.ts); [apps/desktop/src/main/app-updates.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/apps/desktop/src/main/app-updates.ts).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Project memory, Orcling history/instruction tools, model settings, update/feed and supported product documentation.
- Plausible first-party paths checked: learned user needs, project lessons, instruction evolution, available provider models and released updates.
- Why no material first-party path remains: reviewed paths retain task/identity context or apply externally made release choices; no shipped external/prospective adaptation-options-to-current-capability loop is evidenced.

## S5 — Policy and identity

- State: A(P)
- Function: maintain a persistent Orcling behavioral identity/charter in alternative agent-owned and parent-governed modes.
- Disturbance / variety regulated: new lasting collaboration requirements or owner dissatisfaction require changing the same actor instructions across future sessions.
- Decisive decision or feedback right: Allow mode lets the Orcling choose and save revised enduring instructions; Approve/Plan requests explicit parent authorization, and user profile editing/restoration supplies a direct parent mode.
- Decision owner: Orcling model for autonomous instruction revision; local user for approved/editor/restore mode and immutable permission/identity ceilings.
- Supporting / enforcement mechanisms: versioned orcling_instructions, reason/author records, action-policy approval gate, profile editing/restoration and fresh-process identity brief.
- Closure path: lasting identity/working rule → model revised charter or user-selected edit/restore → version saved → next session/process injects current instructions wherever the actor works.
- Why this is / is not agent-owned: the autonomous base is the local actor charter, not authority to widen host permissions; parent mode separately owns identity/permission selection and approved charter change.
- Caveats: not every instruction edit is S5: the positive witness concerns persistent identity/behavioral mandate. Models remain under parent-set host permission ceilings; no global institutional S5 is claimed.
- Boundary reachability: Orcling tools are mounted for the saved speaker; updateInstructions authorizes according to its effective mode and saves a version. New provider processes receive the same saved identity/current charter through orclingBrief.
- Identity / ultimate-policy issue: the long-term companion role and enduring behavioral instructions that define how this actor works across projects and conversations.
- Ultimate authority in each claimed mode: Allow mode delegates charter revision to the actor within its immutable host ceiling; Approve/Plan and user edit/restore retain parent decision over the proposed charter/identity.
- Return-to-operation path: saveInstructions/restoreInstructions append the authoritative version; orclingBrief puts current instructions into each newly started process, with an explicit next-session boundary.
- Evidence: [packages/core/src/services/orcling-briefs.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/orcling-briefs.ts); [packages/core/src/services/orclings.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/orclings.ts); [packages/core/src/services/app-actions.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/app-actions.ts); [packages/core/src/services/run-approvals.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/run-approvals.ts); [packages/core/src/mcp-host/orcling.ts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/mcp-host/orcling.ts); [docs/orclings.md](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/docs/orclings.md).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Orcling model, within user-set host ceiling | Lasting collaboration/identity instruction needs revision in Allow mode | orcling_instructions_update saves model-selected charter; next process receives it | mcp-host/orcling.ts; app-actions.ts; orcling-briefs.ts |
| Parent (`P`) | Local user | Approve/Plan identity-instruction proposal, profile edit or restore | Exact approval or saved/restored version returns to next actor session | run-approvals.ts; orclings.ts; docs/orclings.md |

## Distributed OSS parent arrangement

Parent modes are local user/project/team or Orcling identity arrangements. Maintainer releases and contributors are not automatically part of this organization; multiple providers do not create project-level governance.

## Self-hosted and non-human modes

Desktop/core compose installed coding CLIs and enforce the stricter place/Orcling permission. Team mode, review and Orcling modes are shipped; authentication is an execution prerequisite. A(P) records alternative charter owners, not two simultaneous ultimate authorities.

## Recursion

Team hierarchy and nested assignments provide local autonomy and return paths but do not prove full viable recursion. S3 P concerns the current team; S5 A(P) is the supported persistent-actor identity mode, explicitly separated from company governance.

## Variety and escalation

Claims, isolated workspaces, retained conflict copies, role-scoped tools, journals/generation fencing, bounded messages, capacity limits and recovery preserve evidence while controlling operational disturbances. Parent current-control can stop/retry/redirect; file negotiations remain local when possible. A status/error alone is not an algedonic channel.

## Evidence gaps

No live CLI/provider/Browser task, paid action or remote review posting performed. Native benchmark-measurement parser tests: 5/5 PASS; these are narrow developer helper checks, not team/review/Orcling execution evidence. Dependency-heavy pnpm/vitest and Electron suites were not installed/run; their source tests are corroboration only. Claim discipline, review efficacy and long-term charter adherence remain unmeasured. Historical discovery mentioning OpenOrc as an external-agent workspace is not a canonical assessment and does not decide this pinned richer runtime.
