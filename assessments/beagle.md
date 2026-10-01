---
harness_id: beagle
project_name: Beagle
repository: https://github.com/SalesforceAIResearch/Beagle
review_ref: 165343b46a85b5d28c6370e6197ac665c7eda871
reviewed_at: 2026-10-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-01
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: —
---

# Beagle

## Review boundary

- System in focus: one first-party Beagle evaluation/evolution organization at pinned revision `165343b46a85b5d28c6370e6197ac665c7eda871`, including its agent abstraction/adapters, task rollout infrastructure, benchmark-native evaluation seam, registered evolution algorithms, and the shipped DarwinX search/selection/verification implementation.
- Purpose and identity: evaluate agent harnesses and autonomously evolve their persistent harness surface so later operational rollouts can perform better on external task distributions while guarding against regressions and reward hacking.
- Relevant environment: user-supplied or bundled/reference agent-harness repositories, benchmark task corpora and benchmark-native graders/runners, model-provider endpoints, Git hosting, Docker/xrlenv execution substrates, and operator-authored run configuration.
- Standard-distribution boundary: the shipped `beagle` package, its agent interfaces/adapters and rollout/eval machinery, registered algorithms, and the hosted DarwinX implementation under `beagle/algorithms/darwinx`. The internal decision paths concretely wired by those surfaces are credited; external harness internals, benchmark frameworks/ground truth, model providers, GitHub and execution substrates remain adjacent dependencies.
- Credited operating / distribution surfaces: `README.md`; `beagle/agents/core`; shipped reference adapters such as `beagle/agents/mini_swe` and `beagle/agents/monet`; `beagle/eval`; `beagle/algorithms/base.py`; `beagle/algorithms/darwinx/{algorithm.py,eval.py,meta_agent.py,_launch.py}`; and the hosted `vendor/{evolve,gate,dx_trace}` implementation reached by `beagle evolve`.
- Adjacent first-party surfaces excluded from ownership: repository-development CI, contributor/release governance, `.claude` development agents, tests and smoke artifacts except as reachability corroboration, published paper/result tables, and documentation of unported/inert DarwinX knobs. External evolvee/evolver repositories and benchmark-native runners do not donate their internal S2–S5 functions.
- First-party operating / deployment modes considered: `beagle evaluate`; `beagle evolve` with DarwinX; local-Docker and xrlenv-backed rollouts; supported agent adapters/configured Editors; optional DarwinX verification gates where the shipped implementation provides a function-specific path.
- Recursion level: one Beagle evolution campaign is the system-in-focus. An operational candidate-harness rollout is the S1 unit whose behavior Beagle evaluates; DarwinX plus its evolver and verification/search machinery form the metasystem around those rollouts. Parallel benchmark trials or candidate subprocesses are repeated/isolated episodes unless a concrete inter-S1 coordination relation is established.
- Reviewed revision: `165343b46a85b5d28c6370e6197ac665c7eda871`.
- Observation date: 2026-10-01.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Beagle exposes a common agent abstraction around runnable/evolvable harnesses and drives them in benchmark task environments. The README defines two principal modes: `evaluate`, which runs the selected harness through the benchmark's own runner/grader, and `evolve`, where a configured evolver agent edits an evolvee harness and an evolution algorithm evaluates the resulting candidates. Shipped adapters make concrete external harnesses reachable through the same rollout lifecycle; for example the mini-swe adapter installs an exact pinned harness revision in the Beagle-provisioned task container, invokes its native `mini` CLI, captures its repository changes and returns a `TaskResult`.

The shipped DarwinX implementation is not a documentation-only research reference. `DarwinX.evolve()` materializes the evolvee experiment copy, injects the configured Beagle `Editor` as the evolver, translates the run config, launches the hosted genealogy/QD pipeline, evaluates candidate branches through Beagle's benchmark-native evaluation seam, and reads the campaign winner back. The hosted implementation maintains a genealogy tree and quality-diversity archive, chooses parents, proposes mutations, scores candidates and preserves/recombines useful stepping stones.

Candidate acceptance has a distinct verification construction path. The bundled `gate` package provides structural/scope checks, anti-cheat and honeypot checks, verifier trajectory scoring, canary probes, cross-model and cross-benchmark transfer checks, and a promote/archive/reject result. Some gates are opt-in or configuration-dependent, and the actual benchmark/verifier/model independence depends on the instantiated run; therefore the generic distribution exposes a real complementary-audit constructor rather than one universally closed autonomous auditor.

