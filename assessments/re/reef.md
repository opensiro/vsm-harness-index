---
harness_id: reef
project_name: Reef
repository: https://github.com/Coral-Bricks-AI/reef
review_ref: 33aefaa12d78891bf5ba70a0d96b070d471ecc78
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Reef

## Review boundary

- System in focus: The public Reef repository as a **multi-product open-source harness distribution**: (1) Reef model/tool runtime, (2) AlphaCumen finite-query multi-specialist finance operation built on it, and (3) Polyp autonomous experiment-program generator, coder, worker and analyzer loop. Function positives can be established at a concrete supported product recursion but are **not** extrapolated to a nonexistent single corporate multi-agent super-organization.
- Purpose and identity: General agent/tool construction, scoped finance analysis, and ongoing optimization of research experimentation. Specifically Polyp makes future research-line decisions and returns them to a queue of executable experiments.
- Relevant environment: Open-source Python package and scripts, external LLM provider or configured Claude CLI, specialist tools/data, PostgreSQL experiment state, separate CPU/GPU machines optional worker runtime, human-provided policy/constraints, optional monitoring/telemetry integrations.
- Standard-distribution boundary: Shipped Reef `reef.react.run_react`, `reef.llm`, tools/constraints/enforcer; deployed `alphacumen.swarm.run` with roster/synthesizer/specialist ReAct calls; Polyp `polyp.runner.architect_watcher`, `suggest_experiment`, `architect_code_task`, `worker_watcher`/`worker_shift`, `architect_analyze_task`, Postgres-backed `polyp.queue.cbq` experiment status protocol. Treat these as separate concrete recursion witnesses, not automatically one joint operating structure.
- Credited operating / distribution surfaces: [`reef/react.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/react.py); [`reef/llm.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/llm.py); [`reef/enforcement.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/enforcement.py); [`reef/constraints.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/constraints.py); [`alphacumen/swarm.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/swarm.py); [`alphacumen/roster.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/roster.py); [`polyp/runner/architect_analyze_task.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_analyze_task.py); [`polyp/runner/suggest_experiment.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/suggest_experiment.py); [`polyp/runner/architect_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_watcher.py); [`polyp/runner/worker_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/worker_watcher.py); [`polyp/runner/architect_code_task.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_code_task.py); [`polyp/runner/worker_shift.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/worker_shift.py); [`polyp/queue/cbq.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/queue/cbq.py); [`reef/agents/headless_claude.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/agents/headless_claude.py). The Polyp auto-suggester route is an **optional active installed mode**, not merely a README aspiration.
- Adjacent first-party surfaces excluded from ownership: Private Coral Bricks hosted platform/sandbox or corporate management, claims of empirical performance in project README, screenshots/plots, research archives, external postprocessor content that only reformats current answers, static prompt/persona/skill reference files when not plugged into runtime, tests and demos, external data/GPU cloud accounts, maintainer GitHub workflows. Some architecture docs corroborate runtime entry but do not supply a missing decisive owner.
- First-party operating / deployment modes considered: Reef direct provider-compatible ReAct; AlphaCumen synthesizer and bounded parallel specialists; Polyp queue/architect/generator/worker/analyzer with configurable human constraints and operational worker availability. No assumption that all three packages run together or share a single executive controller.
- Recursion level: Concrete **finite-task** S1 in Reef/AlphaCumen and **longer research-campaign** task and prospective adaptation loops in Polyp; current Polyp roles are pipeline functions, not independently viable research departments. The same repository's multiplicity does not by itself prove organizational viable system or shared S2/S3/S5.
- Reviewed revision: `Coral-Bricks-AI/reef@33aefaa12d78891bf5ba70a0d96b070d471ecc78`; stable GitHub repository ID `1173617561`, immutable tree `1a552a677c6fd1b38e6e07bfa3b2761ff2f07d67`, Apache-2.0, public nonfork, source-first 2026-10-20.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The general Reef harness's `run_react` drives a first-party model/tool loop using direct-provider `reef.llm.chat`: inspect model tool calls, dispatch via defined tool functions, return results, continue toward a final answer. ConstraintEnforcer validates read-date limits, tool budgets and related run invariants in deterministic code; `AuditingEnforcer` logs violations for a run but is not an external reality auditor. [`reef/react.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/react.py); [`reef/llm.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/llm.py); [`reef/enforcement.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/enforcement.py); [`reef/constraints.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/constraints.py).

