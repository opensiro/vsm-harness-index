---
harness_id: capstan
project_name: Capstan
repository: https://github.com/theStrangeAdventurer/capstan
review_ref: 60f284fc94ce96d05e72b52d2ffe55b4096b0177
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: A
autonomy_s5: —
---

# Capstan

## Review boundary

- System in focus: the supported Capstan terminal/headless/ACP coding-agent implementation, whose C host and embedded first-party Lua agent/runtime/plugins jointly operate one coding session and optionally spawn bounded child-agent runs.
- Purpose and identity: a lightweight local coding agent that inspects and changes workspace files, invokes tools and tests, delegates scoped tasks to model-based subagents, and optionally teaches itself durable local Lua extensions.
- Relevant environment: local project workspace, user/configured provider and model, filesystem and shell, embedded agent scripts, permission popup/rules, optional MCP servers, operator session, and local configuration/skills/plugins.
- Standard-distribution boundary: the C program (terminal/headless/ACP, local state, permission enforcement, hot-reload) and shipped Lua agent loop, built-in tools, plugins, profiles and enabled embedded self-improvement skill at this exact revision. Providers, external MCP services, project/user-contributed plugins and third-party model decisions are not separate first-party organizational owners; model decisions via the wired runtime may be counted.
- Credited operating / distribution surfaces: src/agent.c, src/dispatch.c, src/permit.c, src/plugins.c, src/plugins_runtime.c, agent/runtime.lua, agent/tools.lua, agent/tasks.lua, agent/profiles.lua, plugins/file_edit.lua, plugins/file_write.lua, plugins/shell.lua, profiles/implement.lua, profiles/plan.lua, skills/self-improvement/SKILL.md, and shipped interactive/headless/ACP entry paths.
- Adjacent first-party surfaces excluded from ownership: development CI/build workflows, benchmark/evaluation reports, exploratory Aider Polyglot runs, test and example harnesses, AGENTS.md author instructions, and merely documented/user-authored custom review profiles; they are not automatically operating organizational components.
- First-party operating / deployment modes considered: default implement coding loop, read-only plan profile, headless run and ACP using the same Lua runtime, model-requested parallel subagents (enabled by default), explicit optional completion-review continuation, opt-in self-improvement capability/skill with persistent Lua plugin hot reload, human permission-configured execution, and Wiki retrieval.
- Recursion level: one Capstan coding-agent session is the system in focus; simultaneously spawned child agents are subordinate task units. Individual external projects whose files are changed are operating environments, not additional Capstan organizations.
- Reviewed revision: 60f284fc94ce96d05e72b52d2ffe55b4096b0177.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Capstan's C host owns terminal input/output, session data, provider HTTP transport plumbing, permission/storage boundaries and live plugin reload. Embedded Lua owns the model request/response tool loop, provider selection, profile tool-filtering, subagent execution and local task-state handling. A model chooses edit/read/shell/fetch actions via first-party tool schemas; the runtime enforces declared scope and returns tool results for further decisions.

A model-facing subagents tool accepts a list of scoped child tasks with per-child tools/model/turn caps, running several independent in-process Lua agent loops concurrently via asynchronous network waits. The parent receives a bounded batch JSON result after children finish and then decides what to do next; child calls do not nest. Queueing, cancellation and retry handling are deterministic runtime services. The task-plan store persists explicit task statuses/revisions, not an independently empowered manager or an S2-specific conflict controller.

Default profiles include implement and plan. The optional completion_review flag inserts a follow-on review instruction into the SAME main agent message chain for certain unvalidated multi-file changes; built-in profiles disable it by default. A user may create a custom read-only review profile, but the example is not itself a shipped dedicated reviewer.

A distinct opt-in capability makes the bundled self-improvement skill available. When enabled, the model can identify a repeatable future workflow, construct a durable user Lua plugin/tool/hook in the permitted configuration directory, and thereby change the commands or model tools available in later runs; first-party C code hot-reloads those files. The self-improvement skill and its capability-gated loader are credited, not a hypothetical arbitrary user extension. This is a conditional shipped operating mode, not a default on every installation.

