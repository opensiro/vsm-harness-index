---
harness_id: oh-my-claudecode
project_name: oh-my-claudecode
repository: https://github.com/Yeachan-Heo/oh-my-claudecode
review_ref: 5281b19e0d64f8e6dc6767f2130299a88af2dc71
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# oh-my-claudecode

## Review boundary

- System in focus: the first-party `Yeachan-Heo/oh-my-claudecode` (OMC) multi-agent software-engineering runtime at frozen revision `5281b19e0d64f8e6dc6767f2130299a88af2dc71`, including bundled native Team, its lead/worker/reviewer contracts, Team state/runtime machinery, and bundled `self-improve` where they bear on organizational function.
- Purpose and identity: orchestrate model-backed software-engineering workers around a target repository, coordinate parallel work, regulate current team commitments, independently verify delivered changes, and in self-improve mode research and experimentally select improvements over repeated rounds.
- Relevant environment: target repositories and tests/builds; user task/acceptance criteria; worker liveness/progress; git/worktree conflicts; external documentation, papers, benchmarks and similar projects; model/provider availability; benchmark outcomes.
- Standard-distribution boundary: bundled OMC TypeScript runtime, Team skill/pipeline, shipped agent prompts, task/team state, worktree/merge support, verification/reviewer lanes and bundled self-improve skill are inside. Claude Code itself, model inference providers, optional external CLI providers, user repositories, web sources and benchmark commands are external dependencies/environment; they may supply execution or evidence but are not silently credited as OMC decision owners.
- Credited operating / distribution surfaces: `skills/team/SKILL.md`; `src/team/*`; `src/hooks/team-pipeline/*`; shipped `executor`, `verifier`, `security-reviewer` and `code-reviewer` contracts; bundled `skills/self-improve/*` and `/self-improve` dispatch.
- Adjacent first-party surfaces excluded from ownership: repository development tests/fixtures; release/installer maintenance; contributor governance; CI; historical agent fixtures; standalone examples; telemetry/notification plumbing where it only transports state; unrelated graph approval and merge-readiness utilities unless wired into a credited mode.
- First-party operating / deployment modes considered: native `/team` staged multi-agent execution with a model-backed lead and native workers; Team variants with MCP/tmux/worktree support where they corroborate current regulation/conflict handling; Team+Ralph where relevant to verification/retry; bundled autonomous `self-improve` after its setup/trust gate.
- Recursion level: one OMC software-engineering organization around a target repository. File/module-scoped worker agents are operational S1 units; the lead coordinates and regulates the current set; verifier/reviewer lanes audit worker output; self-improve research/planning supplies prospective adaptation. Individual tool calls, task-list rows and provider processes are not viable systems merely because they are concurrent.
- Reviewed revision: `5281b19e0d64f8e6dc6767f2130299a88af2dc71`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

OMC ships a model-facing orchestration layer rather than only static role prompts. Canonical Team decomposes a software task into file/module-scoped work, pre-assigns named workers, spawns them in parallel, persists stage/task state and requires a lead to monitor the whole team through messages and status snapshots. The lead can unblock, reassign, retry, skip, replace dead workers, alter dependency commitments and decide merge-conflict handling while deterministic runtime machinery persists and enforces those decisions.

Team is designed around concrete interference modes. Native Team lacks atomic claiming, so the shipped skill requires lead pre-assignment to avoid races; tasks are scoped to avoid file conflicts; optional worktrees isolate concurrent edits; merge/rebase conflict evidence is routed back to lead/worker, with the leader instructed to choose strategy. Current-control is separate: the lead monitors worker liveness/current tasks/team-wide counts/messages and can change current commitments when workers fail, stall, die or leave dependencies blocked.

Verification is structurally separated from production. The shipped `verifier` is read-only, prohibits self-approval, independently runs fresh tests/build/type diagnostics and checks original acceptance criteria after the authoring pass. Team verification can additionally route security-sensitive work to read-only `security-reviewer` and large/architectural changes to `code-reviewer`. Failed verification generates fix tasks and returns control to `team-fix`.