AlphaCumen is a shipped domain-specific run entry point `alphacumen.swarm.run`: an LLM synthesizer chooses bounded specialist invocations and can converge; financial persona specialists run Reef ReAct against their own rosters and return structured outputs to a common thread. This is effective task decomposition under one query; the specialist roster does not demonstrate separately viable autonomous departments or a permanent organizational center. Some platform-facing runtime hooks depend on external hosting; they are not credited for missing metasystem ownership. [`alphacumen/swarm.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/swarm.py); [`alphacumen/roster.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/roster.py); [`alphacumen/postprocessor.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/postprocessor.py); [`alphacumen/tools.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/tools.py).

Polyp separately ships Postgres queue commands and CPU/GPU workers. The architect watcher claims `enqueued` tasks for Claude Code work-item authoring; worker scripts produce experimental results; a separate analyze phase reads results/deviations, decides scientific `done`, `falsified`, or `blocked`, and records the verdict in Postgres and optional archives. When no immediate per-experiment iteration is active and worker capacity is available, the same first-party architect watcher launches `suggest_experiment`: headless Claude reads **whole historical experiment portfolio** and practical constraints, chooses new/continuing research line and actually calls `cbq submit --origin auto-suggest`. The queued task becomes part of the next researcher/worker operating cycle. This is a bounded **future experiment-program adaptation** function distinct from a single failed work-item retry. [`polyp/README.md`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/README.md); [`polyp/runner/README.md`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/README.md); [`polyp/runner/architect_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_watcher.py); [`polyp/runner/architect_code_task.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_code_task.py); [`polyp/runner/worker_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/worker_watcher.py); [`polyp/runner/worker_shift.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/worker_shift.py); [`polyp/runner/architect_analyze_task.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_analyze_task.py); [`polyp/runner/suggest_experiment.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/suggest_experiment.py); [`polyp/queue/cbq.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/queue/cbq.py).

## Operational model

The three independently packaged products serve different tasks, so a VSM capability may be evidenced at **one supported** standard-distribution boundary without inventing collaboration between them. The essential extra function here is Polyp's experimental portfolio intelligence; it does not imply that an AI model governs the entire Coral Bricks research company's mission or that task-specialist orchestration is organization-wide current management. Polyp analyzes actual prior experiment outcomes and converts a prospective hypothesis into *new scheduled experiment work*. This gives a source-bounded positive S4 at Polyp's program iteration recursion, not a measured claim about discovery effectiveness.

## S1 — Operations

- State: A
- Function: Goal-facing operational task execution, covering the ReAct model/tool loop, AlphaCumen's finite finance analysis requests, and Polyp's next queued research experiment execution.
- Disturbance / variety regulated: Unpredictable user queries and retrieved data, model-generated tool calls, specialist output, failed model/tool requests, uncertain results, workload failures, GPU capacity and experiment deviations.
- Decisive decision or feedback right: Configured LLM selects next tool use and stops in Reef; AlphaCumen planner/synthesizer issues specialist tasks and chooses whether another analytical round is needed; Polyp's architect coding agent/worker executes a concrete scheduled experimental work unit.
- Decision owner: Reef external configured model acting through first-party ReAct; AlphaCumen per-query synthesizer/specialist models; Polyp's model-backed Claude agent processes acting via first-party phase wrappers. Caller retains task, tool permission and scientific target.
- Supporting / enforcement mechanisms: reef.llm provider adapters, run_react tool dispatch/trajectory, AlphaCumen roster and common thread, Polyp queue claim/leases, worker heartbeat/recovery, result.json and scientific verdict transitions.
- Closure path: User/queue task → model-directed action or specialist delegation → tool/worker result → returned observations and continuation/final output; experiment branches/specs produce results and are finalized into evidence and queue status.
- Boundary reachability: Bundled Python source implements each path; ReAct dispatches direct provider calls; AlphaCumen invokes first-party Reef loop with specialist config; Polyp watcher and scripts call HeadlessClaude and queue commands to perform actions, not merely record prompt templates.
- Why this is / is not agent-owned: Removing model reasoning leaves only data transport, static constraints and queue scheduling: the next exploratory tool choice, qualitative analysis or authored code is not reproduced by the deterministic scaffolding.
- Evidence: [`reef/react.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/react.py); [`reef/llm.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/llm.py); [`alphacumen/swarm.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/swarm.py); [`alphacumen/roster.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/roster.py); [`polyp/runner/architect_code_task.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_code_task.py); [`polyp/runner/worker_shift.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/worker_shift.py); [`polyp/queue/cbq.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/queue/cbq.py); [`reef/agents/headless_claude.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/agents/headless_claude.py).
- Basis: Shipped source-wiring for supported separate products, structural.
- Confidence: High for real agent-loop wiring; no empirical model outcomes repeated here.
- Caveats: Three separately installable subsystems are alternative first-party modes, not automatically one co-resident distributed organization. AlphaCumen depends on external configured services and Polyp depends on headless Claude and operator-supplied worker hardware.

## S2 — Coordination

- State: —
- Function: No independently decisive relation demonstrably attenuates mutual operational interference between separately viable S1 business units.
- Disturbance / variety regulated: AlphaCumen parallel specialist analysis may overlap or disagree; Polyp work on CPU/GPU may contend for resources; queued tasks may race.
- Decisive decision or feedback right: Planner controls AlphaCumen specialist invocations under one question; Polyp queue leases and watchers serialize jobs, manage slots and stale claims. Neither is evidenced as separate inter-S1 organizational negotiation/feedback among viable departments.
- Decision owner: Per-request synthesizer or deterministic queue/watcher; no separately mandated S2 over viable operational S1 units.
- Supporting / enforcement mechanisms: Specialist roster/fan-out/common_thread, process pool, postgres SELECT FOR UPDATE SKIP LOCKED, locks/leases/heartbeat and worker reconciliation.
- Closure path: Task outputs return to synthesizer and results to experiment queue; resource contention is bounded by slot/claim machinery but no distinct S1-to-S1 reciprocal conflict damping changes interdepartmental behavior.
- Why this is / is not agent-owned: Seven domain personas operate as task-scoped specialist invocations of one finance query. Polyp workers/architects are phases of the same experiment pipeline rather than separately viable customer-facing organizational divisions. S2 cannot be conferred by fan-out or locks.
- Evidence: [`alphacumen/swarm.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/swarm.py); [`alphacumen/roster.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/roster.py); [`polyp/queue/cbq.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/queue/cbq.py); [`polyp/runner/architect_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_watcher.py); [`polyp/runner/worker_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/worker_watcher.py); [`polyp/runner/README.md`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/README.md).
- Basis: Bounded negative after inspecting both specialist and CPU/GPU queue coordinating routes.
- Confidence: Medium-high.
- Caveats: A deployment with truly independent research departments might add an S2 at a different organizational boundary, not evidenced by this distributed workflow.

