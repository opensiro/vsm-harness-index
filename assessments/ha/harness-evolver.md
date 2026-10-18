---
harness_id: harness-evolver
project_name: Harness Evolver
repository: https://github.com/raphaelchristi/harness-evolver
review_ref: 87fa7612358acccb01d34abf72426a7e47329642
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-21
last_checked_ref: 87fa7612358acccb01d34abf72426a7e47329642
last_checked_at: 2026-09-21
last_reassessment_round: R3
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Harness Evolver

## Review boundary

- System in focus: Harness Evolver's first-party evolution organization at pinned revision `87fa7612358acccb01d34abf72426a7e47329642`: the shipped `/harness:evolve` loop, supplied proposer/evaluator/Critic/Architect/Consolidator roles, selection/gating machinery, archive/state, and first-party mutation/evaluation tools.
- Purpose and identity: autonomously improve an external target agent harness by analyzing evidence, proposing code changes, evaluating candidates, selecting accepted changes, learning across iterations, and repeating.
- Relevant environment: the target harness/codebase, evaluation dataset and LangSmith experiment surface, external model/provider and coding-agent host, Git worktrees, and human-supplied objective/configuration.
- Standard-distribution boundary: repository-shipped skills, agent-role prompts, Python tools, evolution state, and their documented composition. The target harness being evolved, generated candidate harnesses, external Claude Code/Codex-style execution hosts, model providers, LangSmith service, and user-supplied objectives/datasets remain environment or adjacent systems rather than inherited organizational owners.
- Credited operating / distribution surfaces: `skills/evolve/SKILL.md`, `agents/harness-proposer.md`, `agents/harness-critic.md`, `agents/harness-evaluator.md`, `tools/add_evaluator.py`, `tools/run_eval.py`, selection/gating tools, archive/history tools, and documented runtime composition in `docs/ARCHITECTURE.md` / `CLAUDE.md`.
- Adjacent first-party surfaces excluded from ownership: repository-development plans/specs, CI/release/dev-validation skills, playground examples, and the organizational properties of target/generated harnesses. These may corroborate implementation intent but do not supply missing closure to the assessed evolution organization.
- First-party operating / deployment modes considered: plugin/skill-driven evolution with model-driven proposer agents, code/LLM evaluation, candidate selection/merge, post-iteration learning, and conditionally triggered Critic/Architect roles.
- Recursion level: one harness-evolution organization. Target/generated harnesses are separate systems-in-focus and are not credited back as lower viable recursions merely because Harness Evolver mutates them.
- Reviewed revision: `87fa7612358acccb01d34abf72426a7e47329642`.
- Observation date: 2026-09-18.
- Generated Profile version: 0.2.2.
- Generated Methodology version: 0.3.1.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

The shipped evolution loop performs preflight/baseline work, gathers traces/results, synthesizes strategy and investigation lenses, launches autonomous proposer agents in isolated worktrees, evaluates candidates, compares/gates them, merges an accepted winner, archives candidates, records regressions/memory, and decides whether to continue. Proposers are model-driven actors that investigate evidence, form their own hypothesis, choose what to change, implement it, or abstain.

A separate Critic is explicitly an anti-gaming auditor/fixer. It receives complementary access to best-run outputs, evaluator behavior and score history; it judges whether high scores reflect substance or evaluator blind spots; and on detected gaming it invokes `add_evaluator.py` to add stricter evaluator names/definitions to `.evolver.json`.

The same-ref correction concerns the final audit-return edge. At this revision, `add_evaluator.py` can persist arbitrary code-evaluator definitions under `code_evaluators`, but `run_eval.py::load_evaluators()` does not read or execute those stored definitions. It always adds `has_output`, has explicit handling for `token_efficiency`, treats `latency` as trace-only, and otherwise does not construct arbitrary configured code checks. The separate `harness-evaluator` role handles only the LLM-as-judge `correctness` and `conciseness` path. Thus the repository supplies a concrete S3*-specific construction path, but not the complete autonomous corrective closure previously claimed.

## Operational model

The primary transformation at this boundary is evolution of an external target harness. Proposer/evaluator activity, selection, accepted target-code mutation, archive/history, and iteration control are stages of that operation. Parallel proposer worktrees isolate candidate alternatives, but the pinned distribution does not establish a separate disturbance-specific S2 mutual-adjustment loop among proposer S1 units.

