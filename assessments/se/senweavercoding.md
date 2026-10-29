---
harness_id: senweavercoding
project_name: SenWeaverCoding
repository: https://github.com/senweaver/SenWeaverCoding
review_ref: 8ba81d595ba154f300428dd554d2065b9a268432
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SenWeaverCoding

## Review boundary

- System in focus: the MIT-licensed SenWeaverCoding IDE/CLI agent runtime, model-mediated tool loops, multi-agent delegation and local feedback subsystems at the pinned source revision; not the provider models, external organizations or user's whole development environment.
- Purpose and identity: carry out human-specified software-development work through interactive or headless coding agents, optionally delegating compatible subtasks and integrating tool evidence into subsequent choices.
- Relevant environment: coding requests, editable repositories, tool outcomes, provider errors, conflicting subagent edits, capacity limits, user corrections and execution feedback.
- Standard-distribution boundary: first-party Rust runtime with IDE/Tauri and `sen` CLI entry surfaces; model providers and user-supplied credentials are dependencies rather than harness-owned S5.
- Credited operating / distribution surfaces: `src/agent/agent.rs`, unified agent loop, delegate parallel tool, subagent execution, task graph scheduler, coordination locks, registered runtime and result merge.
- Adjacent first-party surfaces excluded from ownership: UI presentation, static source scanners, documentation claims, stand-alone telemetry, provider infrastructure, user-defined identities and external CI or approval rights.
- First-party modes considered: model-led agent/tool iteration; configured multi-agent task DAG with specialist agents, isolation and integration; optional self-judging/evolution and user-configured web search.
- Recursion level: one human-assigned coding task with a model parent controlling present specialist-agent execution; not an automatically viable wider organization.
- Reviewed revision: `8ba81d595ba154f300428dd554d2065b9a268432`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Rust agent invokes a model/tool loop: it constructs tool-aware conversation context, interprets model-selected calls, executes the selected tool and incorporates the result into later turns. One registered tool, `delegate_parallel`, accepts subtask descriptions/dependencies and dispatches them through the multi-agent runtime. Its agentic workers may run in isolated Git worktrees; worker merges are guarded by a base-workspace lock, and a dirty parent causes merge deferral and branch salvage. The runtime also has shared-resource/region coordination and a capacity-limited task graph. The tool then returns both merged output and per-task failure/degradation metadata, which the parent agent can use for subsequent model control. The optional LLM merger synthesizes worker outputs but is not an independently governed complement to central control. Separately, the evolution judge grades the same assistant's previous output against next-state feedback and writes lessons; this is local performance learning, not prospective environmental S4.

Pinned source evidence:

- [README: IDE, CLI, model/tool agent modes](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/README.md)
- [Agent entry and unified-loop invocation](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/src/agent/agent.rs)
- [Unified model/tool loop](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/src/agent/loop_/unified.rs)
- [Parallel delegation, isolated Git worktrees and merge/failure return](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/src/tools/delegate/parallel.rs)
- [Multi-agent runtime, scheduler, registry and task outcome](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/src/agent/multi_agent_runtime.rs)
- [Shared resource and region lock coordination](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/src/agent/coordination.rs)
- [Delegated result aggregation, failure accounting and optional LLM synthesis](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/src/coordinator/delegation.rs)
- [Supervisor service liveness and restart logic](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/src/agent/supervisor.rs)
- [Next-state reward judge](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/src/evolution/judge.rs)
- [Historical self-reflection and lesson writeback](https://github.com/senweaver/SenWeaverCoding/blob/8ba81d595ba154f300428dd554d2065b9a268432/src/evolution/reflection/reflector.rs)

## Operational model

The user supplies a bounded coding request. A configured provider's model chooses tool actions, receives results and iterates. For parallel tasks the model can call `delegate_parallel` with an explicit DAG and optional agentic workers. The constructor-written runtime enforces limits, orders prerequisites and prevents worker workspace collisions where possible. It collects task success/failure, merges worker outputs and reports degradation to the parent model loop for revised decisions or user escalation. Optional feedback judge/reflection reads past assistant turns and next-state observations to record lessons, without establishing a separate auditor of the parent orchestrator.

## S1 — Operations

- State: A
- Function: model-mediated software development from user request through file/tool operations, testing/observation and subsequent repair or response.
- Disturbance / variety regulated: heterogeneous coding tasks, unexpected tool outputs, compiler/test failures, file contents and changed instructions.
- Decisive decision or feedback right: select next tools or code actions based on previous responses and produce/revise a user-facing task result.
- Decision owner: the active configured model in the first-party agent/unified loop and, when selected, agentic delegated role workers.
- Supporting / enforcement mechanisms: IDE/headless CLI, provider adapters, tool registry, unified loop policy, file/shell/git tools, conversation messages and subagent runtime.
- Closure path: human goal → model chooses actions → first-party tool effects → observed results in model context → next model action, repair, response or bounded stop.
- Why this is / is not agent-owned: the model chooses tool sequence and changes its actions on feedback; the Rust executor supplies capabilities and limits rather than deterministically prescribing all task decisions.
- Evidence: agent entry, unified loop and delegated agentic worker in pinned source links above.
- Basis: reachable model-run source path with real tool effects and returned observations.
- Confidence: medium-high for supported configuration.
- Caveats: outcome quality, model credentials and live execution are not validated by this static source review.
- Boundary reachability: `src/agent/agent.rs` invokes `UnifiedLoop::run`, and `delegate_parallel` is a first-party registered tool callable from the model/tool loop.

## S2 — Coordination

- State: C
- Function: attenuate cross-worker file/edit contention and task-order conflicts during concurrent delegated coding.
- Disturbance / variety regulated: agentic subagents modifying shared files, simultaneous Git updates, dirty parent workspace, dependency inversions and excessive parallelism.
- Decisive decision or feedback right: isolate workers in Git worktrees, serialize base-workspace merges, preserve branches when parent is dirty, and limit/sequence DAG execution.
- Decision owner: constructor-specified scheduler, file/region lock manager, worktree and merge guards, not an independently policy-setting coordination agent.
- Supporting / enforcement mechanisms: task dependency graph, subagent limiter, `base_merge_lock`, named worktree creation, commit/merge and salvage checks, region and buffer locks.
- Closure path: concurrent worker requests → graph/limit checks and separate workspaces → bounded parallel execution → serialized guarded merge or salvaged output → merged status/failure metadata available to parent and subsequent workers.
- Why this is / is not agent-owned: S2 handles a concrete interference relation between distinct active S1 workers; guards and conditional concurrency are source-defined rules rather than model-owned autonomous negotiation.
- Distinct S1 units: separately instantiated agentic model workers with their own task prompt, provider invocation, allowed tools and working directory.
- Inter-S1 disturbance: overlapping edits or merge attempts contaminate the same codebase and can invalidate siblings' results.
- Attenuating coordination relation: each worker gets an isolated named worktree where available; base-workspace merge is lock-serialized, dirty parents defer merging, and scheduler capacity/dependencies govern dispatch.
- Feedback into subsequent S1 behaviour: merged output exposes per-task successes/failures, degraded fallback and merge notes; failed/dirty merges preserve branches and report conditions to the parent, altering next task execution.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: worktree isolation and the per-base exclusive merge lock directly suppress simultaneous file-state interference between multiple independently coding S1s.
- Evidence: `src/tools/delegate/parallel.rs` worktree/merge/return path, `src/agent/coordination.rs`, multi-agent runtime and merge module (links above).
- Basis: runtime code with concrete conflict attenuation, not just agent messaging or a parallelism claim.
- Confidence: medium-high.
- Caveats: when worktree creation fails workers can use a shared workspace under file locks; implementation does not prove freedom from every possible merge conflict.
- Boundary reachability: model-accessible `delegate_parallel` executes the scheduler/worktree code and returns merge/failure metadata to the calling model.

## S3 — Inside-and-now control

- State: A
- Function: model parent makes present whole-task control decisions using tool results, delegated execution outcomes and failures to choose next steps.
- Disturbance / variety regulated: changing task feasibility, partial subagent failures, unavailable capabilities/providers, ambiguous merged results, tool timeouts and integration failures.
- Decisive decision or feedback right: decompose or pursue a task directly, select/delegate work and merge style, inspect aggregate success/degraded status, retry or change approach before final user response.
- Decision owner: top-level model agent operating the unified loop and issuing `delegate_parallel` tool calls; deterministic scheduling/merging supports its decisions.
- Supporting / enforcement mechanisms: conversation and tool state, task graph, registry/blackboard, `MergedOutput` failures, optional LLM merge, bounded tool limits and cancellation.
- Closure path: parent user goal → top-level model selects task execution/delegation → scheduler runs subordinate S1 agents → merged outputs/failed-task metadata return as a tool result → parent model re-evaluates current work, acts or ends.
- Why this is / is not agent-owned: the top-level model's future tool selections depend on feedback about the task as a whole, whereas graph dispatch/health supervision alone are deterministic support.
- Whole-system current view: aggregate subtask success/degradation, merge results/failures, tool observations and current conversation/workspace state visible to the parent for the assigned coding task.
- Current-control decision scope: whether to invoke subagents, which tasks/dependencies/merge mode to request, and whether the present task needs more actions or is ready for a response.
- Evidence: `src/agent/agent.rs`, `src/agent/loop_/unified.rs`, `src/tools/delegate/parallel.rs` lines covering task submission/result serialization, `src/coordinator/delegation.rs`.
- Basis: model ownership of current task orchestration with closed worker-result return route.
- Confidence: medium.
- Caveats: this is task-scoped S3, not ownership of external product release, organization portfolio, user permissions or a guaranteed multi-agent deployment.
- Boundary reachability: the registered delegation tool returns serialized merged/failure metadata to the same model-aware unified loop that determines subsequent tool calls.

## S3* — Complementary audit

- State: —
- Function: internal judges and verification provide task quality signals, but no independently bounded challenger of the parent S3 decision is established.
- Disturbance / variety regulated: incorrect answers, weak tool outcomes, next-turn user corrections and possible integration faults.
- Decisive decision or feedback right: separately challenge an S3 completion claim using independently held complementary evidence and route a finding into its corrective authority.
- Decision owner: optional provider-backed next-state reward judge, LLM candidate merger and verification pipeline operate under the same runtime/configuration; independent S3* decision owner is not demonstrated.
- Supporting / enforcement mechanisms: evolution reward queue, previous/next conversation state, self-reflection lessons, verification pipeline and optional LLM result synthesis.
- Closure path: local task result → internal judge/reflection/reward or optional merge → assistant learning/report; no demonstrated blind independent S3-audit scope and binding corrective return.
- Why this is / is not agent-owned: using a second model call as a score/judge is not sufficient evidence of complementary governance independence; this is internal evaluation of the same task or output.
- Evidence: `src/evolution/judge.rs`, reflection worker, `src/coordinator/delegation.rs` and `src/agent/verification/pipeline.rs`.
- Basis: independence-and-return-path test; ordinary self-check and reward are not S3*.
- Confidence: medium-high for scoped absence.
- Caveats: an external reviewer could be installed by a user, but that independent institution is not part of the reviewed first-party boundary.

### Absence scope

- Surfaces inspected: model judge and reward queue, historical reflection, verification pipeline, LLM candidate synthesis, supervisor and agent coordination.
- Plausible first-party paths checked: `LlmJudge` merge as an audit role, reward judge as outside S3*, ordinary verification as independent challenge and deterministic supervisor as watchdog.
- Why no material first-party path remains: observed checks evaluate/merge within the same task control or local quality loop; source does not show an independent complementary auditor with a distinct evidence mandate that can challenge central current-control claims and force corrective S3 action.

## S4 — Outside-and-then intelligence

- State: —
- Function: optional self-reflection/evolution learns from historical turns, but does not demonstrate ongoing prospective external-environment sensing with future capability choices for the system.
- Disturbance / variety regulated: repeated assistant mistakes, weak tool outcomes, user corrections and deteriorating local work patterns.
- Decisive decision or feedback right: scan the outside future environment, select strategic adaptations beyond the present task, and return actionable options into current control.
- Decision owner: internal evolution/reflection agents and constructor writeback controls for local lessons; no separately evidenced prospective S4 decision-maker.
- Supporting / enforcement mechanisms: next-state reward judge, reflection worker, lesson writeback, history/distiller and optional web-search tool for ordinary user tasks.
- Closure path: past answer and next-turn outcome → reward/lesson extraction → locally stored guidance; no traced external future signals → strategic option → S3 adaptation loop.
- Why this is / is not agent-owned: model-driven past-performance reflection is real but does not on its own satisfy outward-looking future intelligence; ad hoc browser/search tools are not proof of a continuing S4 mandate.
- Evidence: `src/evolution/judge.rs`, `src/evolution/reflection/reflector.rs`, `src/evolution/distiller.rs`, web-search registration in `src/agent/agent.rs`.
- Basis: external-future versus retrospective internal-learning distinction.
- Confidence: medium-high.
- Caveats: a specific user could direct a research task, but that is S1 work within the supplied goal and not systematic own-system S4.

### Absence scope

- Surfaces inspected: evolution judge, reflection, distillation, lesson writeback, agent web-search capability and multi-agent role pipeline.
- Plausible first-party paths checked: reflection as foresight, user-directed web search as strategic sensing, accumulated rewards as long-horizon adaptation.
- Why no material first-party path remains: these paths concern local historical task quality or reactive user requests, without first-party prospective environment monitoring and a future-oriented system adaptation decision return.

## S5 — Policy and identity

- State: —
- Function: configuration and agent operating modes specify limits but do not grant authority to redefine legitimate overall system purpose or ultimate policy conflicts.
- Disturbance / variety regulated: provider permissions, credentials, tool restrictions, risk/approval constraints, model choices and user intent.
- Decisive decision or feedback right: decide the system's binding identity and top-level normative priorities when objectives conflict, with legitimate authority over the other functions.
- Decision owner: external user, repository maintainers and configured permissions/providers set the top-level purpose and rules; the runtime supplies enforcement.
- Supporting / enforcement mechanisms: user settings, tool allowlists, configured model/provider, safety boundaries, agent mode and runtime guardrails.
- Closure path: external user policy/request → configured restrictions → model executes bounded task or stops; no first-party final constitutional policy adjudication.
- Why this is / is not agent-owned: model discretion over coding steps and optional lesson generation is not independent legitimate authority to revise the harness's identity or user mandate.
- Evidence: README modes, `src/agent/agent.rs` configuration/tool routing, delegate tool allowed-tool/max-iteration controls.
- Basis: ultimate policy-right ownership boundary.
- Confidence: high for scoped absence.
- Caveats: S5 may exist in a larger human-led enterprise, but is not inherited into this runtime assessment.

### Absence scope

- Surfaces inspected: task/mode configuration, model/provider dependencies, delegation limits, runtime health supervision and self-reflection writeback.
- Plausible first-party paths checked: role orchestration as S5, auto-lessons as identity revision, safety/approval settings as normative decision making.
- Why no material first-party path remains: all identified decisions are bounded by externally selected goals/configuration and are operational rather than ultimate policy authority.

## Recursion

The top-level coding agent manages the current user assignment and can deploy separate task S1 subagents. Task-specific concurrency management attenuates conflicts across those subagents. The top-level model reads their collective feedback and controls subsequent current work. No additional full viable-system recursion level, independent S3* or organization-level S5 is inferred from the number of workers.

## Variety and escalation

Model/tool iteration regulates changing coding circumstances. Conditional worktree isolation, a serial base-merge lock, DAG scheduling and subagent ceilings attenuate coordination variety. The parent receives structured failures/degraded-state reports, can retry/replan and ultimately answer or escalate to the user. Optional reward/self-reflection supplies retrospective improvements without claiming independent audit or future-environment intelligence.

## Evidence gaps

- Static pinned-source review only: no model-provider E2E run, credential use, live concurrent file edit, timed benchmark or production-grade success guarantee.
- Agentic delegation requires configured runtime/agents/tools and can degrade to non-agentic or shared-workspace fallback; the assessment credits the traceable supported route, not every installation.
- The LLM merger and evolution judge reuse local runtime inputs and do not establish S3* independence.
- Prospective external-sensing S4 and ultimate normative S5 remain unproven at this revision.

## Assessment summary

**Proposed disposition: `included`.** SenWeaverCoding has source-backed model-led coding operations (S1=A), constructor-enforced cross-agent edit/merge coordination (S2=C) and task-level model-owned current orchestration over integrated subagent results (S3=A). Internal judges and self-reflection do not establish separate complementary audit S3* or outside-and-then S4, while ultimate policy authority remains external. Vector: **A · C · A · — · — · —**.
