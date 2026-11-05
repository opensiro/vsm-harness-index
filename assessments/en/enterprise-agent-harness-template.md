---
harness_id: enterprise-agent-harness-template
project_name: Enterprise Agent Harness Template
repository: https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template
review_ref: 02d40b3cd712af07d5e5ccab12edee9980b988fe
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Enterprise Agent Harness Template

## Review boundary

- System in focus: The runnable Python `Harness` with shipped agent YAML roster and the `supervisor → research/coding/review` child-run delegation configuration; not a deployed enterprise platform beyond this template.
- Purpose and identity: Configurable agent harness with provider-neutral model loop, guarded tools/sandbox, checkpoint/recovery, API/CLI/MCP, evaluation scripts and model-driven multi-agent task supervision.
- Relevant environment: User tasks and specialist subtask returns, workspace/code/database/web state, provider responses/errors, tool approvals, tenant/session state, cost/step/time budgets and configured policy constraints.
- Standard-distribution boundary: `src/harness/{runtime,core,orchestration,safety,state,tools,llm,memory,evals,api}`, `agents/*.yaml`, `src/harness/prompts/templates/supervisor/v1.md`, `policies/default.yaml`, packaged demo/testing entry paths. Deployed credentials/infrastructure and independent third-party audits are excluded.
- Credited operating / distribution surfaces: [architecture](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/docs/architecture.md), [composition root](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/runtime.py), [core loop](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/core/loop.py), [delegation](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/orchestration/delegation.py), [supervisor roster](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/agents/supervisor.yaml), [supervisor prompt](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/prompts/templates/supervisor/v1.md), [integration test](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/tests/integration/test_orchestration.py).
- Adjacent first-party surfaces excluded from ownership: Offline test/evaluation suite, synthetic `FakeLLM` integration fixtures, static YAML policies, tamper-evident audit log, human tool-approval service and external deployment/CI. These are read for boundary/negative screening but are not automatically independent audit, strategy or ultimate-policy authorities.
- First-party modes inspected: Native model/tool loop with registered specialist agents and `delegate` tool, supervisor parallel child runs, cost rollup, child pause/failure return and re-delegation prompts; optional Agno engine, API/CLI/MCP use, fake-model offline tests, safety approvals, audit log and eval regression scoring.
- Recursion level: One bounded supervisor-led task organization with three distinct autonomous specialist S1 agents as lower units; not the owner's entire enterprise, the benchmark corpus or all tenants on a server.
- Reviewed revision: `ashishpatel26/Enterprise-Agent-Harness-Project-Template@02d40b3cd712af07d5e5ccab12edee9980b988fe` (first-party MIT source).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`Harness.build` loads agent specs, validates the supervisor's sub-agent roster and delegation tool, installs `install_delegation`, and creates child `AgentLoop` instances on demand. Each specialist has its own prompt, model, tools, limits and isolated messages. The supervisor is itself an agent whose model can emit multiple parallel `delegate` tool calls; each starts or resumes a deterministic child run, returns a specialist answer or explicit failure/approval-pause observation, and rolls child cost/usage into the parent. The shipped supervisor prompt instructs it to plan work, choose specialists, review outputs, re-delegate inadequate results and combine completion. Core loops emit state, audit/metrics and checkpointed tool outcomes; separate evaluation scripts can test baseline regressions but are not wired as an independent real-time corrective authority over deployed runs. [runtime](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/runtime.py), [delegation](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/orchestration/delegation.py), [loop](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/core/loop.py), [test](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/tests/integration/test_orchestration.py).

## Operational model

Specialist models own task-operating S1 choices and can use different tools, while the supervisor's configured model holds a narrower but real whole-task **current** allocation/monitoring right: decide which specialist gets which subtask, consider returned answers/failures, reassign and merge outcomes under the parent task budget. This is a bounded S3 at the supervisor-led task recursion. Technical lease/idempotency/rate-limit/approval hooks enforce rather than originate that management. The distinct `review` model sees supervisor-supplied material but has no independent external truth access, and the eval runner is a separate offline test workflow; neither establishes operational S3* closure.

## S1 — Operations

