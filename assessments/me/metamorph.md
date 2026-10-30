---
harness_id: metamorph
project_name: Metamorph
repository: https://github.com/yohanvillarp/metamorph
review_ref: 8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Metamorph

## Review boundary

- System in focus: one installed Metamorph migration CLI run against a selected source codebase, with Mozaik-driven agent workers, shadow workspace, event bus, SQLite plan, verification and optional dashboard.
- Purpose and identity: autonomously migrate supported frontend/backend code between selected frameworks in a disposable shadow tree, validate changes, and let an operator explicitly apply a successful result to a branch.
- Relevant environment: existing source files and cross-file imports/exports, framework constraints, package manifests, model inference, build and syntax failures, dependency collisions, concurrent migration tasks and user application decision.
- Standard-distribution boundary: publicly installed `@nikelyh/metamorph` CLI `run`, `detect`, `apply`, `rollback`, configured inference adapters (non-mock default and optional mock), first-party application agents and event/state machinery, deterministic validators and optional dashboard. The external Mozaik provider implements general agent inference/process plumbing; its unrelated organization is not credited.
- Credited operating / distribution surfaces: `packages/@nikelyh/cli/src/commands/run/run.command.ts`, `packages/@nikelyh/application/src/{MigrationRunner,runtime,index}.ts`, `agents/registry/AgentRegistry.ts`, production `agents/worker/*`, `agents/reviewer/*`, `CoordinatorAgent.ts`, `IntegrationAgent.ts`, `PackageManagerAgent.ts`, `ReporterAgent.ts`, `packages/@nikelyh/infrastructure/src/inference/*`, `workspace/{ShadowWorkspace,MigrationIntegrator}.ts`, the domain catalogs and live CLI/UI state paths.
- Adjacent first-party surfaces excluded from ownership: `lab/server` and `lab/ui` experimentation, architecture whitepapers beyond code, root contributor `AGENTS.md`/`GEMINI.md`, test fixtures, package release/CI scripts, mock-only simulated model judgment and external Mozaik agent framework itself. A class named `Agent` without model-led decisive discretion is not counted as an autonomous actor.
- First-party operating / deployment modes considered: normal non-mock model-backed migration and optional `--mock`; reviewer enabled by default versus explicit disabled reviewer with deterministic auto-approval fallback; configurable concurrency/retries/integration rounds; interactive framework selection/dry-run; shadow-only completion and separate manual `apply`; optional dashboard observation.
- Recursion level: one migration project/run with separately created model Worker turns on source files as S1 units, an independent model Reviewer for per-file evidence and a deterministic plan-wide coordination/integration layer. Other migrations on the same machine are not one inferred strategic recursion.
- Reviewed revision: `8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c` (`develop` default head at freeze).
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The first-party `metamorph run` CLI chooses the source/target framework and resolves configuration, then constructs a persistent SQLite plan and separate shadow workspace with file/AST/build tools limited to that shadow root. `MigrationRunner` bootstraps an active Mozaik event bus and first-party descriptor registry; deterministic Mapper enumerates files, PackageManager edits manifest/compatibility metadata, and Coordinator monitors task/phase readiness. The registry distinguishes token-consuming Worker, Reviewer, Reporter and Integration from zero-token deterministic participants. Worker events enqueue model-driven temporary per-file Mozaik agents; a configured `InferencePort` uses `MozaikInferenceAdapter` in non-mock mode and a separate deterministic mock adapter in explicitly selected mock mode.

The active Reviewer has a separate model loop, supplied with a separately reread migrated file, architecture catalog, neighboring modules and syntax/structural checks. It can independently approve, reject, or report fatal mismatch; rejected file tasks return with errors for Worker repair. The Coordinator itself explicitly *does not call a model*: it starts integration when files/package tasks are settled and runs a watchdog. Integration runs real shadow install/build and structural verifiers; on build failure a temporary model agent may repair implicated files, followed by deterministic rebuild/requeue/failure within a fixed round budget. Successful run is marked by deterministic build/structural checks, not by autonomous project-wide discretion. A user must separately invoke `apply` for completed success, which creates a migration branch; that is release acceptance, not identity-level policy governance.

