---
harness_id: rust-code
project_name: rust-code
repository: https://github.com/fortunto2/rust-code
review_ref: fcc91a93deb69fab3de2c96a32129cbd69beea72
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

# rust-code

## Review boundary

- System in focus: the shipped first-party Rust terminal coding agent (`rust-code` from `crates/rc-cli`), using the local `sgr-agent` decision loop and registered coding tools, including built-in swarm/delegation and opt-in `--loop`/`--evolve` execution.
- Purpose and identity: turn a user's coding request into source inspection, edits, shell commands, test/build and git operations, with persisted project/session state and optional child task execution.
- Relevant environment: working repository, operating-system filesystem and shell, configured LLM provider, optional external CLI agents/MCP servers, persistent task files, project instructions, tools and human prompts.
- Standard-distribution boundary: installed `rust-code` CLI and first-party workspace crates as connected by `crates/rc-cli/src/main.rs`, `agent.rs`, `tools/swarm_tools.rs`, `tools/delegate.rs`, `sgr-agent/src/agent_loop.rs`, `swarm.rs`, and `evolution.rs`. A source checkout may offer bundled `skills/self-evolve`; the crates.io package's `include` list does not prove that repository-level skill files are installed.
- Credited operating / distribution surfaces: terminal TUI and headless prompt route, first-party root tool registry, model-guided coding loop, optional built-in spawned model-guided children, external-CLI delegation adapter when separately installed, local tasks, telemetry/history-driven self-improvement loop, and explicit operator control.
- Adjacent first-party surfaces excluded from ownership: project contributors, CI/build/release jobs, developer documentation, tests and examples, benchmarks, a separate agent installed by a user, and downstream model-provider governance. Opt-in self-modification does not automatically turn repository-maintainer review into first-party operational S3* or S5.
- First-party operating / deployment modes considered: interactive TUI, headless `-p`, session resume, background tmux delegation, `--loop N`, `--evolve`, provider/tool configuration, and optionally installed MCP/skills.
- Recursion level: one user-initiated `rust-code` coding-task organization, including the first-party root's eligible child work cells; not a federation of unrelated installations or the maintainer organization.
- Reviewed revision: [`fcc91a93deb69fab3de2c96a32129cbd69beea72`](https://github.com/fortunto2/rust-code/tree/fcc91a93deb69fab3de2c96a32129cbd69beea72) from immutable batch intake #200.
- Observation date: 2026-10-22; first-party pinned-source inspection, without external-provider execution, independently measured swarm runs, or a live self-rebuild.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The Rust workspace ships a `rust-code` CLI, `sgr-agent` loop/tool/session building blocks and TUI. In headless mode the application creates an `Agent`, registers file, patch, shell, git, task, memory, external API, delegate and swarm tools, passes provider responses through the agent loop and returns action observations to the next model choice. The interactive app also creates this agent. The code permits parallel subagent lifecycles and separately installed external CLI delegates, but the built-in spawn path passes a **new empty tool registry** to its child. Hence documented explorer/worker/reviewer roles do not alone prove a multi-cell coding division with independent read/write operational ability.

The root's optional `--evolve` route collects current task telemetry, scores efficiency, identifies recurring errors from local sessions, constructs a self-edit prompt and continues the same coding loop; a special text signal can request a restart. The inspected built-in signal sources concern current/local execution reliability, not a prospective model of external demand, ecosystem change or future opportunity. Moreover the reported `keep`/`discard` score is logged and is not a demonstrated code-acceptance/rollback gate.

Primary evidence: [CLI modes and loop](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/main.rs#L1223-L1559), [root tool registry](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/agent.rs#L211-L322), [subagent tool creation](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/tools/swarm_tools.rs#L56-L94), [evolution engine](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/sgr-agent/src/evolution.rs#L1-L266).

## Operational model

The decisive task action is a model choice inside the first-party root agent, bounded by static tools, user context, provider availability and tool results. Parent-provided role/task prompts may launch child reasoning. The `SwarmManager` imposes fixed count/depth caps and exposes task result/status/cancel; external-CLI delegation uses tmux and task-file statuses. These capabilities provide decomposition and observation, but separate whole-system current-control and inter-S1 conflict closure must be established from a specific decision right, not from the word `swarm`.

## S1

- State: A
- Function: Execute a coding request by deciding concrete source/tool actions, inspecting results, and continuing or completing the task.
- Disturbance / variety regulated: Unknown project structure, differing user goals, unexpected tool output, shell failures and changing code state during an operating task.
- Decisive decision or feedback right: The model-based root chooses file/shell/git/task operations and the next continuation from prior tool observations; eligible model-based subagents can independently choose a response to their assigned task, though the default embedded child has an empty tool registry.
- Decision owner: First-party configured LLM-driven `Agent` in the `sgr-agent` loop; tool registry executes its selected actions.
- Supporting / enforcement mechanisms: SGR JSON decision parsing, registered file/patch/bash/git tools, persistent session and memory, loop detection, per-run step cap, provider fallback and optional background commands.
- Closure path: User request → model decision → typed action dispatch → tool result/observed errors → subsequent model decision or finish.
- Why this is / is not agent-owned: Choosing an actual coding action after observations is autonomous operating discretion; the static registry, retries and CLI operator activation do not make that S1 decision for it.
- Boundary reachability: Both `-p` headless route and interactive application instantiate the first-party coding agent; ordinary CLI invocation reaches the shipped decision loop without adding a user-written plugin.
- Evidence: [Agent creation and registered tools](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/agent.rs#L211-L322), [headless run loop and events](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/main.rs#L1327-L1430), [first-party application loop](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/sgr-agent/src/app_loop.rs#L444-L505), [child agent loop](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/sgr-agent/src/agent_loop.rs#L267-L340).
- Basis: structural.
- Confidence: high for coding action ownership; actual external-provider completion was not tested.
- Caveats: Child tool ability and external CLI installation differ by route; no measured success rate is claimed.

## S2

- State: —
- Function: Regulate disruptive interference or oscillation between separately operating S1 cells.
- Disturbance / variety regulated: Potential concurrent coding agents writing the same repository or competing for file/tool resources.
- Decisive decision or feedback right: No first-party per-file ownership arbitration, detected cross-child write conflict or returned mutual-adjustment decision is shown. Fixed spawn count/depth caps and wait/cancel are lifecycle operations.
- Decision owner: Absent for S2-specific inter-S1 disturbance; root may assign work while a deterministic swarm manager holds handles.
- Supporting / enforcement mechanisms: `SwarmManager` caps at eight active handles and depth three, cancellation and result channel; optional external CLI tmux/task status; one mutex for the manager's state.
- Closure path: Agents can be spawned and returned to root, but no source-backed conflict observation → attenuation → revised independent S1 work closure exists.
- Why this is / is not agent-owned: Task decomposition and concurrency quotas cannot be promoted to S2 without the actual interference relationship and returned coordination response.
- Evidence: [swarm limits and spawn](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/sgr-agent/src/swarm.rs#L205-L348), [wait/status/cancel](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/sgr-agent/src/swarm.rs#L370-L550), [separate CLI delegate](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/tools/delegate.rs#L1-L235).
- Basis: structural.
- Confidence: medium-high within first-party inspected mechanisms.
- Caveats: A separately installed delegate could implement its own coordination, but this cannot be silently credited to the packaged root.

### Absence scope

- Surfaces inspected: swarm manager/child spawn tool, external delegate lifecycle, local task-state tool, root registry and headless loop.
- Plausible first-party paths checked: concurrent spawned child execution, read-write role labels, agent quotas, tmux delegates, shared task-file statuses, cancellation and wait channels.
- Why no material first-party path remains: These paths transport or limit independent tasks but do not observe a concrete inter-S1 disturbance and return a compensating adjustment into the competing work units.

## S3

- State: —
- Function: Regulate current whole-task commitments, resources, priorities and accountability across independently viable operational units.
- Disturbance / variety regulated: Concurrent task progress, shared task-level resources, loop/runtime costs and partial failures.
- Decisive decision or feedback right: Root model can assign and cancel child tasks, but no distinct evidenced whole-system current resource/commitment decision based on a shared cross-cell view is established.
- Decision owner: No packaged S3-specific owner demonstrated; root coding model chooses individual operational delegations and the operator selects loop/model settings.
- Supporting / enforcement mechanisms: Task board, agent statuses, finite loop count/time limit, fixed spawn limits, delegate manager, per-run cost display and circuit breaker.
- Closure path: A delegated task reports completion into the root task loop; that is a task result rather than a whole-current managerial intervention with continued cross-unit accountability.
- Why this is / is not agent-owned: Delegation/aggregation and static guardrails do not prove the additional whole-system managerial right.
- Evidence: [root delegation tooling](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/agent.rs#L286-L322), [task board](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/tools/task_tool.rs#L1-L110), [loop caps and per-run record](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/main.rs#L1223-L1542).
- Basis: structural.
- Confidence: medium.
- Caveats: A custom external orchestrator might impose a higher-level resource policy, but lies outside this recursive boundary.

### Absence scope

- Surfaces inspected: task statuses/priorities, child/delegate status manager, agent result returns, cost reporting, fixed budgets/limits and loop control.
- Plausible first-party paths checked: parent task allocations, cancellation, status dashboards, resource caps, next-step selection, task priority changes and running/deferred delegate statuses.
- Why no material first-party path remains: No packaged controller closes a whole-current commitments/resource tradeoff over separately viable S1 divisions; observed actions are local-task decomposition, status and fixed execution limits.

## S3*

- State: —
- Function: Give current management complementary, sufficiently independent access to actual operations so claims can be challenged and corrected.
- Disturbance / variety regulated: Incorrect child completion claims, incomplete code, faulty patches and unobserved operating errors.
- Decisive decision or feedback right: No shipped audit role with alternate, sufficiently independent access to S3's whole-current operating claims and corrective return is established.
- Decision owner: Absent at S3*; reviewer child labels and local tests describe ordinary work QA.
- Supporting / enforcement mechanisms: `reviewer` role prompt, session history, telemetry counters, test/build commands, git diffs and error-feedback logs.
- Closure path: Reviewer responses or tests can inform an ordinary coding step, but they are not an independent management-accountability audit that corrects S3.
- Why this is / is not agent-owned: A reviewer child shares the root's task/response channel and the inspected `spawn_agent` child receives an empty tool registry; a different role label is not independent operational evidence access.
- Evidence: [role definitions](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/sgr-agent/src/swarm.rs#L44-L85), [child empty tools](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/tools/swarm_tools.rs#L56-L94), [telemetry/evaluation](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/sgr-agent/src/evolution.rs#L1-L234).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Independent human/project CI review is adjacent governance, not demonstrated as an installed S3* channel at this recursion.

### Absence scope

- Surfaces inspected: shipped swarm reviewer role, child tool registry, normal test/build commands, git tools, session logs and evolution evaluation.
- Plausible first-party paths checked: reviewer/explorer child roles, external CLI delegates, verification commands, errors and telemetry, and repository CI.
- Why no material first-party path remains: These constitute task QA or adjacent maintenance; no alternative audit of a defined S3 claim with separated operational access, accountable findings and corrective control return was found.

## S4

- State: —
- Function: Interpret external/future environmental change and formulate capability adaptations linked to present operation.
- Disturbance / variety regulated: Changing model/tool capabilities, external requirements and future coding-environment demands are plausible but not evidenced as inputs to a shipped prospective intelligence process.
- Decisive decision or feedback right: Opt-in `--evolve` prompts self-edit from current efficiency/errors and recent local session patterns; it does not distinguish the relevant external future or choose options against prospective outside conditions.
- Decision owner: Local model may choose and implement operational self-fixes, but no functionally evidenced S4-specific external/future adaptation owner.
- Supporting / enforcement mechanisms: Current run `RunStats`, `score`, history JSONL, rule-based `evaluate`, generated edit/test/commit prompt, restart marker and bounded loop.
- Closure path: Current execution → diagnostic counters → suggested self-fix → possibly model edit and rebuild. The missing prospective external distinction and S3↔S4 conversation prevent calling this S4 closure.
- Why this is / is not agent-owned: The agent's ability to modify its own source can be real local S1 self-maintenance; source-named self-evolution is not VSM S4 on internal performance feedback alone.
- Evidence: [telemetry-based triggers](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/sgr-agent/src/evolution.rs#L1-L266), [recent session patterns](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/sgr-agent/src/evolution.rs#L275-L497), [evolve loop/score/restart](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/main.rs#L1440-L1559), [bundled skill](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/skills/self-evolve/SKILL.md).
- Basis: structural.
- Confidence: medium-high on bounded classification.
- Caveats: A human can give the agent an external-trend research task, but a generic tool prompt alone does not establish first-party recurrent S4 ownership. No live evolution/rebuild experiment performed.

### Absence scope

- Surfaces inspected: `--evolve` route, self-evolve skill, `evolution.rs` scoring/history, `--loop`, context/skills and generic model/API tools.
- Plausible first-party paths checked: local error trends, improvement proposals, next-run task generation, code patch/test/commit/restart, externally accessible MCP/OpenAPI and human future-oriented prompts.
- Why no material first-party path remains: All built-in feedback predicates are operational/session-internal; no defined external horizon, prospective alternatives and binding path back through whole-current capability control are demonstrated.

## S5

- State: —
- Function: Determine legitimate ultimate identity, governing purpose and policy for the task organization, balancing current operation and future change.
- Disturbance / variety regulated: Conflicting user goals, tool permissions, project instructions, dangerous actions and potential changes of the coding agent's purpose.
- Decisive decision or feedback right: The user/provider/configuration and project prompt set constraints; the shipped agent has no independent legitimate ultimate-policy decision/appeal mechanism with binding return to governing operation.
- Decision owner: Human operator or adjacent project governance for identity/policy, not a first-party S5 cell in the installed coding organization.
- Supporting / enforcement mechanisms: User prompts, project `AGENTS.md`/`CLAUDE.md`, local `SOUL`/`IDENTITY` context, intent flags, static prompt and tools, optional skill instructions and shell sandbox/permission choices in external CLI delegates.
- Closure path: Inputs set the context or gate certain actions. They do not establish a legitimate adjudication of ultimate organizational identity or a new binding S5 decision returned into S3/S4.
- Why this is / is not agent-owned: Context files, static prompts and user-selected options are authority sources or safeguards; a model executing them is not thereby authorized to change ultimate policy.
- Evidence: [layered identity/project context](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/agent.rs#L200-L227), [system prompt](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/agent.rs#L114-L195), [operator intent/provider setup](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/main.rs#L1180-L1212), [external delegate invocation](https://github.com/fortunto2/rust-code/blob/fcc91a93deb69fab3de2c96a32129cbd69beea72/crates/rc-cli/src/tools/delegate.rs#L60-L110).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Repo maintainer decisions and vendor policies are adjacent; none is silently imported as an implemented parent-governed S5 mode.

### Absence scope

- Surfaces inspected: context/identity files, system prompt, project instructions, operator flags, execution permissions, skills, delegated CLI settings and contributor governance adjacency.
- Plausible first-party paths checked: local SOUL/IDENTITY memory, `AGENTS.md`, tool permissions, prompt changes, self-evolve source edits, and operator-selected provider/intent.
- Why no material first-party path remains: Neither prompt authority nor operational self-modification gives the installed agent legitimate final identity/policy decision rights or demonstrated S3–S4 governance return.

## Distributed OSS parent arrangement

Maintainer reviews, release builds and public documentation belong to the OSS development organization, not to the first-party running `rust-code` session. Separately installed `claude`, `codex`, `gemini`, `opencode` and `rust-code` CLI instances can be driven through a tmux adapter, but are external executables whose full independent governance is not embedded in this package. They contribute potential operating task work only when available.

## Self-hosted and non-human modes

Terminal and headless source-built operation, multiple provider choices and locally installed external tools do not change the recursion. `--evolve` is an opt-in repeated local diagnostic/self-modification mode, not a proven strategic environmental loop; nor does the documented `keep`/`discard` log itself enforce rollback. No autonomous S2/S3/S3*/S4/S5 rights are inferred solely from non-human execution.

## Recursion

At the selected coding-task level, model-directed coding work is S1. Spawned first-party child sessions have a separate model and context but are passed an empty tool registry by the built-in adapter; optional external delegates can operate as additional work cells but do not establish metasystemic closure just by being present. A broader organization of multiple installations would require a different system-in-focus and evidence set.

## Variety and escalation

Tool and runtime errors return to the operating model; loop-warning thresholds, step limits and operator stop/pause files attenuate pathological repetition. Swarm results, task-status files and local logs are available for task-level feedback, while the evolution mode analyzes repeated local failures. These statuses are not independently an algedonic route to a qualified S3, S4 or S5 response authority.

## Evidence gaps

- Source-inspection result only. No configured provider credentials, actual coding run, subagent conflict reproduction or self-evolution/rebuild trace were executed.
- The registered spawn tool constructs a child with no tools; claims of role-specific read/write effectiveness beyond code-level model decisions require runtime proof or a later wired tool registry.
- The opt-in evolution path can request coding changes, but its evaluation is internal to local execution history and its logged `keep`/`discard` is not verified adoption control. A future implementation providing environmental scanning, prospective options and return-to-current-control could change S4.
