---
harness_id: kadath
project_name: KADATH
repository: https://github.com/i3T4AN/KADATH
review_ref: db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: P
---

# KADATH

## Review boundary

- System in focus: KADATH's standard evolutionary run: the non-evolving kernel plus the controlled population of evolvable organisms, specialist agents, evidence/grading path, selection, mutation/reproduction, memory, and lineage machinery shipped by the repository.
- Purpose and identity: evolve complete agent frameworks against a user-approved measurable objective while keeping benchmark, grading, lineage, isolation, and evolutionary control outside the evolvable genomes.
- Relevant environment: the user-supplied goal; approved benchmark and measurements; task/tool/browser/search environments encountered by organisms; model endpoints; optional configured external measurement connectors.
- Standard-distribution boundary: the first-party KADATH runtime documented and implemented at the pinned revision, including the kernel, organism runtime, Architect, Grader, Tweaker, Birther, brokered workers, persistence, and container controls.
- Credited operating / distribution surfaces: `kadath/engine.py`, the first-party organism/specialist execution paths, grading/evidence pipeline, selection/mutation/reproduction path, memory/broker path, and the documented `./kadath.sh` standard run.
- Adjacent first-party surfaces excluded from ownership: repository tests, screenshots/assets, deployment examples, and development/CI surfaces. Vendored `smolagents`, model providers, SearXNG, Playwright/browser services, PostgreSQL/MinIO/LiteLLM infrastructure, and optional measurement services are dependencies rather than borrowed VSM owners.
- First-party operating / deployment modes considered: the documented interactive local/self-hosted evolutionary run after the operator approves the Architect-produced benchmark.
- Recursion level: one KADATH evolutionary run as the viable system; heritable organisms are the principal S1 operational units. Temporary workers are subordinate extensions of one organism rather than independent S1 units at this recursion.
- Reviewed revision: `db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

KADATH separates a non-evolving kernel from evolvable organism genomes. The kernel owns run lifecycle, benchmark locks, containers, evidence freezing, formula application, population selection, database/lineage, recovery, exports, and cleanup. Organisms execute the user goal with a complete editable agent framework, persistent workspace and memory, brokered model/tool access, and optional bounded temporary workers. During an epoch the genome is mounted read-only; adaptation is applied only after grading.

An Architect proposes a machine-readable benchmark from the goal and available environment, but the run remains inactive until the operator approves it. Approval locks objective/tool/runtime hashes. After execution the kernel freezes each attempt and a model Grader audits that frozen boundary, extracting rubric facts, automatic-failure decisions, anti-fraud decisions, tie-break inputs, and evidence references. The kernel validates those references and deterministically applies the locked scoring formulas. Grading then feeds population ranking and evolutionary selection. Middle organisms can inspect their own scored behavior and population/elite evidence and autonomously propose changes to their own framework; Tweaker and Birther paths generate reproduction guidance and mutated descendants. The resulting genomes run in subsequent epochs.

Primary evidence: [README architecture and lifecycle](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md), [kernel implementation](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/kadath/engine.py).

## Operational model

The operational outcome is successful task performance by a population of heritable organism agents under a locked fitness definition. Each organism owns the discretionary task-solving loop inside its execution boundary. The kernel constrains resources and mutation timing, freezes evidence, computes locked scores, and enforces selection rules. Specialist model-driven roles are functionally separated from those mechanisms where the evidence supports a distinct organizational function.

## S1 — Operations

- State: A
- Function: heritable organism agents perform the user goal by reasoning, using tools, managing durable progress, producing artifacts/results, and optionally delegating bounded subproblems to temporary workers.
- Disturbance / variety regulated: open-ended task/environment variety encountered while trying to satisfy the approved measurement criterion.
- Decisive decision or feedback right: choose the next reasoning/tool/workspace action and determine the candidate operational result within the organism's allowed capabilities.
- Decision owner: the organism's model-driven agent loop.
- Supporting / enforcement mechanisms: read-only genome mount, scoped broker token, workspace/artifact storage, browser/search tools, worker limits, epoch deadline, resource/container isolation, and the kernel's lifecycle enforcement.
- Closure path: observations and tool/worker results return to the organism; the organism updates durable progress/output and continues acting until the epoch finishes.
- Boundary reachability: organism execution is the standard population runtime created for every approved KADATH run; it does not rely on a development-only or external harness owner.
- Why this is / is not agent-owned: the kernel constrains the action space but does not choose the organism's task-solving actions; those choices are model-driven inside the shipped organism loop.
- Evidence: [inside an epoch and worker behavior](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#inside-an-epoch), [research, browsing, and temporary workers](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#research-browsing-and-temporary-workers).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: temporary workers are subordinate to a parent organism and are not separately credited as S1 units at the declared recursion.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at the declared population recursion.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: per-organism containers, scoped credentials, separate browser contexts, population ranking, and sequencing isolate or compare organisms but do not by themselves regulate a demonstrated interference/oscillation among cooperating S1 units.
- Closure path: not established.
- Why this is / is not agent-owned: population plurality, competition, shared benchmark use, and isolation are insufficient to establish S2 without a specific inter-S1 disturbance and attenuation loop.
- Evidence: [population execution and isolation](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#inside-an-epoch), [isolation and credentials](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#isolation-and-credentials).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a deployment could build cooperative coordination among organisms, but the reviewed standard distribution does not establish the required S2-specific witness.

### Absence scope

- Surfaces inspected: README architecture/lifecycle, organism and worker execution, population lifecycle, isolation, memory/heredity, and kernel implementation surfaces.
- Plausible first-party paths checked: population interaction, shared memory/rating, temporary workers, browser/profile handling, scheduling, isolation, selection, and reproduction.
- Why no material first-party path remains: these paths either subordinate workers to one S1, isolate competing organisms, or rank/select them; the reviewed evidence does not identify a concrete inter-S1 interference/conflict/oscillation plus an attenuation relation that feeds back into subsequent behavior of distinct cooperating S1 units.

## S3 — Inside-and-now control

- State: C
- Function: the kernel maintains a whole-run current-control path over population status and applies ranking, survival/replacement, execution limits, and activation decisions that regulate the current evolutionary organization.
- Disturbance / variety regulated: population failure, uneven verified performance, invalid/duplicate adaptation, runaway execution, and loss of a viable active population.
- Decisive decision or feedback right: determine which verified genomes remain active, which are culled/replaced, and which valid post-grade adaptations become the next active population under the fixed current-control policy.
- Decision owner: the standard runtime exposes this S3-specific control path through developer-authored deterministic kernel policy; no autonomous agent owns the decisive population-control policy in the reviewed mode.
- Supporting / enforcement mechanisms: frozen grading results, deterministic score/rank computation, population-size rules, content-addressed genomes, worktree validation, resource limits, and activation/cleanup machinery.
- Closure path: verified outcomes and ranks enter the kernel selection path; the selected survivors/adaptations/children become the active population for the next epoch.
- Boundary reachability: the selection/activation path is built into the standard kernel and runs after every non-final graded epoch; it is not a CI or example-only construction.
- Why this is / is not agent-owned: Tweaker/Birther and middle agents can propose adaptations, but the whole-population current-control right remains in fixed kernel selection/activation rules. KADATH therefore supplies a concrete S3 construction path without an autonomous S3 owner.
- Whole-system current view: the kernel has run/epoch identities, frozen grading outcomes, ranks, lineage, population membership, crashes, and active genome state for the whole population.
- Current-control decision scope: population survival/replacement/activation and enforcement of run-wide execution constraints; deterministic enforcement is recorded separately from model-driven adaptation proposals.
- Evidence: [evidence freezing and grading](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#evidence-freezing-and-grading), [selection and evolution](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#selection-and-evolution), [kernel implementation](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/kadath/engine.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: `C` does not credit hard enforcement as autonomous management. It records the first-party function-specific current-control path while preserving that the decisive policy is developer-authored rather than agent-owned.

## S3* — Complementary audit

- State: A
- Function: a separate model Grader inspects a frozen evidence boundary rather than ordinary organism self-report, makes rubric/anti-fraud/failure judgments, and returns those findings into population control.
- Disturbance / variety regulated: fabricated, unsupported, fraudulent, crashed, or otherwise invalid claims of task success and misleading organism self-scores.
- Decisive decision or feedback right: make the semantic audit judgments for rubric facts, automatic failures, anti-fraud checks, tie-break facts, and cited evidence from the frozen attempt.
- Decision owner: the model-driven Grader.
- Supporting / enforcement mechanisms: kernel-owned evidence freezing, fragment coverage/checksums, reference validation, integrity seals, and deterministic locked formula application.
- Closure path: Grader findings are validated by the kernel, converted through locked formulas into verified outcome/score/rank, and directly affect selection, culling, and reproduction for the next population.
- Boundary reachability: the Grader/frozen-evidence path is part of every standard grading phase, separate from the evolvable organism genome and reachable without borrowing a development-only reviewer.
- Why this is / is not agent-owned: the kernel does not itself make the semantic evidence judgments; it freezes evidence, validates references, and applies formulas. Removing the Grader leaves those discretionary audit judgments absent.
- Claim being audited: the organism's claimed task outcome and evidence satisfy the approved benchmark without triggering failure/anti-fraud rules.
- Ordinary reporting path: organism result envelope, workspace/artifacts, high-level activity, tool/model traces, worker outputs, and provisional result material produced during execution.
- Complementary access path: kernel-created immutable frozen attempt including artifacts, traces, browser/worker evidence, crash/identity metadata, exact objective/genome hashes, and optional independent measurement facts.
- Independence boundary: the Grader operates after all parents/workers are stopped, against frozen evidence; organisms cannot rewrite the benchmark, score, scheduler, lineage, or frozen post-run evidence and self-scores are explicitly ignored.
- Who acts on findings: the kernel validates the audit references, computes locked scores/ranks, and uses them in population selection and reproduction.
- Evidence: [evidence freezing and grading](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#evidence-freezing-and-grading), [selection and evolution](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#selection-and-evolution).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the deterministic kernel owns formula application and enforcement, not the model Grader's audit judgment; this split is why the audit is not inferred merely from the component name `Grader`.

## S4 — Outside-and-then intelligence

- State: A
- Function: the evolutionary adaptation loop turns verified environment/benchmark performance and evidence from the current population into changed agent frameworks for future epochs.
- Disturbance / variety regulated: mismatch between present organism capability and the externally measured performance demanded by the locked task environment/benchmark.
- Decisive decision or feedback right: choose adaptation proposals for future capability: middle organisms may mutate or remain unchanged; Tweaker/Birther paths derive reproduction guidance and mutated children from verified population evidence.
- Decision owner: model-driven organism/specialist adaptation actors within the shipped evolutionary loop.
- Supporting / enforcement mechanisms: kernel grading/ranking, elite dossiers and snapshots, population/own/inherited memory, mutation validation, duplicate rejection, Git lineage, and next-epoch activation.
- Closure path: verified performance/evidence informs model-driven mutation/reproduction choices; valid changed genomes are committed and activated; subsequent epochs execute those changed capabilities against the environment.
- Boundary reachability: middle-agent reflection and Tweaker/Birther reproduction are standard post-grade phases of the shipped run rather than separate development tooling.
- Why this is / is not agent-owned: deterministic selection and mutation safeguards constrain candidates, but the substantive adaptation proposals are produced by model-driven actors from verified evidence.
- External distinction: observed, frozen, independently graded performance and evidence under the approved benchmark/tool/environment configuration.
- Future / prospective distinction: which framework characteristics, memories, and mutations are likely to improve performance in subsequent epochs.
- Adaptation option generated: preserve, mutate prompt/source/dependencies/files, or reproduce a mutated descendant from an elite genome.
- Path back into current capability / S3: the kernel validates and commits accepted mutations, restores the configured population, and activates the changed genome set for the next epoch.
- Evidence: [middle-agent reflection, Tweaker and Birther](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#middle-agent-reflection), [memory and heredity](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#memory-and-heredity).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this credit is not based on the label `evolution`; it depends on a closed future-capability loop from measured environment performance to changed genomes that actually run later.

## S5 — Policy and identity

- State: P
- Function: establish and lock the run-level definition of success, permitted evidence/tools, anti-fraud constraints, and measurement policy that governs every organism and evolutionary selection decision.
- Disturbance / variety regulated: ambiguity or drift in what the evolutionary organization is optimizing and what evidence/behavior counts as legitimate success.
- Decisive decision or feedback right: approve or reject the Architect's proposed benchmark before activation; once approved, the benchmark/objective/tool/runtime hashes are locked for the run.
- Decision owner: the human operator as parent authority for the run.
- Supporting / enforcement mechanisms: Architect proposal generation, structured benchmark contract, preflight, immutable hash locks, and runtime refusal to continue after locked-input tampering.
- Closure path: operator approval activates and locks the policy; the locked benchmark subsequently governs grading, ranking, selection, and all future epochs. Rejection leaves the proposed run inactive.
- Boundary reachability: benchmark proposal and explicit approval are part of the standard interactive launch path, not repository governance or an adjacent development process.
- Why this is / is not agent-owned: the Architect proposes policy content but does not hold ultimate activation authority; there is no evidenced standard mode in which an agent can unilaterally redefine and authorize the run's ultimate fitness policy.
- Identity / ultimate-policy issue: what the whole evolutionary run exists to optimize, what measurements define success, and which anti-fraud/tool/evidence constraints bind the population.
- Ultimate authority in each claimed mode: parent mode only — the human operator approves the benchmark that becomes authoritative for the run.
- Return-to-operation path: approved benchmark and hashes become immutable runtime inputs to grading, ranking, and evolutionary selection across all epochs.
- Evidence: [Architect and benchmark locking](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#architect-and-benchmark-locking), [run setup and approval](https://github.com/i3T4AN/KADATH/blob/db7a6438d98c18d590b78b2146dc3bcd2c4ea0ef/README.md#what-happens-when-a-run-starts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary organism result approval is not being called S5. The credited parent decision is the run-wide, persistent fitness/legitimacy policy that controls the identity of the evolutionary process.

## Recursion

The declared system is one KADATH evolutionary run. Heritable organisms are S1 units at that recursion. A temporary worker is nested under one organism and cannot grade, reproduce, mutate its parent, or become independently heritable, so worker spawning alone is not treated as an additional viable recursion. Each evolved genome could itself contain internal organization, but that would require a separate boundary-specific assessment.

## Variety and escalation

KADATH attenuates variety through isolated execution, scoped credentials, deadlines/resource limits, immutable benchmark locks, evidence freezing, deterministic formula application, duplicate mutation rejection, and population-size restoration. Failures and crashes are retained as evidence; failed organisms are preferentially culled. The run can terminate cleanly when every organism fails and no verified genome remains. The operator's pre-run benchmark approval is the evidenced parent policy path; ordinary runtime failures do not create additional S5 credit.

## Evidence gaps

- S3 is classified `C` because the whole-population current-control path is concrete but its decisive policy is fixed/developer-authored; reassess if KADATH adds an autonomous manager that owns population resource/priority/intervention decisions rather than merely adaptation proposals.
- Reassess S2 if a first-party population mode introduces cooperating S1 units with an explicit conflict/oscillation witness and a coordination result that changes later unit behavior.
- Reassess S5 if a supported mode allows an autonomous actor to authorize or revise the run-level objective/fitness policy without parent approval, or exposes a distinct constructor mode for that ultimate-policy right.
