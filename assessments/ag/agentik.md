---
harness_id: agentik
project_name: Agentik
repository: https://github.com/jaredpalmer/agentik
review_ref: 5a57da25d2c58ff9b783e51fce8879563f26f7aa
reviewed_at: 2026-10-30
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

# Agentik

## Review boundary

- System in focus: the first-party Agentik runtime and included coding-agent CLI operating one model-directed task session.
- Purpose and identity: execute coding tasks through iterative model decisions and local file/shell/web tools, with optional nested agents.
- Relevant environment: user tasks, local repository/files/processes, model-provider responses, tool failures, steering input and context limits.
- Standard-distribution boundary: packages/runtime plus packages/coding-agent; provider SDK is inference support, not a donor of additional organizational functions.
- Credited operating / distribution surfaces: agent.ts, agent-loop.ts, built-in tools, hooks, subagents, session-store/manager, compaction helpers and cli.ts instantiated model/tools.
- Adjacent first-party surfaces excluded from ownership: examples, tests, project CI/development and suggested downstream reviewer/CI assistants; these do not supply runtime audit/governance owners.
- First-party operating / deployment modes considered: included interactive and print CLI; reusable Agent runtime; optional configured subagents, hooks, queues and recording. RPC explicitly throws as unimplemented.
- Recursion level: one coding session and its optional nested task cells; nested loops are not proof of complete VSM recursion.
- Reviewed revision: `jaredpalmer/agentik@5a57da25d2c58ff9b783e51fce8879563f26f7aa`, frozen intake #2412 / controller #2413.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[packages/coding-agent/src/cli.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/coding-agent/src/cli.ts) instantiates an Agent with built-in file/edit/search/bash/web tools and optional configured subagent tools. [packages/runtime/src/agent-loop.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/agent-loop.ts) streams model output, executes selected tools, appends results to model context and continues; maxSteps, abort and stop/follow-up logic bound the session. [packages/runtime/src/agent.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/agent.ts) maintains messages and steering/follow-up queues. [packages/runtime/src/subagents.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/subagents.ts) creates nested model/tool loops from registered definitions. [packages/runtime/src/hooks.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/hooks.ts) exposes developer callbacks for tool permissions, failure, stop and lifecycle. Session recording stores a branching history; compaction is a callback-based context transformation, not automatically organizational adaptation.

## Operational model

The included CLI is a complete first-party S1 composition: the model chooses operational actions and receives actual tool results. Optional subagents execute their own local tasks but neither their presence nor shared-memory plumbing establishes an additional metasystem function. User steering and developer hooks retain their actual local scope; no whole-fleet parent authority is inferred.

## S1 — Operations

- State: A
- Function: produce coding-task outcomes by inspecting/modifying files and running tools.
- Disturbance / variety regulated: unknown repository contents, tool errors, intermediate results and changing user instructions.
- Decisive decision or feedback right: select tool, arguments, next action and completion after observations.
- Decision owner: the model-directed Agent instantiated by the CLI; nested agents own their configured local tasks.
- Supporting / enforcement mechanisms: AI SDK streamText transport, built-in tools, serial execution, event stream, maxSteps and abort signal.
- Closure path: model tool call → first-party tool execution → ToolResultMessage appended → next model turn or final answer.
- Boundary reachability: cli.ts constructs Agent with concrete built-in tools and calls agent.prompt; agent-loop.ts closes the result-return path without downstream loop composition.
- Why this is / is not agent-owned: removing the model leaves a tool registry and state but no semantic action selection.
- Evidence: [packages/coding-agent/src/cli.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/coding-agent/src/cli.ts); [packages/runtime/src/agent-loop.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/agent-loop.ts); [packages/runtime/src/tools/edit.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/tools/edit.ts)
- Basis: structural
- Confidence: high
- Caveats: static source judgment; no live model/task performance claim.

## S2 — Coordination

- State: —
- Function: No specific inter-S1 coordination regulation established.
- Disturbance / variety regulated: Subagent registry/shared-memory storage, sequential tool execution, private child contexts and lifecycle callbacks were checked.
- Decisive decision or feedback right: no qualifying function-specific decisive loop found in the supported distribution.
- Decision owner: developer/user supplies configuration; ordinary task discretion belongs to S1.
- Supporting / enforcement mechanisms: packages/runtime/src/subagents.ts, packages/runtime/src/agent-loop.ts, packages/runtime/src/hooks.ts
- Closure path: The distribution offers delegation/transport and ordinary sequencing, without an identified cross-cell collision/oscillation and a specific attenuation/feedback protocol. Generic fresh contexts and registry uniqueness do not alone establish S2.
- Why this is / is not agent-owned: generic programmable hooks/queues are not an already-established organizational function.
- Evidence: [packages/runtime/src/subagents.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/subagents.ts); [packages/runtime/src/agent-loop.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/agent-loop.ts); [packages/runtime/src/hooks.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/hooks.ts)
- Basis: structural
- Confidence: high
- Caveats: bounded shipped-mode finding; custom downstream code could create a different organization.

