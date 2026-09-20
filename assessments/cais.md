---
harness_id: cais
project_name: Causal AI Scientist (CAIS)
repository: https://github.com/causalNLP/causal-agent
review_ref: 2289e9e3c11376336dec027fd17269a46443a784
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
autonomy_s4: —
autonomy_s5: —
---

# Causal AI Scientist (CAIS)

## Review boundary

- System in focus: the current first-party `CausalAgent` causal-analysis runtime and its shipped query/data analysis, method selection, optional IV discovery, control selection, cleaning, estimation, and explanation path.
- Purpose and identity: autonomously turn a causal question plus dataset into a selected causal-inference analysis and an explained result using first-party causal-method tooling and model-assisted decisions.
- Relevant environment: user causal query, supplied dataset and description, configured LLM provider/model, supported causal estimators, and statistical properties of the data.
- Standard-distribution boundary: current `CausalAgent.run_analysis()` plus the first-party tools/components it directly invokes at the pinned revision.
- Credited operating / distribution surfaces: `cais/agent.py` current `CausalAgent`; dataset/query analyzers; method/controls selection; optional IV discovery; dataset cleaner; estimator/method executor; explanation generator.
- Adjacent first-party surfaces excluded from ownership: the deprecated `run_causal_analysis()` compatibility path, `CausalAgent.validate_method()` marked `Do not use yet`, tests/docs/CI, and unintegrated validator/refactoring surfaces. External model providers are inference dependencies rather than borrowed organizational owners.
- First-party operating / deployment modes considered: `CausalAgent.run_analysis()` with its default LLM method-selection path and the optional `use_iv_pipeline` mode when IV is selected.
- Recursion level: one causal-analysis run; helper components and IV critics are subordinate specialist paths unless evidence establishes a separate VSM function at this recursion.
- Reviewed revision: `2289e9e3c11376336dec027fd17269a46443a784`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

`CausalAgent.run_analysis()` performs a staged causal-analysis workflow: analyze the dataset/query, select a causal method, optionally discover instruments, select controls, clean the data, execute the estimator/method, and generate an explanation. The method selector can use an LLM-backed decision tree. The optional IV path uses a hypothesizer, confounder miner, and separate exclusion/independence critics before accepted IVs proceed.

The repository also contains richer method-validation machinery and documentation describing a Stage-3 feedback loop, but the current `CausalAgent` path does not call that validator: `validate_method()` is explicitly marked `Do not use yet`, while the old compatibility `run_causal_analysis()` function is marked deprecated. This assessment therefore does not borrow S3/S3* closure from those adjacent surfaces.

Primary evidence: [current CausalAgent](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/agent.py), [IV discovery component](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/components/iv_discovery.py), [method validator](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/components/method_validator.py).

## Operational model

The operational decision loop is causal-analysis work itself. Model-assisted components interpret the query/data and choose analysis structure; first-party estimators/tools execute that choice; results are returned through the explanation path. Validation/critic components are evaluated function-first rather than promoted from their names: the current integrated IV critics screen candidate instruments inside the ordinary S1 method-construction path, while the broader method-validator feedback described in documentation is not closed through the current `run_analysis()` entry point.

## S1 — Operations

