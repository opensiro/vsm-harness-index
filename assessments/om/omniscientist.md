---
harness_id: omniscientist
project_name: OmniScientist
repository: https://github.com/Omni-Scientist/OmniScientist
review_ref: fb0164a1c4ff739b57f230cbc0b9a68796a45e1f
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# OmniScientist

## Review boundary

- System in focus: OmniScientist's shipped autonomous research workflow, especially the self-contained `agentic.py` research harness and its ideation, experiment, evidence, and write-up stages.
- Purpose and identity: autonomously form a research hypothesis, execute grounded analysis/experiments, preserve evidence, and produce a paper-like write-up without fabricating unsupported results.
- Relevant environment: user research task and source data/materials; external scientific literature/search services; executable analysis environment; model/perception endpoints.
- Standard-distribution boundary: first-party OmniScientist agent loop, tools, deterministic exit gates, evidence layer, stage artifacts, experiment execution, and writer surfaces at the pinned revision.
- Credited operating / distribution surfaces: `engine/omniscientist/agentic.py`, the mirrored distributed OmniSci skill, evidence/writer/paperlint surfaces, and their standard stage artifacts.
- Adjacent first-party surfaces excluded from ownership: desktop/UI packaging, CI/release workflows, evaluation assets, screenshots, development fixtures, and duplicate vendored copies used for packaging. OpenAlex/Crossref and model/perception providers are external dependencies rather than imported organizational owners.
- First-party operating / deployment modes considered: the self-contained agentic scientist path and the packaged OmniSci skill that reproduces the same first-party research loop.
- Recursion level: one autonomous research run; stage-specific reasoning is treated as one operational research system rather than assuming each named stage is an independent viable S1 unit.
- Reviewed revision: `fb0164a1c4ff739b57f230cbc0b9a68796a45e1f`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

OmniScientist's agentic path is explicitly described as a self-contained harness. A thin outer stage sequence calls a generic ReAct-style `agent_loop`: the model chooses tool calls, receives tool results, and continues until a deterministic stage exit gate accepts a finalized artifact or the run exhausts its step budget. The ideation stage requires real literature retrieval and novelty/feasibility screening. The experiment stage consumes the saved idea, designs a method, runs real code, and iterates method and execution until it has grounded results or an honest null/infeasible outcome. A writer then turns stored evidence and results into the research artifact.

Deterministic exit gates enforce minimum evidence and anti-fabrication requirements. They can reject a proposed finalize and return the exact missing condition to the same agent loop, but enforcement of a stage contract is not credited as a separate whole-system management or audit function.

Primary evidence: [agentic harness implementation](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/engine/omniscientist/agentic.py), [OmniSci skill](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/skill/omnisci/SKILL.md).

## Operational model

The S1 operational loop is the model-driven research agent acting through first-party tools and persistence. Stage gates are deterministic acceptance machinery around that agent. The outside-and-then loop is established separately by literature-grounded ideation: external scientific distinctions are converted into candidate research directions and a selected hypothesis that changes the subsequent experiment program.

## S1 — Operations

