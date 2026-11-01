---
harness_id: certo
project_name: Certo
repository: https://github.com/alessioricco/Certo
review_ref: d4b58e5113809a82f2fe6a42dbc76306663b4241
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Certo

## Review boundary

- System in focus: Certo's shipped task/model/verification controller assembled with its OpenHands SDK agent and supported local administrative CLI.
- Purpose and identity: complete coding tasks across configurable models with bounded execution and evidence-based terminal verdicts.
- Relevant environment: target code/workspace, task constraints, provider/model availability, tool failures, operator model-capability choices and budgets.
- Standard-distribution boundary: normal CLI/server task pipeline and local independent-tests strict mode; supported init-models operator workflow included. SDK/provider internals are dependencies; benchmark runs and maintenance research are not operational owners.
- Credited operating / distribution surfaces: agent.py/tool wiring, runner.py task lifecycle, verification/acceptance and independent_tests, model catalog/selection/escalation, init_models and skill/configuration interfaces.
- Adjacent first-party surfaces excluded from ownership: benchmark datasets/replay reports, repository development agents/CLAUDE.md and CI, contributor governance; benchmark tooling may explain interfaces but its scores do not donate functions.
- First-party operating / deployment modes considered: local and Docker task execution, autonomous versus interactive checkpoints, configured model fallback/escalation, optional local non-resume independent tests with strict verdict control, and terminal-only model onboarding.
- Recursion level: one deployed harness instance; child execution is not presumed recursively viable.
- Reviewed revision: `d4b58e5113809a82f2fe6a42dbc76306663b4241`.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7 (Index active release; Skills main 0.3.8 inspected but not silently activated).

## Repository architecture

agent.py composes an SDK Agent with project tools, skills and task-completion policies. runner.py creates/persists conversations, enforces deadlines/cost/iteration limits, detects unfinished task-tracker items and independently reruns project checks; bounded follow-ups or a model ladder retry on current-task failure. ModelChain walks a ranking fixed for that task, not a learned future policy. Independent test writers run before the build in separate scratch workspaces with the pre-build project and only an editor; the builder cannot read their test sets. After the build, hash-checked tests are injected/run/removed; strict mode can downgrade verified to independent_failed. Operator init_models discovers reachable model candidates, probes tool-calling, obtains user ratings/activation, writes model files and previews/chooses persistent per-run mode.

## Operational model

The assembled builder agent owns code actions; Certo owns first-party task, environment, model/tool, retry and verdict orchestration rather than borrowing all OpenHands functions. Hidden-test writers are separate quality-observation actors. Deterministic project-check reruns, model cursors and budget enforcement do not become autonomous S3 merely because they govern task phases. A supported operator capability-onboarding loop is assessed separately from task-local model fallback.

## S1 — Operations

