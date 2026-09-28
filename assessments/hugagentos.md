---
harness_id: hugagentos
project_name: HugAgentOS
repository: https://github.com/ZJU-REAL/HugAgentOS
review_ref: 9436fcb77261bc995e6e7a45cdc5e192eae9bc74
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: A(P)
---

# HugAgentOS

## Review boundary

- System in focus: one supported project-scoped HugAgentOS Community Edition operating cell at pinned revision `9436fcb77261bc995e6e7a45cdc5e192eae9bc74`, including the FastAPI backend, AgentScope-backed ReAct runtime, first-party tools/sandbox/MCP integration, callable sub-agents, autonomous-loop driver/reviewer, project instructions and memory, personal evolution, and supported background/automation surfaces.
- Purpose and identity: operate a durable project workspace in which model-driven agents perform substantive work with tools, delegate bounded work, continue long-running tasks, preserve project context, verify results independently, and remain governed by durable project rules.
- Relevant environment: user/project files, configured model providers, MCP/external services, browser and command environments, sandbox state, task/project history, operator permissions and approvals, provider/tool failures, and changing project requirements.
- Standard-distribution boundary: public Community Edition code and ordinary supported project/runtime capabilities present at the pinned revision. Enterprise-only or explicitly target-architecture surfaces are not used to establish a positive function merely because related public modules are present in the monorepo.
- Credited operating / distribution surfaces: ordinary project chat/ReAct execution; callable sub-agent execution; built-in autonomous-loop execution and its read-only reviewer; project-root `AGENTS.md` synchronization and `/init`; direct authorized project-instruction editing; project-scoped memory; Community Edition personal evolution where relevant to S4 boundary analysis.
- Adjacent first-party surfaces excluded from ownership: repository contributor governance; CI/release machinery; tests except as corroboration; future/target architecture; Enterprise-only fleet governance; ontology control-plane claims not shown to be a completed ordinary Community Edition operating path; upstream AgentScope/model-provider internals.
- First-party operating / deployment modes considered: standard project chat; callable sub-agent dispatch; autonomous long-running loop; supported background/automation; personal memory/evolution; project `/init` in supported write-permitted approval modes; direct project editor/admin instruction editing.
- Recursion level: one HugAgentOS project operating cell is the system-in-focus. Main/sub-agent executions that own substantive project outcomes are S1 operations. The authoritative project-root `AGENTS.md` is assessed at this same project recursion because it defines durable goals, work rules, quality/acceptance expectations and operating boundaries injected into later project conversations.
- Reviewed revision: `9436fcb77261bc995e6e7a45cdc5e192eae9bc74`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

HugAgentOS owns the first-party assembly around AgentScope's `ReActAgent`: project/request context, prompt and tool surfaces, model/provider selection, sandbox/MCP execution, streaming, logging, durable chats/runs and project-scoped state. A model-driven actor iterates reasoning, tool choice, observation and later action, so the project cell contains substantive autonomous operations rather than only a UI or provider adapter.

Callable sub-agents use the same execution machinery. The first-party `call_subagent` implementation deliberately runs each child in a separate worker thread with its own event loop because MCP/AnyIO cancellation scopes otherwise produce cross-task runtime errors. This supplies a narrow concrete S2 anti-interference path rather than crediting delegation or parallelism generally.

Long-running work is organized by a driver-owned requirement ledger. The autonomous-loop driver selects one unfinished requirement at a time, persists checkpoints and handoffs, applies stall/failure guards, and requires independent review before flipping a requirement to passed. These are strong task-level controls, but they do not establish a separate whole-project S3 regulator over the current portfolio of S1 resources, commitments, priorities and synergy.

Complementary audit is explicit: the driver starts a separate read-only reviewer agent in the same project sandbox, with requirement/acceptance criteria rather than the worker conversation. The reviewer personally inspects real files and read-only command evidence instead of trusting worker self-report; its verdict returns to the loop, and final completion receives an independent second pass.

Personal evolution is also substantive. Community Edition can mine one user's historical episodes, identify repeated successful tool sequences, use a semantic judge, produce private skill candidates and install approved capability changes. This is genuine adaptation, but it is grounded in internal operating history rather than a distinct external-and-prospective environmental model, so it does not close S4 at this recursion.

