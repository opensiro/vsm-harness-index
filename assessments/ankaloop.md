---
harness_id: ankaloop
project_name: AnkaLoop
repository: https://github.com/tao12345666333/ankaloop
review_ref: 6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216
reviewed_at: 2026-10-16
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
autonomy_s5: A(P)
---

# AnkaLoop

## Review boundary

- System in focus: the first-party installed AnkaLoop Python coding-agent runtime at pinned `6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216`, with its model/tool loop, session-bound optional subagents, memory-review process and persistent global identity/soul files.
- Purpose and identity: execute user-directed coding tasks with file/shell/MCP tools, delegate narrow subtasks and preserve owner-defined persona and preferences across new sessions and interfaces.
- Relevant environment: local repository and shell, external LLM endpoint, user requests and definitions, session history, global/project durable memory, CLI/server/Telegram interfaces.
- Standard-distribution boundary: bundled `ankaloop` Python package, native agent/tool loop, first-party `TaskManager` and subagent registry, shipped memory tool/review, `SOUL.md` and `IDENTITY.md` identity persistence and system prompt assembly.
- Credited operating / distribution surfaces: first-party `Agent` with `ToolLoop.enhanced_chat_with_tools`; CLI/server/Telegram task entrypoints; bounded subagent execution; normal model-callable identity/soul memory writes and on-demand pre-compaction memory-review actor; global persona scope and session-frozen subsequent system-prompt injection.
- Adjacent first-party surfaces excluded from ownership: optional third-party MCP servers, externally authored agent specs, CI, project maintainer decisions, external cron execution and hosted LLM reasoning weights. Project ordinary memory and transcript summarization by themselves do not prove future organizational intelligence S4.
- First-party operating / deployment modes considered: normal coding loop and optional subagent tasks; ordinary user-defined persona instructions and model memory tool invocation; optional memory review before compaction/periodic checkpoint; persisted user-scoped persona injected at new-session context construction; operator manual edits via CLI/file controls. No live model-backed coding or persona-update demonstration was executed in this source-first inspection.
- Recursion level: one owner-directed, installed coding-agent service with an enduring user-scoped identity across CLI/HTTP/Telegram sessions. The user provides the rightful top-level persona authority; model may transform/store user-declared identity but not invent a new external organization's legitimacy.
- Reviewed revision: `6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216` from Index frozen candidate #379.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

AnkaLoop's native `Agent` and `ToolLoop` construct a first-party model/tool/result feedback loop. `enhanced_chat_with_tools` builds an executable local/MCP tool registry and a capability-constrained executor, requests model tool calls, handles their results and feeds them to later turns until exit or budget. CLI, server and Telegram surfaces share the native agent runtime ([src/ankaloop/agent.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/agent.py), [src/ankaloop/tool_loop.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/tool_loop.py), [src/ankaloop/tool_execution.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/tool_execution.py), [README.md](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/README.md)). `TaskManager` can spawn separate model-driven coder/planner/explorer/focused_coder subagents on bounded semaphores, with delegation envelope and task results returning to the parent ([src/ankaloop/task.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/task.py), [src/ankaloop/multi_agent.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/multi_agent.py)). Scheduling/capacity and ordinary task messages do not themselves attest an inter-S1 interference-specific coordination function or a separately owned whole-current S3.

The distinctive durable **identity path** is more than generic fact memory: the packaged memory tool exposes `write_soul`, `write_identity` and `identify`, confined to a **global user persona scope**. The instructions encourage the model to use these on user-defined identity, name, values, style or persona, including a separate model-invoked `run_memory_review` actor at a durability checkpoint ([src/ankaloop/memory_review.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory_review.py), [src/ankaloop/tools.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/tools.py), [src/ankaloop/memory.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory.py)). The first-party memory manager writes `SOUL.md` and `IDENTITY.md`, rejects project-scoped competing identities and returns a unified global persona across all interfaces. `ContextBuilder.get_system_prompt` **prepends** this source to the base agent instruction in later sessions, and `Agent._get_memory_prompt_context` freezes it per current session to prevent implicit mid-turn identity drift ([src/ankaloop/context_builder.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/context_builder.py), [src/ankaloop/agent.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/agent.py), [src/ankaloop/memory.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory.py)). This is a distinct identity-policy publication/return mechanism under user legitimacy, not a generic one-turn permission check.

Memory dream and review also summarize/recover durable facts, but no verified future capability strategy, optimizer, held-out adaptation gate, or autonomous environment-prospective S4 operator is shown. The second model invoked by memory review checks what *facts to store*, not producer coding correctness; it is not S3* solely because the module uses the word review.

