---
harness_id: xin-code
project_name: Xin Code
repository: https://github.com/xincode-ai/xin-code
review_ref: c5a7969309f7286d1f513caf0821256d4036f4d7
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

# Xin Code

**WORKING DRAFT ONLY — NOT CANONICAL / NOT ADMITTED.** Frozen Index batch [#1842](https://github.com/opensiro/vsm-harness-index/issues/1842), source intake [#860](https://github.com/opensiro/vsm-harness-index/issues/860), row 6. Source-first provisional vector `A / — / — / — / — / —`; incumbent reviewer must make the semantic disposition.

## Review boundary

- System in focus: First-party Go Xin Code terminal coding-agent application in one user's supported installation/workspace/session.
- Purpose and identity: Execute operator-requested coding tasks via model-generated tools, session state, and optional synchronous subagent task delegation.
- Relevant environment: Local source/workspace files, terminal, external provider API, optional MCP servers, local tool permissions, user project instructions.
- Standard-distribution boundary: Shipped Go main executable, first-party model/tool loop, subagent and permissions, session and config; no agentic capabilities borrowed from an external model vendor's own host or third-party plugin implementation.
- Credited operating / distribution surfaces: [main.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/main.go), [agent.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/agent.go), [internal/tool/builtin/register.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/register.go), [internal/tool/builtin/agent_tool.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/agent_tool.go), [internal/tool/builtin/sendmsg_tool.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/sendmsg_tool.go), [internal/tool/executor.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/executor.go), [internal/agent/registry.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/agent/registry.go), [internal/session/session.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/session/session.go), [internal/tool/permission.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/permission.go), [config.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/config.go).
- Adjacent first-party surfaces excluded from ownership: [docs/superpowers/specs/2026-04-02-xin-code-design.md](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/docs/superpowers/specs/2026-04-02-xin-code-design.md), [.github/workflows/build.yml](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/.github/workflows/build.yml), [internal/slash/handler.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/slash/handler.go); roadmap, developer/CI workflows, agent review-as-task and human maintainer choices do not become the installed agent's S3–S5. Third-party provider internal reasoning and optional plugins are not first-party governance owners.
- First-party operating / deployment modes considered: Terminal TUI single-agent runtime, optional synchronous subagents and tasks, prompt review, session resume, user permission modes and optional third-party MCP/skills/plugins.
- Recursion level: One Xin Code coding task organization per local installed runtime; spawned subagents are bounded delegated task cells, not proven autonomous viable subsystems.
- Reviewed revision: [xincode-ai/xin-code@c5a7969309f7286d1f513caf0821256d4036f4d7](https://github.com/xincode-ai/xin-code/tree/c5a7969309f7286d1f513caf0821256d4036f4d7)
- Observation date: 2026-10-22
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The first-party [main.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/main.go) prepares provider/session/configuration, registers tools with [internal/tool/builtin/register.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/register.go) and launches [agent.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/agent.go).
The main Agent.Run cycles from model streaming output to calls through [internal/tool/executor.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/executor.go) and returned tool observations; [internal/session/session.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/session/session.go) maintains the conversation. [internal/tool/builtin/agent_tool.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/agent_tool.go) creates a separate message-history model loop and returns results to the calling parent synchronously. [internal/tool/builtin/sendmsg_tool.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/sendmsg_tool.go) states explicitly that asynchronous child messaging is unsupported. A process-global [internal/tool/builtin/task.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/task.go) stores task entries; [internal/tool/permission.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/permission.go) enforces selected user permission modes. [internal/slash/handler.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/slash/handler.go) implements /review as a prompt to the same agent and /agents,/team as not-yet-implemented stubs. Optional external MCP/tools, user-installed skills/plugins, session memory and hooks add execution/context but do not independently establish higher VSM functions.

## Operational model

An operator requests a coding change; the main model agent chooses task operations using first-party tools, observes outputs and continues, revises or finishes. Synchronous child task execution can be called from one main agent turn; those children share a tool registry and do not form an evidenced separately governed S1 portfolio. Permissions are chosen by the operator and deterministic code enforces them. This assessment does not claim an executed cloud-model benchmark or successful coding task.

## S1 — Operations

- State: A
- Function: Model-guided coding actions and result-responsive tool execution.
- Disturbance / variety regulated: Varying user coding instructions, files, tool failures, and outcomes.
- Decisive decision or feedback right: Model-generated choice of a next tool or response after observing tool output.
- Decision owner: Xin Code main agent/model loop; tool executor performs chosen effects, with human permission when configured.
- Supporting / enforcement mechanisms: Provider adapter, registry, permission checker, result compaction and session persistence.
- Closure path: Prompt → model request → tool calls → tool execution → result messages → next model request; history is saved.
- Boundary reachability: Shipped main.go registers first-party tools and instantiates Agent.Run; no custom external harness required.
- Why this is / is not agent-owned: Without the model-owned next-tool judgment, the first-party host is a command UI, not the coding S1.
- Evidence: [agent.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/agent.go); [main.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/main.go); [internal/tool/executor.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/executor.go); [internal/tool/builtin/register.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/register.go)
- Basis: explicit and structural
- Confidence: high for wiring, no live model benchmark
- Caveats: Frozen source-only analysis; no Go toolchain or provider-backed end-to-end test attested.

## S2 — Coordination

- State: —
- Function: No established inter-S1 interference attenuation/return for separate viable operational units.
- Disturbance / variety regulated: Potential contention between spawned child agents for filesystem/tools, user attention or limited resources.
- Decisive decision or feedback right: A qualifying S2 decision would handle observed competition between distinct S1 units and return an attenuating action to them.
- Decision owner: No decisive S2 owner established; parent agent may delegate work and the executor serializes tool effects.
- Supporting / enforcement mechanisms: Synchronous child-agent tool and registry; permission dialog; read-only tool batching.
- Closure path: Child Agent returns one result synchronously to parent, while SendMessage explicitly rejects asynchronous child messaging; no sibling-conflict feedback to separate S1s.
- Boundary reachability: No positive S2 boundary reachability established.
- Why this is / is not agent-owned: Spawning child models or serializing one turn's mutating tools is not inter-S1 homeostasis.
- Evidence: [internal/tool/builtin/agent_tool.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/agent_tool.go); [internal/tool/builtin/sendmsg_tool.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/sendmsg_tool.go); [internal/tool/executor.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/executor.go); [internal/agent/registry.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/agent/registry.go)
- Basis: structural bounded negative
- Confidence: moderate; source-only
- Caveats: Frozen source-only analysis; no Go toolchain or provider-backed end-to-end test attested.

### Absence scope

- Surfaces inspected: Subagent execution, registry, SendMessage, task store, permission path and shared executor.
- Plausible first-party paths checked: Synchronous parent/child return, explicit child-message unsupported state, concurrent read-tool semantics, child tool resource contention.
- Why no material first-party path remains: No shipped mechanism resolves interference among distinct simultaneously viable S1 units with a returned coordination decision; hypothetical plugin composition is outside this reviewed boundary.

## S3 — Inside-and-now control

- State: —
- Function: No installed whole-system current-control decision over a portfolio of S1 operations and shared commitments.
- Disturbance / variety regulated: Current task states, costs, retries, sessions, resource use and failures.
- Decisive decision or feedback right: A qualifying current-control owner would decide global priorities/resources/commitments in response to a whole-system view.
- Decision owner: No such distinct owner shown; the operator configures budgets/modes, while the model manages a single user task.
- Supporting / enforcement mechanisms: TaskStore, cost tracker, MaxTurns, active run mutex, permission checks, session view.
- Closure path: Task create/update/list and cost reporting support task-local execution but do not form a whole-current supervisory intervention returned to multiple independent operations.
- Boundary reachability: No positive whole-current management path credited.
- Why this is / is not agent-owned: Static limits and task records are not current-control authority; per-task model planning cannot be counted as a global manager.
- Evidence: [internal/tool/builtin/task.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/builtin/task.go); [config.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/config.go); [main.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/main.go); [agent.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/agent.go); [internal/cost/tracker.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/cost/tracker.go)
- Basis: structural bounded negative
- Confidence: moderate; source-only
- Caveats: Frozen source-only analysis; no Go toolchain or provider-backed end-to-end test attested.

### Absence scope

- Surfaces inspected: Main runtime, task store, config budgets, sessions, run mutex, permission gates.
- Plausible first-party paths checked: Per-task task status, cost/limit enforcement and possible parent task-management choices.
- Why no material first-party path remains: No observed whole-current managerial vantage and authoritative resource/commitment intervention across independent active S1 operations.

## S3* — Complementary audit

- State: —
- Function: No separate complementary and sufficiently independent operational auditing of an S3 management account.
- Disturbance / variety regulated: Coding errors, misreported outcomes, unsafe tool results, and QA requests.
- Decisive decision or feedback right: An independently sourced audit judgment that changes accountable current management.
- Decision owner: No installed audit judgment owner; /review just prompts the ordinary main agent for a git diff review.
- Supporting / enforcement mechanisms: Slash review prompt, tool outputs, hooks and local permission checks.
- Closure path: A model may review code on request, but no independent S3 reporting challenge or authorized corrective return to current management is wired.
- Boundary reachability: No positive S3* audit path credited.
- Why this is / is not agent-owned: Review of task code and deterministic hook/permission gates do not establish an independent complementary channel.
- Evidence: [internal/slash/handler.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/slash/handler.go); [internal/hooks/hooks.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/hooks/hooks.go); [internal/tool/executor.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/executor.go); [main.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/main.go)
- Basis: structural bounded negative
- Confidence: moderate; source-only
- Caveats: Frozen source-only analysis; no Go toolchain or provider-backed end-to-end test attested.

### Absence scope

- Surfaces inspected: Slash review implementation, subagent, tool results, hooks and user tool approvals.
- Plausible first-party paths checked: Independent audit actor/source, audit of the S3 account, corrective finding return.
- Why no material first-party path remains: A /review prompt and optional task reviewer are ordinary task quality work, not a complementary S3 audit function with an independently owned correction path.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped prospective adaptation decision and durable adoption into future agent capability.
- Disturbance / variety regulated: Changing external coding constraints, project conditions, tool/model options and task outcomes.
- Decisive decision or feedback right: A qualified S4 owner would compare prospective alternatives, choose and install a new operating capability or arrangement for later tasks.
- Decision owner: Not established; human chooses model/settings/plugins and developers ship software changes.
- Supporting / enforcement mechanisms: Session resume, local context compaction, user-provided skills/plugins, retry and model config.
- Closure path: Past messages can inform another step and user edits may change configuration, but no source-wired meta-adaptation promotion from observations into subsequent runtime strategy/capability is identified.
- Boundary reachability: No positive S4 adaptation path credited.
- Why this is / is not agent-owned: Context compaction, installing third-party plugins and developer roadmaps are not an autonomous organizational future-intelligence loop.
- Evidence: [internal/session/compact.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/session/compact.go); [internal/plugins/plugins.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/plugins/plugins.go); [internal/skills/skills.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/skills/skills.go); [config.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/config.go); [internal/agent/retry.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/agent/retry.go)
- Basis: structural bounded negative
- Confidence: moderate; source-only
- Caveats: Frozen source-only analysis; no Go toolchain or provider-backed end-to-end test attested.

### Absence scope

- Surfaces inspected: Session/history compaction, extension loading, hook config, model selection, retries and roadmap.
- Plausible first-party paths checked: Longer-horizon evaluation of environmental conditions, strategy selection, prospective capability adoption.
- Why no material first-party path remains: No shipped source-first path turns external prospective analysis into selected durable changed future agent operation; developer changes and optional plugins cannot be borrowed.

## S5 — Policy and identity

- State: —
- Function: No runtime organization-level ultimate-purpose or identity authority closing back into operation.
- Disturbance / variety regulated: User prompts, project instructions, credentials and permission policies.
- Decisive decision or feedback right: A qualified S5 owner would adjudicate ultimate system purpose/identity, then return a binding decision to the harness.
- Decision owner: Operator supplies project directives, APIs, models and permission mode; harness enforces chosen limits.
- Supporting / enforcement mechanisms: XINCODE.md, settings, SimplePermissionChecker, request/approval TUI and CLI.
- Closure path: Policy checks govern effects of individual tools and model context, but no distinct ultimate-policy issue → legitimate authority → authoritative return path is installed.
- Boundary reachability: No positive S5 mode credited, including no function-specific parent-closed loop.
- Why this is / is not agent-owned: Static prompts, tool approvals and installation settings represent external task bounds and execution controls, not first-party S5 ownership.
- Evidence: [internal/tool/permission.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/tool/permission.go); [config.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/config.go); [internal/context/claudemd.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/internal/context/claudemd.go); [main.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/main.go); [agent.go](https://github.com/xincode-ai/xin-code/blob/c5a7969309f7286d1f513caf0821256d4036f4d7/agent.go)
- Basis: structural bounded negative
- Confidence: moderate; source-only
- Caveats: Frozen source-only analysis; no Go toolchain or provider-backed end-to-end test attested.

### Absence scope

- Surfaces inspected: Settings/permissions, tool approval, XINCODE project instructions, main session wiring and TUI.
- Plausible first-party paths checked: Ultimate mission/identity matters, legitimate parent adjudication and authoritative return into operation.
- Why no material first-party path remains: Shipped controls implement user-selected per-tool permissions; no first-party function-specific identity/ultimate-policy decision ownership and closure.

## Recursion

Single self-hosted agent operation per installed workspace; optional spawned subagents share tools/provider and synchronously return delegated task results. No automatic organizational-recursion equivalence from spawning.

## Variety and escalation

User tasks and tool observations are operational variety (S1). API retry, token compaction and user permission requests are bounded task-level regulation. No evidenced Organization-level algedonic channel or higher recursion escalation. Independent human maintenance/release governance belongs outside this assessed deployed program.

## Evidence gaps

1. No live provider-assisted execution or Xin Code Go unit tests were run: the inspection host lacked Go. Code-wiring is source evidence, not runtime attestation.
2. An alternate user-installed plugin/MCP could implement additional functions but is outside the first-party supported default boundary; no upgrade without exact shipped reachability.
3. The remote branch `assessment/b1842-xin-review` currently exists and points at the Index main baseline with no change; this draft is a **handoff**, not an independent parallel review, a canonical claim, a PR, a semantic approval or a release.