Bundled `self-improve` is an autonomous repeated adaptation mode after a user-defined setup gate. Every round runs a researcher over repository/history and, when useful, external papers, benchmarks, similar projects and official documentation; planners generate testable hypotheses; approved plans are implemented in isolated experiment worktrees and benchmarked; tournament logic re-benchmarks and merges a winner; the next round starts from that updated improvement branch and accumulated history.

Primary evidence:

- [`README.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md)
- [`skills/team/SKILL.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/team/SKILL.md)
- [`src/team/allocation-policy.ts`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/src/team/allocation-policy.ts)
- [`src/team/task-router.ts`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/src/team/task-router.ts)
- [`src/team/conflict-mailbox.ts`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/src/team/conflict-mailbox.ts)
- [`src/team/governance.ts`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/src/team/governance.ts)
- [`agents/verifier.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/agents/verifier.md)
- [`agents/security-reviewer.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/agents/security-reviewer.md)
- [`agents/code-reviewer.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/agents/code-reviewer.md)
- [`skills/self-improve/SKILL.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/self-improve/SKILL.md)
- [`skills/self-improve/si-researcher.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/self-improve/si-researcher.md)

## Operational model

In native Team the lead creates file/module-scoped subtasks/dependencies, pre-assigns owners, spawns model-backed workers and monitors progress. Workers inspect/edit/test their assigned repository scope and report completion/failure. The lead receives current task/liveness/messages across the set and changes assignments/commitments as exceptions arise. After execution, separate verifier/reviewer agents inspect actual repository evidence; failed verdicts create corrective work and loop back. In self-improve a higher-order research/planning/experiment loop proposes/tests candidate changes against a sealed benchmark, merges a verified winner and uses the resulting branch/history as the basis for the next round.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work on the target repository through autonomous file/module-scoped workers that inspect, edit, test and debug assigned outcomes.
- Disturbance / variety regulated: heterogeneous implementation/debugging/documentation/test tasks, source state, test/build failures, dependency constraints and repository feedback.
- Decisive decision or feedback right: within assigned scope, choose concrete inspection, edit, command, test and debugging actions needed to produce the requested software outcome.
- Decision owner: model-backed OMC worker agents such as `executor`, `debugger`, `designer`, `writer` and `test-engineer`.
- Supporting / enforcement mechanisms: Claude Code Agent/Task execution; OMC worker prompts; task ownership; shell/file tools; task state; optional worktrees; provider routing.
- Closure path: lead assigns bounded outcome → worker inspects repository and chooses actions → repository/test output returns → worker iterates to completion/failure → evidence returns to Team lead for verification/correction.
- Boundary reachability: native `/team` is canonical documented OMC runtime; `team-exec` explicitly spawns these workers and their results drive the pipeline.
- Why this is / is not agent-owned: removing model-backed workers leaves task/state/tool machinery but removes open-ended local engineering decisions.
- Evidence: [`skills/team/SKILL.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/team/SKILL.md); [`agents/executor.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/agents/executor.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Claude/model inference is externally provided, but OMC packages the role contracts and runtime path invoking those actors.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among concurrently operating workers through ownership/dependency decisions and conflict responses that return into worker behaviour.
- Disturbance / variety regulated: duplicate task claiming, overlapping file edits, dependency races, branch/worktree collisions and merge/rebase conflicts.
- Decisive decision or feedback right: choose task/file ownership/dependency ordering and, when collisions occur, decide which worker should own/retry/rebase/defer affected work or which merge strategy to take.
- Decision owner: the model-backed Team lead in native Team mode.
- Supporting / enforcement mechanisms: pre-assigned owners; `blockedBy`; file/module scoping; worktree isolation; conflict detection/mailboxes; task updates; worker messages; deterministic allocation helpers.
- Closure path: collision/race becomes visible → lead selects ownership/dependency/reassignment/conflict response → task/inbox/worktree state changes → affected workers follow revised assignment or resolve/defer collision → later evidence returns to lead.
- Boundary reachability: native Team instructs the lead to pre-assign owners, monitor concurrent workers, reassign work and handle conflict/failure cases as part of the bundled workflow.
- Why this is / is not agent-owned: deterministic worktree/mailbox/allocation mechanisms transport/enforce coordination, but native Team leaves substantive cross-worker ownership/retry/conflict choices to the lead model.
- Evidence: [`skills/team/SKILL.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/team/SKILL.md); [`src/team/conflict-mailbox.ts`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/src/team/conflict-mailbox.ts); [`src/team/allocation-policy.ts`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/src/team/allocation-policy.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: delegation/least-load routing alone is not the witness; the mapping relies on explicit race/file/merge disturbances plus lead-owned responses.
- Distinct S1 units: multiple simultaneously spawned Team workers, each owning a file/module-scoped software outcome and model/tool loop.
- Inter-S1 disturbance: Team explicitly records non-atomic claim races and bounded file ownership; worktree/merge support exposes concrete concurrent file and branch conflicts.
- Attenuating coordination relation: lead pre-assignment, dependency ordering, bounded file scope, reassignment and conflict-strategy decisions, with worktree isolation/conflict checks as enforcement.
- Feedback into subsequent S1 behaviour: updated owner/dependency records and lead messages determine what each worker works on next; conflict instructions pause/redirect affected workers until resolved.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation is tied to explicit cross-worker race/edit/merge collision modes and changes later worker behaviour to prevent or resolve them.

## S3 — Inside-and-now control

- State: A
- Function: maintain current whole-team cohesion by observing the live worker/task set and intervening in current commitments/capacity when workers fail, stall, die or leave dependencies blocked.
- Disturbance / variety regulated: uneven/idle load, stuck tasks, worker death, repeated failures, blocked dependencies, failed tasks and incomplete commitments.
- Decisive decision or feedback right: from the whole-team view, decide retry versus reassign versus skip, change ownership/dependencies, stop assigning to a repeatedly failing worker, spawn replacement or proceed to shutdown/verification.
- Decision owner: the model-backed Team lead.
- Supporting / enforcement mechanisms: `getTeamStatus`; task-list polling; messages/outbox; heartbeat/liveness state; watchdog timing; failure counters; task updates; spawn/shutdown; deterministic router/allocation policy.
- Closure path: whole-set exception becomes visible → lead chooses present-time intervention → owner/dependency/worker set or commitment changes → workers execute revised commitments → later status/completion/failure evidence returns to lead.
- Boundary reachability: monitoring, reassignment and error handling are explicit bundled native-Team duties while tasks are live.
- Why this is / is not agent-owned: watchdog/runtime state detect or enforce exceptions but do not make materially the same retry/reassign/skip/dependency choice if the lead model is removed.
- Evidence: [`skills/team/SKILL.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/team/SKILL.md); [`src/team/task-router.ts`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/src/team/task-router.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: initial decomposition/worker selection alone is not credited; witness is live whole-team exception regulation after work is underway.
- Whole-system current view: Team monitoring combines all workers' registration/liveness, current task, team-wide pending/in-progress/completed counts and recent messages.
- Current-control decision scope: lead can alter live ownership/dependencies, retry/skip work, replace dead workers, withhold assignments from repeatedly failing workers and terminate/progress current Team phase.

## S3* — Complementary audit

- State: A
- Function: independently challenge worker completion/quality claims through a separate read-only verification/review pass that gathers fresh repository evidence and returns findings into corrective control.
- Disturbance / variety regulated: executor self-approval, stale/unsupported completion claims, acceptance-criteria gaps, regressions and risk-specific security/quality defects not reliably exposed by ordinary worker status.
- Decisive decision or feedback right: independently judge PASS/FAIL/INCOMPLETE or issue risk/quality findings from fresh tests, diagnostics, builds, source inspection and conditional specialist audits.
- Decision owner: model-backed `verifier` and, when selected by risk/scale, separate `security-reviewer` / `code-reviewer` agents.
- Supporting / enforcement mechanisms: read-only reviewer contracts; prohibited Write/Edit; fresh test/build/LSP commands; OWASP/secrets/dependency audits; stage routing; verify/fix transition and bounded retry loop.
- Closure path: workers report execution results → separate verifier/reviewer independently inspects actual repository/evidence → PASS permits progression, failed findings generate fix tasks → Team enters `team-fix` → separate executors correct work → another verification pass.
- Boundary reachability: `team-verify` is canonical Team stage; verifier is always routed after execution and risk-sensitive/large changes explicitly add specialist reviewers.
- Why this is / is not agent-owned: runtime transitions enforce verdict consequences, but substantive acceptance/risk judgment is produced by separate model-backed audit actors that cannot author the change they audit.
- Evidence: [`agents/verifier.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/agents/verifier.md); [`agents/security-reviewer.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/agents/security-reviewer.md); [`agents/code-reviewer.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/agents/code-reviewer.md); [`skills/team/SKILL.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/team/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary executor tests are not the witness; mapping relies on separated no-self-approval review plus conditional risk/scale reviewers with materially different access.
- Claim being audited: completed worker changes actually satisfy original acceptance criteria without fresh test/build/type failures, regressions or risk-specific defects.
- Ordinary reporting path: worker completion/failure and implementation evidence return through Team task/message state to lead.
- Complementary access path: after authoring, read-only verifier independently runs fresh tests/build/LSP and reads repository evidence rather than trusting worker claims; security-sensitive or large/architectural changes additionally receive specialized audit.
- Independence boundary: reviewer roles are separate from authoring, `verifier` explicitly forbids self-approval and credited reviewer roles disallow Write/Edit.
- Who acts on findings: Team lead/pipeline consumes verdicts; failed verification creates fix work for separate executor/debugger actors before re-verification.

## S4 — Intelligence / adaptation

- State: A
- Function: model external/future-relevant improvement opportunities, develop competing adaptation hypotheses and return experimentally validated improvements into capability used by later self-improve rounds.
- Disturbance / variety regulated: changing techniques/dependencies, unknown optimization opportunities, failed prior approaches, plateaus and uncertainty over which future change will improve target capability.
- Decisive decision or feedback right: develop testable improvement hypotheses from repository/history/external evidence, turn them into candidate changes and carry accepted evidence-backed options into the improvement branch.
- Decision owner: distributed model-backed self-improve arrangement: researcher/planners own semantic research/hypothesis generation and executors instantiate candidates; deterministic tournament rules rank/confirm those agent-generated options by benchmark.
- Supporting / enforcement mechanisms: research briefs/history; external search; planner/architect/critic agents; experiment worktrees; sealed benchmark; tournament ranking/re-benchmark; merge/revert; best-score/plateau/circuit-breaker state.
- Closure path: current repository/history plus external research → researcher/planners generate future options → executors implement hypotheses in worktrees → benchmark/tournament validates winner → winner merges into `improve/{goal_slug}` → next iteration branches from updated state and uses accumulated history/results.
- Boundary reachability: `/self-improve` dispatches to bundled skill; after explicit setup/trust configuration the documented loop runs autonomously until predefined stop conditions.
- Why this is / is not agent-owned: benchmark ranking/merge gates enforce evidence, but without researcher/planner/executor model actors the open-ended external interpretation and hypothesis-generation/adaptation repertoire disappears.
- Evidence: [`skills/self-improve/SKILL.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/self-improve/SKILL.md); [`skills/self-improve/si-researcher.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/self-improve/si-researcher.md); [`commands/self-improve.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/commands/self-improve.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic task planning/model routing/learned-skill storage are not credited; witness is external/prospective research → competing hypotheses → experiment → persistent winner → next-round closure.
- External distinction: dedicated researcher inspects dependencies/repository evidence and may search external papers, benchmarks, similar projects and official documentation, producing cited ideas rather than relying only on internal task state.
- Future / prospective distinction: strategy changes after failures, approach-family exhaustion or proximity to target; planners generate testable future hypotheses and alternative future states are evaluated before adoption.
- Adaptation option generated: approved plans become concrete experiment-branch changes across architecture, training/configuration, data, infrastructure, optimization, testing or other approach families.
- Path back into current capability / S3: benchmark-confirmed winner merges into persistent improvement branch; later experiments branch from that improved state while best-score/history feeds later research/planning.

## S5 — Identity / ultimate policy

- State: —
- Function: no material first-party runtime identity/ultimate-policy decision loop with legitimate ultimate authority and returned operational closure was established at the selected OMC recursion.
- Disturbance / variety regulated: OMC exposes static policies, permissions, governance fields, approval gates and user-selected self-improve goal/benchmark/harness constraints, but these define/approve ordinary operation rather than resolve identity-level tension between current control and future adaptation.
- Decisive decision or feedback right: no S5-specific runtime right was found to reinterpret OMC's ultimate purpose/ethos or adjudicate an identity/ultimate-policy issue and return that ruling into subsequent operation.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: prompt policy; Team governance configuration; graph/action approvals; permissions; self-improve goal/benchmark/harness setup and trust confirmation; static stop/guardrail conditions.
- Closure path: no S5-specific closure established. Setup choices/approvals bound ordinary execution; once self-improve begins, its policy forbids pausing for user confirmation between iterations and stops on predefined conditions rather than escalating identity/policy questions.
- Why this is / is not agent-owned: model agents optimize/regulate inside already chosen task/governance/goal boundaries; static developer/user constraints and action approvals do not form an ultimate-policy loop.
- Evidence: [`src/team/governance.ts`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/src/team/governance.ts); [`skills/self-improve/SKILL.md`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/skills/self-improve/SKILL.md); [`src/agents/prompt-ssot/sections.ts`](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/src/agents/prompt-ssot/sections.ts).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: a user is ultimate external authority over invocation/configuration, but generic setup/action approval/out-of-band modification is not S5 without a first-party identity/ultimate-policy escalation-and-return path.

### Absence scope

- Surfaces inspected: Team governance/configuration and prompt policy; native Team workflow/cancellation/handoffs; graph/remote approvals; permission/model-routing configuration; self-improve goal, benchmark, harness, trust and stop-condition paths; notification approval transport; repository-wide policy/governance/identity/escalation searches.
- Plausible first-party paths checked: Team `plan_approval_required`; user task/goal selection; self-improve trust/benchmark confirmation; self-improve goal/harness as constitution; graph human approvals; prompt policy; permissions/risk/model escalation; merge/readiness approval; cancellation/user intervention.
- Why no material first-party path remains: reviewed paths either establish static constraints, choose task/objective before execution, approve ordinary potentially dangerous actions, or transport operational control. None demonstrates a runtime identity/ultimate-policy issue reaching legitimate ultimate authority, receiving a ruling and returning it to govern later operation.

## Recursion, variety, escalation

Team workers count as S1 only where they have bounded software outcomes, repository environment and local model/tool discretion. S2 is based on concrete claim/file/merge collision modes and feedback, not messaging/routing labels. S3 is based on live whole-team exception regulation, not initial decomposition. S3* is the separated evidence-gathering review path, not ordinary tests. S4 is the external/prospective self-improve experiment loop, not generic planning/memory. Static policy/approval surfaces remain outside S5.

## Admission conclusion

Proposed vector at the pinned revision: `A A A A A —`. OMC closes autonomous S1 through model-backed software workers; autonomous S2 through lead-owned anti-race/ownership/conflict coordination; autonomous S3 through live whole-team monitoring and exception-driven commitment reassignment; autonomous S3* through separate read-only evidence-gathering verifier/reviewer lanes whose failed findings enter the fix loop; and autonomous S4 through an external/prospective research-and-tournament self-improvement mode whose winners persist into later rounds. No runtime identity/ultimate-policy S5 closure is established at the frozen standard-distribution boundary.
