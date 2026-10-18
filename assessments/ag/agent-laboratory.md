---
harness_id: agent-laboratory
project_name: Agent Laboratory
repository: https://github.com/SamuelSchmidgall/AgentLaboratory
review_ref: d9017d90e329112d2a80b7712f37ee9094d2cd27
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
autonomy_s3_star: ?
autonomy_s4: A(P)
autonomy_s5: —
---

# Agent Laboratory

## Review boundary

- System in focus: the first-party Agent Laboratory research workflow at pinned revision `d9017d90e329112d2a80b7712f37ee9094d2cd27`, including `LaboratoryWorkflow`, PhD/postdoc/professor/ML/SW agents, literature search, planning, data preparation, executable ML experiments, interpretation, report generation/refinement, state saves and the documented Co-Pilot mode.
- Purpose and identity: assist a human researcher with an end-to-end research workflow spanning literature review, research planning, experimentation, interpretation and report writing while allowing autonomous or human-guided operation.
- Relevant environment: researcher topic/notes and compute constraints; arXiv/AgentRxiv literature; Hugging Face data; model-provider responses; local Python execution/files; experiment outputs and manuscript artifacts; human feedback in Co-Pilot mode.
- Standard-distribution boundary: code/configuration shipped in `SamuelSchmidgall/AgentLaboratory` at the reviewed revision. External model providers, arXiv/Hugging Face services, the human researcher and underlying OS/compute are environment/Parent unless a first-party parent loop explicitly returns their decisions.
- Credited operating / distribution surfaces: `ai_lab_repo.py`; `agents.py`; `mlesolver.py`; `papersolver.py`; `tools.py`; first-party YAML configuration and state-save paths used by the documented workflow.
- Adjacent first-party surfaces excluded from ownership: AgentRxiv as a broader collaborative research system beyond the local workflow except where its retrieval is called by Agent Laboratory, project website/paper claims, repository CI/docs and external service internals.
- First-party operating / deployment modes considered: standard autonomous workflow and YAML-configured `copilot_mode`; local workflow checkpoint/resume; optional AgentRxiv retrieval where called by the workflow.
- Recursion level: one LaboratoryWorkflow research project/run as the system-in-focus. Specialized agents are internal actors; the human researcher is Parent in Co-Pilot mode.
- Reviewed revision: `d9017d90e329112d2a80b7712f37ee9094d2cd27`.
- Observation date: 2026-09-20.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

`LaboratoryWorkflow` executes ordered research phases: literature review, plan formulation, experimentation (data preparation and running experiments), then results interpretation/report writing/report refinement. It instantiates distinct PhD, postdoc, professor, ML-engineer, SW-engineer and reviewer roles, shares accepted products among them, and persists workflow checkpoints.

Literature review is agent-driven over arXiv/optional AgentRxiv. Plan formulation alternates postdoc and PhD reasoning until a plan is submitted. Data preparation has SW- and ML-engineer agents exchange task-specific dialogue, run generated code and react to execution failures; experiment execution delegates to `MLESolver`. Report generation uses `PaperSolver`. A separate `ReviewersAgent` produces three peer-review perspectives over the plan/report. `report_refinement()` contains a path that can send those reviews back and recursively reset the workflow to planning/experimentation, but the pinned constructor hard-codes `review_override = True` and default counters cause the automated branch to choose completion rather than corrective return. That reachability ambiguity is preserved rather than promoted to S3*.

## Operational model

The research run converts a topic and notes into literature state, a research plan, executable data/experiment code, interpreted results and a manuscript. Agent decisions are bounded by phase prompts and max-step/solver budgets. In Co-Pilot mode, phase products are presented to the human; rejection prompts for explicit notes, resets agent state and reruns the phase with those notes. This parent path is materially relevant to future research direction during literature/plan phases.

## S1 — Operations

