---
harness_id: hivegate
project_name: HiveGate
repository: https://github.com/hivegate-ai/hivegate
review_ref: 96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# HiveGate

## Review boundary

- System in focus: First-party HiveGate Python FastAPI/Agno production agent runtime, including persisted agent configurations, team construction, leader/worker satellite supervisor integration, worker job queue and user approval return paths at the pinned commit.
- Purpose and identity: Serve user-specific model-backed agents and agent teams through authenticated REST, with persisted prompts, sessions and user-linked external tools, and optional remote-container worker execution.
- Environment: Tenant/user requests, OAuth-scoped external Google/Microsoft tools, Agno model and team APIs, external configured LLM providers, Postgres/Qdrant, remote agent workers, pending approvals and job errors.
- Standard-distribution boundary: Shipped `agents/`, `api/`, `supervisor/`, `remote_agent/`, `prompts/`, database and deployment adapters, including first-party invocation of Agno agents/Team. Agno implementation and providers are dependencies, not assumed first-party organizational decision or conflict-resolution machinery.
- Credited operating / distribution surfaces: Chat/commit endpoints, model-backed Agno Agent, first-party Team creation and supervisor-mode `build_supervisor_team`, JobProducer/Consumer and retry circuit-breaker, persisted prompt and owner API calls, user approvals and resumed `RunRequirement` updates.
- Adjacent first-party surfaces excluded from ownership: Post-run `evals/` evaluation and metrics, ordinary supervisor run audits and usage traces, CI tests, deployment configuration and upstream project governance.
- First-party operating / deployment modes considered: Single Agent API with paused tool approvals; coordinate and supervisor Team APIs with Agno model-led dispatch and workers; container job queue and optional OOM recovery; authenticated user changing agent/team data or prompts.
- Recursion level: One HiveGate service/owner runtime with several user/tenant sessions and team worker-agent sub-units. Unrelated tenants are not presumed mutually coordinating S1 units; Agno team and model internals are not silently assigned ownership to HiveGate policy.
- Reviewed revision: `96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0` (`main` frozen default-branch source).
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

HiveGate constructs Agno `Agent` model/tool sessions from stored agent configs and versioned prompt templates; FastAPI chat/commit endpoints execute them, store sessions and resume paused tool executions through confirmed/denied/edited `RunRequirement` objects. Team endpoints assemble configured member agents and an Agno `Team(mode=coordinate)`. A separately selected `supervisor` team route constructs a model-backed team leader with worker tools (Claude Code / managed agent), then runs the resulting external Agno Team object. Job producer/consumer adapt remote workers, persist state and allow optional human approval and OOM retry/replan/circuit-breaker. `supervisor/audit.py` persists normal supervisor run status; the evaluation suite scores after runs, not as an independent complementary feedback channel. Prompt CRUD and API key authorization configure future sessions but no established identity/ultimate-policy governance function should be inferred merely from editable prompts.

Sources: [agent.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/agents/agent.py), [agents.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/agents.py), [teams.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/teams.py), [team_builder.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/team_builder.py), [consumer.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/queue/consumer.py), [recovery.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/recovery.py), [hitl.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/agents/hitl.py), [audit.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/audit.py), [prompts.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/prompts.py).

## S1 — Operations
- State: A
- Function: Perform user-directed model-backed agent tasks and team worker work with tools and resumable sessions.
- Disturbance / variety regulated: Different user messages, model outputs, OAuth tool results, remote execution outcomes and requests to approve/deny pending tool actions.
- Decisive decision or feedback right: Configured Agno Agent, supervisor leader and worker agents choose user-response content and eligible tool actions; the user may approve particular effects but does not author each model step.
- Decision owner: Model-backed Agno agents hosted through the shipped first-party get_agent and Team/Worker modes, with dependency-owned Agno turn loop.
- Supporting / enforcement mechanisms: Agno Agent, Team, first-party API endpoints, tenant-prompt loading, MCP/toolkits, session persistence, approved run continuation and remote worker adapters.
- Closure path: Agent/tool result returns to the model or user; a paused tool call resumes with the human's approved/edited/refused requirement, changing the subsequent tool execution.
- Boundary reachability: No remote model call or full HiveGate pytest suite was executed as part of this Index source review.
- Why this is / is not agent-owned: `get_agent` returns configured model/tool agent; `api/routes/v2/agents.py` invokes it; team and supervisor routes build and execute Agno model-backed teams; HITL tests cover actual Agno pause/confirmed/rejected resume.
- Evidence: The supported distribution creates model-conditioned first-party exposed agents; Agno and configured provider models are required external execution dependencies, not invented first-party S3 governance.
- Basis: [agent.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/agents/agent.py), [agents.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/agents.py), [teams.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/teams.py), [team_builder.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/team_builder.py), [hitl.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/agents/hitl.py), [test_hitl.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/tests/test_hitl.py)
- Confidence: explicit first-party source, Agno integration tests
- Caveats: high for supported agent mode


