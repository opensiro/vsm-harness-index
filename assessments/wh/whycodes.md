---
harness_id: whycodes
project_name: WhyCodes
repository: https://github.com/whycorporation/whycodes
review_ref: ef5126824739673d93815b29456ba3e5bdddf87c
reviewed_at: 2026-10-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# WhyCodes

## Review boundary

- System in focus: shipped first-party WhyCodes Rust coding runtime and supported CLI/TUI/headless/server agent modes, including registered `task` and model-invoked `swarm` orchestration of independently model-running subagents in a shared checkout or isolated git worktrees.
- Purpose and identity: perform software engineering requests with model-selected tools, optionally partitioning one complex present task into several concurrent agents whose source changes are reconciled into the user's workspace.
- Relevant environment: local git/non-git checkout, tool permissions and sandbox, configured model/provider endpoints, session/history store, code/index/memory aids, on-demand subordinate agents and user-facing TUI/SDK surfaces.
- Standard-distribution boundary: first-party `whycodes` agent model/tool loops, built-in `build` and `plan`/`ask` roles, built-in `general`/`explore`/`scout` subagents, default-enabled `swarm`, in-process claim mailbox and worktree merging; not user-maintained external agent organizations or CI/eval experiments.
- Credited operating / distribution surfaces: [README.md](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/README.md); [architecture.md](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/docs/architecture.md); [mod.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/mod.rs); [turn.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/turn.rs); [gate.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/gate.rs); [dispatch.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/dispatch.rs); [swarm.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/swarm.rs); [swarm.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/tools/src/agent_tools/swarm.rs); [swarm_worktree.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/swarm_worktree.rs); [file_claims.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/core/src/file_claims.rs); [swarm_hub.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/core/src/swarm_hub.rs); [subagent.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/subagent.rs); [types.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/config/src/types.rs); [mod_tests.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/mod_tests.rs).
- Adjacent first-party surfaces excluded from ownership: non-runtime GitHub CI/release/benchmarks, website/marketing/docs archive, unrelated user/enterprise governance, manually orchestrated independent remote clients, external provider/MCP effects and standalone developer test tools. Tests corroborate the wired runtime but do not donate autonomous control themselves.
- First-party operating / deployment modes considered: ordinary model/tool coding session; optional `task` single subagent; native `swarm` call (default enabled) with bounded parallel `general` coding S1s and `explore`/`scout` read-only variants; default git-worktree execution with three-way guarded merge and non-git/opt-out same-checkout mode with exclusive file claims.
- Recursion level: top-level current coding lead over independently model-running subordinate worker S1 units for one task/swarm wave. In single coding-agent use without spawned workers, only S1 is exercised; this does not claim operating governance over an external organization.
- Reviewed revision: `ef5126824739673d93815b29456ba3e5bdddf87c`.
- Observation date: 2026-10-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[architecture.md](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/docs/architecture.md) identifies the shipped code layers: executable CLI/TUI/server → Agent model turn → tool registry and subagents. [turn.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/turn.rs) maintains the model/tool result loop, while [gate.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/gate.rs) intercepts `swarm` and `task` calls into first-party agent methods. [types.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/config/src/types.rs) explicitly enables `swarm` by default, with four concurrent members unless configured lower/higher (hard cap eight), and worktree mode enabled by default.

[dispatch.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/dispatch.rs) parses model-specified work units, models/worker types, paths and max turns, allocates a per-swarm `FileClaimRegistry` and real `SwarmHub`, and schedules model-running workers. [file_claims.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/core/src/file_claims.rs) implements same-checkout per-path exclusive write claims and stale-read notifications; an overlapping preclaim returns an actual error with offending path and owner, before dispatch. In git mode [swarm_worktree.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/swarm_worktree.rs) creates isolated worktrees, then three-way compares base/worker/main and refuses unsafe overlapping merges, returning specific merge conflicts rather than silently replacing diverged main content. [dispatch.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/dispatch.rs) records worker success/failure, merge conflicts, source-changed results and a whole-wave report to the parent model; [swarm_hub.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/core/src/swarm_hub.rs) and [swarm_message.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/tools/src/agent_tools/swarm_message.rs) implement actual between-worker mailbox delivery rather than a placeholder.

These technical mechanisms are separate from the root model's decisions about decomposition, worker scopes and follow-up work after observing the aggregate current wave. They provide native executable interference attenuation and wave-status evidence, but no automatic independent correctness-reviewer verdict. Permission/sandbox and memories are contextual/constraint machinery, not automatically S4/S5.

## Operational model