Project identity/policy has a separate durable surface. The project-root `AGENTS.md` is authoritative, is automatically carried into project conversations, and defines project goals/scope, sources, workflows, quality/acceptance expectations and operating boundaries. A supported `/init` mode gives the model actor a project-bound write tool so it can inspect project material, decide the exact durable rule update, persist it and read it back. Separately, legitimate project editors/admins can directly edit the same authoritative file. Subsequent project conversations load the changed rules into the system-prompt project section. These two supported ownership modes close S5 as `A(P)` at the project recursion.

## Operational model

At this recursion, model-driven main/sub-agent executions are S1 units when they own substantive project outcomes. Per-child async isolation supplies deterministic S2 coordination for a concrete sibling-interference mode. No project-wide S3 current regulator is established. The autonomous-loop reviewer supplies independent S3* audit. Personal evolution does not satisfy S4's outside-and-then threshold. Durable project-root `AGENTS.md` policy closes S5 through two first-party modes: model-owned `/init` synthesis and parent-owned direct project-rule editing.

## S1 — Operations

- State: A
- Function: perform substantive project work through model-driven iterative reasoning, tool use and observation-driven continuation.
- Disturbance / variety regulated: ambiguous tasks, changing project/file state, tool/service results, browser/command outcomes, model uncertainty and evolving user context.
- Decisive decision or feedback right: choose task-specific reasoning/tool actions and revise subsequent actions from returned observations until the bounded outcome is complete.
- Decision owner: the model-driven ReAct actor assembled and executed through HugAgentOS's first-party runtime.
- Supporting / enforcement mechanisms: `orchestration/workflow.py`, `core/llm/agent_factory.py`, AgentScope integration, tool registry, sandbox/MCP execution, project/context/memory injection, streaming and approval controls.
- Closure path: project objective + assembled context → model actor selects action/tool → HugAgentOS executes within the permitted boundary → result returns to the actor → later model action changes in response → project outcome advances.
- Boundary reachability: ordinary first-party project-chat and supported background paths instantiate the ReAct runtime directly; no contributor-only actor is required.
- Why this is / is not agent-owned: removing the model actor while retaining FastAPI, tools, persistence and sandbox leaves execution infrastructure but removes the task-specific discretionary action choice.
- Evidence: [`document/en/modules/chat.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/document/en/modules/chat.md); [`src/backend/orchestration/workflow.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/workflow.py); [`src/backend/core/llm/agent_factory.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/llm/agent_factory.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: AgentScope and model/provider internals remain dependencies. `A` credits the model actor reached through HugAgentOS's supported first-party harness path, not organizational functions internal to those dependencies.

## S2 — Coordination

- State: C
- Function: attenuate a concrete runtime interference mode between concurrently dispatched S1-capable sub-agents by isolating each child's asynchronous execution/cancellation scope.
- Disturbance / variety regulated: multiple child agents using MCP/AnyIO machinery can otherwise create cross-task cancellation-scope errors that disrupt sibling operation.
- Decisive decision or feedback right: determine the execution-isolation boundary for each dispatched child so one sub-agent's async/cancellation lifecycle cannot corrupt another child's task scope.
- Decision owner: deterministic first-party HugAgentOS runtime policy in `call_subagent`; no autonomous coordination actor chooses this isolation relation.
- Supporting / enforcement mechanisms: dedicated `ThreadPoolExecutor`, one event loop per child thread, child cancellation bridge, isolated MCP clients and separated child runtime construction.
- Closure path: parent dispatches distinct S1-capable children → unsafe cross-task async interference is separated by per-child thread/event-loop isolation → each child continues its own model/tool lifecycle → independent results return for subsequent operation.
- Boundary reachability: `call_subagent` is a shipped first-party tool and the isolation is its ordinary implementation at the pinned revision.
- Why this is / is not agent-owned: the anti-interference policy remains if the model agents are replaced; deterministic runtime code decides and enforces the isolation boundary. The function is therefore constructor/runtime-owned `C`, not `A`.
- Distinct S1 units: two or more concurrently dispatched model-driven child/main agents capable of substantive delegated project work.
- Inter-S1 disturbance: cross-task AnyIO/MCP cancellation-scope interaction can raise runtime errors and interrupt sibling child execution when async lifecycles share an unsafe task boundary.
- Attenuating coordination relation: each child executes in its own worker thread with its own event loop and isolated MCP/client lifecycle, keeping cancellation scopes inside the owning task.
- Feedback into subsequent S1 behaviour: isolated children remain able to execute later model/tool steps and return results instead of failing from sibling cancellation-scope corruption.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping rests on an explicitly named cross-task failure mode and a first-party isolation mechanism intended to remove that interference. Delegation, routing and the pool are not independently treated as S2.
- Evidence: [`src/backend/core/llm/subagent_tool.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/llm/subagent_tool.py); [`document/en/modules/chat.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/document/en/modules/chat.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is a narrow technical coordination function. It does not imply that all sub-agent routing, batching or delegation is S2.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-project current-control function is established at the assessed recursion.
- Disturbance / variety regulated: individual autonomous loops regulate requirement progress, retries, checkpoints, reviewer findings, stalls and hard limits; automation/batch paths regulate their own jobs. These are lower-scope execution controls rather than a distinct project-wide S3.
- Decisive decision or feedback right: no qualifying whole-project current-control decision over active operational resources, commitments, priorities, constraints or synergy is established.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: autonomous-loop ledger, one-requirement-at-a-time driver, checkpoints, replan hooks, runaway breakers, background lifecycle, batch orchestration and user approvals.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: planner/worker/reviewer agents make bounded task decisions while deterministic drivers enforce one loop/job's progression. Neither demonstrates a separate whole-project S3 owner.
- Evidence: [`document/en/modules/autonomous-loop.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/document/en/modules/autonomous-loop.md); [`src/backend/orchestration/autonomous_loop.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/autonomous_loop.py); [`src/backend/orchestration/batch_orchestrator.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/batch_orchestrator.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: at a narrower recursion one autonomous-loop driver is a strong controller of its own worker/reviewer process; this assessment does not lift that local task controller into project-level S3.

### Absence scope

- Surfaces inspected: autonomous-loop driver/reviewer; batch orchestration; callable sub-agents; automation/background execution; task lifecycle; model/provider routing; approval and project/runtime context paths.
- Plausible first-party paths checked: requirement ledger as supervisor; planner/replanner as manager; automation scheduler; batch orchestrator; worker pool; background task manager; provider/model control; HITL surfaces.
- Why no material first-party path remains: the inspected mechanisms regulate one task, loop, dispatch or configured job, or expose local/operator controls. None establishes a distinct current whole-project view plus authority over the project's operational portfolio on behalf of the whole.

## S3* — Complementary audit

- State: A
- Function: independently verify whether a worker's claimed autonomous-loop requirement is actually implemented by inspecting real project output through a separate read-only agent path, then return findings into correction.
- Disturbance / variety regulated: worker self-report can claim completion when underlying files/output do not satisfy the requirement; the ordinary worker path can therefore hide defects or absent deliverables.
- Decisive decision or feedback right: inspect actual produced files/command evidence independently and return `done`, `continue`, `off_track` or `need_human` for the requirement.
- Decision owner: the separate model-driven loop reviewer agent instantiated by the first-party autonomous-loop driver.
- Supporting / enforcement mechanisms: distinct reviewer context, read-only capability policy, same project sandbox, explicit acceptance criteria, structured verdict/evidence, independent second pass, sub-agent logs and deterministic driver routing.
- Closure path: worker produces candidate + summary → driver starts independent reviewer with requirement/criteria but not worker conversation → reviewer reads/searches/runs read-only checks against actual project output → verdict/findings return to driver → non-done findings change subsequent work; accepted evidence permits ledger advancement.
- Boundary reachability: `autonomous_loop.py` invokes `review_requirement` in the shipped autonomous-loop path; docs expose the loop through the normal API/frontend and `can_run_autonomous_loop` capability.
- Why this is / is not agent-owned: the substantive audit judgment is produced by a distinct model-driven reviewer. Deterministic read-only restrictions and driver routing enforce the boundary but do not decide whether the output satisfies the requirement.
- Claim being audited: the worker's claim that the current requirement is complete and its project artifacts satisfy the requirement/acceptance criteria.
- Ordinary reporting path: worker summary and its ordinary model/tool trajectory, plus machine evidence produced during the work iteration.
- Complementary access path: separate reviewer agent personally opens/searches the same project sandbox and may run read-only commands rather than trusting worker self-report.
- Independence boundary: reviewer and worker use distinct contexts/agent executions; the reviewer does not reuse the worker conversation, is explicitly read-only and is deterministically spawned by the driver rather than by the worker being judged.
- Who acts on findings: the autonomous-loop driver; `continue`/`off_track`/`need_human` feed correction/replanning/escalation, while only accepted evidence-backed completion advances the requirement ledger.
- Evidence: [`document/en/modules/autonomous-loop.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/document/en/modules/autonomous-loop.md); [`src/backend/orchestration/autonomous_loop.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/autonomous_loop.py); [`src/backend/orchestration/subagents/loop_reviewer.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/orchestration/subagents/loop_reviewer.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ontology committee/review code is not needed for this finding; the credited path is the directly reachable autonomous-loop reviewer.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established at the assessed project recursion.
- Disturbance / variety regulated: HugAgentOS preserves memory, observes tools/services and can adapt private capability from accumulated operational episodes, but the reviewed path does not maintain a distinct model of the outside/future environment and return adaptation options through a separate current/future organizational conversation.
- Decisive decision or feedback right: no qualifying S4 prospective adaptation judgment/feedback right is established.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: project/user memory, automation/triggers, personal evolution, historical-episode mining, semantic SOP judge, private skill candidates and owner approval.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: personal evolution genuinely changes capability, but it mines the user's own historical operating episodes for repeated successful patterns. Internal learning from past operations is not enough by itself to establish Profile S4.
- Evidence: [`src/backend/core/evolution/personal.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/evolution/personal.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the negative finding distinguishes real history-driven capability adaptation from the specific outside-and-then organizational function required for S4.

### Absence scope

- Surfaces inspected: memory retrieval/storage; personal evolution and candidate promotion; automation/triggers; external tools/browser/MCP; project context; planner/replanning; ontology/runtime governance; model/provider configuration.
- Plausible first-party paths checked: evolving memory as S4; personal skill evolution; event reaction; external research tools; loop replanning; provider changes; ontology updates.
- Why no material first-party path remains: memory/evolution is grounded primarily in internal historical episodes; event-triggered work and external research remain S1 task execution unless connected to a distinct prospective adaptation function; no separate S3↔S4 current/future organizational conversation is established at this recursion.

## S5 — Policy and identity

- State: A(P)
- Function: maintain the durable project identity and ultimate operating rules that define project goals/scope, authoritative sources, work methods, output/quality expectations and operating boundaries for later project operations.
- Disturbance / variety regulated: project drift, missing or obsolete durable rules, conflicting/incomplete operating instructions and changes to project goals, quality requirements or boundaries.
- Decisive decision or feedback right: decide the authoritative root `AGENTS.md` content for the project and make that policy decision govern subsequent project-agent operation.
- Decision owner: Base (`A`) mode — the model-driven project-init agent decides the exact rule update after inspecting current rules and representative project material, then persists and verifies it. Parent (`P`) mode — a legitimate project editor/admin directly edits the same authoritative root file through supported project-instruction surfaces.
- Supporting / enforcement mechanisms: `ProjectInstructionsService`, project permissions, optimistic revision checks, project-bound instruction tools, runtime approval mode, context assembly and project system-prompt injection.
- Closure path: identity/policy issue → project-init agent synthesis or legitimate parent edit → authoritative root `AGENTS.md` write → later project context reads changed instructions → project system prompt injects them → subsequent project-agent behavior is governed by the returned policy.
- Boundary reachability: project instructions, `/init`, direct authorized instruction editing and automatic project-context injection are shipped Community Edition paths at the frozen revision. The documented `auto` and `full` approval presets provide supported write-permitted modes in which ordinary project-instruction persistence does not require a human to choose or approve the exact model-generated content.
- Why this is / is not agent-owned: in base mode, the operator selects the initialization operation but the model actor makes the semantic decision about which durable goals/workflows/quality/boundary rules to add or revise from project evidence. Removing the model leaves storage and permission machinery but not that project-policy judgment. In parent mode, the authorized human directly owns the authoritative policy edit.
- Identity / ultimate-policy issue: what the project is for and the durable rules later project agents must follow, including goals/scope, important sources, workflows, output/quality expectations and operating boundaries.
- Ultimate authority in each claimed mode: Base (`A`) — the project-init model actor for the exact synthesized update in the autonomous initialization mode; Parent (`P`) — the authorized project editor/admin for direct authoritative edits.
- Return-to-operation path: changed root `AGENTS.md` is the canonical project-instruction source, is loaded into project context, and is injected into subsequent project system prompts/conversations.
- Evidence: [`document/en/modules/projects-myspace.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/document/en/modules/projects-myspace.md); [`src/backend/core/services/project_instructions.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/services/project_instructions.py); [`src/backend/core/llm/tools/project_instructions_tool.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/llm/tools/project_instructions_tool.py); [`src/backend/prompts/project_init.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/prompts/project_init.md); [`src/backend/prompts/project_section.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/prompts/project_section.py); [`src/backend/core/llm/agent_factory.py`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/src/backend/core/llm/agent_factory.py); [`document/en/modules/chat.md`](https://github.com/ZJU-REAL/HugAgentOS/blob/9436fcb77261bc995e6e7a45cdc5e192eae9bc74/document/en/modules/chat.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `/init` is explicitly user-invoked and is instructed to preserve human-authored constraints. `A` credits the model-owned semantic project-policy decision within that supported mode; it does not imply authority to erase higher-level operator constraints or rewrite unrelated platform policy.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | model-driven project-init agent | authorized project `/init` invocation in a supported write-permitted mode | inspect project/current rules → decide exact durable rule update → save and read back authoritative `AGENTS.md` → later project prompts load it | `project_init.md`, `project_instructions_tool.py`, `agent_factory.py`, `projects-myspace.md` |
| Parent (`P`) | legitimate project editor/admin | direct supported instruction edit / project PATCH | parent edits root `AGENTS.md` → revision-checked authoritative save → subsequent project turns load/inject changed rules | `projects-myspace.md`, `project_instructions.py`, `project_section.py` |

## Distributed OSS parent arrangement

The public repository's maintainer/contributor organization is outside this project-runtime boundary. Repository governance and release authority therefore do not donate S5. The `P` mode above is instead the supported parent relationship inside a deployed project: a legitimate project editor/admin directly owns the authoritative project-policy edit and the runtime returns that decision into subsequent project operation.

## Self-hosted and non-human modes

HugAgentOS is local-first and supports remote/background operation. Generic human approvals over tools or private evolution candidates are not treated as S3/S4/S5. The S5 parent mode is narrower and function-specific: an authorized project editor/admin changes the authoritative durable project rules that later project agents receive.

## Recursion

A project can contain a main agent, callable child agents, autonomous-loop worker/reviewer executions, automation jobs and tool subprocesses. This assessment treats model-driven actors as S1 operations when they own bounded substantive project outcomes. Nested processes are not automatically recursive viable systems. Project-root policy is mapped at the project recursion because it governs those later project operations rather than merely configuring one transient task.

## Variety and escalation

HugAgentOS attenuates operational variety with sandboxing, scoped tools/MCP, context management, explicit approvals, per-child runtime isolation, durable loop ledgers, project rules and independent review. It amplifies response variety through multiple models, skills, sub-agents, browser/tool access and memory. Escalation appears in approval prompts, reviewer `need_human`, loop hard guards and failed background work; those channels remain mechanisms inside their mapped functions rather than standalone VSM functions.

## Evidence gaps

- S2 is intentionally narrow: it credits a documented cross-task cancellation-scope interference and first-party child isolation, not multi-agent naming, delegation, queues or parallelism generally.
- The autonomous-loop driver is powerful but remains a bounded task controller at this recursion; no project-wide S3 is inferred from it.
- S3* is based on the standard autonomous-loop reviewer path, not the ontology trust-control-plane target architecture.
- Personal evolution is real capability adaptation but is not promoted to S4 without external/prospective environmental distinctions and an S3↔S4 organizational loop.
- S5 `A(P)` is specific to the project recursion and authoritative root `AGENTS.md`: model-owned `/init` synthesis and parent-owned direct project-rule editing are distinct supported modes. Generic editable prompts or ordinary approval gates are not used as the S5 witness.
