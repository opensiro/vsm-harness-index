---
harness_id: nanobot
project_name: nanobot
repository: https://github.com/HKUDS/nanobot
review_ref: 24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# nanobot

## Review boundary

- System in focus: the first-party nanobot personal-agent runtime at the pinned revision, including the top-level agent loop, model/tool runner, built-in tools, session/context state, subagent manager, gateway/automation paths, Dream memory consolidation, and the `my` runtime self-management tool.
- Purpose and identity: provide a lightweight self-hosted personal AI agent that turns user or scheduled work into model-selected tool actions, persists conversational/project context, and can delegate bounded work to background subagents.
- Relevant environment: user and channel messages, files and shell state, web/tool results, external APIs and MCP servers, model-provider responses, and scheduled/automation triggers.
- Standard-distribution boundary: the shipped nanobot Python runtime and its supported CLI/gateway/API execution paths at the pinned revision. External model providers, messaging platforms, MCP servers, web services, and user-authored downstream applications are outside the first-party ownership boundary.
- Credited operating / distribution surfaces: `nanobot/agent/loop.py`, `nanobot/agent/runner.py`, the built-in tool loader/registry and tools, `SubagentManager`, session/context/memory machinery, gateway/cron automation, Dream, and `MyTool`/`RuntimeControl` as shipped in the normal distribution.
- Adjacent first-party surfaces excluded from ownership: repository tests, examples, contributor/development material, CI/release machinery, and documentation are used only as corroborating evidence; they do not supply organizational ownership unless their path is wired into the credited runtime mode.
- First-party operating / deployment modes considered: normal CLI/gateway/API agent execution; background/inline subagent execution; scheduled gateway work and Dream; default read-only `my` self-inspection; and the documented optional `tools.my.allow_set: true` mode that gives the running agent the shipped self-management setter.
- Recursion level: one running nanobot personal-agent organization is the system-in-focus. Spawned subagents are bounded operational workers; spawning and nesting do not establish that each is a recursively viable lower-level system.
- Reviewed revision: `24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f`.
- Observation date: 2026-09-20.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

The candidate pin from batch #89 is preserved. Current upstream `main` is newer, but this standalone assessment deliberately classifies only the frozen candidate revision.

## Repository architecture

nanobot owns its own agent runtime rather than delegating the reasoning/tool loop to another agent product. `AgentLoop` handles inbound routing, sessions, workspace selection, commands, background tasks, compaction and outbound delivery, while `AgentRunner` performs the repeated provider → tool-call → tool-result → next-provider-turn cycle under first-party iteration and context controls. Built-in tools expose filesystem, execution, web/MCP and other environment actions.

`SubagentManager` can launch inline or background subagents through the same first-party runner. It gives each worker an isolated tool registry, tracks runtime phase/tool events/usage, and uses a semaphore to bound concurrency. These workers are task-decomposition paths; the reviewed code does not supply a separate disturbance-specific peer-coordination function merely because several workers can run.

The runtime also provides durable sessions, context compaction and long-term memory. Dream periodically consumes archived conversation history through a restricted tool registry and may update `SOUL.md`, `USER.md`, `memory/MEMORY.md`, and reusable `skills/<name>/SKILL.md` files. That is meaningful long-term behavioral adaptation, but the supplied Dream objective is retrospective consolidation of observed conversations and recurring workflows rather than an external-and-prospective S4 intelligence loop.

The distinctive metasystem construction surface is `MyTool`. It can inspect a runtime-wide snapshot including model/runtime limits and live subagent status. The shipped setter can change model preset, iteration budget, provider retry mode, tool-result limits and related safe runtime values. The setter is deliberately disabled by default (`tools.my.allow_set: false`) and becomes available only when the operator/developer enables the first-party configuration switch. Core infrastructure, credentials and security boundaries remain protected.

Primary evidence:

- [`nanobot/agent/loop.py`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/agent/loop.py)
- [`nanobot/agent/runner.py`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/agent/runner.py)
- [`nanobot/agent/subagent.py`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/agent/subagent.py)
- [`docs/my-tool.md`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/docs/my-tool.md)
- [`nanobot/agent/tools/self.py`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/agent/tools/self.py)
- [`nanobot/agent/memory.py`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/agent/memory.py)
- [`nanobot/templates/agent/dream.md`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/templates/agent/dream.md)
- [`nanobot/templates/agent/identity.md`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/templates/agent/identity.md)

## Operational model

