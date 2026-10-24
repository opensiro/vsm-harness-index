---
harness_id: wasp
project_name: WASP
repository: https://github.com/agentwasp/agentwasp
review_ref: 8282a76f57aa4d0b7f2071321f064b26be942024
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C(P)
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: C(P)
---

# WASP

## Review boundary

- System in focus: one first-party self-hosted WASP `agent-core` organization at pinned revision `8282a76f57aa4d0b7f2071321f064b26be942024`, including the model/skill execution loop, GoalOrchestrator, persistent Agent runtimes, standard scheduler jobs, Resource Governor/CPI controls, Self-Integrity Monitor, Behavioral Learning loop, Identity Engine and first-party dashboard control surfaces.
- Purpose and identity: operate a persistent autonomous execution assistant for one operator, executing model-driven goals and skills, hosting multiple persistent agents, regulating aggregate runtime load, learning from environmental/user feedback and preserving operator-governed identity/policy boundaries.
- Relevant environment: operator requests/corrections, external web/API/integration state, files and tool outputs, model-provider responses, system CPU/latency/error pressure, persistent memories, agent/goal state and operator dashboard decisions.
- Standard-distribution boundary: first-party `containers/agent-core` runtime, shipped scheduler/cognitive systems, documented self-hosted dashboard and configuration surfaces at the pinned revision. External model providers, Telegram, third-party APIs/connectors and operator infrastructure are environmental dependencies; they do not donate VSM ownership.
- Credited operating / distribution surfaces: standard LLM/skill execution pipeline; GoalOrchestrator and AgentOrchestrator; global agent-step/token/CPU controls; Resource Governor and CPI feedback; dashboard all-agent snapshot plus pause/resume controls; scheduled Self-Integrity Monitor; default-enabled Behavioral Learning loop and prompt injection; IdentityManager plus dashboard identity save/reset/rollback closure.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor workflows and tests; documentation as evidence-only; telemetry/logging where merely observational; the disabled-by-default `MetaSupervisor`/`meta_orchestrate` research surface; Capability Evolution paths documented as opt-in/not auto-registered; examples and experimental surfaces not wired into the assessed standard operating mode.
- First-party operating / deployment modes considered: ordinary interactive model/skill execution; autonomous Goal Engine operation; persistent multi-agent operation under `AgentOrchestrator`; default-enabled scheduled cognitive jobs; attended parent/operator control through the shipped dashboard; and the identity constructor API exposed by `IdentityManager`. The research-only `META_AGENT_ENABLED=false` mode is not credited as an operating owner.
- Recursion level: one WASP assistant organization is the primary system-in-focus. Persistent autonomous agents/goals are treated as operational S1 units where they pursue distinct outcomes inside the shared organization; their creation alone is not treated as evidence of lower-recursion viability.
- Reviewed revision: `8282a76f57aa4d0b7f2071321f064b26be942024`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

WASP is a Python self-hosted agent platform whose main request path combines deterministic intent/fast-path classification with a model-driven skill loop. The execution pipeline builds persistent context, lets the model choose skills over multiple rounds, executes those skills through `SkillExecutor`, returns tool/environment evidence to the model and validates the final response. The Goal Engine adds model-generated task graphs, persistent execution state, task failure/replanning and bounded autonomous execution. Separate persistent `Agent` entities can each hold independent objectives, goal queues and execution contexts.

At the multi-agent recursion, the standard `AgentOrchestrator` supplies deterministic cross-agent attenuation rather than autonomous coordination ownership. All active agents share model/provider capacity and system resources; the orchestrator limits concurrent agent steps with a semaphore, enforces a global token budget, applies CPU backpressure and ticks active agents through shared infrastructure. These mechanisms regulate concrete shared-capacity interference, but their coordination policy is configured/deterministic. The repository also contains a model-driven `MetaSupervisor` that decomposes teams into distinct non-overlapping roles and dependencies, but the pinned distribution explicitly keeps `meta_agent_enabled=false` and tests describe that path as research-only, so it is excluded from operating ownership.

