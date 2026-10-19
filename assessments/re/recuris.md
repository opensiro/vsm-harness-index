---
harness_id: recuris
project_name: Recuris
repository: https://github.com/Gen-Verse/Recuris
review_ref: 7d3745ab787b1206ccd981cb1511100476097266
reviewed_at: 2026-10-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Recuris

## Review boundary

- System in focus: The **shipped Python Recuris frozen-downstream-model agent plus skill-memory operating harness**, and its separately invoked **model-backed meta-agent learning campaign** that creates candidate memory changes from execution evidence and conditionally adopts them for later downstream episodes. At this recursion a downstream task-serving agent is S1, and an enabled memory adaptation cycle is bounded S4; benchmark evaluators, user permission and data curation are distinct.
- Purpose and identity: Solve long-horizon tasks using a frozen underlying model and dynamically selected experiential/working-memory support, with optionally learned revisions to future memory-carrier behavior.
- Relevant environment: Unfamiliar user tasks, tool receipts, failed multi-turn plans, incorrect state claims, long-horizon regressions, missed memory invocation, proposal errors, sample leakage, benchmark split variation and changing task demands.
- First-party standard distribution: `src/recuris/runtime.py`, `adapters/tau2/agent.py`, `skillmemory.py`, `wm/*`, `em/*`, `builtin/checkers.py`, `grounding.py`, `metaagent/{driver,gates,domain_adapter,plan_schema,reachability}.py`, `metaagent/launchers`, `metaagent/downstream.py`, `cli.py`, packaged memory manifests and documentation. Frozen downstream model providers and selected upstream coding-agent model executable are **external**; only their supported first-party integration is credited.
- Credited operating / distribution surfaces: [README.md#L35](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/README.md#L35), [README.md#L380](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/README.md#L380), [docs/architecture.md#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/docs/architecture.md#L1), [src/recuris/runtime.py#L121](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L121), [src/recuris/runtime.py#L157](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L157), [src/recuris/runtime.py#L192](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L192), [src/recuris/adapters/tau2/agent.py#L247](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L247), [src/recuris/metaagent/driver.py#L682](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L682), [src/recuris/metaagent/driver.py#L7412](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L7412), [src/recuris/metaagent/driver.py#L9677](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L9677), [src/recuris/metaagent/gates.py#L31](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/gates.py#L31).
- Adjacent first-party surfaces excluded from ownership: Held-out benchmark scoring authority, external tau2/SkillFlow/Terminal-Bench original systems and patched copies, training data split definitions, human researcher grant of evaluation/compute budget, the paper's reported empirical numbers, and internal decisions of an external Claude Code or downstream provider. Benchmark results in README are not measured in this review.
- Supported operating / deployment modes considered: Default loaded skill-memory downstream agent and concrete tau2 bridge; within-task adaptation and cross-task episodic state; optional `recuris metaagent run` model-driven candidate editing with paired held-out gate, `qualify`, progressive/provisional working-base modes, hierarchical parallel diagnosis, continuation and resumed rounds; provided TB2.1/SkillFlow adapters reviewed for boundary, not merged into a generic single S1 division without evidence.
- Recursion: Single downstream task-serving model operating role with memory tools and a separate *evolution/research campaign* capable of changing that role's future installed memory. Parallel diagnosis contributors are candidates for one memory package, not separately viable operational departments with stable inter-unit obligations. S4 positivity is confined to source-backed configured meta-agent campaign, not default autonomous every-turn memory redesign.
- Frozen source identity: Public `Gen-Verse/Recuris` GitHub ID **1345723168**, default `main@7d3745ab787b1206ccd981cb1511100476097266`, Git tree `b91fb20b1db783a4ed961832af44d841c3bbb1f8`, Apache-2.0 root LICENSE; [batch #1750](https://github.com/opensiro/vsm-harness-index/issues/1750). Reviewed 2026-10-19, Profile 0.2.4 / Methodology 0.3.7.

## Repository architecture

`RecurisAgent` subclasses the tau2-model agent and delegates each `generate_next_message` to first-party `TurnRuntime.run_turn`, passing a concrete `_Tau2Port` that invokes actual downstream model `llm_draft`, optional corrective redraft and `commit`. `TurnRuntime` first grounds tool-result receipts, refreshes the working-memory ledger under manager-selected cadence, invokes installed skill-memory deliverers, prepares contextual working memory, sends it to the model, applies draft checkers, sanitizes outgoing text and returns the committed model response. This is the shipped task–model–observation operating cycle, rather than static prompt storage; optional benchmark/port setup is required for live runs. [src/recuris/adapters/tau2/agent.py#L81](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L81); [src/recuris/adapters/tau2/agent.py#L143](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L143); [src/recuris/adapters/tau2/agent.py#L189](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L189); [src/recuris/adapters/tau2/agent.py#L247](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L247); [src/recuris/adapters/tau2/agent.py#L284](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L284); [src/recuris/runtime.py#L157](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L157); [src/recuris/runtime.py#L192](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L192); [src/recuris/runtime.py#L228](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L228).

The separately configured `recuris metaagent run` `Driver` evaluates the currently installed memory package on the train split, stores failing tasks and sanitized traces, asks model-backed external coding agent(s) to diagnose and edit **candidate** memory components (E, W, invocation policy ρ, checkers C), and validates the candidate package with schema/lint/leakage/activation checks. A paired held-out gate using item-clustered bootstrap and a regression cap supplies the code-owned acceptance verdict; an accepted package is committed as the future base for later rounds. Rejected candidates may be used **provisionally** as a temporary working base under explicitly selected settings and are not equivalent to canonical admission. The model proposes prospective changes; it does **not** unilaterally own their validated adoption. [src/recuris/metaagent/driver.py#L682](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L682); [src/recuris/metaagent/driver.py#L5898](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L5898); [src/recuris/metaagent/driver.py#L7412](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L7412); [src/recuris/metaagent/driver.py#L8268](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L8268); [src/recuris/metaagent/driver.py#L9381](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L9381); [src/recuris/metaagent/driver.py#L9420](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L9420); [src/recuris/metaagent/driver.py#L9677](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L9677); [src/recuris/metaagent/driver.py#L10350](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L10350); [src/recuris/metaagent/gates.py#L31](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/gates.py#L31).

The `Ledger`, ground-truth receipt validator, leakage scan, fingerprints, causal prescription and checked held-out scores are safeguards for current task correctness and **memory candidate admission**. They should not be silently classified as S3 operational executive oversight, independent S3* management audit or S5 constitutional rights. [src/recuris/metaagent/gates.py#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/gates.py#L1); [src/recuris/grounding.py#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/grounding.py#L1); [src/recuris/wm/ledger.py#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/wm/ledger.py#L1); [docs/architecture.md#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/docs/architecture.md#L1).

## Operational model

The downstream model selects its actual responses/tool calls in a current session based on tool feedback and enriched skill-memory context. With the operator-enabled metaagent campaign, a different configured model proposes durable changes to future memory components; first-party code compares accepted vs candidate behavior and, if the gate passes, carries the new package into later operating trials. This is opt-in prospective capability evolution, not by itself management or constitutional authority for a broader enterprise.

## S1 — Operations

- State: A
- Function: Select context-dependent task actions and responses using the configured underlying model, grounded task observations and currently installed skill memory.
- Disturbance / variety regulated: Heterogeneous requests, uncertain model outputs, tool failures, state/intent ambiguity and incorrectly declared task completion.
- Decisive decision or feedback right: The model behind the supported `_Tau2Port.llm_draft` chooses a tool call/answer based on delivered memory and actual turn context; checker bounces may cause a second model-generated answer, and grounded tool receipts feed later turns.
- Decision owner: Configured downstream language model reached through `RecurisAgent.generate_next_message` and `TurnRuntime.run_turn`; the first-party memory manager/checkers are bounded scaffolding, not the owner of the model's next substantive task action.
- Supporting / enforcement mechanisms: Working-memory ledger, experiential memory card delivery, invocation rule ρ, receipt matching, checkers and sanitation, contextual draft and redraft, tau2 runtime adapter.
- Closure path: New task/receipt → first-party grounding/working memory update → delivery/context → model draft including actual tool intention → checker/redraft/commit → environment produces new tool result → subsequent agent turn and answer.
- Boundary reachability: The packaged `RecurisAgent` constructor loads skill memory, implements tau2 agent `generate_next_message`, wires concrete `_Tau2Port` model draft/commit methods to the exported first-party `TurnRuntime`; documented tau2/agent adapter runs this operating route. External tau2 provider is required for live execution, but the first-party integration is present.
- Why this is / is not agent-owned: Without the model, memory/rules/checkers can constrain and ground progress but cannot select contextual next actions and synthesize task responses from new observations. Removing the outer research evaluator does not eliminate this model-backed S1 operating path.
- Evidence: [src/recuris/runtime.py#L192](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L192), [src/recuris/runtime.py#L227](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L227), [src/recuris/adapters/tau2/agent.py#L81](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L81), [src/recuris/adapters/tau2/agent.py#L189](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L189), [src/recuris/adapters/tau2/agent.py#L247](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L247), [src/recuris/adapters/tau2/agent.py#L284](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/adapters/tau2/agent.py#L284).
- Basis: Source-integrated downstream model/tool result path, not empirical performance verification.
- Confidence: High for model-facing wiring; untested provider/runtime availability.
- Caveats: The underlying frozen model, simulator and original task-provider internals are external actors, not borrowed as additional Recuris metasystem functions.

## S2 — Coordination

- State: —
- Function: No distinct first-party **interference regulator among independently viable S1 operating divisions** with returned mutual adjustments is demonstrated at this memory-evolving single-agent recursion.
- Disturbance / variety regulated: Multiple hierarchical diagnosis workers can propose competing repairs; separate benchmark trials can disagree; ledger rules can select among them. These are experiment/proposal conflicts, not necessarily competing operational services.
- Decisive decision or feedback right: Meta-agent diagnosis merges candidate memory patches within one future package, while deterministic gates admit changes based on tests; no distinct organization-level agent adjudicates concrete interference among two independently viable S1 service divisions and returns revised ongoing commitments.
- Decision owner: Operator-selected meta-agent workflow and deterministic candidate gate; not a persistent S2 coordination mandate over an S1 federation.
- Supporting / enforcement mechanisms: Hierarchical diagnosis workers/reducer, candidate plan schema, package lint, fingerprint, parallel task evaluation and memory-version serialization.
- Closure path: Observed experiment failures → candidates consolidated → validation/gate → one revised memory package; no operating-S1 conflict detection → inter-divisional dampening decision → reciprocal S1 operational rights/behavior.
- Why this is / is not agent-owned: A model reconciling alternate experimental proposals contributes to S4 option generation; its presence does not make worker copies independently viable departments.
- Evidence: [src/recuris/metaagent/driver.py#L7412](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L7412), [src/recuris/metaagent/driver.py#L8268](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L8268), [src/recuris/metaagent/driver.py#L10310](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L10310), [src/recuris/metaagent/plan_schema.py#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/plan_schema.py#L1).
- Basis: Function-first negative including hierarchical diagnosis and parallel validation paths.
- Confidence: Medium-high at defined recursion.
- Caveats: A downstream multi-agent deployment could add its own S2; it is not sourced here.

### Absence scope

- Surfaces inspected: Hierarchical diagnosis worker batches, reducer, meta-agent plan consolidation, package candidates, memory ledger and evaluation fanout.
- Plausible first-party paths checked: Competing suggested memory fixes, shared candidate edits, concurrent trial resources and coordinator arbitration.
- Why no material first-party path remains: All checked paths support one task agent's memory-evolution campaign, without a separately owned first-party inter-operating-division conflict regulator returning mutual adjustments to independently viable S1 units.



## S3 — Inside-and-now control

- State: —
- Function: No first-party agent executive owns discretionary present priorities, resource allocation and binding feedback across a **portfolio of independently viable S1 divisions**.
- Disturbance / variety regulated: Simulation budget, power limitations, stale candidate versions and task progress errors may threaten an evolution study; configured budgeting/round gates manage this run, not a current viable organization.
- Decisive decision or feedback right: Research operator chooses environment, trial counts, seed, splits, rounds, regression cap and gate policy; first-party Driver and budget accounting apply these settings, while the model selects task or proposed memory content under that configuration.
- Decision owner: Operator/research protocol and deterministic run Driver; no independently mandated current organizational S3.
- Supporting / enforcement mechanisms: Generation profile/simulation budget, held-out power gate, run state and checkpoints, fail-closed plan acceptance, milestone/round/seed management and startup integrity checks.
- Closure path: Model/task outcome → configured limit/gate/checkpoint controls → experiment retries, stops or continues; no whole-current managerial claim → discretionary change to ongoing independent S1 service commitments.
- Why this is / is not agent-owned: A ledger or manager-selected working-memory update cadence does not equate to managing separate live S1 organizations or their resource contract.
- Evidence: [src/recuris/metaagent/driver.py#L682](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L682), [src/recuris/metaagent/driver.py#L4536](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L4536), [src/recuris/metaagent/driver.py#L10000](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L10000), [src/recuris/runtime.py#L192](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L192).
- Basis: Source-bounded negative after checking both default runtime and research campaign.
- Confidence: Medium-high.
- Caveats: External research organization/benchmark owner may exercise genuine S3 but is beyond packaged runtime ownership.

### Absence scope

- Surfaces inspected: Research Driver, simulations/round/split budgets, state/checkpoint, working-memory manager cadence, patch acceptance policies.
- Plausible first-party paths checked: Current agent portfolio resourcing, task budget overrides, priority shift and resource assignment, stop/admit authority.
- Why no material first-party path remains: No first-party role owns a whole-current cross-viable-S1 management mandate; surfaced controls either apply preset experiment policy or operate one downstream model's current task.



## S3* — Complementary audit

- State: —
- Function: No independent complementary audit of the actual S1/S3 operational management picture with corrective findings returned to a separate current S3 authority is established.
- Disturbance / variety regulated: False agent completion, synthetic tool receipts, benchmark leakage, candidate causality errors and harmful patches are guarded; these are operational correctness and **future memory-admission** risks.
- Decisive decision or feedback right: Deterministic receipt grounding, checker bounces, paired held-out tests, fingerprint probes and leakage scans may veto current claims or future patches. No separate independent auditor challenges a sourced S3 management report and returns a correction to that manager.
- Decision owner: First-party safety/checker/gate algorithms plus external benchmark scoring oracle; not an S3* mandate.
- Supporting / enforcement mechanisms: Truth checkers, GroundingKernel, skill-carrier probes, paired bootstrap gate, no-synthetic-receipt safeguards, ledger and audit receipts.
- Closure path: Current draft or candidate memory → local check/reject/redraft or statistical acceptance → current task continues or future memory replaced; absent reality inspection → S3 management picture correction → new S3 current control decisions.
- Why this is / is not agent-owned: Strict scientific independent validation of a proposed S4 change is not by itself VSM S3*. The latter must serve a separate current S3 executive with a complementary operating-reality challenge.
- Evidence: [src/recuris/runtime.py#L192](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L192), [src/recuris/grounding.py#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/grounding.py#L1), [src/recuris/metaagent/gates.py#L31](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/gates.py#L31), [src/recuris/metaagent/reachability.py#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/reachability.py#L1).
- Basis: Scoped negative despite substantial independent quality and safety assurance.
- Confidence: Medium-high.
- Caveats: These receipts could be inputs to externally designed S3* but do not establish first-party mandate/closure.

### Absence scope

- Surfaces inspected: Draft truth checkers, GroundingKernel receipts, fingerprint and held-out candidate evaluation, leakage checks, metaagent review records.
- Plausible first-party paths checked: Independent field inspection of task outcomes, contradiction of S1/S3 self-report, independent corrective audit with management feedback.
- Why no material first-party path remains: Quality and candidate-admission checks validate task-level model claims or prospective S4 changes; no separately constituted S3 executive receives a complementary operational reality finding that drives current organizational control.



## S4 — Outside-and-then intelligence

- State: A
- Function: Produce model-generated prospective changes to an agent's reusable skill-memory components from prior task failures and selectively adopt evidence-validated versions into subsequent downstream operations.
- Disturbance / variety regulated: Systematic future task failure classes, memory carrier missing/incorrect invocation, weak procedural cards, task horizon effects and regressions across unseen held-out tasks.
- External distinction: `Driver.evaluate` runs the currently installed memory over training tasks; failures, serialized/sanitized trajectories, mechanism fingerprints and differential evidence reveal operational inadequacies with respect to the environment.
- Future / prospective distinction: A separately configured **upstream model-powered coding meta-agent** consumes evidence and formulates memory package changes `E`, `W`, invocation rule `ρ` or checkers `C` **for later downstream runs**, not merely a redraft of the same current task answer.
- Adaptation option generated: A structured patch plan and concrete disposable candidate package (including memory cards, routing/checkers/working memory), tested for schema, source integrity, mechanism activation and leakage. This model's candidate is an option, not a self-authorized accepted policy.
- Path back into current capability / S3: When deterministic paired held-out improvement/regression criteria pass, `Driver.commit` versions and adopts the candidate package; `_working_base_package` and next-round downstream evaluation use the selected memory. Some *rejected* candidates may be only provisional working bases under explicit progressive rules, not falsely reported as canonically accepted. The return is to **future S1 memory capability**, not an independently established S3 executive.
- Decisive decision or feedback right: Model-backed meta-agent chooses future memory content; code-owned `held_out_paired_gate`, leakage/activation/repair rules and operator-chosen experiment constraints decide admission and subsequent test schedule.
- Decision owner: Upstream configured model through shipped metaagent Driver/launcher and first-party candidate integration; acceptance is deterministic first-party code plus benchmark oracle.
- Supporting / enforcement mechanisms: Sanitized trajectories, diagnosis workers, candidate plan, lint/reachability check, gate with item bootstrap CI and regression cap, immutable checkpoints, committed memory manifests and future run loader.
- Closure path: Downstream trial observation → model diagnosis/patch option → candidate sanity checks and paired held-out comparisons → admit (or reject/provisional) → selected version stored → next downstream run loads new memory → fresh task outcomes.
- Boundary reachability: Documented `recuris metaagent run` starts the packaged `Driver`, `phase_d`/ `phase_p` use configured upstream coding-agent launcher to create actual patches, `gate` checks comparable prior-vs-candidate evidence, `commit` updates the accepted memory base and subsequent `evaluate` loads it for downstream `TurnRuntime`. No new application glue is invented.
- Why this is / is not agent-owned: Without the upstream model, deterministic evaluations and gates could accept/refuse a provided patch but could not generate semantically grounded memory repair from new failure traces. Without the code gate and adoption, the model's suggestions would be non-operational advice; the positive is this source-connected bounded composition.
- Evidence: [README.md#L380](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/README.md#L380), [docs/architecture.md#L79](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/docs/architecture.md#L79), [src/recuris/metaagent/driver.py#L5898](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L5898), [src/recuris/metaagent/driver.py#L7412](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L7412), [src/recuris/metaagent/driver.py#L8268](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L8268), [src/recuris/metaagent/driver.py#L9381](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L9381), [src/recuris/metaagent/driver.py#L9420](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L9420), [src/recuris/metaagent/driver.py#L9677](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L9677), [src/recuris/metaagent/driver.py#L10350](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/driver.py#L10350), [src/recuris/metaagent/gates.py#L31](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/gates.py#L31).
- Basis: First-party integrated prospective model-option→verified selective adoption→future downstream operation path; empirical gain not independently reproduced.
- Confidence: High for source-connected loop, moderate for measured effectiveness.
- Caveats: Meta-agent loop is explicitly run/experiment-budget opt-in, may reject all candidates, and neither benchmark success nor improvement is guaranteed. Human selection of tasks and policy remains external, and S4 positivity does not confer S3/S5 rights.

## S5 — Policy and identity

- State: —
- Function: No internally legitimate, first-party deciding authority resolves ultimate organizational identity/purpose conflicts and returns durable binding policy to the assessed downstream agent organization.
- Disturbance / variety regulated: Data leakage, fake evidence, benchmark invalidity and unsafe memory mutation create integrity concerns; these are guarded by specified constraints rather than autonomous policy-identity judgments.
- Decisive decision or feedback right: Human experimenter sets allowed tools, gate thresholds and frozen oracle/benchmark assumptions; loader and deterministic code refuse invalid changes. Neither current model nor meta-agent is allowed to rewrite the constitution of its own acceptance gate.
- Decision owner: External protocol/user and first-party deterministic enforcement, not a first-party legitimate S5 agent.
- Supporting / enforcement mechanisms: Immutable package identity and integrity digests, plan schema, leakage check, gate policy and tool/write restrictions.
- Closure path: Invalid candidate/action → configured check stops/rejects → continue under original protocol; no ultimate purpose dispute → S5 authority → returned enduring policy revision.
- Why this is / is not agent-owned: Hard-coded gate restrictions, locked benchmarks or a human operator's outside authority do not constitute a model-formed legitimate governance mandate.
- Evidence: [src/recuris/metaagent/gates.py#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/gates.py#L1), [src/recuris/metaagent/integrity.py#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/integrity.py#L1), [src/recuris/metaagent/plan_schema.py#L1](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/metaagent/plan_schema.py#L1), [src/recuris/runtime.py#L192](https://github.com/Gen-Verse/Recuris/blob/7d3745ab787b1206ccd981cb1511100476097266/src/recuris/runtime.py#L192).
- Basis: Bounded negative through normal/opt-in model evolution and safety modes.
- Confidence: Medium-high.
- Caveats: Research team/other deployment organization may hold genuine ultimate policy powers externally; unassessed at this recursion.

### Absence scope

- Surfaces inspected: Integrity/acceptance gates, benchmark/hold-out policy, operator budget and model tool grants, memory manifests and commitment ledger.
- Plausible first-party paths checked: Long-horizon purpose conflicts, constitutional revisions, overriding benchmark acceptance and legitimate identity-setting authority.
- Why no material first-party path remains: The shipped gate enforces externally set research constraints; no first-party decision transaction assigns final organizational identity or returns binding changed policy to operational agents.



## Recursion

S1 is the downstream frozen-model agent executing real tasks with memory. The independent meta-agent's **prospective option creation** supplies bounded S4 to that task-serving capability only when the research/evolution workflow is activated; its diagnosis workers and benchmark trials do not create an independently viable operational federation or delegated S5 at this recursion.

## Variety and escalation

Receipt grounding, stage-aware working-memory bookkeeping and checkers attenuate current task hallucination variety; meta-agent memory editing amplifies prospective solution variety under source-evidenced data/held-out acceptance limits. Run-level errors, a gate rejection or a regression are not automatically algedonic escalation into an autonomous S3/S5 actor.

## Evidence gaps

- This is frozen public source review, **not** independent rerun of Recuris's published benchmark gains; external tau2/SkillFlow/TB2.1 setup, Claude Code coding meta-agent and real provider model services require additional environment/API/simulation budgets. Do not infer reproductions of the paper's reported metrics.
- `TurnRuntime` and the tau2 adapter are concrete first-party integration, while parts of actual LLM runtime and third-party benchmark forks are external. No unsupported first-party ownership of their governance is assumed.
- Normal downstream run does **not** self-edit skill memory automatically each turn; S4 requires opt-in metaagent campaign and an evidence-gated positive candidate. Provisional/rejected working bases are not presented as canonical accepted packages.
- The standalone artifact is `proposed`; no catalog signature or cohort membership is changed until the separately validated canonical admission transaction.
