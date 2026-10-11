---
harness_id: luckycli
project_name: LuckyCLI
repository: https://github.com/Fenix46/LuckyCLI
review_ref: 496c89124c9a349c36337df35df6581533e26581
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# LuckyCLI

## Review boundary

- System in focus: the first-party LuckyCLI provider-agnostic interactive terminal coding agent and its embedded core agent/tool engine at one local coding session and project, including configurable named, sequential subagents, workflow review/verification commands, local tasks, knowledge/skills graphs, and optional ACP/MCP presentation modes.
- Purpose and identity: carry out uncertain user-specified coding, search, editing and project operations with model-selected actions and explicit human permission for side effects. Optional subagent profiles let a root agent delegate self-contained subordinate tasks while remaining the serialized caller.
- Relevant environment: user repository/working tree, OS/shell and file system, Git diff, third-party model APIs, language toolchains, user approval and project test/build scripts.
- Standard-distribution boundary: npm workspaces `packages/cli` and `packages/core` with their shipped CLI/ACP/interactive entry points, first-party runtime and tool registry, registered sub-agent, verification, plan, task and graph machinery. External provider inference, editor integrations, user organization, public roadmap/feature-tasklist documents, and maintainer CI are excluded as organizational owners.
- Credited operating / distribution surfaces: [package.json](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/package.json); [packages/cli/src/run-cli.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/run-cli.ts); [packages/cli/src/runtime.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/runtime.ts); [packages/cli/src/ui/Root.tsx](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/Root.tsx); [packages/cli/src/ui/hooks/useTurnRunner.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/hooks/useTurnRunner.ts); [packages/core/src/agent/agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agent/agent.ts); [packages/core/src/agents/runner.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agents/runner.ts); [packages/core/src/tools/builtin/spawn-agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/spawn-agent.ts); [packages/core/src/tools/builtin/index.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/index.ts); [packages/core/src/tools/builtin/tasks.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/tasks.ts); [packages/core/src/tasks/store.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tasks/store.ts); [packages/core/src/tools/builtin/verify.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/verify.ts); [packages/core/src/workflow/verify.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/workflow/verify.ts); [packages/cli/src/ui/commands/workflow.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/commands/workflow.ts); [packages/cli/src/workflow-cli.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/workflow-cli.ts); [packages/core/src/workflow/review.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/workflow/review.ts); [packages/core/src/graph/enrich.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/graph/enrich.ts).
- Adjacent first-party surfaces excluded from ownership: [README.md](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/README.md) descriptions are checked against code but are not executable proof; [APP_REFACTOR_PLAN.md](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/APP_REFACTOR_PLAN.md), [FEATURE_TASKLIST.md](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/FEATURE_TASKLIST.md), [ACP_TASKLIST.md](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/ACP_TASKLIST.md) describe planned or tracker work; [.github/workflows/release.yml](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/.github/workflows/release.yml) is maintainer release infrastructure. A user-chosen model/provider, codebase test suite and external editor using ACP/MCP are not imported as separate first-party managers, S3* auditors, future intelligence or policy authorities.
- First-party operating / deployment modes considered: terminal UI, direct CLI runs and ACP; model/tool feedback loop; optional built-in named subagent profiles; workflow `/review`, `/verify`, `lucky review` and `lucky verify`, `verify` tool, optional `verificationMode=after-edit`; task list and plan/user approval; graph indexing/context injection and configurable update flow.
- Recursion level: one LuckyCLI coding installation/session with subordinate self-contained subagent runs. The user software organization and other service providers lie outside its VSM recursion; multiple independent concurrent teammate units are not demonstrated by the sequential child execution path.
- Reviewed revision: 496c89124c9a349c36337df35df6581533e26581.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `packages/core` [packages/core/src/agent/agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agent/agent.ts) class owns a streaming provider/tool loop. `Agent.send` accumulates a transcript and model-selected tool calls, enforces per-tool permission/approval gates, dispatches registered tools, appends real results to model context, retries transient inference errors under safeguards and handles context compaction and interruptions. It can stop after a turn without tools or on explicit abort. [packages/cli/src/runtime.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/runtime.ts) builds and configures this core agent for the first-party CLI, and [packages/cli/src/ui/Root.tsx](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/Root.tsx) makes its turn loop available through the terminal UI.

