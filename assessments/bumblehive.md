---
harness_id: bumblehive
project_name: BumbleHive
repository: https://github.com/wxhcore/bumblehive
review_ref: c09189ae47a19b8e1acbf220d0b60eaa804cd4e7
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# BumbleHive

## Review boundary

- System in focus: one instantiated first-party BumbleHive Python SDK/runtime at pinned revision `c09189ae47a19b8e1acbf220d0b60eaa804cd4e7`, centered on `BumblehiveRuntime`, `AgentLoop`, `ToolCallingRunner`, tool/MCP execution, runtime context, sessions/history and user-installed skills.
- Purpose and identity: provide a lightweight reusable Python runtime that closes a model/tool Agent Loop for application developers while owning tool lifecycle, context construction, session persistence, Skills and provider adaptation around the model call.
- Relevant environment: application/user requests, external model-provider responses, file/shell/API/MCP tool results, caller-selected workspace and runtime configuration, user-installed skills and persisted conversation state.
- Standard-distribution boundary: the installable reusable Python SDK under `src/bumblehive/**` and its first-party runtime mechanisms. External model endpoints and MCP/business services remain environmental dependencies and do not donate organizational ownership.
- Credited operating / distribution surfaces: `BumblehiveRuntime`; `AgentLoop`; `ToolCallingRunner`; first-party ToolManager/built-in tool/MCP execution; ContextBuilder; SessionManager and persisted checkpoints/recovery; SkillsManager; provider manager; observability hooks/events insofar as they are reachable runtime support.
- Adjacent first-party surfaces excluded from ownership: the repository's optional Desktop reference application, `server/**`, `webui/**`, runnable `examples/**`, tests/CI and contributor/development surfaces. In particular, the server-added `sub_agent` tool and the example multi-agent composition demonstrate a downstream construction pattern but are not part of the reusable SDK boundary declared by the project README and therefore do not donate S2/S3*/other ownership to this standalone assessment.
- First-party operating / deployment modes considered: direct stateless `runtime.run`/`stream`/`run_console`; caller-owned `MessageHistory`; managed persisted `session_id`; configured built-in/Python/MCP tools; configured Skills; model-provider-backed operation.
- Recursion level: one instantiated reusable BumbleHive runtime/agent loop is the system-in-focus. Multiple separately instantiated runtimes or server-created sub-agents are separate downstream/application composition unless the core standard distribution itself establishes the higher-level organizational relation.
- Reviewed revision: `c09189ae47a19b8e1acbf220d0b60eaa804cd4e7`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

BumbleHive's installable SDK contains a substantive first-party autonomous operating loop. `BumblehiveRuntime._run_agent` resolves the configured provider, builds an `AgentLoop`, constrains filesystem/tool reach through `ToolPathPolicy`, and passes the request into `ToolCallingRunner`. `ToolCallingRunner` repeatedly asks the model for the next action. When the model emits tool calls, the runtime executes those calls, appends each tool result to the message sequence, checkpoints the updated sequence when configured, and invokes the model again. When the model no longer requests tools, its final content closes the turn. Deterministic iteration/context/path/approval constraints bound this autonomy without selecting the substantive tool call or completion decision.

The runtime also owns conversation/session continuity. A managed `session_id` is loaded and recovered under a per-session lock; the triggering user message is persisted before model execution; model/tool checkpoints are atomically persisted; and interrupted sequences are repaired before later turns. These mechanisms provide continuity and integrity for one conversation, not a cross-S1 coordination or whole-system management function.

The repository contains a richer optional product layer. `server/src/bumblehive_server/subagents.py` registers a `sub_agent` tool that starts a separate read-only child session and can provide an independent second perspective. The root README, however, describes Desktop as an optional reference application built with the Python SDK, and the reusable SDK itself does not register that organizational role. Likewise `examples/runtime/multi_agent.py` shows how an adopter can construct delegation. Under the Profile boundary-provenance rule, those adjacent construction/application surfaces cannot close higher functions for the standalone SDK unless the assessed core mode packages or wires them.

Within the core runtime, sessions, tool parallelism, MCP/provider management and observability do not establish S2 or S3. Per-session locking protects one conversation's history rather than attenuating a concrete disturbance between distinct S1 units. Per-run `max_iterations`, path policies, tool approvals and provider/resource lifecycle are local constraints. The core does not expose a standard whole-organization current view paired with authority to revise commitments, shared resource allocation or priorities across operational units.

