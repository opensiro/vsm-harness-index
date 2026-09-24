---
harness_id: appliedscientist
project_name: TheAppliedScientist
repository: https://github.com/TheAppliedScientist/TheAppliedScientist
review_ref: 762824fd41598370e75588861b48991b0a9fd784
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# TheAppliedScientist

## Review boundary

- System in focus: one first-party TheAppliedScientist scientific-revision run at pinned revision `762824fd41598370e75588861b48991b0a9fd784`, including the Scientist research workspace/agent, experiment and manuscript execution, the Search service/CLI, the separately deployed Reviewer service/API, versioned review submissions and the first-party feedback-to-revision loop.
- Purpose and identity: improve an existing scientific paper through literature investigation, reproducible experiments, manuscript revision, independent peer review and repeated evidence-backed correction.
- Relevant environment: the user-supplied paper/code/reviews/task, external scientific literature, model-provider endpoints, datasets and public code, local compute/filesystem/container state, experiment outputs, and reviewer judgments over the current manuscript.
- Standard-distribution boundary: the shipped `tas`/Scientist/Reviewer/Search components and their documented Docker/native operating paths. External LLM providers, literature corpus contents, third-party datasets/repos, user input artifacts and external publication/evaluation institutions remain environment/dependencies.
- Credited operating / distribution surfaces: top-level `README.md`; `components/ai-scientist/run.sh`; `components/ai-scientist/.claude/CLAUDE.md`; `components/ai-scientist/scripts/submit_for_review.sh`; `components/ai-reviewer/review_api.py`; `components/ai-reviewer/prompts/paper_reviewer_instruction_template.md`; shipped Search integration reached through `/app/search`.
- Adjacent first-party surfaces excluded from ownership: benchmark/evaluation scripts and experiment-compatibility fixtures used to reproduce the accompanying research, integration/smoke tests, CI/release/deployment checks, example task/result artifacts and the published paper's aggregate experimental results. These may corroborate architecture or capability but do not donate VSM ownership to the assessed runtime.
- First-party operating / deployment modes considered: documented all-components Docker deployment; native deployment; default Scientist run with `REVIEWER_MODE=api-external`; supported resume path; user-supplied paper tasks with or without public human reviews. The default external Reviewer service path is the basis for S3*.
- Recursion level: one scientific-revision job is the system-in-focus. The Scientist's research/experiment/manuscript production is operational S1; the separate Reviewer supplies complementary audit; literature-facing prospective option development is S4. Search and Reviewer are support/metasystem services rather than additional S1 units merely because they are separate processes.
- Reviewed revision: `762824fd41598370e75588861b48991b0a9fd784`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

TheAppliedScientist packages three first-party components: Search, AI Reviewer and AI Scientist. `./tas setup search reviewer scientist` plus `./tas up` starts the services, while `./tas run ...` launches one Scientist job from a validated paper-task JSON. The Scientist receives the paper/code/task into an isolated workspace, searches scientific literature, runs and analyzes experiments, writes/compiles the manuscript and maintains versioned submissions and run artifacts.

The ordinary documented Scientist path defaults `REVIEWER_MODE` to `api-external` and points `REVIEW_API_URL` at the separately deployed Reviewer service. The Scientist instructions explicitly prohibit replacing this main loop with the Scientist's own subagent/ensemble path. Submission posts the current manuscript to the Reviewer API, which creates a fresh review task/trajectory and invokes a review-specific agent prompt. That Reviewer independently reads the current paper, searches literature, evaluates novelty/methodology/framing, and returns weaknesses, actionable improvement suggestions and scores.

The Scientist must read the persisted review response, perform meaningful corrective work — including new experiments or analysis when needed — append a rebuttal, and submit another version. Each `submit_for_review.sh` call freezes the paper, experiment code, figures and reviewer communication into a numbered snapshot before the working workspace continues. The standard research instructions tell the Scientist to repeat this cycle until reviewer questions are satisfactorily addressed.

## Operational model

The primary transformation is scientific revision: turn an existing paper/code/task into a stronger evidence-backed manuscript. The Scientist autonomously chooses literature queries, experiment designs and implementations, analyses results, edits the manuscript and decides how to address review findings within operator-provided goals and constraints. Deterministic scripts provide isolation, task validation, submission/versioning, service transport and artifact persistence but do not choose the substantive scientific edits.

## S1 — Operations