- State: A
- Function: autonomously perform environment-facing research work across data preparation, executable experimentation, interpretation and report production.
- Disturbance / variety regulated: data/source-selection problems, generated-code errors, experiment outcomes, model responses, interpretation uncertainty and report-generation needs.
- Decisive decision or feedback right: select context-sensitive data/code/experiment/research actions within each operational phase and revise them from execution/dialogue feedback.
- Decision owner: specialized first-party agents and solver agents (notably ML/SW/PhD/postdoc paths) invoked by `LaboratoryWorkflow`.
- Supporting / enforcement mechanisms: phase loop, code execution feedback, `MLESolver`, `PaperSolver`, max-step bounds, shared accepted products and checkpoint state.
- Closure path: phase goal/current products -> specialized agent proposes action/code -> first-party tools/solvers execute/materialize -> error/result/dialogue returns -> agent revises or submits phase product.
- Boundary reachability: these agents and solvers are instantiated by the documented `ai_lab_repo.py` workflow invoked from the supplied YAML entrypoint.
- Why this is / is not agent-owned: workflow code sequences phases, but local scientific/engineering choices are made by model-driven specialized agents.
- Evidence: [`README.md`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/README.md), [`ai_lab_repo.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/ai_lab_repo.py), [`agents.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/agents.py).
- Basis: structural
- Confidence: high
- Caveats: `MLESolver`/`PaperSolver` are credited only as first-party operational mechanisms in the pinned repository; external providers remain substrate.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination path is established at the reviewed recursion.
- Disturbance / variety regulated: specialized agents exchange dialogue and products, but no concrete cross-S1 interference/conflict/oscillation is identified and attenuated through a coordination relation.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: phase sequence, ML/SW dialogue passing, shared notes/products and reset/checkpoint state.
- Closure path: outputs/messages are passed to collaborators or next phases; no interference -> attenuation decision -> changed affected-S1 behavior loop is evidenced.
- Why this is / is not agent-owned: collaboration, role plurality and dialogue are not sufficient S2 evidence without a specific interference-regulation witness.
- Evidence: [`ai_lab_repo.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/ai_lab_repo.py), [`README.md`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/README.md).
- Basis: structural
- Confidence: high
- Caveats: the ML/SW data-preparation exchange is cooperative task production, not demonstrated S2 conflict attenuation.

### Absence scope

- Surfaces inspected: workflow phase loop, specialized agent role interactions, ML/SW data-preparation dialogue, shared notes/products, checkpoint/reset and review/refinement paths.
- Plausible first-party paths checked: multi-role collaboration, dialogue relay, shared research state and phase resets.
- Why no material first-party path remains: none names or senses an inter-S1 disturbance and selects a coordination response specifically to attenuate it.

## S3 — Inside-and-now control

- State: —
- Function: no qualifying whole-system current-control owner is established.
- Disturbance / variety regulated: workflow phases, retry loops, max-step budgets and report-refinement decisions alter progression, but whole-run control is predominantly scripted/configured and local phase judgments do not amount to broad S3 authority.
- Decisive decision or feedback right: no autonomous actor is shown holding a whole-project current view and discretionary authority over shared resources, commitments, priorities or constraints.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: `self.phases`, `phase_status`, solver/max-step budgets, checkpoint state, recursive reset to earlier phases and Co-Pilot flags.
- Closure path: scripted phase state/flags govern progression; local agent submissions or human phase acceptance feed that lifecycle without establishing S3's whole-system decision right.
- Why this is / is not agent-owned: specialized agents make local research decisions, while workflow-wide progression and resets are encoded in Python/YAML or depend on local review controls.
- Evidence: [`ai_lab_repo.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/ai_lab_repo.py).
- Basis: structural
- Confidence: high
- Caveats: Co-Pilot phase review is not promoted to S3(P); the human does not receive a demonstrated whole-system current resource/commitment control right at the Profile threshold.

### Absence scope

