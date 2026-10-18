---
harness_id: reigen
project_name: Reigen / Conductor
repository: https://github.com/zachary-wilde/reigen
review_ref: 6236f47a1b2f3081a0f22bcba47705bcd1680720
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Reigen / Conductor

## Review boundary

- System in focus: one first-party Conductor/Reigen Ravel organization at pinned revision `6236f47a1b2f3081a0f22bcba47705bcd1680720`, including the persistent Core, Ravel manager event cycles, exact plan-revision/approval protocol, brief/task state, per-worker worktree/process lifecycle, dependency handoffs, independent verification path, review/landing controls, human-seat/operator path, automation/occurrence ledger and remote worker controls that service that organization.
- Purpose and identity: organize bounded software-development work by turning a user objective into an approved mission and specialist briefs, governing autonomous external coding workers through completion/review while preserving operator authority over consequential current commitments.
- Relevant environment: human operator/approver; project repository and Git state; Claude Code, Codex and Z.AI/OMP-compatible external harness/model workers; local shell/process environment; project-defined verification commands; remote browser/mobile operator; and scheduled occurrences configured by the operator.
- Standard-distribution boundary: first-party Conductor desktop/Core/Ravel/Operations runtime plus its shipped manager protocol, worker controls, plan/verification/review/automation machinery. External Claude/Codex/Z.AI model reasoning remains separate. A project-supplied verification command contributes independent evidence but does not become an autonomous Conductor auditor by configuration alone.
- Credited operating / distribution surfaces: `README.md`; `src/main/ravel.ts`; `src/main/ravel-model.ts`; `src/main/manager-turn.ts`; `src/main/harness.ts`; `src/main/operations/core.ts`; `src/main/operations/worker-controls.ts`; first-party persistent Core and normal Ravel/remote-operator paths described by the standard distribution.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/release work, tests and smoke fixtures except as corroboration of runtime semantics, maintainer/contributor governance, and any model/harness-internal organizational behavior not reached through the declared Conductor runtime relation.
- First-party operating / deployment modes considered: event-driven Ravel manager with user-approved plan revisions; autonomous external child dispatch into isolated worktrees; dependency-gated handoffs; direct operator worker controls; human-seat completion; optional project verification before manager reaction; review/land flow; persistent Core and remote operator; scheduled/heartbeat automation.
- Recursion level: one Ravel-controlled coding organization is the system-in-focus. Its specialist coding sessions are sibling S1 units. The Ravel manager and first-party control surfaces form the metasystem for that organization. Other independent Ravels/normal sessions in the same persistent Core are adjacent organizations rather than silently aggregated S1 units for this mapping.
- Reviewed revision: `6236f47a1b2f3081a0f22bcba47705bcd1680720`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Conductor is a durable desktop/background control organization around external coding-agent CLIs. A Ravel manager is not a persistent TUI session: each user message, approved plan event, child event or other trigger rebuilds a bounded manager prompt and invokes the configured external harness/model once, with a maximum of three sequential manager invocations per event. That prompt contains the current approved plan, mission constraints, brief/dispatch states and live fleet snapshot. The manager can propose a plan, spawn a ready brief, message a live child, request status, log or complete. Children are separate autonomous coding-agent processes in separate Git worktrees and receive only their own bounded brief plus explicitly published dependency outputs.

Plan structure supplies a concrete coordination relation for parallel work. The manager protocol requires every brief in a multi-brief plan to carry real `doNotTouch` entries specifically because parallel agents can collide. Plan validation rejects multi-brief proposals without those boundaries, and `buildRolePrompt()` injects them into each worker's execution prompt. Conductor also records current changed paths and its Insights rules can identify protected-path violations or two active agents editing the same file. The positive S2 mapping does not rely on the dependency graph or worktrees alone; it relies on this explicit collision mode, manager-selected separation relation and return into worker behavior.

Current control is split into two first-party ownership configurations. In the autonomous base mode, the Ravel manager gets a whole-Ravel current snapshot and makes bounded dispatch/intervention decisions in response to events, including spawning ready briefs and messaging children; an operator detach explicitly triggers a manager replan event. In the parent mode, the operator must approve the exact plan revision before spawning is legal and can also message, pause/resume, stop, retry, archive or detach workers through the Operations Core. Deterministic approval checks, dependency gates, process lifecycle and worktree isolation enforce these choices without owning the organizational decision.

