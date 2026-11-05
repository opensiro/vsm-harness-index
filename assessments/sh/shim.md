---
harness_id: shim
project_name: Shim
repository: https://github.com/Balanov/shim
review_ref: 22b485fe5ac516f8d1ae44de2edeb77e907cfe9e
reviewed_at: 2026-11-05
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

# Shim

## Review boundary

- System in focus: A single locally installed Shim CLI/REPL agent executing one configured model against local workspace tools, optional MCP services and persistent session messages; not an organization of many independent agents.
- Purpose and identity: Lightweight Go terminal agent harness with configurable model providers, local tools, optional MCP/skills, permission prompts and saved sessions.
- Relevant environment: Human terminal operator, workspace contents, tool execution errors, API availability, MCP service responses, model output and persistent JSONL history.
- Standard-distribution boundary: `cmd/shim`, first-party `internal/{cli,agent,provider,tools,mcp,skills,router,session,config}` Go packages and documented CLI modes.
- Credited operating / distribution surfaces: [architecture](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/docs/ARCHITECTURE.md), [run wiring](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/cli/run.go), [agent](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/agent/agent.go), [tool enforcement](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/tools/tools.go), [router](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/router/router.go), [MCP](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/mcp/manager.go), [session](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/session/session.go).
- Adjacent surfaces excluded from operational credit: External model inference providers, external MCP server intelligence, operator-provided `AGENTS.md`/SKILL.md instructions, GitHub CI and repository maintainer decisions. These may guide or test Shim, but are not installed independent governing units.
- First-party modes inspected: `shim run` model/tool loop with configured provider and `--max-steps`; interactive chat and optional natural-language management-command router; read-only / ask / auto tool permissions, optional MCP registration, skills loaded on demand, resumed JSONL session.
- Recursion level: One task-working model agent and its local first-party harness, with operator controls at its boundary. Do not infer multiple S1 agents from multiple tools, models, sessions or MCP connections.
- Reviewed revision: `Balanov/shim@22b485fe5ac516f8d1ae44de2edeb77e907cfe9e` (first-party MIT source).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`cli.runPrompt` selects a configured provider, registers first-party filesystem/shell/skill tools plus optional MCP wrappers, constructs an `Executor` with the selected permission mode and invokes `agent.Run`. Its bounded Go loop appends user and assistant turns, asks the configured model for tool calls, executes calls through the gate, appends each result as a tool message, and asks the model again. The session store appends JSONL records and can resume them. A distinct REPL router either recognizes fixed phrases or asks a configured model to compile a *management* slash command, whose output is allowlisted and requires user confirmation when mutating. This is not an autonomous coordinating metasystem. [run](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/cli/run.go), [agent](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/agent/agent.go), [REPL](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/cli/repl.go), [router](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/router/router.go).

## Operational model

The configured model owns discretionary next-action selection inside a user task; the Go agent loop closes tool-result feedback to the next model decision. The user/operator owns provider choice, permissions and management changes; fixed guard rules constrain execution. Extra model endpoints and remote MCP providers extend tool access but do not establish additional first-party S1 units or governance. The distinct model-based router may choose a whitelisted management command subject to operator confirmation, which cannot be promoted to independent S4/S5 authority.

## S1 — Operations

- State: A
- Function: Model-directed workspace task work with tool observations fed into subsequent decisions.
- Disturbance / variety regulated: User requests, changing workspace files and shell outputs, MCP/tool errors and model-generated tool arguments.
- Decisive decision or feedback right: Configured model selects ordinary response versus tool calls, target tool and arguments and next response after receiving observations.
- Decision owner: Configured model through first-party `agent.Agent.Run`, with host execution mediated by the installed tool executor.
- Supporting / enforcement mechanisms: Provider normalization, tool schema registry, bounded `MaxSteps`, workspace path checks, read-only/ask/auto permission gate and append-only session history.
- Closure path: Terminal prompt → CLI composition → provider inference → model-selected tool → executor/workspace or MCP → tool result message → next inference or final response.
- Boundary reachability: `runPrompt` registers tools and calls the agent loop; real provider clients are explicitly configurable. It is more than a test-only agent skeleton, although remote-provider operation was not replayed here.
- Why this is / is not agent-owned: The model chooses task steps and reacts to tool outcomes. Shell/permission transports and human-approval prompts do not themselves choose strategy.
- Evidence: [run wiring](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/cli/run.go), [agent loop](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/agent/agent.go), [executor](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/tools/tools.go), [MCP](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/mcp/manager.go).
- Basis: Installed first-party decision/action/observation/redecision route evidenced by source and unit-test scaffolding.
- Confidence: High for source reachability; not a claim of an executed paid-provider E2E.
- Caveats: The chosen external model's behavior and any MCP server are outside first-party Shim; permissions may stop tools.