Subagents are genuinely first-party independently model-directed S1 task runs, not mere prompt strings: [packages/core/src/tools/builtin/spawn-agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/spawn-agent.ts) invokes `runSubAgent` through an injected bridge, and [packages/core/src/agents/runner.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agents/runner.ts) instantiates a second `Agent` with its own provider/model profile, native tools, graph context and tool-feedback loop. But that runner explicitly executes children **sequentially**, one complete task at a time; children have `spawn_agent`, `ask_user` and `present_plan` removed to avoid unmanaged recursion or direct human control. Child reports return to the root, which then decides the next current coding action.

The native [packages/core/src/tasks/store.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tasks/store.ts) persists one-session task state with `pending/in_progress/completed`, while [packages/core/src/tools/builtin/tasks.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/tasks.ts) gives the model tools to create, list and update this task state. The first-party [packages/core/src/graph/enrich.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/graph/enrich.ts) and graph tool paths present source/codebase context, while skill graph and graph update tasks support current coding context. None establishes arbitration between **simultaneously competing operative S1 units** or a current-organization portfolio owner beyond the task-owning root coder.

Verification/review is more than labels but must be mapped to the right organizational boundary. [packages/core/src/workflow/verify.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/workflow/verify.ts) selects trusted installed project scripts and runs concrete checks with structured status. [packages/core/src/tools/builtin/verify.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/verify.ts) exposes it to the same model tool loop. Optionally, [packages/core/src/agent/agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agent/agent.ts) runs the checks automatically after an edit when `verificationMode=after-edit`, appends results to the *same* operational tool observation and marks failure as a tool error. [packages/cli/src/ui/commands/workflow.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/commands/workflow.ts) exposes `/verify` and `/review`, with `/review` sending the diff as a new prompt to the **same** `ctx.agent`; [packages/cli/src/workflow-cli.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/workflow-cli.ts) offers explicit user-invoked `review` and `verify` commands, with a fresh ordinary agent checking a Git diff but reporting to the user/CLI rather than an independent current-organization audit decision owner. [packages/core/src/workflow/review.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/workflow/review.ts) normalizes review findings but does not own an independently selected audit and returned metasystemic control action. These are legitimate verification instruments, not automatically S3*.

## Operational model

LuckyCLI's decisive first-party autonomous role is the coding S1. The model chooses which registered tool or subagent to use, receives actual data and continues. Subagents add temporary independent operational executors but are serial and subordinate to the requesting task, without a concurrent S1 collision channel. The local task list is an S1 planning aid; named profiles are model/provider choices. Runtime approvals and verification enrich the operative loop rather than independently governing multiple S1 commitments or executing an S3* complementary audit.

## S1 — Operations

- State: A
- Function: execute a coding request through iterative native model-directed file/command/search/graph actions and optional independently operated subagent subtasks.
- Disturbance / variety regulated: changes in requested repository work, incomplete context, tool errors, failed verification, codebase structure, model errors and return reports from delegated subtasks.
- Decisive decision or feedback right: select the next first-party tool/delegated task, respond to its result, alter the work path, and decide when the current request is sufficiently complete.
- Decision owner: model running within first-party `Agent.send` of the root or a separately instantiated sequential subordinate `Agent`. The local provider supplies inference but does not own the tool orchestration or terminal workflow.
- Supporting / enforcement mechanisms: tool registry, model transport, transcript/context compaction, permission callback, subagent profile registry, subagent bridge, graph enrichment and ordinary test checks.
- Closure path: user request → model stream with tool calls → local first-party dispatcher → filesystem/shell/graph or child-agent report → concrete tool result appended to active conversation → model chooses another action or final answer.
- Boundary reachability: `packages/cli/src/runtime.ts` builds the main Agent for installed CLI and ACP/TUI; `packages/core/src/agent/agent.ts` directly executes the tool/result continuation; `Root.tsx` creates a reachable child delegation bridge. No third-party coding-agent process is required for the owned S1 loop.
- Why this is / is not agent-owned: without the model's chosen tool call/delegation and interpretation of returned observations, runtime still enforces safety and verifies scripts but cannot autonomously decide the next coding operation.
- Evidence: [packages/core/src/agent/agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agent/agent.ts); [packages/cli/src/runtime.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/runtime.ts); [packages/cli/src/ui/Root.tsx](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/Root.tsx); [packages/core/src/agents/runner.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agents/runner.ts); [packages/core/src/tools/builtin/spawn-agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/spawn-agent.ts); [packages/core/src/tools/builtin/index.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/index.ts).
- Basis: structural + explicit.
- Confidence: high from first-party loop implementations.
- Caveats: evidence establishes a native operational feedback right but not live benchmark performance or universal working provider credentials.

