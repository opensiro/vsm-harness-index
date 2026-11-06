---
harness_id: runloop
project_name: runloop
repository: https://github.com/murilo-bassan/durable-agent-runtime
review_ref: 1d68208d017d27d1b21805753b51a3872c888a52
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# runloop

## Review boundary

- System in focus: runloop durable procurement-agent service with multiple owner-scoped runs, not a generic external tool gateway.
- Purpose and identity: Execute long model/tool tasks with persisted recovery, approvals and bounded shared resource use.
- Relevant environment: Submitted procurement requests, model providers, supplier/order tools, Postgres, worker failures and action reviewers.
- Standard-distribution boundary: runtime package, API/console, worker process, concrete procurement AgentSpec and configured OpenAI-compatible provider mode.
- Credited operating / distribution surfaces: runtime model/tool execution, Postgres run/lease/budget/approval/effect paths, supported API/console and Python control primitives.
- Adjacent first-party surfaces excluded from ownership: Tests, screenshots, demos, SIGKILL chaos drill and development CI; other tool-gateway repositories and external authentication are outside.
- First-party operating / deployment modes considered: Deterministic ScriptedPlanner demo versus shipped OpenAI-compatible model mode; embedded or separate multi-slot workers; console/API reviewer and developer Python controls.
- Recursion level: One service with distinct procurement-run S1 cells sharing owner budgets; worker slots are execution carriers, not separate viable systems.
- Reviewed revision: `1d68208d017d27d1b21805753b51a3872c888a52`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

A Postgres run row is both queue entry and durable transcript. Workers atomically claim work, heartbeat it, checkpoint model/tool results and recover stale ownership. execute resumes unanswered tool calls and uses either a deterministic procurement planner or an OpenAI-compatible model. Write calls pause for exact-argument approval and run through an effect-key record; rejection/expiry returns as an observation. Shared owner tokens are reserved/settled/released. API/console expose live runs, usage, approvals and cancellation; prompts are versioned and pinned per run. [`runtime/agent_loop.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/agent_loop.py); [`runtime/llm.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/llm.py); [`runtime/service.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/service.py); [`runtime/worker.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/worker.py)

## Operational model

Separate procurement runs are the S1 cells; database rows/threads are support. Shared-budget coordination and owner-envelope current control are distinct constructor decisions, not agent-owned just because they are enforced automatically. Human order consent is local operational approval, without a demonstrated S3/S4/S5 parent function.

## S1 — Operations

