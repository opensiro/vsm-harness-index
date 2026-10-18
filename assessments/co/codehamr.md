---
harness_id: codehamr
project_name: codehamr
repository: https://github.com/plaxtoris/codehamr
review_ref: 24482811592f44c4e3b7e28561b8faa74cb3f1b1
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

# codehamr

## Review boundary

- System in focus: the first-party codehamr terminal coding-agent runtime at frozen revision 24482811592f44c4e3b7e28561b8faa74cb3f1b1, including its Go model/tool loop, four built-in coding tools, conversation/context state, verification/recovery nudges, prompt queue, provider client and TUI cancellation/configuration paths.
- Purpose and identity: a small local-first coding agent that reads a project, makes changes, runs checks and reports completion through one model-backed conversation loop.
- Relevant environment: user requests, repository files, shell/process/test results, provider/model responses, context-window pressure, queued follow-up prompts, cancellation and local configuration.
- Standard-distribution boundary: shipped codehamr binary and repository-owned prompt/runtime/tool/TUI/config modules. External model servers/providers, the host shell/toolchain, GitHub update service and the user's repository are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: cmd/codehamr, internal/tui, internal/llm, internal/ctx, internal/tools and embedded internal/config/PROMPT_SYS.md.
- Adjacent first-party surfaces excluded from ownership: CI/release/update infrastructure, tests, demo/media recording, optional real-provider integration tests and repository maintainer workflows.
- First-party operating / deployment modes considered: ordinary interactive terminal coding, supported model profiles, queued next-turn prompts, local history/logging and cancellation.
- Recursion level: one codehamr coding conversation. No separate standard operational agent unit is instantiated inside the frozen distribution.
- Reviewed revision: 24482811592f44c4e3b7e28561b8faa74cb3f1b1.
- Observation date: 2026-10-06.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

codehamr builds a single TUI model around one streaming LLM client and four coding tools: bash, read_file, write_file and edit_file. Conversation history is retained in memory and packed newest-first under a context budget, preserving complete tool-call/result groups and an original user anchor. The TUI supports one queued follow-up while a turn runs, cancellation with Ctrl+C, provider/profile switching and local prompt history.

The runtime adds deterministic safeguards for runaway/failure patterns and a finish re-grounding nudge after substantial modifying work. That nudge asks the same coding agent to verify what it claims before final completion. It is not a separate reviewer, evidence channel or organizational owner.

## Operational model

The active model chooses repository inspections, edits, shell commands, verification actions and final completion. Runtime code executes those choices, bounds context/tool output, preserves message shape and may inject deterministic corrective instructions when a turn appears stuck or under-verified.