## S2 — Coordination

- State: —
- Function: No intra-recursion coordination among distinct autonomously task-operating S1 units is installed.
- Disturbance / variety regulated: Tool name collisions, concurrent model-provider options and MCP availability are possible technical conflicts, not demonstrated conflict between autonomous S1 work units.
- Decisive decision or feedback right: The registry rejects collisions and a human selects a model; no agent resolves clashes between S1 objectives.
- Decision owner: Static namespace/registry and operator configuration.
- Supporting / enforcement mechanisms: Tool registry, MCP namespacing, CLI model selection and management router allowlist.
- Closure path: Registry collision → setup failure, or user configuration → next session; no two S1 cells → coordination decision → returned operational adjustment.
- Why this is / is not agent-owned: Tool schemas and MCP endpoints are services consumed by one model, not multiple independently deciding S1 agents.
- Evidence: [MCP manager](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/mcp/manager.go), [registry](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/tools/tools.go), [run](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/cli/run.go).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: User-authored external MCP services could implement coordination, but are outside this first-party boundary.

### Absence scope

- Surfaces inspected: Tool registry, MCP manager/clients, CLI run/REPL, model selection and router.
- Plausible first-party paths checked: MCP namespaced tool mediation, multiple configured providers, management router as coordinator, sequential tool calls as conflict resolution.
- Why no material first-party path remains: None installs two self-deciding S1 units, detects their operational contention and returns an accountable balancing decision to them.

## S3 — Inside-and-now control

- State: —
- Function: No present-time portfolio control of independently operating S1 units is established.
- Disturbance / variety regulated: Excess steps, risky file changes and tool failures are bounded at one agent's task level.
- Decisive decision or feedback right: `MaxSteps` errors after a fixed number of turns; permission mode is configured by a human and can request one-shot approval, not autonomously reallocate commitments.
- Decision owner: CLI operator and static loop/executor conditions.
- Supporting / enforcement mechanisms: Step cap, `--read-only`/`--yes`, executor mode and REPL confirmations, session logging.
- Closure path: Limit or denied tool call → current-run error/result; there is no S3 observation/priority/resource decision affecting a portfolio of S1 units.
- Why this is / is not agent-owned: Host guardrails regulate one S1's conduct without independently managing whole-system current performance.
- Evidence: [agent loop](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/agent/agent.go), [executor](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/tools/tools.go), [CLI run](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/cli/run.go).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: Per-task model self-monitoring belongs within S1 at this recursion, not an independent S3.

### Absence scope

- Surfaces inspected: Agent step loop, executor permission model, CLI confirmation and session record lifecycle.
- Plausible first-party paths checked: Step budget as S3, tool approvals as resource management, session log as management dashboard, router as management controller.
- Why no material first-party path remains: They do not observe and choose whole-system operations for a set of S1 actors and feed revised commitments back into them.

## S3* — Complementary audit

- State: —
- Function: No separately owned independent reality-checking audit lane complements current S3 management.
- Disturbance / variety regulated: Malicious tool outputs, unsafe filesystem changes and provider replies may be constrained by prompt or tool gates, not independently audited.
- Decisive decision or feedback right: `Executor` checks static level and human permission; unit tests use fixtures, neither yields independent runtime audit findings returned to S3.
- Decision owner: Operator for approvals, deterministic guards for execution, developer for tests.
- Supporting / enforcement mechanisms: Permission gating, resolved-path confinement, agent prompt treating tool/MCP content as untrusted, unit tests.
- Closure path: Tool response returns to same model or approval blocks one operation; no alternate evidence acquisition → independent audit verdict → corrective S3 management path.
- Why this is / is not agent-owned: Human approval and ordinary unit tests are not an installed S3* auditor, and agent self-recheck would not be independent.
- Evidence: [executor](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/tools/tools.go), [prompt](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/agent/agent.go), [tool tests](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/tools/files_test.go).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: Operators may run external audits; this is not a first-party installed runtime audit channel.

### Absence scope

