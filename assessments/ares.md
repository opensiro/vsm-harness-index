---
harness_id: ares
project_name: ARES
repository: https://github.com/Timwood0x10/ARES
review_ref: f03153acace190c555c3721019407a7df47c139f
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: —
autonomy_s4: C(P)
autonomy_s5: —
---

# ARES

## Review boundary

- System in focus: one first-party ARES runtime/serve organization at pinned revision `f03153acace190c555c3721019407a7df47c139f`, including the agent and task fabrics, L2 session/planning graphs, model-driven planner cognition, kernel scheduler and executor population, load/budget/lease/preemption machinery, runtime lifecycle manager, introspection/action control plane, evidence pipeline and the production-wired strategy-evolution lifecycle.
- Purpose and identity: operate durable autonomous agent processes that can plan and execute tool-bearing work while the kernel schedules shared execution capacity, recovers durable tasks across disposable agents and adapts runtime strategy from observed operating evidence.
- Relevant environment: user objectives, model responses, tool/service results, peer-agent activity, task dependencies and priorities, current executor capacity, failures and recoveries, runtime outcome/cost/latency/collaboration evidence, external tool/model availability and legitimate operator interventions.
- Standard-distribution boundary: the first-party ARES kernel/fabric/runtime, `ares serve` operating paths, shipped control/action APIs and production bootstrap wiring at the pinned revision. External model providers, third-party tools/MCP services, databases and user applications remain dependencies and do not donate VSM ownership.
- Credited operating / distribution surfaces: `internal/fabric/agent` planner cognition and live agent fabric; `internal/fabric/task`; `internal/kernel` scheduling, load, leases, priorities, preemption, snapshots and component lifecycle; `internal/runtime`; `internal/introspect`; authenticated `cmd/ares` agent/evolution action routes; production `internal/ares_bootstrap` evolution wiring; `internal/runtime/ares_evolution` strategy generation, evidence, gates, promotion and rollback; active-strategy feedback into the planner.
- Adjacent first-party surfaces excluded from ownership: repository CI/release and contributor governance; tests and fixtures used only to corroborate behavior; archived design material; examples; offline or development-only evaluation/arena surfaces that are not wired into the assessed operating mode; documentation-only aspirations; observability surfaces that expose evidence but do not own a decision right.
- First-party operating / deployment modes considered: ordinary `ares serve` peer/runtime operation; autonomous planner/tool sessions; multiple live agent-process execution through the shared kernel; automatic production-wired strategy evolution and rollback; optional manual-approval evolution mode; authenticated operator current-control through shipped agent lifecycle actions.
- Recursion level: one running ARES organization is the system-in-focus. Durable model-driven agent processes performing separate operational objectives are S1 units at this recursion; scheduler workers, queues, leases and kernel components are metasystem/support machinery unless they themselves close an organizational decision right.
- Reviewed revision: `f03153acace190c555c3721019407a7df47c139f`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

ARES implements a substantive agent operating system rather than a provider wrapper. Its task fabric makes work durable across disposable executors through leases, fencing epochs, checkpoints and recovery. The agent fabric supplies live executable agent processes, while the kernel scheduler repeatedly takes resumable tasks through capability-aware scheduling, lease acquisition, one semantic execution quantum and durable finalize/yield transitions. The architecture explicitly separates agent discretion from kernel enforcement: agents decide operationally while the kernel schedules, synchronizes and enforces resource/lifecycle constraints.

Operational reasoning lives in the L2 planner cognition. For each planner quantum it reconstructs context from the session graph and predecessor/tool outputs, exposes available tool schemas, applies currently active strategy steering and calls the model. The model chooses tool calls or a terminal answer. Tool calls become new graph nodes and a subsequent plan node; the shared scheduler executes those tool nodes and their outputs re-enter later planner context. This produces a model-owned decision/action/observation loop even though execution is split across graph and scheduler layers.

The shared scheduler provides explicit cross-unit regulation. Multiple autonomous agents/tasks can be simultaneously ready while individual agent processes are non-reentrant and shared execution capacity is finite. Candidate construction uses capability, live load, confidence and priority; `TryBegin` prevents concurrent quanta from occupying one cognitive process; bounded drain parallelism limits aggregate fan-out; and `PreemptLowerPriority` releases lower-priority running commitments when higher-priority ready work cannot otherwise obtain capable capacity. These decisions are algorithmic kernel policy rather than model-owned coordination judgment.