### Absence scope

- Surfaces inspected: packages/runtime/src/subagents.ts, packages/runtime/src/agent-loop.ts, packages/runtime/src/hooks.ts, README operating modes and runtime/CLI tests.
- Plausible first-party paths checked: Subagent registry/shared-memory storage, sequential tool execution, private child contexts and lifecycle callbacks were checked.
- Why no material first-party path remains: The distribution offers delegation/transport and ordinary sequencing, without an identified cross-cell collision/oscillation and a specific attenuation/feedback protocol. Generic fresh contexts and registry uniqueness do not alone establish S2.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control loop established.
- Disturbance / variety regulated: maxSteps, thinking budgets, abort/steering, Stop hooks, tool permission callbacks and optional delegation were checked.
- Decisive decision or feedback right: no qualifying function-specific decisive loop found in the supported distribution.
- Decision owner: developer/user supplies configuration; ordinary task discretion belongs to S1.
- Supporting / enforcement mechanisms: packages/runtime/src/agent.ts, packages/runtime/src/agent-loop.ts, packages/runtime/src/hooks.ts, packages/coding-agent/src/cli.ts
- Closure path: Controls bound or steer one session; callbacks must be supplied by consumers and do not expose an evidenced S3-specific whole-system regulator. The CLI wires no aggregate resource/commitment bargaining or complete parent current-control mode.
- Why this is / is not agent-owned: generic programmable hooks/queues are not an already-established organizational function.
- Evidence: [packages/runtime/src/agent.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/agent.ts); [packages/runtime/src/agent-loop.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/agent-loop.ts); [packages/runtime/src/hooks.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/hooks.ts); [packages/coding-agent/src/cli.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/coding-agent/src/cli.ts)
- Basis: structural
- Confidence: high
- Caveats: bounded shipped-mode finding; custom downstream code could create a different organization.

### Absence scope

- Surfaces inspected: packages/runtime/src/agent.ts, packages/runtime/src/agent-loop.ts, packages/runtime/src/hooks.ts, packages/coding-agent/src/cli.ts, README operating modes and runtime/CLI tests.
- Plausible first-party paths checked: maxSteps, thinking budgets, abort/steering, Stop hooks, tool permission callbacks and optional delegation were checked.
- Why no material first-party path remains: Controls bound or steer one session; callbacks must be supplied by consumers and do not expose an evidenced S3-specific whole-system regulator. The CLI wires no aggregate resource/commitment bargaining or complete parent current-control mode.

## S3* — Complementary audit

- State: —
- Function: No complementary audit function established.
- Disturbance / variety regulated: PostToolUse/Failure, session/event logs, optional subagent review and README suggestions for CI/diff review were checked.
- Decisive decision or feedback right: no qualifying function-specific decisive loop found in the supported distribution.
- Decision owner: developer/user supplies configuration; ordinary task discretion belongs to S1.
- Supporting / enforcement mechanisms: packages/runtime/src/hooks.ts, packages/runtime/src/agent-loop.ts, packages/runtime/src/session-store.ts, README.md
- Closure path: These are production callbacks/records or downstream application ideas. No shipped independent auditor obtains materially different operational evidence and returns a finding to control.
- Why this is / is not agent-owned: generic programmable hooks/queues are not an already-established organizational function.
- Evidence: [packages/runtime/src/hooks.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/hooks.ts); [packages/runtime/src/agent-loop.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/agent-loop.ts); [packages/runtime/src/session-store.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/session-store.ts); [README.md](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/README.md)
- Basis: structural
- Confidence: high
- Caveats: bounded shipped-mode finding; custom downstream code could create a different organization.

### Absence scope

