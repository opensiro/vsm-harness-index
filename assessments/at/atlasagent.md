---
harness_id: atlasagent
project_name: AtlasAgent
repository: https://github.com/malevrigns/atlas-agent-control-plane
review_ref: 9e7dbe23409f82c8c111e8035843c1d69aae8b28
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AtlasAgent

## Review boundary

- System in focus: the first-party **currently deployed TypeScript Hono API** (`backend/api-ts`), its documented direct Node entry, officially shipped Docker Compose API service, and shipped TS sandbox/clients at frozen revision `9e7dbe23409f82c8c111e8035843c1d69aae8b28`.
- Purpose and identity: publicly described agent-control plane promising plans, tooling, risk/approval, acceptance gates, evidence provenance and checkpoint recovery, but the **current chosen runtime is a partial TypeScript migration**, not the legacy feature-complete Python source tree.
- Relevant environment: one operator, TypeScript SQLite task/session records, optional model-provider endpoint and API key, browser/TUI, sandbox service, API calls, user/task text.
- Standard-distribution boundary: both documented `cd backend/api-ts && pnpm dev` and `docker compose` (the `api` service builds `./backend/api-ts`). Follow source imports from `src/app.ts` into actual route handlers. Do **not** include `backend/api/app/application/*`, which the current README explicitly labels **legacy Python (not the runtime)**.
- Credited operating / distribution surfaces: `README.md`, `docker-compose.yml`, `scripts/start.sh`, `backend/api-ts/src/app.ts`, TS session SSE, actual `/control-plane/tasks` implementation, TS stubbed checkpoint/tool/acceptance endpoints and TS sandbox endpoints.
- Adjacent first-party surfaces excluded from ownership: the substantial but unwired legacy Python agent loop/planner/tool gates/checkpoint/acceptance/review stack, 62-chapter explanatory tutorial, marketing diagrams and aspirational README features, frontend placeholders and developer CI.
- First-party operating / deployment modes considered: recommended quick-start Node API and full Docker Compose with optional `LLM_API_KEY` configured; simple chat model endpoint vs offline local answer; both resolve to TS source and no active autonomous task runner.
- Recursion level: the AtlasAgent **deployed** single runtime as manager of user conversation/tasks; not the historical, no-longer-selected Python agent process.
- Reviewed revision: `9e7dbe23409f82c8c111e8035843c1d69aae8b28` (discovery #193 frozen).
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The source contains a striking implementation **split**. `backend/api/app/application/agent_loop.py`, `tool_runtime.py`, `agent_task_runner.py`, `checkpoint_service.py`, `acceptance_gate_service.py`, `scope_audit_service.py`, `coverage_review_service.py` and related Python files offer rich *historical* candidate control-plane logic. But the current README directly marks `backend/api/` as **legacy Python (not the runtime)**. Both advertised execution commands — `backend/api-ts` Node Hono and Docker Compose `api.build.context: ./backend/api-ts` — select the separate TypeScript application. No shipped integration starts or imports the Python agent-runner from the TS application. Do not award source-level VSM autonomy to unused code merely because it resides in the same Git repository ([README.md](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/README.md), [docker-compose.yml](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/docker-compose.yml), [backend/api-ts/src/app.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/app.ts), [backend/api/app/application/agent_task_runner.py](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api/app/application/agent_task_runner.py)).

The shipped `controlPlaneRoutes` accepts an operator JSON description and inserts a row with `status: pending` and a static empty `progress` graph. It offers list/get. Its `/tasks/:taskId/checkpoints` and `/tool-invocations` endpoints return literal empty items; the Hono app additionally mounts `stubRoutes` for `/agent-core/tools`, `/acceptance/checks`, `/security/checks`, `/skills`, `/multi-agent/roles`, etc. These paths do not start a task or execute a tool/acceptance decision ([backend/api-ts/src/presentation/http/routes/control-plane.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/control-plane.ts), [backend/api-ts/src/presentation/http/routes/stubs.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/stubs.ts), [backend/api-ts/src/app.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/app.ts)).

The shipped `agent-stream` updates conversation session state, appends the user's message, then calls `generateAnswer` **once**. With `LLM_API_KEY`, `generateAnswer` POSTs one `/chat/completions` request and streams its returned text as sliced SSE deltas. Without a key it emits an offline explanatory acknowledgment. There is no loop in which the model chooses a tool, receives tool results, revises the plan or continues to an operational task; a persisted `task_done` event is emitted for the chat response, not for acceptance-gated task execution. Model-generated prose is not an adaptive autonomous harness S1 merely because it is streamed and remembered ([backend/api-ts/src/application/agent-stream.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/application/agent-stream.ts), [backend/api-ts/src/application/session-service.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/application/session-service.ts), [backend/api-ts/src/presentation/http/routes/sessions.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/sessions.ts)).

The official sandbox `backend/sandbox-ts` can expose operations through a separate service, but the deployed TS API's chat/task routes do not connect model tool calls to that sandbox. Presence of isolated infrastructure therefore does not make an operating agent loop. The first-party app is currently an API shell/chat client/task ledger, not the documented autonomous control plane ([docker-compose.yml](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/docker-compose.yml), [backend/api-ts/src/app.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/app.ts), [backend/api-ts/src/application/agent-stream.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/application/agent-stream.ts)).

## Operational model

A user submits a task: TS records a pending row and returns its metadata. A user sends chat text: the application stores a conversation message, optionally makes one model text-completion call, emits its text and `task_done` message, then marks the chat idle. No control-plane task executor consumes pending rows, model-driven tool invocations are not wired, and advertised acceptance/checkpoint lists are empty. The operator cannot obtain the legacy Python processing paths through the documented Node/Docker program. There was no live LLM/sandbox execution; the deployed reachability is established by direct source/wiring inspection.

## S1 — Operations

- State: —
- Function: no first-party shipped agentic operational loop that takes a task, chooses contextual actions, observes results and advances execution to task completion is demonstrated.
- Disturbance / variety regulated: user queries are answered with one completion or an offline acknowledgment, while separately stored task records remain pending.
- Decisive decision or feedback right: choose next substantive tool/task action in response to observed environment/tool result; not exercised by current TypeScript app.
- Decision owner: none in the deployed agent-control-plane runtime; the external text-completion model generates a single reply, not the app's autonomous task/tool workflow.
- Supporting / enforcement mechanisms: Hono route, SQLite task/session store, single LLM completion/SSE, TS sandbox not connected to task actions.
- Closure path: message → one model prose answer → chat `task_done`; or JSON task → pending DB record. Neither closes an adaptive task/action/environment feedback cycle.
- Boundary reachability: both documented official Node and Compose paths run `backend/api-ts`, not legacy Python.
- Why this is / is not agent-owned: there is no installed operational agent controller in TypeScript that selects and acts on tools/tasks; external completion is an answer, and legacy Python agent loop is not active.
- Evidence: [README.md](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/README.md); [docker-compose.yml](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/docker-compose.yml); [backend/api-ts/src/app.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/app.ts); [backend/api-ts/src/application/agent-stream.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/application/agent-stream.ts); [backend/api-ts/src/presentation/http/routes/control-plane.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/control-plane.ts).
- Basis: explicit deployed entry, source call graph and no-op route implementation.
- Confidence: high in narrow frozen shipping state, not a prediction about a later TS port.
- Caveats: source repository contains historical Python implementations, but no current documented distribution path executes them.

### Absence scope

- Surfaces inspected: current Node/Docker entry, TS Hono composition, task routes, chat/SSE generator, stubs, sandbox integration, legacy Python package location.
- Plausible first-party paths checked: `POST /control-plane/tasks`, chat SSE, `agent-core/tools`, sandbox TS worker, legacy `agent_task_runner` and `agent_loop`.
- Why no material first-party path remains: TS creates pending records and prose replies but exposes no model-led environment action/feedback loop; Python task runtime is not selected by official modes.

## S2 — Coordination

- State: —
- Function: no deployed inter-S1 conflict-regulation or sibling-work attenuation can close when no deployed operational S1 workers are instantiated by the selected TS runtime.
- Disturbance / variety regulated: distinct sessions and task rows can coexist, but there are no active sibling coding agents with a shared execution resource under this runtime.
- Decisive decision or feedback right: select and enforce a conflict-regulating response between concurrently operating S1 actors; absent.
- Decision owner: none demonstrated in TS.
- Supporting / enforcement mechanisms: SQLite sessions/tasks and sandbox services, but not applied to a live multi-agent operation.
- Closure path: task rows are stored and queried, no linked sibling S1 actions or interference-specific remedy returns.
- Boundary reachability: `/multi-agent/roles` is a stub returning `items: []`; task ledger is non-executing.
- Why this is / is not agent-owned: no first-party multi-agent coordination constructor or decision loop exists on the shipped call path.
- Evidence: [backend/api-ts/src/presentation/http/routes/control-plane.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/control-plane.ts); [backend/api-ts/src/presentation/http/routes/stubs.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/stubs.ts).
- Basis: deployed route and call-graph negative.
- Confidence: high for reviewed TypeScript mode.
- Caveats: a sandbox may prevent external file cross-contamination; unsupported integration is not credited.

### Absence scope

- Surfaces inspected: TS task records, sessions, multi-agent stub, sandbox container, Compose services.
- Plausible first-party paths checked: task concurrency, queued rows, multi-agent roles API and task ownership.
- Why no material first-party path remains: no active sibling S1 operations are created or controlled by the shipped TS API.

## S3 — Inside-and-now control

- State: —
- Function: no first-party current whole-agent-system control judgment and returned change in executing operations is demonstrated.
- Disturbance / variety regulated: pending tasks, chat session status and basic API authorization.
- Decisive decision or feedback right: prioritize, allocate, interrupt or redirect current worker commitments based on whole-system state, not just store/view task records.
- Decision owner: no active model-led or parent-facing whole-current control path over operational workers.
- Supporting / enforcement mechanisms: `/control-plane/tasks` create/get/list and SSE session status `running/idle`.
- Closure path: UI/API creates a pending task and reads it; without execution workers there is no regulatory return into operations.
- Boundary reachability: current TS API only.
- Why this is / is not agent-owned: a control-plane route name, DB ledger and a chat status flag are not current organizational management.
- Evidence: [backend/api-ts/src/presentation/http/routes/control-plane.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/control-plane.ts); [backend/api-ts/src/application/agent-stream.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/application/agent-stream.ts).
- Basis: shipped source path negative.
- Confidence: high.
- Caveats: user-driven work in an unrelated external application is not claimed here.

### Absence scope

- Surfaces inspected: TS task CRUD, session/message event stream, API status and app wiring.
- Plausible first-party paths checked: task scheduler, reallocation, task start/retry, whole-current operator control and persisted session status.
- Why no material first-party path remains: no installed task execution or group of controlled operational S1 units exists to receive S3 corrections.

## S3* — Complementary audit

- State: —
- Function: no deployed independently sourced audit of agent work with findings-to-correction/acceptance enforcement is demonstrated.
- Disturbance / variety regulated: completion claims, quality, scope and code/test coverage might need independent verification.
- Decisive decision or feedback right: access actual produced artifacts/evidence independently and reject/repair/accept a claim; absent from selected runtime.
- Decision owner: none in current TS app.
- Supporting / enforcement mechanisms: README promises triple-gate acceptance; Python legacy includes acceptance, scope and coverage services; TS `/acceptance/checks` returns empty items.
- Closure path: chat `task_done` fires following a single model answer with no code/evidence check; task rows remain pending, not audited.
- Boundary reachability: TS acceptance and audit handlers are stubs; legacy Python file presence does not yield a shipped control effect.
- Why this is / is not agent-owned: names and historical verification code cannot produce a current independent challenge or corrective return.
- Evidence: [backend/api-ts/src/presentation/http/routes/stubs.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/stubs.ts); [backend/api-ts/src/application/agent-stream.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/application/agent-stream.ts); [backend/api/app/application/acceptance_gate_service.py](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api/app/application/acceptance_gate_service.py); [backend/api/app/application/coverage_review_service.py](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api/app/application/coverage_review_service.py).
- Basis: deployed route and legacy boundary mismatch.
- Confidence: high.
- Caveats: future TS implementation could provide a genuine reviewer; not proven at this frozen ref.

### Absence scope

- Surfaces inspected: TS acceptance/security stubs, single-turn completion, legacy Python acceptance/scope/coverage logic and runtime selector.
- Plausible first-party paths checked: final acceptance command, scope audit, coverage reviewer, event history, tool acceptance gate.
- Why no material first-party path remains: all substantive candidates are legacy Python and not wired; current TS route returns empty lists and chat completion bypasses acceptance.

## S4 — Outside-and-then intelligence

- State: —
- Function: no deployed prospective environmental intelligence that changes future working capabilities and returns the result into operations.
- Disturbance / variety regulated: shifting external tasks/requirements/providers/knowledge.
- Decisive decision or feedback right: examine future/external differences and choose/install a new capability/strategy; absent.
- Decision owner: none on selected runtime.
- Supporting / enforcement mechanisms: optional LLM provider configuration, TS file/session store and memory/RAG/skills stubs.
- Closure path: configuration read or UI task creation → static subsequent interactions; no external scanning and future capability adaptation loop.
- Boundary reachability: `/memories`, `/skills` and `/rag/knowledge-bases` currently empty; no agent adapts operating repertoire.
- Why this is / is not agent-owned: a configurable text-completion model and empty knowledge endpoints are not future-sensing organizational intelligence.
- Evidence: [backend/api-ts/src/presentation/http/routes/stubs.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/stubs.ts); [backend/api-ts/src/application/agent-stream.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/application/agent-stream.ts).
- Basis: shipped source negative.
- Confidence: high for pinned TS runtime.
- Caveats: manually changing environment variables is operator setup, not first-party S4.

### Absence scope

- Surfaces inspected: TS memory/skills/RAG stubs, static config and chat model selection, current task API.
- Plausible first-party paths checked: long-term learning, external change analysis, skill revision and prospective provider choice.
- Why no material first-party path remains: no implemented TS future-sensing or autonomous/parent-returned capacity-change transaction.

## S5 — Identity and ultimate policy

- State: —
- Function: no separate first-party highest-level identity/ethos/policy judgment and binding return to organization-wide operations is evidenced.
- Disturbance / variety regulated: ultimate project mission, conflict of operational requirements with future identity constraints.
- Decisive decision or feedback right: settle ultimate mandate/policy and return governing policy into S1–S4; absent.
- Decision owner: user/developer owns API key and static configuration outside any regulatory mission choice.
- Supporting / enforcement mechanisms: TS API key auth/CORS and environment config, DB task project ID.
- Closure path: static API authorization and user-supplied task names regulate access and data, not a legitimate ultimate-policy judgment.
- Boundary reachability: `authMiddleware` and config are wired, but no policy-choice channel exists and no active S3/S4 tension is resolved.
- Why this is / is not agent-owned: authentication, key validation, and project labels do not constitute an S5 organ.
- Evidence: [backend/api-ts/src/app.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/app.ts); [backend/api-ts/src/core/auth.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/core/auth.ts); [backend/api-ts/src/presentation/http/routes/control-plane.ts](https://github.com/malevrigns/atlas-agent-control-plane/blob/9e7dbe23409f82c8c111e8035843c1d69aae8b28/backend/api-ts/src/presentation/http/routes/control-plane.ts).
- Basis: bounded negative on actual shipping path.
- Confidence: high.
- Caveats: human institutional governance of a wider project may exist outside this source artifact.

### Absence scope

- Surfaces inspected: current auth/tenant configuration, task project field, docs, selected entry and operational handlers.
- Plausible first-party paths checked: root agent charter, system identity, policy approvals and ultimate decision-return.
- Why no material first-party path remains: all observed choices are static setup/auth or plain task labels, not distinct ultimate organizational policy decisions.

## Evidence gaps

- Live Node/Docker/LLM/provider deployment was not exercised. Assessment maps actual documented source wiring at the immutable Git commit.
- The repository contains more capable *legacy Python* control-plane code, but the **current README** and **both official deploy modes** select `backend/api-ts`. This is a **runtime selection** exclusion, not a claim that no agent-capable source ever existed or could be resurrected.
- A single LLM `/chat/completions` API call is not an autonomous operational task/tool loop; streaming SSE and `task_done` for prose must not be conflated with finished/accepted code tasks.
- `/control-plane/tasks` creates only `pending` records, while checkpoint/tool/acceptance endpoints are stubs, so README evidence/verification claims cannot be imported as operational VSM evidence.
- A future version shipping the Python agent stack, or a genuinely implemented TS runner, would require a new pinned assessment, not retrospective reinterpretation of this frozen source.

## Conclusion

**Canonical exclusion:** terminal status `excluded-no-agentic-vsm`, vector `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`. The frozen deployed AtlasAgent TypeScript runtime performs task-data storage and one-shot chat text completion but no model-driven tool/action-observation operational loop. Current external app/wider actor and unwired legacy Python controls are excluded by the explicit shipping boundary. All six absences are scoped to **current first-party supported deployment**, not theoretical capability of future versions.
