---
harness_id: pi-foreman
project_name: pi-foreman
repository: https://github.com/Shredi/pi-foreman
review_ref: 8f8c473cc2332602373d03850d4826eea2f79f51
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# pi-foreman

## Review boundary

- System in focus: the installed pi-foreman extension and its integrated Pi coding-agent crew carrying out work in a repository, including its foreman, builder/explorer/reviewer roles, first-party ceremony, permission and review gates, and optional human checkpoints.
- Purpose and identity: turn a coding session into supervised, bounded work units with reviewable artifacts and a controlled finish/PR path.
- Relevant environment: user tasks, changing repository source/tests, model/tool output, git worktrees, optional other sessions and remote developer infrastructure.
- Standard-distribution boundary: the installable pi-foreman package, bundled role agent definitions, Pi extension adapter, CLI scripts, default feature profiles and pinned pi-subagents/intercom integration. Pi and third-party model internals are execution dependencies, not separately donated organizational functions.
- Credited operating / distribution surfaces: `extensions/core-adapter/`, `agents/`, `docs/ceremony.md`, `docs/review.md`, `docs/safety.md`, `scripts/foreman_session.py`, and installed Pi-session subagent integration.
- Adjacent first-party surfaces excluded from ownership: project contributor CI, tests as development proof only, benchmark rig not necessarily present at runtime, remote Herdr administration and external source repositories. Optional model-run reviews are credited only where the package binds their raw-input access and corrective return.
- First-party operating / deployment modes considered: default interactive foreman with builder and reviewer, trivial fast path, heavy plan with user checkpoint, autonomous subordinate session, optional multi-session/worktree and remote handoff, headless/print mode.
- Recursion level: one foreman-coordinated coding task/crew; opening another pi-foreman session can repeat the pattern but is not a complete recursively viable independent business.
- Reviewed revision: `8f8c473cc2332602373d03850d4826eea2f79f51`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

pi-foreman is a Pi coding-agent extension, not a standalone model. The foreman receives a user task, records a tier and a task ledger, launches model-backed explorer/builder/reviewer roles through pi-subagents and watches their results. TypeScript hooks enforce read, tool, shell/git, launch, review and finish rules; Python utilities keep task session, traces and retrospective records. A standard task normally needs a completed builder and reviewer verdict; a heavy task additionally routes the reviewed plan through a human checkpoint before its builder can start. All function grades below belong to these installed agent modes, not to static gates alone.

Pinned first-party evidence: [README](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/README.md), [ceremony](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/ceremony.md), [review protocol](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/review.md), [safety](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/safety.md), [retro](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/retro.md).

## Operational model

The foreman is a discretionary model-backed owner of task decomposition/current-control decisions; builder subagents edit and test bounded repository artifacts in their own scoped checkout; reviewer subagents separately inspect those artifacts and return item/head-bound findings and verdicts. Hard gates (PR reviewed-head, prohibited operations, checkpoint approval hash) are safety enforcement, not autonomous cognition. The top-level human can direct the task and, on heavy plans, exercises an explicit non-delegable approval right.

## S1 — Operations

- State: A
- Function: model-backed builder agents execute variable repository coding tasks, inspect/test their changes and return artifacts to the foreman.
- Disturbance / variety regulated: source state, unexpected errors, requested behavior, tests and revision instructions.
- Decisive decision or feedback right: select concrete code edits and tests within a delegated ledger item, then revise after failed review.
- Decision owner: configured Pi subagent builder model, acting through the package's role definition and scoped tool runtime.
- Supporting / enforcement mechanisms: Pi tools, run binding, role model maps, per-role permissions, git and shell guards, launch/read budgets.
- Closure path: foreman launches builder with item/brief, builder changes code/tests and reports, review returns findings, builder can perform corrective revision.
- Boundary reachability: standard install explicitly provisions the builder role and the foreman's launch mechanism; user asks for a task, not a custom role integration.
- Why this is / is not agent-owned: builders choose coding actions in a wired model/tool session; guards constrain them without owning the coding decisions.
- Evidence: [role protocol](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/roles.md), [ceremony](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/ceremony.md), [launch binding](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/extensions/core-adapter/ceremony.ts).
- Basis: structural.
- Confidence: high.
- Caveats: code execution was not benchmarked in this review; the trivial path may omit reviewer by its bounded exception.

## S2 — Coordination

