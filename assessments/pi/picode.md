---
harness_id: picode
project_name: picode
repository: https://github.com/n3sRan/picode
review_ref: b66917691341dcca05f571ed7220afd601aeeee5
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# picode

## Review boundary

- System in focus: the first-party installed picode TypeScript/Node.js local coding assistant, including its model-driven agent loop, registered workspace tools, one-task terminal host, context management and session recovery.
- Purpose and identity: take user programming requests and complete bounded local read/edit/check tasks using a configured OpenAI-compatible model and explicit `finish` protocol.
- Relevant environment: workspace files, command results, model/tool protocol failures, task requirements, operator approvals, bounded context, recovered session state and the local operating system.
- Standard-distribution boundary: packaged picode v0.1.0 Node.js 22+ CLI for macOS/Linux at frozen `b66917691341dcca05f571ed7220afd601aeeee5`. External inference gateway and user shell are infrastructure; development/demo fixtures and a separately operated model service are not part of the harness metasystem.
- Credited operating / distribution surfaces: `src/agent/`, `src/tools/`, `src/llm/`, `src/context/`, `src/sessions/`, `src/security/`, `src/ui/`, `src/cli.ts`, `src/config.ts` and domain state/event/message modules, compiled into the packaged `dist` and `picode` bin.
- Adjacent first-party surfaces excluded from ownership: `AGENTS.md` contributor instructions, implementation `docs/PLAN.md` and `docs/SPEC.md`, developer tests and mock providers, demonstration/real-API smoke run, npm build/release tasks and university project planning. None is an independently installed governance cell.
- First-party operating / deployment modes considered: one-shot `picode "task"`, interactive CLI, `--resume` session recovery, human shell-command approval/abort, verbose UI, explicit/optional automatic context compaction and alternate compatible gateway settings.
- Recursion level: one local coding task and its continuing interactive session. There are no first-party nested autonomous S1 workers or multi-installation organizational controls.
- Reviewed revision: `b66917691341dcca05f571ed7220afd601aeeee5` (batch #1011 frozen row 10).
- License screen: `package.json` declares MIT; README also reports MIT.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`TerminalApp` creates one `AgentLoop`, one `ToolRegistry`, a workspace-constrained `PathPolicy` and an `ApprovalBroker`. The model receives the seven registered read/search/write/edit/command/finish tool schemas; `AgentLoop.runLoop()` validates a model-proposed batch, executes each valid tool strictly serially, records results in the conversation and continues until a validated `finish` call or an explicit error/limit/abort. `TaskLimitTracker` and repetition/context guards enforce fixed constraints; human approval is requested for every shell command. Atomic session snapshots record messages, usage and a pending side-effect marker, so resume never automatically replays unconfirmed mutations.

`ContextCompactor` optionally asks a model to summarize older dialogue for *the same* coding session and keeps the recent state; it is not a future-environment intelligence worker. The interactive CLI can start/list/resume separate *serial* sessions, turn verbose output on/off and abort the current task. The declared MVP explicitly excludes Web/IDE integration, MCP, subagents, parallel tools, general event audit, a safe OS command sandbox and provider-independent adaptive governance.

Primary frozen evidence: [agent loop](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/agent/loop.ts), [terminal](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/ui/terminal.ts), [tool registry](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/tools/registry.ts), [compactor](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/context/compactor.ts), [architecture](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/docs/ARCHITECTURE.md).

## Operational model

The configured model owns ordinary coding-tool decisions within a single S1 loop. Deterministic local validation, serial execution, path checks, approval broker, context limits and crash-safe persistence constrain the loop but do not themselves decide an S2/S3/S3*/S4/S5 organizational function. One actively running task can be aborted by its user; no shipped current whole-of-multiple-operations manager, independent auditor, prospective adaptation process or identity-policy authority is exposed.

## S1 — Operations

- State: A
- Function: execute local software-development requests through model-decided workspace inspection, file changes, checks and task completion.
- Disturbance / variety regulated: different codebases/tasks, tool errors/denials, failed validations, insufficient context, inconsistent provider responses and partial executions.
- Decisive decision or feedback right: the configured model selects registered tools and parameters; after each returned result it can revise the next action and must explicitly call `finish` to declare a successful task.
- Decision owner: configured coding model within the first-party `AgentLoop`.
- Supporting / enforcement mechanisms: tool schema validation, `PathPolicy`, `CliApprovalBroker`, serial batch execution, request/time/repetition budgets, context management, session snapshots and event rendering.
- Closure path: user request → model selects a tool/batch → local validation, approval and execution → tool result/denial or protocol reminder enters context → next model action or `finish` termination.
- Boundary reachability: `TerminalApp.runTask()` constructs the model-backed `AgentLoop` and built-in registry for installed CLI/one-shot paths; compiled files are the declared published package.
- Why this is / is not agent-owned: the model makes substantive context-sensitive coding choices; validators and human shell approvals impose limits without choosing the solution.
- Evidence: [loop](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/agent/loop.ts), [terminal construction](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/ui/terminal.ts), [tool definitions](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/tools/index.ts), [finish](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/tools/finish.ts).
- Basis: frozen source and scripted-provider deterministic tests.
- Confidence: high for first-party S1 construction.
- Caveats: no real model execution or agent-quality benchmark performed in this assessment.

## S2 — Coordination

- State: —
- Function: no coordination relation between distinct S1 operational units at the assessed recursion is provided.
- Disturbance / variety regulated: workspace file collisions could occur if independent coding agents shared a project, but the installed process runs one Agent Loop with strictly serial tool calls and one active task.
- Decisive decision or feedback right: none for inter-S1 conflict resolution; fixed tool ordering and busy-task rejection manage one loop's local operations.
- Decision owner: fixed `AgentLoop` tool executor/`TerminalApp` guard for local serialization; no inter-unit coordinator exists.
- Supporting / enforcement mechanisms: prevalidation of all tool calls, serial batch executor, `TerminalBusyError`, pending side-effect snapshots and path policy.
- Closure path: only one running S1 receives its own tool results; there is no inter-S1 disturbance/attenuation/returned-coordination loop.
- Why this is / is not agent-owned: local sequential command order, batch atomicity checks and session switching are not relations between independently deciding operational units.
- Evidence: [architecture](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/docs/ARCHITECTURE.md), [loop](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/agent/loop.ts), [terminal](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/ui/terminal.ts).
- Basis: explicit single-agent/serial MVP constraint plus source implementation.
- Confidence: high for bounded absence.
- Caveats: users may launch multiple independent processes, but no first-party mechanism coordinates them.

### Absence scope

- Surfaces inspected: CLI and terminal task lifecycle, `AgentLoop` tool batches, tool registry, sessions, events, architecture and declared MVP exclusions.
- Plausible first-party paths checked: serial model tool batches as S2, busy-task guard as conflict control, pending side-effect recovery as coordination and multiple resumable sessions as distinct active S1 cells.
- Why no material first-party path remains: these are internal one-loop safety/order constraints or saved dormant histories; no simultaneously distinct autonomous S1s and no feedback-regulated inter-S1 interference exist.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control owner over a set of S1 commitments/resources is established.
- Disturbance / variety regulated: one task can exceed limits, block on approval or be stopped, but this is local task control and not supervision of a whole operational portfolio.
- Decisive decision or feedback right: human may approve/deny individual shell calls and cancel the one active task; fixed request/active-time/repetition limits stop the loop, while the model plans its own actions.
- Decision owner: operator for tactical action approval/cancel, configured deterministic runtime for budgets, model for operational choices.
- Supporting / enforcement mechanisms: `CliApprovalBroker`, `AbortController`, `ActiveTimeTracker`, `TaskLimitTracker`, process busy flag and status rendering.
- Closure path: an individual tool or task stops/continues, but no whole-current resource/commitment overview → management decision → returned multi-unit operational regulation occurs.
- Why this is / is not agent-owned: hard limits enforce policies chosen by configuration, while one-task cancel/approval is not an S3 parent-governed function.
- Evidence: [terminal](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/ui/terminal.ts), [limits](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/agent/limits.ts), [approval](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/security/approval.ts).
- Basis: bounded first-party runtime/operator control source.
- Confidence: high for absence at declared recursion.
- Caveats: an external user could manually supervise several separate installations, which is outside picode's standard installed control plane.

### Absence scope

- Surfaces inspected: CLI commands, terminal/session lifecycle, busy/abort handling, task limits, approval, render/event surfaces and architecture docs.
- Plausible first-party paths checked: `/sessions` and `/resume` as whole-current view, terminal abort as parent S3=P, request budget as autonomous supervisor and serial tool dispatch as current operational coordination.
- Why no material first-party path remains: session listings are stored conversations rather than a concurrent whole-current operations view, and stop/limits concern only one S1 task; no substantive cross-unit supervisory decision closure is shipped.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit path that challenges normal operational reports and returns a separate corrective finding.
- Disturbance / variety regulated: code errors can be caught by requested command checks and tool errors, but those are ordinary feedback to the same coding agent.
- Decisive decision or feedback right: model chooses whether to invoke a shell/check; operator authorizes it; the ordinary tool result comes back to the coder. No distinct reviewer decides an audit verdict.
- Decision owner: main coding model for task checks; fixed runner/tool validator for deterministic results.
- Supporting / enforcement mechanisms: scripted fixture tests, `run_command`, execution checkpoint recovery, event renderer, explicit `finish` status and safe output redaction.
- Closure path: tool/check output returns through S1; no independently controlled raw-evidence audit and separate corrective return is present.
- Why this is / is not agent-owned: a model consulting its own tests is normal S1 verification, not complementary institutional audit.
- Evidence: [shell tool](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/tools/run-command.ts), [agent loop](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/agent/loop.ts), [project scope](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/AGENTS.md).
- Basis: direct tool/runtime inspection plus explicit no-subagent MVP boundary.
- Confidence: high for bounded negative.
- Caveats: a separate human/external review might be added around the CLI but is not a packaged audit loop.

### Absence scope

- Surfaces inspected: shell checks, finish protocol, tool result handling, event rendering, session recovery, mock tests and project architecture/exclusions.
- Plausible first-party paths checked: self-invoked `run_command` as audit, scripted provider tests as evaluator, replay of saved session as independent evidence, output/limit guards as watchdog and model `finish` as separate verdict.
- Why no material first-party path remains: all are within the coder's routine work, deterministic safety enforcement or adjacent developer evaluation, without a separate audit judgment and corrective control return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external/future-environment sensing and organizational adaptation choice returned to present capability is provided.
- Disturbance / variety regulated: future tasks and model limits could change, but the built-in response is bounded context reduction and user-updated configuration, not prospective strategic capability acquisition.
- Decisive decision or feedback right: the model summarizes its own historic conversation at an optional threshold; the user supplies model endpoint/settings. Neither selects future adaptations from outside distinctions.
- Decision owner: configured runtime and present-task model for compaction; user for external configuration.
- Supporting / enforcement mechanisms: `ContextCompactor`, `BudgetTracker`, config, atomic sessions, explicit `/compact`, optional automatic compaction and provider abstraction.
- Closure path: old transcript → model summary → shorter context for same task; no external prospective options/adoption into continuing capabilities.
- Why this is / is not agent-owned: model-based compression and saved memories are not automatically S4; the supported code contains no future-capability governance.
- Evidence: [compactor](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/context/compactor.ts), [budget](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/context/budget.ts), [CLI commands](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/ui/commands.ts).
- Basis: frozen context/configuration code and explicit MVP exclusions.
- Confidence: high for bounded negative.
- Caveats: later project development could add adaptive abilities, but is outside this ref.

### Absence scope

- Surfaces inspected: context budget/compaction, session persistence, config/provider adapters, CLI commands and architecture/MVP scope.
- Plausible first-party paths checked: autonomous context compaction as learning, persistent sessions as knowledge acquisition, compatible gateway/model setting as adaptation and external developer plans as agent S4.
- Why no material first-party path remains: all operate on past/current task context or static human-provided configuration; no shipped prospective external-option selection and return-to-current-capability loop exists.

## S5 — Policy and identity

- State: —
- Function: no agent or parent-governed ultimate identity/policy decision loop is part of the installed single-user session.
- Disturbance / variety regulated: requests can breach workspace/security/user limits, but they are handled by established fixed constraints and tactical shell consent, not constitutional policy reconsideration.
- Decisive decision or feedback right: user approves individual shell actions; programmer fixes allowed paths, tool schemas, model system prompt and context limits at build/configuration time.
- Decision owner: user for immediate actions, developer/configuration for shipped constraints, with no distinct ultimate-policy authority attached to the live installed organization.
- Supporting / enforcement mechanisms: path escape checks, secret redaction, approval broker, prompt, task limit/repetition guard and local session recovery.
- Closure path: tool request → allow/deny/stop check → next current task step; there is no identity/ultimate-policy issue → legitimate governing authority → binding decision returned to future operation.
- Why this is / is not agent-owned: safety policies, static instructions and individual consent do not make the model or user a first-party S5 loop.
- Evidence: [path policy](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/security/path-policy.ts), [approval](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/security/approval.ts), [prompt](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/src/agent/prompt.ts), [architecture](https://github.com/n3sRan/picode/blob/b66917691341dcca05f571ed7220afd601aeeee5/docs/ARCHITECTURE.md).
- Basis: frozen security/configuration/entry-point evidence.
- Confidence: high for bounded negative.
- Caveats: ordinary human priority-setting outside a single installed task is not automatically S5=P.

### Absence scope

- Surfaces inspected: system prompt, user command approval, file/path policy, secret handling, configuration, CLI/session controls, final status protocol and project-level author instructions.
- Plausible first-party paths checked: shell approval as S5=P, safety invariants as identity policy, `finish` as strategic choice, manual project roadmap as distributed ultimate authority and resumed sessions as changed organizational policy.
- Why no material first-party path remains: these are current-action controls, static developer instructions or adjacent development decisions, without a reachable identity-level authoritative decision and return path in the installed session.

## Distributed OSS parent arrangement

Maintainers of the public source may make design and release decisions, but the installed picode CLI does not join independent users or maintainers into a first-party organizational parent supervising their tasks. Repo instructions and release plans belong to that adjacent software-development recursion and do not establish first-party S3/S4/S5 ownership.

## Self-hosted and non-human modes

Both one-shot and interactive self-hosted CLI modes allow the model to make S1 tool choices, while the attending user may approve shell commands or abort the one current task. No supported mode gives the model or parent a separate whole-current, prospective or identity-policy control loop.

## Recursion

One model-driven S1 performs coding operations in one workspace/task. Persisted sessions and serial tool calls are not separately viable S1 children; no recursive subagent metasystem or distinct coordination among multiple S1s is installed.

## Variety and escalation

Tool failures, rejected shell commands, timeout/loop guard events and context thresholds either return to the current coder or stop it. Human approval is tactical, and exceptional status/termination rendering is not an additional S-function or an algedonic channel with a separate reachable governance closure.

## Evidence gaps

- Frozen `n3sRan/picode@b66917691341dcca05f571ed7220afd601aeeee5`, Node.js v24.19.0 (package supports Node >=22). `npm ci --ignore-scripts` used exact `package-lock.json`. `npm run build` and `npm run typecheck` PASS. Native scripted-provider `vitest run`: **106 PASS, 1 SKIP across 9 test files** with local child processes allowed; no live model/API E2E was run.
- In the initial restricted shell, **104 PASS, 2 FAIL, 1 SKIP**; both failures concerned child shell subprocess output assertions. The identical suite rerun with permitted local subprocess execution produced **106 PASS, 1 SKIP**. This is evidence of environment-sensitive shell tests, not a changed codebase or a newly implemented fix.
- Positive S1 records shipped executable control wiring, not the probability of successful code correction by a real LLM. The explicitly optional upstream real-API demonstration was excluded under the batch offline-only rule.
- Negative states are bounded to the published one-agent/single-process distribution and documented first-party modes, not a claim that picode can never be extended into a multi-agent organization.
