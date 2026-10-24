---
harness_id: seek
project_name: Seek
repository: https://github.com/whyiyhw/seek
review_ref: 52e90e68b9b1f266f7eff952426eb996ec7f87f9
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: ?
autonomy_s5: —
---

# Seek

## Review boundary

- System in focus: published Seek Go binary coding-agent runtime, native tool/model loop, first-party subagents, Autopilot Decomposer+Fleet mode, goal driver, worktree management, local verification/review, memory and operator permissions at the selected user's coding project.
- Purpose and identity: autonomous repository development, with optional unattended task partition and parallel worktree-agent execution.
- Relevant environment: local Git repository/worktrees, source code, test/tool results, configured inference endpoints, operator policies and user/project context across sessions.
- Standard-distribution boundary: bundled Go binary, shipped CLI/TUI/headless/autopilot modes and registered code; external inference services, Git, OS sandbox, custom MCP/skills and human contribution/release organization do not donate VSM decision rights.
- Credited operating / distribution surfaces: `pkg/agent`, `internal/subagent`, `internal/autopilot`, `internal/goal`, `internal/worktree`, `internal/tools`, `internal/memory` plus first-party CLI and TUI wiring.
- Adjacent first-party surfaces excluded from ownership: `eval/`, tests, design PRDs, examples/demo captures, repository contributor/CI/release organization, separately owned user workflows and external models; docs corroborate but do not independently close a function.
- First-party operating / deployment modes considered: interactive/headless autonomous coding; `seek autopilot run` with model-chosen task splits plus isolated workers; `seek goal run` single-worker continuation; TUI `/code-review`; three-tier project/soul memory with optional auto-dream; operator permission controls.
- Recursion level: one user's coding project under a Seek multi-work-cell Autopilot operating mode when selected; independent coding subagents are local S1 operating cells. In ordinary single-agent mode S2 is not necessarily active.
- Reviewed revision: `52e90e68b9b1f266f7eff952426eb996ec7f87f9`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Seek ships a first-party Go model/tool coding runtime with streaming turns, tool execution and first-party sessions. The dedicated subagent Manager constructs independently running child models and contexts, restricts child tool/policy scope, tracks child usage and bounded concurrency, and optionally uses distinct Git worktree environments.

The shipped `autopilot` mode has an agentic `DeepSeekDecomposer`: a model is specifically instructed to produce independent nonoverlapping tasks, mitigating parallel write conflicts. The `Driver` then deterministically fans those tasks out through `managerFleet` into separate worktree-bound coding agents, aggregates statuses and leaves each successful child's local commit for manual review. This mode supplies a narrow prospective S2 interference-avoidance relation, **not** a general adaptive orchestration/whole-current S3. In `/goal` mode, a cheap judge loops a single worker across turns rather than managing a multi-unit organization.

The `/code-review` command constructs a review prompt and submits it to the primary agent turn; reviewer wording does not create an independent audit owner. Cross-project memory and `Dreamer` collect user traits in pending and potentially promoted stable Soul notes that later enter prompts; the environmental/prospective adaptation interpretation is not settled solely by persistence and automatic promotion rules. Permission, sandbox and human review modes limit execution but cannot import S5.

Primary evidence: [pkg/agent/agent.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/pkg/agent/agent.go); [internal/subagent/manager.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/subagent/manager.go); [internal/autopilot/autopilot.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/autopilot.go); [internal/autopilot/decompose.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/decompose.go); [internal/autopilot/fleet.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/fleet.go); [internal/tui/commands.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/tui/commands.go); [internal/memory/dream.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/memory/dream.go).

## Operational model

The main agent autonomously enacts coding tool operations and incorporates returned observations. In Autopilot, a model chooses independent task slices and changes what each child S1 later operates on, while fixed Go controls launch, isolate and collect. No recurring agentic global manager uses current whole-fleet information to change running workers' resource/commitment decisions. The source's optional code review and goal-completion checks are ordinary model-based operations, not automatically independent S3* audit.

## S1 — Operations