The primary S1 is the running nanobot agent loop. It receives a user, API, channel or scheduled objective, asks the configured model for the next action, executes first-party tools, observes their results and continues until a final response or runtime stop condition. Background subagents reproduce a bounded version of this operational loop for delegated tasks and return their results to the originating context.

Developer/operator configuration defines providers, models, tool availability, workspace/security bounds, automation and whether the agent may use the shipped self-management setter. Deterministic runtime machinery enforces these bounds. Dream can revise durable memory/profile/skills from accumulated history, while `MyTool` supplies a separate live-current-control construction path when mutation is enabled.

## S1 — Operations

- State: A
- Function: autonomously transform user/scheduled objectives into environment-facing model/tool work and returned outcomes.
- Disturbance / variety regulated: heterogeneous task instructions, model responses, tool results/errors, filesystem/shell/web state, and follow-up messages arriving during an active trajectory.
- Decisive decision or feedback right: choose the next model-directed tool/action or stop with a final response based on the current conversation and returned tool observations.
- Decision owner: the running nanobot agent/model actor inside the first-party `AgentRunner` loop.
- Supporting / enforcement mechanisms: `AgentLoop` routing/session machinery, the tool registry/loader, provider adapters, workspace restrictions, iteration limits, context management and execution backends.
- Closure path: each tool result and newly injected message is returned to the first-party runner context and can change the next model-selected action until completion.
- Boundary reachability: the credited `AgentLoop`/`AgentRunner` and built-in tool path are the normal shipped CLI/gateway/API runtime, not a development-only or external-agent surface.
- Why this is / is not agent-owned: the runtime supplies the loop and tool execution, but the discretionary next-action choice is produced by the autonomous model actor on each iteration rather than being a fixed workflow transition selected by the developer.
- Evidence: pinned `agent/loop.py` and `agent/runner.py`; `subagent.py` corroborates that the same first-party runner executes delegated operational work.
- Basis: `structural`.
- Confidence: high.
- Caveats: model/tool/provider choice and runtime limits are developer/operator-configured constraints around the operational discretion.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 anti-oscillation or conflict-regulation function was established at the declared recursion.
- Disturbance / variety regulated: none established as an S2 witness; multiple subagents can coexist, but the reviewed runtime does not identify a concrete sibling interference/conflict/oscillation that a first-party coordination relation specifically attenuates.
- Decisive decision or feedback right: no S2-specific coordination decision right is supplied.
- Decision owner: not established.
- Supporting / enforcement mechanisms: subagent task spawning, per-session task tracking, result return, message transport, isolated tool registries, and a semaphore that caps concurrent subagents.
- Closure path: delegation results return to the caller and the semaphore admits queued work, but neither path is tied to regulation of a specific inter-S1 disturbance.
- Why this is / is not agent-owned: bounded concurrency and delegation are execution mechanisms; no autonomous or constructor-owned S2-specific discretion is evidenced.
- Evidence: pinned `nanobot/agent/subagent.py`, `agent/loop.py` and runner/tool paths.
- Basis: `structural`.
- Confidence: high.
- Caveats: a downstream application may add task dependencies, resource reservations or collision policy, but that composed organization would be a different system-in-focus.

### Absence scope

- Surfaces inspected: first-party agent loop/runner, `SubagentManager`, task/session tracking, message bus/routing surfaces, concurrency limits, tool loading and the documented multi-agent paths at the pinned revision.
- Plausible first-party paths checked: subagent semaphore/admission, session task registry, delegation/result return, generic messaging and shared runtime state.
- Why no material first-party path remains: the identified mechanisms bound or transport parallel work but are not tied to a concrete inter-S1 interference/conflict/oscillation plus a feedback path that changes later S1 behaviour as required for S2.

## S3 — Inside-and-now control