- State: A
- Function: Select procurement actions and produce an evidence-based answer through persisted model/tool feedback.
- Disturbance / variety regulated: Different item/quantity/price requests, supplier quotes, tool errors, rejected/expired purchases and recovered steps.
- Decisive decision or feedback right: Choose the next tool/arguments or final answer using the current transcript and observations.
- Decision owner: Configured live model agent; an action reviewer retains exact write consent. ScriptedPlanner is a separate deterministic demonstration.
- Supporting / enforcement mechanisms: Worker claim/checkpoint/fencing, per-call token reservations, schema checks, approval hashes, effect-key replay and provider retries constrain/sustain operation.
- Closure path: execute calls the configured LLM, checkpoints its tool calls, executes approved/read tools, appends observations and asks again. Rejection/expiry returns a tool error; restarted workers resume from the stored transcript.
- Boundary reachability: Worker.from_settings selects the shipped LLM adapter; AgentSpec registers actual procurement tools and service.submit queues that concrete composition. Autonomous ownership is not inferred from deterministic demo results.
- Why this is / is not agent-owned: Without the live model the state machine still persists/gates steps, but cannot choose an open live action sequence; the optional scripted planner does not donate autonomous decision ownership.
- Evidence: [`runtime/agent_loop.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/agent_loop.py); [`runtime/llm.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/llm.py); [`runtime/service.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/service.py); [`runtime/worker.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/worker.py); [`runtime/agents.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/agents.py); [`runtime/tools/procurement.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/tools/procurement.py); [`runtime/approvals.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/approvals.py)
- Basis: structural
- Confidence: high
- Caveats: No live provider or real purchase performed; write-tool exactly-once guarantees depend on the shipped transaction/effect implementation.

## S2 — Coordination

- State: C
- Function: Attenuate a concrete shared-token overspend race among concurrent run S1 cells.
- Disturbance / variety regulated: Multiple runs see the same remaining owner budget and collectively commit more model tokens than the shared envelope permits.
- Decisive decision or feedback right: Reserve a share before a model step, settle actual usage or release it, and refuse an over-budget commitment. The autonomous coordination allocation/revision actor still requires composition.
- Decision owner: Budget/envelope and reservation policy are developer-selected; deterministic Postgres machinery applies them. No agent chooses shared-budget negotiation or revision.
- Supporting / enforcement mechanisms: Owner row lock and reserve/settle/release ledger serialize the shared-resource check/commit. Queue locks, idempotency and soft concurrency cap are distinct mechanisms.
- Closure path: Each first-party execute path reserves against all owner runs; refusal ends that run with budget_exceeded, while settlement/release changes the budget available to subsequent steps/runs.
- Boundary reachability: agent_loop directly invokes budget.reserve before every model call and settle/release afterwards; this is the concrete shipped multi-run composition, not hypothetical generic queue coordination.
- Why this is / is not agent-owned: Removing the model leaves the same fixed admission/envelope rules; a developer must compose any autonomous selection/revision of coordination allocation over the explicit primitive.
- Distinct S1 units: Separate goal-bearing procurement runs under one owner, each with its own transcript/outcome.
- Inter-S1 disturbance: Concurrent runs can oversubscribe one shared token pool; ADR0003 and concurrent-reservation tests describe the concrete race.
- Attenuating coordination relation: Atomic shared-owner reservation and subsequent settle/release.
- Feedback into subsequent S1 behaviour: A later model step is admitted or fails according to the changed shared ledger.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The primitive specifically controls concurrent claims on one scarce pool and returns admission feedback; queue existence alone is not credited.
- Evidence: [`runtime/budget.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/budget.py); [`runtime/agent_loop.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/agent_loop.py); [`docs/adr/0003-token-budget-reservations.md`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/docs/adr/0003-token-budget-reservations.md); [`tests/test_budget_prompts.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/tests/test_budget_prompts.py)
- Basis: structural
- Confidence: high for the function-specific construction; no A claim
- Caveats: The separate per-owner run-count cap is explicitly soft; this conclusion is not a claim of hard overall concurrency enforcement.

## S3 — Inside-and-now control

- State: C
- Function: Expose whole-service/owner current-use visibility and shared resource/commitment intervention.
- Disturbance / variety regulated: Current aggregate spend and live commitments can exceed an operator/developer selected envelope or require cancellation.
- Decisive decision or feedback right: Choose/revise owner daily budget/concurrency constraints or cancel selected current runs using shared run/usage information.
- Decision owner: Developer/host controller must compose the discretionary current-control actor, legitimate authority and policy over these specific surfaces. No autonomous controller or function-specific parent governance mode is established.
- Supporting / enforcement mechanisms: budget.set_budget/remaining, run metrics/list, request_cancel and checkpoint enforcement apply resource/intervention decisions; they do not own their organizational rationale.
- Closure path: A selected set_budget update changes the owner envelope used by later reservations/claims. Cancellation changes queued/waiting state immediately or returns through a running agent checkpoint. Console exposes runs/metrics/budget and cancel, but does not autonomously select the intervention.
- Boundary reachability: Python runtime exposes owner-budget mutation and service-wide metrics/current-run/cancel APIs; installed worker loops consume those settings/cancellation flags. This supplies a resource/current-control-specific construction rather than only a static configuration file.
- Why this is / is not agent-owned: The procurement agent has no budget setter, fleet-view policy choice or intervention tool over peer runs; fixed budget enforcement is not S3=A.
- Whole-system current view: Runs/aggregate metrics and shared owner token availability, exposed by runtime and the API/console.
- Current-control decision scope: Shared owner token/concurrency envelope and cancellation of current service commitments, distinct from choosing one supplier quote.
- Evidence: [`runtime/budget.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/budget.py); [`runtime/runs.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/runs.py); [`runtime/api.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/api.py); [`web/static/app.js`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/web/static/app.js); [`runtime/agent_loop.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/agent_loop.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Only the explicit constructor is credited. X-Owner is not authentication; external gateway/legitimate operator authority and a whole-system supervisory procedure are not supplied, so no P modifier.

## S3* — Complementary audit

- State: —
- Function: Persisted steps, approval history and side-effect receipts are ordinary execution evidence. Tests and the chaos drill are development validation; no complementary independently judged audit with returned current-control findings is supplied.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Step/metrics/approval readouts, ownership/fencing checks, schema validation, exact-argument consent, side-effect replay and test/chaos paths. Reviewers approve an action rather than audit an independent operational claim.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`runtime/api.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/api.py); [`runtime/approvals.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/approvals.py); [`runtime/tools/base.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/tools/base.py); [`scripts/chaos.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/scripts/chaos.py); [`tests/test_api_worker.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/tests/test_api_worker.py)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Complete runtime/API/console/schema tree, procurement composition, prompts/configuration, README/ADRs, scripts and source tests.
- Plausible first-party paths checked: Step/metrics/approval readouts, ownership/fencing checks, schema validation, exact-argument consent, side-effect replay and test/chaos paths. Reviewers approve an action rather than audit an independent operational claim.
- Why no material first-party path remains: Persisted steps, approval history and side-effect receipts are ordinary execution evidence. Tests and the chaos drill are development validation; no complementary independently judged audit with returned current-control findings is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: Quote comparison/rejection adaptation is present-task procurement behavior. Prompt publication/versioning changes configuration but has no external-and-prospective sensing/options/decision-return loop for the service capability.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Scripted/live next-quote behavior, supplier tools, prompt versions/activation, retries, recovery and budget limits; no capability-research/adoption workflow or parent adaptation procedure.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`runtime/llm.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/llm.py); [`runtime/prompts.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/prompts.py); [`runtime/agents.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/agents.py); [`runtime/api.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/api.py); [`runtime/service.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/service.py)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Complete runtime/API/console/schema tree, procurement composition, prompts/configuration, README/ADRs, scripts and source tests.
- Plausible first-party paths checked: Scripted/live next-quote behavior, supplier tools, prompt versions/activation, retries, recovery and budget limits; no capability-research/adoption workflow or parent adaptation procedure.
- Why no material first-party path remains: Quote comparison/rejection adaptation is present-task procurement behavior. Prompt publication/versioning changes configuration but has no external-and-prospective sensing/options/decision-return loop for the service capability.

