---
harness_id: foe
project_name: Foe
repository: https://github.com/pedapudi/foe
review_ref: 167455955b79ee31e7e8ac3c2ecfff40a6b14ec2
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Foe

## Review boundary

- System in focus: the packaged first-party Foe autonomous coding episode **plus supported `builtin:team` recursive execution mode** at the exact frozen repository revision. The team leader's child episodes are first-party S1 operating units at the selected *team recursion*, not third-party coding agents.
- Purpose and identity: perform finite autonomous coding work against specified task/outcome contracts with permission-constrained tools, verified/typed outcome, append-only evidence, and optionally dynamically delegated concurrent work.
- Relevant environment: source repository and filesystem changes, model results, test/verifier outcomes, delegated worker updates and failures, host/operator-given task and limits, independently configured model endpoints.
- Standard-distribution boundary: the runnable Rust `foe` CLI from its supported `builtin:coding`, `builtin:oneshot` and `builtin:team` contracts, core episode/model/tool runtime, recursive first-party process spawner and team coordination tools, executable permissions, durable journals and child budget pool. The team configuration is packaged in `crates/cli/src/builtin-team.json`.
- Credited operating / distribution surfaces: executable episode `crates/core` / `crates/code`, `crates/contract` and `crates/log`, the first-party `crates/team` board/roster/inbox/overlap/dependency logic, `spawn` child process and budget reservation, first-party `builtin:team` leader/worker/surveyor contracts, supported command-line and Python embedding modes.
- Adjacent first-party surfaces excluded from ownership: tests and conformance under `evals/`, demonstration tasks in `examples/`, model-backed benchmark reports, retrospective trajectory collections/self-improvement experiments, viewer UX, `docs/` future/deferred ideas, contributor governance and CI; source code evidence for runtime behavior is credited, but test actors/research workflow are not borrowed into active S3*/S4/S5 roles.
- First-party operating / deployment modes considered: autonomous single episode; standard opt-in `--config builtin:team` agent team including parallel workers, nested teams and surveyors; Python/host protocol embedding (host supplies model endpoint but does not inherit decision rights). No unproven always-on control plane across unrelated installations is asserted.
- Recursion level: one task-bounded root team, containing a lead S1 and separately running child coding/answer S1 units; each child can lead a subordinate team, preserving explicit hierarchy.
- Reviewed revision: `167455955b79ee31e7e8ac3c2ecfff40a6b14ec2` (frozen `main` ref from Index #848).
- Observation date: 2026-10-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/README.md) describes the executable single-episode model/tool loop and the shipped `builtin:team` mode rather than promising a forthcoming feature. [crates/core/src/loop_.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/loop_.rs) owns episode state transitions, prompt/tool loop, logs, verification/retry/outcome, while [crates/core/src/registry.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/registry.rs) and [crates/code/src/lib.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/code/src/lib.rs) provide constrained work tools. [crates/contract/src/document.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/contract/src/document.rs) resolves executable contracts, grants, budgets, child contracts and outcome predicates. [crates/core/src/spawn.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/spawn.rs) / [crates/core/src/wiring.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/wiring.rs) link separately executing child episodes with reserved budgets to the parent. Every child has its own append-only log, contract, inbox and sandbox.

At team recursion, [crates/team/src/lib.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/team/src/lib.rs) owns the log-projected task board, scoped messages, overlap guard and dependency-aware scheduler, with `spawn`, `wait`, `steer`, `cancel`, `send`, `ask` and `team` tools. [crates/cli/src/builtin-team.json](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/cli/src/builtin-team.json) is a *shipped, directly selectable contract*, giving a lead model an explicit task-decomposition/priority/partition/worker-followup mandate. The lead makes discretionary allocation, adjustment and integration decisions, while the kernel enforces that granted write roots cannot overlap live worker roots and reservations fit budgets. The runtime returns child outcomes and status to the lead through its own journal/inbox and future model requests, making this a viable multi-agent operating mode rather than a generic SDK from which such a team could hypothetically be written.

Single-episode `--config builtin:oneshot` does not itself claim team-level S2/S3. Team mode is the concrete positive evidence. [docs/design.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/design.md) sections "Agent teams" and "The episode" describe causal wiring; [crates/team/src/lib_test.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/team/src/lib_test.rs) tests overlapping roots, scheduling/dependency updates, message delivery and bounded question waiting. Local views and logs aid reconstruction but do not independently own decisions.

## Operational model