Primary sources: [CLI](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/cli/src/commands/run/run.command.ts), [migration runner](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/MigrationRunner.ts), [bootstrap](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/index.ts), [agent registry](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/registry/AgentRegistry.ts), [production inference adapter](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/infrastructure/src/inference/MozaikInferenceAdapter.ts), [apply](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/cli/src/commands/apply/apply.command.ts).

## Operational model

The operator selects a desired framework migration. A deterministic Mapper discovers files and generates events; the first-party Worker enqueues multiple file-specific inference loops on the real Mozaik runtime, with each temporary model agent reading source/imports and selecting edits in the isolated shadow tree. For each model-produced file, a separately instantiated Reviewer model receives direct filesystem-derived content, surrounding interfaces and architecture rules and can return a rejection that requeues the corresponding Worker with corrective feedback. These separate model judgments are S1 work and complementary audit. Cross-file compatibility feedback also regulates actual interactions among file workers. A separate deterministic Coordinator/Integration/SQLite layer observes all current file/package tasks, controls phase transitions and reopens broken tasks after whole-shadow build failures; although this is a strong first-party S3-specific construction path, discretionary whole-system control is not assigned to a model there. The end user—not the model workers—chooses whether to apply the successful shadow result to their original repository branch.

## S1 — Operations

- State: A
- Function: model-owned semantic transformation of individual migration files and bounded repair of failed build/source code in the active non-mock migration mode.
- Disturbance / variety regulated: varied framework conventions, imports/exports, code structure, tool results, API mismatch and incomplete or erroneous transformed files.
- Decisive decision or feedback right: a temporary Worker model decides source-specific edits via read/write/rename/create/delete/list tools, and a conditional integration-repair model chooses source fixes against real build errors; deterministic Mapper/PackageManager do not make these semantic model choices.
- Decision owner: actual per-file Mozaik model agents created by first-party production `InferencePort`, and optional temporary model repair agent, under CLI-selected source/target framework and workspace limits.
- Supporting / enforcement mechanisms: framework/architecture catalogs, shadow-root-bound tools, Mozaik inference adapter, configured model ID, Worker queue, file completion/status events, operator-selected source/target and deterministic task bookkeeping.
- Closure path: `FILE_DISCOVERED` and migration context → temporary model agent reads neighboring files and changes shadow source → actual file readback and inference completion → `FILE_MIGRATED` → reviewer/build feedback or completed file outcome changes subsequent correction/work.
- Boundary reachability: normal CLI `run` resolves non-mock credentials/config, passes shadow tools into `MigrationRunner` and production `MozaikInferenceAdapter`, then Worker enqueues `startWorkerLoop`, which creates and starts real `runLoop` models. `--mock` is a separate advertised simulation mode, not evidence of actual model judgment.
- Why this is / is not agent-owned: removing the model from Worker leaves the file enumeration, package edits and event queue but not adaptive semantic rewriting; dynamic source/API choices are made by an inference-loop actor. Mock transformations are deterministic and are not borrowed as independent proof of autonomy.
- Evidence: [active Worker](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/worker/WorkerAgent.ts), [Worker inference and file readback](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/worker/WorkerInferenceRunner.ts), [per-file prompt/evidence](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/worker/WorkerPromptBuilder.ts), [production Mozaik adapter](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/infrastructure/src/inference/MozaikInferenceAdapter.ts), [factory mock boundary](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/infrastructure/src/inference/InferenceFactory.ts).
- Basis: explicit and structural.
- Confidence: high for installed model-owned S1 wiring, medium for unexecuted live provider success.
- Caveats: model provider and Mozaik runtime are external dependencies; `--mock` does not prove live model behavior. Predefined package/framework rules and deterministic file scans should not be confused with LLM-owned decisions.

## S2 — Coordination