## Operational model

A user asks the agent to work in a project; its first-party model chooses file/shell/MCP actions and receives observed results. Parent may delegate a focused task to a read-only explorer or focused coder, and task status/result returns through local dispatch. Separately, when the user explicitly defines an enduring agent identity, personality or work style, the running model is instructed to choose the global memory tool's soul/identity action; the checkpoint memory-review actor can independently recognize and store an owner-declared identity before compaction. The memory manager publishes the file to the user scope, and new sessions later load it into their system prompt. The operator can directly edit identity and soul files and provide further legitimate definitions. This sustains a global identity rather than an invented user-company governance system. Absent a defined persona update, no change is assumed.

## S1 — Operations

- State: A
- Function: carry out open-ended coding tasks through model-driven file/tool execution and observation feedback.
- Disturbance / variety regulated: changing project files, code search, failed commands, tool errors, user instructions and child task results.
- Decisive decision or feedback right: model chooses executable tools/arguments, subsequent corrections, task delegation and completion based on observations.
- Decision owner: first-party AnkaLoop `Agent` model-directed actor with tool-loop mediator and locally registered tools; selected external model supplies inference.
- Supporting / enforcement mechanisms: `ToolLoop`, tool registry, `ToolExecutor`, session state, asynchronous provider adapters, native file/shell tools and optional child task.
- Closure path: request→`_call_llm`→model-chosen tools→local/MCP `ToolExecutor.execute`→tool observation appended to model context→follow-up action or terminal answer.
- Boundary reachability: ordinary CLI/server/Telegram package launch invokes this first-party runtime without an external coding-agent harness.
- Why this is / is not agent-owned: model steers context-dependent coding work, not a fixed deterministic script.
- Evidence: [src/ankaloop/tool_loop.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/tool_loop.py), [src/ankaloop/agent.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/agent.py), [src/ankaloop/tool_execution.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/tool_execution.py), [README.md](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/README.md).
- Basis: source-evidenced first-party feedback loop.
- Confidence: high for integrated path; not live runtime performance.
- Caveats: provider access, model quality and optional external tools not independently verified.

## S2 — Coordination

- State: —
- Function: no observed first-party mechanism detecting and attenuating concrete interference between separate active operational S1 subagents.
- Disturbance / variety regulated: parallel agents can work on the same project files, competing for write access and compute budget, but no conflict-specific coordination return is shown.
- Decisive decision or feedback right: decide changes to separate S1 assignments in response to measured shared-work interference; absent.
- Decision owner: `TaskManager` enforces semaphore and role restrictions, while parent agent issues tasks and consumes their responses; no conflict-specific sibling coordinator identified.
- Supporting / enforcement mechanisms: fixed task cap, parent session/role envelopes, no-delegation subagent mode, task queues and cancellation.
- Closure path: generic completed task result or cancellation returns; no shared-write conflict detect→rescope/serialize→later child action response established.
- Why this is / is not agent-owned: the presence of an explorer/planner/coder roster and bounded parallel task manager is generic delegation/capacity control, not organizational S2.
- Evidence: [src/ankaloop/task.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/task.py), [src/ankaloop/multi_agent.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/multi_agent.py), [src/ankaloop/tool_execution.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/tool_execution.py).
- Basis: bounded negative source inspection.
- Confidence: moderate.
- Caveats: external project worktrees/locks could be added by user, but not credited as first-party S2.

### Absence scope

- Surfaces inspected: task queue and semaphore, role configuration, nested delegation, task result/notification feedback, execution limits and workspace use.
- Plausible first-party paths checked: multiple child worker cap, shared workspace, role-based read-only scout tasks, task cancellation and priority.
- Why no material first-party path remains: no verified first-party interference-specific shared-resource arbitration, conflict evidence owner, and actual modified sibling commitments.

## S3 — Inside-and-now control

- State: —
- Function: no distinct superior whole-current organizational regulator over all operating child S1 units at the selected user-task recursion.
- Disturbance / variety regulated: failed tool calls, per-session step budget, child queue congestion, cancellation, context limits and provider retries are local operational concerns.
- Decisive decision or feedback right: independent system-wide current resource/priority and commitment allocation with feedback to S1; not found.
- Decision owner: main coding model delegates user tasks as needed, task manager schedules by fixed rules, human triggers session/cancellation commands; no separate whole-system current plan/control owner.
- Supporting / enforcement mechanisms: tool loop limit, server session manager, TaskManager, event bus and tool/role authorization.
- Closure path: local task/cancel/queue state changes, not externally governed whole-current S3 decisions based on system-wide evidence.
- Why this is / is not agent-owned: parent coding actor's task decomposition and deterministic capacity guard do not prove distinct S3 regulation.
- Evidence: [src/ankaloop/task.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/task.py), [src/ankaloop/agent.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/agent.py), [src/ankaloop/server/session_manager.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/server/session_manager.py).
- Basis: bounded negative.
- Confidence: moderate.
- Caveats: user can govern multiple deployments externally, but that parent organization was not assessed.

