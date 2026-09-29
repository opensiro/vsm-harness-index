---
harness_id: metaharness
project_name: MetaHarness
repository: https://github.com/ruvnet/metaharness
review_ref: d5833dc6512ac1adeeef91a331c29055cd8a4dbb
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: —
---

# MetaHarness

## Review boundary

- System in focus: the first-party `ruvnet/metaharness` harness-engineering distribution at frozen revision `d5833dc6512ac1adeeef91a331c29055cd8a4dbb`, including the `metaharness` scaffolder, generated-harness Darwin integration, the published `@metaharness/darwin` evolution runtime and its supported model-backed mutation / real-LLM evaluation modes, plus the published `@metaharness/avo` governed-variation control layer where it supplies first-party control or audit machinery.
- Purpose and identity: mint repo-specific AI-agent harnesses and provide a governed path for evaluating and improving harness behaviour while keeping capability, safety, budget, promotion and evidence boundaries explicit.
- Relevant environment: the target repository and its test/evaluation environment; external model/host runtimes; user/operator configuration; generated harness files; benchmark/evaluator tasks; tool/process results; cost and safety limits.
- Standard-distribution boundary: shipped npm/CLI/library packages and the default generated-harness integration are inside. External model endpoints and agent hosts remain dependencies/actors. A caller-supplied `VariationAgent`, caller-supplied evaluator/supervisor strategy factory and third-party host internals are not silently promoted into first-party owners. Repository-development Dream Cycle material, benchmark-result claims, CI/release workflows and scenario-specific experiments are adjacent unless a shipped runtime path explicitly uses the same mechanism.
- Credited operating / distribution surfaces: root `metaharness` scaffolder; generated `npm run evolve` integration; `@metaharness/darwin` `evolve` API/CLI; supported `ruvllm` model-backed mutator; supported `llm-agent` sandbox; Darwin archive/scoring/promotion selection; `@metaharness/avo` variation state, policy, evaluator-binding, quarantine/rollback, budgets and signed-receipt machinery.
- Adjacent first-party surfaces excluded from ownership: repository-development Dream Cycle / maintainer workflows; SWE-bench and other benchmark drivers except where they corroborate a shipped API contract; tests and result bundles; private/experimental ARC-specific packages; caller implementations of `VariationAgent`, `EvaluatorSuite`, `ApprovalGate`, `StrategyFactory` or external host/model logic that are only dependency-injected into AVO.
- First-party operating / deployment modes considered: scaffolding with Darwin enabled by default; Darwin deterministic evolution; opt-in local `ruvllm` model-backed mutation; opt-in `llm-agent` real-agent behavioural evaluation; graded benchmark/promotion modes; AVO governed variation when composed through its public first-party operator contract.
- Recursion level: one MetaHarness-managed generated harness/evolution organization around a target repository. A candidate harness variant executing a real agent task is an operational unit at this recursion. Darwin/AVO selection, governance, audit and adaptation regulate those candidate operations. External Claude/RuvLLM/model-provider internals and the target repository's own organization remain environmental dependencies.
- Reviewed revision: `d5833dc6512ac1adeeef91a331c29055cd8a4dbb`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

MetaHarness describes itself as a factory for agent frameworks rather than another monolithic agent framework. The scaffolder creates repo-specific harnesses for external agent hosts and, by default, deep-integrates the published Darwin package so generated harnesses expose `npm run evolve`. The ordinary generated script uses deterministic mutation, but the same shipped Darwin CLI/library supports a local model-backed `ruvllm` mutator and a real-LLM `llm-agent` evaluation substrate.

Darwin separates proposal from measurement and selection. A model-backed mutator receives the current harness surface, repository summary, parent score and recent failed traces and proposes a replacement while a fixed safety validator constrains new capabilities. Candidate variants are then executed/evaluated, scored and archived. Graded modes can apply statistical promotion gates; promoted children become parents for later generations, while stalled generations select from the archive or configured diversity/quality strategies. The CLI writes a `.metaharness` work tree and reports the winner/lineage rather than silently replacing arbitrary source files outside the evolution workspace.