- State: A
- Function: model-judged attenuation of cross-file interface conflicts between concurrently migrated S1 file workers, with correction returned to the implicated Worker task.
- Disturbance / variety regulated: one worker changing a component/export while another worker uses stale prop/import names, incompatible router screens, missing modules and inconsistent dependency structure across independently transformed files.
- Decisive decision or feedback right: the separate Reviewer model examines the migrated file against neighboring imported modules, decides APPROVED/REJECTED/FATAL_MISMATCH, and sends concrete cross-file mismatch errors; the affected Worker model chooses the subsequent fix from the new evidence.
- Decision owner: first-party separately launched Reviewer inference model for substantive interface-consistency judgment, followed by the responsible Worker model for correction. Deterministic syntax checks, concurrency caps and ready flags only transport/enforce.
- Supporting / enforcement mechanisms: concurrency-limited Worker queue, global file-tree and neighbor/import context, original file readback, separate reviewer prompt/model, `FILE_REJECTED` requeue with bounded retries and integration's failed-build repair feedback.
- Closure path: different S1 file migrations create incompatible interfaces in one shadow project → Reviewer directly inspects updated source plus neighboring import/prop/export evidence → emits targeted rejection → Worker receives exact mismatch/neighbor hints and edits source → subsequent review/build checks the corrected relation.
- Boundary reachability: actual non-mock `run` initializes both Worker and enabled-by-default Reviewer descriptors; per-file completions emit `FILE_MIGRATED` to the Reviewer, whose independently created model then returns `FILE_REJECTED` and Worker retries. Disabling Reviewer removes this agent-owned relation and invokes an explicitly different deterministic bypass.
- Why this is / is not agent-owned: the cross-file interface judgment is made by a Reviewer model from concrete code evidence, not merely by message routing or fixed phase guards; Worker model interprets correction within its source task.
- Distinct S1 units: independently instantiated per-file Mozaik Worker inference sessions, potentially active up to configured concurrency, each transforming a file/surrounding source in a shared shadow migration.
- Inter-S1 disturbance: one S1 changes a module's prop/export or file placement while a different S1 updates its consumer based on old assumptions; the resulting imports/route integration conflict across their outputs.
- Attenuating coordination relation: first-party cross-file consistency reviewer model with project/neighbor evidence and explicit targeted reject/retry into the affected file worker.
- Feedback into subsequent S1 behaviour: `FILE_REJECTED` errors are embedded in `buildFixRejectedPrompt`, with actual disk/import evidence and a revised correction task before the next worker iteration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the Reviewer prompt explicitly checks inter-file imports, public callback/export compatibility and shared router composition; the correction regulates incompatible co-produced S1 changes, not mere existence of an event bus or three-slot queue.
- Evidence: [Worker concurrency/repair path](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/worker/WorkerAgent.ts), [project-wide file hints](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/worker/WorkerPromptBuilder.ts), [cross-file review prompt and return](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/reviewer/ReviewerInferenceRunner.ts), [separate Reviewer participant](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/infrastructure/src/inference/MozaikInferenceAdapter.ts), [neighbor context](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/context/NeighborContext.ts).
- Basis: explicit and structural.
- Confidence: medium-high for source-defined cross-file rejection loop; no live multi-file provider-backed migration executed.
- Caveats: the Reviewer uses a context snapshot assembled by first-party code rather than arbitrary live file tools. If disabled or in deterministic mock mode the specific autonomous S2 witness is not exercised; locks/queues alone are not credited S2.

## S3 — Inside-and-now control