- Surfaces inspected: Permission executor, file/path tools and tests, model and MCP adapters, session store.
- Plausible first-party paths checked: Approval as audit, permission checking as complementary reality access, source tests as independent truth, session logs as audit feedback.
- Why no material first-party path remains: No separate auditor obtains operational evidence via an independent path, renders a complementary judgment and closes the finding to S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective environmental strategy/adaptation cycle is installed over the harness.
- Disturbance / variety regulated: Model/provider availability, new MCP services, skill updates and evolving user tasks.
- Decisive decision or feedback right: Operator selects/adds providers, skills or MCP services; a compiled management command is whitelisted and explicitly confirmed before mutating.
- Decision owner: Human operator; narrow router compiler can suggest a bounded command but has no independent future-horizon mandate.
- Supporting / enforcement mechanisms: Config updates, model discovery, lazy skill loading, MCP registration and opt-in model-based router.
- Closure path: Manual configuration change or task reply → present operation; no future-environment intelligence → strategy decision → coordination with S3 → adopted future change.
- Why this is / is not agent-owned: CLI convenience for service installation and slash-command compilation is not owned prospective strategy or adaptation feedback.
- Evidence: [router](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/router/router.go), [REPL](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/cli/repl.go), [architecture](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/docs/ARCHITECTURE.md).
- Basis: Bounded absence review including strongest S4 candidate, the optional AI management router.
- Confidence: High.
- Caveats: Individual agent may discuss future plans as ordinary S1 user work; no installed organizational S4 is evidenced.

### Absence scope

- Surfaces inspected: Router commands/validation, REPL approval, model/skills/MCP management, agent run and persisted sessions.
- Plausible first-party paths checked: Model routing as strategy, automatic provider discovery as environmental sensing, skill installation as adaptation, saved memory as future intelligence.
- Why no material first-party path remains: Management is operator-confirmed configuration without a prospective environmental model, autonomous option selection and operationally adopted S4–S3 loop.

## S5 — Policy and identity

- State: —
- Function: No distinct ultimate identity-policy authority and closed mandate governs the running agent organizationally.
- Disturbance / variety regulated: User intent, workspace permissions, untrusted instructions and changing local configuration.
- Decisive decision or feedback right: The human sets permissions/model and confirms mutating router requests; static prompt tells the model to treat external content as untrusted.
- Decision owner: External operator/developer for policy, not a packaged S5 governance role or agent-level identity body.
- Supporting / enforcement mechanisms: Prompt safety text, local AGENTS.md injection, tool approval/read-only restrictions, router whitelist.
- Closure path: Human config/approval → a permitted task action; no identity-level issue → legitimate ultimate-policy deliberation or parent decision → returned enforceable organizational policy.
- Why this is / is not agent-owned: Static instructions, user approvals and optional AGENTS.md do not prove S5 self-governance or an accountable parent-assisted policy cycle.
- Evidence: [prompt construction](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/agent/agent.go), [executor](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/tools/tools.go), [REPL](https://github.com/Balanov/shim/blob/22b485fe5ac516f8d1ae44de2edeb77e907cfe9e/internal/cli/repl.go).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: Human policy ownership exists outside this assessed local runtime, but the specific returned S5 control path is not installed.

### Absence scope

- Surfaces inspected: System prompt and AGENTS.md inclusion, operator confirmation, model/router permissions, config/skills and CLI execution modes.
- Plausible first-party paths checked: Repository AGENTS.md as charter, provider/operator approval as parent-assisted S5, router allowlist as policy-making, static system prompt as identity choice.
- Why no material first-party path remains: These are external rules or one-step gates with no identity-level deliberation, legitimate decision owner and closed return of an authoritative mandate.

## Recursion

One agent using many tools is one S1 task-operating unit. The optional management command compiler, remote MCP service wrappers and multiple model profiles are not separate first-party organizational S1 units. No installed recursively viable parent system is demonstrated.

## Variety and escalation

Model tool selection and optional MCP skills amplify available task action variety; schema registry, max-step limit, workspace confinement and human permission narrow it. Errors return to the model or terminal; no separately evidenced algedonic escalation from S1 into an accountable S3/S4/S5 governance body. Human questions remain ordinary CLI interaction rather than an installed ultimate-policy channel.

## Evidence gaps

- The container does not have `go` installed (`go test ./...` returned `go: command not found`); the first-party Go source/architecture was reviewed without an executable local test result.
- No configured real provider credentials or MCP server were exercised, and externally operated inference/tool correctness is not independently verified. S1 credit rests on the installed first-party wiring and closed loop in pinned source.
- A future multi-agent composition or external auditor could add other VSM functions; such hypothetical capabilities are not assigned to this frozen standard distribution.
