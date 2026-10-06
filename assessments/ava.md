---
harness_id: ava
project_name: AVA
repository: https://github.com/Artificial-Source/AVA
review_ref: 1b886dc5b80c6bf459cfe47550aa197537d5916d
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AVA

## Review boundary

- System in focus: the first-party AVA C++23 coding-agent runtime at frozen revision 1b886dc5b80c6bf459cfe47550aa197537d5916d, including the model/tool agent loop, built-in tools, built-in general/explore subagents, SubagentCoordinator/background-job control, permissions, sessions/compaction, RPC/ACP surfaces, MCP/plugin integration and interactive/headless modes.
- Purpose and identity: perform software-engineering work through a model-backed coding agent that can inspect/edit/run project state, delegate bounded work to child sessions, observe and selectively steer/cancel live delegated jobs, and persist/resume coding sessions.
- Relevant environment: user goals and permissions, repository/workspace state, process/tool/test results, provider/model outputs, child-job status/results, session history, MCP/plugin services and runtime configuration.
- Standard-distribution boundary: shipped AVA runtime plus repository-owned built-in agent/tool/session/job/permission/RPC/ACP machinery. External model providers, MCP servers, plugins, user/project agent-definition files and the user's repository are dependencies/configuration and cannot donate organizational ownership.
- Credited operating / distribution surfaces: src/ava/agent, src/ava/app/runtime and session controller, built-in tools and general/explore subagents, SubagentCoordinator/background jobs, permissions, sessions, TUI/print/RPC/ACP operation.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/goals/plans/history, engineering-time independent reviews, tests except as structural corroboration, and user-configured primary/subagent definitions such as the documented reviewer example.
- First-party operating / deployment modes considered: ordinary TUI/headless coding, built-in foreground/background task subagents, model-visible job control, interactive/RPC job control, resumable sessions, supported permission/provider modes and ACP/RPC automation.
- Recursion level: one AVA coding session plus its instantiated child coding sessions. The parent model-backed coding agent and write-capable general subagents can own bounded S1 outcomes at this level.
- Reviewed revision: 1b886dc5b80c6bf459cfe47550aa197537d5916d.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

AVA's core AgentLoop performs the model/tool coding cycle through first-party tool dispatch, permissions, provider calls and append-only session state. The task tool can create a durable child session using either the built-in general agent, which inherits the parent's visible operational tools apart from recursive task/job/todowrite, or the built-in read-only explore agent. Child work may execute foreground or background and returns a bounded result to the parent.

The process-local SubagentCoordinator tracks owner-bound jobs and exposes model-visible job operations including list/status/wait/result/cancel/steer. Steering targets one exact running owned job and is consumed at a safe provider boundary. Background completion is later delivered to the owning parent as a synthetic turn once the parent is idle. TUI/RPC surfaces additionally expose inspection and promotion.

AVA does not, at the frozen revision, establish a standard first-party cross-child file/worktree/lease arbitration loop. Several write-capable general children may exist under the concurrency cap, but the inspected runtime does not supply a peer-interference-specific ownership/path/conflict feedback mechanism. Likewise, only general and explore are built-in agent types; the documented reviewer is a user-configured Markdown definition, so it cannot be imported as a standard S3* owner.

## Operational model

The parent model owns open-ended coding and delegation decisions. Child general agents own their bounded engineering choices. Permission gates, process supervision, session leases, tool scheduling and job limits constrain execution but do not themselves supply higher-function decision ownership.

