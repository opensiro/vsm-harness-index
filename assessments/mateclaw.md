---
harness_id: mateclaw
project_name: MateClaw
repository: https://github.com/mateaix/mateclaw
review_ref: 5c67af85fc85060a8518fa25ca66a7c19f1e11ab
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: A(P)
autonomy_s5: —
---

# MateClaw

## Review boundary

- System in focus: one first-party MateClaw installation at pinned revision `5c67af85fc85060a8518fa25ca66a7c19f1e11ab`, including the native StateGraph employee runtime, Agent Teams / Team Runs shared-board machinery, persistent goals, first-party skills/evolution services, workspace/tool-policy enforcement, and first-party operator surfaces that close supported parent-governed modes.
- Purpose and identity: provide persistent digital employees and teams that autonomously execute tool-mediated work, coordinate and supervise shared project delivery, recover long-running work, and adapt reusable capability from repeated user demand while remaining governable through workspace/operator controls.
- Relevant environment: user requests and recurring request patterns; local/workspace files and processes; external web/API/MCP/A2A/tool state; model-provider responses; team-member outputs, blockers, failures and deliverables; skill/runtime capability; workspace administrators and human approval decisions.
- Standard-distribution boundary: the shipped MateClaw server/UI/runtime and its documented native StateGraph, Team Run, skill-evolution and operator modes at the frozen revision. External model providers, MCP/A2A peers, OS/container/browser substrates and external ACP employees are environment/backends. DeepSeek Harness (DSH) is treated as a managed external runtime backend where it owns the inner reasoning loop; MateClaw receives credit only for first-party lifecycle/policy/tool/workspace closure that remains outside that external loop.
- Credited operating / distribution surfaces: `mateclaw-server/src/main/java/vip/mate/agent/graph/StateGraphReActAgent.java`; native graph nodes/builder under `vip/mate/agent/`; Team Run services/tools/controllers under `vip/mate/team/`; persistent goal scheduling/runtime; first-party skill routine/reflection/curator services under `vip/mate/skill/`; workspace/Tool Guard/approval integration; and first-party admin APIs/UI that operate those runtime functions.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests, release/governance activity, docs as intent where no runtime path exists, benchmark/evaluation-only code, and future roadmap claims. DSH/Cordis internals are not imported as MateClaw organizational actors merely because MateClaw manages their subprocess/session lifecycle.
- First-party operating / deployment modes considered: native ReAct StateGraph employees; native Plan-Execute employees; Team Runs with autonomous lead/member agents; persistent-goal bounded segments; unattended recurring-request skill promotion when enabled; operator-governed Team/skill-routine controls; and DSH only to the extent MateClaw itself owns the surrounding closure.
- Recursion level: one MateClaw installation as the system-in-focus. Team member employee runs are S1 units; a team lead can own S2/S3 decisions for a Team Run; operator/admin surfaces are Parent at this recursion. An individual employee can itself contain a ReAct/Plan-Execute loop, but that lower recursion is not used to inflate metasystem functions of the installation.
- Reviewed revision: `5c67af85fc85060a8518fa25ca66a7c19f1e11ab`.
- Historical identity: the source export referenced historical `matevip/mateclaw`; current GitHub canonical identity is `mateaix/mateclaw`, stable repository id `1201201482`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

MateClaw ships a native StateGraph runtime whose ReAct implementation explicitly owns the Thought → Action → Observation loop. `StateGraphReActAgent` builds fresh graph state per invocation, executes a compiled graph, persists structured reasoning/tool events and returns the graph's final answer. The corresponding reasoning/action nodes expose tools and feed observations back into the next model decision. Plan-Execute is another first-party mode. This native path is sufficient for S1 without borrowing autonomy from DSH. At the reviewed revision DSH is a managed JSON-RPC subprocess runtime; MateClaw controls provider/session lifecycle and host-side policy/tool mediation, but DSH owns its own internal context and reasoning loop, so those internals are excluded from ownership attribution.

Agent Teams add a materially stronger organizational layer. A team has one lead and multiple member/reviewer employees around a shared board. The lead is not merely named "manager": `TeamContextBuilder` gives it an explicit orchestration playbook and injects a live snapshot of every non-terminal team task on every turn. The lead creates a sealed Team Run, assigns members, sets dependencies and priorities, reviews returned results, receives blocker/failure announcements in a fresh turn, and can retry or cancel work. Member task runs are separate full agent graphs. `TeamTasksTool` role-gates these decision rights so lead actions are distinct from member execution rights.