- State: A
- Function: Autonomous Go coding/tool execution with feedback to model.
- Disturbance / variety regulated: Unfamiliar repository state, requested changes, command/test failure, and changing code.
- Decisive decision or feedback right: Select next model tool action, modify/inspect code, and react to tool outcomes.
- Decision owner: Model-driven first-party main Seek Agent and bounded subagent S1 coding workers.
- Supporting / enforcement mechanisms: Tool registry, provider transport, permission/sandbox, session state, deadlines and worktree filesystem.
- Closure path: User goal → model-directed tool operation → first-party handler changes/reads working environment → result returns to agent → revised next action or completion.
- Boundary reachability: Shipped `seek` TUI/headless directly constructs the first-party pkg/agent loop and registers coding tools; worker Fleet runs the native subagent Manager rather than only an example.
- Why this is / is not agent-owned: Agent chooses and revises local operation using results; deterministic Go code enforces, records and transports.
- Evidence: [pkg/agent/agent.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/pkg/agent/agent.go); [internal/subagent/manager.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/subagent/manager.go); [README.md](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/README.md).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: External provider inference is a dependency; explicit action policies constrain permitted tools..


## S2 — Coordination

- State: A
- Function: Prospective attenuation of conflicting edits among two or more concurrently active coding S1 work cells.
- Disturbance / variety regulated: Parallel agents assigned overlapping file changes could overwrite edits or create conflicting branches, causing cross-unit interference.
- Decisive decision or feedback right: Plan nonoverlapping independent slices and decide each child task prompt before fanout; assign isolation for all peers.
- Decision owner: First-party model-based DeepSeekDecomposer in the standard Autopilot run.
- Supporting / enforcement mechanisms: Deterministic bounded fanout Driver, per-child Git worktree, isolated cwd, commit/reviewable branches, cap guards.
- Closure path: Goal → model chooses disjoint scoped tasks to avoid file overlap → worktree Fleet dispatch uses each selected task as the child S1 operating instruction → children subsequently edit separate isolated environments → outcomes returned in report.
- Boundary reachability: Standard `seek autopilot run` wires DeepSeekDecomposer and managerFleet into the concrete Driver/Fleet path. The same repository ships the real worktree and subagent implementations.
- Why this is / is not agent-owned: The model owns selection of work partition/assigned file scope; the runner only enforces selected partitions with worktree isolation.
- Evidence: [internal/autopilot/decompose.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/decompose.go); [internal/autopilot/autopilot.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/autopilot.go); [internal/autopilot/fleet.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/fleet.go); [internal/worktree/worktree.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/worktree/worktree.go); [docs/guide-autopilot.md](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/docs/guide-autopilot.md).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: The positive S2 mapping is restricted to the bundled Autopilot task-decomposition mode. It is **prospective/pre-execution** interference attenuation only: no adaptive negotiation or corrective coordination after fanout is credited..

- Distinct S1 units: at least two separately running general-purpose coding subagents, each with own model tool loop, tool budget and worktree.
- Inter-S1 disturbance: overlapping file edits or task dependencies across parallel workers would create collisions or inconsistent changes at the same repository boundary.
- Attenuating coordination relation: model-directed instruction to produce independent nonoverlapping tasks, followed by separate working directories and bounded fanout.
- Feedback into subsequent S1 behaviour: the coordination decision becomes each child's specific prompt/worktree scope before it begins its next operation; worker operations follow that partitioning. Outcome reports return to the parent, but no post-fanout adaptive conflict controller is established.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the decomposition explicitly identifies incompatible overlapping edits as the interference it prevents and changes actual worker assignments/operating contexts to attenuate them.


## S3 — Inside-and-now control

- State: —
- Function: No separately evidenced whole-system discretionary current-control over live multi-S1 commitments/resources beyond preplanned task partition.
- Disturbance / variety regulated: Current performance problems, task failures and competing commitments require live whole-system intervention; an autopilot aggregate report alone is not such regulation.
- Decisive decision or feedback right: Not established: the Autopilot driver deterministically fans out preselected tasks and aggregates results, without independently re-prioritizing/reassigning running units.
- Decision owner: No positive S3 decision owner established; human can inspect report and manually merge worktrees.
- Supporting / enforcement mechanisms: Concurrent caps, timeouts, budget tracking, child cancel index, goal judge and report counts.
- Closure path: Children return success/failure statuses → summary delivered for human review; no demonstrated first-party whole-current discretionary decision closes back into current worker priorities/resources.
- Why this is / is not agent-owned: Fixed launch/cancel limits, aggregate statuses and the separate single-agent goal judge do not autonomously own whole-current S3 regulation.
- Evidence: [internal/autopilot/autopilot.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/autopilot.go); [internal/autopilot/fleet.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/fleet.go); [internal/goal/goal.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/goal/goal.go); [internal/subagent/manager.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/subagent/manager.go); [docs/guide-autopilot.md](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/docs/guide-autopilot.md).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: The model's one pre-run decomposition may establish S2 but is not promoted to whole-current S3 without evidence of ongoing resource/commitment intervention..