Complementary audit is distinct from ordinary scoring: the Critic challenges whether the evaluation regime itself is being gamed. Its audit judgment and evaluator-construction path are first-party. What remains unclosed is execution of the newly stored arbitrary evaluator definitions in subsequent evaluation/selection.

## Primary evidence

- [`skills/evolve/SKILL.md`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/skills/evolve/SKILL.md) — end-to-end evolution loop, candidate evaluation/selection, proposer waves, post-iteration handling, and Critic trigger.
- [`agents/harness-proposer.md`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/agents/harness-proposer.md) — model-driven proposer discretion, isolated code mutation, self-abstention and committed candidate changes.
- [`agents/harness-critic.md`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/agents/harness-critic.md) — independent anti-gaming inspection, evaluator-blind-spot judgment and required corrective evaluator construction.
- [`tools/add_evaluator.py`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/tools/add_evaluator.py) — first-party mutation of configured evaluator names and `code_evaluators` definitions.
- [`tools/run_eval.py`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/tools/run_eval.py) — actual code-evaluator construction/execution path; does not consume arbitrary stored `code_evaluators` definitions.
- [`agents/harness-evaluator.md`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/agents/harness-evaluator.md) — separate LLM-as-judge path limited to `correctness` / `conciseness`.
- [`docs/ARCHITECTURE.md`](https://github.com/raphaelchristi/harness-evolver/blob/87fa7612358acccb01d34abf72426a7e47329642/docs/ARCHITECTURE.md) — role topology, evolution loop, gates and documented auto-trigger surfaces.

## S1 — Operations

- State: A
- Function: execute the harness-evolution transformation by diagnosing target failures, generating and implementing candidate changes, evaluating/selecting candidates, installing accepted target changes, and iterating.
- Disturbance / variety regulated: target-harness design uncertainty, benchmark failures, trace-derived failure modes, alternative implementation hypotheses, and candidate performance variation.
- Decisive decision or feedback right: choose a substantive diagnosis/change strategy for the target harness and produce a candidate implementation or abstain; the enclosing evolution loop then selects and installs an accepted candidate.
- Decision owner: model-driven proposer/evolution actors operating under the shipped first-party role and evolve-loop contract.
- Supporting / enforcement mechanisms: isolated Git worktrees, LangSmith-backed evaluation, constraint/efficiency gates, selection tools, archive/history, regression tracking and merge machinery.
- Closure path: evidence from the current target state → proposer diagnosis and candidate mutation → candidate evaluation/selection → accepted candidate merged into the target harness → changed target becomes the baseline/context for later evolution iterations.
- Boundary reachability: the standard `/harness:evolve` procedure directly instantiates the shipped proposer role and first-party tools; no downstream organizational component is required to expose proposer discretion or the candidate-selection/merge path.
- Why this is / is not agent-owned: deterministic tools isolate, evaluate, gate and merge candidates, but the substantive hypothesis and code-change choice is made by the model-driven proposer. The target harness being changed is environment; its internal organization is not imported into Harness Evolver's own vector.
- Evidence: `skills/evolve/SKILL.md`; `agents/harness-proposer.md`; `docs/ARCHITECTURE.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model/coding-agent hosts execute the supplied role contract, and generated candidate harnesses remain separate systems-in-focus.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes regulation of a concrete interference, conflict or oscillation among distinct operational S1 units at this recursion.
- Disturbance / variety regulated: not established as S2.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: parallel proposer waves, isolated worktrees, staged execution, shared strategy/archive context and later candidate comparison reduce collision in the search process but do not establish a peer mutual-adjustment function by themselves.
- Closure path: not applicable as S2.
- Why this is / is not agent-owned: worktree isolation prevents candidate-state collision and wave ordering structures search; the evidence does not show an S2-specific actor observing destructive inter-S1 interference/oscillation and feeding a coordination response back into subsequent peer behavior.
- Evidence: `skills/evolve/SKILL.md`; `docs/ARCHITECTURE.md`.
- Basis: structural absence review.
- Confidence: high.
- Caveats: a downstream orchestration of proposer agents could add an S2 loop, but generic parallelism and isolation are insufficient at the reviewed boundary.

### Absence scope

- Surfaces inspected: proposer wave protocol, worktree isolation/copy behavior, shared strategy/lenses/archive, candidate evaluation and staged selection.
- Plausible first-party paths checked: parallel proposer isolation as S2; wave-2 visibility of wave-1 outputs as S2; shared archive/state as S2; candidate comparison as S2.
- Why no material first-party path remains: these mechanisms organize search and prevent shared-state collision, but do not reconstruct a concrete inter-S1 conflict/oscillation plus an S2-specific feedback relation changing later peer operation.

## S3 — Inside-and-now control

- State: —
- Function: no distinct first-party whole-organization current-control function is established over a portfolio of operational S1 commitments.
- Disturbance / variety regulated: not established as S3 at this recursion.
- Decisive decision or feedback right: not established for whole-current-system regulation.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: candidate selection, constraint/efficiency gates, iteration stop criteria, retry/cleanup and Architect triggers regulate the primary evolution process but do not by themselves create a distinct whole-organization current-control owner.
- Closure path: not applicable as S3.
- Why this is / is not agent-owned: the selection/gating machinery governs which candidate advances inside the S1 evolution transformation. The reviewed evidence does not establish a separate actor with a whole-current view plus discretionary authority over shared resources, commitments, priorities or multiple operational units on behalf of the organization as a whole.
- Evidence: `skills/evolve/SKILL.md`; `docs/ARCHITECTURE.md`.
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: role names such as Architect/Consolidator and deterministic gates are not promoted to S3 without the required function.

### Absence scope

- Surfaces inspected: selection/gating, iteration gate, Architect trigger, Consolidator, worktree lifecycle, archive/history and retry/cleanup paths.
- Plausible first-party paths checked: selection as S3; stop/continue gate as S3; Architect as S3; Consolidator as S3; worktree cleanup/retry as S3.
- Why no material first-party path remains: these paths regulate stages of the evolution operation or maintain its state, but no distinct whole-system current regulatory loop across operational commitments is established.

## S3* — Complementary audit

- State: C
- Function: independently challenge whether ordinary evaluator/benchmark scores correspond to substantive target-harness quality rather than evaluator gaming, blind spots or score inflation.
- Disturbance / variety regulated: high-scoring but substantively wrong outputs, hallucination/format gaming, evaluator blind spots, suspicious score jumps and inflation that can mislead ordinary candidate selection.
- Decisive decision or feedback right: judge whether the ordinary evaluation regime is being gamed or misses a material quality dimension and choose a stricter evaluator/check intended to close that blind spot.
- Decision owner: the autonomous Critic owns the complementary audit judgment and chooses the corrective evaluator within the supplied audit role; the final executable return from arbitrary stored evaluator definition to later scoring remains uncomposed in the pinned runtime.
- Supporting / enforcement mechanisms: Critic trigger conditions, direct access to best-run outputs/evaluator behavior/score history, `add_evaluator.py`, `.evolver.json` evaluator storage, `critic_report.md`, and config validation.
- Closure path: Critic finding → Critic invokes `add_evaluator.py` → evaluator name/definition is persisted in `.evolver.json`. The first-party path stops short of demonstrated operational closure for arbitrary Critic-added code evaluators: `run_eval.py::load_evaluators()` does not load `config["code_evaluators"]`, while `harness-evaluator` handles only `correctness`/`conciseness`. A developer/composer must wire the stored evaluator definition into executable later evaluation/selection feedback.
- Boundary reachability: the Critic role, Critic trigger and `add_evaluator.py` are shipped and reachable from the standard evolve procedure, so the S3*-specific construction path is first-party. The missing evaluator-execution edge is not borrowed from an adjacent project or hypothetical downstream integration.
- Why this is / is not agent-owned: the audit judgment itself is agent-owned and sufficiently separated from ordinary proposer/evaluator production. However, Methodology `A` requires the decisive audit/feedback loop to be operationally closed; persisting a corrective evaluator definition that the shipped evaluator path does not execute is insufficient. The function-specific first-party path therefore satisfies `C`, not `A`.
- Evidence: `agents/harness-critic.md`; `tools/add_evaluator.py`; `tools/run_eval.py`; `agents/harness-evaluator.md`; `skills/evolve/SKILL.md`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the correction does not claim the Critic lacks independence or discretion. It narrows only the previously overstated corrective closure. A later upstream revision that actually executes Critic-added evaluator definitions can be reassessed separately.
- Claim being audited: that high evaluator/benchmark scores represent substantive target-harness quality rather than exploitation of the current scoring regime.
- Ordinary reporting path: candidate runs are scored by the normal configured evaluation path and those scores feed candidate comparison/selection.
- Complementary access path: the separate Critic inspects best-run outputs, evaluator behavior and cross-iteration score history specifically to challenge the ordinary score path and diagnose blind spots/gaming.
- Independence boundary: the Critic is a separately supplied role from proposer and ordinary evaluator, is not tasked to optimize a candidate directly, and receives evidence specifically for adversarial audit of the evaluation regime.
- Who acts on findings: the Critic itself writes the corrective evaluator configuration. At the pinned revision no first-party later runtime actor is demonstrated to execute arbitrary stored `code_evaluators` definitions into subsequent scores, so the final corrective return still requires composition.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then intelligence loop is established for Harness Evolver itself.
- Disturbance / variety regulated: not established as S4 at the assessed recursion.
- Decisive decision or feedback right: not established for external/future adaptation of the Harness Evolver organization.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: trace analysis, benchmark-driven improvement, strategy/lens synthesis, archive mining, regression history, Architect/Consolidator roles and evolution memory improve the current target-search operation but remain internally oriented to that operation/distribution.
- Closure path: not applicable as S4.
- Why this is / is not agent-owned: learning and self-improvement around the target benchmark are not promoted to S4 without a loop that senses external/future distinctions for the Harness Evolver organization and returns adaptation options into its present capability.
- Evidence: `skills/evolve/SKILL.md`; `docs/ARCHITECTURE.md`; proposer/archive/memory paths.
- Basis: structural absence review.
- Confidence: high.
- Caveats: the evolved target may gain future-facing capability, but target-harness adaptation is not imported as S4 of Harness Evolver.

### Absence scope

- Surfaces inspected: trace/results analysis, strategy/lens synthesis, evolution archive, regression tracking, evolution memory, Architect and Consolidator roles, target mutation.
- Plausible first-party paths checked: benchmark learning as S4; archive/memory as S4; Architect as S4; target-harness self-improvement as S4.
- Why no material first-party path remains: inspected paths optimize or remember the current target-evolution task; they do not establish an external-and-prospective intelligence loop that changes Harness Evolver's own organizational capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is supplied for the Harness Evolver organization.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: not established for ultimate organizational identity/policy.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: user-supplied objective, evaluator configuration, constraints, target score, iteration count and stop criteria bound the evolution search but do not form a first-party identity-policy loop.
- Closure path: not applicable as S5.
- Why this is / is not agent-owned: accepting configuration or enforcing goals does not establish runtime authority to define/revise the organization's ultimate purpose or constitutional policy.
- Evidence: `skills/evolve/SKILL.md`; setup/configuration and gate paths.
- Basis: structural absence review.
- Confidence: high.
- Caveats: human/operator authorship of the objective is environment/configuration, not automatically a published parent-governed S5 mode.

### Absence scope

- Surfaces inspected: objective/configuration, evaluator settings, constraints, target score, iteration/gate logic, deployment/setup material and agent-role prompts.
- Plausible first-party paths checked: user objective as S5; fixed constraints as S5; gate/stop criteria as S5; role prompts as S5.
- Why no material first-party path remains: these are supplied operating constraints or instructions; no runtime identity/ultimate-policy issue reaches a legitimate authority and returns as a governing organizational-policy decision.

## Recursion

The target harness and generated candidates may contain or become viable organizations, but they are separate systems-in-focus. Harness Evolver changing another harness does not by itself create a viable lower recursion inside Harness Evolver, and no recursive organization is credited from code mutation alone.

## Variety and escalation

Parallel proposers amplify design variety; evidence gathering, evaluation, constraint/efficiency gates and selection attenuate it. The Critic supplies complementary challenge when the ordinary scoring regime itself becomes suspect. At the pinned revision its audit judgment can alter configuration, but arbitrary corrective code-evaluator definitions are not yet shown to close into later executable scoring.

## Evidence gaps

The assessment does not infer execution semantics from external Claude Code/Codex-style hosts beyond responsibilities explicitly required by the first-party role/skill contracts. No execution trace in the pinned repository demonstrates an arbitrary Critic-added `code_evaluators` definition being consumed by `run_eval.py` and changing later selection. If such a runtime path exists outside the inspected standard distribution, it requires primary evidence before upgrading S3* from `C`.

## Admission conclusion

Canonical vector: `A — — C — —`.
