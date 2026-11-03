---
harness_id: friday
project_name: Friday
repository: https://github.com/splashxmoon/friday
review_ref: 7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Friday

## Review boundary

- System in focus: one locally operated, first-party Friday session or Crew room organizing multiple coding agents through its shipped runner, shared task board, agent mesh, worktree/session state, review/check and budget controls.
- Purpose and identity: turn human-stated repository or workspace goals into shared coding-agent work with controlled assignment, coordination, peer checking, recoverable handoff and explicit human publication control.
- Relevant environment: a local Git repository, tasks, changing source files, CLI provider usage limits, cross-agent file collisions, tests, run errors, PR outcomes, operator permission choices and human feedback.
- Standard-distribution boundary: the MIT local Friday app, its TypeScript `src/agent-mesh.ts`, `src/runner/`, `src/teammates.ts`, `src/goal.ts`, `src/team-selfrun.ts`, `src/team-budget.ts`, `src/routing.ts`, `src/route-learning.ts`, `src/team-skills.ts`, associated state/store, and its provided agent-facing instructions. The hosted Friday Team/Pro service is not assessed.
- Credited operating / distribution surfaces: Code sessions with multiple external CLI agents; Crew room with a model-driven lead and task board; explicitly enabled self-run toward an operator goal; optional separate model-driven reviewer; locally configured smart routing, usage handoff and checks. The actual choice of tool/model is installation-dependent.
- Adjacent first-party surfaces excluded from ownership: provider vendors' own CLI/internal planning tools, their API safety/usage policies, GitHub approval and branch protection, Friday's developer release governance, hosted Friday Team orchestration and any user's separate management organization.
- Recursion level: one local Friday work organization; individual agent lanes are operational units, not imported complete viable systems from their provider implementations.
- Frozen source revision: `7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a` (`splashxmoon/friday`). Observation date 2026-11-03; Profile 0.2.4 and released assessment Methodology 0.3.7.

## Repository architecture

Friday operates a local server and desktop UI over session/event state. It launches already authenticated coding CLIs, or its separately configured Friday Code runner, in agent lanes associated with the same project; worktrees can isolate file edits. A lead agent receives `assign_task`, `post_tasks`, `manage_task` and, in Crew, `steer_agent`. Friday's agent mesh retains a finite, dependency-checked board, allocates ready work among available agent lanes, notifies peers about owned/held files, runs configured checks after completion, and gives a different agent the work and evidence for review. Failed checks or review are fed to the original worker within a bounded retry count. A human can reassign, retry, send back or cancel tasks and has the final say before commit/PR publication. Local routing considers usage windows and observed task outcomes, while running work remains delegated to provider CLI models.

Pinned first-party evidence:

