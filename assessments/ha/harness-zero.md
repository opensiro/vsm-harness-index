---
harness_id: harness-zero
project_name: Harness-Zero
repository: https://github.com/metaevo-ai/harness-zero
review_ref: 8697d54462e45caaa239b0a999acacd36399435b
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Harness-Zero

## Review boundary

- System in focus: The first-party **supervised rollout harness**, a student coding/task agent plus a separate harnessing-agent reviewer that can replace unexecuted student actions. The system is not the subsequently distilled model by itself.
- Purpose and identity: Produce executable student task trajectories while applying a reference harness's behavioral guidance through a reviewing agent, for later SFT data construction.
- Relevant environment: Harbor task environments and sandboxes, user-selected model providers, the task dataset, local domain components, and downstream training/evaluation services.
- Standard-distribution boundary: The released `harness-zero run-rollout` entry, `HarnessZeroMinisweAgent` with its configured student and `DeepAgentReviewer`, one student trial, and the first-party middleware and trial store. The optional documented `passthrough` baseline is a different, non-reviewing mode.
- Credited operating / distribution surfaces: `src/harness_zero/{cli,rollout,harness,student,teacher,review,store,student_harness}.py`, the standard student/reviewer prompts, and supported training-time Harbor deployment of those modules.
- Adjacent first-party surfaces excluded from ownership: Offline harness-bank evolution/adaptation instructions, SFT dataset builder/trainer, benchmark task sets and scores, test helpers, the later minimal-harness distilled-model deployment, and contributor/CI governance. They do not silently close functions in a supervised trial.
- First-party operating / deployment modes considered: Standard teacher-reviewed supervised rollouts (credited), explicit passthrough baseline (negative contrast), optional student skills/memory/middleware composition, and separate SFT/deployment commands (boundary contrast).
- Recursion level: One supervised student trial and its first-party harness supervisor; batches of concurrent trials are a higher operator-run experiment without evidenced shared autonomous current control.
- Reviewed revision: `8697d54462e45caaa239b0a999acacd36399435b`.
- Observation date: 2026-10-26.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`cli.py` exposes separate `run-rollout`, `build-sft` and `train-sft` commands. The rollout command constructs a Harbor invocation with explicit student/teacher model and task inputs; `HarnessZeroMinisweAgent.build_graph` creates a sandbox-backed student model/tool loop and a separate teacher reviewer. The student agent has an executable sandbox `execute` tool; optional configured skills, memory and tool/middleware factories alter that student harness. The review middleware intercepts **each complete student model response before the action is accepted or executed**, builds a typed `ReviewCandidate`, requests exactly one `PASS`/`REPLACE` from the reviewer, and sends only the accepted response onward. The reviewer is a separate LangChain agent with private reference components, read-only filesystem tools and `submit_review`; its durable context spans turns of the trial. `TrialStore` records candidates, accepted responses and eventual reward. The model providers supply the agent decisions; the repository-owned first-party graph and middleware close their operational path.

The offline harness-bank artifacts and teacher prompt are inputs; SFT/benchmark outputs are *not* a runtime feedback controller that autonomously redeploys or revises this supervised trial. The supervised training-time mode is a genuine agentic harness even though the project's ultimate result is a distilled model run under a minimal harness.

Primary architecture: [CLI](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/cli.py), [Harbor entry/graph](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/harness.py), [student middleware](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/student.py), [teacher reviewer](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/teacher.py), [trajectory storage](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/store.py).

## Operational model

One S1 unit is the student agent performing an environment task over repeated model → executable command → observation turns. The teacher agent is a distinct *current supervising role*, not automatically a second independent S1 unit just because it is a second model process. Its `PASS`/`REPLACE` right changes the student's impending operational action for the whole trial. This supports S3 at the declared trial recursion; it does not establish inter-S1 S2 coordination or a separate complementary S3* audit. The operator selects model/configuration/budget, and Harbor executes sandbox commands, but neither acquires the teacher's discretionary review right from enforcing it.

