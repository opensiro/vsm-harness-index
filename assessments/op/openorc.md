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
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# OpenOrc

## Review boundary

- System in focus: the shipped OpenOrc desktop workspace and one user-supervised local coding-agent team/task, including integrated Codex/Claude/OpenCode subprocesses, project threads, team coordination, review and Orcling identity mode; not the whole OpenOrc OSS contributor organization or external CLI providers.
- Purpose and identity: help a human direct durable software tasks and multiple coding agents, preserve working context, integrate peer work and inspect code changes while maintaining explicit user control over execution, publication and long-term companion identity.
- Relevant environment: local Git workspaces, user instructions, provider accounts and native agent CLI processes, source files, peer coordination, task backlog, SQLite ledger, tests, user review, project memory and GitHub.
- Standard-distribution boundary: Electron desktop UI, utility-process core, TypeScript packages `core`, `agents`, `protocol`, `db`, `git`, `memory`, `mcp`, first-party TeamCoordinator/assignment/chat/turn state, review services and Orcling profile tools. External provider CLIs choose coding decisions within OpenOrc-scoped context.
- Credited operating / distribution surfaces: [`TeamCoordinator`](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-coordinator.ts), [`team-instructions.ts`](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-instructions.ts), [`team-chat.ts`](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-chat.ts), [`team-assignments.ts`](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-assignments.ts), review handlers and Git integration, Orcling identity/instructions and attached owner UI.
- Adjacent first-party surfaces excluded from ownership: tests and scripted-provider simulations, CI/release/packaging work, website demo and roadmap, contributor GitHub reviews, third-party model-provider internal approval/capabilities, and unconfigured external host/web/Slack governance. They may corroborate first-party paths without supplying their missing decisions.
- First-party operating / deployment modes considered: direct local coding chat, project task and isolated-worktree execution, optional saved beta team with lead/member/reviewer and shared room or isolated assignments, human live steering/review, Orcling companion with persistent owner-edited identity, manual project memory. Supported platform caveats in README are retained.
- Recursion level: a local user-defined team/task cell with distinct operational member agents, optionally an Orcling playing a role. A different parent-level OS organization is not inferred from multi-provider use.
- Reviewed revision: `85bf1c5e4c81000911d8a5a90e23dbb7cf869283`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Electron shell passes typed RPC requests to a utility-process `OpenOrc` core, which maintains SQLite team/run/assignment journals, workspace state, provider child-process adapters and a run-scoped MCP tool server. Explicit user task requests start provider work; backlog or Plan mode alone does not. Saved teams can include lead, managers, implementers and reviewers from different CLI providers. The first-party TeamCoordinator owns admission, source/actor state transitions, scheduling, recovery, live steering and file publication. Model actors decide task decomposition, worker assignments, actionable messages and edits under team instructions. Peer messages are delivered to working turns or queued; isolated workers share snapshots and the lead receives accepted outputs on subsequent turns. [Architecture and process](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/ARCHITECTURE.md#L3-L22), [team architecture](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/ARCHITECTURE.md#L78-L94), [behavioral instructions](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-instructions.ts).

Shared-workspace teams implement first-party `team_claim` collision avoidance: a held path cannot be claimed by a second actor, which receives the current holder and is told to ask or choose another file. The lead is instructed to inspect `team_status`, address only affected workers, and report delivery uncertainty. Review workflows expose real source diffs, line comments and selected review feedback; a separately chosen reviewer model/Orcling can read project changes and issue review findings, while the user still decides commits, pushes and merges. Orclings maintain a persistent owner-chosen identity, instructions, memory and permission ceiling across projects, with user edit/restore controls and next-turn prompt propagation. [Team file claims](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-chat.ts#L310-L344), [lead correction/coordination prompts](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-instructions.ts#L1-L9), [Orcling operating guide](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/docs/orclings.md#L1-L41).

## Operational model

The end-to-end S1 result is a user-directed code change, proposal, review comment or saved task artifact. Each provider-backed member controls its source edits/reasoning within a current assignment. First-party team channels reduce cross-worker file/message collisions and a model lead makes discretionary scoped coordination decisions after observing status, teammate reports and human correction. A runtime priority algorithm and immutable journal enforce capacity and ordering, not independently own strategic management. Optional independent review models can inspect the actual changes and return criticism, although user initiation/role configuration remains external. The local human retains ultimate execution/publication and companion identity policy.

## S1 — Operations

- State: A
- Function: implement, investigate, test and review user-requested software changes using model-authored plans, edits, tool calls and peer work.
- Disturbance / variety regulated: heterogeneous codebases and tasks, unknown implementation details, test failures, merge conflicts, provider differences, review comments and revised user priorities.
- Decisive decision or feedback right: acting Codex/Claude/OpenCode model chooses implementation, tool steps, task responses and model-authored corrections; team lead models choose subordinate bounded assignments within user scope.
- Decision owner: external native CLI model sessions explicitly composed by first-party OpenOrc process/run controllers; the user controls whether work is authorized and published.
- Supporting / enforcement mechanisms: typed RPC and provider adapters, task/run journal, Git snapshots/worktrees, per-run MCP tools, permissions, cancellation and result integration.
- Closure path: user task → local provider run → model edits/tool observations → bounded completion/checkpoint and peer/review feedback → corrected work or user-visible artifact/diff.
- Boundary reachability: documented desktop release and source-run workflows actually start native CLI agents; saved team and direct task modes are implemented in the first-party core, not only roadmap wireframes.
- Why this is / is not agent-owned: task-specific implementation and reviewer responses originate in model-agent turns; provider subprocess adapters merely normalize and enforce the selected runtime mode.
- Evidence: [run lifecycle architecture](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/ARCHITECTURE.md#L54-L70), [user authorization limits](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/PRODUCT.md#L7-L15), [team actor instructions and assignment](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-instructions.ts#L49-L70), [README shipped agents](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/README.md#L12-L46).
- Basis: structural.
- Confidence: high for explicit model/run roles; native live provider quality not measured.
- Caveats: the app uses existing provider CLI accounts and explicitly does not guarantee model compliance with instruction-level team coordination.

## S2 — Coordination

- State: A
- Function: prevent concurrent team members from interfering in shared files/workspace and adapt assignment/direction handoffs when overlapping work or user corrections threaten a combined result.
- Disturbance / variety regulated: two agents editing the same path, incompatible assignments, colliding workspace publications, unnecessary relays and racing peer corrections during live work.
- Decisive decision or feedback right: team model lead chooses independent work units, file boundaries and which affected members to correct; peers can request/release file claims and negotiate a held path by messaging the owner.
- Decision owner: provider-backed team lead/member models. Deterministic TeamCoordinator refuses conflicting claims, tracks ownership and serializes delivery, but does not choose the content of the coordination response.
- Supporting / enforcement mechanisms: `team_claim`, shared file ownership context, directed `team_say`/`team_message`, team status, source/actor journals, isolated assignments and recipient-scoped delivery.
- Closure path: lead partitions roles/paths → member claims a file → a competing member sees holder and must coordinate/replan → selected member receives direct correction or changed assignment → next model turn operates with updated claims/messages and integrated work.
- Boundary reachability: shipped team beta mode exposes `team_claim` and messaging in role prompts, and first-party `TeamChat` rejects overlapping claims rather than merely documenting etiquette.
- Why this is / is not agent-owned: the lock/claim check is enforcement; the agent chooses whether to ask a colleague, work elsewhere, release a claim or adjust a worker's scope based on current team evidence.
- Distinct S1 units: separate registered Codex/Claude/OpenCode members/worker turns in a saved team, each with model/tool context and assigned code work.
- Inter-S1 disturbance: overlapping edits and uncoordinated changes to the same shared workspace file, or divergent work after user direction changes.
- Attenuating coordination relation: file claims and holder disclosure, model-selected boundaries, addressee-specific correction relays and later reinspection of team status.
- Feedback into subsequent S1 behaviour: rejected conflicting claim explicitly instructs the second member to ask owner or choose another file; addressed members read model-chosen corrections on current or next turns before completing work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a concrete shared-file collision produces a refusal naming the holder and a required adjustment, supported by working member messages and enforced future claim state; this is more specific than a team chat API existing.
- Evidence: [claim rejection and holder feedback](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-chat.ts#L310-L344), [claim visibility in next turn](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-chat.ts#L519-L530), [lead assignment/targeted correction](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-instructions.ts#L1-L9), [live provider-specific delivery limits](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/docs/team-live-steering.md#L7-L46).
- Basis: structural.
- Confidence: medium-high for function-specific first-party mechanism and model response channels; actual model conflict resolution is unmeasured.
- Caveats: claims are advisory to tool behavior, not OS sandbox enforcement of all edits; a provider accepting a message does not prove a model obeyed it.

## S3 — Inside-and-now control

- State: —
- Function: no separate, whole-cell discretionary current-control owner with an accountable resource/commitment bargain established beyond task delegation and S2 adjustments.
- Disturbance / variety regulated: team capacity, active-run delays, task dependencies, model/permission changes, provider crashes and worktree conflicts.
- Decisive decision or feedback right: the lead decides which specific task to delegate or correct inside the assigned user objective, while scheduling priority, provider slots and recovery fences are algorithmic; operator can stop, queue or steer selected members.
- Decision owner: task lead model for local S1/S2 delegation, deterministic TeamScheduler/TeamCoordinator for gating, and human for user corrections; no separately demonstrated portfolio-wide executive.
- Supporting / enforcement mechanisms: `team_status`, SQLite team journal, actor transition tables, priority scheduler, capacity limit, cancellation and recovery, UI status.
- Closure path: routine work progress and failures become result/queue/stop or directed task correction; not a whole-system discretionary allocation choice over current competing commitments returned to a portfolio.
- Why this is / is not agent-owned: team leads coordinate deliverables and choose subtasks, but no shown independent whole-team executive mandate over resources or priority conflicts beyond delegated task scope; a configurable concurrent-agent limit is enforcement, not judgment.
- Evidence: [team controller and scheduler](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/ARCHITECTURE.md#L78-L94), [fixed scheduling priorities](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/team-scheduling-priority.ts), [live steering and capacity behavior](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/docs/team-live-steering.md#L53-L63).
- Basis: structural.
- Confidence: medium at the one-user-team recursion.
- Caveats: model-led within-task priority decisions are not asserted as autonomous S3; a distinct supervising host/enterprise layer could implement S3 externally.

### Absence scope

- Surfaces inspected: team coordinator/turn scheduling, hierarchical assignments, human team UI, active steering/stop, permission modes and recovery.
- Plausible first-party paths checked: model lead status and planning, concurrency controls, task assignments, operator reprioritization, per-member correction and publication approval.
- Why no material first-party path remains: the observed discretion is scoped to S1 task choice or S2 interference correction; no demonstrated whole-cell executive takes a current portfolio view and returns an accountable resource/priority decision distinct from those loops.

## S3* — Complementary audit

- State: A
- Function: independently inspect implementation claims and actual source changes through a separately selected reviewer-agent/Orcling mode, retaining review findings for correction.
- Disturbance / variety regulated: a builder's unverified completion, hidden code defects, unsound changes, failures to satisfy explicit human review comments or overconfident success reports.
- Decisive decision or feedback right: reviewer model/agent can inspect project code and diff and author review critique; user or team receives it, and implementation agent can revise with selected feedback.
- Decision owner: a distinct configured reviewer CLI model/Orcling role; the user remains authoritative over actual GitHub review submission/approval where configured.
- Supporting / enforcement mechanisms: real Git worktree/diff, source line-comment editor, reviewed-comment delivery with immutable selection IDs, separate team member sessions and GitHub reviewer-app submission with explicit approve privilege toggle.
- Closure path: implementation/source diff → independent reviewer session/model criticism → line-level findings/selected feedback → returned builder/lead work and reinspection; terminal publication stays user-owned.
- Boundary reachability: built-in task/team review and Orcling PR review are supported operating modes; a reviewer with its own provider/session can be selected without writing custom framework code.
- Why this is / is not agent-owned: the reviewer model makes semantic critiques against actual source evidence, while the app validates comment routing and the human controls final posting/merge authority.
- Claim being audited: code and task artifacts from another model/worker satisfy a requested change and leave no blocking issues.
- Ordinary reporting path: implementer completion narrative and team task result/events.
- Complementary access path: source diff/project worktree inspection and reviewer-owned pass over selected changed code plus attached test/review comments; not only the implementing model's self-report.
- Independence boundary: different provider/model seat or Orcling session from the writer, access to actual code files and Git diff; however assignment review may be configured by user and is not universal/default, and test results are not independently rerun by OpenOrc for every review.
- Who acts on findings: review comments are stored and can be explicitly forwarded to the executing team/worker for a later turn; operator retains approval, commit, push and PR publication.
- Evidence: [README review mode](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/README.md#L30-L46), [task review feedback reactivation tests](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/team-task-activation.test.ts#L217-L319), [separate reviewer source access and outputs](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/team-runtime-routing.test.ts#L1343-L1392), [Orcling PR review mode](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/docs/orclings.md#L24-L38).
- Basis: structural.
- Confidence: medium for optional structural audit topology; substantive audit efficacy not measured.
- Caveats: generic human read-only diff UI is not itself an agent-owned audit; S3* positive is the separately executed model reviewer path, not mandatory human code review.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported future-environment intelligence option that alters the operating organization after consultation with current control.
- Disturbance / variety regulated: remembered project decisions, new model/provider capabilities, outside project info and roadmap requests; these enter local task context or developer updates.
- Decisive decision or feedback right: task agents can search/plan on a user request, and project memory records lessons; none is given continuing future-adaptation authority over OpenOrc's own capabilities.
- Decision owner: developer/owner evolves the application; task models own software requests; memory extraction is context maintenance.
- Supporting / enforcement mechanisms: project memory, search, backlog tasks, skill/provider settings, release updater and roadmap.
- Closure path: history/lessons → retrieval on a later task or maintainer idea; no prospective environmental model/option → S3/adaptation authority → implemented capability change is wired into running OpenOrc.
- Why this is / is not agent-owned: cross-task memory and new ideas are not by themselves S4, even if they influence later S1 coding work.
- Evidence: [README project memory/usage](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/README.md#L35-L42), [core architecture and memory seams](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/ARCHITECTURE.md#L23-L55), [product task scope](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/PRODUCT.md#L7-L15).
- Basis: structural.
- Confidence: medium-high for supported modes.
- Caveats: external developer/governance choices and agent-coded feature upgrades are adjacent to the local runtime organization.

### Absence scope

- Surfaces inspected: project memory/extraction, tasks/backlog, provider discovery, Orcling continuity, team reports, roadmap and update surfaces.
- Plausible first-party paths checked: learning project decisions, multi-model discussion, research/plan mode, retained model memories and app updates.
- Why no material first-party path remains: these are context, user task or maintainer publication channels; no shipped, organizationally authorized prospective adaptation option closes back into current capability management.

## S5 — Policy and identity

- State: P
- Function: preserve legitimate local parent authority over the identity and ultimate behavioral/permission ceiling of a persistent Orcling companion across contexts and sessions.
- Disturbance / variety regulated: competing contexts, changes in name/persona/model, unauthorized strengthening of permission, drift in identity instructions or memory, and guest role reuse across projects.
- Decisive decision or feedback right: the human owner creates/edits/restores the Orcling's name, instructions and permission cap, while the Orcling may propose/update its instruction version subject to the owner's ability to override it.
- Decision owner: the local user as parent of the persistent companion; model may author revisions to subordinate instructions but cannot raise owner permission ceiling.
- Supporting / enforcement mechanisms: versioned `orcling_instructions`, local `orclings` identity rows, `Approve`/`Allow` ceiling, user edit/restore UI, Orcling brief injection at new run and guest/session partition.
- Closure path: an identity/permission issue → user updates/restores Orcling dossier or permission → persisted authoritative version and ceiling → next run/role prompt carries updated identity and stricter permission governs operations across tasks.
- Boundary reachability: Orclings are shipped as personal agents and optional team/review seats with actual persistent identity records, rather than future roadmap claims; profile editing restores versioned instructions through first-party UI/tooling.
- Why this is / is not agent-owned: the model can rewrite subordinate instructions, but the ultimate owner has a runtime-editable and enforceable authority path over what the agent is allowed to be/do; only P is established for ultimate identity.
- Identity / ultimate-policy issue: what kind of continuing companion it is, its name/role/permissions and maximum outward action rights as it moves between project/workspace/Slack/PR contexts.
- Ultimate authority in each claimed mode: human who edits the profile and chooses the more restrictive permission; external vendor model cannot unilaterally weaken this ceiling.
- Return-to-operation path: current identity/instructions/permission read into prompt on each process start, including team seats; owner changes persist and govern the next operation rather than simply recording static documentation.
- Evidence: [Orcling identity and user restoration](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/docs/orclings.md#L1-L22), [cross-context prompt propagation](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/docs/orclings.md#L23-L48), [permission ceiling](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/docs/orclings.md#L53-L64), [first-party Orcling service](https://github.com/davejj1530/openorc/blob/85bf1c5e4c81000911d8a5a90e23dbb7cf869283/packages/core/src/services/orclings.ts).
- Basis: structural.
- Confidence: medium-high for shipped parent identity path; live identity compliance not measured.
- Caveats: parent closure is local to a user's own Orcling; routine individual task approval and user Git publication are not credited as S5, nor is institutional OSS governance.

## Distributed OSS parent arrangement

OpenOrc is open-source and every user can run separate local desktop agents without shared task data. The evidenced parent governance in S5 is local human ownership of one persistent Orcling; it does not imply project-wide policy consensus or distributed higher recursion.

## Self-hosted and non-human modes

The local desktop and its native provider adapters keep credentials, tasks and memories on the user's computer. Team model members have scoped S1/S2 choice rights, while the user decides plan-to-act transitions and external Git publication. A self-modifying Orcling instruction path does not independently prove autonomous ultimate S5 because human permission/name/restore remain final.

## Recursion

A team hierarchy contains lead, manager, workers and optional reviewers. Nested task assignment, worktree independence and provider sessions alone do not demonstrate autonomous viability at every layer. This mapping credits one local team/cell and describes broader GitHub or OpenOrc maintenance as adjacent systems.

## Variety and escalation

Model agents absorb software variety; scoped file claims, directed messages and isolated workspace merging address cross-unit conflicts; optional independent reviewer models challenge code changes. Human messages may enter live provider turns or queue depending on adapter and actual acceptance, and safe recovery retains ambiguous deliveries rather than resending blindly. Fixed capacity, deadlines and permission ceilings constrain operations, while operator review remains authoritative for external side effects.

## Evidence gaps

- No live provider-backed Codex/Claude/OpenCode team was executed in this environment. Source and maintainer-described beta mode, including scripted tests, support structural paths but not empirical coordination or audit efficacy.
- Native test dependencies were not installed; project requests Node 24 and pnpm 11; no full `pnpm test` was run. Test source is used as corroboration, not a PASS claim.
- S2 credits a model-chosen response to a specific file-claim disturbance. The claim does not imply OS-level locking of arbitrary writes or perfect observance of team instructions.
- S3* is optional model reviewer with direct source access and feedback return; no universal independent audit stage or automatically trustworthy PR review is asserted.
- S5 P is limited to the user/Orcling continuing identity mode, not general plan approval, GitHub merge or public maintainer governance.
