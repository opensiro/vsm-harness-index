---
harness_id: agentwork
project_name: agentwork
repository: https://github.com/Sinkear/agentwork
review_ref: 3aecbef55ac694d64cb77403092aa850279b60a8
reviewed_at: 2026-11-05
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

# agentwork

## Review boundary

- System in focus: One `agentwork` domain/goal organization managed by the first-party Go daemon/service and its explicitly launched CLI agent owner, task assignees, optional sub-goal verifier and single human operator.
- Purpose and identity: Run a user's goal through agent assignments, delegated sub-goals, conflict-aware integration, machine/agent verification and human-gated delivery while preserving goal-level authority and crash-recoverable state.
- Relevant environment: User-defined domain acceptance policy and project, Git worktrees and branches, external ACP/JSONL/JSON-RPC CLI agents, separate machine or agent verifiers, Git hosting/tracker and Feishu notifications, run failures and human decisions.
- Standard-distribution boundary: First-party Go daemon/connector, service state machines, `agentwork` CLI shim, SQLite, web goals UI, per-run worktrees and compiled domain checks. Agent backends/transports provide external operational models but their internal control loops are excluded.
- Credited operating / distribution surfaces: [README operating model](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/README.md), [collaboration contract](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/Collaboration.v2.md), [goal reconciliation and owner wake](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/goal.go), [sub-goal verification/conflict return](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/subgoal.go), [role-isolated worktrees](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/daemon/daemon.go), [verification evidence](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/daemon/verify.go).
- Adjacent first-party surfaces excluded from ownership: `DESIGN.md` aspirations not implemented at the frozen ref, GitHub/Feishu providers' internal autonomy, unit-test mocks, marketing or website claims, external CLI agent architectures and developer maintenance scripts.
- First-party operating / deployment modes considered: Agent-owned goal/squad-leader delegation with optional distinct verifier; machine-only verification; conflict → assignee rework; consult/handoff; human-assigned manual placeholder; squad reviewer comment plus human approval; domain-policy checkpoint and delivery.
- Recursion level: One goal with sub-goal work units at the next operational layer, serviced by owner/goal control; sub-goals are explicitly not recursive child goals and are not credited their own full VSM metasystems.
- Reviewed revision: `Sinkear/agentwork@3aecbef55ac694d64cb77403092aa850279b60a8` (MIT).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The goal row, not a terminal run's self-report, holds authoritative lifecycle and ownership. A goal can be assigned to an agent or a squad leader, who receives a run token linked to the `(goal, agent, role)` identity, reads the goal/sub-goal/change state, chooses owner-only handoff, consult, sub-goal creation and change integration. Assignees operate in separate per-run Git worktrees, and every sub-goal has a separately tracked result/verification state. Reconcile reads authoritative SQLite changes, derives `OwnerAttention` (`integration`, `recovery`, `user_action`) and conditionally enqueues one owner successor run, injecting the current actionable work; a human owner receives attention without an agent run. The coordinator is deterministic and does not perform integration in the owner agent's place.