## S5 — Policy and identity

- State: —
- Function: Procurement prompt rules, a caller-supplied owner header and human approval of exact order arguments do not provide an identity/ultimate-policy matter reaching legitimate authority and returning a binding governing decision.
- Disturbance / variety regulated: No distinct function-specific regulation established at this boundary.
- Decisive decision or feedback right: None supplied for this organizational function.
- Decision owner: No first-party function owner established.
- Supporting / enforcement mechanisms: Prompt activate/pin flow, configured spending/permission constraints, approval expiry/consumption and gateway boundary; no runtime identity deliberation or ultimate-policy escalation path.
- Closure path: No function-specific returned regulation; the operational mechanisms remain as described.
- Why this is / is not agent-owned: The reviewed mechanisms do not establish the function before ownership classification.
- Evidence: [`runtime/agents.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/agents.py); [`runtime/prompts.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/prompts.py); [`runtime/approvals.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/approvals.py); [`runtime/api.py`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/runtime/api.py); [`docs/adr/0004-approvals-bound-to-arguments.md`](https://github.com/murilo-bassan/durable-agent-runtime/blob/1d68208d017d27d1b21805753b51a3872c888a52/docs/adr/0004-approvals-bound-to-arguments.md)
- Basis: structural
- Confidence: high within the declared boundary
- Caveats: Bounded absence in the reviewed distribution, not impossibility of future composition.

### Absence scope

- Surfaces inspected: Complete runtime/API/console/schema tree, procurement composition, prompts/configuration, README/ADRs, scripts and source tests.
- Plausible first-party paths checked: Prompt activate/pin flow, configured spending/permission constraints, approval expiry/consumption and gateway boundary; no runtime identity deliberation or ultimate-policy escalation path.
- Why no material first-party path remains: Procurement prompt rules, a caller-supplied owner header and human approval of exact order arguments do not provide an identity/ultimate-policy matter reaching legitimate authority and returning a binding governing decision.

## Recursion

Worker slots, retries and resumed attempts do not create recursive viable organizations.

## Variety and escalation

Model/tool selection absorbs local procurement variety. Version pins, idempotency, ownership checks, schema/approval gates and shared-budget reservations constrain effects. Rejected approvals return concrete observations; budget failures/cancel states are statuses, without an evidenced exceptional organizational authority channel.

## Evidence gaps

No Postgres/model service was started. Native tests require a disposable Postgres database and pytest; their source was inspected but no native-suite/chaos pass is claimed. The source explicitly records a soft run-count cap and external authentication boundary. Index/Skills tests validate this assessment separately.