- State: C
- Function: first-party whole-migration-current plan/phase control through status aggregation, integration admission, deterministic cross-task remediation and terminal success/failure authority; autonomous discretionary project controller must still be composed.
- Disturbance / variety regulated: pending/failed file and package tasks, lost completion signals, incomplete builds, malformed architectural output, excessive retries, stalled migration phases and uncertainty over whether the entire run is actually ready.
- Decisive decision or feedback right: a function-specific coordinator/plan path exposes phase-start, project-wide work-status, requeue, retry-budget, migration success/failure and integration controls. Shipped policy makes those choices deterministically from task status and build/validator results; no agent chooses discretionary whole-project priority, resource reassignment or acceptance criteria.
- Decision owner: currently deterministic first-party `CoordinatorAgent`/`IntegrationAgent` handlers and fixed configuration; a developer would have to compose an autonomous S3 controller with legitimate discretion over the exposed plan/current-control path to receive `A`.
- Supporting / enforcement mechanisms: SQLite `MigrationPlan`, global pending/failed/completed records, `planReadyForIntegration`, event-triggered Coordinator, watchdog, integration locks, build/verifier diagnostics, requeued file tasks and dashboard reporting.
- Closure path: all file/package task states plus integration build/validator evidence → current-plan coordinator/integrator determines phase transition, retry/repair set or failure/success within configured limits → `PHASE_INTEGRATION_STARTED`, `FILE_REJECTED` or `MIGRATION_COMPLETED` changes subsequent task execution and run state; discretionary model control is not wired.
- Boundary reachability: ordinary CLI initialization joins the shipped Coordinator and Integration participants, invokes `StateRepository` plan methods, and exports `createCoordinatorAgent`, `resolveRuntime` and application agents as function-specific construction surfaces. These are active, not merely tests; the missing component is model ownership of the whole-current supervisory decision.
- Why this is / is not agent-owned: source explicitly says the Coordinator does not call a model; the Integration temporary model performs local source repair after deterministic build failure, not project-wide current priority/commitment choice. Purely mechanical timeouts, phase gates and build pass/fail cannot be scored `A`.
- Whole-system current view: the run-level persisted plan gathers every file task, package-manager task, phase, result and integration-round count; the Coordinator watches readiness and the UI/CLI can show progress, unlike one worker's local task report.
- Current-control decision scope: dispatch integration only after all relevant work settles, reopen implicated file tasks, stop after retry/watchdog budget, and finalize a successful verified shadow migration; a future agent owner could use these direct controls to decide current task/resource commitments.
- Evidence: [model-free Coordinator and watchdog](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/CoordinatorAgent.ts), [integration control/repair/terminalization](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/IntegrationAgent.ts), [ready-for-integration predicate](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/planReady.ts), [state/runtime API](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/runtime.ts), [CLI plan and progress](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/cli/src/commands/run/run.command.ts).
- Basis: structural function-specific constructor, without autonomous S3 owner.
- Confidence: medium for positive construction path and high that present Coordinator is deterministic.
- Caveats: `C` is not a claim that the built-in Coordinator autonomously manages a project. The optional dashboard is telemetry, integration repair model is task-local, and manual `apply` is a separate operator publication action—not a second parent-governed S3 mode.

## S3* — Complementary audit

