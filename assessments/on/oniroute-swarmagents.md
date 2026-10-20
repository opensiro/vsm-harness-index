---
harness_id: oniroute-swarmagents
project_name: OniRoute SwarmAgents
repository: https://github.com/AniruddhaDas1/OniRoute_SwarmAgents
review_ref: c47d553ad2e1aa547cce000c095a9feda5434ee2
reviewed_at: 2026-10-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OniRoute SwarmAgents

## Review boundary

- System in focus: The Python OniRoute 1.2.1 standard-distribution local-first engineering request-to-artifact runtime, including first-party inference-backed engineering workers, orchestration, quality gates and recovery. Distinguish this real code-generation path from a distinct, demonstrably simulated swarm-wave execution subsystem.
- Purpose and identity: Accept a user's software construction objective, organize a workspace and implementation contract, invoke a configured LLM to generate source/configuration content, enforce local boundary and quality checks, and return/report an engineering outcome.
- Environment: The user's natural-language specification and workspace filesystem; local Python tooling, code constraints and validation; configured OpenAI-compatible or Ollama endpoints/model roster; provider/network failures, competing file targets, output defects and budget/permission constraints.
- Standard-distribution boundary: First-party `cli/main.py`, `runtime/router/router.py`, engineering/invocation/model/provider abstraction, `runtime/agent`, workspace, quality/review/healing/validation and governance/control code shipped at pinned Git revision. Model inference itself is the configured external endpoint; source-level decisions in model requests are first-party agent-owned when the package builds the autonomous request and uses its response in a loop. Code labels alone do not establish higher functions.
- Credited operating / distribution surfaces: [cli/main.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/cli/main.py); [runtime/router/router.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/router/router.py); [runtime/engineering/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/engineering/engine.py); [runtime/invocation/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/invocation/engine.py); [runtime/models/manager.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/models/manager.py); [runtime/models/providers.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/models/providers.py); [runtime/agent/execution_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/agent/execution_engine.py); [runtime/swarm/autonomous_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/swarm/autonomous_engine.py); [runtime/swarm/coordination_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/swarm/coordination_engine.py); [runtime/review/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/review/engine.py); [runtime/healing/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/healing/engine.py); [runtime/validation/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/validation/engine.py); [runtime/control/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/control/engine.py); [runtime/governance/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/governance/engine.py); [runtime/contracts/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/contracts/engine.py); [runtime/allocation/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/allocation/engine.py).
- Adjacent first-party surfaces excluded from ownership: documentation promises and diagrams, release/CI, certification scores and simulation-only test fixtures; external hosted model intelligence apart from first-party invocation/feedback wiring; an end user's ongoing organization or maintainer governance.
- First-party operating / deployment modes considered: the supported `oniroute build`/CLI router project assembly + P5 engineering generation/quality/repair and verification; direct AgentExecutionEngine single-agent invocation; `AutonomousExecutionEngine.execute_swarm` simulated six waves with synthetic ArtifactRecords and calculated token/cost ledger; `SwarmCoordinationEngine.coordinate_swarm` artifact bus/consensus based on those waves; operator model/settings/governance/control and self-hosted configurations.
- Recursion level: One user-requested engineering project/task organization with role-specific implementation contracts, one first-party operational coding work cell per contract, locally orchestrated synthesis and verification. Do not assume a lasting, mutually independent organization of viable S1 divisions from simulated waves.
- Reviewed revision: `AniruddhaDas1/OniRoute_SwarmAgents@c47d553ad2e1aa547cce000c095a9feda5434ee2` and Git source tree `fb2f6c61640ed27c96f97ba70f367a81c561da92`; original GitHub repo ID 1321987742; created 2026-08-03T16:14:10Z; Apache-2.0 public nonfork, default main.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

A large local-first Python package exposes a Typer CLI and a natural-language router. The first-party router constructs skill discovery and profiles, deployment plan, swarm snapshot and workspace scaffold, blueprint, allocation and engineering contract reports, then instantiates an `EngineeringWorkerEngine`. The worker engine accepts typed contracts; `InvocationPlanner.plan_batch` makes ordered implementation and optional documentation tasks, checks dependencies, constructs `InvocationRequest` and `SelectionRequest`, and executes `InvocationEngine.invoke` using `ModelManager` and provider adapter, parses its actual `InvocationResponse.text`, then writes generated content to a bounded target path. The router calls QualityGateEngine, RepairPlanner, SelfHealingEngine, VerificationEngine and AcceptanceEngine on worker outputs. The separate `AgentExecutionEngine.execute_session` similarly invokes models on prompts assembled from agent sessions and stores actual response artifacts. These are source-wired first-party *inference-backed* task work paths, not merely downloaded external agent CLI wrappers. [runtime/router/router.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/router/router.py); [runtime/engineering/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/engineering/engine.py); [runtime/invocation/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/invocation/engine.py); [runtime/models/manager.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/models/manager.py); [runtime/agent/execution_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/agent/execution_engine.py); [runtime/review/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/review/engine.py); [runtime/healing/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/healing/engine.py).

