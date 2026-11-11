---
harness_id: orchi
project_name: Orchi
repository: https://github.com/adamentwistle/orchi-build
review_ref: db5a720ad7cccfd579e26b7ced7a1bbdcf586306
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Orchi

## Review boundary

- System in focus: installed macOS Orchi configuration, Herdr interface mods, shipped Claude Code slash commands/skills, orchestration helpers, legwork/ticket adapters and switchboard paths for one project or several watched projects.
- Purpose and identity: plan project work from an operator's legwork roadmap/tickets, spawn concurrent coding agents, review PRs and keep human decisions/recovery visible.
- Relevant environment: code repositories, changing tasks/roadmaps, GitHub/Linear/Markdown tickets, external model agents, CI/PR results, usage limits and live human steering.
- Credited operating / distribution surfaces: [`/fanout` skill](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/fanout/SKILL.md), [`/pr-review` loop](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/commands/pr-review.md), [`/switchboard` skill](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/switchboard/SKILL.md), `skills/switchboard-protocol/`, `bin/herdr`, `bin/switchboard-*`, `bin/usage-*`, Orchi panels and configured ticket inputs.
- Adjacent first-party surfaces excluded from ownership: unconfigured third-party Herdr/Claude/Codex and their internals; `legwork` as an independent tracker, Cursor Bugbot provider internals, upstream GitHub/Linear authority, installer/theme/demo artifacts, and this repository's development/test CI.
- First-party operating/deployment modes: invoked `/fanout` unattended run for a legwork project, operator-requested switchboard supervising Claude Code project orchestrators, optional independent PR review via Bugbot or Claude Code's `/code-review`, manual Herdr panes.
- Recursion level: a legwork-defined project composed of several coding work units; the cross-project switchboard may operate at the next enclosing level and is not automatically a second S1.
- Reviewed revision: `db5a720ad7cccfd579e26b7ced7a1bbdcf586306` (2026-11-11), primary-source static; no macOS Herdr/Claude model session or external GitHub publication was executed for this assessment.
- Generated Profile/Methodology: 0.2.4 / 0.3.8; active Profile/Methodology: 0.2.4 / 0.3.8.

## Repository architecture

Orchi is not itself a model engine: it installs Herdr-oriented panels, scripts and first-party Claude Code instructions that launch and supervise external model-backed coding sessions. `/fanout` reads a project's legwork Vision, Next Prompt, roadmap/log, current PRs, repo gate and reviewer state; it makes a task plan, decides parallel/serial dependencies, launches workers, validates PRs and sends rebasing/fix instructions. A switchboard session watches multiple live project orchestrators and passes user decisions via durable files/scripts. A separate PR-review loop requests code/diff scrutiny and returns findings to fix workers. [README](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/README.md), [fanout implementation contract](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/fanout/SKILL.md), [Herdr bridge](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/herdr/SKILL.md).

## Operational model

- The operator authorizes the project, supplies Vision and tasks and chooses whether merge is permitted. The Orchi-launched orchestrator owns bounded task slicing, scheduling, worker instructions, failure resolution and PR readiness within those constraints.
- Distinct coding workers act through live panes or delegated model agents; Orchi's control-plane uses project tracker and PR/CI results as feedback rather than treating agent text as final proof.
- The switchboard routes genuine parent decisions and persists status; a deterministic watchdog only checks liveness and must not be credited with discretionary organizational judgment.

## S1 — Operations

- State: A
- Function: implement and verify bounded software tasks in separate coding-agent work units.
- Disturbance / variety regulated: evolving issue requirements, code state, test failures, review findings and tool output.
- Decisive decision or feedback right: choose edits, testing, fixes and PR contents within a worker brief; the orchestrator also changes briefs after findings.
- Decision owner: first-party-launched Claude Code/Codex coding agents operating through Herdr panes or subagent routes; external model inference is not confused with independent Orchi organizational authority.
- Supporting / enforcement mechanisms: worktrees, Herdr `agent prompt`, git/gh CLI, gate commands, worker briefs, pane lifecycle and review notifications.
- Closure path: legwork task → orchestrator brief → model worker edits/tests → PR and gate result → review finding or completion → corrective prompt or accepted PR.
- Boundary reachability: standard `/fanout` command dispatches agents in an installed Orchi/Herdr environment using the shipped skill; real third-party agent accounts and dependencies must be configured.
- Why this is / is not agent-owned: worker model chooses implementation and corrective actions; deterministic worktree setup and shell commands carry them.
- Evidence: [fanout task briefs and dispatch](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/fanout/SKILL.md), [Herdr agent controls](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/herdr/SKILL.md), [user-facing commands](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/README.md).
- Basis: explicit operational skill and adapter wiring.
- Confidence: medium-high for shipped agent mode; no live paid-model confirmation here.
- Caveats: real merge rights and approvals remain external; `fanout` without `--merge` prepares open review-ready PRs, not auto-merges.

