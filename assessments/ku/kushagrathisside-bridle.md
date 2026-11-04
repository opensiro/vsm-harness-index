---
harness_id: kushagrathisside-bridle
project_name: Bridle
repository: https://github.com/kushagrathisside/bridle
review_ref: 9b9b9f868c18958a921b6967fcd7d64acde877fc
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Bridle (kushagrathisside)

## Review boundary

- System in focus: The native-Windows Bridle coding agent with local-model chat, Rust tool/policy runtime, project board and sequential model-operated team members.
- Purpose and identity: Perform developer coding tasks through model-directed tool use under enforced local policy; support model-driven planning, execution and review of shared project issues.
- Relevant environment: Workspace and Git state, local llama.cpp server, tool outcomes, team-role work assignments, dependency blockers, developer intervention, secret files and optional web sources.
- Standard-distribution boundary: First-party Tauri desktop, harness CLI/core/runtime, board, model-facing team tools, machine roster, optional OpenCode hook. Team members use the same local model one at a time.
- Credited operating / distribution surfaces: [agent runtime](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/chat.rs), [desktop member runner](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/bridle-desktop/src/crew_cmd.rs), [board tools/permissions](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/board_tools.rs), [board store](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/board.rs), [roster/role prompts](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/crew.rs), [policy](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-core/src/security/tool_policy.rs).
- Adjacent first-party surfaces excluded from ownership: Planned parallel worktrees/multi-model fleet, test/eval harness, build/release process, maintainer governance and browser/mock-server fixtures; they do not own live project-team control.
- First-party operating / deployment modes considered: Direct coding chat, OpenCode shim, tagged team board runs, PM model splitting issues into dependency-linked engineering/QA work, QA review, human board interventions and roster editing.
- Recursion level: One local project/team with distinct role-scoped model S1 turns and a shared current-work portfolio; team member processes are serialized, not parallel workers.
- Reviewed revision: 9b9b9f868c18958a921b6967fcd7d64acde877fc.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Bridle's desktop/CLI runs a locally served model through a tool loop with file, Git, shell and verification tools. Path, secret, shell and per-tool policy blocks unsafe calls and redacts returns. The desktop adds named PM, engineering, research and QA members; tagging creates a project-board issue. Each member has its own role prompt and conversation, receives real model-callable board tools, and works from a claimed issue. Board events are checksummed; issue keys avoid duplicates; blocked dependencies, status transitions, claim guards and one project-wide Git run lock regulate work. Run checkpoints give human per-issue undo. Lead models can plan interdependent issues and reassign or change statuses, while QA models have direct read/test tools and review rights. All members share the same main model and worktree, executing serially. [README](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/README.md), [team guide](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/docs/guide/team-and-board.md), [runner](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/bridle-desktop/src/crew_cmd.rs).

## Operational model

Each acting team member is a distinct model/tool operational S1 session with its own issue, role and model decisions. A lead model can inspect the overall board, make a multi-issue plan and change current commitments. Deterministic claim/run guards avoid duplicate issues and concurrent same-project edits; those gates do not own adaptive agent coordination. An independently prompted QA role can inspect actual code/tests and send work back instead of trusting an engineer's self-report. Human board assignments, statuses and stop/restart are a separately closed parent current-control mode. Roster editing and security settings are task/staffing configuration, not evidenced ultimate-policy S5.

## S1 — Operations

- State: A
- Function: Iterative model-led code edits, repository investigation and verification for a user or board issue.
- Disturbance / variety regulated: Unknown project state, errors, failed checks, insufficient implementation and user-requested changes.
- Decisive decision or feedback right: Choose the next file/tool call, edit and follow-up based on returned evidence.
- Decision owner: Chat model or the currently active role-specific member model session.
- Supporting / enforcement mechanisms: Agent::run_turn, tools server, file/command/Git tools, tool policy, llama.cpp provider, turn bounds and per-member context.
- Closure path: Prompt or issue → model decides tool call → policy checks → execution result returns → model revises code or completes/updates board.
- Boundary reachability: Agent::for_member constructs the working model/tool agent; desktop run_issue supplies real member tools, issue brief and chat job.
- Why this is / is not agent-owned: Static policy and persistence cannot select which code change actually solves the task.
- Evidence: [agent loop](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/chat.rs), [member-run wiring](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/bridle-desktop/src/crew_cmd.rs).
- Basis: explicit + structural.
- Confidence: high for wired model/tool loop.
- Caveats: Windows-only deployment verified by author on one machine; no live provider task run reproduced in this review.

