---
harness_id: gsh
project_name: gsh
repository: https://github.com/kuangxing6367/gsh
review_ref: d5d1c6160b24430b80d78f7e135bc28040faa287
reviewed_at: 2026-11-04
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

# gsh

## Review boundary

- System in focus: `gsh`, a Go plugin-based conversational agent harness at its single-process CLI/Web/TUI and embeddable `harness.Harness` boundary.
- Purpose and identity: Execute user-selected local or configured remote shell/file tasks through a model-decided tool loop, preserving sessions and bounded permissions.
- Relevant environment: User instructions, local workspace and optional remote nodes, tool results, external model endpoints, permission decisions, and persisted conversation/audit files.
- Standard-distribution boundary: The pinned Go binary and reusable package, with default `session → tools → llm → loop → web → ui` plugins and configured `echo` or OpenAI-compatible model transport.
- Credited operating / distribution surfaces: [main.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/main.go), [harness/harness.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/harness/harness.go), [internal/loop/loop.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/loop/loop.go), [internal/tools/](https://github.com/kuangxing6367/gsh/tree/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools), [internal/session/session.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/session/session.go) and [internal/web/server.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/web/server.go).
- Adjacent first-party surfaces excluded from ownership: Repository development/test suite, VitePress documentation generation, external DSH architectural inspiration, independently hosted models, user-operated SSH nodes, consumer compositions embedding the Go package, and later projects using its plugin API.
- First-party operating / deployment modes considered: Headless `-e`, REPL, TUI, Web chat/SSE, session resume/fork/replay, embeddable `Run`/`Serve`; configured remote-node execution and permission levels; `echo` offline diagnostic versus external OpenAI-compatible inference.
- Recursion level: One configured gsh process and its task/session interactions; external remote hosts and unrelated concurrent gsh processes are environment, not subordinate autonomous S1 organizations.
- Reviewed revision: `d5d1c6160b24430b80d78f7e135bc28040faa287`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`main.go` constructs a `Harness`, loads the default plugins and selects headless, REPL, TUI or HTTP operation. The reusable package composes session, tool, model, loop and interface services using a plugin kernel. The `agentLoop` sends the persisted conversation plus registered tool schemas to the model; it executes each model-requested tool through the central registry, appends tool results and repeats up to 24 model turns. The session store writes append-only JSONL and supports open/fork/replay. The registry applies a configured permission guard, optional TUI per-call human approval and workspace restrictions, and writes redacted execution metadata to a separate audit log. The Web API manages sessions, workspace, permission settings and cancellation of individual active chat requests. The model is an injected echo diagnostic or external OpenAI-compatible endpoint, not a first-party trained model. [README](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/README.md), [harness](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/harness/harness.go), [loop](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/loop/loop.go), [tools](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools/tools.go), [Web API](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/web/server.go).

## Operational model

The operational S1 unit is the model-driven task/session loop: it selects tools and observes their results to satisfy the user's request. Multiple user sessions can coexist in Web mode, but no built-in autonomous subagent or independent task-unit organization is wired. The runtime selects the plugin set and enforces permissions, turn limits, path rules and audit persistence; it does not decide which substantive tool steps achieve the task. A human supplies the request, may choose global permission level or confirm TUI tool actions, and may cancel a run. These interventions are local operational authority and do not independently establish S3/S4/S5 governance.

## S1 — Operations

- State: A
- Function: Repeated model-selected workspace/remote actions in response to observed tool feedback until a final answer.
- Disturbance / variety regulated: Unknown repository or host state, tool failures, changing task details and model/tool protocol outcomes.
- Decisive decision or feedback right: Choose which registered tool to call with what arguments, interpret returned content and decide the next step or final answer.
- Decision owner: The external-inference-backed agent working through gsh's first-party `agentLoop`; deterministic guard and human optional approval can refuse actions but do not select the task solution.
- Supporting / enforcement mechanisms: Plugin registry, JSON tool specifications, tool execution dispatcher, session JSONL, permission guard, human approval, audit log, turn cap and shell/workspace restrictions.
- Closure path: User message → model `Chat` with tool list → model `ToolCalls` → `registry.Execute` → tool result appended as `RoleTool` → another model call or final answer; aborts with a bounded error after 24 rounds.
- Boundary reachability: `main.go` and `harness.Run`/`RunHeadless`/`RunREPL`/`RunTUI` reach the same shipped `Loop` service. Configured OpenAI-compatible inference uses the tool-call protocol; echo is only a deterministic diagnostic mode.
- Why this is / is not agent-owned: The model's proposed tool and next-turn choice determine the substantive task trajectory; the Go loop implements its feedback/action channel rather than substituting a deterministic task script.
- Evidence: [loop.go#L35-L137](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/loop/loop.go#L35-L137), [llm.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/llm/llm.go), [tools.go#L343-L405](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools/tools.go#L343-L405), [main.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/main.go).
- Basis: explicit + structural
- Confidence: high for the installed agent/tool/feedback path; not a claim about model success rate.
- Caveats: No live external provider was exercised here; `echo` is not independent evidence of autonomous model capability.

## S2 — Coordination

- State: —
- Function: No demonstrated first-party attenuation of a specific interference or oscillation between distinct autonomous S1 units.
- Disturbance / variety regulated: Multiple Web sessions and configured remote nodes may contend externally, but this distribution exposes them as sessions/execution targets, not a coordinated multi-agent S1 organization.
- Decisive decision or feedback right: Select a corrective inter-unit relation for competing S1 agents and return coordination feedback to both; no such built-in path established.
- Decision owner: A model chooses tools in its own session; session IDs and Web request routing are deterministic transport.
- Supporting / enforcement mechanisms: Session-specific JSONL, `RunSession` selection, Web per-run cancellation map and shared workspace configuration.
- Closure path: Each session receives its own model/tool feedback; no distinct inter-S1 conflict → coordination decision → changed future behaviour path is implemented.
- Why this is / is not agent-owned: Session isolation, remote-node selection and tool sequencing do not by themselves establish a function-specific S2 witness.
- Evidence: [loop.go#L48-L87](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/loop/loop.go#L48-L87), [web/server.go#L248-L328](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/web/server.go#L248-L328), [session.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/session/session.go).
- Basis: structural
- Confidence: medium-high at the declared process/session boundary.
- Caveats: A host application could compose independent agents with separate coordination, but that actor is not shipped here.

### Absence scope

- Surfaces inspected: Plugin registration, `RunSession`, session fork/list/open, Web chat/stop, remote node configuration, TUI and README architecture.
- Plausible first-party paths checked: Multi-session state, per-run dispatch, shared workspace/permission settings, SSH node targeting and session forking.
- Why no material first-party path remains: None establishes two independent task-owning S1 cells together with a conflict-attenuating decision and returned inter-unit adjustment.

## S3 — Inside-and-now control

- State: —
- Function: No separate whole-system current-control discretion regulating multiple autonomous task commitments at this recursion.
- Disturbance / variety regulated: Tool risk, working directory scope, concurrent Web requests and task cancellation are bounded by fixed operator/runtime rules.
- Decisive decision or feedback right: Allocate or revise current cross-cell resources, priorities, commitments or interventions based on a whole-system operating view; not wired as a distinct S3 decision path.
- Decision owner: Human selects task/permission mode and individual stop; runtime applies configured guard; model decides local task steps.
- Supporting / enforcement mechanisms: Web session listing, current permission display, `Guard.Set`, per-run `CancelFunc`, turn cap, workspace guard and tool audit records.
- Closure path: User changes a permission tier or stops an individual run and subsequent tools are permitted/blocked or cancelled; no whole-system diagnosis → current-control decision over an operational portfolio → returned cross-unit regulation is established.
- Why this is / is not agent-owned: A global permission switch and stop button are operational controls/enforcement; there is no evidenced whole-system control decision owner, autonomous or closed parent-governed, at the assessed boundary.
- Evidence: [web/server.go#L130-L151](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/web/server.go#L130-L151), [web/server.go#L311-L328](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/web/server.go#L311-L328), [web/server.go#L547-L582](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/web/server.go#L547-L582), [perm.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools/perm.go).
- Basis: structural
- Confidence: medium at the chosen single-process recursion.
- Caveats: The Web UI exposes operator control, but the code does not establish it as a first-party S3 whole-current parent loop.

### Absence scope

- Surfaces inspected: Web state/sessions, stop/settings/permission APIs, tool guard and approval, runtime cap and kernel services.
- Plausible first-party paths checked: Global permission-tier changes, session activity display, per-run cancellation, workspace settings and model/tool errors.
- Why no material first-party path remains: These are directly requested local constraints/interventions without an evidenced whole-system current view plus an accountable discretionary resource/commitment feedback loop over distinct S1 units.

## S3* — Complementary audit

- State: —
- Function: No independent complementary operational-reality audit with corrective returned ownership is wired into the standard runtime.
- Disturbance / variety regulated: Tool execution errors and permission denials are logged for inspection; the same registry records ordinary events.
- Decisive decision or feedback right: Independently sample reality, challenge a running unit's claim and feed an audit finding into corrective current control; not supplied.
- Decision owner: Tool registry synchronously records its own execution metadata; a future human could read records but no first-party independent auditor is designated.
- Supporting / enforcement mechanisms: `AuditLog.Record` append-only metadata, `Recent`, Web `/api/audit` and session trajectory replay.
- Closure path: Registry executes/refuses a tool and logs its own result; no independent observation/verdict is automatically returned to a separate corrective control function.
- Why this is / is not agent-owned: A file named audit and ordinary telemetry are not an S3* actor or sufficiently independent complementary-access decision.
- Evidence: [audit.go#L17-L113](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools/audit.go#L17-L113), [tools.go#L343-L405](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools/tools.go#L343-L405), [web/server.go#L508-L528](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/web/server.go#L508-L528).
- Basis: explicit + structural
- Confidence: high for the distinction between logging and independent audit.
- Caveats: Records might be consumed by an external auditor, which is outside this standard distribution.

### Absence scope

- Surfaces inspected: Audit log creation/capture/retrieval, session replay, Web audit endpoint, tool execution and TUI approval.
- Plausible first-party paths checked: Independent audit log versus session transcript, recent audit view, execution error return and operator review.
- Why no material first-party path remains: Both logs originate in the ordinary executor; there is no independent direct-reality sampling, auditor judgment or returned corrective audit-to-control path.

## S4 — Outside-and-then intelligence

- State: —
- Function: No separately closed external/future intelligence and strategic adaptation loop in the shipped gsh runtime.
- Disturbance / variety regulated: A model can react to new host facts inside the present task; configuration and skill discovery can change tool exposure but do not form a prospective change decision.
- Decisive decision or feedback right: Select future capability adaptations from external prospects and return them to present organizational operation; no such path is established.
- Decision owner: Developer/operator configures plugins, remote nodes, providers and skill directory; model chooses current task tool actions.
- Supporting / enforcement mechanisms: Plugin kernel, configurable tool list, on-demand skill loading, model provider switch and history replay.
- Closure path: Current tool/skill info may shape subsequent task turns; no outside-and-then option generation/selection leads to an accountable later capability change.
- Why this is / is not agent-owned: Plugin extensibility and local replanning are S1 execution support, not an externally prospective adaptation right.
- Evidence: [kernel.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/kernel/kernel.go), [tools.go#L155-L279](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools/tools.go#L155-L279), [skills.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools/skills.go), [loop.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/loop/loop.go).
- Basis: structural
- Confidence: medium-high within the pinned supported distribution.
- Caveats: A consuming project might independently build evolutionary agent infrastructure on the generic kernel.

### Absence scope

- Surfaces inspected: Model/loop, plugin lifecycle, skills, provider configuration, session persistence, README and Web settings.
- Plausible first-party paths checked: Dynamic tool loading, per-task tool choice, skills, provider configuration and session fork/replay.
- Why no material first-party path remains: These support current work or user-specified configuration; no first-party prospective environmental evaluation generates and returns a strategic change in current capability.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy deliberation and closed authoritative return path at this process recursion.
- Disturbance / variety regulated: Unsafe shell/file actions and workspace escape are checked against preselected permission/security rules.
- Decisive decision or feedback right: Adjudicate identity-level or ultimate-policy tensions and return an authoritative change that governs later operation; not supplied.
- Decision owner: Maintainer/operator establishes config and permission levels; registry applies rules. Human TUI prompt authorizes a specific risky tool, not enduring ultimate policy.
- Supporting / enforcement mechanisms: Permission guard, always-allow runtime toggles, shell safety blocklist, workspace restriction, audit and Web permission switch.
- Closure path: Per-action approval or operator tier change affects subsequent tool execution; no first-party identity/policy matter reaches legitimate ultimate authority and returns as a governing policy resolution.
- Why this is / is not agent-owned: Fixed safety constraints and a user approval gate do not own an identity-level organizational discretion; no S5 parent-mode loop is wired.
- Evidence: [perm.go](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools/perm.go), [tools.go#L299-L405](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/tools/tools.go#L299-L405), [web/server.go#L560-L582](https://github.com/kuangxing6367/gsh/blob/d5d1c6160b24430b80d78f7e135bc28040faa287/internal/web/server.go#L560-L582).
- Basis: structural
- Confidence: medium-high for bounded absence.
- Caveats: Operator/maintainer authority over a different organization is not part of the assessed process.

### Absence scope

- Surfaces inspected: Tool permission modes, TUI approval, security checks, Web settings, plugin configuration and README.
- Plausible first-party paths checked: Safety-mode changes, operator approvals, plugin policy changes and remote-node configuration.
- Why no material first-party path remains: All cited paths constrain or authorize operational tools; no identity/ultimate-policy issue, legitimate decision and durable return-to-operation closure is provided.

## Distributed OSS parent arrangement

The public repository has a maintainer and implementation tests, but those development actors are not a wired parent governing each shipped run. Locally operator-controlled permissions and task instructions are not credited as an organization-level S3/S4/S5 parent mode.

## Self-hosted and non-human modes

The headless, REPL, TUI, Web and embedded modes share the same single-agent core, while operators may change execution permissions. No distinct autonomous S3/S4/S5 mode or complete parent-governed alternative is established by these operational interface choices.

## Recursion

Session fork creates a conversation copy and remote node execution targets a host; neither creates a separately viable S1 recursion with its own full metasystem. No autonomous subagent hierarchy is implemented in this pinned default plugin composition.

## Variety and escalation

Tool schemas, remote-node selection, skill lookup and plugin extensibility amplify the task's action repertoire. Permission levels, workspace boundaries, turn limits and approval attenuate risk. Errors and stop events are ordinary task feedback; without exceptional routing to an established authority they are not independent algedonic or S3/S5 evidence.

## Evidence gaps

- Go toolchain is unavailable in the reviewing environment; pinned upstream `go test ./...` was not run. Source-path and bundled unit-test review can establish architecture but not live runtime reliability.
- No real provider credentials or external model run were exercised; statements about agent-owned model decisions concern the implemented supported tool-call path, not benchmarked performance.
- Potential consumer-created multi-agent coordination, independent audit and strategic/policy governance are deliberately outside the default shipped gsh boundary.