- State: A
- Function: Distinct research, coding and review specialists perform model-selected work for their assigned subtasks; supervisor itself uses a model-directed delegation loop.
- Disturbance / variety regulated: Research/document changes, coding outcomes, partial/incorrect drafts, tool responses, task-specific failures and approval delays.
- Decisive decision or feedback right: Each specialist model chooses its action or answer from a fresh subtask prompt and any available permitted tools; the supervisor model chooses `delegate` tool calls and final composition.
- Decision owner: Configured specialist agent model at each child-run S1 boundary, implemented via the runnable `AgentLoop`/tool pipeline.
- Supporting / enforcement mechanisms: Per-agent YAML model/tool/limits, isolated child contexts, standard tool execution/guards, checkpoints, retries/recovery and explicit `RunState` outcomes.
- Closure path: Parent task → model-chosen delegate call → distinct child model/tool/observation loop → child result/error → parent feedback/next decision.
- Boundary reachability: First-party `Harness.build` installs delegation and validates shipped supervisor YAML's specialist names; `delegate` calls `create_run`/`execute`, not merely an example external orchestrator. Integration tests exercise parallel independent children with fake LLMs; configured production inference endpoints were not exercised here.
- Why this is / is not agent-owned: Child models own discretionary task steps; the host executes checks and records state. The supervisor's choice of subtask does not erase independent specialist S1 agency.
- Evidence: [loop](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/core/loop.py), [runtime wiring](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/runtime.py), [child registry](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/orchestration/delegation.py), [integration fixture](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/tests/integration/test_orchestration.py).
- Basis: Installed separate autonomous child-run model/tool feedback, with source and test-case corroboration.
- Confidence: High for source-distribution reachability; runtime paid-model outcome not independently verified.
- Caveats: Child availability and model quality depend on operator configuration; test assertions with FakeLLM prove paths rather than live autonomy quality.

## S2 — Coordination

- State: —
- Function: A specific installed attenuating channel for **inter-S1 operational conflict** is not demonstrated, despite real sub-agent delegation.
- Disturbance / variety regulated: Overlapping specialist tasks, incompatible answers or resource contention could arise, but the source does not encode detection/settlement of reciprocal S1 clashes.
- Decisive decision or feedback right: Supervisor can assign and repeat work, and static registry validates allowed children; no evidence of separate horizontal S1-to-S1 disturbance arbitration or an S2-specific feedback relation.
- Decision owner: Supervisor model as current task manager; deterministic roster/permission validation handles routing, not inter-unit conflict mediation.
- Supporting / enforcement mechanisms: `sub_agents` allowlist, parallel `delegate` calls, child IDs and shared tenant/tools with separate contexts.
- Closure path: Parent delegation → child replies → supervisor current control; no distinct conflict signal between S1 children → attenuating settlement → reciprocal changed operation.
- Why this is / is not agent-owned: Delegation, tool routing, serial/parallel sequencing and shared budget accounting alone do not establish the VSM S2 function.
- Evidence: [delegation](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/orchestration/delegation.py), [supervisor](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/agents/supervisor.yaml), [integration tests](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/tests/integration/test_orchestration.py).
- Basis: Bounded absence review against the strongest multi-agent candidate.
- Confidence: Medium-high; positive S3 supervision is not automatically positive S2 conflict attenuation.
- Caveats: A future operator policy could require or build explicit inter-specialist conflict arbitration, but no independent pathway is currently closed in the shipped model.

### Absence scope

- Surfaces inspected: Supervisor prompt/YAML, delegate implementation, core tool batching, specialist definitions and orchestration tests.
- Plausible first-party paths checked: Parallel delegation as S2, review feedback as an S1 conflict adjudicator, deterministic child reuse as conflict avoidance, shared run budget as horizontal coordination.
- Why no material first-party path remains: These do not specify an attenuating inter-S1 disturbance relation with a stable decision/feedback channel separate from ordinary supervisor task assignment and outcome review.

## S3 — Inside-and-now control