Observability hooks, runtime events and checkpoints expose ordinary execution state and recovery evidence but do not establish a complementary independent audit path. Skills are user-installed packages copied into a managed directory and rendered into future prompt context; the core does not itself sense an external/future change, generate or select an adaptation option, and revise a skill/capability on that basis. Finally, caller-supplied `agent.instructions`, dynamic context, platform policy, tool/path configuration and approvals constrain operation but do not create an identity/ultimate-policy issue → legitimate ultimate authority → returned policy decision loop.

Primary evidence:

- [`README.md`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/README.md) — public reusable-SDK boundary and explicit optional Desktop reference-application status.
- [`src/bumblehive/runtime.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/runtime.py) — high-level runtime, provider/tool lifecycle, stateless/history/session modes and core loop construction.
- [`src/bumblehive/agent/loop.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/agent/loop.py) — context construction and handoff to the model/tool runner.
- [`src/bumblehive/agent/runner.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/agent/runner.py) — model-owned tool-call decisions, tool-result feedback and iterative completion loop.
- [`src/bumblehive/session/manager.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/session/manager.py) — persisted conversation checkpoints, per-session locking and interrupted-turn recovery inspected for S2/S3/S4.
- [`src/bumblehive/skills/manager.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/skills/manager.py) — user-installed skill loading/install/remove/reload and prompt-context rendering inspected for S4.
- [`src/bumblehive/config/schema.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/config/schema.py) — caller-owned model, generation, agent-instruction, tool, skill and runtime constraints inspected for S3/S5.
- [`src/bumblehive/agent/context/builder.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/agent/context/builder.py) — configured agent instructions, platform policy, capability context and runtime/environment context inspected for S4/S5.
- [`server/src/bumblehive_server/runtime_service.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/server/src/bumblehive_server/runtime_service.py) and [`server/src/bumblehive_server/subagents.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/server/src/bumblehive_server/subagents.py) — adjacent optional product/reference surfaces inspected for boundary provenance; not credited as owners of the reusable SDK organization.

## S1 — Operations

- State: A
- Function: execute user/application objectives through a model-driven loop that selects tools and arguments, observes environment/tool results and continues until a substantive final response is chosen.
- Disturbance / variety regulated: ambiguous requests, changing model/tool observations, filesystem/API/MCP results, tool failures, changing conversation context and tasks requiring multiple environment interactions.
- Decisive decision or feedback right: choose whether another tool call is required, which exposed tool(s) and arguments to invoke, and when to stop tool use and return the final result.
- Decision owner: the model acting through the first-party `ToolCallingRunner` loop.
- Supporting / enforcement mechanisms: `BumblehiveRuntime` provider/tool setup, ContextBuilder, ToolManager, path policy, tool approval handler, context governance, deterministic maximum iterations, session checkpoints/recovery and observability events.
- Closure path: request/history/context enter `AgentLoop` → model receives exposed tools → model selects tool calls or completion → first-party ToolManager executes selected calls → tool observations are appended to the model context → the model takes another decision → final content is returned and, in managed-session mode, checkpoints persist the changed conversation state.
- Boundary reachability: this loop is the core documented `run`/`stream`/`run_console` path of the installable Python SDK, not behavior borrowed from the optional Desktop/server application.
- Why this is / is not agent-owned: deterministic runtime controls bound the action space and enforce safety/lifecycle constraints, but do not choose the substantive tool names, arguments or completion point. Removing the model decision maker while leaving those mechanisms in place removes the task-level adaptive choice.
- Evidence: [`src/bumblehive/runtime.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/runtime.py); [`src/bumblehive/agent/loop.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/agent/loop.py); [`src/bumblehive/agent/runner.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/agent/runner.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: external model providers supply the model inference capability and external MCP services may supply tools, but the first-party BumbleHive runtime owns the iterative operating organization around those dependencies. Stateless and deterministic support mechanisms do not themselves earn `A`; the reachable model-owned tool/action feedback loop does.

## S2 — Coordination

- State: —
- Function: no material first-party coordination function among multiple distinct S1 operational units is established at the reusable SDK boundary.
- Disturbance / variety regulated: not established at inter-S1 scope.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: per-session locks, independent runtime/session construction, tool execution, caller-defined parallel applications and adjacent server/example sub-agent composition were inspected.
- Closure path: no first-party disturbance-specific inter-S1 attenuation → changed subsequent S1 behavior loop is packaged by the core SDK.
- Why this is / is not agent-owned: a developer can instantiate multiple BumbleHive runtimes or construct an agent-as-tool pattern, but constructor capability alone does not establish S2. The core `SessionManager` lock serializes access to one conversation's persisted history; it does not coordinate separate operational units. The optional server's read-only child-agent tool deliberately gives children separate sessions and restricted permissions, but that application-level topology is outside the credited core boundary and still does not by itself identify a concrete sibling disturbance and adaptive coordination right.
- Evidence: [`src/bumblehive/runtime.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/runtime.py); [`src/bumblehive/session/manager.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/session/manager.py); [`README.md`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/README.md); [`server/src/bumblehive_server/subagents.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/server/src/bumblehive_server/subagents.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: a downstream product composed from BumbleHive may establish genuine S2 and must be assessed as its own system-in-focus.

### Absence scope

- Surfaces inspected: core Runtime/AgentLoop/Runner, managed sessions/locks, ToolManager-facing execution, core configuration, optional server `sub_agent` registration and documented reference-application boundary.
- Plausible first-party paths checked: multiple runtime instances, session locking, parallel tool/sub-agent construction, separate child sessions, shared provider/tool infrastructure and ordinary delegation.
- Why no material first-party path remains: the reusable SDK does not package at least two stable S1 units together with a concrete inter-unit conflict/oscillation and a coordination relation whose result feeds back into their later behavior. Application code must supply that organization.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-management function is established at the reusable SDK boundary.
- Disturbance / variety regulated: not established at whole-system current-operation scope.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: per-run iteration/context limits, path/tool restrictions, approvals, session locks/recovery, provider/tool resource lifecycle and server-side active-run guarding of settings changes were inspected.
- Closure path: no standard whole-system current view → current resource/commitment/priority decision → changed multi-unit operation loop is packaged.
- Why this is / is not agent-owned: `max_iterations`, path policies and approvals constrain one operating loop; session locks protect one conversation; provider/tool managers own technical resources. The adjacent server counts `_active_runs` primarily to reject configuration/skill/MCP changes while work is active, but that reference-application safeguard neither belongs to the core SDK boundary nor exercises a discretionary current-control right over the active runs themselves.
- Evidence: [`src/bumblehive/runtime.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/runtime.py); [`src/bumblehive/config/schema.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/config/schema.py); [`src/bumblehive/session/manager.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/session/manager.py); [`server/src/bumblehive_server/runtime_service.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/server/src/bumblehive_server/runtime_service.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: a host application can construct current-control behavior around hooks/configuration/cancellation; that downstream owner is not present as a core BumbleHive S3 function.

### Absence scope

- Surfaces inspected: Runtime lifecycle, provider/tool managers as reached through Runtime, per-run limits/path policies, sessions/checkpoints/recovery, configuration schema and adjacent RuntimeService active-run/settings guards.
- Plausible first-party paths checked: runtime manager naming, active-run count, session state, configuration replacement, MCP/skill reload gates, approvals, per-run ceilings and technical resource cleanup.
- Why no material first-party path remains: none combines a whole-organization view of multiple current operations with a first-party right to bargain/revise their commitments, resources, priorities or constraints on behalf of the whole.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit function is established for ordinary core-SDK operation.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: runtime observability hooks/events, model/tool checkpoints, session recovery, tool approvals and the adjacent server's read-only `sub_agent` second-perspective path were inspected.
- Closure path: no core-SDK independent complementary-access findings → corrective current-operation return loop is packaged.
- Why this is / is not agent-owned: events and checkpoints report the same normal execution path and therefore do not add independent access to operational reality. The server-level `sub_agent` can open a separate conversation with direct read-only workspace access and return a second perspective, but it is registered by the optional product/reference layer rather than the reusable SDK. Boundary provenance therefore prevents it from upgrading the standalone core assessment.
- Evidence: [`src/bumblehive/agent/runner.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/agent/runner.py); [`src/bumblehive/session/manager.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/session/manager.py); [`README.md`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/README.md); [`server/src/bumblehive_server/subagents.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/server/src/bumblehive_server/subagents.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: the optional server/reference application is a plausible separate system-in-focus for a future assessment; this assessment does not claim that its read-only child-agent path could never realize S3* in that wider product boundary.

### Absence scope

- Surfaces inspected: core Runner checkpoints, session repair/persistence, runtime observability hooks/events, approval support, optional server sub-agent implementation and public boundary documentation.
- Plausible first-party paths checked: traces/events, checkpoint/replay-like persistence, ordinary approvals, model/tool errors and the adjacent read-only second-perspective sub-agent.
- Why no material first-party path remains: the core operating distribution has no materially independent auditor with complementary access and corrective return; the strongest candidate resides in the explicitly optional reference-product layer excluded from ownership.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective capability-adaptation loop is established.
- Disturbance / variety regulated: not established as future-oriented organizational adaptation.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persisted conversation history, dynamic runtime context, external tool/MCP observations, user-installed Skills, skill file snapshot/reload behavior and parent-controlled server skill/MCP configuration were inspected.
- Closure path: no first-party external/future distinction → generated/selected adaptation option → durable capability change → later-operation loop is packaged.
- Why this is / is not agent-owned: SkillsManager can install, remove, reload and render user-provided `SKILL.md` packages into future prompts, but it does not itself detect environmental/future change or decide how a skill should be revised. Session history records prior operation; dynamic context reflects current environment; neither is prospective adaptation merely because it influences later prompts.
- Evidence: [`src/bumblehive/skills/manager.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/skills/manager.py); [`src/bumblehive/session/manager.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/session/manager.py); [`src/bumblehive/agent/context/builder.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/agent/context/builder.py); [`server/src/bumblehive_server/runtime_service.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/server/src/bumblehive_server/runtime_service.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: an adopter can use hooks, external evaluations or human skill editing to build an adaptation organization. The reusable framework does not package that missing decision/feedback path.

### Absence scope

- Surfaces inspected: SkillsManager install/remove/reload/render paths, sessions/history/recovery, dynamic/environment context, MCP/tool integration, provider configuration and adjacent server settings APIs.
- Plausible first-party paths checked: skill reload, persisted memory/history, changing external tool data, dynamic context, provider/MCP replacement and human-uploaded capabilities.
- Why no material first-party path remains: all inspected mechanisms either expose current information, persist past operation or apply externally authored capability/configuration changes; none creates the required first-party prospective adaptation option from external/future evidence and returns that decision into current capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the declared runtime recursion.
- Disturbance / variety regulated: not established at identity/ultimate-policy scope.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: caller-configured agent instructions, static built-in platform/tool-use instructions, tool/path restrictions, approval handlers, generation settings, selected skills/tools and external provider configuration were inspected.
- Closure path: no identity/ultimate-policy issue → legitimate ultimate authority decision → returned decision governing later operation loop is packaged.
- Why this is / is not agent-owned: `agent.instructions` and prompt context can describe behavior, while path/tool/approval settings constrain it, but generic prompts and configured constraints are not S5. The core exposes no function-specific runtime process that raises identity-level tension to an ultimate authority and returns the resulting policy decision into operation.
- Evidence: [`src/bumblehive/config/schema.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/config/schema.py); [`src/bumblehive/agent/context/builder.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/agent/context/builder.py); [`src/bumblehive/runtime.py`](https://github.com/wxhcore/bumblehive/blob/c09189ae47a19b8e1acbf220d0b60eaa804cd4e7/src/bumblehive/runtime.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: a parent application may define identity/governance around BumbleHive. That authority is not a first-party S5 closure of the reusable SDK itself.

### Absence scope

- Surfaces inspected: agent instructions/system-context construction, runtime configuration, tool/path restrictions, approvals, Skills, provider/MCP configuration and optional product settings surfaces.
- Plausible first-party paths checked: system/agent prompts, policy-like platform instructions, user approval, tool permissions, skill selection and runtime settings.
- Why no material first-party path remains: these are behavior/configuration constraints or ordinary task approvals. No reviewed path establishes an identity/ultimate-policy issue, legitimate ultimate authority and a returned policy decision at the assessed recursion.

## Recursion

The SDK supports nested construction patterns but does not by itself establish a recursive viable organization. A downstream application can instantiate multiple runtimes or expose one runtime as a tool to another; the optional server does exactly this for read-only child sessions. Such a composition becomes a separate system-in-focus and needs its own evidence for S1–S5. The standalone reusable runtime therefore is not credited with higher-recursion coordination/control solely from construction capability.

## Variety and escalation

BumbleHive attenuates local operating variety with context governance, configured tool exposure, path restrictions, approvals, per-run iteration limits and session serialization. It amplifies S1 response variety through model reasoning, built-in/Python/MCP tools, Skills and persisted context. Errors and interrupted message sequences have explicit local recovery paths. No separate whole-system escalation relation is credited because these mechanisms remain within the current operating loop or its caller-defined constraints rather than closing S3/S4/S5 at a higher recursion.

## Summary

BumbleHive is an autonomous single-runtime harness at the reviewed reusable-SDK boundary. Its first-party model/tool loop closes S1 autonomously. The same repository demonstrates how applications can add child agents and richer product behavior, but those optional/reference surfaces do not donate organizational functions to the core SDK. Session locking, persistence, Skills, observability, approvals and configurable prompts remain support/construction mechanisms without standalone S2, S3, S3*, S4 or S5 closure.