- State: A
- Function: autonomous coding-task transformation through the assembled first-party execution pipeline.
- Disturbance / variety regulated: unknown repositories, implementation failures and model/tool errors.
- Decisive decision or feedback right: choose and execute code/tool actions and corrective actions on received check feedback.
- Decision owner: Certo's configured builder agent in an OpenHands conversation.
- Supporting / enforcement mechanisms: agent/tool wiring, workspace/project environment, persisted Conversation, task tracker and bounded retries.
- Closure path: tool results and harness check/task-tracker follow-ups return into the builder conversation; final outcome is recorded.
- Boundary reachability: runner stream_task builds the configured first-party Agent and invokes its SDK conversation with the requested workspace, task and tools.
- Why this is / is not agent-owned: removing the builder's model choice leaves execution/check machinery without discretionary implementation.
- Evidence: [src/certo/agent.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/agent.py); [src/certo/tools.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/tools.py); [src/certo/runner.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/runner.py); [README.md](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: SDK supplies underlying model/tool loop; only Certo's assembled operating mode is credited.

## S2 — Coordination

- State: —
- Function: no distinct-S1 interference/coordination relation established.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: Model stages take over the same coding task; independent writers produce audit probes in separate scratch areas. No concrete interacting operational S1 cells with a shipped disturbance-specific mutual coordination loop were established.
- Evidence: [src/certo/runner.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/runner.py); [src/certo/model_selection.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/model_selection.py); [src/certo/escalation.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/escalation.py); [src/certo/independent_tests.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/independent_tests.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [src/certo/runner.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/runner.py); [src/certo/model_selection.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/model_selection.py); [src/certo/escalation.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/escalation.py); [src/certo/independent_tests.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/independent_tests.py); agent.py/tool wiring, runner.py task lifecycle, verification/acceptance and independent_tests, model catalog/selection/escalation, init_models and skill/configuration interfaces..
- Plausible first-party paths checked: model handoffs/ladder, sequential task phases, independent writer sets, workspace isolation and benchmark concurrency.
- Why no material first-party path remains: Model stages take over the same coding task; independent writers produce audit probes in separate scratch areas. No concrete interacting operational S1 cells with a shipped disturbance-specific mutual coordination loop were established.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current organizational regulatory decision loop.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: These paths enforce one coding task's completion/resource contract and fixed fallback rules. Generic task continuation/action approval does not establish whole-system current resource/commitment bargaining; no distinct function-specific autonomous or parent regulatory closure was found.
- Evidence: [src/certo/runner.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/runner.py); [src/certo/deadline.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/deadline.py); [src/certo/cost_limit.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/cost_limit.py); [src/certo/model_selection.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/model_selection.py); [src/certo/escalation.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/escalation.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [src/certo/runner.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/runner.py); [src/certo/deadline.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/deadline.py); [src/certo/cost_limit.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/cost_limit.py); [src/certo/model_selection.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/model_selection.py); [src/certo/escalation.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/escalation.py); agent.py/tool wiring, runner.py task lifecycle, verification/acceptance and independent_tests, model catalog/selection/escalation, init_models and skill/configuration interfaces..
- Plausible first-party paths checked: current task tracker, deadlines/budgets, fixed candidate ranking, rung continuation and interactive/confirmation callbacks, including possible operator parent modes.
- Why no material first-party path remains: These paths enforce one coding task's completion/resource contract and fixed fallback rules. Generic task continuation/action approval does not establish whole-system current resource/commitment bargaining; no distinct function-specific autonomous or parent regulatory closure was found.

## S3* — Complementary audit

- State: A
- Function: complementary task-grounded challenge to builder/project-check claims in strict independent-tests mode.
- Disturbance / variety regulated: a builder can pass its own checks while omitting requirements or sharing mistaken assumptions.
- Decisive decision or feedback right: independently derive expected behavior from the original task/pre-build project, then challenge acceptance with protected test evidence.
- Decision owner: separate test-writer agents supply the independent oracle judgment; deterministic run/vote/strict-verdict machinery transports it.
- Supporting / enforcement mechanisms: scratch folders outside builder workspace, pre-build copy, editor-only conversations, test hashes, post-build execution/cleanup and majority vote.
- Closure path: runner applies strict independent failures after ordinary checks/acceptance, changing verified into independent_failed and persisting the actual final verdict returned to the caller.
- Boundary reachability: stream_task invokes _write_independent_tests before build and _apply_independent_tests plus _apply_strict_independent_tests afterward; local non-resume mode only.
- Why this is / is not agent-owned: the agent authors the independent expected-behavior tests; the harness's vote/parser does not own that judgment. Removing writer discretion leaves no independent oracle generation.
- Evidence: [src/certo/independent_tests.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/independent_tests.py); [src/certo/runner.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/runner.py); [src/certo/config.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/config.py).
- Basis: structural.
- Confidence: high.
- Caveats: report-only mode alone is not credited as corrective closure. Strict failure prevents successful acceptance; it does not automatically repair the code. Test quality is not guaranteed and split/error/none do not downgrade.
- Claim being audited: the builder's final project meets its task despite ordinary checks passing.
- Ordinary reporting path: builder narrative, task completion and project verification verdict.
- Complementary access path: independently specified hidden probes, authored from task/pre-build state and executed against finished artifacts.
- Independence boundary: writers never see builder work; tests remain outside the project during build and are hash-checked before execution.
- Who acts on findings: the first-party strict verdict path withholds verified acceptance and returns/persists independent_failed for caller control.

## S4 — Outside-and-then intelligence

- State: P
- Function: operator-governed adaptation of the deployed model-capability repertoire for future task runs.
- Disturbance / variety regulated: available/reachable provider models differ from the previously configured repertoire; future tasks need a chosen capability/cost strategy.
- Decisive decision or feedback right: after discovery/probes, choose supported models and ratings, then select persistent manual/auto/escalate operating mode.
- Decision owner: the legitimate local operator in certo init models; no autonomous S4 owner credited.
- Supporting / enforcement mechanisms: reachable-model enumeration, tool-calling test, model/catalog/profile files, mode preview and user-settings persistence.
- Closure path: only working candidates are written; returned operator choice writes models.yaml/catalog data and CERTO_MODEL_SELECTION, consumed by subsequent task configuration and model ranking/ladder.
- Boundary reachability: init_models.main is shipped terminal CLI administration; its fetch/check/choose/write/preview path persists settings used by normal runner/model_selection. Not a research-only benchmark script.
- Why this is / is not agent-owned: the operator decides the future repertoire; deterministic discovery/probing and serialization implement that decision. Per-task fallback alone remains ordinary operation.
- Evidence: [src/certo/init_models.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/init_models.py); [src/certo/model_catalog.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/model_catalog.py); [src/certo/model_selection.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/model_selection.py); [src/certo/config.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/config.py).
- Basis: structural.
- Confidence: medium.
- Caveats: narrow parent capability-onboarding loop, not autonomous learning or continuous environmental strategy; user ratings may be subjective. Ordinary static YAML edits alone would not justify P.
- External distinction: models installed on the local Ollama server or available through configured providers, plus actual tool-calling viability.
- Future / prospective distinction: which capability/cost repertoire and model-selection strategy will be available for future coding tasks.
- Adaptation option generated: working candidate sets with known/user-provided ratings and previewed manual, auto-model or escalation choices.
- Path back into current capability / S3: operator activation writes model/setting files; subsequent load_config/catalog selection changes the actual builder model repertoire. No separate positive S3 is inferred.
- Parent adaptation closure: discovered/tested options → operator choice → persisted active model set/mode → subsequent task execution under that capability choice.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy authority-return path established.
- Disturbance / variety regulated: the function-specific disturbance described below is not regulated by a shipped organizational loop.
- Decisive decision or feedback right: no function-specific decisive organizational right established.
- Decision owner: not established; runtime mechanisms retain their narrower implementation role.
- Supporting / enforcement mechanisms: the inspected task, lifecycle or configuration mechanisms below.
- Closure path: no function-specific returned decision into subsequent regulation established.
- Why this is / is not agent-owned: These paths set coding-task constraints, approve actions or adapt the model repertoire. No identity/ultimate-policy dispute is routed to a legitimate ultimate authority and returned as a resolved governing policy. Contributor governance is outside the product boundary.
- Evidence: [src/certo/agent.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/agent.py); [src/certo/config.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/config.py); [src/certo/runner.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/runner.py); [src/certo/init_models.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/init_models.py); [src/certo/acceptance.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/acceptance.py).
- Basis: structural.
- Confidence: medium.
- Caveats: Bounded to the pinned supported distribution; hypothetical downstream extensions are not assessed.

### Absence scope

- Surfaces inspected: [src/certo/agent.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/agent.py); [src/certo/config.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/config.py); [src/certo/runner.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/runner.py); [src/certo/init_models.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/init_models.py); [src/certo/acceptance.py](https://github.com/alessioricco/Certo/blob/d4b58e5113809a82f2fe6a42dbc76306663b4241/src/certo/acceptance.py); agent.py/tool wiring, runner.py task lifecycle, verification/acceptance and independent_tests, model catalog/selection/escalation, init_models and skill/configuration interfaces..
- Plausible first-party paths checked: task instructions, generated project context, permission/confirmation callbacks, budgets, model-onboarding decisions and caller acceptance checks.
- Why no material first-party path remains: These paths set coding-task constraints, approve actions or adapt the model repertoire. No identity/ultimate-policy dispute is routed to a legitimate ultimate authority and returned as a resolved governing policy. Contributor governance is outside the product boundary.

## Distributed OSS parent arrangement

MIT licensing and contributor/maintainer activity establish distribution provenance, not project-level S3/S4/S5 parent closure. This assessment concerns the deployed product boundary; no organization-level parent mode is inferred from local maintainer decisions.

## Self-hosted and non-human modes

Local operators have a concrete S4 model-repertoire onboarding mode, distinct from generic task approvals. Interactive checkpoints remain task-level operation, not a separately inferred S3 or S5 parent mode. Docker/resume paths do not support hidden test writing and are not used for the S3* positive claim.

## Recursion

Nested execution and delegated tasks do not establish recursive viable systems; no child full metasystem is claimed.

## Variety and escalation

Verification outcomes and failure signatures attenuate noisy task reports into bounded follow-ups or terminal states; static model ranks/ladders expand retry repertoire. Independent tests add complementary requirement distinctions. Limits enforce operator-selected constraints without inheriting organizational decision ownership.

## Evidence gaps

No real SDK/provider agent run or benchmark performed. Native pytest-dependent tests could not run in the workspace (pytest absent); pure source, relevant existing test surfaces and exact runner/admin wiring were inspected. S4 is a bounded operator-onboarding interpretation at medium confidence, not a generic claim that configuration is adaptation. Hidden-test efficacy is not empirically established here.