Verification is deliberately complementary but not autonomously owned by Conductor. When configured, the repository's own verification command runs in a finished child's worktree before the manager receives the child-exit event. Its verdict is persisted and presented to the manager before the child's self-report; pending verification prevents premature fleet completion. The first-party path is therefore an S3*-specific constructor primitive. The actual audit criterion/judgment, however, comes from a project/operator-configured command rather than a packaged autonomous auditor. The autonomous manager owns the downstream current-control response to that evidence, which does not transfer S3* audit ownership to the manager.

## Operational model

A user gives a Ravel an objective. The autonomous manager may clarify it and proposes a mission plus specialist briefs. The exact revision must be approved before any brief can spawn. Once approved, manager event turns consume the current plan/fleet state and dispatch ready briefs to external Claude/Codex/Z.AI workers. Each child receives bounded context, explicit acceptance criteria, `doNotTouch` boundaries and dependency outputs; the child owns task-local reasoning and acts in its isolated worktree.

Child exits, operator detaches and other current events return to the Ravel manager. A configured verify command first inspects the finished child's worktree and its pass/fail result is inserted ahead of the child's own report in the manager directive. The manager then decides what to do next under its tool protocol. Operator controls remain available as a separate parent path, and review/landing rechecks reviewed state before merge. Scheduled automation can create or wake work according to operator-defined cadence, but the scheduler is deterministic execution of configured recurrence rather than environmental intelligence.

## S1 — Operations