## S2 — Coordination

- State: C
- Function: Avoid competing project issue claims and overlapping shared-workspace member runs.
- Disturbance / variety regulated: Duplicate issue creation, duplicate claim/retry and conflicting same-project file mutations by distinct members.
- Distinct S1 units: Independently prompted PM, engineering and QA model turns, serial on one provider rather than simultaneous models.
- Inter-S1 disturbance: Two members can try to claim the same card or re-create a task, or act on shared files with unfinished earlier edits.
- Attenuating coordination relation: BoardStore atomic claim/status gate, stable issue-key deduplication, dependency/ready checks and one project RunGuard lock.
- Feedback into subsequent S1 behaviour: board_create reports Already exists with the issue id; invalid claims report existing status/assignee; subsequent models read changed ready/blocked board and comments.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The checks prevent concrete duplicate ownership and mutually interfering access, returning a conflict-sensitive outcome to affected agent turns.
- Decisive decision or feedback right: Determine claim winner/reject duplicate or exclusive project-run admission. No model-owned adaptive S2 conflict policy is shipped.
- Decision owner: Deterministic first-party BoardStore/RunGuard constructor path and fixed operator/developer rules; models choose issues but do not own the exclusion algorithm.
- Supporting / enforcement mechanisms: Exclusive board locks, claim preconditions, issue-key collision checks, dependency gates, run lock and Git checkpoints.
- Closure path: Repeated/competing issue or member-run attempt → duplicate/claim/lock verdict → member receives error/current board state → only eligible next work proceeds.
- Boundary reachability: Model-callable board_create/claim are injected into actual member agent; desktop run_issue takes project lock and board claim before starting a model turn.
- Why this is / is not agent-owned: The same coordination gates operate without model discretion; technical-manager advice to avoid touching the same files is not enforced file leasing.
- Evidence: [board implementation](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/board.rs), [board tools](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/board_tools.rs), [run recovery/lock](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/docs/reference/run-recovery.md).
- Basis: explicit + structural.
- Confidence: medium-high for this bounded S2 constructor.
- Caveats: No fine-grained path leases, parallel worktree model agents, global conflict negotiation or dynamic model ownership of the lock rule.

## S3 — Inside-and-now control

- State: A(P)
- Function: Manage the current multi-member issue portfolio: resources, priorities, dependencies, review and interventions.
- Disturbance / variety regulated: Wrong owner, failed task, blocked review, unbalanced workload or stalled work chain.
- Whole-system current view: board_list/show expose all issue statuses, priorities, owners, blockers and comments to lead model; desktop board shows all current work and member load to human.
- Current-control decision scope: Lead model can create multi-step plans, choose assignments, dependencies and priorities, reassign existing issues or change status; human can assign, hold, return, rerun or stop work.
- Decisive decision or feedback right: Model lead chooses/revises active team commitments; in optional parent mode human directly changes current assignments/states or interrupts a run.
- Decision owner: Base A — role-scoped lead model. Parent P — human desktop operator. Board and runner enforce each decision.
- Supporting / enforcement mechanisms: board_plan, lead board_update reassignment/status, board overview, ready priority queue, dependency solver and operator actions.
- Closure path: Base: model surveys board → creates/updates cross-member commitments → store records choices → next members see new ready/blocked assignments. Parent: human inspects board/runner → assigns, moves, holds or stops → upcoming turns obey updated board.
- Boundary reachability: The shipped member runner injects board tools with lead privileges; desktop board commands edit the same BoardStore and control active turns.
- Why this is / is not agent-owned: The base plan and follow-up status choices are discretionary model decisions, whereas the UI is a separately evidenced human control mode; the ready queue alone is not an owner.
- Evidence: [lead tool permissions and plan](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/board_tools.rs), [member runner and UI changes](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/bridle-desktop/src/crew_cmd.rs), [guide](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/docs/guide/team-and-board.md).
- Basis: explicit + structural.
- Confidence: medium-high for reachable rights, not model decision success rates.
- Caveats: Team model roles are simulated with one model, in serial, and upstream says PM outcomes are weakly measured.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model lead | Current board/issue state calls for reallocation | Model board_plan/update changes dependencies, assignee or status used by later turns | [board tools](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/board_tools.rs) |
| Parent (`P`) | Human operator | Sees blocked/incorrect live project work | UI changes owner/status/runner state; next run uses corrected board | [desktop commands](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/bridle-desktop/src/crew_cmd.rs) |