Inside-and-now control is similarly hybrid. CPI computes a whole-system pressure signal from active goals, recent errors, latency, memory growth and CPU, then gates background autonomous/perception/dream activity under high pressure; the Resource Governor imposes aggregate caps. These are real current-control relations, but their base decisions are deterministic. A distinct parent mode is shipped through the dashboard: the operator receives an all-agent current snapshot including status, active goals and cognitive-budget state, and can pause/resume/archive agents through `AgentOrchestrator`, changing subsequent current operation.

WASP also ships a complementary audit path. `SelfIntegrityMonitorJob` periodically cross-checks self-model claims and epistemic confidence against direct observed skill success rates and `audit_log` outcomes, detects audit anomalies and cognitive-system silence, then automatically removes unsupported strengths, corrects epistemic confidence and queues improvement work. This is materially different access to operational reality than the self-model's ordinary claims. The audit judgment itself is threshold/rule-driven rather than owned by an autonomous model agent, so the path establishes S3* as a constructor rather than autonomous ownership. By contrast, Plan Critic and response validators are ordinary production-plan/output checks and are not credited as S3* merely because they use words such as critic or validator.

The strongest autonomous metasystemic path is Behavioral Learning. User corrections are detected in the live environment and queued; every two minutes the default-enabled `BehavioralLearnerJob` asks an LLM to derive a durable behavioral rule/few-shot/anti-pattern for avoiding the error, validates the generated rule, persists it as active behavioral memory and injects active rules into every future system prompt. That explicit environment → prospective adaptation option → changed future operating capability loop establishes autonomous S4.

Identity is operator-governed but has a dedicated constructor path. `IdentityManager` owns versioned identity prompt state, compiles identity properties such as autonomy/confirmation/risk posture, and injects a non-default identity into subsequent model prompts. The dashboard gives the single operator first-party save/reset/rollback authority, which establishes a closed parent S5 mode. Independently, the identity-specific write/version/injection API is a first-party constructor primitive to which an autonomous ultimate-policy actor could be composed, but WASP does not ship such an actor in the reviewed mode; this yields `C(P)`, not `A(P)`.

Primary evidence:

- [`docs-site/docs/architecture/execution-pipeline.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/architecture/execution-pipeline.md) — model/skill loop, parallel execution, returned observations, recovery and validation chain.
- [`containers/agent-core/src/goal_orchestrator/orchestrator.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/goal_orchestrator/orchestrator.py) — goal planning/execution, priorities, bounded replanning and first-party control-layer wiring.
- [`containers/agent-core/src/agent_manager/orchestrator.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/agent_manager/orchestrator.py) — persistent multi-agent runtime, shared concurrency, CPU and global-token controls.
- [`docs-site/docs/advanced/agent-orchestration.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/advanced/agent-orchestration.md) and [`agent_manager/meta_agent.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/agent_manager/meta_agent.py) — multi-agent isolation and experimental model-driven team supervisor; the latter is explicitly disabled by default.
- [`docs-site/docs/core-concepts/resource-governor.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/core-concepts/resource-governor.md), [`agent/cpi.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/agent/cpi.py) and [`scheduler/cpi_monitor.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/scheduler/cpi_monitor.py) — aggregate current-state pressure sensing and deterministic throttling.
- [`dashboard/routes/agents.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/dashboard/routes/agents.py) — parent all-agent current snapshot and pause/resume/archive closure.
- [`scheduler/integrity.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/scheduler/integrity.py) — complementary self-model/epistemic audit against direct operational evidence and corrective feedback.
- [`docs-site/docs/cognitive-systems/behavioral-learning.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/cognitive-systems/behavioral-learning.md) and [`scheduler/behavioral_learner.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/scheduler/behavioral_learner.py) — default-enabled user-correction → LLM adaptation-rule → future prompt closure.
- [`docs-site/docs/cognitive-systems/opportunity-engine.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/cognitive-systems/opportunity-engine.md) and [`dashboard/routes/opportunities.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/dashboard/routes/opportunities.py) — prospective suggestions and a documentation/code mismatch that prevents parent S4 credit at this ref.
- [`identity/manager.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/identity/manager.py) and [`dashboard/routes/identity.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/dashboard/routes/identity.py) — identity-specific constructor path and closed operator parent authority.
- [`docs-site/docs/operations/configuration.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/operations/configuration.md) — standard configuration boundary and default-enabled cognitive feature flags.

## S1 — Operations

- State: A
- Function: autonomously execute operator objectives through an iterative model/tool loop and bounded goal runtime that can absorb tool/environment results and choose subsequent operational action.
- Disturbance / variety regulated: request ambiguity, tool/API/file results, failed skill calls, changing goal/task state, external data and intermediate observations that alter the next useful action.
- Decisive decision or feedback right: choose model-driven skill calls and subsequent action/recovery across the LLM loop, and for autonomous goals generate and execute task plans within the configured repertoire.
- Decision owner: the model-driven WASP operational agent/goal actor.
- Supporting / enforcement mechanisms: intent fast paths, Context Builder, SkillExecutor, model manager, GoalOrchestrator, deterministic validators/guards, budgets, persistence, tool adapters and retry limits.
- Closure path: operator/autonomous objective enters the runtime → model chooses skills/actions → first-party executor runs them → observations/errors return to model/goal state → model continues, replans where applicable or completes → result returns to the operator/environment.
- Boundary reachability: the model/skill loop and Goal Engine are first-party standard operating surfaces documented and wired by the shipped `agent-core` runtime.
- Why this is / is not agent-owned: deterministic routing, limits and post-response guards constrain the loop, but substantive ordinary skill/action choices and goal planning are made by model inference rather than by those enforcement mechanisms.
- Evidence: [`execution-pipeline.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/architecture/execution-pipeline.md); [`goal_orchestrator/orchestrator.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/goal_orchestrator/orchestrator.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: fast paths and final validators can deterministically handle or constrain some requests. The `A` claim is based on the standard model-driven execution/goal path, not on every possible fast path being agent-owned.

## S2 — Coordination

- State: C
- Function: attenuate interference among multiple persistent autonomous agents that share finite model, token, CPU and execution capacity in one WASP deployment.
- Disturbance / variety regulated: simultaneously RUNNING agents can collectively monopolize model/provider capacity, exceed the global token budget, overload CPU or create excessive concurrent steps, degrading other S1 units despite each unit being locally valid.
- Decisive decision or feedback right: choose/revise the cross-agent concurrency, shared-token and load-throttling regime that determines when an S1 may take its next step under shared pressure.
- Decision owner: no autonomous standard-mode S2 owner is packaged. `AgentOrchestrator` deterministically enforces configured limits; the model-driven `MetaSupervisor` that could own richer team coordination is disabled by default and explicitly described as research-only at this revision.
- Supporting / enforcement mechanisms: `asyncio.Semaphore` across agent steps, global Redis token counter, CPU threshold, active-agent store, shared model manager and deterministic throttling events.
- Closure path: multiple S1 agents request/take ticks → shared concurrency/token/CPU conditions are evaluated → over-capacity work is deferred/throttled or serialized → capacity/next window becomes available → affected agents resume later.
- Boundary reachability: shared throttles are wired directly into the standard `AgentOrchestrator.tick()` path used by persistent agents; no adopter-defined transport is needed for the coordination relation.
- Why this is / is not agent-owned: the inter-S1 disturbance and attenuation path are explicit, but the decisive regime is static/configured and mechanically enforced. An autonomous coordination actor would have to be composed/enabled beyond the credited standard mode, so the state is `C`, not `A`.
- Evidence: [`agent_manager/orchestrator.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/agent_manager/orchestrator.py); [`agent-orchestration.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/advanced/agent-orchestration.md); [`config.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/config.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: Plan Critic is not credited as S2 because validating one goal plan does not regulate interference among distinct S1 units. The disabled MetaSupervisor corroborates a richer possible pattern but does not upgrade the credited runtime mode.
- Distinct S1 units: two or more persistent autonomous `AgentRuntime` instances with separate objectives, goal queues and execution contexts hosted by the same `AgentOrchestrator`.
- Inter-S1 disturbance: these agents share model infrastructure, CPU and global token/step capacity, so aggregate activity can starve or overload peers even when no individual agent violates its own goal semantics.
- Attenuating coordination relation: the orchestrator serializes/bounds simultaneous agent steps, stops all new agent ticks when the global token budget is exhausted and skips ticks under CPU overload.
- Feedback into subsequent S1 behaviour: throttled agents do not take the current step; once the semaphore/window/load permits, a later tick re-enters their runtime and their next operational action occurs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited mechanism exists specifically to regulate contention created by multiple autonomous agents sharing finite resources, not merely to pass messages or assign subtasks.

## S3 — Inside-and-now control

- State: C(P)
- Function: maintain an organization-wide current view of operational pressure/commitments and intervene in current autonomous activity through aggregate throttling or parent supervisory controls.
- Disturbance / variety regulated: excessive active-goal pressure, recent operational error rate, high latency, runaway memory growth, CPU saturation, resource-cap exhaustion and current agent commitments that should be paused/resumed on behalf of the whole deployment.
- Decisive decision or feedback right: determine which current organizational activity is allowed to proceed under aggregate pressure and, in the parent mode, decide which persistent agents remain active, paused or resumed after reviewing current organization state.
- Decision owner: base `C` mode — deterministic CPI/Resource Governor/AgentOrchestrator rules execute configured current-control responses with no autonomous S3 owner. Parent `P` mode — the single self-hosting operator owns supervisory pause/resume/archive decisions through the first-party all-agent dashboard.
- Supporting / enforcement mechanisms: CPI component collectors and `agent:cpi_high`; Resource Governor counters/caps; AgentOrchestrator status persistence; dashboard all-agent snapshot showing status, active goals and cognitive budgets; scheduler jobs that honor CPI gating.
- Closure path: current whole-system pressure/status is gathered → base deterministic controls gate background/current work, or the parent operator reviews the all-agent snapshot and chooses pause/resume/archive → AgentOrchestrator persists the new status/removes or recreates runtime state → subsequent ticks follow the changed current-control decision.
- Boundary reachability: CPI/governor controls are wired into standard scheduler/runtime operation, while the all-agent dashboard and pause/resume/archive endpoints are shipped first-party operator surfaces over the same `AgentOrchestrator`.
- Why this is / is not agent-owned: WASP has concrete whole-system current-control structure, but the base current-control judgments are configured thresholds rather than model-owned discretion. The operator dashboard supplies a separately closed parent supervisory mode, hence `C(P)` rather than `A`.
- Evidence: [`agent/cpi.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/agent/cpi.py); [`scheduler/cpi_monitor.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/scheduler/cpi_monitor.py); [`resource-governor.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/core-concepts/resource-governor.md); [`dashboard/routes/agents.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/dashboard/routes/agents.py); [`agent_manager/orchestrator.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/agent_manager/orchestrator.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: per-goal replanning is local S1/current-task recovery, not whole-system S3 by itself. Parent credit relies on the all-agent status/budget view plus operative pause/resume closure, not merely on a generic human edit or stop button.
- Whole-system current view: CPI combines active-goal count, recent error rate, latency, memory growth and CPU; the dashboard separately lists every persistent agent with current status, active-goal count/IDs and cognitive-budget usage.
- Current-control decision scope: base rules gate background autonomous/perception/dream work and enforce shared operational caps; the parent can remove an agent from active operation by pausing/archiving it or restore it with resume, changing current commitments represented in subsequent ticks.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | No autonomous S3 actor is packaged; deterministic CPI/governor/orchestrator rules execute the configured current-control regime | Aggregate active-goal/error/latency/memory/CPU pressure or configured resource-cap conditions | CPI/resource flags and governor/orchestrator gates defer or reject current activity; later operation follows the enforced regime | `agent/cpi.py`, `scheduler/cpi_monitor.py`, `governance/governor.py`, `agent_manager/orchestrator.py` |
| Parent (`P`) | Self-hosting WASP operator | Operator reviews the all-agent current snapshot and decides an agent should pause, resume or be archived | dashboard endpoint → `AgentOrchestrator.pause_agent`/`resume_agent`/`archive_agent` → persisted status/runtime change → subsequent ticks include/exclude that S1 | `dashboard/routes/agents.py`, `agent_manager/orchestrator.py` |

## S3* — Complementary audit

- State: C
- Function: challenge WASP's ordinary self-model and epistemic claims with materially different direct operational evidence and return discrepancies into subsequent control/state.
- Disturbance / variety regulated: the agent can believe it has strengths or domain confidence that no longer match actual observed skill outcomes, while silent cognitive subsystems or recent error spikes can remain invisible in the self-model's ordinary narrative.
- Decisive decision or feedback right: judge whether claimed strengths/confidence are contradicted by direct skill success rates, audit-log outcomes or missing cognitive heartbeats and decide which self-model/epistemic corrections follow.
- Decision owner: the standard distribution supplies the full complementary evidence and corrective path, but the decisive audit judgment is encoded in deterministic thresholds/rules in `SelfIntegrityMonitorJob`; no autonomous auditor owns that judgment in the credited mode.
- Supporting / enforcement mechanisms: direct SQL reads from `audit_log` and cognitive-system tables, Redis self-model/epistemic state, success-rate thresholds, drift threshold, report persistence, automatic self-model removal/epistemic correction and improvement queueing.
- Closure path: ordinary self-model/epistemic claims persist → scheduled monitor independently reads raw operational success/error/heartbeat evidence → threshold comparisons produce findings → unsupported strengths are removed, epistemic confidence is corrected and improvement work can be queued → later reasoning uses the corrected state.
- Boundary reachability: `SelfIntegrityMonitorJob` is imported and registered by the standard runtime and the default configuration exposes `integrity_monitor_enabled=true`; its evidence and correction stores are the same first-party runtime stores used by live cognition.
- Why this is / is not agent-owned: the complementary access and feedback closure are real, but the audit judgment is deterministic rather than an autonomous agent's discretionary independent assessment. That is a function-specific constructor path (`C`), not `A`.
- Evidence: [`scheduler/integrity.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/scheduler/integrity.py); [`configuration.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/operations/configuration.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: Plan Critic and final ResponseValidator are not used as the positive S3* witness because they are routine checks inside the production path rather than complementary access to operational reality.
- Claim being audited: self-model assertions of strengths and epistemic confidence, plus the implicit claim that core cognitive producers are operating normally.
- Ordinary reporting path: `agent:self_model`, `agent:epistemic` and ordinary runtime/cognitive state describe what WASP believes about its capability and confidence.
- Complementary access path: `SelfIntegrityMonitorJob` reads measured skill success/failure data, recent `audit_log` anomalies and direct DB/Redis heartbeat evidence from the cognitive producers rather than relying on those self-claims.
- Independence boundary: the scheduled monitor is separate from the model process that creates/uses the self-model and checks alternative operational records; however its verdict logic remains deterministic and therefore does not establish autonomous audit ownership.
- Who acts on findings: first-party monitor actuators remove invalid strengths, overwrite drifted epistemic confidence and queue improvement items; the corrected state then affects subsequent cognition/operation.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert explicit environmental/user correction signals into prospective behavioral adaptation that changes how future WASP operation reasons and acts.
- Disturbance / variety regulated: user corrections reveal that current behavior is systematically wrong — for example hallucination, inappropriate refusal, wrong-skill choice or missing-context handling — and repetition of that behavior would degrade future viability with the operator/environment.
- Decisive decision or feedback right: interpret the correction context, formulate the durable future-facing rule/few-shot/anti-pattern that should prevent recurrence and admit that adaptation into active behavioral memory.
- Decision owner: the model-driven `BehavioralLearnerJob` owns semantic rule extraction; deterministic safety filtering/deduplication/storage constrain and persist the result.
- Supporting / enforcement mechanisms: correction-pattern detection, Redis pending queue, two-minute scheduler, adversarial-rule filter, behavioral-rules DB, dedup/conflict checks, future prompt injection and notification surfaces.
- Closure path: user/environment correction is detected → exchange is queued → scheduled LLM analyzes the failure and generates a behavioral adaptation rule → safe active rule is persisted → Context Builder injects active learned rules/few-shots into future system prompts → subsequent S1 behavior operates under the adaptation.
- Boundary reachability: Behavioral Learning is documented as default-enabled, registered in `main.py`, and its stored active rules are consumed by the standard prompt builder; no downstream learner or manual prompt edit is required.
- Why this is / is not agent-owned: the semantic choice of what future behavior should change is produced by an autonomous model call. The queue, filters and database only transport/constrain that adaptation judgment, so the decisive S4 option-generation right is agent-owned.
- Evidence: [`behavioral-learning.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/cognitive-systems/behavioral-learning.md); [`scheduler/behavioral_learner.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/scheduler/behavioral_learner.py); [`memory/behavioral.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/memory/behavioral.py); [`configuration.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/operations/configuration.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: generic memory, current-goal replanning and Skill Evolution are not needed for this mapping. The Opportunity Engine is also not credited as a parent S4 mode because, at the pinned ref, its dashboard `accepted` endpoint only changes status; the documented action-execution closure is not present in the inspected route.
- External distinction: a user correction is a first-party captured environmental distinction about how the running organization failed to meet operator expectations; the learner retains the request, bad response and explicit correction context.
- Future / prospective distinction: the LLM is asked what rule the agent should follow to avoid the error in future interactions, turning the observed correction into a forward-looking behavioral distinction rather than merely recording the past event.
- Adaptation option generated: a typed behavioral rule plus optional `skill_poison` and dynamic few-shot pair describing the changed future response/skill policy.
- Path back into current capability / S3: accepted-safe rules are saved active and injected into every later system prompt, directly modifying the operating repertoire used by subsequent S1 decisions; operator/dashboard surfaces can deactivate bad rules if needed.

## S5 — Policy and identity

- State: C(P)
- Function: maintain and revise the WASP organization's explicit identity, purpose/autonomy posture and ultimate operating principles, with a dedicated constructor path and a separately closed single-operator parent mode.
- Disturbance / variety regulated: changes or disputes about what the agent is for, how autonomous it should be, confirmation/risk posture, proactive behavior and other identity-level directives that should govern subsequent operation rather than one ordinary task.
- Decisive decision or feedback right: authoritatively choose the current identity prompt (or restore a prior/default identity) that defines purpose/autonomy/policy posture for future model operation.
- Decision owner: base `C` mode — `IdentityManager` exposes an identity-specific save/version/rollback/injection path but no autonomous ultimate-policy actor is wired to own it. Parent `P` mode — the single deployment operator owns the authoritative identity decision through the first-party dashboard.
- Supporting / enforcement mechanisms: Redis identity prompt/compiled state, version history, prompt compilation of autonomy/confirmation/risk/proactive directives, dashboard save/reset/rollback API, audit logging and Context Builder identity injection.
- Closure path: identity/policy issue reaches the identity constructor or operator dashboard → a new/default/prior identity is selected → `IdentityManager` saves/compiles/version-controls it → subsequent prompt construction injects the active identity/directives → later S1 behavior is governed by the returned decision.
- Boundary reachability: IdentityManager is initialized by the standard runtime and passed into prompt construction; dashboard identity routes call its live save/reset/rollback methods. Both constructor and parent paths are first-party surfaces of the assessed self-hosted deployment.
- Why this is / is not agent-owned: WASP intentionally supplies a function-specific identity decision/return primitive, supporting `C`, but does not wire an autonomous agent as legitimate ultimate identity authority. The standard closed authority is the deployment's single operator, supporting `(P)` rather than `A`.
- Evidence: [`identity/manager.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/identity/manager.py); [`dashboard/routes/identity.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/dashboard/routes/identity.py); [`agent/context.py`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/containers/agent-core/src/agent/context.py); [`configuration.md`](https://github.com/agentwasp/agentwasp/blob/8282a76f57aa4d0b7f2071321f064b26be942024/docs-site/docs/operations/configuration.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: `prime.md`, safety guards and ordinary task approvals are not independently treated as S5. Parent credit rests specifically on the Identity Engine's identity-level authoring/version/return path. Self-improvement of implementation code is not assumed to grant autonomous ultimate-policy authority.
- Identity / ultimate-policy issue: the `DEFAULT_PROMPT` explicitly states the organization's identity/purpose, autonomous operating mode and governing principles; IdentityManager compiles materially identity-level properties such as autonomy, confirmation threshold, risk tolerance and proactivity.
- Ultimate authority in each claimed mode: base `C` exposes the identity-specific decisive path but leaves legitimate autonomous authority to a downstream composition; parent `P` assigns authoritative selection to the self-hosting single operator through the dashboard identity editor/reset/rollback controls.
- Return-to-operation path: operator/constructor decision → `IdentityManager.save`/`reset`/`rollback` → active prompt + compiled identity cache/Redis state → `format_for_prompt`/Context Builder injection → subsequent model decisions operate under the selected identity.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | No autonomous ultimate-policy owner is wired; first-party `IdentityManager` exposes the identity-specific decision/version/return primitive | Downstream composition supplies a legitimate autonomous identity authority and calls the identity-specific write path | `save`/`reset`/`rollback` → compiled active identity → prompt injection into subsequent operation | `identity/manager.py`, `agent/context.py` |
| Parent (`P`) | Single self-hosting WASP operator | Operator decides the agent's purpose/autonomy/policy identity should change or a prior/default identity should be restored | dashboard identity save/reset/rollback → `IdentityManager` state/version update → future prompt injection → later operation follows the authoritative identity | `dashboard/routes/identity.py`, `identity/manager.py` |

## Recursion

At the assessed deployment recursion, persistent model-driven agents/goals can act as distinct operational units while sharing the same orchestration, model/resource and dashboard metasystem. WASP also supports sub-agent creation and an experimental MetaSupervisor, but nesting/decomposition alone is not evidence that every child is a complete lower viable system. The assessment therefore uses child agents only where a function-specific cross-S1 relation is evidenced.

## Variety, escalation and closure

WASP attenuates operational variety through intent routing, capability/policy gates, per-request/goal budgets, shared multi-agent throttles, Resource Governor caps, CPI background gating and deterministic response validation. It amplifies regulatory capacity through model-driven goal/skill choices, multiple persistent agents, external integrations, memory/world-state surfaces, scheduled cognitive jobs and durable learned behavioral rules.

Exceptional or high-pressure conditions remain function-relative: high CPI suppresses background autonomous work as S3 current control; integrity discrepancies enter S3* corrective state; user corrections enter S4 learning; identity changes reach S5 parent authority. The queue/status/alert mechanisms carrying those signals are not treated as additional VSM functions.

## Evidence gaps

No material evidence gap requires `?` at the pinned boundary. The boundary-sensitive conclusions are explicit: the repository's own `System 2`/`System 3` labels do not determine classification; `MetaSupervisor` is excluded from operating ownership because it is disabled/research-only; S3* is constructor-owned because the complementary auditor is deterministic; Opportunity Engine documentation is not allowed to donate a parent S4 closure absent matching code; and S5 separates the identity constructor primitive from the operator-owned parent authority.