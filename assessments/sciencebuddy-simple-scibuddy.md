---
harness_id: sciencebuddy-simple-scibuddy
project_name: ScienceBuddy / Simple-SciBuddy
repository: https://github.com/Gen-Verse/ScienceBuddy
review_ref: 53177995fd549068cbe25282273bed771e843f50
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: —
---

# ScienceBuddy / Simple-SciBuddy

## Review boundary

- System in focus: Only frozen publicly released `src/simple_scibuddy` runnable research experiment, comprising a task-model-driven Python scientific agent, evidence-assisted proposed modifications of the operating harness, independent validation selection, bounded current phase/model-work control, and alternating harness evolution / on-policy RL model update. Recursion is the standalone harness+model evolution experiment over frozen scientific task distribution, not hosted `science-buddy.io` product.
- Purpose and identity: Solve scientific tasks using an executable Python `run(task, api)` harness and improve that future task capability from public interaction/feedback while preserving private held-out evaluation and controlled model/harness lifecycle.
- Relevant environment: Frozen Train/Val/Test scientific task data, public user/skill/tool observations, optional simulated researcher feedback, private answer-reference verifier, model inference and training GPU resources, candidate Python harness programs, configurable auxiliary improver.
- Standard-distribution boundary: First-party Python `simple_scibuddy` CLI/scientific `run` / episode broker / coevolution loop / candidate generation / validation chooser / host private verifier / model training-worker protocol and exported model handoff. External model inference provider and SkyRL library are dependencies; attributed control/selection code must exist inside frozen repository.
- Credited operating / distribution surfaces: [src/simple_scibuddy/harness/scientific.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/scientific.py); [src/simple_scibuddy/harness/broker.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/broker.py); [src/simple_scibuddy/harness/controller.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/controller.py); [src/simple_scibuddy/coevolve/loop.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/loop.py); [src/simple_scibuddy/coevolve/phase.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/phase.py); [src/simple_scibuddy/coevolve/program.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/program.py); [src/simple_scibuddy/coevolve/feedback.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/feedback.py); [src/simple_scibuddy/coevolve/context.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/context.py); [src/simple_scibuddy/coevolve/evidence.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/evidence.py); [src/simple_scibuddy/coevolve/selection.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/selection.py); [src/simple_scibuddy/coevolve/worker.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/worker.py); [src/simple_scibuddy/coevolve/protocol.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/protocol.py); [src/simple_scibuddy/data/verifier.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/data/verifier.py); [src/simple_scibuddy/cli.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/cli.py); [docs/algorithm.md](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/docs/algorithm.md).
- Adjacent first-party surfaces excluded from ownership: Marketing/paper descriptions of hosted ScienceBuddy, its 224 advertised tools/22 modules, demo video and hosted researcher chat/workspace; `skyrl` Git submodule internals, model artifacts trained elsewhere, server-selected live product tools and paper benchmark scores. Do not infer functionality from `ScienceBuddy` branding or training paper alone.
- First-party operating / deployment modes considered: Runnable baseline scientific harness run, configured `harness_evolve` inner recursion (task model held fixed, candidate generated/evaluated), configured `coevolve` outer loop with SkyRL GRPO worker and exported next model, verified continuation/stop, isolated task container and private verifier. Compare one-off harness evolution vs full multi-round coevolution only where enabled.
- Recursion level: One first-party configured harness/model improvement experiment. S1 is actual scientific task-solving episodes; current-run experiment phase/validation controller governs present task/program candidates and training commitments; independent private verifier checks scientific answers and candidate improvement claims; auxiliary model proposes future version of task-solving harness and return-to-next-run.
- Reviewed revision: `53177995fd549068cbe25282273bed771e843f50`, frozen #186, batch #1648 row 7; verified detached Git object.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The **only assessed first-party OSS application** is `src/simple_scibuddy/`. Hosted ScienceBuddy Preview functionality, its scientific web tools and interactive research product are excluded. The packaged `simple-scibuddy` experiment starts from a frozen task dataset and runnable Python `run(task, api)` scientific harness. The implementation broker executes that user program in a per-task controller runtime and exposes a bounded API for model generation, code execution and submitted answers. It records the actual model input/output, tool results, submissions, errors and feedback. This is model-enabled S1 operational science work, not just a static scoring harness. [src/simple_scibuddy/harness/scientific.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/scientific.py); [src/simple_scibuddy/harness/controller.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/controller.py); [src/simple_scibuddy/harness/broker.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/broker.py).