## S3* — Complementary audit

- State: A
- Function: Independently check an engineer's reported completion against repository source and test reality through a separate QA role.
- Disturbance / variety regulated: A worker's done/in_review claim can hide incomplete, invalid or unverified changes.
- Claim being audited: Engineering issue completion according to acceptance criteria.
- Ordinary reporting path: Engineer's board_comment, status and answer, plus runner-generated changed-files note.
- Complementary access path: QA member directly reads actual files, Git diffs and runs project checks with standard tools, beyond the worker's own report.
- Independence boundary: QA is another prompted member with its own model conversation and tools; model weights, repository and policy are shared, not independent institutional evidence.
- Who acts on findings: QA lead/tester model can flag failed acceptance, send an in_review issue to ready or create a corrective bug issue; a lead may close reviewed work.
- Decisive decision or feedback right: QA agent makes its own evidence-based accept/reject judgment and changes review status or follow-up obligations.
- Decision owner: The model acting in the separately instantiated QA member, not the worker whose claims are under test.
- Supporting / enforcement mechanisms: QA role prompts, independent member session, read/test/Git tools, QA board_update rights and acceptance/dependency fields.
- Closure path: Engineer reports work → QA issue ready or original card in review → separate QA model reads raw files/tests → judges results → corrective board_update/rework affects future engineering and S3 choices.
- Boundary reachability: Shipped roster includes QA lead/tester; PM can create a dependent QA task, and desktop run_issue initializes the QA member with file/test and board tools. QA status rights explicitly allow review return.
- Why this is / is not agent-owned: A QA model chooses whether observed source satisfies criteria and what corrective card/status to emit; test commands only supply evidence.
- Evidence: [QA personas](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/crew.rs), [QA review rights](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/board_tools.rs), [separate member execution](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/bridle-desktop/src/crew_cmd.rs).
- Basis: structural + documented team review scenario.
- Confidence: medium; no live adversarial QA finding reproduced.
- Caveats: QA is not mandatory for each work item, and accepting a worker's text without checking raw evidence would not exercise S3*. This is logical role separation, not an external auditor.

## S4 — Outside-and-then intelligence

- State: —
- Function: No independently closed external/prospective option-development and capability-return loop.
- Disturbance / variety regulated: New tools/models, evolving dependencies and changing external requirements might necessitate adaptation; existing roles handle assigned work.
- Decisive decision or feedback right: Evaluate future environmental options and implement a changed present capability; no such model decision/return pipeline is wired.
- Decision owner: User manually changes models, web settings and project design; model researcher responds to current tickets.
- Supporting / enforcement mechanisms: Research team prompt, optional web tools, multiple manually chosen model slots, ideas queue and unbuilt fleet roadmap.
- Closure path: Research can produce a ticket answer or an idea another ticket may use, but no standard future-oriented strategic loop governs current operating structure.
- Why this is / is not agent-owned: Research role, temporal storage and roadmap features are not proof of prospective organizational adaptation.
- Evidence: [roles](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/crew.rs), [team limits](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/docs/guide/team-and-board.md), [README status](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/README.md).
- Basis: explicit + structural.
- Confidence: medium-high within shipped mode.
- Caveats: A human can request a future-planning issue, but such task compliance would not establish the ongoing metasystem function.

