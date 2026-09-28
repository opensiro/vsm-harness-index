---
harness_id: superharness
project_name: superharness
repository: https://github.com/artificemachine/superharness
review_ref: 8bd54bc1ea7db2391190de25087bc638d503e549
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# superharness

## Review boundary

- System in focus: one initialized superharness project operating cell at pinned revision `8bd54bc1ea7db2391190de25087bc638d503e549`, including first-party SQLite task/inbox state, delegation and launcher paths, agent adapters, watcher/operator service, fan-out/swarm execution, worktree isolation, handoff/ledger state, project rules and generated agent instruction surfaces.
- Purpose and identity: coordinate multiple AI coding-agent harnesses against one project contract so tasks can be admitted, dispatched, executed, reviewed, recovered and completed without losing project state or allowing parallel agents to corrupt one another's work.
- Relevant environment: project files and git state, task/dependency portfolio, agent/model availability, subprocess/heartbeat health, handoffs and review outcomes, deadlines, failures, operator commands, project rules, budgets and external model/tool results.
- Standard-distribution boundary: shipped first-party Python/CLI runtime and generated project protocol surfaces at the pinned revision. Repository contributor governance, tests/benchmarks except as corroboration, and aspirational/default-branch changes after the frozen ref are excluded.
- Credited operating / distribution surfaces: ordinary `delegate`/inbox dispatch; background watcher; SQLite contract/inbox/task state; fan-out and swarm modes; worktree isolation; generated project instruction templates; `.superharness/rules/` and their dispatch-context injection; supported operator commands.
- Adjacent first-party surfaces excluded from ownership: GitHub repository maintainership and release policy; CI; documentation claims not matched by frozen runtime; peer-plan-review semantics that are wired incorrectly at the frozen revision; underlying Claude/Codex/Gemini/OpenCode/Pi model/provider internals.
- First-party operating / deployment modes considered: direct/manual delegation; unattended watcher/auto-dispatch; ai-driven lifecycle; supervised/approval-gated operation; parallel fan-out; swarm review/optional auto-merge; owner-maintained project rules/instruction files.
- Recursion level: one superharness-managed software project is the system-in-focus. Model-driven coding agents dispatched to bounded project tasks are S1 units. The watcher regulates the current project work portfolio at S3. Project-owner policy/rules are assessed at the same project recursion.
- Reviewed revision: `8bd54bc1ea7db2391190de25087bc638d503e549`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

superharness is a local, SQLite-backed coordination layer around multiple coding-agent harnesses. It owns the shared project task and inbox state, explicit task lifecycle, delegation prompts/context, agent launcher/adapters, persistent handoffs and ledger, background watcher, operator commands, worktree management, parallel fan-out and swarm review. The underlying coding models remain dependencies, but the first-party harness determines when and under what project context those model-driven workers are launched and how their results return into shared project state.

Parallel execution has a concrete coordination mechanism rather than only a multi-agent label. Fan-out/swarm workers receive distinct git worktrees and branches. This attenuates the specific interference that would occur if multiple coding agents modified the same working tree concurrently; each S1 worker can continue its own model/tool loop and return a diff for later integration.

The watcher supplies a distinct current-control layer over the project portfolio. It reads the shared task/inbox state, dependencies, statuses, process/heartbeat liveness and lifecycle timestamps; admits/dispatches ready work; applies retries and recovery; reconciles dead launchers; enforces lifecycle timeouts and archives/fails/reopens work according to deterministic rules. This is broader than a single task's internal execution loop and therefore closes project-level S3 as constructor-owned control.

Complementary audit is strongest in swarm mode. Multiple S1 workers solve the same task independently in isolated worktrees; first-party code collects their actual git diffs; a fresh reviewer model with `warm_start=False` receives the original task plus those diffs and judges correctness/completeness/code quality. Its winner decision determines the branch selected and, in `auto_merge` mode, which result is merged back into the project. A separate advertised peer-plan-review path is not credited because at this frozen revision its formatted review prompt is discarded and `plan_only=True` routes through ordinary plan-authoring semantics.