AVO adds a separate governed control contract. A `VariationAgent` chooses actions, but that actor is dependency-injected by the caller and is therefore not used to establish first-party autonomous ownership by itself. The first-party operator owns immutable capability checks, budgets, protected paths/invariants, policy decisions, evaluation binding, quarantine/rollback, lineage/checkpoints and signed receipts. A separately supplied evaluator observes candidate state through an operator-bound branch/workspace snapshot; agent-returned state is cloned/frozen and cannot authoritatively rewrite the evaluation binding. These are strong constructor-control and complementary-audit paths even when the semantic variation agent is external.

Primary evidence:

- [`README.md`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/README.md)
- [`docs/adrs/ADR-147-metaharness-darwin-deep-integration.md`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/docs/adrs/ADR-147-metaharness-darwin-deep-integration.md)
- [`packages/darwin-mode/src/cli.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/cli.ts)
- [`packages/darwin-mode/src/evolve.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/evolve.ts)
- [`packages/darwin-mode/src/ruvllm-mutator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/ruvllm-mutator.ts)
- [`packages/darwin-mode/src/openrouter-mutator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/openrouter-mutator.ts)
- [`packages/darwin-mode/src/llm-agent-sandbox.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/llm-agent-sandbox.ts)
- [`packages/avo/README.md`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/README.md)
- [`packages/avo/src/operator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/operator.ts)
- [`packages/avo/src/ports.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/ports.ts)
- [`packages/avo/src/types.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/types.ts)
- [`packages/avo/src/supervisor.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/supervisor.ts)

## Operational model

A generated harness can run its normal host-facing work and invoke the integrated Darwin evolution surface. In model-backed Darwin mode, a first-party mutator asks a configured model to revise one bounded harness surface from the parent artifact, repository summary, parent score and failed traces. Candidate variants are safety-checked, executed against a configured substrate, scored and either promoted or retained only as archive material. A supported real-LLM substrate launches a restricted one-turn agent under the candidate's own policy guidance and records whether the resulting behaviour satisfies the task. Promotion changes the parent population used by subsequent generations, so accepted evidence changes later operating capability inside the evolution run.

AVO can replace the one-call variation proposal path with a longer inspect/edit/execute/evaluate/repair loop, but the semantic `VariationAgent` and evaluator implementations are injection points. This assessment therefore credits first-party autonomous ownership only where MetaHarness itself supplies the model-driven decision path (Darwin model-backed mutation / real-agent execution) and records AVO's policy/evaluation machinery as constructor-owned where the decisive semantic actor remains caller supplied.

## S1 — Operations

- State: A
- Function: execute a candidate harness as an agentic work unit and/or produce a concrete harness-engineering change through a first-party model/context/action loop, returning observable task or repository outcomes to the evolution organization.
- Disturbance / variety regulated: changing task prompts, candidate policy guidance, repository/harness state, model responses, failed traces, test/tool outcomes and bounded safety/cost conditions.
- Decisive decision or feedback right: in supported model-backed modes, choose the substantive agent response under a candidate harness policy or choose the concrete bounded harness-surface revision after observing parent code and failure evidence.
- Decision owner: the model actor invoked through first-party Darwin runtime paths: the restricted real agent in `llm-agent` evaluation and the configured local model behind `RuvllmMutator` for harness-surface generation.
- Supporting / enforcement mechanisms: candidate variant materialization; safety inspection; restricted CLI invocation; timeout/spend caps; mutation-surface allowlist; sandbox execution; run traces; archive and score storage.
- Closure path: task/current candidate or parent evidence enters Darwin → first-party runtime constructs model context/guidance → model selects substantive response or revised surface → runtime executes/materializes it → task/test/trace feedback is recorded → later operation can continue from the resulting candidate/evidence.
- Boundary reachability: both `--mutator ruvllm` and `--sandbox llm-agent` are supported shipped Darwin CLI modes at the frozen revision; the scaffolder deep-integrates the same published Darwin runtime into generated harnesses.
- Why this is / is not agent-owned: removing the model actor while leaving sandbox, archive, safety and selection code intact removes the substantive choice of response/revision in these supported modes; the remaining machinery can validate and rank candidates but cannot make materially equivalent open-ended decisions.
- Evidence: [`cli.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/cli.ts); [`ruvllm-mutator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/ruvllm-mutator.ts); [`llm-agent-sandbox.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/llm-agent-sandbox.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the default generated `npm run evolve` uses deterministic mutation, so `A` is a supported opt-in first-party mode rather than the default mutation owner. A caller-supplied AVO `VariationAgent` is not used as additional first-party autonomy evidence.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation was established among distinct credited S1 units at the assessed recursion.
- Disturbance / variety regulated: candidate variants can run concurrently and share archive-level selection context, but no concrete cross-S1 oscillation/interference plus a function-specific mutual-adjustment relation was established for credited operational units.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: bounded concurrency, separate variant directories/branches, archive single-writer steps, branching, queues/budgets and sandbox isolation.
- Closure path: no S2-specific closure established.
- Why this is / is not agent-owned: concurrency and branch isolation prevent implementation races but do not by themselves establish a coordination function regulating a specific disturbance between autonomous operational units.
- Evidence: [`evolve.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/evolve.ts); [`operator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/operator.ts).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: this does not deny that generated downstream multi-agent harnesses may add S2; those generated organizations require their own boundary/evidence.

### Absence scope

- Surfaces inspected: Darwin generation/concurrency/selection, archive commit path, sandbox isolation, AVO branching/checkpoints, shared budgets and supervisor contracts.
- Plausible first-party paths checked: parallel variants as S1 units, archive serialization as conflict attenuation, branch isolation, shared risk budget, candidate selection and supervisor redirection.
- Why no material first-party path remains: the reviewed mechanisms isolate, sequence or select experimentation; none demonstrates a specific inter-S1 interference/oscillation that is fed back as a coordination adjustment between credited autonomous operational units.

## S3 — Inside-and-now control

- State: C
- Function: regulate the current variation/evolution organization by enforcing capability boundaries, budgets, candidate admission/promotion, quarantine/rollback and which current candidates remain eligible for further work.
- Disturbance / variety regulated: unsafe capability expansion, protected-path edits, stale evaluations, budget/risk exhaustion, failing candidates, non-improving candidates, contaminated branch state and invalid promotion evidence.
- Decisive decision or feedback right: decide whether current candidate work may proceed, be denied/quarantined, be committed/promoted, be rolled back or cease consuming the run's remaining resources.
- Decision owner: constructor-defined MetaHarness runtime policy and promotion logic in the credited mode; semantic variation proposals may be agentic, but current-control admission/commitment decisions are mechanically owned by first-party code.
- Supporting / enforcement mechanisms: `VariationState`; immutable capabilities/protected invariants; policy verdicts; approval hooks; fresh evaluation binding; budget/risk counters; promotion delta/statistical gates; archive candidate state; quarantine/rollback/checkpoints.
- Closure path: current candidate/action/evaluation enters the operator or Darwin controller → first-party control logic checks whole-run state and constraints → candidate/action is allowed, denied, quarantined, promoted, rolled back or stopped → subsequent generation/current operation proceeds under that changed commitment.
- Boundary reachability: these controls are on the public AVO operator and Darwin evolution paths rather than repository-development CI only.
- Whole-system current view: AVO `VariationState` carries current candidate/branch, receipts, evaluations, candidates, interventions, budget and pending approvals; Darwin holds the current parent population, archive scores, traces and shared risk/cost state.
- Current-control decision scope: the controller changes active commitments and future eligibility of candidate work, not merely logging status or routing a caller-supplied command.
- Why this is / is not agent-owned: the decisive current-control gates are fixed runtime rules even when an injected/model-driven actor proposes the underlying variation; removing that actor leaves materially the same admission, budget, quarantine and promotion decisions for a supplied action/candidate, so ownership is constructor-level `C`.
- Evidence: [`packages/avo/README.md`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/README.md); [`operator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/operator.ts); [`types.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/types.ts); [`evolve.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/evolve.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `SemanticSupervisor` can call a supplied `StrategyFactory`, but that injected strategy owner is not treated as first-party autonomous S3. Ordinary action approval is also not promoted to S5.

## S3* — Complementary audit

- State: C
- Function: independently challenge a candidate/mutation's improvement and safety claims using execution/evaluator evidence bound to the actual candidate state before promotion/commit.
- Disturbance / variety regulated: a proposed harness edit can be syntactically plausible yet fail tests, regress behaviour, violate safety constraints, be evaluated against stale branch state or present misleading model-authored summaries.
- Decisive decision or feedback right: determine from separately executed/observed candidate evidence whether the artifact satisfies the evaluation/safety conditions relied on by current control.
- Decision owner: constructor-defined MetaHarness evaluator/scorer/safety and evaluation-binding logic; the audit verdict used for promotion is not authored by the mutation model.
- Supporting / enforcement mechanisms: candidate sandbox execution; safety inspection; test/run traces; score cards; protected/hidden or configured benchmark results; operator-authored `EvaluationBinding`; immutable/frozen agent return snapshots; signed receipts and archive evidence.
- Closure path: mutator/variation agent proposes candidate → separate first-party runtime executes or binds evaluator observation to exact branch/workspace state → score/safety/evaluation result challenges the proposal → S3 promotion/quarantine/rollback logic consumes the finding → later candidate commitments change.
- Boundary reachability: Darwin evaluation/scoring/safety is part of the shipped evolution runtime; AVO evaluation binding and signed evidence are part of the public governed-variation operator.
- Claim being audited: that a candidate is safe, valid, attributable to the evaluated workspace and measurably suitable for promotion rather than merely a plausible mutation.
- Ordinary reporting path: mutation generator/variation agent returns replacement code, action choices, summaries and candidate state.
- Complementary access path: sandbox/test execution and evaluator observations inspect the candidate artifact/environment directly; AVO overwrites caller-supplied evaluation binding with the operator's actual branch/workspace/state snapshot.
- Independence boundary: the mutation actor does not control safety inspection or authoritative evaluation binding/promotion score; stale or invalidating post-evaluation actions prevent commit. This is functional independence from the audited proposal, not a claim of an external trust domain.
- Who acts on findings: the first-party Darwin/AVO current-control path changes promotion, quarantine, rollback or parent selection from the audit result.
- Why this is / is not agent-owned: the audit judgment credited here is deterministic/runtime-owned even when the proposed mutation is model-driven; therefore `C`, not `A`.
- Evidence: [`evolve.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/evolve.ts); [`llm-agent-sandbox.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/llm-agent-sandbox.ts); [`operator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/operator.ts); [`ports.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/ports.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: generic repository tests alone would not establish S3*. Credit depends on the separate proposal-versus-observation boundary, exact candidate binding and findings feeding promotion/current control.

## S4 — Intelligence / adaptation

- State: A
- Function: use observed task/evaluation failures and changing performance evidence to generate bounded prospective harness adaptations and feed selected improvements into later generations of current capability.
- Disturbance / variety regulated: current harness guidance/configuration can underperform on repository/task behaviour, repeat failure signatures, plateau or incur poor quality/cost tradeoffs as the target environment changes.
- Decisive decision or feedback right: in the supported model-backed mode, choose the concrete bounded mutation of a harness surface in response to parent score, repository context and failed traces so later variants operate under a different capability/policy.
- Decision owner: the model invoked by first-party `RuvllmMutator` (and equivalent library `OpenRouterMutator` mode) for semantic mutation choice; deterministic Darwin machinery validates and selects but does not reproduce the same open-ended edit choice.
- Supporting / enforcement mechanisms: parent score and failed-trace summaries; repository profiling; mutation-surface allowlist; generated-code safety gate; sandbox/evaluator; archive; promotion gates; lineage; next-generation parent selection; optional curriculum/diversity/pareto selection.
- Closure path: candidate performs current work → execution/evaluation produces score/failure distinctions → model-backed mutator receives those distinctions and proposes a future-oriented surface revision → runtime validates/evaluates the child → accepted/promoted child becomes a parent for subsequent generations → later operation uses the changed harness capability and is measured again.
- Boundary reachability: `--mutator ruvllm` is a shipped Darwin CLI mode, model-backed generator APIs are published library surfaces, and the scaffolder integrates Darwin into generated harnesses by default. No repository-development Dream Cycle actor is required for this path.
- External distinction: evaluation/test/real-agent outcomes come from the target repository/task environment and can distinguish success, failure, regression, cost and safety independently of the mutator's proposal.
- Future / prospective distinction: mutation is chosen to improve subsequent candidate generations from current failures rather than merely retrying the same current action.
- Adaptation option generated: bounded revisions of harness surfaces such as reviewer/planner/routing/context/repair guidance, constrained to preserve exported contracts/capabilities.
- Path back into current capability / S3: validated promoted children enter the subsequent parent population and therefore determine later candidate operation; S3 promotion/budget/quarantine gates mediate that return path.
- Why this is / is not agent-owned: with the model mutator removed, Darwin can still deterministically enumerate/tune variants, but it cannot make materially the same semantic code/policy revision from repository context and failed traces in the supported model-backed mode.
- Evidence: [`README.md`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/README.md); [`ADR-147`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/docs/adrs/ADR-147-metaharness-darwin-deep-integration.md); [`evolve.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/evolve.ts); [`ruvllm-mutator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/ruvllm-mutator.ts); [`openrouter-mutator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/darwin-mode/src/openrouter-mutator.ts).
- Basis: explicit + structural.
- Confidence: high for the supported model-backed Darwin mode; medium for treating a final reported winner as production deployment outside the evolution workspace, which is not required for the credited within-run closure.
- Caveats: default scaffolded evolution uses deterministic mutation and the CLI writes evolution artifacts/lineage rather than silently replacing arbitrary production source. `A` therefore describes a supported first-party model-backed adaptation mode, not an assertion that every default run autonomously rewrites deployed production.

## S5 — Identity / ultimate policy

- State: —
- Function: no runtime identity/ultimate-policy decision loop with legitimate authority and returned closure was established at the assessed recursion.
- Disturbance / variety regulated: MetaHarness exposes governance policies, protected invariants, capability envelopes and approval hooks, but those surfaces primarily constrain operational actions rather than adjudicate unresolved identity/ultimate-policy questions.
- Decisive decision or feedback right: an S5 witness would need a supported path for an unresolved identity/ultimate-policy issue to reach legitimate parent authority and for the resulting policy decision to return into later operation; that path was not established.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: immutable capabilities, protected paths/invariants, default-deny policy, action-level `require-approval`, generated governance configuration, signed receipts and release/evidence gates.
- Closure path: no S5-specific escalation-and-return path established. Ordinary action approval returns permission for an action but does not by itself decide system identity or ultimate policy.
- Why this is / is not agent-owned: static governance constraints and action approval are strong enforcement/support mechanisms, but Profile 0.2.4 explicitly does not equate them with S5 authority.
- Evidence: [`packages/avo/README.md`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/README.md); [`operator.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/operator.ts); [`ports.ts`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/packages/avo/src/ports.ts); [`README.md`](https://github.com/ruvnet/metaharness/blob/d5833dc6512ac1adeeef91a331c29055cd8a4dbb/README.md).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: operators can configure governance and generated harness identity out of band; this assessment does not convert configuration ownership into S5 without a supported identity/ultimate-policy closure path.

### Absence scope

- Surfaces inspected: generated governance policy, AVO capability policy/invariants, approval gate, supervisor contract, signed-receipt/evidence boundaries, Darwin safety constraints and scaffold customization guidance.
- Plausible first-party paths checked: action `require-approval`; protected capabilities; security-policy non-evolvability; operator customization of generated governance; release claim gates; supervisor interventions.
- Why no material first-party path remains: each reviewed path enforces or configures lower-level behaviour, admission or release evidence. None shows an unresolved identity/ultimate-policy matter being classified/escalated to a legitimate ultimate authority and the returned ruling closing subsequent operation at this recursion.