## S2 — Coordination

- State: —
- Function: no native inter-S1 interference/oscillation regulation relation among simultaneously active first-party operational units was established at this recursion.
- Disturbance / variety regulated: subagent write conflicts are avoided by *not running peers at the same time*; there is no separate active multi-worker collision that a dedicated coordinating mechanism observes and attenuates with feedback to both agents.
- Decisive decision or feedback right: main agent chooses the next sequential delegate; the runner completes one child before returning. No peer-claim arbitration, shared multiple-writer lock, cross-agent collision feedback or active conflict attenuation decision owner is supported.
- Decision owner: root operational task agent decides delegation, while deterministic child invocation serializes; neither establishes S2-specific feedback across concurrently active S1s.
- Supporting / enforcement mechanisms: static serial subagent runner, child tools exclusion list, task list, tool permission limits and request/response child summaries.
- Closure path: root awaits completion of one child → report returned → next task selected by the root as an S1 action; no distinct inter-unit disturbances or compensating S2 loop are presented to active peers.
- Why this is / is not agent-owned: model-guided sequencing of one current child is part of the operational task and does not become distinct S2 coordination merely because the tool is called `spawn_agent`.
- Evidence: [packages/core/src/agents/runner.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agents/runner.ts); [packages/core/src/tools/builtin/spawn-agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/spawn-agent.ts); [packages/core/src/tasks/store.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tasks/store.ts); [packages/core/src/tools/builtin/tasks.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/tasks.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: if external users run several installations concurrently, their external coordination is not a native first-party LuckyCLI function.

### Absence scope

- Surfaces inspected: `Agent` root and child execution, subagent restrictions, CLI child bridge, tasks store, native plans, permission tools and workflow review/verify.
- Plausible first-party paths checked: multiple independently running S1 units with shared resource collisions, peer claims, synchronization/lock arbitration, interference signals, independent S1 communication and returned regulation of subsequent choices.
- Why no material first-party path remains: the shipped child runner explicitly executes sequentially; root/child reports and persisted tasks support current coding orchestration without inter-peer conflict arbitration. No other first-party peer-worker relationship with an S2 return is evidenced.

## S3 — Inside-and-now control

- State: —
- Function: no independently owned whole-current organization oversight of simultaneously operating S1 units, commitments and resources was established beyond one user's coding objective.
- Disturbance / variety regulated: the root may split a project into serial subtasks, track local work progress and choose different providers, but that is one S1's delegated implementation rather than system-wide management of multiple ongoing operational units.
- Decisive decision or feedback right: select a named child profile/task, update the local task list and request user approvals; none is a demonstrated whole-current authority over an independent operational workforce.
- Decision owner: the root coder for current task progress, user for consent. No separate first-party S3 management decision right at the declared recursion.
- Supporting / enforcement mechanisms: local tasks, plans, sequential delegations, checkpoint/snapshot and review tool outputs, usage/status panel.
- Closure path: child completion or tool error → root task agent continues ordinary work; no distinct current-organization decision over multiple active S1 resource/commitment obligations is returned to those units.
- Why this is / is not agent-owned: although a model chooses local work order, it does not exercise whole-current control over an operational organization separate from the one coding task.
- Evidence: [packages/core/src/agents/runner.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agents/runner.ts); [packages/core/src/agent/plan.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agent/plan.ts); [packages/core/src/tasks/store.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tasks/store.ts); [packages/core/src/tools/builtin/tasks.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/tasks.ts); [packages/cli/src/ui/Root.tsx](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/Root.tsx); [packages/cli/src/ui/components/TaskPanel.tsx](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/components/TaskPanel.tsx).
- Basis: structural.
- Confidence: medium-high.
- Caveats: generic task planning and model/provider configuration do not establish S3; an external project manager may coordinate multiple independent LuckyCLI instances outside this boundary.

### Absence scope

- Surfaces inspected: main session/coder, child execution and reporting, task stores, planning/user approvals, project graph, multi-provider configuration and workflow commands.
- Plausible first-party paths checked: whole-current portfolio snapshot, active distinct S1 responsibility/resource tradeoffs, global operational prioritization based on reports, owned supervisory decision and consequential return to several independent S1 units.
- Why no material first-party path remains: exactly one operative coding task controls serial children; the available task store and root delegations carry no separate management mandate or return path over multiple active systems.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit judgment/alternative access path that returns findings to a distinct current-control owner is established in this first-party coding installation.
- Disturbance / variety regulated: generated code may fail tests or differ from changed Git diffs; those risks are addressed by ordinary first-party coding verification or user-initiated review and do not establish a separate complementary organizational inquiry.
- Decisive decision or feedback right: current coding loop can choose a `verify` tool or run configured `after-edit` tests; the user can invoke explicit review/verify commands, but no independent audit actor takes an alternative evidentiary mandate and returns an S3* finding to a metasystemic current decision owner.
- Decision owner: project scripts and in-band model supply tests/review text; the producing root agent and/or user decide subsequent ordinary task steps.
- Supporting / enforcement mechanisms: trusted project-script execution, structured result/exit code, mandatory re-entry to the tool transcript after editing when enabled, diff collection, JSON review schema, manual `/review` and `lucky review`.
- Closure path: edit → ordinary script/check status appended to that very tool result (or user-initiated diff review in the same model's session) → coder may retry the failing edit. This is useful testing but not a sufficiently independent, *complementary* audit-control path beyond routine production checks.
- Why this is / is not agent-owned: distinct raw tests can contradict a current edit's apparent success, but `after-edit` is an in-band routine QA hook with no independent auditor selecting substantive evidence or returning a distinct whole-current audit finding. The manual `lucky review` command presents findings to its caller; it does not wire an S3*→S3 control return into ongoing agent execution.
- Evidence: [packages/core/src/agent/agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agent/agent.ts); [packages/core/src/tools/builtin/verify.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/verify.ts); [packages/core/src/workflow/verify.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/workflow/verify.ts); [packages/core/src/workflow/review.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/workflow/review.ts); [packages/cli/src/ui/commands/workflow.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/commands/workflow.ts); [packages/cli/src/workflow-cli.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/workflow-cli.ts); [packages/core/src/tools/builtin/index.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/tools/builtin/index.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: this is not a claim that separate human review or tests are unnecessary or ineffective, only that their witnessed ownership/return does not establish the Profile's organizational S3* at this recursion.

### Absence scope

- Surfaces inspected: `verificationMode`, after-edit injection to operational transcript, verify tool/check-runner, structured review/diff collection and manual CLI/UI commands, subagent runner, permission gates, snapshot/restore support.
- Plausible first-party paths checked: independent reviewer/evaluator invocation, alternative raw-artifact sampling/replay, validator with distinct evidence and accountable audit mandate, findings routed to current organization control and correction rechecked after return.
- Why no material first-party path remains: checks are local task-operation QA and manual reviews use the same live model or isolated user-commanded report; no independent complementary audit actor with a distinct findings-to-S3 control loop is first-party wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective outside-and-then process that creates future capability adaptation alternatives and returns them to current control is evidenced.
- Disturbance / variety regulated: future provider/model availability, changing source structure and codebase knowledge may matter to the developer, but LuckyCLI code reviewed uses them to improve current task context and route immediate inference/tool operations.
- Decisive decision or feedback right: models choose current coding work and provider configurations; deterministic graph index and skill matching gather relevant current repository facts. No owned long-horizon environmental intelligence decision or adaptation-option/return is found.
- Decision owner: current task coder or user for model updates and settings, not a separate first-party S4 function.
- Supporting / enforcement mechanisms: project knowledge graph build/query/update, skill graph matching, context enrichment, update policy/staging, provider catalog and session history.
- Closure path: updated graph facts or installed user-selected release influence current/future prompt context, but no external prospective investigation → adaptation choice → S3 system capability adjustment loop is implemented.
- Why this is / is not agent-owned: persistent memory, code graph refresh and user-initiated software updates are helpful facilities but not prospective organizational intelligence in the VSM sense.
- Evidence: [packages/core/src/graph/enrich.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/graph/enrich.ts); [packages/core/src/graph/update.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/graph/update.ts); [packages/core/src/skills/graph.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/skills/graph.ts); [packages/core/src/update/policy.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/update/policy.ts); [packages/cli/src/update.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/update.ts); [README.md](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: project users may use the tool to research future options, but such tasks alone are not native ongoing system-level adaptation authority.

### Absence scope

- Surfaces inspected: project and skills graph, update policy/staging, provider/model selection, session history, task/delegation, review/verify workflows and README/roadmap.
- Plausible first-party paths checked: future external change detection, comparative adaptation options, choice affecting long-horizon capabilities, bidirectional S4–S3 conversation and consequential implementation.
- Why no material first-party path remains: observed features supply current task context, local maintenance and model/provider selection, not an outside/future strategy process with returned governance of current operations.

## S5 — Policy and identity

- State: —
- Function: no first-party highest-authority identity/ethos decision and binding governance return exists at the installed agent organization boundary.
- Disturbance / variety regulated: local tool risk, provider permissions, user trust and session approval, updates and model selection are handled by configured execution constraints instead of an ultimate-identity dispute.
- Decisive decision or feedback right: human user grants/denies a tool action, software enforces tool permission and approved command scopes; no discretionary S3–S4 identity-level resolution with durable returned policy.
- Decision owner: user for ordinary consent and provider/config settings, deterministic runtime for enforcement, not a verified first-party S5 actor.
- Supporting / enforcement mechanisms: tool permission policy, `approveTool` callback, remembered approvals, session trust prompt, plan presentation and update rules.
- Closure path: action request is allowed/denied and current coding operation continues; no exceptional mission/identity issue reaches a legitimate highest-level authority and returns a binding system-level rule.
- Why this is / is not agent-owned: ordinary approval and persistent configuration are not policy-identity arbitration; no parent governance is inferred solely from user ownership of settings.
- Evidence: [packages/core/src/agent/agent.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agent/agent.ts); [packages/cli/src/approval.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/approval.ts); [packages/cli/src/ui/TrustPrompt.tsx](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/cli/src/ui/TrustPrompt.tsx); [packages/core/src/agent/plan.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/agent/plan.ts); [packages/core/src/update/policy.ts](https://github.com/Fenix46/LuckyCLI/blob/496c89124c9a349c36337df35df6581533e26581/packages/core/src/update/policy.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a human/enterprise organization may govern installations externally; its policy may constrain the program but that does not create a first-party S5 return.

### Absence scope

- Surfaces inspected: native permission and tool decisions, session trust/consent, model configuration, plan approval, update staging, root/subagent limits, source workflow and public docs.
- Plausible first-party paths checked: identity/policy-level conflict, legitimate ultimate decision authority, policy choice balancing current/future requirements and durable consequential return to multiple operating functions.
- Why no material first-party path remains: identified controls concern ordinary tool/mode consent and deterministic safety enforcement, not an implemented ultimate-policy judgment and organizational return.

## Recursion

A single LuckyCLI coding root and its serial subordinate `Agent` calls are the first-party recursion assessed. Subagents may have independent model/tool choices during their assigned operational run, but they are invoked one at a time and cannot delegate further or directly ask users, and their results return to the root. This does not establish a persistent concurrent peer organization or separate S3 management authority. External users, their engineering team and third-party LLMs are distinct systems and are not imported as first-party S5/S4/S3 ownership.

## Variety and escalation

User requests and filesystem/tool results drive S1 variety; the provider abstraction and context graph amplify operational distinctions, while context compaction, test/script feedback and permission prompts constrain action. Failed post-edit tests enter the same tool result and may prompt correction within current coding. An approved `spawn_agent` temporarily delegates a bounded assignment and returns a report; the standard implementation serializes writes rather than regulating conflicts among simultaneously active peers. No independently controlled S3* alternate audit, prospective S4 adaptation or ultimate-policy S5 path is demonstrated.

## Evidence gaps

This is source-first classification of the exact frozen revision and supported first-party modes, not a performance measurement. The local review workspace does not provide a running Node/npm installation, so no live LuckyCLI terminal run or provider-backed invocation is claimed; first-party runtime control was traced through checked-in implementations, CLI wiring and test surfaces. The installed CLI exposes structured verification and manual review features but the inspected control return is in-band to the operative coder or user, not a separate S3* audit. The bounded negatives are restricted to this supported standard-distribution boundary; externally composed teams, external review, custom plugins or future development may implement other VSM loops but do not warrant positive states for this frozen assessed system.