There is no bundled delegation/subagent subsystem. A queued prompt is user input for the next turn, not another operational unit. Provider/model profiles change which model executes the same single-agent organization.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify a software project in response to a user coding objective.
- Disturbance / variety regulated: unfamiliar repository state, implementation decisions, build/test/tool failures, context-window pressure and provider/model behavior.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret evidence, decide repairs and decide when the requested work is complete.
- Decision owner: the active model-backed codehamr agent.
- Supporting / enforcement mechanisms: bash/read/write/edit tools, streaming Responses API client, context packing/truncation, queued follow-ups, cancellation, retry/backstop nudges and local configuration.
- Closure path: user request → model selects tool/coding actions → first-party runtime executes and returns results → model revises/validates work → model emits final response.
- Boundary reachability: the shipped terminal program directly instantiates the LLM client, conversation state and built-in tools for ordinary operation.
- Why this is / is not agent-owned: deterministic code constrains and transports the work, but the model owns the open-ended engineering choices and interpretation.
- Evidence: [README.md](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/README.md); [internal/tui/model.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/tui/model.go); [internal/llm/llm.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/llm/llm.go); [internal/config/PROMPT_SYS.md](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/config/PROMPT_SYS.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the agent runs with the user's OS permissions; codehamr itself does not supply a sandbox, but external permission scope does not remove autonomous S1 decision ownership.

## S2 — Coordination

- State: —
- Function: no material inter-S1 coordination function is established.
- Disturbance / variety regulated: none at the declared recursion because the standard runtime does not instantiate distinct concurrent operational agent units whose interference must be attenuated.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: prompt queueing and context/tool sequencing serialize one conversation but do not coordinate peer S1 units.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: there is no distinct-S1 coordination function to own.
- Evidence: [README.md](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/README.md); [internal/tui/queue_test.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/tui/queue_test.go); [internal/tui/model.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/tui/model.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: batching multiple tool calls in one model turn is intra-S1 execution, not inter-S1 coordination.

### Absence scope

- Surfaces inspected: runtime/TUI loop, tool execution, prompt queue, context packing, model/provider switching and repository tree for subagent/orchestration surfaces.
- Plausible first-party paths checked: subagents, parallel workers, worktrees, peer scheduling, file ownership/conflict arbitration and multi-agent message routing.
- Why no material first-party path remains: no distinct operational agent units or S2-specific interference/attenuation loop are supplied by the frozen distribution.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established beyond the single operational loop.
- Disturbance / variety regulated: no portfolio of current S1 commitments/resources exists under a separate current-control owner.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Ctrl+C cancellation, turn/round limits, failure/runaway nudges and queued next-turn input enforce or alter one S1 conversation only.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the same S1 agent manages its own coding work; deterministic stop/nudge mechanisms do not create a separate whole-system current-control function.
- Evidence: [internal/tui/model.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/tui/model.go); [internal/tui/queue_test.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/tui/queue_test.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: an operator may cancel a turn, but generic emergency stop/local correction is not sufficient S3 under Methodology 0.3.6.

### Absence scope

- Surfaces inspected: active-turn state, queue/cancel behavior, round/tool counters, recovery/backstop nudges, provider/model activation and slash-command controls.
- Plausible first-party paths checked: whole-current dashboard, commitment/resource prioritization, live worker intervention, model-owned supervisor and parent-governed current-control loop.
- Why no material first-party path remains: all identified controls operate inside one S1 turn or terminate it; no separate whole-system current-control loop is present.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is established.
- Disturbance / variety regulated: no independently accessed claim/evidence path challenges an operational result before correction/acceptance.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: the embedded prompt asks the same agent to verify work and a deterministic re-grounding nudge may reprompt that same conversation before finishing.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: self-verification by the author agent is part of S1; no separate reviewer, fresh context or complementary evidence channel is instantiated.
- Evidence: [README.md](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/README.md); [internal/config/PROMPT_SYS.md](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/config/PROMPT_SYS.md); [internal/tui/model.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/tui/model.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: tests/commands provide operational evidence to S1, not independent audit ownership.

### Absence scope

- Surfaces inspected: system prompt, finish verification nudge, failure/runaway nudges, tests/tool execution and repository tree for review/verifier components.
- Plausible first-party paths checked: fresh-context reviewer, independent test/eval agent, second-model critique, separate evidence access and audit verdict gate.
- Why no material first-party path remains: every verification/re-grounding path returns to the same author conversation without an independent audit owner.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no outside/future condition is transformed into adaptation options that update current capability.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: local prompt history, context packing, provider/model configuration and automatic binary update checks preserve/use state or software currency but do not close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: remembered prompts and model/profile changes are user/configuration inputs, not an autonomous prospective adaptation function.
- Evidence: [README.md](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/README.md); [internal/ctx/ctx.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/ctx/ctx.go); [cmd/codehamr/main.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/cmd/codehamr/main.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: automatic software updating is deployment maintenance, not an agent-owned outside-and-then intelligence loop.

### Absence scope

- Surfaces inspected: history persistence, context management, model profiles, updater, prompts and TUI state.
- Plausible first-party paths checked: durable learned strategy, environment scanning, autonomous capability/model/tool reconfiguration and future-oriented option development.
- Why no material first-party path remains: inspected mechanisms preserve context or apply externally selected software/configuration changes rather than close S4.

## S5 — Policy and identity

- State: —
- Function: no material identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level policy issue is routed to an authoritative owner and returned as runtime governing policy.
- Decisive decision or feedback right: none established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: embedded system prompt, model/provider config, context limits and OS/user permissions constrain execution but do not create S5 closure.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent follows compiled/configured policy and cannot authoritatively redefine codehamr's identity or ultimate operating principles.
- Evidence: [internal/config/PROMPT_SYS.md](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/config/PROMPT_SYS.md); [README.md](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/README.md); [internal/config/config.go](https://github.com/plaxtoris/codehamr/blob/24482811592f44c4e3b7e28561b8faa74cb3f1b1/internal/config/config.go).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user configuration and local permissions are legitimate operating constraints, not identity governance.

### Absence scope

- Surfaces inspected: embedded prompt, config profiles, slash commands, provider settings, update mechanism and OS-permission notes.
- Plausible first-party paths checked: autonomous constitution/policy revision, parent identity governance, agent-authored permission policy and authoritative runtime policy feedback.
- Why no material first-party path remains: all observed policy surfaces are static or externally configured operating constraints.

## Distributed OSS parent arrangement

The assessed system is the running codehamr coding agent, not the GitHub maintainer project. Maintainer/release governance is outside runtime ownership.

## Self-hosted and non-human modes

codehamr is local-first and may connect to local or hosted model services. The S1 claim is provider-neutral. No qualifying first-party parent-governed S3/S4/S5 mode is established by generic operator cancellation/configuration.

## Recursion

The declared recursion contains one operational coding agent. Tool calls, queues, context-management routines and verification nudges are components of that S1 rather than additional viable operational units.

## Variety and escalation

S1 absorbs coding variety and ordinary verification. Deterministic context, runaway/failure and finish re-grounding mechanisms bound execution and encourage truthful verification but do not establish S2/S3/S3*/S4/S5.

## Evidence gaps

No ? state is required. The frozen repository is compact and exposes the complete first-party runtime, tools, prompt, context, queue/cancel and configuration surfaces needed for the bounded negative conclusions.