- State: C
- Function: regulate the running nanobot organization by observing current runtime state and revising selected live capability/resource constraints.
- Disturbance / variety regulated: current task complexity, remaining execution latitude, model/runtime suitability, provider retry behavior, tool-result volume, and observable active-subagent state.
- Decisive decision or feedback right: choose whether to alter the live model preset, iteration budget, provider retry mode, tool-result limit or other explicitly exposed safe runtime values after inspecting current state.
- Decision owner: constructor-owned at the reviewed standard boundary: first-party `MyTool` exposes the function-specific decision/feedback path, but the developer/operator must authorize the agent setter with `tools.my.allow_set: true`; default distribution leaves the tool read-only.
- Supporting / enforcement mechanisms: `RuntimeControl` snapshots/setters, type/range validation, protected/read-only fields, session-scoped model-preset handling and audit logging.
- Closure path: an authorized `my set` call invokes the first-party runtime setter; the changed preset/limit/retry/runtime value is then used by subsequent agent operation, while protected security/core state remains outside that authority.
- Boundary reachability: `MyTool` and its runtime-control setters ship in the normal first-party runtime. The missing piece is deliberately the constructor authorization flag, not an adjacent test, dogfood agent or external control service.
- Why this is / is not agent-owned: the shipped mechanism is intentionally capable of agent self-regulation, but out-of-box `allow_set: false` prevents the autonomous agent from owning the decisive mutation right. Enabling the supplied setter composes that authority, which is the Methodology's narrow `C` case rather than `A`.
- Evidence: pinned [`docs/my-tool.md`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/docs/my-tool.md) and [`nanobot/agent/tools/self.py`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/agent/tools/self.py).
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: generic operator configuration is not credited as a parent-governed S3 mode; the positive claim is the function-specific first-party constructor path available to a running agent.
- Whole-system current view: the `my` snapshot exposes current model/runtime limits, retry/tool-result settings and observable subagent statuses from the running organization rather than only one delegated task's local state.
- Current-control decision scope: selected current model and execution-budget/runtime constraints that immediately shape subsequent work; credentials, core subsystems and security boundaries are explicitly blocked.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit path was established beyond ordinary operational feedback, runtime observability and memory integrity machinery.
- Disturbance / variety regulated: no separate audit disturbance is supplied; tool errors, model retries and runtime checks are part of the ordinary production path.
- Decisive decision or feedback right: no first-party independent audit judgment with corrective return into current control was established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: tool-result feedback, hooks/status telemetry, Dream's diff-grounded memory commit messages, logs and runtime validation.
- Closure path: ordinary failures can change the same agent trajectory and Dream can verify its own file edits, but no complementary access path challenges an operational claim independently and returns findings into S3.
- Why this is / is not agent-owned: no separate agent or sufficiently independent first-party auditor is wired into the credited runtime mode.
- Evidence: pinned runner/tool feedback paths, `subagent.py`, `memory.py` Dream helpers, and repository search across verifier/critic/reviewer/evaluation surfaces.
- Basis: `structural`.
- Confidence: high.
- Caveats: an external evaluator or downstream reviewer could be composed around nanobot, but external composition is outside this standalone boundary.

### Absence scope

- Surfaces inspected: agent loop/runner hooks and tool feedback, subagent runtime/status machinery, Dream verification/diff/audit helpers, logs, tests/docs and repository search for verifier/critic/reviewer/evaluator paths.
- Plausible first-party paths checked: routine tool validation/retry, subagent status observation, Dream edit verification and git-diff-grounded audit records.
- Why no material first-party path remains: each identified check is either on the ordinary production/memory-maintenance path or lacks a materially independent access-and-corrective-control loop, so none closes complementary S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented organizational intelligence/adaptation loop was established.
- Disturbance / variety regulated: Dream reacts to accumulated conversation history and recurring workflows, but does not separately model changing external conditions or possible future environments for the organization.
- Decisive decision or feedback right: no first-party path was found that turns future/external distinctions into adaptation options and returns them to present S3 capability.
- Decision owner: not established.
- Supporting / enforcement mechanisms: Dream scheduling, long-term memory, `SOUL.md`/`USER.md` updates, reusable skill creation, history cursors, context compaction and normal web/tool access during S1 work.
- Closure path: Dream can change future prompts/memory/skills based on past interactions, but this is retrospective consolidation rather than the required outside-and-then S4 conversation with present control.
- Why this is / is not agent-owned: the Dream agent owns some memory/skill editing discretion, but the organizational function evidenced is memory consolidation and workflow reuse, which the Profile explicitly distinguishes from S4 without an external/prospective adaptation witness.
- Evidence: pinned [`nanobot/agent/memory.py`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/agent/memory.py), [`nanobot/templates/agent/dream.md`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/templates/agent/dream.md), Dream configuration/scheduling and identity-context paths.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: recurring autonomous learning-like behavior is materially useful but is not promoted to S4 solely because it changes future agent behavior.

### Absence scope