- State: A
- Function: perform the research task through iterative tool use: inspect source material, search literature, formulate an idea, design and execute analysis, inspect results, and produce a grounded research artifact.
- Disturbance / variety regulated: uncertainty in source data/materials, literature landscape, analysis design, execution failures, and result interpretation.
- Decisive decision or feedback right: choose research/tool actions and decide how to revise the current method or result proposal in response to observations and gate feedback.
- Decision owner: the model-driven `agent_loop` for the active research stage.
- Supporting / enforcement mechanisms: tool schemas/executors, search and image budgets, stage persistence, trace capture, deterministic done gates, code execution, and writer/evidence utilities.
- Closure path: tool/execution/search results are appended to the agent history; the agent chooses subsequent actions and eventually submits a stage artifact that passes its gate and becomes input to the next research stage.
- Boundary reachability: the loop is the core shipped `agentic.py` operating path and is reproduced in the distributed skill; no external agent harness is required to supply the decision loop.
- Why this is / is not agent-owned: deterministic gates can reject outputs, but they do not choose the substantive research action that follows; the model-driven loop does.
- Evidence: [generic agent loop](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/engine/omniscientist/agentic.py), [experiment stage](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/engine/omniscientist/agentic.py#L1).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the external LLM/perception endpoint supplies inference, but the tool protocol, persistence, gates, and operational loop are first-party OmniScientist surfaces.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination loop is established at the declared recursion.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: stage sequencing, shared artifacts, optional perception tools, and pipeline handoffs provide workflow structure but do not evidence regulation of interference among distinct S1 operational units.
- Closure path: not established.
- Why this is / is not agent-owned: the reviewed path is primarily one staged research agent/process, not a set of evidenced S1 units whose interaction creates a specific conflict or oscillation.
- Evidence: [outer stage sequence and agent-loop design](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/engine/omniscientist/agentic.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: file/artifact handoffs could participate in a future multi-unit coordination design, but generic sequencing is not S2.

### Absence scope

- Surfaces inspected: stage orchestration, generic agent loop, tool execution, evidence layer, skill workflow, writer, and persistence/artifact handoffs.
- Plausible first-party paths checked: stage-to-stage artifact flow, tool/perception separation, research/execution iterations, and packaged skill composition.
- Why no material first-party path remains: no reviewed path establishes distinct S1 units plus a concrete inter-unit interference/conflict/oscillation and an attenuation relation that changes later S1 behavior.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system discretionary current-control function is established beyond ordinary workflow/gate enforcement.
- Disturbance / variety regulated: not established at S3 scope.
- Decisive decision or feedback right: not established at whole-system current-control scope.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: fixed stage sequence, step/search/image budgets, max-step pressure, deterministic exit gates, and retry/nudge messages constrain operation.
- Closure path: these mechanisms return local gate feedback to the same stage agent but do not evidence a distinct whole-system resource/priority/commitment manager.
- Why this is / is not agent-owned: a gate that says whether a stage artifact satisfies a contract is enforcement of predefined constraints, not a whole-system discretionary current-control owner.
- Evidence: [agent loop and exit-gate behavior](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/engine/omniscientist/agentic.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: the active research agent can revise its own local work after rejection; that local operational regulation remains S1 unless evidence establishes whole-system current control.

### Absence scope

- Surfaces inspected: stage sequence, done gates, budgets, retry logic, experiment iteration, persistence, and writer path.
- Plausible first-party paths checked: deterministic finalize rejection, max-step convergence pressure, stage sequencing, result/null handling, and task-level replanning.
- Why no material first-party path remains: none provides a whole-system view plus a discretionary decision over resources, priorities, commitments, accountability, synergy, or intervention on behalf of the research organization as a whole.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary-audit loop is established in the reviewed standard distribution.
- Disturbance / variety regulated: not established at S3* scope.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: provenance/evidence requirements, deterministic exit gates, `paperlint`, and anti-fabrication checks validate ordinary stage outputs but remain part of the same production/acceptance path.
- Closure path: ordinary gate rejection returns to the producing agent; no separate audit findings-to-control loop is established.
- Why this is / is not agent-owned: validator/gate naming is not sufficient. The reviewed `agentic.py` stage map explicitly has review as future work (`4 (review) to come`), and the existing gates do not establish an independent auditor with complementary access.
- Evidence: [agentic stage map and gates](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/engine/omniscientist/agentic.py), [paper-writing support](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/engine/omniscientist/writer.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a future separate review stage could change this classification if it gains sufficiently independent evidence access and its findings alter subsequent operation.

### Absence scope

- Surfaces inspected: deterministic stage gates, evidence/provenance utilities, paperlint/writer path, traces, experiment results, and stage registry.
- Plausible first-party paths checked: finalize gates, evidence validation, citation/provenance checks, writer checks, and the planned review-stage surface.
- Why no material first-party path remains: current validators are on the ordinary production/acceptance path, while the distinct review stage is not implemented in the reviewed agentic stage sequence; no sufficiently independent complementary access plus corrective return loop is established.

## S4 — Outside-and-then intelligence

- State: A
- Function: sense the external scientific landscape, generate and screen research options, and return a selected literature-grounded hypothesis into the experiment program.
- Disturbance / variety regulated: risk that the research direction is trivial, already covered by prior work, infeasible, or poorly matched to available material/data.
- Decisive decision or feedback right: choose among candidate hypotheses/research directions after external literature retrieval and novelty/feasibility screening.
- Decision owner: the model-driven ideation agent.
- Supporting / enforcement mechanisms: OpenAlex/search tooling, required-search counters, candidate-count/finalize gates, source-material inspection, and persisted stage-one artifact.
- Closure path: retrieved literature and observed material inform candidate generation/screening; the finalized idea/hypothesis is persisted; stage two reads that saved idea and designs/runs the experiment around it.
- Boundary reachability: literature-grounded ideation is a required first-party stage in the shipped agentic research path, and stage two directly consumes its saved result.
- Why this is / is not agent-owned: the gate requires evidence but does not select the research direction; the model-driven ideation loop interprets external distinctions and chooses the proposal.
- External distinction: retrieved prior scientific work and source-material observations relevant to novelty and feasibility.
- Future / prospective distinction: which candidate direction is sufficiently novel/feasible to become the next experiment program rather than merely explaining the current result.
- Adaptation option generated: candidate research questions/hypotheses and the selected developed proposal.
- Path back into current capability / S3: the selected stage-one idea is saved and becomes the fixed input from which stage two designs and executes the method, changing what the research system subsequently does.
- Evidence: [agentic design constraints and ideation loop](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/engine/omniscientist/agentic.py), [OmniSci skill research workflow](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/skill/omnisci/SKILL.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary experiment retries/null handling are not the basis for S4; credit comes from the closed external-literature → option selection → later experiment path.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the declared research-run recursion.
- Disturbance / variety regulated: not established at S5 scope.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: user task text, system prompts, fixed stage contracts, model/provider configuration, and deterministic evidence gates constrain the run but do not themselves create a policy-authority loop.
- Closure path: not established at identity/ultimate-policy scope.
- Why this is / is not agent-owned: task direction and prompt/gate definitions are operating constraints; there is no evidenced runtime process for disputing or redefining the research system's identity/ultimate policy and returning that authoritative decision to operation.
- Evidence: [agentic harness entry and stage contracts](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/engine/omniscientist/agentic.py), [skill instructions](https://github.com/Omni-Scientist/OmniScientist/blob/fb0164a1c4ff739b57f230cbc0b9a68796a45e1f/skill/omnisci/SKILL.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: human configuration or task selection is not automatically parent-governed S5.

### Absence scope

- Surfaces inspected: entry/task handling, system prompts, stage definitions, evidence gates, provider/model configuration, and packaged skill instructions.
- Plausible first-party paths checked: user task direction, finalize gates, model configuration, stage policy, and error/null escalation.
- Why no material first-party path remains: none establishes an identity/ultimate-policy issue reaching a legitimate authority whose returned decision governs subsequent operation at the declared recursion.

## Recursion

The assessment treats the complete research run as the system in focus. Ideation, experiment, and writing are functional stages within that system, not automatically separate viable recursions. External search/model/perception providers remain dependencies. A deployment that wraps OmniScientist in a larger laboratory organization would require a separate boundary-specific assessment.

## Variety and escalation

Variety is attenuated through tool/search/image budgets, deterministic exit gates, explicit evidence requirements, execution retries, honest null/infeasible outcomes, trace persistence, and staged artifacts. Gate rejection returns a concrete reason to the same agent loop. That is a local correction path, not by itself S3 or S3*. Gateway failures and max-step exhaustion can terminate a stage as failed rather than fabricating completion.

## Evidence gaps

- Reassess S3* when the indicated review stage is implemented: verify separate audit access/independence and a findings-to-corrective-control return path rather than awarding credit from the `review` label alone.
- Reassess S3 if a distinct manager gains a whole-run current view and discretionary resource/priority/intervention authority across research operations.
- Reassess S5 only if a supported runtime mode introduces genuine identity/ultimate-policy authority and closure; user prompts/configuration alone remain insufficient.
