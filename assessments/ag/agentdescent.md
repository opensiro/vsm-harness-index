---
harness_id: agentdescent
project_name: AgentDescent
repository: https://github.com/Birfy/agentdescent
review_ref: d1cfa8f6eb570d927826278c70aa23b86d3c5264
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

# AgentDescent

## Review boundary

- System in focus: **First-party AgentDescent model-backed evolution harness** in its packaged `evolve()` agent/reflector mode: an operating solver runs user-provided tasks, a model-backed proposer reflects on failure, parallel worker proposals are measured and merged into a version-controlled evolving skill/prompt/harness artifact, and later workers read the accepted version. This is one evolution **operating organization**, not the external enterprise deploying the resulting agent or an abstract ecosystem of all algorithm ports.
- Purpose and identity: Produce and improve an agent's reusable behavior through task/reward feedback and evidence-gated durable changes to an executable prompt, skill or harness artifact.
- Relevant environment: Diverse task inputs, feedback/rewards, changing task competence, candidate edits, same-key diff interference, stale concurrent worker versions, oracle/held-out checks, model backend errors and compute budgets.
- Standard-distribution boundary: Published Python package `agentdescent`, especially `evolution.py` (shipped `LLMAgent`, `reflector`, `_build_engine`, `evolve` and round worker), `agents.py` (provider adapters), `aggregator.py` and `defaults.py` (evidence cards and commit decision), `fusion.py` (optional model-based merge), `ledger.py`, `verifier.py`, `governance.py`, `async_evolve.py`, `harness.py`, and CLI `demo.py`. Optional algorithm policies must be linked to a documented supported operational path to contribute ownership.
- Credited operating / distribution surfaces: [README.md#L49](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/README.md#L49), [agentdescent/evolution.py#L120](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L120), [agentdescent/evolution.py#L206](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L206), [agentdescent/evolution.py#L2270](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L2270), [agentdescent/evolution.py#L2795](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L2795), [agentdescent/evolution.py#L3686](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L3686), [agentdescent/aggregator.py#L675](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L675), [agentdescent/aggregator.py#L1412](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L1412), [agentdescent/ledger.py#L1](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/ledger.py#L1), [agentdescent/governance.py#L70](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/governance.py#L70), [agentdescent/demo.py#L1](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/demo.py#L1).
- Adjacent first-party surfaces excluded from ownership: Research papers and performance tables, tests/CI, experiment orchestration scripts outside the packaged wheel, benchmark/test dataset selection, a developer's downstream organization deploying the evolved strategy, external Pydantic/Claude/OpenAI-compatible model providers, unchosen alternative policies, GitHub maintainer/release governance, and third-party human L0 authorities. The published model-call adapter and its model feedback path count as a shipped composition even though provider weights and service governance are not first-party.
- Operating/deployment modes considered: Packaged `evolve(tasks,reward,agent=LLMAgent(complete),strategy=...)`; the equivalent `run=...` plus `propose=reflector(complete)` path; parallel workers with a round barrier, asynchronous evolution, pluggable default and reflective fusion, configurable held-out/scorer and budget policies, Git-backed ledger and packaged CLI/offline demo. External custom `run` and `propose` functions alone do not prove first-party autonomous ownership, nor do names of unused optional algorithms.
- Recursion and S1 boundary: Each model-backed solver/worker task/rollout is an operational S1 unit at the **learning harness's immediate task-processing recursion**. Multiple workers are parallel candidate experimenters of one evolving artifact, not by themselves separately viable departments delivering an independent external service. The assessed S4 is the model's separate prospective change-of-future-capability path, not the solver's next immediate tool call.
- Frozen source identity: Public GitHub repository ID **1311085469**, default branch `main`, SHA `d1cfa8f6eb570d927826278c70aa23b86d3c5264`, tree `790720ebeee90735cdb924a04efebe5c065d8867`; [batch #1738](https://github.com/opensiro/vsm-harness-index/issues/1738). Root LICENSE is MIT; packaged `pyproject.toml` declares `MIT AND Apache-2.0` owing to adapted RRSI subtree. Reviewed 2026-10-19, active Profile 0.2.4 / Methodology 0.3.7.

## Repository architecture

The shipped `LLMAgent.solve` invokes `Completion` with rendered artifact and task, and `LLMAgent.propose` uses the same model-completion adapter to reflect on the observed output, reward and expected-answer evidence to produce a candidate rule. `_build_engine` actually wires `agent.solve` and `agent.propose` when supplied, or requires `run` and `propose` / a concrete proposal policy; it constructs a ledger, verifier and aggregator. This is a supported integrated runtime path, not an unconnected interface. External LLM providers are accessed through published `Completion` adapters and remain external service actors. [agentdescent/evolution.py#L120](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L120); [agentdescent/evolution.py#L206](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L206); [agentdescent/evolution.py#L2250](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L2250); [agentdescent/agents.py#L1](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/agents.py#L1).

In synchronous `evolve`, each work unit snapshots an artifact, executes its task rollout using `eng.executor.rollout`, records `score`, invokes the model-backed `propose` with output and score when task is not solved, converts it to a `Diff`, optionally self-verifies and inserts an `EvidenceCard` into the aggregator. The aggregator drains cards, rejects oversized/stale candidates, resolves same-key conflicts and selects/combines candidate diff(s), checks artifact invariants, compares measured held-out reward and writes accepted changes to the Git-backed ledger. Subsequent workers snapshot the newly accepted head. The deferred/async runtime supports related semantics without changing the ownership claim. [agentdescent/evolution.py#L3649](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L3649); [agentdescent/evolution.py#L3730](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L3730); [agentdescent/evolution.py#L3790](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L3790); [agentdescent/aggregator.py#L1426](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L1426); [agentdescent/aggregator.py#L1570](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L1570); [agentdescent/aggregator.py#L1613](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L1613).

The separate `governance.py` L0 frozen-artifact invariant prevents the optimizer from rewriting its own oracle/policy, while `L1SerialGate` is explicitly documented as a **not-yet-wired** primitive and cannot be credited as a live runtime owner. `audit` and held-out verification provide quality evidence and statistical gates for candidate acceptance; their naming is not an autonomous S3*/S5 mandate. The packaged `demo.py` substitutes deterministic subprocess solver/reflector for actual model cognition and is only an offline pipeline test, not live LLM-performance evidence. [agentdescent/governance.py#L75](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/governance.py#L75); [agentdescent/governance.py#L94](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/governance.py#L94); [agentdescent/governance.py#L134](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/governance.py#L134); [agentdescent/demo.py#L1](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/demo.py#L1).

## Operational model

The task-facing solver is the operating component. The evolution layer changes the solver's future instructions/skill/harness artifact based on observations outside an individual task; the committed version influences new rollout instances. Static merger policy, concurrency/snapshot locks, budget accounting and policy constraints are distinct from both the model solver's operating choice and the model reflection's prospective choice.

## S1 — Operations

- State: A
- Function: Produce model-selected responses to heterogeneous tasks using the current candidate reusable skill/prompt artifact, and obtain outcome feedback.
- Disturbance / variety regulated: Different task prompts and expected outputs, current skill weaknesses, uncertain model responses and live per-task result variance.
- Decisive decision or feedback right: The `LLMAgent.solve` model, reached by `_build_engine` and `eng.executor.rollout`, produces a contextual answer from the rendered strategy and task; the scorer observes that answer and the same run may then change its candidate strategy through a separate reflection path.
- Decision owner: Configured model through shipped `LLMAgent` and `Completion` adapter; the harness supplies the call route and feedback, whereas a test/demo's scripted `offline_agent` is not proof of model inference.
- Supporting / enforcement mechanisms: Task and input formatting, scorer, workers/parallel task sampling, executor, candidate render, provider request/usage adapter and run/result logs.
- Closure path: Active artifact snapshot + selected task → `LLMAgent.solve` `complete` → task response → scored outcome / recorded trajectory → subsequent task operation and separate prospective proposal if wrong.
- Boundary reachability: The package exports `LLMAgent` and `evolve`, `_build_engine` binds `agent.solve` to the rollout executor, and public documented examples use `run=...` / `propose=reflector(model)`; the decisive modeled act is supported in shipped first-party composition, even though the selected provider is external.
- Why this is / is not agent-owned: Removing the model from the supported `LLMAgent` path leaves sampling, persistence and reward arithmetic but not contextual task-response synthesis. The model's answer is the S1 decision, not the merge gate's numerical acceptance.
- Evidence: [agentdescent/evolution.py#L120](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L120), [agentdescent/evolution.py#L2250](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L2250), [agentdescent/evolution.py#L3740](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L3740), [agentdescent/agents.py#L1](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/agents.py#L1), [README.md#L120](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/README.md#L120).
- Basis: Source-wired packaged model-backed operating path; no empirical inference performance attested.
- Confidence: High for structural wiring, moderate for ability to run under the isolated evidence environment.
- Caveats: The underlying task-solving model may itself be an application-supplied tool-using agent; its organizational metasystem and separate task services are not imported into AgentDescent.

## S2 — Coordination

- State: —
- Function: No positively evidenced **organizational inter-S1 interference regulator** with an autonomous ownership path and subsequent coordinated adjustments between independently viable S1 operating divisions is shown at this recursion.
- Disturbance / variety regulated: Concurrent rollout workers may propose contradictory edits against shared keys, race against stale ledger snapshots or exceed their task slice; these disturbances are **candidate-artifact merge conflicts**, not evidenced competing independent S1 divisional commitments.
- Decisive decision or feedback right: Default `DefaultConflict.resolve` chooses higher held-out-scoring contradicting diffs and `DefaultFusion` combines compatible ops; optional `ReflectiveFusion` can use a model to synthesize contested values. These are change-merger optimization decisions for one shared artifact, not separate mutual regulation of independently viable service departments.
- Decision owner: Deterministic default conflict/verifier policy (or optionally a model behind pluggable fusion) governs **candidate admission**; no first-party organization-level S2 owner is demonstrated for independently operating S1 units.
- Supporting / enforcement mechanisms: Per-worker snapshots, staleness filters, evidence buffer, `DefaultConflict`, `DefaultFusion`, optional `ReflectiveFusion`, section guards and serialized single-merger commit.
- Closure path: Candidate `Diff` cards → conflict/merge rule → held-out gate → updated single artifact head → next worker snapshot; this is coherence of an experimental artifact, not sourced S1-vs-S1 interference/oscillation → S2 damping → coordinated separate S1 behavior.
- Why this is / is not agent-owned: Even model-assisted diff synthesis is not automatically an organizational S2 function; removing it leaves the same underlying single-artifact optimization goal rather than an autonomous coordinating relationship among distinct S1 departments.
- Evidence: [agentdescent/defaults.py#L90](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/defaults.py#L90), [agentdescent/defaults.py#L141](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/defaults.py#L141), [agentdescent/fusion.py#L127](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/fusion.py#L127), [agentdescent/aggregator.py#L827](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L827), [agentdescent/evolution.py#L3686](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L3686).
- Basis: Bounded negative after checking both default and optional model-merger paths.
- Confidence: Medium-high at the declared learning-harness recursion.
- Caveats: If this framework is used to optimize several independently viable agents sharing operational resources, a new application-specific assessment boundary might expose real S2 evidence; generic `N` worker count does not prove it.

### Absence scope

- Surfaces inspected: Parallel/async workers, evidence-card buffer, DefaultConflict/DefaultFusion, optional ReflectiveFusion, worker snapshots and task-branch handling.
- Plausible first-party paths checked: Same-key diff contention, stale snapshots, conflicting prospective changes, per-worker task assignment and feedback into future artifact versions.
- Why no material first-party path remains: All checked paths regulate candidate artifact edits inside one learning process, without a first-party observed concrete inter-division operational disturbance and a dedicated regulator returning independently revised S1 commitments.



## S3 — Inside-and-now control

- State: —
- Function: No autonomous executive management of a portfolio of independently viable present S1 operations with negotiated priorities/resources and binding feedback is established.
- Disturbance / variety regulated: Worker errors, budgets, round timeouts, task allocation and token spending can destabilize an evolution run, but the linked responses are configured limits/scheduling and local algorithmic optimization, not enterprise-level management.
- Decisive decision or feedback right: Caller sets workers, evaluation threshold, compute limits, task selection/policy and trust region. `BudgetGovernor` and worker health enforce/calculate thresholds; aggregator determines candidate fitness, not organizational present obligations across S1 divisions.
- Decision owner: Operator configuration and deterministic package code; specific S1 model answers and S4 reflection are separate.
- Supporting / enforcement mechanisms: `BudgetGovernor`, sampler, `WorkerHealth`, max-worker-errors, timeout, token/governance/trust regions and commit policy.
- Closure path: Resource/error readings → fixed or configured scheduling/budget/sampler actions → continue/stop/skip individual experiment; no first-party manager discretion over cross-S1 present capabilities and reallocation with an organizational return path.
- Why this is / is not agent-owned: Adaptive numeric compute placement and candidate selection are not a discretionary S3 authority over S1 commitments.
- Evidence: [agentdescent/evolution.py#L2795](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L2795), [agentdescent/evolution.py#L3515](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L3515), [agentdescent/budget.py#L1](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/budget.py#L1), [agentdescent/pipeline.py#L49](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/pipeline.py#L49), [agentdescent/aggregator.py#L1412](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L1412).
- Basis: Source-bounded negative across current-control and mode variants.
- Confidence: Medium-high.
- Caveats: The human operator of a portfolio of deployment agents may be a real S3 externally; it is not a packaged parent-governed return path.

### Absence scope

- Surfaces inspected: Worker loop and health states, sampler, budget governor, round-timeout logic, merge/trust-region gates and host-configured algorithm ports.
- Plausible first-party paths checked: Whole-current assignment of tasks, capacity/budget allocation, retry/error escalation, trust-region/held-out commit decisions.
- Why no material first-party path remains: These paths configure or algorithmically manage one optimization run; no autonomous organizational manager changes present commitments among separately viable operating divisions.



## S3* — Complementary audit

- State: —
- Function: No independent complementary audit of **S1/S3 operational reality** with a mandate to correct a current S3 managerial picture and a returned management decision path is established.
- Disturbance / variety regulated: Model-generated candidate edits could corrupt performance, hallucinate improvements or violate artifact invariants; the held-out/oracle check independently measures candidate success, but is principally a change-acceptance/quality gate.
- Decisive decision or feedback right: The `ThreeLayerVerifier` and `AuditScheduler` supply evidence and can veto/queue validation for prospective artifact changes. They do not inspect competing operational reports against underlying reality and return corrective findings to an established S3 owner in the assessed boundary.
- Decision owner: Deterministic verifier/audit thresholds and external supplied reward/oracle; no separate first-party complementary auditor with governance corrective mandate.
- Supporting / enforcement mechanisms: Held-out rewards, oracle audit queue, replay/diagnostics, immutable L0 guards, statistical selection and change acceptance.
- Closure path: Candidate rollout evidence → held-out verifier/audit/acceptance decision → changed or refused future artifact; no independent operational inspection → correction of S3 current enterprise control → management action.
- Why this is / is not agent-owned: The audit terminology describes robust scientific evaluation for future learning, not necessarily VSM S3*; model/reflection and a scorer can occupy S1/S4 feedback without a distinct operational executive audit relationship.
- Evidence: [agentdescent/verifier.py#L1](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/verifier.py#L1), [agentdescent/aggregator.py#L968](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L968), [agentdescent/audit/wiring.py#L1](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/audit/wiring.py#L1), [agentdescent/governance.py#L70](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/governance.py#L70).
- Basis: Explicit audit/evaluation mechanics assessed under their concrete organizational closure role.
- Confidence: Medium-high.
- Caveats: A deployment could adopt independent run-time compliance audits as an application function, requiring its own evidence.

### Absence scope

- Surfaces inspected: ThreeLayerVerifier, AuditScheduler, audit/wiring, acceptance and ledger paths, held-out/prospective checks, frozen L0 governance.
- Plausible first-party paths checked: Independent operations observation, challenge to S1/S3 reports, corrective findings with mandate returned to present management, potential first-party parent approvals.
- Why no material first-party path remains: The shipped verifier gates the validity of proposed evolving artifacts; it does not supply a separate first-party S3 operating-management relationship into which independent audit findings are returned.



## S4 — Outside-and-then intelligence

- State: A
- Function: Learn from environment/task performance and explore future changes to the task-serving skill/prompt/harness, then adopt and feed those changes into the next operational version.
- Disturbance / variety regulated: Future task mix, repeated solver failure modes, reward changes, competition between candidate strategies and uncertainty about which generalized edits will improve upcoming task success.
- External distinction: The worker runs the current strategy on sampled environmental tasks, records model outputs, measured reward and expected-result metadata, and uses those observations as evidence of current strategy inadequacy.
- Future / prospective distinction: The `LLMAgent.propose` / `reflector(complete)` model reads the failed task, current rules, output and reward and proposes a generalized edit to the **persistent future reusable artifact**, not just a next-turn reply to the same task.
- Adaptation option generated: The model chooses a candidate new instruction/rule/skill/harness value; `Strategy.to_diff` produces a concrete prospective `Diff`, possibly alongside alternative proposals generated by peer workers.
- Path back into current capability / S3: The aggregator scores/filters candidates with held-out evidence and invariant/governance constraints, atomically commits accepted `Diff` to the versioned ledger and the next rollout snapshots read the updated artifact. The return is into the **operating solver's future capability**, not into an independently evidenced S3 executive; absence of an S3 owner is not hidden.
- Decisive decision or feedback right: **Prospective option formulation belongs to the configured model** through the shipped reflection adapter. The commit/adoption veto belongs to deterministic held-out/invariant gates and ultimately the operator-selected reward/constraints, which bound (but do not replace) model-generated strategic content.
- Decision owner: Model-backed `LLMAgent.propose` or `reflector` in the supported shipped first-party `evolve` mode; deterministic gates authorize materialization, not conceptual option invention. Autonomous S4 is bounded to proposing and adopting prospective improvements under a predefined learning mission, not constitutional policy authority.
- Supporting / enforcement mechanisms: EvidenceCard, snapshot/ledger, selection and staleness, optional reflective model fusion, `ThreeLayerVerifier`, reward gate, budgets, stop conditions and transaction logs.
- Closure path: External task-result contrast → model reflection/options → diff → held-out/invariant acceptance → committed persistent strategy/skill version → subsequent task solver uses new artifact → fresh feedback round.
- Boundary reachability: `LLMAgent.propose` and public `reflector(model)` are shipped, `_build_engine` actually wires them into `evolve`, `_propose_one` calls `propose(mine.render(),task,output,score)`, aggregator ingests card and commits to the same ledger used for next worker snapshots; public quickstart exercises this integrated model-and-artifact mode. The offline demo runs the same algorithm with a **scripted surrogate**, not claimed as model evidence.
- Why this is / is not agent-owned: Remove the proposer model while leaving worker scheduler, scoring, merge and ledger intact and the general semantic rule/strategy revision would not be generated from task evidence; fixed gates can accept/refuse candidates but cannot themselves invent the task-specific future improvement.
- Evidence: [agentdescent/evolution.py#L120](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L120), [agentdescent/evolution.py#L206](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L206), [agentdescent/evolution.py#L2250](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L2250), [agentdescent/evolution.py#L3740](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L3740), [agentdescent/evolution.py#L3790](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L3790), [agentdescent/aggregator.py#L1412](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L1412), [agentdescent/ledger.py#L1](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/ledger.py#L1).
- Basis: Source-connected first-party LLM reflection and durable future version adoption; not evidence of production task-success gains.
- Confidence: High for the option→accept→next-run wiring, medium for realized reward improvement.
- Caveats: This is a **bounded future operating-capability adaptation path**; it does not imply independent monitoring of society, a full organizational S3/S5, constitutional delegation, or automatic improvement without configured model/reward/dataset.

## S5 — Identity and ultimate policy

- State: —
- Function: No legitimate first-party agent/human constitutional authority is wired to receive fundamental purpose/identity conflicts and return binding enduring identity policy for the assessed organization.
- Disturbance / variety regulated: Dangerous self-modification and oracle/policy corruption are anticipated through frozen L0 and invariant guards; these are static protections rather than governance of identity conflicts.
- Decisive decision or feedback right: Operator/developer sets the objective, evaluator, immutable artifact ids, blast radius and thresholds. `assert_mutable` rejects frozen IDs and fixed policies enforce configured criteria; no bounded protocol resolves ultimate-purpose questions through a legitimate S5 authority.
- Decision owner: External task/operator for constitutional objectives, deterministic gate for enforcement.
- Supporting / enforcement mechanisms: L0 frozen IDs, governance `classify`/immutable assertions, contract invariants, rewards, public configurable policies and audit gates.
- Closure path: Configured constraint → proposed invalid mutation refused → continue or error; no question of organizational identity reaches a first-party S5 actor and returns as future binding identity policy.
- Why this is / is not agent-owned: Preventing a model from rewriting its own oracle is important security, but a hard-coded immutable condition cannot adjudicate the organization's ultimate purpose or legitimate authority.
- Evidence: [agentdescent/governance.py#L70](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/governance.py#L70), [agentdescent/governance.py#L134](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/governance.py#L134), [agentdescent/evolution.py#L2270](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/evolution.py#L2270), [agentdescent/aggregator.py#L1426](https://github.com/Birfy/agentdescent/blob/d1cfa8f6eb570d927826278c70aa23b86d3c5264/agentdescent/aggregator.py#L1426).
- Basis: Bounded negative from both model-driven and governance paths.
- Confidence: Medium-high.
- Caveats: External human owners may enforce or revise ultimate goals; the packaged learning engine contains no first-party return transaction qualifying as parent-governed S5.

### Absence scope

- Surfaces inspected: L0 frozen artifact policy, governable L1/L2 layers, repository operator config, invariants, held-out acceptance, model reflection and audit gates.
- Plausible first-party paths checked: Oracle and evaluator immutability, goal/reward changes, strategy/governance policy ownership and human approval of constitutional exceptions.
- Why no material first-party path remains: The first-party runtime enforces already supplied constraints but does not route identity/ultimate-policy matters to a legitimate deciding authority and return a binding long-horizon policy change.



## Recursion

The credited model-backed immediate S1 is task-solving from a current evolving artifact; S4 is a separate model-backed prospective adaptation of that persistent artifact. Parallel worker copies are experimental replicas in one artifact's optimization trajectory. Port-selection leaderboards, population islands, policy plugins and externally supplied workflows are not silently aggregated into an organizational S2/S3/S3*/S5 at this recursion.

## Variety and escalation

Input and candidate variety is attenuated through worker sampling, trust region, staleness checks, held-out evaluation, invariant veto, bounded budgets, frozen oracle identifiers and recorded versioned commits. A high-priority gate refusal, audit queue or terminal `stop_reason` is not automatically an algedonic path to S3/S4/S5.

## Evidence gaps

- The documented offline `python -m agentdescent.cli demo` invocation in a clean isolated checkout stopped before exercising code because required external package `numpy` was not installed: `ModuleNotFoundError: No module named 'numpy'`. No live LLM inference, dataset outcome/throughput verification or claimed benchmark numbers are derived from this exercise.
- First-party `Completion` adapters and `LLMAgent` provide a connected model-backed route, but external provider service or downstream task agent's internal planning is not credited as first-party AgentDescent organizational ownership.
- Statistical change gates and the fact that code labels a module `audit`, `governance` or `harness` are not proof of independent S3* or S5 authority. A genuinely separate run-time audit-and-management return would require new evidence under a different deployment boundary.
- This is a **proposed** standalone general assessment; catalog position, signatures and cohort views are untouched until a separately tested canonical admission PR.
