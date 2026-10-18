---
harness_id: shelley
project_name: Shelley
repository: https://github.com/boldsoftware/shelley
review_ref: 3fa4e71b10469495800c33843b9ff162735320f2
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Shelley

## Review boundary

- System in focus: the first-party Shelley coding runtime at frozen revision 3fa4e71b10469495800c33843b9ff162735320f2, including its Go conversation/agent loop, coding tools, persisted conversation/message state, model/provider integration, writable subagent conversations, queued/asynchronous completion delivery, browser/shell/patch tools, and supported web/headless interaction surfaces.
- Purpose and identity: provide a single-user coding agent that can inspect, edit and execute within a working directory, persist conversations and delegate focused work to independent child conversations whose results return to the parent.
- Relevant environment: user goals and cancellation, repository/workspace files, shell/process/tool results, provider/model responses, persisted SQLite conversation state, asynchronous subagent completion, skills/integrations, and external browser/network services.
- Standard-distribution boundary: shipped Shelley server, loop, claudetool toolset, database/conversation manager, subagent runner and UI/API surfaces. External model providers, exe.dev Reflection integrations, MCP-like external services, operating-system programs and the user's repository are dependencies and cannot donate VSM ownership.
- Credited operating / distribution surfaces: loop/, claudetool/, server/convo.go, server/subagent.go, server/system_prompt.go and subagent system prompt, db conversation/message persistence, supported web/UI/API execution and built-in tools.
- Adjacent first-party surfaces excluded from ownership: CI/release machinery, tests, development-only harnesses, Sketch provenance, external exe.dev Reflection integrations, and repository-maintainer workflows.
- First-party operating / deployment modes considered: normal top-level coding conversations; synchronous and asynchronous task delegation through the subagent tool; persisted/resumed conversations; web UI/API cancellation; supported model/provider and tool configurations.
- Recursion level: one Shelley coding conversation together with any delegated child coding conversations it creates. The top-level model-backed coding loop is the primary S1; write-capable subagent conversations can also own bounded operational outcomes when instantiated.
- Reviewed revision: 3fa4e71b10469495800c33843b9ff162735320f2.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Shelley is a Go-based coding-agent server backed by SQLite. Each ConversationManager owns a model/tool loop, persistent messages, current working directory and toolset. The standard ToolSet exposes bash/shell, patch, change-directory and related coding tools. The runtime records conversation state and can reconstruct/resume it after interruption.

The subagent tool creates or reuses child conversations under the same parent and working-directory lineage. Subagents are independent model conversations and receive the ordinary coding toolset, including write-capable shell/patch tools. Calls may wait synchronously or return immediately; a background child can continue working and its completion is later injected into the parent conversation. The tool description also exposes a query that lists delegated subagents with working state and latest reply, so the parent can observe delegated progress and send later follow-up prompts.

Those capabilities establish delegation but not, by themselves, S2 or S3. The frozen source does not show a first-party file-lease/worktree/merge/conflict-control relation among concurrently write-capable child S1s. Likewise, sending a new message to a busy child queues it until the child's current turn finishes instead of interrupting or reallocating that live commitment. Cancelling the parent deterministically tears down active managed children, but the active Methodology does not treat a generic stop/emergency-cancel path as whole-system S3 current control.

## Operational model

The model-backed conversation loop owns open-ended coding decisions. A parent agent may choose to delegate bounded work to a fresh child model, wait or continue in parallel, observe child status and incorporate the returned result. Runtime queues, locks local to one subagent slug, persistence, cancellation and completion delivery are enforcement/transport mechanisms.

Multiple child agents can operate in the same workspace and can edit files, but no standard first-party interaction loop was found that detects/attenuates their cross-agent file interference and returns a coordination decision into later peer behavior. A child completion is returned to the parent as operational evidence; it does not create a separate whole-current controller or independent audit role.

## S1 — Operations

