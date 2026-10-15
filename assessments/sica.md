---
harness_id: sica
project_name: SICA
repository: https://github.com/MaximeRobeyns/self_improving_coding_agent
review_ref: ed8275dca4d3c5dbf77229964351fe9b424797dc
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# SICA — Self-Improving Coding Agent

## Review boundary

- System in focus: public research harness containing a first-party multiagent coding runtime, a model-driven MainOrchestrator, a separately launched model Overseer, and the outer benchmark/archive/meta-improvement loop that builds successive agent versions.
- Purpose and identity: solve coding tasks through supervised delegated models and improve the coding agent's own future task competence from benchmark results.
- Relevant environment: benchmark tasks and graders, archived performance/utility across generations, local code/tests and Docker containers, model providers and cost/time budgets.
- Standard-distribution boundary: `runner.py`, documented `base_agent` module entrypoint, and first-party `base_agent/src` classes. Inference requires model credentials and Docker; no external benchmark engine internals or research operator decisions credited as autonomous.
- Credited operating / distribution surfaces: [runner.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/runner.py); [base_agent/agent.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/agent.py); [base_agent/src/agents/implementations/main_orchestrator.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/agents/implementations/main_orchestrator.py); [base_agent/src/oversight/overseer.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/oversight/overseer.py); [base_agent/src/tools/reasoning_structures/meta_improvement.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/tools/reasoning_structures/meta_improvement.py); [base_agent/src/tools/committee_design.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/tools/committee_design.py).
- Adjacent first-party surfaces excluded from ownership: external benchmark truths/graders, human experiment goals and accepted identity, dashboard visualizations alone, static security settings, paper hypotheses and unexecuted analysis notes.
- First-party operating / deployment modes considered: standalone coding/benchmark agent mode, multiworker benchmark runner, `improve` mode for next self-modified version, separate monitored model Overseer. Positive functions may be realized at different nested recursions and are not claimed to coexist within every individual child.
- Recursion level: deployed experiment/harness with iterative self-improvement, containing one operating coding-agent organization (MainOrchestrator + S1 children + Overseer), then an outer version adaptation loop.
- Reviewed revision: `ed8275dca4d3c5dbf77229964351fe9b424797dc`.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The public runner starts multiple benchmark jobs in bounded isolated Docker containers with exclusive worker-allocated host ports and per-benchmark tracker locks. Each job uses a first-party model-driven MainOrchestrator, which decomposes goals into coding/analysis workers and sees results and a live callgraph. A separately invoked Overseer monitors first-party event-derived execution and may notify or cancel failing nested actors. The meta-improvement mode analyzes archived benchmark outcomes and instructs model-driven changes to the next agent code generation, with separate reviewer models and subsequent retesting. [runner.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/runner.py); [base_agent/agent.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/agent.py); [base_agent/src/agents/implementations/main_orchestrator.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/agents/implementations/main_orchestrator.py); [base_agent/src/oversight/overseer.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/oversight/overseer.py).

## Operational model

At the coding recursion, S1 models implement tasks, S2 prevents benchmark child interference in shared host resources and records, S3 model directs current delegated work, and S3* model independently inspects execution health and can intervene. At the broader version recursion, model-led S4 proposes and deploys future changes from measured prior iterations. None establishes an ultimate legitimate S5 identity authority.

## S1 — Operations

- State: A
- Function: First-party agent loops perform model-directed coding/source inspection, sandboxed shell operations, benchmark problem solving and independently executing delegated workers.
- Disturbance / variety regulated: New bug/task descriptions, mutable repository content, tool errors, model output and local experiment conditions.
- Decisive decision or feedback right: Model selects concrete coding steps and allowed tools after receiving tool outputs or prior subagent results.
- Decision owner: Executing CodingAgent/ProblemSolver child model, MainOrchestrator's bounded solver actions and base agent tool-call continuation.
- Supporting / enforcement mechanisms: Agent classes, tool parser and call graph, execute_command, file and edit tools, sandbox Docker process.
- Closure path: Task → model-directed operations → actual tool/command outputs and artifact → subsequent step or returned result, with sandbox limits.
- Boundary reachability: Packaged `base_agent.agent` runs `MainOrchestratorAgent`, which can create coding/model workers; shipped `runner.py` invokes that executable in isolated Docker containers.
- Why this is / is not agent-owned: Task-specific coding decisions are model-generated rather than only an external benchmark script.
- Evidence: [base_agent/agent.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/agent.py); [base_agent/src/agents/implementations/coder.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/agents/implementations/coder.py); [base_agent/src/agents/agent_calling.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/agents/agent_calling.py); [base_agent/src/tools/execute_command.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/tools/execute_command.py); [runner.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/runner.py)
- Basis: explicit / structural
- Confidence: high for first-party mode; no measured coding quality
- Caveats: External model credentials and Docker environment are required to execute real inference; source-only evidence.

