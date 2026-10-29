---
harness_id: epic-harness
project_name: Epic Harness
repository: https://github.com/epicsagas/epic-harness
review_ref: 1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Epic Harness

## Review boundary

- System in focus: Epic Harness's installed agent-host plugin skills, hooks and Rust orchestration/evolution support at the exact pinned revision; not the entire unrestricted Claude Code, Codex, or Antigravity host.
- Purpose and identity: plan/build/review/ship scoped coding tasks through `/orbit`, retain run state, inspect changed artifacts through separate audit modes and adjust future skill prompts from observed failures.
- Relevant environment: changing feature requests, git/code/test results, concurrent agents, regression hazards, reviewer findings, host permissions, installed skills and error-pattern telemetry.
- Standard-distribution boundary: plugin manifest exposes first-party `skills/` and hooks to an installed AI coding host; the `epic-harness` Rust binary persists pipeline state, orchestrator events, memory/evaluation and evolved skills.
- Credited operating / distribution surfaces: `/orbit`, `/go`, `/audit`, `/eval`, `/evolve` skills; `src/orchestrate`, `src/evolve`, hook entry, plugin manifests, local state and installed host agents executing these policies.
- Adjacent first-party surfaces excluded from ownership: dashboard visualization, example tasks and benchmarks, README marketing, optional external CI providers, third-party model/runtime internals and actual GitHub human merge rights.
- First-party modes considered: packaged host-driven `/orbit` execution; automatic or explicit `audit` (including opt-in `--strict`); opt-in `EPIC_ORCHESTRATION=enabled` controls; Rust post-invocation reflect/evolve and candidate skill synthesis.
- Recursion level: current project/task portfolio within one installed host, with specialist S1 builders, constructor bounded conflict avoidance and an orchestration/audit return path; no claimed global corporate S5.
- Reviewed revision: `1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The published plugin places model-executed skills in the host session. `/orbit` detects the task mode, generates a spec, enters an isolated worktree, directs `/go` agent workers through TDD and tool observations, invokes `/audit`'s separately scoped code/security/test reviewers, and returns failures for fixes before creating a reviewable PR. Its flow and bounds are in the pinned skill files, while Rust stores/guards pipeline and optional control messages; the model decision engine is provided by an installed host, not by Rust inference code. In the `--strict` audit mode the source expressly mandates artifact-only reviewer inputs, independent conclusions and exclusion of the builder's identity, then routes findings into the `/orbit` rework gate. A distinct Rust evolution loop mines past session failures and creates/scores future skills, but has no demonstrated prospective *external environment* inquiry.

Pinned source evidence:

- [README: plugin, orbit flow, host modes and skill evolution](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/README.md)
- [Orbit: mode choice, model work, audit, retries, CI and evolve](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/skills/orbit/SKILL.md)
- [Go: TDD agent work, conflicting files and integration](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/skills/go/SKILL.md)
- [Audit: strict trust isolation and complementary code/security/test access](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/skills/audit/SKILL.md)
- [Eval: baseline and regression evidence](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/skills/eval/SKILL.md)
- [Hook wiring to restart context and reflection](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/hooks.json)
- [Orchestration opt-in, agent event return and control directives](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/src/orchestrate/mod.rs)
- [Evolution: memory of failure, proposed skill changes](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/skills/evolve/SKILL.md)
- [Evolution adaptation landscape: persistent failures and untried edits](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/src/evolve/planner.rs)
- [Evolution no-regression seesaw gate](https://github.com/epicsagas/epic-harness/blob/1f3823af536b1f56b3cb8af90cc8ea77ef71c4bd/src/evolve/seesaw.rs)

## Operational model

The user supplies a coding goal; the model-host executes the shipped `/orbit` plan. The model orchestrator selects direct versus council mode, delegates specialist work, reads test/QA observations, retries failures and returns a PR rather than merging on behalf of the user. Constructor-written file conflict and retry rules attenuate overlap. When `audit --strict` is chosen, independent fresh reviewer agents inspect actual diff/spec/tests without builder reasoning or one another's findings, return a synthesized PASS/WARN/FAIL and trigger the orchestration rework path. Rust hooks record events, enforce opt-in user directives, and digest skill failure history for later runs.

## S1 — Operations

- State: A
- Function: model-directed software task execution from request/spec through task decomposition, code/tool intervention, test observation and local repair.
- Disturbance / variety regulated: varied feature requests, test failures, codebase changes, missing context and integration feedback.
- Decisive decision or feedback right: select each next code/tool step, diagnose a failed test or review and revise artifacts until acceptance criteria or escalation conditions are reached.
- Decision owner: host model running first-party `/orbit` and `/go` policies, with spawned specialist model agents owning scoped implementation decisions.
- Supporting / enforcement mechanisms: installed plugin skills, Claude/Codex/agy agent-host tools, TDD protocol, Git worktree, test runner, persistent orbit state and Rust hook state.
- Closure path: user task → generated spec/role work → model-chosen edits/tests → test/reviewer evidence → model retry/adjust/stop → PR or bounded request for user decision.
- Why this is / is not agent-owned: the model agents make changing next-step decisions; Rust's storage and hook checks do not replace model-driven work.
- Evidence: `/orbit`, `/go`, README, `src/orchestrate/mod.rs` (links above).
- Basis: first-party installed protocol and executable host reachability.
- Confidence: medium-high for supported mode.
- Caveats: runtime depends on installed host permissions/tools and the provider; no live E2E/quality certification was performed.
- Boundary reachability: plugin manifests and installation load the first-party skills, and `/orbit` directly invokes model-host workers and returns their observations to its stateful pipeline.

## S2 — Coordination

- State: C
- Function: prevent incompatible concurrently editing builder S1 agents from modifying the same file scope without isolation or sequencing.
- Disturbance / variety regulated: parallel tasks targeting identical files, integration hazards and duplicate build work across worker contexts.
- Decisive decision or feedback right: serialize overlapping tasks or isolate such workers in separate Git worktrees; permit independent files to proceed in parallel.
- Decision owner: constructor-prescribed file-intersection and worktree isolation rules in `/go` and `/orbit`, executed by the model orchestration rather than an unrestricted autonomous policy setter.
- Supporting / enforcement mechanisms: per-task `modifies` list, dependency graph, worktree isolation, agent result states, integration test and multi-agent review.
- Closure path: conflicting pending S1 tasks → overlap/ordering decision → deferred or isolated worker executes → integration results feed later tasks/review, avoiding clobbering simultaneous edits.
- Why this is / is not agent-owned: the S2 relation targets identified shared-resource interference, beyond generic agent messaging or delegation; the governing interference rule is constructor-owned.
- Distinct S1 units: independently executing TDD builder subagents in one `/go` multi-task plan.
- Inter-S1 disturbance: two parallel model workers edit a common file, causing merge/working-tree collision and invalid integration.
- Attenuating coordination relation: explicit `Tasks modifying same files → serialize or use worktree isolation`, with per-task overlap checked before dispatch.
- Feedback into subsequent S1 behaviour: serialized workers only run after predecessors settle; isolated workers return changed trees/results for integration and failed integration feeds the repair loop.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the source names an actual concurrent-write conflict and prescribes isolation/serialization conditional on overlap, altering S1 execution to attenuate interference.
- Evidence: `/go` conflict analysis and parallel execution table, `/orbit` worktree protocol.
- Basis: concrete first-party orchestration constraints and returned integration path.
- Confidence: medium.
- Caveats: the rule is a skill-level scheduling prescription; no universal cross-process conflict detector or measured failure rate is established.
- Boundary reachability: `/orbit` calls `/go`, which requires overlap-aware planning before spawning the installed host model workers.

## S3 — Inside-and-now control

- State: A
- Function: model-led whole-pipeline current control over specs, tasks, worker results, verification, retries and PR readiness.
- Disturbance / variety regulated: changing task scope, failing audits/tests, missing context, partial worker outcomes, CI regressions and crash recovery state.
- Decisive decision or feedback right: choose direct/council mode, integrate task status, dispatch and retry workers, decide phase transition or escalate a repeated failure.
- Decision owner: `/orbit` model orchestration persona, operating the whole current work run under first-party rules and limits.
- Supporting / enforcement mechanisms: persisted `PIPELINE-*.json`, phase history, worktree lock, `/go` integration, `/audit` report, optional `/eval`, CI checks, Rust orchestration events.
- Closure path: goal plus whole-run state → model selects plan and workers → reads every stage's evidence → repairs failed phases or returns final PR/report/human pause.
- Why this is / is not agent-owned: current portfolio decisions are model policy within `/orbit`; Rust state management and audits supply controls and evidence but do not author the task-level strategy.
- Whole-system current view: scope, phase history, worktree state, spec/AC coverage, task result states, cumulative audit failures, optional regression results and PR/CI state.
- Current-control decision scope: which model subagents and phases run next, whether to retry/replan, and when the current workflow is ready to advance to ship or return to the user.
- Evidence: `/orbit` full phase and recovery protocol, `/go` integration, `src/orchestrate/mod.rs`.
- Basis: directly specified current orchestrator decision and closure rights.
- Confidence: medium-high.
- Caveats: not autonomous authority over final GitHub merge or business-wide operations; `EPIC_ORCHESTRATION` advanced directives are opt-in.
- Boundary reachability: `/orbit` is a shipped runnable entry and sequentially reads/writes pipeline state, explicitly consuming audit and worker outcomes.

## S3* — Complementary audit

- State: A
- Function: strict-mode separate code, security/performance and test/AC investigators challenge the current build's claimed completion, returning independent evidence into `/orbit` control.
- Disturbance / variety regulated: missed defects, builder self-certification, false-positive pass claims, review anchoring and hidden spec/test gaps.
- Decisive decision or feedback right: independently inspect artifacts and determine PASS/WARN/FAIL findings that block or redirect current orchestration.
- Decision owner: distinct fresh-context audit agents under the first-party `audit --strict` protocol, not the building agent; orchestrator then owns implementation of corrective action.
- Supporting / enforcement mechanisms: artifact-only diff/spec input, builder session-ID exclusion, blind independent mode findings, tests, lint/security checks, dedup and synthesized audit report.
- Closure path: S1 output/S3 completion claim → separate blind audit modes independently inspect actual diff/tests/acceptance criteria → synthesized finding → `/orbit` gates ship or triggers up to three corrective S1 cycles.
- Why this is / is not agent-owned: these are independent model reviewers using complementary code/security/test access and returning a decision into S3, not merely the same builder reading its own self-report.
- Claim being audited: the build orchestration's statement that all spec requirements are covered, implementation quality is adequate and a PR is ready.
- Ordinary reporting path: `/go`'s builder-submitted DONE/test summary and `/orbit`'s own phase status.
- Complementary access path: independently scoped diff/spec inspection, full test execution and security-review paths deliberately blinded to builder narrative in `--strict` mode.
- Independence boundary: fresh audit agent instances cannot be the builder, cannot see builder session history or other reviewers' conclusions before synthesis; explicit opt-in trust-isolation protocol.
- Who acts on findings: `/orbit` consumes synthesized PASS/WARN/FAIL; failing findings cause repair/re-audit or user escalation, rather than being silently archived.
- Evidence: `skills/audit/SKILL.md` strict audit mode, `/orbit` Step 4/5 and `skills/eval/SKILL.md` optional regression checks.
- Basis: mode-specific structural independence, complementary evidence route and mandatory corrective return.
- Confidence: medium; static source evidence of supported strict mode, not a verified independent deployed audit run.
- Caveats: default audit lacks the explicit strict isolation promises; S3* credit applies only to reachable `--strict` configuration, and external CI/human review independence is not presumed.
- Boundary reachability: the shipped `/audit` skill exposes `--strict`, its three independent model reviewer modes return the report consumed by the installed `/orbit` verdict/retry gate; a user/engagement setting must enable strict mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: multi-session evolution adapts local skills from past failures; it does not establish prospective external-environment sensing and strategic future organizational capability decisions.
- Disturbance / variety regulated: recurrent failed commands, regressions, ineffective prompts and yet-untried skill edit types.
- Decisive decision or feedback right: investigate external future changes/opportunities, select strategic adaptations and return them into the current S3 operational capability.
- Decision owner: Rust deterministic pattern/variant pipeline and optional host synthesis for local skill repair; no independent future-environment intelligence agent found.
- Supporting / enforcement mechanisms: post-invocation `reflect`, historical failure patterns, adaptation landscape, skill variants, seesaw no-regression gate and rollback.
- Closure path: past local observations → failure classification/proposed skill patch → test/rollback/reload next session; no distinct external future view and strategic option selection.
- Why this is / is not agent-owned: evolving a response skill from local historical errors is useful operational learning but not sufficient for VSM outside-and-then S4, even if branded 'self-evolving'.
- Evidence: `/evolve`, `src/evolve/analysis.rs`, `src/evolve/planner.rs`, `src/evolve/seesaw.rs`, `hooks.json`.
- Basis: external-vs-internal feedback discrimination.
- Confidence: medium-high.
- Caveats: future releases could add environmental scouting; the pinned revision is not credited for hypothetical paths.

### Absence scope

- Surfaces inspected: evolve planner, persistent-failure digests, skill synthesis, variant gates, history and post-invocation hooks.
- Plausible first-party paths checked: adaptation landscape as strategic foresight, automatic skill revision as organizational S4 and optional model critic as future intelligence.
- Why no material first-party path remains: all signals derive from past/current task execution; no prospective external environment source and future-oriented organizational policy/capability choice are traced.

## S5 — Policy and identity

- State: —
- Function: scope/permission gates, installed skill identity and human STOP choices constrain code actions but do not establish first-party ultimate identity and policy adjudication.
- Disturbance / variety regulated: unsafe tool use, permission failures, repeated audit failures, runtime installation variance and disputed user intent.
- Decisive decision or feedback right: legitimately decide overarching system purpose and highest-level policy conflicts, returning binding identity choices to operations.
- Decision owner: external user, plugin maintainers and host/provider permissions supply rules; the harness follows them and pauses for user decisions.
- Supporting / enforcement mechanisms: preflight lock, user pause on three failed audits, host permission model, plugin config, worktree restrictions and PR review.
- Closure path: externally given goal and rules → installed operating checks, model's bounded behavior or human pause; no first-party ultimate-policy adjudication loop.
- Why this is / is not agent-owned: ability to create a PR or edit locally evolved skills is not constitutional identity authority over user/system goals.
- Evidence: `/orbit` user gates, README installation/governance, `src/orchestrate/mod.rs` user-directed pause/cancel.
- Basis: separation of external mandates and software enforcement.
- Confidence: high for bounded S5 exclusion.
- Caveats: separate human governance may be S5 in a larger assembled organization; it is not automatically imported here.

### Absence scope

- Surfaces inspected: host permission/engagement rules, orbit pause gate, orchestration opt-in and plugin identity/config paths.
- Plausible first-party paths checked: automatic spec approval as S5, skill evolution as policy setting and orchestrator control action as ultimate authority.
- Why no material first-party path remains: all remain scoped task-control actions or externally authored rules, not legitimate independent redefinition of organizational identity.

## Recursion

Specialist model workers execute scoped task S1 inside the host; `/orbit` governs their present run and receives complementary strict audit evidence. Rust hooks and evolution persist/attenuate operations across sessions, but do not automatically constitute further viable hierarchical VSM levels.

## Variety and escalation

The model host absorbs varied code tasks, while first-party scheduling/worktree protocol reduces overlapping edits. `/orbit` re-plans after audit failures; `audit --strict` sends a separated corrective challenge into current control. Persistent historical failures may change local skill rules between sessions. Repeated failures, interactive ambiguity and external merge authority remain human-gated.

## Evidence gaps

- Static pinned-source audit only; no live model, plugin installation, GitHub publication, CI-run, independent auditor or provider billing was exercised.
- Explicit positive S3* is conditional on the documented strict audit configuration; default audit has weaker isolation and is not automatically credited.
- Several decision flows are host-executed skill instructions, not Rust-native autonomous LLM loops. Supporting Rust code handles state, hooks and evolution; the installed host remains necessary.
- Evolution's empirical quality and regression protection are not independently validated; S4 is intentionally left unsupported because local adaptation is not external strategic anticipation.

## Assessment summary

**Proposed disposition: `included`.** Epic Harness packages model-led coding operations (S1=A), constructor-specified conflict attenuation for parallel builders (S2=C), model orchestrated present task control (S3=A) and a reachable *strict* independent complementary audit/rework route (S3*=A). The local history-based skill evolution engine is not by itself prospective environmental S4, and the software does not own ultimate S5. Vector: **A · C · A · A · — · —**.