One episode calls the model with task/inbox/working context; the model chooses tool calls and/or a typed outcome; runtime enforces capability grants, receives tool results, verifies completion and issues further turns or a terminal outcome. In `builtin:team`, the lead model decides which subtasks require another operational episode, reserves distinct write scopes, creates child tasks by `spawn`, and receives their outcomes, messages and actual progress via the board and `wait`. Its discretion can then retask/steer/cancel a child, answer a time-bounded question, amend unfinished work, integrate accepted results and decide whether the root commitments are fulfilled. Scheduler, log and budgets enforce and transport those choices; they do not make the leader's problem-specific decisions for it. The operator fixes the outer task and allowance; no organization-wide human governance mode is imputed from that.

## S1 — Operations

- State: A
- Function: execute one bounded code investigation/edit/test/report task through model-guided tool use and environmental feedback.
- Disturbance / variety regulated: different source tree/test observations, errors, model/tool outputs, tool denials, returned messages and task-specific constraints.
- Decisive decision or feedback right: choose what source/tool/action to inspect or modify next and when to report a solution, blockage or need for assistance.
- Decision owner: the model-driven episode actor, inside the first-party Foe autonomous `run` loop; externally hosted inference computes responses but does not supply a separate harness's execution/control organization.
- Supporting / enforcement mechanisms: Rust tool registry and coding functions, sandbox/grants, logged model turns, budget, completion verifier and typed outcome.
- Closure path: objective/inbox → model-request → proposed tool call → first-party validated dispatch → result recorded in log → next model observation/action or terminal verified outcome.
- Boundary reachability: standard `foe` executable with built-in coding/oneshot/team contracts launches this first-party loop without borrowing an external coding-agent CLI, eval fixture or user-authored work scheduler.
- Why this is / is not agent-owned: model chooses task-specific actions and reacts to feedback; deterministic constraints veto unsafe/over-budget work but cannot choose the semantic next solution step by themselves.
- Evidence: [README.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/README.md); [crates/core/src/loop_.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/loop_.rs); [crates/cli/src/run.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/cli/src/run.rs); [crates/code/src/lib.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/code/src/lib.rs); [docs/design.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/design.md).
- Basis: explicit shipped wiring and code.
- Confidence: high.
- Caveats: a deliberately model-less deterministic workflow alone would not justify S1=A; positive evidence is actual model/tool episode.

## S2 — Coordination

- State: A
- Function: attenuate work interference and oscillation between distinct concurrently operating child episode S1s in a team, especially contested mutable code paths and task dependency cycles/overlap.
- Disturbance / variety regulated: two S1s trying to modify overlapping filesystem scopes, stale dependent work launched too early, messages/questions that would induce duplicate or conflicting efforts.
- Decisive decision or feedback right: select independent/non-overlapping work partitions, keep shared surfaces with the lead, order dependent units, and revise subordinate work when child results or risks change. This is a specific model-directed coordination judgment; the kernel's overlap refusal is the enforcement layer.
- Decision owner: the first-party model-driven team lead exercising `spawn`, `blocked_by`, `send`, `steer`, `cancel` and `wait` in the shipped `builtin:team` contract; the deterministic board denies invalid overlapping roots and prevents concurrent writers.
- Supporting / enforcement mechanisms: canonical path overlap check on board admission and at child launch, dependency DAG, unique task assignment, single-writer log projection, per-child grants/sandbox, peer-message delivery with reply ids/deadlines.
- Closure path: leader partitions tasks → `Team::delegate` rejects an overlapping current write root unless dependent → scheduler admits disjoint ready children with restricted grants → child outcomes and notifications return through durable team log/board/inbox → leader's next model turn revises/continues partition, or reorders/cancels affected work.
- Boundary reachability: `builtin:team` provides this rule explicitly and provides model-callable coordination tools; separately launched child processes, scoped grants and board are part of the shipped CLI/runtime distribution.
- Why this is / is not agent-owned: the lead's task-specific choice of conflict-free partition and follow-up from actual worker feedback is not determined by the static scheduler. Removing the lead's model leaves mechanical collision rejection/dependency order but removes the actual substantive team-level response to coding conflicts; this distinguishes owner from enforcer.
- Distinct S1 units: separately running worker and surveyor episodes with their own model/tool loops or read-only task outcome, in the root team; recursive children may add subordinate teams.
- Inter-S1 disturbance: potential simultaneous writes under the same source directory, incompatible edits to shared interfaces, dependent changes proceeding before prerequisites and worker waiting/communication stalling.
- Attenuating coordination relation: leader-authored partition/ownership rules, immutable in-boundary child grants, overlap-refusal and dependency gating, bounded reply correlation and cancellation.
- Feedback into subsequent S1 behaviour: board/task revisions and child outcome/inbox evidence influence leader's next spawn/steer/cancel/integration decisions, and those decisions return to affected child tasks.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: concurrent autonomous child S1s share writeable source resources, the code detects *specific overlapping write conflict* before launch, and leader-owned adaptive partition/replanning responds with enforced new S1 boundaries. This is concrete interference attenuation beyond mere channels or task-order fields.
- Evidence: [crates/cli/src/builtin-team.json](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/cli/src/builtin-team.json); [crates/team/src/lib.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/team/src/lib.rs); [crates/team/src/lib_test.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/team/src/lib_test.rs); [docs/design.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/design.md); [crates/core/src/spawn.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/spawn.rs).
- Basis: explicit causal code, supported built-in mode and structural owner test.
- Confidence: medium-high.
- Caveats: `A` is limited to a model-driven lead in builtin team mode; kernel-only overlap enforcement is deterministic and would not separately be S2=A. Local quality/correctness of final merged code is not guaranteed by partitioning.