- State: A
- Function: separate model-and-structural inspection of transformed source against migration intent and neighboring code, with binding rejection/correction feedback.
- Disturbance / variety regulated: worker self-report mismatch, syntactically invalid transforms, hollow/incorrect UI moves, mismatched callbacks/exports, missing files and architecture drift.
- Decisive decision or feedback right: independent Reviewer inference model judges file content and neighbor/canonical migration evidence with APPROVED/REJECTED/FATAL_MISMATCH; a rejection is acted upon through the built-in retry path before project integration.
- Decision owner: a separately instantiated Reviewer model, distinct from the writing Worker model and its source-change loop; deterministic syntax/structure verifiers are complementary enforcement, not an autonomous decision maker.
- Supporting / enforcement mechanisms: actual migrated file reread, built neighbor context, migration catalogs, syntax/structure validation, separate model role and optional `reviewerModel`, strict structured JSON result, status/event persistence, bounded repair queue and integration verification.
- Closure path: a Worker announces a migrated file → first-party code rereads the real shadow source and checks syntax/structure, independent Reviewer model analyzes direct file and neighbor evidence → approval completes task or reject/fatal feeds the Worker/plan → corrected file is rechecked before whole-project build and eventual application.
- Boundary reachability: the default live registry joins `Reviewer` (separate from Worker) and `FILE_MIGRATED` activates model inference in the normal CLI. `--disable-agents reviewer` intentionally selects a different zero-token bypass mode and removes model audit, but does not invalidate the shipped default autonomous path.
- Why this is / is not agent-owned: Reviewer model, not Worker, owns substantive correctness/architecture verdict; fixed syntax checks alone would not justify `A`, and mock/disabled-reviewer auto-approval must not be mistaken for independent audit.
- Claim being audited: a model Worker changed one source file in the shadow workspace correctly for the selected framework, with valid imported APIs and intact application structure.
- Ordinary reporting path: Worker inference completion and `FILE_MIGRATED`, plus file content readback and task status, supply the standard implementation report.
- Complementary access path: independent Reviewer gets a first-party filesystem-derived copy of the migrated code, neighbor module context and migration rules; syntax/structure checks also inspect current disk evidence independent of the Worker model's final text.
- Independence boundary: Reviewer is a separately instantiated model participant with its own review instruction and structured verdict, no worker editing tools; the same configured provider/model may serve both roles, and Reviewer does not have arbitrary direct tool browsing beyond supplied snapshots.
- Who acts on findings: built-in `FILE_REJECTED`/`FILE_FATAL_MISMATCH` handlers requeue the affected Worker or mark it failed; the whole-migration Coordinator/Integration then waits, validates or fails rather than treating a worker's self-attestation as success.
- Evidence: [live Reviewer/bypass distinction](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/reviewer/ReviewerAgent.ts), [independent reviewer model/structured verdict](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/infrastructure/src/inference/MozaikInferenceAdapter.ts), [reviewer direct-evidence prompt and return](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/reviewer/ReviewerInferenceRunner.ts), [retry return](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/worker/WorkerAgent.ts), [pre-inference structural checks](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/reviewer/StructureVerifier.ts).
- Basis: explicit and structural.
- Confidence: medium-high for source-defined independent review return; no live LLM run.
- Caveats: reviewer independence is a separate model context and directly sourced artifact snapshots, not necessarily a separate vendor or direct unbounded file access. Deterministic bypass mode auto-approves and would not itself meet S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped process autonomously senses external/future migration-market distinctions, generates long-horizon capability options, selects adaptation and returns that choice into present Metamorph capability.
- Disturbance / variety regulated: emerging framework changes, future migrations and platform developments are addressed by release catalog maintenance rather than a first-party outside-and-then intelligence system.
- Decisive decision or feedback right: no model or legitimately delegated parent owns a documented prospective external/environmental adaptation decision inside the running migration organization.
- Decision owner: none established at this boundary; the user picks from currently supported framework pairs, and maintainers may later ship new rules as adjacent development work.
- Supporting / enforcement mechanisms: static layered migration catalogs, runtime framework detection, hints for current Next.js migration structure, model selection/configuration, telemetry and release documentation.
- Closure path: no prospective sensing → new strategic migration capability option → authoritative adaptation choice → returned changed agent/config/capability cycle. Target selection and rule-based current-source transformations are S1/planning input, not S4.
- Why this is / is not agent-owned: model Workers infer code changes inside one declared migration objective, but do not determine which future environmental opportunities should change Metamorph's own capabilities.
- Evidence: [current migration catalog](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/migration/registry.ts), [current Next migration hints](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/analysis/NextMigrationHints.ts), [CLI target selection](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/cli/src/commands/run/run.command.ts), [static catalog architecture](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/docs/architecture/05-layered-migration-catalogs.md).
- Basis: bounded first-party absence.
- Confidence: medium-high for current production paths.
- Caveats: OSS maintainers can add migration catalogs or change provider models, but this external development control is not a first-party operational S4 return loop.

### Absence scope

- Surfaces inspected: CLI detection/run/config, application catalog registry and current migration hints, inference adapters, Reporter, plan/dashboard telemetry, developer architecture/release documents and mock mode.
- Plausible first-party paths checked: catalog selection from environment, AI review of new code, Next target structure hints, reported next steps, user configuration and future catalog contributions.
- Why no material first-party path remains: they transform/verify the current selected source-to-target migration or offer static advice, without a shipped prospective external scanning/adaptation option generator and return of capability-level choices to subsequent Metamorph operation.

## S5 — Policy and identity

