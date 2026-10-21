---
harness_id: zaino
project_name: Zaino
repository: https://github.com/zenodea/zaino
review_ref: f842bd0589471972bf680aaa35a8a6159eb8c8df
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Zaino

**Proposed, noncanonical general VSM assessment** for [Index batch #1842](https://github.com/opensiro/vsm-harness-index/issues/1842) row 9 from original frozen intake [#860](https://github.com/opensiro/vsm-harness-index/issues/860). Evidence-bounded source vector `A / C / — / — / — / —` is not provider task benchmark or proof of perfect conflict isolation.

## Review boundary

- System in focus: Shipped Go Zaino terminal coding agent for one user's workspace and optional independently model-guided subagents.
- Purpose and identity: Perform user-directed coding work with first-party model/tool feedback loop, workspace tools, optional background children, and operator-configured permissions.
- Relevant environment: Project files/shell, provider APIs, terminal or TUI, optional MCP/hook, local session/history/memory.
- Standard-distribution boundary: Frozen shipped cmd/zaino + internal/agent/tool/workspace/permission implementations; model provider inference is a dependency, but all task orchestration and shared-file guards assessed are first-party.
- Credited operating / distribution surfaces: [cmd/zaino/main.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/cmd/zaino/main.go), [internal/agent/agent.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/agent.go), [internal/agent/task.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/task.go), [internal/agent/subagent.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/subagent.go), [internal/tool/workspace.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/workspace.go), [internal/tool/edit.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/edit.go), [internal/tool/write.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/write.go), [internal/permission/gate.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/permission/gate.go), [internal/store/session/file.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/store/session/file.go).
- Adjacent first-party surfaces excluded from ownership: [.github/workflows/landing.yml](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/.github/workflows/landing.yml), [README.md](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/README.md), [install.sh](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/install.sh) used for docs/distribution evidence, but CI/promotion/release work and maintainer task governance do not supply the installed harness's S3–S5 decision owners. User hooks and external MCP are not autonomous first-party policy owners.
- First-party operating / deployment modes considered: installed TUI/REPL, print mode, plan/manual/bypass permissions, standard synchronous tasks and optional background main-level subagents, shared file edit/write, budget cap, session tree, project memory.
- Recursion level: One self-hosted Zaino installed work organization; multiple child S1 task cells may run with separate contexts but shared project tools, not demonstrated independent higher recursion.
- Reviewed revision: [zenodea/zaino@f842bd0589471972bf680aaa35a8a6159eb8c8df](https://github.com/zenodea/zaino/tree/f842bd0589471972bf680aaa35a8a6159eb8c8df)
- Observation date: 2026-10-22
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The executable [cmd/zaino/main.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/cmd/zaino/main.go) wires first-party raw provider clients and [internal/agent/agent.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/agent.go) model/tool turn loop to the installed file/shell tools and permission gate. The model selects operations and receives result content on each subsequent turn. [internal/agent/task.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/task.go) may spawn synchronous or background child model loops with separate context and tool access; background completion becomes a steered message for the parent. Except the per-child task depth/individual Todo, the first-party tool instances are inherited, including the same [internal/tool/workspace.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/workspace.go) object. Its per-path lock and snapshot-sensitive [internal/tool/edit.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/edit.go) / [internal/tool/write.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/write.go) operations prevent conflicting stale writes from discarding another concurrent operation; a failed stale update reports an error for re-reading instead of silently clobbering. The shared [internal/agent/budget.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/budget.go) enforces configured spending cap; session tree, project memory, user hooks and approval modes are operational supports, not self-evident S3–S5 ownership.

## Operational model

Primary S1 runs model-guided coding tool turns. Optional parallel child S1 units can work in the same repository under inherited first-party tools, with child reports fed back to the parent. A shared per-file lock and stale-state precondition regulate an actual resource competition between concurrently running coding cells (narrow deterministic S2=C). All other model routing/task tracking, user file approvals and persistent memory are judged function-first rather than promoted by feature labels.

## S1 — Operations

- State: A
- Function: Model-directed software editing, investigation and command execution through a shipped terminal coding-agent loop.
- Disturbance / variety regulated: Unstructured repository tasks, uncertain file state, failing tool calls, provider errors and changed developer requirements.
- Decisive decision or feedback right: Select next operational tool call, use returned observations, revise a coding operation or issue final answer.
- Decision owner: First-party Zaino agent/model loop; runtime executes selected calls subject to operator-defined permissions.
- Supporting / enforcement mechanisms: Provider clients, tools registry, streamed model messages, permission gate, session tree/rewind, hooks, budget and context compaction.
- Closure path: User task → installed agent.Run provider turn → chosen tool calls → admit/execute tool operations → observed result blocks in next model request → new action or answer.
- Boundary reachability: The shipped cmd/zaino and internal/agent/agent.go own the model/tool loop; raw provider/client implementations and installed workspace tools are in the first-party executable, not hypothetical plugins.
- Why this is / is not agent-owned: If model action selection is removed, tool wrappers and terminal UI alone cannot perform open-ended coding work. User tool approval limits effects, not normal task decision ownership.
- Evidence: [cmd/zaino/main.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/cmd/zaino/main.go); [internal/agent/agent.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/agent.go); [internal/tool/tool.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/tool.go); [internal/tool/read.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/read.go); [internal/tool/edit.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/edit.go); [internal/provider/anthropic/client.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/provider/anthropic/client.go)
- Basis: explicit/structural
- Confidence: high for shipped first-party wiring; live model outcomes not measured
- Caveats: This is frozen Go-source analysis; no source Go test execution or provider-backed multiagent collision run was attested.

## S2 — Coordination

- State: C
- Function: Deterministic per-file arbitration and stale-write rejection for independent model-guided parent/child S1 coding operations sharing a workspace.
- Disturbance / variety regulated: Separate background or foreground model-guided child agents may write the same workspace file while other S1 edits are proceeding. If both use a stale original, a later writer could overwrite the earlier writer's work.
- Decisive decision or feedback right: Serialize file writes, compare the file's actual current bytes with the pre-edit snapshot, reject a stale write and return conflict feedback to the offending S1's subsequent model context.
- Decision owner: First-party deterministic shared tool.Workspace per-path lock and edit/write admission/run checks; model-initiated S1 edits remain independently owned.
- Supporting / enforcement mechanisms: Workspace lock table, read/write snapshot, edit/write prepared call, shared child tool pointers, background task reinjection, error-to-tool-result plumbing.
- Closure path: Distinct S1 model loops share inherited parent workspace tools → concurrent write intentions compete on common path → per-path lock serializes writes → later stale call detects actual file changed and fails with 'read it again' → error becomes a tool result for that child/parent next model action; released lock permits retry against fresh content.
- Boundary reachability: Installed task tool can spawn separate model-guided children, including background mode; taskCall.spawn inherits parent tools except task-depth and per-child Todo, so children use the same workspace and its per-path lock. edit/write checks run in first-party standard modes.
- Why this is / is not agent-owned: S2=C here credits only the deterministic first-party inter-S1 file interference barrier, not a general conflict-resolution policy or autonomous organizational coordination. Generic asynchronous messaging alone would not suffice; the shared path lock + stale rejection + model-visible feedback is the decisive witness.
- Evidence: [internal/agent/task.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/task.go); [internal/agent/agent.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/agent.go); [internal/tool/workspace.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/workspace.go); [internal/tool/edit.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/edit.go); [internal/tool/write.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/write.go); [internal/tool/tool_test.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/tool_test.go)
- Basis: explicit/structural with source test
- Confidence: moderate-high for source-closed mechanism; no Go runtime tests executed
- Caveats: This is frozen Go-source analysis; no source Go test execution or provider-backed multiagent collision run was attested.

- Distinct S1 units: The parent and spawned child or multiple background children run separate model/tool loops using inherited shared workspace tools; a background child can outlive a main turn.
- Inter-S1 disturbance: Two coding cells prepare edit/write calls against the same file but one writes first; the other might discard its change without recognizing a stale basis.
- Attenuating coordination relation: Workspace.Lock(abs) serializes write attempts for one shared file, then Edit/Write.Run refuses a stale prepared snapshot (rather than clobber the first writer).
- Feedback into subsequent S1 behaviour: The refused call reports a 'changed on disk since it was read — read it again' tool error; Agent.runTools returns results in next model context for the affected independent S1, enabling re-read/retry.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The lock and stale-file guard handle a specific resource collision among independent active coding cells; output is not merely a parent task summary, tool batch ordering or shared database existence.

## S3 — Inside-and-now control

- State: —
- Function: No independent whole-system manager making current resource/commitment decisions across multiple coding cells has been established.
- Disturbance / variety regulated: Shared provider cost, child task budgets, active background agents and todo progress.
- Decisive decision or feedback right: Would require a whole-current view and decisive reprioritization of resources/commitments with a returned intervention into S1 operations.
- Decision owner: No qualifying S3 owner. Operator sets spend cap and model chooses coding steps; budget is shared enforcement and job/status UI is descriptive.
- Supporting / enforcement mechanisms: Shared Budget, spend cap and task limits, background agent task info, Todo, session history and job status views.
- Closure path: Budget threshold can halt a running model loop and individual task status is returned, but no manager-level whole-current choice changes priority or commitments across independently operating S1 cells.
- Boundary reachability: No S3 positive mode credited from first-party installed runtime.
- Why this is / is not agent-owned: A spent-dollar counter, limit gate, task tracker or parent task delegation is not an S3 resource authority with whole-system current-control closure.
- Evidence: [internal/agent/budget.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/budget.go); [internal/agent/task.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/task.go); [internal/tool/todo.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/todo.go); [internal/tool/job.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/job.go); [internal/agent/agent.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/agent.go)
- Basis: bounded structural negative
- Confidence: moderate
- Caveats: This is frozen Go-source analysis; no source Go test execution or provider-backed multiagent collision run was attested.

### Absence scope

- Surfaces inspected: Agent Budget/limits, task and background-job registry, Todo, session/UI status, child steering.
- Plausible first-party paths checked: Whole-current operational balance over independent S1s; legitimate manager changes shared priorities/commitments and returns decisions.
- Why no material first-party path remains: Existing mechanisms are caps, instrumentation and local task management. Shared enforcement does not make the enforcer owner of S3 decisions.

## S3* — Complementary audit

- State: —
- Function: No complementary, sufficiently independent operational audit of S3 management claims with returned corrective control.
- Disturbance / variety regulated: Misreported tool results, coding mistakes, unapproved edits and incorrect session history.
- Decisive decision or feedback right: A distinct auditor would compare S3 managerial reporting to independently accessed operational reality and return corrective authority.
- Decision owner: No S3* audit owner found; user diff review, history rewind and hooks inspect task artifact/operation, not independently audit an S3 managerial account.
- Supporting / enforcement mechanisms: Saved file checkpoints, session journey/rewind, tool error checks, per-tool hooks and tests.
- Closure path: One file edit may be shown or reverted through UI, but no independent whole-current-manager assertion is investigated and converted to corrective managerial action.
- Boundary reachability: No positive audit mode; review and session tools are shipped but operate below the manager audit boundary.
- Why this is / is not agent-owned: Reviewing edits or observing logs is not the S3* organizational function without independent evidence path and feedback to current management.
- Evidence: [internal/frontend/tui/rewind.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/frontend/tui/rewind.go); [internal/agent/hook_test.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/hook_test.go); [internal/store/session/store.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/store/session/store.go); [internal/tool/diff.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/diff.go); [internal/agent/agent.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/agent.go)
- Basis: bounded structural negative
- Confidence: moderate
- Caveats: This is frozen Go-source analysis; no source Go test execution or provider-backed multiagent collision run was attested.

### Absence scope

- Surfaces inspected: Session tree/history and file checkpoints, UI rewind/diff, hook callbacks, task completion records.
- Plausible first-party paths checked: Independent sampling and judgment of S3 current-management assertions and returned corrective decision.
- Why no material first-party path remains: All inspected review surfaces concern task operations/artifact history, and no independent S3 management audit and intervention path was identified.

## S4 — Outside-and-then intelligence

- State: —
- Function: No evidenced prospective outside-environment intelligence selecting and adopting a durable change in the installed agent's future capability.
- Disturbance / variety regulated: Future changes in repositories, LLM providers, tool workflows and task requirements.
- Decisive decision or feedback right: Assess future/external conditions, select a concrete organizational adaptation option, then install/return it into present capability.
- Decision owner: Not demonstrated. Operator configures models/hooks/MCP and agent optionally writes persistent notes, but no S4-specific adoption owner is wired.
- Supporting / enforcement mechanisms: Project-scoped Memory tool, LLM context compaction, provider settings, configurable user hooks, MCP and optional named agents.
- Closure path: Saved notes can inform later task prompts; no future-environment option comparison and adopted capability or governance change is executed from first-party feedback.
- Boundary reachability: Installed memory and config can be used during normal operation, but their existence does not establish a positive prospective adaptation loop.
- Why this is / is not agent-owned: Remembering test commands, switching providers or handling a prompt are operational supports, not S4 unless outside-and-future adaptation is decided and realized.
- Evidence: [internal/tool/memory.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/memory.go); [internal/agent/compact.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/compact.go); [internal/config/config.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/config/config.go); [internal/agent/subagent.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/subagent.go); [README.md](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/README.md)
- Basis: bounded structural negative
- Confidence: moderate
- Caveats: This is frozen Go-source analysis; no source Go test execution or provider-backed multiagent collision run was attested.

### Absence scope

- Surfaces inspected: Project Memory, context compaction, agent selection, hooks and MCP config.
- Plausible first-party paths checked: Prospective intelligence distinguishing future external conditions, adaptation judgment/decision and feedback into changed future organizational capability.
- Why no material first-party path remains: Observed features preserve/use context and operator-defined extensions; first-party mechanism for future adaptation adoption is not found.

## S5 — Policy and identity

- State: —
- Function: No ultimate identity/purpose/policy owner closes an authoritative organization-level governance loop in the shipped harness.
- Disturbance / variety regulated: Unsafe tool requests, access to protected paths, command execution outside working directory and operational spend risks.
- Decisive decision or feedback right: Determine ultimate legitimate policy and organizational identity and return a binding decision governing subsequent operation.
- Decision owner: Operator or configuration sets tool permissions and workspace envelope; gate enforces rights for individual calls, not a first-party whole-agent-organization policy owner.
- Supporting / enforcement mechanisms: Manual/accept-edits/plan/bypass permissions, allow/deny rules, workspace path normalization, approval dialogs, inherited child gate and max spend.
- Closure path: Protected operation → static rule or per-tool user consent → allow/deny the tool call; no separate ultimate identity/policy matter is adjudicated then returned to later organization-wide governance.
- Boundary reachability: No qualifying positive S5 mode despite user permissions and sandbox protections being present in standard installation.
- Why this is / is not agent-owned: A permission dialog and deny rule are operational guardrails, not a legitimate final identity/policy decision loop; generic human presence alone does not create S5=P.
- Evidence: [internal/permission/gate.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/permission/gate.go); [internal/permission/permission.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/permission/permission.go); [internal/tool/workspace.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/tool/workspace.go); [internal/agent/agent.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/agent.go); [internal/agent/task.go](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/internal/agent/task.go); [README.md](https://github.com/zenodea/zaino/blob/f842bd0589471972bf680aaa35a8a6159eb8c8df/README.md)
- Basis: bounded structural negative
- Confidence: moderate
- Caveats: This is frozen Go-source analysis; no source Go test execution or provider-backed multiagent collision run was attested.

### Absence scope

- Surfaces inspected: Permission modes and requests, workspace policies, inherited child gates, budget enforcement, operator settings.
- Plausible first-party paths checked: Explicit ultimate identity dispute → legitimate parent/system authority → authoritative policy resolution → feedback into organizational operation.
- Why no material first-party path remains: Shipped permissions decide only tool effects within operator-predefined bounds. No independent whole-organization ultimate policy authority/closure was established.

## Recursion

Model-guided children are separable operational S1 cells in one local workspace; they do not independently demonstrate a full higher-recursion viable organization, S3 or S5 ownership.

## Variety and escalation

Variable coding tasks and tool feedback are handled by S1. In the installed shared workspace, simultaneous file-writer variety among distinct S1 cells can be attenuated by deterministic path locks and stale-base refusal, with error returned for subsequent reread/rework. Budget and user approval are operational constraints, not a new VSM function without function-specific closure.

## Evidence gaps

1. No Go toolchain in the source inspection host: code and first-party test fixtures were inspected, but neither multiagent race nor tests were executed in this environment.
2. The S2=C claim is limited to the shared concrete file-write collision path in standard first-party child/runtime tools; it is not a claim of distributed-organization conflict resolution, perfect atomicity for all shell edits or agent-owned policy.
3. User-provided hooks, MCP implementations, private deployments and future repository evolution were excluded; cannot donate unverified higher-function states.