### Absence scope

- Surfaces inspected: Role prompts, board and ideas, web research, model slots, runtime/configuration, future fleet plan.
- Plausible first-party paths checked: Researcher changes operating policy, model upgrade, future-design backlog, web intelligence reconfiguring S3 and provider changes.
- Why no material first-party path remains: These are reactive tickets, manual options or unimplemented plans; no external-prospective option judgment returns to live capability.

## S5 — Policy and identity

- State: —
- Function: No runtime identity-level or ultimate-policy dilemma resolution loop with authorized decision return.
- Disturbance / variety regulated: Secret access, risky tools, member activation, role assignments and approval/security boundaries.
- Decisive decision or feedback right: Settle contested system mission or ultimate policy and enact that verdict for later operations; not installed.
- Decision owner: Human edits staffing/settings; code enforces pre-authored role and security limits; model members decide current tasks.
- Supporting / enforcement mechanisms: ToolPolicy, TeamStore in machine config, roster validation, role rights and human crew editor.
- Closure path: Operator changes roster/headcount or policy configuration and subsequent tasks use it; there is no separately evidenced identity-policy proposal, human constitutional judgment and returned governing choice.
- Why this is / is not agent-owned: A safety gate, role prompt and staffing UI bound routine tasks but do not give a model or a human a first-party runtime constitutional S5 loop.
- Evidence: [roster and role structure](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/harness-cli/src/crew.rs), [roster editor](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/crates/bridle-desktop/src/crew_cmd.rs), [security rules](https://github.com/kushagrathisside/bridle/blob/9b9b9f868c18958a921b6967fcd7d64acde877fc/docs/concepts/security.md).
- Basis: structural + explicit.
- Confidence: medium-high at the project-team boundary.
- Caveats: The user's legitimate project-governance rights and upstream maintainer governance exist outside this narrowly observed deployed mechanism.

### Absence scope

- Surfaces inspected: TeamStore, crew editor, lead status permissions, board UI, model and security config, policy hooks and upstream governance docs.
- Plausible first-party paths checked: Human membership edits, static policy allow/deny, PM requests, role hierarchy and external research/policy escalation.
- Why no material first-party path remains: Roster changes are personnel/current-work choices, and security bounds are static; no live identity-level disagreement and authoritative constitutional return path was found.

## Distributed OSS parent arrangement

Apache-2.0 public maintenance and releases do not automatically become an embedded S5 actor in each self-hosted Bridle run. The local human legitimately supervises current board assignments; that is the separately evidenced S3 parent mode.

## Self-hosted and non-human modes

Local llama.cpp supplies inference while optional web access is off by default. All named members are first-party model-operated sessions using the same model serially, with the operator able to reassign, stop and rerun. No parallel GPU team or autonomous multi-organization policy governor is installed.

## Recursion

Individual member work items are lower S1 task cells; the common project board and lead roles form the inspected whole. Nested child issue IDs and personnel names do not alone establish independent viable recursive organizations.

## Variety and escalation

LLM coding tools, role specialists and web options amplify task response variety. Policy denial, role checks, serial project lock, board dependencies, QA review, turn limits and recoverable Git checkpoints constrain it. Blocked tasks return to board/human attention, not by themselves to a constitutional S5 process.

## Evidence gaps

- Rust toolchain and native Windows desktop were unavailable to this reviewer; no pinned upstream build, UI or live local-model run was reproduced.
- S2 is limited to deterministic project conflict/duplicate attenuation, not parallel path leases or an agent-owned adaptive conflict policy.
- QA independence is logical separation by role/session on the same model and repository; an actual adversarial QA dispute was not reproduced and not every change receives QA.
- Upstream describes little empirical evidence for the simulated PM team's reliability. The states report source-backed rights/closure rather than success rates.

## Assessment verdict

Included: a first-party autonomous coding agent with model-run team roles, bounded deterministic cross-member coordination, dual model/human current board control and a distinct model-operated QA readback/rework path. No shipped closed S4 or S5 path established.