### Absence scope

- Surfaces inspected: Reef ReAct caller/tool architecture, AlphaCumen shared-thread specialist fan-out, Polyp watcher/worker allocation, queue lock/lease/heartbeat and worker slots.
- Plausible first-party paths checked: Concurrent finance specialist analyses, GPU machine class and experiment resource contention, overlapping scientist roles and stale claims as possible inter-S1 interference.
- Why no material first-party path remains: These are finite task specializations and stage safety/throughput controls. Neither separate ongoing viable operational S1 departments nor reciprocal conflict-damping interventions returned to such units are shown in this released repo.

## S3 — Inside-and-now control

- State: —
- Function: No demonstrated agent-owned inside-and-now managerial portfolio/regulator over separately viable continuing S1 departments in a shared mission.
- Disturbance / variety regulated: Specialist quality/coverage and costs, failed experimental tasks and GPU capacity stress a current run or queued portfolio.
- Decisive decision or feedback right: AlphaCumen GP selects which specialists to invoke per single query; Polyp watcher scheduler moves queued phases, and code/analysis agents revise individual experiment verdicts. Neither has independent whole-organizational current manager authority reallocating viable S1 departmental obligations.
- Decision owner: Single-task model planner and first-party per-stage deterministic scheduler; human owner supplies scientific research mission/constraints.
- Supporting / enforcement mechanisms: Max rounds, pruning, per-tool limits and asof clamps; queue SQL status machine, worker heartbeat, capacity checks and code/analysis retries.
- Closure path: Current request/work item → narrower invocation, stop, retry, park or archive. No evidenced viable-department status→system-wide discretionary resource/commitment decision→binding returned adjustments to those departments.
- Why this is / is not agent-owned: A synthesizer GP name does not establish S3. The watcher CPU/GPU slot scheduler executes predetermined claim rules; its per-task control is not an agent-owned managerial law of a network of viable operating units.
- Evidence: [`alphacumen/swarm.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/swarm.py); [`reef/enforcement.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/enforcement.py); [`reef/constraints.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/constraints.py); [`polyp/queue/cbq.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/queue/cbq.py); [`polyp/runner/architect_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_watcher.py); [`polyp/runner/worker_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/worker_watcher.py); [`polyp/runner/worker_shift.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/worker_shift.py).
- Basis: Bounded negative after testing agent planner and queue scheduler as plausible S3 candidates.
- Confidence: Medium-high.
- Caveats: A real Coral Bricks organization/operator could decide budgets and direction externally; no first-party manager-right return is established.

### Absence scope

- Surfaces inspected: AlphaCumen planner/synthesizer decisions, constraints-enforcer, Polyp CPU/GPU scheduler and status protocol, per-experiment coder/analyzer roles and operator commands.
- Plausible first-party paths checked: GP dynamic specialist routing as alleged resource control; watcher free-slot and lease handling; experiment status/stop; externally supplied management budget.
- Why no material first-party path remains: One-query specialist orchestration and job queue control do not establish an independent whole-current S3 owner making binding resource/obligation decisions across independently viable S1 departments.

## S3* — Complementary audit

- State: —
- Function: No independent complementary verification of management's picture of *live operating reality* feeding back corrective recommendations to a distinguishable whole-current S3 manager.
- Disturbance / variety regulated: Finance findings might be inconsistent, experiment outcomes might be invalid, worker deviations might remain undocumented or obscure failure.
- Decisive decision or feedback right: Polyp's Analyzer agent independently reads a finished experiment's results/deviations and posts scientific done/falsified/blocked verdict in the queue. Reef AuditingEnforcer records constraint checks and AlphaCumen traces calls. They do not directly audit managerial current-state reports with challenge/returned S3 correction.
- Decision owner: Experiment analyzer model and deterministic recorders own their narrower scientific evaluation/audit trail; no designated independent management-auditor function.
- Supporting / enforcement mechanisms: polyp architect_analyze_task, queue cbq verdict status and archives, Reef AuditingEnforcer, model trajectory logging, AlphaCumen per-run traces.
- Closure path: Experiment evidence→scientific acceptance/falsification→queue archive/constraint update→future hypothesis generation; not audit of whole-operational control report→distinct S3 decision→corrective operating action.
- Why this is / is not agent-owned: An independent judge of experiment validity is a substantive assessment of experimental output but is not automatically a VSM S3* audit. The separate organizational current-management owner and alternate reality-information channel are missing.
- Evidence: [`polyp/runner/architect_analyze_task.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_analyze_task.py); [`polyp/queue/cbq.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/queue/cbq.py); [`reef/enforcement.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/enforcement.py); [`alphacumen/swarm.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/alphacumen/swarm.py); [`polyp/runner/suggest_experiment.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/suggest_experiment.py).
- Basis: Bounded absence with explicit inspection of the strongest positive candidate, the Polyp Analyzer.
- Confidence: Medium-high.
- Caveats: Future external field-audit or independent expert inspection would be out of scope. Scientific falsification feeding future research direction is credited under that function, not as S3*.