- State: A
- Function: perform bounded software-development work for an approved Ravel brief through an external coding-agent process acting in its own project worktree.
- Disturbance / variety regulated: task-specific repository state, implementation uncertainty, tool/build/test feedback, local errors and the bounded context needed to satisfy the brief.
- Decisive decision or feedback right: choose the substantive reasoning path, code/tool actions and local implementation decisions needed to satisfy the assigned brief within its constraints.
- Decision owner: the autonomous external Claude/Codex/Z.AI model actor launched through the first-party child-session path.
- Supporting / enforcement mechanisms: first-party harness resolution/launch, worktree and branch lifecycle, role prompt, brief scope, dependency-output publication, optional auto-approval, session/process tracking and operator controls.
- Closure path: approved brief becomes ready → Ravel manager selects `spawn_child` → Conductor creates/binds the worker session and worktree with the role prompt → external model actor chooses task actions and receives repository/tool feedback → child exits/publishes result → outcome returns into Ravel verification/current control.
- Boundary reachability: Ravel child dispatch and external CLI launch are normal shipped operating paths in `ravel.ts`/`harness.ts`; the autonomous actor is reached directly by the standard product rather than through repository-development tooling.
- Why this is / is not agent-owned: Conductor constrains and supervises the child, but the substantive task-local choices are made by the external model actor. Worktree/process machinery does not replace that operational discretion.
- Evidence: [`README.md`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/README.md); [`src/main/ravel.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/ravel.ts); [`src/main/harness.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/harness.ts); [`src/main/ravel-model.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/ravel-model.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external harness/model internals are not inherited into Conductor. The positive state credits the external autonomous S1 actor only because the first-party standard runtime directly launches and governs it.

## S2 — Coordination

- State: A
- Function: attenuate destructive file/scope interference among sibling coding workers executing parallel briefs in the same Ravel plan.
- Disturbance / variety regulated: parallel S1 workers can edit overlapping repository paths or enter one another's intended scope, producing conflicting changes and unstable integration assumptions.
- Decisive decision or feedback right: select concrete per-brief scope-exclusion boundaries that partition parallel work sufficiently to reduce collision risk while retaining useful local autonomy.
- Decision owner: the autonomous Ravel manager when it constructs the multi-brief plan and chooses each brief's `doNotTouch` boundaries from the mission/repository context.
- Supporting / enforcement mechanisms: manager protocol requiring meaningful `doNotTouch` for fan-out, plan validation rejecting missing boundaries, worktree isolation, dependency gates, role-prompt injection, changed-path observation and Insights overlap/protected-path detection.
- Closure path: manager decides to fan work out across distinct briefs → it must choose explicit `doNotTouch` boundaries for every parallel brief → plan validation preserves those boundaries and the approved plan becomes executable → `buildRolePrompt()` injects the selected exclusions into each S1 worker → subsequent worker behavior is constrained away from sibling scope; current changed-path observations can surface boundary violations/overlap for further intervention.
- Boundary reachability: the coordination rule is embedded in the normal manager prompt and plan validator and is returned into standard child prompts; it is not a documentation-only convention or CI check.
- Why this is / is not agent-owned: deterministic validation merely refuses an invalid fan-out plan and worktrees merely isolate physical working copies. The manager chooses the semantic separation relation. The human's exact-plan approval governs whether the whole current plan may execute, but the S2-specific choice of collision-attenuating boundaries is generated by the manager; removing the manager leaves no equivalent adaptive boundary-selection decision.
- Evidence: [`src/main/manager-turn.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/manager-turn.ts); [`src/main/ravel-model.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/ravel-model.ts); [`src/main/insights/rules.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/insights/rules.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: dependency edges, role names, worktrees and turn ordering are not counted merely from topology. The positive witness is the explicit parallel-edit collision problem plus an agent-selected scope-separation relation that is mandatory in multi-brief plans and returned to each worker. Human ratification of the overall exact plan is S3 parent governance and does not by itself own the narrower S2 boundary-selection judgment.
- Distinct S1 units: two or more separately launched coding-agent child sessions associated with different briefs in one approved multi-brief Ravel plan.
- Inter-S1 disturbance: parallel workers can touch the same file/scope; the manager protocol states that boundaries are required when there is somebody else to collide with, and the Insights subsystem structurally detects concurrent changed-path overlap/protected-path violations.
- Attenuating coordination relation: explicit per-brief `doNotTouch` scope exclusions selected during autonomous plan construction, with worktree isolation and dependency gating supporting the relation.
- Feedback into subsequent S1 behaviour: the selected exclusions are serialized into each worker's role prompt before execution, so the coordination decision changes what each S1 is instructed not to modify; violations/overlap remain observable for current intervention.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited path is explicitly tied to preventing concrete parallel-agent scope/file collisions, not merely to moving messages or ordering tasks.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate the current Ravel organization as a whole by choosing and revising present work commitments, dispatch/intervention actions and responses to current fleet events.
- Disturbance / variety regulated: ready/blocked briefs, child completion/failure, verification results, live worker behavior, capacity, harness availability, detached workers, dependent briefs and other current conditions can require whole-Ravel intervention.
- Decisive decision or feedback right: in autonomous mode, decide which approved ready brief to spawn, whether/how to message a live child, how to respond to child/verification/detach events and when the approved fleet is complete; in parent mode, decide whether an exact current plan revision may execute and directly intervene in worker lifecycle/commitments.
- Decision owner: base mode — the autonomous Ravel manager invoked on bounded event turns. Parent mode — the human operator/approver using exact-plan approval and Operations Core worker controls.
- Supporting / enforcement mechanisms: bounded reconstructed manager context, current-plan and fleet digests, plan-revision guard, dependency eligibility, process/worktree lifecycle, persistent Core/store, Operations event journal, worker-control availability/confirmation logic and remote transport.
- Closure path: current whole-Ravel plan/fleet/event state is assembled → manager or operator makes a current-control decision → first-party tool/control path validates and applies spawn/message/approval/pause/resume/stop/retry/archive/detach/replan consequences → runtime/persistence changes the live organization → new fleet/current state is fed into subsequent event turns or operator views.
- Boundary reachability: manager turns and operator controls are both normal supported runtime paths. The manager is invoked directly through the configured external harness in the Ravel operating mode; parent controls are exposed by the desktop/Core/remote operator surfaces.
- Why this is / is not agent-owned: the manager has more than a delegation label: every turn receives the approved mission/plan, dispatch state and live fleet snapshot, and it has current intervention tools. Deterministic dependency, approval and lifecycle checks enforce allowed transitions but do not choose the manager's intervention. The operator path independently closes the same current-control function in a first-party parent mode.
- Evidence: [`src/main/manager-turn.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/manager-turn.ts); [`src/main/ravel.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/ravel.ts); [`src/main/ravel-model.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/ravel-model.ts); [`src/main/operations/core.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/operations/core.ts); [`src/main/operations/worker-controls.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/operations/worker-controls.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: initial task decomposition alone would not establish S3. The positive mapping relies on the manager's whole-Ravel current snapshot plus event-driven current intervention/replan path. Exact-plan approval is not treated as S5; at this recursion it is a parent decision over present organizational commitments.
- Whole-system current view: the manager prompt carries the current mission constraints, exact plan revision/approval state, every brief's role/harness/dispatch/dependency state and the live child fleet; the Operations Core additionally exposes persistent normalized worker/timeline state to the operator.
- Current-control decision scope: autonomous dispatch and live-child messaging/reaction to current events; parent exact-plan admission plus message/pause/resume/stop/retry/archive/detach controls, with detach explicitly causing a manager replan event around blocked dependents.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | autonomous Ravel manager | user/approval/child/verification/detach event changes current whole-Ravel state | manager receives bounded current plan+fleet context, selects first-party control tools, and resulting dispatch/message/replan/completion state returns into later event turns | `src/main/manager-turn.ts`; `src/main/ravel.ts`; `src/main/harness.ts` |
| Parent (`P`) | human operator / exact-plan approver | a plan revision requires commitment or current worker state needs intervention | operator approves the exact revision or applies shipped worker controls; first-party runtime enforces the decision and subsequent current operation changes | `src/main/ravel-model.ts`; `src/main/operations/core.ts`; `src/main/operations/worker-controls.ts`; `README.md` |

## S3* — Complementary audit

- State: C
- Function: independently check a finished worker's ordinary success claim against project-defined verification evidence before the metasystem acts on that exit.
- Disturbance / variety regulated: a child can report successful completion even when the repository's independent verification command fails or cannot run.
- Decisive decision or feedback right: define and produce the complementary pass/fail audit judgment over the finished child's worktree; that judgment must reach current control before the child's self-report is acted on.
- Decision owner: no autonomous S3* owner is packaged by Conductor. The project/operator supplies the repository verification command and therefore the audit criterion/judgment source; Conductor supplies the S3*-specific execution, ordering, persistence and return path. The autonomous Ravel manager owns the downstream S3 response to the audit result, not the audit judgment itself.
- Supporting / enforcement mechanisms: `runVerify` in the child's worktree, configured global/per-repository verify command, captured exit/output verdict, `verifying` pending set, fail-closed runner failure, persisted `DispatchVerification`, manager directive ordering and completion hold while verification is pending.
- Closure path: child exits and ordinary self-report is captured → first-party Ravel marks verification pending → configured repo verify command runs separately in that child's worktree → verdict/output is persisted → manager event is withheld until the verdict lands → the manager receives `VERIFY COMMAND PASSED/FAILED` before the child's own report and makes the next current-control decision with that contradiction/evidence in context.
- Boundary reachability: verification is wired into the normal Ravel child-exit path when the operator/project configures a verify command; no repository-maintainer CI path is required. The first-party runtime deliberately executes it in the finished child's worktree before invoking the manager on that exit.
- Why this is / is not agent-owned: Conductor establishes a function-specific complementary access and feedback path, but the audit judgment itself is the configured external/deterministic repo command. The manager's autonomous reaction does not retroactively own that audit judgment. A developer/operator must compose the meaningful verification criterion, so the autonomous audit function remains constructor-owned rather than `A`.
- Evidence: [`README.md`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/README.md); [`src/main/ravel.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/ravel.ts); [`src/main/ravel.integration.test.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/ravel.integration.test.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the verify command may be a test/build/check script and need not itself be an AI evaluator. That is why the state is `C`, not `A`. Human review/landing surfaces provide additional checking but are not used to claim a parent modifier, which Methodology 0.3.x does not publish for S3*.
- Claim being audited: a child process's ordinary claim/exit signal that its assigned brief completed successfully and its result is fit to advance the fleet.
- Ordinary reporting path: child session exit plus its own report/tail/result enters the Ravel child-exit path.
- Complementary access path: separately configured repository verification command executes in the finished child's actual worktree/branch and produces an independent pass/fail plus captured output.
- Independence boundary: the verification process is not the child self-report and runs through a separate first-party hook runner against repository state after the child finishes; runner failure is recorded as failed verification rather than accepted success.
- Who acts on findings: the Ravel manager receives the verification verdict before the child's report and owns the subsequent S3 decision; pending verdicts block premature `complete`, ensuring the complementary result enters control before closure.

## S4 — Outside-and-then adaptation

- State: —
- Function: no material installation/Ravel-level S4 outside-and-then adaptation loop is established in the reviewed standard distribution.
- Disturbance / variety regulated: Conductor records durable history, computes Insights over current/recent fleet state, supports Roundtable deliberation, schedules future occurrences and can fall back among installed manager harnesses, but these paths do not establish external prospective sensing that develops an adaptation option and returns it into present organizational capability.
- Decisive decision or feedback right: not established for an S4 function at the declared recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deterministic Insights rules, event journal/timeline, Roundtable discussion, cron/heartbeat scheduling, occurrence ledger, installed-harness discovery/fallback and persistent Core state.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: internal performance/coordination/verification observations and scheduled future execution can support operations, but neither is evidence of an externally and prospectively oriented adaptation conversation with S3.
- Evidence: [`README.md`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/README.md); [`src/main/insights/rules.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/insights/rules.ts); [`src/main/insights/engine.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/insights/engine.ts); [`src/main/operations/automation-engine.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/operations/automation-engine.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a user can ask a Roundtable/Ravel to reason about future strategy, but generic prompt expressiveness is not a packaged S4 organizational loop without a standard environmental sensing/adaptation-return path.

### Absence scope

- Surfaces inspected: README architecture/status claims; Ravel manager/event flow; persistent Core/operations/timeline; Insights rules/engine; Roundtable role in the documented product; harness availability/fallback; scheduler/cron/occurrence machinery; automation wake/create paths; review/landing and durable state.
- Plausible first-party paths checked: model/vendor availability handling, historical fleet insights, strategy Roundtable handoff, scheduled future work, persistent event history and manager re-planning.
- Why no material first-party path remains: these surfaces reason about current/internal state, user-supplied questions or preconfigured time occurrences. None establishes a standard path that senses an external environmental distinction, models a future implication, generates an adaptation option from it and returns that option into current capability/S3.

## S5 — Identity / ultimate policy

- State: —
- Function: no material Ravel-level identity/ultimate-policy closure is established in the reviewed standard distribution.
- Disturbance / variety regulated: users approve exact plan revisions, select mission/model/roster settings, grant shell consent and may stop/detach/review/land work, but these are task/current-control/risk decisions rather than a runtime identity or ultimate-policy issue for the Ravel organization.
- Decisive decision or feedback right: not established for an identity/ultimate-policy matter.
- Decision owner: not established.
- Supporting / enforcement mechanisms: exact-plan approval, mission/brief configuration, shell/auto-approve consent, worker confirmation rules, review/land decision path, model/harness selection and operator authentication.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the operator has substantial authority, but human final say over a task plan or worker action is not S5 unless the underlying matter concerns identity/ultimate policy and closes that function.
- Evidence: [`README.md`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/README.md); [`src/main/ravel-model.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/ravel-model.ts); [`src/main/operations/worker-controls.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/operations/worker-controls.ts); [`src/main/operations/core.ts`](https://github.com/zachary-wilde/reigen/blob/6236f47a1b2f3081a0f22bcba47705bcd1680720/src/main/operations/core.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: this negative state does not claim the system lacks policy or authority; it keeps present-work approval, permissions and review at their actual operational functions rather than promoting them to S5.

### Absence scope

- Surfaces inspected: mission/plan creation and exact-revision approval; worker lifecycle/confirmation controls; human-seat path; shell/auto-approve consent; review/landing; harness/model selection and fallback; persistent Core settings; Roundtable/automation surfaces.
- Plausible first-party paths checked: operator mission approval, plan revision ratification, worker detach/stop, reviewed merge/land decisions, safety/permission settings and manager/provider selection.
- Why no material first-party path remains: all inspected authority concerns current task commitments, operational risk, execution permissions or integration of work. No standard runtime path presents an identity/ultimate-policy conflict to an ultimate authority and returns that resolution as policy governing the Ravel organization's identity.

## Summary

| Function | State | Assessment |
| --- | --- | --- |
| S1 | A | First-party Ravel dispatch launches external autonomous coding workers that own task-local reasoning in bounded worktrees. |
| S2 | A | The autonomous manager selects mandatory per-brief scope exclusions specifically to damp parallel worker collisions, and those boundaries return into worker prompts. |
| S3 | A(P) | Event-driven manager turns autonomously regulate the current Ravel from whole-plan/fleet state; the shipped operator path independently closes parent current control through exact-plan approval and worker controls. |
| S3* | C | Conductor supplies an independent worktree verification/ordering/feedback path, but the actual audit criterion/judgment must be supplied by project/operator configuration. |
| S4 | — | Insights, persistence, strategy discussion, scheduling and fallback do not establish external prospective adaptation closure. |
| S5 | — | Plan approval, permissions, mission/model selection and review are operational authority, not identity/ultimate-policy closure. |

The resulting standalone signature is **`A A A(P) C — —`**.