## S2 — Coordination
- State: —
- Function: No first-party attenuator of a concrete conflict or oscillation among distinct operational agent units was established in the reviewed HiveGate team path.
- Disturbance / variety regulated: Multiple team workers can be routed sequentially and share task messages, but an observed cross-worker interference requiring reconciliation is not identified by this code.
- Decisive decision or feedback right: A specific competing action/commitment conflict would need an arbitration/attenuation decision returned to the relevant workers.
- Decision owner: No S2 owner established; Agno coordinate-mode handoff, configured roles and order are not by themselves a specialized coordination function.
- Supporting / enforcement mechanisms: Team(mode=coordinate), leader classification, worker execution dispatch, queue claim, transaction status and API role/order settings.
- Closure path: Team progress and worker results return through Agno Team and job status; there is no evidenced first-party inter-worker conflict determination/resolution loop.
- Why this is / is not agent-owned: Neither a team label, a routing model nor a queue claim proves S2 inter-S1 disturbance regulation.
- Evidence: [teams.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/teams.py), [team_builder.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/team_builder.py), [consumer.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/queue/consumer.py), [producer.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/queue/producer.py), [test_supervisor_team.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/tests/v2/test_supervisor_team.py)
- Basis: bounded negative source adjudication
- Confidence: medium
- Caveats: External Agno internals may implement additional coordination features; this repository-relative review does not import them as first-party HiveGate mechanisms.

### Absence scope
- Surfaces inspected: Source-shipped Team and supervisor builder, V2 team route and tests, remote job producer/consumer, queue CRUD and approval state.
- Plausible first-party paths checked: Conflicting shared-resource writes, duplicate agent commitments, out-of-order work invalidation, arbitration or damping of inter-agent oscillation with feedback into subsequent actions.
- Why no material first-party path remains: Inspected shipped relation coordinates routing and execution handoffs but contains no concrete first-party interference witness with its own attenuator and closed return path.


## S3 — Inside-and-now control
- State: ?
- Function: A model-backed Agno team leader plus deterministic worker queue/recovery may perform whole-current supervisory regulation, but the decisive whole-system decision and closure cannot be reconstructed from this first-party boundary.
- Disturbance / variety regulated: Multiple workers may fail or exhaust resources and cause conflicting current team commitments or job priorities.
- Decisive decision or feedback right: A qualifying supervisor would need whole-current team/worker commitments and a discretionary choice to reallocate, repair, stop or escalate them, with results applied to subsequent workers.
- Decision owner: Plausible Agno model-backed Team leader in configured supervisor mode; queue consumer and recovery helpers are deterministic. The authority over a shared-current whole-system decision is not sufficiently established by first-party source or mocked tests.
- Supporting / enforcement mechanisms: `build_supervisor_team` creates a model-backed Agno Team with Claude Code/managed worker tools; job queue handles remote execution; retry policy escalates OOM and circuit breaker; test route mocks team runs.
- Closure path: Leader classification/route to worker is exercised by mocked tests; OOM helper retries or flags replan, but the full leader observation→whole-current intervention→returned worker-state path has not been source-demonstrated.
- Why this is / is not agent-owned: The leader name and TeamMode.coordinate are insufficient for agent-owned S3, while deterministic retry alone is insufficient for S3=C. The concrete Agno team leader path prevents a confident bounded absence and therefore remains ?.
- Evidence: [team_builder.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/team_builder.py), [teams.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/teams.py), [test_supervisor_team.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/tests/v2/test_supervisor_team.py), [recovery.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/recovery.py), [consumer.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/queue/consumer.py), [models.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/models.py)
- Basis: source-verified plausible function, undecided decisive owner/closure
- Confidence: medium-low
- Caveats: Specific first-party test mocks build_supervisor_team instead of showing actual whole-team current control. Requires targeted first-party runtime trace of current team state, chosen supervisory action and its effect on subsequent workers.
- Whole-system current-view candidate: The Agno Team supervisor knows its configured worker roster and receives at least the current team run's task/result context; whether it reads all concurrent worker commitments and resource status was not demonstrated.
- Current-control decision-scope candidate: Select/redirect workers, replan after failure and intervene on live job commitments; first-party source supports routing and recovery but not the entire regulatory closure.

