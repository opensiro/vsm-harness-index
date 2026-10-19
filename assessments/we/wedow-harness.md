---
harness_id: wedow-harness
project_name: wedow Harness
repository: https://github.com/wedow/harness
review_ref: 5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44
reviewed_at: 2026-10-19
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

# wedow Harness

## Review boundary

- System in focus: The shipped Bash/plugin model-backed agent operating cell invoked through `bin/harness` and bundled first-party default plugins, especially the headless `agent` command and its supported interactive REPL alternative. This is an assessment of the running agent harness, not the GitHub development team or a user-authored optional plugin organization.
- Purpose and identity: Complete an operator-selected task with a model selecting tool actions, shell/file tools executing them and tool observations incorporated into later model turns.
- Relevant environment: Local repository/workspace and filesystem, terminal, externally configured inference provider, optionally independently spawned task subagents, session messages, command failures and tool results.
- Standard-distribution boundary: `bin/harness`, `plugins/core/commands/agent`, `plugins/core/hooks.d`, bundled OpenAI/Anthropic/ChatGPT protocol adapters, first-party tool plugins and `plugins/subagents`. Operator-installed `.harness` overrides are configurable input, not guaranteed first-party agent executive/governance.
- Credited operating / distribution surfaces: [bin/harness](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/bin/harness#L118), [plugins/core/commands/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/commands/agent#L10), [plugins/core/hooks.d/assemble/20-tools](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/assemble/20-tools#L1), [plugins/core/hooks.d/send/10-send](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/send/10-send#L1), [plugins/openai/hooks.d/receive/10-save](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/openai/hooks.d/receive/10-save#L1), [plugins/core/hooks.d/tool_exec/10-exec](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/tool_exec/10-exec#L1), [plugins/core/hooks.d/tool_done/10-save](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/tool_done/10-save#L1), [plugins/subagents/tools/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/subagents/tools/agent#L43).
- Adjacent first-party surfaces excluded from ownership: Repository documentation/specs, release scripts, optional dynamically sourced third-party projects or `~/.harness` extensions, provider-hosting infrastructure, user-selected goals/API budgets, externally owned host resource permissions, and development/contributor operations.
- First-party operating / deployment modes considered: Headless one-shot `hs "task"`, `hs agent`, REPL/session resume, provider-specific bundled hooks, model-invoked shell/file operations, optional `agent` subagent tool, optional session-context compaction and hot-loaded plugin discovery. No provider inference or externally authorized task execution is claimed in this source review.
- Recursion level: One model-backed working agent cell as S1; delegated spawned agents are separate child task executions whose organizational interference and higher management still require proof.
- Reviewed revision: `5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44` (public GitHub repository ID 1190739032), exact clean source tree `23b1b45452fd71dd08677984ee22dce69c9d6dfd`, frozen in [batch #1724](https://github.com/opensiro/vsm-harness-index/issues/1724).
- Observation date: 2026-10-19; Profile 0.2.4 / Methodology 0.3.7, same immutable generation-origin pair.

## Repository architecture

`bin/harness` boots with built-in plugin sources, discovers executable hooks and dispatches them by stage. Each source can override hooks by basename and `call` pipes JSON state between hooks. `agent_loop` follows `next_state` from `start` to `assemble`, `send`, `receive`, `tool_exec`, `tool_done`, repeated assembly, and terminal `done` or `error`. The core Bash state follower is deterministic and does **not** independently decide which task or tool to perform. [bin/harness](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/bin/harness#L42); [bin/harness](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/bin/harness#L59); [bin/harness](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/bin/harness#L118).

The headless agent command resolves the selected inference provider, saves the user message, and invokes the first-party session loop. The `send` hook dispatches the assembled provider payload; an OpenAI-style `receive` hook interprets model-supplied tool calls and moves to `tool_exec` or returns text; the executable-tool hook resolves the selected tool implementation and runs `--exec` with model-provided input; `tool_done` persists the result for the following turn. Thus the model's context-dependent decisions are actually wired into an S1 work-feedback loop, while provider selection, transport, file writing and failure handling are support. [plugins/core/commands/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/commands/agent#L10); [plugins/core/hooks.d/send/10-send](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/send/10-send#L50); [plugins/openai/hooks.d/receive/10-save](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/openai/hooks.d/receive/10-save#L12); [plugins/core/hooks.d/tool_exec/10-exec](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/tool_exec/10-exec#L4).

The optional subagent plugin starts another invocation of `bin/harness agent`, creates nested sessions, accepts parent-selected prompts/model/provider and returns a child's output. A nested send hook can allocate a configured `HARNESS_AGENT_CONCURRENCY` slot before inference and release it afterward. These are task-decomposition and transport/capacity controls; the code inspected does not establish an S2 feedback-based adjudicator for competing autonomous S1 commitments, a distinct whole-current executive, independent corrective auditor or S4/S5 authority. [plugins/subagents/tools/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/subagents/tools/agent#L16); [plugins/subagents/tools/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/subagents/tools/agent#L81); [plugins/core/hooks.d/send/10-send](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/send/10-send#L10); [plugins/core/hooks.d/send/10-send](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/send/10-send#L205).

## Operational model

The accountable operational loop is the model's next tool or final-output choice based on the user's goal, accumulated session context and actual tool feedback. An optional child agent also executes this mechanism but remains task-subordinate: nothing in the inspected default composition establishes a metasystem that regulates an organization of independent operating divisions. The `next_state` protocol, plugin priority, queued tool results, session persistence and API concurrency gate transport/limit operating variety but do not themselves hold a separate organizational mandate.


## S1 — Operations

- State: A
- Function: Select and execute context-sensitive tools or final answers for an operator-specified software/workspace task.
- Disturbance / variety regulated: Unpredictable repository files, tool outputs/errors, user task constraints and successive observations from tool actions.
- Decisive decision or feedback right: A configured model returns tool-call names and inputs or a final response; the first-party receive hook creates the next `tool_exec` step, which executes and returns actual results for later model decisions.
- Decision owner: Model-backed agent operating through shipped provider hooks and tool executors; a provider supplies cognition, but tool choice is genuinely wired into the first-party agent cell rather than a developer-only example.
- Supporting / enforcement mechanisms: Deterministic Bash state follower, tool discovery and `--exec` dispatch, provider adapters, session messages, error hooks, command controls, transport and session persistence.
- Closure path: User goal + saved context → assembled provider messages → model tool selection → executable tool with arguments → saved result → next assembled model turn or final answer.
- Boundary reachability: The published `hs "task"` / `bin/harness agent` route sources bundled `plugins/core`, resolves the provider and invokes `agent_loop`. Bundled receive/tool-exec hooks implement the substantive model-to-tool-return path in the normal distribution, subject to valid provider credentials.
- Why this is / is not agent-owned: Removing the model leaves a hook pipeline incapable of choosing a substantive next tool on unfamiliar task observations; the deterministic follower and tool executors alone cannot replace that discretionary decision.
- Evidence: [README.md](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/README.md#L1), [bin/harness](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/bin/harness#L118), [plugins/core/commands/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/commands/agent#L7), [plugins/core/hooks.d/send/10-send](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/send/10-send#L205), [plugins/openai/hooks.d/receive/10-save](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/openai/hooks.d/receive/10-save#L12), [plugins/core/hooks.d/tool_exec/10-exec](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/tool_exec/10-exec#L4), [plugins/core/hooks.d/tool_done/10-save](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/tool_done/10-save#L1).
- Basis: Explicit shipped source control/feedback path and documented headless command.
- Confidence: High for supported model-backed structural capability, not a measured production task-completion claim.
- Caveats: Authentication and provider availability required; source inspection does not attest model inference, real task success or external service behavior.


## S2 — Coordination

- State: —
- Function: No established separately accountable regulation of actual inter-S1 conflict/oscillation among distinct independently viable operating units.
- Disturbance / variety regulated: Child tasks can share provider request capacity and workspace context. A configured semaphore bounds simultaneous provider calls, but no conflict-specific cross-task judgement or feedback stabilizing competing S1 operational policies is demonstrated.
- Decisive decision or feedback right: A parent model chooses to spawn a child; nested child inference acquires a mechanical maximum-concurrency slot. No other distinct agent selects a coordination compromise when contention is observed.
- Decision owner: Parent model for task decomposition; configured semaphore and depth gate are deterministic supporting restrictions.
- Supporting / enforcement mechanisms: `HARNESS_AGENT_CONCURRENCY` session-root slot directories, child timeout, `HARNESS_DEPTH` cap, tool-dispatch queue and source discovery.
- Closure path: Parent tool request → child subprocess → child output/timeout → parent result; a provider request may wait on a slot. This is task delegation and fixed resource admission, not source-established specific inter-S1 disturbance → regulator decision → adjusted participating-unit behavior.
- Why this is / is not agent-owned: A model may choose which child task to ask for, but that S1 task choice does not amount to governance of mutual interference between viable operational units; queue/concurrency enforcement is not its own autonomous S2 right.
- Evidence: [plugins/subagents/tools/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/subagents/tools/agent#L81), [plugins/subagents/tools/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/subagents/tools/agent#L117), [plugins/core/hooks.d/send/10-send](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/send/10-send#L17), [plugins/core/hooks.d/send/10-send](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/send/10-send#L205), [plugins/core/hooks.d/tool_exec/10-exec](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/tool_exec/10-exec#L1).
- Basis: Bounded absence after tracing default first-party delegation and configured shared-slot enforcement.
- Confidence: Medium-high for declared one-agent/child-task recursion.
- Caveats: A custom plugin organization may add S2, but it is not inherited into this frozen default distribution.

### Absence scope

- Surfaces inspected: Bundled subagent tool, child-session propagation, depth gate, streaming tool dispatcher, provider-send concurrency semaphore.
- Plausible first-party paths checked: Child/parent requests, provider slot pressure, parallel tool results and recovery paths.
- Why no material first-party path remains: The examined controls are preset limits and task-subordinate responses; no separate interference judgment and reciprocal stabilization feedback among autonomous S1 operating divisions is source-established.


## S3 — Inside-and-now control

- State: —
- Function: No evidenced whole-current organizational management function that owns live priorities, shared commitments and corrective resource decisions over distinct S1 operations.
- Disturbance / variety regulated: Provider errors, concurrent inference slots, tool timeouts, task progress and per-session compaction are local execution conditions rather than a complete organizational current-control portfolio.
- Decisive decision or feedback right: The operator sets task/provider/concurrency choices; script loops enforce them; no standing first-party agent executive judges whole-system current resource/priority conflicts and returns binding choices.
- Decision owner: Operator configuration and task-local model, not a separate S3 executive.
- Supporting / enforcement mechanisms: Session directory state, plugin errors, configured limits, hook resolution, child depth gate and optional compaction.
- Closure path: Error or slot pressure → deterministic task/transport handling or a return to the same local S1; no whole-current management decision → changed cross-unit operation loop.
- Why this is / is not agent-owned: The task model decides immediate work tools but lacks an evidenced whole-current organizational mandate; slot allocator follows predefined limits without decision discretion.
- Evidence: [bin/harness](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/bin/harness#L118), [plugins/core/hooks.d/send/10-send](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/send/10-send#L205), [plugins/core/hooks.d/error/10-display](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/error/10-display#L1), [plugins/rlm/hooks.d/assemble/25-compact](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/rlm/hooks.d/assemble/25-compact#L1).
- Basis: Source-bounded absence of distinct inside-and-now management ownership/closure.
- Confidence: Medium-high.
- Caveats: A user's management of multiple terminals or outside host is not counted as first-party S3 parent governance.

### Absence scope

- Surfaces inspected: Agent loop, send-slot implementation, session lifecycle, error hooks, optional context compaction.
- Plausible first-party paths checked: Concurrency limits, run/session-level monitoring, error handling, parent spawning and operator-set provider routing.
- Why no material first-party path remains: No whole-system current decision right and returned cross-operational commitment/resource regulation is connected in shipped default paths.


## S3* — Complementary audit

- State: —
- Function: No separate complementary operational-reality auditor with independently sourced evidence, corrective judgment and returned revision of operations/S3.
- Disturbance / variety regulated: Tool errors, malformed provider output and local context loss can be caught by transport checks; such checks do not independently verify claims made by a current-control executive.
- Decisive decision or feedback right: Hooks parse provider/tool results and produce errors; no separately authorized reviewer challenges an operational report and sends corrective findings into governance.
- Decision owner: Deterministic error handlers and task agent for subsequent local recovery.
- Supporting / enforcement mechanisms: JSON validation, explicit tool-error flags, session transcripts, stderr and stream output, child JSON-schema completeness checks.
- Closure path: Tool/provider failure → recorded error/retry/repair by local task agent, rather than complementary S3 reports → independent discrepancy judgment → binding corrective return.
- Why this is / is not agent-owned: Persisted logs and schema checking are not an independently reasoning S3* evaluator; spawning an optional subagent does not automatically give it independent audit authority.
- Evidence: [plugins/core/hooks.d/tool_exec/10-exec](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/tool_exec/10-exec#L25), [plugins/core/hooks.d/error/10-display](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/error/10-display#L1), [plugins/subagents/tools/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/subagents/tools/agent#L43), [plugins/openai/hooks.d/receive/10-save](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/openai/hooks.d/receive/10-save#L12).
- Basis: Negative from specific shipped verification/log/delegation paths.
- Confidence: Medium-high.
- Caveats: An external audit workflow or custom configured specialist could require a separate assessment.

### Absence scope

- Surfaces inspected: Core tool-exec/error hooks, provider receive adapter, child schema checks, message persistence, default prompt guidance.
- Plausible first-party paths checked: Stored transcripts, independent child invocations, error parsing and schema completion.
- Why no material first-party path remains: These paths validate tool/transport/task outputs without a distinct complementary S3 report audit, authorized corrective judgment and returned operating-control loop.


## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party externally prospective scan → new organizational capability option → adoption/return loop is established in the supported default distribution.
- Disturbance / variety regulated: Changing task context and available tools can require adaptation; hook discovery each iteration and context compaction are present-task extension/recovery, not future organization strategy.
- Decisive decision or feedback right: Operator/file installation chooses plugins; the state follower discovers them. No agent S4 owner selects external opportunities, weighs future options and installs a new operating policy with a return path to later work.
- Decision owner: Human/project plugin authors for extensions; task agent for current work/tool choice.
- Supporting / enforcement mechanisms: Hot source discovery, extend-harness skill, `plugins/rlm` compaction and stored session history.
- Closure path: User installs/edits plugin → next hook scan sees it, or current context compacts → same task continues; no first-party S4–S3 future-option selection and authorized adoption feedback is evidenced.
- Why this is / is not agent-owned: Dynamic plugins and model-authored code could support external development, but this does not establish an agent-owned future organizational strategy decision in the shipped runtime.
- Evidence: [bin/harness](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/bin/harness#L42), [bin/harness](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/bin/harness#L123), [plugins/core/skills/extend-harness/SKILL.md](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/skills/extend-harness/SKILL.md#L1), [plugins/rlm/hooks.d/assemble/25-compact](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/rlm/hooks.d/assemble/25-compact#L1).
- Basis: Bounded negative after checking relevant supplied extension and memory paths.
- Confidence: Medium-high in documented first-party modes.
- Caveats: This does not rule out external human evolution of the open-source project.

### Absence scope

- Surfaces inspected: Plugin hot-reload/bootstrap, extend-harness skill, optional recursive compaction, session history and REPL modes.
- Plausible first-party paths checked: Tool source additions, agent-written skill/plugin files, memories and operator-mediated extension.
- Why no material first-party path remains: None is wired as a separate prospective environmental intelligence owner deciding and adopting viable future operating capabilities with a returning control path.


## S5 — Policy and identity

- State: —
- Function: No first-party legitimate arbitration of ultimate harness purpose, organizational identity and foundational policy with binding return into operating mode.
- Disturbance / variety regulated: User requests, tool access, provider selection and generic action warnings restrict current tasks but do not create an ultimate-purpose constitutional issue.
- Decisive decision or feedback right: Users/configuration set prompt, runtime provider, plugins and environmental permissions; default prompts can constrain model calls. No S5 actor judges conflicting organizational identities/ultimate policy and returns a legitimized decision.
- Decision owner: External operator/project maintainers for overall aims and constraints; not a packaged first-party S5 mode.
- Supporting / enforcement mechanisms: Static system/agent prompt, user configuration, tool wrappers and optional plugin override priority.
- Closure path: Operator-configured prompt/tools → model task execution; no institutional identity dispute → legitimate parent/agent decision → changed enduring organizational constitution/operation.
- Why this is / is not agent-owned: User-level task instructions and fixed hooks are not the authority to define an organization's ultimate ends; a model's tool choice does not confer that right.
- Evidence: [plugins/core/prompts/001-system.md](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/prompts/001-system.md#L1), [plugins/core/hooks.d/assemble/30-prompts](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/hooks.d/assemble/30-prompts#L1), [bin/harness](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/bin/harness#L42), [plugins/core/commands/agent](https://github.com/wedow/harness/blob/5f5d968a86b9762f4c69a6e4d0fe3bf1c5cb5c44/plugins/core/commands/agent#L10).
- Basis: Source-bounded negative under released harness distribution.
- Confidence: Medium-high.
- Caveats: Hosting organization and human plugin governance remain external to this assessment recursion.

### Absence scope

- Surfaces inspected: Default prompts, provider/agent entrypoints, plugin override discovery and fixed tool-execution controls.
- Plausible first-party paths checked: Human-configured goal/provider/limits, plugin management, safety instructions and tool permissions.
- Why no material first-party path remains: No first-party mechanism receives an ultimate-purpose/identity matter and returns a legitimately decided enduring policy into later operation.


## Recursion

S1 is one configured model-backed working task loop. Optional child `agent` invocations operate as subordinate task agents with independent sessions and feedback, not automatically viable separate operating divisions with a common autonomous metasystem. The repository supports external composition; such separate deployments must not be silently combined in the default assessment.

## Variety and escalation

Workspace observations and tool failures return to the model-driven task loop. Error hooks stop or surface failures; depth/time/concurrency limits bound execution. Neither an error status nor a request for human setup by itself proves a separate algedonic signal, S3/S4/S5 control or legitimate governance channel.

## Evidence gaps

- Frozen first-party source and documentation were reviewed. This environment had Bash 5.2, but `jq` was absent at preflight, so the end-to-end Bash specs and live configured-provider inference were **not** executed or claimed; functional statements describe shipped reachable source paths.
- Concrete inter-S1 competition feedback under simultaneous child tasks was not observed. A configured model/child concurrency cap alone is not promoted to S2.
- Dynamically installed local/user plugins, unrelated upstream providers or future versions may realize different functions; they are outside this pinned assessed standard distribution.
- This `status: proposed` artifact is noncanonical until separate exact-head CI, review and later Index catalog/admission workflow.
