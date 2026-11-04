---
harness_id: sceneevolve-code
project_name: SceneEvolve Code
repository: https://github.com/haoyu-agent/SceneEvolve_Code
review_ref: e6727f248eae77af31902b9c7e6a3fc46449f79f
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# SceneEvolve Code

## Review boundary

- System in focus: the shipped Python scene-reconstruction harness evolution runner, composed from `sceneharness.py`, candidate `policy.solve` loops, Blender renderer, fixed scoring and external Codex proposer; not the research authors' paper organization.
- Purpose and identity: improve model-directed reconstruction of single-view indoor RGB images into Blender scenes by proposing and evaluating changes to the agent policy on a controlled development set.
- Relevant environment: operator-supplied RGB scene dataset and manifests, Qwen multimodal inference, Codex proposer, Blender execution, SSIM/LPIPS/DINOv2 scoring, experiment history and held-out final test.
- Standard-distribution boundary: included baseline policy, `sceneharness.py` search/finalize, `benchmark.py` separate task processes, `runtime.py`, independent scorer, proposer prompt/wrapper, evidence archive, declared config; a real dataset, credentials and Blender/model runtime are required.
- Credited operating / distribution surfaces: [search/controller](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py), [baseline agent policy](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/harnesses/baseline/policy.py), [candidate evaluator](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/benchmark.py), [independent artifact scorer](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/evaluate.py), [candidate instructions](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/prompt-templates/proposer.txt).
- Adjacent first-party surfaces excluded from ownership: README publication claims, benchmark's post-final held-out test as a separately operating organization, paper/arXiv and contributor publication workflow, unattached datasets and external provider organizations. The experiment's **active** development-set evaluator is included because it directly determines ongoing next-round candidates, not merely a developer-side test.
- First-party operating / deployment modes considered: baseline reconstruction loop, Codex-generated two-policy proposals per round, bounded concurrent evaluator jobs and model/Blender budgets, evolution frontier, optional `--rounds` resume, `--test` only after search completion.
- Recursion level: one configured research experiment whose S1 units are scene reconstruction agents and policy-proposer iterations, under an evaluation controller and human experiment owner.
- Reviewed revision: `e6727f248eae77af31902b9c7e6a3fc46449f79f`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`sceneharness.py` snapshots candidate policies, runs `benchmark.evaluate`, archives evidence and updates a retained highest-score frontier. A Codex proposer receives the current parent, development-set scores, full trajectory/evidence locations and visual comparison sheets; it edits two candidate policy directories, subject to fixed-runtime and snapshot-hash restrictions. `inner_loop.py` imports each candidate's `policy.solve`, which uses `Runtime.ask` and `Runtime.execute`: model-generated Python constructs Blender scenes, whose render and execution errors are returned for iterative repair. `benchmark.py` runs separate scene processes, freezes candidate code, limits concurrency and invokes the scorer on artifacts after generation. `evaluate.py` reloads the Blender file and compares the rendered image directly against the reference with SSIM, LPIPS and DINOv2. [Runner](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py); [worker/runtime](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/runtime.py); [scoring](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/evaluate.py).

## Operational model