- State: A
- Function: autonomously perform software-engineering work through model-selected repository, shell, patch, browser and related tool actions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, process/test outcomes, tool failures, provider/model variation, persisted conversation state and bounded delegated tasks.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret results, decide whether to delegate focused work and decide when the coding response is complete.
- Decision owner: the active model-backed Shelley coding agent; delegated child conversations own their bounded coding decisions while executing assigned work.
- Supporting / enforcement mechanisms: loop execution, ToolSet, SQLite message persistence, queued-message machinery, provider adapters, tool dispatch, cancellation and subagent completion delivery.
- Closure path: user request → model selects coding/tool action or child task → first-party runtime executes and returns evidence → model revises the implementation or delegates further work → final response closes the turn.
- Boundary reachability: the shipped server constructs ConversationManager + loop + ToolSet for normal conversations and constructs equivalent managed child conversations for subagent work.
- Why this is / is not agent-owned: runtime code executes and records decisions, but removing the model removes the open-ended choice of implementation, investigation, delegation and completion.
- Evidence: [README.md](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/README.md); [loop/README.md](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/loop/README.md); [claudetool/toolset.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/claudetool/toolset.go); [server/convo.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/server/convo.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: sensitive execution may remain subject to external/operator constraints, but those constraints do not supply the substantive coding choice.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination loop is established for concurrently active coding conversations.
- Disturbance / variety regulated: concurrent child conversations can share a working directory and write files, but the reviewed standard runtime does not place that cross-agent interference under a distinct S2 attenuation/feedback path.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: per-slug call serialization, queued child prompts, parent/child completion queues and conversation persistence prevent duplicate conversational delivery but do not coordinate peer file ownership or coding conflicts.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: the parent may decide to spawn several children, but delegation and message serialization do not constitute a function-specific coordination loop over peer operational interference.
- Evidence: [claudetool/subagent.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/claudetool/subagent.go); [claudetool/toolset.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/claudetool/toolset.go); [server/subagent.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/server/subagent.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: child agents are capable of concurrent write work; that makes interference plausible, not positively coordinated.

### Absence scope

- Surfaces inspected: child creation/reuse, subagent tool schema, ToolSet write capabilities, parent/child completion queues, subagent runner, cancellation tree and persisted conversation state.
- Plausible first-party paths checked: file/path leases, worktree isolation, conflict detector, shared mutation arbiter, scheduler feedback, parent-provided peer constraints and merge/integration controller.
- Why no material first-party path remains: the located synchronization protects message/conversation delivery or one child slug, not a concrete peer-S1 coding interference relation.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established at the declared coding-organization boundary.
- Disturbance / variety regulated: child status and completion are observable, but no actor in the standard runtime is shown owning a substantive live allocation/intervention loop over the whole current set of operational commitments.
- Decisive decision or feedback right: none established for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: child working-state query, asynchronous completion injection, queued follow-up messages, parent cancellation cascading to managed children and ordinary conversation cancel endpoints.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: a busy child cannot be live redirected through the subagent tool; new prompts queue until the current turn ends. Generic parent cancellation tears down delegated work but is an emergency/termination mechanism rather than evidenced whole-system resource/commitment control.
- Evidence: [claudetool/subagent.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/claudetool/subagent.go); [server/subagent.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/server/subagent.go); [server/convo.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/server/convo.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: the parent agent does receive child results and can create/reuse children, but task delegation/status is insufficient without a whole-current decision right and returned control loop.

### Absence scope

- Surfaces inspected: parent dynamic subagent listing, synchronous/asynchronous result delivery, busy-child follow-up behavior, cancellation tree, API/UI conversation cancellation and queued-message machinery.
- Plausible first-party paths checked: model-owned current worker allocation, selective live interruption/reprioritization, parent dashboard current-control mode, budget/resource reallocation and retry/kill/restart decisions over the whole worker set.
- Why no material first-party path remains: observed control is spawn/status/queue/stop enforcement; no substantive whole-current decision loop is reconstructed.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is established.
- Disturbance / variety regulated: no first-party reviewer is assigned a distinct claim, independent operational evidence path and corrective return loop.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: ordinary task subagents, tool evidence, tests run by the same coding loop, distillation and external exe.dev Reflection integrations can support operation but do not establish first-party S3*.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: generic subagents can be prompted to review, but no shipped independent reviewer constructor or mandatory fresh evidence path with a returned audit verdict is established. The repository's Reflection integration code is an external integration surface rather than a first-party coding audit owner.
- Evidence: [claudetool/subagent.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/claudetool/subagent.go); [server/reflection.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/server/reflection.go); [server/subagent_system_prompt.txt](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/server/subagent_system_prompt.txt).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user-constructed review delegation is generic S1 composition and is not promoted to S3* without the function-specific independence/feedback witness.

### Absence scope

- Surfaces inspected: subagent prompts/tools, normal tool/test paths, Reflection integration, distillation, conversation forks and persisted messages.
- Plausible first-party paths checked: dedicated reviewer/verifier role, authorship-independent second pass, fresh repository audit worker, external audit callback and automatic corrective gate.
- Why no material first-party path remains: no standard first-party path supplies both independent operational access and an audit judgment returned into corrective S1 behavior.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no future/external distinction is transformed by an adaptation owner into options that change later organizational capability.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent conversations, previous-conversation skill, distillation, model switching, skills and integration discovery preserve context or current capability but are not sufficient S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: persistence and summarization retain information; they do not demonstrate an outside-and-then option-development loop returning into current capability.
- Evidence: [server/distill.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/server/distill.go); [skills/builtin/previous-conversations/SKILL.md](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/skills/builtin/previous-conversations/SKILL.md); [server/convo.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/server/convo.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: retained history can influence future turns, but memory/context reuse alone does not satisfy S4.

### Absence scope

- Surfaces inspected: persistent conversations/messages, distillation, previous-conversation retrieval, model/integration configuration, skills and subagent reuse.
- Plausible first-party paths checked: future environment sensing, learned strategy/policy update, autonomous capability reconfiguration and durable option-generation feedback.
- Why no material first-party path remains: inspected paths store/retrieve/summarize current or past context rather than close an external-and-prospective adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level or ultimate-policy issue is routed to an authoritative owner and returned as governing runtime policy.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: system prompts, tool configuration, deployment authentication/sandbox choices, conversation options and model selection constrain operation but do not create S5 closure.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: Shelley agents operate within configured/developer-authored rules and have no authority to redefine Shelley's identity or ultimate operating principles.
- Evidence: [server/system_prompt.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/server/system_prompt.go); [claudetool/toolset.go](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/claudetool/toolset.go); [README.md](https://github.com/boldsoftware/shelley/blob/3fa4e71b10469495800c33843b9ff162735320f2/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: deployment operators control ordinary configuration and security boundaries, but no function-specific identity/ultimate-policy return loop is established.

### Absence scope

- Surfaces inspected: prompts, tool configuration, deployment/authentication notes, conversation options, provider/model controls, cancellation and external integrations.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity governance, runtime policy-authoring actor and authoritative policy feedback.
- Why no material first-party path remains: identified controls are operating configuration or execution constraints rather than an S5 governance loop.

## Distributed OSS parent arrangement

The assessed organization is the running Shelley coding organization, not its GitHub maintainer project. Repository contribution/release governance is not imported as runtime parent ownership.

## Self-hosted and non-human modes

Shelley is self-hostable and can use multiple providers. The positive S1 claim is provider-independent. No qualifying first-party parent-governed S3/S4/S5 mode is established from generic operator configuration or cancellation alone.

## Recursion

One top-level coding conversation plus its managed child coding conversations is the declared viable-unit candidate. Parent and child model loops are S1 operational units when they own coding outcomes. Conversation queues, persistence and cancellation are support mechanisms rather than additional VSM functions.

## Variety and escalation

Ordinary coding variety remains in S1. Delegated children can absorb bounded work and report completion asynchronously. Queueing, persistence, cancellation and distillation regulate execution mechanics but, at the frozen boundary, do not establish S2/S3/S3*/S4/S5 ownership.

## Evidence gaps

No ? state is required. The frozen runtime exposes the child toolset, parent/child delivery behavior, cancellation, persistence and integration boundaries sufficiently to support the positive S1 and bounded negative conclusions for the remaining functions.
