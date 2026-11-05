---
harness_id: proagent-os
project_name: ProAgent OS
repository: https://github.com/jahonn/ProAgent-OS
review_ref: 543433e933e115a825d77a553067c1d22d9cec45
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ProAgent OS

## Review boundary

- System in focus: ProAgent OS self-hosted task/recommendation service at one tenant-product recursion.
- Purpose and identity: Execute business/support/ops research tasks with tool-using specialists and operator-gated recommendations.
- Relevant environment: Tenant requests, knowledge sources, configured model endpoints, tool/network targets and tenant operators.
- Standard-distribution boundary: FastAPI app plus optional proactive worker and shipped vertical/agent/skill definitions.
- Credited operating / distribution surfaces: proagent_os runtime, actual tools, tenant stores, task/recommendation APIs, worker and shipped vertical configuration.
- Adjacent first-party surfaces excluded from ownership: tests, golden-task/optional judge evaluation, recording/demo scripts, CI/release and contributor development; these do not supply product audit ownership.
- First-party operating / deployment modes considered: Configured live OpenAI-compatible model mode; deterministic mock demo, optional replan/compaction, task pause/resume and off/noop/webhook recommendation executors.
- Recursion level: Tenant service with task execution cells; provider/deployment organization outside.
- Reviewed revision: `543433e933e115a825d77a553067c1d22d9cec45`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

FastAPI services compose a YAML agent registry, filesystem skill loader, tool registry and a provider-neutral orchestrator over SQLite. The outer planner→specialists→aggregator path includes native specialist tool rounds and an optional bounded task replan ring. HITL stores exact gated arguments/checkpoints and receipts for resumed observations, with documented limits on overlapping continues. A separate scheduled monitor path creates recommendations for human approval and off/noop/configured-webhook execution. Outcome feedback stores metrics, memory and weight nudges; it is not a trained policy. [`proagent_os/harness/orchestrator.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/harness/orchestrator.py); [`proagent_os/services.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/services.py); [`proagent_os/llm/openai_compat.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/llm/openai_compat.py); [`docs/ARCHITECTURE.md`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/docs/ARCHITECTURE.md)

## Operational model

Operational task cells use planners/specialists as stages of their own transformation; naming them agents does not establish separate VSM metasystem units. Proactive monitors are product operations. Tenant operators own individual consequential-action approvals. No separately evidenced parent S3/S4/S5 mode is inferred from that consent.

## S1 — Operations

- State: A
- Function: Produce task outcomes through model-authored plans, specialist tool decisions and aggregation.
- Disturbance / variety regulated: Different tenant tasks, knowledge queries, tool errors, multi-round observations and interrupted approvals.
- Decisive decision or feedback right: Planner chooses concrete steps; specialist selects tool arguments and subsequent turns; aggregator returns the result from observations.
- Decision owner: Configured model-driven planner/specialist composition; operator retains individual gated-action consent.
- Supporting / enforcement mechanisms: SQLite task/conversation state, registry/tool schema validation, bounded rounds, checkpoint and execute receipts, tenant scoping and HTTP/SSE console.
- Closure path: run_task persists model plan, runs each specialist model→tool→observation loop, optionally replans from results, aggregates and stores the final result/history. Approved gated observations are injected back into the interrupted specialist.
- Boundary reachability: services builds the actual Orchestrator/LLM/tool composition used by task APIs. OpenAI-compatible mode is shipped; autonomous action selection is not inferred from the mock demo.
- Why this is / is not agent-owned: Without model decisions the runtime can store/check/approve calls but cannot choose a live task plan and tool sequence. Human gating constrains particular effects, rather than authoring every ordinary operational step.
- Evidence: [`proagent_os/harness/orchestrator.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/harness/orchestrator.py); [`proagent_os/services.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/services.py); [`proagent_os/llm/openai_compat.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/llm/openai_compat.py); [`docs/ARCHITECTURE.md`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/docs/ARCHITECTURE.md); [`proagent_os/harness/hitl.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/harness/hitl.py); [`proagent_os/professional/tools/base.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/professional/tools/base.py)
- Basis: structural
- Confidence: high
- Caveats: Mock mode is deterministic, executor off/noop is not real-world effect, and provider quality was not measured.