- State: C
- Function: attenuate accidental shared-checkout collisions when multiple operational builders/sessions use related repository work.
- Disturbance / variety regulated: concurrent writers may change the same working tree or push from unauthorized session/branch.
- Decisive decision or feedback right: worktree/session binding and guard refuse a child write/push outside its owned checkout; the foreman can compose a different task/worktree and sequence follow-up.
- Decision owner: deterministic gate and worktree ownership checks; any choice to split conflicting tasks or coordinate a new branch remains with foreman/human composition.
- Supporting / enforcement mechanisms: per-launch worktrees, child-bound `cwd`, shell-write guard, git push/branch ownership and session handoff metadata.
- Closure path: a prohibited operation is refused with a reason; the foreman may give the builder an owned worktree or serialize the conflicting edit, then retry the changed task.
- Boundary reachability: worktree launching and guards are shipped first-party options on top of directly integrated child roles.
- Why this is / is not agent-owned: a function-specific guard prevents concrete shared-resource interference, but dynamic multi-builder conflict negotiation and repair do not have an installed autonomous S2 owner.
- Distinct S1 units: separate builder agents or full pi-foreman child sessions operating in parallel.
- Inter-S1 disturbance: a non-owning child trying to change a checkout or push a branch while another session works there.
- Attenuating coordination relation: owned-worktree isolation and per-session branch/checkout checks, with explicit refusal.
- Feedback into subsequent S1 behaviour: refusal directs a model/human to a permitted checkout or rescheduling; no automatic agent-side conflict mediation is guaranteed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the checks enforce particular cross-agent write/checkout contention, beyond message transport or generic task ordering.
- Evidence: [worktree session setup](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/sessions.md), [worktree boundary](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/extensions/core-adapter/ownworktree.ts), [safety](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/safety.md).
- Basis: structural.
- Confidence: medium.
- Caveats: no general merge-conflict resolution or automatic global scheduling is established; the session registry explicitly lacks a transaction lock.

## S3 — Inside-and-now control

- State: A(P)
- Function: convert current user task to scoped ledger commitments, choose helper roles and tiers, review progress, authorize iteration and close the task only after required evidence.
- Disturbance / variety regulated: overlarge/unverified changes, blocked child work, missing tests, stale reviews and non-aligned PRs.
- Decisive decision or feedback right: foreman chooses task decomposition/launch/revision and can issue corrected work; in a heavy plan mode the human can veto or approve the precise reviewed plan hash before execution.
- Decision owner: the foreman agent in normal mode; the owner at the explicit heavy-plan checkpoint, under a separate parent intervention rather than an agent approval.
- Supporting / enforcement mechanisms: tier ledger, plan/revision counters, finish gate, reviewer marks, model ladder, checkpoint hash, PR head validation.
- Closure path: foreman receives child completions/verdicts, updates ledger and launches revisions; exact review gates constrain finish. Heavy mode first returns plan to owner and only an approved version opens builder launch.
- Boundary reachability: standard installed foreman protocol and role extensions include both the autonomous current-control path and the explicit human checkpoint tool.
- Why this is / is not agent-owned: the model chooses plans/assignments/revisions; deterministic checks enforce minimum ceremony. Heavy-plan release is intentionally and demonstrably human-owned.
- Whole-system current view: task ledger, active child runs, reviewer findings, cost/session state and bound current plan.
- Current-control decision scope: task tier, delegated item ownership/ordering, revision requests, review closure and completion.
- Evidence: [ceremony and checkpoint](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/ceremony.md), [current-control gate](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/extensions/core-adapter/ceremony.ts), [plan review](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/extensions/core-adapter/planreview.ts).
- Basis: structural.
- Confidence: high.
- Caveats: a default task has no human checkpoint, and a gate is not itself discretionary S3. Incomplete-review escape after repeated refusals is explicit and visible.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Foreman model | new item, child result or failed review | choose assignment/revision/finish, record ledger state and return action to builder | [ceremony](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/ceremony.md) |
| Parent (`P`) | Legitimate human task owner | heavy-plan checkpoint after review | approve exact plan hash, reject or request revision; only approved plan opens builder gate | [heavy checkpoint](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/ceremony.md) |

## S3* — Complementary audit