### Absence scope

- Surfaces inspected: Autopilot Driver, Fleet, subagent Manager, per-turn goal driver, worktree/result lifecycle, CLI status surfaces.
- Plausible first-party paths checked: Parallel caps, fan-out task choices, child kill/cancellation, goal completion judge, failure reports, morning merge process.
- Why no material first-party path remains: The whole-current multi-unit management and exception-based intervention path is not supplied: after launch the Driver collects outcomes without model-driven cross-unit reprioritization or corrective release; human downstream review is outside this first-party autonomous closure.


## S3* — Complementary audit

- State: —
- Function: No evidenced sufficiently independent complementary audit of live operating claims with returned corrective closure in the standard combined runtime.
- Disturbance / variety regulated: An operational agent could claim successful changes without actual code correctness.
- Decisive decision or feedback right: Built-in `/code-review` asks the ordinary active agent to review a gathered diff; the goal judge checks single-worker progress, not independent operational evidence.
- Decision owner: The same executing model for slash-command review or a narrow separate goal-completion model; no independent complementary audit owner established.
- Supporting / enforcement mechanisms: Diff collection, bundled code-review skill prompt, optional plan/approval for fixes, goal judge.
- Closure path: A user triggers ordinary review in the same active conversation; potential corrective plan needs further agent/human action, not an automatic independent S3* audit-feedback loop.
- Why this is / is not agent-owned: A review label or second judge model cannot replace evidence access independent from the normal operational stream.
- Evidence: [internal/tui/commands.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/tui/commands.go); [internal/skill/builtin/code-review.md](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/skill/builtin/code-review.md); [internal/goal/goal.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/goal/goal.go); [internal/goal/judge.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/goal/judge.go).
- Basis: structural + explicit.
- Confidence: medium-high.
- Caveats: An external independent reviewer, or user-created separate agent mode, is not included in the credited standard workflow..

### Absence scope

- Surfaces inspected: Shipped /code-review TUI command, prompt construction, bundled review skill, goal judge, Autopilot reports and evidence surfaces.
- Plausible first-party paths checked: Separate model completion check, slash-command diff review, local git/test checks, subagent search roles.
- Why no material first-party path remains: The standard `/code-review` routes its prompt into the same main agent and can use ordinary diff evidence, but no independently owned complementary audit channel with automatic corrective return to the operational organization is established.


## S4 — Outside-and-then intelligence

- State: ?
- Function: Cross-project user-preference induction is a potential future-facing adaptation support path, but S4 decision/closure ownership is not conclusively established.
- Disturbance / variety regulated: Future project contexts and changing user preferences may require differentiated agent capabilities or instructions.
- Decisive decision or feedback right: Dreamer derives patterns and maintenance may promote cross-project candidates into a future injected stable soul; the connection to an autonomous *external-and-prospective capability-governance* choice remains ambiguous.
- Decision owner: Model-driven user-trait distiller plus deterministic source/time promotion rules; human may review manually.
- Supporting / enforcement mechanisms: Session/project/soul memory, >=2 source filter, configurable auto-dream cadence, >=3 source and age stability maintenance, prompt injection.
- Closure path: Recorded cross-project observations → model proposes reusable user traits → pending/stability process → stable memory can be loaded into later prompts. Whether this constitutes prospective organization-level adaptation rather than personalized recall requires further semantic adjudication.
- Why this is / is not agent-owned: Durable cross-project knowledge can alter later behavior but does not automatically establish S4's environment-facing prospective decision right.
- Evidence: [internal/memory/dream.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/memory/dream.go); [internal/memory/soul_maintenance.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/memory/soul_maintenance.go); [internal/memory/hook.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/memory/hook.go); [internal/memory/soul.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/memory/soul.go); [docs/guide-memory.md](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/docs/guide-memory.md).
- Basis: structural + explicit.
- Confidence: medium for material candidate; uncertain for positive S4.
- Caveats: No unsupported negative `—` is published here; this source-native ambiguity should be independently reviewed..


