---
harness_id: autoresearchclaw
project_name: AutoResearchClaw
repository: https://github.com/aiming-lab/AutoResearchClaw
review_ref: be4ba4755bf1b52220f25e13b2293b5956590070
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# AutoResearchClaw

## Review boundary

- System in focus: one first-party AutoResearchClaw research run at pinned revision `be4ba4755bf1b52220f25e13b2293b5956590070`, from topic decomposition and literature-facing hypothesis work through executable experiments, research decisions, paper production, peer review and revision.
- Purpose and identity: autonomously transform a research topic into an evidence-backed research artifact/paper while retaining first-party paths for experiment execution, result-conditioned pivot/refine decisions, external-literature intelligence and review-driven correction.
- Relevant environment: user-supplied research topic/configuration; OpenAlex, Semantic Scholar, arXiv and other literature sources; model providers; filesystem/process/container/GPU substrate; external packages and datasets; optional parent/operator guidance.
- Standard-distribution boundary: the `researchclaw` runtime, maintained prompt/configuration surfaces and shipped experiment/sandbox paths in `aiming-lab/AutoResearchClaw` at the reviewed revision. External model providers, literature services, OS/container/GPU substrate, datasets and third-party packages remain environment/dependencies.
- Credited operating / distribution surfaces: `researchclaw/pipeline/runner.py`; `researchclaw/pipeline/executor.py`; `researchclaw/pipeline/stage_impls/_literature.py`; `_synthesis.py`; `_experiment_design.py`; `_execution.py`; `_analysis.py`; `_review_publish.py`; `researchclaw/llm/__init__.py`; and the documented standard CLI/run configuration.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests, ARC-Bench evaluation material, website copy, contributor/project governance, development-only code-review notes and modules not shown reachable from the assessed runtime path.
- First-party operating / deployment modes considered: ordinary autonomous pipeline operation; executable sandbox/docker and maintained domain-agent experiment modes; the supported separate `llm.reviewer_model` review mode; optional HITL guidance/gates only as caveats unless their decisive organizational ownership is independently established.
- Recursion level: one research project/run is the system-in-focus. Experiment/code execution is operational S1; the project-level research-decision stage is S3; independent review with corrective return is S3*; literature/synthesis/hypothesis work is S4. Debate personas or model-panel participants are subcomponents inside those functions, not automatically distinct S1 units.
- Reviewed revision: `be4ba4755bf1b52220f25e13b2293b5956590070`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

AutoResearchClaw implements a staged research pipeline rather than a single prompt/response wrapper. The standard flow moves from research framing and literature collection through synthesis and hypothesis generation, experiment design/code/resource planning, executable experiment runs, result analysis, an explicit research-decision stage, paper writing, peer review and revision. The runtime persists artifacts between stages and can recursively roll back after a project-level `PIVOT` or `REFINE` decision.

The operational experiment path is substantive. Stage 12 executes generated experiment code in sandbox/docker modes or invokes maintained domain-agent sandboxes, captures structured results/metrics and returns execution evidence for later analysis. After result analysis, Stage 15 presents the accumulated analysis and automated diagnosis to a model-driven research decision. A parsed `REFINE` or `PIVOT` is not merely descriptive: `runner.py` versions affected stage state and recursively re-enters the pipeline at the mapped rollback target. This creates a whole-project current-control loop distinct from task-local experiment actions.

The repository also separates complementary review when configured. Stage 18 builds an independent reviewer client from `llm.reviewer_model`, records author/judge provenance and reviews the materialized draft together with actual experiment evidence. Stage 19 then consumes those reviews as explicit corrective input to the writer and produces a revised paper. The fallback that reuses the generator model does not by itself establish independence; the positive S3* state is based on the first-party separate-reviewer mode and its closed corrective return.

Prospective intelligence is likewise explicit. Earlier stages construct model-selected literature search strategies, collect external papers, synthesize knowledge cards/gaps and generate hypotheses; the resulting hypothesis artifact becomes input to experiment design and therefore changes what the present operational pipeline attempts. Optional multi-model debate/tournament mechanisms strengthen option generation but are treated as internal S4 machinery, not as S2 coordination merely because several model roles participate.

Primary evidence:

- [`README.md`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/README.md) — documented end-to-end autonomous pipeline, external literature, experiment, review and HITL modes.
- [`researchclaw/pipeline/stage_impls/_execution.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_execution.py) — executable experiment/resource path and returned run evidence.
- [`researchclaw/pipeline/stage_impls/_analysis.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_analysis.py) — model-driven project research decision over proceed/pivot/refine using result/diagnosis evidence.
- [`researchclaw/pipeline/runner.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/runner.py) — rollback/re-entry closure for project-level decisions.
- [`researchclaw/pipeline/stage_impls/_review_publish.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_review_publish.py) and [`researchclaw/llm/__init__.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/llm/__init__.py) — separate reviewer construction, provenance and review-to-revision path.
- [`researchclaw/pipeline/stage_impls/_literature.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_literature.py), [`researchclaw/pipeline/stage_impls/_synthesis.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_synthesis.py), and [`researchclaw/pipeline/stage_impls/_experiment_design.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_experiment_design.py) — external-literature search, synthesis/hypothesis generation and return into experiment design.