- State: A
- Function: a separate read-only reviewer agent examines raw builder changes/tests against ledger scope and returns findings/verification before a PR.
- Disturbance / variety regulated: a builder may incorrectly declare a work item done, introduce regressions or miss required tests.
- Decisive decision or feedback right: reviewer reports per-item PASS/FAIL and located findings from diff/source/test inspection; review gate requires current valid PASS for PR and ordinary standard completion.
- Decision owner: the distinct reviewer subagent with independent read-only access to repository artifacts and ledger; foreman acts on the verdict.
- Supporting / enforcement mechanisms: reviewer role deny-write tool set, ledger scope injection, different-model rule where available, head-bound review records, re-review item list and PR guard.
- Closure path: reviewer receives independently sourced code/diff context, returns item findings/verdict; foreman delegates correction; rerun review validates changed head; guard returns pass/fail to promotion.
- Boundary reachability: installed reviewer role is part of standard required ceremony and the PR gate, not just a suggested external review service.
- Why this is / is not agent-owned: a separate model-backed child observes direct operational artifacts rather than relying solely on builder's claimed completion, and its findings return through an actual corrective gate.
- Claim being audited: builder's ledger-item completion and correctness of modified repository artifacts.
- Ordinary reporting path: builder's completion message and foreman's ledger.
- Complementary access path: distinct reviewer tool session inspecting raw checkout/diff/tests under its own read-only role, with scoped ledger injected.
- Independence boundary: role and run separated from builder, its write tools denied; reviewer model differs from foreman when available, but a distinct model from builder is not absolutely guaranteed.
- Who acts on findings: foreman requests builder revision; head-aware review/PR gate blocks promotion until valid verdict (subject to documented finish exceptions).
- Evidence: [review protocol](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/review.md), [review marks](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/extensions/core-adapter/reviewmarks.ts), [git/PR guard](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/safety.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: reviewing the same model family weakens cognitive independence, no guarantee of a successful audit outcome or fully independent external organization; trivial bounded tasks need not launch reviewer.

## S4 — Outside-and-then intelligence

- State: —
- Function: no standard first-party loop from external future environment evidence to prospective capability choices and returned current-control adaptation was established.
- Disturbance / variety regulated: tool/provider shifts or future project demands could need adaptation, but the shipped system mostly reacts to current tasks and internal process friction.
- Decisive decision or feedback right: no dedicated externally sensing prospective planner chooses future options and feeds an adaptation decision into S3.
- Decision owner: owner can change role models and policies, and the foreman may record retro hints, but neither is an evidenced installed S4 function.
- Supporting / enforcement mechanisms: `/retro` summaries, trace-based permission-map proposals, model ladder/presets, cost/bench metrics.
- Closure path: `/retro` proposes permission rules and warns that the owner must apply them manually; no grounded outside/future option-to-adapt loop is wired by default.
- Why this is / is not agent-owned: retrospective telemetry and model selection optimize present workflow from past self-traces, not a distinct prospective environmental intelligence function.
- Evidence: [retrospective boundary](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/retro.md), [design/architecture](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/design/architecture.md).
- Basis: structural.
- Confidence: medium.
- Caveats: a user may explicitly ask the foreman for research/future strategy, but generic model capacity does not establish the distributed S4 contract.

### Absence scope

- Surfaces inspected: architecture, ceremony, roles, retro, session/bench docs, extension state and model-ladder controls.
- Plausible first-party paths checked: retro permission suggestions, model rung changes, plan-review, benchmark results, future ledger items and optional remote sessions.
- Why no material first-party path remains: each is internal trace tuning, present-work review or configurable model mapping rather than a distinct outside-and-then sensing, future option and S3-return closure.

## S5 — Policy and identity

- State: —
- Function: package exposes human authorization and configuration preferences but no organizational identity/ultimate-policy deliberation and authoritative return procedure.
- Disturbance / variety regulated: sensitive operations, protected branches, secrets and child permissions require safety constraints, not necessarily a whole-organization ethos dispute.
- Decisive decision or feedback right: human decides asks/plan approval and sets permission policy, but no installed S5-specific identity issue or legitimate policy forum processes such issues.
- Decision owner: human owner and deterministic safety gate exercise task/security authority, not an evidenced separate S5 policy identity loop.
- Supporting / enforcement mechanisms: permission whitelist, hard floors, protected-file ownership, heavy checkpoint and child-ask flows.
- Closure path: a decision to allow/deny a tool or approve a plan affects current execution; no S5 issue -> identity policy resolution -> returned organizational governance path is packaged.
- Why this is / is not agent-owned: human involvement is not automatically S5, nor does a role policy and permissions file itself express the VSM identity-policy function.
- Evidence: [permissions](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/permissions.md), [safety](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/safety.md), [checkpoint](https://github.com/Shredi/pi-foreman/blob/8f8c473cc2332602373d03850d4826eea2f79f51/docs/ceremony.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: site-level organizational rules can be installed via overlays, but those are not a first-party ultimate-policy loop by themselves.

### Absence scope

- Surfaces inspected: permission and configuration layers, checkpoint flow, hierarchy/session model, model ladder, architecture and safety controls.
- Plausible first-party paths checked: owner approval, model role policy, package permissions baseline, organizational overlays and project protected-file stewardship.
- Why no material first-party path remains: these govern allowed task actions and current risk, without an explicit highest-policy identity issue and legitimate decision/return mechanism.

## Distributed OSS parent arrangement

The upstream project has maintainers and CI, but those external contributors are not the deployed foreman crew's S3/S4/S5 parents. The user is the legitimate task parent for heavy checkpoint mode; no independent installed S5 governance body is inferred.

## Self-hosted and non-human modes

The extension runs on the user's Pi session. A configured provider/model is required for agent ownership; in a headless run requiring human approval, the documented gate fails closed rather than silently inventing permission. Optional other sessions can run on other machines, subject to trust and credentials, without becoming independent VSM policy authorities.

## Recursion

A foreman may open another foreman session and delegate a scoped branch/task, repeating a current-control pattern. No evidence establishes complete S1–S5 recursion at every nested level.

## Variety and escalation

Tier triage, model ladder and ledger attenuate task complexity; autonomous builders/reviewers amplify response capacity. Review FAILs and blocked checkpoint/permission asks return corrective information to foreman or owner. These current-control and audit paths should not be conflated with external-future S4 or ultimate-policy S5.

## Evidence gaps

- Assessment is source-structural at the pinned SHA, not an end-to-end provider-run experiment.
- S2's worktree isolation is function-specific but static; mediation between competing writers is not autonomous by default.
- S3* is a structurally independent role and direct inspection path, with weaker model-level independence when role models coincide; trivial mode can bypass review within a constrained diffscan floor.
