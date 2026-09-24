---
harness_id: redteam
project_name: redteam
repository: https://github.com/AscendyProject/redteam
review_ref: c2bedf14aca43cc03330503f35e60e12b72f37ee
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# redteam

## Review boundary

- System in focus: one first-party redteam batch execution at pinned revision `c2bedf14aca43cc03330503f35e60e12b72f37ee`, including the repository-owned orchestrator, persisted task/phase state, planner/implementer/reviewer/rescue role dispatch, verification and review/correction transitions, optional goal-mode task dependencies, tier/gate configuration and draft-PR production.
- Purpose and identity: turn human-authored coding tasks or a batch goal into reviewed code changes and draft pull requests through an autonomous worker plus an adversarially separate reviewer, with bounded retries/escalation and operator control over final merge.
- Relevant environment: the target Git repository and codebase, human-authored task/goal inputs, Claude/Codex provider runtimes, project hard rules/security checklist/test conventions, Git/GitHub, test/tool executables and optional human intervention at configured gates or escalations.
- Standard-distribution boundary: the shipped `.redteam/workflows/` runtime, phase runners, provider adapters, templates/configuration and prompts that execute the documented agent-pair/TDD flows. External model/provider internals, the target project's own code and GitHub merge authority remain environmental dependencies.
- Credited operating / distribution surfaces: `README.md`; `.redteam/workflows/orchestrator.py`; `.redteam/workflows/phase_runners/implement.py`; `.redteam/workflows/phase_runners/review_code.py`; `.redteam/workflows/adapters/`; `.redteam/config.toml`; `.redteam/templates/state.template.json`; shipped project-context/security/test-policy inputs reached by the runtime.
- Adjacent first-party surfaces excluded from ownership: `.redteam/batches/` dogfood/development records, `.redteam/tests/`, CI/release machinery, benchmark design/runner result-development artifacts, repository issue/PR history and maintainer governance. These surfaces can corroborate implementation behavior but do not donate S-functions to the installed operating harness.
- First-party operating / deployment modes considered: default `agent-pair` mode; configured tier variants including `review=true` or `review=false`; optional TDD mode; headless cross-provider reviewer path and documented manual-review fallback; optional goal-mode batch dependencies and human gates. The default agent-pair mode is the basis for the positive S3* state.
- Recursion level: one redteam batch/run is the system-in-focus. Each task-local implementation loop contributes operational work; goal-mode may sequence several such task cells, but task nesting/dependency edges are not assumed to be recursive viable systems.
- Reviewed revision: `c2bedf14aca43cc03330503f35e60e12b72f37ee`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

redteam is a persistent coding-agent harness whose default state template starts in `agent-pair` mode. The orchestrator advances tasks through `plan_outcome → plan_review → implement → review_code → create_pr`; `rescue` and human-gate states are entered conditionally rather than forming the ordinary successful path. Task state is persisted after phase transitions so runs can resume.

The implementer is an autonomous worker invoked through a provider adapter. It receives the approved plan plus prior failure/review feedback, edits the target repository, and then the first-party runtime independently runs snapshotted verification commands, commits the worker range and materializes the exact branch diff to be reviewed.

The `review_code` phase is structurally separate. In default agent-pair mode it invokes a fresh headless reviewer over the actual branch diff plus task outcome, prior plan review, project security checklist, hard rules and test conventions. The runtime rejects a configured headless reviewer that resolves to the same provider as the worker. The reviewer returns `APPROVED`, `CHANGES_REQUESTED`, `RESCUE_REQUIRED` or `ASK_USER`. A requested change is routed back to `implement`, with the review body persisted as failure feedback; after the worker changes the repository, `review_code` runs again. Only an approved review advances directly to draft-PR creation.

Goal mode can decompose a human goal into task briefs and a single-parent dependency DAG. The batch scheduler validates the manifest, enforces hard ceilings, blocks children until parents finish and runs task branches against the appropriate base. Those deterministic workflow and dependency mechanisms are separated below from organizational-function ownership.

