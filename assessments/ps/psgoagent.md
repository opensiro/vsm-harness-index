---
harness_id: psgoagent
project_name: PSGoAgent
repository: https://github.com/nakasyou/power-agent
review_ref: a258539983e3ffbcb04f7762d73f98b67940e5b8
reviewed_at: 2026-10-31
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

# PSGoAgent

## Review boundary

- System in focus: The shipped PowerShell PSGoAgent coding-agent runtime, module and standalone release entrypoint at the frozen commit.
- Purpose and identity: Let one model-driven coding assistant inspect, edit and run PowerShell commands in a selected workspace, with user-selected permissions and persistent sessions.
- Relevant environment: User prompts, workspace files, shell processes, model provider APIs, MCP tools, local instructions/skills and operator approvals.
- Standard-distribution boundary: `Start-GoAgent.ps1`/standalone `Power-Agent.ps1` command modes and importable `PSGoAgent` module, seven built-in tools, `Invoke-GoAgent`, session serialization, tool permissions, optional MCP/web-search and streaming protocols.
- Credited operating / distribution surfaces: `PSGoAgent.psm1`, `Tools.ps1`, `Streaming.ps1`, `Console.ps1`, `Start-GoAgent.ps1`, `PSGoAgent.psd1` and supported release bundling.
- Adjacent first-party surfaces excluded from ownership: Unit tests, build/release GitHub workflows, updater scripts, documentation and provider implementations are not extra runtime VSM actors.
- First-party operating / deployment modes considered: Interactive TUI, plain/headless `-Prompt`, module API, `Ask`, `Auto`, `ReadOnly`, supported provider protocols and optional MCP; persisted session resume without persisted approvals/credentials.
- Recursion level: One coding-agent session as the operating whole; a selected local project is its environment rather than a governed multi-agent team.
- Reviewed revision: `a258539983e3ffbcb04f7762d73f98b67940e5b8`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`New-GoAgent` creates model/transport/tool/permission/session state. `Invoke-GoAgent` sends the current conversation and tool schemas to the provider, parses the model's tool calls, runs `Invoke-GoTool` with validated arguments and permission checks, stores correlated tool results and re-enters the model until a final answer or turn budget. Tools include workspace-confined read/search/write/edit and a separately spawned PowerShell command process; provider/API calls stream through `Streaming.ps1`. Completed exchanges persist for resume. MCP connectors and a provider-native web-search tool can extend the operating S1 tool set. See [agent loop](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/PSGoAgent.psm1), [tool runner](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/Tools.ps1), [design](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/docs/design.md), [README](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/README.md).

## Operational model

The external LLM chooses coding actions, while the PowerShell runtime validates and executes them and feeds back results. `Ask` mode requires operator confirmation for mutations, but the model still selects what to request; `Auto` runs within the same schemas without an approval round, and `ReadOnly` limits actions. Resume preserves model history but not operator authority. Retry, cancellation, streaming, session persistence and version upgrade are runtime support and maintenance rather than autonomous organization-level decisions.

## S1 — Operations

- State: A
- Function: A model-backed coding agent pursues a user's software task by choosing workspace inspection, edits and command/tool invocations.
- Disturbance / variety regulated: Unknown code and directory structure, search results, tool errors, test feedback, failed edits and new user instructions.
- Decisive decision or feedback right: Determine next response and tool name/arguments after each returned result, or stop with final answer.
- Decision owner: Configured LLM acting through the first-party PowerShell model/tool loop; human supplies the overall request and selects permission policy.
- Supporting / enforcement mechanisms: Seven Pi-style tools, JSON-schema validation, workspace path guards, permission callback, SSE parser, tool result truncation, retries, persisted history and MCP adapters.
- Closure path: User prompt/history → LLM tool choice → `Invoke-GoTool` validation/execute or deny → correlated tool result appended to history → subsequent model choice.
- Boundary reachability: `Invoke-GoAgent` in the public module and CLI invokes this loop; both user-confirmed `Ask` and autonomous-on-tool-authorization `Auto` modes are supported and documented.
- Why this is / is not agent-owned: Removing the model removes open-ended choice of which files and commands to inspect or change. Operator approval in `Ask` is a per-action boundary, not the origin of the model's task reasoning.
- Evidence: [agent](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/PSGoAgent.psm1), [tools](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/Tools.ps1), [design](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/docs/design.md).
- Basis: structural.
- Confidence: high.
- Caveats: Model quality, live account/API availability and permission prompts are not validated end-to-end; PowerShell command tool is not OS-sandboxed.