## Operational model

A project begins from a user-supplied research topic and configuration. Model-driven stages decompose/search/synthesize the domain and propose hypotheses. Those prospective artifacts feed experiment design and code/resource planning. The runtime then executes actual experiment code or a maintained domain-agent sandbox, captures metrics/results and analyzes them.

The project does not then advance only by fixed sequencing. Stage 15 lets a model decide whether the current evidence warrants proceeding, refining the experiment or pivoting; the runner converts that semantic decision into a rollback/re-entry action and subsequent operations change accordingly. Once a paper draft exists, a separately configured reviewer model can inspect the draft plus experiment evidence; its findings return to the paper-revision model before later quality/export stages.

## S1 — Operations

- State: A
- Function: autonomously execute the concrete research/experiment work needed to turn the selected research direction into empirical artifacts and a paper.
- Disturbance / variety regulated: differing hypotheses/designs, generated code, runtime/dependency failures, hardware/time constraints, experiment outputs/metrics, domain-specific sandbox behavior and paper-production needs.
- Decisive decision or feedback right: choose concrete experiment implementation/actions and continue the research work in light of generated design and observed run state/results.
- Decision owner: first-party model-driven research/code/domain agents used by the standard pipeline; deterministic sandbox/runner code transports and executes their selected work.
- Supporting / enforcement mechanisms: generated experiment plans/code, resource schedules, sandbox/docker/domain-agent executors, run directories, captured stdout/stderr/metrics/results and bounded retry/refinement machinery.
- Closure path: hypothesis/design -> agent-generated executable work -> sandbox/domain-agent execution -> metrics/errors/artifacts -> analysis/refinement inputs -> subsequent agent action or project decision.
- Boundary reachability: the executable experiment path is part of the documented 23-stage standard pipeline and is reached before result analysis/research decision.
- Why this is / is not agent-owned: deterministic Python decides how to launch and persist execution, while substantive research/code choices are produced by model-driven agents and their results feed later decisions.
- Evidence: [`README.md`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/README.md); [`researchclaw/pipeline/stage_impls/_execution.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_execution.py); [`researchclaw/pipeline/stage_impls/_experiment_design.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_experiment_design.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: simulated/fallback paths exist, but the standard distribution also exposes substantive executable autonomous modes; S1 credit is not based on template fallbacks.

## S2 — Coordination

- State: —
- Function: no material first-party S2 path regulating an identified disturbance between distinct autonomous S1 units at the declared one-project recursion is established.
- Disturbance / variety regulated: model panels, debate personas, specialist agents, experiment tasks and resource-plan entries may coexist, but the reviewed evidence does not establish them as distinct S1 operational units whose interaction creates a concrete conflict/oscillation that a dedicated coordination relation attenuates.
- Decisive decision or feedback right: none established for an inter-S1 coordination disturbance.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: staged sequencing, model debate/tournament, task dependencies, schedules, persisted artifacts and shared project state.
- Closure path: these mechanisms compose or sequence work inside S1/S3/S4, but no identified inter-S1 disturbance -> coordination judgment -> changed later behavior of distinct S1 units loop is established.
- Why this is / is not agent-owned: multi-agent vocabulary and debate are not sufficient; the decisive S2 functional witness is absent at the chosen recursion.
- Evidence: [`researchclaw/pipeline/stage_impls/_synthesis.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_synthesis.py); [`researchclaw/pipeline/stage_impls/_execution.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_execution.py); [`researchclaw/pipeline/runner.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/runner.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: a higher recursion that treats specialist/domain agents as separately accountable operations could require a different assessment boundary.

### Absence scope

- Surfaces inspected: pipeline stages/runner, model-panel debate/tournament, resource planning, specialist/domain-agent experiment paths, persisted project state and HITL/collaboration-adjacent surfaces visible from the standard run.
- Plausible first-party paths checked: debate between model roles; specialist-agent composition; task dependencies/resource schedules; shared artifacts; parallel/domain execution; reviewer/writer interaction.
- Why no material first-party path remains: these are composition, evaluation, scheduling or subfunctional relations; evidence does not tie them to attenuation of a concrete interference/oscillation between distinct first-party S1 operational units with a returned coordination decision.

## S3 — Inside-and-now control

- State: A
- Function: make a whole-project current-control judgment after experiment analysis and intervene in the active research trajectory by proceeding, refining or pivoting.
- Disturbance / variety regulated: insufficient/degenerate experiment quality, diagnosis findings, weak ablations, failed requirements, repeated empty metrics and the need to decide whether the present project should continue as-is or reopen earlier work.
- Decisive decision or feedback right: choose `PROCEED`, `REFINE` or `PIVOT` from project evidence, thereby deciding whether current commitments remain or which earlier operational stage is reopened.
- Decision owner: the model-driven Stage 15 research-decision actor (or the model-driven requirements gate in maintained domain-agent modes).
- Supporting / enforcement mechanisms: result analysis, experiment diagnosis, quality/ablation hints, decision parsing/structured artifacts, deterministic rollback map, versioned rollback state, pivot budget and recursive pipeline re-entry.
- Closure path: experiment executes -> result analysis/diagnosis -> model evaluates current project evidence -> `PROCEED/REFINE/PIVOT` -> runner maps the decision to continuation or rollback target -> subsequent pipeline operation changes -> new results return into later analysis/decision.
- Boundary reachability: Stage 15 and runner rollback handling are part of the standard pipeline rather than repository-only test/governance machinery.
- Why this is / is not agent-owned: Python enforces rollback mechanics and limits, but the context-sensitive organizational choice among proceed/refine/pivot is produced by the model from whole-project evidence.
- Evidence: [`researchclaw/pipeline/stage_impls/_analysis.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_analysis.py); [`researchclaw/pipeline/runner.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/runner.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic max-pivot/forced-proceed rules bound agent discretion; they are enforcement around rather than replacement of the ordinary model-owned current-control judgment.

## S3* — Complementary audit

- State: A
- Function: independently challenge the research manuscript against actual experiment evidence and return findings into a corrective revision path.
- Disturbance / variety regulated: unsupported claims, draft-quality defects, methodology/evidence mismatches, weak baselines/ablations and discrepancies between manuscript claims and actual executed experiment evidence.
- Decisive decision or feedback right: produce a review judgment/weakness/action set from a reviewer path separate from the author model and make those findings corrective input to the subsequent paper revision.
- Decision owner: the separately configured first-party reviewer/judge model in `llm.reviewer_model` mode.
- Supporting / enforcement mechanisms: experiment-evidence collection, reviewer-specific prompt bank, independent reviewer client construction, author/judge provenance recording, persisted `reviews.md`, `review_provenance.json` and Stage 19 review-conditioned revision.
- Closure path: writer produces draft -> separate reviewer receives draft plus experiment evidence -> review findings/provenance are persisted -> Stage 19 supplies findings to the revision actor -> revised paper is produced for later quality/export stages.
- Boundary reachability: `build_reviewer_llm` and the Stage 18/19 path are first-party standard-distribution code; no custom external orchestrator is needed beyond configuring a distinct reviewer model/provider-compatible credential path.
- Why this is / is not agent-owned: the reviewer owns the semantic challenge judgment; deterministic code collects evidence, records provenance and transfers findings to the reviser.
- Claim being audited: that the generated manuscript accurately and adequately represents/supports the executed research and satisfies review-quality expectations.
- Ordinary reporting path: experiment/results -> analysis -> paper draft by the author/generator path.
- Complementary access path: Stage 18 separately reads the materialized draft and independently collected experiment evidence using a reviewer-specific client/prompt.
- Independence boundary: when `llm.reviewer_model` differs from the author model, the repository records the differing author/judge identities and marks the reviewer independent; fallback to the generator is explicitly non-independent.
- Who acts on findings: Stage 19 paper-revision agent through the first-party review-conditioned revision path.
- Evidence: [`researchclaw/pipeline/stage_impls/_review_publish.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_review_publish.py); [`researchclaw/llm/__init__.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/llm/__init__.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: S3* is mode-dependent. If no separate reviewer is configured, Stage 18 falls back to the generator and that fallback alone does not establish the independence required here. The positive state is based on the first-party separate-reviewer mode.

## S4 — Outside-and-then intelligence

- State: A
- Function: sense the external research environment, synthesize gaps/options and generate prospective research hypotheses that alter what the current project attempts next.
- Disturbance / variety regulated: changing/competing prior literature, uncertainty about research gaps/novelty, alternative hypotheses and future experiment options.
- Decisive decision or feedback right: choose literature-search strategy/queries, synthesize external findings into prioritized gaps and generate/select prospective hypotheses that become the input to experiment design.
- Decision owner: model-driven search/synthesis/hypothesis actors, optionally strengthened by first-party debate/tournament and reviewer/judge modes.
- Supporting / enforcement mechanisms: external literature APIs/web-fetch adapter, persisted search plans/candidate papers/knowledge cards, synthesis artifacts, multi-perspective/debate/tournament machinery, novelty checking and hypothesis artifacts.
- Closure path: topic/problem context -> model develops search strategy -> external literature returns evidence -> model synthesizes gaps -> model generates prospective hypotheses -> `hypotheses.md` feeds Stage 9 experiment design -> resulting operation executes in later stages.
- Boundary reachability: literature, synthesis and hypothesis stages are part of the normal documented pipeline and directly precede experiment design.
- Why this is / is not agent-owned: external APIs supply observations, while the context-sensitive search, synthesis and option-generation judgments are model-owned and their outputs change the experiment path.
- External distinction: retrieved scientific papers/metadata and evidence from external literature services.
- Future / prospective distinction: which gap/hypothesis is worth turning into a subsequent experiment rather than how to execute an already-fixed experiment.
- Adaptation option generated: model-authored research hypotheses and corresponding experiment direction.
- Path back into current capability / S3: the hypothesis artifact is consumed by experiment design and becomes executable operational work; later Stage 15 can further pivot/refine the resulting project.
- Evidence: [`researchclaw/pipeline/stage_impls/_literature.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_literature.py); [`researchclaw/pipeline/stage_impls/_synthesis.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_synthesis.py); [`researchclaw/pipeline/stage_impls/_experiment_design.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/pipeline/stage_impls/_experiment_design.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the novelty-check report is non-blocking at this revision, so S4 credit does not depend on treating that score as a hard gate; the closure is the broader literature -> synthesis -> hypothesis -> experiment-design loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the one-project runtime boundary.
- Disturbance / variety regulated: topic/configuration, target venue, quality criteria, prompts, HITL guidance and runtime limits constrain research, but they are task, quality, execution or adaptation controls rather than an evidenced identity/ultimate-policy adjudication loop.
- Decisive decision or feedback right: none established for redefining or authoritatively reconciling the system's organizational identity/ultimate policy.
- Decision owner: none established for runtime S5.
- Supporting / enforcement mechanisms: user topic/configuration, prompt banks, quality gates, CLI flags, reviewer settings and optional HITL guidance.
- Closure path: these inputs constrain or redirect research work directly; no identity-level issue -> legitimate ultimate authority -> authoritative policy decision -> returned governance of subsequent operation loop is evidenced.
- Why this is / is not agent-owned: research agents can choose hypotheses, current project interventions and reviews, but those are S1/S3/S3*/S4 judgments rather than authority to redefine the organizational identity or ultimate policy of the research system.
- Evidence: [`README.md`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/README.md); [`researchclaw/config.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/config.py); [`researchclaw/cli.py`](https://github.com/aiming-lab/AutoResearchClaw/blob/be4ba4755bf1b52220f25e13b2293b5956590070/researchclaw/cli.py).
- Basis: structural negative search.
- Confidence: high.
- Caveats: the user is a parent task setter and can intervene, but Methodology 0.3.6 does not promote ordinary task selection, approval or guidance into S5=P without an identity/ultimate-policy function and closure.

### Absence scope

- Surfaces inspected: standard CLI/configuration, prompt banks, pipeline stage graph, research-decision path, review/quality gates, HITL guidance/approval surfaces and project/governance separation.
- Plausible first-party paths checked: topic selection as identity; target conference/quality policy as S5; human final approval; reviewer verdict as ultimate authority; prompt/configuration policy; repository governance.
- Why no material first-party path remains: each checked path governs task scope, research quality, current control, adaptation or development governance rather than runtime identity/ultimate-policy authority at the declared recursion.

## Recursion

The assessment treats one research project/run as the viable system in focus. Concrete experiment/code/domain-agent work forms S1. Stage 15 regulates the whole active project as S3. A separately configured reviewer supplies S3* challenge and corrective feedback to the writer. Literature-facing synthesis/hypothesis generation supplies S4. Model panels/debate roles remain subcomponents of those functions; their multiplicity is not enough to redefine the recursion as a coordinated population of autonomous S1 units.

## Variety and escalation

Operational variety first returns through experiment metrics/errors and local refinement. Evidence about experiment quality then reaches the project-level research-decision actor, which can proceed, refine or pivot and thereby reopen earlier work. External scientific variety enters through literature search/synthesis before hypotheses become experiments. Manuscript/evidence discrepancies can be challenged through the separate-reviewer mode and returned into paper revision. No identity-level escalation owner was established.

## Evidence gaps

- Structural review only; no new research run was executed.
- S3* depends on the supported separate-reviewer configuration. The generator fallback is not counted as independent audit.
- Optional HITL/Co-Pilot surfaces are real first-party mechanisms, but this assessment does not publish `(P)` modifiers because the reviewed evidence did not establish a sufficiently clean, separate parent-owned S3/S4 organizational closure beyond ordinary guidance/approval at the declared boundary.
- The repository contains additional self-evolution, collaboration and benchmark/evaluation surfaces. They were not promoted into S2/S5 or stronger states unless reachable first-party runtime evidence established the relevant function at the chosen recursion.