- State: A
- Function: A live supervisor controls the present specialist-work portfolio for one parent task by selecting subagents, reviewing outcomes and adjusting assignments under a shared task budget.
- Disturbance / variety regulated: Diverse subtasks, inadequate specialist output, failed/paused child runs, concurrent execution and aggregate token/cost limits.
- Decisive decision or feedback right: Model-driven supervisor chooses which allowed specialist gets each subtask (possibly in parallel), sees child answers/errors/pause status, can delegate corrective work, decides when to synthesize the overall answer.
- Decision owner: Configured `supervisor` model; installed `delegate` tool and harness enforce its chosen child-run requests and report results. The static budget cap is not itself the S3 decision owner.
- Supporting / enforcement mechanisms: `supervisor.yaml` and `supervisor@v1` instructions, child roster, depth ceiling, deterministic child IDs for crash recovery, rolled-up child usage/cost, isolated subtask execution and returned status/answer observations.
- Closure path: Supervisor task view → delegate choices → child S1 task execution → successful/error/awaiting-approval tool outcome → supervisor's next model turn and re-delegation/answer choice, with aggregate cost/usage enforced by parent loop.
- Whole-system current view: At the declared parent-task recursion, the supervisor sees its approved specialist roster and actual result/error messages from each dispatched child; shared parent budget counts child usage. It does **not** see all users/tenants or manage an enterprise fleet.
- Current-control decision scope: Current assignment, follow-up/reassignment, review sequencing and acceptance/synthesis of the research/coding/review portfolio, not long-term system strategy or ultimate-policy rights.
- Boundary reachability: The first-party composition root installs the `delegate` registry, shipped supervisor config enumerates specialists, prompt explicitly directs re-delegation on bad results, and integration test runs independent children concurrently and returns results/cost to the parent. This is operational first-party S3 for the bounded task organization, not the mere class name `Supervisor`.
- Why this is / is not agent-owned: Model can choose or revise present portfolio assignments after actual child feedback. Deterministic guard/leases/idempotency alone would not qualify; positive mapping depends on the installed decision path plus child autonomy.
- Evidence: [supervisor instructions](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/prompts/templates/supervisor/v1.md), [shipped roster](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/agents/supervisor.yaml), [delegate return](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/orchestration/delegation.py), [tests](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/tests/integration/test_orchestration.py).
- Basis: Evidence-backed installed supervisory current-control closed loop across autonomous child work, sharply scoped to one task organization.
- Confidence: Medium-high (decision-path closure proven at source; live provider correctness and conflict handling not tested).
- Caveats: A supervisor may simply accept poor outputs; normative quality of its choices is untested and S3 is not S3* independent audit.

## S3* — Complementary audit

- State: —
- Function: No independent complementary reality-checking auditor verifies task claims via alternate evidence and closes findings into current management.
- Disturbance / variety regulated: Bad research claims or coding changes can be questioned by `review` specialist or offline eval regression tests, but their installed evidence paths do not make an independent live audit circuit.
- Decisive decision or feedback right: `review` agent has no first-party truth-access tools and receives only a supervisor-authored subtask prompt; audit log hashes observed events without verifying their truth. Eval runner is a separate test/CI workflow, not a returned S3 corrective channel for live work.
- Decision owner: Supervisor decides whether to request review and whether to act on it; review model lacks independent access to workspace/reality evidence, offline scorer/CI operator lives outside the task controller.
- Supporting / enforcement mechanisms: Optional `review` sub-agent, tamper-evident `AuditLog.verify`, policy safety guard, offline test expectations and regression baseline comparison.
- Closure path: Supervisor-provided material → review critique → supervisor continuation (an ordinary S1 report); or offline test → regression report. Neither creates independent complementary evidence → audit verdict → enforceable S3 correction through an accountable audit role.
- Why this is / is not agent-owned: Separate model identity alone does not imply independent observational access; hash-chain integrity only proves log continuity, and a CI pass is not an independent audit of actual deployment claims.
- Evidence: [review spec](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/agents/review.yaml), [audit log](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/safety/audit.py), [evals](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/evals/runner.py), [delegation](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/orchestration/delegation.py).
- Basis: Explicit separation of reviewer model, audit-log transport and offline eval against required S3* complementary-independence conditions.
- Confidence: Medium-high.
- Caveats: An operator could independently audit via external tools/records; the current `review` agent may use its learned knowledge but has no distinct first-party reality observation path in its YAML.

### Absence scope

- Surfaces inspected: Review agent's tool list, supervisor prompt, event/audit log, ApprovalService, eval suite/scorers and tool-result path.
- Plausible first-party paths checked: Review agent as S3*, SHA-chain verification as independent truth, human approvals as complementary audit, CI regression gate as live S3* feedback.
- Why no material first-party path remains: None simultaneously demonstrates independent operational evidence access, complementary judgment ownership and a returned authoritative correction to current S3 across the declared task organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: No distinct future-environment scanning/adaptation authority governs the whole task organization beyond current user work.
- Disturbance / variety regulated: New provider availability, changing task types, tool/schema policy, evolving skill capability and future usage forecasts.
- Decisive decision or feedback right: Human operator controls agent YAML/provider/plugin updates; specialist research serves current delegated question rather than strategic capability change.
- Decision owner: Developer/tenant for future architecture; supervisor for present delegation only.
- Supporting / enforcement mechanisms: Plugin extension points, config reload/deployment, memory stores, eval baselines and model/provider retries.
- Closure path: Tasks and current tool feedback → user answer or manual version update; no autonomous prospective environmental intelligence → option selection → S3 negotiation/adopted future capability.
- Why this is / is not agent-owned: A research sub-agent and memory embeddings may help present tasks, but do not install an organizational future-modeling/strategy actor.
- Evidence: [architecture](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/docs/architecture.md), [research spec](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/agents/research.yaml), [runtime](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/runtime.py).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: Tool-using agents can discuss the future within individual tasks; that is not a shipped S4 organizational feedback loop.

