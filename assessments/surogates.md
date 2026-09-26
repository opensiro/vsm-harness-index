---
harness_id: surogates
project_name: Surogates
repository: https://github.com/invergent-ai/surogates
review_ref: 4069e5ad736f1b21584543f734c9481193bcde65
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Surogates

## Review boundary

- System in focus: one first-party Surogates-managed **Mission organization** at pinned revision `4069e5ad736f1b21584543f734c9481193bcde65`, including the coordinator session, task-backed worker sessions, durable task DAG, coordination board, mission evaluator/judge, first-party harness/tool/runtime state, parent mission controls and mission-rubric refinement path.
- Purpose and identity: pursue a durable criterion-driven objective through several autonomous worker operations while preserving coordination, whole-mission current control, independent challenge of completion claims and legitimate parent authority over the mission's ultimate success policy.
- Relevant environment: user/parent intent and intervention; repository/data/business resources reached by mission workers; external model providers; tool results and sandboxes; changing task outcomes/failures; worker crashes/timeouts; verifier evidence; mission budget; external services and work products.
- Standard-distribution boundary: the AGPL Surogates backend/runtime, worker harness, built-in mission/task/board tooling and documented self-hosted execution reached by `/mission`. External LLM endpoints, MCP servers, business systems and Kubernetes/PostgreSQL/Redis infrastructure remain dependencies/environment. Installation-level expert training and repository-development/evaluation surfaces are outside the chosen mission recursion unless a documented mission path directly reaches them.
- Credited operating / distribution surfaces: `README.md`; `docs/tasks/index.md`; `docs/board/index.md`; `surogates/missions/commands.py`; `surogates/missions/evaluator.py`; mission/task dispatcher and worker-notification paths; first-party coordinator/worker tool filtering; mission dashboard/current-state APIs; the documented research-mission held-out merge gate as corroborating S3* independence.
- Adjacent first-party surfaces excluded from ownership: generic multi-tenant installation administration; expert collection/training/activation lifecycle; CI/release/development plans; tests as tests; standalone repository benchmarking; downstream application-specific business logic. Research-mission target-code optimization is treated as one possible mission's operational work, not automatically as S4 adaptation of the mission organization itself.
- First-party operating / deployment modes considered: ordinary `/mission` with a coordinator and durable task workers; automatic coordination board for fan-out; mission judge continuation loop; parent pause/resume/cancel/budget controls; parent-authorized rubric refinement. Research mission `/auto-research` is used only where it strengthens the independent-audit witness through a machine-owned held-out evaluation path; its benchmark-improvement objective is not used to assign S4.
- Recursion level: one Mission is the system-in-focus. Its task-backed worker sessions are distinct S1 units when they own separate operational outcomes. The coordinator is the metasystemic current-control actor at this recursion. A whole Surogates installation is a higher recursion and is deliberately not mixed into this assessment.
- Reviewed revision: `4069e5ad736f1b21584543f734c9481193bcde65`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Surogates ships its own managed-agent runtime rather than merely wrapping an external agent product. Workers run the reasoning loop and tool routing; sessions are durable append-only event logs; tool execution is governed before it reaches isolated sandboxes or external services. At the Mission recursion, the harness deliberately separates operational task workers from a strict coordinator: `handle_mission_create()` stamps the coordinator session with `coordinator=True` and `strict_coordinator=True`, removes implementation tools and preloads the task-orchestrator skill so the coordinator must manage work through durable task/delegation surfaces rather than performing the implementation itself.

The task layer provides persistent S1 work cells. A coordinator can `spawn_task`; each task owns one or more attempt sessions, a goal, dependencies, result metadata and a durable lifecycle. Workers can explicitly complete or block themselves. The dispatcher promotes ready tasks, claims them atomically, classifies ended attempts and retries crash/timeout failures up to the configured limit. Worker terminal events are written into the coordinator's log and re-enqueue the coordinator so current mission control actually observes the change.