## S2 — Coordination

- State: A
- Function: prevent incompatible concurrent coding work units from producing cross-branch/file conflicts and reconcile their results.
- Disturbance / variety regulated: overlapping edit scope, PR dependency ordering and newly merged main invalidating sibling branches.
- Decisive decision or feedback right: choose concurrent versus sequential dispatch from task scope and serialize uncertain overlaps, then redirect sibling workers for rebase/conflict repair when main changes.
- Decision owner: model-backed project orchestrator executing the first-party `/fanout` decisions, not just a fixed global semaphore.
- Supporting / enforcement mechanisms: worktree isolation, explicit dependency markers, PR refs, gate reruns, rebase/fix prompts, `worker_limit` and usage-guard.
- Distinct S1 units: independent coding agents assigned to separate PR-sized project tasks/worktrees.
- Inter-S1 disturbance: agents can independently change shared files or depend on an ancestor branch that another agent just merged.
- Attenuating coordination relation: the planner marks tasks `parallel` only for disjoint paths/packages and otherwise `after <task>`; after merges, sibling workers receive a mandatory current-main reconciliation instruction.
- Feedback into subsequent S1 behaviour: affected workers merge current main, repair conflicts, rerun gates and re-review before their PR can be accepted.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation names the actual intersecting-work and stale-branch disturbance and changes worker execution to attenuate it; not merely a mailbox or task list.
- Closure path: competing task scopes/merge event → orchestrator serial/parallel or rebase decision → changed worker instructions → new branch/gate result → further adjustment.
- Boundary reachability: `/fanout` runs this decision procedure in its ordinary multi-worker mode; manual single-worker sessions alone would not demonstrate it.
- Why this is / is not agent-owned: orchestrator evaluates overlap and remedies from live task/PR facts; scripts and worktrees enforce the chosen route.
- Evidence: [fanout planning and post-merge sibling handling](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/fanout/SKILL.md), [Herdr worktree API](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/herdr/SKILL.md).
- Basis: explicit disturbance and correction path.
- Confidence: medium-high structurally; no concurrent PR trace was replayed.
- Caveats: actual risk depends on model obedience and repository scope; worker-count cap alone is not the S2 evidence.

## S3 — Inside-and-now control

- State: A
- Function: regulate current delivery commitments, worker assignments, status and operational bottlenecks for a whole project run.
- Disturbance / variety regulated: failed checks/reviews, blocked workers, active PR dependencies, usage cap, outstanding task scope and current resource availability.
- Decisive decision or feedback right: choose work packages, order, routing/model, worker follow-up, blocked/skip/fix outcomes and when work is ready to close.
- Decision owner: `/fanout` orchestrator model within the project; optional switchboard monitors multiple project orchestrators at a higher recursion and relays reserved human choices.
- Supporting / enforcement mechanisms: legwork `fanout-state.md` progress board, repo gate, open PR list, bugbot status, worker panes, switchboard status/wait, usage guard.
- Whole-system current view: orchestrator loads the full project roadmap and recent log, current open PRs and gate, plus a run-wide worker table with progress/status; switchboard aggregates live project orchestrators and outstanding decisions.
- Current-control decision scope: independently plan/dispatch/reprioritize PR-sized tasks, recover blocked workers, fix review findings and preserve handoff state.
- Closure path: project state + current PR/agent results → orchestrator scheduling/repair decision → worker dispatch or new brief → status/PR updates → run state and project `/wrap`.
- Boundary reachability: regular `/fanout` path provides this system-wide state and decision right; switchboard is separate opt-in oversight, not required for the claim.
- Why this is / is not agent-owned: model chooses and changes commitments; deterministic health watcher and usage counter cannot make those selections by themselves.
- Evidence: [fanout load/plan/dispatch/land/cleanup](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/fanout/SKILL.md), [switchboard state and check-in](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/switchboard/SKILL.md), [README panels](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/README.md).
- Basis: structurally wired autonomous present-control mode.
- Confidence: medium-high.
- Caveats: unconfigured Herdr/Claude accounts and model fallibility limit realized results; no live run audited.

