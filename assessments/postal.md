---
harness_id: postal
project_name: Postal
repository: https://github.com/andrefetch/postal
review_ref: 8631e85f01cd42d72470289c29ecb3c738a87f0d
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Postal

## Review boundary

- System in focus: Postal's first-party Python terminal coding-agent runtime at frozen revision `8631e85f01cd42d72470289c29ecb3c738a87f0d`, including `Agent`, `Session`, built-in coding tools, default subagents, approvals, session/checkpoint/context machinery, MCP/skills integration and interactive/single-shot execution surfaces.
- Purpose and identity: perform coding work in a selected local repository by inspecting, planning, editing, running and reviewing code while allowing the operator to choose the approval envelope.
- Relevant environment: user tasks, current repository/worktree state, shell/file/search results, model-provider responses, web/URL evidence, configured MCP tools, project instructions/skills, persisted memory and operator approval decisions.
- Standard-distribution boundary: Postal's own model/tool loop, tool registry, default subagents, approval manager, sessions/context, memory and supported terminal modes are inside. OpenRouter/models, MCP servers, web endpoints and user-authored skills/configuration are dependencies or configuration and do not donate organizational functions.
- Credited operating / distribution surfaces: `README.md`; `agent/agent.py`; `agent/session.py`; `tools/registry.py`; `tools/subagents/subagents.py`; `docs/tools.md`; `docs/approvals.md`; session/context and approval implementations reachable from the shipped runtime.
- Adjacent first-party surfaces excluded from ownership: tests, publish/release workflow, contributor governance and roadmap-only features. In particular, README's `Parallel Subagents` item is future work and is not credited at the frozen revision.
- First-party operating / deployment modes considered: interactive TUI; single-shot execution; approval modes `on_request`, `auto_edit`, `auto`, `on_fail`, `never`, and `yolo`; standard default tool registry; the five shipped specialized subagents; session resume/checkpoint/rewind; MCP/skills where Postal remains the harness owner.
- Recursion level: the assessed organization is a primary Postal session plus any bounded child `Agent` instantiated synchronously as a subagent tool. Each child runs a complete local model/tool loop and is therefore a distinct subordinate S1 when invoked, but spawning alone does not establish full recursive viability.
- Reviewed revision: `8631e85f01cd42d72470289c29ecb3c738a87f0d`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`Agent.run()` adds the current user task to session context and enters `_agentic_loop()`. Each loop iteration prunes or compacts context when required, sends the current messages and tool schemas to the configured model provider, records returned assistant content/tool calls, invokes each selected tool through Postal's first-party registry and approval path, appends tool results to the model context and repeats. A loop detector can inject a corrective prompt when repeated actions indicate stagnation. Completed turns are checkpointed by the parent session.

Default subagents are registered as ordinary model-facing tools. `SubAgentTool.execute()` creates a narrowed configuration, disables child checkpoint persistence, then constructs a new full `Agent` with its own session/context and turn budget. The child runs synchronously to completion and its final response plus tool-use summary is returned as the parent tool result. Child approvals are routed through the parent confirmation callback, so delegation cannot bypass the active approval policy.

The frozen revision ships five subagent roles: `codebase_investigator`, `code_reviewer`, `software_architect`, `test_writer`, and `debugger`. The `code_reviewer` gets a separate read-only `Agent` with `read`, `grep`, and `list_directories`, and an audit-specific prompt to inspect bugs, inconsistent/unclean code, security issues and improvement opportunities. Its direct codebase findings return through the normal tool-result path to the primary agent. By contrast, parallel subagents are explicitly roadmap-only at this revision.

Postal also supplies planning, persistent key-value memory, web search/fetch, sessions/checkpoints/rewind, approval policies, context pruning/compaction, MCP and skills. These mechanisms support operations but do not by themselves establish S2/S3/S4/S5.

Primary evidence:

- [`README.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/README.md)
- [`agent/agent.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/agent/agent.py)
- [`tools/registry.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/tools/registry.py)
- [`tools/subagents/subagents.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/tools/subagents/subagents.py)
- [`docs/tools.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/docs/tools.md)
- [`docs/approvals.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/docs/approvals.md)

## Operational model