- State: A
- Function: autonomously construct and execute a causal analysis from a dataset and query, including method/control choices and explanation of the resulting estimate.
- Disturbance / variety regulated: variation in causal question, dataset schema/characteristics, candidate causal method, control variables, optional instruments, cleaning requirements, and estimator execution.
- Decisive decision or feedback right: interpret the causal problem and select the method/variables/control structure that determines the analysis to execute.
- Decision owner: model-assisted CAIS analysis components, especially query/dataset interpretation and LLM-backed method selection; the selected structure is then executed by first-party causal tools/estimators.
- Supporting / enforcement mechanisms: tool wrappers, estimator library, data cleaning, typed models, optional IV discovery, deterministic estimator code, and provider transport.
- Closure path: dataset/query observations feed the selection components; selected method/variables determine cleaning and execution; computed results feed the explanation generator and returned analysis.
- Boundary reachability: this path is the current public `CausalAgent.run_analysis()` workflow, not a test or deprecated compatibility function.
- Why this is / is not agent-owned: substantive interpretation/method-selection discretion is model-driven in the standard path; deterministic estimators execute the chosen causal analysis rather than owning that upstream decision.
- Evidence: [CausalAgent workflow](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/agent.py), [README workflow](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: CAIS can switch to rule-based method selection; the positive state is based on the first-party standard model-assisted mode exposed by `llm_method_selection=True`.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination function is established at the declared recursion.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: staged tool calls and specialist helpers pass structured state but do not evidence regulation of interference among distinct S1 operational units.
- Closure path: not established.
- Why this is / is not agent-owned: dataset analyzer, selector, critics, executor, and explainer are functional components of one causal-analysis operation; plurality of components is not an S2 witness.
- Evidence: [CausalAgent staged workflow](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/agent.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a future multi-analysis/team mode would need an actual inter-S1 disturbance and attenuation loop to qualify.

### Absence scope

- Surfaces inspected: current CausalAgent workflow, method/query/data/control helpers, IV discovery/critics, execution and explanation path, state manager, and method-validation surfaces.
- Plausible first-party paths checked: staged helper interaction, IV critic plurality, shared variables/state, method-selection handoffs, and tool sequencing.
- Why no material first-party path remains: no reviewed path establishes distinct S1 operational units plus a specific interference/conflict/oscillation and a first-party coordination relation that changes their subsequent behavior.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established separately from task-local causal-method selection and pipeline sequencing.
- Disturbance / variety regulated: not established at S3 scope.
- Decisive decision or feedback right: not established at whole-system management scope.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: fixed stage order, method-selection logic, estimator availability checks, tool error handling, and optional flags regulate local task execution.
- Closure path: local selections flow into the next analysis step, but no whole-system supervisory decision over resources, commitments, priorities, accountability, or cross-operation intervention is evidenced.
- Why this is / is not agent-owned: choosing the causal method for the analysis is part of producing the S1 outcome; it is not automatically S3 simply because it chooses among methods.
- Evidence: [current run_analysis sequence](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/agent.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: documentation calls out staged validation and feedback, but current pinned runtime integration controls the assessment.

### Absence scope

- Surfaces inspected: CausalAgent state, pipeline stages, method selection/validation code, estimator registry, execution/error handling, and optional IV pipeline.
- Plausible first-party paths checked: method recommendation, method fallback, validation suggestions, estimator availability, and pipeline state.
- Why no material first-party path remains: the current standard entry point supplies task-local analytic decisions but no distinct whole-system current view and management authority at the declared recursion.

## S3* — Complementary audit

- State: —
- Function: no material, operationally closed complementary-audit function is established in the current standard `CausalAgent` path.
- Disturbance / variety regulated: not established at S3* scope.
- Decisive decision or feedback right: not established as an independent audit right over current operation.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: optional IV exclusion/independence critics and the repository's method-validator/assumption-check machinery provide validation primitives, but the current operating path does not close a separate complementary audit loop over executed S1 work.
- Closure path: the current IV critics filter proposed instruments before method execution; the broader method-validator path is not invoked by `run_analysis()`. No independent audit finding is shown returning to whole-system control after observing operational reality.
- Why this is / is not agent-owned: critic/validator naming is insufficient. The IV critics inspect candidate instrument plausibility inside ordinary method construction, and the current public `validate_method()` is explicitly not in use.
- Evidence: [current CausalAgent including `validate_method()` and `run_analysis()`](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/agent.py), [IV critics integration](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/components/iv_discovery.py), [method validation machinery](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/components/method_validator.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: if the method-validator/assumption-check feedback loop becomes part of the supported current entry point, reassess its complementary access, organizational independence, judgment owner, and return-to-control closure rather than assigning S3* automatically.

### Absence scope

- Surfaces inspected: current run entry point, IV critics, method validator, statistical assumption checks, README-described validation flow, and deprecated compatibility path.
- Plausible first-party paths checked: IV exclusion/independence critics, statistical assumption tests, method-validator recommendations, and documented feedback to method selection.
- Why no material first-party path remains: the integrated critics are upstream candidate screening inside S1, while the broader validator feedback path is either marked unused/deprecated or lacks a current supported executed-result audit → independent finding → corrective control closure.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then adaptation loop is established at the declared recursion.
- Disturbance / variety regulated: not established at S4 scope.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: domain-informed prompts, candidate causal-method knowledge, IV hypothesis/critic reasoning, dataset analysis, and method alternatives help solve the current causal task.
- Closure path: current data/query distinctions feed current analysis choices; no separately evidenced external/prospective sensing loop changes later system capability or research strategy.
- Why this is / is not agent-owned: knowledge of multiple methods and generation of alternative suggestions are current problem-solving options, not by themselves S4.
- Evidence: [method validator](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/components/method_validator.py), [IV discovery](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/components/iv_discovery.py), [current CausalAgent](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/agent.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: an external-literature or prospective adaptation loop that changes subsequent causal-analysis capability could change this state.

### Absence scope

- Surfaces inspected: query/data analysis, decision trees, IV discovery/critics, method validation, estimator selection, explanations, and repository documentation.
- Plausible first-party paths checked: alternative-method suggestions, domain-reference prompts, IV hypothesizing, dataset characterization, and method retry concepts.
- Why no material first-party path remains: these paths remain tied to solving the current causal question; the reviewed standard runtime does not close external/future sensing into changed subsequent organizational capability or program direction.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy function is established at the declared causal-analysis recursion.
- Disturbance / variety regulated: not established at S5 scope.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: user query, configuration, provider/model selection, causal-method library, prompts, and flags constrain the analysis.
- Closure path: not established at identity/ultimate-policy scope.
- Why this is / is not agent-owned: the user query defines the current analysis request; it does not establish a runtime governance loop for the system's identity or ultimate policy.
- Evidence: [CausalAgent constructor and run entry point](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/agent.py), [configuration](https://github.com/causalNLP/causal-agent/blob/2289e9e3c11376336dec027fd17269a46443a784/cais/config.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: ordinary human choice of dataset/query/provider is not parent-governed S5.

### Absence scope

- Surfaces inspected: constructor/configuration, query handling, prompts, method policy, optional flags, error handling, and repository docs.
- Plausible first-party paths checked: query authority, model/provider configuration, method constraints, validator recommendations, and user-facing operation.
- Why no material first-party path remains: none establishes an identity/ultimate-policy issue, legitimate ultimate authority, authoritative decision, and return-to-operation closure at the assessed recursion.

## Recursion

One causal-analysis run is the system in focus. Tool/components such as dataset analyzer, method selector, IV critics, estimators, and explainer are subordinate functions inside that run unless a separate viable-system boundary is evidenced. External LLM providers remain inference dependencies.

## Variety and escalation

CAIS handles analytical variety through typed dataset/query interpretation, method selection, optional IV discovery, control selection, cleaning, estimator fallbacks, and explanation generation. Exceptions can return errors or invoke alternate execution tooling. These mechanisms improve robustness of S1 work but do not independently establish higher VSM functions without the required organizational witnesses.

## Evidence gaps

- The README-described validation feedback is ahead of the current `CausalAgent.run_analysis()` integration. Reassess S3* if method/assumption validation becomes a supported closed path over operational evidence and its findings alter subsequent analysis under a sufficiently independent auditor.
- Reassess S4 if CAIS adds a first-party external/prospective sensing loop whose decisions alter future analysis capability or research strategy rather than only the current method choice.
- Reassess S2 only if multiple operational units and a concrete inter-unit disturbance/attenuation loop are introduced.