## S3* — Complementary audit

- State: A
- Function: inspect proposed PR code changes separately from worker completion reports and feed correctness concerns into repairs.
- Disturbance / variety regulated: builder mistakes and false confidence despite successful local self-reported tests.
- Decisive decision or feedback right: model reviewer reports real actionable findings or a clean verdict for a specific PR head; orchestrator accepts/rejects findings and orders fixes.
- Decision owner: independently invoked Cursor Bugbot when enabled for the repo; otherwise the shipped fallback delegates a code-review pass to Claude Code's `/code-review` skill. Provider/reviewer internals are external.
- Supporting / enforcement mechanisms: `bugbot-wait` post-trigger result, GitHub inline comments and review time, code review fallback, repeated tests and three-round bound.
- Claim being audited: the coding worker's PR is correct, safe and review-clean.
- Ordinary reporting path: worker's PR body, completed gate line and self-reported results.
- Complementary access path: review service reads submitted PR code/diff and independently reports inline faults; the orchestrator opens flagged file/line and tests fix decisions.
- Independence boundary: Bugbot is an external reviewer login distinct from the submitting worker; `/code-review` fallback is an agent review path but independent vendor/provider identity is not guaranteed. Do not infer an impartial institution from a shared model account.
- Who acts on findings: orchestrator/fix worker patches real findings, reruns gate, republishes and requests a new review; unresolved findings block the clean end state.
- Closure path: submitted PR → separate reviewer → findings/clean verdict → orchestrator correction and rerun → next review round or blocked result.
- Boundary reachability: shipped `/pr-review` command runs before clean PR is accepted in ordinary `/fanout`; Bugbot-mode availability depends on GitHub repo setup, fallback is defined for other repos.
- Why this is / is not agent-owned: evaluative code findings arise from model reviewer judgment, while `bugbot-wait` and loops just trigger, convey and enforce the result.
- Evidence: [PR review command](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/commands/pr-review.md), [fanout review/repair loop](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/fanout/SKILL.md), [bugbot polling tool](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/bin/bugbot-wait).
- Basis: explicit separate reviewer and corrective loop, optional external integrations.
- Confidence: medium for actually independent review, high for wired repair mechanics.
- Caveats: model reviewer independence in `/code-review` fallback is not validated directly; missing review answer times out rather than being considered clean.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party autonomous or parent-closed prospective environment-to-strategy adaptation circuit established for Orchi's future capabilities.
- Disturbance / variety regulated: external tickets, roadmap additions and changing product needs can be consumed as work, but no separate foresight/adaptation decision path is shown.
- Decisive decision or feedback right: `/fanout` decides how to deliver the operator's existing priorities now; it does not select future positioning or invent an external-environment adaptation program.
- Decision owner: user/maintainer may change the legwork roadmap outside the assessed installed harness; no demonstrated S4 actor within it.
- Supporting / enforcement mechanisms: ticket list, GitHub/Linear adapters, legwork Vision/Next Prompt/Roadmap inputs and task planner.
- Closure path: a user-supplied roadmap item enters the current PR task plan; that is S3/S1 task delivery, not yet a first-party prospective S4 circuit.
- Why this is / is not agent-owned: model work decomposition of already-authorized backlog does not alone establish outside-and-then option generation.
- Evidence: [README ticket sources](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/README.md), [fanout load/plan](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/fanout/SKILL.md).
- Basis: bounded no-path.
- Confidence: medium; a configured organization could add separate long-horizon strategy outside this boundary.
- Caveats: a future-oriented roadmap is real input but does not by itself prove strategic adaptation ownership.