The same parent model can inspect its current owned job set and selectively steer or cancel one running commitment. This is a genuine current-control return path rather than mere completion notification. Session persistence, compaction, trust, provider settings and extensions support continuity/current operation but do not close S4 or S5.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify software through model-selected coding/tool actions, directly or in bounded child sessions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, build/test/process failures, tool/provider errors, context pressure, permission boundaries and delegated subtasks.
- Decisive decision or feedback right: choose substantive engineering actions, interpret results, decide repairs/delegation and decide when the assigned objective is complete.
- Decision owner: the active model-backed AVA parent agent and, when instantiated, model-backed general subagents for their delegated outcomes.
- Supporting / enforcement mechanisms: built-in tools, permissions, provider transport, session state, task dispatch, context compaction, cancellation and RPC/ACP/TUI hosts.
- Closure path: user/parent goal → model chooses repository/tool action or task delegation → first-party runtime executes → evidence/result returns → model revises work until completion or a boundary stops it.
- Boundary reachability: ordinary TUI, print and RPC execution instantiate the same first-party agent/tool runtime; task is a standard model-visible tool.
- Why this is / is not agent-owned: deterministic runtime code transports/constrains actions, but the model owns open-ended engineering selection and interpretation.
- Evidence: [README.md](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/README.md); [src/ava/agent/agent_loop.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/agent/agent_loop.cpp); [src/ava/agent/tool_dispatch_task.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/agent/tool_dispatch_task.cpp); [docs/core/subagents.md](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/docs/core/subagents.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: explore is read-only and not counted as a write-capable peer by itself; positive S1 does not require every configured/custom agent to be first-party.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 interference-attenuation loop is established for concurrently active write-capable child agents.
- Disturbance / variety regulated: multiple general subagents may operate against the same project state, but no standard first-party path was found that owns file/path claims, worktree isolation, peer conflict detection or mutual-adjustment feedback.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: concurrency limits, child ownership, job IDs, recursive-task hiding, permissions and per-session/process synchronization bound execution but do not coordinate peer coding interference.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: parent delegation and a maximum concurrent-job count are not enough without a concrete peer-interference relation and attenuation/feedback loop.
- Evidence: [docs/core/subagents.md](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/docs/core/subagents.md); [src/ava/agent/subagent_coordinator.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/agent/subagent_coordinator.cpp); [src/ava/agent/subagent_launch.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/agent/subagent_launch.cpp).
- Basis: structural absence review.
- Confidence: high.
- Caveats: the runtime has extensive locking/process/session safety, but those locks protect runtime state and authority rather than regulating a demonstrated peer-S1 coding collision.

### Absence scope

- Surfaces inspected: task launch, SubagentCoordinator/background registry, built-in agent capabilities, child workspace/session handling, process supervision, tool scheduling and runtime/session locks.
- Plausible first-party paths checked: file/path leases, per-agent worktrees, write ownership, dependency graph, conflict detector, merge arbiter and parent-selected peer mutual-adjustment protocol.
- Why no material first-party path remains: located mechanisms manage child lifecycle and runtime integrity, not a concrete distinct-S1 work-interference/attenuation/feedback loop.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current set of delegated operational commitments by observing owner-bound job state and selectively steering or cancelling live child work.
- Disturbance / variety regulated: a running child that is misdirected, no longer needed, blocked, needs new information, or should be stopped while other current work continues.
- Decisive decision or feedback right: inspect current jobs, request status/result, send a bounded steer to one exact live child, or cancel a selected owned running job.
- Decision owner: the model-backed parent AVA agent through the model-visible job tool.
- Supporting / enforcement mechanisms: SubagentCoordinator, BackgroundJobRegistry, exact owner-bound job IDs, FIFO steering queue, cooperative cancellation, completion delivery and live snapshots.
- Closure path: parent sees its current job set/status → chooses a particular live commitment → issues job steer/cancel → coordinator delivers the instruction or stop signal to that child → child state/result changes → updated status/completion returns to the parent.
- Boundary reachability: model-visible job control is part of the standard first-party subagent runtime; TUI/RPC add promotion/inspection but are not required for the autonomous claim.
- Why this is / is not agent-owned: runtime code enforces ownership and delivery, while the parent model makes the substantive live intervention decision.
- Whole-system current view: job list/status exposes the parent's active/terminal owned child jobs and their current execution state.
- Current-control decision scope: selective live-child steer and cancel, plus status/wait/result interpretation; user-facing TUI/RPC can additionally promote eligible work.
- Evidence: [docs/core/subagents.md](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/docs/core/subagents.md); [src/ava/agent/job_control.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/agent/job_control.cpp); [src/ava/agent/subagent_coordinator.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/agent/subagent_coordinator.cpp).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic session stop or permission approval is not used for this claim; it rests on selective model-owned current control over the live child-job set.

## S3* — Complementary audit

- State: —
- Function: no material standard first-party independent complementary-audit path is established.
- Disturbance / variety regulated: no bundled independent reviewer is assigned a coding claim, direct evidence channel and returned audit judgment.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: none established.
- Supporting / enforcement mechanisms: built-in explore can gather read-only evidence and custom agent definitions can be configured as reviewers, but neither establishes a bundled review function.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: AVA always provides only general and explore; README/configuration explicitly describe reviewer as something configured by the user. Repository-development review history is outside the running-harness boundary.
- Evidence: [docs/core/subagents.md](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/docs/core/subagents.md); [docs/core/configuration.md](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/docs/core/configuration.md); [README.md](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a parent can delegate a review prompt to explore/general or install a reviewer definition, but generic/configured composition is not a standard first-party S3* constructor.

### Absence scope

- Surfaces inspected: built-in agent catalog, custom-agent configuration, task/subagent execution, repository review references, tests and job-return paths.
- Plausible first-party paths checked: bundled reviewer/verifier, fresh independent code-review role, separate evidence runner, mandatory second pass and automatic corrective verdict gate.
- Why no material first-party path remains: reviewer behavior requires user/project configuration or belongs to repository development history rather than the shipped standard runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no future/external condition is owned by a function that develops adaptation options and returns them into current organizational capability.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: sessions, compaction, custom context resources, providers/models, plugins/MCP/LSP and resumable history affect later work but are persistence/configuration/current capability surfaces.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: preserving history or loading external capabilities does not demonstrate an outside-and-then option-development owner feeding adaptation into current control.
- Evidence: [README.md](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/README.md); [src/ava/agent/context_compaction.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/agent/context_compaction.cpp); [src/ava/app/runtime/Session.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/app/runtime/Session.cpp).
- Basis: structural absence review.
- Confidence: high.
- Caveats: ordinary agents can use web/MCP or persisted context for future-facing work; ad hoc S1 research is not a standard S4 organization.

### Absence scope

- Surfaces inspected: session persistence/compaction, model/provider configuration, plugins/MCP/LSP, custom context/agent resources, RPC/ACP and resumability.
- Plausible first-party paths checked: autonomous learned strategy update, environmental scanning → adaptation options, durable capability reconfiguration and feedback from future modeling into S3.
- Why no material first-party path remains: observed mechanisms store/load/route capabilities or current evidence rather than close a prospective adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level or ultimate-policy conflict is routed to an authoritative S5 owner and returned as governing organizational policy.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permissions, project trust, tool visibility, configured primary agents/system prompts, containment and RPC/ACP policies constrain execution but do not create identity-policy closure.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: agents operate inside developer/user-authored policy and cannot authoritatively redefine AVA's identity or ultimate operating principles.
- Evidence: [src/ava/permissions/permission.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/permissions/permission.cpp); [src/ava/app/project_trust.cpp](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/src/ava/app/project_trust.cpp); [docs/core/configuration.md](https://github.com/Artificial-Source/AVA/blob/1b886dc5b80c6bf459cfe47550aa197537d5916d/docs/core/configuration.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: permission/trust controls are legitimate authority boundaries, not identity/ultimate-policy governance.

### Absence scope

- Surfaces inspected: permission rules, project trust, primary-agent/system-prompt configuration, containment, provider/model selection, plugin/MCP trust and session/RPC/ACP authority.
- Plausible first-party paths checked: autonomous constitution revision, identity dispute escalation, agent-authored ultimate policy and authoritative policy return into operating rules.
- Why no material first-party path remains: all observed controls are execution/configuration/security boundaries rather than an S5 governance loop.

## Distributed OSS parent arrangement

The assessed organization is the running AVA coding organization, not the GitHub maintainer project. Engineering review/release/governance artifacts are not imported as runtime S3*/S4/S5 ownership.

## Self-hosted and non-human modes

AVA supports hosted/custom providers, TUI, print, RPC and ACP modes. The S1/S3 claims are first-party runtime claims and do not depend on a specific provider or human parent.

## Recursion

The declared viable-unit candidate is the parent coding agent plus instantiated child operational sessions. Parent/general agents provide S1; the parent model owns S3 live job control. Runtime/session/job registries are supporting mechanisms. No standard S2 or S3* function is inferred from plurality/configurability alone.

## Variety and escalation

Engineering variety remains with S1. Delegated children absorb bounded work and report completion. Current child-job exceptions can return to the parent for selective steer/cancel under S3. Concurrency caps, permissions, persistence and configurable agents support execution without establishing S2/S3*/S4/S5.

## Evidence gaps

No ? state is required. Frozen source and canonical subagent documentation directly expose the job-control loop and built-in agent boundary, while inspected coordination/reviewer/persistence/policy surfaces are broad enough for the bounded negative conclusions.
