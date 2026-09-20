---
harness_id: ai-scientist
project_name: The AI Scientist
repository: https://github.com/SakanaAI/AI-Scientist
review_ref: 1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# The AI Scientist

## Review boundary

- System in focus: the first-party AI Scientist v1 research runtime at pinned revision `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb`, including idea generation/reflection, literature novelty checking, template-based executable experiment iteration, manuscript generation, automated paper review and the supported review-driven improvement mode.
- Purpose and identity: perform template-scoped autonomous scientific discovery from research-idea generation through executable experiments, paper writing and review.
- Relevant environment: user-selected experiment template; template code/baseline; external scientific literature; model-provider responses; local GPU/filesystem/process state; generated experiment metrics/plots and paper artifacts.
- Standard-distribution boundary: code/templates shipped in `SakanaAI/AI-Scientist` at the reviewed revision. External LLM providers, Semantic Scholar/OpenAlex, CUDA/OS/container substrate and third-party packages remain environment/dependencies.
- Credited operating / distribution surfaces: `launch_scientist.py`; `ai_scientist/generate_ideas.py`; `ai_scientist/perform_experiments.py`; `ai_scientist/perform_writeup.py`; `ai_scientist/perform_review.py`; maintained experiment templates used by the launcher.
- Adjacent first-party surfaces excluded from ownership: example generated papers/runs as evidence artifacts, external Drive datasets, community-contributed templates not maintained by the project, repository CI/docs and publication/blog claims not backed by pinned code.
- First-party operating / deployment modes considered: standard paper-generation run, optional parallel independent ideas, standard automated review and the documented/supported `--improvement` mode that applies review feedback and re-reviews an improved manuscript.
- Recursion level: one AI Scientist paper-generation run as the system-in-focus. An idea's experiment/coder loop is operational S1; idea/literature novelty work is S4; the separate paper reviewer is the complementary challenge actor when improvement mode is enabled.
- Reviewed revision: `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb`.
- Observation date: 2026-09-20.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

The top-level launcher generates/refines candidate research ideas from a template and baseline code, optionally checks each idea against Semantic Scholar/OpenAlex for novelty, then runs every novel idea through an experiment workspace copied from the template. An Aider-based coding agent edits `experiment.py`/`plot.py`/notes, `perform_experiments` executes and iterates experiments, and successful work is converted into a LaTeX manuscript.

After writing, a separate review function evaluates the generated PDF through multiple review/reflection samples and emits structured weaknesses/decision fields. In ordinary mode the review is terminal evidence. In the supported `--improvement` mode, however, the review is passed to `perform_improvement(review, coder)`, the manuscript is regenerated, and the improved PDF is reviewed again. The launcher can run several ideas in parallel, but those workers are independent paper attempts rather than a coordinated multi-S1 organization.

## Operational model

For one idea, the operational loop starts from baseline template results and a proposed experiment. The coding agent changes executable experiment/write-up files, runs experiments, observes results/errors and continues until the experiment phase succeeds or fails. Separately, idea generation and novelty checking look outward to existing scientific work and decide which prospective ideas enter the experiment path.

## S1 — Operations

- State: A
- Function: autonomously implement and execute research experiments and produce the resulting scientific artifacts within a maintained experiment template.
- Disturbance / variety regulated: code/runtime errors, differing experimental ideas, metric outcomes, plotting/write-up needs and project-file state.
- Decisive decision or feedback right: choose concrete experiment/code edits and subsequent actions based on the idea, baseline state and observed execution/results.
- Decision owner: the active model-driven Aider coding/experiment agent used by the first-party experiment loop.
- Supporting / enforcement mechanisms: copied per-idea workspace, baseline results, `perform_experiments`, Aider file editing, process execution, notes/logs and bounded experiment flow.
- Closure path: idea/baseline/workspace -> agent edits experiment implementation -> code executes -> result/error evidence returns -> agent chooses further experiment edits or completion.
- Boundary reachability: the loop is invoked by the documented `launch_scientist.py` entrypoint for every novel idea in a standard paper-generation run.
- Why this is / is not agent-owned: Python launcher logic enforces sequencing, but the context-sensitive experiment/code choices are model-agent decisions.
- Evidence: [`launch_scientist.py`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/launch_scientist.py), [`README.md`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md), [`ai_scientist/perform_experiments.py`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/ai_scientist/perform_experiments.py).
- Basis: structural
- Confidence: high
- Caveats: the template supplies substantial prior structure; S1 autonomy is scoped to agentic research execution within that template, not unrestricted scientific-domain autonomy.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination path is established.
- Disturbance / variety regulated: multiple ideas may execute in parallel on different GPUs, but the workers are independent attempts; no concrete cross-S1 conflict/oscillation and attenuation relation is evidenced.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: multiprocessing queue, GPU assignment and independent per-idea workspaces.
- Closure path: scheduling distributes independent jobs; it does not return a coordination decision to change behavior because of inter-S1 interference.
- Why this is / is not agent-owned: resource scheduling is deterministic runtime support and parallelism alone is not S2.
- Evidence: [`launch_scientist.py`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/launch_scientist.py).
- Basis: structural
- Confidence: high
- Caveats: this finding is at the one-run recursion; external cluster schedulers are outside the boundary.

