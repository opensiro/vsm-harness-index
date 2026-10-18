---
harness_id: wrongstack
project_name: WrongStack
repository: https://github.com/WrongStack/WrongStack
review_ref: 42d410f938ba644e70771e200f39903117507a72
reviewed_at: 2026-10-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-14
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: —
---

# WrongStack

## Review boundary

- System in focus: WrongStack's first-party installable local coding-agent product, including its model/tool kernel, multi-agent Director/Fleet mode, worktree task integration, optional FleetSupervisor/Brain, Chimera review and Kanban verifier, role learning and project-governance boundary at pinned revision `42d410f938ba644e70771e200f39903117507a72`.
- Purpose and identity: carry out model-led software engineering, optionally with delegated parallel role agents, current fleet supervision, quality review and durable project-specific learnings.
- Relevant environment: mutable project files and build/test output, model APIs, concurrent agent tasks and file overlaps, project-specific rules, user approvals, project learning signals, review findings and configured client surfaces.
- Standard-distribution boundary: shipped first-party packages instantiated via supported WrongStack CLI/desktop/web sessions (including optional Fleet/Director, worktree, reviewer, Kanban and learning configurations). Third-party models, MCP/ACP remotes, user-authored skills, target project's contributors, CI/release and upstream project governance are not automatically organizational owners.
- Credited operating / distribution surfaces: `packages/core/src/core/agent-loop.ts`, `packages/core/src/coordination/director.ts`, `packages/core/src/coordination/worktree-task-runner.ts`, `packages/core/src/worktree/worktree-manager.ts`, `packages/core/src/coordination/fleet-supervisor.ts`, `packages/cli/src/fleet/`, `packages/cli/src/execution-chimera-review.ts`, `packages/kanban/src/verification/`, `packages/core/src/coordination/agents/project-agent-auto-optimize.ts`, `packages/cli/src/fleet/host-context.ts`, `packages/governance/src/`.
- Adjacent first-party surfaces excluded from ownership: unit/E2E tests, benchmarks, sample projects, the repository's own `.wrongstack/agents/` seeded learning content unless loaded in the shipped consumer's project, packaging/CI/release workflows, README future-positioning and independent third-party agent processes.
- First-party operating / deployment modes considered: ordinary single coding-agent session; supported Director/Fleet with first-party model-running child agents and optional worktree integration; optional Brain-assisted FleetSupervisor; Chimera reviewer on a changed-file event; Kanban managed-board verification; enabled project-agent learning optimization; local interactive/remote UI surfaces without treating display clients as separate organizations.
- Recursion level: one local coding project/session and its participating role agents when Director mode is enabled. HQ may aggregate broader status across projects/machines but is not silently borrowed as a whole-company operational owner.
- Reviewed revision: `42d410f938ba644e70771e200f39903117507a72` (exact frozen source from candidate #898; no later upstream features credited).
- Observation date: 2026-10-14.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The local agent loop dispatches model-selected tools over an owned coding workspace. The shipped `Director` can spawn first-party role agents, assign tasks, maintain a task registry and fleet bus, observe results, terminate agents and return outcomes into the parent model. The supported `MultiAgentHost` creates a `FleetManager` with a roster and live task states. A `FleetSupervisor` observes idle/overloaded/stuck workers and the queue, invokes a tiered Brain decision over remedial options and carries out approved actions such as retargeting *pending* work, steering workers or spawning help. Human escalation and deterministic policy bounds remain distinguishable from agent-made current fleet choices.

In supported worktree mode, `wrapSubagentRunnerWithWorktrees` allocates isolated git checkout branches for mutating children, executes them in those directories, attempts serial integration and reports exact conflict files or failed integration as a returned task failure/status. Merge-conflict decisions or a caller-provided resolver must still be distinguished from the deterministic git merge detector. In optional reviewer mode, `Chimera` launches a separate read-only model reviewer which directly examines changed files and verifies source citations; findings are persisted and sent to the project mailbox. Crucially, the current `execution-chimera-review.ts` explicitly marks default feedback as **informational** and says no leader turn/fix cascade was started, so a complete automatic corrective S3* return cannot be assumed. The separate Kanban completion gate can run external tests and block/park task `Done` transitions in managed boards; whether this is a complementary S3* auditor with an organizational corrective return is left unresolved on the inspected evidence.

Task learning records per-role outcomes and directives. With auto-optimization enabled, the first-party scheduler can invoke an LLM to consolidate raw experience into durable role guidance and skill-specific project addenda, which are loaded by `host-context.ts` for subsequent role use. This is a real prospective *capability-update candidate*, not merely context compaction; whether its chosen environmental distinctions and returned options close the stricter Profile S4 outside-and-then function requires further source-specific analysis.

Architecture evidence: [`README.md`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/README.md); [`packages/core/src/core/agent-loop.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/core/agent-loop.ts); [`packages/core/src/coordination/director.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/director.ts); [`packages/cli/src/fleet/host-director-builder.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/fleet/host-director-builder.ts); [`packages/core/src/coordination/worktree-task-runner.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/worktree-task-runner.ts); [`packages/core/src/worktree/worktree-manager.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/worktree/worktree-manager.ts); [`packages/core/src/coordination/fleet-supervisor.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/fleet-supervisor.ts); [`packages/cli/src/execution-chimera-review.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/execution-chimera-review.ts); [`packages/kanban/src/verification/completion-gate.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/kanban/src/verification/completion-gate.ts); [`packages/core/src/coordination/agents/project-agent-auto-optimize.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/agents/project-agent-auto-optimize.ts); [`packages/cli/src/fleet/host-context.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/fleet/host-context.ts).

## Operational model

The coding worker's model has S1 next-action discretion over real files/tests. In multi-agent mode distinct children execute bounded work in separately instantiated agent runs; the supervisor's view of current tasks and the Director's discretionary assignments constitute a wider management level than a worker's own plan. Worktree isolation/merge conflict feedback is a constructor S2 path for inter-worker write collisions, not a claim of autonomous S2 policy ownership. Independent source review and project-specific learning are implemented mechanisms with unresolved higher-function closure in the precise enabled modes; routine policy gates are not credited as S5.

## S1 — Operations

- State: A
- Function: transform uncertain software-development tasks into model-chosen file edits, tool commands and feedback-driven corrections.
- Disturbance / variety regulated: changing codebase, errors, tests, provider output, tool feedback and task constraints.
- Decisive decision or feedback right: select task-relevant coding tools, delegate bounded work and alter next actions on returned observations.
- Decision owner: WrongStack's first-party model-directed worker and optional role subagents; external inference serves the first-party loop.
- Supporting / enforcement mechanisms: tool executor, provider transports, permission gates, session/context/memory stores, tool outcome events, kernel run controller.
- Closure path: model receives task+workspace evidence → chooses tool/arguments → first-party execution → real result returned into conversation → revised model coding choice or outcome.
- Boundary reachability: shipped CLI/desktop/web agent sessions instantiate the first-party loop and tools without launching a different coding-agent CLI. Fleet mode spawns additional first-party model runners.
- Why this is / is not agent-owned: removing model-directed tool choices while leaving runtime/permissions yields no equivalent adaptive task execution.
- Evidence: [`README.md`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/README.md); [`packages/core/src/core/agent-loop.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/core/agent-loop.ts); [`packages/runtime/src/host.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/runtime/src/host.ts); [`packages/core/src/coordination/director.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/director.ts); [`packages/cli/src/fleet/host-subagent-factory.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/fleet/host-subagent-factory.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: provider/model output is a dependency; autonomous coding is not a proof of higher organizational grades or of correct delivered code.

## S2 — Coordination

- State: C
- Function: attenuate interference when distinct mutating first-party S1 workers produce overlapping changes for the same coding project.
- Disturbance / variety regulated: conflicting edits and commits from concurrent independent coding tasks, risking overwrites/invalid integration.
- Decisive decision or feedback right: a shipped worktree constructor isolates a child to its own branch and admits or rejects subsequent integration on real three-way merge conflict evidence. Its conflict/commit result enters the originating task's status and parent task handling; optional resolver may select a repair, but this is not credited to the deterministic constructor.
- Decision owner: first-party runtime `WorktreeTaskRunner`/`WorktreeManager` constructor for isolation, merge admission, conflict detection and returned failure/status; human/model authority over how to repair remains distinct.
- Supporting / enforcement mechanisms: git worktrees/branches, `commitAll`, `merge --squash`, index/conflict-marker checks, `WorktreeIntegrationError` and task/worktree state registry.
- Closure path: competing child changes → isolated branches → guarded merge → either integrated accepted result or path-specific conflict/failure returned into task state/parent observation → next work can be revised or withheld rather than silently committed.
- Boundary reachability: `Director` wires `wrapSubagentRunnerWithWorktrees` with the `WorktreeManager` constructed by shipped `MultiAgentHost` in the supported enabled worktree policy; this is more than a library method waiting for downstream implementers.
- Why this is / is not agent-owned: the S2 anti-interference function is real, but the isolation/merge/conflict-return rule remains deterministic even with the model actor removed; therefore constructor `C`, not `A`.
- Distinct S1 units: separately model-running coding subagents attached to a Director session and independently modifying their assigned worktrees.
- Inter-S1 disturbance: same-path/same-project changes that cannot be safely combined after parallel worker work.
- Attenuating coordination relation: per-subagent checkout isolation and serialized git merge admission with conflict-file detection.
- Feedback into subsequent S1 behaviour: failed integration returns a structured `WorktreeIntegrationError` and task `conflict` status with specific files to parent/Director rather than exporting an undetected conflicting combined edit.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the control specifically guards actual conflicting *outputs of different S1 workers* at the shared integration point, and provides conflict-specific regulation/return rather than just sequencing task dispatch.
- Evidence: [`packages/core/src/coordination/worktree-task-runner.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/worktree-task-runner.ts); [`packages/core/src/worktree/worktree-manager.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/worktree/worktree-manager.ts); [`packages/core/src/coordination/director.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/director.ts); [`packages/cli/src/fleet/host-director-builder.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/fleet/host-director-builder.ts).
- Basis: structural + explicit
- Confidence: medium-high
- Caveats: optional worktrees may be off or fall back in some configurations. The positive C state is bounded to the supported worktree-enabled multi-worker mode. No evidence of autonomous inter-worker bargaining is claimed.

## S3 — Inside-and-now control

- State: A
- Function: control current commitments, assignments and capacity of the running role-agent fleet, not merely a worker's own task schedule.
- Disturbance / variety regulated: unbalanced workload, stuck/erroring workers, stale commitments, idle helpers, constrained parallel capacity and non-progressing work.
- Decisive decision or feedback right: the model-directed leader/Director chooses task delegation and reassignments from task/fleet state; the optionally enabled supervisor further proposes operational interventions and asks Brain (policy/LLM/human tier) before retargeting unstarted work or steering a worker.
- Decision owner: model-directed first-party Director lead for discretionary whole-fleet current decisions in the supported fleet mode; Brain/model/human tier ownership is recorded separately for supervisor interventions, rather than assuming a deterministic watchdog always owns the decision.
- Supporting / enforcement mechanisms: `FleetManager`, `DirectorTaskRegistry`, FleetBus, task results, budget rules, `FleetSupervisor`, `engageRebalance`, roster status and terminal/remote fleet controls.
- Closure path: live worker/queue/commitment state → leader model task/agent decision (or optional Brain-adjudicated supervisor proposal) → assigned/retargeted/steered/terminated worker → updated per-task and fleet status for subsequent management turns.
- Boundary reachability: shipped `MultiAgentHost` instantiates Director/FleetManager; `Director` exposes spawn, assign, status, retarget and terminate functions to active agent sessions. `FleetSupervisor` is a wired optional supervisory mode, not a documentation-only wishlist.
- Why this is / is not agent-owned: removing the model-directed leader from Director mode removes its discretionary prioritization and reassignment choices; deterministic roster bookkeeping, hard spawn caps and timeout monitors remain supporting tools. Automated Brain policy enforcement alone is not the positive A basis.
- Whole-system current view: the current project-fleet roster, task registry, pending/completed work, running/idle subagents, outcomes and budget/usage within the declared Director session.
- Current-control decision scope: discretionary current task assignment and reallocation to workers, worker steering/termination, response to stuck status and live capacity selection.
- Evidence: [`packages/core/src/coordination/director.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/director.ts); [`packages/core/src/coordination/director/director-task-registry.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/director/director-task-registry.ts); [`packages/core/src/coordination/fleet-supervisor.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/fleet-supervisor.ts); [`packages/core/src/coordination/fleet-supervisor-rebalance.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/fleet-supervisor-rebalance.ts); [`packages/cli/src/fleet/host-director-builder.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/fleet/host-director-builder.ts); [`packages/cli/src/fleet/host-supervisor.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/fleet/host-supervisor.ts).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: this S3=A is for actual first-party Fleet/Director model mode, not merely the single-agent REPL or all UI dashboards. A separate parent-governed S3 path has not been positively established here; no speculative `(P)` is attached.

## S3* — Complementary audit

- State: ?
- Function: independently challenge claims about changed code/task completion and return evidenced findings to operational control.
- Disturbance / variety regulated: incorrect patches, test regressions, non-factual claims of successful completion and unverified acceptance criteria.
- Claim being audited: model-worker implementation success / code quality / changed-file defect freedom.
- Ordinary reporting path: authoring worker's own tool/test output, task result and session/Director reporting.
- Complementary access path: Chimera independently instantiated model reviewer with separate read-only permissions, real source/diff evidence and on-disk citation verification; Kanban verification gate also examines executable acceptance checks.
- Independence boundary: reviewer has separate model runner and constrained direct-file evidence access; deterministic Kanban test execution is distinct from a worker's prose. Material independent *decision and closure* across these mechanisms remains unresolved.
- Who acts on findings: Chimera report is persisted and delivered via project mailbox; code explicitly says the default delivery is informational and **does not automatically start a leader turn, fixer or cascade**. Kanban gate can reject or park a managed task, but its relationship to complementary supervisory correction needs the full configured mode traced.
- Decisive decision or feedback right: reviewer model owns code critique; gate owns test verdict; downstream authoritative corrective dispatch cannot be established from those facts alone at the stated boundary.
- Decision owner: model auditor for Chimera critique, deterministic verifier for Kanban evidence, and optional leader/human for subsequent action; final composite S3* ownership unresolved.
- Supporting / enforcement mechanisms: `chimera.review_needed` event, read-only reviewer policy, citation-to-disk validation, mailbox and report stores, `finalizeTaskCompletion` and managed-board completion checks.
- Closure path: independent inspection → report/verdict → mailbox or completion-gate status; whether findings cause closed corrective management action in a supported first-party mode is not yet evidenced.
- Why this is / is not agent-owned: model-backed challenger exists and may be genuinely complementary, but independence of inspection alone is not the complete S3* correction function, especially where normal review explicitly avoids automatic reentry.
- Evidence: [`packages/cli/src/execution-chimera-review.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/execution-chimera-review.ts); [`packages/cli/src/chimera-reviewer-policy.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/chimera-reviewer-policy.ts); [`packages/cli/src/execution-chimera-cascade.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/execution-chimera-cascade.ts); [`packages/kanban/src/verification/completion-gate.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/kanban/src/verification/completion-gate.ts); [`packages/kanban/src/verification/completion-protocol.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/kanban/src/verification/completion-protocol.ts).
- Basis: structural + unresolved
- Confidence: medium
- Caveats: `?` identifies a concrete first-party reviewer/gate return ambiguity, not a missing reviewer component. Do not promote to `A` or `C` without closing the outcome→remediation path or proving the independent gate itself closes complementary audit at the correct recursion.

## S4 — Outside-and-then intelligence

- State: ?
- Function: transform project-environment feedback and past role failures/successes into prospective changes in the agent organization's future practice/capability.
- Disturbance / variety regulated: recurring defects and changing project conventions/tool competence that might require a new role-specific rule or reusable skill.
- External distinction: project/task outcomes, repo-specific observations and applied directive success rates are captured outside the immediate internal prompt-generation logic.
- Future / prospective distinction: auto-optimization selects and refines reusable role instructions/addenda for later work, not merely the current tool call.
- Adaptation option generated: model-driven consolidation of past directives with applied/win statistics and generated skill-specific addenda.
- Path back into current capability / S3: serialized guidance is reloaded by subsequent role-agent context building; however whether this closes the full outside-and-then *organizational* S4 loop rather than internal experience distillation is not resolved.
- Decisive decision or feedback right: auto-optimization scheduler deterministically selects when to run; model optimizer can synthesize the material practice, but classification of the environmentally prospective organizational decision remains unproven.
- Decision owner: first-party model optimizer for consolidation; runtime for scheduling and persistence; possible S4 decisive owner unresolved.
- Supporting / enforcement mechanisms: learned directive capture and grades, optimization thresholds, `LearningOptimizationScheduler`, persisted consolidated documents and skill addenda, project-aware skill retrieval.
- Closure path: scored completed task observations → scheduled optimization/model synthesis → persistent project-role skill addendum → subsequent specialist context; remaining gap is proving that this is a VSM S4 external-future adaptive control decision rather than routine local retrospective learning.
- Why this is / is not agent-owned: real model-dependent future-guidance synthesis exists, so a bounded no-path `—` is premature; whether it meets the complete S4 functional relation must be separated from positive S1 memory.
- Evidence: [`packages/cli/src/fleet/host-learning.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/fleet/host-learning.ts); [`packages/cli/src/fleet/host-learning-scheduler.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/fleet/host-learning-scheduler.ts); [`packages/core/src/coordination/agents/project-agent-auto-optimize.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/agents/project-agent-auto-optimize.ts); [`packages/core/src/coordination/agents/project-agent-optimizer.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/agents/project-agent-optimizer.ts); [`packages/cli/src/fleet/host-context.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/cli/src/fleet/host-context.ts).
- Basis: structural + unresolved
- Confidence: medium
- Caveats: `?` is not a claim that any memory or self-improvement feature is automatically S4. The specific future-role-guidance path is implemented, but its organizational/outside-future decision boundary is unsettled.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-purpose dispute → legitimate authority → returned authoritative organizational policy loop established for this installed coding organization.
- Disturbance / variety regulated: risky tool calls, unauthorized paths, changes to team constraints, human-required operations and project governance rules are possible policy enforcement inputs.
- Decisive decision or feedback right: the operator/developer configures an autonomy envelope and project permissions; governance/Brain decides or escalates individual risk-tier operations, not a demonstrated authoritative decision over ultimate organizational identity/purpose.
- Decision owner: operator/config for permission ceilings and project-authored goals; policy/Brain layers for task/action authorization, but no owner identified for a first-party identity-level S5 function.
- Supporting / enforcement mechanisms: governance `AutonomyEnvelope`, rule/permission policy, Brain approval/escalation, path gates, capability grants and project task contracts.
- Closure path: a permission decision returns to authorize/reject a tool or task; no supported ultimate identity/policy issue → legitimate S5 authority → durable returned rule changing the organizational purpose/governing identity has been traced.
- Why this is / is not agent-owned: the presence of autonomous approval decisions does not make the Brain an ultimate-policy owner; removing the Brain leaves higher-level operator-defined risk limits and project identity settings.
- Evidence: [`packages/governance/src/autonomy-envelope.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/governance/src/autonomy-envelope.ts); [`packages/governance/src/task-contract.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/governance/src/task-contract.ts); [`packages/governance/src/project-service.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/governance/src/project-service.ts); [`packages/core/src/coordination/brain.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/coordination/brain.ts); [`packages/core/src/security/permission-policy.ts`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/packages/core/src/security/permission-policy.ts); [`README.md`](https://github.com/WrongStack/WrongStack/blob/42d410f938ba644e70771e200f39903117507a72/README.md).
- Basis: explicit + structural
- Confidence: medium
- Caveats: the repository includes extensive first-party runtime governance; this finding is bounded to ultimate-policy/identity closure, not a claim that risk or task governance is absent.

### Absence scope

- Surfaces inspected: project governance envelope, capability/permission types, Brain approval/human escalation, task/contract transition paths, project configuration and CLI/product descriptions.
- Plausible first-party paths checked: risk-tier approval, human tool confirmation, direct Brain decisions, task-goal contracts, persistent configuration, explicit identity/mission policy escalation and return.
- Why no material first-party path remains: inspected shipped paths regulate action authorization and commitments under external goals, but no concrete distinct ultimate identity dispute and legitimate policy-authority return changing the organization's constitutional purpose/identity appears in the standard coding runtime.

## Distributed OSS parent arrangement

WrongStack's upstream contributors, extension/plugin developers and independent downstream users are not one first-party parent-government body for a running installed project. An HQ client may observe multiple worker sessions but does not transfer identity-level decision authority merely by presenting them.

## Self-hosted and non-human modes

WrongStack runs locally, may use a local LLM and can operate in interactive, headless/goal and model-led fleet modes. Optional human escalation remains a real control path for risk-tier actions. That does not by itself establish a distinct eligible `(P)` S3/S4/S5 mode; no parent modifier is asserted on this first review.

## Recursion

A model-running Director controls multiple model-running role agents. This supplies a genuine organizational management boundary and multiple S1 operational units. Do not infer an endlessly nested viable system solely from spawn depth, sessions, nested roles or the mailbox.

## Variety and escalation

A model-tool-feedback loop handles coding variety; worker worktrees and guarded integration attenuate write collision; Director/FleetSupervisor observe and react to current-capacity and stall variety. Risk-tier Brain can escalate dangerous actions to a human. An event called an alert, audit or escalation alone is not another independent VSM function without its specified closure.

## Evidence gaps

- S3*: determine whether a shipped configured cascade/managed-Kanban verifier mode owns and returns an independent corrective organizational verdict, rather than only publishing an informational Chimera report or gating one card's state. Do not borrow a user's custom fixer workflow.
- S4: determine whether automatic role learning/skill augmentation constitutes prospective response to external environmental distinctions at the reviewed recursion with legitimate adaptation ownership, rather than only retrospective local tactic distillation. The project-specific optimization/reload path itself is first-party and should not be dismissed.
- S2: worktree-based constructor closure depends on the *enabled* Fleet worktree mode; clarify its default setting during later comparative analyses. No agent-owned merge-conflict resolution is claimed.
- Source-first static assessment of the pinned repository. No model-backed system run was performed; these are ownership/closure claims, not an empirical performance benchmark.
