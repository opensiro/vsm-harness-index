---
harness_id: salazar
project_name: Salazar
repository: https://github.com/shawnpetros/salazar
review_ref: e16841146e2ef2d71aa99117334939037e9804ff
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Salazar

## Review boundary

- System in focus: Salazar's shipped TypeScript CLI/engine implementing spec-to-code workflows, model-backed planner and generator sessions, deterministic code validators, optional separate model-backed evaluator sessions, corrective retry, progress history and local database.
- Purpose and identity: compile a product specification into a working code repository through feature-by-feature autonomous generation and bounded validation/critical review.
- Relevant environment: spec/BDD features, filesystem/Git repository and Node toolchain, Claude Agent SDK/provider, npm-installed package, user-configured generator/evaluator model tiers and security hooks.
- Standard-distribution boundary: [entrypoint](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/index.ts) invokes first-party [Orchestrator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts), which calls three first-party model session adapters to plan, implement and inspect code, applies validators and returns evaluator feedback for correction. SDK internal tool dispatch and model inference are external, but first-party engine implements the actual composition, review gate and retry loop.
- Credited operating / distribution surfaces: [README CLI and shipped mode](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/README.md), [orchestrator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts), [planner](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/planner.ts), [generator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/generator.ts), [evaluator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/evaluator.ts), [model config](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/client.ts), [hard validators](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/validators.ts), [evaluator instructions](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/prompts/evaluator.md).
- Adjacent first-party surfaces excluded from ownership: Claude Agent SDK internals/provider, marketing assertions about benchmark outputs and self-building, demo GIFs, downstream output repositories, TUI rendering (unless connected to engine decisions), and tests only asserting expected behavior.
- First-party modes considered: README `salazar run <spec>`, default greenfield path in orchestrator, configurable role-model tiers, planner-on-new-run, feature continuation, generator→validator→optional evaluator and failure retry/rollback; TUI as operator view.
- Recursion: one product-building session across serial feature production tasks with an independent per-feature review attempt. Planner/generator/evaluator are sequential roles; the evaluator's separate task and evidence-gathering is relevant to S3*, not automatically to inter-S1 S2.
- Frozen revision: `e16841146e2ef2d71aa99117334939037e9804ff`, Index intake #3047, controller #3048; reviewed 2026-11-10 with Profile 0.2.4 and Skills Methodology 0.3.8. Source-static, not a live Claude SDK run.

## Repository architecture

The [Orchestrator.run](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts) detects `feature_list.json`; if absent it calls the model-backed [planner](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/planner.ts) to decompose the spec into BDD features and schema-checks the output. The [feature loop](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts) selects the next incomplete feature and calls the model-backed [generator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/generator.ts), which runs Claude SDK `query` to edit code in the output directory. After generation, independent **deterministic** typecheck/lint/build/tests run before optional model review. Failures return validator logs for additional generation attempts, with fixed limits.

For features tagged `moderate` or `complex`, Salazar launches a distinct [evaluator query](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/evaluator.ts) with its own critical-review [system instructions](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/prompts/evaluator.md). It can inspect code and tests using allowed SDK tools, reports weighted criteria and issues, and yields a gate: score at least 7.0 with no high-severity security finding. Failed findings are passed into the generator's next attempt. Thus S3* is a separate first-party audit path with a corrective return to task operations. For `setup`/`simple` features, the evaluator is explicitly skipped and only deterministic gates run; S3* claim is conditional on shipped moderate/complex mode.

Role-specific model names can differ through [makeQueryOptions](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/client.ts), but default provider and workspace remain shared. The evaluator prompt mentions browser automation, whereas the actual tool allowlist includes Read/Write/Edit/Glob/Grep/Bash, not a browser tool; that aspiration is not credited. The evaluator suggests `git diff HEAD~1`, which may not represent currently uncommitted changes; broader working-tree inspection and test tools are available, but static source does not prove accurate real-world verdicts. SQLite state and TUI events are telemetry, not themselves first-party S3/S4 policy owners.

## Operational model

