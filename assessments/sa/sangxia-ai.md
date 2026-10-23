---
harness_id: sangxia-ai
project_name: Sangxia.ai
repository: https://github.com/EthanYin-0701/sangxia-ai
review_ref: f38f484d8c7f15f6937d5da553d9c25ef1953daf
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Sangxia.ai

## Review boundary

- System in focus: one locally operated Sangxia.ai coding-agent session, its first-party ACP/TUI entry points, model/tool loop, project initialization, project memory, local hooks, persistence and optional MCP/skill tools at the pinned source revision.
- Purpose and identity: help a developer inspect and modify a project through an ACP-compatible coding assistant using an OpenAI-compatible model provider.
- Relevant environment: a user's source tree, terminal/editor/TUI, external LLM API, optional MCP servers, local skill files and project-specific instructions.
- Standard-distribution boundary: the packaged Node/TypeScript agent and its first-party ACP/TUI modes; the editor client and LLM provider are external participants, not additional first-party governing agents.
- Credited operating / distribution surfaces: `src/index.ts`, `src/agent.ts`, `src/harness/*`, `src/tools/*`, `src/project-memory.ts`, `src/persistence.ts`, `src/hooks/*`, `src/tui/*`, and packaged setup/configuration paths.
- Adjacent first-party surfaces excluded from ownership: maintainer GitHub/CI/release work, documentation and proposals, development-only fake model/ACP smoke fixtures, and external editor/MCP/provider implementations; they were considered as boundary evidence but cannot independently close a runtime VSM function.
- First-party operating / deployment modes considered: editor-mediated ACP over stdio; first-party local TUI bridging ACP; `confirm` and `auto` tool permission modes; optional hooks, MCP, skill, user-memory and project-memory configuration; initial project-memory initialization accepted or skipped by the operator.
- Recursion level: the one installed coding-assistant session working in one project; tool calls, subturns, UI plans and external MCP services are not presumed independent S1 organizations.
- Reviewed revision: `f38f484d8c7f15f6937d5da553d9c25ef1953daf`.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `SangxiaAgent` ACP service creates/restores sessions, assembles builtin tools plus optional MCP and skills, and delegates prompt turns to `runTurn`. The loop streams model output, validates calls, checks permission and optional pre/post-tool hooks, executes file/terminal/plan tools, appends results to persisted conversation state and continues until final response, failure, cancellation or iteration bound. `src/tui/*` is a first-party local interface to the same agent, not a second autonomous worker. Sessions are serialized per ID and persisted in JSONL form; the runtime can repair an interrupted tool-call history without pretending its side effects are known.

The noteworthy longitudinal mechanism is project initialization: for missing `AGENTS.md` or `.sangxia/memory.md`, the agent asks the operator whether and where to initialize. If permitted, the *model* performs a dedicated bounded investigation/edit subturn with read/list/search/write tools and a prompt to synthesize project rules, architecture, decisions and TODO context. It then rebuilds the live system prompt from the durable files; new sessions load that project memory as well. A separate user-level instruction file may also be loaded but is not generated autonomously. Hook commands are external user-defined programs: they can deny, request approval, modify arguments or inject context, but no shipped independent auditor is constituted by that extensibility alone.

Primary source: [`src/agent.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/agent.ts), [`src/harness/loop.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/harness/loop.ts), [`src/project-memory.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/project-memory.ts), [`src/hooks/index.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/hooks/index.ts).

## Operational model

The S1 unit is the model-guided, tool-using coding agent. Human operator and ACP client supply requests and permission decisions; provider supplies inference and MCP servers supply optional tools. The first-time project-initialization subturn is still one session's S1 work, but its output is deliberately aimed at the *capabilities of later work*, forming a separate prospective adaptation function. A visible task plan, session cancellation, fixed iteration caps and hook approvals do not by themselves constitute inter-S1 coordination, whole-organization resource governance, independent audit or identity-level policy.

## S1 — Operations