DarwinX is also a persistent adaptation loop. An injected model-backed `Editor` proposes code/config changes to the harness workspace; candidate behavior is measured on external tasks; selection and verification decide which variants survive; accepted branches and the genealogy/archive persist campaign state; long-term lessons feed later proposals; and the returned winner is a changed harness revision intended for later operational use. This is more than context reuse or retry: external performance evidence changes durable future capability.

## Operational model

A campaign starts from a selected evolvee harness/revision and benchmark/task set. Beagle provisions a task environment and runs the harness through its first-party adapter, while the harness's autonomous inference actor chooses substantive task actions. Benchmark-native evaluation turns the resulting trajectory/submission into outcome evidence. In evolution mode DarwinX supplies that evidence and campaign history to the configured evolver Editor, which proposes persistent harness changes. Candidate revisions are evaluated, challenged by configured gate/verifier surfaces, retained/rejected/archived under the search policy, and used as parents for later proposals. The campaign ultimately returns a selected persistent harness candidate.

At this recursion, the operational agent loop is S1 and the evidence-driven persistent harness mutation loop is S4. Parallelism, genealogy bookkeeping, parent selection and lifecycle supervision are part of the adaptation/search mechanism rather than a separately evidenced S2 or whole-current S3 function. Complementary verifier/gate paths can independently challenge candidate/trajectory claims, but their concrete independence and decision owner depend on the configured evaluator/model/benchmark, so S3* is constructor-owned.

## S1 — Operations