Primary source anchors:
- [agent loop and completion-review path](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/runtime.lua)
- [tool schema, subagent fan-out and child result collection](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/tools.lua)
- [task-plan store](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/tasks.lua)
- [first-party agent-loop spec](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/agent-loop.md)
- [subagent runtime contract](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/subagents.md)
- [self-improvement capability/skill loader](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/src/plugins_runtime.c)
- [self-improvement shipped instructions](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/skills/self-improvement/SKILL.md)
- [user-plugin hot reload](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/src/plugins.c)
- [model tool permission scope](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/permissions.md)

## Operational model

One parent model owns the local coding task: inspect the workspace, choose tool calls, integrate returned evidence, optionally delegate child tasks, validate and deliver. The parent has discretion over the content and routing of tasks but does not gain a continuously updated live portfolio-control interface merely from requesting a parallel batch. The permission/runtime guard enforces allowed tools, budgets and cancellation without owning those task-specific choices. An optional capability-gated, future-directed code-generation workflow can change the agent's own future extension surface; it still obeys human-configured permission limits.

## S1 — Operations

- State: A
- Function: implement/inspect/verify a requested change through iterative model-selected actions in the project workspace.
- Disturbance / variety regulated: varying user code requests, repository contents, tool failures, tests, model/tool availability, permission denials and returned outputs.
- Decisive decision or feedback right: select next tool/action, revise approach from tool/test output, request delegation, and determine when the code change is complete.
- Decision owner: Capstan's main model loop; child models own bounded delegated operational tasks.
- Supporting / enforcement mechanisms: C host, provider transport, Lua tool dispatcher, skills/profiles, sandbox and permit controls, sessions, guard and telemetry.
- Closure path: prompt → model tool decision → permission-gated first-party action → returned observation → next model decision and correction or final response.
- Boundary reachability: the shipped implement and headless/ACP modes call the same live agent runtime and expose the first-party coding tools.
- Why this is / is not agent-owned: C executes and enforces; the model retains the task-specific operational discretion and reacts to evidence.
- Evidence: [runtime.lua](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/runtime.lua), [tools.lua](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/tools.lua), [agent-loop.md](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/agent-loop.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external models/providers and approval rules are necessary dependencies/constraints, not additional credited autonomous owners.

## S2 — Coordination

- State: —
- Function: no first-party feedback loop specifically attenuating conflict or oscillation BETWEEN distinct S1 work units is established.
- Disturbance / variety regulated: parallel child tasks may contend for provider slots, tools and a shared workspace, but no demonstrated task-to-task interference regulator with feedback into subsequent individual S1 choices is shipped.
- Decisive decision or feedback right: none meeting S2-specific closure at the declared recursion.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: child concurrency cap, inherited permission scope, per-child whitelist and turn limits, result ordering, deterministic queue, retry/cancellation.
- Closure path: not established as S2; child results are returned to a parent after execution.
- Boundary reachability: no positive path claimed.
- Why this is / is not agent-owned: a parent agent delegates tasks, while runtime queue and guard enforce chosen limits; neither demonstrates specific cross-child conflicting-operation detection and attenuation.
- Evidence: [subagents spec](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/subagents.md), [subagent runtime](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/tools.lua), [task store](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/tasks.lua).
- Basis: structural.
- Confidence: medium-high.
- Caveats: concurrency-cap resource scheduling can prevent overload, but should not be re-labelled inter-S1 coordination absent disturbance-specific returned regulation.

### Absence scope

- Surfaces inspected: supported child-agent spec/dispatcher/queue/retry/cancellation, task-plan store, profile restrictions, permissions and parent continuation.
- Plausible first-party paths checked: parallel workspace tasks, shared provider capacity, tool whitelists, ordered result joins, parent choosing follow-on tasks after batch completion.
- Why no material first-party path remains: no wired first-party task-conflict, competing-worktree/ownership or oscillation-specific detection and returned coordination adjustment governing the already distinct S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current-operation management loop with a current comprehensive view, substantive portfolio control and returned supervisory intervention is established.
- Disturbance / variety regulated: budgets, asynchronous child work and task-plan status are bounded locally; whole-current organization regulation is not demonstrated.
- Decisive decision or feedback right: no identified management decision over all active S1 commitments beyond planning and routing individual work.
- Decision owner: no S3 actor established.
- Supporting / enforcement mechanisms: parent subagent orchestration, immutable ordered batch results, timeout/turn caps, local task statuses/revision, headless/TUI run status and cancellation.
- Closure path: model sees completed child results and may launch more work; no live whole-current control or feedback path over active commitments is shown.
- Boundary reachability: no positive path claimed.
- Why this is / is not agent-owned: model task selection and deterministic scheduling are not by themselves a whole-current authority. Human cancellation/permission popups likewise do not constitute a supervised current-control mode.
- Evidence: [subagents spec](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/subagents.md), [tools.lua](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/tools.lua), [tasks.lua](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/tasks.lua), [agent-control spec](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/agent-control.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: genuine autonomous task-level routing is credited to S1, not automatically S3.

### Absence scope

- Surfaces inspected: parent model and result-join path, child live status and cancellation, task-plan persistence, CLI/ACP/TUI controls and profiles.
- Plausible first-party paths checked: batch subagent dispatch, task board, dynamic provider selection, live UI indicators, budget/guard/cancel and the optional completion-review continuation.
- Why no material first-party path remains: checked paths do not combine whole-current subordinate visibility with a manager-owned current-control decision and a substantive returned intervention changing the running S1 set.

## S3* — Complementary audit

- State: ?
- Function: shipped read-only child-model/tool compositions may furnish direct workspace access for a separate review judgment, but a complete independent complementary-audit/corrective-return path is not yet conclusively evidenced.
- Disturbance / variety regulated: implementation mistakes and discrepancies between agent claims and actual files/tests could be examined, but the distinct review authority/return path needs confirmation.
- Decisive decision or feedback right: potentially a read-only child-agent with fresh context evaluating artifacts; separate corrective-control ownership and actual triggering remain unresolved.
- Decision owner: unresolved; the same-agent completion-review continuation is not independent, while an explicitly prompted subagent might make a first-party complementary audit possible.
- Supporting / enforcement mechanisms: independent child Lua execution context, read-only profile/tools, file_read and shell inspection if allowed, model-selected delegation, and optional same-agent completion-review switch.
- Closure path: potential parent initiates independent inspection → receives child findings → decides correction; no concrete built-in verification-trigger and return-to-action workflow was established by inspected sources.
- Boundary reachability: a positive state is not claimed; child-agent read access and parent batch-result collection are shipped, but an audit-specific operational mode still requires function-level evidence.
- Why this is / is not agent-owned: mere generic delegation or the self-review continuation must not be treated as independent S3*. The unresolved question is whether a concrete supported standard-mode parent-to-read-only-child audit has the required complementary authority and feedback.
- Evidence: [tools.lua](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/tools.lua), [subagents spec](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/subagents.md), [agent profiles](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/agent-profiles.md), [runtime completion-review implementation](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/agent/runtime.lua).
- Basis: structural + unknown.
- Confidence: low.
- Caveats: requires source-first semantic adjudication of direct evidence access, independence boundary and real corrective return; no independently executed reviewer receipt is claimed here.

## S4 — Outside-and-then intelligence

- State: A
- Function: in the opt-in shipped self-improvement mode, assess future repeat-use needs and construct a durable local agent capability in response.
- Disturbance / variety regulated: new/repeating operator workflows and capability gaps whose solution must persist beyond one coding request.
- Decisive decision or feedback right: select reusable command/model tool/hook shape, design a Lua plugin and optional skill, write it with first-party tools, and revise from validation/feedback.
- Decision owner: the Capstan model when the owner has enabled the first-party self-improvement capability and authorized the relevant write.
- Supporting / enforcement mechanisms: configuration flag, embedded skill loader, ordinary permission checks, plugin scanner and hot reload, durable Lua plugin and skill directories.
- Closure path: prospective workflow need detected in the user/environment → model designs persistent capability → permission-gated plugin/skill write → C hot reload registers future executable behavior → subsequent Capstan runs can invoke the new command/tool/hook.
- Boundary reachability: the shipped C loader intentionally enables the bundled skill when capabilities.self_improvement is true; shipped file-write/shell model tools can create the suggested durable plugin, and C watches/reloads it in the supported installation. This is an explicit opt-in first-party mode, not borrowed CI/dogfood or a hypothetical third-party plugin.
- Why this is / is not agent-owned: the human controls whether the mode is enabled and grants file permissions, but the model determines the prospective adaptation content and implements the persistent future capability. The hot-reload loop enforces, rather than chooses, the change.
- External distinction: prospective repeated workflow need and owner/project environment not yet served by present built-in command/tool set.
- Future / prospective distinction: the requested extension should remain useful in later sessions and may serve later as a command, model tool, or hook.
- Adaptation option generated: executable local Lua plugin, optional paired skill and automation hook.
- Path back into current capability / S3: newly created plugin is hot-loaded into the active Capstan command/tool/hook registry for later agent use; no positive S3 is inferred.
- Evidence: [self-improvement skill](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/skills/self-improvement/SKILL.md), [self-improvement spec](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/self-improvement.md), [embedded skill loader](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/src/plugins_runtime.c), [plugin reload](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/src/plugins.c).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: disabled by default; first-party agent may suggest an extension but cannot bypass the human's explicit capability and file permissions. This is not proof that Capstan automatically evolves itself without user-context needs or authorization. Independent semantic review should scrutinize whether the outside-and-then adaptation right is adequately instantiated in this opt-in mode.

## S5 — Policy and identity

- State: —
- Function: no legitimate first-party ultimate organizational identity/purpose arbiter with returned constitutional-policy decision is established within the assessed session.
- Disturbance / variety regulated: permission exceptions, selected agent profile, provider choice and extension capabilities are operational/configuration constraints, not demonstrated S5 identity reconciliation.
- Decisive decision or feedback right: not established for whole-system ultimate purpose/identity; owner configuration and permits set local limits.
- Decision owner: no evidenced first-party S5 decision loop; ordinary parent user consent is not enough for a P state.
- Supporting / enforcement mechanisms: Lua configuration, profile selection, permit rules, static system prompt, first-party skill enablement and project AGENTS.md.
- Closure path: user-selected execution permissions affect tools but no articulated identity/purpose matter traverses a legitimate ultimate-policy body and returns as authoritative organizational policy for future operation.
- Boundary reachability: no positive path claimed.
- Why this is / is not agent-owned: removing the model leaves preset policy enforcement, not autonomous ultimate-purpose decisions; removing operator prompts removes configuration without revealing an autonomous S5 owner.
- Evidence: [permissions](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/permissions.md), [profile policy](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/specs/agent-profiles.md), [system prompt](https://github.com/theStrangeAdventurer/capstan/blob/60f284fc94ce96d05e72b52d2ffe55b4096b0177/ai/system_prompt.txt).
- Basis: structural.
- Confidence: medium-high.
- Caveats: advanced externally authored governance policies are possible but not automatically part of this assessed distribution.

### Absence scope

- Surfaces inspected: first-party config and permit model, profile policies, completion-review switch, built-in prompt, user extensions and opt-in self-improvement skill.
- Plausible first-party paths checked: operator enabling capabilities, grants/deny decisions, plan-versus-implement profile changes, editing project/system instructions, and persistent agent-made Lua extension.
- Why no material first-party path remains: inspected paths govern task execution or add capabilities but do not establish a whole-system constitutional identity/purpose question, legitimate ultimate decision owner and returned S5 policy closure.

## Recursion

The parent Capstan session is one coding S1 operating organization; child model runs are bounded delegated operational subunits at the next recursion and do not themselves prove that all higher VSM functions are instantiated. A user-owned fleet of independent Capstan installations has not been assessed as a single organizational boundary.

## Variety and escalation

Workspace variation is absorbed by iterative model/tool cycles; model/provider errors may trigger bounded retries, and permission restrictions are escalated to the human permit surface. Child tasks have configurable caps, deterministic queues and a bounded response to the parent. Feedback that returns after subagent completion permits the parent to revise tasks, but does not establish S2 or a live S3 controller. Opt-in self-improvement can change future first-party plugin capabilities within authorized local policy. Runtime errors, telemetry and cancellation are operational signals, not independent proof of algedonic channel or a metasystemic VSM function.

## Evidence gaps

- S3*: frozen first-party child-run infrastructure supports independent child context and direct tools, yet source review did not confirm a shipped recurring audit-specific verification trigger, independent audit authority and returned corrective close. The optional completion-review feature reuses the parent model message chain and is expressly not independent. Re-evaluate this specific function in review without importing a separate Index reviewer as evidence.
- S4: verify whether the enabled self-improvement skill plus model-directed future extension actually meets the Profile S4 prospective outside/then requirement rather than merely executing a user-specified current coding task. The A proposal is restricted to the explicit opt-in persistent-capability path.
- No runtime live provider invocation or end-to-end hosted model evaluation was performed; this is a source-first frozen-revision assessment.