## S3 — Inside-and-now control

- State: A
- Function: regulate whole-current commitments, bounded resources, team membership and intervention at the declared single-root-team recursion.
- Disturbance / variety regulated: insufficient child capacity or token/time budget, blocked dependencies, failed/cancelled workers, incomplete/unaccounted deliverables, unnecessary or wrong delegated units.
- Decisive decision or feedback right: from a team-wide board/roster and returned worker outcomes, decide which unit to perform internally, which child to spawn and with what scope, which child to steer or cancel, and how/when to integrate accounted work or exit.
- Decision owner: the model-driven lead episode in `builtin:team`. `Team::schedule`, budget pool, verification and log are bounded machinery executing decisions rather than owning team-level discretionary work/commitment allocation.
- Supporting / enforcement mechanisms: task board with `queued/running/terminal` revisions and owner/dependencies, roster, shared child budget reservations and releases, `team`/wait tools, bounded completion accounting, stop and recovery.
- Closure path: leader reads the current team/task/worker state → chooses spawn/steer/cancel/wait/reallocation/integration → admission, execution and status changes are journaled and enforced → next model turn sees settlement/progress and can revise current commitments.
- Boundary reachability: packaged built-in `team` lead and team tools operate in the normal binary without a separate coordinator service, external human dispatcher or development-only example.
- Why this is / is not agent-owned: the lead chooses *which work and constraints to commit* in light of current whole-team state; deterministic budget rules, task statuses, and verifier account checks only transport and enforce those choices.
- Whole-system current view: team-wide log-projected task board (task id, owner, status, dependencies, write scopes, outcomes), roster, messages, and shared descendant budget accounting at this team's recursion, via first-party `team`, `wait`, and task-result surfaces.
- Current-control decision scope: delegation, prioritization of current units, disjoint grants, current resource reservations (within declared ceilings), intervention/cancellation, task accounting and final integrated commitments; not ultimate organization-wide policy.
- Evidence: [crates/cli/src/builtin-team.json](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/cli/src/builtin-team.json); [crates/team/src/lib.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/team/src/lib.rs); [crates/core/src/loop_.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/loop_.rs); [crates/core/src/budget.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/budget.rs); [docs/design.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/design.md).
- Basis: explicit shipped loop and agent-decided team regulation.
- Confidence: medium-high.
- Caveats: S3 belongs to **this root team's recursion**, not Foe-wide stewardship across different user installations. No positive parent-governed variant inferred from an operator providing the initial task or inspecting the viewer.

## S3* — Complementary audit

