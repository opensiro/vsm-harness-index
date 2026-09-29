---
harness_id: water-code
project_name: Water Code
repository: https://github.com/pacificwater2/water-code
review_ref: e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Water Code

## Review boundary

- System in focus: Water Code's first-party Node coding-agent runtime at frozen revision `e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b`, including `src/core/agent-loop.js`, runtime/tool registry, permission modes, session/context state, custom-agent delegation/swarm, detached background-task workers, plugins/skills and terminal/headless/bridge execution surfaces.
- Purpose and identity: perform coding work in a selected project while optionally decomposing current work into additional first-party Water Code agent runtimes whose lifecycle can be inspected and controlled by the main agent.
- Relevant environment: user tasks, current project/worktree state, provider responses, filesystem/shell/git results, configured MCP tools, project agents/skills/plugins, background-task status/logs and operator permission decisions.
- Standard-distribution boundary: Water Code's own runtime, built-in tools, session/task stores, detached task worker and supported custom-agent orchestration are inside. External model providers and MCP servers are dependencies. User-authored plugins/agents/skills can configure or extend the system but do not donate unshipped organizational functions.
- Credited operating / distribution surfaces: `README.md`; `src/core/agent-loop.js`; `src/core/runtime.js`; `src/core/system-prompt.js`; `src/core/permissions.js`; `src/commands/index.js`; `src/tasks/store.js`; `src/tasks/worker.js`; built-in background-task tools and first-party tool/session plumbing.
- Adjacent first-party surfaces excluded from ownership: release/packaging/smoke scripts, editor shim presentation, contributor/release workflows, and example MCP/plugin behavior where the external/custom component rather than Water Code would own a function.
- First-party operating / deployment modes considered: ordinary interactive/headless model/tool sessions; `yolo`, `ask`, `accept-edits` and `read-only` permission modes; isolated `/delegate`; sequential `/swarm`; detached background tasks; task lifecycle tools; local bridge/editor clients using the same runtime.
- Recursion level: the assessed organization is one main Water Code session plus first-party subordinate background Water Code task runtimes that it can create/inspect/cancel. Each detached task executes its own complete model/tool loop and therefore qualifies as a distinct subordinate S1 at this recursion. Sequential `/delegate` and `/swarm` runs are additional isolated S1 executions but do not themselves create simultaneous interaction.
- Reviewed revision: `e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The primary `AgentLoop` persists a user message, requests one provider turn, executes one model-selected tool call through the first-party registry, appends normalized tool evidence, and repeats until a final assistant response or the turn limit. The loop is repository-owned and shared by ordinary sessions, isolated custom-agent runs and detached task workers.

Custom agents are project-defined prompt/persona configurations. `/delegate` creates one isolated loop/session for one selected agent. `/swarm` iterates through selected agent names sequentially, invoking `runPromptWithAgent` one at a time and collecting outputs; the swarm implementation therefore supplies multiplicity but not simultaneous cross-S1 interference or an S2 attenuation relation.

Background tasks are stronger. `start_background_task` is a model-facing built-in tool. The runtime writes task metadata, starts a detached `water-code --task-worker` child process in the same project root, and that worker creates a new full Water Code runtime with its own session/model loop, active agent/skills, provider, permission mode and tool access. Multiple detached workers can coexist while the foreground main session continues.

The main actor also has model-facing `list_background_tasks`, `get_background_task` and `cancel_background_task`. It can therefore view the current task population/status, inspect task output/logs, create a new subordinate commitment with a chosen agent/skills, and terminate a running commitment. Start and cancel are `dangerous: true`, permission group `background`. In `yolo` they are automatically authorized; in interactive `ask` mode the operator owns the final approval decision and approval can be remembered for the run.

No first-party mechanism was found that arbitrates filesystem conflicts, partitions writable resources, detects cross-worker oscillation, or otherwise attenuates interference among concurrent background runtimes. The task store tracks lifecycle and logs; it does not coordinate their repository actions. That distinction supports S3 without supporting S2.

Primary evidence:

- [`README.md`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/README.md)
- [`src/core/agent-loop.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/agent-loop.js)
- [`src/core/runtime.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/runtime.js)
- [`src/tasks/store.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tasks/store.js)
- [`src/tasks/worker.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tasks/worker.js)
- [`src/tools/start-background-task.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tools/start-background-task.js)
- [`src/tools/list-background-tasks.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tools/list-background-tasks.js)
- [`src/tools/get-background-task.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tools/get-background-task.js)
- [`src/tools/cancel-background-task.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tools/cancel-background-task.js)
- [`src/core/permissions.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/permissions.js)

