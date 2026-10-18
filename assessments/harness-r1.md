---
harness_id: harness-r1
project_name: Harness-R1
repository: https://github.com/DeepExperience/Harness-R1
review_ref: 2b3f125710ed14ea8a863e6b39a2eb9951cc7181
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Harness-R1

## Review boundary

- System in focus: The distributed first-party executable Harness-R1 **harness-improvement experiment** at the level of operational task-agent rollouts, model-backed harness-engineer patch proposals, validation, and reruns with changed runtime hooks. This is the experiment recursion, not an entire enterprise or the external model-serving infrastructure.
- Purpose and identity: Execute environment-coupled agent tasks, learn from failed trajectories, propose new executable runtime overlay hooks and exercise those hooks in subsequent target rollouts to evaluate prospective harness capability.
- Relevant environment: WebShop, ALFWorld and DBBench tasks, tool affordances and actions, target agent failures, response/observation traces, external engineer/target inference and measured task rewards.
- Standard-distribution boundary: Bundled AgentBench target task runtime, first-party hook compiler and patch schema, Relax example engineer/evaluator driver and shipped evaluation scripts for model-backed patch generation and subsequent target rerun. Shipped executable experimental mode is credited; remote models' unrelated policy, benchmark authorities, project maintainers and training enterprise are not.
- Credited operating / distribution surfaces: [task.py L252-295](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L252-L295), [task.py L469-550](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L469-L550), [task.py L542-655](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L542-L655), [harness_r1_patch.py L357-443](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_patch.py#L357-L443), [harness_r1_patch.py L669-715](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_patch.py#L669-L715), [harness_r1_batch_debug.py L483-496](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_batch_debug.py#L483-L496), [code_runner.py L136-225](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/harness/code_runner.py#L136-L225), [eval_webshop_checkpoint_patches.py L462-625](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L462-L625), [eval_webshop_checkpoint_patches.py L626-815](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L626-L815), [eval_webshop.sh L1-75](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/scripts/eval_webshop.sh#L1-L75).
- Adjacent first-party surfaces excluded from ownership: Training model weights, developer/CI/release organization, paper score tables, precomputed benchmark result fixtures, model-provider organization, human-run deployment/production acceptance. The demo at [run_demo.py L1-20](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/demo/run_demo.py#L1-L20) replays a stored engineer patch and does not itself generate autonomous edits.
- First-party operating / deployment modes considered: Real model-backed WebShop task execution; model-backed engineer patch generation with fresh target-rerun feedback; separately enabled generate-only/reused patch run; ALFWorld/DBBench hook support; deterministic offline demo as corroboration only.
- Recursion level: The harness-improvement experimental process; separate task-agent episodes deliver S1 outcomes while retrospective external-task failures drive future capability changes in S4.
- Reviewed revision: 2b3f125710ed14ea8a863e6b39a2eb9951cc7181, frozen by [Index intake #1691](https://github.com/opensiro/vsm-harness-index/issues/1691) and [batch #1692](https://github.com/opensiro/vsm-harness-index/issues/1692).
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The WebShop task runtime injects actual environment observations and available actions into the model session, obtains model tool_calls using session.sync_action, executes the chosen search/click action subject to configured guards, then delivers fresh outcome observations to the next model turn. The installed code hooks can alter action policy or guidance; these are operational execution constraints rather than identity-level decisions. [task.py L469-550](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L469-L550); [task.py L542-655](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L542-L655).

The harness engineer receives failed baseline trajectories, calls a configured model, parses a structured patch, validates add_code_hook against the declared schema, and compiles restricted AST hook code. The first-party evaluator writes a patch file and executes a **new target rollout** using the modified task definition. Its paired comparison checks source task identifiers and goal hashes before computing new-versus-baseline reward. [eval_webshop_checkpoint_patches.py L462-625](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L462-L625); [eval_webshop_checkpoint_patches.py L710-815](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L710-L815); [harness_r1_patch.py L357-443](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_patch.py#L357-L443); [code_runner.py L136-225](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/harness/code_runner.py#L136-L225).

The shipped task-definition builder installs patches as a harness_overlay; WebShop task initialization compiles the hook and reaches its on_init, make_pre_hint, on_before_action and on_post_step callback points. Generation-only and patch_source_root allow persisted artifacts to be evaluated/reused separately. Unlike a multi-round promotion engine, no first-party autonomous universal production release adoption policy is established. [harness_r1_patch.py L669-715](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_patch.py#L669-L715); [harness_r1_batch_debug.py L483-496](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_batch_debug.py#L483-L496); [task.py L252-295](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L252-L295); [eval_webshop_checkpoint_patches.py L626-815](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L626-L815).

An isolated local source checkout at this exact commit passed python scripts/check_release.py: required-file, symlink, sensitive-text, shell syntax, Python compileall and **38/38 upstream unittest tests**. This verifies shipped source conformance, not claims of actual benchmark score or GPU/model output. Apache-2.0 first-party license was reviewed, while bundled dependencies retain their separate notices.

## Operational model

A model-operated target task loop chooses tools based on environment observations (current operational S1). A separately configured model-backed harness engineer examines earlier task failures and proposes prospective executable changes. Patch validation constrains their effect; the evaluator installs the changed capability in a later target task attempt and measures returned feedback. This is a bounded research/experiment S4 adaptation loop, not proof of deployment to arbitrary production systems or of standing whole-current organizational governance.

## S1 — Operations

- State: A
- Function: Environment-coupled agent task action and outcome production.
- Disturbance / variety regulated: Variable task goals, search/click affordances, observations and failed tool outcomes.
- Decisive decision or feedback right: Configured target model selects tool call and subsequent response in light of real prior environment outcomes.
- Decision owner: Model-backed target agent instantiated into the first-party AgentBench task loop; third-party inference is a service, not the harness governance owner.
- Supporting / enforcement mechanisms: Session state, WebShop tools/environment, hook/guard runtime, tool schema, step budget and output collection.
- Closure path: Environment observation → session.sync_action → model tool_calls → first-party tool/environment effect → observation delivered to the next session turn → task result.
- Boundary reachability: The first-party task code actually invokes the decision loop via its shipped evaluation task definition and runnable entrypoint, not merely an optional abstract integration.
- Why this is / is not agent-owned: Removing model discretion leaves fixed rules and replay but not novel choice over next action; restrictions constrain rather than originate context-sensitive tool decisions.
- Evidence: [task.py L469-550](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L469-L550); [task.py L542-655](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L542-L655); [harness_r1_batch_debug.py L483-496](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_batch_debug.py#L483-L496).
- Basis: Explicit source-wired operational agent/tool feedback.
- Confidence: High structural confidence; live hosted inference not run.
- Caveats: Hard-coded hooks may force or block local actions; benchmark success is not established by this assessment.

## S2 — Coordination

- State: —
- Function: No demonstrated first-party disturbance-specific reciprocal regulation of independently viable S1 units.
- Disturbance / variety regulated: Concurrent evaluation batches and processes risk shared ports/output collision, handled by static per-batch allocation and isolation.
- Decisive decision or feedback right: Runner assigns deterministic worker port, batch order and process lifecycle rather than exercising context-sensitive inter-S1 coordination authority.
- Decision owner: External run configuration and deterministic evaluator, not an agent-owned S2-specific controller.
- Supporting / enforcement mechanisms: Batch-specific port/paths, worker process launch, configured limits, isolation.
- Closure path: Scheduled subprocesses produce isolated run outputs; no observed inter-S1 disturbance → revised mutual operating constraint → feedback into distinct S1 units is present.
- Why this is / is not agent-owned: Concurrency protection and sequencing alone are not a VSM S2 coordination relation between independent operational cells.
- Evidence: [harness_r1_batch_debug.py L1-100](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_batch_debug.py#L1-L100); [harness_r1_batch_debug.py L560-680](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_batch_debug.py#L560-L680); [eval_webshop_checkpoint_patches.py L462-625](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L462-L625).
- Basis: Bounded first-party negative after inspecting parallel-run paths.
- Confidence: Medium-high within shipped experiment mode.
- Caveats: External orchestrators may build separate coordination that is outside the reviewed recursion.

### Absence scope

- Surfaces inspected: Target task loop, runner assignment/concurrency controls, evaluation subprocess handling, patch execution sandbox, reward dispatch.
- Plausible first-party paths checked: Concurrent batches, worker port contention, sharing patches and evaluator resource controls.
- Why no material first-party path remains: These paths isolate or serialize work; they do not sense and damp a concrete disturbance between two independently viable S1 units with returned coordination decisions.

## S3 — Inside-and-now control

- State: —
- Function: No agent-owned or operationally closed parent-governed whole-current resource/commitment regulation at this recursion.
- Disturbance / variety regulated: Task execution failures, patch rejection and timeouts threaten single experiment batch execution, not a standing whole-current portfolio.
- Decisive decision or feedback right: Fixed CLI/config run bounds and target assignment, not a whole-system priority/commitment intervention decision.
- Decision owner: Experiment operator and deterministic runner for ordinary task scheduling; engineer model owns a prospective patch, not current multi-unit resource bargaining.
- Supporting / enforcement mechanisms: Worker concurrency limits, retry/failure statuses, task metrics, process cleanup.
- Closure path: Batch failures → ordinary retry/score; missing whole-current resource/commitment view → S3 choice → binding cross-unit current action.
- Why this is / is not agent-owned: Executing budgets, task dispatch or scoring does not confer independent current-control decision rights.
- Evidence: [eval_webshop_checkpoint_patches.py L462-625](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L462-L625); [eval_webshop_checkpoint_patches.py L626-815](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L626-L815); [harness_r1_batch_debug.py L560-680](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_batch_debug.py#L560-L680).
- Basis: Bounded absence for first-party real experiment execution.
- Confidence: Medium-high.
- Caveats: An external researcher may revise the larger experimental plan, which is not a supported first-party S3 parent closure.

### Absence scope

- Surfaces inspected: CLI arguments/config, target dispatcher, model-backed engineer script, paired evaluator, benchmark reward and demo.
- Plausible first-party paths checked: Adaptive task schedules, shared-resource intervention, human-configured priorities and external decision return.
- Why no material first-party path remains: Available surfaces administer per-batch evaluation and tool budgets; no standing whole-system current view and discretionary governance decision with returned operational effect is implemented.

## S3* — Complementary audit

- State: —
- Function: Ordinary evaluation of an edited harness is not a complementary independent audit of a separate S3 management claim.
- Disturbance / variety regulated: Unfair patch comparisons and invalid claimed patch effects are checked against fresh task identities and matched rewards.
- Decisive decision or feedback right: Evaluator calculates deterministic success/reward and validates task identity; no independent corrective audit actor owns a challenge to ordinary S3 reporting.
- Decision owner: Patch quality/evaluation pipeline, with external environment providing ground-truth task reward; not an independent S3* mandate.
- Supporting / enforcement mechanisms: Task manifest hashes, evaluation logs, score delta, restricted code validator.
- Closure path: Patch → fresh paired target task rerun → reward delta → engineer feedback; no independent audit finding → accountable S3 correction.
- Why this is / is not agent-owned: A legitimate experimental patch test is not automatically independently commissioned whole-current management audit.
- Evidence: [eval_webshop_checkpoint_patches.py L462-625](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L462-L625); [reward_webshop_patch.py L989-1004](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/reward_webshop_patch.py#L989-L1004); [code_runner.py L136-225](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/harness/code_runner.py#L136-L225).
- Basis: Negative at declared experiment recursion, after testing complementary-report candidates.
- Confidence: Medium-high.
- Caveats: Quality validation is genuine first-party functionality, but a different organizational function.
 
### Absence scope

- Surfaces inspected: Trajectory capture, deterministic patch validator, matched target baseline/evaluation, benchmark scoring and release tests.
- Plausible first-party paths checked: Independent target reruns, reward verification and raw evidence inspection challenging patch author claims.
- Why no material first-party path remains: Ground-truth patch tests belong to the ordinary S4 evaluation path; no sufficiently independent audit of routine S3 operating claims and corrective return to S3 is established.

## S4 — Outside-and-then intelligence

- State: A
- Function: Prospectively change the executable target harness from observed external-task failures and return this generated option into later agent capability.
- Disturbance / variety regulated: Task-environment failures and varying external action affordances exceed the previous fixed guidance/guard strategy.
- Decisive decision or feedback right: Configured model-backed engineer generates a new executable code hook from failure trajectories; the first-party patch validator accepts its syntax/effect bounds, and the evaluator installs it for a subsequent operating episode.
- Decision owner: Harness engineer agent in the shipped evaluation workflow chooses adaptation content; first-party code enforces patch restrictions and installs accepted proposal. External model endpoint supplies inference and does not own organizational policy.
- Supporting / enforcement mechanisms: Failure packet, patch schema, AST sandbox, recorded patch path, task-definition overlay, matched identity check, reward delta and persisted artifacts.
- Closure path: Previous target failures → engineer model call → code-hook proposal → normalize/compile → patch.json → patched **new target run** → actual changed guidance/action effect → fresh reward/observation feedback.
- Boundary reachability: The shipped evaluation entrypoint invokes the engineer and target runner; the runner installs generated overlay into the WebShop task where the hooks execute in new environment sessions. The path is not only a paper claim or an offline stored-demo.
- Why this is / is not agent-owned: Without the engineer model, validators can only check/replay supplied code; source-grounded adaptation-option judgment depends on model output rather than deterministic enforcement.
- External distinction: New WebShop/ALFWorld/DBBench environment failure patterns and actual action trajectories, not merely an internal instruction.
- Future / prospective distinction: Earlier observed failure batch informs code installed into a **subsequent** target episode; held-out evaluation documents additional future task applications but reported numerical benefits are not accepted as independent result evidence.
- Adaptation option generated: Executable source code for on_init, make_pre_hint, on_before_action and/or on_post_step hooks in the runtime substrate.
- Path back into current capability / S3: Generated patch → compile_patch_to_task_definition → live harness_overlay → later tool-coupled task operation → measured feedback. Closure returns directly into changed S1 capability; no separate S3 is inferred.
- Evidence: [eval_webshop_checkpoint_patches.py L462-625](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L462-L625); [eval_webshop_checkpoint_patches.py L626-815](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/Relax/examples/harness_r1/eval_webshop_checkpoint_patches.py#L626-L815); [harness_r1_patch.py L357-443](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_patch.py#L357-L443); [harness_r1_patch.py L669-715](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_patch.py#L669-L715); [harness_r1_batch_debug.py L483-496](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_batch_debug.py#L483-L496); [task.py L252-295](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L252-L295); [task.py L469-550](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/tasks/webshop/task.py#L469-L550); [README.md L1-25](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/examples/heldout_generalization/README.md#L1-L25).
- Basis: Source-wired model-proposed option, validated hook installation, next-run operational effect and experimental feedback.
- Confidence: Medium-high for **bounded experimental S4**, not deployed autonomy.
- Caveats: Same-batch rerun is a controlled prospective test, not automatic universal promotion. A generated-only file, a stored demo and offline RL weight training alone would not close S4. No online model experiment was run by this assessor.

## S5 — Policy and identity

- State: —
- Function: No legitimate ultimate-purpose/identity arbitration with returned authority is supplied by the shipped experiment.
- Disturbance / variety regulated: Patch safety, benchmark identity and static experiment constraints bound action, but not conflicts over ultimate mission or ethos.
- Decisive decision or feedback right: Fixed task/patch configurations and sandbox enforce preset limits; no owner arbitrates an identity-level matter at runtime.
- Decision owner: Developer/operator externally chooses experiments; no first-party S5 agent or legitimate parent-governed runtime return path is established.
- Supporting / enforcement mechanisms: Restricted patch schema, sandbox limits, CLI configuration and release licensing.
- Closure path: Static rules → allowed/disallowed patches; absent identity/policy issue → legitimate final authority → returned binding operational policy revision.
- Why this is / is not agent-owned: Restrictions do not originate autonomous ultimate policy; human launching a benchmark is not a parent S5 organization decision.
- Evidence: [harness_r1_patch.py L357-443](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/scripts/harness_r1_patch.py#L357-L443); [code_runner.py L136-225](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/code/life-harness/AgentBench/src/server/harness/code_runner.py#L136-L225); [eval_webshop.sh L1-75](https://github.com/DeepExperience/Harness-R1/blob/2b3f125710ed14ea8a863e6b39a2eb9951cc7181/scripts/eval_webshop.sh#L1-L75).
- Basis: Bounded absence after examining identity and policy candidates.
- Confidence: Medium-high.
- Caveats: Real research governance could exist outside these first-party executable surfaces and cannot be silently included.

### Absence scope

- Surfaces inspected: Patch schema and sandbox, model engineer/task prompts, user-launch configuration, demo, evaluation code and operator-run paths.
- Plausible first-party paths checked: Runtime mission override, identity-level exception, model/parent policy decision returned to later operations.
- Why no material first-party path remains: Examined paths are fixed technical restrictions and experiment knobs with no legitimized identity-level authority and return.

## Recursion

The task episodes are genuine model-operated agent units within a research experiment, but repeated tasks or spawned workers are not by themselves recursively viable divisions. The experiment adaptation loop changes its own operating capability while no S2, S3, S3* or S5 whole-system ownership has been established.

## Variety and escalation

Variable environment observations and model-chosen actions are current operational variety. Failure packets and engineer-generated hook candidates amplify future response variety while AST restrictions attenuate unsafe actions. A failed patch, timeout or score regression is ordinary evaluation feedback, not automatically an algedonic signal or an autonomous S3 policy decision.

## Evidence gaps

- Upstream frozen release verification passed 38/38 tests and Python/shell source checks, but live hosted inference and full benchmark task reruns were **not performed**.
- Proposed S4 is restricted to an experimentally wired patch applied in later target episodes; automatic cross-project production promotion is not established.
- External model provider decisions, research-team priorities, benchmark scoring authority and hosted infrastructure do not inherit first-party VSM rights from source co-location.
- Negative classifications are limited to the inspected standard-distribution boundary and do not claim impossibility for custom deployments.

