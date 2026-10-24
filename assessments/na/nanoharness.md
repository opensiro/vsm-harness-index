---
harness_id: nanoharness
project_name: NanoHarness
repository: https://github.com/semi-hollow/NanoHarness
review_ref: 70a0285383630e78c31ea65023fe5e1e48b6f7dd
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# NanoHarness

## Review boundary

- System in focus: one supported NanoHarness multi-agent repository-work organization at pinned revision `70a0285383630e78c31ea65023fe5e1e48b6f7dd`, comprising canonical `AgentLoop` workers, adaptive planning, fanout scheduling, LIVE handoffs, isolated worktrees, candidate integration and the post-integration Finalizer.
- Purpose and identity: solve repository engineering tasks through multiple autonomous tool-using workers while the first-party harness coordinates dependencies, interference, integration and final acceptance.
- Relevant environment: user task and acceptance criteria, repository/worktree state, model-provider outputs, tool/test results, external MCP/services and operator input.
- Standard-distribution boundary: shipped `agent_forge/runtime` plus `agent_forge/multi_agent` and the first-party application/wiring paths that instantiate them. External model providers and external MCP/tools remain dependencies and do not donate ownership.
- Credited operating / distribution surfaces: `agent_forge/runtime/application/agent_loop.py`; runtime tool/context/governance wiring; `agent_forge/multi_agent/application/{planning,fanout,live_handoff}.py`; `agent_forge/multi_agent/adapters/{local_worker,live_agent_worker,git_workspace}.py`; associated multi-agent domain/ports and standard run composition that invokes these paths.
- Adjacent first-party surfaces excluded from ownership: `agent_forge/bench/**`, `agent_forge/evaluation/**`, `apps/workbench/**`, `benchmarks/**`, repository CI/tests/examples, showcase/control-plane demonstrations and repository-development experiments. The ordinary single-run operator console is not borrowed as a fanout-level parent S3 mode without whole-system multi-agent closure.
- First-party operating / deployment modes considered: canonical single-agent runtime; local fanout multi-agent execution; LIVE coordinated fanout with model-authored semantic handoffs; post-integration Finalizer review.
- Recursion level: the whole fanout run is the system-in-focus. Each independently executing worker AgentLoop is an S1 unit; a worker process or graph node is not counted merely by topology.
- Reviewed revision: `70a0285383630e78c31ea65023fe5e1e48b6f7dd`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

NanoHarness packages a canonical model/tool `AgentLoop` with persistent thread/run state, tool authorization, context construction, memory and governed side effects. Its multi-agent layer wraps the same first-party loop into isolated worker executions, creates task plans, schedules fanout work, maintains dependency and candidate state, optionally carries LIVE semantic handoffs between concurrent workers, integrates worker candidates into a staging branch and invokes a distinct read-only Finalizer over the integrated result.

The important organizational distinctions are functional rather than nominal. Adaptive planning establishes task decomposition before execution but is not by itself S3. Fanout scheduling owns current whole-system admission and integration rules but those decisions are deterministic/configured, so S3 is constructor-owned. S2 is stronger than mere scheduling because LIVE workers autonomously decide when and what semantically relevant READY/FEEDBACK/UPDATE evidence to publish to another active S1; the first-party coordinator validates route/version/freshness and injects that evidence into the receiver's next model step. S3* is also independently closed: the Finalizer runs a separate autonomous AgentLoop in a dedicated read-only worktree after integration, directly inspects the integrated repository rather than relying on worker self-reports, and its verdict changes the fanout's final status.

Persistent memory, model adaptation tests and benchmark/evaluation infrastructure were inspected but not promoted into S4. The standard operating boundary does not wire external/future sensing into a prospective capability-adaptation loop. Likewise prompts, permissions, approvals, skills and operator controls bound execution without establishing a system-level identity/ultimate-policy closure for the multi-agent organization.

Primary evidence:

- [`agent_forge/runtime/application/agent_loop.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/runtime/application/agent_loop.py) — canonical autonomous model/tool loop.
- [`agent_forge/multi_agent/application/planning.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/application/planning.py) — model-assisted decomposition and LIVE route construction.
- [`agent_forge/multi_agent/application/fanout.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/application/fanout.py) — current fanout state, dependency/write-scope scheduling, integration, finalization and terminal status.
- [`agent_forge/multi_agent/application/live_handoff.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/application/live_handoff.py) — frozen semantic routes, event validation/versioning/freshness and receiver delivery.
- [`agent_forge/multi_agent/adapters/live_agent_worker.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/adapters/live_agent_worker.py) — autonomous worker AgentLoop with model-callable LIVE handoff publication and next-step delivery.
- [`agent_forge/multi_agent/adapters/local_worker.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/adapters/local_worker.py) — isolated worker worktrees and separate read-only Finalizer AgentLoop.
- [`agent_forge/memory/application/service.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/memory/application/service.py) and [`agent_forge/tools/builtins/remember_memory.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/tools/builtins/remember_memory.py) — persistent memory inspected without equating memory with S4.
- [`agent_forge/runtime/application/operator_control.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/runtime/application/operator_control.py) — ordinary single-run operator control inspected without borrowing it as fanout-level S3 parent ownership.

## S1 — Operations

- State: A
- Function: independently perform assigned repository-engineering outcomes through iterative model/tool interaction inside each worker environment.
- Disturbance / variety regulated: repository structure, failing tests, tool observations, intermediate code state, incomplete information, execution failures and task-specific local decisions.
- Decisive decision or feedback right: select the next tool/action and arguments from current context and observations, decide how to react to results and decide when the assigned operational task is complete.
- Decision owner: the model-driven NanoHarness worker AgentLoop.
- Supporting / enforcement mechanisms: isolated worktrees, tool registry/router, permissions/approvals, context assembly, step/run control, persistent threads, model gateway, memory and runtime budgets.
- Closure path: subtask enters a worker → AgentLoop builds current context → model chooses a tool/action → first-party runtime executes or governs it → result returns to the loop → model chooses subsequent action or final answer → worker candidate/result returns to fanout control.
- Boundary reachability: both local and LIVE multi-agent worker adapters instantiate the shipped canonical AgentLoop inside the supported fanout runtime.
- Why this is / is not agent-owned: runtime mechanisms constrain and execute decisions but do not select the substantive repository action or response to changing observations; removing the model actor removes that discretion.
- Evidence: [`agent_forge/runtime/application/agent_loop.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/runtime/application/agent_loop.py); [`agent_forge/multi_agent/adapters/local_worker.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/adapters/local_worker.py); [`agent_forge/multi_agent/adapters/live_agent_worker.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/adapters/live_agent_worker.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: deterministic tool governance and worktree isolation support S1 but do not create the autonomous ownership claim.

## S2 — Coordination

- State: A
- Function: attenuate semantic staleness/dependency conflict among concurrently active worker S1s so downstream work can adjust to newly discovered producer evidence without destructive interference.
- Disturbance / variety regulated: a downstream worker may continue from stale assumptions while an upstream/peer worker discovers evidence or a dependency result that changes what the downstream worker should do; overlapping write scopes also create a structural concurrent-edit/merge conflict risk.
- Decisive decision or feedback right: decide when a discovered semantic change is coordination-relevant, what READY/FEEDBACK/UPDATE evidence to send on an allowed LIVE route and how the receiving S1 should alter its subsequent work after receiving that evidence.
- Decision owner: producer and recipient model-driven worker agents own the substantive coordination judgment and response. The runtime owns deterministic route/freshness validation and write-scope enforcement only.
- Supporting / enforcement mechanisms: `LiveHandoffCoordinator`, frozen semantic routes, route/version/freshness validation, receiver inboxes, safe next-model-step injection, dependency metadata and deterministic write-scope conflict scheduling.
- Closure path: distinct worker S1s execute concurrently → producer model encounters coordination-relevant evidence and calls the LIVE publish tool → first-party coordinator validates/routes/version-tags the event → receiver obtains the event as control input at the next model-step boundary → receiver model changes its subsequent action/plan; separately, conflicting write scopes are withheld from concurrent launch.
- Boundary reachability: LIVE publication is exposed as a first-party worker tool and the receiver control boundary is wired into the supported `LiveAgentWorker` execution path, not merely demonstrated in tests or examples.
- Why this is / is not agent-owned: the runtime cannot determine the semantic content, relevance or response on its own; those decisions disappear if the model workers are removed. Deterministic route/freshness/write-scope rules enforce the coordination channel without owning the semantic coordination discretion.
- Evidence: [`agent_forge/multi_agent/application/live_handoff.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/application/live_handoff.py); [`agent_forge/multi_agent/adapters/live_agent_worker.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/adapters/live_agent_worker.py); [`agent_forge/multi_agent/application/fanout.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/application/fanout.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: generic fanout, dependency edges and shared state are not the basis of `A`; the positive claim rests on the model-owned semantic handoff/response path. Write-scope serialization is constructor-owned supporting coordination.
- Distinct S1 units: two or more `LocalAgentWorker`/`LiveAgentWorker` instances, each running its own canonical autonomous AgentLoop against an isolated worktree and assigned subtask.
- Inter-S1 disturbance: semantically dependent concurrent subtasks can diverge when a producer discovers evidence that invalidates or updates the downstream worker's assumptions; overlapping declared write scopes can additionally create direct integration conflict.
- Attenuating coordination relation: frozen LIVE routes plus typed/versioned/freshness-checked READY/FEEDBACK/UPDATE events carry producer evidence to the intended receiver; the scheduler also prevents simultaneously launching known conflicting write scopes.
- Feedback into subsequent S1 behaviour: accepted LIVE events are injected at the receiver's next model-call boundary as control context, requiring the recipient model to operate with the updated evidence; write-scope gating changes which S1 may run concurrently.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the LIVE relation is explicitly tied to a concrete cross-worker semantic-staleness disturbance and changes later receiver behavior, while write-scope gating addresses a concrete concurrent-write collision. The claim does not rely on worker plurality, task edges or a generic mailbox alone.

## S3 — Inside-and-now control

- State: C
- Function: regulate the current fanout organization as a whole by deciding which commitments may run, which must wait, how shared concurrency is allocated, which candidates may be integrated and when the organization may transition to finalization.
- Disturbance / variety regulated: dependency violations, write-scope collisions, excessive concurrent workers, failed/blocked subtasks, stale LIVE prerequisites, multiple candidate outputs and incomplete integration state.
- Decisive decision or feedback right: admit/hold current subtasks, enforce `max_workers`, serialize conflicting write scopes, gate downstream work on dependency/LIVE readiness, integrate eligible candidates and decide when all current commitments are ready for finalization.
- Decision owner: first-party deterministic/configured `FanoutCoordinator` scheduling and integration regime; no autonomous whole-system current-control agent owns these decisions in the supported runtime.
- Supporting / enforcement mechanisms: persistent fanout state, subtask statuses/dependencies, running/pending sets, candidate/result records, write-scope metadata, LIVE route/freshness state, worktree integration helpers and finalizer transition logic.
- Closure path: coordinator observes current fanout-wide task/candidate/dependency state → deterministic eligibility/capacity/conflict rules choose launch/hold/integrate/finalize transitions → workers and integration state are changed accordingly → updated whole-system state feeds the next scheduling cycle.
- Boundary reachability: `FanoutCoordinator` is the shipped execution owner for supported multi-agent fanout and directly drives worker launch/integration/finalization.
- Why this is / is not agent-owned: AdaptivePlanner is model-driven but performs initial decomposition; it does not own the live whole-system inside-and-now decisions. Those current-control decisions remain encoded in the coordinator/runtime, so `C` is appropriate rather than `A`.
- Evidence: [`agent_forge/multi_agent/application/fanout.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/application/fanout.py); [`agent_forge/multi_agent/application/planning.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/application/planning.py); [`agent_forge/multi_agent/adapters/local_worker.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/adapters/local_worker.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary single-agent pause/steer/cancel facilities are not promoted to `C(P)` because a first-party parent loop with fanout-wide current view and returned whole-system control was not established at this recursion.
- Whole-system current view: `FanoutCoordinator` holds the complete current subtask plan/status set, dependencies, running/pending/completed/failed state, candidate outputs, LIVE-route readiness/freshness, integration state and concurrency occupancy for the fanout run.
- Current-control decision scope: current worker admission/holding, concurrency allocation, collision avoidance, dependency readiness, candidate integration and transition to finalization/completion.

## S3* — Complementary audit

- State: A
- Function: independently challenge the claim that the integrated multi-worker candidate actually satisfies the task and acceptance criteria after all worker changes have been combined.
- Disturbance / variety regulated: worker self-reports and successful integration can miss cross-change regressions, inconsistencies or requirement failures visible only in the combined repository state.
- Decisive decision or feedback right: inspect the integrated candidate directly and issue an autonomous PASS / NEEDS_REVISION / BLOCKED judgment with findings that determines whether the fanout may report clean success.
- Decision owner: the model-driven Finalizer AgentLoop.
- Supporting / enforcement mechanisms: dedicated finalizer worktree, read-only/mutation-tool removal, fresh finalizer thread, structured verdict parsing and deterministic mapping of verdict into overall fanout status.
- Closure path: workers produce candidates → coordinator integrates them → separate Finalizer AgentLoop receives the integrated repository in its own read-only worktree → model directly inspects artifacts/diff and emits verdict/findings → coordinator consumes the verdict → non-PASS verdict changes the fanout terminal result/control instead of allowing ordinary success.
- Boundary reachability: `LocalFanoutWorkerRunner.run_finalizer(...)` is directly invoked by the supported fanout path after integration and before final status is computed.
- Why this is / is not agent-owned: the runtime creates the isolation and parses/enforces the verdict, but the substantive audit judgment and findings are chosen by a separate model-driven agent with complementary direct repository access.
- Evidence: [`agent_forge/multi_agent/adapters/local_worker.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/adapters/local_worker.py); [`agent_forge/multi_agent/application/fanout.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/multi_agent/application/fanout.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary worker validation and repository benchmark/evaluator packages are not needed for this mapping and are not credited as S3*. The positive witness is the post-integration, separate, read-only Finalizer path.
- Claim being audited: the combined integrated candidate produced by the fanout organization satisfies the original task/acceptance criteria and is coherent as a whole.
- Ordinary reporting path: worker results/candidate summaries, task statuses and successful candidate integration into the staging branch.
- Complementary access path: a fresh Finalizer AgentLoop directly inspects the actual integrated repository/diff in a dedicated finalizer worktree with mutating tools removed.
- Independence boundary: the finalizer uses a separate thread/worktree and read-only tool boundary after integration; it is not the worker whose claim it evaluates and is not limited to worker self-report.
- Who acts on findings: the `FanoutCoordinator` consumes the structured finalizer verdict and maps it into overall `fanout_status`; NEEDS_REVISION/BLOCKED prevents a normal clean successful outcome.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established in the supported NanoHarness operating boundary.
- Disturbance / variety regulated: not established as S4; persistent memory, retries and benchmark feedback exist but do not by themselves model external/future change and generate organizational adaptation options.
- Decisive decision or feedback right: none established for future-oriented adaptation of the runtime organization.
- Decision owner: none established.
- Supporting / enforcement mechanisms: long-term memory service, `remember_memory`, context retrieval, skills, model configuration/adaptation tests, failure analysis and benchmark/evaluation datasets were inspected.
- Closure path: no standard operating path closes external/future distinction → adaptation option generation/selection → durable capability change → return into present capability/S3.
- Why this is / is not agent-owned: model workers can remember task-relevant facts and react to current observations, but memory persistence is not prospective intelligence. Benchmark/evaluation/failure-analysis surfaces are adjacent development/evaluation systems rather than wired owners of product-runtime adaptation.
- Evidence: [`agent_forge/memory/application/service.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/memory/application/service.py); [`agent_forge/tools/builtins/remember_memory.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/tools/builtins/remember_memory.py); [`agent_forge/evaluation`](https://github.com/semi-hollow/NanoHarness/tree/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/evaluation); [`agent_forge/bench`](https://github.com/semi-hollow/NanoHarness/tree/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/bench).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: a downstream deployment or repository-development workflow may use NanoHarness's memory/evaluation primitives to build adaptation, but that would be a separate evidenced system/path.

### Absence scope

- Surfaces inspected: long-term memory domain/service/tool; context retrieval/injection; skills registry/packages; model configuration and adaptation tests; benchmark/evaluation/failure-analysis/workbench surfaces; fanout planning/retry/finalizer paths.
- Plausible first-party paths checked: memory-derived future behavior, model adaptation, benchmark-driven tuning, failure feedback, skill evolution, planner replanning and finalizer findings.
- Why no material first-party path remains: implemented operating paths persist/retrieve context, solve current tasks or evaluate runs. The richer experiment/evaluation surfaces are adjacent rather than wired into a standard external-and-prospective capability adaptation loop for the assessed multi-agent runtime.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established for the NanoHarness multi-agent organization at the declared recursion.
- Disturbance / variety regulated: execution permissions, side-effect approvals, prompts/instructions, tool policies and operator controls constrain ordinary operation but no whole-system identity/ultimate-policy issue is closed.
- Decisive decision or feedback right: none established for identity/ultimate-policy questions.
- Decision owner: none established.
- Supporting / enforcement mechanisms: system prompts/instructions, safety guardrails, permissions, approvals, tool authorization, skills/configuration and operator-control surfaces were inspected.
- Closure path: no system-level identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned governance of subsequent multi-agent operation was found.
- Why this is / is not agent-owned: static prompts/policies and human approval of ordinary side effects constrain S1/S3 operation; they do not constitute S5 merely because they are high authority for a tool call.
- Evidence: [`agent_forge/runtime/application/tool_authorization.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/runtime/application/tool_authorization.py); [`agent_forge/runtime/application/operator_control.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/runtime/application/operator_control.py); [`agent_forge/safety`](https://github.com/semi-hollow/NanoHarness/tree/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/safety); [`agent_forge/context/application/system_prompt.py`](https://github.com/semi-hollow/NanoHarness/blob/70a0285383630e78c31ea65023fe5e1e48b6f7dd/agent_forge/context/application/system_prompt.py).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: users/developers can configure the harness and approve effects, but ordinary configuration/approval is not a first-party S5 closure without an identity-level issue and return path.

### Absence scope

- Surfaces inspected: system prompt/instruction resolution; runtime governance; safety/permission/approval modules; skills/configuration; operator console and run-control paths; multi-agent planning/fanout/finalizer control.
- Plausible first-party paths checked: prompt identity, safety/governance policy, human approval, operator pause/steer/cancel, task goals/acceptance criteria and skill configuration.
- Why no material first-party path remains: these surfaces govern ordinary task execution and side effects. None establishes a NanoHarness-wide identity/ultimate-policy issue reaching legitimate ultimate authority and returning as system-level policy closure.

## Summary

NanoHarness closes autonomous S1 through its canonical model/tool AgentLoop, autonomous S2 through model-authored LIVE semantic handoffs between isolated worker units, constructor-owned S3 through deterministic whole-fanout scheduling/integration control, and autonomous S3* through a separate read-only Finalizer over the integrated candidate. Memory/evaluation surfaces do not establish standard prospective S4 adaptation, and prompts/approval/governance surfaces do not establish whole-system S5. The standalone vector is `A / A / C / A / — / —`.