The names `AutonomousExecutionEngine` and `SwarmCoordinationEngine` are not treated as evidence of autonomous swarm workers. In the distinct `execute_swarm` six-wave routine the code constructs `ArtifactRecord` without model invocations, calculates `task_tokens = 350 + len(task.agent_role)*10`, fabricates per-task cost and can inject forced failures; it labels an artifact as produced without generating task-specific source. The coordinator then derives status messages, artifact exchange, handoffs, synthetic conflict injection and consensus from these result records. These useful demonstration/control surfaces must not be promoted to live multi-S1 operations or independent S2/S3/S3* governance. [runtime/swarm/autonomous_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/swarm/autonomous_engine.py); [runtime/swarm/coordination_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/swarm/coordination_engine.py).

## Operational model

The standard supported mode is a user-commissioned engineering deliverable with model-mediated coding decisions under typed contract boundaries and local safety checks. The decisive source generation is delegated to an actual LLM invocation via the first-party invocation engine and the returned text is applied to the workspace. Orchestration, model selection rules, workspace safety, static quality/review, repair action selection and acceptance are in important parts deterministic; they do not inherit autonomy from the model call. Provider selection is configured and governance-bounded. Source inspection establishes reachability, **not** live model endpoint success, deployed performance or independent organizational viability.

## S1 — Operations

- State: A
- Function: Environment-facing coding work: interpret a bounded engineering contract, generate task-specific files and fulfill implementation/documentation outcomes under actual workspace and model feedback.
- Disturbance / variety regulated: Open-ended user goals, unfamiliar code requirements, different engineering disciplines, model response uncertainty, target path and quality failures.
- Decisive decision or feedback right: Choose substantive generated content for requested project deliverables from model reasoning conditioned on a contract; the returned content changes a workspace and is evaluated.
- Decision owner: A configured model acting through the first-party EngineeringWorkerEngine/InvocationEngine request-response path; the agent's task-specific coding choice, not deterministic task-order scheduler or Python file writer, supplies the autonomous discretionary decision.
- Supporting / enforcement mechanisms: Typed task batches, capability/request routing, model manager/provider protocols, workspace path checks, response parsing, file writing, quality and verification gates. The AgentExecutionEngine has a separate model invocation route for a READY agent session.
- Closure path: Natural-language build request → first-party router/project contract → EngineeringWorkerEngine constructs prompt/request → provider-backed model returns source text → workspace file write → quality review and repair/verification → accepted or rejected user-visible engineering outcome. An implementation/documentation task is conditioned on earlier content/dependencies.
- Boundary reachability: CLI/router constructs EngineeringWorkerEngine and its execute_all_contracts, invokes actual provider adapters, writes returned generated file content and checks it; no hypothetical plugin or test-only demo is needed.
- Why this is / is not agent-owned: Remove model actor but keep typed task planner, file writer and deterministic gates: no substantive novel source content can be chosen for arbitrary user specifications in the normal P5 path. The first-party engine explicitly creates and consumes inference requests; not merely a static prompt file or external agent harness shell.
- Evidence: [runtime/router/router.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/router/router.py); [runtime/engineering/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/engineering/engine.py); [runtime/invocation/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/invocation/engine.py); [runtime/agent/execution_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/agent/execution_engine.py); [runtime/models/manager.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/models/manager.py); [runtime/models/providers.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/models/providers.py); [runtime/review/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/review/engine.py)
- Basis: structural source-wired first-party inference-backed operational mode
- Confidence: High for code-path ownership and bounded positive, not live success.
- Caveats: The simulated swarm execution is NOT counted as additional autonomous work; no live model calls or built-project quality were observed.

## S2 — Coordination