The board/runtime also has deterministic attenuation machinery. Execution leases and heartbeats prevent an already-running task from being re-dispatched after transient scheduler/restart ambiguity; the documentation names the concrete failure mode as two task instances running simultaneously and overwriting each other. Conditional task state transitions, dependency release and one-task-per-member execution further enforce the selected coordination. These deterministic mechanisms do not themselves own the organizational decision; for the agent-owned S2 path the lead receives the live in-flight board specifically so it does not duplicate ongoing work and can revise/cancel/retry assignments when blockers/results return.

MateClaw also ships an autonomous capability-adaptation path. Recurring-request mining clusters opening user requests for an employee across sessions/days. Qualified candidates are promoted unattended when enabled. `SkillRoutinePromoter` gives plural conversation evidence to a model, has that model synthesize a reusable skill, persists it through the first-party skill-management path and stamps the owning employee so the skill is auto-bound and reachable on that employee's next turn. An operator can independently inspect candidates and dismiss/reopen or call `promoteNow`, bypassing recurrence gates; this creates a distinct parent-governed S4 mode over the same adaptation path.

## Operational model

In native employee operation, a user request enters a first-party graph. The active employee decides whether and how to call tools; MateClaw executes/gates the call, records the observation, and returns it into the graph until a final answer or bounded termination condition is reached. Persistent goals can break long work into bounded recoverable segments, but persistence/restart machinery is treated as reliability support rather than a metasystem function by itself.

In Team Run operation, the lead sees the team roster plus a current board snapshot, decomposes the objective and assigns tasks to member S1s. The dispatcher starts independent member conversations/graphs. Dependencies, leases and task ownership keep execution coherent. Member progress/results/blockers mutate the board and are announced back to the lead. That feedback gives the lead a new current view from which it can retry, cancel, add/re-dispatch work or synthesize completion. An operator can instead intervene through first-party admin Team APIs/UI: inspect the same run/task state, create tasks, approve/reject outputs, provide worker feedback, retry/cancel tasks or cancel the whole run.

In skill-routine adaptation mode, recent user-demand patterns are mined per employee. Once a recurrence gate is met, the unattended pass invokes a synthesis model over several representative conversations and creates a reusable skill; the skill is auto-bound to the source employee. In the parent mode, an operator views the inferred candidate and can suppress it or explicitly promote it early. Both modes return the adaptation into later operational capability.

## S1 — Operations

- State: A
- Function: autonomously transform task/environment state through an iterative reasoning → action/tool → observation loop and continue until a bounded task outcome is produced.
- Disturbance / variety regulated: heterogeneous user goals, changing workspace/file/process/web/API/tool state, model/tool errors, intermediate observations and long-running task state that require context-sensitive next actions.
- Decisive decision or feedback right: choose the next tool/action from current task context and observations, decide whether another operational step is needed, and terminate or continue the run accordingly.
- Decision owner: the active native MateClaw employee agent in ReAct or Plan-Execute mode; Team member conversations instantiate the same class of autonomous employee operation for assigned work.
- Supporting / enforcement mechanisms: compiled StateGraph execution, `ReasoningNode`/Action/Observation nodes, Tool Guard, loop/iteration limits, conversation persistence, context budgeting, stream tracking, workspace adapters and persistent-goal scheduling/recovery.
- Closure path: user/assigned task + current state → employee chooses action/tool → MateClaw executes/gates action → observation/result enters graph state → employee chooses next action or final answer.
- Boundary reachability: native StateGraph ReAct/Plan-Execute employees are standard documented runtime modes and Team member tasks execute full first-party agent graphs; S1 therefore does not depend on DSH internals, tests or repository-development actors.
- Why this is / is not agent-owned: if the model-driven employee is removed while graph transport, Tool Guard and persistence remain, the system no longer makes context-sensitive operational choices. Deterministic graph/runtime machinery executes and bounds the choices rather than replacing them.
- Evidence: [`StateGraphReActAgent.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/agent/graph/StateGraphReActAgent.java), [`ReasoningNode.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/agent/graph/node/ReasoningNode.java), [`README.md`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/README.md).
- Basis: structural
- Confidence: high
- Caveats: external model inference is compute substrate. DSH is an external managed inner runtime in its mode, so undocumented DSH autonomy is not imported; the positive S1 claim is established independently by MateClaw's native runtime.