- State: —
- Function: no *complementary independent organizational* inspection and corrective-return relationship distinct from the normal root lead/episode feedback is established in supported runtime modes.
- Disturbance / variety regulated: incorrect coding changes, verifier errors, missing task accounting or unsafe execution.
- Decisive decision or feedback right: a complementary actor would independently inspect direct evidence about current operation, challenge ordinary S3 reports, form an audit finding and cause a corrective decision/return.
- Decision owner: the configured verifier/tool produces determinate acceptance/findings as part of ordinary execution; team lead accounts for units and responds to returned findings; no separate independent S3* corrective authority is shipped.
- Supporting / enforcement mechanisms: `done_when.verify` and verifier result events, append-only logs, final outcome evidence, lead's `wait`/task accountability, sandbox/grants and optional viewer/benchmark reports.
- Closure path: verifier reports can trigger same episode's retry or failure; child outcome reports can trigger lead response. No separate independently owned complementary audit path into S3 is demonstrated.
- Why this is / is not agent-owned: model tool feedback or externally authored deterministic verifier is ordinary quality control, and read-only surveyors are task contributors, not guaranteed independent evidence auditors with corrective return rights.
- Evidence: [crates/core/src/loop_.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/loop_.rs); [crates/cli/src/builtin-team.json](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/cli/src/builtin-team.json); [docs/evidence.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/evidence.md); [docs/design.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/design.md); [docs/evaluation.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/evaluation.md).
- Basis: bounded source-negative mapping.
- Confidence: medium-high.
- Caveats: a particular configured independent code audit episode can be constructed; no mandatory first-party S3* arrangement or dedicated audit correction path in standard modes is evidenced.

### Absence scope

- Surfaces inspected: runtime verifier and outcome events, model/team reviewer/surveyor contracts, append-only logs, viewer and evidence bundle, examples/CI/evaluations.
- Plausible first-party paths checked: separate verifier grants and executable fingerprint, task-accounting rejection, read-only surveyor reports, cross-episode direct log access and retrospective evaluation feedback.
- Why no material first-party path remains: these are normal task-time validation/reporting or external tests. None is a shipped separate audit actor holding an independently obtained direct-evidence judgment and an established corrective-return right into root team's current operations.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped prospective environmental/capability adaptation loop returning from external future intelligence to the operational team's capability baseline.
- Disturbance / variety regulated: evolving coding ecosystem, new threats/provider interfaces, accumulated failures and hypothetical future runtime improvements.
- Decisive decision or feedback right: independently select future capability/strategy changes based on outside/forward-looking evidence and return adaptation to currently executing coding organization.
- Decision owner: human operators/maintainers choose upgrades and configuration; local model may propose coding changes *as its task*, but the standard runtime does not own autonomous future organizational adaptation.
- Supporting / enforcement mechanisms: generic coding/edit tools, optional task-specific research, log history, candidate workflows and trajectory evidence, manually selected self-improvement workflows.
- Closure path: `examples/self-extension` and `evals/terminal_bench` can assess evidence and suggest edits in isolated evaluation tasks, but are adjacent eval/demo workflows and do not automatically promote a runtime/capability change into ordinary deployed Foe operations.
- Why this is / is not agent-owned: changing some code under a coding task is ordinary S1; neither task-specific model planning nor append-only learning artifacts autonomously chooses future whole-harness adaptation from external environment.
- Evidence: [docs/self-improvement.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/self-improvement.md); [docs/deferred.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/deferred.md); [docs/design.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/design.md); [README.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/README.md).
- Basis: explicit documented limitation and bounded absence.
- Confidence: high.
- Caveats: Foe's research reports describe bounded source-edit loops but explicitly say autonomous selection/promotion/general self-improvement remain unsupported; no inference that S4 is impossible to build atop its runtime.

### Absence scope

- Surfaces inspected: first-party episode and team modes, compaction/log persistence, task-specific model planning, self-extension example and research eval workflows, deferred features.
- Plausible first-party paths checked: replay/cross-run evidence diagnosis, model-chosen prospective capability improvement, runtime config/contract mutation, promotion/redeployment after evaluation.
- Why no material first-party path remains: shipped ordinary runtime's decisions are task-bounded; development/evaluation workflows require externally selected tasks and separately controlled source promotion, with explicit upstream limitation against general autonomous adaptation closure.

## S5 — Policy and identity