A verified sub-goal produces a `Change` and revision pinned to a merge base. Owner integration can yield a Git conflict after another sub-goal altered that base. `MarkChangeIntegrated(false)` atomically records `conflict`, returns that sub-goal to `running` and enqueues the assignee to rework on a fresh base; a new revision then returns as `ready` for owner integration. By contrast, default machine verification executes domain-check commands. In the explicitly supported `verifier_id` mode, an independently scheduled `verify` agent receives a detached Git snapshot and may issue a structured `passed`/`rejected` verdict; the latter atomically returns the work to assignee rework. Squad reviewer opinions have no decision authority; human checkpoints approve/reject/reassign goals, with rejected reasons returned to owner successor runs. See [goal reconciliation](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/goal.go#L2130-L2270), [conflict return](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/subgoal.go#L552-L627) and [verifier snapshot](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/daemon/daemon.go#L1450-L1488).

## Operational model

The owner model receives a current-goal assignment and can create task sub-goals, consult helpers, transfer ownership and decide which verified `Change` to integrate. The daemon's deterministic role/lifecycle checks and event-triggered reconciliation prevent duplicate authority and return necessary actions to the right actors. A separate verifier may inspect the actual submitted work before integration; default machine checks alone are not classified as agent-owned S3*. A human operator sets domain acceptance/gates and has a direct reject-to-owner corrective loop. This is a goal-specific viable arrangement, not an arbitrary aggregation of all user projects.

## S1 — Operations

- State: A
- Function: CLI-model execution of assigned goals and delegated sub-goal code/work tasks, with context and tool-result feedback.
- Disturbance / variety regulated: Changing repo contents, requirements, test failures, independent reviewer verdicts, integration-base shifts, consulted advice and human rejection reasons.
- Decisive decision or feedback right: Choose substantive work/edits/tool calls and responses in owner/sub-goal runs; local assignee chooses how to repair a rejected or conflicting revision.
- Decision owner: External connected CLI model running under first-party `agentwork` role/identity token as an explicit operational actor.
- Supporting / enforcement mechanisms: Daemon/machine dispatcher, per-run worktree, assigned agent persona, ACP/JSONL/JSON-RPC transport, role-scoped CLI, timeouts/watchdogs, stateful resume and Git worktree snapshot.
- Closure path: Human goal → owner run/model plans/directs → assignee model executes local project changes and reports → run terminal/verification signals → feedback/wake/context into successor agent turns → revised task or completion.
- Boundary reachability: Documented `agentwork connect` launches configured agent CLI runtimes on machine dispatch, and the first-party service creates owner/sub-goal runs with explicit role context.
- Why this is / is not agent-owned: The models decide which sub-goals to create, tools to invoke and code changes to make; deterministic state reconciliation and permission checks are support, not task reasoning.
- Evidence: [README quick start](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/README.md), [run prompt assembly](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/daemon/daemon.go#L2888-L3053), [sub-goal creation](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/subgoal.go#L49-L189).
- Basis: explicit + structural first-party operational integration.
- Confidence: High for implemented role/feedback reachability, medium for live external-model behavior.
- Caveats: No authenticated target-domain agent process was launched in this review; internal behaviors of ACP/CLI backends are not imported.

## S2 — Coordination

- State: C
- Function: Detect and attenuate conflicts between independently produced sub-goal changes, directing the responsible assignee to rebase/rework rather than silently integrating an incompatible revision.
- Disturbance / variety regulated: Different S1 sub-goal units edit against a shared goal branch and create incompatible integration bases or merged changes.
- Decisive decision or feedback right: A failed owner integration marks a specific `Change` conflicting, invalidates its prior verified state and enqueues the same assignee on the latest goal base; owner later chooses integration of a new ready revision.
- Decision owner: First-party constructor-owned service transition and event/goal coordinator establish the S2-specific return, with model owner initiating integration and assignee choosing the concrete repair. No independent agent-owned *S2-specific* attenuation policy is claimed.
- Supporting / enforcement mechanisms: Per-run isolated branches/worktrees, `Change` and ordered revisions, `integrate_change`, conditional transitions, `quality_iteration` and idempotent run enqueue.
- Closure path: Parallel sub-goal outputs → owner integrates one into shared branch → subsequent integration conflict → service marks `conflict` and enqueues affected assignee → assignee reworks against newer base → new revision becomes `ready` → owner retries integration.
- Distinct S1 units: Concurrent independently assigned sub-goal implementation runs, each with its own assignee/worktree and `Change` against the same goal branch.
- Inter-S1 disturbance: A previous sub-goal's integration changes the shared base, making another independently completed change incompatible at merge.
- Attenuating coordination relation: Conflict-specific `MarkChangeIntegrated(false)` returns the disrupted sub-goal to rework instead of accepting stale output; `Change` revision history preserves the old failure/new base relation.
- Feedback into subsequent S1 behaviour: The assignee receives a successor run and prompt text explicitly identifying the prior conflicting `Change` and requirement to resolve it on the new integration base.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A concrete disturbance is generated *between* independently produced S1 changes, then causes a targeted adjustment in the affected peer's subsequent work; static worktree isolation alone is not the positive witness.
- Boundary reachability: The documented sub-goal/change-integration workflow invokes `MarkChangeIntegrated` on failed Git integration, with the recovery path wired into normal owner/assignee runs.
- Why this is / is not agent-owned: The relation is first-party fixed conflict policy (`C`), while agent workers provide the actual revision and owner chooses when/what to merge; no general independent S2 judgment actor is shown.
- Evidence: [collaboration conflict contract](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/Collaboration.v2.md), [conflict transition/rework](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/subgoal.go#L552-L624), [assignee conflict wake](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/daemon/daemon.go#L2998-L3014).
- Basis: explicit + structural constructor control with subsequent operational return.
- Confidence: High for specific first-party conflict-loop mechanics.
- Caveats: `C` does not assert a free-standing model coordinator that negotiates all possible peer conflicts; ordinary consult/handoff alone are not counted as S2.

## S3 — Inside-and-now control

- State: A(P)
- Function: Own and regulate goal-wide current commitments — sub-goal assignment, integration/recovery and handover — with a separate legitimate human intervention mode.
- Disturbance / variety regulated: Competing incomplete sub-goals, failed verifications, ready/conflicting changes, stalled owner runs, disputed acceptance and human-requested rework.
- Decisive decision or feedback right: Agent owner may choose assignees/sub-goals, request help, transfer ownership and integrate ready changes from a current goal-wide state; parent human may redirect/assign and reject a goal in review, returning binding correction to the owner.
- Decision owner: Agent/squad leader owner model in autonomous mode (`A`) under goal-role authority; human operator acting through review/assignment UI/API in parent mode (`P`). Coordinator derives attention but does not make these substantive decisions.
- Supporting / enforcement mechanisms: Goal/sub-goal/change/verification SQLite state, role tokens and `requireOwnerOf`, owner-only CLI, event-driven `OwnerAttention`, guarded single owner run, human review state and feedback comments.
- Closure path: Goal/sub-goal/change status → derived owner attention and current context → owner model allocates or integrates operational commitments → assignee execution and results → persisted state and next owner wake. Parent mode: goal-wide review evidence → human approve/reject/redirect → binding review transition → a rejected goal creates a new owner run with explicit human reason, or approval triggers delivery.
- Whole-system current view: The owner can list goal/sub-goals/changes/verification and sees an actionable wake summary; human UI exposes goal progress, review and changed artifacts. This is the whole declared *goal*, not an unverified cross-domain fleet command center.
- Current-control decision scope: Assigning work to specific S1 units, integrating/reworking their results, changing owner accountability, deciding continuation vs accepted delivery and returning human rejection priorities into next operation; distinct from static concurrency caps.
- Boundary reachability: README and `Collaboration.v2.md` prescribe owner-only subgoal/integration/handoff tools; service rejects non-owner use, wakes owner after actionable changes and records human review decisions via `ResolveReview`.
- Why this is / is not agent-owned: The connected owner model owns substantive task division and integration decisions in agent-assigned mode. The human's accepted/rejected review and reassignment are distinct authorized parent interventions; the daemon only enforces transitions.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Current goal owner agent / squad leader | Ready changes, sub-goal failures and new actionable state | Owner model creates/reassigns work, integrates or handoffs; changed sub-goal state returns via reconcile | `goal.go` owner attention, `subgoal.go` and owner CLI roles |
| Parent (`P`) | Human operator | Goal review checkpoint, rejected deliverable or manual reassignment | Review reject/redirect records reason and resumes owner agent with corrected instruction; approve delivers | `goal.go` `ResolveReview`, review UI/README |

- Evidence: [goal owner attention and whole state](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/goal.go#L2130-L2270), [human review return](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/goal.go#L1489-L1705), [owner commands and roles](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/Collaboration.v2.md), [README goal layer](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/README.md).
- Basis: explicit + structural autonomous and separate legitimate parent return.
- Confidence: Medium-high for scoped goal control; live model decision quality not verified.
- Caveats: Human-assigned `assignee_type=human` goals are manual placeholders (no autonomous owner run), not proof that every parent mode retains autonomous control. This score does not imply S3 authority over all independent domains or tenant organizations.

## S3* — Complementary audit

- State: A
- Function: Separately assigned agent verifier checks a sub-goal's actual output from an independent stable snapshot and can reject work before owner integration.
- Disturbance / variety regulated: An assignee reports `completed` while produced code/result violates the sub-goal's declared requirements or quality expectations.
- Decisive decision or feedback right: Named verifier agent issues structured `passed` or `rejected` with evidence through `verify_sub_goal`; rejected verdict prevents Change admission and enqueues another assignee run.
- Decision owner: Explicitly configured distinct `verifier_id` model acting in `role=verify`; platform authenticates verdict to that named verifier and owns deterministic state transition.
- Supporting / enforcement mechanisms: Detached Git snapshot for verifier, separate verify run identity, no owner role authority, persisted `verification_result`, agent-specific verdict tool and assignee rework loop.
- Closure path: Assignee completes and source revision is frozen → verification run inspects stable snapshot → verifier model returns verdict/evidence → platform records result → `rejected` reopens task and enqueues the assignee with rejection summary, `passed` creates a ready Change for owner.
- Claim being audited: The assignee's produced sub-goal deliverable is complete/valid enough to become an integrable `Change`.
- Ordinary reporting path: Assignee's run completion, summary, commits and domain machine-check output recorded on the goal and sub-goal.
- Complementary access path: Dedicated verifier run in a detached snapshot of the submitted sub-goal branch can inspect real work/files and issue independent verdict/evidence; named verifier's `verify_sub_goal` call, not assignee self-report, closes the audit.
- Independence boundary: Distinct configured verifier agent/worktree/run/role versus assignee, with a stable detached submitted ref. Service verifies verifier identity, status and running verdict window; a single-actor configuration or default machine verification does **not** demonstrate independent agent audit. The code validates the named `verifier_id` but does not categorically forbid configuring it equal to assignee ID, so independence must be configured.
- Who acts on findings: Service immediately transitions rejected sub-goals into new assignee work with `quality_iteration` increment and rejection summary injected; passed work goes to owner integration. Squad reviewer comments are separately human-advisory and are not the source of this positive claim.
- Boundary reachability: The `sub_goal` API supports `verifier_id`, daemon dispatches `role=verify` on a stable source snapshot and `VerifySubGoal` commits the verdict plus subsequent correction run. This is a first-party standard optional mode.
- Why this is / is not agent-owned: A model verifier decides the substantive completion judgment on independent source evidence; routine machine verification/guardrails are supporting checks only.
- Evidence: [sub-goal creation/verifier ID](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/subgoal.go#L49-L135), [verdict authority and rework](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/subgoal.go#L435-L551), [detached verifier workspace](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/daemon/daemon.go#L1447-L1464).
- Basis: explicit + structural complementary audit mode.
- Confidence: High for first-party configured verifier control, medium for actual independence when an operator does not select distinct agents.
- Caveats: Default verifier is machine-command-based and not a positive *agent* S3* by itself; human review of squad opinions remains the human's verdict. Role-level sandbox relies on first-party worktree/role implementation and external execution environments.

## S4 — Outside-and-then intelligence

- State: —
- Function: No established agent-owned or parent-closed prospective adaptation of the domain/goal organization's future capabilities.
- Disturbance / variety regulated: New tracker issues, schedules, acceptance failures and historical task results affect current/recurring work, not a decision on future organization design.
- Decisive decision or feedback right: Human defines domain policy and runtime/agent configuration; a processor can compile natural-language acceptance rules, but has no authority to choose prospective strategic changes in a future environmental model.
- Decision owner: Operator for domain acceptance/agent roster; active agents for present work only.
- Supporting / enforcement mechanisms: Policy-text compilation to deterministic checks, history, gate statistics, cron/issue triggers and domain reporting.
- Closure path: Human policy → checks/gates → operational verification/delivery; schedule → clone current goal. Neither is environmental futures → adaptation options → strategic selection → reconfiguration return.
- Why this is / is not agent-owned: Acceptance-policy compilation and recurring triggers are present control configuration, not prospective intelligence about external future requirements.
- Evidence: [policy and trigger overview](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/README.md), [domain policy configuration](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/DESIGN.md).
- Basis: bounded structural absence.
- Confidence: Medium-high.
- Caveats: A human may use historical results to redesign future capabilities outside this bounded first-party loop.

### Absence scope

- Surfaces inspected: Domain acceptance policy/compiler, schedules/triggers, goal reconciliation, cross-run feedback, history and review decision metrics.
- Plausible first-party paths checked: Cron as future strategy, policy compiler as S4, learning from review stats as prospective adaptation, owner planning as future environmental intelligence.
- Why no material first-party path remains: These generate/verify current tasks or expose retrospective statistics; no owned future-environment distinction and consequential new operating-capability decision path is established.

## S5 — Policy and identity

- State: —
- Function: No declared closed ultimate-purpose/identity arbitration authority beyond human domain acceptance and operational gates.
- Disturbance / variety regulated: Unapproved side effects, assignee role violation, poor task quality and agent handoff loops are bounded by service/human gates.
- Decisive decision or feedback right: Human may define domain acceptance, approve/reject a goal or stop a handoff loop; those are goal acceptance/operational continuation decisions rather than enduring identity/purpose arbitration.
- Decision owner: Single human operator for policy configuration and review actions; deterministic service for permission checks. No recurring S5 issue adjudicator distinct from S3 control.
- Supporting / enforcement mechanisms: Goal ownership authority, role tokens, acceptance-policy freeze, human checkpoint, handoff-loop guard and audit logs.
- Closure path: Human config → operational acceptance checks/permissions, or review → goal rejection/approval → next run/delivery; no mission/identity conflict → legitimate ultimate-policy judgment → changed binding constitution.
- Why this is / is not agent-owned: Human final approval does not automatically imply VSM S5; even a domain policy string is an execution constraint rather than an ultimate organizational identity dispute loop.
- Evidence: [domain/goal policy](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/README.md), [review resolution](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/goal.go#L1489-L1705), [role authority](https://github.com/Sinkear/agentwork/blob/3aecbef55ac694d64cb77403092aa850279b60a8/internal/service/goal.go#L873-L936).
- Basis: bounded structural absence.
- Confidence: Medium-high.
- Caveats: Ultimate identity/purpose decisions may exist in the real operator's institution, outside this open-source single-user software boundary.

### Absence scope

- Surfaces inspected: Goal/domain policy, gate decisions, human review/handoff, permissions and acceptance-policy compilation, owner role/lifecycle.
- Plausible first-party paths checked: Human approve/reject as S5, frozen domain checks as constitutional mandate, owner handoff-loop adjudication as ultimate policy arbitration.
- Why no material first-party path remains: All decisions are tied to current goal success, assignment or side-effect permission; no first-party actor handles and returns a distinct ongoing identity/ultimate-policy dispute.

## Recursion

Sub-goals are deliberately not child goals; they inherit the parent goal's authority and produce scoped Changes. The owner/assignee/verifier roles form one organizational level with internal operating units, not a nested tree of fully viable independent organizations. A squad is a routing group with a leader, not another automatically viable S1 firm.

## Variety and escalation

Owner-selected subgoal fanout and diverse backends amplify execution variety. Worktree isolation, owner-only permissions, verifier identity and bounded failure attempts attenuate risks. Merge conflict generates specific S2 corrective returns; optional direct-source verification generates S3* feedback; owner goal-state decisions and human review/reject control current commitments. Watchdog/handoff loops and weak verification can escalate to a human. No separate S4 or S5 is inferred from the control-plane vocabulary.

## Evidence gaps

- Code-traced repository-first assessment at frozen ref; no live connected ACP/CLI agent, Git host delivery or Feishu review was exercised. Tests and documents are structural support only.
- Independent verifier requires a distinct configured agent; `CreateSubGoal` does not enforce inequality between `assignee_id` and `verifier_id` globally. Default machine checks and squad reviewer comments alone are not claimed as autonomous S3*.
- Parent S3(P) is the human's explicit goal review/reject/assignment return, not an assertion of independent human enterprise-wide portfolio governance.
- Negative S4/S5 findings apply to the declared single-user goal control product rather than a wider deploying organization.
