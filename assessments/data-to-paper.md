---
harness_id: data-to-paper
project_name: data-to-paper
repository: https://github.com/Technion-Kishony-lab/data-to-paper
review_ref: 81df14c4b9600466e645c3b2b336cc54daa3df3a
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# data-to-paper

## Review boundary

- System in focus: the first-party `data-to-paper` scientific-research framework at pinned revision `81df14c4b9600466e645c3b2b336cc54daa3df3a`, including hypothesis-testing step runners, code-generation/execution/debug loops, literature/novelty/goal refinement, paired performer/reviewer conversations, product/provenance machinery and the shipped Copilot human-review surface.
- Purpose and identity: automate end-to-end data-driven scientific research from raw data through hypothesis formation, literature search, analysis code execution, interpretation and manuscript production while preserving backward traceability and optional human guidance.
- Relevant environment: user-provided datasets and optional research goals; public scientific literature; model-provider responses; local Python/R execution and generated files; analysis outputs, tables/figures and manuscript artifacts; human scientist feedback in Copilot mode.
- Standard-distribution boundary: the installable `data_to_paper` package and shipped application/research-type code at the reviewed revision. Model providers, literature services, scientific packages and the human scientist are external substrate/environment/Parent unless a supported parent mode explicitly returns decisions through the framework.
- Credited operating / distribution surfaces: `src/data_to_paper/research_types/hypothesis_testing/`; `src/data_to_paper/base_steps/`; `src/data_to_paper/run_gpt_code/`; `src/data_to_paper/conversation/`; `src/data_to_paper/interactive/`; product/data-chaining and manuscript-production paths reachable from the shipped CLI/application.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests as such, supplementary papers/demos, publication metadata, contributor workflows and external scientific-package behavior not owned by the framework.
- First-party operating / deployment modes considered: fully autonomous Autopilot runs and documented Copilot runs with human review/guidance; hypothesis-testing workflow with literature/novelty, code, interpretation and writing stages.
- Recursion level: one data-to-paper research project/run as the system-in-focus. Performer/code agents and reviewer agents are internal actors; the human scientist is Parent in Copilot mode.
- Reviewed revision: `81df14c4b9600466e645c3b2b336cc54daa3df3a`.
- Observation date: 2026-09-20.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

`HypothesisTestingStepsRunner` owns a typed research-stage sequence covering data description/exploration, goal formation, literature review, novelty assessment, hypothesis-testing planning, data-analysis code, tables, interpretation, literature review for writing, section-by-section manuscript writing and compilation. The goal/novelty path is not a one-way pipeline: literature-derived novelty assessment can set `re_goal` and return the workflow to the goal stage for another research-goal proposal.

Operational code work is performed through first-party code conversers/debuggers and `CodeRunner`; generated code is executed, failures/output problems become feedback, and the model revises until a valid code-and-output product exists. Separately, `ReviewDialogDualConverserGPT` runs performer and reviewer as distinct LLM conversations. Reviewer feedback is returned to the performer for a complete rewrite until approval or a configured round bound. The same interaction surface supports LLM-only review, LLM-first human review and human review with optional LLM assistance.

## Operational model

The framework maintains explicit products between scientific stages. Agent outputs therefore change subsequent research context rather than merely produce chat text. Analysis code is generated, executed and debugged against actual project data/files; manuscript values are linked backward through data/code products. In Autopilot, model agents own goal/hypothesis, review and revision choices within configured constraints. In Copilot, the application can expose those products/reviews to the human scientist, whose feedback replaces or supplements reviewer feedback and is returned into the same revision loop.

## S1 — Operations

- State: A
- Function: autonomously perform the environment-facing scientific work needed to transform project data and research state into executable analyses and research artifacts.
- Disturbance / variety regulated: heterogeneous datasets, generated-code errors, unexpected outputs/files, statistical-analysis requirements, intermediate product state and manuscript construction requirements.
- Decisive decision or feedback right: choose and revise analysis/code/content actions in response to current project products, execution results and validation/reviewer feedback.
- Decision owner: the active first-party performer/code-writing agents in the hypothesis-testing workflow.
- Supporting / enforcement mechanisms: stage runner, `CodeRunner`, debugger conversers, code extract/check logic, output requirements, product store, data chaining and configured iteration bounds.
- Closure path: current scientific products/data -> agent proposes code/content action -> first-party runner executes/materializes it -> output/error/product state returns -> agent revises or advances.
- Boundary reachability: these paths are the shipped hypothesis-testing research workflow invoked by the installable application/CLI, not benchmark-only examples.
- Why this is / is not agent-owned: runtime and guardrails execute/check code, but the context-sensitive analysis/content choice and revision remain model-agent decisions.
- Evidence: [`README.md`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/README.md), [`steps_runner.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/research_types/hypothesis_testing/steps_runner.py), [`request_code.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/base_steps/request_code.py).
- Basis: structural
- Confidence: high
- Caveats: safety/validity guardrails are supporting enforcement; they are not credited as the owner of the operational scientific choices.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination path is established at the reviewed recursion.
- Disturbance / variety regulated: the workflow contains multiple performer/reviewer roles and research stages, but no concrete interference, conflict or oscillation among distinct S1 units is identified and attenuated by a dedicated coordination relation.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: typed stage transitions, product passing, paired conversations, deterministic sequencing and rewind/retry utilities.
- Closure path: these mechanisms sequence work and transmit review feedback; they do not close a cross-S1 interference-regulation loop.
- Why this is / is not agent-owned: interacting agents and state transfer are real, but the reviewed paths are production/review dependencies rather than S2-specific conflict attenuation.
- Evidence: [`steps_runner.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/research_types/hypothesis_testing/steps_runner.py), [`dual_converser.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/base_steps/dual_converser.py).
- Basis: structural
- Confidence: high
- Caveats: generic conversational interaction is not promoted to S2 without a disturbance-and-attenuation witness.