- [README: how Friday runs agents, boards, review and human sign-off](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/README.md)
- [Agent mesh: role tools, lead assignment and task lifecycle](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/src/agent-mesh.ts)
- [Local runner and CLI handoff](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/src/runner/runner.ts)
- [Crew teammate roles, access and tool fallback](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/src/teammates.ts)
- [Self-run goal, lead decisions and stop limits](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/src/team-selfrun.ts)
- [Session-level goal evidence and model judge](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/src/goal.ts)
- [Usage/token and working-hour budget controls](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/src/team-budget.ts)
- [Task-fit routing and usage-weighted selection](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/src/routing.ts)
- [Outcome-based route learning](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/src/route-learning.ts)
- [Reusable Crew skill proposal and human acceptance](https://github.com/splashxmoon/friday/blob/7db025c6513eae1c05a93f6e7ba58fd5ffad2a2a/src/team-skills.ts)

## Operational model

An operator names a goal or assigns a task and grants tool access. The first-party mesh lets a designated lead model make substantive current-work allocation and correction decisions, while worker models choose implementation steps through their external CLI executors. Deterministic custody and permission gates constrain those actions. Distinct peer lanes can negotiate conflicts or audit a finished task, but a deterministic fallback is not itself an independent agent. Evidence of an owned S3 current-control actor comes specifically from the first-party-managed model-driven lead using `post_tasks`, `manage_task` and `steer_agent` to govern the board; the runner merely enforces its authorized actions. Friday's future-looking routing estimates and saved learning are not promoted into organization-wide S4 strategy without a distinct prospective capability decision loop.

## S1 — Operations

- State: A
- Function: transform an operator's work objective into code, tests, documents or other concrete repository artifacts and correct defects according to tool/source feedback.
- Disturbance / variety regulated: ambiguous requirements, codebase differences, unexpected test results and task-local implementation choices.
- Decisive decision or feedback right: the assigned model-driven lane chooses substantive implementation/tool calls, interprets outcomes and revises its own artifact before reporting completion.
- Decision owner: a Friday-managed coding-agent lane invoking its configured external Claude Code, Codex, other CLI or Friday Code model; not the UI, deterministic task allocator or model vendor's unrelated organization.
- Supporting / enforcement mechanisms: session state, local CLI adapter and worktree, role instructions, checkpoints, task board, test runner, manual permission mode and event history.
- Closure path: human/lead task → owned lane executes substantive model/tool steps → workspace and check feedback → revised files/report → task complete or returned for rework.
- Boundary reachability: README standard Code and Crew paths, `src/runner/runner.ts` run/turn interface, `src/agent-mesh.ts` assign/claim/finish and `src/teammates.ts` role handoff are shipped first-party integration paths.
- Why this is / is not agent-owned: removing the model-driven lane leaves only launch, log and gate code; that code cannot determine source-specific implementation by itself.
- Evidence: pinned README, `src/runner/runner.ts`, `src/agent-mesh.ts`, `src/teammates.ts`.
- Basis: explicit + structural.
- Confidence: high for owned role and executable paths, not for every vendor CLI combination's observed quality.
- Caveats: provider CLI agents and models remain external execution dependencies; their internal agent hierarchies are not attributed to Friday.

## S2 — Coordination

- State: C
- Function: attenuate interference among simultaneously editing worker lanes by assigning file custody and returning conflict warnings to the agent before further edits.
- Disturbance / variety regulated: two otherwise independent agent lanes claiming or editing the same file, incompatible interface changes and stale board/task ownership.
- Decisive decision or feedback right: accept non-overlapping `claim_files` paths; reject claims already owned by other lanes; on a conflicting diff, instruct the colliding worker to stop editing and consult or wait for the holder.
- Decision owner: constructor-defined Friday mesh claim/ownership checks; subsequent peer negotiation is by task actors, not evidence of a dedicated autonomous S2 policy authority.
- Supporting / enforcement mechanisms: `files.held`, `files.released`, board `owns` sets, `heldBy`, `onDiff`, agent messages and wake events.
- Closure path: first lane holds path → second lane claims or changes it → Friday identifies holder and refuses claim or warns the violator → second lane must stop and coordinate or wait before continuing.
- Boundary reachability: agent-visible `claim_files` and `release_files` tools and automatic `onDiff` are part of shipped `src/agent-mesh.ts` integration.
- Why this is / is not agent-owned: the coordination relation reaches worker behavior, but collision arbitration is a prewritten deterministic rule; peer dialogue alone does not prove an independent S2 agent making the binding priority policy.
- Distinct S1 units: independent Friday-managed coding-agent lanes working in the same session/repository.
- Inter-S1 disturbance: conflicting writes/claims to the same source path or a board-owned file.
- Attenuating coordination relation: ownership claim, refused second claim and holder-specific warning on changed files.
- Feedback into subsequent S1 behaviour: collision message explicitly directs the second worker to stop changing the file, ask the owner, or wait for release.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it detects and returns a concrete cross-worker collision, rather than merely listing agents or assigning tasks.
- Evidence: pinned `src/agent-mesh.ts` (`holdFiles`, `releaseFiles`, `onDiff`, `heldBy`) and README team-worktree instructions.
- Basis: structural.
- Confidence: high for the implemented narrow path.
- Caveats: collision warning and cooperative file claiming are advisory; no proof that arbitrary external tools cannot violate the instructions or that the entire repository has transactional file locks.

## S3 — Inside-and-now control

- State: A
- Function: an authorized lead agent manages present board commitments, assignment, current blocked work, reallocation and completion under an operator's goal.
- Disturbance / variety regulated: stalled team progress, uneven available capacity, failed checks/review, agents running out of usage, inconsistent task progress and unclear priorities across active lanes.
- Decisive decision or feedback right: the designated lead model can autonomously create/decompose a board, assign work, steer or stop a teammate in Crew mode, cancel/retry/reassign blocked tasks, inspect reports and decide the next current step.
- Decision owner: the configured first-party-managed lead agent inside a Friday Code/Crew session; Friday enforces role permissions, and the human owner still has higher-level intervention rights.
- Supporting / enforcement mechanisms: guarded `post_tasks`, `assign_task`, `manage_task`, `steer_agent`; dependency/cycle checks, finite board, event projection, current budget/usage signals, deterministic dispatch, retries and lead reports.
- Closure path: goal/current workload and progress evidence → lead model posts or adjusts the board/steers worker → Friday dispatches its authorized decision → reports/tests/usage/blocks return to lead → lead revises assignments or calls for remediation.
- Boundary reachability: `src/agent-mesh.ts` offers board management to the lead and reserves steering to `state.lead`; `src/team-selfrun.ts` explicitly tells an enabled autonomous lead to choose the next valuable tasks, hand them out, decide open questions, and stop only at goal completion/budget/stall.
- Why this is / is not agent-owned: current-work authority is not only deterministic queue management; an explicitly designated model-driven lead can choose and alter task partition and reprioritization through role-gated tools. This positive state requires the supported lead/Crew path, not passive solo-agent UI mode.
- Whole-system current view: one session/room's board statuses, owners, checks, message reports, agent availability, usage limits and budget, bounded by the human's goal.
- Current-control decision scope: board admission and redistribution, teammate redirection and when to try/stop/rework; not a demonstrated corporate-level resource or identity authority.
- Evidence: pinned `src/agent-mesh.ts` (`manageTask`, `postTasks`, `control`, `steer`, `round`, `reportBoard`) and `src/team-selfrun.ts`; README Crew path.
- Basis: explicit + structural.
- Confidence: medium-high for first-party-owned agent lead control mode.
- Caveats: whether the chosen provider model actually exercises that discretion well is not observed; deterministic budgets and automated selection are C components within this A ownership claim.

## S3* — Complementary audit

- State: A
- Function: ask a separate model-driven reviewer to challenge a worker's own completion claim against its actual artifacts, task requirements and recorded proof, and return necessary corrections before board completion.
- Disturbance / variety regulated: unverified self-reported completion, missed requirements and defects not caught by the worker's own tests.
- Decisive decision or feedback right: a different available reviewer lane reads another agent's task, report, proof and diff/source and returns a substantive approval or correction verdict.
- Decision owner: the independently assigned model-driven reviewer lane, distinct from the task's implementing lane. Friday's check runner and verdict parser are support/gates rather than the substantive audit judge.
- Supporting / enforcement mechanisms: `reviewOrPass`, different-lane `pickReviewer`, `awayDiff`, proof/changes handoff, `board.reviewed`, bounded `rework`, configured tests, optional model-based `goalRequest` judge.
- Closure path: worker reports finished task + actual diff/proof → Friday runs its checks → if eligible, separate reviewer sees task and evidence → reviewer decides pass or correction → failed verdict sends defects back to worker and repeats review, or terminal escalation after rework bound.
- Boundary reachability: the standard multi-agent board review path `src/agent-mesh.ts` dispatches to a lane other than `t.lane`; `onRunEnded` records its verdict, and `rework` returns rejected findings. A separate task goal judge is available under `src/goal.ts`.
- Why this is / is not agent-owned: in the supported second-review path, the reviewer model reads changed artifacts and makes a case-specific challenge that code cannot predefine. Automatic checks alone, a UI read-only panel, and an operator's final review are not counted as autonomous S3*.
- Claim being audited: a specific assigned board task is correctly finished and fits acceptance/requirements.
- Ordinary reporting path: implementing lane's completion report, test commands and worktree changes.
- Complementary access path: Friday presents the other reviewer source/worktree or the recorded diff and task proof, with independent reviewer instructions and test receipts rather than merely trusting the author's summary.
- Independence boundary: different agent lane, not guaranteed different model vendor or fully isolated model context; source access depends on whether the reviewer runs on the same machine or receives a recorded diff.
- Who acts on findings: mesh sends failed verdict and concrete instructions back to the original task lane for bounded repair; successful review unlocks dependent tasks.
- Evidence: pinned `src/agent-mesh.ts` (`runChecks`, `reviewOrPass`, `pickReviewer`, `round`, `boardRunEnded`, `rework`, `awayDiff`), `src/team-proof.ts`, `src/goal.ts`.
- Basis: explicit + structural.
- Confidence: medium-high in configured multi-agent second-review mode.
- Caveats: Friday deliberately skips cross-review for qualifying small changes with real passing tests, no changed files or unavailable alternate reviewer; thus S3*=A is conditional, not universal. Vendor/model or context independence is not proven beyond different lanes and evidence paths.

## S4 — Outside-and-then intelligence

- State: —
- Function: no demonstrated first-party decision loop that turns anticipated external developments into changes of the Friday work organization's future mission/capability envelope.
- Disturbance / variety regulated: changed tool limits, learned model effectiveness, later repo errors and new scheduled tasks are sensed, but the cited response is route optimization or current execution within existing permissions.
- Decisive decision or feedback right: model/tool selection, replayed lessons and human-accepted reusable skills do not by themselves constitute durable first-party prospective-capability choice.
- Decision owner: constructor-defined scoring rules and human skill approver for the observed adaptation mechanisms; no bounded autonomous Friday S4 organizational actor identified.
- Supporting / enforcement mechanisms: `route-learning` feedback grades, model benchmark priors, `routing.ts` choice, Crew skill proposals and human acceptance, memory/automation setup.
- Closure path: observed test/review feedback → model-fit estimate/current routing or proposed skill → later present task; no environmental forecast and S4 option evaluation leading to an authorized changed future organizational capability is shown.
- Why this is / is not agent-owned: a feedback-driven heuristic and task-level learning are not enough to assign future-facing organization intelligence; even autonomous self-run leads act on the current user goal and board.
- Evidence: pinned `src/route-learning.ts`, `src/routing.ts`, `src/team-skills.ts`, `src/team-selfrun.ts`, README memory/automation sections.
- Basis: bounded absence.
- Confidence: medium.
- Caveats: this is not a denial of ordinary learning, future-oriented user projects, or the possibility that a parent organization uses Friday as its S4 tool.

### Absence scope

- Surfaces inspected: local routing/learned grades, repeated-error repo memory and check suggestions, saved skills, Crew automations, self-run goal, team planning and public README roadmap-like feature descriptions.
- Plausible first-party paths checked: future skill/capability evolution via agent suggestion; operational model routing via measured outcomes; autonomous Crew goals and scheduled dependency/code-change tasks as a proxy for S4.
- Why no material first-party path remains: learned model scores alter bounded tool allocation, while proposed procedures require human approval and autonomous goals are externally specified; none closes a prospective environmental assessment and new harness-wide future capability/mandate through an autonomous authority.

## S5 — Policy and identity

- State: —
- Function: no supported ultimate-identity or constitutional-policy adjudication loop for a Friday installation was found.
- Disturbance / variety regulated: access modes, permissions, publishing authority, spending/usage bounds and goal text arrive as user-set constraints or constructor safeguards rather than deliberated organization policy.
- Decisive decision or feedback right: the person establishes the goal, access level, budgets, and final commit/PR/deployment approval; model-driven workers cannot legitimize a change of identity or waive these user boundaries.
- Decision owner: external local user/owner and platform permission constraints; no first-party S5 policy-maker with a demonstrated return to the running organization.
- Supporting / enforcement mechanisms: Crew read/ask/full permissions, `src/team-budget.ts`, approval events, self-run prohibitions on default-branch push/deployment/data deletion/spending, manual final review.
- Closure path: human chooses constraints → Friday enforces them during tasks → agent operates in the bounded space; no question of ultimate mission/identity is assessed by an S5 authority and promulgated as a legitimate new policy.
- Why this is / is not agent-owned: an autonomous lead controlling *work* is S3, not by itself a constitutional S5, and static access/approval settings are control tools rather than a policy arbitration loop.
- Evidence: pinned README human review/Crew settings, `src/teammates.ts`, `src/team-selfrun.ts`, `src/team-budget.ts`, `src/runner/runner.ts`.
- Basis: bounded absence.
- Confidence: medium-high.
- Caveats: a human operator or organization may exercise S5 outside the shipped runtime; such parent authority is not silently imported.

### Absence scope

- Surfaces inspected: teammate access and credentials, local-only account boundary, self-run run/stop and permissions, manual reviews, automation setup and budgets, human goal/lead selection.
- Plausible first-party paths checked: autonomous lead as ultimate authority; self-run choosing every question; default branch/deployment safeguards as policy; saved skills or repository preferences as identity evolution.
- Why no material first-party path remains: these are per-task executive choices, permissions, or externally set fixed rules; there is no source-supported distinct ultimate-policy issue, legitimate adjudicator and returned constitutional decision for the Friday work organization.

## Distributed OSS parent arrangement

Different people install and run independent Friday instances with their own goals, models, credentials and filesystem access. Friday's maintainers may revise software and a local human may set or change task policy, but those facts do not prove one first-party distributed S5 authority common to deployments. Hosted Friday Team is deliberately outside this OSS assessment.

## Recursion

The assessed recursion is one local work session/Crew room containing multiple operating model-driven lanes. A lead lane can close present-control decisions and a distinct reviewer lane can audit another lane's results. The provider CLI's internal recursion, GitHub corporate governance and human user's wider company are not assumed to be nested first-party Friday management functions.

## Variety and escalation

Friday attenuates variety through task partition, role-lane ownership and advisory file holds, then resolves operating surprises through model-driven workers. Current workload is monitored through task/usage/test results and actively adjusted by a lead in supported Crew mode; separate peer review challenges self-reported correctness. Failed tests/review return to the doer for bounded retries; exhausted tasks and unsafe publishing decisions escalate to the human. Outcome-based model routing and saved memory are not conflated with prospective organizational strategy or ultimate policy.

## Evidence gaps

- Frozen source and its first-party code/docs were inspected; no live model-provider run, production team session or external repository publishing transaction was executed for this assessment.
- Agent-owned S3 requires the authorized lead to act through shipped task/steer tools; a sole human-moderated Code session with no lead does not have the same autonomous control path.
- Independent S3* challenge depends on an actual second reviewer lane; Friday explicitly bypasses it for some checked small changes or when no separate reviewer exists.
- S2 file collision handling is an advisory mechanism with cross-lane feedback, not verified OS-level/transactional enforcement across arbitrary CLI edits.
- Route learning and skill suggestions are acknowledged but not upgraded to S4 without a prospective capability-change decision closure; no S5 parent organization is assumed.

## Assessment summary

Proposed included, bounded to the shipped multi-agent/Crew paths: **A · C · A · A · — · —**. Model-driven worker lanes own S1; first-party file ownership/conflict feedback closes a narrow constructor S2; authorized model-driven lead tools close current-work S3; a genuinely different model-driven reviewer can challenge completion evidence for S3*. Model routing, saved lessons, human-set permissions and final publication approval do not independently establish first-party S4 or S5.