## S2 — Coordination

- State: —
- Function: Planner-to-specialist sequencing and result aggregation decompose one task. Neither distinct task cells nor tenant isolation have an evidenced specific inter-S1 oscillation/conflict plus a coordination response/return path.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Serial plan execution, prior-context sharing, tenant isolation, task HITL receipts and replan ring. Receipts suppress a repeated gated call; they do not coordinate discretion between distinct S1 units.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`proagent_os/harness/orchestrator.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/harness/orchestrator.py); [`proagent_os/services.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/services.py); [`proagent_os/llm/openai_compat.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/llm/openai_compat.py); [`docs/ARCHITECTURE.md`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/docs/ARCHITECTURE.md); [`proagent_os/harness/hitl.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/harness/hitl.py); [`docs/AUTH.md`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/docs/AUTH.md)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Full runtime/API/worker tree, shipped vertical/agent/skill definitions, README, architecture/auth/DB/eval/tool docs and relevant tests.
- Plausible first-party paths checked: Serial plan execution, prior-context sharing, tenant isolation, task HITL receipts and replan ring. Receipts suppress a repeated gated call; they do not coordinate discretion between distinct S1 units.
- Why no material first-party path remains: Planner-to-specialist sequencing and result aggregation decompose one task. Neither distinct task cells nor tenant isolation have an evidenced specific inter-S1 oscillation/conflict plus a coordination response/return path.

## S3 — Inside-and-now control

- State: —
- Function: Dashboard counts, rate limits and operator task consent do not establish a whole-product current-control relationship over shared commitments/resources. No shipped agent or operator loop couples that view to whole-system bargaining, priority or constraint decisions.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Tenant dashboard/tasks/usage views; per-task pause/resume/reject; recommendation approval; static rate limits and bounded tool/replan configuration. The task owner can intervene locally, but no broader current-control decision path is supplied.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`proagent_os/api/dashboard.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/api/dashboard.py); [`proagent_os/api/tasks.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/api/tasks.py); [`proagent_os/ratelimit.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/ratelimit.py); [`proagent_os/proactive/recommendations.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/proactive/recommendations.py)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Full runtime/API/worker tree, shipped vertical/agent/skill definitions, README, architecture/auth/DB/eval/tool docs and relevant tests.
- Plausible first-party paths checked: Tenant dashboard/tasks/usage views; per-task pause/resume/reject; recommendation approval; static rate limits and bounded tool/replan configuration. The task owner can intervene locally, but no broader current-control decision path is supplied.
- Why no material first-party path remains: Dashboard counts, rate limits and operator task consent do not establish a whole-product current-control relationship over shared commitments/resources. No shipped agent or operator loop couples that view to whole-system bargaining, priority or constraint decisions.

## S3* — Complementary audit

- State: —
- Function: Golden trajectory scoring and optional LLM judge are developer-invoked evaluation of test cases, outside the running product boundary. Product logs/receipts and schema checks provide ordinary evidence, without a sufficiently independent complementary audit judgment returning into current regulation.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: eval/golden.py and judge.py, developer fixture invocation, trace summaries, recommendation audit rows and HITL receipt summaries; no product audit trigger or finding-to-control integration.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`proagent_os/eval/golden.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/eval/golden.py); [`proagent_os/eval/judge.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/eval/judge.py); [`docs/EVAL.md`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/docs/EVAL.md); [`proagent_os/harness/loop.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/harness/loop.py); [`proagent_os/proactive/recommendations.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/proactive/recommendations.py)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Full runtime/API/worker tree, shipped vertical/agent/skill definitions, README, architecture/auth/DB/eval/tool docs and relevant tests.
- Plausible first-party paths checked: eval/golden.py and judge.py, developer fixture invocation, trace summaries, recommendation audit rows and HITL receipt summaries; no product audit trigger or finding-to-control integration.
- Why no material first-party path remains: Golden trajectory scoring and optional LLM judge are developer-invoked evaluation of test cases, outside the running product boundary. Product logs/receipts and schema checks provide ordinary evidence, without a sufficiently independent complementary audit judgment returning into current regulation.