For each scene the Qwen worker writes and revises Python/Blender output from tool/render feedback until a budget/stop. The experiment controller evaluates all candidate policies on the search split, independently scores their submitted artifacts, and selects the next parent using actual numeric evidence. The Codex proposer then changes the policy files for the next round, with no permission to modify fixed geometry, scoring, budgets or tests. This makes active current control and a complementary evidence-check path, but not an independent inter-worker conflict coordination loop: scenes are separate tasks with bounded concurrency. Policy evolution generalizes from past search evidence, but does not itself establish prospective *outside-and-then* environmental sensing or explicit future scenario choice. [Search lifecycle](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py#L114-L181); [benchmark](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/benchmark.py#L54-L146).

## S1 — Operations

- State: A
- Function: model-directed agent constructs a scene from one RGB image, renders it and iteratively repairs its 3D program; proposer agent also edits candidate operating policies.
- Disturbance / variety regulated: diverse scene geometry, camera ambiguity, image-to-render mismatch, Python/Blender failures and bounded model/render budgets.
- Decisive decision or feedback right: Qwen chooses scene code and revisions based on visual/exception feedback; Codex chooses generalizable policy edits inside designated candidate directories.
- Decision owner: the configured Qwen task model per scene and distinct Codex model for harness policy proposals; the benchmark scheduler does not choose those edits.
- Supporting / enforcement mechanisms: `policy.solve`, `Runtime.ask`, `Runtime.execute`, Blender render results, `Runtime.select`, proposal prompt, immutable-candidate hashes and fixed budget.
- Closure path: reference image → model emits full scene program → Blender render/tool error → image/result in next model message → revised program or `DONE`; proposal model receives failure evidence and outputs edited candidate policies.
- Boundary reachability: baseline policy is shipped and evaluated by `sceneharness.search`; `codex_wrapper.run` supplies the standard two-candidate proposer. Requires user-supplied data, configured model providers and executable Blender/Codex; no full live run claimed here.
- Why this is / is not agent-owned: model selects geometry, code and policy edits; the surrounding deterministic Python loops enforce budgets and evaluate, rather than author the work.
- Evidence: [baseline iterative policy](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/harnesses/baseline/policy.py), [tool and render feedback](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/runtime.py#L36-L105), [proposer model call and guarded edits](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py#L55-L112).
- Basis: first-party source and configured modes; no benchmark reproduced for this assessment.
- Confidence: high for operational model ownership.
- Caveats: paper results and anticipated gains are not observational evidence in this assessment; missing data/model/Blender infrastructure prevents execution.

## S2 — Coordination

- State: —
- Function: no observed function-specific inter-S1 interference mitigation loop spanning separate scene agents or competing candidate policies.
- Disturbance / variety regulated: simultaneous scene workers contend for compute and two policy proposals may derive from one common parent, but their outputs occupy separate job directories and are scored independently.
- Decisive decision or feedback right: fixed `ThreadPoolExecutor` concurrency/budget and candidate snapshots bound execution; no corrective negotiation or shared-resource conflict decision is returned to multiple interacting S1 agents.
- Decision owner: not established; runner mechanically schedules tasks and reads summaries.
- Supporting / enforcement mechanisms: immutable candidate snapshot, per-scene opaque directory, `benchmark.concurrency`, subprocess budget and digest checks.
- Closure path: worker results complete independent scene jobs and are aggregated; the next selected policy is an experiment-wide scoring decision, not inter-worker conflict attenuation.
- Why this is / is not agent-owned: parallelism, shared scores, serial candidate comparison and a common parent alone are generic sequencing/evaluation; no demonstrated cross-cell mutual disturbance is actually sensed and regulated.
- Evidence: [candidate/process isolation and concurrency](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/benchmark.py#L76-L145), [independently evaluated proposals](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py#L124-L156).
- Basis: bounded negative-state source review.
- Confidence: high for independent per-scene path; medium for potential customized policies.
- Caveats: proposal authors are constrained to separate candidate directories but could independently design team logic that is not present in the shipped baseline.

### Absence scope

- Surfaces inspected: default `policy.solve`, benchmark process executor, experiment frontier, proposer and candidate file constraints, `processes.py` and runtime budgets.
- Plausible first-party paths checked: two proposals from one retained parent; per-scene concurrent execution; shared benchmark score table and resource budget enforcement.
- Why no material first-party path remains: the stock agent processes do not communicate or change each other's work; shared execution limits and best-policy ranking do not implement feedback to settle inter-S1 disturbance.

## S3 — Inside-and-now control

- State: C
- Function: the experiment's deterministic controller keeps the current state and selects which active policy governs the next round of operational work.
- Disturbance / variety regulated: multiple competing candidate outcomes, failed reconstructions, interrupted runs, budget/round completion and need to retain a best-known policy.
- Decisive decision or feedback right: compare all evaluated candidate scores, retain best frontier, select that policy as the next proposal parent and freeze search before final testing.
- Decision owner: `sceneharness.py` fixed `max(overall)`/frontier logic, not an autonomous model-based management decision; human sets config/rounds.
- Supporting / enforcement mechanisms: `history.json`, `frontier_search.json`, per-policy and per-scene scores, `evolution_state.json`, completed-round/restart guard and immutable candidate hashes.
- Closure path: each current policy run yields scored summaries → controller compares complete candidates and updates global best → next round clones the retained policy and grants Codex a constrained edit budget; invalid/interrupted states are rejected.
- Boundary reachability: `python sceneharness.py --config ...` runs baseline and rounds, persists/resumes state and applies frontier selection in the stock experiment; needs configured data and execution dependencies.
- Why this is / is not agent-owned: policy-selection right is owned by deterministic code following human scoring policy; the model edits proposals but does not override frontier selection, so `C` is bounded constructor control rather than autonomous S3 `A`.
- Whole-system current view: recorded per-candidate history, overall scores, evidence archive and best frontier cover the active configured search experiment, not arbitrary research organization tasks.
- Current-control decision scope: which candidate policy is retained and used as parent for subsequent trial executions, and whether final evaluation may start.
- Evidence: [history, frontier and round selection](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py#L11-L28), [current comparison/return to proposer](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py#L114-L166), [immutable evaluated snapshots](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/benchmark.py#L54-L65).
- Basis: structural deterministic constructor path.
- Confidence: high for the scored selection mechanism, bounded to research experiment.
- Caveats: cannot infer proactive cross-project agent supervision; this is narrow experiment-level current control, not a generalized S3 hierarchy.

## S3* — Complementary audit

- State: C
- Function: separately inspect the working S1's **actual submitted Blender artifact**, rather than trusting its claimed successful scene reconstruction, and feed the finding into candidate policy selection and rework.
- Disturbance / variety regulated: a model may emit a plausible-looking output or declare `DONE` while the `.blend` is invalid, camera framing is wrong, a render is absent or visual similarity is weak.
- Decisive decision or feedback right: reject missing/invalid projects, load/validate geometry and camera, calculate independent image metrics, set a zero/failure score or measured quality and pass the evidence to the experiment controller.
- Decision owner: an external-to-worker deterministic scorer in a distinct subprocess with fixed benchmark metrics; not an independently discretionary reviewer model.
- Supporting / enforcement mechanisms: `evaluate.py` direct `.blend` header/Blender validation, PNG size checks, SSIM/LPIPS/DINOv2 evidence and separate scoring process; `candidate_evidence` visual comparisons and full trajectory archive.
- Closure path: S1 submits scene output → benchmark invokes independent scorer on scene files and reference image → scored results and comparison sheets become both frontier acceptance/rejection input and the next Codex proposal's actual failure evidence.
- Boundary reachability: every search-split candidate evaluation invokes `evaluate.py` after generation, and `sceneharness.search` uses the score plus archived evidence in the next proposal round. This is not the post-final held-out test alone.
- Why this is / is not agent-owned: direct artifact checking is independent of the authoring model's self-report and implemented outside its process, but fixed scorer/ranking does not exercise independent autonomous audit discretion, hence `C` not `A`.
- Claim being audited: that the generated 3D project is loadable, renders with valid geometry/camera and reconstructs the supplied reference image adequately.
- Ordinary reporting path: the reconstruction agent's own `DONE`, generated `scene.blend`/`final.png` and logged tool outcomes.
- Complementary access path: distinct scoring subprocess reloads the Blender project, compares output pixels/perceptual features with the direct reference, and archives actual rendered images/trajectories for proposer inspection.
- Independence boundary: evaluator modules and formula are fixed and not exposed to the candidate policy or the proposer for editing; the candidate receives only a public RGB task and not the held-out metrics.
- Who acts on findings: deterministic frontier control rejects inferior policies, and the Codex proposer receives scored failure patterns/sheets in the next round to change the operational policy.
- Evidence: [separate scorer invocation and immutable candidate](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/benchmark.py#L85-L145), [direct Blender validation and metrics](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/evaluate.py#L31-L118), [visual evidence and archive](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/evidence.py), [evidence-driven next proposal](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py#L55-L112).
- Basis: structural complementary inspection and corrective return in an active operating evaluation loop.
- Confidence: medium; separate direct-data scorer and return path are explicit, actual model/Blender runs were not executed here.
- Caveats: the benchmark scores quality, not security or all semantics; SSIM/LPIPS/DINOv2 accuracy depends on metric/runtime dependencies. The scoring formula is human-authored and can miss defects.

## S4 — Outside-and-then intelligence

- State: —
- Function: model-generated candidate improvements do not alone establish prospective sensing of **changed external future conditions** and a function-specific strategic adaptation decision.
- Disturbance / variety regulated: unseen 3D scenes and dataset shifts may require different reconstruction skills, tools or capabilities.
- Decisive decision or feedback right: no installed monitor of future external scene/workflow changes, prospective environment interpretation or scenario-specific strategic capability option is observed.
- Decision owner: not established; proposer optimizes current fixed search benchmark based on historical results.
- Supporting / enforcement mechanisms: Codex generalizable-policy prompt, archived failures, two proposed policy variants per round, retained best score and withheld final test.
- Closure path: proposer mutates the next operating policy from current development-set feedback; this is real policy evolution but the evidence is retrospective fixed-benchmark optimization, with no separate outside-and-then external scan/forward option closure.
- Why this is / is not agent-owned: a Codex model owns the edits but the function claim requires the full prospective environmental distinction, not merely a model editing harness files or optimizing for unseen samples of a fixed static task.
- Evidence: [proposer constrained to archived search evidence](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/prompt-templates/proposer.txt), [fixed splits/rounds](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/config.yaml), [final held-out test only after search](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py#L94-L134).
- Basis: bounded negative-state structural review.
- Confidence: medium; policy adaptation is present, distinction from strict outside-and-future S4 is interpretive.
- Caveats: a deployed system that continuously senses changing production scene environments could provide stronger S4 evidence; not part of the reviewed distribution.

### Absence scope

- Surfaces inspected: proposal prompt, evidence archive, development/final splits, search/finalize and policy mutation loop.
- Plausible first-party paths checked: cross-round policy evolution, generalization to held-out images, fixed-score comparisons and new candidate revisions.
- Why no material first-party path remains: all paths optimize the configured benchmark using earlier search results; none identifies evolving external conditions or brings a prospective option into current operations after a separate future-environment judgment.

## S5 — Policy and identity

- State: —
- Function: no observed installed identity/ultimate-policy owner continuously adjudicates or renews organizational purpose and binding policy.
- Disturbance / variety regulated: model assignment, dataset criteria, evaluation authority and experiment identity are fixed by the supplied config/source and user outside the worker.
- Decisive decision or feedback right: operator can edit configs and launch a fresh experiment, but no recurring identity-level policy dispute/decision/return loop is shipped; proposer is explicitly forbidden from changing fixed components.
- Decision owner: not established at the installed autonomous experiment boundary; human researcher owns setup externally.
- Supporting / enforcement mechanisms: fixed runtime hashes, restricted candidate edit scope, source-controlled `config.yaml`, locked scoring and budgets.
- Closure path: static constraints enforce prior user/designer choices, not a demonstrated change-and-return identity policy feedback function.
- Why this is / is not agent-owned: S1 model cannot change test rules, policy foundation or experiment identity; fixed instructions and a researcher's startup command are not enough to infer S5 P.
- Evidence: [fixed runtime guards and candidate edits](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/sceneharness.py#L55-L114), [config model and evaluator boundaries](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/config.yaml), [immutable evaluator](https://github.com/haoyu-agent/SceneEvolve_Code/blob/e6727f248eae77af31902b9c7e6a3fc46449f79f/benchmark.py#L19-L52).
- Basis: bounded negative-state structural review.
- Confidence: medium-high at the local experiment recursion.
- Caveats: a university/research lab may have policy governance; that is external and not a demonstrated product-owned return loop here.

### Absence scope

- Surfaces inspected: runner configuration, proposal constraints, score formula, frozen-runtime enforcement, CLI resume/finalize and research README.
- Plausible first-party paths checked: author-locked budgets and model, researcher-selected datasets, policy files modifiable by Codex and manual experiment restart.
- Why no material first-party path remains: these are fixed initial instructions, local operational adaptation or external researcher decisions; no first-party identity/ultimate-policy deliberation with an accountable returned change is implemented.

## Distributed OSS parent arrangement

Research authors and GitHub maintainers control the upstream repository, which is outside this configured experiment's operating recursion. A local researcher supplies data and credentials, but startup config and CI do not prove an installed S5 parent feedback loop. The evaluator is inside the **runtime experiment** because its measurements directly affect next-round S1 policy selection, unlike unrelated contributor tests.

## Self-hosted and non-human modes

This is a local research orchestration script requiring Qwen, Codex, Blender and metric model weights, not a fully deployed agent service. Deterministic experiment S3 and S3* are scored `C`, not asserted autonomous management. A parallel execution limit is not S2, and held-out evaluation is not evidence of an ongoing S4 forecast. `--test` explicitly requires all configured search rounds to finish, preserving the search/evaluation separation.

## Recursion

Qwen task agents are distinct but independent S1 cells; Codex proposer is a higher-level S1 policy-editing cell. The outer experiment controller retains a best-candidate view and programmatically returns feedback to the next proposal, but no separate fully viable organizational recursion for each candidate is demonstrated. The research institution and external providers are outside this scope.

## Variety and escalation

Model rendering and policy mutations amplify scene-handling variety; strict model/render budgets, immutable runtime, fixed candidate snapshots, scene subprocess isolation and external scoring attenuate evaluation drift. Failed renders get immediate S1 feedback; scored visual evidence supplies later corrective policy feedback. Interruptions are archived without being reused as completed results. Completion of the configured rounds and tests remains human-configured; no operational S4/S5 loop is inferred.

## Evidence gaps

- No model/API, Blender, metric-weight or dataset execution was available for this source-only review; all function evidence is structural.
- `S3* C` is limited to actual artifact validation plus deterministic quality scoring and experimental correction, not a broadly independent code/security auditor.
- The conceptual boundary between benchmark-driven policy evolution and true external/future S4 is narrow; current code shows fixed historical search evidence, not environmental foresight.
- The standard baseline and evaluator are available, but unpublished future Codex-generated candidate policies might contain additional functions and must not be credited at the pinned revision.
