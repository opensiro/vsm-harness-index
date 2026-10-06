---
harness_id: termide
project_name: TermIDE
repository: https://github.com/termide/termide
review_ref: 351a551ad234ea5071a8a4fe226e172dcb5d76ee
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

# TermIDE

## Review boundary

- System in focus: the first-party built-in TermIDE coding-agent runtime at frozen revision 351a551ad234ea5071a8a4fe226e172dcb5d76ee, including the Rust model/tool loop, coding/web tools, permissions, sessions/checkpoints, plan/goal/handoff commands, task-delegation constructor, MCP integration and built-in interactive/headless execution.
- Purpose and identity: execute software-engineering work through a model-backed coding loop and, in the shipped /goal mode, autonomously continue the active goal until a separate model judge concludes that completion is evidenced.
- Relevant environment: user requests and steering, repository state, shell/tool results, model/provider responses, permissions, context pressure, persisted session state, optional user-defined agent definitions, MCP services and external ACP agents.
- Standard-distribution boundary: shipped TermIDE crates and bundled system prompts. External models, MCP servers, external ACP agents and user-authored custom agents are dependencies/extensions and cannot donate uninstantiated organizational functions.
- Credited operating / distribution surfaces: crates/agent-core, crates/agent-tools, crates/panel-agent, bundled system prompts, first-party permission/session/checkpoint machinery and built-in interactive/headless modes.
- Adjacent first-party surfaces excluded from ownership: non-agent editor/file-manager/LSP operation, CI/tests/development-only artifacts, external ACP agent runtimes and user/project custom agent definitions not shipped as instantiated agents at the frozen revision.
- First-party operating / deployment modes considered: ordinary built-in coding sessions; plan mode; /goal autonomous goal mode; /loop; built-in headless execution; task delegation only when custom definitions are supplied; ACP compatibility without importing the external agent as TermIDE-owned.
- Recursion level: one built-in TermIDE coding session. The built-in coding loop is the established S1; no additional first-party standard-distribution S1 unit is instantiated by default.
- Reviewed revision: 351a551ad234ea5071a8a4fe226e172dcb5d76ee.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

TermIDE ships a provider-agnostic Agent that owns a single-threaded transcript/tool loop. The model can read, edit, write, run commands, use web/MCP tools where configured, receive steering/follow-up messages, compact context, pause/resume and persist sessions/checkpoints. Permission hooks and plan mode constrain execution but do not choose engineering actions.

A generic task tool can run another named custom agent with a fresh context and return its final report, but the frozen repository ships no custom agents/<name> definitions. Its design also states parallel delegation is not implemented and the loop runs one tool at a time. The constructor therefore does not establish a standard-distribution multi-S1 topology by itself.

The shipped /goal mode does establish a separate current-control loop. After each completed work turn, TermIDE invokes a separate read-only model call on a copy of the complete current transcript with the bundled goal-judge prompt. That model returns DONE or CONTINUE. CONTINUE is turned into a new work prompt describing the most important missing item and starts another operational turn; DONE terminates the goal task.

## Operational model

The main coding model owns open-ended implementation and investigation choices. Runtime code transports tool calls, enforces permissions/modes and preserves state. In /goal mode, a separate model judge owns the substantive current commitment decision: terminate the active goal or continue with another operational turn.