- State: —
- Function: No established ongoing regulator of reciprocal interference between separately continuing viable S1 units at this assessed one-user engineering-project recursion.
- Disturbance / variety regulated: Multiple task/wave outputs may collide at file/artifact handoff boundaries; phase sequencing and role capacity could produce conflict or bottlenecks.
- Decisive decision or feedback right: SwarmCoordinationEngine computes messages, conflict records, handoffs and consensus from swarm-wave results, while InvocationPlanner enforces a deterministic one-contract task order. Neither changes two independently operating continuing S1 units based on real reciprocal disturbance.
- Decision owner: Deterministic runtime and configured static phase/contract dependencies; not an autonomous inter-S1 regulator.
- Supporting / enforcement mechanisms: SharedContextManager, MessageBus, ArtifactExchange, HandoffCoordinator, SwarmConsensusEngine, ordered wave queue and per-contract task dependency checking.
- Closure path: Simulated waves → synthetic ArtifactRecords/status → deterministic coordination/consensus reports; or one real worker's ordered tasks → output checks. Missing ongoing autonomous S1 department A ↔ department B interference → balancing rule → feedback to both continued business operations.
- Why this is / is not agent-owned: This is the strongest candidate for S2 in the source: coordination/conflict/handoff classes. However the wave execution is synthetic and the real inference-backed coding route has transient engineering contracts, not multiple continuing independently viable S1 operations with measured mutual disturbance and returned correction.
- Evidence: [runtime/swarm/autonomous_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/swarm/autonomous_engine.py); [runtime/swarm/coordination_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/swarm/coordination_engine.py); [runtime/engineering/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/engineering/engine.py); [runtime/router/router.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/router/router.py); [runtime/allocation/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/allocation/engine.py)
- Basis: bounded negative after direct positive candidate inspection
- Confidence: High at declared recursion.
- Caveats: A later real multi-agent execution could require new assessment; static names and injected force_conflict do not suffice.

### Absence scope

- Surfaces inspected: Swarm autonomous and coordination engines, artifact exchange/consensus, real engineering contract planner, router handoffs, shared-context paths.
- Plausible first-party paths checked: Checked whether wave-level conflict and consensus actually regulate ongoing independent agent work, compared with true inference-backed P5 engineering execution and parent-style human coordination.
- Why no material first-party path remains: Wave artifacts/token ledgers/conflict injection are synthetic and coordinator records do not close an actual continuing S1-to-S1 disturbance loop; live worker task dependencies are intra-task scheduling. No material first-party S2 feedback relation is shipped at this recursion.

## S3 — Inside-and-now management

- State: —
- Function: No continuing present management ownership over multiple independent S1 operating units with binding resource, output-accountability and corrective interventions.
- Disturbance / variety regulated: Engineering failures, failed tests or workspace tasks may need rework and budget decisions across roles.
- Decisive decision or feedback right: The mission/router and control engine manage state, defaults, budgets, generation plan and acceptance for the current requested project; safety gates reject violations. The decisive whole-organization management authority/return to independently viable businesses is not demonstrated.
- Decision owner: Deterministic MissionControlEngine and router/workflow constructors plus operator configuration, with one real S1 coding actor. Their task-level plan enforcement is not agent-owned S3 management.
- Supporting / enforcement mechanisms: Mission control state, role allocation, budget tracking, quality/acceptance status, approval decisions and snapshot persistence.
- Closure path: User task → deterministic project contract and role assignment → model-generated work → static quality/rework control or terminal report. No whole-current organizational managerial report → S3 discretion → continuing multi-business allocation and subsequent operations.
- Why this is / is not agent-owned: Names MissionControl, engineering director, role manager or review gate cannot establish management as a distinct VSM function. The model makes source content, not cross-unit present management decisions; control plane largely sets fixed task state.
- Evidence: [runtime/control/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/control/engine.py); [runtime/router/router.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/router/router.py); [runtime/engineering/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/engineering/engine.py); [runtime/review/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/review/engine.py); [runtime/governance/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/governance/engine.py); [runtime/swarm/autonomous_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/swarm/autonomous_engine.py)
- Basis: bounded negative
- Confidence: Medium-high.
- Caveats: A surrounding human-run project can perform S3 outside this first-party runtime.

### Absence scope

- Surfaces inspected: MissionControlEngine, router plan/build, allocation/contract, budget/governance, quality/repair and control events.
- Plausible first-party paths checked: Tested principal/control current resource claims and remediation as S3, including legitimate operator oversight and the possible shared snapshot as S3 picture.
- Why no material first-party path remains: At most these are a bounded engineered task and an artifact simulation; no live ongoing independently viable S1 units, binding S3 portfolio management owner or corrective return to those units is evidenced.