A model-led coding session can invoke `swarm` with several subtasks and optional exclusive paths. Independently model-running workers proceed concurrently within an enforced limit. The configured isolation mode enforces non-collision by separate working trees with conflict-aware merge, or a shared checkout with per-file claims and conflict/stale-read feedback. Results return to the same root model's ongoing tool turn, allowing it to choose another corrective batch, revised scopes or direct edits. This is bounded to current workflow waves; no real-time preemption of every running agent or global fleet supervisor is claimed.

## S1 — Operations

- State: A
- Function: take discretionary local codebase engineering actions and repairs via first-party model-selected tools, and independently execute model-owned delegated subtask work.
- Disturbance / variety regulated: unknown code state, compilation/test failures, incomplete edits, missing information and live tool error observations.
- Decisive decision or feedback right: the root or child coding model chooses its own repository read/edit/shell operations and responds to real outcomes.
- Decision owner: active language-model agent within the standard runtime; a spawned `general` worker has its own model/tool context.
- Supporting / enforcement mechanisms: turn loop, tool/permission gate, local session and persistent history, code tools and optional subagent process/worktree.
- Closure path: engineering request → model-selected tools → actual local execution/result → next tool/repair choice or completion.
- Boundary reachability: normal `whycodes` agent loop and first-party registered `task`/`swarm`, not only tests.
- Why this is / is not agent-owned: fixed dispatch/sandbox and memory cannot choose a context-sensitive code change without the model's discretionary action.
- Evidence: [README.md](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/README.md); [turn.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/turn.rs); [gate.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/gate.rs); [dispatch.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/dispatch.rs); [subagent.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/subagent.rs); [mod.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/mod.rs)
- Basis: explicit / structural
- Confidence: high for executable source wiring, no credentialed provider task
- Caveats: deterministic merge, permission checks and worktree isolation are supporting enforcement, not additional autonomous coding S1s.

## S2 — Coordination

- State: C
- Distinct S1 units: concurrent first-party model-running `general` or other delegated coding workers in one `swarm` task wave; each has independent model turn/tool decisions and an assigned scoped goal.
- Inter-S1 disturbance: two worker S1s can claim/write an overlapping source file in the same checkout, observe an out-of-date version of another worker's changed file, or contribute overlapping changes that would overwrite diverged main checkout content when merging isolated worktrees.
- Attenuating coordination relation: `FileClaimRegistry` refuses double ownership, logs/reports stale reads and actively emits `FileConflict`; preclaims reject inconsistent `paths` before work; default separate worktrees quarantine writes and three-way guarded merge declines conflicting paths rather than silently clobbering main.
- Feedback into subsequent S1 behaviour: a conflicting same-checkout writer receives a tool denial/conflict owner, an attempted preclaim returns an immediate error to parent, and worktree conflicts appear in worker/aggregate results so the parent can narrow scopes or retry/reassign. Nonconflicting file changes are applied to the main checkout.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: these first-party checks regulate concrete multi-S1 interference over *the same file's ownership or merged effects*, not merely launch tasks or display messages.
- Function: attenuate source-file/merge interference among multiple independently model-running coding S1 workers.
- Disturbance / variety regulated: concurrent overlapping file writes, stale reads and conflicting post-worktree integration.
- Decisive decision or feedback right: deterministic same-checkout file-claim gate and three-way merge decide whether a conflicting write or integration may proceed; conflict event/result names the current owner/path.
- Decision owner: deterministic first-party coordination constructor (C), not an autonomous S2 model.
- Supporting / enforcement mechanisms: shared registry, worker-specific context, read/write tool hooks, preclaim checks, worktree creation/merge, conflict events and status reports.
- Closure path: independent workers approach same source path → exclusive claim or guarded merge compares ownership/base/main → unsafe action is blocked or marked conflicted → affected worker or root receives conflict information → subsequent work can adopt safe scoped action/repair.
- Boundary reachability: [types.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/config/src/types.rs) default enables swarm/worktrees; [gate.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/gate.rs) and [dispatch.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/dispatch.rs) execute code-owned `swarm` entrypoint and claims/merge in supported modes.
- Why this is / is not agent-owned: interference-specific admission/merge outcome is coded and remains if model decision-making is removed; the model may *respond* as S3 but does not own the fixed S2 conflict rule.
- Evidence: [swarm.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/tools/src/agent_tools/swarm.rs); [file_claims.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/core/src/file_claims.rs); [swarm_worktree.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/swarm_worktree.rs); [dispatch.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/dispatch.rs); [subagent.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/subagent.rs); [swarm_hub.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/core/src/swarm_hub.rs); [mod_tests.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/mod_tests.rs)
- Basis: explicit first-party code paths and regression tests
- Confidence: high for bounded technical write/merge conflict regulation
- Caveats: same-checkout conflicts are observed only through claimed file operations; undeclared semantic conflicts and independent manually launched sessions are not guaranteed covered. Worktree conflicts can remain for manual/follow-on resolution.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: the root's `swarm` result aggregates every invoked worker's type, goal, completion/failure, duration, output, merge conflicts and applied file effects into one current-wave report; the parent retains the ongoing model conversation and tool outcomes.
- Current-control decision scope: root model selects an initial set of worker roles, scope/path ownership and concurrency, then can elect an additional/corrective wave, change active task scope assignments for the *next* wave, or directly repair integration issues based on aggregate current worker status/conflicts.
- Function: manage the current set of delegated coding commitments through model-selected work partitioning and evidence-based follow-on assignment/correction between waves.
- Disturbance / variety regulated: uneven worker completion, failed tasks, merge conflicts, integration tradeoffs and current coding workload allocation.
- Decisive decision or feedback right: root model selects which present work to assign to which subordinate type and scope, and how to revise current remaining work after observing whole-wave results.
- Decision owner: top-level model over the supported first-party `swarm` mode, not fixed semaphore/worktree merge code.
- Supporting / enforcement mechanisms: `swarm` task spec/tool contract, aggregate report with per-member status/conflicts, model turn tool-result return, and S2 guarded application.
- Closure path: model assigns a concurrent worker roster → independent workers act and current report returns including failures/conflicts → model can choose changed worker brief/scope, follow-up task or repair → next first-party tool/run applies the revised commitment.
- Boundary reachability: default-enabled first-party `swarm` in actual `Agent::run_turn` execution, not an unwired utility or example.
- Why this is / is not agent-owned: deterministic worker scheduling and reporting cannot determine appropriate future *current-job* assignments or repairs absent the root model's discretion.
- Evidence: [swarm.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/swarm.rs); [swarm.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/tools/src/agent_tools/swarm.rs); [dispatch.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/dispatch.rs); [gate.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/gate.rs); [turn.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/turn.rs); [types.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/config/src/types.rs); [subagent.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/subagent.rs)
- Basis: structural, with supported tool-model response loop
- Confidence: medium for wave-boundary model-control closure, no live provider session run
- Caveats: manager sees consolidated wave results after workers settle; real-time mid-wave organizational reprioritization/preemption and whole-deployment resource policy are not claimed. This is current multi-worker job management, not prospective S4.

