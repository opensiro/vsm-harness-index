---
harness_id: wardayacode
project_name: WardayaCode
repository: https://github.com/fawwazmw/wardayacode
review_ref: e2758f09fc706669e5be7cdc1a0ca4e957f02058
reviewed_at: 2026-10-14
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# WardayaCode

## Review boundary

- System in focus: the installable WardayaCode TypeScript/Node terminal coding agent at frozen `e2758f09fc706669e5be7cdc1a0ca4e957f02058`, including its first-party `Agent` model-tool loop, locally registered coding tools, tool permissions, sessions, context compaction, hooks/skills and MCP support.
- Purpose and identity: perform user-requested software-development tasks in a local repository with model-selected tool usage subject to operator-defined permissions.
- Relevant environment: task instructions and project files, model-provider output, shell/code tool results and errors, user approvals, project context, saved sessions and configured extensions.
- Standard-distribution boundary: packaged `wardayacode` CLI, first-party `src/agent/`, `src/tools/`, permissions, session/context and supplied extensibility infrastructure. External inference APIs, third-party MCP servers, user-installed custom hooks/skills, other coding agents, the shell environment, and upstream development/CI are dependencies, not independent first-party function owners.
- Credited operating / distribution surfaces: `src/cli.ts`, `src/agent/Agent.ts`, built-in tools/registry, `src/permissions/PermissionSystem.ts`, `src/context/ContextManager.ts`, `src/session/`, `src/extensibility/`, `src/mcp/`, `src/ui/SlashCommands.ts` and provider adapters.
- Adjacent first-party surfaces excluded from ownership: tests and CI, branch/release strategy, contributor governance, example documentation and project setup content, unshipped custom agent implementations, external programs/tools exposed through a user's shell or MCP.
- First-party operating / deployment modes considered: standard interactive TUI with default, plan, acceptEdits and auto permission modes; resumed session, checkpoint/undo, configured hooks/skills/MCP, model/provider switching and basic project initialization. The shipped product does not instantiate a first-party worker fleet in the reviewed code.
- Recursion level: one installed terminal coding session with one model-directed worker S1 and its local action/permission/context machinery.
- Reviewed revision: `e2758f09fc706669e5be7cdc1a0ca4e957f02058` (frozen intake #898; no repinning to latest upstream).
- Observation date: 2026-10-14.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`Agent.run` constructs model-visible first-party tool definitions and calls the Vercel AI SDK `streamText` with `maxSteps` controlling the bounded tool-use sequence. For a tool call, `executeTool` runs pre-tool hooks, consults `PermissionSystem`, executes the named `ToolRegistry` tool and returns a serialized result to the model. Coding tools include read/write/edit, bash, git, glob/grep and file listing. Thus the model/tool/observation loop is first-party, while providers furnish inference only.

`PermissionSystem` defines normal, read-only planning, edit-approving and auto modes, with per-tool/user-prompt decisions, persistent *in-session* allowlist and optional sandbox restrictions. The CLI/TUI handles session continuity and user commands for model, permissions, statistics, diff/undo, checkpoints and project initialization. `Session` stores append-only JSONL; `ContextManager` truncates old results or windows and is not an adaptation department. `HookSystem` and `SkillSystem` provide interception/discovery for user-supplied capabilities; an external MCP client can expose more tools but does not make another first-party decision-owning S1. No model-backed independent S3* audit actor or separate S3/S4/S5 management loop is instantiated by default.

Evidence: [`README.md`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/README.md); [`src/agent/Agent.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/agent/Agent.ts); [`src/tools/ToolRegistry.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/tools/ToolRegistry.ts); [`src/permissions/PermissionSystem.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/permissions/PermissionSystem.ts); [`src/context/ContextManager.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/context/ContextManager.ts); [`src/session/Session.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/session/Session.ts); [`src/extensibility/HookSystem.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/extensibility/HookSystem.ts); [`src/extensibility/SkillSystem.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/extensibility/SkillSystem.ts); [`src/ui/SlashCommands.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/ui/SlashCommands.ts); [`src/mcp/McpManager.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/mcp/McpManager.ts).

## Operational model

An operator supplies coding objectives. The model owns task-specific choices to inspect/edit/execute and can adapt its next tool call to workspace observations; the executable tools and permission gates transport/enforce those decisions. Per-session plans, review UI and user preferences are not whole-organization S3 or S5. There is no first-party second operations unit whose interference must be attenuated, nor a supported autonomous or parent-owned function-specific higher-metasystem mode.

## S1 — Operations

- State: A
- Function: transform coding request and uncertain workspace state into model-selected software-development operations.
- Disturbance / variety regulated: unknown source structure, bugs, compiler/shell feedback, changing files, model/provider responses and tool execution failures.
- Decisive decision or feedback right: choose task-relevant coding tools/actions and revise the next action based on concrete output.
- Decision owner: the instantiated model-directed WardayaCode `Agent`, with configured LLM endpoint as a dependency, not a third-party coding harness.
- Supporting / enforcement mechanisms: Vercel AI SDK streamed steps, local ToolRegistry, adapters, pre/post hooks, permission policy, context and session support.
- Closure path: user request + code observations → model-selected tool call → first-party registry/permission/execution → returned result/error in model context → subsequent model choice or completion.
- Boundary reachability: `src/cli.ts` starts the agent class and registers the project's built-in tools in the shipped terminal distribution. `Agent.run` and `executeTool` are actual source code, not roadmap examples.
- Why this is / is not agent-owned: removing model-directed tool selection leaves deterministic tool execution and permission policy, but no equivalent task-responsive coding action policy.
- Evidence: [`src/agent/Agent.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/agent/Agent.ts); [`src/cli.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/cli.ts); [`src/tools/ToolRegistry.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/tools/ToolRegistry.ts); [`src/tools/index.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/tools/index.ts); [`README.md`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: S1 autonomy does not imply tested effectiveness or safety and does not promote permission/telemetry machinery into S3-S5.

## S2 — Coordination

- State: —
- Function: no first-party control path attenuating interference between separate operational S1 agents at this session boundary.
- Disturbance / variety regulated: conflicting concurrent independent coding workers, were such workers configured, but the standard product does not instantiate them.
- Decisive decision or feedback right: no inter-S1 interference-specific arbitration choice is wired into the shipped runtime.
- Decision owner: not established; external agent coordination may be supplied by a caller or MCP but is outside the declared system-in-focus.
- Supporting / enforcement mechanisms: one agent's serial/bounded model tool-use steps, hook ordering, session files, path/permission controls and user project context.
- Closure path: tool results return to the same S1 model; no inter-S1 disturbance-specific attenuation feedback changes another S1's subsequent behavior.
- Why this is / is not agent-owned: single-agent tool sequencing and approvals operate *inside one S1* rather than regulating independently acting workers.
- Evidence: [`src/agent/Agent.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/agent/Agent.ts); [`src/tools/ToolRegistry.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/tools/ToolRegistry.ts); [`src/extensibility/HookSystem.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/extensibility/HookSystem.ts); [`README.md`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/README.md).
- Basis: structural
- Confidence: high
- Caveats: MCP tool discovery is not an owned multi-agent coordination loop.

### Absence scope

- Surfaces inspected: model/tool loop, registry and tools, sessions, hook/skill/MCP extension points and documented CLI modes.
- Plausible first-party paths checked: spawning distinct model agents, maintaining concurrent worker state, cross-worker conflict/oscillation detection and corrective coordination feedback.
- Why no material first-party path remains: the frozen shipped code instantiates a single model-directed coding agent; externally supplied extensions could implement a fleet, but no standard-distribution S2-specific response is wired.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current operational management over a population of S1 units.
- Disturbance / variety regulated: competing present obligations or resource commitments across multiple operations, which would require a whole-current view and return.
- Decisive decision or feedback right: the current agent plans *one task*, and user permissions restrict *individual actions*; neither is shown making whole-system current portfolio trade-offs.
- Decision owner: none established for S3; operator owns permissions at the task-tool boundary, not a multi-S1 parent supervision loop.
- Supporting / enforcement mechanisms: `/status`, usage/cost summaries, session lists, current-model selection, permission changes, checkpoint and retry limits.
- Closure path: per-task/user UI commands alter the same run; no whole-system current decision returns to regulate multiple independent S1 commitments.
- Why this is / is not agent-owned: model task planning and deterministic policy/usage monitoring are not S3 current control over a wider organization.
- Evidence: [`src/agent/Agent.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/agent/Agent.ts); [`src/ui/SlashCommands.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/ui/SlashCommands.ts); [`src/permissions/PermissionSystem.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/permissions/PermissionSystem.ts); [`src/session/SessionManager.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/session/SessionManager.ts); [`README.md`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: supported human approvals may unblock one tool, but do not constitute parent-governed S3 at the declared recursion.

### Absence scope

- Surfaces inspected: agent loop, slash commands/status, local session management, permission modes, hooks, checkpoints and context.
- Plausible first-party paths checked: current roster/commitments, fleet-wide resource reassignment, multi-agent supervision and a parent with a whole-current operational return channel.
- Why no material first-party path remains: the shipped surfaces expose only a single coding task/actor plus local support and operator per-action controls.

## S3* — Complementary audit

- State: —
- Function: no independently owned evidence-audit judgment and corrective return separate from the coding actor's ordinary tool/reporting path.
- Disturbance / variety regulated: code defects, incorrectly claimed successful tests, undiscovered regressions or incomplete changes.
- Decisive decision or feedback right: the same coding agent or operator can inspect diffs and run tests; the shipped `/review` command lists PRs, not a separate source-first auditor with consequential rejection.
- Decision owner: no first-party complementary audit owner established.
- Supporting / enforcement mechanisms: diff/checkpoint viewer, git tooling, test-capable bash commands, optional hook gates and permission prompts.
- Closure path: one actor may request tests, read diffs or receive user feedback, but no distinct independent inspection → challenged finding → corrective management action loop is wired.
- Why this is / is not agent-owned: ordinary self-testing, visual diff review and arbitrary user hooks do not supply another evidence owner.
- Evidence: [`src/ui/SlashCommands.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/ui/SlashCommands.ts); [`src/tools/DiffView.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/tools/DiffView.ts); [`src/tools/GitTool.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/tools/GitTool.ts); [`src/agent/Agent.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/agent/Agent.ts); [`src/extensibility/HookSystem.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/extensibility/HookSystem.ts); [`README.md`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: a separate reviewer *could* be integrated with user MCP/hook extensions but is not shipped as a closed first-party system.

### Absence scope

- Surfaces inspected: `/review`, diff/checkpoint/rollback commands, tool/test paths, hooks, model loop, README supported features and project source tree.
- Plausible first-party paths checked: separate reviewer model, acceptance gate owned by a distinct verifier, independent raw-artifact audit with returned corrective work.
- Why no material first-party path remains: the product ships file/diff inspection and task tools only, without any first-party reviewer-runner or independent corrective verification pipeline.

## S4 — Outside-and-then intelligence

- State: —
- Function: no operational outside-and-prospective adaptation cycle that changes WardayaCode's organizational capabilities from environmental intelligence.
- Disturbance / variety regulated: shifting tools, user repository conventions and future external threats/opportunities could warrant system-level adaptation.
- Decisive decision or feedback right: the model can research or analyze a present task and user can configure a new skill/model; no shipped future-capability adaptation owner is established.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: skills loaded from file, project context, user configuration, context trimming, session persistence, provider selection and update checks.
- Closure path: saved context or user config influences later task execution but no external prospective distinction → selected adaptation option → returned organizational capability update is wired.
- Why this is / is not agent-owned: summarizing a current conversation, choosing a provider, or applying a user-authored skill is not an autonomous S4 future-orientation.
- Evidence: [`src/context/ContextManager.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/context/ContextManager.ts); [`src/extensibility/SkillSystem.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/extensibility/SkillSystem.ts); [`src/extensibility/skillLoader.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/extensibility/skillLoader.ts); [`src/config/defaults.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/config/defaults.ts); [`src/utils/updateCheck.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/utils/updateCheck.ts); [`README.md`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/README.md).
- Basis: structural
- Confidence: high
- Caveats: project `/init` and new future skills would be a different assessed capability only if first-party prospective and adoption closure were established.

### Absence scope

- Surfaces inspected: context/compaction, session persistence, model/provider configuration, skills/hooks/MCP, `/init`, package update checks and README.
- Plausible first-party paths checked: environmental scouting, future option generation, autonomous evaluation/selection of new organizational capabilities, durable adopted practice that changes future management/operation.
- Why no material first-party path remains: current source supports user-defined extensions and present-task memory or startup configuration, not a first-party future-oriented organizational intelligence and adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no first-party closure over an ultimate identity/purpose or constitutional policy issue of the installed coding organization.
- Disturbance / variety regulated: unsafe file operations and authorization scope are important, but only routine operational constraints here.
- Decisive decision or feedback right: operator can choose tool permission mode or approve an action; no legitimate identity-level policy authority/return is built in.
- Decision owner: user configuration and per-tool prompt for operational authorization; no S5-specific decision owner.
- Supporting / enforcement mechanisms: four permission modes, session allowlist, sandbox restrictions, hook veto and project config.
- Closure path: allowed/denied tool calls reflect user settings, but no identity-level issue reaches a legitimate parent, receives a constitutional decision and returns as durable ultimate-policy governance of later operation.
- Why this is / is not agent-owned: the model cannot authoritatively redefine purpose/identity from permission behavior; runtime only enforces an external operational envelope.
- Evidence: [`src/permissions/PermissionSystem.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/permissions/PermissionSystem.ts); [`src/config/defaults.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/config/defaults.ts); [`src/extensibility/HookSystem.ts`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/src/extensibility/HookSystem.ts); [`README.md`](https://github.com/fawwazmw/wardayacode/blob/e2758f09fc706669e5be7cdc1a0ca4e957f02058/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: human codebase authority or maintainer project governance outside the installed CLI must not be borrowed into S5.

### Absence scope

- Surfaces inspected: permission rules, sandbox toggles, hook veto, config cascade, user slash commands and default model instruction.
- Plausible first-party paths checked: policy/identity proposals, authoritative human-parent decision, escalation/appeal on constitutional purpose and returned durable governing policy.
- Why no material first-party path remains: the first-party paths provide per-tool authorization/settings only; the required ultimate-purpose/policy dispute and return loop is not shipped.

## Distributed OSS parent arrangement

Contributors maintain the upstream codebase, but distributed developer governance is not operationally wired as a single parent authority for a user's installed coding session. Multiple independent installations do not share a first-party organization state.

## Self-hosted and non-human modes

Users may run a locally installed terminal session in `auto` mode, with less frequent tool approvals, or in `plan` mode, with no writes. These affect S1 permission scope, not the existence of distinct S3/S4/S5 parent-governed modes. No `(P)` is claimed.

## Recursion

The reviewed CLI instantiates one coding-agent operational cell with supporting model/tool/context structures. No nested viable system is inferred from a long conversation, multiple provider adapters, MCP tools or reusable skills.

## Variety and escalation

The model handles coding variety through tool selection and tool-result feedback. Permission controls, sandbox mode, retry limits and context compaction attenuate risk/resource variety. Asking a human to approve a tool is a local authorization escalation, not by itself an algedonic channel or higher metasystem.

## Evidence gaps

- Source-first static assessment only; this execution did not run a live model/inference benchmark or certify software correctness.
- A separately supplied MCP server or user-authored hook/skill could realize additional organizational functions outside this frozen first-party standard-distribution boundary; that possible extension does not make the bundled S2-S5 states unknown by itself.