The judge is not credited as S3*: it receives the ordinary transcript from the same operational path and has no materially different repository, replay or ground-truth access.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify a software project through model-selected coding and tool actions.
- Disturbance / variety regulated: unfamiliar repository state, implementation choices, tool/test failures, provider variation, permission refusal, context pressure and user steering.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret evidence and choose the next engineering step.
- Decision owner: the active built-in model-backed TermIDE Agent.
- Supporting / enforcement mechanisms: tool registry, provider adapters, permissions, plan guard, queues, compaction, sessions/checkpoints, MCP/web transport and cancellation.
- Closure path: user/current goal → model selects action → runtime executes and returns evidence → model revises work or completes the turn.
- Boundary reachability: ordinary built-in TermIDE agent panels and built-in headless execution instantiate this loop without requiring a custom external agent.
- Why this is / is not agent-owned: deterministic machinery constrains and transports action; the model owns the open-ended engineering choice.
- Evidence: [agent.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-core/src/agent.rs); [agent tools](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-tools/src/lib.rs); [README](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external ACP agents are separate systems and are not used for this claim.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established in the frozen standard distribution.
- Disturbance / variety regulated: no concrete concurrent peer-S1 interference is placed under a first-party attenuation loop.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: generic task delegation, sequential tool execution, permissions and message queues route or constrain work but do not coordinate distinct simultaneously active first-party S1 units.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: task delegation requires user-supplied custom agents, and the frozen design says parallel delegation is not implemented.
- Evidence: [task.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-tools/src/task.rs); [agent design](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/doc/en/agent-design.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: generic extensibility is not credited as an already closed S2 function.

### Absence scope

- Surfaces inspected: task tool, custom-agent catalog path, built-in loop, permissions, queues, panel runtime and repository tree for bundled agent definitions.
- Plausible first-party paths checked: parallel subagents, peer work queues, worktree/file leases, shared-resource arbitration, conflict detection and cross-agent feedback.
- Why no material first-party path remains: no standard first-party set of concurrent operational agents plus interference-specific attenuation loop is instantiated.

## S3 — Inside-and-now control

- State: A
- Function: regulate the active autonomous goal commitment by deciding, from a whole-session current view, whether work is complete or must continue.
- Disturbance / variety regulated: premature completion, incomplete evidence, remaining failed/missing work and mismatch between the user-stated goal and current operational evidence.
- Decisive decision or feedback right: issue DONE to release the current goal commitment or CONTINUE with the most important missing item, causing another work turn.
- Decision owner: the separate model-backed goal judge invoked by first-party /goal mode.
- Supporting / enforcement mechanisms: transcript cloning, bundled goal prompt, verdict parser, iteration cap/scheduling and panel event routing.
- Closure path: operational turn finishes → judge receives the full current transcript plus goal → judge returns DONE or CONTINUE → DONE ends the goal; CONTINUE becomes the next work prompt → subsequent current operation changes.
- Boundary reachability: /goal is a shipped built-in command and uses the built-in Agent.judge path plus bundled goal prompt.
- Why this is / is not agent-owned: deterministic code schedules and parses the verdict; the model judge makes the substantive completion/continuation judgment.
- Whole-system current view: the judge receives a copy of the complete current built-in-agent transcript for the active goal, including prior user turns, assistant messages and tool results.
- Current-control decision scope: whether the current whole-session goal commitment terminates or remains active for another operational turn, including the missing item returned to that turn.
- Evidence: [agent.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-core/src/agent.rs); [goal prompt](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-core/assets/system/goal.md); [submit.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/panel-agent/src/submit.rs); [agent docs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/doc/en/agent.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic user pause/stop is not used for this state; the claim rests on the autonomous /goal completion/continuation loop.

## S3* — Complementary audit

- State: —
- Function: no material complementary audit function with independent access to operational reality is established.
- Disturbance / variety regulated: the goal judge checks completion but receives the ordinary session transcript rather than a materially different evidence path.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: none established.
- Supporting / enforcement mechanisms: /goal judgment, plan mode, checkpoints and ordinary verification evidence can improve confidence but do not create complementary independence.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: the goal judge is a separate model call but audits only the normal transcript; richer reviewer agents require user-supplied custom definitions.
- Evidence: [agent.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-core/src/agent.rs); [goal prompt](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-core/assets/system/goal.md); [task.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-tools/src/task.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: an extension can define a reviewer, but an uninstantiated extension point is not a standard first-party audit loop.

### Absence scope

- Surfaces inspected: goal judge, task/custom-agent constructor, plan mode, checkpoints, built-in tools, transcript and bundled agent-definition tree.
- Plausible first-party paths checked: fresh reviewer with direct repository access, replay, independent tests/eval agent, external ground truth and authorship-independent audit gate.
- Why no material first-party path remains: the shipped judge is transcript-only and richer reviewer roles are extension-supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no external/future distinction is transformed into adaptation options and returned into current organizational capability.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: web tools, MCP, session history, compaction, handoff briefs, skills and model/tool configuration provide information or continuity but do not close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: web research within a current task and forward-looking handoff text are operational/context mechanisms, not a durable prospective adaptation conversation with S3.
- Evidence: [handoff.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-core/src/handoff.rs); [web tools](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-web/src/tools.rs); [toolset.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/panel-agent/src/toolset.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: future custom agents/skills could implement adaptation, but that is outside this frozen standard-distribution closure.

### Absence scope

- Surfaces inspected: web/MCP tools, handoff, compaction, sessions, skills, model/tool switching, /loop and /goal.
- Plausible first-party paths checked: environment sensing with future-option generation, durable learned strategy, autonomous capability reconfiguration and S4-to-S3 return.
- Why no material first-party path remains: inspected paths support current work, continuity or externally configured capability, not a closed prospective adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level or ultimate-policy issue is routed to a legitimate authoritative owner and returned as governing runtime policy.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes/rules, system prompts, toolset switches, plan mode and user configuration constrain operation but do not create S5 closure.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: coding and goal-judge agents operate inside developer/user-authored rules and cannot redefine TermIDE's identity or ultimate policy.
- Evidence: [permissions.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-core/src/permissions.rs); [toolset.rs](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/panel-agent/src/toolset.rs); [plan prompt](https://github.com/termide/termide/blob/351a551ad234ea5071a8a4fe226e172dcb5d76ee/crates/agent-core/assets/system/plan.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: operator permissions/configuration are ordinary operating constraints rather than identity governance.

### Absence scope

- Surfaces inspected: permissions, plan mode, system prompts, toolset controls, model/provider selection, sessions/checkpoints and built-in commands.
- Plausible first-party paths checked: runtime constitution revision, identity-policy escalation, authoritative policy actor and return-to-operation governance.
- Why no material first-party path remains: identified mechanisms configure or constrain ordinary execution; none closes an identity/ultimate-policy decision loop.

## Distributed OSS parent arrangement

The assessed organization is the running built-in TermIDE coding session, not the TermIDE maintainer project. Repository contribution/release governance and external ACP agent governance are outside runtime ownership.

## Self-hosted and non-human modes

TermIDE supports local model endpoints and built-in headless execution. The positive S1 and S3 claims are first-party and provider-neutral. Generic operator pause/cancel/configuration is not used to manufacture parent-mode notation.

## Recursion

At the frozen standard boundary the built-in coding loop is the established operational S1. The generic task tool can instantiate user-defined agents, but the repository ships no such definitions and no parallel delegation topology, so higher functions are not inferred from the extension constructor.

## Variety and escalation

S1 absorbs ordinary engineering/tool variety. /goal adds a separate current-control judgment over whether the active goal commitment is complete or requires another operational turn. Permissions, plan, pause, checkpoint, compaction and handoff mechanisms bound or preserve work without establishing S2/S3*/S4/S5.

## Evidence gaps

No ? state is required. The frozen repository directly establishes the built-in coding loop and goal-judge closure, and its task/custom-agent, audit, adaptation and policy surfaces are broad enough to support the bounded negative conclusions.