## S3* — Complementary audit

- State: —
- Function: no shipped separately owned complementary reviewer established to independently inspect an implementing S1's current completion claim and return a corrective verdict to the first-party S3 current manager.
- Disturbance / variety regulated: incorrect reported code completion or regressions accepted without a separate direct-evidence challenge.
- Decisive decision or feedback right: no independent reviewer verdict/return path within assessed standard modes. A swarm report describes worker outcomes; file merge check detects structural conflicts but not independent semantic quality of coding claims.
- Decision owner: implementing coding model and the root can run ordinary tests/read code; optional human/CI review remains outside system.
- Supporting / enforcement mechanisms: worktree guarded merge, file-claim conflict reports, generic read-only scout/explore workers, permission and test tools.
- Closure path: results are reported to parent coding model; no first-party dedicated independent reviewer claim check → manager judgment → required corrective operation established.
- Why this is / is not agent-owned: generic worker read-only capability or worktree merge safety does not become a separate source-first complementary auditor by labeling output an audit.
- Evidence: [dispatch.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/dispatch.rs); [swarm.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/tools/src/agent_tools/swarm.rs); [subagent.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/subagent.rs); [swarm_worktree.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/swarm_worktree.rs); [README.md](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/README.md); [mod.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/mod.rs)
- Basis: structural review of shipped roles/wiring
- Confidence: medium-high
- Caveats: a user/root may specifically ask a generic scout to review code, but no separate first-party review-and-correct management loop is demonstrated from that hypothetical discretionary composition.

### Absence scope