## S1 — Operations

- State: A
- Function: Execute an assigned environment task through repeated agent-selected actions and observations.
- Disturbance / variety regulated: Task-specific terminal state, tool results, errors and uncertain next actions in the Harbor sandbox.
- Decisive decision or feedback right: The student model selects its next response/tool call based on the current task trajectory; accepted tool observations return to later turns.
- Decision owner: Student LLM actor in the shipped first-party LangChain student graph. The reviewer can alter a pending action but does not replace the student as the continuing operational unit.
- Supporting / enforcement mechanisms: `execute_tool`, Harbor sandbox backend, typed tool schemas, the max-turn guard, optional memory/skills, and trial storage.
- Closure path: Student response → middleware acceptance/replacement → sandbox `execute` tool → observation appended to graph messages → next student turn or final answer.
- Boundary reachability: `create_supervised_miniswe` is invoked directly by the supported `HarnessZeroMinisweAgent.build_graph` runtime and binds the model and executable backend, not a test-only mock.
- Why this is / is not agent-owned: The agent chooses task actions under observed context; deterministic adapters/guards transport and constrain those choices rather than selecting the task strategy.
- Evidence: [student.py `create_supervised_miniswe`, execute tool and middleware](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/student.py), [harness.py graph construction](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/harness.py).
- Basis: explicit code.
- Confidence: high.
- Caveats: No live model/provider evaluation was run; this is source-supported organizational ownership, not task-success evidence.

## S2 — Coordination

- State: —
- Function: No first-party demonstrated attenuation of an inter-S1 conflict at the one-trial recursion.
- Disturbance / variety regulated: Student task errors are local S1 variety; teacher intervention is vertical supervision, not a demonstrated interference between two parallel S1 units.
- Decisive decision or feedback right: No S2-specific discretionary arbitration/feedback between distinct S1 operations is exposed.
- Decision owner: Not established.
- Supporting / enforcement mechanisms: Harbor concurrency arguments, stores, review turn order and candidate IDs are orchestration/serialization, not a conflict-regulating relation among distinct S1 units.
- Closure path: Not applicable to S2.
- Why this is / is not agent-owned: An agent reviewer and agent student exist, but they are different functions in one trial. Their handoff is not proof of S2.
- Evidence: [rollout.py](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/rollout.py), [student.py](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/student.py), [teacher.py](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/teacher.py).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: The broader experiment operator can run several trials concurrently, but no first-party trial-to-trial S2 decision and closure are evidenced within this stated boundary.

### Absence scope

- Surfaces inspected: Trial graph, student and teacher agent roles, Harbor batch command wiring, store and candidate/review sequencing.
- Plausible first-party paths checked: Multi-trial concurrency, reviewer/student exchange, candidate IDs, ordering and shared file surfaces.
- Why no material first-party path remains: No two independent credited S1 units with a specific operational interference and attenuating feedback path are supplied for the one-trial organization; concurrency and message sequence do not establish that function.

## S3 — Inside-and-now control