## S2 — Coordination

- State: A
- Function: attenuate destructive overlap and coordination failure among concurrent team-member S1 runs while preserving member-local execution autonomy.
- Disturbance / variety regulated: duplicate/in-flight work and accidental double execution can cause two task instances to perform/overwrite the same work; concurrent member work also creates dependency/blocker states that must be reconciled without each worker independently guessing team state.
- Decisive decision or feedback right: based on a live board and returned blocker/result feedback, decide whether work should be created/assigned, withheld as already in flight, retried, cancelled or followed by newly coordinated work.
- Decision owner: the autonomous Team lead agent for the discretionary coordination response. Deterministic leases, state transitions and the dispatcher enforce exclusivity/dependencies after those task/coordination decisions.
- Supporting / enforcement mechanisms: live per-turn board snapshot, role-gated `team_tasks`, task ownership/dependencies, one-task-per-member execution, 60-minute execution leases with heartbeat, stale detection, conditional DB transitions, dispatch requests and cancellation propagation.
- Closure path: current member/task state plus blocker/result events → board snapshot/announcement reaches lead → lead chooses create/avoid-duplicate/retry/cancel/follow-up coordination → board changes → dispatcher/lease machinery changes subsequent member execution.
- Distinct S1 units: separate member employee conversations, each running its own full agent graph on assigned team tasks; multiple members may execute in parallel under one Team Run.
- Inter-S1 disturbance: the shipped documentation and context builder explicitly guard against duplicate in-flight work; the execution hardening text identifies the concrete failure mode of a task being re-dispatched while still running so two instances overwrite each other. Dependency/blocker information also creates real coordination requirements among simultaneously active member units.
- Attenuating coordination relation: the lead receives a live board specifically to avoid duplicate task creation and owns retry/cancel/follow-up choices; execution leases and dependency gates then enforce single ownership and ordering where required.
- Feedback into subsequent S1 behaviour: lead `team_tasks` decisions persist to the board, trigger/stop dispatch, release or withhold dependent tasks, interrupt a running member on cancel, and therefore change which member S1 runs next and under what task context.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive witness is not the board or delegation alone; it is tied to an explicit destructive-interference mode (duplicate concurrent execution/overwriting and duplicate in-flight work), a coordination response using current team state, and a return path that prevents/revises subsequent S1 execution.
- Boundary reachability: Team Runs, the lead playbook/live snapshot, `team_tasks`, leases and dispatcher are shipped first-party standard-distribution features documented since 2.1.0 and present at the frozen revision.
- Why this is / is not agent-owned: hard leases can prevent a second executor but do not own the organizational coordination choice. The autonomous lead does: it is instructed and enabled to inspect current in-flight work, decide assignments/retries/cancellation/follow-ups, and receives blocker/results feedback. Removing the lead leaves enforcement machinery but removes discretionary cross-member coordination.
- Evidence: [`teams.md`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/resources/docs/en/teams.md), [`TeamContextBuilder.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/team/service/TeamContextBuilder.java), [`TeamTasksTool.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/team/tool/TeamTasksTool.java).
- Basis: structural
- Confidence: high
- Caveats: deterministic leases are credited as attenuation/enforcement, not autonomous ownership. Generic dependency ordering alone would not satisfy S2; the classification relies on the explicit duplicate/interference witness plus agent-owned live coordination.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain current cohesion of a Team Run through a whole-team view and authority to assign commitments, intervene on blocked/failed/in-review work, stop work, retry it and drive the run toward one coherent outcome.
- Disturbance / variety regulated: changing current task commitments across members, failed/stale/blocked tasks, duplicate/in-flight work, human-review holds, incomplete deliverables and returned results that can invalidate the original task plan.
- Decisive decision or feedback right: choose current task decomposition/assignees/dependencies/priorities, review settled results, decide retry/cancel/follow-up work and determine when the run can move toward final synthesis; in the parent mode an admin can create work, approve/reject, provide worker feedback, retry/cancel tasks or cancel a run.
- Decision owner: Base mode — the autonomous Team lead agent. Parent mode — a workspace admin/operator using first-party Teams APIs/UI. Dispatcher/state-machine/lease code enforces either owner's returned decisions.
- Supporting / enforcement mechanisms: live per-turn board injection, Team Run projection/state machine, role-gated `team_tasks`, worker result/blocker announcements, task leases/heartbeats, dispatch service, task/run cancellation, worker interruption, admin Team Run/Team Task endpoints and SSE/current-state views.
- Closure path: whole-run current board + member results/blockers/failures → lead or parent evaluates current commitments → create/retry/cancel/approve/reject/feedback decision → board/run state mutates and dispatcher/worker session changes → subsequent current operation reflects the intervention.
- Whole-system current view: the lead receives the active board snapshot every turn and can query full task detail; Team Run ties objective, task DAG, worker conversations, progress, events, approvals and deliverables under one `runId`. The operator sees the same run/task projection and timelines through Teams APIs/UI.
- Current-control decision scope: task commitments and assignees, dependencies and priority, retries/cancellation, worker interruption, review/approval state, supplemental worker feedback and run cancellation — decisions over current shared work rather than merely selecting one helper for one subtask.
- Boundary reachability: autonomous Team lead operation and the operator Teams control surface are both first-party supported runtime modes at the frozen revision, with service/API paths that directly mutate active runs/tasks.
- Why this is / is not agent-owned: in the base mode the lead receives live whole-team state and makes the discretionary intervention/commitment choices; deterministic state/dispatch code only enforces them. A separately supported admin path can own those same current-control decisions, hence the parent modifier rather than replacing the autonomous base state.
- Evidence: [`TeamContextBuilder.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/team/service/TeamContextBuilder.java), [`TeamTasksTool.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/team/tool/TeamTasksTool.java), [`TeamController.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/team/controller/TeamController.java), [`TeamRunController.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/team/controller/TeamRunController.java), [`teams.md`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/resources/docs/en/teams.md).
- Basis: structural
- Confidence: high
- Caveats: initial goal decomposition by itself would be below S3. The positive classification depends on live whole-run feedback plus later intervention rights. Human approval of a single tool call alone is not the parent witness; the parent witness is the Teams surface's whole-run current view plus task/run intervention closure.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | autonomous Team lead agent | new team objective plus live board/result/blocker/failure feedback | lead creates/assigns/retries/cancels/follows up through `team_tasks`; persisted board changes dispatch/interruption and later member work | `TeamContextBuilder`, `TeamTasksTool`, Team Run docs |
| Parent (`P`) | workspace admin/operator | operator review of live Team Run/task state, approval need, worker issue or desired intervention | Teams API/UI creates work, approves/rejects, gives feedback, retries/cancels tasks or cancels run; service mutates state and dispatcher/worker execution changes | `TeamController`, `TeamRunController`, Team Run docs |

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established for current Team/employee operational claims.
- Disturbance / variety regulated: MateClaw records task timelines, worker transcripts, reasoning trajectories, source evidence, runtime events and admin-visible live state, but these primarily expose the ordinary execution/reporting path rather than a separate audit channel that independently challenges it and returns an audit finding into S3.
- Decisive decision or feedback right: no first-party autonomous audit actor is shown controlling a complementary access path and issuing an independent current-operation finding that S3 then acts on.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: Team task event/audit tables, full worker-conversation drill-down, runtime live console, reasoning/trajectory persistence, reviewer role metadata, source-evidence tracking and human approval gates.
- Closure path: normal task results/progress/blockers and timelines can inform the lead/operator, but they arise from the same operational/reporting chain; human review can accept/reject a gated task but is an ordinary parent control path, not a published S3* autonomous complementary-audit topology.
- Why this is / is not agent-owned: naming a reviewer role or exposing complete traces does not create independent audit judgment. No reviewed shipped mode separates the claim, ordinary reporting path, materially independent access path, auditor and return-to-S3 action as required by the Profile.
- Evidence: [`teams.md`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/resources/docs/en/teams.md), [`TeamController.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/team/controller/TeamController.java), [`StateGraphReActAgent.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/agent/graph/StateGraphReActAgent.java).
- Basis: structural
- Confidence: high
- Caveats: human operators can use raw transcripts/timelines for manual forensic review; Methodology 0.3.x does not publish a parent modifier for S3*, and no autonomous complementary audit closure is established here.