- Surfaces inspected: Dream memory store/consolidation/tools/prompt, long-term profile/memory files, skill creation/reuse, heartbeat/cron automation, ordinary external web/tool access and runtime self-management.
- Plausible first-party paths checked: periodic Dream, repeated-workflow skill synthesis, durable project/user/profile updates, heartbeat and scheduled jobs, and agent access to current external tools.
- Why no material first-party path remains: these paths are retrospective consolidation, recurring operations or current-task sensing; none supplies a distinct future/external model, adaptation-option development and return path into current S3 capability.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure was established for the nanobot organization.
- Disturbance / variety regulated: profile text, platform policy and operator configuration constrain behavior, but no identity-level dispute/proposal is routed to legitimate ultimate authority through a first-party closure loop.
- Decisive decision or feedback right: no first-party runtime right was found that authoritatively settles system identity/ultimate-policy questions and returns that decision to govern subsequent operation.
- Decision owner: not established as an S5 function; users/developers configure the agent and Dream may maintain profile files, but those paths do not by themselves instantiate ultimate-policy authority.
- Supporting / enforcement mechanisms: `SOUL.md`, `USER.md`, platform policy injection, tool/security configuration, Dream's restricted profile editing and general operator settings.
- Closure path: profile/config changes can alter later behavior, but no S5-specific issue → legitimate authority → authoritative decision → returned-governance path is supplied.
- Why this is / is not agent-owned: Dream may edit behavioral profile content and the operator can edit configuration, yet neither path is evidenced as legitimate ultimate-policy closure rather than ordinary personalization/memory/configuration.
- Evidence: pinned [`nanobot/templates/agent/identity.md`](https://github.com/HKUDS/nanobot/blob/24c41a6af0736330cd9c67b3c9d1ec9adeefdf5f/nanobot/templates/agent/identity.md), Dream prompt/memory machinery, `MyTool` protection boundaries and runtime configuration.
- Basis: `structural`.
- Confidence: high.
- Caveats: a separately governed deployment could retain S5 at a human or institutional parent recursion, but the standalone nanobot distribution does not establish that function-specific parent loop.

### Absence scope

- Surfaces inspected: runtime identity prompt, `SOUL.md`/`USER.md` profile handling, Dream profile editing, platform policy injection, tool/security configuration, operator settings and self-management protection rules.
- Plausible first-party paths checked: Dream-authored profile changes, direct operator configuration, permission/security controls and the `my` self-management surface.
- Why no material first-party path remains: all identified paths personalize, constrain or maintain operation without reconstructing an identity/ultimate-policy issue reaching legitimate ultimate authority and returning as authoritative governance.

## Distributed OSS parent arrangement

The public repository has maintainers and contributors, but repository governance is adjacent to the assessed self-hosted product runtime. No organization-level S3/S4/S5 parent loop is inferred from open-source contribution or release authority. Likewise, an individual operator's ability to edit local configuration is not promoted to `(P)` without a function-specific parent decision and returned closure at the declared runtime recursion.

## Self-hosted and non-human modes

nanobot is self-hosted and deliberately exposes substantial operator configuration. The reviewed default `my` mode is read-only, while the documented `allow_set: true` option composes agent-owned use of the first-party S3 setter; this supports `S3=C`, not an operator `P` mode. Human permission/configuration surfaces elsewhere remain task/security/installation controls unless a specific S3/S4/S5 parent loop is established.

## Recursion

Subagents run autonomous first-party model/tool loops for bounded delegated work, but the reviewed evidence does not establish that each carries the metasystemic functions needed for recursive viability. They are therefore treated as operational decomposition rather than automatically viable nested systems.

## Variety and escalation

nanobot attenuates operational variety through tool/workspace constraints, iteration and context limits, concurrency caps, session compaction and protected self-management fields. It amplifies operational capacity through tools, MCP, subagents, persistent memory, scheduled work and optional runtime self-tuning.

Operational exceptions generally return through the same model/tool loop as errors or observations. Subagent results return to the originating session. The standard distribution also exposes user/operator control through configuration and channels, but no separate algedonic/escalation path was established that changes the six-state classification.

## Evidence gaps

No unresolved evidence gap requires `?`. The review covered the pinned first-party runtime loop, tool execution, subagents, runtime self-management, Dream/memory/skills, identity/configuration, scheduling and plausible audit/coordination paths broadly enough to support the published positive and negative states. Current upstream `main` contains later changes and requires a separate new-ref reassessment if those changes are to become canonical evidence.

## Admission conclusion

Canonical vector at the frozen batch #89 revision: `A — C — — —`.

nanobot qualifies for Index admission because the pinned repository ships an autonomous first-party operational agent loop. Its `my` self-management path is a genuine S3-specific constructor surface: the runtime provides whole-system inspection plus live setters, but the autonomous mutation right is deliberately disabled by default and must be enabled by the constructor. Subagent concurrency/delegation does not meet the S2 disturbance witness, Dream remains retrospective memory/skill consolidation rather than S4, and no independent S3* or ultimate-policy S5 closure is supplied.