### Absence scope

- Surfaces inspected: multiprocessing/GPU dispatch, per-idea workspace execution, experiment loop, paper review and idea-generation archive.
- Plausible first-party paths checked: parallel ideas, shared GPU availability, previous-idea archive and review aggregation.
- Why no material first-party path remains: the reviewed mechanisms schedule or compare independent attempts; none regulates an identified disturbance between operational units through a dedicated S2 feedback relation.

## S3 — Inside-and-now control

- State: —
- Function: no agent-owned whole-system current-control function is established.
- Disturbance / variety regulated: failures/success at experiment/write-up/review stages change control flow, but stage ordering and stop/advance rules are fixed by the launcher.
- Decisive decision or feedback right: no autonomous actor is shown holding a whole-run current view and discretionary authority over current shared resources, commitments, priorities or constraints.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: launcher stage sequence, exceptions/return values, GPU/process setup, skip/improvement flags and fixed success gates.
- Closure path: deterministic success/failure and CLI configuration drive stage transitions.
- Why this is / is not agent-owned: local agents decide experiments/write-up content, while whole-run control remains scripted.
- Evidence: [`launch_scientist.py`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/launch_scientist.py).
- Basis: structural
- Confidence: high
- Caveats: model reflection inside idea/experiment tasks is not promoted into whole-system S3.

### Absence scope

- Surfaces inspected: launcher, idea generation, experiment execution, write-up, review/improvement and multiprocessing control.
- Plausible first-party paths checked: launcher as supervisor, reviewer score as manager decision, idea reflection as current control and GPU scheduling as resource authority.
- Why no material first-party path remains: all whole-run transition/resource decisions are fixed/scripted; agent decisions remain task-local or prospective.

## S3* — Complementary audit

- State: A
- Function: independently challenge the produced research manuscript and, in the supported improvement mode, return findings into a separate corrective write-up path.
- Disturbance / variety regulated: unsupported/unclear claims, presentation weaknesses, methodological weaknesses and other defects observable by a paper reviewer but not necessarily corrected during ordinary write-up.
- Decisive decision or feedback right: produce a structured peer-review judgment/weakness set over the completed paper; those findings become explicit corrective input in improvement mode.
- Decision owner: the first-party automated paper-review invocation, separate from the Aider writer/coder session being reviewed.
- Supporting / enforcement mechanisms: PDF loading, review ensemble/reflections, persisted `review.txt`, `perform_improvement`, PDF regeneration and second review.
- Closure path: writer produces PDF -> separate reviewer evaluates it -> structured review/weaknesses -> `perform_improvement(review, coder)` returns findings to writer/coder -> revised PDF -> reviewer evaluates the revised artifact again.
- Boundary reachability: `--improvement` is an explicit supported launcher mode using first-party review and improvement functions; it requires no external custom orchestration beyond normal model credentials.
- Why this is / is not agent-owned: the reviewer owns the semantic challenge judgment; the launcher only transfers review findings and enforces the second pass.
- Claim being audited: that the research manuscript adequately presents/supports the generated scientific work at peer-review quality.
- Ordinary reporting path: experiment notes/results -> manuscript generation by the coding/writing agent.
- Complementary access path: a separate review invocation reads the rendered paper and evaluates it with a review-specific prompt/ensemble rather than reusing the writer conversation.
- Independence boundary: writer/coder and reviewer are separate model interactions/roles; review is generated after the artifact is materialized.
- Who acts on findings: the Aider writer/coder through `perform_improvement`, followed by manuscript regeneration.
- Evidence: [`launch_scientist.py`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/launch_scientist.py), [`ai_scientist/perform_review.py`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/ai_scientist/perform_review.py).
- Basis: structural
- Confidence: high
- Caveats: the review primarily audits the manuscript and its represented claims, not an independently rerun experiment; S3* credit depends on the explicit corrective return in improvement mode, not on review scoring alone.