The same kernel supplies inside-and-now control. It has whole-system views of ready/running/resumable tasks, executors, loads, scheduling decisions and component health, and it changes current leases, priorities, budgets and assignments. The first-party control plane adds an attended mode: authenticated action routes can kill, resume or retry live agents while read surfaces expose the fleet and runtime health. The base regime is constructor-owned; the operator mode supplies a distinct parent current-control closure.

ARES also ships a production-wired adaptation subsystem. Runtime execution evidence feeds strategy fitness and evolution. Candidate strategies can change prompt templates, model parameters, tool choices and other runtime/genome properties. A `StrategyLifecycle` is the sole activation path, runs verification gates, promotes a candidate, watches live post-deployment evidence and rolls back on degradation; the planner reads the active strategy on subsequent quanta. The standard zero-LLM path remains capable of deterministic scoring/mutation/lifecycle decisions, so the decisive base S4 adaptation right is not established as AI-agent-owned. A separate configuration can hold a qualifying candidate in SHADOW until an authenticated operator invokes `/api/evolution/approve`, producing a legitimate parent adaptation mode.

No separate complementary current-operation audit is established at this boundary. Flight-recorder/replay/introspection evidence, ordinary evaluation, evolution shadow comparisons, regression gates and chaos/recovery mechanisms are valuable verification and adaptation machinery, but the reviewed operating distribution does not show a distinct S3* path that independently challenges an ordinary S1/S3 operational claim and returns findings into current corrective control as a complementary audit function. Likewise, configuration, security policy, guardrails and evolution approval do not establish an identity/ultimate-policy loop, so no S5 closure is credited.

Primary evidence:

- [`README.md`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/README.md) — agent-operating-system boundary, durable tasks, agent discretion/kernel enforcement, scheduling, recovery, dynamic DAG and runtime evolution.
- [`ARCHITECTURE.md`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/ARCHITECTURE.md) — system layering, leaderless kernel scheduling, agent/task fabrics, runtime control and evolution placement.
- [`internal/fabric/agent/planner_cognition.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/fabric/agent/planner_cognition.go) — model-owned tool/answer choice, graph growth, observation/context reconstruction and active-strategy actuation.
- [`internal/kernel/scheduler.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/scheduler.go) — shared scheduler state, live candidates, load/confidence, concurrency, governance and decision recording.
- [`internal/kernel/scheduler_dispatch.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/scheduler_dispatch.go) — bounded parallel drain and capability-aware priority preemption.
- [`internal/kernel/scheduler_execute.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/scheduler_execute.go) — candidate scoring, budget filtering, leases and atomic non-reentrant agent admission/requeue.
- [`internal/kernel/snapshot.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/snapshot.go) — whole-kernel current component snapshot and aggregate health state.
- [`internal/introspect/control.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/introspect/control.go) — current fleet/config/health, evolution and flight-recorder read surfaces.
- [`cmd/ares/agent_routes_agents.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/cmd/ares/agent_routes_agents.go) — authenticated agent kill/resume/retry and manual evolution approval actions.
- [`internal/ares_bootstrap/bootstrap_evolution.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/ares_bootstrap/bootstrap_evolution.go) — production evolution, evidence, shadow/rollback, lifecycle, scheduler and ticker wiring.
- [`internal/ares_bootstrap/evolution_lifecycle_config.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/ares_bootstrap/evolution_lifecycle_config.go) — deployment configuration for lifecycle thresholds and manual-approval mode.
- [`internal/runtime/ares_evolution/lifecycle.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/runtime/ares_evolution/lifecycle.go) and [`lifecycle_promotion.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/runtime/ares_evolution/lifecycle_promotion.go) — sole active-strategy state machine, verification, promotion, manual hold/approval and automatic rollback.

## Operational model

The primary S1 units are model-driven ARES agent processes whose planner quanta choose tool-bearing operational steps and final answers against local session/environment state. Tasks are deliberately more durable than individual agents, so task records, leases, scheduler workers and recovery processes are not automatically separate S1s: they transport or restore operational commitments. When several autonomous agents coexist, the shared kernel attenuates execution contention and regulates current commitments without taking over the agents' substantive task-level choices.

The metasystem is hybrid. S2 and the base S3 regime are deterministic first-party kernel mechanisms with function-specific closure, so they are constructor-owned rather than autonomous agent-owned. S3 additionally exposes an operator parent mode. S4 is similarly a complete first-party adaptation path whose default decisive promotion/mutation regime can operate algorithmically without an AI decision owner, while an optional manual gate transfers the final adaptation decision to the legitimate operator. No qualifying S3* or S5 path is established.

## S1 — Operations

- State: A
- Function: execute user/task objectives through model-selected plan/tool actions whose results become observations for subsequent operational decisions.
- Disturbance / variety regulated: request ambiguity, predecessor/tool outputs, session graph state, external tool results, changing task context and evidence that changes the next useful operational step.
- Decisive decision or feedback right: choose which available tool calls to make and with what arguments, whether to grow another plan round or terminate with an answer, within kernel/tool constraints.
- Decision owner: the model-driven ARES planner agent executing the session quantum.
- Supporting / enforcement mechanisms: L2 session graph, tool binder/schema exposure, task fabric, kernel scheduler, leases/fencing, depth limits, L1 tool enable/budget constraints, checkpoints and runtime strategy injection.
- Closure path: session/task reaches planner quantum → planner reconstructs context including prior tool outputs → model selects tool calls or final answer → tool calls become L2 nodes → scheduler executes them → results/checkpoints become predecessor observations → later planner quantum selects the next action or terminates with the answer.
- Boundary reachability: the first-party `plannerCognition` plus task-fabric/kernel execution path is wired into the standard runtime/serve architecture; no downstream organizational actor is needed to implement the model/tool feedback loop.
- Why this is / is not agent-owned: kernel scheduling and L1 limits constrain which actions can execute, but they do not predetermine the substantive tool sequence. Removing the model-driven planner removes the ordinary choice of tool calls, arguments and completion.
- Evidence: [`internal/fabric/agent/planner_cognition.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/fabric/agent/planner_cognition.go); [`internal/kernel/scheduler_execute.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/scheduler_execute.go); [`README.md`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: scheduling, tool eligibility, depth and resource limits are deterministic enforcement. `A` is based on model ownership of the substantive operational plan/tool decision, not on every runtime transition being autonomous.

## S2 — Coordination

- State: C
- Function: attenuate interference among distinct autonomous ARES operational agents competing for shared executable capacity and non-reentrant cognitive processes.
- Disturbance / variety regulated: multiple ready operational tasks can contend for the same capable agents and finite parallel capacity; assigning two quanta concurrently to one non-reentrant agent would corrupt its single cognitive state, and higher-priority ready work can otherwise be blocked behind lower-priority current commitments.
- Decisive decision or feedback right: choose/revise the function-specific cross-S1 scheduling/admission/preemption regime that determines which agent may accept a quantum, when saturated work must be released/requeued and which lower-priority commitment yields when scarce capable capacity is needed.
- Decision owner: no autonomous S2 actor is established. The first-party kernel implements the coordination relation and deterministically selects outcomes from configured priorities, capabilities, loads, budgets and concurrency constraints; revision of that regime remains constructor/configuration-owned.
- Supporting / enforcement mechanisms: shared `ReadyTasks`/resumable work source, capability matching, `LoadTracker`, per-agent confidence/priority, bounded `maxConcurrent`, leases/fencing, budget filtering, atomic `TryBegin(..., maxConcurrentPerAgent=1)`, release-to-READY and `PreemptLowerPriority` with checkpoint preservation.
- Closure path: concurrent S1 commitments become ready → kernel builds a live candidate pool and evaluates shared capacity/load → admission assigns a capable free agent or releases/requeues saturated work → higher-priority scarcity can preempt a lower-priority running commitment → later drains resume/reassign preserved work, changing which S1 executes its next quantum.
- Boundary reachability: these scheduler/admission/preemption mechanisms are the standard first-party kernel execution path over the live agent fabric, not an example-only or downstream extension.
- Why this is / is not agent-owned: the inter-S1 disturbance and attenuation relation are explicit and closed, but selection follows deterministic scheduler policy rather than discretionary coordination by an AI actor. This supports `C`, not `A`.
- Evidence: [`internal/kernel/scheduler.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/scheduler.go); [`internal/kernel/scheduler_dispatch.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/scheduler_dispatch.go); [`internal/kernel/scheduler_execute.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/scheduler_execute.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: leaderless task dispatch or peer messaging alone is not credited. Positive S2 rests specifically on shared-capacity/non-reentrancy/priority interference and the scheduler relation that attenuates it.
- Distinct S1 units: two or more live model-driven ARES agent processes/executors carrying separate operational commitments through the shared task and agent fabrics.
- Inter-S1 disturbance: ready commitments can compete for a finite capable-agent pool and a single agent's non-reentrant cognitive state; higher-priority work can also be delayed by lower-priority commitments occupying the only suitable agents.
- Attenuating coordination relation: capability/load-aware scheduling plus one-quantum-per-agent admission, bounded parallelism, release/requeue on saturation and targeted priority preemption.
- Feedback into subsequent S1 behaviour: a winning S1 receives the next quantum; a saturated candidate loses/relinquishes the lease and the work returns READY; a preempted lower-priority commitment preserves its checkpoint and resumes only on a later assignment.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited path regulates a concrete cross-unit execution conflict — scarce capable capacity and non-reentrant agents — and changes subsequent S1 execution specifically to damp that conflict, rather than merely moving messages or decomposing work.

## S3 — Inside-and-now control

- State: C(P)
- Function: regulate current whole-system commitments, executor capacity, priorities and agent lifecycle for the running ARES organization, with a separate legitimate operator intervention mode.
- Disturbance / variety regulated: the current organization can have many ready/running/suspended tasks, uneven agent load/capability, exhausted budgets, stale/dead executors, priority inversions and live agents whose current commitments must be stopped or restarted.
- Decisive decision or feedback right: base mode — determine the first-party current-control regime governing task leases/assignment, resource admission, priority preemption, budget-based yield and current executor lifecycle; parent mode — inspect the live fleet and choose to kill, resume or retry a current agent commitment.
- Decision owner: base mode — no autonomous metasystem actor; the kernel's function-specific current-control policy is deterministic/configured and therefore constructor-owned. Parent mode — the authenticated legitimate ARES operator using shipped action routes.
- Supporting / enforcement mechanisms: task/agent fabrics; scheduler candidate pool, leases/fencing, load/confidence/priority tracker, budget gates and preemption; kernel component registry/snapshot; scheduling decision recorder; introspection agent/health/config views; runtime manager; authenticated action API and audit logging.
- Closure path: base mode — current organization/task/executor state enters the kernel → scheduler/lifecycle rules alter present assignments, leases, priorities, yields and executable population → subsequent running/ready state changes. Parent mode — operator reads live fleet/current state → sends kill/resume/retry → runtime manager stops or restarts the target agent → subsequent scheduler/fleet state reflects the changed commitment.
- Boundary reachability: both the deterministic kernel-control path and authenticated lifecycle actions are shipped and wired into `ares serve`; neither depends on a downstream organization to close current-control feedback.
- Why this is / is not agent-owned: kernel machinery has real whole-system authority, but its current-control choices are mechanically derived from configured rules and inputs rather than made by an autonomous S3 actor. The separate operator path has a reconstructable parent owner. Hence `C(P)`, not `A`.
- Evidence: [`internal/kernel/scheduler.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/scheduler.go); [`internal/kernel/snapshot.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/kernel/snapshot.go); [`internal/introspect/control.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/introspect/control.go); [`cmd/ares/agent_routes_agents.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/cmd/ares/agent_routes_agents.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: lifecycle orchestration by name is not credited as S3. Positive credit rests on organization-wide current state plus authority over current resources/commitments/priorities; parent credit rests only on shipped current-agent actions, not generic administrator access.
- Whole-system current view: ready/running/resumable tasks, live agent/executor population, current load/confidence/priority, scheduler decisions, kernel component status/health and first-party fleet/introspection snapshots expose the present organization at the declared recursion.
- Current-control decision scope: current task assignment and lease ownership, per-agent admission, global parallelism, budget-driven yield, priority preemption, stale-executor recovery and operator kill/resume/retry of live agents.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | First-party deterministic kernel/current-control regime, configured by deployment/operator inputs | Ready/running task changes, capacity/load/budget conditions, priorities, executor health | Scheduler/lifecycle changes leases, assignment, yield/preemption or executor availability; later current operation follows the changed state | `internal/kernel/scheduler*.go`, `internal/kernel/snapshot.go` |
| Parent (`P`) | Authenticated legitimate ARES operator | Operator observes live agent/current state and elects kill, resume or retry | Shipped action route invokes runtime `StopAgent`/`RestartAgent`; target agent and subsequent scheduling state change | `internal/introspect/control.go`, `cmd/ares/agent_routes_agents.go` |

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary-audit closure is established for ordinary current ARES operation at the declared recursion.
- Disturbance / variety regulated: no distinct ordinary operational claim plus sufficiently independent complementary access/judgment/return path is established as an S3* function.
- Decisive decision or feedback right: not established for a complementary current-operation audit.
- Decision owner: none established.
- Supporting / enforcement mechanisms: flight-recorder timelines/decisions/diagnostics, event/evidence stores, evaluator and arena infrastructure, shadow comparisons, regression/evolution gates, health/anomaly introspection, chaos and recovery tooling.
- Closure path: these surfaces observe, test or constrain operation/evolution, but the reviewed standard runtime does not establish a separate complementary path that independently challenges an ordinary S1/S3 claim and necessarily returns a current-control correction on that claim.
- Why this is / is not agent-owned: evaluators, replay and shadow checks can make judgments in their own evaluation/adaptation contexts, but component names and independent test evidence do not create S3* unless the complementary audit relation to ordinary operational reporting and corrective current control is actually closed.
- Evidence: [`ARCHITECTURE.md`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/ARCHITECTURE.md); [`internal/introspect/control.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/introspect/control.go); [`internal/ares_bootstrap/bootstrap_evolution.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/ares_bootstrap/bootstrap_evolution.go); [`internal/runtime/ares_evolution/lifecycle.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/runtime/ares_evolution/lifecycle.go).
- Basis: explicit + structural absence
- Confidence: medium-high
- Caveats: the evolution shadow/regression path can use evidence independent of a candidate strategy and is material to S4 candidate admission, but this assessment does not re-label that future-capability verification as S3* for ordinary current operations without a distinct operational-claim audit closure.

### Absence scope

- Surfaces inspected: kernel decision/flight-recording and introspection layers; runtime health/anomaly paths; evaluator/arena/evidence architecture; production evolution bootstrap; shadow, eval/regression and rollback gates; chaos/recovery control surfaces.
- Plausible first-party paths checked: direct replay/flight diagnostics, independent scoring/shadow comparison, regression suites, anomaly detection, chaos observations, evaluator registry and evolution evidence/gate results.
- Why no material first-party path remains: the inspected paths are observability, evaluation, recovery or prospective strategy-verification mechanisms. None establishes all of the ordinary claim, materially complementary current-reality access, independent audit judgment and returned corrective S3/S1 control required for S3* at this operating boundary.

## S4 — Outside-and-then intelligence

- State: C(P)
- Function: learn from real operating/environment evidence, generate prospective runtime-strategy alternatives, evaluate them before/after deployment and return a selected strategy into present ARES capability, with an optional parent-owned promotion mode.
- Disturbance / variety regulated: task outcomes, latency/cost, scheduler and recovery performance, collaboration/tool-use evidence and runtime degradation can make the currently active prompt/parameter/tool/runtime strategy less suitable for future work.
- Decisive decision or feedback right: base mode — generate/evaluate candidate strategy changes and determine promotion/rollback through the first-party GA/lifecycle/gate regime; parent mode — when manual approval is configured, decide whether the already-gated SHADOW candidate may become ACTIVE.
- Decision owner: base mode — the first-party evolution constructor path: algorithmic mutation/selection, evidence aggregation, verification gates and `StrategyLifecycle`; no AI actor is required to own the decisive promote/rollback right in the standard zero-LLM-capable mode. Parent mode — the authenticated legitimate ARES operator deciding the manual promotion gate.
- Supporting / enforcement mechanisms: runtime evidence/event store, fitness aggregation, population/genome mutation, optional experience guidance/LLM scoring, shadow sampler/evaluator, eval/regression gates, active-strategy manager, blacklist/residency controls, rollback policy/watch loop, metrics and lifecycle snapshots.
- Closure path: real operation produces outcome/performance evidence → evolution constructs prospective candidate strategies and evaluates them against active capability → lifecycle gates either reject, hold or promote a candidate → active strategy becomes the planner's live prompt/parameter steering source (and wider runtime evolution paths can compile/apply attributed changes) → subsequent operation runs under changed capability; post-deployment degradation can automatically restore the previous strategy. In parent mode the same path pauses at SHADOW → operator approval → `Approve()` → promote → subsequent planner/runtime behavior changes.
- Boundary reachability: production `wireGAEvolution` constructs the wired evolution system, starts the lifecycle watch/observer and evolution scheduler/ticker, while planner cognition reads the active strategy during normal execution. Manual approval is a shipped lifecycle configuration plus authenticated action route.
- Why this is / is not agent-owned: the S4 relation is substantive and closed, but its base decisive adaptation right can operate through deterministic/algorithmic GA, scorers, thresholds and lifecycle rules without an autonomous AI decision owner; optional LLM hints/scoring do not transfer ownership of the mandatory promote/rollback right. The parent mode independently closes the same adaptation function through an operator decision. Therefore `C(P)`.
- Evidence: [`internal/ares_bootstrap/bootstrap_evolution.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/ares_bootstrap/bootstrap_evolution.go); [`internal/ares_bootstrap/evolution_lifecycle_config.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/ares_bootstrap/evolution_lifecycle_config.go); [`internal/runtime/ares_evolution/lifecycle.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/runtime/ares_evolution/lifecycle.go); [`internal/runtime/ares_evolution/lifecycle_promotion.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/runtime/ares_evolution/lifecycle_promotion.go); [`internal/fabric/agent/planner_cognition.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/fabric/agent/planner_cognition.go); [`cmd/ares/agent_routes_agents.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/cmd/ares/agent_routes_agents.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: internal optimization by itself is not S4. Positive credit rests on real runtime/environment evidence feeding prospective candidate capability changes and a deployed return path into future operation. LLM-backed hints/scoring are optional and therefore are not used to upgrade base ownership to `A`.
- External distinction: the evolution plane consumes evidence from actual task outcomes and operating channels such as latency/cost, scheduler/recovery behavior, collaboration/tool execution and post-deployment performance rather than only replaying an internal planning trace.
- Future / prospective distinction: candidate strategies are generated as alternative future configurations and judged in shadow/eval/regression gates before activation; the lifecycle preserves active/previous strategies and monitors whether a newly promoted future option should remain or roll back.
- Adaptation option generated: first-party population/genome mutation and runtime-evolution machinery produce candidate changes to prompt/parameters/tools and other evolvable runtime strategy/genome properties; experience guidance may bias those options when wired.
- Path back into current capability / S3: `StrategyLifecycle.promote` deploys the selected strategy through the active-strategy manager; ordinary planner quanta read the active strategy and apply its prompt/parameter steering, while rollback restores the previous strategy when live evidence degrades.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | First-party algorithmic evolution/lifecycle regime | New runtime evidence and scheduled evolution produce a gated candidate or post-deployment degradation | Lifecycle rejects/promotes/rolls back; active strategy returns into planner/runtime capability for later work | `internal/ares_bootstrap/bootstrap_evolution.go`, `internal/runtime/ares_evolution/lifecycle*.go`, `internal/fabric/agent/planner_cognition.go` |
| Parent (`P`) | Authenticated legitimate ARES operator | Candidate has passed automatic gates and is held in SHADOW because `RequireManualApproval=true` | Operator calls `/api/evolution/approve` → `StrategyLifecycle.Approve()` promotes held candidate → active strategy governs subsequent operation | `internal/ares_bootstrap/evolution_lifecycle_config.go`, `cmd/ares/agent_routes_agents.go`, `internal/runtime/ares_evolution/lifecycle_promotion.go` |

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established for the ARES organization at the declared recursion.
- Disturbance / variety regulated: no identity- or ultimate-policy-level issue with a qualifying authority-and-return loop is established.
- Decisive decision or feedback right: not established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: deployment configuration, security/authentication, runtime guardrails, tool/capability restrictions, scheduler/governance budgets, evolution gate thresholds, manual candidate approval and repository/project governance.
- Closure path: these mechanisms constrain current operation or adaptation, but the reviewed standard distribution does not expose an organizational identity/ultimate-policy issue that reaches legitimate ultimate authority and returns an authoritative identity/policy decision to govern subsequent ARES operation.
- Why this is / is not agent-owned: hard limits, guardrails and parent approval over a strategy candidate are decisions about execution or adaptation, not automatically S5. No autonomous or parent-owned system-level identity/ultimate-policy function is established.
- Evidence: [`README.md`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/README.md); [`ARCHITECTURE.md`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/ARCHITECTURE.md); [`internal/ares_bootstrap/bootstrap_evolution.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/internal/ares_bootstrap/bootstrap_evolution.go); [`cmd/ares/agent_routes_agents.go`](https://github.com/Timwood0x10/ARES/blob/f03153acace190c555c3721019407a7df47c139f/cmd/ares/agent_routes_agents.go).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: a deployment owner can of course edit configuration or source, but generic ownership of the process/project is not enough for S5 without a first-party function-specific identity/ultimate-policy closure path.

### Absence scope

- Surfaces inspected: runtime/kernel architecture, deployment configuration, security/auth action plane, tool/resource governance, evolution guardrails/lifecycle/manual approval, introspection/control surfaces and repository governance documentation.
- Plausible first-party paths checked: system/model prompts and strategy prompts, operator configuration, security/auth policy, budget/tool restrictions, evolution approval/rollback, kernel lifecycle control and project governance.
- Why no material first-party path remains: every inspected positive authority concerns operational execution, current control, adaptation admission or software-project governance. None supplies a runtime organizational identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned governance loop at the assessed ARES recursion.

## Distributed OSS parent arrangement

ARES is public OSS, but this assessment does not infer organization-level parent governance from maintainers or contributors. The credited parent modes are local to a supported running deployment: its authenticated operator can intervene in current agent operation (S3) and, when configured, approve a held strategy adaptation (S4). Repository governance is outside the operating ownership boundary and is not credited as S5.

## Self-hosted and non-human modes

The assessed standard distribution supports self-hosted operation. Automatic kernel scheduling/current control and automatic strategy evolution remain valid constructor modes without a human parent in the decision loop. Operator presence is therefore recorded only as an alternative supported S3/S4 parent mode, not as evidence that every deployment is parent-governed.

## Recursion

The top-level system is one ARES runtime organization. Model-driven agent processes are operational S1 units with their own local task/session environments, while the shared kernel/fabrics regulate their coexistence. Durable tasks, executor registrations and spawned recovery replacements are not promoted to separate viable recursions merely because they have lifecycle state. A downstream application that embeds ARES or assigns durable organizational identities to subteams would require its own system boundary and evidence.

## Variety and escalation

ARES attenuates operational variety through capability matching, per-agent non-reentrancy, bounded concurrency, leases/fencing, budgets, priorities and checkpointed cooperative preemption while preserving model discretion inside each operational quantum. Failures can move through lease expiry/recovery and runtime lifecycle mechanisms; present-work interventions can escalate to an authenticated operator through the control plane. Adaptation variety is handled separately by the evolution plane: runtime evidence is compressed into fitness/gate judgments, candidates are promoted or rejected, and degraded active strategies can roll back. Manual-approval mode explicitly escalates a qualifying S4 adaptation decision to the parent operator. None of these escalation paths is treated as S5 unless the underlying issue is identity/ultimate-policy level, which was not established here.

## Evidence gaps

The pinned repository is large and exposes several optional evolution/evaluation modes. The assessment therefore credits only production-reachable paths evidenced by bootstrap/runtime wiring and does not borrow ownership from tests, archived designs or optional LLM helpers. A future revision could change S4 ownership if an AI actor becomes the decisive owner of adaptation selection/promotion rather than merely an optional hint/scoring component. Likewise, a future first-party audit path could establish S3* if it independently challenges ordinary operational claims and closes findings into current control, and a governance/identity runtime could establish S5 if ultimate-policy issues are operationally routed to legitimate authority and returned into operation.
