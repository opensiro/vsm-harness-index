---
harness_id: soothe
project_name: Soothe
repository: https://github.com/mirasoth/soothe
review_ref: be4fa14c0aa53203b8861dbff367eccb0df77668
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Soothe

## Review boundary

- System in focus: one first-party Soothe deployment at pinned revision `be4fa14c0aa53203b8861dbff367eccb0df77668`, including `StrangeLoop`, `CoreAgent`, `ContextEngine`, LoopRail selection/interpreting/builtins, the daemon/runner surfaces that launch loops, and the pinned first-party `soothe-nano` runtime dependency.
- Purpose and identity: execute user goals through persistent model/tool loops while supporting goal-DAG planning, rail-governed multi-goal orchestration, delegated workers, review/recovery workflows, and daemon/CLI operation.
- Relevant environment: user objectives, local workspaces and git repositories, external model providers, web/research sources, human approvals/clarifications, and downstream applications that may compose the exported rail/guard primitives.
- Standard-distribution boundary: current loop-native Soothe runtime at the frozen revision. The retired standalone `soothe-autopilot` package and removed daemon `AutopilotService` are historical evidence only and are not credited as current autonomous owners.
- Credited operating / distribution surfaces: standard runner/daemon → StrangeLoop execution; current ContextEngine goal/DAG state; explicit or automatically selected LoopRails; shipped builtin rails; public `soothe.rails` exports including `LoopRailInterpreter(guards=...)`, `GuardEvaluator`, `LLMGuardEvaluator` and CE-facing rail builtins; the pinned first-party `soothe-nano` CoreAgent runtime where reached through Soothe's normal host wiring.
- Adjacent first-party surfaces excluded from ownership: repository-development tests, archived implementation notes/RFC implementation plans, stale documentation describing the removed `soothe-autopilot` or daemon `AutopilotService`, examples that are not reached from the frozen runtime, and generic research/evaluation artifacts except where current production wiring corroborates them.
- First-party operating / deployment modes considered: normal StrangeLoop execution; explicit or automatically selected LoopRails; daemon/runner launch with `autopilot_rail_id`; ContextEngine multi-goal execution; builtin maker-checker and greenfield rail patterns; research and skill retrieval paths.
- Recursion level: one Soothe deployment/job is the assessed organization. Individually executing model/tool goals or maker goals are S1 operational units when the rail/ContextEngine path instantiates them as distinct loops. The user/operator and downstream integrator remain environment/parent actors unless a first-party loop closes the relevant decision right.
- Reviewed revision: `be4fa14c0aa53203b8861dbff367eccb0df77668`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Soothe is centred on `StrangeLoop` and `ContextEngine`. `StrangeLoop` drives one goal through a model/tool execution loop, while ContextEngine persists a multi-goal DAG with priorities, dependencies, lifecycle state and claim/complete/fail/retry operations. The daemon and runner feed work into this runtime. A LoopRail can be selected explicitly or by an LLM selector and bound to a running job to provide job-scoped orchestration policy.

The frozen revision is in the middle of an architectural consolidation: the former daemon-owned `AutopilotService` has been removed and Autopilot behavior has been folded into loop-native rail execution. Current `StrangeLoop.run_with_progress()` constructs a `LoopRailInterpreter` when a rail id is supplied, but it does so without a `GuardEvaluator`. The interpreter fail-closes named/natural-language `when` rules when no evaluator is installed. This matters because the shipped maker-checker and greenfield rail definitions rely heavily on named conditions such as `needs_check`, `maker_needs_merge`, `needs_feedback`, `branch_is_stuck` and `needs_qa`.

At the same time, this is not merely speculative documentation. The first-party package intentionally exports `LoopRailInterpreter`, `GuardEvaluator` and `LLMGuardEvaluator`; the interpreter explicitly accepts a guard evaluator; the guard implementation receives current job/event/goal/sibling/tag/retry and structural state; and the rail builtins implement concrete goal spawning, worktree/merge handling, retry/replant, feedback cycles, review goals, pause and completion actions. Those are function-specific constructor surfaces. Under Methodology 0.3.6 they support Constructor (`C`) where the organizational function is already implemented but a downstream composition must still attach the autonomous actor/decision closure.

Primary evidence:

- [`packages/soothe/src/soothe/sloop/strange_loop.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/sloop/strange_loop.py) — current model/tool loop and loop-native `LoopRailInterpreter` binding.
- [`packages/soothe/src/soothe/coreagent/core_agent.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/coreagent/core_agent.py) — first-party CoreAgent integration with the pinned `soothe-nano` runtime.
- [`packages/soothe/src/soothe/context/engine.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/context/engine.py) and [`packages/soothe/src/soothe/context/planning_scheduling.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/context/planning_scheduling.py) — persisted multi-goal state, ready-goal scheduling, claim/lifecycle and retry machinery.
- [`packages/soothe/src/soothe/rails/selector.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/selector.py) — model-based rail selection.
- [`packages/soothe/src/soothe/rails/interpreter.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/interpreter.py) — job-scoped rail interpreter, explicit guard injection point and fail-closed behavior when no evaluator is configured.
- [`packages/soothe/src/soothe/rails/guards.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/guards.py) — `GuardContext`, model-backed guard evaluation and structural conditions over current job/goal state.
- [`packages/soothe/src/soothe/rails/builtins_exec.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtins_exec.py) — CE-facing orchestration actions including maker/reviewer creation, branch retry/replant, merge/feedback state and job completion control.
- [`packages/soothe/src/soothe/rails/builtin_rails/maker-checker.yml`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtin_rails/maker-checker.yml) — first-party implement → independent checker → send-back/replant → QA organizational pattern.
- [`packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml) — first-party multi-maker worktree, merge, review, QA, feedback, recovery and optional-human workflow.
- [`packages/soothe/src/soothe/rails/__init__.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/__init__.py) — intentional public export surface for the interpreter and guard implementations.
- [`packages/soothe-daemon/src/soothe_daemon/cron/service.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe-daemon/src/soothe_daemon/cron/service.py) and [`packages/soothe/src/soothe/protocols/runner.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/protocols/runner.py) — current reachability of loop-native rail binding after removal of `AutopilotService`.
- [`CHANGELOG.md`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/CHANGELOG.md) — frozen-revision architectural change recording the consolidation from daemon Autopilot into loop-native rail execution.
- [`packages/soothe/src/soothe/subagents/veritas/implementation.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/subagents/veritas/implementation.py) — clarification inference path inspected and not credited as independent operational audit.
- [`packages/soothe/src/soothe/rails/autoresearch_exec.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/autoresearch_exec.py) and [`packages/soothe-daemon/src/soothe_daemon/skillify/service.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe-daemon/src/soothe_daemon/skillify/service.py) — external research and skill retrieval paths inspected for S4.

## Operational model

A normal StrangeLoop is an autonomous operational loop: model output selects substantive tool actions, returned observations alter the context, and the model chooses subsequent actions. ContextEngine can hold multiple goals and the rail layer can define how distinct goals/makers are spawned and related. Builtin rails explicitly encode worktree isolation, merge/recovery, independent review and corrective feedback patterns.

The organizational distinction is ownership. At the frozen revision, ordinary loop-native rail wiring does not install the shipped model-backed guard evaluator, so the first-party current-control and audit workflows are not closed by a standard autonomous controller. The package nevertheless exposes those VSM-specific decision/feedback paths deliberately and without requiring replacement of their underlying orchestration logic. S2, S3 and S3* are therefore Constructor paths rather than autonomous closures.

## S1 — Operations

- State: A
- Function: transform an accepted user/job goal into tool-mediated effects through a repeated model → action/tool → observation → model loop.
- Disturbance / variety regulated: changing workspace state, tool outputs/failures, ambiguous goal requirements, model results, clarification state and execution progress.
- Decisive decision or feedback right: choose the next substantive action/tool and revise subsequent behavior from returned operational evidence.
- Decision owner: the active StrangeLoop/CoreAgent model actor.
- Supporting / enforcement mechanisms: ContextEngine goal state, CoreAgent tool execution, runner/daemon lifecycle, model configuration, rail constraints and ordinary safety/clarification machinery.
- Closure path: goal enters StrangeLoop → model chooses substantive action/tool → tool/environment returns changed evidence → evidence is recorded in loop context/state → model receives that evidence and chooses the next action until termination.
- Boundary reachability: the runner/daemon standard path invokes StrangeLoop directly; no downstream harness is required to instantiate the operational loop.
- Why this is / is not agent-owned: removing the model leaves scheduling, tools and state machinery but removes the discretionary choice of what substantive action to take next and how to respond to operational results.
- Evidence: [`packages/soothe/src/soothe/sloop/strange_loop.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/sloop/strange_loop.py); [`packages/soothe/src/soothe/coreagent/core_agent.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/coreagent/core_agent.py); [`packages/soothe/src/soothe/context/engine.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/context/engine.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: external model inference is environmental, but the first-party Soothe runtime owns the persistent loop, tool invocation and observation-return path.

## S2 — Coordination

- State: C
- Function: attenuate structural interference among concurrently executing maker/worker S1 units that would otherwise collide through shared files, branches and integration state.
- Disturbance / variety regulated: overlapping write sets, concurrent branch/worktree edits, merge conflicts, stale peer worktrees and failed integration that can make one maker invalidate another maker's work.
- Decisive decision or feedback right: determine when maker work is isolated, merged, retried/replanted or deferred, and feed integration/conflict state back into subsequent maker execution.
- Decision owner: no autonomous S2 owner is closed in the frozen default wiring. The first-party rail/guard/builtin surface exposes the decision path; downstream composition must attach the guard/coordination actor and close the event path.
- Supporting / enforcement mechanisms: rail job state, worktree/branch metadata, maker annotations, merge state, structural guard facts, retry/replant builtins, peer refresh/integration logic and ContextEngine lifecycle state.
- Closure path: multiple maker goals exist as distinct operational loops → shared-workspace/merge interference is represented by worktree and branch/integration state → rail conditions choose isolation/merge/retry handling → builtins change branch/goal state → later maker/integration behavior observes the changed state.
- Boundary reachability: builtin rails are shipped, selectable through the normal rail surface, and the relevant interpreter/guard/builtin classes are public first-party exports. The standard StrangeLoop rail binding does not currently install a guard evaluator, so this path requires constructor composition rather than closing autonomously out of the box.
- Why this is / is not agent-owned: the S2 function and feedback path are first-party and interference-specific, but the frozen standard composition lacks an attached autonomous guard/coordination owner. Wiring the shipped guard surface can supply that owner without replacing the coordination implementation; this supports `C`, not `A`.
- Evidence: [`packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml); [`packages/soothe/src/soothe/rails/builtins_exec.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtins_exec.py); [`packages/soothe/src/soothe/rails/guards.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/guards.py); [`packages/soothe/src/soothe/rails/interpreter.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/interpreter.py).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: generic ContextEngine scheduling or parallelism is not the witness. The positive witness is the rail path specifically addressing concurrent maker write/integration interference.
- Distinct S1 units: separately created maker/worker goals executing model/tool work with their own goal identities and, in the greenfield path, isolated worktrees/branches.
- Inter-S1 disturbance: concurrent makers can target one repository and create overlapping/stale/incompatible changes or merge conflicts that disturb other makers' operations.
- Attenuating coordination relation: worktree isolation plus rail-governed merge, retry/replant, conflict handling and state refresh coordinate those competing operations.
- Feedback into subsequent S1 behaviour: merge/conflict/retry state changes the goal/branch state used for later execution, and failed work can be replanted onto a fresh branch rather than continuing unchanged.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanism is explicitly tied to a concrete inter-S1 write/integration disturbance and changes later maker behavior to attenuate that disturbance.

## S3 — Inside-and-now control

- State: C
- Function: maintain job-wide current operating control over the live goal population and intervene in execution through spawning, retry/replant, feedback, pause and completion decisions.
- Disturbance / variety regulated: stalled/failed branches, incomplete integration, pending or active sibling goals, retry exhaustion, missing review/QA/feedback, and changing job-wide progress toward acceptance.
- Decisive decision or feedback right: inspect current whole-job/goal state and decide whether to create corrective work, retry/replant failed work, gate progression, pause, or complete the job.
- Decision owner: no autonomous S3 controller is closed in standard frozen wiring. `LLMGuardEvaluator` is the first-party decision actor available to a constructor; `LoopRailInterpreter` and builtins execute the resulting current-control actions.
- Supporting / enforcement mechanisms: `GuardContext` current event/goal/sibling/tag/retry/structural state, ContextEngine DAG and lifecycle APIs, persistent rail job state, builtins for spawn/retry/feedback/pause/complete, and rail trace/state storage.
- Closure path: live ContextEngine/rail state supplies a whole-job current view → guard evaluation determines whether a current-control condition applies → interpreter selects the associated builtin → builtin mutates goals/branches/job state or creates corrective work → subsequent operational goals run under that changed current-control state.
- Boundary reachability: the evaluator, interpreter and builtins are intentional public first-party rail APIs and shipped rails name the current-control conditions/actions. Frozen StrangeLoop binds the interpreter but omits `guards=...`; a downstream constructor must attach the shipped evaluator/authority path, so the state is `C` rather than `A`.
- Why this is / is not agent-owned: current-control discretion can be supplied by the shipped model-backed evaluator, but Soothe does not wire that actor into the standard loop-native rail path at this revision. Deterministic ContextEngine scheduling alone would not qualify as autonomous S3.
- Evidence: [`packages/soothe/src/soothe/rails/guards.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/guards.py); [`packages/soothe/src/soothe/rails/interpreter.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/interpreter.py); [`packages/soothe/src/soothe/rails/builtins_exec.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtins_exec.py); [`packages/soothe/src/soothe/context/engine.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/context/engine.py); [`packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml).
- Basis: explicit + structural
- Confidence: medium
- Caveats: `C` depends on the function-specific public guard/interpreter/builtin composition, not on generic scheduler APIs. Historical `AutopilotService` ownership is not credited.
- Whole-system current view: `GuardContext` plus rail/ContextEngine structural state expose the current job id, triggering event/goal, sibling statuses, role/tags, retry state, pending/active counts, implementation/review/integration ids and branch/job annotations needed for job-level intervention.
- Current-control decision scope: the constructor path can choose whether to spawn additional/corrective goals, merge or retry/replant work, initiate feedback/review/QA, pause progression, or declare job completion; these choices change current commitments and execution state rather than merely enforcing a fixed concurrency ceiling.

## S3* — Complementary audit

- State: C
- Function: provide a complementary review channel that can inspect completed maker output with a fresh goal identity and return a challenge that causes corrective work rather than merely confirming routine production status.
- Disturbance / variety regulated: implementation defects or requirement misses that survive the maker's own production loop and ordinary progress reporting.
- Decisive decision or feedback right: independently inspect the merged/diff-scoped maker result, decide whether it passes review, and send failed work back into a corrective/replant path.
- Decision owner: no autonomous independent-audit owner is closed in the frozen default composition. The maker-checker rail plus fresh reviewer goal and guard/replant primitives expose the audit-specific constructor path.
- Supporting / enforcement mechanisms: separate review goal creation and `reviewer` role annotation, diff-scoped review brief, maker/reviewer separation, send-back/retry-branch/replant actions and ContextEngine lineage/state.
- Closure path: maker completes work → a separate review goal with fresh identity is created to inspect the result → review outcome can select send-back/retry → failed maker work is replanted/corrected → the changed work returns to the production/review sequence.
- Boundary reachability: `maker-checker.yml` is a shipped builtin rail and the review/retry verbs are implemented in first-party builtins. The current default interpreter lacks the attached guard evaluator needed to close conditional progression, so this remains a constructor path.
- Why this is / is not agent-owned: the audit route is materially separate from the maker's own model loop and can challenge/correct its output, but the autonomous review-control closure is not installed by standard frozen wiring. Generic Veritas clarification and ordinary tests are not credited as S3*.
- Evidence: [`packages/soothe/src/soothe/rails/builtin_rails/maker-checker.yml`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtin_rails/maker-checker.yml); [`packages/soothe/src/soothe/rails/builtins_exec.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtins_exec.py); [`packages/soothe/src/soothe/rails/interpreter.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/interpreter.py); [`packages/soothe/src/soothe/subagents/veritas/implementation.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/subagents/veritas/implementation.py).
- Basis: explicit + structural
- Confidence: medium
- Caveats: the review goal is credited because it is a fresh, complementary inspection path over maker output with corrective return. A same-model self-check or routine acceptance check alone would not qualify. The missing standard guard wiring prevents `A`.
- Claim being audited: that a maker's completed/merged implementation actually satisfies the requested slice without correctness or requirement defects that the maker's own loop failed to detect.
- Ordinary reporting path: the maker goal's own completion/progress state and artifacts flow through the normal ContextEngine/rail production path.
- Complementary access path: `review` creates a distinct reviewer goal with a fresh identity and a diff-scoped brief over the maker result rather than merely consuming the maker's self-report.
- Independence boundary: reviewer and maker are separate goal identities/roles and the reviewer can challenge the maker result; independence is constructor-level because default frozen guard wiring does not autonomously schedule and close the full review/send-back path.
- Who acts on findings: rail builtins can convert failed review/send-back into `retry_branch`/replant and corrective work, returning the finding to production rather than leaving it as an advisory report.

## S4 — Outside-and-then intelligence

- State: —
- Function: scan materially external and prospective conditions, form an adaptation option for the Soothe organization/capability, and return that option into present operating capability or S3 control.
- Disturbance / variety regulated: none established at the organizational S4 level; current-task web evidence and existing-skill lookup regulate task uncertainty rather than organizational adaptation.
- Decisive decision or feedback right: no first-party owner was found that can decide an organizational adaptation from outside/future evidence and close it back into current capability.
- Decision owner: none established within the reviewed boundary.
- Supporting / enforcement mechanisms: autoresearch, browser/research collection and skill indexing/retrieval are available task-support mechanisms but do not themselves own S4 adaptation.
- Closure path: no material first-party outside/future → adaptation option → present capability/S3 return loop was established.
- Why this is / is not agent-owned: model-based research may be agent-owned for a task, but the evidence does not show that the model owns organizational adaptation of Soothe itself.
- Evidence: [`packages/soothe/src/soothe/rails/autoresearch_exec.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/autoresearch_exec.py); [`packages/soothe-daemon/src/soothe_daemon/skillify/service.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe-daemon/src/soothe_daemon/skillify/service.py); [`packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml).
- Basis: scoped absence
- Confidence: high
- Caveats: future-facing task research is not S4 unless it returns as organizational adaptation.

### Absence scope

- Surfaces inspected: StrangeLoop/ContextEngine/rail runtime, builtin rails, autoresearch execution, daemon skill retrieval/indexing, public subagents, runner/daemon launch paths and frozen current architecture docs/source.
- Plausible first-party paths checked: autoresearch/web research, research synthesis, skillify indexing/retrieval, model/rail selection and corrective feedback/retry paths.
- Why no material first-party path remains: the inspected paths either improve the current task with external information or select/retrieve already available behavior; none closes an external-and-prospective conversation that changes Soothe's present organizational capability and verifies that adaptation in operation.

## S5 — Policy and identity

- State: —
- Function: resolve identity-level or ultimate-policy questions for the assessed Soothe organization through an ultimate authority and return the resulting policy/identity decision into lower-system operation.
- Disturbance / variety regulated: none established at the S5 level; approvals, clarification and configured rails constrain individual actions/workflows but do not resolve organizational identity or ultimate policy.
- Decisive decision or feedback right: no first-party owner was found with ultimate authority to decide who/what the organization is or its highest-level policy and return that decision into S1-S4 operation.
- Decision owner: none established within the reviewed boundary.
- Supporting / enforcement mechanisms: human pauses/approvals, configuration, rail choice and clarification can enforce local operational constraints but are not evidence of S5 ownership.
- Closure path: no identity/ultimate-policy issue → ultimate authority → authoritative decision → return-to-operation loop was established.
- Why this is / is not agent-owned: no internal agent owns the ultimate identity/policy right, and ordinary operator approval of an irreversible or risky step is action-level governance rather than S5 closure.
- Evidence: [`packages/soothe/src/soothe/rails/interpreter.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/interpreter.py); [`packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/rails/builtin_rails/greenfield-system.yml); [`packages/soothe/src/soothe/context/engine.py`](https://github.com/mirasoth/soothe/blob/be4fa14c0aa53203b8861dbff367eccb0df77668/packages/soothe/src/soothe/context/engine.py).
- Basis: scoped absence
- Confidence: high
- Caveats: a human approval gate is not S5 merely because a human has final say over one action.

### Absence scope

- Surfaces inspected: rail definitions/interpreter, approvals/clarifications, human pause/cutover hooks, runtime configuration, ContextEngine state, daemon/runner surfaces and builtin workflow controls.
- Plausible first-party paths checked: human approval, clarification, configured/default rail choice, job acceptance/completion and optional human handling of irreversible cutover.
- Why no material first-party path remains: all inspected paths concern operational authorization, workflow selection or completion; none routes an identity/ultimate-policy issue to a legitimate ultimate authority and returns that decision to govern subsequent S1-S4 behavior.

## Recursion

The positive classification is at one deployment/job recursion. A StrangeLoop goal is an S1 unit; multi-maker rails can instantiate several such units under one job. Constructor S2/S3/S3* claims therefore concern the job-level rail/ContextEngine layer over those operational units. Historical daemon Autopilot ownership is not imported from an older recursion or version.

## Variety and escalation

Operational variety is handled first by each S1 loop through tool feedback. The constructor rail layer exposes additional variety attenuation through maker isolation/merge handling, retry/replant, review, QA, feedback and optional human pause. Because the current frozen standard binding omits the guard evaluator, those higher-function escalation paths require composition before they become autonomous organizational closure.

## Evidence gaps

The main gap is the frozen transition from the removed daemon `AutopilotService` to loop-native rails. First-party decision and action primitives remain present, but standard `StrangeLoop` wiring does not install `LLMGuardEvaluator`; therefore this assessment deliberately stops at `C` for S2/S3/S3*. A future reassessment should first check whether production wiring has attached the guard actor and whether goal/send-back/idle event closure is fully restored before considering any `A` upgrade.