## S5 — Policy and identity

- State: —
- Function: No first-party runtime identity/ultimate-policy issue, legitimate ultimate authority and authoritative return path at the selected project recursion.
- Disturbance / variety regulated: Safety permissions, operator consent and task purpose are not ultimate identity-policy disputes.
- Decisive decision or feedback right: None at the relevant S5 level.
- Decision owner: User/institution controls deployment and action policies outside a first-party S5 closed loop.
- Supporting / enforcement mechanisms: Permissions, sandbox, deterministic limits, Git remote guard, operator morning branch review, instructions.
- Closure path: Approving file/shell execution or merging local commits is bounded operational authority, not an S5 final identity/ultimate-policy decision returned to the organization.
- Why this is / is not agent-owned: Static constitutions, agent identity prompt and human review/approval alone do not prove the S5 governance function.
- Evidence: [internal/autopilot/fleet.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/fleet.go); [internal/autopilot/autopilot.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/autopilot/autopilot.go); [internal/subagent/manager.go](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/internal/subagent/manager.go); [README.md](https://github.com/whyiyhw/seek/blob/52e90e68b9b1f266f7eff952426eb996ec7f87f9/README.md).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: This is boundary-scoped, not a claim no human can govern a Seek deployment..

### Absence scope

- Surfaces inspected: Native permission/sandbox/report/worktree paths, Autopilot no-remote guard, go agent and configuration/docs.
- Plausible first-party paths checked: Operator approvals, policy configuration, manual merge/release, identity prompt, goal selection.
- Why no material first-party path remains: No shipped first-party institutional or autonomous ultimate-policy adjudication and return to later organization behavior is identified; action approvals and human branch integration are not S5.


## Distributed OSS parent arrangement

Public contributors, repository CI and release systems are adjacent to installed Seek systems and are not credited as organization-level parent VSM functions of a particular user's coding-session recursion. The user reviewing Autopilot worktree commits does not automatically constitute S5 ultimate-policy governance or first-party S3/P modes.

## Self-hosted and non-human modes

Seek can use third-party inference or operator-selected providers but all claimed function ownership depends on the first-party mode wiring and decision/feedback paths, not model names. Autopilot S2 is an autonomous *pre-run* mode rather than an inference that every installed instance always uses a multi-agent fleet. Human permission gates and morning branch reviews are operational boundary constraints, not an additional S3/S4/S5 parent mode.

## Recursion

Bounded child coding workers have real task/environment discretion at a lower operating-cell level. Spawning alone is not VSM recursion; the model-directed interference attenuation at the focal project level, when enabled in Autopilot, is what supports the S2 claim. The deterministic runner does not own the planning judgment, nor do external providers own the Go harness's deployment boundary.

## Variety and escalation

Tool failures return to the model; separate worktrees prevent direct overlapping file edits and outputs remain separate branches for human inspection. Bounded goal, child-count, time, permission and no-remote guards constrain work. A failed child appears in a summary but does not automatically trigger agentic multi-unit reprioritization. Optional memory distillation may change future prompts, but classification of S4 ownership remains unresolved.

## Evidence gaps

- S2 is **restricted** to prospective file-conflict attenuation in first-party Autopilot and does not claim automatic conflict recovery after fanout, independent code integration or ongoing negotiation among workers.
- S3 is negative because the source shows a bounded deterministic fleet plus human follow-up rather than a separate whole-current discretionary management loop; if other shipped supervisory modes are subsequently demonstrated, reassess explicitly at the same frozen ref.
- S3* is negative for the standard TUI reviewer, which shares the primary agent review channel, and the single-worker goal judge.
- S4 remains `?`: model-derived cross-project traits and automated evidence thresholds could support future agent behaviour, but source alone does not settle a function-specific, external-and-prospective organizational adaptation decision right.
- No task benchmark or runtime success-rate measurement is inferred from the project's own promotional demos or existing evaluation files.
