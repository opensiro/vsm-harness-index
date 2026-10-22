---
harness_id: no-human
project_name: no_human
repository: https://github.com/no-human-ai/no_human
review_ref: 5f99b7af3142bf9fc562bd35d127b852a99bc113
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: P
---

# no_human

## Review boundary

- System in focus: the installable self-hosted `no_human` coding factory operating a portfolio of independently executed issue-to-PR coding tasks, with the normal coder/reviewer/worker/queue and operator controls. The chosen recursion is one local `no_human` instance managing its tasks, not the `no-human-ai` open-source company or its software-development organization.
- Purpose and identity: turn issues into planned, implemented, independently reviewed and test-evidenced PRs while withholding merge authority from the coding agents.
- Relevant environment: changing target repositories and branches, incoming tickets, provider quotas, cross-task resource contention, review findings, test failures, CI/forge results and operator decisions.
- Standard-distribution boundary: `nh` CLI and board/API; `core` scheduler/orchestrator, installed model backends, worktree/VCS integration, independent reviewer, guards, persisted state, feedback/learning and supported interactive operator modes.
- Credited operating / distribution surfaces: `src/no_human/core/{scheduler,orchestrator,db,task}.py`, `agent/{claude_backend,codex_backend,supervisor}.py`, `review/reviewer.py`, `testing/`, `blockers/`, `learning/`, `cli/commands.py`, `api/app.py`, `vcs/` and documented supported `nh serve`, `nh task config`, `nh approve`, `nh rules` and `nh learnings` workflows.
- Adjacent first-party surfaces excluded from ownership: developer CI and release engineering, `eval/` benchmark campaigns and scoring/judging, demonstration screenshots and reported aggregate dogfood metrics, `docs/` design commentary and public project maintainer governance. They may corroborate reachable code but cannot alone supply assessed runtime owners.
- First-party operating / deployment modes considered: one coding task; multi-worker isolated concurrent task pool; independent reviewer gate; operator board/priority/approval/rule controls; scheduled learning harvest with default auto-management and the explicitly supported human-confirmation mode (`learning.auto_manage: false`). CLI `nh serve` constructs the harvest job; the separate API `lifespan` path does not always construct it, a bounded reachability caveat.
- Recursion level: one local owner-operated coding factory with multiple separate coding tasks. Each coder task is a lower-level S1 unit; reviewer and supervisor have separate gate/feedback roles without becoming additional independent coding S1 units by mere model multiplicity.
- Reviewed revision: [`no-human-ai/no_human@5f99b7af3142bf9fc562bd35d127b852a99bc113`](https://github.com/no-human-ai/no_human/tree/5f99b7af3142bf9fc562bd35d127b852a99bc113), frozen by [batch #1884](https://github.com/opensiro/vsm-harness-index/issues/1884).
- Observation date: 2026-10-22; source/config/docs inspection only, with no LLM-agent, provider or benchmark execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The user adds an issue or board task, optionally supplying criteria and a priority. `Scheduler` owns a SQLite-backed concurrent queue and starts isolated worktree runs (`max_workers` limits). The `Orchestrator` gathers context, uses planner and coding backends for plan/action selection, runs tests and a mechanical tamper/reproduction gate, asks a fresh-context read-only adversarial reviewer for file/line-cited judgments and either sends actionable failures back to the coder, parks/escalates, or prepares a reviewed PR. The reviewer checks the same task's implementation claim, not an independent audit of portfolio-management claims. A human `nh approve` action controls merge; `merge_policy` is a best-effort *advisory* readiness calculation, not auto-merge authority.

The pool reserves task IDs, isolates worktrees, respects concurrency and priorities and can pause the *entire* fleet when one worker discovers a shared subscription quota wall. This is an implemented cross-task attenuation path, but dispatch/ranking and quota cooldown decisions are deterministic. The operator can read the status/board's whole portfolio and change queued-task priority through human-only CLI controls, as well as pause/restart/cancel jobs; the scheduler subsequently consumes that authoritative override.

The learning subsystem records repeated supervisor corrections, review failures, escalations and tamper trips. The standard `nh serve` mode constructs a periodic `HarvestJob`: it creates scoped proposals; with `learning.auto_manage: true` (default) mechanically screens and promotes eligible items, logs events, and a future coder run selects triggered active memories for its prompt. Its promotion/filter decisions are predetermined deterministic rules, not an independently autonomous S4 model judging alternative adaptation policies. A supported `auto_manage: false` path retains human confirmation of proposed lessons; a human may additionally add/remove direct confirmed policy rules using `nh rules`. The later coder prompt consumes those persistent decisions. Separate optional curator/second-brain code does not change ownership without evidence of a standard autonomous prospective judgment in this reachability path.

Primary sources: [README and CLI](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/README.md), [scheduler](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/scheduler.py), [orchestrator](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/orchestrator.py), [reviewer](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/review/reviewer.py), [learning queue](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/learning/queue.py), [configuration](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/docs/configuration.md).

## Operational model

Each separately scoped coding task is a model-driven S1 actor: the model chooses what to inspect/change, receives tool/test/reviewer feedback, and retries or completes within predefined bounds. The shared pool is an implementation mechanism for inter-task capacity and availability, not a discretionary autonomous capacity manager. The human operator is the legitimate factory-level owner of current priority/commitment decisions and of persistent policy/rule changes. Scheduled lesson activation is real future-facing adaptation, yet the specific S4 adaptation acceptance in its default shipped path is a configured deterministic screen, so the autonomous decision-owner requirement is not met; the alternative confirmation mode is parent-owned.

## S1 — Operations

- State: A
- Function: interpret and implement a repository software task, iteratively select code/tool actions and repair a failed task attempt until reviewed PR delivery or explicit stop.
- Disturbance / variety regulated: ambiguous issue requirements, unknown code locations, tool/test errors, invalid patches, review findings, stale base branches and nonconvergence.
- Decisive decision or feedback right: the model-backed coder chooses repository exploration and implementation actions based on the issue, plan, worktree state and returned feedback; subsequent attempts may implement reviewer-requested corrections.
- Decision owner: task-local coding model via the supported `ClaudeBackend`/`CodexBackend` executor; planner/reviewer models contribute distinct planning/verdict inputs, while `Orchestrator` enforces bounds and routes outcomes.
- Supporting / enforcement mechanisms: model SDK/tool interface, bounded iterative attempts, isolated worktrees, tests, tamper/reproduction guards, adversarial review, VCS PR creation, blocker routing.
- Closure path: queued task → model-generated plan/implementation actions → tools/tests → independent review verdict → next coder correction attempt or review-passed PR/explicit terminal blocker.
- Boundary reachability: `nh task add` / the board and `nh start` / `nh serve` create actual tasks dispatched to `Orchestrator.run_task`; the orchestrator's coding backend performs the live model/tool session rather than merely rendering a hypothetical example.
- Why this is / is not agent-owned: implementation content/action choice is not predetermined by the scheduler or operator's task creation; failures are returned to the model for new decisions. The model does not own merging or whole-portfolio governance.
- Evidence: [CLI task lifecycle](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/README.md#run-one-task), [agent session and attempt loop](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/orchestrator.py), [model backends](https://github.com/no-human-ai/no_human/tree/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/agent).
- Basis: source-grounded reachable standard execution path.
- Confidence: high for structural S1 action/discretion; actual LLM performance not evaluated.
- Caveats: no model sessions were started for this assessment; API/credential/provider availability governs live completion and does not alter the shipped decision wiring.

## S2 — Coordination

- State: C
- Function: damp concrete cross-task resource contention in the pool, specifically shared provider quota and finite concurrent execution capacity.
- Disturbance / variety regulated: one independently executing worker exhausts the subscription or infrastructure availability relied on by other independently executing coding tasks; too many tasks claim limited execution slots.
- Decisive decision or feedback right: a shared quota wall from one worker stops fleet-wide *new dispatch* until recovery; tasks are reserved against duplicate claims and queued pending available slots. The material correction is shipped, but chosen by fixed configured rules rather than an autonomous S2 agent.
- Decision owner: deterministic `Scheduler` implementing configured resource/cooldown policy; an autonomous coordination-choice owner is not established.
- Supporting / enforcement mechanisms: SQLite task states, isolated worktrees, `_inflight` reservations, shared subscription quota cooldown and reset, pool width, recover/resume sweeps.
- Closure path: S1 worker parks `PAUSED_QUOTA` → scheduler arms shared cooldown → sibling task dispatch is withheld → cooldown expiry/known reset → parked tasks become resumable and new sibling S1 work is dispatched.
- Boundary reachability: first-party `Scheduler` is constructed and run by documented `nh serve`/board modes; its shared quota policy operates over distinct task worktrees in one installed pool.
- Why this is / is not agent-owned: regulation is more specific than a task-list mailbox: it responds to an observed *shared resource interference* affecting several S1 units. But explicit resource limits, static ranking and programmed pause/resume do not prove autonomous discretion; an S2-specific constructor/control path supports `C`, not `A`.
- Evidence: [scheduler cross-worker quota contract and dispatch](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/scheduler.py#L1-L25), [quota recovery/claim code](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/scheduler.py#L750-L1020), [periodic pool tick](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/scheduler.py#L2125-L2355).
- Distinct S1 units: distinct task-local model-driven coder attempts with isolated repository worktrees.
- Inter-S1 disturbance: shared quota exhaustion by task A would cause sibling task B/C to fail or waste attempts when they were otherwise ready.
- Attenuating coordination relation: a single shared-quota gate temporarily suppresses cross-pool dispatch instead of allowing every worker to keep issuing calls into the same quota wall.
- Feedback into subsequent S1 behaviour: siblings remain queued/parked during cooldown, then resume/run after the reset instead of repeatedly failing at the same provider limit.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the feedback specifically captures a cross-worker provider-capacity shock and alters other S1 units' admission; ordinary priority queue sorting alone is not credited.
- Basis: actual first-party cross-S1 regulation with deterministic decision owner.
- Confidence: medium-high.
- Caveats: this is a narrow capacity-coordination function, not autonomous resolution of contradictory code commitments or dynamic S3 resource governance; merge conflict precheck is operator advisory rather than a separate autonomous S2 owner.

## S3 — Inside-and-now control

- State: P
- Function: let the local factory owner supervise the current portfolio, revise queued commitments/priorities, and return that decision to the running dispatcher.
- Disturbance / variety regulated: different tasks compete for attention and execution capacity; emergent task urgency and blocked or stale commitments may require the portfolio owner to redirect resources in the present.
- Decisive decision or feedback right: the operator observes whole-portfolio task lanes/statuses, then executes `nh task config <id> priority=high|medium|low`, pauses/cancels/resumes a task, or grants an explicit task-level bound override. The scheduler subsequently changes admission order or the action's task lifecycle.
- Decision owner: legitimate human operator of the self-hosted instance; no autonomous model owns the whole-pool priority/commitment judgment. `Scheduler._rank_pending` merely respects returned priority inputs and enforces slot/quota policy.
- Supporting / enforcement mechanisms: `nh status` portfolio view, board/API, priority column and human audit event, `task config` human-only writes, `_claimable`/`_rank_pending`, cancel/pause/reply controls, SQLite state.
- Closure path: portfolio status/board → operator judges a priority or commitment change → human-only CLI/API writes task state/priority → next scheduler tick chooses different pending work (or honors pause/cancel) → changed task status feeds the next portfolio view.
- Boundary reachability: documented `nh status`/board and human-only `nh task config` are installed operator surfaces backed by the same task store and pool used by the ongoing coding workers.
- Why this is / is not agent-owned: the discretionary current priority is chosen by the operator, not deduced by `Scheduler`; static concurrency caps and reviewer readiness do not establish autonomous S3.
- Evidence: [portfolio status](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/cli/commands.py#L4396-L4510), [human task override](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/cli/commands.py#L1309-L1400), [scheduler priority consumption](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/scheduler.py#L939-L1005), [documented priority contract](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/docs/configuration.md#dispatch-priority).
- Whole-system current view: the self-hosted instance's stored and board/CLI-displayed queued, running, waiting, review and terminal task portfolio with task identifiers and current condition.
- Current-control decision scope: human owner adjusts dispatch priorities/active task state and task-level commitment/budget overrides, altering which pending work the bounded fleet executes next.
- Basis: first-party closed operator-mode present-management loop, narrower than cross-organization strategy.
- Confidence: moderate; human observation/choice is a supported operating mode rather than a witnessed live operator decision in this source-only assessment.
- Caveats: `nh status --json` produces portfolio counts; detailed item context comes through board/task detail. `priority` does not preempt running tasks, and a static priority configured at creation alone is not the credited S3 judgment.

## S3* — Complementary audit

- State: —
- Function: independent audit of S3 management claims and return of its own corrective management judgment.
- Disturbance / variety regulated: the independent adversarial reviewer does catch fabricated completion claims, false evidence and tampering within *one coding task*, but this is not an independent audit of whole-portfolio priority, resource and accountability management.
- Decisive decision or feedback right: the reviewer can block task delivery/send the coder back on cited code quality evidence; no shipped independent function judges the factory owner's S3 portfolio-management claims through a separate audit channel.
- Decision owner: separate read-only reviewer model owns task-local quality-check judgments; tamper/test gates are mechanical, and neither claims S3* audit authority at the assessed recursion.
- Supporting / enforcement mechanisms: fresh-context read-only `AdversarialReviewer`, mechanical tamper/repro checks, evidence citations, review feedback/retry gates and PR comments.
- Closure path: coder completion claim → independent diff/test review → coder correction or withheld PR. That is a task-level assurance path; the missing S3* return would independently inspect S3 portfolio decisions and correct S3 action.
- Why this is / is not agent-owned: independence from the *coder* alone does not make review complementary audit of *management*. The reviewed subject and acted-on feedback belong to S1 task acceptance, not the S3 control view.
- Evidence: [reviewer prompt/session](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/review/reviewer.py#L2419-L2600), [orchestrator review return](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/orchestrator.py), [mechanical guard](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/testing/tamper_guard.py).
- Basis: bounded first-party negative at the portfolio-management recursion.
- Confidence: medium-high for the reviewed factory-level boundary.
- Caveats: at a differently chosen recursion, one could separately analyze the QA independence of the task pipeline; this report does not rename ordinary task QA as S3*.

### Absence scope

- Surfaces inspected: reviewer and supervisor prompts/decisions, orchestrator gate, `merge_policy` readiness, tamper/reproduction/verification checks, pool status, audit event logging and operator controls.
- Plausible first-party paths checked: independent source verification of coder output, portfolio-health telemetry, reviewer gate returning corrective feedback, operator readback and learning event audit.
- Why no material first-party path remains: the separate reviewer can access code/diff/tests but does not independently test claims made by whole-portfolio S3 priority/commitment control or direct S3 corrections; status/event records are not an independent complementary audit owner.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: infer reusable future-work improvements from outcomes/failures across earlier tasks and return selected learning/policy adaptations into later coding-agent behavior.
- Disturbance / variety regulated: recurring reviewer defects, repeated supervisor corrections, tamper triggers, escalation patterns and changing target-repository demands that can make the existing coding practices fail repeatedly.
- Decisive decision or feedback right: in normal auto-management, review/supervisor observations yield scoped rule/anti-pattern proposals, but *promotion* is chosen by deterministic dedupe/PII/provenance/vendor-term screens and a 24-hour cap, not by an S4 agent judging competing future strategies. In explicit human-confirmation mode, the operator chooses which proposed lesson deserves activation; this decision returns to subsequent coder prompts.
- Decision owner: the first-party S4 constructor comprises model-derived review/supervisor findings plus scheduled heuristic harvest and future prompt injection (`C`). Under `learning.auto_manage: false`, the legitimate local operator decides which candidates become active (`P`). No fully agent-owned prospective adaptation-selection judgment is established in the default loop.
- Supporting / enforcement mechanisms: `HarvestJob` scheduled correction/failure harvesting, scoped persistent learning queue, `LearningQueue.auto_activate` checks, human `confirm`/`reject`, triggered/ranked prompt memories, retirement sweeps and learning event logs.
- Closure path: external repository/task failure pattern → harvested prospective repeat-prevention lesson → either default mechanical screen or parent confirm decision → active persistent rule → task-trigger match → later coder plan/implementation prompt includes lesson → different future S1 behavior.
- Boundary reachability: `nh serve` creates `HarvestJob` with `learning.auto_manage: true` by default and calls it from `Scheduler.tick`; `auto_manage: false` is a documented configuration switch and `nh learnings --confirm` uses the shipped queue. `Orchestrator._load_active_memories` and `_build_implement_prompt` close consumption of activated rules on subsequent real tasks.
- Why this is / is not agent-owned: the actor evaluating individual task correctness is model-driven, but the *future adaptation acceptance* step is preset screening and optional human judgment; model assistance in deriving a finding must not be conflated with autonomous S4 ownership. Specific prospective learning/proposal/injection surfaces justify `C`, and supported operator confirmation closes `P` independently.
- Evidence: [scheduled harvest/activation](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/scheduler.py#L3017-L3170), [activation screen](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/learning/queue.py#L1363-L1500), [human confirmation](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/learning/queue.py#L1173-L1210), [runtime prompt rule injection](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/orchestrator.py#L19859-L20015), [configuration](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/config.py#L2350-L2380).
- External distinction: repeated errors and corrections across real codebases, provider situations and prior externally supplied coding tickets, rather than just replanning within one task.
- Future / prospective distinction: harvest tries to turn repeatable past failures into safeguards/practices for *later* independent tasks; it is not the reviewer retrying the current diff.
- Adaptation option generated: project- or context-scoped rule/anti-pattern proposal extracted from recurring reviewer, supervisor, escalation and tamper evidence.
- Path back into current capability / S3: confirmation/auto-activation persists a rule in the active set; the next task's trigger/ranking and implement prompt consume it as a changed operational instruction.
- Basis: first-party shipped prospective learning pathway with contrasting deterministic and parent decision ownership.
- Confidence: moderate for `C(P)`; this is a constructor/parent-mode classification, not proof that auto-managed lessons measurably improve coding outcomes.
- Caveats: auto-managed activation is real but mechanically governed. The separate `ReanalysisJob` and optional curator are not used to assert an autonomous adaptation-decision owner. Harvest reachability is `nh serve`; the API server's separate worker lifespan may omit `HarvestJob`.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | first-party review/supervisor findings plus deterministic harvest/activation policy; no autonomous future-policy judge | recurring corrected coding-task outcomes | learning proposal screened/auto-activated and injected into later coder prompts, but the autonomous S4 decision owner remains uncomposed | `core/scheduler.py` `HarvestJob`; `learning/queue.py`; `core/orchestrator.py` |
| Parent (`P`) | human operator via `nh learnings --confirm` and the queue's `confirm()` | inspected pending cross-task lessons when `learning.auto_manage: false` | approved lesson becomes confirmed persistent rule and changes subsequent coding prompt | `learning/queue.py`, `cli/commands.py`, `docs/configuration.md` |

## S5 — Policy and identity

- State: P
- Function: set persistent local-factory normative boundaries (what coding practices the factory must follow) while keeping the ultimate acceptance/merge authority under its legitimate human owner.
- Disturbance / variety regulated: disagreement over permissible coding behavior, trust boundary between agent-generated edits and accepted work, and changing enduring operator requirements that should apply to later tasks rather than a single retry.
- Decisive decision or feedback right: the operator directly sets/removes globally or project-scoped confirmed rules using `nh rules add/remove`, controls agent-versus-approve git identity and retains exclusive `nh approve` merge authority. The credited ultimate-policy decision is the durable rule choice, not an isolated PR approval.
- Decision owner: local parent human owner; the model executor does not authoritatively redefine the confirmed standing rule set through `nh rules`, and `merge_policy` cannot approve or merge on its own.
- Supporting / enforcement mechanisms: human CLI command, confirmed memory persistence, prompt rule injection, separate commit/approval identities, independent review and explicit merge operation.
- Closure path: owner chooses or revises a standing normative coding constraint → `nh rules add/remove` persists authoritative confirmed policy → `_load_active_memories` selects the applicable rule → `_build_implement_prompt` conveys it to later model-driven coding tasks → operator continues to withhold or grant merge on reviewed output.
- Boundary reachability: shipped operator `nh rules` commands write immediately confirmed rule entries into the same database the production task prompt path reads. This is a live operator/policy mode on a local instance, not OSS repository maintainer governance projected into customers' installations.
- Why this is / is not agent-owned: durable normative contents and approval identity are ultimately operator-chosen; coder agents may make operational implementation decisions inside those bounds but do not independently redefine the factory's purpose or final acceptance constitution.
- Evidence: [confirmed standing-rule management](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/cli/commands.py#L2850-L2930), [rule ingestion into coder prompt](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/orchestrator.py#L19390-L19440), [human approval identity/merge](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/cli/commands.py#L5584-L5650), [merge policy explicitly advisory](https://github.com/no-human-ai/no_human/blob/5f99b7af3142bf9fc562bd35d127b852a99bc113/src/no_human/core/merge_policy.py#L1-L28).
- Identity / ultimate-policy issue: which enduring rules and operational limits govern coding on behalf of the self-hosted instance owner, and who is authorized to accept resulting changes into the repo.
- Ultimate authority in each claimed mode: owner/operator (`P`) only; the task reviewer and coder cannot independently replace standing human-authored policy or become the approval authority.
- Return-to-operation path: operator rule decision → confirmed persistent rule → triggered injection into future coder prompt; merge remains a separate human-controlled final authority path.
- Basis: supported, operationally closed parent policy mode at the local-factory recursion.
- Confidence: moderate, limited to durable local normative rules rather than claiming that the upstream maintainers' product identity is governed through runtime CLI.
- Caveats: model instruction compliance is not itself technically guaranteed by rule text, so practical effectiveness is not asserted. Individual task acceptance alone was not used to upgrade S5; the standing rule/authority closure is the distinctive positive evidence.

## Distributed OSS parent arrangement

This artifact assesses one installed factory, not the distributed OSS project's maintainer organization. An owner of a local installation is a legitimate parent for the documented operator controls. Contributors, GitHub PR maintainers and released versions of `no_human` do not thereby demonstrate a centrally shared parent at the multi-contributor project recursion.

## Self-hosted and non-human modes

The self-hosted user can operate multiple coding tasks with a human-owned live priority and standing policy loop. S4 supports a default auto-activation policy and a human-confirmed alternative; automatic enforcement cannot be relabeled autonomous agent judgment solely because no click is needed. Independent QA checks are within coding-task delivery, not automatically S3* at the local portfolio recursion.

## Recursion

Task-local coder is an S1 unit at the local factory's portfolio recursion. The full factory contains many S1 units with shared capacity, S2 capacity attenuation, and a human current manager. Inside a single coding task, planner/coder/reviewer are phases/roles for that task, not automatically a second factory with the same vector. The codebase's upstream OSS governance is a higher, unassessed recursion.

## Variety and escalation

Model exploration and corrective review absorb per-task uncertainty; reproducibility/tamper and budget gates limit unsafe variety. Pool cooldowns regulate shared provider shocks. Human priority changes reprioritize queued commitments, task blockers ask operators for missing decisions, and durable lessons can modify later prompt guidance. Neither task-local review nor provider-quota limits is evidence of autonomous whole-factory S3 ownership.

## Evidence gaps

- No LLM-agent/model-provider or real PR run was executed: this is a pinned source-based assessment of shipped decision paths, not measured coding effectiveness or external platform availability.
- S2 credit is narrow to structurally explicit cross-task quota/capacity attenuation; no claim is made about autonomous conflicting-change reconciliation.
- S3 `P` describes a supported human whole-instance management path, not an observed specific operator's decision or a policy for multiple independent customers.
- S4 `C(P)` is deliberately conservative about default automatic activation: future learned-rule promotion is screened by a deterministic policy, while the human-confirmation mode has an explicit decisive owner. The API-only worker-mode harvest omission bounds the qualifying shipped surface.
- S5 `P` concerns direct persistent owner-authored standing rules and identity/merge authority at the local factory, not mere per-ticket approvals or theoretical policy decisions by OSS maintainers.