`coevolve.loop.run` validates identities of frozen train/validation/test, current model and task harness, and initiates an inner harness-improvement phase by `harness_evolve`. A controller allocates batches of Train tasks to the **current** harness and task model, with optional simulated researcher replies selected by a separate auxiliary model from constrained templates. `public_evidence` constructs proposal input from real model/tool episodes, field-validated feedback interpretations and diagnostic outputs **without** leaking reference answers or reward into the improver's proposal prompt. The improver then proposes full replacement Python programs, not only textual recommendations. [src/simple_scibuddy/coevolve/loop.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/loop.py); [src/simple_scibuddy/coevolve/phase.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/phase.py); [src/simple_scibuddy/coevolve/evidence.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/evidence.py); [src/simple_scibuddy/coevolve/program.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/program.py).

The `select_candidates` controller ensures every candidate was proposed before it reveals any validation outcome, preflights structurally valid programs and compares them to the unchanged parent on the same complete held-out Val task IDs and matched configuration. `data.verifier` scores against private reference answers **outside candidate model/harness insight**. Only a candidate with zero evaluation errors and **strictly greater** correct-task count can replace the existing harness; otherwise the parent remains. The result selects an actual Python file for the next task model training / subsequent round. This supports constructor-governed current evaluation/selection and a complementary independent assessment of task accuracy—not an independent model judge taking responsibility for a research paper. [src/simple_scibuddy/coevolve/selection.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/selection.py); [src/simple_scibuddy/coevolve/phase.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/phase.py); [src/simple_scibuddy/data/verifier.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/data/verifier.py).

For the configured outer recursion, `coevolve.loop.run` sends the selected harness and current model checkpoint through a structured training-worker request, validates the worker's exported model artifacts, and uses the new model together with the selected harness in the **next harness-evolution phase**. This is a first-party concrete return from future-capability development to the ongoing capability used in real task episodes. A fixed auxiliary proposer suggests further improvements in future rounds; model training itself is delegated to SkyRL/worker but control, selection and phase handoff remain in the shipped first-party OSS. No claim that an external training run was reproduced in this assessment. [src/simple_scibuddy/coevolve/loop.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/loop.py); [src/simple_scibuddy/coevolve/worker.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/worker.py); [src/simple_scibuddy/coevolve/protocol.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/protocol.py).

Parallel parent/candidate Val batch evaluations use a shared `asyncio.Semaphore(cfg["workers"])` to cap inference/task concurrency; it is a concrete throughput limit but does not alone demonstrate Beer-style coordination in response to an actual oscillating or colliding inter-S1 problem. Model-generated corrections and PRM feedback labels are not promoted into verified independent S3* judgments; they remain public-evidence hypotheses, whereas the host private verifier operates on withheld references and can veto adoption.

## S1 — Operations

- State: A
- Function: A scientific task model solves individual tasks through first-party program-directed generation, tool execution and submission cycles.
- Disturbance / variety regulated: Varied scientific user questions, reasoning uncertainty, tool/answer format failures, changing observations and additional simulated researcher feedback.
- Decisive decision or feedback right: The task model chooses reasoning/output and possible tool calls under a runnable Python program's control, responds to actual observations and submits a scientific answer. A replacement candidate can change harness call/order/context strategies.
- Decision owner: First-party `run(task, api)` program plus connected model-inference runtime; the scientific task's model owns content decisions, and frozen code owns interaction/action feedback.
- Supporting / enforcement mechanisms: API.generate/execute/submit, bounded broker messages, isolated controller sandbox, input/token limits, recorded trajectories and task/verifier datasets.
- Closure path: scientific question → harness/model action → actual execution/tool output → model continuation and submitted answer → recorded result/reply, optionally next conversation turn.
- Boundary reachability: `coevolve.phase.batch` calls `harness.broker.run_episode` with first-party scientific `run(task,api)`; the broker executes the installed Python harness controller, mediates actual model generation/execution/submission and saves episode events. Same path feeds inner and validation tasks.
- Why this is / is not agent-owned: The task model and harness generate contingent actions and explanations from actual task/tool feedback, not a prewritten fixed answer table.
- Evidence: [src/simple_scibuddy/harness/scientific.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/scientific.py); [src/simple_scibuddy/harness/broker.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/broker.py); [src/simple_scibuddy/harness/controller.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/controller.py); [src/simple_scibuddy/coevolve/phase.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/phase.py).
- Basis: Executable first-party task-agent/model-feedback path.
- Confidence: High source path; no model-produced empirical result validated in this review.
- Caveats: RL training and model weights are external dependencies; hosted scientific workspace is excluded.