## S4 — Outside-and-then intelligence

- State: —
- Function: The shipped monitors react to KB count/search or configured current metric values; outcome feedback appends memory and nudges stored weights. These paths do not develop externally prospective adaptation options with returned changes to present capability. Specialist prompts take the first five loaded skills, not an evidenced environment-driven adaptation decision.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: kb_change/metric_stub/data_source monitors; ingest_more recommendation, noop/configured-webhook execution; outcome-feedback memory/skill-weight nudge; compaction and task replanning. Generic webhook programmability is not an instantiated adaptation loop.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`proagent_os/proactive/monitors.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/proactive/monitors.py); [`proagent_os/proactive/executors.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/proactive/executors.py); [`proagent_os/profitable/learning.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/profitable/learning.py); [`proagent_os/professional/skills/loader.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/professional/skills/loader.py); [`proagent_os/harness/orchestrator.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/harness/orchestrator.py)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Full runtime/API/worker tree, shipped vertical/agent/skill definitions, README, architecture/auth/DB/eval/tool docs and relevant tests.
- Plausible first-party paths checked: kb_change/metric_stub/data_source monitors; ingest_more recommendation, noop/configured-webhook execution; outcome-feedback memory/skill-weight nudge; compaction and task replanning. Generic webhook programmability is not an instantiated adaptation loop.
- Why no material first-party path remains: The shipped monitors react to KB count/search or configured current metric values; outcome feedback appends memory and nudges stored weights. These paths do not develop externally prospective adaptation options with returned changes to present capability. Specialist prompts take the first five loaded skills, not an evidenced environment-driven adaptation decision.

## S5 — Policy and identity

- State: —
- Function: Brand goals/tone, RBAC and tool approval constrain tasks but supply no identity or ultimate-policy matter→legitimate authority→decision-return closure at this recursion. Neither tenant key administration nor ordinary action approval establishes S5.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Brand/tenant configuration, authentication/RBAC, recommendation decision routes and task approval snapshots; developer registry and skill editing are outside runtime identity deliberation.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`proagent_os/professional/brand/store.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/professional/brand/store.py); [`proagent_os/api/tenants.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/api/tenants.py); [`proagent_os/rbac.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/rbac.py); [`proagent_os/harness/hitl.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/harness/hitl.py); [`proagent_os/proactive/recommendations.py`](https://github.com/jahonn/ProAgent-OS/blob/543433e933e115a825d77a553067c1d22d9cec45/proagent_os/proactive/recommendations.py)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Full runtime/API/worker tree, shipped vertical/agent/skill definitions, README, architecture/auth/DB/eval/tool docs and relevant tests.
- Plausible first-party paths checked: Brand/tenant configuration, authentication/RBAC, recommendation decision routes and task approval snapshots; developer registry and skill editing are outside runtime identity deliberation.
- Why no material first-party path remains: Brand goals/tone, RBAC and tool approval constrain tasks but supply no identity or ultimate-policy matter→legitimate authority→decision-return closure at this recursion. Neither tenant key administration nor ordinary action approval establishes S5.

## Recursion

Task stages, tenants and vertical packs do not demonstrate independently viable recursive subsystems.

## Variety and escalation

Model/tool decisions absorb local task variety; tool schemas, tenant scopes, bounded rounds, compaction and durable approvals constrain it. A pending approval reaches an operator and can resume/cancel that task; it is not an identity-level escalation.

## Evidence gaps

Static source assessment includes live-provider wiring but no live provider/webhook calls. Attempted selected offline pytest witnesses could not start because pytest is absent in the runtime; no upstream test pass is claimed. Source tests/docs corroborate behavior, while Index/Skills validation is performed separately.