### Absence scope

- Surfaces inspected: ticket adapters, legwork tracker processing, `/fanout` plan, `/switchboard` and `/pr-review` modes.
- Plausible first-party paths checked: ticket ingestion, roadmap planning, human Vision, PR gate feedback and model research delegated to workers.
- Why no material first-party path remains: these paths act on an already-selected task/roadmap, without a distinct environment-sensing → prospective option → adaptation authority → changed future capability loop.

## S5 — Policy and identity

- State: P
- Function: preserve the operator's authoritative project identity and ultimate constraints while delegating ordinary work to coding agents.
- Disturbance / variety regulated: pressure to execute/merge work contrary to the legwork project's Vision, human-required credentials, blocked status or reserved outward-facing merge authority.
- Decisive decision or feedback right: define and revise the project's Vision and bounded work/merge mandate, including whether an unattended run may merge outward-facing PRs.
- Decision owner: legitimate local human project operator who authors the legwork Vision, selects projects/tickets and grants `--merge` or withholds it; orchestrator cannot unilaterally obtain that merge mandate.
- Supporting / enforcement mechanisms: tracker `## Vision`, project `blocked_on`, `## Next prompt`, worker briefs, default no-merge, switchboard `DECISION` / `ACTION` handoff and explicit answers.
- Identity / ultimate-policy issue: which project the agent team serves and what future work falls inside that mission, distinct from ordinary approval of a single command.
- Ultimate authority in each claimed mode: operator owns project Vision and outward-publication authority; the orchestrator's task choices are subordinate to that policy in installed `/fanout` mode.
- Return-to-operation path: operator's tracker Vision/blocked status and merge selection → `/fanout` reads at startup → task brief, stop condition and merge permission → agent operation/PR outcome; switchboard relays reserved human policy decisions to project orchestrators.
- Closure path: local parent updates project Vision/mandate → subsequent run loads it → current worker constraints and publication behavior change, retaining the parent's authority.
- Boundary reachability: shipped `/fanout` requires a legwork project with `Vision` and explicitly respects `blocked_on`, human-required steps and default no-merge; its own inputs are available in supported installed mode.
- Why this is / is not agent-owned: autonomous orchestrator may select ordinary implementation priorities but not rewrite the operator's ultimate purpose or grant itself outward publishing rights.
- Evidence: [fanout project Vision and blocked/merge gates](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/fanout/SKILL.md), [switchboard decision relays](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/skills/switchboard/SKILL.md), [legwork requirement](https://github.com/adamentwistle/orchi-build/blob/db5a720ad7cccfd579e26b7ced7a1bbdcf586306/README.md).
- Basis: operational parent-governed local project mission/mandate return path.
- Confidence: medium; whether a specific Vision document contains actual identity-level claims depends on deployment, but the first-party format/path is explicit.
- Caveats: only local project/operator S5 is claimed, not distributed Orchi OSS governance; ordinary per-task tool approvals are not treated as S5.

## Distributed OSS parent arrangement

No first-party evidence is asserted for a distributed maintainer S5 over the upstream `orchi-build` project. `P` concerns the local operator's legwork project identity.

## Self-hosted and non-human modes

Most work is model-mediated, but project selection, account credentials, deferred decisions and default external merge authority remain human. A watchdog can restart a crashed switchboard; that is deterministic recovery, not an autonomous S5 decision.

## Recursion

Individual coding workers are project S1; `/fanout` coordinates their S2/S3. A multi-project switchboard is an enclosing current-control level, so evidence for its global supervision is not automatically assigned to each individual project cell.

## Variety and escalation

Task briefs, disjoint-scope scheduling, worktrees, review rounds, usage guard, budget, explicit `blocked_on` and default no-merge attenuate variety; unresolved credentials/permissions or human-only decisions remain barriers even in unattended mode.

## Evidence gaps

- Source-static only, no installed macOS Herdr/Claude session, actual parallel edits, Bugbot response or GitHub merge tested.
- S3* fallback `/code-review` depends on external Claude Code behavior; same-provider independence is not claimed.
- `P` is scoped to operator-owned project Vision/mandate, not automatically to the Orchi package maintainers' identity or wider OSS organization.