## S2 — Coordination

- State: —
- Function: No source-backed inter-S1 mutual disturbance or interference-regulation feedback established beyond shared batch throughput caps.
- Disturbance / variety regulated: Different candidate and parent evaluations simultaneously compete for inference throughput, but code does not demonstrate a documented resource collision/oscillation remedied by adaptive S2 balancing.
- Decisive decision or feedback right: A configured semaphore serializes/caps concurrent task batches; no separate decision adapts conflicting S1 operating mandates or co-activity after observing a disturbance.
- Decision owner: Deterministic batch executor and configured worker concurrency limit.
- Supporting / enforcement mechanisms: One shared validation semaphore across parent/candidate evaluations, task-specific isolated runtime and result recording.
- Closure path: Task batch → semaphore admission → episode completion frees token. This is general capacity management, not a demonstrated conflict signal → inter-S1 correction → feedback to changed sibling operations.
- Why this is / is not agent-owned: Pure concurrency limiting without observed inter-operational conflict and responsive attenuation must not be inflated into autonomous or constructor-owned S2.
- Evidence: [src/simple_scibuddy/coevolve/phase.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/phase.py); [src/simple_scibuddy/coevolve/selection.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/selection.py); [src/simple_scibuddy/harness/broker.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/harness/broker.py).
- Basis: Negative bounded causal search of shared execution and parallel candidate evaluation.
- Confidence: Medium; improvement would need documented clash between distinct S1 activity lanes and a meaningful active attenuation return.
- Caveats: The semaphore is a real first-party concurrency guard; exclusion of S2 does not deny resource protection.

### Absence scope

- Surfaces inspected: Candidate task selection, shared validation semaphore, task-isolated execution, workers/hosted inference pool and candidate selection.
- Plausible first-party paths checked: Batch concurrency, candidate test isolation, parent/candidate score comparison, task budget and tool call limits.
- Why no material first-party path remains: Those measures bound task throughput or evaluate proposed harness quality but do not attest conflict-specific inter-S1 coordination closure.


## S3 — Inside-and-now control

- State: C
- Function: Regulate present multi-episode experiment phase and commitments: selected harness/model, Train/Val/Test boundaries, current candidate submissions/validation tasks, task execution budget, training handoff and fail-closed state.
- Disturbance / variety regulated: Unsupported Python candidate programs, incomplete or incomparable validation coverage, evidence leakage into proposals, failed workers, changed frozen data and unstable training/assessment.
- Decisive decision or feedback right: First-party `coevolve.loop.run` schedules current harness learning and RL model updates, freezes dataset identities, advances Train cursor, calls candidate selector, triggers or halts training based on selected improvement and checks worker result before updating current model/harness.
- Decision owner: Deterministic first-party coevolution/controller code and static experimental budget/config. The auxiliary model proposes and task model operates; neither owns whole-experiment now-control.
- Supporting / enforcement mechanisms: Frozen identities, Train cursor, manifests, complete heldout Val match, preflight, selection winner and validation trace, request/result integrity and stop conditions.
- Closure path: Current episodes, candidate readiness and validation outcomes → source controller chooses reject/adopt/stop/train/new model → changes active harness/model and next execution commitments → writes persisted phase history and repeats.
- Whole-system current view: Parent and candidate harness identities, current task-model checkpoint, frozen train/val/test source, worker status, phase counters and comparative evaluation results for the whole experiment.
- Current-control decision scope: Govern current allocation to scientific task batches, compared candidate evaluations, training worker, later phase start and hard stop, not just an individual scientific task.
- Boundary reachability: `coevolve.loop.run` invokes `harness_evolve` and reads `phase_summary["improved"]` before publishing/claiming training requests; `select_candidates` decides adoption from complete Val results, and `validate_result` supplies next model to the next harness phase. This is the runnable experiment entry, not an offline report.
- Why this is / is not agent-owned: Selection/admission/train handoff and return are explicit first-party rules, not an autonomous policy model choosing all current resource mandates; S3=C.
- Evidence: [src/simple_scibuddy/coevolve/loop.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/loop.py); [src/simple_scibuddy/coevolve/phase.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/phase.py); [src/simple_scibuddy/coevolve/selection.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/selection.py); [src/simple_scibuddy/coevolve/protocol.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/protocol.py).
- Basis: Installed full-current experiment and verified phase transitions.
- Confidence: High for deterministic current control, bounded to experiment recursion.
- Caveats: No enterprise lab portfolio governance inferred; SkyRL provides computation inside a structured worker contract.