## S2 — Coordination

- State: —
- Function: No first-party S2-specific regulation among multiple distinct operational agents is shipped.
- Disturbance / variety regulated: Concurrent file mutation and user input could interfere, but only one active model turn per agent is supported.
- Decisive decision or feedback right: No agent-to-agent conflict diagnosis, negotiated adjustment or return to multiple S1s is present.
- Decision owner: Deterministic turn serialization and named file mutex; no inter-agent coordinator.
- Supporting / enforcement mechanisms: Reject concurrent turns on the same agent, sequential tool call execution and same-path write/edit mutex.
- Closure path: Concurrency controls prevent collisions, but do not recognize an inter-S1 disturbance and feed an S2-specific resolution into agents' ongoing work.
- Why this is / is not agent-owned: File locking and sequential operation protect integrity, not an autonomous S2 organization of distinct agents.
- Evidence: [agent](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/PSGoAgent.psm1), [tools](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/Tools.ps1), [design](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/docs/design.md).
- Basis: structural.
- Confidence: high.
- Caveats: Separately run agents might coordinate through manually configured MCP or external channels, not a supplied first-party S2 path.

### Absence scope

- Surfaces inspected: Single-agent session loop, tool and file locks, MCP configuration, CLI modes, history and design document.
- Plausible first-party paths checked: Multiple session files, concurrent turns, tool queues, workspace write locks and MCP tool interactions for cross-S1 interference recognition/attenuation.
- Why no material first-party path remains: They prevent races or expose generic tools; no distinct team cells and function-specific coordination feedback are composed.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system discretionary operational management across S1 units is established.
- Disturbance / variety regulated: Request length, model timeout, tool risks, history persistence, provider retries and human changes of model/permission.
- Decisive decision or feedback right: No supervisor assesses whole-agent operating commitments and reallocates cross-unit current priorities.
- Decision owner: The user selects permissions/model/turn budget; deterministic runtime enforces limits, retries or cancellation.
- Supporting / enforcement mechanisms: `MaxTurns`, session save/resume, `/model`, `/permission`, `-TimeoutSeconds`, retry rules and command cancel.
- Closure path: Stop/retry/permission results return to the same S1 session; there is no whole-system current-control managerial intervention.
- Why this is / is not agent-owned: Static limits and per-action human approval have runtime effect but are not independently evidenced S3 organizational judgments.
- Evidence: [agent](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/PSGoAgent.psm1), [streaming](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/Streaming.ps1), [console](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/Console.ps1).
- Basis: structural.
- Confidence: high.
- Caveats: An operator can interrupt the active agent, but no first-party parent S3 multi-cell topology is provided.

### Absence scope

- Surfaces inspected: Agent loop and lifecycle, console controls, protocol switching, permission logic and tool callback.
- Plausible first-party paths checked: Turn ceilings, model switch, cancellation, retry and operator approval for operational-manager decision/returned revised commitments.
- Why no material first-party path remains: All apply to a single task stream or execute preselected policy; no current whole-system S3 discretion is constructed.

## S3* — Complementary audit