## S2 — Coordination

- State: C
- Function: Prevent distinct concurrent benchmark-running agent S1 workers from interfering through shared host HTTP ports and shared benchmark result-tracker mutation.
- Distinct S1 units: Multiple Python/Docker child coding agents each solve separate benchmark problems through `run_benchmarks_with_job_queue` and `process_job`, independently maintaining a coding task loop.
- Inter-S1 disturbance: If two independently executing benchmark agents bind the same host port 8080/808x, one container fails to start; concurrent writes to the same benchmark JSONL tracker may lose or corrupt result/progress state.
- Attenuating coordination relation: `run_benchmarks_with_job_queue` allocates a unique worker_id from bounded id_queue; `process_job` binds container host port `808{worker_id}`. Each benchmark uses `asyncio.Lock` around tracker start/result updates, preventing simultaneous writes to shared provenance.
- Feedback into subsequent S1 behaviour: Each worker occupies one reserved ID/port while running its model and returns ID only on exit; subsequent agent work waits for a safe slot or starts on another allocated ID; results can be safely saved and analyzed for next iteration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The first-party ID lease and tracker lock address two named interference modes produced by distinct simultaneously acting model agents; the evidence goes beyond mere task assignment/queue routing.
- Disturbance / variety regulated: Host port contention and cross-worker result-store writes.
- Decisive decision or feedback right: Allocate/release exclusive host port and serialize benchmark tracker mutations.
- Decision owner: First-party deterministic id_queue and per-benchmark asyncio.Lock constructor, not an autonomous S2 mediator model.
- Supporting / enforcement mechanisms: Bounded max_workers, unique Docker names, per-problem workdir mounts and benchmark data lock.
- Closure path: Several runnable problem jobs → lease worker_id/unique host port → parallel model sessions → guarded tracker write → release lease → next job.
- Boundary reachability: Default `runner.py` uses this first-party benchmark job runner during evaluation of each agent iteration; positive S2 is bounded to this concurrent benchmark-agent mode.
- Why this is / is not agent-owned: Safe exclusive-resource scheduling is deterministic host-owned (`C`), not the meta agent's discretionary choice.
- Evidence: [runner.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/runner.py); [base_agent/src/benchmarks/base.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/benchmarks/base.py)
- Basis: structural
- Confidence: high for construction; medium for effectiveness
- Caveats: Does not establish general multi-writer code merge safety or external cluster coordination.

## S3 — Inside-and-now control

- State: A
- Function: Model-driven executive direction of multiple current subordinate coding workers with shared task progress and corrective redirection based on their execution results.
- Whole-system current view: MainOrchestrator owns the top-level task and receives the complete problem and a synthesized live execution tree from CallGraphManager after subordinate calls, including already attempted work/results and current subordinate execution state.
- Current-control decision scope: MainOrchestrator selects/decomposes active subagent tasks, assigns complete subtask instructions, scrutinizes their returned evidence, changes the plan, commissions further workers/verification and decides when a coherent current task result is submitted.
- Disturbance / variety regulated: Subagent failures, incomplete work, duplicate approaches, requirement mismatch and uncertain current progress.
- Decisive decision or feedback right: Discretionary model-controlled reassignment, continuation/stop and verification of the current multi-agent goal; no reliance solely on fixed queue.
- Decision owner: First-party MainOrchestratorAgent LLM (`A`) at parent/current multiunit recursion, separate from subordinate child-model operational work.
- Supporting / enforcement mechanisms: CallGraphManager, generated execution-tree event, model-driven agent calls, structured task results, cost/time governors.
- Closure path: Current top-level intent → orchestrator decomposition → model worker runs → returned results plus direct callgraph operating state → revised plans/delegation and final task acceptance.
- Boundary reachability: `base_agent/agent.py` constructs MainOrchestratorAgent and starts it as the initial executing actor in CLI and benchmark mode; role documented in the agent's first-party core prompt.
- Why this is / is not agent-owned: The parent model uses evidence and discretionary judgment to govern concurrent/successive independently thinking subagent units, rather than merely running a predefined list of subtasks.
- Evidence: [base_agent/agent.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/agent.py); [base_agent/src/agents/implementations/main_orchestrator.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/agents/implementations/main_orchestrator.py); [base_agent/src/callgraph/manager.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/callgraph/manager.py); [base_agent/src/agents/agent_calling.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/agents/agent_calling.py)
- Basis: explicit / structural
- Confidence: medium-high for actor authority and feedback path
- Caveats: Current S3 claim is bounded to the nested coding-agent organization, not company-wide management or the outer research owner.