## S3* — Complementary audit

- State: C
- Function: Independently check proposed candidate claims of improved scientific task performance against privately retained ground-truth evidence, and return veto/admission to current control.
- Disturbance / variety regulated: A model-proposed harness change can hallucinate improvement, accidentally overfit public examples, fail to submit valid answers or contaminate proposed evidence with Val/Test labels.
- Decisive decision or feedback right: Host private-reference verifier grades actual completed Val episodes, requires complete same-task coverage and zero candidate execution errors; candidate replaces parent only on strictly higher correct-task count. No model critic owns that alternative correctness decision.
- Decision owner: First-party deterministic held-out verifier and selection mechanism, with private reference answers withheld from the candidate/proposer; choice is constructor-owned.
- Supporting / enforcement mechanisms: Data verifier, frozen Val task IDs, task-answer collection from episodes, parent/candidate same-model comparison, valid program preflight, private ground-truth isolation.
- Closure path: Model-improver proposed harness improvement → actual unseen held-out Val task rollout and host private-reference scoring → controller rejects/accepts replacement → selected/rejected harness changes future S1 operation and next evolution round.
- Claim being audited: Whether a proposed Python harness program is scientifically valid operationally and *actually improves* scored task success relative to current parent.
- Ordinary reporting path: Improver `propose` with hypothesis and public execution feedback; candidate program runs episodes and submits answers.
- Complementary access path: Independent private reference labels and actual held-out Val execution paths are hidden from proposal inputs; structured host scoring verifies answers under matched tasks/model and full coverage.
- Independence boundary: Model improver cannot read Val/Test oracle labels or score before proposals freeze; controller owns the verifier and may share code authorship but not the model's candidate claims. This is a constructor/host-scored audit, not a separate autonomous model judge.
- Who acts on findings: `select_candidates` computes exact parent/candidate accuracy and checks zero errors; chooses winner or retains parent. The selected source file and its validation receipt feed next harness/model phase through `harness_evolve`/`coevolve.loop`.
- Boundary reachability: `harness_evolve` calls `select_candidates`, which runs every candidate and parent on the Val panel and only writes `status: applied` for strict improvements; the loop uses `selected` harness file for later Train/RL phases. Verified on source, not inference speculation.
- Why this is / is not agent-owned: A separate private oracle determines whether current change claims hold, but comparison/admission logic is deterministic, so S3*=C rather than A. Optional auxiliary PRM feedback interpretation is hypothesis generation, not promoted as an independent auditor.
- Evidence: [src/simple_scibuddy/coevolve/selection.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/selection.py); [src/simple_scibuddy/data/verifier.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/data/verifier.py); [src/simple_scibuddy/coevolve/phase.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/phase.py); [src/simple_scibuddy/coevolve/evidence.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/evidence.py).
- Basis: First-party source-attested independent verifier and binding quality-admission path.
- Confidence: Medium-high for held-out auditable comparison; this is not a human external independent review.
- Caveats: Same dataset owner/controller may govern protocols; performance verification is not proof of every scientific intermediate step. Full Val coverage does not guarantee deployment generalization.


## S4 — Outside-and-then intelligence