### Absence scope

- Surfaces inspected: main agent, child TaskManager, session scheduling, server interaction, tool event stream and cancellation.
- Plausible first-party paths checked: main agent acting as planner, child task restrictions, server status, scheduled jobs and human session intervention.
- Why no material first-party path remains: no distinct current-control owner with group-wide monitoring, discretionary allocation/policy and returned regulation separate from normal task execution.

## S3* — Complementary audit

- State: —
- Function: no independently assigned coding-claim audit with independent evidence and binding findings/corrective return path.
- Disturbance / variety regulated: incorrect code changes and false completion claims; task-local tools and model self-check may encounter them.
- Decisive decision or feedback right: a distinct reviewer should inspect producer claims and return failing evidence to a controller with power to block/correct; not shown.
- Decision owner: parent/subagent coder/planner and optional memory-review model only review task context or memory facts, not a first-party coding-claim audit mandate.
- Supporting / enforcement mechanisms: agent result, tool observations, user-confirmed hooks, memory review and project rules.
- Closure path: normal tool/child result can help a coder, while memory review writes facts; no complementary code-evidence→independent verdict→accountable repair relation.
- Why this is / is not agent-owned: model review of **which user facts to remember** is not independent verification of operations. Generic planner/explorer subagents do not have a mandatory correctness gate.
- Evidence: [src/ankaloop/memory_review.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory_review.py), [src/ankaloop/task.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/task.py), [src/ankaloop/agent.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/agent.py).
- Basis: bounded negative.
- Confidence: moderate.
- Caveats: user-authored custom reviewer agent could add a workflow not shown as first-party default.

### Absence scope

- Surfaces inspected: memory review actor, normal/subagent tool paths, agent role definitions, hooks and task results.
- Plausible first-party paths checked: separate memory model, read-only explorer, planner, test command and generic post-tool hooks.
- Why no material first-party path remains: none is a claimed-work complementary audit with separate findings disposition into current operational correction.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct prospectively selected organizational capability adaptation from external/future environment evidence.
- Disturbance / variety regulated: context loss, stale user preference and repetitive history are addressed by memory, not by separately judging future capability changes.
- Decisive decision or feedback right: choose a novel or changed skill/system capability based on cross-session environmental opportunities and return a durable operational adaptation; not evidenced.
- Decision owner: the first-party dream/memory-review model consolidates facts and user-scoped identity; the installed capability repertoire remains configured or user/plugin authored.
- Supporting / enforcement mechanisms: `MemoryDreamer`, long-term memory store, searchable history, skill loader and session snapshots.
- Closure path: project/user facts or global identity reload as context; no autonomous future-capability experiment, option judgment and admission path to alter actual skill/tool repertoire.
- Why this is / is not agent-owned: fact learning/compaction and identity S5 publication are separate functions, neither by itself supplies prospective S4 strategic intelligence.
- Evidence: [src/ankaloop/memory_dream.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory_dream.py), [src/ankaloop/memory.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory.py), [src/ankaloop/skills.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/skills.py), [src/ankaloop/memory_review.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory_review.py).
- Basis: bounded negative.
- Confidence: moderate.
- Caveats: an external adopter may extend skills or capabilities later; no source-backed standard-issue S4 control is imported.

### Absence scope

- Surfaces inspected: memory consolidation, identity/prompt building, skill discovery, long-term storage, hooks and automated jobs.
- Plausible first-party paths checked: memory dream, periodic model memory review, auto skill inclusion, dynamic context and scheduled run results.
- Why no material first-party path remains: no outside/future capability selection, evidence-based promotion or binding later skill/tool change apart from saved facts and global persona.

## S5 — Identity and ultimate policy