- State: —
- Function: No independent complementary audit of the model's ordinary coding claims and corrective return is shipped.
- Disturbance / variety regulated: Incorrect edits, false test-success claims, missing command results and inconsistent session records.
- Decisive decision or feedback right: No separate auditor can independently challenge a completion claim and direct a corrective control decision.
- Decision owner: Same operating model may run tests and inspect results; user can read transcripts, but no independent runtime auditor is composed.
- Supporting / enforcement mechanisms: Validated edit diffs/patches, tool output logging, session history, tests and provider result checks.
- Closure path: Tool results feed the same S1 model; test suites run in project development, not as a complementary live audit-to-S3 path.
- Why this is / is not agent-owned: A well-documented operation and another tool observation are not S3* without independently owned challenge and returned correction.
- Evidence: [tools](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/Tools.ps1), [design](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/docs/design.md), [tests](https://github.com/nakasyou/power-agent/tree/a258539983e3ffbcb04f7762d73f98b67940e5b8/tests).
- Basis: structural.
- Confidence: high.
- Caveats: External reviewers may examine session files outside the assessed product.

### Absence scope

- Surfaces inspected: Tool receipts, edit patch output, logging, model response validation, user history and tests.
- Plausible first-party paths checked: Transcript replay, bounded tool output, saved diffs and user approvals for independent evidence access/audit authority/corrective return.
- Why no material first-party path remains: These are ordinary agent operations, safety validations and development tests, not a runtime complementary auditor.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective capability-adaptation loop for the coding-agent harness is supplied.
- Disturbance / variety regulated: New provider availability, future project requirements, missing tools and changes to agent implementation.
- Decisive decision or feedback right: No deployed agent evaluates environmental trends and chooses enduring harness capability updates from them.
- Decision owner: User/developer chooses provider/model/installed skills and explicitly runs upgrade; external release maintainers publish newer binaries.
- Supporting / enforcement mechanisms: Session history, global/local instructions/skills, model switching, optional MCP/web tools and release updater.
- Closure path: Context informs current response; an upgrade downloads a human-published release with checksum and replaces the script, not an agent-generated future-adaptation decision.
- Why this is / is not agent-owned: Changing selected models or tools during a session affects S1 operation, and static release installation is maintenance rather than S4 intelligence.
- Evidence: [agent](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/PSGoAgent.psm1), [updater](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/Upgrade.Core.ps1), [README](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Agent may propose code changes during a user task; no source-wired ongoing capability-selection/deployment loop is shown.

### Absence scope

- Surfaces inspected: Session learning/history, skill and instruction loading, provider/permission changes, MCP, updater and release process.
- Plausible first-party paths checked: Persistent experience, dynamic model selection, auto-upgrade, plugin discovery and coding its own project for external/future distinctions and adopted new capability.
- Why no material first-party path remains: Paths are current task context, human-driven settings or external software release maintenance; no shipped S4 design/decision/return loop remains.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy adjudication-and-return path is implemented for the coding agent.
- Disturbance / variety regulated: Trust of shell commands, file write authorization, provider authentication, user constraints and workspace identity.
- Decisive decision or feedback right: Human sets `Ask`/`ReadOnly`/`Auto` policy and approves individual actions, but no legitimacy-level identity issue is raised, resolved and returned.
- Decision owner: Local human/operator and static code; S1 model operates within selected policy.
- Supporting / enforcement mechanisms: Tool allowlist, permission callback, workspace boundaries, key hygiene, resumptions resetting to `Ask`, and command approval.
- Closure path: Approve/deny changes one tool outcome; no identity or ultimate-policy ruling is embedded in a subsequent governed operation.
- Why this is / is not agent-owned: Per-command permission and safety do not become S5 solely due to human authority.
- Evidence: [permissions and agent](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/PSGoAgent.psm1), [tools](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/Tools.ps1), [README](https://github.com/nakasyou/power-agent/blob/a258539983e3ffbcb04f7762d73f98b67940e5b8/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Operator can change restrictions or instructions, but there is no evidenced policy-level parent feedback channel.

### Absence scope

- Surfaces inspected: Permission modes, approval callback, AGENTS/skills, model/provider settings, CLI commands and persisted session rules.
- Plausible first-party paths checked: Ask-mode approvals, ReadOnly/Auto switches, model change, skill selection and external account policy for S5 issue/ultimate ruling/operating return.
- Why no material first-party path remains: They control actions/configuration, not a legitimate ultimate-policy resolution function.

## Distributed OSS parent arrangement

Distributed contributors build and release a PowerShell program. There is no first-party visibility or decision return connecting independent local agent sessions into an organization-level S3/S4/S5 metasystem; maintainer releases are not the local runtime's adaptation judgment.

## Self-hosted and non-human modes

The local PowerShell client can use external cloud APIs, a local compatible endpoint or different providers. In `Auto` mode the model chooses allowed actions without a human confirmation per tool; `Ask` mode retains model choice but requires a human permission gate; `ReadOnly` permits only observational S1 actions. Shell commands run with user permissions, so these ownership claims imply no sandbox or safety guarantee.

## Recursion

One session has an agentic S1 action loop with history and tool feedback. Multiple saved sessions and plugin tool endpoints do not establish nested viable organizations or higher operational metasystems.

## Variety and escalation

Tool schemas, workspace guards, truncation and `MaxTurns` attenuate action variety. User approvals and cancellation gate risky actions, while failed tool results return to the same model to choose another step. Retries and streaming preserve continuity but do not create higher organizational authority.

## Evidence gaps

Static pinned source; PowerShell was not executed and paid provider or live MCP endpoints were not contacted. The README documents mock/integration tests but this assessment does not treat them as a real account trial. No unshipped autonomous S2–S5 feature is assumed from the coding-agent label.
