---
harness_id: autoresearchlab
project_name: AutoResearchLab
repository: https://github.com/TaewiKim/autoresearchlab
review_ref: bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A(P)
autonomy_s5: —
---

# AutoResearchLab

## Review boundary

- System in focus: The self-hosted AutoResearchLab **research-program cycle** that takes a research direction, acquires field evidence, selects a problem, designs and runs experiments, challenges the results, revises decisions, and prepares a reviewed result. The system is the orchestration of its own agent roles, not the external Codex implementation or a scientific community being studied.
- Purpose and identity: Produce a falsifiable and independently reviewed research result, including negative/inconclusive outcomes, under an owner-specified domain and bounded runtime budget. The source explicitly calls the release an early preview and does not claim a published research result.
- Relevant environment: Scientific literature, changing field beliefs/frontiers, datasets, reproducibility constraints, external tools and packages, researcher instructions, computational resource limits, and competing scientific hypotheses.
- Standard-distribution boundary: Shipped `bin/researchlab` → Node CLI/runtime → Rust `researchlab-harness` role scheduler → Codex CLI role lanes and first-party Python drivers; local `.research-lab/` artifacts and the documented Docker/native installation. Model/provider services, remote scholarly registries, external source repositories, human research institutions and unpublished actual-cycle outcomes are outside first-party ownership.
- Credited operating / distribution surfaces: [CLI entry](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/bin/researchlab#L1-L10), [runtime seams](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/docs/architecture.md#L16-L36), [agent plan and owned roles](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/agents/lab_director/agent_plan.js#L161-L223), [first-party selection dispatcher](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/dispatch.rs#L280-L353), [review aggregation](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/reporting/reviews/gate/gatekeeper_reviews.js#L175-L349), and [role communication](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/reporting/message_bus/channels.js#L43-L96).
- Adjacent first-party surfaces excluded from ownership: Benchmarks and example answers under `evals/`, source test fixtures, code-maintainer interventions and optional maintainer Codex patching, repository GitHub/CI governance, author-reported performance anecdotes in architecture comments, and published-paper claims from the README. These may corroborate code reachability but do not supply operational outcomes or another VSM owner.
- First-party operating / deployment modes considered: Native or Docker self-hosted CLI with configured Codex auth; default agent-owned LabDirector/scout/analyst/engineer/runner/gatekeeper lanes; explicit researcher candidate selection; documented timeout-based auto-selection; optional maintainer disabled by default. No model-backed lane was run for this assessment.
- Recursion level: One complete research-program cycle. Role lanes have local outcomes but do not automatically become independently viable nested organizations; the external experimental code/package is a tool or subject of research, not a separate first-party VSM level.
- Reviewed revision: `bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8` from [Index frozen intake #2000](https://github.com/opensiro/vsm-harness-index/issues/2000) and [serial batch #2001](https://github.com/opensiro/vsm-harness-index/issues/2001).
- Observation date: 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The JavaScript CLI constructs agent roles and prompts, a Rust scheduler materializes and dispatches role lanes, and Python search/analysis drivers operate as bounded external subprocesses. Each role lane has its own task, plan, run record and result, and state is persisted for resume. LabDirector controls scientific lead/refine/pivot/conclude choices; Scout acquires papers/datasets; Chronicle synthesizes evidence; Analyst specifies experiments; Engineer provisions capabilities; Runner executes the preregistered design; independently dispatched Gatekeepers adjudicate scientific quality; Author and Illustrator prepare reports. A supervisor/watchdog detects stalls and may raise a request but explicitly must not substitute its own scientific judgment for LabDirector's. See [documented roles and rights](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/docs/AGENTS.md#L7-L48), [execution split](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/docs/architecture.md#L16-L69), and [supervisor/role separation](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/docs/AGENTS.md#L80-L112).

The research question is developed from a first-party landscape/SOTA-card gate into a field-belief map and a deliberately instrument-blind candidate slate. A Gatekeeper panel evaluates options; novelty and feasibility checks follow; the researcher may select a surviving lead, with a supported timeout fallback. The selected lead becomes a hypothesis for Analyst/Engineer/Runner, after which three independent Gatekeeper review rubrics can block acceptance and return specific work to LabDirector. A message bus and append-only ledgers preserve role requests, decisions, and feedback; these transport/enforcement systems are not themselves attributed agent discretion. See [source selection stages](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/dispatch.rs#L280-L370), [owner gate](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/gate.rs#L159-L189), and [gate returns](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/reporting/reviews/gate/build.js#L83-L130).

## Operational model

Operational S1 work consists of the scientific work cells: field/evidence collection, experiment design and engineering, sealed measurement, and research-document production. They hold bounded agent choices within their own deliverables; the Rust scheduler makes tasks available and enforces constraints but does not perform the scientific inference. LabDirector is the present-cycle metasystem decision path; independent Gatekeepers challenge quality claims before they become final. The program's outside-and-then path uses field evidence to revise which research direction the current lab will pursue; a separately supported human choice governs one mode of that agenda selection.

## S1 — Operations

- State: A
- Function: Autonomous role lanes produce scoped scientific work: locate and evaluate evidence, design a falsifiable experiment, provision execution, run analysis, and write defensible results.
- Disturbance / variety regulated: Unfamiliar academic domains, unavailable tools/datasets, conflicting data quality, unanticipated engineering failures, analytical alternatives and result uncertainty.
- Decisive decision or feedback right: Scout agents choose/refine field-specific queries, Analyst chooses estimands and tests, Engineer chooses how to provision the selected toolchain without altering the science, and Runner writes/runs the contract-bound analysis; their outputs determine subsequent experimental work.
- Decision owner: Configured model-backed role agents operating through the first-party lane contracts; external Codex CLI executes the model sessions but its mere availability does not establish additional first-party S-functions.
- Supporting / enforcement mechanisms: Rust lane dispatch, role-scoped sandboxes, sealed contracts/artifacts, runtime state and deterministic validity checks.
- Closure path: Role plan → agent work/result artifact → contract and gate checks → next role uses the output or reports a blocker to the director → subsequent experiment/review changes accordingly.
- Boundary reachability: The shipped CLI and agent plan construct these Codex role lanes, the native harness runs them and persists returned results; these are not example-only or CI-only role stubs.
- Why this is / is not agent-owned: Agents possess bounded scientific and implementation discretion; queue/budget enforcement and filesystem persistence are deterministic supports, not the source of their scientific choices.
- Evidence: [role rights](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/docs/AGENTS.md#L20-L40); [reasoning roles in shipped plan](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/agents/lab_director/agent_plan.js#L228-L283); [native lane entry](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/main.rs#L31-L60).
- Basis: Structural shipped agent-role/decision and result-return paths, supplemented by explicit source-owning architecture descriptions.
- Confidence: High for first-party configurability and decision ownership, not a measurement of model effectiveness.
- Caveats: No live Codex/LLM agent, scholarly API or actual research experiment was run in this assessment; science quality is not a VSM autonomy grade.

## S2 — Coordination

- State: ?
- Function: Candidate stabilization of cross-role experiment/review work, but a separately established inter-S1 oscillation-attenuation *function* remains ambiguous at the declared recursion.
- Disturbance / variety regulated: Competing author experiment requests, engineering/analysis handoff dependencies, status messages crowding other channels and duplicate/superseded work may disrupt delivery to other scientific units.
- Decisive decision or feedback right: The bus carries author→director requests and enforces per-channel capacity, unique identity, delivery receipts and escalation; LabDirector can adopt/decline experiments with reasons. It is not established that the latter is a **distinct inter-S1 damping** decision rather than S3 prioritization and sequential task handoff.
- Decision owner: Agents answer substantive requests, but deterministic bus/scheduler implements capacity, escalation and delivery; S2-specific ownership is unresolved.
- Supporting / enforcement mechanisms: Request/standing channel registry, per-channel quotas, stateful deduplication, escalations, lane sequencing and contract-bound handoffs.
- Closure path: Author request → bus → director response → changed experiment/document plan is plausible, but the reviewed evidence does not separate this from hierarchical current-control return sufficiently for an autonomous S2 claim.
- Why this is / is not agent-owned: Actual feedback messages and decisions exist; their S2-specific function and direct reciprocal stabilization of distinct operational units cannot be inferred merely from those mechanisms.
- Evidence: [author request with owed reason](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/reporting/message_bus/channels.js#L43-L96); [per-channel capacity and delivery](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/reporting/message_bus/index.js#L3-L49); [projection and return](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/reporting/message_bus/index.js#L249-L291); [documented channel history](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/docs/architecture.md#L71-L128).
- Basis: Structural coordination candidates; unknown function-specific inter-S1 relation.
- Confidence: Medium that coordination machinery exists; low on attribution of a separate S2 function.
- Caveats: The specific unresolved witness is two independently operating S1 cells whose *mutual interference*, rather than a parent backlog/approval dependency, is attenuated through an accountable, closed S2 path.

## S3 — Inside-and-now control

- State: A
- Function: Regulate present scientific commitments and next work for the entire current research program, responding to failed reviews, stalled runs, evidence gaps and competing follow-up demands.
- Disturbance / variety regulated: Expensive repeated analyses, weak lead hypotheses, unresolved gate blockers, scientific stagnation, contradictory handoffs and limited lane budget/time.
- Decisive decision or feedback right: LabDirector selects/refines/pivots/concludes a research lead and chooses follow-up scientific tasks, based on Chronicle, current gate results and supervisor notices; it may not override independently recorded reviewer scores.
- Decision owner: The model-backed LabDirector agent for scientific priority/correction. Supervisor stall detection, Rust dispatch/termination, budgets and hard rubric gates constrain or request action but do not own that scientific decision.
- Supporting / enforcement mechanisms: Cycle-wide summaries and notes, request escalations, lane priority/dispatch, budget and stagnation guards, protected lead memory, append-only feedback.
- Closure path: Whole-cycle evidence/active review blocker → director's scientific correction/pivot/priority decision → role task/lead updates → scheduler launches affected subsequent lanes → newer results are reviewed again.
- Boundary reachability: The default agent plan includes a LabDirector across stages, and the native cycle uses its lead decisions and reviewer feedback to create follow-ups; not a maintainer-only or external governance workflow.
- Whole-system current view: Chronicle digest, evidence/decision notes, active blockers, gate review and lane/cycle states across the same research-program boundary.
- Current-control decision scope: Next research work, which lead/claim is current, which further measurements or corrections are owed, and whether to pivot or conclude under the fixed scientific and resource constraints.
- Why this is / is not agent-owned: The director has substantive authority to adjudicate scientific commitments; a deterministic forced-stall request cannot replace its selection of a scientifically justified next hypothesis.
- Evidence: [director role and limits](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/docs/AGENTS.md#L20-L30); [agent plan duty](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/agents/lab_director/agent_plan.js#L185-L197); [active blocker review return](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/reporting/reviews/gate/build.js#L83-L130); [source-bound strategy decisions](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/plan/run_loop.rs#L1001-L1070).
- Basis: Explicit role contract plus structural gate→decision→followup path.
- Confidence: Medium-high for source-wired current control; no live effectiveness evidence.
- Caveats: Forced livelock termination and resource enforcement are deterministic. Owner instructions can constrain individual choices, but ordinary operator steering does not by itself establish a distinct closed S3 parent mode.

## S3* — Complementary audit

- State: A
- Function: Independently challenge the producing research roles' hypothesis, validity, technical/reproducibility and reporting claims before acceptance.
- Disturbance / variety regulated: Novelty overclaims, unsound analysis, stale evidence, unreplicated results, and a production lane's optimistic interpretation of its own outputs.
- Decisive decision or feedback right: Separately dispatched Gatekeeper model agents assess current bound evidence and return `approve`/`challenge`/`reject`, rubric scores and missing validations; their judgments cannot be overwritten by LabDirector.
- Decision owner: Independent Gatekeeper agent lanes; deterministic rubric parsing, conjunctive gates and scheduling enforce the returned review, without claiming autonomous judgment for the scorer code itself.
- Supporting / enforcement mechanisms: Separate lane state, current-lead/validation binding, reviewer role split, sealed panel reports, structural rubric gates and append-only review history.
- Closure path: Producing roles' claim and validation artifacts → separate reviewer access/judgment → gate objections and rejection persisted → LabDirector receives binding scientific blockers and chooses changed investigation/followup → subsequent review of revised evidence.
- Boundary reachability: Gatekeepers are included in the normal agent plan and their result parsing/aggregation is wired into the production review path; this is not CI testing or a developer-only quality script.
- Claim being audited: Research lead's purported novelty, technical validity, reproducibility, measured results and completeness of evidence.
- Ordinary reporting path: Analyst/Runner outputs and LabDirector/Chronicle research summary.
- Complementary access path: Separate gatekeeper prompts bound to the current lead and validation artifacts, literature graph and prior reviews; independent rubric outputs and objections.
- Independence boundary: Distinct role/lanes, sealed review collection and prohibition on director score override, though all may use the same external model family; independence is **organizational/role**, not proof of model independence or external peer review.
- Who acts on findings: LabDirector for scientific replanning; native gate enforces publication/promotion hold until sufficient review.
- Why this is / is not agent-owned: Model-backed reviewers choose scientific objections and verdicts with their own role contracts. The JS aggregator applies those decisions but does not generate the underlying audit judgment.
- Evidence: [separation of powers](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/docs/AGENTS.md#L42-L49); [independent lane design](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/docs/AGENTS.md#L80-L92); [gatekeeper plan](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/agents/lab_director/agent_plan.js#L212-L225); [review parsing and provenance](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/reporting/reviews/gate/gatekeeper_reviews.js#L112-L171); [review objections/return](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/src/reporting/reviews/gate/build.js#L83-L130).
- Basis: Explicit source boundary plus executable reviewer-lane/result-return structure.
- Confidence: Medium-high on first-party complementary audit mode, not on external peer-review quality.
- Caveats: A Gatekeeper may see summaries rather than independently replaying an experiment; S3* positive is narrowly complementary access through separate role, literature/review evidence and scientific corrective return, not a claim of adversarial execution of the raw dataset on every run.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: Model a changing scientific field and generate future research-agenda options from its beliefs, gaps and frontier, returning selected options into the current program's experimental capabilities.
- Disturbance / variety regulated: New competing hypotheses and publications, oversaturated or already-solved research questions, uncertainty about future impact and which experimental directions deserve commitment.
- Decisive decision or feedback right: Agent-owned Scout/LabDirector field/belief/candidate synthesis and independent expert comparisons develop future-facing research options. A supported timeout mode automatically promotes the highest eligible ranked survivor; a distinct normal mode lets the researcher choose from the same evidence-grounded candidate slate, after which LabDirector operationalizes the choice.
- Decision owner: Autonomous research agents own the external interpretation, slate and expert judgments in the base mode; the legitimate cycle-owning human explicitly owns the final agenda choice in the supported selection mode. Rust gate merely enforces the chosen candidate and resumes work.
- Supporting / enforcement mechanisms: Field landscape quality gate, SOTA cards, instrument-blind candidate slate, sealed expert panel, novelty refutation, feasibility anchors, owner pause/selection file and timeout policy.
- Closure path: Field literature/frontier → SOTA/beliefs → agent-created candidate futures → panel and novelty/feasibility filtering → automatic survivor or parent-selected candidate → LabDirector lead and reproduction anchor → current Analyst/Engineer/Runner work changes.
- Boundary reachability: Expert selection is dispatched by the first-party native program when a lead is absent and its landscape/cards are ready; the published owner pause and timeout are supported runtime paths, not research-paper suggestions.
- External distinction: Newly examined scientific claims, field-wide paper frontiers, contradictions, open problems and external assets in the requested research field.
- Future / prospective distinction: A ranked set of *not-yet-undertaken* research programs designed to change accepted beliefs, evaluated for novelty, uncertainty and feasible reproduction.
- Adaptation option generated: Alternative research hypotheses and experiment programs, including cross-field/bottleneck paths; the selected candidate changes the research lab's lead and required future experiment capabilities.
- Path back into current capability / S3: The selected-vetted candidate is supplied as the bound new lead and next reproduction work in the director's current-control path, constraining subsequent role task creation.
- Why this is / is not agent-owned: Agent roles make the field/option judgments, with an operational automatic option; separately the user has a genuine alternative supported decision right, so `(P)` is not inferred merely from a configuration knob.
- Evidence: [source landscape selection engagement](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/dispatch.rs#L109-L140); [instrument-blind slate](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/dispatch.rs#L280-L353); [owner choice return to lead](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/gate.rs#L159-L189); [runtime owner checkpoint](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/owner.rs#L284-L355); [timeout selection](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/owner.rs#L435-L507).
- Basis: Structural source paths for field-informed future agenda and two alternative supported selection owners.
- Confidence: Medium for S4 ownership boundary; high for the existence of selection paths.
- Caveats: This is prospective adaptation of a research **program's agenda**, not proven autonomous redesign of AutoResearchLab's own software, model weights or deployment. Whether the optional timeout is enabled is configuration-dependent; no live literature search or model evaluation was run.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | LabDirector/panel model agents develop and rank the prospective slate; the configured automatic survivor rule selects from their eligible output | Eligible frontier/slate, with configured owner timeout | Selected survivor reaches the next director lead/experiment | [dispatch](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/dispatch.rs#L280-L370), [timeout](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/owner.rs#L443-L507) |
| Parent (`P`) | Research program owner chooses a vetted alternative/release and can revise choice | Published owner selection checkpoint / later reselection | Selection is recorded, constrains LabDirector's current lead and subsequent experiment | [checkpoint/reselection](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/owner.rs#L328-L435), [lead binding](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/gate.rs#L159-L189) |

## S5 — Policy and identity

- State: —
- Function: No separately established first-party ultimate identity/policy arbitration with a closed decision-return path at the research-program recursion.
- Disturbance / variety regulated: User research directions and binding owner directives affect venue, method count, project preferences and evidentiary discipline, but these are program/task priorities and source-quality constraints rather than a demonstrated ultimate-policy dispute.
- Decisive decision or feedback right: The owner may submit a research request, select the lead, and record binding instructions with reasons. No shipped role or explicit parent path adjudicates a conflict over the institution's identity/ultimate policy as distinct from research-agenda/current-control decisions.
- Decision owner: External research owner supplies task/domain/program preferences; validity controls enforce them without acquiring ultimate-policy discretion.
- Supporting / enforcement mechanisms: Research request/configuration, owner-directive file, role prompt injection, scientific score rules and selected-candidate enforcement.
- Closure path: Owner research instructions → role task constraints and agenda decisions. Missing identity-level issue → legitimate policy deliberation/decision → governing policy returned to subsequent program operation.
- Why this is / is not agent-owned: A binding preference and research agenda selection are material parent decisions, but not automatically S5. A static instruction or scientific gate also cannot own ultimate policy merely by enforcement.
- Evidence: [owner directives and scope](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/runtime/owner_directives.rs#L1-L21); [binding role clause](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/runtime/owner_directives.rs#L102-L125); [owner research selection](https://github.com/TaewiKim/autoresearchlab/blob/bd70a67aafa172a4e7c5a3f4477d6e438cfeb0d8/native/researchlab-harness/src/labdirector/problem_selection/gate.rs#L159-L189).
- Basis: Bounded source-first negative after distinguishing parent agenda and scientific control from true ultimate-policy authority.
- Confidence: Medium-high within the supported single research-program boundary.
- Caveats: A human university or research institution can exercise a higher-recursion S5 outside the software; no organizational parent mode is imported from its mere possible presence.

### Absence scope

- Surfaces inspected: CLI/research input, documented role rights, LabDirector/panel/gate system, explicit owner selection, runtime owner directives and first-party policy/guard code.
- Plausible first-party paths checked: Human selection as program-identity governance; binding owner directive as ultimate policy; scientific gatekeeper as policy arbiter; maintainer/CI restrictions as S5.
- Why no material first-party path remains: These sources govern individual scientific commitments, candidate agenda and evidence requirements but do not supply a distinct identity/ultimate-policy matter, legitimate final adjudication and binding return for the research-program organization.

## Distributed OSS parent arrangement

Multiple contributors and optional local maintainer agents are not imported into the assessed research cycle. A single researcher has genuine in-cycle agenda selection authority (S4 parent mode), but project-level OSS maintainership, provider policies and institutional governance do not by location alone establish S3/S4/S5 ownership at this recursion.

## Self-hosted and non-human modes

The shipped product is self-hosted with configured Codex CLI lanes, plus Python drivers and Rust deterministic guard machinery. The documented owner checkpoint has an alternate timeout auto-selection path. No claimed autonomous state is inferred from the separate optional maintenance agent or from benchmark/test fixtures. No external agent execution occurred in this assessment.

## Recursion

The whole research cycle is the unit of analysis. Role lanes have specific tasks, outputs and local environments, but spawning three gatekeepers, several scouts and a worker pool does not by itself prove additional complete viable systems. Gatekeeper independence is evaluated as a complementary audit relation in this declared program, not as an extra S1 organization.

## Variety and escalation

The field-map/SOTA funnel amplifies external distinctions; instrument blindness attenuates opportunity-selection bias. First-party gatekeeping detects unsupported results, while provenance contracts limit relabeling and repeated measurement. Supervisor stalls, author experiment requests and gate objections reach LabDirector through recorded feedback; watchdog/queue status is not an extra VSM function or automatic algedonic authority. Researcher candidate selection is a supported parent strategic option with actual return to research work.

## Evidence gaps

- S2 remains `?`: bus starvation/duplicate-request controls and scientific role handoff revisions are real, but their S2-specific closure for two independently viable S1 operations (distinct from S3 current prioritization) is not established at this recursion.
- S4 `A(P)` is narrowly a **research-agenda** adaptation mode. Neither autonomous evolution of the AutoResearchLab code nor a durable cross-cycle capability-improvement loop is claimed.
- The reviewed README says early preview and no published result. Source paths and deterministic tests can substantiate implemented control flow; they do not independently attest model-backed successful science, subjective agent quality, actual reviewer independence against collusion, or a completed real research cycle.
- Offline-only source checks: `node --test tests/message_bus.test.js tests/gate_review.test.js tests/gate_rubric_ownership.test.js tests/hypothesis_pipeline_hardening.test.js` passed (four test files). No Codex, LLM provider, Browser, network scholarly lookup or live benchmark ran.