## S3* — Complementary audit

- State: A
- Function: Separate model-driven runtime monitor checks independent live callgraph/effect events for subagent nonprogress, looping and abnormal execution and can issue corrective notices or terminate faulty child work.
- Claim being audited: Operational actors' implicit assertions of continuing useful work and healthy nested execution; notably a child may be silently looping or failing while its parent awaits results.
- Ordinary reporting path: Each coding child returns self-authored work and final text to its parent, potentially omitting stalled nested activity.
- Complementary access path: An independently launched Overseer model periodically/event-triggeredly reads `generate_overseer_execution_tree(CallGraphManager)`, a first-party event-derived live execution graph, not only the child/parent's narrative result. This is source-observed execution, although not an independently executed code quality benchmark.
- Independence boundary: Overseer is a separate model invocation outside producer and supervising parent tool-delegation turn, with its own model option and timing/event observations. Shared first-party callgraph and provider limits remain; no external independent auditor claim.
- Who acts on findings: Overseer itself publishes OVERSEER_NOTIFICATION to an implicated agent/parent and calls CallGraphManager.cancel_agent when model judge sets force_cancel_agent; parent responds via next tool/model decision. It also adapts future monitoring cadence.
- Disturbance / variety regulated: Task nonprogress, recursion loops, stalled/erratic worker execution and hidden operational states.
- Decisive decision or feedback right: Model independently decides concern/notifiability, which actor to notify, whether to cancel, and whether future checks are time/event-driven.
- Decision owner: Separate autonomous Overseer model, not a rule-only timeout checker.
- Supporting / enforcement mechanisms: EventBus subscriptions, execution-tree renderer, OverseerJudgement schema, LLM check interval, notifications and cancellation path.
- Closure path: Real child event and call graph → separate model Overseer diagnosis → notification or direct cancel → parent agent control loop sees issue and can reassign; subsequent oversight resamples.
- Boundary reachability: `base_agent/agent.py` always instantiates and starts Overseer when running packaged agent; its `_monitoring_loop` subscribes to tool result/assistant events while root agent executes.
- Why this is / is not agent-owned: The audit's judgment and direct cancellation/intervention are separate model decisions using a complementary event-derived operating view; not a producer self-review or passive observability dashboard.
- Evidence: [base_agent/agent.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/agent.py); [base_agent/src/oversight/overseer.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/oversight/overseer.py); [base_agent/src/callgraph/reporting.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/callgraph/reporting.py); [base_agent/src/callgraph/manager.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/callgraph/manager.py)
- Basis: explicit / structural
- Confidence: medium-high for wiring, medium for audit effectiveness
- Caveats: Overseer is an execution-health complementary audit, **not** independent code correctness review. It may share model provider and callgraph evidence with producer; cancellation can be mistaken or delayed. ReviewCommittee is separately model-driven design critique but is not credited as direct runtime correctness audit.

## S4 — Outside-and-then intelligence

- State: A
- Function: Model-driven future-capability adaptation: evaluate externally defined benchmark tasks and past agent-version results, generate and implement software architecture/tool changes for subsequent agent generations.
- External distinction: Benchmark tasks and measured grader outcomes originate outside the current coding agent's self-report; the archive records past failures, costs and utility scores. Published literature/web exploration can inform new feature options in the meta-improvement reasoning workflow.
- Future / prospective distinction: The meta agent is tasked to improve the **next** version's general coding competence, not just solve the currently evaluated benchmark problem or fix the present code task.
- Adaptation option generated: MetaImprovementReasoningStructure directs archive analysis (working and failed features), a model-chosen new feature/strategy, code change proposal, multi-member read-only ReviewCommittee critique, model-directed implementation and planned tests.
- Path back into current capability / S3: `runner.py` evaluates a version, selects a base version by stored benchmark statistics and confidence bound, copies code into next iteration, runs that version's model-driven `improve` mode on its own codebase, then rebuilds Docker and runs subsequent version benchmarks; resulting changed tool/prompt/coding policy becomes future subordinate S1 capability used by MainOrchestrator's current-work organization.
- Disturbance / variety regulated: Long-term changes in measured coding benchmark performance and repeated feature failures, rather than current tool-loop transient errors.
- Decisive decision or feedback right: Model chooses which agent architecture/tool/behavior feature should be changed after comparing archived experience and review committee feedback, with real downstream implementation and retest.
- Decision owner: Meta-improvement MainOrchestrator/CodingAgent and archive analysis model in the explicit self-improvement operating mode; version selection/testing is first-party deterministic support.
- Supporting / enforcement mechanisms: Benchmark registry, archive analyzer with utility/CI, `select_base_agent`, independent model-driven ReviewCommittee, meta-improvement reasoning structure, agent_change_log.md, isolated next-agent directory.
- Closure path: External benchmark/task outcomes → version-level archive → model diagnosis and novel future improvement option → separate committee critique → actual coding changes to next version → newly launched/evaluated agent iteration and updated archive.
- Boundary reachability: Documented `python runner.py` default cycle executes benchmarks and then `run_meta_agent_benchmark`, which launches `base_agent` `improve` mode. That mode integrates meta-improvement reasoning and committee. No external company service is required.
- Why this is / is not agent-owned: Future capability choice and proposal/refinement are model-authored, not merely a static benchmark-triggered template or heuristic version selector; first-party script closes deployment/evaluation.
- Evidence: [runner.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/runner.py); [base_agent/src/tools/reasoning_structures/meta_improvement.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/tools/reasoning_structures/meta_improvement.py); [base_agent/src/agents/implementations/main_orchestrator.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/agents/implementations/main_orchestrator.py); [base_agent/src/tools/committee_design.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/tools/committee_design.py); [base_agent/src/agents/implementations/archive_explorer.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/agents/implementations/archive_explorer.py)
- Basis: explicit / structural
- Confidence: medium-high for model-driven improvement cycle, low for empirical net improvement
- Caveats: A new iteration is produced even when benchmark gains are not established; selection uses observed statistics but does not prove monotonic improvement, safety or benchmark transfer. No production performance results inferred.