Fan-out automatically creates a Coordination Board. Workers and the coordinator share verified typed notes. `CLAIM` notes exist specifically to prevent overlapping work; `FAIL` notes expose an already-observed dead end before siblings repeat it. Board snapshots/deltas are injected into later harness iterations, so the coordination relation changes subsequent S1 behavior instead of remaining passive storage.

Mission current control is separate from the deterministic dispatcher. The coordinator sees task outcomes/current work and holds the tools to spawn, unblock or cancel child commitments. When new task evidence arrives, the mission evaluator independently reads completed/in-flight task rows plus structured result metadata under a strict rubric. It explicitly ignores completion claims in prose. A `needs_revision` verdict is persisted and returned as a synthetic continuation telling the coordinator what is missing; the coordinator then decides which corrective tasks to create. This closes an independent challenge-to-correction loop rather than merely recording an eval score.

Parent authority is also functionally separated. The user can change current-control resources through the mission token budget and can cascade-cancel all non-terminal workers. More importantly, when the judge concludes that the rubric itself is defective, it may author a replacement but cannot apply it; the coordinator may only relay it; only the user can accept or reject. Acceptance commits the recorded rubric verbatim, emits an amended-mission event and resumes the same mission under the new completion policy. That is an identity/ultimate-policy path at the chosen mission recursion, not an ordinary one-tool approval.

## Operational model

A principal creates `/mission <description>\n\nRubric: ...`. Surogates persists the Mission, marks the calling session as strict coordinator and wakes it with a kickoff instructing decomposition into specialist task workers and verifier tasks. The coordinator chooses a task structure and creates durable tasks. Distinct worker sessions perform the actual work, can spawn further work where allowed, write evidence/results and share coordination notes. Their completed/failed/blocked state wakes the coordinator.

Every terminal task can trigger the mission judge. The judge reads the standing rubric, coordinator response, completed task evidence/result metadata and in-flight state. `satisfied`, `blocked` and `failed` can terminate; `needs_revision` increments the iteration and injects actionable feedback into the coordinator's next turn. The coordinator then makes a current whole-mission decision about additional/corrective work. The parent can pause/resume the evaluator, set/clear the mission token ceiling, or cancel the mission; cascade cancellation interrupts every running mission worker and marks all non-terminal task rows cancelled.

If repeated evidence demonstrates that the success policy itself is unreachable, the judge can propose a replacement rubric. The mission pauses. The coordinator cannot author or apply it. `/mission accept` reads the recorded proposal, amends the Mission row and resumes subsequent operation; `/mission reject` ends under the held verdict. The mission description remains the standing intent and rubric amendments are capped, preventing ordinary operational drift from silently redefining success.

## S1 — Operations