- State: A
- Function: interpret a developer request, inspect/edit files, invoke tools and return a coding outcome.
- Disturbance / variety regulated: variable repository structure, requested edits, tool errors, model errors, path/permission constraints and interrupted sessions.
- Decisive decision or feedback right: select next tool calls and arguments in response to observations and tool results; decide whether further coding iterations are needed.
- Decision owner: the configured model actor in `runTurn`, subject to permission/timeout/hook gates.
- Supporting / enforcement mechanisms: ACP session management, tool registry, input-schema validation, permission prompts, bash/file tools, MCP integration, streamed provider calls, bounded retries and event persistence.
- Closure path: user task → model choice → validated and permitted local tool call → observable tool result in conversation history → model's next work or final answer.
- Boundary reachability: standard ACP and local TUI sessions both call `SangxiaAgent.prompt`, which invokes the shipped model/tool loop with first-party tools.
- Why this is / is not agent-owned: deterministic dispatch enforces calls, but the model chooses operational actions based on returned evidence. The operator can veto protected effects without owning the model's task-step choices.
- Evidence: [`src/agent.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/agent.ts); [`src/harness/loop.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/harness/loop.ts); [`src/tools/index.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/tools/index.ts).
- Basis: direct source tracing and offline fake-provider/ACP executable smoke tests.
- Confidence: high for the shipped decision route.
- Caveats: no real remote model was called; observed execution is structural/mock-backed, not measured coding success under a live provider.

## S2 — Coordination

- State: —
- Function: no shipped inter-S1 disturbance attenuation is established inside this one-session organization.
- Disturbance / variety regulated: possible conflicting edits or resource use among independent agents, but no first-party independent peer/child agent set is operated here.
- Decisive decision or feedback right: none over relations among distinct S1 units.
- Decision owner: the model sequences its own tool calls; the runtime serializes concurrent prompts on the same session.
- Supporting / enforcement mechanisms: `promptInFlight`, tool-call ordering, ACP updates, local `update_plan` display, optional MCP connections.
- Closure path: sequencing protects one session's history; there is no inter-S1 disturbance → coordination judgment → revised independent S1 behavior loop.
- Why this is / is not agent-owned: plan publication and same-session serialization do not coordinate distinct autonomous operating units.
- Evidence: [`src/agent.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/agent.ts); [`src/tools/plan.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/tools/plan.ts); [`src/mcp/client.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/mcp/client.ts).
- Basis: shipped runtime and available tool registry inspection.
- Confidence: high for the declared first-party session boundary.
- Caveats: an outside MCP server or multiple users could independently deploy agents, but that does not make their relations a shipped Sangxia S2 loop.

### Absence scope

- Surfaces inspected: ACP new/load/prompt modes, TUI bridge, builtin/MCP tool assembly, task plan, session state, cancellation and initializer subturn.
- Plausible first-party paths checked: model-planned task steps as S2; concurrent ACP sessions as peer S1; MCP servers as coordinated S1 agents; initialization as delegation.
- Why no material first-party path remains: session-local scheduling/serializing, external tool integration and two consecutive turns provide no cross-S1 owner or disturbance-specific coordinating feedback.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control actor reallocating resources or commitments across a portfolio of S1 activity is established.
- Disturbance / variety regulated: current deadlines, partial tool failures, conversation length and user-approval constraints are handled operationally, without organizational-level current steering.
- Decisive decision or feedback right: no actor owns a distinct cross-operation allocation, priority intervention or accountability return for the declared recursion.
- Decision owner: S1 model chooses its own steps; static caps and permission rules are configured by operator/runtime; client can cancel a session.
- Supporting / enforcement mechanisms: iteration/token/timeouts, abort controller, ACP permission mode, tool plan status and hook command results.
- Closure path: operational attempts continue/stop under gates; no separate whole-organization view → current-control judgment → redirected S1 commitments loop.
- Why this is / is not agent-owned: neither a fixed time budget nor a generic stop/approval UI establishes a VSM S3 decision owner; user permission is per action, not portfolio governance.
- Evidence: [`src/agent.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/agent.ts); [`src/harness/loop.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/harness/loop.ts); [`src/harness/permissions.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/harness/permissions.ts).
- Basis: inspected available resource/permission/current-state decision paths.
- Confidence: medium-high.
- Caveats: operator could supervise a real-world organization with external tooling, but no qualifying parent-governed S3 mode is closed by this runtime itself.

### Absence scope

- Surfaces inspected: agent sessions, TUI, runtime loop, prompts, resource caps, plan tool, hooks, persistence, permissions and cancellation.
- Plausible first-party paths checked: S1 self-scheduling as S3; ACP `cancel`/approval as parent steering; TUI plan as whole-system dashboard; hooks as S3 controller.
- Why no material first-party path remains: each affects a turn, tool or local session without an owner that sees and steers the current commitments of multiple S1 operations at this recursion.

## S3* — Complementary audit

- State: —
- Function: no separate complementary audit path checks S1 claims with a distinguishable owner and returned findings.
- Disturbance / variety regulated: undetected tool errors, unsafe actions and defective edits could benefit from audit, but the shipped hooks are general user-defined instrumentation/gates.
- Decisive decision or feedback right: no first-party independent or complementary auditor decides the validity of S1 reports.
- Decision owner: external user-supplied hook scripts may deny or annotate calls; Sangxia executes and reports them without supplying a separate audit role/evidence path.
- Supporting / enforcement mechanisms: `pre_tool_use`, `post_tool_use`, lifecycle hooks, exit-code/error policies, command invocation and context injection.
- Closure path: hooks may block a tool or feed diagnostics into the same model loop; there is no first-party separate claims-audit → finding → mandated correction path.
- Why this is / is not agent-owned: a configurable program hook is a usable sensor or gate, not proof that an auditor actor, complementary access and sustained review right are shipped.
- Evidence: [`src/hooks/index.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/hooks/index.ts); [`src/hooks/types.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/hooks/types.ts); [`src/harness/loop.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/harness/loop.ts).
- Basis: inspected hook registry and tool integration.
- Confidence: medium-high for stock/optional shipped configurations.
- Caveats: an operator could write a reviewer as a hook, but that unobserved external composition cannot be credited as first-party S3*.