The primary Postal actor owns the open-ended coding decision loop inside the selected approval envelope. It may invoke a specialized child actor as one tool call; the parent waits while that child executes a complete, narrowed model/tool loop and then receives the child's result. In autonomous `auto`/`yolo` operation, the primary model can therefore invoke the read-only `code_reviewer` without a human becoming the decisive audit owner, receive complementary findings, and choose corrective actions in the next parent model turn.

The multi-agent topology remains synchronous. The parent does not maintain a population of simultaneously active subordinate commitments. The frozen README explicitly places parallel subagents on the roadmap, which is material negative evidence for S2/S3 rather than merely absence of a discovered implementation.

## S1 — Operations

- State: A
- Function: perform repository-facing coding work by interpreting the current task, choosing permitted file/search/shell/network/delegation actions, executing them and revising subsequent action from returned evidence.
- Disturbance / variety regulated: changing code/worktree state, implementation alternatives, tool and shell failures, provider uncertainty, context pressure, repeated-action loops and task-specific evidence encountered during execution.
- Decisive decision or feedback right: choose the next task-specific tool/action or final response and revise that choice after observing tool results.
- Decision owner: the model-backed Postal agent; each invoked child `Agent` owns the corresponding bounded local S1 discretion for its delegated task.
- Supporting / enforcement mechanisms: `Session`; `ToolRegistry`; approval manager; context pruning/compaction; loop detector; checkpoints; provider client; MCP/skills; configured turn limits.
- Closure path: current task/session evidence → model selects action → first-party tool invocation → result appended to context → same model actor selects the next action or finishes.
- Boundary reachability: the `Agent`/`Session` loop and default registry are the standard runtime used by the documented interactive and single-shot product modes.
- Why this is / is not agent-owned: removing the model actor while retaining registry, approvals, checkpoints and context machinery removes the task-specific choice of what to inspect, edit, run, delegate or report next; deterministic components constrain or transport the decision rather than replace it.
- Evidence: [`agent/agent.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/agent/agent.py); [`tools/registry.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/tools/registry.py); [`README.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: default `on_request` can make the operator decisive for individual mutating actions, while first-party `auto` and `yolo` provide autonomous operating modes within their respective hard-safety envelopes.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 disturbance-attenuation loop was established at the frozen boundary.
- Disturbance / variety regulated: distinct child S1 executions exist, but the current runtime does not expose simultaneous child interaction whose conflict/oscillation is then regulated by an S2-specific relation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: synchronous parent-to-child delegation; child tool narrowing; parent-routed approvals; ordinary workspace semantics; sequential parent tool execution.
- Closure path: absent at S2 level; no concrete concurrent inter-S1 disturbance → attenuation decision → feedback changing competing S1 behaviour was found.
- Why this is / is not agent-owned: choosing a subagent and awaiting its result is delegation, not coordination among interacting S1 units. The parent agent may decompose work, but no S2-specific discretionary response is required or evidenced for the frozen topology.
- Evidence: [`agent/agent.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/agent/agent.py); [`tools/subagents/subagents.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/tools/subagents/subagents.py); [`README.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the roadmap names parallel subagents, which could create new inter-S1 disturbance and coordination evidence in a later revision; roadmap intent is not current evidence.

### Absence scope

- Surfaces inspected: parent agent tool-call loop; default tool registry; subagent implementation and definitions; subagent approval routing; tools documentation; README current feature list and roadmap.
- Plausible first-party paths checked: simultaneous subagent execution, cross-agent messaging, shared reservations/locks, workspace partitioning, collision detection, conflict arbitration, negotiated plans and a collaboration scheduler.
- Why no material first-party path remains: the parent executes model tool calls sequentially and each `SubAgentTool` awaits one child `Agent` to completion. Parallel subagents are explicitly roadmap-only, so no current multi-S1 interaction/attenuation closure is supplied.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party S3 whole-current control loop was established at the assessed recursion.
- Disturbance / variety regulated: the parent can decompose a task, maintain one plan and delegate one bounded child run, but no independently evolving whole-current population of operations is exposed for S3 regulation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `plan` todo state, session/checkpoint state, synchronous subagent calls, turn limits, approval policy, loop detector and context controls.
- Closure path: absent at S3 level; no whole-system current view → resource/commitment/priority intervention → returned change across a current operation population was found.
- Why this is / is not agent-owned: selecting one synchronous subagent is task decomposition. The main agent is not shown observing a persistent set of active S1 commitments and exercising current-control authority over that set on behalf of the whole.
- Evidence: [`docs/tools.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/docs/tools.md); [`tools/subagents/subagents.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/tools/subagents/subagents.py); [`agent/agent.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/agent/agent.py).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a later implementation of parallel/background subagents with population visibility and commitment authority could change the S3 result; it is not in this frozen revision.

### Absence scope

- Surfaces inspected: plan tool documentation, agent/session lifecycle, session/checkpoint/rewind behavior, tool registry, subagent lifecycle, approval modes and documented terminal controls.
- Plausible first-party paths checked: live subordinate task registry; background workers; population/status view; cancellation/reprioritization; shared budget/resource allocation; organization-wide current performance/accountability intervention.
- Why no material first-party path remains: subagents are awaited tool invocations tied to one parent turn and are not checkpointed as independent commitments. Planning tracks one operational task; checkpoints and approvals preserve or constrain that stream rather than supply whole-system current control.

## S3* — Complementary audit

- State: A
- Function: challenge the primary coding actor's ordinary implementation/reporting path through a separate read-only code-review actor with direct access to operational repository artifacts, then return its findings into subsequent primary control.
- Disturbance / variety regulated: defects, regressions, security issues, inconsistent code or improvement needs that the primary implementation actor's ordinary self-reporting/tool-validation path may miss.
- Claim being audited: that the current code/change state is acceptable with respect to correctness, quality, security and relevant improvement risks.
- Ordinary reporting path: the primary Postal agent performs the coding task through its own conversation/tool loop and can run normal file/shell/test actions before reporting completion.
- Complementary access path: model-facing `subagent_code_reviewer` constructs a new full `Agent` under the dedicated `CODE_REVIEWER` definition, with its own session/context/turn budget and direct read-only `read`, `grep`, and `list_directories` access to the workspace.
- Independence boundary: the reviewer is not a routine deterministic checker inside the primary tool sequence. It is a separately instantiated model actor with a fresh child context and audit-specific prompt, narrowed to read-only evidence access; it reads operational artifacts rather than merely accepting the parent's completion claim. It shares the repository boundary and provider configuration, so independence is complementary rather than institutional/external.
- Who acts on findings: the primary model-backed Postal actor receives the reviewer result as the `SubAgentTool` tool result in its ordinary conversation context and can respond with edits, tests, further investigation or another audit invocation.
- Decisive decision or feedback right: the child reviewer owns the audit judgment over directly inspected code; the parent owns subsequent corrective operational choices after receiving those findings.
- Decision owner: autonomous model-backed reviewer in supported `auto`/`yolo` modes; deterministic registry/approval machinery transports and constrains invocation but does not make the audit judgment.
- Supporting / enforcement mechanisms: default registration of all subagent tools; child `Agent` construction; narrowed read-only tool set; turn timeout/cap; parent progress/result transport; approval policy.
- Closure path: primary model invokes `code_reviewer` → separate reviewer Agent directly inspects code and forms findings → `SubAgentTool` returns findings as a tool result → parent conversation receives the audit result → primary model can alter subsequent coding/testing actions from that challenge.
- Boundary reachability: `CODE_REVIEWER` is one of the default subagents registered by `create_default_registry`, and first-party `auto`/`yolo` modes allow the primary agent to invoke this mutating-classified subagent without a human owning the audit decision. No custom reviewer implementation is required.
- Why this is / is not agent-owned: removing the reviewer model while retaining read-only tools and result transport removes the independent audit judgment; the remaining machinery cannot decide whether the code has the reviewed defects. Removing the parent after judgment would break corrective return, which is why both roles are stated separately.
- Evidence: [`tools/subagents/subagents.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/tools/subagents/subagents.py); [`tools/registry.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/tools/registry.py); [`agent/agent.py`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/agent/agent.py); [`docs/approvals.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/docs/approvals.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: default `on_request` requires user confirmation before a subagent run because subagents are classified mutating; Methodology 0.3.x does not publish an S3* parent modifier. The `A` state rests on the separately supported autonomous `auto`/`yolo` operating modes and on the model-owned reviewer judgment/return path, not on default-mode human approval.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop over Postal's own current organizational capability was established.
- Disturbance / variety regulated: web search/fetch, persistent key-value memory, current project instructions/skills and context compaction can improve task execution or reuse, but they do not establish the required outside-and-then organizational adaptation function.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: web `search`/`fetch`; persistent `memory`; skills; current configuration; context pruning/compaction; model switching.
- Closure path: no external/future distinction → adaptation-option generation → returned change to present organizational capability/S3 path was established.
- Why this is / is not agent-owned: the model can retrieve external information and store reusable facts while solving tasks, but neither current-task sensing nor persistence alone constitutes prospective adaptation of the harness organization.
- Evidence: [`docs/tools.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/docs/tools.md); [`README.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: user/developer changes to tools, subagents, skills or configuration can adapt future runs, but ordinary extensibility is not a first-party closed S4 function.

### Absence scope

- Surfaces inspected: web tools; persistent memory; skills/MCP integration; model/config controls; context pruning/compaction; plan/subagent definitions; README roadmap and configuration-oriented extension surfaces.
- Plausible first-party paths checked: environmental monitoring, future-scenario modeling, provider/tool capability scouting, autonomous generation/evaluation/adoption of new capabilities, persistent lesson-to-capability change and adaptation proposals returned into current control.
- Why no material first-party path remains: external information and memory enter current/future task context but no shipped loop turns prospective environmental distinctions into adaptation options that change Postal's current organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: approval modes, dangerous-command rules, path-boundary confirmation, allowed tools, configuration and project instructions constrain ordinary operation but are not themselves an identity/ultimate-policy decision loop.
- Decisive decision or feedback right: not established for S5-level identity or ultimate policy.
- Decision owner: not established at S5; operator/developer configuration supplies constraints outside a qualifying runtime policy-identity closure.
- Supporting / enforcement mechanisms: approval manager; `DANGEROUS_PATTERNS`; outside-workspace confirmation; `allowed_tools`; configuration files; `AGENTS.md`; model/provider selection.
- Closure path: absent at S5 level; no identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned policy governing subsequent operation path was found.
- Why this is / is not agent-owned: the agent operates within configured approval/safety policy and cannot be credited with ultimate authority merely because it is autonomous inside that envelope. Operator approval of an ordinary tool call is likewise not S5.
- Evidence: [`docs/approvals.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/docs/approvals.md); [`README.md`](https://github.com/andrefetch/postal/blob/8631e85f01cd42d72470289c29ecb3c738a87f0d/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: maintainer governance and future configuration changes are adjacent to the assessed product runtime and are not imported as S5 closure.

### Absence scope

- Surfaces inspected: approval modes and hard safety rules; config/project overrides; `allowed_tools`; AGENTS/skills behavior; model/provider controls; session commands; contributor/repository governance adjacency.
- Plausible first-party paths checked: runtime constitution/identity revision; agent-owned ultimate-policy choice; parent escalation of identity-level disputes; durable policy decisions returned into the running harness; project governance wired as a product policy authority.
- Why no material first-party path remains: the inspected mechanisms enforce or expose operator/developer-authored constraints and ordinary task approvals. No boundary-reachable S5-level issue/authority/return loop is supplied.

## Recursion

Each specialized subagent is built from the same full `Agent` class and receives its own session/context, local delegated goal, narrowed tool environment and bounded autonomy. This is enough to treat an invoked child as a distinct subordinate S1 for functional analysis, especially the complementary reviewer path. The evidence does not establish that a child also possesses the full metasystemic organization required to call it a recursively viable system, so no stronger recursion claim is made.

## Variety and escalation

Postal attenuates operational variety through approval modes, dangerous-command checks, path-boundary confirmation, narrowed child tool sets, turn limits, context pruning/compaction and loop detection. It amplifies operational capacity with file/shell/network tools, MCP, skills, persistent memory and specialized full-loop child agents.

The material audit escalation path is model-owned in autonomous modes: the primary actor can escalate uncertainty about code quality to `code_reviewer`; the reviewer obtains complementary read-only evidence and returns a judgment; that result re-enters the primary model context for corrective work. Ordinary user confirmation remains an optional operational gate in interactive modes rather than a published S3*/S5 ownership state.

## Evidence gaps

- Parallel subagents are explicitly roadmap-only at the frozen revision, so no current simultaneous multi-S1 coordination or whole-current population control is credited.
- The S3* autonomy claim depends on supported `auto`/`yolo` modes; default `on_request` inserts a human approval gate before the reviewer invocation.
- No external-and-prospective capability adaptation loop was found for S4; web/memory reuse is intentionally insufficient.
- No runtime identity/ultimate-policy closure was found for S5.