- State: —
- Function: the runtime enforces author-defined operational grants and contract values but no independently closed ultimate identity/policy governance function exists at selected team recursion.
- Disturbance / variety regulated: unsafe tools, write authority, budget and task scope, blocked questions and possible policy conflicts.
- Decisive decision or feedback right: decide or legitimately escalate ultimate purpose/identity conflicts beyond current work, return binding resolved policy to ongoing operations.
- Decision owner: human/operator authors outer contract and permissions; children are granted only narrower scoped contracts. Model lead cannot legitimately override the organization's ultimate source of authority.
- Supporting / enforcement mechanisms: immutable contract fingerprints, grants and path overlap, permission/sandbox checks, role-defined child contracts, typed completion outcomes, agent `ask` and `block`.
- Closure path: pre-authored rule → kernel enforcement. Bounded question/answer and ordinary task routing can return an operational answer, but no first-party ultimate identity-level dispute → legitimate authoritative adjudication → new organizational policy → subsequent governed operations path.
- Why this is / is not agent-owned: an immutable access boundary or model choosing to self-block is operational safety, not S5 ultimate values; operator ability to launch/update an episode is not an S5 parent-governance mode.
- Evidence: [crates/contract/src/document.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/contract/src/document.rs); [crates/core/src/grants.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/core/src/grants.rs); [crates/team/src/lib.rs](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/team/src/lib.rs); [crates/cli/src/builtin-team.json](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/crates/cli/src/builtin-team.json); [docs/design.md](https://github.com/pedapudi/foe/blob/167455955b79ee31e7e8ac3c2ecfff40a6b14ec2/docs/design.md).
- Basis: source-bounded absence.
- Confidence: medium-high.
- Caveats: individual host institutions could implement identity/policy governance using the host protocol, but this is separate from the frozen standard distribution.

### Absence scope

- Surfaces inspected: contract schema/document/fingerprints, all tool and child grants, parent/child team authority, interrupt and question primitives, host protocol, operator/viewer and contributor docs.
- Plausible first-party paths checked: model-generated child authority escalation, lead's authority to change own grant envelope, parent-assisted policy adjudication, human/host override and recursive governance modes.
- Why no material first-party path remains: external operator chooses the contract once, kernel enforces invariants and child permission attenuation; the active episode has no shipped ultimate-policy dispute owner or returned binding identity-level change process in its declared supported mode.

## Distributed OSS parent arrangement

The public source can be maintained and used by independent contributors; a particular operator supplies credentials, completion predicates and grants for a local episode. No shared first-party organization-wide cross-installation parent current-control, S4 future adaptation or S5 ultimate-policy return channel follows from those separate activities. Team lead/worker authority remains at one runtime root-team recursion rather than inheriting maintainer governance. No unsupported `(P)` mode is asserted.

## Self-hosted and non-human modes

The local CLI permits a human to provide the initial task, grant capabilities or examine outcome evidence; this is initial specification/observation, not automatically an operationally complete parent-governed S3/S4/S5 function. The positive S2/S3 claims depend on the **first-party model-guided `builtin:team`** configuration, where the lead chooses actions from live board and child feedback and the kernel enforces authority boundaries. Other configurations may have only S1.

## Recursion

Each child is independently running S1 in its parent's team and also can be a lead for a nested team. `Team::delegate`, `Team::schedule` and its parent/child logs implement the recursive composition; organizational labels must be interpreted relative to the explicit current root team. A hierarchy of processes does not supply arbitrary higher VSM functions on its own.

## Variety and escalation

Variety includes unbounded source changes and model responses but is attenuated operationally by task/permission limits, bounded budgets/outcomes, constrained disjoint team scopes, dependency ordering and deadline-driven question correlation. Workers can ask their lead and block for one identified reply; when unanswered, a typed deadline/default avoids indefinite wait. Child failure/blocked status reaches lead's board and must be accounted for, potentially causing model revision. These are team coordination/current-control loops rather than proof of a separately governed S5 or independent audit.

## Evidence gaps

- No model/provider-backed live coding benchmark was executed in this assessment. Shipped code, standard contracts, implementation tests and immutable primary-source documentation support structural claims, not the empirical success rate of model decisions.
- S2=A and S3=A are **mode-qualified** to the shipped `builtin:team` leader. Their specific first-party rights and feedback paths are source-grounded, but no claim is made for every possible user-provided standalone contract. Kernel overlap/budget checks alone would support enforcement, not autonomous decision ownership.
- A concrete user-authored third-party reviewer, external policy governor or prospective improvement agent may augment the runtime. It is outside the standard distribution unless first-party, reachable and closed at the assessed boundary.
- Tests and self-improvement examples are considered for absence/counterfactual checks, but their actors are not silently promoted into production control functions.

## Assessment summary

**Proposed disposition: `included`.** Source-bounded vector `S1=A / S2=A / S3=A / S3*=— / S4=— / S5=—`. The positive metasystem claims are specific to the **shipped opt-in model-directed team mode**, whose lead partitions conflicting worker writes, manages live team commitments, and acts on recorded worker feedback; they do not follow from generic orchestration labels. No independent reviewer/semantic approval is claimed merely by writing or structurally checking this assessment.