## S4 — Outside-and-then intelligence

- State: A
- Function: generate prospective research options, interrogate external literature for novelty and return novel ideas into current experimentation.
- Disturbance / variety regulated: existing prior work may make a candidate idea non-novel; alternative ideas differ in feasibility/interestingness and should change the next experiment attempted.
- Decisive decision or feedback right: propose/refine research ideas and, during novelty checking, choose literature queries and decide whether each idea is novel enough to enter the experiment set.
- Decision owner: first-party idea-generation/novelty-checking model agents.
- Supporting / enforcement mechanisms: idea reflection archive, Semantic Scholar/OpenAlex search, structured idea JSON, novelty flag and launcher filtering to `novel_ideas`.
- Closure path: template/task context -> agent proposes/refines idea -> external literature searches return evidence -> novelty judgment marks idea -> only novel ideas are dispatched into executable experiments.
- Boundary reachability: idea generation and novelty checking are invoked by the standard launcher unless explicitly skipped; their JSON/novelty outputs directly gate experiment admission.
- Why this is / is not agent-owned: search APIs provide external observations, but query selection, idea refinement and novelty judgment are model-agent decisions.
- External distinction: retrieved titles/abstracts/metadata from Semantic Scholar or OpenAlex.
- Future / prospective distinction: whether a proposed idea is sufficiently novel/feasible/interesting to justify a future experiment.
- Adaptation option generated: structured experiment idea with title, experiment outline and quality ratings.
- Path back into current capability / S3: launcher filters `ideas` to `novel_ideas` and runs each accepted idea through `do_idea` experiment/write-up execution.
- Evidence: [`ai_scientist/generate_ideas.py`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/ai_scientist/generate_ideas.py), [`launch_scientist.py`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/launch_scientist.py).
- Basis: structural
- Confidence: high
- Caveats: template boundaries constrain the option space; they do not negate the literature-facing prospective loop within that space.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy closure is established.
- Disturbance / variety regulated: experiment templates, prompt/task descriptions, model/engine flags and safety/container advice constrain operation, but no identity-level issue is routed to an ultimate authority.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: template `prompt.json`, CLI options, maintained template structure and static safety guidance.
- Closure path: configuration/prompt/template policy directly constrains work; no identity/ultimate-policy decision loop is evidenced.
- Why this is / is not agent-owned: research agents can select ideas/experiments but do not own authority to redefine the system's organizational identity or ultimate policy.
- Evidence: [`README.md`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/README.md), [`launch_scientist.py`](https://github.com/SakanaAI/AI-Scientist/blob/1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb/launch_scientist.py).
- Basis: structural
- Confidence: high
- Caveats: the human choosing a template/topic is an external task-setting act, not a demonstrated first-party S5 parent mode.

### Absence scope

- Surfaces inspected: template/task configuration, idea generation, experiment/write-up/review pipeline, CLI flags and safety/container guidance.
- Plausible first-party paths checked: template prompt as identity, review decision as ultimate authority, human template selection as parent policy and launcher success gates as policy closure.
- Why no material first-party path remains: all are task scope, quality or execution controls. None constitutes identity/ultimate-policy adjudication with authoritative return into operation.

## Recursion

One paper-generation research run is the system-in-focus. Experiment/coding work is S1; idea/literature novelty is S4; paper review becomes S3* only in the first-party improvement mode where findings return to the writer. Parallel idea workers are separate attempts rather than S2-coordinated operational units.

## Variety and escalation

Experiment failures/results return locally to S1. Prospective scientific uncertainty escalates to literature novelty search before an idea is admitted. Manuscript-quality concerns can be challenged by a separate reviewer and, in improvement mode, returned to the writer. No whole-system current-control or identity-level escalation owner was found.

## Evidence gaps

- Structural review only; no new run was executed.
- S3* is mode-dependent: without `--improvement`, automated review is terminal evaluation and would not by itself satisfy the corrective-return threshold.
- External provider behavior and community templates are outside the assessed ownership boundary.