Project identity/policy remains parent-owned. Initialization creates user-owned `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and `SOUL.md` instruction surfaces and a `.superharness/rules/` directory. The generic templates define identity, operating constraints, lifecycle obligations and guardrails on behalf of the project owner. Active project rules encode policies/conventions/architecture facts, and first-party delegation automatically injects `all_rules_text(project_dir)` into later agent prompts as `project_rules`. The runtime does not establish an autonomous policy-amendment owner for these ultimate project rules, so S5 is `P`, not `A` or `A(P)`.

## Operational model

At the assessed recursion, dispatched model-driven coding agents are S1 operations. Per-worker git worktree isolation supplies constructor-owned S2 attenuation for concurrent workspace interference. The background watcher owns deterministic inside-and-now project portfolio control at S3. Swarm's fresh reviewer owns S3* judgment over independently produced git diffs. Historical failure/skill distillation remains internal learning rather than S4. Durable project identity, constraints and rules are set by the legitimate project owner and returned to later agent operations, closing parent-owned S5.

## S1 — Operations

- State: A
- Function: perform substantive software-project work through model-driven coding agents launched against bounded tasks with project context, tools and acceptance criteria.
- Disturbance / variety regulated: ambiguous implementation tasks, changing repository state, build/test/tool results, external model uncertainty, failures and task-specific acceptance criteria.
- Decisive decision or feedback right: choose task-specific implementation/reasoning actions and revise subsequent work from observed repository/tool results within the delegated task boundary.
- Decision owner: the dispatched model-driven coding agent (Claude Code, Codex CLI, Gemini CLI, OpenCode, Pi or another supported harness) running through superharness's first-party delegation/adapter path.
- Supporting / enforcement mechanisms: task/contract state, delegation prompt assembly, context hints/rules, SDK/CLI adapters, budgets/timeouts, handoffs and lifecycle state.
- Closure path: shared project task → superharness builds bounded task context/prompt → model-driven agent selects implementation/tool actions → repository/tool results return to the agent → later actions change from those observations → handoff/result returns to shared project state.
- Boundary reachability: direct `delegate`, inbox dispatch and watcher-driven auto-dispatch are shipped first-party operating paths at the frozen revision.
- Why this is / is not agent-owned: removing the model-driven coding actor while retaining SQLite, watcher, adapters and lifecycle code leaves coordination infrastructure but removes the task-specific semantic decisions that perform the software work.
- Evidence: [`README.md`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/README.md); [`src/superharness/commands/delegate.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/commands/delegate.py); [`src/superharness/commands/inbox_dispatch.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/commands/inbox_dispatch.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model/provider internals are dependencies. `A` credits the model-driven S1 actor reached through superharness's first-party runtime, not autonomy of the deterministic coordination machinery itself.

## S2 — Coordination

- State: C
- Function: attenuate interference between concurrently active coding-agent S1 units by isolating their mutable repository work into separate git worktrees/branches before later integration.
- Disturbance / variety regulated: parallel coding agents operating on the same project can overwrite, race with or otherwise corrupt one another's uncommitted workspace changes.
- Decisive decision or feedback right: assign each concurrent worker an isolated first-party worktree/branch and keep its mutable file operations separated from sibling workers until explicit comparison/merge.
- Decision owner: deterministic first-party fan-out/swarm/worktree runtime.
- Supporting / enforcement mechanisms: worktree creation/removal, per-slot branches, parallel worker threads, copied superharness state, diff collection and conflict-aware merge.
- Closure path: multiple S1-capable coding agents are dispatched concurrently → each receives a separate worktree/branch → sibling edits no longer share the same mutable working tree → each worker can continue its own model/tool loop → completed diffs return for comparison/integration.
- Boundary reachability: fan-out and swarm are shipped first-party execution modes using `parallel_dispatch.py`, `swarm.py` and worktree helpers.
- Why this is / is not agent-owned: the isolation relation is selected and enforced by deterministic runtime code even if the model workers are replaced; therefore the coordination decision is `C`, not `A`.
- Distinct S1 units: two or more model-driven coding workers executing substantive project tasks in parallel.
- Inter-S1 disturbance: concurrent edits to the same mutable repository working tree can collide or contaminate sibling work.
- Attenuating coordination relation: first-party creation of a distinct git worktree and branch for each worker/slot.
- Feedback into subsequent S1 behaviour: each isolated worker continues later coding/tool actions against its own stable workspace; completed branches/diffs are then returned to first-party comparison/merge instead of exposing workers to sibling intermediate edits.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping rests on a concrete inter-worker mutable-workspace interference and a mechanism that attenuates that interference, not on delegation or parallelism alone.
- Evidence: [`src/superharness/engine/parallel_dispatch.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/engine/parallel_dispatch.py); [`src/superharness/engine/swarm.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/engine/swarm.py); [`src/superharness/engine/worktree_ops.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/engine/worktree_ops.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: merge conflict handling is downstream integration. The S2 claim is the pre-integration attenuation of concurrent workspace interference.

## S3 — Inside-and-now control

- State: C
- Function: regulate the current project-wide portfolio of admitted work by maintaining a single operational view of tasks/inbox/dependencies/liveness and deterministically dispatching, retrying, recovering, failing or archiving work as conditions change.
- Disturbance / variety regulated: blocked dependencies, stale/overdue tasks, dead launcher processes, retryable failures, missing heartbeats, lifecycle timeouts, concurrent inbox load and tasks that are not yet dispatchable.
- Decisive decision or feedback right: decide whether current project work is dispatchable and apply current-control state transitions across the active portfolio, including dispatch, retry, failure/recovery and archival actions.
- Decision owner: the deterministic first-party watcher/lifecycle engine.
- Supporting / enforcement mechanisms: authoritative SQLite task/inbox state, dependency checks, watcher lock/heartbeat, launcher liveness checks, lifecycle rules, retry writers, task-status writers, auto-dispatch and operator-command reconciliation.
- Closure path: current project portfolio/state is read from the shared SoT → watcher evaluates dependencies, status, liveness, timestamps and policy → runtime selects dispatch/retry/recover/fail/archive transition → shared current state changes → later watcher/agent behaviour uses that updated portfolio state.
- Boundary reachability: the watcher is a shipped background operating mode (`inbox_watch`) and can run unattended; current-control rules are first-party runtime code rather than repository-maintainer procedure.
- Why this is / is not agent-owned: the whole-project current-control judgment here is encoded in deterministic watcher/lifecycle policy. Model workers perform S1 work but do not own this portfolio-level regulatory decision, so the state is `C`.
- Evidence: [`src/superharness/commands/inbox_watch.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/commands/inbox_watch.py); [`src/superharness/engine/lifecycle_rules.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/engine/lifecycle_rules.py); [`docs/ARCHITECTURE.md`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/docs/ARCHITECTURE.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: supervised/approval-gated profiles expose human interventions over individual tasks, but the reviewed evidence does not establish a distinct parent-owned whole-project S3 mode sufficient for `C(P)`. Per-task approve/reject is not promoted into a second project-wide S3 owner.

## S3* — Complementary audit

- State: A
- Function: independently compare actual outputs from multiple S1 coding workers against the original task and select the solution that should be returned into project operation.
- Disturbance / variety regulated: a worker may produce an incomplete, incorrect or lower-quality implementation even when it reports successful completion; comparing only worker self-report would not expose that difference.
- Decisive decision or feedback right: judge candidate solutions for correctness, completeness and code quality from their actual collected git diffs, select the winning slot and provide reasoning.
- Decision owner: the separate model-driven swarm reviewer instantiated by first-party `swarm_dispatch`.
- Supporting / enforcement mechanisms: isolated worker worktrees, deterministic diff collection, fresh reviewer `SDKRunner(..., warm_start=False)`, explicit review prompt/output parser, winner validation and optional winner-only merge.
- Closure path: independent S1 workers produce candidate branches → first-party code collects actual git diffs → a fresh reviewer model receives original task + candidate diffs → reviewer returns `WINNER` + reasoning → winner branch is selected → in `auto_merge` mode only that reviewed branch is merged back into the project.
- Boundary reachability: `swarm.py` is a shipped first-party execution mode built on `parallel_dispatch`; no test-only or contributor-only surface is required.
- Why this is / is not agent-owned: deterministic code gathers evidence and enforces the selected branch, but the substantive comparative judgment over correctness/completeness/code quality is made by the distinct reviewer model.
- Claim being audited: which independently produced worker solution best satisfies the original task and is suitable to return to the project.
- Ordinary reporting path: each worker's own run/result and branch produced in its isolated worktree.
- Complementary access path: first-party `_collect_diffs` reads actual git changes from completed worker branches and supplies those artifacts, plus the original task, to a separate reviewer; the reviewer need not trust worker narrative self-report.
- Independence boundary: workers and reviewer are separate executions; reviewer uses a new `SDKRunner` with `warm_start=False`, a reviewer model/budget surface and a prompt containing candidate diffs rather than any worker conversation context.
- Who acts on findings: `swarm_dispatch`; it validates the reviewer-selected slot, returns the selected branch and, when `auto_merge=True`, merges only that winner into the main project worktree.
- Evidence: [`src/superharness/engine/swarm.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/engine/swarm.py); [`src/superharness/engine/parallel_dispatch.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/engine/parallel_dispatch.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the separate watcher peer-plan-review path is not used as evidence for this mapping. At the frozen revision it formats `_PEER_REVIEW_PROMPT` without retaining/passing the resulting prompt, while its inbox item is `plan_only=True`; the ordinary delegate path describes `plan_only` as plan authoring rather than review. The S3* claim therefore rests solely on the independently closed swarm reviewer path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established at the assessed project recursion.
- Disturbance / variety regulated: superharness records failures, handoffs, decisions and lessons and can distill historical project operation into later hints, but the reviewed surfaces do not establish a distinct model of the outside/future environment that returns adaptation options into current project governance.
- Decisive decision or feedback right: no qualifying S4 prospective adaptation judgment/feedback right is established.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: failure pattern matching, historical handoffs/ledger, `distill`, memory/lessons, insights and later dispatch-context hints.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: an LLM may summarize historical internal project evidence, but internal lessons and retry hints do not by themselves become an outside-and-then organizational function.
- Evidence: [`src/superharness/commands/distill.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/commands/distill.py); [`README.md`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: this negative finding does not deny that superharness learns from prior execution. It distinguishes historical operational learning from Profile S4's external/prospective current-future organizational loop.

### Absence scope

- Surfaces inspected: failure pattern matching; handoff/ledger recall; `distill`; insights/memory; model/adapter selection; scheduler; discussion; watcher current-control; project rules and context injection.
- Plausible first-party paths checked: historical failure learning as S4; distilled skills/lessons; discussion as environmental sensing; schedule/deadline awareness; external model/tool use; swarm reviewer feedback.
- Why no material first-party path remains: reviewed learning surfaces primarily summarize internal operational history or improve execution; external tools/model calls remain part of current S1 work; no separate prospective environmental model and no distinct S3↔S4 current/future adaptation conversation is established at the project recursion.

## S5 — Policy and identity

- State: P
- Function: define and maintain the project's durable identity, operating constraints, guardrails and authoritative project rules that later dispatched agents must follow.
- Disturbance / variety regulated: project-policy drift, inconsistent agent behaviour, unsafe actions, changing owner constraints, architectural conventions and ambiguity about what agents are allowed or expected to do.
- Decisive decision or feedback right: decide the durable owner-authored instruction/rule content that governs later project-agent work.
- Decision owner: the legitimate project owner/operator who owns the generated user instruction files and project rule files.
- Supporting / enforcement mechanisms: generated `AGENTS.md`/`CLAUDE.md`/`GEMINI.md`/`SOUL.md` templates, user-owned refresh semantics, `.superharness/rules/`, `all_rules_text(project_dir)` and automatic `project_rules` injection during delegation.
- Closure path: owner identifies an identity/policy/constraint issue → owner edits durable instruction/rule surfaces → first-party delegation reads active project rules and injects them into later task context (while supported agent CLIs also receive their generated root instruction surfaces) → subsequent model-driven S1 work is governed by the changed owner policy.
- Boundary reachability: `init_project.py` creates these surfaces for an ordinary initialized project and explicitly treats existing root instruction files as user-owned unless `--force` is requested; `delegate.py` automatically injects active rules into later work.
- Why this is / is not agent-owned: no reviewed first-party mechanism grants a model actor ultimate authority to amend these project identity/policy surfaces on its own behalf. The authoritative decision remains with the parent project owner/operator, so the state is `P`.
- Identity / ultimate-policy issue: what the project is, whom the coding agents serve, the operating constraints/guardrails they must obey and the project policies/conventions/architecture facts that bound later work.
- Ultimate authority in each claimed mode: Parent (`P`) — the legitimate project owner/operator who owns and edits the durable root instruction and `.superharness/rules/` surfaces.
- Return-to-operation path: active `.superharness/rules/` are read by `all_rules_text(project_dir)` and inserted into subsequent delegated agent prompts as `project_rules`; generated root instruction files provide durable project identity/guardrail context for supported coding-agent harnesses.
- Evidence: [`protocol/templates/AGENTS.md.template`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/protocol/templates/AGENTS.md.template); [`protocol/templates/SOUL.md.template`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/protocol/templates/SOUL.md.template); [`src/superharness/commands/init_project.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/commands/init_project.py); [`src/superharness/commands/rules.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/commands/rules.py); [`src/superharness/commands/delegate.py`](https://github.com/artificemachine/superharness/blob/8bd54bc1ea7db2391190de25087bc638d503e549/src/superharness/commands/delegate.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic editability is not itself the S5 evidence. The positive mapping depends on the explicit identity/guardrail semantics of generated project instructions plus the first-party return path that injects owner-maintained project policies into later delegated work.

## Distributed OSS parent arrangement

The public GitHub repository's maintainers and release process are outside the deployed project boundary and do not donate S5. The `P` state is instead the supported parent relationship inside an initialized project: the legitimate project owner/operator owns the durable project identity, constraints and rule surfaces that later agents receive.

## Self-hosted and non-human modes

superharness is local/self-hosted and can run unattended through the watcher. That does not remove the parent ownership of S5: unattended task dispatch/recovery uses already-defined project policy. Likewise, human plan approvals or task closes are not separately promoted to `C(P)` for S3 because the positive project-wide current regulator is the deterministic watcher; the inspected human controls are primarily task-level interventions.

## Recursion

One managed project is the assessed viable-system boundary. Individual dispatched coding agents, including parallel fan-out/swarm workers, are S1 units when they own bounded substantive implementation outcomes. The watcher is mapped one recursion level above them because it holds and regulates the shared current portfolio. Swarm reviewer activity is complementary audit of S1 outputs at that project recursion. Owner-authored rules constrain the same project's later S1 operation.

## Variety and escalation

superharness attenuates operational variety with explicit task states, dependencies, worktree isolation, bounded retries, lifecycle timeouts, liveness checks, budgets, rule injection and review. It amplifies response variety by routing work across multiple coding-agent harnesses/models and by fan-out/swarm execution. Escalation appears through approval-gated modes, failed reviews, operator commands, blocked dependencies and unrecoverable lifecycle failures; these channels remain mechanisms inside the mapped functions rather than standalone VSM functions.

## Evidence gaps

- S2 is intentionally tied to concurrent mutable-workspace interference and worktree isolation; generic queues/delegation are not counted as S2.
- S3 credits the project-wide SQLite/watcher current-control loop, not each task's local status machine in isolation.
- S3* credits only the swarm reviewer path. The frozen peer-plan-review implementation contains a prompt-wiring defect and is explicitly excluded from the positive claim.
- S4 remains absent despite real historical distillation/failure learning because no distinct external/prospective adaptation loop is established.
- S5 is parent-owned only. The assessment does not infer autonomous policy authority merely because coding agents can edit repository files in ordinary implementation work.