## S3* — Complementary audit
- State: —
- Function: No independent complementary operational auditor with separately obtained evidence and corrective feedback was evidenced.
- Disturbance / variety regulated: Persisted agent/supervisor results and usage logs can repeat the producer's own mistaken completion claims.
- Decisive decision or feedback right: A separate sufficiently independent audit actor would need inspect actual operational evidence, make a judgment and feed a challenge back into current supervision.
- Decision owner: No first-party independent complementary audit owner identified. Supervisor 'audit' module records normal self-reported execution state, and offline evals score results outside the live loop.
- Supporting / enforcement mechanisms: SupervisorRunDB trace, usage meter, observability/tracing, evaluation scripts and routine tests.
- Closure path: Audit records and evaluation scores do not flow as independent corrective decisions to a current agent team supervisor; no complementary runtime probe/return loop found.
- Why this is / is not agent-owned: The word audit, metrics, optional external observability and benchmark score are not S3* ownership.
- Evidence: [audit.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/supervisor/audit.py), [evaluator.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/evals/evaluator.py), [test_supervisor_team.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/tests/v2/test_supervisor_team.py), [agents.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/agents.py)
- Basis: bounded negative from first-party runtime and post-run surfaces
- Confidence: medium-high
- Caveats: A third-party monitoring stack might be independently configured, but its governance closure is not part of HiveGate's reviewed standard distribution.

### Absence scope
- Surfaces inspected: Supervisor/audit.py, observability providers, metrics/usage recording, evals/evaluator.py, team/worker routes and tests.
- Plausible first-party paths checked: Independent source of operational truth, third-party challenge role, live complementary spot-check and corrective feedback into team control.
- Why no material first-party path remains: Reviewed sources store producer/queue outcomes, performance counters and separate offline evaluations without a first-party independently adjudicated corrective audit loop.


## S4 — Outside-and-then intelligence
- State: —
- Function: No first-party environment sensing and prospective organizational adaptation choice was established in the supported runtime.
- Disturbance / variety regulated: Future changes in vendors, customer usage or tool availability could require redesigning the agent team's structure or capabilities.
- Decisive decision or feedback right: A qualifying mechanism would produce external-and-then options and decide/apply a prospective change to current capability.
- Decision owner: No first-party S4 adaptation decision owner; operators directly create/configure agents, teams, prompts and plugins.
- Supporting / enforcement mechanisms: Prompt CRUD/versioning, toolkit registry, agent/team API, pack loader and deployment settings.
- Closure path: User/admin configuration changes affect later agent construction but are not selected by an evidenced future-oriented environmental intelligence loop.
- Why this is / is not agent-owned: Mutable agents, versioned prompts and model-choice APIs are available to a human constructor, but no evaluated future option/return path has been shown.
- Evidence: [prompts.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/prompts.py), [service.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/prompts/service.py), [v2_selector.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/agents/v2_selector.py), [teams.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/teams.py), [agent.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/agents/agent.py)
- Basis: bounded negative first-party inspection
- Confidence: medium
- Caveats: Runtime model-tier alias resolution and conventional config updates respond to current model availability; neither alone closes S4.

