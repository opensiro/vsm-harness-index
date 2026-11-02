---
harness_id: agent-harness-happiness-cheng
project_name: Agent Harness (happiness-cheng)
repository: https://github.com/happiness-cheng/agent-harness
review_ref: 50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b
reviewed_at: 2026-11-02
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

# Agent Harness (happiness-cheng)

## Review boundary

- System in focus: The installed local Adrian/min_agent personal-agent workbench, not the repository's development/evaluation organization.
- Purpose and identity: Answer user requests, perform specifically authorized todo/reminder effects and bounded public research with persistent evidence/recovery.
- Relevant environment: Local user, model provider/Ollama, SQLite session/business state, public search/pages, local artifacts and authorized memory.
- Standard-distribution boundary: `min_agent.web`/HarnessApplication→Runtime→owned tool registry and context/budget/session machinery at the pinned revision. Live cloud and local Ollama are alternative inference backends; demo/scripted operation is not autonomous-model evidence.
- Credited operating / distribution surfaces: Runtime/application, tools/task authorization, research subloop, session storage, context/memory, progress guard and optional public-goal feedback.
- Adjacent first-party surfaces excluded from ownership: `min_agent.evaluation` isolated synthetic suites, verifier, night queue and restricted calculator-improvement experiments; tests, acceptance reports, contributor dialogues and CI. The evaluation guide explicitly distinguishes these engineering/diagnostic systems from user-task runtime and shows one-way evaluation→application dependencies.
- First-party operating / deployment modes considered: Local single-user web/CLI, plan/build, user-confirmed writes, pause/steer/checkpoint resume, optional research/memory/public-goal observation.
- Recursion level: One local personal-agent application and its task/research execution.
- Reviewed revision: `50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/README.md) and [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py) expose a first-party Python runtime behind a local web/API application. The application constructs ManagedModel, ToolRegistry, context projection/compaction, durable cumulative/segment budgets, tracing and recovery. [src/min_agent/runtime.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/runtime.py) owns the model→tool→result loop; responses can complete, wait for a concrete user grant, pause on bounded resource failure or resume a factual checkpoint. Authoritative business state and consumed-action receipts are separate from assistant text.

[src/min_agent/research.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/research.py) creates a narrower read-only research loop with parent-shared budget and validated citation/artifact output. Session memory and optional long memory supply retrieved context, not new organizational adaptation rights. [src/min_agent/public_goal_adapter.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/public_goal_adapter.py) optionally compares a frozen confirmed goal with trusted business observation; it is deterministic task progress feedback, not an independent autonomous auditor.

[docs/EVALUATION_V1.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/docs/EVALUATION_V1.md) describes an isolated evaluation system that invokes the same application on synthetic tasks, protects standards and can test restricted calculator patches in retained candidate worktrees. It expressly states that this does not provide general unattended coding or user-task success evidence. Repository co-location does not wire those experimental actors into the assessed local workbench.

## Operational model

The user supplies a goal and retains specific side-effect authorization. Inside that scope, the runtime's model chooses queries/actions and reacts to actual tool results. Local todo/reminder/research outcomes are S1 transformations. Runtime stops, one-time grants, idempotency, evidence preservation and user steering constrain task work without themselves creating S2/S3/S3*/S4/S5.

## S1 — Operations

- State: A
- Function: Goal-directed answers and authorized tool-mediated business/research outcomes.
- Disturbance / variety regulated: User intent, tool failures, ambiguous write state, missing evidence and limited context/budget.
- Decisive decision or feedback right: Select local tool requests, synthesize observations and choose a task response within the confirmed scope.
- Decision owner: Configured model-driven min_agent task agent.
- Supporting / enforcement mechanisms: First-party Runtime, typed tools, exact action grants, authoritative SQLite state/receipts, budgets, compaction, progress guard and checkpoints.
- Closure path: Runtime dispatches selected calls, appends actual outcomes/errors and re-enters model generation; recoverable uncertainty/limits preserve state for targeted continuation.
- Boundary reachability: HarnessApplication._worker directly constructs and invokes Runtime with first-party tools; local Ollama/cloud inference does not replace the first-party loop.
- Why this is / is not agent-owned: A user authorizes scope but does not choose every in-scope reasoning/tool step. Removing model discretion leaves safeguards/storage without equivalent task-dependent operation.
- Evidence: [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [src/min_agent/runtime.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/runtime.py); [src/min_agent/research.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/research.py); [src/min_agent/task_state.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/task_state.py).
- Basis: structural
- Confidence: high for implementation ownership.
- Caveats: Demo and scripted tests are not live autonomy validation. No provider run or user-task quality measurement was executed for this assessment.

## S2 — Coordination

- State: —
- Function: Coordination at the declared delivery-system recursion.
- Disturbance / variety regulated: Candidate regulatory paths are inspected below.
- Decisive decision or feedback right: No material function-specific path established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Configuration, workflow state and constraints remain mechanisms.
- Closure path: No shipped closure for this function.
- Why this is / is not agent-owned: Local production or a deterministic transition does not own this separate function.
- Evidence: [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [src/min_agent/research.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/research.py); [src/min_agent/operations.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/operations.py)
- Basis: structural
- Confidence: medium-high within the declared source boundary.
- Caveats: Downstream/operator organizations may add functions outside this assessment.

### Absence scope

- Surfaces inspected: [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [src/min_agent/research.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/research.py); [src/min_agent/operations.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/operations.py)
- Plausible first-party paths checked: Separate sessions/owners, a narrowed research child, per-session single writer/queues, transactions and idempotent action receipts.
- Why no material first-party path remains: Session isolation and parent-child task decomposition do not establish an inter-S1 conflict-adjustment relation with autonomous coordination discretion. The application ships no S2-specific mutual adjustment constructor; deterministic data integrity is not by itself such a function.


## S3 — Inside-and-now control

- State: —
- Function: Inside-and-now control at the declared delivery-system recursion.
- Disturbance / variety regulated: Candidate regulatory paths are inspected below.
- Decisive decision or feedback right: No material function-specific path established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Configuration, workflow state and constraints remain mechanisms.
- Closure path: No shipped closure for this function.
- Why this is / is not agent-owned: Local production or a deterministic transition does not own this separate function.
- Evidence: [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [src/min_agent/task_state.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/task_state.py); [src/min_agent/progress_guard.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/progress_guard.py); [src/min_agent/runtime.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/runtime.py)
- Basis: structural
- Confidence: medium-high within the declared source boundary.
- Caveats: Downstream/operator organizations may add functions outside this assessment.

### Absence scope

- Surfaces inspected: [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [src/min_agent/task_state.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/task_state.py); [src/min_agent/progress_guard.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/progress_guard.py); [src/min_agent/runtime.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/runtime.py)
- Plausible first-party paths checked: Cumulative and segment budgets, user stop/steer, plan/build, exact grants, task queues, checkpoints and public task scores, including possible parent current control.
- Why no material first-party path remains: These regulate one task or enforce preselected constraints. No whole-application current operating view coupled to substantive cross-unit resource/commitment authority and returned regulation is supplied. Individual user task approvals/steering are not an S3 parent loop.


## S3* — Complementary audit

- State: —
- Function: Complementary audit at the declared delivery-system recursion.
- Disturbance / variety regulated: Candidate regulatory paths are inspected below.
- Decisive decision or feedback right: No material function-specific path established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Configuration, workflow state and constraints remain mechanisms.
- Closure path: No shipped closure for this function.
- Why this is / is not agent-owned: Local production or a deterministic transition does not own this separate function.
- Evidence: [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [src/min_agent/public_goal_adapter.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/public_goal_adapter.py); [src/min_agent/public_feedback.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/public_feedback.py); [docs/EVALUATION_V1.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/docs/EVALUATION_V1.md); [src/min_agent/evaluation/verifier.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/evaluation/verifier.py)
- Basis: structural
- Confidence: medium-high within the declared source boundary.
- Caveats: Downstream/operator organizations may add functions outside this assessment.

### Absence scope

- Surfaces inspected: [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [src/min_agent/public_goal_adapter.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/public_goal_adapter.py); [src/min_agent/public_feedback.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/public_feedback.py); [docs/EVALUATION_V1.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/docs/EVALUATION_V1.md); [src/min_agent/evaluation/verifier.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/evaluation/verifier.py)
- Plausible first-party paths checked: Runtime tracing/result truth, public-goal business-state observation, progress scoring and isolated evaluation/verifier/restricted-improvement tooling.
- Why no material first-party path remains: Within the local workbench, observations and deterministic task checks support routine completion/accountability, without a separately empowered complementary audit actor and corrective return. The stronger protected evaluator belongs to the explicitly adjacent synthetic engineering system; its dependency is evaluation→application and is not installed as the application's audit loop.


## S4 — Outside-and-then intelligence

- State: —
- Function: Outside-and-then intelligence at the declared delivery-system recursion.
- Disturbance / variety regulated: Candidate regulatory paths are inspected below.
- Decisive decision or feedback right: No material function-specific path established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Configuration, workflow state and constraints remain mechanisms.
- Closure path: No shipped closure for this function.
- Why this is / is not agent-owned: Local production or a deterministic transition does not own this separate function.
- Evidence: [src/min_agent/research.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/research.py); [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [README.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/README.md); [docs/EVALUATION_V1.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/docs/EVALUATION_V1.md); [src/min_agent/evaluation/improvement.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/evaluation/improvement.py)
- Basis: structural
- Confidence: medium-high within the declared source boundary.
- Caveats: Downstream/operator organizations may add functions outside this assessment.

### Absence scope

- Surfaces inspected: [src/min_agent/research.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/research.py); [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [README.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/README.md); [docs/EVALUATION_V1.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/docs/EVALUATION_V1.md); [src/min_agent/evaluation/improvement.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/evaluation/improvement.py)
- Plausible first-party paths checked: Public research, memory retrieval/retention, contextual compaction, user memory settings and restricted calculator candidate generation, including parent adaptation options.
- Why no material first-party path remains: Research executes the current user question; memory preserves context. No external/prospective environment model produces organizational capability adaptation options and returns them to current workbench regulation. Synthetic defect repair is adjacent internal engineering and is not imported as runtime S4.


## S5 — Policy and identity

- State: —
- Function: Policy and identity at the declared delivery-system recursion.
- Disturbance / variety regulated: Candidate regulatory paths are inspected below.
- Decisive decision or feedback right: No material function-specific path established.
- Decision owner: No credited first-party owner for this function.
- Supporting / enforcement mechanisms: Configuration, workflow state and constraints remain mechanisms.
- Closure path: No shipped closure for this function.
- Why this is / is not agent-owned: Local production or a deterministic transition does not own this separate function.
- Evidence: [src/min_agent/task_state.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/task_state.py); [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [src/min_agent/public_goal_registry.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/public_goal_registry.py); [README.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/README.md)
- Basis: structural
- Confidence: medium-high within the declared source boundary.
- Caveats: Downstream/operator organizations may add functions outside this assessment.

### Absence scope

- Surfaces inspected: [src/min_agent/task_state.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/task_state.py); [src/min_agent/application.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/application.py); [src/min_agent/public_goal_registry.py](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/src/min_agent/public_goal_registry.py); [README.md](https://github.com/happiness-cheng/agent-harness/blob/50b27bfab099e7e4b3f085a9468d0b8bc6b44c4b/README.md)
- Plausible first-party paths checked: User goals/confirmation, plan/build transitions, tool restrictions, source/owner checks, memory consent and developer-defined application policies; possible parent governance.
- Why no material first-party path remains: These protect specific operational authority/data. No identity/ultimate-policy matter reaches a legitimate parent through a function-specific decision path and returns as governing policy at this recursion. Human final say over an ordinary write is not S5.


## Recursion

The research child has narrower tools and a linked budget/trace; it is task decomposition, not an independently viable recursive unit with a proven local metasystem. Sessions are operational contexts, not automatically viable organizations.

## Variety and escalation

Typed errors, unknown-effect state, citations, raw artifacts and factual checkpoints preserve distinctions needed for continuation. Compaction is explicitly lossy model/context projection. Budget exhaustion, user confirmation and FAILED/UNKNOWN records are not themselves algedonic channels or positive higher-function evidence.

## Evidence gaps

Assessment uses pinned public source and supported entrypoint wiring; no local/cloud model, personal database, memory or paid external service was accessed. Existing author's acceptance numbers were not reproduced or treated as organizational evidence. Adjacent evaluation/night/improvement experiments are described to make boundary exclusion reproducible, not credited to the runtime.