- Surfaces inspected: standard agent roles, `task`/`swarm` worker profiles, model turn, worktree conflict/merge and tool verification/permissions.
- Plausible first-party paths checked: separate independent evidence reviewer role, direct code/diff examination of worker's completion claim, critical reviewer verdict returned to S3 root and applied corrective assignment.
- Why no material first-party path remains: examined shipped orchestration provides generic workers, source integration controls and result aggregation, but no substantive independent audit ownership/reviewer-specific verdict with corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no future-oriented environmental intelligence and applied organizational capability adaptation owner demonstrated.
- Disturbance / variety regulated: future coding environments, model/provider capability shifts and new classes of tooling.
- Decisive decision or feedback right: no model or legitimate parent selects organizational future capabilities then returns an implemented change.
- Decision owner: user/config/developers set provider/workflow/skills; root handles present coding work and current worker allocation.
- Supporting / enforcement mechanisms: memory, session compaction, skill registry, provider routing, SDK/daemon interface, schedule and contextual tools.
- Closure path: configuration and memory inform current actions, but future environmental sensing → strategic capability selection → applied new operating capacity is not wired as one ownership cycle.
- Why this is / is not agent-owned: adding workers to the current coding task or recalling previous files is S1/S3 present control, not S4 organizational adaptation.
- Evidence: [README.md](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/README.md); [architecture.md](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/docs/architecture.md); [lib.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/memory/src/lib.rs); [mod.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/mod.rs); [types.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/config/src/types.rs)
- Basis: structural
- Confidence: medium
- Caveats: user-authored plugins/repository roadmap may build an external future adaptation system, not credited in this product.

### Absence scope

- Surfaces inspected: first-party memory, plugin/skills/provider settings, runtime task/team selection and SDK/daemon architecture.
- Plausible first-party paths checked: long-horizon external sensing, owned future-capacity choice, enacted organizational reconfiguration and returned changed S1/S3 capabilities.
- Why no material first-party path remains: observed mechanisms serve persistence/configuration and execution of present coding jobs, with no integrated prospective adaptation decision-and-effect loop.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate organizational mission/identity policy authority with binding corrective return.
- Disturbance / variety regulated: choice over organizational purpose/constitutional priorities, beyond acceptance of individual code edits.
- Decisive decision or feedback right: no legitimate S5 owner sets/reconciles final mission values and returns binding governing change to subordinate organizational functions.
- Decision owner: operator/project owners configure prompts, tool capabilities and permissions; model selects execution within the declared scope.
- Supporting / enforcement mechanisms: permission policies and user approvals, tool/shell sandbox, session roles, inherited worker restrictions.
- Closure path: risky tool actions allowed, denied or paused under user/developer rules; neither constitutes an organizational identity-policy choice nor changes the system's governing purpose.
- Why this is / is not agent-owned: per-tool allowed/denied and sandbox boundaries enforce action safety, not ultimate organization policy.
- Evidence: [types.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/config/src/types.rs); [mod.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/mod.rs); [gate.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/agent/gate.rs); [subagent.rs](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/crates/agent/src/subagent.rs); [README.md](https://github.com/whycorporation/whycodes/blob/ef5126824739673d93815b29456ba3e5bdddf87c/README.md)
- Basis: structural
- Confidence: medium-high
- Caveats: maintainer community policy and operators' ultimate system goals remain outside this runtime.

### Absence scope

- Surfaces inspected: model-agent role definitions, config/permissions, sandbox, workforce scopes, user approval and project maintainer boundary.
- Plausible first-party paths checked: identity/purpose dispute → legitimate policy decision owner → enacted binding management outcome in operating agents.
- Why no material first-party path remains: code constrains tools, access, role and worker scope only, without a superior final-purpose authority or closed policy redirection.

## Recursion

Within one local coding task, a root model-led current manager delegates to independently model-running S1 workers in a supported first-party swarm. Deterministic S2 guards physical/logical file interference while root S3 can change present worker assignments based on aggregate reports between waves. Ordinary one-agent operation has one active S1 and does not instantiate these optional multi-agent functions. External human organizations and multiple independent daemon clients do not automatically become a recursively managed deployment.

## Variety and escalation

S1 handles uncertain source edits and tool results. Swarm S2 prevents same-path write claims and rejects concurrent divergent merge effects instead of clobbering shared source; events and aggregate reports return to the root's ongoing coding tool turn. Root S3 can rescope subsequent work and repair present integration damage. Shell/tool safeguards and generic worker reports do not establish an independent S3* semantic auditor, prospective S4 capability planning or ultimate S5 policy authority.

## Evidence gaps

Pinned-source code, documentation and regression-test review; no live API-credentialed swarm run. Positive S2 is bounded to explicit file ownership and guarded merge in first-party swarm modes, not semantic conflict detection across disjoint files. Positive S3 is bounded to wave-level model-directed task allocation and response to whole-wave reports, without asserting a mid-wave live supervisor. Reviewer capability remains generic: no separate shipped independent correction-return chain was shown for S3*. S4/S5 absences are distribution-relative rather than universal impossibility.