- Surfaces inspected: packages/runtime/src/hooks.ts, packages/runtime/src/agent-loop.ts, packages/runtime/src/session-store.ts, README.md, README operating modes and runtime/CLI tests.
- Plausible first-party paths checked: PostToolUse/Failure, session/event logs, optional subagent review and README suggestions for CI/diff review were checked.
- Why no material first-party path remains: These are production callbacks/records or downstream application ideas. No shipped independent auditor obtains materially different operational evidence and returns a finding to control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation loop established.
- Disturbance / variety regulated: Session persistence/compaction, model/provider/resource loading and configurable subagents were checked.
- Decisive decision or feedback right: no qualifying function-specific decisive loop found in the supported distribution.
- Decision owner: developer/user supplies configuration; ordinary task discretion belongs to S1.
- Supporting / enforcement mechanisms: packages/runtime/src/compaction/index.ts, packages/runtime/src/session-manager.ts, packages/runtime/src/resource-loader.ts, packages/runtime/src/model-registry.ts
- Closure path: Context summarization and configured resource/model selection support current tasks. No supported owner models external future distinctions, develops adaptation options and returns them into present capability or an S3 conversation; no parent adaptation mode closes it.
- Why this is / is not agent-owned: generic programmable hooks/queues are not an already-established organizational function.
- Evidence: [packages/runtime/src/compaction/index.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/compaction/index.ts); [packages/runtime/src/session-manager.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/session-manager.ts); [packages/runtime/src/resource-loader.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/resource-loader.ts); [packages/runtime/src/model-registry.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/model-registry.ts)
- Basis: structural
- Confidence: high
- Caveats: bounded shipped-mode finding; custom downstream code could create a different organization.

### Absence scope

- Surfaces inspected: packages/runtime/src/compaction/index.ts, packages/runtime/src/session-manager.ts, packages/runtime/src/resource-loader.ts, packages/runtime/src/model-registry.ts, README operating modes and runtime/CLI tests.
- Plausible first-party paths checked: Session persistence/compaction, model/provider/resource loading and configurable subagents were checked.
- Why no material first-party path remains: Context summarization and configured resource/model selection support current tasks. No supported owner models external future distinctions, develops adaptation options and returns them into present capability or an S3 conversation; no parent adaptation mode closes it.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy runtime closure established.
- Disturbance / variety regulated: Instructions, agent definitions, tool allow/deny/ask, steering and launch/provider configuration were checked.
- Decisive decision or feedback right: no qualifying function-specific decisive loop found in the supported distribution.
- Decision owner: developer/user supplies configuration; ordinary task discretion belongs to S1.
- Supporting / enforcement mechanisms: packages/runtime/src/config.ts, packages/runtime/src/hooks.ts, packages/runtime/src/agent-definition.ts, packages/coding-agent/src/cli.ts
- Closure path: These constrain or guide ordinary task execution. No identity-level issue reaches legitimate ultimate authority and returns as authoritative governance over subsequent operation; generic approval is not S5.
- Why this is / is not agent-owned: generic programmable hooks/queues are not an already-established organizational function.
- Evidence: [packages/runtime/src/config.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/config.ts); [packages/runtime/src/hooks.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/hooks.ts); [packages/runtime/src/agent-definition.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/runtime/src/agent-definition.ts); [packages/coding-agent/src/cli.ts](https://github.com/jaredpalmer/agentik/blob/5a57da25d2c58ff9b783e51fce8879563f26f7aa/packages/coding-agent/src/cli.ts)
- Basis: structural
- Confidence: high
- Caveats: bounded shipped-mode finding; custom downstream code could create a different organization.

### Absence scope

- Surfaces inspected: packages/runtime/src/config.ts, packages/runtime/src/hooks.ts, packages/runtime/src/agent-definition.ts, packages/coding-agent/src/cli.ts, README operating modes and runtime/CLI tests.
- Plausible first-party paths checked: Instructions, agent definitions, tool allow/deny/ask, steering and launch/provider configuration were checked.
- Why no material first-party path remains: These constrain or guide ordinary task execution. No identity-level issue reaches legitimate ultimate authority and returns as authoritative governance over subsequent operation; generic approval is not S5.

## Distributed OSS parent arrangement

Maintainer/contributor governance is outside the running coding-session boundary. Multiple users of a runtime do not establish project-level parent modes.

## Self-hosted and non-human modes

The included CLI closes autonomous S1 after setup. Public hooks/queues are mechanisms for custom compositions; no positive S3/S4/S5 parent mode is inferred from their existence.

## Recursion

Optional child Agent loops have local tasks and results, but complete recursive viability is not established by spawning.

## Variety and escalation

Tool errors return to the model; steering can skip remaining calls, abort stops, and maxSteps bounds iteration. Events/queues are routine channels, not an evidenced exceptional algedonic authority path.

## Evidence gaps

Exact-ref source/tests/README reviewed. Bun and Node are absent on the inspection host, so upstream native build/test was not run; no paid-provider or agent E2E task. No specific additional shipped metasystem path remains unresolved; future downstream hook implementations are outside this boundary.