## S5 — Policy and identity

- State: —
- Function: No evidenced legitimate ultimate-purpose/policy authority with identity-level deliberation and binding return across all future agent adaptations.
- Disturbance / variety regulated: Risk of benchmark Goodharting, security tradeoffs, resource spending and deciding which future changes are acceptable.
- Decisive decision or feedback right: Humans configure objectives/budget, benchmark suite, model credentials and Docker trust. Committee can critique designs but cannot ratify ultimate identity or adjudicate mission change.
- Decision owner: External experiment operator and developer-set prompt/policy boundaries; no dedicated legitimate S5 body.
- Supporting / enforcement mechanisms: ReviewCommittee 'taste maker', testing manager, fixed guards, benchmark score criterion, sandbox/budget limits.
- Closure path: Committee reports recommendations and model may refine next feature; no identity-level issue/ultimate authority/legitimate binding policy return at S5 recursion.
- Why this is / is not agent-owned: A sophisticated self-improvement S4 or design-review committee does not imply governing constitutional/organizational identity authority.
- Evidence: [base_agent/src/tools/committee_design.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/tools/committee_design.py); [runner.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/runner.py); [base_agent/src/agents/implementations/review_committee_member.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/agents/implementations/review_committee_member.py); [base_agent/src/config.py](https://github.com/MaximeRobeyns/self_improving_coding_agent/blob/ed8275dca4d3c5dbf77229964351fe9b424797dc/base_agent/src/config.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Human research/program governance above the tool is outside the declared system boundary.

### Absence scope

- Surfaces inspected: Meta improvement design critique, version selection and archive scoring, top-level prompt, sandbox/security configuration and developer docs.
- Plausible first-party paths checked: Taste-maker committee, runner objective selection, budget/monitor intervention, agent self-edit instructions and loop termination.
- Why no material first-party path remains: None assigns/executes a legitimate ultimate identity/policy arbiter with authoritative binding return; all remain evaluator or external user-scoped policies.

## Recursion

The S3 and S3* functions are nested first-party management and complementary monitoring of multiple operational child agents in one coding-agent run. The S2 resource gate is owned by the *outer* concurrent benchmark runner and therefore is not attributed to the internal CodingAgent alone. The S4 model-driven archive-to-next-version loop is one recursion above the ordinary task: it generates **future capability changes**, not a superior current-work S3. No function is inferred solely by counting model actors.

## Variety and escalation

Concurrency/host port collision → exclusive worker ID and port mapping; shared benchmark-store mutation → per-benchmark lock. Child work uncertainty → MainOrchestrator's direct subagent results and execution tree → revised delegated work. Live abnormal execution → separate Overseer model verdict → explicit notification or force cancel. Benchmark generalization failures → archived experiment scores → model-authored future modification → new tested version.

## Evidence gaps

- Source pin is exact, but no empirical independent benchmark was executed. The methods described in README and source are not evidence of measured self-improvement.
- Positive S3*=A pertains to execution-health audit through event/callgraph evidence; it does not establish independent direct-code correctness audit. Review committee separately critiques *proposed future design* and should not be silently substituted for runtime S3*.
- S4=A is bounded to the shipped `runner.py` meta-improvement mode and its model-directed capability option, not every coding subagent. The deterministic statistically selected base revision does not by itself warrant A.
- S5=—: self-editing and benchmark goal optimization are not organizational constitutional authority.
