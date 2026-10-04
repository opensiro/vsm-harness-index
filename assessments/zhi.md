---
harness_id: zhi
project_name: Zhi
repository: https://github.com/mikemikimike/zhi
review_ref: f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Zhi

## Review boundary

- System in focus: Zhi's first-party terminal coding loop at frozen revision `f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56`, including CLI loop composition, scaffold generation/model invocation, critic plant, aggregate/Pareto gate, optional autonomous worktree/test/security/PR/CI path, and bounded recovery.
- Purpose and identity: accept a coding goal, generate a bounded code scaffold, independently challenge the generated artifact with first-party critic/evaluation machinery, and either block/retry or advance the artifact toward commit/PR completion.
- Relevant environment: user goal, generated code, optional Git worktree, local repository/toolchain, model provider, critic findings, test/security evidence, GitHub PR/CI state and bounded retry/budget conditions.
- Standard-distribution boundary: `src/cli/`, `engine/loop/`, `engine/build/`, `engine/critic/`, `engine/eval/`, `engine/resil/`, `engine/orch/`, `engine/model/` and first-party Git/gh wiring are inside when reachable from the shipped CLI. Repository-development CI, marketing claims, docs that describe uninstantiated behavior, and adjacent tests/examples are not credited as owners.
- Credited operating / distribution surfaces: default CLI loop; cloud-model generation when `MODEL_API_KEY` is configured; deterministic local-stub fallback; first-party critic plant and aggregate gate; optional `ZHI_AUTO_PR=1` worktree/eval/commit/PR/CI path; bounded recovery and circuit-breaker wiring.
- Adjacent first-party surfaces excluded from ownership: standalone design claims, repository CI used to develop Zhi, test-only fixtures, unfinished/simulated orchestration behavior that is not a production operational actor, and modules not reachable from the default/auto-PR CLI composition.
- First-party operating / deployment modes considered: non-TTY and TTY CLI; local-stub and cloud invoker selection; ordinary offline loop; `ZHI_AUTO_PR=1` autonomous Git/PR mode.
- Recursion level: one Zhi goal-to-artifact loop is the focal operation. The critic/eval path is a complementary constructor audit channel at the same harness recursion, not a second production S1.
- Reviewed revision: `f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The shipped CLI creates one `LoopDriver` and runs state handlers built from `offlineDeps`, optionally enriched by `autonomousDeps` when `ZHI_AUTO_PR=1`. The reachable state sequence is `INTAKE → PLAN → ISOLATE → EXECUTE → CRITIQUE → EVALUATE → COMMIT → PR_OPEN → CI_WATCH → DONE`, with gate failures returning through `RECOVER` into another execution attempt.

The PLAN surface parses the goal and builds a deterministic DAG/schedule, but the production `DefaultOrchestratorRunner` is not a multi-worker coding organization: at the frozen ref it walks steps sequentially and simulates completion/tokens. This does not establish multiple same-recursion S1 actors.

EXECUTE invokes `engine/build/core/scaffold.ts`, which creates a bounded domain scaffold and, when a model invoker is available, asks the selected model to generate file content. `MODEL_API_KEY` selects the cloud invoker; otherwise the shipped local deterministic stub is used.

CRITIQUE runs the first-party critic plant over generated code. At the reviewed ref the production `composeCritiques` path invokes eleven implemented checks (including security, architecture, maintainability, style, TODO, imports and SLOC) despite broader README language about fifteen critics. Scores are aggregated and then EVALUATE applies the Pareto threshold. In auto-PR mode, EVALUATE additionally runs actual worktree secret scanning/tests, and CI_WATCH can return red status into RECOVER.

Primary evidence:

- [CLI entry](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/src/cli/index.ts)
- [CLI loop command](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/src/cli/commands/loop/loop.ts)
- [offline loop dependencies](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/src/cli/offline-deps/offline-deps.ts)
- [autonomous PR dependencies](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/src/cli/autonomous-deps/autonomous-deps.ts)
- [loop handler builder](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/loop/wiring/handlers/builder.ts)
- [loop transitions](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/loop/states/states.ts)
- [scaffold generator](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/build/core/scaffold.ts)
- [model invoker selection](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/model/invoker/select.ts)
- [critic composition](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/critic/plant/compose.ts)
- [single-critic runner](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/critic/plant/run-critic/index.ts)
- [critic aggregate](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/critic/aggregate.ts)
- [evaluation coordinator](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/eval/eval.ts)
- [evaluation gate](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/eval/gate.ts)
- [bounded recovery](https://github.com/mikemikimike/zhi/blob/f7a0b5ebabdc4afd299f7ba3cac1ece39af39a56/engine/resil/retry.ts)

## S1 — Operations

- State: A
- Function: turn a user coding goal into generated source artifacts and, in autonomous mode, carry them through an isolated Git worktree toward commit/PR completion.
- Disturbance / variety regulated: heterogeneous goal text, model-generation variation/failure, artifact verification failures, critic findings, test/security failures, CI failure and bounded retry conditions.
- Decisive decision or feedback right: in cloud mode the selected model determines generated source content for the scaffold files; subsequent loop progress depends on returned generation and audit evidence.
- Decision owner: the configured model-backed Zhi generation actor on the shipped `MODEL_API_KEY` path.
- Supporting / enforcement mechanisms: goal parser/DAG builder, scaffold template, model invoker seam, loop state machine, worktree/Git wiring, retry budget, circuit breaker and deterministic gates.
- Closure path: user goal → deterministic plan/scaffold framing → model generates file content → Zhi records the generated artifact → critic/eval evidence determines retry or advancement → accepted output can proceed to commit/PR.
- Boundary reachability: `selectInvoker` chooses the cloud model in the ordinary shipped loop whenever `MODEL_API_KEY` is present; no development-only path is required.
- Why this is / is not agent-owned: removing the model actor while retaining the state machine and templates leaves only the deterministic local stub/template behavior and removes the open-ended source-content judgment credited here.
- Evidence: `src/cli/offline-deps/offline-deps.ts`; `engine/build/core/scaffold.ts`; `engine/model/invoker/select.ts`; `engine/model/invoker/cloud.ts`; loop handler builder.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the operational scope is narrower than README language about a general-purpose iterative coding agent; the frozen implementation generates a bounded scaffold rather than exposing a general model/tool editing loop.

## S2 — Coordination

- State: —
- Function: no same-recursion coordination function among multiple operational S1 units was established.
- Disturbance / variety regulated: the goal may be decomposed into DAG steps, but the frozen production orchestration runner does not instantiate multiple independent coding S1s whose interference requires coordination.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: DAG construction, topological ordering, allocation/scheduling metadata, loop sequencing and worktree isolation.
- Closure path: no concrete inter-S1 disturbance → coordination decision → changed peer behavior loop is present.
- Why this is / is not agent-owned: deterministic task decomposition and sequencing operate inside one focal coding process; they do not create or coordinate multiple autonomous operational units.
- Evidence: `engine/orch/runner/runner.ts`; `engine/orch/runner/dag.ts`; `engine/orch/runner/allocator.ts`; CLI/offline dependencies.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: module names and README references to orchestration/concurrency do not override the frozen runtime implementation.

### Absence scope

- Surfaces inspected: goal parser, DAG builder, allocator/scheduler, production orchestrator runner, loop state machine, worktree path and critic/eval plurality.
- Plausible first-party paths checked: DAG scheduling as coordination; critic plurality as peer coordination; worktree isolation as collision control.
- Why no material first-party path remains: there are no two distinct production S1 coding units with a structurally evidenced interference relation; the inspected mechanisms decompose, sequence or audit one operation.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function over a portfolio of operational S1 commitments/resources was established.
- Disturbance / variety regulated: loop phase, retry budget, breaker state, token/step limits and commit-readiness are regulated, but all remain controls over one focal operation.
- Decisive decision or feedback right: not established at S3 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `LoopDriver`, bounded retries, circuit breaker, stage budget/timeout guards, worktree isolation and gate transitions.
- Closure path: no whole-current view of multiple S1 operations plus substantive portfolio intervention loop was found.
- Why this is / is not agent-owned: the conductor is a deterministic state machine; it enforces preselected transitions and thresholds rather than exercising discretionary whole-system management.
- Evidence: `engine/loop/driver.ts`; `engine/loop/states/states.ts`; `engine/loop/wiring/handlers/builder.ts`; `engine/resil/`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: robust conductor/recovery control is not by itself VSM S3.

### Absence scope

- Surfaces inspected: conductor, loop context, metrics, budget/retry/breaker state, orchestration runner and auto-PR lifecycle.
- Plausible first-party paths checked: conductor as manager; retry/breaker as resource control; scheduler as current portfolio allocator.
- Why no material first-party path remains: the implementation regulates one goal-to-artifact loop and lacks a distinct whole-system authority over several operational units/commitments.

## S3* — Complementary audit

- State: C
- Function: independently challenge whether the generated artifact is fit to advance by inspecting code through a separate deterministic critic/evaluation path and blocking advancement when that evidence fails.
- Disturbance / variety regulated: generated code can look acceptable to the producing model while containing security sinks, architecture violations, TODOs, excessive size/style issues, leaked secrets, failing tests or red downstream CI.
- Decisive decision or feedback right: first-party deterministic critic/eval machinery independently computes findings/scores and a pass/fail commit-readiness gate; in autonomous mode test/security and CI evidence can independently veto advancement.
- Decision owner: constructor-owned deterministic critic/eval/gate machinery; no separate autonomous reviewer model owns the audit judgment.
- Supporting / enforcement mechanisms: `composeCritiques`; `runCritic`; weighted `aggregate`; Pareto threshold; `gate`/`gatePass`; optional real tests/secret scan; CI watch; bounded RECOVER transition.
- Closure path: model-produced artifact → independent critic/eval path examines artifact/runtime/toolchain evidence → gate pass advances to COMMIT, gate/CI failure routes to RECOVER → loop returns to ISOLATE/EXECUTE for another attempt or stops when bounded recovery is exhausted.
- Boundary reachability: CRITIQUE and EVALUATE are standard shipped loop states; the richer test/security/CI path is reachable through the documented first-party `ZHI_AUTO_PR=1` deployment mode.
- Why this is / is not agent-owned: the audit verdict is computed by deterministic first-party rules/toolchain evidence rather than a distinct autonomous critic actor, so the mapping is constructor-owned (`C`) rather than autonomous (`A`).
- Evidence: `engine/critic/plant/compose.ts`; `engine/critic/plant/run-critic/index.ts`; `engine/critic/aggregate.ts`; `engine/eval/eval.ts`; `engine/eval/gate.ts`; loop handler builder; autonomous deps.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the frozen critic compose path implements eleven checks, not the broader README “15 critic” claim; the audit is code/toolchain-oriented and does not independently prove full semantic satisfaction of the user's goal.
- Claim being audited: that the generated code is sufficiently safe/clean/toolchain-valid to advance toward commit/PR completion.
- Ordinary reporting path: the generation actor produces code and the conductor would otherwise advance the artifact through the loop.
- Complementary access path: deterministic critics inspect artifact text/architecture independently of model self-report; auto-PR mode additionally runs worktree secret scanning/tests and observes CI status.
- Independence boundary: audit observations arise from first-party rules and externalized toolchain/CI outcomes rather than from the generation model's own prose judgment; they can contradict and block the producer.
- Who acts on findings: the conductor applies the gate outcome, routing failures into bounded RECOVER and another EXECUTE attempt or terminating after the retry budget is exhausted.

## S4 — Intelligence / adaptation

- State: —
- Function: no outside-and-future adaptation loop that changes reusable Zhi capability/strategy was established.
- Disturbance / variety regulated: current goal parsing, model routing, knowledge storage and critic feedback help the present execution but do not form a prospective capability-adaptation cycle.
- Decisive decision or feedback right: not established at S4 level.
- Decision owner: not established.
- Supporting / enforcement mechanisms: model router/invoker selection, knowledge store/search/summarization, current-run critique/evaluation and recovery.
- Closure path: no external/future sensing → adaptation option → persistent capability/strategy change → later-operation closure was found.
- Why this is / is not agent-owned: current-run correction and static provider selection do not amount to autonomous prospective redesign of the harness.
- Evidence: `engine/model/`; `engine/knowledge/`; loop/recovery wiring.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository-development plans and future-looking docs are adjacent development artifacts, not runtime S4 for the assessed system.

### Absence scope

- Surfaces inspected: knowledge store/search, model router/invoker, critic feedback, recovery, docs/roadmap references and CLI deployment modes.
- Plausible first-party paths checked: retained knowledge as learning; model routing as adaptation; critic findings as self-improvement.
- Why no material first-party path remains: the inspected mechanisms support present execution or fixed configuration and do not select/persist a prospective organizational capability change.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy decision loop was established at the Zhi runtime boundary.
- Disturbance / variety regulated: thresholds, retry limits, architecture rules, worktree isolation and Git/PR policy constrain execution but remain static operating policy.
- Decisive decision or feedback right: no qualifying identity-level issue is escalated to a legitimate parent authority and returned as binding runtime governance.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: fixed Pareto threshold/configuration, loop transition table, architecture/security rules, Git/PR workflow and human/environment configuration.
- Closure path: no identity/policy issue → legitimate ultimate authority decision → returned governance → changed subsequent operation loop was found.
- Why this is / is not agent-owned: neither the generation actor nor deterministic gate machinery owns an identity-level policy decision; they operate under preconfigured thresholds and workflow rules.
- Evidence: loop states/handlers, eval gate, critic rules, CLI configuration and Git wiring.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: commit/PR gating is strong operational governance but does not become S5 merely because it controls release progression.

### Absence scope

- Surfaces inspected: loop transition policy, Pareto threshold, retry/breaker settings, worktree/commit/PR/CI rules, AGENTS/docs and CLI environment flags.
- Plausible first-party paths checked: conductor as ultimate authority; quality gate as policy; PR/CI workflow as parent governance.
- Why no material first-party path remains: these surfaces govern task/artifact progression and safety, not a genuine identity/ultimate-policy question at the chosen recursion.

## Recursion

The focal recursion is one Zhi goal-to-artifact execution. Critic/eval machinery is complementary audit within that harness. The deterministic planner/DAG runner does not establish separately viable operational units at the reviewed ref.

## Variety and escalation

Zhi attenuates current-run variety through deterministic planning, bounded generation retries, circuit breaking, critic scoring, test/security evidence, gate thresholds, worktree isolation and CI feedback. Gate failures escalate into a bounded recovery cycle, while exhausted/fatal conditions terminate rather than spin indefinitely.

## Evidence gaps

No `?` state is required. The exact pinned runtime is sufficiently explicit to establish model-owned S1 in cloud mode and constructor-owned S3* through the reachable critic/eval gate. The same evidence also bounds orchestration, recovery, knowledge and policy mechanisms without promoting them to S2/S3/S4/S5.

## Assessment summary

Zhi closes autonomous S1 through its shipped cloud-model generation path and constructor-owned S3* through a separate deterministic critic/evaluation channel that can veto commit-readiness and send the loop into bounded recovery. Its conductor, DAG scheduler and recovery machinery govern one focal operation rather than a multi-S1 S2/S3 organization, and no prospective S4 or identity-level S5 closure is established.

**Vector:** A · — · — · C · — · —