- State: A
- Function: Current-trial supervision of the student's impending actions for the coherent goal of producing acceptable reviewed trajectories.
- Disturbance / variety regulated: A student candidate action can depart from the teacher's available reference guidance or fail to be an actionable/valid response.
- Decisive decision or feedback right: The teacher agent decides `PASS` or `REPLACE` on each unexecuted response, including a complete substitute action, with trial context and reference components; its decision determines the next accepted operational response.
- Decision owner: `DeepAgentReviewer`'s LLM actor, with first-party reviewer graph and explicit submit tool. Operator-set replacement/turn budgets and typed schemas constrain that discretion; they do not make its selected verdict deterministic.
- Supporting / enforcement mechanisms: `HarnessReviewMiddleware`, typed review submission validation, candidate identity binding, private reference workspace, replacement-budget fallback, and trajectory log.
- Closure path: Candidate/context → reviewer agent `submit_review` → middleware validates and substitutes accepted message → student's next executable action or final response. The teacher's verdict changes live trial operation, rather than merely producing a report.
- Boundary reachability: The standard non-`passthrough` `HarnessZeroMinisweAgent.build_graph` instantiates `DeepAgentReviewer` and passes it to `create_supervised_miniswe`, whose model-call middleware enforces the returned verdict before tool execution.
- Why this is / is not agent-owned: The model chooses the review judgment and replacement content; the middleware enforces the decision. The fallback to unconditional pass on exhausted replacement budget is a configured deterministic guard, not the normal positive owner.
- Whole-system current view: The reviewer receives the student's serialized context delta, candidate and evolving trial context plus private components; this is the one-trial current operational whole, not a global cross-dataset resource view.
- Current-control decision scope: Per-turn admissibility and correction of the student's commitments/actions in the active trial; not autonomous allocation across batches.
- Evidence: [teacher.py reviewer and `submit_review`](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/teacher.py), [student.py `HarnessReviewMiddleware.awrap_model_call`](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/student.py), [harness.py graph wiring](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/harness.py).
- Basis: explicit source and structural role interpretation.
- Confidence: medium-high.
- Caveats: Parent model selection/limits do not independently establish a whole-trial human S3 parent mode. This is supervisory intervention on one trial, not a claim of global experiment S3.

## S3* — Complementary audit

- State: —
- Function: No separate complementary access/audit loop beyond the ordinary in-line supervised review is supplied at this trial boundary.
- Disturbance / variety regulated: Suspicion about student action quality is handled as the primary mandatory teacher review, not as a distinct sporadic audit of routine S1/S3 reports.
- Decisive decision or feedback right: No separate S3*-specific auditor/verdict/return is found.
- Decision owner: Not established for S3*.
- Supporting / enforcement mechanisms: Teacher has private components and traces; `TrialStore` records evidence, but recording and in-line check are not independent complementary audit ownership.
- Closure path: Ordinary S3 review returns to execution; no additional complementary finding-to-current-control path is evidenced.
- Why this is / is not agent-owned: The teacher is an autonomous reviewer for S3 in the credited mode, yet autonomy of a routine verifier does not create an additional S3* function.
- Evidence: [teacher.py](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/teacher.py), [student.py](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/student.py), [store.py](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/store.py).
- Basis: bounded structural absence.
- Confidence: medium.
- Caveats: Private reference material challenges the student's candidates, but the same routine supervisor owns and consumes it. Downstream benchmark evaluation is not automatically a deployed organizational audit.

### Absence scope

- Surfaces inspected: Teacher middleware and graph, trial records, command entrypoints, offline reward/result and SFT interfaces.
- Plausible first-party paths checked: Teacher private component reads, review trace, task reward, evaluation files and optional teacher oracle answer directory.
- Why no material first-party path remains: All observed checks are the normal production review or external/offline evaluation; no distinct complement to routine control with independent finding judgment and returned corrective governance is wired into the trial.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party online prospective environment-model/adaptation loop feeding revised capability into the supervised trial.
- Disturbance / variety regulated: Different tasks and changing benchmark outcomes are potential external learning signals, but are not automatically converted into agent-owned future-oriented adaptation in this mode.
- Decisive decision or feedback right: No shipped S4 adaptation judgment is exercised during the trial.
- Decision owner: Not established; human/offline experiment choices control evolved bank selection and retraining outside the credited runtime.
- Supporting / enforcement mechanisms: Domain-specific harness bank, training commands, reward-tagged trajectories and SFT generation enable offline research but do not automatically revise current trial capability.
- Closure path: No automatic option → S3/current-runtime update path observed.
- Why this is / is not agent-owned: The teacher adapts its immediate response to student context, which is S3/current rather than S4 prospective adaptation. Offline model training is not a first-party real-time S4 owner in this boundary.
- Evidence: [README training sequence](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/README.md), [cli.py separate commands](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/cli.py), [store.py reward materialization](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/store.py).
- Basis: bounded structural absence.
- Confidence: medium-high.
- Caveats: Training/evolution may form another research-system recursion and should not be confused with the supported supervised-trial harness.