## Operational model

The main Water Code actor autonomously executes the standard model/tool feedback loop. It may also decide to create a detached subordinate coding task through `start_background_task`. That task runs independently in a child process and later exposes status/output/session evidence through the task registry. The main actor can inspect those records through ordinary tools and cancel running tasks. Thus the standard distribution can form a small current-operation hierarchy rather than only a single coding loop.

The same S3 commitment path has two first-party ownership configurations. In `yolo`, the model's start/cancel choice is automatically executed. In interactive `ask`, the runtime pauses the proposed background commitment action for operator approval; denial prevents it, while approval closes it and can be remembered for that run.

## S1 — Operations

- State: A
- Function: perform environment-facing coding work by interpreting a task, selecting repository/process/tool actions, executing permitted actions, observing results and iterating to a final answer or bounded stop.
- Disturbance / variety regulated: source/worktree state, shell/git/file evidence, provider uncertainty, implementation alternatives, tool failures and changing project context.
- Decisive decision or feedback right: choose the next task-specific tool/action and revise that choice from returned evidence.
- Decision owner: the model-backed Water Code agent in each foreground or detached runtime.
- Supporting / enforcement mechanisms: tool registry; provider adapter; permission engine; session persistence; project context/instructions; skills/plugins; max-turn bound; normalized tool results.
- Closure path: task/current messages → provider decision → first-party tool execution → result persisted/appended → same model actor receives result → next action/final answer.
- Boundary reachability: standard interactive/headless sessions and detached task workers directly instantiate `AgentLoop`.
- Why this is / is not agent-owned: removing the model actor while retaining tools/permissions/storage removes the open-ended coding decision that sequences actions; deterministic/runtime mechanisms only transport or constrain it.
- Evidence: [`src/core/agent-loop.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/agent-loop.js); [`README.md`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: dangerous actions can be human-gated depending on permission mode; autonomous modes remain first-party supported.

## S2 — Coordination

- State: —
- Function: no material first-party cross-S1 disturbance attenuation loop was established.
- Disturbance / variety regulated: concurrent background S1 runtimes can in principle contend on the same project/workspace, but the reviewed distribution does not identify and regulate that interference through an S2-specific coordination relation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: task status records, separate sessions/processes, sequential `/swarm`, ordinary file/tool semantics and operator permission modes.
- Closure path: absent; no first-party conflict/oscillation detection → attenuation decision → feedback changing the competing S1s was found.
- Why this is / is not agent-owned: the task ledger reports lifecycle, not coordination. Sequential swarm avoids simultaneous interaction by sequencing runs, while detached workers are simply launched independently.
- Evidence: [`src/core/runtime.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/runtime.js); [`src/tasks/store.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tasks/store.js); [`README.md`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: shared-workspace interference is plausible precisely because detached tasks are real concurrent S1s; the negative state records absence of an attenuation path, not absence of possible disturbance.

### Absence scope

- Surfaces inspected: isolated delegation/swarm implementation; detached task spawning/worker lifecycle; task store/status/logs; built-in file/process tooling; project/worktree state and permission mechanisms.
- Plausible first-party paths checked: worker scheduling; file locks/version guards; workspace partitioning/worktree assignment; conflict detection; cross-task messaging; shared queue arbitration; sequential swarm ordering as possible S2.
- Why no material first-party path remains: detached workers receive no first-party interference signal or coordination decision, and the task registry controls lifecycle only. Sequential swarm creates no simultaneous S1 interaction requiring attenuation.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate the current population of subordinate background coding commitments by deciding what additional work to launch, what agent/skills to allocate to it, inspecting current task state/output and terminating commitments that should no longer run.
- Disturbance / variety regulated: current workload decomposition, multiple ongoing subordinate commitments, failed/stuck/unneeded background work and the need to redirect bounded current execution without blocking the foreground S1.
- Decisive decision or feedback right: create a background S1 commitment with selected prompt/agent/skills and cancel a running commitment after observing the current task population/status/output.
- Decision owner: model-backed main Water Code actor in the autonomous `yolo` mode; operator in the interactive `ask` parent-governed mode for the decisive start/cancel authorization.
- Supporting / enforcement mechanisms: model-facing `start_background_task`, `list_background_tasks`, `get_background_task`, `cancel_background_task`; detached process launcher; durable task metadata/logs; worker status transitions; permission engine.
- Closure path: current task population/output → model inspects via list/get tools → model selects start/cancel/current-control action → permission path → runtime spawns or signals subordinate task → new task status/result becomes visible to subsequent list/get/model turns.
- Boundary reachability: all four lifecycle tools are registered in the standard tool surface; detached workers use the shipped entrypoint/runtime, not application-authored orchestration.
- Why this is / is not agent-owned: in `yolo`, removing the main model actor leaves lifecycle machinery but no task-specific decision about which new commitment to create or which current commitment to cancel. In `ask`, operator approval becomes decisive for the same commitment action.
- Evidence: [`src/core/runtime.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/runtime.js); [`src/tools/start-background-task.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tools/start-background-task.js); [`src/tools/list-background-tasks.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tools/list-background-tasks.js); [`src/tools/get-background-task.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tools/get-background-task.js); [`src/tools/cancel-background-task.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/tools/cancel-background-task.js); [`src/core/permissions.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/permissions.js).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this is a deliberately small S3: no priority queue, dependency graph or resource allocator is required for the claim. The positive function is the concrete current commitment/lifecycle authority over subordinate complete S1 runtimes. Task status must be explicitly inspected rather than automatically pushed into the foreground model.

### S3 mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Main model-backed Water Code actor | Model selects `start_background_task` or `cancel_background_task` while permission mode is `yolo` | Runtime immediately spawns/signals subordinate S1; status/output is later inspectable by list/get and can change subsequent model decisions | `runtime.js`; background-task tools; `permissions.js` |
| Parent (`P`) | Interactive operator | Main model proposes the same dangerous `background` tool under `ask`; runtime requests confirmation | Approval permits spawn/cancel and returned result enters the main tool loop; denial returns refusal instead | `permissions.js`; background-task tools; `agent-loop.js` |

The parent mode is credited because the approved matter is itself a current organizational commitment: whether a subordinate coding S1 is created or terminated. It is not merely approval of an incidental file edit.

## S3* — Complementary audit

- State: —
- Function: no material boundary-reachable complementary audit role with sufficiently independent access, audit judgment and corrective return was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. A project may define a custom `reviewer` persona and the runtime can delegate to it, but generic custom-agent delegation does not make that reviewer structurally independent or wire an audit verdict into current control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: custom agents, isolated delegation, sequential swarm, ordinary tests/smoke checks and task output inspection.
- Closure path: absent; no standard independent challenge → audit judgment → corrective return loop is supplied.
- Why this is / is not agent-owned: reviewer naming/instructions are project configuration. The first-party orchestration simply runs arbitrary configured personas; it does not provide an audit-specific independence/closure contract.
- Evidence: [`README.md`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/README.md); [`src/core/runtime.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/runtime.js).
- Basis: structural absence review.
- Confidence: high.
- Caveats: applications can compose review workflows from custom agents; Methodology `C` requires a function-specific first-party constructor, not generic delegation.

