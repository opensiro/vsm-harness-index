---
harness_id: raw-cli
project_name: Raw CLI
repository: https://github.com/lploc94/raw-cli
review_ref: 378610653e2ab369f78c4de24d4828de795bfae8
reviewed_at: 2026-10-28
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

# Raw CLI

## Review boundary

- System in focus: one installed Raw CLI agent/session using the first-party TypeScript run loop, selected model adapter and tool registry in terminal, headless, dashboard or ACP mode; not an arbitrary organization formed by users of Raw.
- Purpose and identity: carry out user-specified coding, file/tool and automation work through a configurable model-driven agent with saved session continuity.
- Relevant environment: user requests, a local project/filesystem and shell, provider model responses, selected MCP services, tool results, operator permissions and host process constraints.
- Standard-distribution boundary: the shipped `@tlelabs/raw` package, `bin/raw.ts`, `src/agent.ts`, provider adapters, bundled tools, registry, sessions, optional managed process tool, hooks, terminal/dashboard and ACP interfaces.
- Credited operating / distribution surfaces: normal configured Raw agent execution (`raw --agent ...`, headless/interactive, ACP), with model-selected tools, policy/hook/approval enforcement and persisted dialogue; opt-in process and dynamic tool/skill configuration are considered only when actually selected.
- Adjacent first-party surfaces excluded from ownership: `examples/parent-agent.ts` is a client composition example, forkable sample agents/packages are not an installed multi-agent organization, `tests/` fixtures are corroboration, and repository CI/development and documentation site are not operating VSM actors. External model providers, MCP servers, user scripts and an ACP parent remain separately owned.
- First-party operating / deployment modes considered: terminal interactive, one-shot/headless, durable resumed sessions, dashboard, ACP server, opt-in hooks/MCP/process and model/tool configurations. Raw does not itself install an autonomous portfolio parent just by exposing these interfaces.
- Recursion level: one configured task/session agent as the operational system; optional external ACP parent or other model-created compositions are adjacent higher recursion unless explicitly wired into a supported first-party organizational function.
- Reviewed revision: `lploc94/raw-cli@378610653e2ab369f78c4de24d4828de795bfae8` (first-party source checkout matched frozen SHA).
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The shipped `src/agent.ts` owns a persistent conversation and an iterative provider request/response loop. Each turn presents the selected tool schemas, accepts model-authored tool calls, dispatches them in sequence through `ToolRegistry`, stores results and returns them to the next inference; a final model answer, cancellation, limit or error terminates that run. The same agent supports automatic/manual compaction, durable session leases/history, queued user input and stop hooks. [Agent loop and model/tool dispatch](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/agent.ts#L1300-L1575), [session recovery](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/sessions/runtime.ts#L19-L45).

The registry validates and normalizes tool arguments; selected policies can allow, deny or request human approval and hooks can block execution. This is enforcement of operator/developer-chosen rules, not independent whole-system policy judgment. A selected `process` tool can run bounded host subprocesses with lifecycle/cleanup, but these are not automatically independent autonomous S1 cells. Skills/tools can be forked or packaged; ACP is a protocol surface through which an *external* parent may drive Raw, not proof of parent-governed S3/S4/S5 in the installed single-agent runtime. [Registry policy and dispatch](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/tools/registry.ts#L195-L307), [process supervisor](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/processes/supervisor.ts#L80-L148), [ACP parent example](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/examples/parent-agent.ts#L1-L24), [supported modes and limits](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/README.md#L1-L55).

## Operational model

One configured model-backed agent absorbs task and project variety by inspecting files, selecting tools and applying results. The runtime mediates those decisions through policy, approvals, output caps, hooks and session persistence. The operator sets the model, tools, skills, working directory and permission rules. Concurrent foreground/background host jobs and multiple saved sessions are capabilities, but a first-party organization of independently active S1 units with its own coordination, current-control, audit or strategic governance closure is not automatically instantiated. No model-provider live task was run in this review; the positive operational finding is from executable first-party wiring.

## S1 — Operations

- State: A
- Function: execute one user's requested coding/automation work by interpreting context, choosing next tool actions, using results and producing a completed response or changed local artifacts.
- Disturbance / variety regulated: diverse user tasks and repositories, tool results/errors, incomplete context, changing code, approval denials and bounded execution failures.
- Decisive decision or feedback right: the model chooses whether to call tools, which exposed tool/arguments to use, how to interpret returned results and whether another step or a final response is appropriate.
- Decision owner: the configured model-driven Raw agent in the shipped `Agent.run` loop; the user originates the task and chooses allowable tools, while `ToolRegistry` enforces policy rather than selecting the task-specific next step.
- Supporting / enforcement mechanisms: provider adapters, tool schemas and result limits, permission approval, hooks, process limits, context compaction and persisted session state.
- Closure path: user/task context → provider-generated next tool call → validated/policy-gated dispatch → recorded result → subsequent provider request/decision, repeated until an answer or controlled stop.
- Boundary reachability: the normal CLI and ACP/dashboard session runtimes construct this `Agent`, and `src/agent.ts` performs the model/tool loop directly; it is not a demonstration-only agent or a feature of an external MCP implementation.
- Why this is / is not agent-owned: the model chooses semantic actions and uses observations; the runtime is a deterministic executor/enforcer. Removing the model's discretion leaves no task-specific choice despite the remaining tool registry and session store.
- Evidence: [provider generation and model action loop](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/agent.ts#L1336-L1518), [tool dispatch and feedback](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/agent.ts#L1519-L1575), [session runtime](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/sessions/runtime.ts#L19-L45), [CLI documentation](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/README.md#L17-L55).
- Basis: structural.
- Confidence: high for shipped loop/discretion structure; no provider performance measured.
- Caveats: selected tools can act with host-account permissions, and `ask` rules or human interaction can block a specific action; those restrictions do not turn the next-step choice into deterministic runtime ownership.

## S2 — Coordination

- State: —
- Function: no separate inter-S1 interference-attenuation relation is established for the standard single configured Raw agent.
- Disturbance / variety regulated: concurrency and shared-state safety of host commands and sessions, but not a structurally evidenced oscillation among independently operating S1 cells.
- Decisive decision or feedback right: model tool selection, host process lifetime and session ownership are handled within one agent/host contract; no separately evidenced mutual-adjustment response between distinct S1 units is selected.
- Decision owner: the model for its own operations; developer-specified supervisor/session guard logic for lifecycle enforcement; an external ACP parent may own any broader coordination.
- Supporting / enforcement mechanisms: persisted session claims, process ownership tokens/caps, tool policy, queued inputs and host process-group cleanup.
- Closure path: process/session gates constrain later activity of a single session; this does not close an S2-specific conflict among multiple S1 operations.
- Why this is / is not agent-owned: concurrent child processes, multiple saved agents and an ACP client example do not establish a specific inter-unit disturbance plus attenuating feedback at this declared boundary.
- Evidence: [session binding](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/sessions/runtime.ts#L19-L45), [bounded process lifecycle](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/processes/supervisor.ts#L80-L148), [ACP parent is an example](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/examples/parent-agent.ts#L1-L24).
- Basis: structural.
- Confidence: medium-high for shipped single-agent modes.
- Caveats: a user can externally compose multiple Raw agents into a team, but such composition is outside the credited first-party distribution.

### Absence scope

- Surfaces inspected: Raw agent loop, session runtime/store, managed process supervisor, tool policy, ACP examples and README-supported operating modes.
- Plausible first-party paths checked: simultaneous saved sessions, queued inputs, process caps, background jobs, ACP parent orchestration and package-defined agents.
- Why no material first-party path remains: these paths isolate or transport single-agent work and allow external composition; they do not ship distinct mutually regulating S1 cells, a concrete inter-S1 collision/oscillation witness and a corrective feedback decision between them.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system discretionary current-control loop over a portfolio of autonomous S1 commitments/resources is established.
- Disturbance / variety regulated: tool permission, process limits, stalled calls, session interruption and execution errors are local safeguards, not whole-system resource bargaining.
- Decisive decision or feedback right: the user/developer configures allowed tools, model, process caps and runtime policies; the agent chooses local tool actions, while runtime code applies those limits.
- Decision owner: operator/developer for static configuration and approvals; the model for its own task; no in-boundary manager with a live whole-system view and substantive current-control authority was found.
- Supporting / enforcement mechanisms: tool registry, policy, approval handlers, hooks, process supervisor, session leases, stop/continue and usage views.
- Closure path: denied/approved calls return to the task or stop the run; no distinct system-wide current-control decision reallocates competing S1 commitments and returns into operations.
- Why this is / is not agent-owned: enforcement is not ownership, and an operator approval over one tool call is not the parent S3 decision scope required for a positive mode.
- Evidence: [tool policy/approval enforcement](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/tools/registry.ts#L195-L307), [process limits](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/processes/supervisor.ts#L80-L148), [operator configuration](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/README.md#L54-L115).
- Basis: structural.
- Confidence: medium-high for the credited operating boundary.
- Caveats: a larger deployment can implement control using Raw as a substrate, but that external manager's decision cannot be credited to this installed session.

### Absence scope

- Surfaces inspected: runtime lifecycle, session claims, registry policy/approval, background process limits, model/config management, dashboard and ACP entry.
- Plausible first-party paths checked: approval decisions, process caps, session interrupt/resume, tool/user configuration, dashboard command controls and external parent ACP invocation.
- Why no material first-party path remains: none supplies a first-party whole-system current view with discretionary shared resource/priority/accountability regulation and returned operation; the available guards and controls are task/host enforcement or optional parent extensions.

## S3* — Complementary audit

- State: —
- Function: no supported materially independent audit path that challenges the operational agent's normal completion claims and returns corrective findings is installed by default.
- Disturbance / variety regulated: local tool or request errors can be visible, but no separate independently judging auditor of operational output is part of the credited run loop.
- Decisive decision or feedback right: the same agent/model decides what to inspect and when to finish; the runtime validates tool contracts and exposes history but does not make a complementary independent assessment of task correctness.
- Decision owner: the operating agent for ordinary self-checks; operators/external test tools may inspect separately but are not first-party wired audit owners.
- Supporting / enforcement mechanisms: tool validation, error statuses, logs, visible tool output, session history, hooks and tests of Raw's own codebase.
- Closure path: errors and tool results can inform the same agent's next step; no separate audit judgment/veto is automatically returned from complementary access into subsequent control.
- Why this is / is not agent-owned: an internal tool check or user-defined review skill is not sufficient independent access to operational reality, and repository tests belong to product development rather than the supported agent's audit loop.
- Evidence: [single agent loop and stop](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/agent.ts#L1476-L1575), [registry validation and hooks](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/tools/registry.ts#L195-L310), [optional configurable skills/hooks](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/README.md#L112-L128).
- Basis: structural.
- Confidence: medium for default and documented optional distribution.
- Caveats: a user may install an independent reviewer through third-party skills, tools or ACP composition; those actor/authority paths are not present by default.

### Absence scope

- Surfaces inspected: loop termination, tool contract validation, hook dispatch, README's skills and tools, ACP examples, session history and development verification surfaces.
- Plausible first-party paths checked: Stop hooks, tests, self-verification via bash, `todo`, callback approvals, independent process jobs and forked user tools.
- Why no material first-party path remains: no shipped distinct auditor has complementary source access and an independent substantive judgment with corrective return into Raw's ordinary operational claims; generic extensibility does not compose that function.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external/prospective environment intelligence loop that generates adaptation options and returns them into Raw's current capability is shipped.
- Disturbance / variety regulated: evolving task and tool outputs are handled within S1; provider choices and user-managed customization do not constitute automatic future-oriented organizational adaptation.
- Decisive decision or feedback right: current task planning belongs to the operating agent; selecting/editing models, skills, agent packages and configuration belongs to the user/developer unless a separate agent is purpose-built externally.
- Decision owner: local user/contributor for product capabilities and configuration; no first-party S4 agent or S4-specific constructor closes prospective adaptation.
- Supporting / enforcement mechanisms: persistent conversation, compaction, packages, skill authoring, model selection and update flows.
- Closure path: configuration edits may affect later sessions, but there is no shipped external-and-future analysis → option choice → authorized current-capability update loop at this recursion.
- Why this is / is not agent-owned: memory/compaction and user-led customization conserve or extend task context; they are not enough to establish S4 prospective environmental modeling and its conversation with current control.
- Evidence: [configuration/agent management](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/management/agents.ts#L1-L75), [context compaction](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/agent.ts#L475-L860), [package and skill management](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/README.md#L112-L137).
- Basis: structural.
- Confidence: medium-high for installed standard distribution.
- Caveats: a third-party agent built with Raw could autonomously adapt a wider system; no such organization is wired into the assessed single-agent mode.

### Absence scope

- Surfaces inspected: agent/config management, compaction, package and skill tooling, hooks, external provider interfaces and first-party operating documentation.
- Plausible first-party paths checked: persistent memory, model switching, skill creation, package upgrade, evolving instructions and task planning.
- Why no material first-party path remains: these are context continuity or operator/developer construction paths, not a shipped future-environment sensing/adaptation decision that feeds back to regulate current operational capability.

## S5 — Policy and identity

- State: —
- Function: no first-party loop for ultimate purpose/identity-policy decisions and returned governance at the single-session recursion is established.
- Disturbance / variety regulated: routine task permissions, provider credentials, user preferences and tool risk are governed as local operational restrictions, not identity-level tensions between S3 and S4.
- Decisive decision or feedback right: an operator selects/edit agents, model, prompts, tools and rules; the runtime enforces them. There is no evidenced identity/ultimate-policy issue routed to a legitimate parent, decided and returned to govern future operations as a first-party mode.
- Decision owner: user/developer for static agent definition and immediate approvals; no runtime agent holds charter/ultimate-policy authority and no function-specific parent S5 path is installed.
- Supporting / enforcement mechanisms: prompt, tool allow/ask/deny policy, hooks, config management, approvals, ACP permission bridge and session scope.
- Closure path: config changes and permission decisions affect local tool availability or current operation, but do not close a system-identity policy conflict at the declared recursion.
- Why this is / is not agent-owned: system prompts, permissions and human approval are only boundary constraints absent a substantive identity-policy decision and returned authority loop.
- Evidence: [model/agent configuration](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/README.md#L56-L113), [config edits](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/management/agents.ts#L10-L75), [policy enforcement](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/tools/registry.ts#L95-L110), [approval](https://github.com/lploc94/raw-cli/blob/378610653e2ab369f78c4de24d4828de795bfae8/src/tools/registry.ts#L250-L278).
- Basis: structural.
- Confidence: medium-high for reviewed modes.
- Caveats: human software ownership and upstream OSS governance are adjacent systems, not first-party S5 closure for an installed Raw session.

### Absence scope

- Surfaces inspected: CLI and configuration docs, `src/management/agents.ts`, registry policy, approval path, hooks, ACP and first-party standard mode descriptions.
- Plausible first-party paths checked: prompts/agent identity settings, permission requests, package installation, capability grants, operator changes, management APIs and ACP external-parent interaction.
- Why no material first-party path remains: controls constrain task operation or let a user reconfigure an agent, without a supported identity/ultimate-policy controversy, authoritative parent/agent disposition and returned ongoing governance loop.

## Recursion

The system-in-focus is one configured agent/session. A saved session is an operational continuity boundary; process children are shell jobs, and forkable agent packages or ACP clients are constructors/interfaces. Neither multiple named configured agents nor a demo ACP parent establishes recursive viable units with their own complete regulatory systems.

## Variety and escalation

Model-selected tools and output observations absorb task variety; result limits, tool policies, process/session cleanup, context compaction and approval requests attenuate unsafe or excessive input/output variety. An unknown or denied tool, interruption, model error, context budget limit or denied approval may stop the run with a durable error/receipt. Those status channels are not algedonic or metasystem functions by name; they normally belong to S1/local host enforcement, and the operator may decide further action outside the assessed boundary.

## Evidence gaps

- No live provider-backed coding task was run. The source wiring, user documentation and deterministic tests are the basis for the agent-owned S1 decision path, not measured task performance.
- Native Raw checkout: `npm ci --ignore-scripts` completed from its lockfile on Node 24.22.1 and `npm run typecheck` passed. Of four selected test files run through `node --import tsx --test`, `agent-lifecycle` and `registry-policy` passed, while `agent` and `process-supervisor` failed in this host with a Node `InternalCallbackScope::Close` assertion; this is **not** a full native suite PASS or proof of a Raw product bug. No provider-backed or GUI E2E task was attempted.
- Optional user-defined tools, skills, hooks and ACP parent integrations can implement additional organizations, but their actor identity/rights are not fixed by Raw's standard distribution; the assessment does not promote hypothetical compositions to canonical modes.
- The negative findings are bounded to the supported first-party single configured agent and shipped selectable mechanisms. They do not assert universal absence in every third-party Raw-based application.