### Absence scope

- Surfaces inspected: Supervisor/research prompts, memory, provider fallback, eval runner and runtime extensions/config.
- Plausible first-party paths checked: Research agent as environmental scanner, model fallback as strategic adaptation, episodic memory as S4 learning, offline eval regression as future capability choice.
- Why no material first-party path remains: All paths service current tasks or operator development; no distinct prospective strategic choice returns to the task supervisor and changes future operating organization.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/policy deliberation or legitimate parent-governed identity-level mandate returns to the supervisor-led organization.
- Disturbance / variety regulated: Security permissions, sensitive data, tool use, tenant accountability and human approval requirements.
- Decisive decision or feedback right: Policy YAML and operator settings define guards; human reviewer approves/denies individual risky tool calls and may be prohibited from approving their own call. None evidences identity-level policy revision.
- Decision owner: External operator/security policy author for static mandates and approval reviewer for individual actions, not a packaged S5 ultimate governance role.
- Supporting / enforcement mechanisms: `SafetyGuard`, default policy, `ApprovalService`, four-eyes switch, audit log, data redaction and tenant API authentication.
- Closure path: Policy rule → tool pause → human yes/no → resumed or denied action. This is a closed **ordinary permission** loop, not identity/mission issue → ultimate authority → revised governance mandate to the organization.
- Why this is / is not agent-owned: Rigorous approvals and tamper-evident security logging enforce chosen policy, but do not confer first-party S5 or the Methodology's parent-mode `P` without a function-specific identity decision right.
- Evidence: [approvals](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/safety/approval.py), [guard](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/src/harness/safety/guard.py), [policy](https://github.com/ashishpatel26/Enterprise-Agent-Harness-Project-Template/blob/02d40b3cd712af07d5e5ccab12edee9980b988fe/policies/default.yaml).
- Basis: Bounded absence review distinguishing action authorization from organizational identity-policy closure.
- Confidence: High.
- Caveats: In a real enterprise, external human governance likely exists; it is not an encoded operational S5 mode within this shipped template.

### Absence scope

- Surfaces inspected: Policies, `ApprovalService` and user separation, guard/checks, authentication, audit log and supervisor prompts.
- Plausible first-party paths checked: Four-eyes tool approval as parent S5, policy YAML as charter, audit log as mission accountability, administrator API credentials as ultimate authority.
- Why no material first-party path remains: These are rule enforcement or one-action approvals, not an identity-level deliberation/mandate with returned policy change affecting subsequent organizational purpose and operation.

## Recursion

At the declared one-parent-task recursion, specialist agents are distinct autonomous S1 units and the model-driven supervisor provides bounded S3 current control. The children do not acquire their own VSM management systems just because recursion is technically allowed to depth three; the owner/tenant enterprise and future fleet operations are outside the assessed unit.

## Variety and escalation

Distinct specialist models and parallel delegation distribute task-solving variety. Allowed child roster, depth limit, child budget rollup, tool guard, checkpoints and approval pauses constrain risk; the supervisor receives child failure/approval observations and may redirect work. These are S3 current feedback and ordinary guardrails, not an additional S2 conflict-cancellation channel or exceptional identity-policy/algedonic governance path. Child approval pauses return a message to supervisor; explicit separate S5 deliberation is not evidenced.

## Evidence gaps

- `python -m pytest tests/integration/test_orchestration.py -q` was unavailable because this container does not install pytest; source and first-party integration test definitions corroborate installed routing, but no configured provider/sandbox/Redis live E2E was performed.
- Positive S3 is narrowly the supervisor model's present task-portfolio allocation and feedback, not a server-wide resource director or proof of effective conflict-resolution quality.
- Review specialist has no independent first-party tools; offline evals, audit logs and human approvals remain separate from the required independent S3* reality-check-and-correction path.