### Absence scope

- Surfaces inspected: custom-agent loader/execution; delegate/swarm commands; example reviewer agent; background task inspection; tests/smoke/release tooling; tool/result feedback.
- Plausible first-party paths checked: reviewer persona, parallel/isolated judge, task monitor as auditor, release checks, second-pass verification and human permission review.
- Why no material first-party path remains: no audit-specific independence or mandatory/sporadic challenge-and-correction path is wired into normal runtime operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective outside-and-then adaptation loop changing Water Code strategy/capability was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Project context, git/worktree inspection, custom skills/plugins/agents, MCP and background tasks support current work but do not autonomously transform future-relevant external distinctions into changed organizational capability.
- Decision owner: not established.
- Supporting / enforcement mechanisms: context loader, project instructions, git/worktree state, plugins/skills/custom agents, provider selection, MCP and persisted sessions/tasks.
- Closure path: absent; no external/future sensing → adaptation proposal/decision → returned capability/strategy change loop was found.
- Why this is / is not agent-owned: extensions and personas are loaded from operator/project configuration; current-task agents can investigate the repository but do not autonomously revise Water Code's strategy/capability layer.
- Evidence: [`README.md`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/README.md); [`src/core/runtime.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/runtime.js).
- Basis: structural absence review.
- Confidence: high.
- Caveats: background research can be delegated as current operational work; that is not automatically S4 unless it returns into organizational adaptation.

### Absence scope

- Surfaces inspected: project context/git/worktree refresh; session persistence; plugins/skills/custom agents; MCP refresh; background task lifecycle; system prompt/tool surface.
- Plausible first-party paths checked: future/environment monitoring, self-improvement, autonomous plugin/skill acquisition, automatic provider/model adaptation, persistent strategic memory, background research changing runtime capability.
- Why no material first-party path remains: all located extension/adaptation surfaces are operator/project-configured or remain within present task execution.

## S5 — Identity and ultimate policy

- State: —
- Function: no material identity/ultimate-policy decision-and-return loop was established at this recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. Permission modes, remembered approvals, system/project instructions, provider choice and extension loading are operator-authored configuration/safety surfaces rather than runtime identity/ultimate-policy deliberation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: permission modes; approval state; project `WATER.md`; CLI configuration; active agent/skills/plugins/MCP selection.
- Closure path: absent; no identity/ultimate-policy issue reaches a legitimate S5 authority and returns as a governing policy change.
- Why this is / is not agent-owned: the model operates inside the configured permission/system boundary and can request actions but does not autonomously redefine Water Code's ultimate purpose/authority structure.
- Evidence: [`src/core/permissions.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/permissions.js); [`src/core/system-prompt.js`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/src/core/system-prompt.js); [`README.md`](https://github.com/pacificwater2/water-code/blob/e207e732e8da2f63f1ee1256a5aa62bcaaadcc6b/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: human approval can own S3 commitment decisions in `ask` mode without becoming S5; the governed matter is current task lifecycle, not identity/ultimate policy.

### Absence scope

- Surfaces inspected: permission/approval modes; system/project instructions; custom-agent/skill/plugin selection; provider/MCP configuration; bridge/session/task controls.
- Plausible first-party paths checked: autonomous policy revision; parent identity escalation; constitutional/purpose changes; permission mode as S5; provider/extension selection as ultimate policy.
- Why no material first-party path remains: the standard distribution exposes configurable constraints and current-control approvals but no identity-level deliberation and returned governing-policy loop.

## Recursion, variety, escalation and unresolved evidence

- Recursion: one main Water Code runtime plus subordinate detached Water Code task runtimes it manages. Sequential custom-agent runs can also be distinct S1 executions, but only background tasks establish concurrent persistent commitments in the reviewed standard distribution.
- Variety: coding uncertainty and project/tool evidence are absorbed by each S1; current workload/task-lifecycle variety can be absorbed at S3 through model-driven background-task management. Cross-worker repository interference remains unattenuated at S2.
- Escalation: dangerous background commitment actions can escalate to the operator in `ask` mode, producing the parent-governed S3 mode; ordinary edit/shell approvals do not independently establish higher functions.
- Unresolved evidence: no material evidence gap required `?`. The S3 claim is intentionally narrow and tied only to explicit background-task commitment management, not to generic multi-agent naming.

## Assessment vector

**`A · — · A(P) · — · — · —`**