### Absence scope

- Surfaces inspected: pre/post-tool hooks, session lifecycle events, mock smoke hooks, ACP updates, model/tool results, project memory and source-test wiring.
- Plausible first-party paths checked: hooks as independent audit, `post_tool_use` diagnostic feedback as verifier, tool-result checking as S3*, Git/test commands as reviewer.
- Why no material first-party path remains: no separate audit owner/access path or specific claim-validation contract is supplied; callbacks are operator-defined and regular tool results return through the same S1 path.

## S4 — Outside-and-then intelligence

- State: A
- Function: inspect the project environment and autonomously synthesize durable project guidance for future coding-agent operation.
- Disturbance / variety regulated: missing/stale project-specific knowledge about architecture, conventions, commands and decisions that would otherwise make later coding sessions start without appropriate context.
- Decisive decision or feedback right: choose which inspected repository facts, working rules, architectural distinctions, decisions and TODOs become future project instruction/memory content.
- Decision owner: the configured model actor running the dedicated project-initialization subturn; human only grants/skips initialization and may choose the scan boundary.
- Supporting / enforcement mechanisms: missing-file detection, explicit ACP operator permission request, scoped init prompt, read/list/glob/grep/write tool restriction, 12-iteration cap, durable `AGENTS.md` and `.sangxia/memory.md`, and `systemPrompt()` reload of project instructions.
- Closure path: missing project instructions at the start of work → operator enables initialization → model inspects README/source/config and develops specific long-lived guidance → writes project memory files → live system prompt rebuild → later/new sessions load that guidance and change their coding context.
- Boundary reachability: `SangxiaAgent.prompt()` invokes `maybeInitializeProject` before the requested work on the standard ACP/TUI route; its model-directed `runTurn` produces durable project files, then `systemPrompt` loads them from the same workspace.
- External distinction: actual user project source, documentation, config, directory layout and optionally permitted parent-directory context outside the Sangxia runtime.
- Future / prospective distinction: persisted instructions are explicitly designated as long-term project memory for later tasks and loaded at session start, rather than produced merely as an immediate answer.
- Adaptation option generated: the model selects and writes rules/technical-stack conventions to `AGENTS.md` plus background/status/decisions/TODO knowledge to `.sangxia/memory.md` after examining the project.
- Path back into current capability / S3: the initializer replaces the session system-prompt content via `systemPrompt(session, initRoot)` and persists it; `newSession` and relevant reload paths take project memory into coding-agent context, changing later operating guidance.
- Why this is / is not agent-owned: the parent approves initiation and scope, but neither static initialization prompt nor file writer determines project-specific judgments. The model owns their synthesis and the files alter subsequent agent context without a second parent adoption decision. An independent parent-governed adaptation mode is not established from a simple yes/no initiation gate.
- Evidence: [`src/agent.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/agent.ts); [`src/project-memory.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/project-memory.ts); [`src/tools/fs-tools.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/tools/fs-tools.ts).
- Basis: traced shipped first-use initializer, model/tool capabilities, subsequent in-memory prompt rebuild and durable read path; fake-provider smoke evidence covers neighboring runtime behavior, not real model guidance quality.
- Confidence: medium-high for ownership/reachability; effect on downstream success is unmeasured.
- Caveats: bounded to user-consented, first-time missing-file initialization; not evidence of continuous external scanning, self-redesign or measured strategic success. Session restoration retains its saved system message except session-start hook additions, so the strongest guaranteed later-read path is a new session; do not infer live re-scan on every resumed session.

## S5 — Policy and identity

- State: —
- Function: no ultimate purpose/identity policy loop governing the assistant as an organization is evidenced.
- Disturbance / variety regulated: credentials, tool access and operator risk tolerance are handled as authentication or local effect permissions rather than ultimate institutional policy disputes.
- Decisive decision or feedback right: no first-party S5 authority adjudicates competing mission/purpose/identity claims and returns binding policy changes.
- Decision owner: human chooses access mode, configures provider and accepts/rejects tool and initialization prompts; maintainers own upstream source externally.
- Supporting / enforcement mechanisms: ACP `authenticate`, `confirm`/`auto` modes, per-tool remembered allowances, hook `deny`/`ask` behavior and system instructions.
- Closure path: tactical permission and authentication gates affect a call/session, but no ultimate-policy issue → authorized identity decision → durable operational return is formed.
- Why this is / is not agent-owned: a token check, user approval or stable system prompt is not by itself the final identity/policy governing function.
- Evidence: [`src/agent.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/agent.ts); [`src/harness/permissions.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/harness/permissions.ts); [`src/config.ts`](https://github.com/EthanYin-0701/sangxia-ai/blob/f38f484d8c7f15f6937d5da553d9c25ef1953daf/src/config.ts).
- Basis: traced authentication, configuration and policy/permission decision paths.
- Confidence: medium-high.
- Caveats: a larger human organization may have its own S5 outside this installed-agent boundary; repository maintainer activity is not attributed to a running session.

### Absence scope

- Surfaces inspected: session/auth/config, role/system prompt, hooks and permissions, memory, TUI controls, packaged distribution and maintainer-facing source files.
- Plausible first-party paths checked: API key as identity policy, parent tool approvals as S5, user project `AGENTS.md` as constitutional authority, repository maintainer governance as distributed S5.
- Why no material first-party path remains: all returned judgments concern access to an operation, user project instructions or an external development process; none supplies a legitimate runtime owner and closed identity-level policy return for the system in focus.

## Distributed OSS parent arrangement

The public repository has contributors and maintainer workflows, but no first-party shared metasystem binding separately installed Sangxia sessions into one operationally governed collective is evidenced. Operator approval is local to an ACP session; project governance must not be imported from adjacent upstream GitHub processes.

## Self-hosted and non-human modes

The packaged assistant is run locally with either the editor ACP client or Sangxia TUI and with `confirm` or `auto` permissions. In both, the coding action loop and project-guidance synthesis are model-owned. The operator's one-off consent for initialization or individual tool edits is not separately sufficient to claim parent-governed S3/S4/S5.

## Recursion

The initializer's limited model subturn, task-planning steps, MCP tool integrations and project-scoped memory all operate within the same local coding-agent organization. They do not independently establish a child S1 organization or a new recursion-level metasystem.

## Variety and escalation

Tool errors, hook denials, provider responses and interrupted history feed the model's next operational choice. The initializer attenuates future workspace-context variety by encoding architecture and conventions into durable files. Permissions and cancellation may stop harmful operations; this is tactical enforcement, not separate S3/S5 ownership.

## Evidence gaps

- The repository was checked out at the frozen commit. `npm ci --ignore-scripts`, TypeScript typecheck, and production build passed under Node 24.19.0. Native offline/mock smoke runs passed for ACP file edit, auth (15 cases), MCP, fake OpenAI endpoint, skills, setup, TUI (66 assertions), hooks (89 assertions), and reliability (41 groups). No real provider/LLM execution was attempted.
- The reliability smoke's cancellation assertion failed in one earlier concurrent execution but passed in an isolated retry; no repeatable functional failure was established. Initial sandbox-constrained smoke attempts were rerun with local subprocess/loopback permissions and passed.
- S4 tests and source establish a reachable decision/return design, not that a real model creates correct project guidance or improves later task success; that outcome requires a separate real-model experiment.
- Optional user-provided hook programs, MCP servers and editor processes may add capabilities outside the first-party assessed boundary; no such external composition is treated as shipped internal S2/S3/S3*/S5 authority.
