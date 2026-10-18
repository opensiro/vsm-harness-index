---
harness_id: djcode
project_name: DJcode
repository: https://github.com/darshjme/djcode
review_ref: d915b89db1b04cca88c2a495de355e4917a34b1a
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# DJcode

## Review boundary

- System in focus: the first-party DJcode 4.4.0 local coding-agent distribution at frozen revision `d915b89db1b04cca88c2a495de355e4917a34b1a`, including the main Operator model/tool loop, built-in specialist registry and model-callable `spawn_agent`, specialist AgentRunner/AgentExecutor loops, ShadowOrchestrator/ParallelCoordinator, ContextBus, bundled DAF/DDAL adapter, tool/workflow dispatch, local sessions/memory, Project Studio, scheduler, completion checks and directly owned terminal/TUI surfaces.
- Purpose and identity: perform local software-engineering work with a primary model-backed coding agent and optional first-party specialist/reviewer agents, workflows and persistent project/session context.
- Relevant environment: the local working tree, shell/Git state, user task, selected model/provider, tool/approval outcomes, specialist results, workflow state, persisted memories/sessions and explicitly configured browser/computer/MCP extensions.
- Standard-distribution boundary: DJcode's shipped Python runtime and bundled `src/djcode/daf_engine` adapter are inside. External model servers/providers, the optional external Vyasa fleet, the separate upstream DAF and DarshJDB repositories, target project code and host OS are dependencies/environment and do not donate VSM ownership.
- Credited operating / distribution surfaces: `agents/operator.py`; `tools/agent_spawn.py`; `agents/registry.py`; `agents/executor.py`; `agents/parallel.py`; `orchestrator/engine.py`; `orchestrator/context_bus.py`; `workflow.py`; provider tool schema; tool dispatch; session/memory/project-studio and TUI/REPL command wiring.
- Adjacent first-party surfaces excluded from ownership: tests and release validation; managed-update/release helpers; design-pack examples; repository-development governance; external Vyasa/DAF/DarshJDB implementations. They may corroborate behavior but do not become owners in the reviewed DJcode runtime.
- First-party operating / deployment modes considered: ordinary Operator sessions with approval or auto-accept; model-selected foreground/background specialist spawning; direct specialist commands; `/orchestra` and `/waves`; Project Studio dependency flows; local scheduler; persistent memory/session use; `/finish` checks.
- Recursion level: one DJcode-assisted project/task organization. The primary Operator and mutating specialist agents can each constitute operational S1 cells when actively doing engineering work. Read-only reviewer specialists are complementary audit actors. Generic tool calls and scheduler jobs are not promoted to S1 merely because they are concurrent.
- Reviewed revision: `d915b89db1b04cca88c2a495de355e4917a34b1a`.
- Observation date: 2026-10-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

DJcode's `Operator` owns the primary multi-turn tool loop. It sends the current conversation to the selected provider, executes model-selected tool calls through the first-party workflow/dispatch layer, appends tool results and asks the model again until a final response or bounded failure. A supported auto-accept mode removes ordinary per-call approval for an authorized unattended run.

The same tool surface exposes `spawn_agent` to the main model. A spawned specialist receives its own `AgentRunner`, `ContextBus`, role prompt and tool policy; foreground children return their result directly, while up to eight background children can be tracked through `agent_status`. Specialist nesting is bounded. The reviewer role (Dharma) is explicitly read-only and instructed to inspect correctness, security, performance, error handling, tests and dependencies with severity-tagged `file:line` findings.

DJcode also ships higher-level orchestration. `ShadowOrchestrator` deterministically classifies/routs a task into single, parallel, pipeline or wave strategies and can run model-backed blocking specialists. `ParallelCoordinator` executes independent specialists concurrently, pipelines outputs or runs waves, while a shared `ContextBus` carries prior findings. The ContextBus detects key collisions and records them, but no runtime consumer resolves those conflicts or changes allocations because of them; summaries expose only a conflict count. Parallel mutating agents otherwise share the same project workspace with no first-party worktree/file-ownership or collision arbitration found at the frozen ref.

Critical/blocking specialists can stop deterministic orchestration when their model output contains configured severe markers. These gates and workflow stages are current execution enforcement. The normal `/orchestra` path does not put the model-backed Vyasa role in charge of the whole run; routing, strategy selection, wave structure and halting are first-party deterministic rules.

Persistent memories and orchestration vector results can be retrieved into later prompts, and users can create/load skills. These are durable context/capability inputs. The reviewed distribution does not autonomously turn external/prospective change into a selected persistent organizational capability adaptation.

Primary evidence:

- [README.md](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/README.md)
- [`agents/operator.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/agents/operator.py)
- [`tools/agent_spawn.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/tools/agent_spawn.py)
- [`agents/registry.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/agents/registry.py)
- [`agents/parallel.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/agents/parallel.py)
- [`orchestrator/engine.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/orchestrator/engine.py)
- [`orchestrator/context_bus.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/orchestrator/context_bus.py)
- [`workflow.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/workflow.py)
- [`provider.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/provider.py)
- [`skills.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/skills.py)

## Operational model

A normal run starts with a user task. The Operator selects repository-facing tools, DJcode executes or approval-gates them, and returned results become the next model observation. The Operator may autonomously call `spawn_agent` to obtain a separate specialist's work or review and can use the returned result in later tool/model decisions. In auto-accept mode this supported composition does not require per-call human approval.

The optional `/orchestra` path launches several specialist model loops under deterministic routing/wave/pipeline rules. These specialists may mutate the same workspace, but the reviewed runtime does not supply a conflict-specific worktree/file-ownership relation that coordinates their shared writes. Its ContextBus detects information-key collisions but does not resolve or attenuate them.

## S1 — Operations

- State: A
- Function: perform open-ended software-engineering work against the selected project by inspecting artifacts, choosing tools/specialists, modifying code, running commands/tests and revising later actions from returned evidence.
- Disturbance / variety regulated: heterogeneous repository structure, task ambiguity, file/Git state, tool and command results, provider failures, debugging/test outcomes, context limits and specialist findings.
- Decisive decision or feedback right: choose the next engineering tool/action or delegated specialist and determine when enough work/evidence exists to complete the task.
- Decision owner: the main model-backed Operator, or a model-backed mutating specialist within its delegated operational scope.
- Supporting / enforcement mechanisms: provider/tool schemas; WorkflowEngine/DDAL dispatch; permissions/auto-accept; context manager; local tools; task tracker; specialist registry; sessions/memory; bounded tool rounds.
- Closure path: task/current project context → model chooses action/tool → first-party dispatch/enforcement executes against the project → concrete result/error returns → model revises the next action or completes.
- Boundary reachability: the ordinary CLI/TUI directly creates the Operator and exposes the full model/tool loop; auto-accept is a supported mode. Model-callable `spawn_agent` is included in the normal provider tool schema and dispatch table.
- Why this is / is not agent-owned: without the model actor, the deterministic workflow/permission/tool machinery cannot choose the task-specific engineering sequence or semantic code changes.
- Evidence: [`agents/operator.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/agents/operator.py); [`provider.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/provider.py); [`tools/__init__.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/tools/__init__.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: approval is default for tool calls, but a supported authorized auto-accept mode provides the autonomous path; external providers supply inference only.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 interference attenuation loop is established.
- Disturbance / variety regulated: parallel mutating specialists can in principle collide in a shared workspace, but the reviewed distribution does not supply a worktree/file-ownership/lock/arbitration path that prevents or resolves those operational collisions and feeds the resolution back into later S1 behavior.
- Decisive decision or feedback right: not established at S2 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deterministic parallel/pipeline/wave scheduling; ContextBus locking/versioning; context handoff; DAF dependency scheduling; agent limits.
- Closure path: not applicable. ContextBus can record duplicate-key conflicts, but no consumer uses the conflict list to arbitrate or alter later allocations/actions; shared-context propagation and DAG sequencing alone do not close S2.
- Why this is / is not agent-owned: spawning many agents and passing outputs among them is topology/communication. The Methodology requires an evidenced interference-specific attenuation relation, which is absent for the actual mutating operational cells.
- Evidence: [`agents/parallel.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/agents/parallel.py); [`orchestrator/context_bus.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/orchestrator/context_bus.py); [`workflow.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/workflow.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the ContextBus's “conflict” name is not sufficient; it detects information-key collisions but does not resolve them or control shared-workspace interference.

### Absence scope

- Surfaces inspected: main Operator; specialist spawn/status; AgentExecutor; ParallelCoordinator; ShadowOrchestrator; ContextBus; DAF workflow adapter; project/studio workflows; scheduler; tool dispatch.
- Plausible first-party paths checked: worktrees; file ownership; file locks/mutexes; task claims; collision arbitration; child-child messaging; ContextBus conflict handling; DAG dependency sequencing and parallel capacity.
- Why no material first-party path remains: no worktree/file-ownership or equivalent anti-interference layer was found for mutating specialist cells, and ContextBus conflicts are recorded rather than resolved. Remaining scheduling/handoff machinery is generic execution structure.

## S3 — Inside-and-now control

- State: —
- Function: no material discretionary whole-system current-control loop over the active operational population is established.
- Disturbance / variety regulated: routing, wave membership, concurrency, specialist timeouts, critical blocking gates, background-agent limits, workflow dependencies and command schedules are regulated, but chiefly by preset deterministic rules or task-local parent choices.
- Decisive decision or feedback right: not established at S3 scope. The main Operator can launch specialists and inspect background statuses, but no normal model-callable path was found to reprioritize, steer, reassign or cancel an existing multi-agent population using a whole-system current picture.
- Decision owner: not established.
- Supporting / enforcement mechanisms: ShadowOrchestrator complexity/route/strategy rules; ParallelCoordinator; blocking-role gates; agent-status registry; fixed concurrency/nesting limits; DAF graph scheduler; explicit scheduler worker.
- Closure path: preset routing/stage/gate rules can start/stop stages, but no whole-system current view → discretionary resource/commitment/prioritization judgment → changed live S1 commitments → returned operational-state loop is packaged.
- Why this is / is not agent-owned: the model-backed Vyasa profile describes orchestration behavior but is not the actor used by the normal `ShadowOrchestrator.execute` control path. Deterministic workflow control does not inherit S3 ownership from the label “orchestrator”.
- Evidence: [`orchestrator/engine.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/orchestrator/engine.py); [`agents/parallel.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/agents/parallel.py); [`tools/agent_spawn.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/tools/agent_spawn.py); [`scheduler.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/scheduler.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: model-backed blocking specialists can veto critical work, but that narrower assurance judgment is not a general whole-system S3 allocation/commitment owner.

### Absence scope

- Surfaces inspected: ShadowOrchestrator routing/strategy/waves/gates; ParallelCoordinator status and halting; background-agent registry/status; main Operator delegation; DAF workflow; Scheduler; TUI/REPL commands and cancellation.
- Plausible first-party paths checked: live fleet overview; model-owned prioritization; worker reassignment; steering; cancellation; current shared-resource allocation; background-agent intervention; blocking-agent halt decisions and Vyasa control profile.
- Why no material first-party path remains: standard orchestration advances predetermined strategies/gates, while model delegation/status is task-local and lacks broad live intervention rights over existing operational commitments.

## S3* — Complementary audit

- State: A
- Function: challenge an ordinary engineering result through a separately instantiated, role-restricted model reviewer that directly inspects project evidence and returns severity-tagged findings to the parent coding loop.
- Disturbance / variety regulated: correctness bugs, security flaws, performance/error-handling defects, insufficient tests, dependency problems and false-positive completion by the ordinary implementation actor.
- Decisive decision or feedback right: the reviewer child independently decides which observed conditions constitute review findings and their severity from its own read-only model/tool loop; the parent model receives that result and can revise the work or request another review.
- Decision owner: the model-backed Reviewer (Dharma) child.
- Supporting / enforcement mechanisms: normal model-facing `spawn_agent` tool; specialist AgentRunner/AgentExecutor; separate ContextBus; Reviewer system prompt; read-only tool policy; foreground result return or background status/result channel; nesting/budget limits.
- Closure path: main Operator implements/changes work → autonomously invokes `spawn_agent(role="reviewer", ...)` → first-party runtime creates a separate reviewer model loop with direct read/search/Git access → reviewer returns file/line/severity findings as tool result → parent Operator receives the finding in its ordinary transcript → later model turns can fix/retest/review before completion.
- Boundary reachability: `spawn_agent` is in the normal provider tool schema and central dispatch, Reviewer is a built-in role, and children are instantiated by first-party code; no external Vyasa fleet or application-authored reviewer is required. Supported auto-accept allows this path without per-call human approval.
- Claim being audited: that the parent/current implementation or recent project change is sufficiently correct, secure, performant and tested to be accepted as complete.
- Ordinary reporting path: main Operator or mutating specialist's own tool results and completion response.
- Complementary access path: a separately created Reviewer AgentRunner with its own context bus, role prompt and read-only direct repository tools re-inspects project state instead of relying only on the implementer's narrative.
- Independence boundary: reviewer context/role/tool policy is distinct from the ordinary implementer and cannot mutate the workspace; the same underlying provider/model family may be reused, so independence is organizational/session/evidence-path separation rather than provider diversity.
- Who acts on findings: the main Operator receives the reviewer response as a normal tool result and owns subsequent corrective code/test/delegation decisions; another reviewer invocation can challenge the revised state.
- Why this is / is not agent-owned: removing the Reviewer model actor while keeping spawn plumbing and read-only enforcement removes the substantive defect/severity judgment; deterministic machinery cannot reproduce arbitrary code-review findings.
- Evidence: [`provider.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/provider.py); [`tools/agent_spawn.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/tools/agent_spawn.py); [`agents/registry.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/agents/registry.py); [`agents/operator.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/agents/operator.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: standalone user-invoked `/review` and deterministic `/finish` checks are not the basis of the autonomous claim; the positive path is the model-callable reviewer child returned to the active parent agent loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective organizational adaptation loop is established.
- Disturbance / variety regulated: persisted memories, stored specialist results, user-created skills and current task routing can change later prompt context, but they do not form a first-party future-environment sensing → adaptation-option → enacted persistent capability change loop.
- Decisive decision or feedback right: not established at S4 scope.
- Decision owner: not established.
- Supporting / enforcement mechanisms: MemoryManager recall; ContextBus/vector result store and retrieval; skill loader/store; provider/model selection; roadmap/timeline and session persistence.
- Closure path: prior results/memories are retrieved as later context, and user-created skill files can be loaded, but no standard autonomous path decides to create/adopt a future capability in response to prospective environmental intelligence.
- Why this is / is not agent-owned: durable experience reuse is memory, and skill creation is a user/project configuration surface. Neither demonstrates the distinct outside-and-then adaptation function.
- Evidence: [`orchestrator/engine.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/orchestrator/engine.py); [`skills.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/skills.py); [README.md](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: future runs can benefit from stored context; persistence alone is not prospective organizational adaptation.

### Absence scope

- Surfaces inspected: persistent memory; vector context storage/retrieval; skills; roadmap/timeline; agent routing; model/provider configuration; managed update; specialist results and Project Studio definitions.
- Plausible first-party paths checked: agent-authored skills, self-improvement/evolution, benchmark-driven adaptation, automatic model/tool/profile changes, external trend sensing and durable strategy/capability revision.
- Why no material first-party path remains: reviewed durable changes are user/configuration/development paths or remembered operational context; no autonomous future-oriented adaptation authority is wired into the standard run.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity or ultimate-policy closure is established at the assessed recursion.
- Disturbance / variety regulated: system prompts, tool policies, permissions, custom agent/team definitions and blocking rules constrain operation, but no first-party actor adjudicates an identity/ultimate-policy issue and returns that decision as authoritative governing policy.
- Decisive decision or feedback right: not established at S5 scope.
- Decision owner: not established inside the runtime.
- Supporting / enforcement mechanisms: main/specialist system prompts; permission manager and auto-accept; agent specs; user-defined Project Studio agents/organisations/flows; config; safety/approval rules.
- Closure path: configuration and prompts are supplied/edited externally and then enforced or loaded. No runtime identity-policy issue is escalated to legitimate ultimate authority, decided there and returned to govern subsequent organization-wide operation.
- Why this is / is not agent-owned: the primary/specialist agents act inside authored policy; neither they nor deterministic orchestration have authority to redefine DJcode's ultimate purpose/identity/policy.
- Evidence: [`prompt.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/prompt.py); [`agents/registry.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/agents/registry.py); [`permissions.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/permissions.py); [`studio.py`](https://github.com/darshjme/djcode/blob/d915b89db1b04cca88c2a495de355e4917a34b1a/src/djcode/studio.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: custom organizations and approval rules can be durable, but authored configuration is not runtime S5 closure.

### Absence scope

- Surfaces inspected: prompts and agent registry; permissions; Project Studio custom agents/organisations/flows; config; blocking gates; skills/memory; scheduler/update paths; public project governance.
- Plausible first-party paths checked: model-owned constitutional/mission changes, ultimate-policy escalation, parent identity governance, durable project policy authority and blocking-agent decisions as possible S5.
- Why no material first-party path remains: policies/identity constraints are pre-authored or user-managed and no runtime ultimate-policy decision-and-return loop is present.

## Recursion

DJcode can instantiate multiple model-backed operational specialists and reviewer roles. This establishes real plurality, but not every child is an S1: read-only review/scout roles are support/audit. The reviewed standard paths do not close S2 or S3 merely through plurality, fan-out, pipelines or wave topology.

## Variety and escalation

Operational variety is amplified by the main model, many first-party tools, specialist spawning, workflows, browser/computer capabilities and persistent context. It is attenuated by permissions, tool policies, bounded rounds/depth/background-agent counts, deterministic workflows, blocking gates and explicit completion checks.

Reviewer findings can escalate to the parent coding loop for correction. Blocking critical specialists can halt an orchestration according to deterministic gate rules. Users can deny tools or cancel work. These mechanisms are significant but do not independently establish S2/S3/S4/S5.

## Evidence gaps

The assessment is revision-relative to `d915b89db1b04cca88c2a495de355e4917a34b1a`. External Vyasa/DAF/DarshJDB implementations were not imported. The complete frozen tree and the specific S2–S5 candidate paths above were inspected; no unresolved evidence gap requires `?`.

## Assessment summary

DJcode closes autonomous S1 through its first-party Operator/model-tool runtime and autonomous complementary S3* through model-callable, separately instantiated read-only reviewer specialists whose findings return to the active parent coding loop. Multi-agent fan-out, ContextBus collision recording and deterministic orchestration do not close conflict-specific S2 or discretionary whole-system S3. Persistent memory/vector context and user-created skills do not establish prospective S4, and prompts/permissions/custom organizations do not establish S5.

Proposed vector: **`A · — · — · A · — · —`**