- State: A
- Function: execute an agent harness against a task environment and produce a substantive task result/trajectory whose outcome can be evaluated.
- Disturbance / variety regulated: task instructions, repository/environment state, tool results and failures, model uncertainty, provider responses, execution limits and other task-local distinctions encountered during a rollout.
- Decisive decision or feedback right: choose the substantive task actions/tool calls/code edits and stopping/submission behavior of the configured agent harness after observing its current task state.
- Decision owner: the autonomous model-driven harness actor concretely invoked by Beagle's supported agent adapter.
- Supporting / enforcement mechanisms: `Agent`/`Runnable` interfaces, agent adapters, `ContainerRuntime`, rollout lifecycle, task context, provider routing, trajectory capture, task-result transport and benchmark runner integration.
- Closure path: benchmark task/environment → Beagle provisions and invokes the configured agent harness → model-driven actor chooses task actions and receives tool/environment feedback → harness returns a result/trajectory/submission → Beagle captures it as `TaskResult` for evaluation and later campaign feedback.
- Boundary reachability: the documented `beagle evaluate` and `beagle evolve` paths instantiate registered agent adapters directly. The mini-swe reference adapter, for example, pins an upstream revision, runs its native single-task CLI inside the Beagle-provisioned environment and captures the produced patch/trajectory; the decisive operational actor is therefore concretely wired into the supported distribution rather than inferred from an unrelated downstream system.
- Why this is / is not agent-owned: deterministic container, adapter and benchmark plumbing do not choose how to solve the task. Removing the model-driven harness actor while leaving Beagle's transport/runtime machinery intact removes the substantive operational decision right.
- Evidence: [`README.md`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/README.md); [`beagle/agents/mini_swe/__init__.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/agents/mini_swe/__init__.py); [`beagle/agents/monet/__init__.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/agents/monet/__init__.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Beagle does not inherit arbitrary internal VSM functions from an external evolvee. S1 credit is bounded to the first-party supported rollout organization that concretely wires an autonomous harness actor into task/action/feedback/result execution.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 disturbance-attenuation function is established at the reviewed campaign recursion.
- Disturbance / variety regulated: not established as an interaction-generated disturbance between distinct sibling S1 units. Candidate trials may run in parallel and lineages compete for selection, but those are evaluation/search episodes rather than evidence of mutually interfering operational units requiring coordination.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: candidate worktrees, parallel rollout concurrency, genealogy tracking, quality-diversity archives, task batching, process/container isolation and result aggregation.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: scheduling, isolation, candidate selection and diversity preservation do not by themselves establish a concrete S1↔S1 disturbance plus an attenuation relation that feeds back into subsequent peer operation.
- Evidence: [`beagle/algorithms/darwinx/algorithm.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/algorithm.py); [`beagle/algorithms/darwinx/vendor/README.md`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/vendor/README.md); [`README.md`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: an evolved harness may itself be multi-agent, but its internal coordination is adjacent unless Beagle itself owns the relevant relation at the declared recursion.

### Absence scope

- Surfaces inspected: top-level evaluate/evolve architecture, agent adapters, rollout infrastructure, DarwinX genealogy/QD search, worktree/candidate execution, benchmark evaluation and verification gates.
- Plausible first-party paths checked: concurrent candidate evaluations, worktree isolation, QD diversity preservation, parent competition, archive/recombination, benchmark batching and distributed worker execution.
- Why no material first-party path remains: these mechanisms isolate, schedule or select candidate work. They do not establish at least two credited sibling S1 units with a concrete interaction-generated conflict/oscillation, an S2-specific attenuation decision and returned feedback changing subsequent peer behavior.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-system current-control function is established separately from S1 execution and the prospective S4 evolution/search loop.
- Disturbance / variety regulated: campaign status, candidate scores, rollout failures, budgets/concurrency and genealogy state are tracked, but reviewed interventions are deterministic lifecycle/search mechanics or future-capability selection rather than separate regulation of present organizational commitments.
- Decisive decision or feedback right: no distinct owner is established for whole-system present resource/commitment/priority decisions at the declared recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: DarwinX pipeline/supervisor sequencing, parent selection, candidate state, configured concurrency, failure handling, stopping limits, archive management and evaluation scheduling.
- Closure path: not applicable for the negative finding.
- Boundary reachability: the control mechanisms are first-party and reachable, but the S3 organizational function itself is not established independently of adaptation/search execution.
- Whole-system current view: genealogy/archive/campaign state provide a campaign view, but it is used primarily to choose future candidate mutations/parents and execute the search algorithm rather than regulate multiple current operational commitments as S3.
- Current-control decision scope: deterministic run/candidate lifecycle and adaptation-search decisions; no separate substantive present-tense authority over shared operational commitments/resources/priorities is established.
- Why this is / is not agent-owned: the evolver owns prospective capability-change judgment mapped to S4. Reclassifying the same parent/candidate selection as S3 would double-count adaptation rather than identify a distinct inside-and-now control loop.
- Evidence: [`beagle/algorithms/darwinx/algorithm.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/algorithm.py); [`beagle/algorithms/darwinx/vendor/README.md`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/vendor/README.md).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: DarwinX describes a distributed supervisor, but supervisor/lifecycle naming is not sufficient for S3; the reviewed campaign decisions are part of the evolution/search function.

### Absence scope

- Surfaces inspected: campaign launcher, genealogy/QD pipeline, candidate evaluation, parent selection, archive/preservation/recombination, worker/process execution, concurrency/failure handling and verification gates.
- Plausible first-party paths checked: distributed supervisor as S3, parent selection as current priority control, archive state as whole-system current view, failure/retry handling as intervention and gate rejection as present control.
- Why no material first-party path remains: these paths either enforce the configured campaign lifecycle or decide which persistent future capability survives. No separate whole-current regulator with a distinct present resource/commitment/priority decision-and-return loop was established.

## S3* — Complementary audit

- State: C
- Function: provide a complementary challenge path over candidate-harness performance/generalization claims before a mutation is promoted.
- Disturbance / variety regulated: a candidate may appear improved from ordinary benchmark pass rate while actually overfitting, hard-coding probe tasks, tampering with evaluation surfaces, reward-hacking, regressing on canaries, or failing transfer to another model/benchmark.
- Decisive decision or feedback right: determine structural/behavioral/verifier/transfer findings and produce promote/archive/reject evidence that can change candidate fitness, parent selection or promotion.
- Decision owner: constructor-dependent. Beagle ships and wires the function-specific gate/verifier pipeline, but the decisive benchmark/verifier/model independence and enabled gate set depend on the concrete run configuration rather than one universal autonomous audit actor.
- Supporting / enforcement mechanisms: scope filter, anti-cheat/content checks, honeypot tasks, canary probes, LLM-as-verifier trajectory scoring, Best-of-N/consensus checks, cross-model and cross-benchmark transfer checks, gate verdict sidecars and verifier-fitness blending.
- Closure path: ordinary candidate rollout/evaluation produces a claimed improvement → separate gate/verifier surfaces inspect candidate diff/trajectories and run fresh challenge evaluations → findings produce gate/verifier scores or promote/archive/reject decisions → enabled fitness/gate integration changes parent selection or candidate promotion → later campaign behavior proceeds from the resulting archive/genealogy state.
- Boundary reachability: the `gate` implementation is hosted in the shipped DarwinX package and wired into the campaign through the gate hook/config surface; it is not repository-development CI. Concrete strong modes are configuration-dependent, supporting constructor rather than unconditional autonomous ownership.
- Claim being audited: that the candidate mutation is a legitimate, generalizable harness improvement rather than a benchmark-specific, reward-hacking, tampering or regressive change.
- Ordinary reporting path: benchmark-native candidate evaluation/pass-rate and candidate-produced trajectory/result.
- Complementary access path: diff/scope inspection, independent verifier scoring, honeypot/canary reruns and optional cross-model/cross-benchmark transfer evaluation.
- Independence boundary: the verification code path and challenge datasets/models can be distinct from the candidate's ordinary evaluation/evolver, but actual model/provider/benchmark separation is selected by configuration and therefore is not universally guaranteed by the generic Beagle distribution.
- Who acts on findings: the hosted DarwinX gate/fitness/search machinery can consume findings to reject/promote/archive or change selection weight; concrete autonomous audit ownership remains dependent on the instantiated verifier/evaluator configuration.
- Why this is / is not agent-owned: a real S3*-specific construction path exists and returns audit findings into regulation, but the generic distribution does not establish one invariant autonomous auditor/independence arrangement across supported configurations. `C` captures that constructor boundary.
- Evidence: [`beagle/algorithms/darwinx/vendor/gate/README.md`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/vendor/gate/README.md); [`beagle/algorithms/darwinx/algorithm.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/algorithm.py); [`beagle/algorithms/darwinx/eval.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/eval.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: several gate modes are opt-in or configuration-dependent; inert/unported knobs documented in the gate README are not used as positive evidence.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert external task/evaluation evidence into persistent changes to the agent harness that alter later operational capability.
- Disturbance / variety regulated: recurring task failures, benchmark performance gaps, new/hard task distinctions, regressions, model/benchmark transfer failures, behavioral novelty and lessons accumulated across an evolution campaign.
- Decisive decision or feedback right: choose what harness mutation to propose and, through the DarwinX search/selection loop, determine which persistent candidate capability is retained as a stepping stone/parent/winner for later operation.
- Decision owner: the configured autonomous model-backed evolver `Editor` owns semantic mutation proposals; DarwinX supplies the first-party selection/verification environment that retains evidence-supported persistent variants.
- Supporting / enforcement mechanisms: `meta_agent` Editor injection, candidate worktrees/branches, genealogy tree, quality-diversity archive, parent selection, novelty scoring, benchmark-native evaluation, verification gates, archive/recombination, long-term campaign memory and returned winner.
- Closure path: external benchmark/task rollouts expose outcome evidence → campaign history/archive and verification evidence are assembled for evolution → autonomous evolver Editor proposes persistent harness changes → candidate revision is evaluated and selected/archived/rejected → surviving revision/history becomes input to later evolution and a winner is returned → later Beagle rollouts execute the changed harness capability.
- Boundary reachability: `beagle evolve` directly resolves the registered DarwinX algorithm, injects the configured Beagle Editor, launches the hosted implementation and returns the selected candidate. No unpublished research branch or external evolution service is needed for this loop.
- Why this is / is not agent-owned: the semantic content of the harness change is chosen by a model-backed evolver rather than predetermined by a fixed transformation. Removing the evolver while keeping evaluation/search plumbing removes the same adaptation judgment. Deterministic selection/gating constrains that agent-owned proposal loop but does not replace it.
- External distinction: benchmark tasks, task-environment outcomes, challenge/honeypot/canary evidence and optional cross-model/cross-benchmark transfer results are observations about conditions outside the harness's current internal state.
- Future / prospective distinction: the loop does not merely repair the current trajectory; it searches for a harness revision intended to generalize to later tasks/models/benchmarks and carries campaign lessons into later proposals.
- Adaptation option generated: the evolver produces concrete edits to evolvable harness surfaces; DarwinX also preserves specialist stepping stones and can recombine them into later candidate variants.
- Path back into current capability / S3: accepted/archived candidate revisions become later parents and the selected winner is returned as the evolved harness; subsequent operational rollouts therefore execute changed persistent capability.
- Evidence: [`README.md`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/README.md); [`beagle/algorithms/darwinx/algorithm.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/algorithm.py); [`beagle/algorithms/darwinx/meta_agent.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/meta_agent.py); [`beagle/algorithms/darwinx/eval.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/eval.py); [`beagle/algorithms/darwinx/vendor/README.md`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/vendor/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the operator chooses the initial evolvee, benchmark and algorithm configuration. That setup authority does not remove autonomous ownership of mutation judgment within the configured campaign.

## S5 — Policy and identity

- State: —
- Function: no closed first-party runtime loop is established for deciding or reaffirming the ultimate identity/purpose/policy of the Beagle campaign or evolved organization.
- Disturbance / variety regulated: configuration, mutation-surface allowlists, security constraints, benchmark selection, evolution goals and acceptance thresholds constrain the campaign, but they are supplied rules/inputs rather than a runtime identity-governance decision loop.
- Decisive decision or feedback right: no first-party actor is shown owning an ultimate-policy/identity issue and returning an authoritative identity/purpose decision into operation.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: typed run configuration, evolvable-surface allowlists, gate thresholds, benchmark/evolvee/evolver selection, provider credentials, Git experiment-copy rules and scope/security denylists.
- Closure path: not applicable; no identity/policy issue → legitimate ultimate authority → authoritative decision → returned governance of subsequent operation path is established.
- Why this is / is not agent-owned: the evolver may alter permitted harness implementation surfaces, but it operates under externally selected goals/configuration and explicit denied security/control paths. Harness self-improvement within that mandate is S4, not authority to redefine the mandate itself.
- Evidence: [`README.md`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/README.md); [`beagle/algorithms/darwinx/config.py`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/config.py); [`beagle/algorithms/darwinx/vendor/gate/README.md`](https://github.com/SalesforceAIResearch/Beagle/blob/165343b46a85b5d28c6370e6197ac665c7eda871/beagle/algorithms/darwinx/vendor/gate/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: strong scope, anti-cheat and security constraints are policy enforcement mechanisms, not S5 ownership without an ultimate-policy/identity decision loop.

### Absence scope

- Surfaces inspected: top-level configuration and mission, agent/evolver/evolvee selection, DarwinX typed configuration, mutation-surface allowlists/denylists, gate policy, Git experiment-copy rules, credentials/provider routing, repository governance and campaign lifecycle.
- Plausible first-party paths checked: evolver changing its own mandate, DarwinX choosing the campaign objective, gate policy as S5, security/scope rules as identity authority, operator config as parent S5 and repository governance as runtime governance.
- Why no material first-party path remains: the campaign's objective, evolvee/evolver/benchmark selection and policy boundaries are externally authored configuration; DarwinX/evolver operates within them. Enforcement and self-improvement do not create a first-party ultimate authority that can decide/reaffirm identity or foundational policy and return that decision into operation.

## Distributed OSS parent arrangement

Repository maintainers govern Beagle development and releases, while users/operators configure individual evaluation/evolution campaigns. That OSS governance is adjacent to a deployed campaign and is not imported as organization-level parent S3/S4/S5 ownership. No qualifying parent-mode modifier is claimed.

## Self-hosted and non-human modes

Beagle can run locally with Docker or against xrlenv rollout infrastructure, and a configured DarwinX campaign can proceed without continuous human intervention once launched. The operator still chooses the run configuration, evolvee/evolver and task/benchmark scope. Those launch-time choices do not create a separate parent-mode notation because no complete parent S3/S4/S5 loop beyond ordinary configuration is established.

## Recursion

At the assessed recursion, one Beagle evolution campaign is the system. Operational harness rollouts are S1 episodes; benchmark/evaluation evidence plus the DarwinX evolver/search loop form the adaptive metasystem. Internal VSM functions of an arbitrary imported harness are not inherited. The autonomous S4 claim rests on Beagle's own hosted evolution organization and its configured autonomous Editor, not on whatever S4 capabilities the evolvee might already contain.

## Variety and escalation

Beagle absorbs task/environment variety through agent rollouts and benchmark-native evaluation, while DarwinX amplifies adaptation variety through multiple candidate mutations, lineage preservation, novelty/QD search and recombination. Verification gates attenuate unsafe or non-generalizable variation. Failures, regressions and challenge evidence feed candidate rejection/archive/selection and later proposals; no distinct S2/S3 or S5 escalation loop is inferred from those mechanics.

## Evidence gaps

- S1 is bounded to Beagle's supported operational rollout wiring; arbitrary external harness internals do not donate higher VSM functions.
- S2 is not inferred from parallel candidates, distributed workers, worktrees, genealogy or quality-diversity population management.
- S3 is not inferred from DarwinX's “supervisor” terminology, candidate lifecycle, selection or campaign scheduling; those mechanisms principally execute S4 search/adaptation.
- S3* is `C` because Beagle ships a genuine complementary verification/gate path, but the concrete independence and audit authority depend on the configured verifier/model/benchmark/gate mode.
- S4 is the strongest higher-order path: external evaluation evidence drives autonomous persistent harness edits that are selected and returned into later operational capability.
- S5 is not inferred from scope/security policies, configuration, approvals or the ability to mutate harness code within an externally authored mandate.