- State: A
- Function: Prospective improve the operational harness's future scientific-task capacity by diagnosing externally encountered task environment, proposing alternative complete executable harness designs, testing their future performance and returning an adopted change into actual ongoing S3/S1 control.
- Disturbance / variety regulated: Poor scientific task success across diverse external Train scenarios, recurrent tool errors, context clipping, unreliable reasoning, shifting effectiveness of model/harness combinations after RL updates.
- Decisive decision or feedback right: Independent auxiliary model `Improver` selects evidence-grounded hypotheses and full replacement Python harness programs; source controller tests alternatives on heldout Val and adopts only validated improvements, then uses selected program in next task-model and evolution stages.
- Decision owner: First-party configured auxiliary model owns new harness idea/program content and selects prospective modifications; deterministic S3 selection holds performance/admission rights. No external hosted ScienceBuddy product decisions imported.
- Supporting / enforcement mechanisms: Public episode evidence and validated feedback, explicit program schema, bounded read/propose/skip, program AST safety gate, Train preflight, matched Val selection and actual file replacement, alternating GRPO model update.
- Closure path: Task-environment episodes/feedback and tool failure → auxiliary-model future harness hypotheses/complete Python programs → independent Val testing → S3 select/adopt → actual new `run(task, api)` program guides future task episodes / model training → new model checkpoint returns for next adaptation phase.
- External distinction: The external Train task distribution and observed researcher/tool errors or feedback vary beyond the currently executing task and create empirically distinct demands on the agent harness, from task episode evidence rather than maintainer memory.
- Future / prospective distinction: Candidate changes target the performance of subsequent heldout Val and future Train/Test tasks after the present task episode; the next model/harness cycle is deliberately separate in time from the observed failures.
- Adaptation option generated: The auxiliary model creates executable alternative complete Python run(task, api) harness programs that change prompt construction, tool orchestration, context management and submission handling; independent Val comparison selects or rejects each candidate.
- Path back into current capability / S3: Host S3 selection writes the winner as the active harness file, uses it for subsequent episodes and RL model training, and feeds the exported model checkpoint plus harness to the next coevolution phase, closing the option-to-operation return.
- External and prospective orientation: The future task distribution and observed researcher/tool environment provide performance pressures; the auxiliary model develops design alternatives to change the **agent's operating harness** for tasks beyond current episode, rather than only answering the current scientific question.
- Adaptation options: Full Python `run` replacements modify prompt organization, parsing, tool use, context/memory and control flow; a candidate can be rejected with history or be adopted under strictly better Val accuracy.
- Two-way return with current control: Current episode failures and validation feedback supply improver inputs; the S3 experiment controller accepts a verified candidate, replaces active harness, trains/updates model and schedules the next current task batch with the changed capability. Future cycle feedback re-enters improver.
- Boundary reachability: `coevolve.phase.harness_evolve` gathers source-safe public evidence and calls `coevolve.program.propose`; `selection.select_candidates` can select a different actual `harness.py` file; `coevolve.loop.run` receives returned harness and trains/starts subsequent rounds with it. This is executable first-party adaptation in configured evolution mode, not passive documentation.
- Why this is / is not agent-owned: The auxiliary model autonomously authors new harness program/hypothesis options based on evidence; constructor selection supplies safety/performance gating. Thus adaptive design generation is A within strict model+host composite, not merely tool/config hot reload.
- Evidence: [src/simple_scibuddy/coevolve/program.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/program.py); [src/simple_scibuddy/coevolve/evidence.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/evidence.py); [src/simple_scibuddy/coevolve/improver.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/improver.py); [src/simple_scibuddy/coevolve/selection.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/selection.py); [src/simple_scibuddy/coevolve/loop.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/loop.py).
- Basis: Exact first-party source of longitudinal harness proposals, empirical selection and return-to-operation path.
- Confidence: High that mechanism is implemented; no observed percentage improvement or completed multi-round GPU training asserted.
- Caveats: S4 applies to configured evolution mode, not every isolated task run. Model training stack and third-party CUDA packages are dependencies, and positive score is not a claim of scientific truth outside frozen tasks.


## S5 — Policy and identity