- State: A
- Function: perform the substantive mission work through autonomous task-backed worker sessions that act on their local task environments and return durable results/evidence.
- Disturbance / variety regulated: heterogeneous task goals; repository/data/tool state; external service responses; model uncertainty; local tool failures; task-specific blockers; worker crashes/timeouts; changing artifacts and observations.
- Decisive decision or feedback right: choose the task-specific action/tool sequence, react to observations and decide when to call `worker_complete`, `worker_block`, or otherwise finish the local task attempt.
- Decision owner: the model actor in each first-party Surogates-managed worker session.
- Supporting / enforcement mechanisms: Surogates worker harness loop; task/session records; sandbox/tool routing; per-session policy; durable event log; `worker_complete`, `worker_block`, `worker_context`; retry/session creation and result persistence.
- Closure path: coordinator creates a task -> dispatcher creates/queues a worker session -> worker model acts through governed tools and receives observations -> worker completes/blocks or naturally terminates -> task result/metadata and event are persisted -> parent coordinator is notified and later operation consumes the result.
- Boundary reachability: `/mission` is a documented ordinary runtime mode; task workers are created by the shipped task layer and run through the same first-party harness loop, not through an adjacent benchmark or external coding-agent process.
- Why this is / is not agent-owned: the dispatcher and tool governors constrain when/how work can run, but the contextual operational choice inside the task is made by the worker model. Removing that actor while leaving task rows, schedules and policy machinery would not produce the same substantive task outcome.
- Evidence: [`README.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/README.md); [`docs/tasks/index.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/docs/tasks/index.md); mission creation/runtime paths in [`surogates/missions/commands.py`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/surogates/missions/commands.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a deterministic dispatcher owns lifecycle transitions such as ready/running/retry, but those are supporting execution mechanics rather than the worker's operational decision right.

## S2 — Coordination

- State: A
- Function: attenuate concrete duplicate-work and collision variety among sibling S1 workers in a fan-out mission by sharing verified claims, dead ends, facts and results before siblings independently repeat conflicting work.
- Disturbance / variety regulated: two or more workers unknowingly taking the same work; siblings repeating a dead end already encountered elsewhere; retry workers losing prior group knowledge; mutually blind parallel exploration wasting the same constrained effort.
- Decisive decision or feedback right: expose a concrete coordination signal such as `CLAIM`/`FAIL`/`RESULT`, interpret the current shared board and alter local work in response — for example, claim an area so siblings avoid overlap or avoid a failure path already demonstrated by another worker.
- Decision owner: distributed Surogates worker/coordinator model actors that choose and consume board notes inside the mission group; first-party verification/admission machinery preserves board quality but does not replace their coordination judgment.
- Supporting / enforcement mechanisms: automatic `context_group_id`; `share_note`, `read_board`, `expand_note`; claim TTLs/caps; note verification; group-wide board; automatic join snapshots and per-iteration deltas; supersede/expiry maintenance; event-log persistence.
- Closure path: sibling S1s operate in the same fan-out -> a worker observes an overlap/dead-end/reusable result and posts a typed note -> Surogates verifies/adopts it and injects board state/deltas into sibling later turns -> sibling model sees the distinction before acting -> later task behavior avoids the claimed or failed path / reuses the result.
- Boundary reachability: board formation is automatic on the first spawn and board tools appear automatically for every group member; mission coordinators and retry attempts inherit the same group id. No optional downstream application wiring is required.
- Distinct S1 units: task-backed or spawned worker sessions that own separate mission subtasks/outcomes.
- Inter-S1 disturbance: structural duplicate work and repeated dead ends among parallel sibling workers; `CLAIM` is explicitly defined to prevent overlap, while `FAIL` exists to stop another worker repeating an observed dead end.
- Attenuating coordination relation: verified typed notes and automatic deltas make the interfering state mutually visible early enough for local adjustment.
- Feedback into subsequent S1 behaviour: board snapshots/deltas are appended into later harness history and `read_board` exposes current state at decision points; the next model turn therefore receives and can act on sibling coordination evidence.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping is tied to an explicitly named interference class — overlapping claims and repeated dead ends — plus an implemented feedback path that changes sibling work. Generic task DAG edges or messages are not used as the decisive evidence.
- Why this is / is not agent-owned: deterministic admission/TTL/deduplication enforce the channel, but the workers decide what concrete work to claim/report and how to revise their own actions after reading sibling state. The material mutual-adjustment discretion is therefore agent-owned.
- Evidence: [`docs/board/index.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/docs/board/index.md); [`docs/tasks/index.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/docs/tasks/index.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the LLM note verifier is not itself credited as S2 owner; it only preserves the coordination channel's integrity.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate current mission-wide commitments, task structure and resource envelope from a whole-mission view, with an autonomous coordinator base mode and an explicit parent current-control mode.
- Disturbance / variety regulated: incomplete or mis-scoped work after evaluation; blocked/failed tasks; current dependency/commitment changes; work requiring another corrective round; token-resource pressure; a mission direction that must be stopped immediately; current workers that must be interrupted together.
- Decisive decision or feedback right: in base mode, choose/revise the mission's current task commitments by spawning corrective work, unblocking owned tasks or cancelling child tasks after observing task/board/judge state; in parent mode, set/clear the mission-wide token ceiling or terminate/cascade-cancel the current workstream.
- Decision owner: base `A` mode — the strict coordinator model actor; parent `P` mode — the authenticated mission principal/user as legitimate parent.
- Supporting / enforcement mechanisms: strict coordinator flag/tool filtering; task DAG/status/result state; coordination board; evaluator continuation; `spawn_task`, `unblock_task`, `cancel_task`; mission dashboard/current-state surfaces; token accounting/budget store; pause/resume/cancel handlers; cascade interrupts and task-state update.
- Closure path: whole-mission current task/evidence state reaches coordinator or parent -> actor selects a current intervention -> Surogates mutates task commitments/budget/mission state and wakes or interrupts relevant sessions -> subsequent S1 work proceeds under the changed current-control state.
- Boundary reachability: mission creation structurally makes the root session a strict coordinator; task events re-enqueue it; parent control verbs are ordinary `/mission` commands in the same runtime.
- Why this is / is not agent-owned: the dispatcher deterministically promotes/claims/retries tasks, but does not decide what new corrective commitments the mission should create after a `needs_revision`. That judgment belongs to the coordinator. Conversely, user budget/cascade choices are genuinely parent-owned rather than attributed to the runtime that enforces them.
- Whole-system current view: evaluator/coordinator paths expose completed and in-flight mission tasks, current mission iteration/rubric, board state and judge feedback; the mission dashboard exposes the DAG and live worker activity to the parent.
- Current-control decision scope: current task commitments/dependencies and corrective waves in `A`; mission-wide token resource ceiling and all-worker termination in `P`.
- Evidence: [`docs/tasks/index.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/docs/tasks/index.md); [`surogates/missions/evaluator.py`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/surogates/missions/evaluator.py); [`surogates/missions/commands.py`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/surogates/missions/commands.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary task decomposition alone is not the S3 evidence. The positive mapping is the mission-wide exception/revision loop plus whole-mission parent resource/termination authority.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | strict coordinator model actor | new terminal task evidence / evaluator `needs_revision` / blocked or failed current commitment | coordinator chooses corrective task creation/unblock/cancel; changed task DAG drives subsequent workers | `docs/tasks/index.md`; `surogates/missions/evaluator.py`; mission kickoff/strict coordinator in `surogates/missions/commands.py` |
| Parent (`P`) | authenticated mission principal/user | parent judges current resource envelope or whole direction must change | `/mission budget` changes the mission token ceiling; `/mission cancel --cascade` cancels all non-terminal task rows and interrupts running worker sessions | `surogates/missions/commands.py` |

## S3* — Complementary audit

- State: A
- Function: challenge ordinary coordinator/worker completion claims through a separately prompted mission judge that reads persisted task reality and returns an independent verdict/corrective finding into mission control.
- Disturbance / variety regulated: coordinator optimism; prose completion claims unsupported by measurable evidence; worker output that appears complete but fails a mission rubric; incomplete current workstream that needs another corrective round.
- Decisive decision or feedback right: judge the mission against the standing rubric using task/result evidence, choose `satisfied`, `needs_revision`, `blocked` or `failed`, and produce actionable corrective feedback when the ordinary workstream has not demonstrated completion.
- Decision owner: the dedicated mission evaluator model actor reached through the first-party evaluator path, separate from the strict coordinator and task-producing worker sessions.
- Supporting / enforcement mechanisms: task DB queries; bounded completed/in-flight blocks; structured `result_metadata`; strict evaluator system prompt; persisted prior evaluator history; mission evaluation events; synthetic continuation injection; in research mode, server-owned held-out re-run/merge gate whose schema accepts no self-reported score.
- Closure path: workers/coordinator produce ordinary task results/claims -> evaluator obtains task rows/result metadata independently of coordinator prose and applies the rubric -> `needs_revision` finding is persisted and injected as a synthetic continuation -> coordinator wakes and creates corrective work -> later task evidence is judged again.
- Boundary reachability: evaluator firing on terminal mission tasks is an ordinary part of `/mission`; it does not require development-only tests or an external benchmark. Research missions additionally expose a supported machine-held-out audit path that corroborates the independence principle.
- Why this is / is not agent-owned: the audit judgment is made by a separate evaluator model under a prompt that explicitly distrusts coordinator prose and requires concrete completed-task evidence. Deterministic event/state machinery only transports/enforces the judgment.
- Claim being audited: that the current mission workstream has actually met the user's written rubric and may stop.
- Ordinary reporting path: worker results, coordinator synthesis/prose and task completion events.
- Complementary access path: evaluator directly queries persisted completed/in-flight mission task rows and structured result metadata; in research mode the merge path independently re-runs the hidden held-out evaluation server-side rather than accepting an executor/coordinator score.
- Independence boundary: evaluator is a dedicated judge call distinct from coordinator/worker sessions and its system prompt explicitly refuses prose-only completion. Research held-out evaluation is additionally withheld from executors and machine-measured by the harness.
- Who acts on findings: the coordinator receives `needs_revision` as a synthetic continuation and chooses corrective task work; terminal verdicts change mission state. A parent may separately handle rubric-refinement proposals.
- Evidence: [`surogates/missions/evaluator.py`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/surogates/missions/evaluator.py); [`docs/tasks/index.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/docs/tasks/index.md); corroborating independent held-out gate in [`docs/research-missions/index.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/docs/research-missions/index.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic audit logs, policy checks and same-worker self-reflection are not counted. The positive claim is the dedicated evaluator/task-evidence/corrective-continuation relation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented adaptation loop is established **at the chosen Mission recursion** that changes the mission organization's own future capability in response to environmental/future distinctions.
- Disturbance / variety regulated: mission workers may search the web, conduct research, optimize code, learn from task outcomes or operate `/auto-research`, but those activities enact the mission's primary transformation rather than adapt the mission organization itself.
- Decisive decision or feedback right: no separate mission-level actor is shown sensing an external/future change, developing alternative organizational capabilities/postures and adopting one back into the Mission's own operating capability.
- Decision owner: none established for qualifying S4 at this recursion.
- Supporting / enforcement mechanisms: research missions and Idea Tree; external search/tools; memory; skills; installation-level expert data collection/activation; event history; future mission creation/configuration.
- Closure path: research/experiment results can change the target artifact and task plans, but no external/future distinction -> mission-capability adaptation option -> adopted change to the Mission organization's own present capability loop closes.
- Why this is / is not agent-owned: an `/auto-research` mission whose purpose is “improve this benchmark” performs benchmark improvement as S1 work. Calling that self-improvement would conflate the object of work with adaptation of the organization doing the work. Separately, expert `Collect -> external Train -> Activate` belongs to the higher installation recursion and explicitly delegates training/adaptation work outside the platform; it is excluded rather than mixed into mission-level S4.
- Evidence: [`docs/research-missions/index.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/docs/research-missions/index.md); [`docs/experts/index.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/docs/experts/index.md); Profile boundary/recursion rules.
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a different assessment whose system-in-focus is the whole Surogates installation could separately examine expert lifecycle as a constructor/parent adaptation path. That higher-recursion question is deliberately outside this Mission assessment.

### Absence scope

- Surfaces inspected: `/auto-research`, Idea Tree/experiment/merge lifecycle, generic mission continuation, web/search/tool access, memory/skills, expert lifecycle, event history and coordinator protocols.
- Plausible first-party paths checked: research ideation; held-out benchmark optimization; worker retry learning; Coordination Board reuse; memory; expert retraining/activation.
- Why no material first-party path remains: research and retry/board feedback modify the work product or current work strategy; memory persists context; expert retraining is a separate installation-level lifecycle with external training. None closes external-and-prospective adaptation of the Mission organization at the declared recursion.

## S5 — Policy and identity

- State: P
- Function: preserve the mission's standing purpose/success policy and return a legitimate parent decision when evidence shows the rubric itself — rather than merely the work — must change.
- Disturbance / variety regulated: a mission whose operational work cannot satisfy the written rubric because the criterion is contradictory, unreachable or references something outside the standing description; risk that an autonomous coordinator/judge could silently redefine success to fit produced work.
- Decisive decision or feedback right: accept or reject a proposed replacement rubric that changes the authoritative criterion under which the mission may subsequently be judged complete.
- Decision owner: the authenticated mission principal/user as legitimate parent. The judge may author a proposal; the coordinator may relay it; neither may apply it.
- Supporting / enforcement mechanisms: immutable standing `description`; persisted rubric; judge-authored `mission.refinement_proposed` event; paused `awaiting_refinement` state; two-amendment cap; `/mission accept` / `/mission reject`; `amend_rubric`; amended continuation and audit events.
- Closure path: task evidence shows the current success policy itself is defective -> evaluator proposes a complete replacement and mission pauses -> coordinator relays without authority to edit/apply -> parent user accepts or rejects -> on acceptance Surogates commits the recorded rubric exactly and resumes the mission -> subsequent S1/S3*/S3 operation is governed and judged under the new ultimate success policy; rejection terminates under the held verdict.
- Boundary reachability: rubric refinement is implemented in the ordinary mission evaluator and `/mission` handlers at the frozen ref; it is not a design-only or repository-governance feature.
- Why this is / is not agent-owned: this is not an ordinary tool-call approval. It changes the top-level success policy of the mission organization itself and the implementation deliberately separates proposal, relay and ultimate authority. The parent holds the decisive right, so the state is `P`, not `A`.
- Evidence: [`docs/tasks/index.md`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/docs/tasks/index.md); proposal/application logic in [`surogates/missions/evaluator.py`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/surogates/missions/evaluator.py) and [`surogates/missions/commands.py`](https://github.com/invergent-ai/surogates/blob/4069e5ad736f1b21584543f734c9481193bcde65/surogates/missions/commands.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: initial user prompt/task text alone is not used as S5 evidence, and ordinary tool confirmations remain below S5. The positive claim is specifically the live identity/policy-level rubric-redefinition path with segregated parent authority and return-to-operation closure.

## Recursion

This assessment intentionally fixes recursion at one Surogates-managed Mission. Task-backed worker sessions are its operational S1 units; the shared fan-out board regulates their interference; the strict coordinator regulates current mission commitments; the evaluator challenges completion claims; the mission principal holds ultimate rubric authority. A Surogates installation contains many additional tenant/session/skill/expert/operations surfaces at a higher recursion, but those are not mixed into this mission-level vector.

Research missions remain a subtype of the same mission recursion. Their executors are operational units and their independent held-out gate strengthens S3* evidence. Optimizing the target repository is still the mission's primary operational purpose, not evidence that the mission organization itself has S4.

## Variety and escalation

Local task variety stays with worker S1s until a worker blocks, fails or completes. Fan-out interference is attenuated through board claims/failures and shared verified state. Terminal task evidence wakes the coordinator and the S3* judge; a `needs_revision` verdict returns corrective variety to S3 rather than silently centralizing task execution. The coordinator can spawn/cancel/unblock new commitments; the parent can alter the mission-wide resource ceiling or cascade-stop all workers. When the disturbance is no longer “how do we execute?” but “is the success policy itself valid?”, the judge may escalate a rubric-redefinition proposal to the parent S5 path. The user decision then returns through the same mission state into subsequent operation.

## Evidence gaps

- Structural/static review only; no live model provider, mission or tool environment was executed during this assessment.
- S2 and S3 positive mappings use the documented/implemented Mission fan-out mode. A solo Surogates chat without multiple task workers does not instantiate those same relations.
- S3* independence is strongest when the rubric uses separately produced structured verifier metadata; research mode adds a server-owned held-out re-run that corroborates the anti-self-report design. Application-specific verifier quality still depends on what the mission asks the verifier worker to measure.
- S5=P is intentionally narrow: ordinary product/tool approvals, initial prompts and static policy profiles are not credited. Only the live rubric-redefinition authority path at the mission recursion is used.
- Installation-level expert lifecycle may warrant a separate higher-recursion S4 constructor/parent analysis; it is excluded here to avoid mixing recursion levels.