## S3* — Complementary audit

- State: —
- Function: No separate audit of S3 whole-operations claims against direct S1 evidence, with findings fed back for S3 corrective governance.
- Disturbance / variety regulated: An implementation may be erroneous, violate security architecture, miss tests or contain a fabricated artifact result.
- Decisive decision or feedback right: QualityGateEngine examines engineering result/contract properties and VerificationEngine checks generated files; their first-party decisions are code/product QA. SwarmConsensusEngine evaluates synthetic wave statuses, not S3 reports. There is no distinct manager-facing complementary evidence investigation.
- Decision owner: Deterministic quality and verification code, with no independent organizational auditor authorized to challenge S3 present-control reporting.
- Supporting / enforcement mechanisms: Static architecture/security/performance/testing/documentation checks, repair planner, hashes, generated artifact validation and wave consensus.
- Closure path: Generated task output → deterministic quality/verifier result → bounded repair/acceptance. Missing whole-operations S3 managerial report → independent sampling of true S1 conditions → S3* adverse finding → revised managerial control.
- Why this is / is not agent-owned: Verification may inspect actual workspace artifacts, but code QA does not automatically become S3*; it does not audit an existing S3 manager's organizational account, and swarm review is based on simulated records.
- Evidence: [runtime/review/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/review/engine.py); [runtime/validation/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/validation/engine.py); [runtime/healing/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/healing/engine.py); [runtime/swarm/coordination_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/swarm/coordination_engine.py); [runtime/swarm/autonomous_engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/swarm/autonomous_engine.py); [runtime/control/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/control/engine.py)
- Basis: bounded negative
- Confidence: High for task QA scope.
- Caveats: Would need a separate S3 target, independent mandate and returned management correction to qualify.

### Absence scope

- Surfaces inspected: QualityGateEngine and VerificationEngine, repair planner/healing, SwarmConsensusEngine, MissionControlEngine reporting and simulation outputs.
- Plausible first-party paths checked: Checked whether direct file/evidence checks bypass the manager and change whole-S1 governance; examined synthetic wave audit and acceptance result recipients.
- Why no material first-party path remains: Only first-party technical deliverable checks and simulated wave consensus close. No distinct S3 management account, complementary audit decision owner or corrective S3 return channel is wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: No continuing strategic foresight process that gathers external future disturbances, evaluates organizational capability alternatives and adopts an ongoing future-directed change.
- Disturbance / variety regulated: Changing model/provider capabilities, external requirements or user technical goals could change future project designs.
- Decisive decision or feedback right: NaturalLanguageRouter maps current user text to build plan and smart defaults; ModelManager/configuration resolves provider and capability requests. Neither gives a standing agent decision for adapting the OniRoute organization across future environmental changes.
- Decision owner: Task-scoped routing/selection and external operator-defined model catalog; no independent continuing strategic actor or accepted policy owner.
- Supporting / enforcement mechanisms: Intent classifier, smart defaults, blueprint, skill discovery/ranking, model capability selection and research/knowledge documentation.
- Closure path: Current user request → deterministic planning and model selection → current deliverable. No outside/then sensing → alternatives for sustained capability viability → authorized adoption → changed future operation.
- Why this is / is not agent-owned: Selecting a model or reading a capability registry for today's code generation is operational routing rather than S4. Documentation on community skill discovery or strategy is not itself a closed future adaptation loop.
- Evidence: [runtime/router/router.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/router/router.py); [runtime/models/manager.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/models/manager.py); [runtime/engineering/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/engineering/engine.py); [runtime/control/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/control/engine.py); [runtime/governance/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/governance/engine.py)
- Basis: bounded negative
- Confidence: High.
- Caveats: Maintainers may adapt future versions, but GitHub maintainer work does not count as an assessed autonomous/parent-governed S4 runtime mode.

### Absence scope

- Surfaces inspected: NL router, model manager/registry, skill discovery, mission control, governance, project blueprint.
- Plausible first-party paths checked: Checked smart-default updating, provider capabilities, environmental knowledge scanning, repair loops and operator-based longer-term strategy acceptance.
- Why no material first-party path remains: All observed decisions target one current project or configured model catalog; no independent ongoing outside-and-then decision right with admitted persistent organizational capability adaptation is present.

## S5 — Policy and identity

