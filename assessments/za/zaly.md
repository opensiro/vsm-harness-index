---
harness_id: zaly
project_name: zaly
repository: https://github.com/folke/zaly
review_ref: a568c033de6418e5a24193f41ae8335ce0ddb2b2
reviewed_at: 2026-10-22
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
autonomy_s5: —
---

# zaly

## Review boundary

- System in focus: shipped first-party `@zaly/cli` terminal coding application, using `@zaly/agent` model/tool runtime and the currently enabled `packages/config/src/defaults.ts` tools, not an arbitrary SDK-embedded custom agent constellation.
- Purpose and identity: resolve user coding requests with local file/search/bash tools in a persistent terminal session and safely continue work after outputs, errors or background completion.
- Relevant environment: user workspace, host shell, model/provider API, tool outputs, sessions/history, current files, permission presets, user/project configuration and enabled optional resources.
- Standard-distribution boundary: `packages/cli`, `packages/agent` and `packages/config` current first-party wiring, with optional SDK abilities distinguished from selected CLI defaults.
- Credited operating / distribution surfaces: terminal chat UI, `Agent` model stream/step loop, selected file/read/edit/bash/search tools, `Tasks` background execution with heartbeats/results, session resume/compaction, permission manager, skills/resource loader and project config.
- Adjacent first-party surfaces excluded from ownership: developer/test fixture and future alpha roadmap, separately installed provider/MCP/plugin/skills implementations, user-defined alternative tool lists or SDK harnesses, and dormant `Swarm`/`subagent` components omitted from the distributed CLI default tool selection.
- Operating modes considered: standard fullscreen/scrollback terminal application, restored session, per-run `--tools` overrides and opt-in SDK subagents/Swarm (not silently treated as active CLI ownership), different permission presets, async tool backgrounding and plugin extension seams.
- Recursion level: one default launched zaly coding session and its task-local tool calls, not zaly OSS development governance or a custom multi-agent application built from the library.
- Reviewed revision: [`a568c033de6418e5a24193f41ae8335ce0ddb2b2`](https://github.com/folke/zaly/tree/a568c033de6418e5a24193f41ae8335ce0ddb2b2), frozen intake #200.
- Observation date: 2026-10-22, source inspection only; no configured external model/provider live trial.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The terminal app constructs an `@zaly/agent` instance from active project/user configuration, loads the configured tool collection and invokes the model stream/step loop. The agent executes requested tools under `Tasks` and permission checks, captures results in a session, and continues. Long-running tasks can detach into the task registry and subsequently inject completion/heartbeat messages. This is feedback into one task-performing model, not a second separately viable coding S1.

The monorepo also supplies first-party `subagent` and `Swarm` abstractions. A child can inherit a parent model/tools/permissions and execute an isolated conversation; `Swarm` can route named agent messages and auto-forward outward text. Those are implemented reusable APIs, but the **default** CLI `tools` array expressly comments out `agent_spawn`, `agent_send` and `subagent`; the CLI actually sets `tools.active` from that configuration. Thus the installed default session does not expose model-invokable child spawning or agent messaging. Even an opt-in SDK swarm's message transport is not by itself measured cross-S1 conflict damping or whole-current authority.

Permission presets and explicit allow/ask/deny rules govern tools; static freshness checks protect stale writes. Configurable resource packs, skills and TypeScript plugins expose extensibility, while context masking/compaction preserves local-session continuity. None of those source-backed mechanisms proves external-future strategy or legitimate final policy autonomy.

Primary evidence: [root README/distribution](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/README.md), [CLI creates agent and wires tool list](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/cli/src/app/agent.ts#L15-L68), [default installed tool list](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/config/src/defaults.ts#L40-L68), [model-driven step and tool loop](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/agent.ts#L445-L705), [optional swarm module](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/swarm.ts#L42-L215).

## Operational model

In the selected CLI, one `Agent` chooses the next project action based on user request, session context and tool result. The `Tasks` registry can run or queue tool calls and notify the same model when execution finishes. The operator controls permissions, configuration and project instructions. Source code for alternative multi-agent use exists but is not the product's active default operating topology.

## S1

- State: A
- Function: Perform a user coding request through model-selected inspection, edit, shell and related first-party tools, adapting steps to returned observations.
- Disturbance / variety regulated: Unknown repository organization, user implementation requirements, tool failures, slow process output and session context limits.
- Decisive decision or feedback right: The configured language model selects task-specific tool calls and continuation after returned tool results, while permission checks may reject certain actions.
- Decision owner: First-party `Agent` per-session model loop with configured provider; `Tasks`/tool handlers carry out those decisions.
- Supporting / enforcement mechanisms: Streaming model adapter, default bash/edit/read/write/fetch/find/grep tools, tool result/session injection, background task poll/heartbeat, session JSONL replay, compaction/masking and permissions.
- Closure path: User input → model tool selection → typed tool dispatch → execution result or permission denial → next model step, explicit stop or later task completion injected into session.
- Why this is / is not agent-owned: The model chooses specific coding interventions and follow-up actions; fixed tools, prompts and permission presets constrain but do not replace that operative decision.
- Boundary reachability: Default CLI loads `createAgent` and sets `tools.active` from user/project config defaults; its selected tool handlers execute through the same agent's step loop.
- Evidence: [standard CLI agent construction](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/cli/src/app/agent.ts#L15-L68), [model stream and step](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/agent.ts#L445-L613), [run continuation](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/agent.ts#L650-L750), [background results](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/tasks.ts#L315-L405).
- Basis: structural.
- Confidence: high for first-party model/action wiring; no empirical live completion claim.
- Caveats: Tool safety and task success depend on selected permission preset, provider availability and actual host behavior.

## S2

- State: —
- Function: Dampen real interference among distinct independently viable operational S1 cells and return coordination adjustments.
- Disturbance / variety regulated: Potential file/edit collisions if multiple coding models execute in the same workspace; simultaneous tool calls and task result ordering in one coding loop.
- Decisive decision or feedback right: The default CLI excludes both named swarm agent-spawn/message tools and one-shot `subagent`; no installed inter-S1 conflict arbitration is reachable in that mode.
- Decision owner: None established for a qualifying S2. `Tasks` sequences parallel/nonparallel tool calls and the optional `Swarm` transports messages when separately activated.
- Supporting / enforcement mechanisms: Per-tool `parallel` flags, task chain ordering, user permissions, freshness checks, async completion injection and unselected SDK child/swarm APIs.
- Closure path: Concurrent tools → deterministic task queuing or result notification → same S1 model; no inter-S1 conflict → coordination decision → independently adjusted S1 behavior closure.
- Why this is / is not agent-owned: Transport, lifecycle and tool sequencing are not a dedicated disturbance-regulation function among operating cells; disabled subagent tools cannot be credited as shipped CLI inter-agent control.
- Evidence: [default tools explicitly omit agents](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/config/src/defaults.ts#L46-L69), [CLI loads active defaults](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/cli/src/app/agent.ts#L58-L60), [task call sequencing](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/tasks.ts#L325-L382), [unselected swarm implementation](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/swarm.ts#L143-L213).
- Basis: structural.
- Confidence: high on default tool exposure, medium-high for bounded S2 classification.
- Caveats: An opt-in consumer of the SDK may create operating subagents; that other supported mode needs independent evidence of concrete cross-agent interference and adjustment before grading S2.

### Absence scope

- Surfaces inspected: config default tools, CLI active list, `Agent.child`, one-shot subagent task, `Swarm` route, agent spawn/send tools, concurrent task sequencing and file freshness checking.
- Plausible first-party paths checked: default and custom tool selections, model child invocation, shared workspace, sibling messages, automated reports, async tool tasks and permission preflight.
- Why no material first-party path remains: The installed default omits model-accessible subagents/swarm, while remaining task concurrency is inside one S1; optional SDK messaging supplies no demonstrated interference-specific compensating loop.

## S3

- State: —
- Function: Control current whole-system commitments, resources and priorities across operational divisions.
- Disturbance / variety regulated: Task queue congestion, simultaneous tool usage, session/context budget and pending work.
- Decisive decision or feedback right: No independent whole-current resource/commitment controller is evidenced; the parent coding model chooses individual tasks and users choose model/configuration settings.
- Decision owner: No S3-specific owner in the default single-agent CLI. `Tasks` implements deterministic per-session pending/run/completion statuses.
- Supporting / enforcement mechanisms: Background tasks, task list/poll/stop, session statuses, token accounting, compaction and permission limits.
- Closure path: Task submitted → tool registry executes/queues → result enters one model's context; not a managerial decision over independently operating S1 commitments.
- Why this is / is not agent-owned: Task scheduler mechanics and user controls cannot substitute for whole-current cross-cell decision authority.
- Evidence: [default single root](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/config/src/defaults.ts#L47-L66), [task manager](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/tasks.ts#L120-L154), [CLI user model selection](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/README.md#L21-L39).
- Basis: structural.
- Confidence: medium-high.
- Caveats: The SDK can be embedded in a larger manager; no such separate current-control loop is credited at this boundary.

### Absence scope

- Surfaces inspected: runtime agent loop, task registry, sessions and token pressure, optional child/swarm tools, CLI model/permissions selection.
- Plausible first-party paths checked: current task priorities, background task cancellation, child ownership and shared state, resource caps and user/agent continuation.
- Why no material first-party path remains: No active portfolio of independently viable operating S1s or autonomous whole-current regulator with binding returned reallocation appears in selected mode.

## S3*

- State: —
- Function: Independently verify current-management operating claims against alternative operational reality and return corrective accountability.
- Disturbance / variety regulated: Misleading task completion, unsafe edits, stale file assumptions and inaccurate run history.
- Decisive decision or feedback right: No first-party independent auditor of S3's current-management claim is wired; source tests, permissions and source-read freshness are task-local correctness/support.
- Decision owner: None for S3*; human project reviewers and test suites outside the running agent are adjacent.
- Supporting / enforcement mechanisms: Tool result logs, session/message tree, edit freshness checks, activity status and tests in the developer repository.
- Closure path: Tool/file observation → same operating model or human approval; no S3 → independent alternative reality audit → corrected S3 decision.
- Why this is / is not agent-owned: Inspecting output and enforcing write preconditions increases task reliability but does not create complementary management-audit authority.
- Evidence: [message/session state](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/session/session.ts#L25-L93), [file edit freshness and preflight](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/tools/edit.ts#L75-L145), [default tools](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/config/src/defaults.ts#L47-L65).
- Basis: structural.
- Confidence: medium-high.
- Caveats: An external human or plugin could perform review but is not a packaged S3* operating channel.

### Absence scope

- Surfaces inspected: primary session logs, tool result pathway, edit/read freshness gate, root toolset, possible subagent role extension and developer tests.
- Plausible first-party paths checked: task status, plugin hooks, simulated reviewer via custom subagent, code checks and actual current-management audit rights.
- Why no material first-party path remains: No independent complementary S3 audit is installed; custom reviewer possibilities are not first-party current management verification.

## S4

- State: —
- Function: Observe and model prospective external change, choose adaptation strategies and return new capability commitments through current control.
- Disturbance / variety regulated: Changing project requirements, model-provider capabilities and future workflows could matter to the coding tool.
- Decisive decision or feedback right: The user may change provider/models/tools/resources; the runtime masks or compacts local history. No installed autonomous prospective external-environment options/adoption decision is shown.
- Decision owner: Human and configuration/resource manager for capability selection, not a first-party S4 strategist.
- Supporting / enforcement mechanisms: Provider registry and model switch, skills/plugins, resource pack reload, local token/compaction/masking and user commands.
- Closure path: Current context pressure or user settings → changed local prompt/resources. No external future → evaluated strategic alternative → binding S3 operating return.
- Why this is / is not agent-owned: Hackable plugins, resource loaders and provider choice give extensibility, not agent-owned proactive adaptation to a forecast external environment.
- Evidence: [resource and model customization](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/README.md#L21-L42), [CLI resource load/config](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/cli/src/app/agent.ts#L19-L81), [context masking/compaction](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/agent.ts#L250-L290).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A custom skill could research future change, but that user-installed or task-instructed extension is a different candidate path.

### Absence scope

- Surfaces inspected: agent root/prompt, model selector, compaction/masking, sessions, skills/resource packs, hooks and optional notification/wakeup tools.
- Plausible first-party paths checked: model changing, persistent context, event notifications, background tasks, future wakeups and plugin extensibility.
- Why no material first-party path remains: The first-party product reacts to current tasks or context pressure and exposes human options, but does not own prospective external futures, select adaptation alternatives, and return them through S3.

## S5

- State: —
- Function: Legitimately settle ultimate identity and governing values for the coding organization.
- Disturbance / variety regulated: Dangerous shell commands, editing without authorization, untrusted project instructions and conflicting user preferences.
- Decisive decision or feedback right: Human chooses requested work, tool permissions and default presets. The runtime applies allow/ask/deny and user prompts; it has no legitimate independent final-purpose/policy decision.
- Decision owner: Human operator/project configuration, mediated by deterministic PermissionManager and tool-specific gates.
- Supporting / enforcement mechanisms: Permission presets `strict`, `readonly`, `permissive`, `yolo`, per-tool allow/ask/deny rules and user approval callback.
- Closure path: User/host policy → tool execution preflight → allow, ask or deny local coding action. It is enforcement, not agent-originated ultimate governance with return to S3/S4.
- Why this is / is not agent-owned: Having a default prompt that calls the agent adaptive or a rule engine controlling tools does not authorize redefinition of the organization's identity and values.
- Evidence: [CLI permissions configuration](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/cli/src/app/agent.ts#L20-L52), [PermissionManager and presets](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/packages/agent/src/permissions/manager.ts#L1-L95), [operator warning](https://github.com/folke/zaly/blob/a568c033de6418e5a24193f41ae8335ce0ddb2b2/README.md#L60-L87).
- Basis: structural.
- Confidence: high about preset/human authority; medium-high about S5 absence.
- Caveats: The explicitly permissive `yolo` mode changes protections, not VSM S5 decision ownership.

### Absence scope

- Surfaces inspected: standard CLI default settings, prompts, permission manager, preflight request callback, local project settings, plugin/resource loading and tool denial.
- Plausible first-party paths checked: named permissions, prompt identity, user confirmation, package trust, tool model decisions and configurable resources.
- Why no material first-party path remains: No first-party agent has legitimate final authority over purposes, values or policy tradeoffs; all governing selections remain externally supplied.

## Distributed OSS parent arrangement

The published SDK offers extra capabilities to external consumers, and the GitHub repository has tests and maintainers; these do not become running default CLI S2–S5 rights. User-supplied plugins and models likewise keep their own authority outside the selected organization.

## Self-hosted and non-human modes

zaly can run locally with remote providers and can be configured for broad unattended tool access under `yolo`. Long-running shell tasks and automatic compaction continue without immediate user intervention, but the selected CLI remains one coding-agent loop by default. Opting into custom tool sets may change the operating boundary; no such additional mode is empirically graded here.

## Recursion

One user coding session is the selected S1. Tool backgrounding is below S1 at action-execution recursion. SDK `Swarm` supplies potential additional coding S1 units only in user-selected alternative assembly and cannot be silently imported into default CLI metasystem autonomy.

## Variety and escalation

Tool errors and asynchronous completions return to the model via task results or injected heartbeat/system messages. Permissions constrain risky actions and file freshness prevents obvious stale edits. These are local execution-feedback and protective loops, not independently evidenced inter-S1 coordination or S3–S5 control.

## Evidence gaps

- Frozen-source review; no provider-backed coding run, user-configured SDK swarm or concurrent file-conflict test was executed.
- Optional `Swarm` and `subagent` APIs are real, but excluded from the active CLI tool list at this revision. A later package default or custom configured deployment may need a separate assessment.
- No objective quality/efficiency measurement for model actions, compaction or permissions was claimed.