### Absence scope

- Surfaces inspected: Polyp analyze phase source, published reports/deviations and verdict/queue links, Reef AuditingEnforcer, AlphaCumen logs and synthesizer loop.
- Plausible first-party paths checked: Separate model analyzing experiment outputs as potential independent reality auditor; trace data as operating-evidence channel; scientific falsification triggering revisions.
- Why no material first-party path remains: The analyzer evaluates single experimental hypothesis/results for scientific acceptance/falsification, then records the result; it does not challenge an S3 controller's representation of independent S1 operating reality or return corrective managerial findings to an evidenced S3 owner.

## S4 — Outside-and-then intelligence

- State: A
- Function: Outside-and-then intelligence for **Polyp's future research-campaign direction**: choose prospective experimental hypotheses and future work lines based on past campaign results and constraints, then actually queue their execution.
- Disturbance / variety regulated: Previous experiments may plateau, falsify hypotheses or reveal blockers; idle iteration and GPU availability create a need to choose a different research trajectory rather than continue an unproductive line.
- Decisive decision or feedback right: Configured headless Claude Auto-suggester can autonomously OPEN a new research line or CONTINUE/reopen one skipped by per-experiment iterators, based on whole prior done/falsified/blocked history, and execute `cbq submit --origin auto-suggest` for the next experiment. A queued accepted task drives later coding/worker/analyze cycles.
- Decision owner: Polyp auto-suggester LLM proposes which *future hypothesis/line* warrants a program change; deterministic watcher admits when portfolio is quiet and a worker is live, Postgres queue commits the resulting candidate for later work. Human constrains research interests but is not required to select each suggested candidate.
- Supporting / enforcement mechanisms: architect_watcher generator trigger gated by live worker and low-watermark; suggest_experiment prompt reads portfolio history and constraints and calls HeadlessClaude; cbq submit validates and persists next task; subsequent architect_code_task and worker_watcher/shift execute it and analyzer returns verdict.
- Closure path: Completed/falsified/blocked experiment evidence and constraints → autonomous portfolio-level future-line decision → persisted Postgres next-experiment submission with origin/parent → new code+worker experimental actions in *subsequent* campaign iteration → fresh experimental evidence feeding the next generator. Can select an entirely new direction, not just rerun the last task.
- Boundary reachability: Polyp is separately installable and explicitly ships this generator path: architect_watcher invokes suggest_experiment only on idle/low-water queue, suggestion LLM can write a task spec and invoke cbq submit; queue status machine hands it to real first-party coding/worker watchers. No proprietary Coral Bricks service, undocumented evaluator or benchmark marketing is needed to establish the structural admission/return route, though runtime requires Postgres/Claude and worker.
- Why this is / is not agent-owned: Remove the auto-suggester model while retaining queue, watchers and worker: the portfolio's discretionary choice of which not-yet-planned hypothesis/new line to try no longer occurs. The fixed heartbeat and queue do not substitute a future intelligence decision. This is S4 specifically at the **bounded research-program recursion**, not proof of corporate market intelligence or a universal S4 for Reef/AlphaCumen.
- External distinction: The Polyp generator inspects research outcomes and constraints collected outside the presently executing experiment: portfolio-wide done/falsified/blocked history, lessons from earlier research lines, and new feasibility information. It runs when current iterators are quiet, not as a tool call of one experiment; this is the bounded experimental-program environment, not corporate market sensing.
- Future / prospective distinction: The generator decides which future experimental family/hypothesis is worth pursuing when the present iteration stops or misses a question, including reopening prior lines for documented new reasons. It does not merely correct the latest answer or retry a single failed step.
- Adaptation option generated: A newly authored research task specification including method, hypothesis and rationale, selecting a genuinely new or previously overlooked research line; the model can submit through the Postgres experiment queue with origin auto-suggest, or abstain if nothing is worthwhile.
- Path back into current capability / S3: A submitted suggestion becomes a durable enqueued Postgres work item; the existing architect watcher claims it for code/spec construction, a worker executes it, and an analyzer records results that inform the next selection. This changes subsequent research-program operation; it does not imply a separate S3 executive or corporate policy authority.
- Evidence: [`polyp/README.md`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/README.md); [`polyp/runner/README.md`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/README.md); [`polyp/runner/suggest_experiment.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/suggest_experiment.py); [`polyp/runner/architect_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_watcher.py); [`polyp/runner/architect_code_task.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_code_task.py); [`polyp/queue/cbq.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/queue/cbq.py); [`polyp/runner/worker_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/worker_watcher.py); [`polyp/runner/architect_analyze_task.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_analyze_task.py).
- Basis: Explicit supported end-to-end structural return path, with model-authored portfolio-level future-option selection and recorded queue submission.
- Confidence: Medium-high for Polyp shipped research-campaign S4; low for wider corporate strategy.
- Caveats: Effectiveness of proposed hypotheses and actual unattended deployment remain unmeasured here. The route is triggered only when conditions are met and supports a human veto/constraints; do not upgrade to A(P) because no distinct first-party binding S4 parent-governed mode is shown. Changing the *experiment program* is not changing Reef framework's global mission.