- State: —
- Function: No ultimate mission/identity policy authority settling organizational values and resolving S3/S4 tension through a legitimate returned decision.
- Disturbance / variety regulated: Risk limits, workspace permissions, model permissions and contradictory task requests might need policy controls.
- Decisive decision or feedback right: PolicyEngine enforces developer/operator configuration, risk thresholds and budgets; MissionControlEngine accepts task commands. No model actor or parent deliberative S5 policy identity right changes ongoing constitutional rules.
- Decision owner: Developer/static policy and user settings are external constraints; model-generated source is one S1 operation, not an organization-wide ultimate identity owner.
- Supporting / enforcement mechanisms: PolicyEngine authorize/deny, BudgetTracker, AuditEngine, risk threshold, workspace boundary and mission-control commands.
- Closure path: Preconfigured permissions → request authorization → permitted model call or blocked task. No policy-identity case → legitimate authority decision → changed and returned organizational policy on subsequent ongoing operations.
- Why this is / is not agent-owned: Technical authorization and safety/risk control are meaningful but do not settle identity or purpose conflicts; a user providing a task is not automatically the shipped system's S5 parent-governed mode.
- Evidence: [runtime/governance/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/governance/engine.py); [runtime/control/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/control/engine.py); [runtime/router/router.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/router/router.py); [runtime/engineering/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/engineering/engine.py); [runtime/invocation/engine.py](https://github.com/AniruddhaDas1/OniRoute_SwarmAgents/blob/c47d553ad2e1aa547cce000c095a9feda5434ee2/runtime/invocation/engine.py)
- Basis: bounded negative
- Confidence: High.
- Caveats: A human owner might set values/mission through the external organization, not through a first-party S5 contract.

### Absence scope

- Surfaces inspected: PolicyEngine, MissionControlEngine, model governance checks, user CLI settings and workspace safety controls.
- Plausible first-party paths checked: Tested whether static policy/mission approvals and user/operator escalation reach legitimate parent constitutional authority and return a binding revised organizational identity/purpose decision.
- Why no material first-party path remains: Enforcement handles one task, permission/budget and model invocation; no first-party ultimate purpose-policy adjudication actor or parent-return path is demonstrated.

## Distributed OSS parent arrangement

The public repository and maintainers supply the program and policy defaults; a self-hosting human chooses the task and model endpoint. They are not an evidenced first-party parent system with separate autonomous S3/S4/S5 management decisions and accepted return paths to continuing S1 units. `MissionControlEngine` operates a single mission and `PolicyEngine` authorizes requests against static permissions and budget, without ultimate purpose deliberation. A surrounding company may have those functions, but is outside the frozen repo-relative runtime.

## Self-hosted and non-human modes

OniRoute explicitly supplies local-first and provider-independent interfaces and configured OpenAI-compatible/Ollama invocations; the first-party coding worker's operational discretionary content comes from a configured model. This assessment does not assume network/model availability. Self-hosted mode means external endpoint inference supporting a first-party task loop, not independent company-style autonomy of every declared swarm member. The simulation-only `AutonomousExecutionEngine` is excluded as an autonomous agent owner, notwithstanding the name.

## Recursion

The unit that demonstrably closes work through LLM feedback is a single coding/construction work cell under a user objective. Engineering contracts, agent profiles, swarm waves and named coordination gates may produce many records, but the analyzed wave engine is simulated and source evidence does not show independent, enduring viable S1 units whose cross-interference is regulated. Higher recursion could be built by a separately composed operator but is not established at this commit.

## Variety and escalation

The model receives task-specific ambiguity and decides source content; typed contract and workspace restrictions attenuate errors, quality/repair attempts implement bounded local rework. Budget and governance may block an unsafe execution or raise an operator-visible event. Synthetic forced failure and consensus are useful testing signals but cannot establish actual S2 homeostasis, S3 resource regulation, S3* management audit, S4 strategy or S5 identity. Failure/event labels do not alone establish an algedonic channel to a legitimate higher-recursion owner.

## Evidence gaps

Source-first code review of pinned commit and tree supports the positive first-party invoke/write path and bounded negatives. No provider endpoint, paid inference, generated user project, build quality or deployment performance was live-tested. Separate synthetic swarm wave records, fixed token formula and injected conflict are explicitly distinguished from real execution. Future releases might wire independent agents into the coordination layer and merit a fresh reassessment. Checked-in certification reports and docs alone are not counted as operational proof.