- State: A(P)
- Function: owner-authorized publication and continuation of agent's durable global persona/identity and role policy, with model-driven extraction and human direct edit/authority modes.
- Disturbance / variety regulated: persistent identity drift across CLI/server/Telegram sessions, inconsistent user-defined role/style and project-specific persona conflicts.
- Decisive decision or feedback right: decide how to record a legitimate explicit user-defined identity/soul statement, publish to user-scope `SOUL.md`/`IDENTITY.md` and return it as precedence-bearing system-prompt context for later sessions. User can explicitly change/overwrite its meaning.
- Decision owner: first-party model-directed normal memory tool and separately invokable memory-review actor synthesize durable identity **from user-supplied authority** (autonomous `A` path); legitimate user/operator directly defines or edits persona and may invoke commands (parent `P` mode). No invented self-authorization over third-party organizational policies.
- Supporting / enforcement mechanisms: `MEMORY_GUIDANCE`, memory-only review prompt, `write_soul/write_identity/identify` tool action, global-only scope check, file persistence, singular persona composition and session-frozen system prompt construction.
- Closure path: explicit owner identity/role correction→model-selected `memory` identity action (normal chat or checkpoint review)→durable global identity/soul file written→new session builds global persona→prepended to base system prompt→subsequent coding sessions operate with updated durable identity. Parent may edit files to override.
- Boundary reachability: the memory tool is shipped by default, and `MEMORY_GUIDANCE` is included in every system prompt; on-demand memory review and user direct commands are both first-party operating modes, not developer CI.
- Why this is / is not agent-owned: model chooses and writes lasting identity text in an installed supported user-authorized path, and the output is made normative in subsequent sessions. User retains ultimate authority; hence `A(P)`, not unconditional autonomous constitutional sovereignty.
- Evidence: [src/ankaloop/memory_review.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory_review.py), [src/ankaloop/tools.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/tools.py), [src/ankaloop/memory.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory.py), [src/ankaloop/context_builder.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/context_builder.py), [src/ankaloop/commands.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/commands.py).
- Identity / ultimate-policy issue: a single global persisted agent identity/persona/values/work-style layer, not project-specific ordinary facts.
- Ultimate authority in each claimed mode: model may select and synthesize durable identity only from explicit user definitions in Base (`A`) mode; the legitimate user directly defines, changes or replaces global persona in Parent (`P`) mode. Global-only scope prohibits competing project personas.
- Return-to-operation path: a later session prepends persisted `Global Soul` and `Global Identity` content to its system prompt, overriding default persona selection after a custom global identity exists.
- Basis: first-party model-mediated user-authoritative durable identity decision/return.
- Confidence: moderate-high for code mechanism; no live persona-change test in assessment.
- Caveats: the model may not reliably update files when not prompted; session persona is deliberately frozen, so updates become active in a new session, not immediately on the same run. The implementation does not govern an external organization's constitution or validate the truth of every model-generated identity statement.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Installed model-directed memory actor and/or checkpoint review model, under user-defined identity scope | User explicitly defines agent persona, name or work style with enduring effect and model recognizes it as identity | Global soul/identity written through first-party memory tool; later session prepends persisted global persona to system prompt | [src/ankaloop/memory_review.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory_review.py); [src/ankaloop/tools.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/tools.py); [src/ankaloop/context_builder.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/context_builder.py) |
| Parent (`P`) | Legitimate operator with global user persona scope and direct write/command authority | Operator directly defines, corrects or replaces `SOUL.md` / `IDENTITY.md` | Global persona file reloaded in next session and may supersede previously model-recorded persona | [src/ankaloop/commands.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/commands.py); [src/ankaloop/memory.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/memory.py); [src/ankaloop/context_builder.py](https://github.com/tao12345666333/ankaloop/blob/6a4aec4b258d4980dad4d8ea0e455ba5d6cd2216/src/ankaloop/context_builder.py) |

## Evidence gaps

- Neither an actual coding task nor a model-backed identity write and reload was executed in this inspection; claims concern explicit first-party source paths and supported modes.
- S5=A(P) is limited to user-governed agent persona/identity rather than independent authority to define an external enterprise's purpose. No default model-written constitution is assumed.
- Isolated memory review and memory dreaming are not coded as audit of producer code; long-term memory by itself cannot satisfy S4.
- Per-subagent fixed semaphore and role restrictions do not prove S2 conflict regulation or S3 whole-current decision right.

## Conclusion

AnkaLoop ships autonomous first-party coding tool loops (S1=A) and standard subagent/task execution but no demonstrated inter-S1 S2, independent whole-current S3, coding-claim complementary S3* or prospective-capability S4. It also ships a separate, globally persistent, user-legitimated `SOUL.md` / `IDENTITY.md` decision-and-return path: the model may write owner-defined identity, and user can authoritatively correct it, yielding **S5=A(P)** in an explicit identity-update mode. Proposed frozen vector: **A / — / — / — / — / A(P)**, not canonical until separately admitted.
