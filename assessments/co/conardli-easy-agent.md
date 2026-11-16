---
harness_id: conardli-easy-agent
project_name: Easy Agent
repository: https://github.com/ConardLi/easy-agent
review_ref: 48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Easy Agent

## Review boundary

- System in focus: One installed Easy Agent coding session, including its opt-in team of named background agents.
- Purpose and identity: Use configured model providers and workspace tools to investigate and change software.
- Relevant environment: User requests, project worktree and tooling, provider responses, tool results and concurrent teammates.
- Standard-distribution boundary: Shipped terminal CLI, session SDK and built-in agent/team, permission and context machinery.
- Credited operating / distribution surfaces: Interactive and headless model/tool execution, optional Agent Teams and interactive operator controls.
- Adjacent first-party surfaces excluded from ownership: Maintainer governance, release/test assets, examples and separately supplied user or plugin code.
- First-party operating / deployment modes considered: Interactive CLI, headless CLI, session SDK, and installed opt-in Agent Teams.
- Recursion level: One configured coding session or team, with agent-led task units inside the team.
- Reviewed revision: `48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c`
- Observation date: 2026-11-16
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Easy Agent ships a Node CLI and session SDK. QueryEngine invokes an agentic loop that keeps model and tool results in the active conversation. The Agent Teams mode adds agent task ownership, persistent team state, peer messages and lifecycle controls. Permissions, hooks and workspace trust delimit available actions. Durable project memory can enter later model prompts. [`package.json`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/package.json#L1-L22), [`src/core/queryEngine.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/core/queryEngine.ts#L1-L31), [`src/core/agenticLoop.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/core/agenticLoop.ts#L1094-L1129), [`docs/agent-teams.md`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/docs/agent-teams.md#L1-L15), [`src/context/systemPrompt.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/context/systemPrompt.ts#L296-L335).

## Operational model

The lead model selects coding operations. Named background teammates operate their own model loops and acquire work from one team task graph. Team members choose work and dependencies within allocated authority, the lead can intervene in current team commitments, and the operator can stop an active background task through the supported UI.

## S1 — Operations

- State: A
- Function: Complete a coding task with iterative workspace and tool actions.
- Disturbance / variety regulated: Project and request uncertainty, tool outputs and errors.
- Decisive decision or feedback right: Choose tools and next actions after observation.
- Decision owner: The session model, or the corresponding model in a teammate unit.
- Supporting / enforcement mechanisms: Provider adapter, permission gate, allowed tools and session state.
- Closure path: Tool execution yields tool results back into conversation state for another model turn.
- Why this is / is not agent-owned: Without the model, the available tools and permission rules do not choose a sequence of workspace operations.
- Evidence: [`package.json`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/package.json#L1-L22), [`src/core/agenticLoop.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/core/agenticLoop.ts#L721-L735), [`src/core/agenticLoop.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/core/agenticLoop.ts#L1080-L1129), [`src/agents/runAsyncAgent.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/agents/runAsyncAgent.ts#L157-L197)
- Basis: structural
- Confidence: High for installed runtime wiring.
- Caveats: Execution depends on the selected provider and workspace grants.
- Boundary reachability: The packaged terminal CLI and SDK use the shipped session and model/tool loop.

## S2 — Coordination

- State: A
- Function: Stabilize shared task allocation among concurrent named teammates with exclusive runtime claims and model-chosen task updates.
- Disturbance / variety regulated: Multiple teammates can choose the same pending task or start dependent work prematurely.
- Decisive decision or feedback right: Choose a task to claim, release or complete, and express dependencies through task tools.
- Decision owner: Model-backed teammates and team lead within their respective task authority.
- Supporting / enforcement mechanisms: Persistent per-team task graph, scoped identities, serialized claims and dependency enforcement.
- Closure path: Failed competing claims or dependency checks return ownership or blocker errors to the calling model. Once the owner closes or releases a task, subsequent claims use the new graph state.
- Why this is / is not agent-owned: The runtime serializes writes. The agent chooses what work to claim or release and updates dependencies based on resulting task state.
- Evidence: [`docs/agent-teams.md`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/docs/agent-teams.md#L3-L11), [`src/agents/teamPromptInjection.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/agents/teamPromptInjection.ts#L83-L97), [`src/tools/taskUpdateTool.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/tools/taskUpdateTool.ts#L153-L195), [`src/state/taskStore.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/state/taskStore.ts#L326-L365)
- Basis: structural
- Confidence: High for the optional team task-graph path.
- Caveats: This concerns shared task claims and dependency state. It does not guarantee arbitrary shared file edits are coordinated.
- Boundary reachability: Enable the shipped Agent Teams mode and run named background teammates in its shared task scope.
- Distinct S1 units: Named live teammates with their own model loops and assigned work outcomes.
- Inter-S1 disturbance: Concurrent attempts to own one pending task or work against an unfinished upstream dependency.
- Attenuating coordination relation: Serialized owner and dependency checks joined to agent-visible TaskUpdate errors and current task listing.
- Feedback into subsequent S1 behaviour: The accepting agent receives its claim and runs the work. An unsuccessful agent receives a corrective owner/blocker result and can choose available work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A direct ownership conflict changes whether each agent can acquire the same work.

## S3 — Inside-and-now control

- State: A(P)
- Function: Change active team commitments from a current team-wide view.
- Disturbance / variety regulated: Stale, blocked or unproductive agents occupying active work and retaining task claims.
- Decisive decision or feedback right: Choose a live commitment to stop and whether to reassign its released work.
- Decision owner: Model lead in team tool mode, or local session operator through the separate background-agent UI.
- Supporting / enforcement mechanisms: Team status in prompt, current task graph, scoped lifecycle store, shutdown/abort signaling and task release.
- Closure path: Stopping ends the chosen worker run. Finalization returns unfinished claims and sends terminal status, allowing subsequent work decisions.
- Why this is / is not agent-owned: Deterministic lifecycle code enforces the stop; the lead or operator selects the target according to the current team situation.
- Evidence: [`src/agents/teamPromptInjection.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/agents/teamPromptInjection.ts#L60-L97), [`src/tools/sendMessageTool.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/tools/sendMessageTool.ts#L184-L224), [`src/agents/runAsyncAgent.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/agents/runAsyncAgent.ts#L340-L376), [`src/ui/hooks/useTeammateNavigation.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/ui/hooks/useTeammateNavigation.ts#L112-L143), [`src/sdk/session/controller.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/sdk/session/controller.ts#L534-L544)
- Basis: structural
- Confidence: High for scoped stop authority and returned workload change.
- Caveats: Scope is the current team, with no whole-organization budget authority inferred.
- Boundary reachability: The installed team option exposes lead controls; the interactive session presents its active background agents and scoped stop action.
- Whole-system current view: The lead receives roster status and the shared task state. The operator's teammate picker exposes active background agents in the current session.
- Current-control decision scope: Stop or allow live teammate commitments to continue and make unfinished work available to the team.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Team lead model | Current roster/task evidence calls for intervention | Lead selects shutdown or abort. Finalization releases unfinished work and reports back. | [`src/tools/sendMessageTool.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/tools/sendMessageTool.ts#L184-L224), [`src/agents/runAsyncAgent.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/agents/runAsyncAgent.ts#L340-L376) |
| Parent (`P`) | Interactive workspace operator | Operator reviews active teammate roster and selects a run to stop | Picker invokes scoped session abort, after which the lifecycle settles and returns claims. | [`src/ui/hooks/useTeammateNavigation.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/ui/hooks/useTeammateNavigation.ts#L112-L143), [`src/sdk/session/controller.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/sdk/session/controller.ts#L534-L544), [`src/agents/runAsyncAgent.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/agents/runAsyncAgent.ts#L340-L376) |

## S3* — Complementary audit

- State: —
- Function: No supplied complementary audit function was established.
- Disturbance / variety regulated: A teammate report could differ from actual artifact or effect.
- Decisive decision or feedback right: No shipping actor is assigned an independent artifact verdict and corrective return for this purpose.
- Decision owner: No first-party audit judgment owner shown.
- Supporting / enforcement mechanisms: Ordinary team status, workspace inspection, Explore and generic shell lifecycle hooks.
- Closure path: The default paths return operation progress, expose observations, or execute operator-supplied commands. An outside checker remains a composition choice.
- Why this is / is not agent-owned: A user or developer can assign an audit role or implement an independent hook. The reviewed distribution supplies no dedicated audit-specific composition beyond generic agents and lifecycle callbacks.
- Evidence: [`src/agents/builtIn/explore.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/agents/builtIn/explore.ts#L20-L59), [`src/agents/runAsyncAgent.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/agents/runAsyncAgent.ts#L265-L295), [`src/hooks/runHooks.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/hooks/runHooks.ts#L220-L261), [`docs/hooks.md`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/docs/hooks.md#L20-L26), [`src/tools/teamCreateTool.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/tools/teamCreateTool.ts#L61-L76)
- Basis: structural
- Confidence: Moderate within the shipped distribution.
- Caveats: A configured independent auditor could use this infrastructure.

### Absence scope

- Surfaces inspected: Bundled built-in agents, background output and worktrees, team instructions, Stop/SubagentStop hooks and terminal diff/rewind.
- Plausible first-party paths checked: Read-only Explore, reviewer as a supplied role, hook cancellation feedback and artifact access in an optional worktree.
- Why no material first-party path remains: Explore is a code discovery unit. The hook has a lifecycle event and optional model return, but its event carries a final message and metadata and delegates any independent evidence acquisition and judgment to caller-written code. The reviewer roles are user-supplied examples.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party capability adaptation process was established at the assessed recursion.
- Disturbance / variety regulated: User corrections, future project needs and stale contextual facts can affect later model decisions.
- Decisive decision or feedback right: The model can select and verify remembered guidance, with no evidenced shipped pathway developing and resolving distinct future capability options.
- Decision owner: Model or user chooses retained context, but no S4-specific decision owner is established.
- Supporting / enforcement mechanisms: Project memory instructions and loader, user configuration, resources and extension mechanisms.
- Closure path: Records enter later prompts and can inform operations. The evidenced path concerns what context to retain and retrieve.
- Why this is / is not agent-owned: Memory selection is agentic when the model chooses it. The source does not close a prospective capability tradeoff with a returned adaptation decision.
- Evidence: [`src/context/memory/memoryTypes.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/context/memory/memoryTypes.ts#L24-L75), [`src/context/systemPrompt.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/context/systemPrompt.ts#L296-L335), [`docs/configuration-security.md`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/docs/configuration-security.md#L3-L29), [`README.md`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/README.md#L53-L68)
- Basis: structural
- Confidence: Moderate.
- Caveats: User-authored skills or separate adaptation tooling can add capability outside this witness.

### Absence scope

- Surfaces inspected: Memory persistence and recall guidance, prompt reconstruction, configuration, resources, tool/plugin loading and session plan/execute.
- Plausible first-party paths checked: Retaining user feedback, validating stale references, project convention reload and manually sourcing a new plugin.
- Why no material first-party path remains: The shipped closure selects context and makes user-configured resources available. The reviewed runtime has no evidenced mode that models future operating changes and decides which capability adaptation to return into operation.

## S5 — Policy and identity

- State: —
- Function: No installed ultimate-policy adjudication loop was established.
- Disturbance / variety regulated: Workspace trust, plan acceptance and tool restrictions bound operating behavior.
- Decisive decision or feedback right: Operator approves workspace trust and tool/plan actions. The managed-policy source supplies settings from outside the session.
- Decision owner: Local operator and administrator own their respective settings, with no evidenced runtime ultimate-policy deliberation role.
- Supporting / enforcement mechanisms: Trust prompt and stored state, policy precedence, permission modes and plan approvals.
- Closure path: Trust state influences whether project settings may load. Approvals feed the corresponding tool or task. Managed configuration bounds execution.
- Why this is / is not agent-owned: The available decisions govern particular operating settings and actions. No route is evidenced for resolving and returning a matter of the session's ultimate purpose or authority.
- Evidence: [`docs/configuration-security.md`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/docs/configuration-security.md#L3-L30), [`src/entrypoint/cli.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/entrypoint/cli.ts#L279-L310), [`src/tools/exitPlanModeTool.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/tools/exitPlanModeTool.ts#L92-L125), [`src/harness/resolve.ts`](https://github.com/ConardLi/easy-agent/blob/48314ccec4b3bbbd119ceebb4c62eebc90bc8d3c/src/harness/resolve.ts#L299-L318)
- Basis: structural
- Confidence: Moderate for the assessed local runtime.
- Caveats: The broader deploying institution and its policy-making process are outside this boundary.

### Absence scope

- Surfaces inspected: Workspace trust, managed settings precedence, on-demand plan approvals, prompt identity configuration and OSS repository governance.
- Plausible first-party paths checked: Project trust as a parent return, managed policy selection and authoring of the agent identity prompt.
- Why no material first-party path remains: The runtime consumes an administrator's policy and returns local permission decisions. It does not route unresolved ultimate policy to a legitimate decision-maker and return a canonical resolution into the assessed session.

## Distributed OSS parent arrangement

The interactive operator controls the local task/team session. Maintainers and independent plugin authors are outside the runtime boundary.

## Self-hosted and non-human modes

The package supports local CLI or embedding with configured model providers. Team ownership can stay with the model lead in the evidenced opt-in path, and the TUI adds the local parent intervention mode.

## Recursion

The session is the assessed whole. Named teammates are local operational units. Separate users or organization-wide deployments are out of scope.

## Variety and escalation

Model/tool feedback, task ownership conflicts, team status, shutdown requests, and ordinary operator approvals address scoped disturbances. The stop and approval paths do not establish a separate algedonic channel.

## Evidence gaps

This is a source-only assessment of the frozen revision. Provider behavior and temporary backend configuration were not exercised.