## S5 — Policy and identity

- State: —
- Function: No first-party legitimate identity/constitutional-purpose policy decider whose returned decision binds subsequent operations of the assessed multi-product org or research-program mode.
- Disturbance / variety regulated: Scientific risk constraints, time cutoffs, permitted datasets, human vetoes and domain policies bound runs.
- Decisive decision or feedback right: Caller passes HarnessConstraints, enforcer applies asof/tool limits; Polyp auto-suggester must respect explicit human-provided interest, constraints and allowed experiment kinds; it cannot change charter-level mission/values. CLI stop/cancel and the experiment rule are externally set.
- Decision owner: Researchers, embedding developers and upstream human organization set mission, allowed topics, governance and permitted hardware; no shipped first-party S5 authority-return workflow.
- Supporting / enforcement mechanisms: HarnessConstraints, deterministic LocalEnforcer, experiment constraints.md checks, cbq cancel/stop, permission/queue origin flags and developer prompt templates.
- Closure path: Human author-controlled rules → task admission/constraints; no identity-policy concern→legitimate parent deliberation/decision→new binding organizational constitutional policy returned to continuing S1/S3/S4 owners.
- Why this is / is not agent-owned: An experimental optimizer that selects future experiments within its provided user goal still cannot redefine the research institution's identity. Enforced scientific constraints and a veto window do not establish S5=P without authoritative constitutional decision closure.
- Evidence: [`reef/constraints.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/constraints.py); [`reef/enforcement.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/reef/enforcement.py); [`polyp/queue/cbq.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/queue/cbq.py); [`polyp/runner/suggest_experiment.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/suggest_experiment.py); [`polyp/runner/architect_watcher.py`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/runner/architect_watcher.py); [`polyp/README.md`](https://github.com/Coral-Bricks-AI/reef/blob/33aefaa12d78891bf5ba70a0d96b070d471ecc78/polyp/README.md).
- Basis: Bounded negative after examining explicit constraints and operator veto in all public modes.
- Confidence: High at the published code boundary.
- Caveats: A private parent Coral Bricks policy process is excluded; cannot infer a first-party S5 from branding or institutional existence.

### Absence scope

- Surfaces inspected: Reef HarnessConstraints and enforcement, AlphaCumen profile/roster prompt selection, Polyp auto-suggester guardrails, queue cancel/stop and human-defined research program constraints.
- Plausible first-party paths checked: User-defined research interests and allowed experiments, operator veto and termination, private hosted company policy as putative parent/S5 modes.
- Why no material first-party path remains: Permissions, task constraints and future experiment direction are real but no first-party constitutional identity-level decision and returned binding policy for this organization is shipped.


## Recursion

Reef ReAct and AlphaCumen are operating workstreams; the GP/specialists operate within bounded finance queries. Polyp forms an experiment production recursion with future campaign-direction decisions; the Auto-suggester can switch the next hypothesis/program line based on accumulated outcomes and submits the new task into the same Postgres workflow. Because this is a future-facing research strategy and returned acceptance path, S4=A is **only** supported for the Polyp optimization-campaign mode. It is not extrapolated to the core Reef framework, to AlphaCumen finance strategy, or to corporate investment allocation. Calling Polyp 'an autonomous optimizer' alone would be insufficient; source-backed review explicitly requires the watcher → portfolio evidence → model choice → actual queued new experiment → execution chain.

## Variety and escalation

Model/tool failures, scientific uncertainty, stalled workers, past falsifications and research constraints produce variety. ReAct may retry tools locally. AlphaCumen converges on a single finance question through its synthesizer. Polyp retains scientific verdicts as archived task evidence and can surface blocked states and stop controls, while the portfolio Auto-suggester selects the next research line under constraints. The queue's status labels and worker alerts are not automatically algedonic signals, nor is scientific QA automatically a separate S3* loop. An external human can veto queued work, but no first-party S5 parent policy decision mode is established.

## Evidence gaps

- Source-first publication: no live hosted API access or GPU experiments were run, and published quantitative benchmark results are **not** independently reproduced.
- This repo bundles distinct installable offerings; no first-party cross-product metasystem is inferred from common Git hosting.
- Polyp's future research-line generator is autonomous only within operator-set research constraints and watcher idle/capacity gate. The claim S4=A is bounded to its **future experimental portfolio** and code-wired admission/feedback, not to global corporate S4 capability.
- Polyp's Analyzer has access to scientific results but no independently evidenced S3 reality-audit mandate; a new deployment showing actual S3 corrective feedback would require separate assessment.
- A real parent-managed S3/S4/S5 structure may exist in the user's embedding organization, but its ownership and returned mandate are absent from this pinned public source.