### Absence scope

- Surfaces inspected: Team reviewer role and task approval; Team task event/audit timeline; worker transcript drill-down; live runtime console; graph reasoning/trajectory persistence; source-evidence ledger paths; worker intervention/feedback; tests/docs for audit/review/evidence terminology.
- Plausible first-party paths checked: reviewer as auditor, lead reviewing member result, admin task approval, task timeline as audit, runtime console as audit, source/citation evidence as independent ground truth and replayed worker transcript as complementary access.
- Why no material first-party path remains: the reviewed paths are ordinary reporting/visibility or parent operational approval. None supplies a first-party autonomous auditor with materially independent access to current operational reality and a distinct finding-return path into S3.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: detect recurring external user demand across sessions, develop a reusable future capability for that pattern, persist it as a skill and return it into the source employee's later operating capability.
- Disturbance / variety regulated: repeated user requests over time reveal a persistent demand pattern that the current employee capability does not yet encode as a reusable routine; thin/noisy patterns must be distinguished from stable recurrence before changing capability.
- Decisive decision or feedback right: decide that a recurring demand pattern should become a reusable skill and select the concrete skill design/content synthesized from several representative conversations. In the parent mode the operator can dismiss/reopen a candidate or deliberately promote it early, overriding unattended recurrence thresholds.
- Decision owner: Base mode — the unattended routine pipeline, with a first-party model synthesizer choosing the concrete reusable skill from plural evidence after first-party recurrence qualification. Parent mode — the workspace operator decides whether an observed candidate should be suppressed/reopened or promoted now; synthesis/persistence then implements that returned adaptation decision.
- Supporting / enforcement mechanisms: recurring-request miner/candidate store, occurrence/distinct-day gates, scheduled routine job, transcript/evidence collection with workspace isolation and secret redaction, synthesis model, `SkillManageTool` security/validation, skill origin/provenance, auto-binding to source employee and curator/snapshot controls.
- Closure path: repeated user requests across sessions → recurrence candidate/qualification → model synthesizes reusable skill (or operator chooses early promotion) → first-party skill management persists it → source employee is auto-bound → new capability is reachable on the employee's next/later turns.
- External distinction: plural user requests observed across separate conversations/days provide an environment-facing demand signal; the promoter intentionally uses several occurrences rather than one internal trace so it can learn the class of recurring request.
- Future / prospective distinction: recurrence thresholds identify work likely to return and therefore worth encoding as future reusable capability rather than solving only the current request; operator review can make the same forward-looking judgment before the automatic threshold.
- Adaptation option generated: a model-synthesized named `SKILL.md` capability based on representative requests/transcripts, persisted with routine origin and owning-employee attribution.
- Path back into current capability / S3: `SkillRoutinePromoter` writes through `SkillManageTool`, stamps `ChatOrigin` with the source employee and auto-binds the resulting skill; the code explicitly states the routine becomes reachable on that employee's very next turn.
- Boundary reachability: recurring-request mining/promotion, admin routine decisions and first-party skill loading/binding are shipped 2.1.0+ standard-distribution services at the frozen revision; the positive path is not a roadmap-only or test-only optimizer.
- Why this is / is not agent-owned: in unattended mode the model-backed promoter owns the substantive option design after the first-party detector selects a stable external pattern; deterministic thresholds schedule when that discretion is invoked. The distinct operator mode owns whether a candidate should be adapted now/suppressed, with a direct return into the same capability pipeline.
- Evidence: [`SkillRoutinePromoter.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/skill/routine/SkillRoutinePromoter.java), [`SkillRoutineService.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/skill/routine/SkillRoutineService.java), [`skills.md`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/resources/docs/en/skills.md).
- Basis: structural
- Confidence: high
- Caveats: LESSONS.md, reflection and memory alone would not establish S4. The classification rests on the stronger cross-session recurring-demand → synthesis → persisted/auto-bound capability loop. The routine feature is opt-in by configuration; reachability in a supported first-party mode is sufficient even when the secure default leaves autonomous writes disabled until enabled.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | first-party unattended routine pipeline with model-backed skill synthesizer | recurrence gates met across repeated user requests/days while routine mode is enabled | synthesized skill persists through `skill_manage`, is attributed/auto-bound to source employee and is usable on later turns | `SkillRoutinePromoter`, `skills.md` |
| Parent (`P`) | workspace operator/admin | operator reviews mined candidate and chooses promote-now, dismiss or reopen rather than waiting for unattended thresholds | `promoteNow` bypasses gates into the same synthesis/persist/auto-bind path; dismiss/reopen governs whether later sweeps may act | `SkillRoutineService`, `SkillRoutinePromoter`, `skills.md` |

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy closure is established for the MateClaw installation at the reviewed recursion.
- Disturbance / variety regulated: employee Role/Goal/Backstory, RBAC, Tool Guard, workspace boundaries, human approvals, team roles and skill-governance settings constrain or configure operation, but no reviewed supported path reconstructs an identity/ultimate-policy issue being surfaced to legitimate ultimate authority and returned as the authoritative policy decision governing the installation.
- Decisive decision or feedback right: no S5-specific runtime decision right is established. Admins can edit identities/configuration and approve actions; agents can even author new specialized employees, but these are configuration/organizational-construction rights rather than an evidenced ultimate-policy closure for the system-in-focus.
- Decision owner: none established for S5 under the active publication boundary.
- Supporting / enforcement mechanisms: employee system prompts/Role/Goal/Backstory, workspace RBAC, Tool Guard, approval gates, team role assignment, security policies, skill origin/adopt/release settings and `AgentAuthoringTool` employee creation.
- Closure path: ordinary configuration, approvals and authoring can change later operation, but the required identity-policy issue → legitimate ultimate authority → authoritative decision → return-to-operation chain is not evidenced as a first-party S5 mode.
- Why this is / is not agent-owned: an agent creating a new employee does not make that agent the ultimate authority for MateClaw's identity; an admin editing Role/Goal/Backstory does not by itself establish the Profile's S5 escalation/closure. Enforcement of security/policy text likewise remains below S5 without that decision path.
- Evidence: [`README.md`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/README.md), [`AgentAuthoringTool.java`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/java/vip/mate/agent/AgentAuthoringTool.java), [`teams.md`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/resources/docs/en/teams.md), [`skills.md`](https://github.com/mateaix/mateclaw/blob/5c67af85fc85060a8518fa25ca66a7c19f1e11ab/mateclaw-server/src/main/resources/docs/en/skills.md).
- Basis: structural
- Confidence: high
- Caveats: MateClaw has substantial parent governance and stable employee identity metadata. The negative classification is intentionally narrow: those facts are not promoted to S5 without an identity/ultimate-policy issue and authoritative return loop at the declared recursion.

### Absence scope

- Surfaces inspected: employee Role/Goal/Backstory and native prompt identity; AgentAuthoringTool; workspace RBAC; Tool Guard; approval flows; team roles/reviewer; persistent goals; skill origin/adopt/release/curator governance; admin/runtime configuration; DSH runtime policy boundary.
- Plausible first-party paths checked: human edit of employee identity as S5, Tool Guard/approval as policy authority, team lead/admin governance as S5, persistent goal as identity, skill governance handover as identity policy, and autonomous employee creation as internal S5.
- Why no material first-party path remains: each inspected path governs ordinary operations, access, capability ownership, task commitments or creation of subordinate actors. None demonstrates an identity/ultimate-policy matter for the whole MateClaw recursion reaching ultimate authority and returning as the governing decision.

## Recursion, variety, escalation, and evidence gaps

- Team member runs are genuine autonomous S1 units, but a spawned/delegated employee is not automatically treated as a recursively viable full VSM system. This assessment uses them as operations at the MateClaw installation/team recursion.
- The same Team lead can perform distinct S2 and S3 functions: S2 concerns preventing/repairing interference among member operations; S3 concerns whole-run current commitments, resource/task allocation and intervention. The same actor does not collapse those functions when the disturbance and decision rights are separately reconstructed.
- DSH is explicitly boundary-limited. MateClaw can manage the DSH subprocess/runtime and retain host policy/tool/workspace controls, but DSH/Cordis-owned inner reasoning, compaction or context behavior is not counted as MateClaw autonomous ownership.
- Human task approvals and worker-tool approvals are operational current control and contribute to the parent S3 mode; they are not S5 merely because the human has final say over a sensitive action.
- Skill reflection/LESSONS are not used as the S4 proof. The stronger routine path supplies external recurrence evidence, future capability choice and auto-binding closure.

## Summary

MateClaw is a high-function autonomous organizational harness at the frozen revision. Native StateGraph employees establish S1. Agent Teams establish an autonomous coordination layer around explicit destructive-overlap/duplicate-work disturbances and a lead-owned whole-run current-control function, with a distinct parent Teams control mode. The shipped recurring-request pipeline closes autonomous and parent-governed future-capability adaptation. Audit/observability remains ordinary reporting rather than S3*, and substantial security/identity configuration does not by itself close S5. Final classification: **`A A A(P) — A(P) —`**.