- State: —
- Function: No installed ultimate ethos/identity/policy dispute resolution for the scientific agent organization; predefined scientific task and improvement goals are inherited rather than governed.
- Disturbance / variety regulated: Public/private dataset confidentiality, artifact tampering, invalid program execution, training protocol mismatches and runtime permissions are handled by fixed rules.
- Decisive decision or feedback right: Experiment controller enforces frozen task split, code safety/preflight, model identity checks and strict Val improvement; it does not decide whether maximizing a frozen verifier's task accuracy is the legitimate ultimate purpose or negotiate value conflicts with a parent institution.
- Decision owner: Maintainer / human experiment designer defines science goal and policy/config; first-party loop executes and reports under those constraints.
- Supporting / enforcement mechanisms: Immutable protocol manifests, private oracle data, AST program validation, task-content redaction, reproducible Train cursor, checkpoint hashes and stop reasons.
- Closure path: Fixed experiment rules → operational acceptance/rejection. No independent legitimate-policy conflict → highest-level purpose choice → binding return to S1–S4.
- Why this is / is not agent-owned: Self-improving harness code does not imply self-governing mission/ethos; neither static experiment config nor signed checkpoints supply policy S5.
- Evidence: [src/simple_scibuddy/coevolve/loop.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/loop.py); [src/simple_scibuddy/coevolve/protocol.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/protocol.py); [src/simple_scibuddy/coevolve/program.py](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/src/simple_scibuddy/coevolve/program.py); [configs/defaults.json](https://github.com/Gen-Verse/ScienceBuddy/blob/53177995fd549068cbe25282273bed771e843f50/configs/defaults.json).
- Basis: Bounded negative source assessment of top-level objective and legitimacy ownership.
- Confidence: Medium-high.
- Caveats: External maintainers or research institutions may be ultimate-policy owners beyond this open-source runtime; not automatically scored as parent S5.

### Absence scope

- Surfaces inspected: Dataset/experiment identity freeze, objective/stop/reward configuration, improver schema, validated program contract and model training handoff.
- Plausible first-party paths checked: Progress target/metric, model and harness self-modification, private label access policy and human external configuration.
- Why no material first-party path remains: These operate within prechosen experiment criteria and cannot settle overriding science goals or governing ethos.


## Distributed OSS parent arrangement

The ScienceBuddy repo includes a hosted product description but **only the open Simple-SciBuddy experiment is scored**. It requires configured inference/training infrastructure; GPU/SkyRL workers and private verifiers run under its declared experiment. The human maintainer supplies frozen scientific task distribution and reward policy, which is not automatically the first-party S5 function. Change-of-harness is S4 only when selecting variants for subsequent tasks and returning them to the experiment's S3 state.

## Self-hosted and non-human modes

Standalone scientific tasks can run with model endpoints; full coevolution additionally needs training GPU and a structured worker. In the configured coevolution mode an auxiliary model develops harness changes, which are structurally checked, preflighted and evaluated against the private oracle; only selected programs replace the active operational harness. Outputs from RL are explicitly returned as model checkpoints. This does not imply an online hosted ScienceBuddy UI or a reproduced experimental result in this assessment.

## Recursion

At the experiment level, scientific task episodes are S1; the phase/harness/model controller regulates present batches and training commitments S3; hidden Val oracle evaluation corrects performance/adoption claims S3*=C; an auxiliary model proposes and tests prospective operating harness alternatives with a two-way return to current execution S4=A. There is no demonstrated collision-specific inter-S1 mutual regulation S2 or policy/ethos governance S5.

## Variety and escalation

Proposer/read/skip commands and model-run tool interactions amplify research and design variety. Bounded budgets, private labels, matched scoring, program preflight and strict improvement selection attenuate unsupported adaptations. Failed/unimproved candidates remain recorded without promotion. A training-worker failure stops the bounded phase; a frozen program does not silently rewrite private reference policy.

## Evidence gaps

- Frozen exact public source only; no live model inference, on-policy GRPO GPU model training or empirical task improvement reproduced. Tests and published figures are not substituted for real validated evidence.
- S4=A is **configured experiment-mode** future capability development, not evidence that the external ScienceBuddy Preview adapts its own production organization.
- S3*=C is host private-reference checking of proposed future program **improvement claims**, not autonomous scientific paper review or protected independent human signoff.
- S2=— acknowledges a real shared concurrency semaphore but requires more than generic throughput-limiting to claim disturbance-specific inter-S1 regulation.
- S5=— concerns absence of first-party ultimate policy/ethos resolution; frozen data/identity and procedural restrictions are current-run rules, not governance of legitimate goals.