### Absence scope
- Surfaces inspected: Agent/team/prompt CRUD, model resolver, supervised worker setup, prompt selection, versioning and post-run evals.
- Plausible first-party paths checked: Environmental horizon scan, prospective option comparison/decision and implementation into future organization capability.
- Why no material first-party path remains: All cited first-party configuration paths are direct calls or live execution support, not self/parent-owned outside-and-then adaptation governance.


## S5 — Policy and identity
- State: —
- Function: No established ultimate-policy or organizational identity arbitration and returned binding decision was found at the operating HiveGate service boundary.
- Disturbance / variety regulated: Operator edits to prompts or permissions could affect agent behavior, but CRUD/API authentication and per-tool approval are not themselves supreme-policy closure.
- Decisive decision or feedback right: A legitimate first-party identity-policy owner would need decide ultimate organizational mandate/continuity and return that decision as governing runtime policy.
- Decision owner: No specific S5 decision authority evidenced in the standard distribution; authenticated administrator/users edit runtime data and grant or refuse individual tool approvals.
- Supporting / enforcement mechanisms: API key scopes, prompt storage and version counters, user approvals, agent/team settings and static auth flags.
- Closure path: An authenticated CRUD update loads into subsequent sessions, and approved/denied tool calls resume; neither is a decision about the overall organizational charter with an explicit ultimate-authority loop.
- Why this is / is not agent-owned: A prompt can be edited and versioned and a dangerous tool gated without establishing a VSM S5 function. No autonomous or eligible parent-governed S5 mode is asserted.
- Evidence: [auth.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/services/auth.py), [prompts.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/prompts.py), [service.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/prompts/service.py), [v2_selector.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/agents/v2_selector.py), [hitl.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/agents/hitl.py), [approvals.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/api/routes/v2/approvals.py), [test_hitl.py](https://github.com/hivegate-ai/hivegate/blob/96b918ba7834a2aaa914fbe3f0e1b40d4e6497f0/tests/test_hitl.py)
- Basis: bounded negative first-party source inspection
- Confidence: medium
- Caveats: A hosting company may govern system identity externally; API admin secrets cannot be equated with a first-party S5 policy loop.

### Absence scope
- Surfaces inspected: Prompt versioning/CRUD, API key RBAC, Agent/Team configuration, user tool-approval state machine and host settings.
- Plausible first-party paths checked: Ultimate identity/missions decisions, a dedicated constitutional policy authority and returned organizational-level identity/continuity enforcement.
- Why no material first-party path remains: Observed interactions are ordinary configuration, user authorization and per-action approval; a distinct supreme-policy decision cycle is not evidenced by the shipped runtime.


## Recursion

Individual tenant agents and nested supervisor-team workers are operational units, but HTTP tenants and configured Agno subagents are not automatically independent viable systems. The declared system is the first-party HiveGate runtime; its API's administrative owner and the users' tool approvals remain separate from agent-owned decisions.

## Variety and escalation

User requests, provider/tool failures and remote job outcomes create work variety. Shipped job/recovery machinery handles configured retries/OOM circuit breakers; risky tool calls may pause and return for human confirmation or denial. Whether the Agno model-backed team head closes a whole-current S3 control function remains a concrete unresolved shipped-mode question. Audit logs and evaluations are not used to infer independence.

## Evidence gaps

- The S3 `?` is a particular supported first-party mode: model-backed supervisor Team built and executed through Agno, but whole-current decision authority, workforce reassignment and return to live worker commitments are not evidenced end to end. Do not silently turn the route's name into S3=A.
- No live Agno/model/container execution, full upstream pytest suite or independent semantic-review runtime was performed; tests were read as pinned source evidence only.
- S2/S3*/S4/S5 `—` are bounded to reviewed first-party paths and not universal impossibility claims. Readme feature descriptions and external Agno source are not credited as independent HiveGate ownership without in-boundary evidence.
- HITL real Agno tests support per-tool approval's return to operation, not parent-governed organizational S5; source-pinned correction remains possible if a qualifying ultimate-policy mode is later demonstrated.