## Operational model

The primary transformation is producing target-repository code changes that satisfy a task and verification contract. In default agent-pair mode the implementer model owns task-local coding choices while the runtime constrains scope, captures a trusted diff, runs verification and persists state. A distinct reviewer then independently challenges the produced diff. Its findings can force another implementation round, trigger rescue or escalate to a human. The final output is a draft PR; human merge remains outside the autonomous common path.

## S1 — Operations

- State: A
- Function: perform task-local software-engineering work by deciding and applying code changes needed to satisfy the approved task plan.
- Disturbance / variety regulated: repository/task uncertainty, implementation choices, tool/runtime feedback, verification failures and corrective feedback returned from prior review rounds.
- Decisive decision or feedback right: choose the concrete implementation edits and task-local coding actions used to turn the approved plan into a working repository change.
- Decision owner: the autonomous implementer model actor invoked through the configured first-party worker adapter.
- Supporting / enforcement mechanisms: approved-plan prompt construction, provider adapter, branch/baseline isolation, path/scope floors, snapshotted verification allowlist, independent verification command execution, commit/diff integrity checks and persistent task state.
- Closure path: task/plan plus any prior failure or reviewer feedback → implementer model edits the repository → runtime executes snapshotted verification → successful work is committed and materialized as the exact branch diff → the produced operational result enters the review/PR path; failures feed back into another implementation attempt.
- Boundary reachability: `implement` is a normal phase in both shipped agent-pair and TDD execution paths and is invoked directly by the standard orchestrator; no adjacent benchmark or dogfood actor is required to reach it.
- Why this is / is not agent-owned: deterministic floors, verification and commit-integrity gates constrain what can be shipped, but they do not choose the substantive implementation. Removing the implementer model while retaining those mechanisms removes the coding decision right.
- Evidence: [`README.md`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/README.md); [`.redteam/workflows/phase_runners/implement.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/phase_runners/implement.py); [`.redteam/workflows/orchestrator.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/orchestrator.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external Claude/Codex model internals are environmental dependencies; the state is credited to the autonomous role reached through redteam's first-party runtime rather than to deterministic verification.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation is established at the reviewed batch boundary.
- Disturbance / variety regulated: goal mode can contain several task cells with dependency edges and stacked branches, but the reviewed implementation does not establish a specific peer-S1 interference, oscillation or shared-constraint disturbance together with a coordination feedback relation whose organizational purpose is to attenuate that disturbance.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: single-parent `depends_on` edges, topological scheduling, parent-done blocking, branch isolation/stacking, task ordering and shared batch status.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the dependency graph orders work and the deterministic scheduler enforces declared prerequisites; those are workflow/decomposition mechanisms rather than evidence of autonomous S2 discretion over a reconstructed inter-S1 disturbance.
- Evidence: [`.redteam/workflows/orchestrator.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/orchestrator.py); [`.claude/agents/goal-decomposer.md`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.claude/agents/goal-decomposer.md); [`docs/decisions/2026-06-27-goal-mode-design.md`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/docs/decisions/2026-06-27-goal-mode-design.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: downstream users can define dependent tasks whose interaction matters, but generic dependency representation and sequencing do not justify `S2=C` without an S2-specific disturbance/attenuation path.

### Absence scope

- Surfaces inspected: default task pipeline, goal decomposition, goal manifest validation, dependency/topological scheduling, parent-child branch handling, task state and provider-role communication.
- Plausible first-party paths checked: `depends_on` DAG edges, parent completion blocking, stacked task branches, task ordering, batch status and worker/reviewer handoff.
- Why no material first-party path remains: the reviewed paths decompose, order, isolate or gate work. They do not evidence a specific interaction-generated conflict/oscillation among distinct S1 units plus a coordination decision/feedback path that changes subsequent peer behavior to attenuate it. Worker→reviewer correction is instead the complementary-audit relation mapped under S3*.

## S3 — Inside-and-now control

- State: —
- Function: no agent-owned whole-system current-control function is established at the reviewed batch boundary.
- Disturbance / variety regulated: the runtime tracks task phases, retries, dependencies, ceilings, blocker carry-over and rescue/escalation state, but these mechanisms implement a predetermined lifecycle rather than an autonomous whole-system regulator deciding current resource/commitment priorities across operations.
- Decisive decision or feedback right: not established for S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deterministic phase order, retry ceilings, dependency scheduler, tier phase construction, rescue-entry thresholds, verification gates, branch handling and goal-completion accounting.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the goal decomposer can propose task decomposition before execution and task-local reviewers can reject or escalate one work product, but neither path establishes an autonomous actor with a live whole-batch view and authority over shared resources, commitments, priorities or constraints. The runtime scheduler enforces configured/static control decisions without owning agentic S3 discretion.
- Evidence: [`.redteam/workflows/orchestrator.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/orchestrator.py); [`.claude/agents/goal-decomposer.md`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.claude/agents/goal-decomposer.md); [`.redteam/config.toml`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/config.toml).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: rescue/ASK_USER are meaningful exception paths, but task-local exception routing does not become S3 merely because it intervenes in current work.

### Absence scope

- Surfaces inspected: batch scheduler, goal decomposition/dependencies, task state, phase progression, retries, rescue routing, review decisions, tier routing, ceilings, branch creation and completion accounting.
- Plausible first-party paths checked: goal decomposer, `_run_batch`/topological scheduler, retry/rescue escalation, reviewer verdicts, tier downgrade guard and human-gate transitions.
- Why no material first-party path remains: current batch regulation is primarily deterministic execution of prior configuration/manifest choices. No reviewed autonomous actor receives a whole-system current view and exercises discretionary authority over shared operational resources, commitments, priorities or constraints on behalf of the whole batch.

## S3* — Complementary audit

- State: A
- Function: independently challenge the operational worker's claim that a produced code change is safe/correct enough to advance, using a fresh adversarial review path with materially different access and judgment from the implementer's own production loop.
- Disturbance / variety regulated: latent correctness, security, scope and production-risk defects that can remain after the worker's implementation reasoning and ordinary verification path, including flaws the producing model may rationalize or overlook.
- Decisive decision or feedback right: issue the structured review judgment `APPROVED`, `CHANGES_REQUESTED`, `RESCUE_REQUIRED` or `ASK_USER` after inspecting the actual implementation range and relevant project constraints.
- Decision owner: the autonomous reviewer model actor reached through the headless reviewer adapter in default agent-pair mode; the standard configuration resolves it to a provider distinct from the implementer.
- Supporting / enforcement mechanisms: read-only reviewer prompt, branch-diff capture, project security/hard-rule/test-policy inputs, verdict parser, self-review/cross-provider guard, persisted review artifacts/items, deterministic backtrack routing, retry/rescue ceilings and state persistence.
- Closure path: implementer produces and verifies a committed branch diff → fresh reviewer independently inspects the actual diff/repository context and emits a review judgment → `CHANGES_REQUESTED` is persisted as failure feedback and deterministically routes back to `implement` → the implementer receives that feedback and changes the work → `review_code` executes again against the revised range → only `APPROVED` advances to draft-PR creation; severe/persistent findings can instead enter rescue or human escalation.
- Boundary reachability: the shipped state template defaults to `mode: agent-pair`; `AGENT_PAIR_PHASE_ORDER` includes `plan_review` and `review_code`; the repository's standard config separates Claude worker roles from a Codex reviewer; `_adversarial_pairing_error` fails closed if a headless reviewer collapses to the worker provider. The positive path is therefore reachable in the ordinary distribution without borrowing a dogfood or benchmark actor.
- Why this is / is not agent-owned: the reviewer model makes the substantive audit judgment. Deterministic parsing, gating and backtracking merely preserve/execute that judgment. Under the counterfactual owner test, keeping the parser and phase machine while removing the reviewer model removes the independent defect judgment and leaves no equivalent S3* decision.
- Evidence: [`README.md`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/README.md); [`.redteam/workflows/phase_runners/review_code.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/phase_runners/review_code.py); [`.redteam/workflows/orchestrator.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/orchestrator.py); [`.redteam/workflows/phase_runners/implement.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/phase_runners/implement.py); [`.redteam/config.toml`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/config.toml); [`.redteam/templates/state.template.json`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/templates/state.template.json).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a configured `review=false` tier intentionally removes this path, and manual fallback can replace the autonomous reviewer after provider failure. Those supported alternatives do not erase the default autonomous mode. TDD mode has a different reviewer topology and is not required for the `A` finding.
- Claim being audited: the implementer's produced branch diff is an acceptable implementation of the task under the approved plan, security checklist, hard rules and test conventions.
- Ordinary reporting path: implementer output plus first-party verification result, committed implementation range and `impl_diff.patch` produced by the normal work path.
- Complementary access path: a fresh read-only adversarial reviewer directly inspects `git diff <pinned-base>...HEAD` (or a safe incremental round diff with carried findings), the task artifacts and independent project constraints; it is not limited to the implementer's self-report or reasoning trace.
- Independence boundary: in default agent-pair mode the reviewer is a distinct fresh actor and the runtime refuses same-provider worker/reviewer collapse; the reviewer is explicitly blind to the writer's reasoning and sees operational artifacts instead.
- Who acts on findings: the first-party orchestrator records the judgment and routes requested corrections back to the implementer, which receives the persisted review feedback; subsequent review rechecks the revised work before PR creation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective adaptation loop is established in the reviewed operating distribution.
- Disturbance / variety regulated: task retries, reviewer correction, rescue and tier handling respond to current coding work; benchmark/reporting machinery can compare harness configurations for developers, but it is adjacent evaluation/development infrastructure rather than an in-run strategic adaptation actor.
- Decisive decision or feedback right: not established for S4.
- Decision owner: not established.
- Supporting / enforcement mechanisms: retries, rescue, persisted review history, tier configuration, benchmark runner/report generation and developer-maintained configuration.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: current-task correction changes the present work product, not the harness's persistent external/future-facing capability repertoire. Benchmark outputs do not automatically reconfigure later operating runs through an autonomous adaptation decision path.
- Evidence: [`README.md`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/README.md); [`.redteam/workflows/orchestrator.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/orchestrator.py); [`.redteam/workflows/benchmark.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/benchmark.py); [`docs/decisions/2026-07-13-benchmark-design.md`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/docs/decisions/2026-07-13-benchmark-design.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: maintainers can use benchmark evidence to improve redteam over time; repository-development learning is adjacent to the assessed operating harness and does not supply autonomous S4 to it.

### Absence scope

- Surfaces inspected: current-task retry/review/rescue loops, tier/config handling, persisted state/history, benchmark execution/reporting and goal-mode planning.
- Plausible first-party paths checked: reviewer-driven revision, rescue escalation, benchmark result generation, tier selection, model/provider configuration and goal decomposition.
- Why no material first-party path remains: all operating paths either regulate present work or execute developer-supplied configuration. No reviewed first-party actor autonomously senses external/future-relevant distinctions, develops adaptation options and returns a selected option into persistent current capability for subsequent runs.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy authority is established for the assessed harness.
- Disturbance / variety regulated: security checklist, hard rules, tier profiles, model-role configuration, verification allowlists and optional human gates constrain current execution, but their existence/enforcement does not establish a decision process that can revise redteam's identity or ultimate policy at runtime.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established at the assessed operating boundary.
- Supporting / enforcement mechanisms: project config, security checklist, hard rules, tier/gate definitions, verification allowlist, manual fallback, human rescue/ask-user paths and the final human-controlled merge outside the autonomous draft-PR producer.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: agents operate inside human/developer-defined policy and task boundaries. Human approval of a plan/rescue/PR or the operator's final merge decision concerns a current contribution and does not by itself constitute an identity/ultimate-policy issue with a returned S5 closure path.
- Evidence: [`README.md`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/README.md); [`.redteam/config.toml`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/config.toml); [`.redteam/workflows/orchestrator.py`](https://github.com/AscendyProject/redteam/blob/c2bedf14aca43cc03330503f35e60e12b72f37ee/.redteam/workflows/orchestrator.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: repository maintainers ultimately define the shipped harness and users control merge/configuration, but ordinary OSS maintenance and per-task approval are outside the required runtime identity/ultimate-policy closure unless a first-party path explicitly turns such issues into governing decisions for subsequent operation.

### Absence scope

- Surfaces inspected: model/project configuration, hard rules, security checklist, tier/gate resolution, human ask/rescue/PR checkpoints, README operating contract and repository-level benchmark/development material.
- Plausible first-party paths checked: operator configuration edits, tier selection, human plan/rescue/PR gates, final merge control, provider fallback and project policy/checklist enforcement.
- Why no material first-party path remains: these surfaces configure or approve ordinary operation. No reviewed standard path identifies an identity/ultimate-policy issue, routes it to a legitimate ultimate authority as S5, receives an authoritative identity/policy decision and returns that decision to govern subsequent harness operation.

## Distributed OSS parent arrangement

redteam is public OSS and the assessed product is self-hosted into target repositories. Repository maintainers and target-project humans retain real authority over code, configuration and merge. The review did not find a first-party organization-level parent loop that converts those human authorities into S3/S4/S5 publication states at the assessed harness recursion. Human intervention therefore remains function-specific environmental/operator control rather than an inferred `(P)` state.

## Self-hosted and non-human modes

The self-hosted distribution supports optional human gates and manual reviewer fallback. These modes materially alter who performs a specific review or current task decision, but they do not create a qualifying parent-mode S3/S4/S5 closure. The default headless agent-pair mode independently supports the published S3* `A` state; Methodology `0.3.x` does not publish a parent modifier for S3*.

## Recursion

Goal mode can decompose one human goal into several task branches and single-parent dependencies. Each task can run its own planning/implementation/review lifecycle, but the reviewed evidence does not show each task cell carrying the full metasystemic repertoire required to claim recursive viability. Nested tasks/dependencies are therefore treated as operational decomposition, not proof of recursive viable systems.

## Variety and escalation

redteam attenuates operational variety with plan/scope constraints, pinned verification commands, branch/diff integrity floors, retry ceilings and dependency ordering. It amplifies regulatory variety through a deliberately different reviewer perspective, carried review findings, staged/fallback reviewers and rescue/human escalation.

Exceptional review outcomes can route `RESCUE_REQUIRED` directly to rescue, repeated blockers can enter rescue after bounded carry-over/retries, and `ASK_USER` can reach a human response path. These are meaningful escalation/algedonic-style channels for exceptional current-work problems, but the signal path is not an extra VSM function: the positive function credited here is the complementary S3* audit judgment and its correction closure.

## Evidence gaps

- The repository contains a Phase-1 benchmark runner/reporting surface, but no committed real benchmark result set was found at the reviewed revision. This assessment therefore makes no quantitative capability claim from benchmark implementation alone.
- The assessment does not infer S2 from goal dependencies or S3 from deterministic scheduling/retry machinery; a future upstream release could add stronger agent-owned coordination/current-control paths and would require a new-ref reassessment.
- The default S3* result is grounded in source-level reachability and decision rights, not in the later non-normative capability benchmark layer. A future public redteam benchmark sweep could provide capability evidence without changing this ownership classification.