- State: —
- Function: no shipped ultimate-identity/constitutional policy adjudication with authoritative model or parent decision and return into subsequent runtime governance.
- Disturbance / variety regulated: whether to publish a migration, which framework to target, credentials and resource limits are handled by users or fixed configuration, not identity-level disputes resolved by a Metamorph policy institution.
- Decisive decision or feedback right: operator selects migration goal and later invokes `apply`; CLI checks successful run and prevents double application. Those are acceptance and safety boundaries, not policy-identity creation or arbitration.
- Decision owner: no qualifying autonomous or parent S5 function owner in this system. The user can set goals and permissions, but there is no first-party identity-dispute return path distinct from current migration acceptance.
- Supporting / enforcement mechanisms: shadow isolation, `apply` success gate/branch, config precedence, reviewer/model disabling rules, explicit rollback and user-owned repository/credentials.
- Closure path: completed shadow migration → user chooses `apply` or rollback → target branch publication changes a particular project; no identity-level issue → legitimate constitutional authority → binding charter decision → return into future operating model.
- Why this is / is not agent-owned: users and maintainers establish fixed scope/configuration outside the run; model workers cannot amend Metamorph's purpose, ultimate-policy rules or the user's repository authority.
- Evidence: [manual apply gate](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/cli/src/commands/apply/apply.command.ts), [migration integrator](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/infrastructure/src/workspace/MigrationIntegrator.ts), [runtime plan/config](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/runtime.ts), [CLI settings](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/cli/src/commands/run/run.command.ts), [reviewer bypass mode](https://github.com/yohanvillarp/metamorph/blob/8871b937a4e6d0f6f5f9f08b4ca1e801fd98196c/packages/@nikelyh/application/src/agents/registry/AgentRegistry.ts).
- Basis: bounded first-party absence.
- Confidence: high for absence of an explicit ultimate-policy loop in the examined runtime.
- Caveats: contributor governance and `apply` permission are legitimate human acts, not function-specific S5 closure; the reviewer is an audit actor, not an identity authority.

### Absence scope

- Surfaces inspected: CLI run/apply/rollback/config; domain and application plan authority; agent registry/reviewer disabling, shadow workspace isolation, integration success gate, dashboard/operator controls and contributor materials.
- Plausible first-party paths checked: user confirmation before applying, migration approval/rejection, reviewer fatal mismatch, config/model change, rollout/rollback and external OSS maintainer decisions.
- Why no material first-party path remains: each is a current migration choice, implementation safeguard, opt-out or out-of-boundary development action; no first-party path formulates, authoritatively adjudicates and returns an ultimate identity or policy verdict to govern future runs.

## Recursion

Each file-specific Worker inference session acts as an S1 operational subunit during one migration run. The independent Reviewer is an audit/consistency participant; the event coordinator is a deterministic participant and does not become an autonomous higher-level model by being named `CoordinatorAgent`. The shadow `MigrationPlan` is run-local, while user CLI controls live at an external operator boundary. The mock adapter and `lab` modules are alternate testing/experiment surfaces and do not supply the production model-owner proof.

## Variety and escalation

File-level model inference and cross-file model review absorb migration variety, while the first-party coordinator/integrator contains current plan and build variety through fixed phase/retry rules. A reviewer rejection returns errors to one Worker; a failed whole-project build reopens implicated file tasks or activates one temporary repair model; exhaustion marks the migration failed. No automatic `apply` follows success: a user separately decides whether to install the shadow result. Neither this operational escalation nor optional catalog work creates a future-strategy or identity system.

## Evidence gaps

- No authenticated provider-backed migration was invoked. Native tests and `--mock` can validate deterministic wiring and examples but cannot prove live inference correctness or a particular model's independent judgment.
- S2's positive witness relies on multiple per-file model-owned S1s, real shared import/API incompatibility and a reviewer model that rejects and returns actionable cross-file feedback; a one-file run or disabled Reviewer need not exercise S2.
- S3 `C` deliberately does **not** credit the deterministic Coordinator's state transitions as `A`. The explicit run-wide phase/retry/control path exists but developer composition of discretionary whole-current model control is missing; mere source visibility or telemetry would not establish it.
- S3* Reviewer model's evidence is a filesystem-derived source/context snapshot with no arbitrary file tools; model-family separation is optional and actual reviewer independence must be checked in live deployments.