- Surfaces inspected: phase/status loop, checkpoints, budgets, report-refinement recursion, human-in-loop controls and specialized agent state.
- Plausible first-party paths checked: professor/PhD roles as manager, report-refinement return to planning, Co-Pilot supervision and phase-status lifecycle.
- Why no material first-party path remains: whole-run control remains scripted or phase-local; no actor combines whole-system current visibility with the required broad discretionary current-control authority.

## S3* — Complementary audit

- State: ?
- Function: a material independent review mechanism exists, but standard-mode corrective closure is ambiguous at the pinned revision.
- Disturbance / variety regulated: manuscript/experiment weaknesses, soundness/presentation/contribution/originality concerns and other peer-review objections.
- Decisive decision or feedback right: three separately prompted reviewer calls produce critical review judgments; a downstream branch can in principle choose to return the project to planning/experimentation.
- Decision owner: `ReviewersAgent` owns review judgments; potential corrective-return choice is intended for a PhD/human path but is not cleanly established as an enabled first-party standard mode in the pinned code.
- Supporting / enforcement mechanisms: three reviewer prompts, structured conference-style scoring, `report_refinement()`, stored `reviewer_response`, phase-status reset and recursive `perform_research()`.
- Closure path: report -> three reviewer judgments -> `report_refinement`; code contains a `y` branch that resets plan/experiment/report phases and re-enters research with reviewer feedback, but constructor-level `review_override = True` with zero default review steps forces the automated branch to `n` (complete) unless runtime state is altered.
- Boundary reachability: reviewer generation is directly reachable; the autonomous corrective return is present in first-party code but its supported standard-mode reachability is not documented/established strongly enough for `A` or `C` under Methodology 0.3.5.
- Why this is / is not agent-owned: semantic review is clearly agent-owned, but the decisive closure from independent findings back to corrective operation is the uncertain part.
- Claim being audited: that the resulting report/experiments constitute an adequate scientific submission.
- Ordinary reporting path: experiment results/interpretation -> `PaperSolver` report.
- Complementary access path: `ReviewersAgent` invokes three distinct critical reviewer personas over the plan and completed report.
- Independence boundary: reviewer invocations are separate from the operational PhD/ML/SW/PaperSolver generation path.
- Who acts on findings: potentially the research workflow after report-refinement reset; default pinned reachability of that action is unresolved because of `review_override` behavior.
- Evidence: [`agents.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/agents.py), [`ai_lab_repo.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/ai_lab_repo.py).
- Basis: structural
- Confidence: medium
- Caveats: a trace or maintainer-documented mode showing reviewer findings actually trigger the autonomous reset without source editing would likely resolve this state.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: acquire external scientific evidence, synthesize future research plans and return those plans into experimentation, with both autonomous and human Co-Pilot review modes.
- Disturbance / variety regulated: new/related literature, external AgentRxiv work, alternative experimental plans and human judgments that the proposed literature synthesis or plan should change before execution.
- Decisive decision or feedback right: in base mode, PhD/postdoc agents search/select/summarize literature and formulate the experiment plan; in Co-Pilot mode, the human can reject a phase product, provide notes and force regeneration under those notes.
- Decision owner: PhD/postdoc research agents in autonomous mode; human researcher in the documented Co-Pilot parent mode for reviewed literature/plan decisions.
- Supporting / enforcement mechanisms: arXiv/AgentRxiv search tools, literature-review accumulation, plan-formulation dialogue, phase-specific notes, YAML `copilot_mode`, `human_in_loop()` phase rejection/retry and shared agent state.
- Closure path: external literature/topic -> agents synthesize literature and plan -> autonomous acceptance or human Co-Pilot review -> rejected output is reset and human notes are attached to that phase -> revised literature/plan -> experimentation consumes the accepted plan/data context.
- Boundary reachability: autonomous literature/plan phases are standard workflow stages; `copilot_mode` is documented and parsed from shipped YAML, and `human_in_loop()` is called directly from literature/plan phases.
- Why this is / is not agent-owned: base research-option synthesis is agent-owned; parent mode intentionally transfers phase acceptance/adaptation judgment to the human and returns their notes into the next agent attempt.
- External distinction: arXiv/AgentRxiv papers, dataset/search context and human research-domain feedback.
- Future / prospective distinction: which literature matters and what experiment plan should be attempted next.
- Adaptation option generated: literature synthesis and an explicit research/experiment plan used by downstream data preparation/experimentation.
- Path back into current capability / S3: accepted or human-revised plan and literature summaries are copied into agent/solver state and directly condition subsequent experimental execution.
- Evidence: [`README.md`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/README.md), [`ai_lab_repo.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/ai_lab_repo.py), [`agents.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/agents.py).
- Basis: structural
- Confidence: high
- Caveats: `(P)` is limited to documented Co-Pilot phase review/retry. Merely supplying initial task notes would not be enough for the parent modifier.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | PhD/postdoc research agents | need to ground/plan future research from topic and external literature | agents retrieve/synthesize literature, formulate plan, and accepted products feed experimentation | [`ai_lab_repo.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/ai_lab_repo.py) |
| Parent (`P`) | human researcher in Co-Pilot mode | human judges literature review/plan product inadequate | `human_in_loop()` records phase-specific notes, resets agents and returns `True`, causing that phase to rerun before experimentation | [`ai_lab_repo.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/ai_lab_repo.py), [`README.md`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/README.md) |

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure is established.
- Disturbance / variety regulated: research topic, notes, compute/model constraints and Co-Pilot approvals shape the project but do not constitute an identity-level policy issue with ultimate-authority closure.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: YAML config, task notes, human phase-review flags, model selection and compute/max-step parameters.
- Closure path: configuration/human notes constrain task execution directly; no identity/ultimate-policy dispute -> authority -> returned governing decision loop is evidenced.
- Why this is / is not agent-owned: professor/PhD role labels do not supply S5 authority, and human Co-Pilot review remains phase/task-level guidance.
- Evidence: [`README.md`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/README.md), [`ai_lab_repo.py`](https://github.com/SamuelSchmidgall/AgentLaboratory/blob/d9017d90e329112d2a80b7712f37ee9094d2cd27/ai_lab_repo.py).
- Basis: structural
- Confidence: high
- Caveats: human research ownership outside the harness is not automatically first-party S5(P).

### Absence scope

- Surfaces inspected: YAML/task notes, specialized agent role prompts/state, Co-Pilot controls, phase acceptance, report refinement and AgentRxiv integration.
- Plausible first-party paths checked: Professor role as S5, research topic/notes as identity, Co-Pilot as ultimate policy and peer-review completion as ultimate authority.
- Why no material first-party path remains: each path governs task content/quality or future research choices; none closes a system-identity/ultimate-policy issue at the declared recursion.

## Recursion

One LaboratoryWorkflow research project is the viable system. Specialized researchers/engineers/solvers are internal S1/S4 actors. The human is a qualifying Parent only in explicit Co-Pilot loops where their decision is returned into a function-specific revision path; generic authorship of the topic is not imported as VSM ownership.

## Variety and escalation

Local operational variety is handled by specialized agents, solver loops and execution feedback. Future scientific variety is handled by literature/plan agents, with optional escalation to the Co-Pilot human. Manuscript concerns are independently reviewed, but autonomous corrective return from those reviewer findings remains unresolved at the pinned revision. No identity-level escalation path was found.

## Evidence gaps

- `review_override = True` in the pinned `LaboratoryWorkflow` obscures whether the autonomous report-review reset is a supported runtime mode rather than a dormant/developer-controlled path; S3* is therefore `?` rather than inferred from reviewer naming.
- Structural review only; no new end-to-end run or Co-Pilot trace was produced.
- AgentRxiv is credited only as an external/prospective evidence source when called by this workflow; its broader multi-lab organization is a separate possible system-in-focus.