- Output: one implementation artifact/repository with per-feature commits, BDD state, result events and persistent session timeline.
- S1: model-backed planner and generator sessions decide semantic feature decomposition and coding actions; loop and deterministic validators impose contractual phases and retry bounds.
- S3*: model-backed evaluator owns a separate claim challenge/reviewer verdict for selected features, reads tools and returns feedback to producer, with deterministic score/security gate and bounded retries.
- Not inferred: coordinated parallel production cells, whole-system current control, prospective environmental adaptation or ultimate mandate formation.

## S1 — Operations

- State: A
- Function: autonomous spec-driven development of code features under changing file/tool/test feedback.
- Disturbance / variety regulated: ambiguous feature requirements, partial code, compiler and test failures, tool responses and implementation defects.
- Decisive decision or feedback right: choose feature breakdown, code edits, tool use and debugging steps rather than merely execute a deterministic template.
- Decision owner: first-party invoked planner/generator model sessions, with the generator acting as the ongoing S1 work unit and planner initializing its plan; first-party orchestrator owns task sequencing and gates.
- Supporting / enforcement mechanisms: Claude SDK model/tool adapter, [role prompts](https://github.com/shawnpetros/salazar/tree/e16841146e2ef2d71aa99117334939037e9804ff/prompts), Zod schema validation, fixed retry caps, Git progress, hard test/build gates and SQLite history.
- Closure path: spec → model planner/decomposition → generator receives feature → model chooses code/tool operations → tool and validator observations → generation revision or feature pass/failure, then next incomplete feature.
- Boundary reachability: CLI and engine include the real [Orchestrator featureLoop](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts) and two [SDK query](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/generator.ts) paths rather than abstract SDK type definitions; requires configured provider and environment.
- Why this is / is not agent-owned: model decisions over nontrivial project code and iterative tools are actually invoked by first-party task machinery, while deterministic gates constrain rather than supply semantic implementation.
- Evidence: [planner](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/planner.ts), [generator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/generator.ts), [orchestrator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts).
- Basis: source-static implemented/invoked model-tool and feedback path.
- Confidence: high for structural agent ownership, without runtime-quality verification.
- Caveats: no live build conducted; coding quality, provider credentials, claimed examples and deployment success are unverified.

## S2 — Coordination

- State: —
- Function: no distinct first-party adaptive coordination layer attenuating conflicts between separately operating S1 cells.
- Disturbance / variety regulated: serial planner/generator/evaluator handoffs and feature ordering prevent overlap by fixed sequencing, rather than reconcile cross-cell clashes.
- Decisive decision or feedback right: negotiate conflicts between concurrent S1 production operations; no first-party role has a sourced inter-S1 conflict decision.
- Decision owner: fixed Orchestrator pipeline and next-incomplete feature selector; evaluator owns separate audit rather than coordination of multiple active S1s.
- Supporting / enforcement mechanisms: feature-list order, Zod contracts, role boundaries, retry limits and status persistence.
- Closure path: each stage completes before the next role runs, so no independently conflicting S1 units send cross-cell disturbance signals to a coordinating agent.
- Why this is / is not agent-owned: named planner/generator/evaluator agents and checked handoffs describe sequential production and QA, not S2-specific inter-S1 oscillation attenuation.
- Evidence: [feature loop](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts), [progress selection](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/progress.ts).
- Basis: structural.
- Confidence: high within shipped greenfield runtime.
- Caveats: distributed versions or external team orchestration could add S2 at a different boundary, not assessed here.

### Absence scope

- Surfaces inspected: planner/generator/evaluator stage schedule, feature loop, model role configs, feature state and parallel validators.
- Plausible first-party paths checked: multiple named agents and parallel typecheck/lint commands; neither shows inter-S1 adaptive conflict management.
- Why no material first-party path remains: first-party mode has ordered role handoffs, no competing active S1 cells and no sourced S2-specific feedback.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous or human-assisted whole-system current-control intervention process beyond single product-build operation.
- Disturbance / variety regulated: per-feature retry, score, cost and progress visibility are managed by hard-coded policy, not discretionary portfolio supervision.
- Decisive decision or feedback right: change whole-system resource commitments, priorities and intervention in response to multiple S1s; not established at this recursion.
- Decision owner: fixed Orchestrator, user-supplied spec/model config and each production agent's local decisions.
- Supporting / enforcement mechanisms: progress dashboard, SQLite session/cost store, retry budgets, next-incomplete feature scanner and event emitter.
- Closure path: feature/test progress → fixed next-feature/rollback/continue choice; no independently analyzed whole-current S1 portfolio decision is returned.
- Why this is / is not agent-owned: cost and progress tracking plus fixed stage gates are local operations, not an S3 supervisory decision loop; no sourced S3=P human proposal/intervention contract.
- Evidence: [orchestrator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts), [storage](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/storage.ts).
- Basis: source-static.
- Confidence: medium-high.
- Caveats: CLI/TUI operator can manually oversee the project but is not a demonstrated S3=P first-party system view.

### Absence scope

- Surfaces inspected: featureLoop, local database, cost counters, UI events, progress handling and retry/rollback rules.
- Plausible first-party paths checked: cost/performance status, feature routing and human-facing TUI.
- Why no material first-party path remains: these are measurements and deterministic actions without whole-system adaptive managerial decision closure.

## S3* — Complementary audit

- State: A
- Function: inspect a produced code feature from a deliberately distinct review session and return corrective evidence to the generator before acceptance.
- Disturbance / variety regulated: latent spec mismatches, security flaws, low code quality and usability errors that can survive the generator and deterministic validators.
- Decisive decision or feedback right: separate evaluator model inspects code/test evidence, assigns criticality/scores, and issues a challenge/recommendations; first-party gate accepts or rejects and sends feedback for generator revision.
- Decision owner: a **separate evaluator Claude SDK session** for audit judgment, with first-party deterministic acceptance enforcing 7.0 threshold and high-security-issue veto; generator does not choose its own evaluation score.
- Supporting / enforcement mechanisms: [critical evaluator prompt](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/prompts/evaluator.md), evaluator-specific model config, SDK allowed file/Bash tools, Zod output contract, weighted score and retry gate.
- Claim being audited: generated moderate/complex feature implements the spec safely and robustly enough to pass before committing.
- Ordinary reporting path: generator reports completion and passes local automated validators within its main production track, potentially including its own tests/progress assertions.
- Complementary access path: a new model-backed evaluator task receives the spec/BDD requirement and output working directory, can independently read the code and run tests through SDK tools, then creates a structured critique and score.
- Independence boundary: separate system prompt, run/task context, evidence acquisition and model role; reviewer/generator share local workspace and provider by default, and are not guaranteed cross-provider independent. Config supports a distinct evaluator model, but optional difference is not claimed as default independent infrastructure.
- Who acts on findings: [Orchestrator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts) routes failed evaluation feedback into the next [generator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/generator.ts) attempt; accepts passing verdict or rolls back after bounded retries.
- Closure path: generated feature → mandatory hard validators → **moderate/complex conditional reviewer session** → score+security issue gate → accept commit or return evaluator feedback to generator → changed implementation and next review.
- Boundary reachability: [shipped featureLoop](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts) invokes [runEvaluator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/evaluator.ts) for concrete moderate/complex features, and `makeQueryOptions` supplies its distinct [role prompt](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/client.ts); setup/simple features skip reviewer, so S3* is not universal.
- Why this is / is not agent-owned: unlike same-agent self-reflection or hard validator results, an independently instantiated model session with a skeptical purpose accesses evidence and yields a return-to-operation decision through a first-party feedback gate.
- Evidence: [runEvaluator](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/evaluator.ts), [featureLoop corrective branch](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts), [review rubric](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/prompts/evaluator.md), [model role options](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/client.ts).
- Basis: static first-party mechanism, conditional shipped mode; no actual audit quality proof.
- Confidence: high structural confidence for reviewer invocation, separate context and corrective return; lower confidence in achieved defect detection and effective tool usage.
- Caveats: shared workspace/provider, reviewer has Write/Edit permission, prompt mentions unavailable browser tool, `git diff HEAD~1` may be stale; source-only finding does not certify reviewer impartiality or benchmark accuracy.

## S4 — Outside-and-then intelligence

- State: —
- Function: no ongoing future-environment sensing and prospective capability adaptation process.
- Disturbance / variety regulated: static spec requirements and current compiler/test feedback are handled within immediate software production, not future environmental shifts.
- Decisive decision or feedback right: anticipate external opportunity/threat, generate new strategic option and feed it to present operations; not owned by Salazar engine.
- Decision owner: user supplies future product spec; planner decomposes present goal, not independent outside-and-then intelligence.
- Supporting / enforcement mechanisms: planner LLM and spec file, context tools, user model configuration and role prompts.
- Closure path: given spec → current feature list → implementation, without continuous outside scan and future-to-current policy feedback.
- Why this is / is not agent-owned: generative planning for a fixed product objective is S1 task decomposition, not VSM S4 intelligence.
- Evidence: [planner source](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/planner.ts), [engine](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/orchestrator.ts).
- Basis: source-static.
- Confidence: medium-high.
- Caveats: a strategic market-research spec might be assigned, but this would be user-selected S1 activity.

### Absence scope

- Surfaces inspected: spec planner, generator/evaluator prompts, tool access, progress handling and user config.
- Plausible first-party paths checked: LLM planning and feature priority; these solve current fixed input and do not forecast external shifts.
- Why no material first-party path remains: no continuous future-oriented intelligence input, strategic adaptation owner or adaptation-to-current feedback closure.

## S5 — Policy and identity

- State: —
- Function: no first-party policy-identity arbitration between operating and future strategies.
- Disturbance / variety regulated: fixed SDK permissions, Bash security hooks and contract score thresholds enforce local task-risk controls.
- Decisive decision or feedback right: set and reconcile mission/identity-level constraints across S3/S4 decisions; not represented in first-party engine.
- Decision owner: user/operator chooses spec/config, developer-configured SDK security and hard validators enforce, agents decide code content.
- Supporting / enforcement mechanisms: permission settings, [security hook](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/security.ts), Zod schemas and fixed evaluator rules.
- Closure path: configured local policy/gate → accept/reject tool or feature; no ultimate policy synthesis returning to the operating organization.
- Why this is / is not agent-owned: a high-severity security veto is valuable audit/risk gating within an engineering task, not general S5 identity authority.
- Evidence: [client model/tool policy](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/client.ts), [security](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/security.ts), [evaluator gate](https://github.com/shawnpetros/salazar/blob/e16841146e2ef2d71aa99117334939037e9804ff/src/engine/agents/evaluator.ts).
- Basis: source-static.
- Confidence: medium-high.
- Caveats: a parent human maintainer may exercise S5, not credited as a first-party autonomously owned loop.

### Absence scope

- Surfaces inspected: CLI config, SDK permission mode, command-hook policy, planner/evaluator templates and acceptance threshold.
- Plausible first-party paths checked: evaluator security veto and operator-specified policy; both are narrow project controls.
- Why no material first-party path remains: no organizational identity reconciliation decision or return-to-operation beyond fixed controls.

## Recursion

The scored recursion is one spec-to-code product-building organization. Its ongoing production generator is S1; the separately instantiated evaluator is conditional, complementary S3*. Planner is a serial project initializer, deterministic validators are mechanisms, and TUI/SQLite expose progress without proving a whole-current S3. A future distributed version with independent concurrent teams requires another assessment.

## Variety and escalation

Zod handoffs, automated validators, fresh model contexts, bounded feedback retries and Git rollback reduce uncertainty. If the reviewer rejects the work repeatedly, Orchestrator rolls back and continues to next feature. This bounded refusal policy does not prove human escalation, universal auditing or operational correctness. External provider/model availability and user-controlled acceptance risk remain outside the scored autonomy.

## Evidence gaps

- No Claude query, live code generation or adversarial audit executed; assessment is source-first only.
- README metrics of self-build success, test counts and costs are unverified project claims.
- Evaluator prompt promises browser checks, but the actual allowed tool list lacks a browser tool; source review credits only file/Bash inspection.
- `git diff HEAD~1` in evaluator instructions could check previously committed rather than current changes; exact evidence quality remains untested.
- Shared provider, mutable shared workspace and write-capable evaluator limit practical isolation, even though the separate audit-and-return mechanism is implemented.