### Absence scope

- Surfaces inspected: research stage runner, performer/reviewer conversations, product passing, code/debug loops, human-review/rewind surfaces and manuscript construction.
- Plausible first-party paths checked: dual-agent review dialogs, director/performer roles, stage sequencing, rewinds and code-review loops.
- Why no material first-party path remains: each path produces, validates, revises or sequences a product; none identifies inter-S1 interference and a coordination relation specifically intended to attenuate it.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous whole-system inside-and-now control function is established at the reviewed recursion.
- Disturbance / variety regulated: stage completion, retries, rewinds, project parameters and review rounds constrain current work, but no first-party autonomous actor is shown holding a whole-project current view plus broad authority over shared resources/commitments/priorities.
- Decisive decision or feedback right: stage flow and retry bounds are primarily encoded in deterministic runner logic and project parameters; local reviewers control product acceptance rather than organization-wide current control.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: `DataStepRunner`/`HypothesisTestingStepsRunner`, stage enums, product readiness, retry/rewind helpers, project parameters and UI actions.
- Closure path: configured stage/retry conditions alter control flow mechanically; no discretionary whole-system S3 owner is evidenced.
- Why this is / is not agent-owned: model agents make local scientific/product decisions, while the broader workflow sequence is framework-defined.
- Evidence: [`steps_runner.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/research_types/hypothesis_testing/steps_runner.py), [`README.md`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/README.md).
- Basis: structural
- Confidence: high
- Caveats: Copilot oversight and rewind are not automatically S3 parent governance; the reviewed evidence does not establish a parent current-control right over the whole project's resources/commitments at the required threshold.

### Absence scope

- Surfaces inspected: stage runner, project parameters, director/performer roles, Copilot controls, rewind/replay, code-review and writing-review loops.
- Plausible first-party paths checked: stage runner as supervisor, human oversight/rewind as parent S3, reviewer acceptance as control and director selection as whole-system authority.
- Why no material first-party path remains: the strongest controls are deterministic lifecycle rules or local product-review decisions. They do not establish whole-project current control with the Profile's resource/commitment/priority authority.

## S3* — Complementary audit

- State: A
- Function: provide a separate challenge channel that reviews scientific/code/writing products and returns concrete corrective feedback before those products are accepted.
- Disturbance / variety regulated: plausible-but-wrong analysis outputs, code/result problems, weak hypotheses/plans, writing defects and other product claims that ordinary performer generation may miss.
- Decisive decision or feedback right: independently approve a product or issue constructive concerns that force another performer revision cycle.
- Decision owner: the separate reviewer LLM conversation in `ReviewDialogDualConverserGPT` and review-specific subclasses; in code paths, review agents inspect executed outputs/code products separately from the generating/debugging conversation.
- Supporting / enforcement mechanisms: separate `ConversationManager`, review termination phrase, max review rounds, product extraction/checks, code-review prompts and rewind utilities.
- Closure path: performer produces valid candidate -> reviewer receives the candidate/background -> reviewer approves or supplies concerns -> concerns are appended to the performer conversation with explicit correction request -> performer rewrites/revises -> review repeats.
- Boundary reachability: the review dialog base class is reused by goal, planning and manuscript-writing review steps in the shipped hypothesis-testing workflow; code review is also embedded in the standard code-product path.
- Why this is / is not agent-owned: the reviewer is a separate agent conversation and owns the semantic approve/challenge judgment; deterministic loop code only routes/enforces that judgment.
- Claim being audited: that a current scientific product/code result is adequate/correct enough to become accepted workflow state.
- Ordinary reporting path: performer response plus normal generated/executed product state.
- Complementary access path: separate reviewer conversation receives the product and relevant background/output context; code review can inspect created output contents.
- Independence boundary: reviewer has its own conversation manager/role and does not share the performer's assistant role; review feedback is generated independently and then returned.
- Who acts on findings: the original performer/code-writing agent revises the product in the next cycle.
- Evidence: [`dual_converser.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/base_steps/dual_converser.py), [`request_code.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/base_steps/request_code.py), [`steps_runner.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/research_types/hypothesis_testing/steps_runner.py).
- Basis: structural
- Confidence: high
- Caveats: this classification is based on the explicit independent reviewer/revision loop, not on traceability or guardrails alone.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: use external literature/novelty evidence to develop or revise future research direction and return the selected direction into the current experimental plan, with both autonomous and Copilot parent-governed modes.
- Disturbance / variety regulated: existing literature may make a candidate goal non-novel, external findings may change relevant hypotheses, and a human scientist may judge the proposed future direction inadequate.
- Decisive decision or feedback right: in Autopilot, research/novelty agents judge literature-derived novelty and generate/refine the goal/hypothesis; in Copilot, human review can replace/supplement reviewer feedback and require revised research products.
- Decision owner: autonomous research/reviewer agents in base mode; human scientist in the supported Copilot parent mode for the reviewed future-direction decision.
- Supporting / enforcement mechanisms: literature-search agents, `NoveltyAssessmentReview`, `ReGoalReviewGPT`, stage return to `GOAL`, human-review application interactions, product storage and plan handoff.
- Closure path: external literature -> novelty/goal review -> autonomous or parent judgment -> if inadequate, workflow returns to goal generation/refinement -> resulting goal/hypothesis/testing plan feeds data analysis and later research stages.
- Boundary reachability: literature/novelty/goal refinement is part of the shipped hypothesis-testing runner, and README plus `HumanReviewType`/review interaction code expose Copilot human feedback through the same first-party workflow.
- Why this is / is not agent-owned: the base mode closes without human direction through model-agent novelty/refinement decisions; the separately supported Copilot mode intentionally transfers the relevant review/judgment right to the human and returns that decision into workflow state.
- External distinction: retrieved scientific literature and most-similar-paper evidence.
- Future / prospective distinction: whether the current research goal/hypothesis is novel/appropriate enough to warrant future experimentation.
- Adaptation option generated: revised research goal/hypothesis and downstream hypothesis-testing plan.
- Path back into current capability / S3: failed novelty sets `re_goal` and returns to `ScientificStage.GOAL`; accepted/revised goal then feeds planning, code analysis and manuscript stages.
- Evidence: [`steps_runner.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/research_types/hypothesis_testing/steps_runner.py), [`dual_converser.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/base_steps/dual_converser.py), [`README.md`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/README.md).
- Basis: structural
- Confidence: high
- Caveats: the parent modifier is limited to the explicit Copilot review/guidance path; generic ability to configure a research goal is not itself the reason for `(P)`.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | novelty/goal/research agents | literature-derived novelty/goal distinction | novelty/goal judgment can regenerate the goal and accepted output proceeds into plan/analysis | [`steps_runner.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/research_types/hypothesis_testing/steps_runner.py) |
| Parent (`P`) | human scientist in Copilot review mode | human judges a reviewed prospective research product inadequate | human feedback replaces/supplements AI review and is returned to the performer/revision loop before later stages | [`dual_converser.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/base_steps/dual_converser.py), [`README.md`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/README.md) |

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy closure is established.
- Disturbance / variety regulated: project parameters, research goals, human feedback and methodological guardrails constrain work, but no identity-level dispute is routed to an ultimate authority and returned as governing organizational policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: startup/project parameters, user research goal, coding guardrails, reviewer prompts and human-review UI.
- Closure path: these controls constrain local research behavior directly; no identity/ultimate-policy issue -> authoritative decision -> returned policy loop is evidenced.
- Why this is / is not agent-owned: neither autonomous agents nor the Copilot human are shown resolving an identity-level policy issue at this recursion.
- Evidence: [`README.md`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/README.md), [`steps_runner.py`](https://github.com/Technion-Kishony-lab/data-to-paper/blob/81df14c4b9600466e645c3b2b336cc54daa3df3a/src/data_to_paper/research_types/hypothesis_testing/steps_runner.py).
- Basis: structural
- Confidence: high
- Caveats: human accountability/oversight is important but is not automatically VSM S5.

### Absence scope

- Surfaces inspected: project startup/parameters, goal-setting, human review, guardrails, literature/novelty loops, stage runner and manuscript review.
- Plausible first-party paths checked: user-supplied research goal as identity, Copilot oversight as ultimate policy, code guardrails as policy and reviewer approval as final authority.
- Why no material first-party path remains: all are task/method/quality controls; none establishes a system-identity or ultimate-policy conflict with authoritative closure into subsequent operation.

## Recursion

The assessment treats one scientific project/run as the viable system. Individual code/writing/research agents are operational/adaptive subactors. The Copilot human is a Parent only where the first-party human-review path explicitly gives that actor a function-specific decision and returns the decision into subsequent workflow.

## Variety and escalation

Execution variety is handled by agent generation, code execution/debugging and reviewer loops. Scientific future variety is handled through literature/novelty/goal refinement. In Copilot mode unresolved quality/future-direction judgments can escalate to the human reviewer; feedback is injected back into the same product-revision path. No identity-level escalation loop was found.

## Evidence gaps

- This review is structural and did not execute a new end-to-end research run.
- The package is broad; negative S2/S3/S5 states are scoped to shipped hypothesis-testing and interactive control surfaces inspected at the pinned revision, not a claim that downstream users cannot program those functions.
- Backward data chaining is scientifically important provenance evidence but is not independently promoted into a VSM function without the corresponding organizational decision/feedback loop.