### Absence scope

- Surfaces inspected: Run/CLI modes, runtime graph and middleware, trajectory store, harness-bank selection, SFT/training commands and README.
- Plausible first-party paths checked: Teacher accumulating per-trial context, `harness_bank` evolution, score/reward results and training/redeployment flows.
- Why no material first-party path remains: Context use is local current-work regulation; distinct offline stages are operator-initiated and do not close an in-boundary prospective adaptation decision returned to current S3/capability.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/policy decision/return loop in the supervised-trial organization.
- Disturbance / variety regulated: Model/provider/config changes, prompts and replacement ceilings constrain a trial but do not by themselves raise an identity-level issue for legitimate closure.
- Decisive decision or feedback right: Not established for S5.
- Decision owner: The operator owns initial job configuration; no function-specific S5 agent or parent policy-return mechanism is shipped at this declared recursion.
- Supporting / enforcement mechanisms: Prompt files, CLI arguments, max-turn/replacement validation, `PASS`/`REPLACE` schema and Harbor sandbox controls.
- Closure path: No identity-level issue → legitimate parent decision → returned governing action loop is exposed.
- Why this is / is not agent-owned: An agent may decide an ordinary response replacement, but has no evidenced right to redefine the harness's identity or ultimate policy.
- Evidence: [cli.py configuration](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/cli.py), [harness.py setup](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/harness.py), [review.py validation](https://github.com/metaevo-ai/harness-zero/blob/8697d54462e45caaa239b0a999acacd36399435b/src/harness_zero/review.py).
- Basis: bounded structural absence.
- Confidence: medium-high.
- Caveats: This does not deny human governance over the broader research project; that is outside the trial's recursion.

### Absence scope

- Surfaces inspected: Standard CLI/job configuration, prompts, first-party agent graph, review and operator gates, store and training handoff.
- Plausible first-party paths checked: Teacher instructions and candidate judgment, user-selected policies/model/budgets, training confirmation, and Harbor execution constraints.
- Why no material first-party path remains: These regulate ordinary task execution or offline research jobs; none establishes a shipped identity-level issue, legitimate decisive owner and decision return into the ongoing supervised-trial organization.

## Distributed OSS parent arrangement

No public shared organizational parent-governed S3/S4/S5 mode is inferred from repository contributors. Local experiment operator choices are not by themselves organizational parent-return evidence.

## Self-hosted and non-human modes

The user may self-host the supervised rollout with configured model providers and optional student middleware. This makes runtime control configurable, but does not by itself yield an S3/S4/S5 parent modifier. The credited S3 verdict remains with the teacher agent in the standard reviewed mode; explicit passthrough omits that review function rather than adding a parent mode.

## Recursion

At the one-trial recursion the student performs tasks and the teacher supervises each unexecuted candidate. A multi-trial scheduler, offline dataset curation and training/deployment pipeline are adjacent parent/experimental systems; they were not silently credited as functions in this assessment.

## Variety and escalation

Student environmental variety is absorbed via the model/tool loop. Candidate errors and deviations reach the teacher's private reference-based `PASS`/`REPLACE` decision before executable side effects. A replacement budget caps that power; when exhausted, the middleware passes the candidate without review, which is an explicit limitation, not evidence of a higher-level policy or complementary-audit loop.

## Evidence gaps

- No live provider/agent-quality run was performed. Static code and first-party documentation establish wiring, not empirical reviewer accuracy or benchmark reproducibility.
- The exact quality of teacher decisions and whether arbitrary external middleware may implement additional VSM functions are outside this shipped-mode conclusion.
- The S3 mapping is limited to the supervised **one-trial** current-control recursion; it does not claim autonomous current control over a concurrent experimental batch.