- State: A
- Function: perform the scientific work that directly produces the system's intended outcome — literature-informed experiments, analyses and manuscript revisions.
- Disturbance / variety regulated: incomplete or weak evidence in the starting paper, experimental/setup failures, alternative baselines/datasets/metrics, observed results, code/runtime errors, manuscript gaps and corrective review feedback.
- Decisive decision or feedback right: choose which concrete experiments, analyses, code changes and manuscript edits to perform in order to improve the current research submission.
- Decision owner: the autonomous Scientist model actor executed by the first-party Scientist runner.
- Supporting / enforcement mechanisms: validated paper-task JSON, isolated Harbor/native workspace, container/host process execution, artifact synchronization, compile/version scripts, timeout/resource configuration, Search API transport and submission persistence.
- Closure path: task/paper/code plus current evidence and any prior reviewer feedback → Scientist chooses and performs literature/experiment/manuscript actions → execution/results/artifacts return to the Scientist → Scientist updates the working research artifact and proceeds to review or another operational iteration.
- Boundary reachability: `./tas run` is the documented standard entrypoint; it stages the Scientist instructions and workspace and invokes the configured model-driven Scientist directly in both Docker and native modes. No benchmark or paper-evaluation actor is needed for ordinary S1 reachability.
- Why this is / is not agent-owned: the runner constrains environment, timeout and persistence, but it does not choose the substantive experiment or revision. Removing the Scientist actor while retaining scripts/services removes the research decision right.
- Evidence: [`README.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/README.md); [`components/ai-scientist/run.sh`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/run.sh); [`components/ai-scientist/.claude/CLAUDE.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/.claude/CLAUDE.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: user inputs establish the paper/task boundary and external model endpoints supply the actor implementation; S1 autonomy is scoped to first-party orchestration of the Scientist within those constraints.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation is established at the reviewed job boundary.
- Disturbance / variety regulated: the standard job exposes one primary Scientist operational unit. Search is an information service and Reviewer is the complementary-audit path; background experiment processes do not by themselves establish distinct autonomous S1 units with an interaction-generated oscillation/conflict.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: background experiment execution, service endpoints, job/workspace isolation, artifact syncing, timeouts and sequential review/version transitions.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: component/process plurality transports or supports one research operation and its metasystemic audit/intelligence functions. No reviewed path makes a discretionary coordination response to a specific inter-S1 disturbance.
- Evidence: [`README.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/README.md); [`components/ai-scientist/run.sh`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/run.sh); [`components/ai-scientist/.claude/CLAUDE.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/.claude/CLAUDE.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: optional experiment subprocesses and separately deployable services are implementation topology, not evidence of peer S1 coordination.

### Absence scope

- Surfaces inspected: top-level deployment/run documentation, Scientist runner and research instructions, Search/Reviewer service relation, experiment/background-task instructions, review submission/versioning and resume paths.
- Plausible first-party paths checked: Search/Scientist communication, Scientist/Reviewer communication, concurrent/background experiments, artifact synchronization, job isolation and service health/orchestration.
- Why no material first-party path remains: the reviewed relations supply information, audit or execution support to one scientific operation. None evidences two distinct S1 units plus a specific interaction-generated conflict/oscillation and a coordination response that changes subsequent peer behavior to attenuate it.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous whole-system current-control function is established at the reviewed job boundary.
- Disturbance / variety regulated: the runner tracks one job, timeout, environment, resume artifacts and service endpoints, while the Scientist manages task-local research work; no separate actor is shown regulating current shared commitments/resources/priorities across operations on behalf of the whole system.
- Decisive decision or feedback right: not established for S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `run.sh` timeout/environment/resource setup, task validation, workspace creation, artifact sync, resume state, process/service health and deterministic submission/version sequencing.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the Scientist makes operational research choices and the Reviewer makes complementary audit judgments. Deterministic runner/service machinery enforces prior configuration but does not own discretionary whole-system current-control decisions.
- Evidence: [`components/ai-scientist/run.sh`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/run.sh); [`components/ai-scientist/.claude/CLAUDE.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/.claude/CLAUDE.md); [`components/ai-scientist/scripts/submit_for_review.sh`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/scripts/submit_for_review.sh).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: reviewer rejection can force corrective work, but that relation audits the produced research artifact and is mapped under S3*, not whole-system resource/commitment control.

### Absence scope

- Surfaces inspected: `tas`/Scientist run path, job/workspace lifecycle, timeout/GPU/runtime configuration, resume/artifact sync, research instructions, reviewer submission/polling and service setup.
- Plausible first-party paths checked: Scientist as supervisor, Reviewer decision as manager intervention, runner resource setup, resume logic, timeout handling and service orchestration.
- Why no material first-party path remains: none supplies an autonomous actor with a whole-system current view and discretionary authority over shared operational resources, commitments, priorities or constraints. The reviewed control surfaces are task-local agent decisions or deterministic enforcement.

## S3* — Complementary audit

- State: A
- Function: independently challenge the Scientist's current manuscript/research claims through a separately deployed fresh reviewer with its own evidence-gathering path, then return actionable findings into another scientific revision and re-review.
- Disturbance / variety regulated: unsupported or overstated claims, missing/obsolete related work, weak experimental design/baselines, methodological confounds, framing/presentation defects and other research weaknesses that can survive the producing Scientist's ordinary execution and self-inspection.
- Decisive decision or feedback right: produce the substantive peer-review judgment over the current submission — strengths/weaknesses, concrete requested improvements, questions, methodology/positioning critique, scores and accept/reject recommendation.
- Decision owner: the autonomous Reviewer model actor executed inside the first-party AI Reviewer service; in the documented main loop this actor is reached through `REVIEWER_MODE=api-external`, separate from the Scientist's driving session.
- Supporting / enforcement mechanisms: separate Reviewer HTTP service, fresh temporary review task/trajectory, review-specific prompt, Search CLI/literature index, async submit/poll protocol, review extraction, persisted `reviewer_communications/response.md`, version snapshots and deterministic submission/version bookkeeping.
- Closure path: Scientist produces current experiments/manuscript → `submit_for_review.sh` sends the current LaTeX to the separate Reviewer API → a fresh Reviewer trajectory reads the paper and gathers independent literature/methodology evidence → Reviewer returns weaknesses/actionable suggestions/judgment → response is frozen into the submission and read by the Scientist → Scientist performs experiments/analysis/manuscript corrections and writes a rebuttal → Scientist resubmits → the Reviewer service runs a fresh review over the revised manuscript; the loop repeats until questions are satisfactorily addressed.
- Boundary reachability: the documented all-components setup installs/starts Reviewer and Scientist together; `run.sh` defaults to `REVIEWER_MODE=api-external` and localhost Reviewer endpoint; the Scientist's shipped instructions say this external-review path is mandatory for the main loop and explicitly prohibit replacing it with subagent/ensemble review. The positive path is therefore part of the supported standard distribution rather than an adjacent evaluation harness.
- Why this is / is not agent-owned: the Reviewer actor makes the semantic audit judgment; HTTP polling, versioning and persistence only transport/record it. Under the counterfactual owner test, retaining those mechanisms without the Reviewer leaves no equivalent independent assessment of the manuscript.
- Claim being audited: that the current research manuscript and its represented experimental contribution are sufficiently sound, novel, supported and positioned for scientific submission.
- Ordinary reporting path: Scientist-produced experiment code/results/figures and the manuscript generated from its own research loop.
- Complementary access path: a separate Reviewer service receives the materialized current manuscript, launches a new review trajectory, independently searches the literature and re-reads exact paper evidence under a review-specific procedure.
- Independence boundary: the default main loop uses a separately deployed API reviewer rather than the Scientist session; each API job constructs a new temporary review task/trajectory from the current LaTeX, and the review procedure has its own search/evidence rules. Previous review history is not needed to make the new audit judgment.
- Who acts on findings: the Scientist actor, which is instructed to address reviewer weaknesses/questions through new experiments, analysis, literature work and manuscript edits before resubmission.
- Evidence: [`README.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/README.md); [`components/ai-scientist/run.sh`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/run.sh); [`components/ai-scientist/.claude/CLAUDE.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/.claude/CLAUDE.md); [`components/ai-scientist/scripts/submit_for_review.sh`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/scripts/submit_for_review.sh); [`components/ai-reviewer/review_api.py`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-reviewer/review_api.py); [`components/ai-reviewer/prompts/paper_reviewer_instruction_template.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-reviewer/prompts/paper_reviewer_instruction_template.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: optional `subagent`/`ensemble` implementation paths exist in the submission script, but the documented Scientist main-loop configuration explicitly selects the separate `api-external` reviewer. S3* credit is based on that supported mode and its corrective/re-review closure, not on generic reviewer vocabulary or the accompanying paper's performance claims.

## S4 — Outside-and-then intelligence

- State: A
- Function: interrogate the external scientific environment and develop prospective research/revision options that alter the current experiment and manuscript trajectory.
- Disturbance / variety regulated: relevant prior work, missing citations/positioning, external baselines and methods, newly identified research gaps, and uncertainty about which additional experiments or analyses would best strengthen the future submission.
- Decisive decision or feedback right: choose literature investigations and, from the resulting external evidence, choose prospective experiments, analyses or framing changes to incorporate into the next research state.
- Decision owner: the autonomous Scientist model actor operating under the first-party research process; the separate Reviewer can additionally surface external gaps through its own literature search, but S4 credit does not depend on treating the Reviewer judgment as S4.
- Supporting / enforcement mechanisms: first-party Search API/CLI over the scientific corpus, downloaded literature/notes, paper task context, mutable experiment/manuscript workspace and deterministic scripts for execution/compilation/versioning.
- Closure path: current paper/results expose an unresolved research/positioning need → Scientist searches and reads external scientific literature → external distinctions reveal related work/gaps/baselines/options → Scientist chooses a prospective experiment/analysis/framing change → performs that work in the current workspace → new evidence/manuscript state becomes present operational capability and is available to the next review/revision cycle.
- Boundary reachability: the shipped Scientist instructions make literature review and repeated `/app/search` use part of the standard research process, including revisiting literature throughout the run; top-level documented tasks explicitly direct the Scientist to use Search to find important gaps and run evidence-backed improvements.
- Why this is / is not agent-owned: Search provides external observations, but the Scientist chooses queries, interprets scientific distinctions and selects what future experiment/revision option to execute. Removing the Scientist while retaining Search leaves no equivalent prospective adaptation choice.
- External distinction: literature/related-work/baseline/method evidence returned from the Search service and full papers.
- Future / prospective distinction: which additional experiment, analysis, citation/positioning change or research correction should be attempted in the next version rather than merely describing current state.
- Adaptation option generated: a concrete evidence-backed experiment/analysis/manuscript-positioning change for the next research iteration.
- Path back into current capability / S3: the selected option is executed by the Scientist in the mutable experiment/manuscript workspace, changing the present research artifact and evidence set before the next submission. This closure exists even though no separate autonomous S3 owner is established at the reviewed boundary.
- Evidence: [`README.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/README.md); [`components/ai-scientist/.claude/CLAUDE.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/.claude/CLAUDE.md); [`components/ai-reviewer/prompts/paper_reviewer_instruction_template.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-reviewer/prompts/paper_reviewer_instruction_template.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic experiment iteration and review-driven correction are not the basis for S4. The credited function is specifically the externally oriented literature/environment inquiry that develops prospective scientific options and returns them into subsequent research capability.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy closure is established at the reviewed job boundary.
- Disturbance / variety regulated: the user-supplied `Task`, paper/code/reviews, `What_NOT_To_Do`, provider/model choices, timeouts and static research-quality rules constrain the run, but no identity- or ultimate-policy-level issue is routed to a legitimate authority and returned as a governing decision.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not established.
- Supporting / enforcement mechanisms: validated task JSON, static Scientist/reviewer instructions, provider configuration, timeout/resource settings, safety/security guidance and submission quality requirements.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the Scientist can alter experiments and manuscript content but is not given authority to redefine the system's identity or ultimate policy; the Reviewer owns quality challenge, not constitutional authority. Human task definition before a run is ordinary external task-setting, not a demonstrated first-party S5 parent loop.
- Evidence: [`README.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/README.md); [`components/ai-scientist/run.sh`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/run.sh); [`components/ai-scientist/.claude/CLAUDE.md`](https://github.com/TheAppliedScientist/TheAppliedScientist/blob/762824fd41598370e75588861b48991b0a9fd784/components/ai-scientist/.claude/CLAUDE.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: operator/provider configuration bounds autonomy but does not by itself establish S5 or `P`.

### Absence scope

- Surfaces inspected: paper-task schema/examples, top-level setup/run interface, Scientist instructions, provider/runtime configuration, review procedure, resume/versioning and static quality/safety constraints.
- Plausible first-party paths checked: `Task` and `What_NOT_To_Do` as policy, reviewer accept/reject as ultimate authority, provider/model selection, resume/feedback input, timeout/resource configuration and static Scientist/reviewer instructions.
- Why no material first-party path remains: these are run scope, quality, environment or execution constraints. None supplies a runtime identity/ultimate-policy issue path to legitimate authority with a returned decision that governs subsequent operation at the chosen recursion.

## Recursion

One scientific-revision job is the system-in-focus. The Scientist is the primary operational S1. Search contributes to the outside-and-then S4 conversation; Reviewer supplies S3* complementary audit. Their separation into services does not by itself make each component a recursive viable system. No lower-level unit was credited as a full recursive VSM merely because it runs in a separate process/container.

## Variety and escalation

Operational experiment/code/manuscript variety is primarily absorbed by the Scientist. External scientific variety is amplified through Search and converted into prospective S4 options. Manuscript/research-quality uncertainty can take the complementary Reviewer path; findings return to the Scientist for correction and another fresh review. Runtime/setup failures are handled by deterministic retry/fallback/configuration mechanisms or operator intervention. No independent whole-system S3 or identity-level S5 escalation owner was established.

## Evidence gaps

- Structural repository review only; no new TheAppliedScientist run was executed for this assessment.
- The accompanying publication and its aggregate iterative-review results were deliberately excluded from ownership classification; they belong to the separate non-normative capability-evidence layer if this repository is later admitted canonically.
- External model-provider behavior and external literature/data contents are outside the assessed ownership boundary.
