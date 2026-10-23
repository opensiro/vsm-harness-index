---
harness_id: arkex
project_name: arkex
repository: https://github.com/attrition-tech/arkex
review_ref: 0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8
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
autonomy_s4: —
autonomy_s5: —
---

# arkex

## Review boundary

- System in focus: first-party terminal coding agent `attrition-tech/arkex@0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8`, assessed as one active repository-oriented coding session.
- Purpose and identity: independently select model-driven file and shell operations in response to a user development request, with per-tool permission checks, session resumption, and a terminal UI.
- Relevant environment: workspace files, shell output, configured model/provider responses, project and global configuration, user approval, persisted conversations, context-window limits and tool errors.
- Standard-distribution boundary: shipped `cmd/arkex` CLI, interactive TUI and print mode, `internal/agent` model/tool runtime, `internal/tools` registered capabilities, mode/permission/scope controls and first-party session handling.
- Credited operating / distribution surfaces: `cmd/arkex/main.go`, `internal/agent/`, `internal/tools/`, `internal/tui/`, `internal/session/`, `internal/config/`, `internal/provider/` and supported `--print` / `--mode` operation.
- Adjacent first-party surfaces excluded from ownership: release signing and self-update as product distribution; repository development CI and tests; `scripts/dev` fixtures; external model providers and standalone fake HTTP test servers; upstream organization/maintainer governance.
- Reviewed modes: interactive TUI, noninteractive print, plan/build/auto, session resume, model switch and context compaction; no built-in independent child-agent population is instantiated.
- Recursion level: a single running coding session, not the external provider company, release pipeline, or a user's collection of terminals.
- License screen: frozen root `LICENSE` is MIT and public GitHub repository metadata identifies MIT; candidate passes the license intake gate.
- Observation date: 2026-10-23; Profile `0.2.4`; Methodology `0.3.7`.

## Repository architecture

`cmd/arkex/main.go` wires one `agent.Agent` to a selected provider, the built-in read/write/edit/bash registry and a shared mode policy. `Agent.RunMessage` appends the user's request, streams a model response, and executes resulting tool calls sequentially through `execute` → `runOne`; denied/failed calls still become tool results in the same model conversation. Context compaction invokes the connected model to summarize old messages and feeds the summary back to this same operating session. `internal/session` stores and resumes transcripts; the TUI renders and allows user intervention. No first-party model-backed delegation, cross-agent resource allocation or autonomous independent audit process is reachable from the supported constructor.

The user can switch plan/build/auto modes and approve or reject specific operations. The mode policy enforces explicit denies and asks separately for paths outside trusted workspace scope, but the source calls this heuristic rather than an OS sandbox. `internal/update` checks a static release manifest and verifies updates with signed checksums; it is deterministic product maintenance, not strategic agent adaptation.

Frozen sources: [`cmd/arkex/main.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/cmd/arkex/main.go), [`internal/agent/agent.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/agent.go), [`internal/tools/tool.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/tools/tool.go), [`internal/agent/mode.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/mode.go), [`internal/agent/scope.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/scope.go), [`internal/update/update.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/update/update.go).

## Operational model

One model-backed actor owns decisions about how to inspect, edit and test the repository, and can revise them after tool-result feedback (S1=A). Multiple returned tool calls are processed sequentially, not delegated to separate independently deciding S1s (S2=—). Human approval, retry and context compaction are supporting controls within one task stream, not a whole-current S3 manager, complementary S3* reviewer or future-oriented S4. Neither path permission rules nor deterministic signed self-update establish legitimate system-purpose arbitration (S5=—).

## S1 — Operations

- State: A
- Function: operate on a software repository to answer or execute a user development request.
- Disturbance / variety regulated: repository contents, unexpected shell/file errors, task uncertainty, permission denials, model/provider outcomes and context budget.
- Decisive decision or feedback right: the model selects which built-in tool to invoke with what arguments and responds to observed result text on the next turn.
- Decision owner: the active model-backed `agent.Agent` for one arkex conversation.
- Supporting / enforcement mechanisms: provider adapters, read/write/edit/bash registry, model streaming, mode and path policy, TUI approval, stuck detection, compaction and persisted sessions.
- Closure path: user prompt → model chooses one or more tool calls → policy decides → sequential tool execution → result/denial/error appended to model conversation → model chooses subsequent work or concludes.
- Boundary reachability: supported `arkex` CLI `connect` builds `Agent` with a provider, tools and mode policy; print and TUI both invoke this loop.
- Why this is / is not agent-owned: the model decides task-specific work and revises it from feedback; policy and loop merely constrain/enforce those choices.
- Evidence: [`cmd/arkex/main.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/cmd/arkex/main.go), [`internal/agent/agent.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/agent.go), [`internal/tools/tool.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/tools/tool.go).
- Basis: frozen first-party source plus deterministic Go test suite; no live LLM experiment.
- Confidence: high for shipped decision and feedback rights.
- Caveats: source and unit tests demonstrate reachable design, not coding success against a real external model.

## S2 — Coordination

- State: —
- Function: no first-party independently deciding operational-unit interactions are coordinated within the assessed session.
- Disturbance / variety regulated: concurrent autonomous worker interference is not a present runtime disturbance; a single agent can issue several serial tool calls.
- Decisive decision or feedback right: `Agent.execute` runs tool results in a `for` loop; the registry exposes only read, write, edit and bash.
- Decision owner: no S2 coordination actor established.
- Supporting / enforcement mechanisms: sequential tool execution, single-session mode policy and shared conversation.
- Closure path: one model's tool calls return to the same model; no child-S1 contention → S2 decision → revised allocation across multiple S1s exists.
- Why this is / is not agent-owned: parallelizable subprocess work and asynchronous terminal UI are mechanisms, not separately tasked autonomous organizational S1s.
- Evidence: [`internal/agent/agent.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/agent.go), [`internal/tools/tool.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/tools/tool.go).
- Basis: explicit native execution path and tool registry.
- Confidence: high.
- Caveats: a user may launch two arkex processes externally, but neither a first-party S2 nor its coordination loop is evidenced.

### Absence scope

- Surfaces inspected: CLI constructors, `Agent.loop`/`execute`, all built-in tools, session operations, TUI event handling and smoke/development fixtures.
- Plausible first-party paths checked: multiple model tool calls as agents, OS subprocesses as agents, TUI background goroutine as independent S1, separate user-launched sessions.
- Why no material first-party path remains: only one reasoning model owner is assembled per session, without bounded autonomous delegation or cross-worker interference attenuation.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current management of a cohort of operating S1s with priorities, resource commitments and corrective rights is implemented.
- Disturbance / variety regulated: approvals, stuck loops, provider retries and context exhaustion affect one coding activity, not current organization-wide commitments.
- Decisive decision or feedback right: users can change mode, stop runs or approve a tool; guard code can pause/compact; neither decides cross-S1 allocation.
- Decision owner: no S3 controller shown.
- Supporting / enforcement mechanisms: session resume, TUI usage/mode indicators, model switch, human approvals, stuck limits and context compaction.
- Closure path: local resource or permission event → guard/operator → single agent resumes/pauses; no shared current-state view → S3 portfolio decision → downstream S1 changes.
- Why this is / is not agent-owned: these are operational safety and usability controls, not autonomous present-management authority over multiple units.
- Evidence: [`internal/agent/agent.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/agent.go), [`internal/tui/app.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/tui/app.go), [`internal/agent/compact.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/compact.go).
- Basis: bounded negative structural review.
- Confidence: high at one-session recursion.
- Caveats: user supervision across processes is not an embedded first-party S3.

### Absence scope

- Surfaces inspected: TUI model/session commands, all agent limits, compaction, policy, runtime events and persisted sessions.
- Plausible first-party paths checked: retry as current control, context compaction as resource management, session list as portfolio, human approval as S3, model switching as reallocation.
- Why no material first-party path remains: no simultaneously operating S1 roster, joint feedback picture or authority to alter cross-unit priority/commitment decisions.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit owner reviewing operations and returning findings to a separate current-control decision circuit.
- Disturbance / variety regulated: faulty generated code and unsafe commands may be inspected by humans or deterministic tests, but no independent first-party audit actor is instantiated.
- Decisive decision or feedback right: test/script results or tool errors are returned directly to the producing model; the TUI shows actions to the same operator.
- Decision owner: none established independently of S1 or external human reviewer.
- Supporting / enforcement mechanisms: explicit mode/permission checks, transcript history, deterministic source tests, signed release verification.
- Closure path: tool outcome or user rejection → same session actor; no distinct auditor evidence → independent audit judgment → corrective S3 return.
- Why this is / is not agent-owned: policy enforcement, transcript observability and CI fixtures are not a complementary evaluator of the operating agent.
- Evidence: [`internal/agent/agent.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/agent.go), [`internal/agent/policy.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/policy.go), [`internal/update/update.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/update/update.go).
- Basis: current shipped code and repo-level development/test separation.
- Confidence: high.
- Caveats: an external independent reviewer could audit arkex output but is not credited to this system.

### Absence scope

- Surfaces inspected: runtime tools, approval UI, event transcripts, unit/smoke tests, signed release pipeline and update client.
- Plausible first-party paths checked: source test harness as runtime auditor, permission veto as review, transcript as S3*, release signature check as complementary audit.
- Why no material first-party path remains: none constitutes an autonomous independent operational reviewer with distinct access and a returned corrective governance channel.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future-oriented environmental scanning and capability-adaptation choice cycle is closed.
- Disturbance / variety regulated: provider availability and release updates are configuration/distribution contingencies, not an autonomous strategic redesign disturbance.
- Decisive decision or feedback right: users choose a model and update channel; a deterministic updater compares semantic versions and verifies signed binaries.
- Decision owner: no autonomous strategic S4 owner.
- Supporting / enforcement mechanisms: provider configuration, manual model switch, signed manifest/checksum update client and context summarization.
- Closure path: selected model/release update affects a local tool/session; there is no external-horizon model → adaptation option → S3 capability redesign return.
- Why this is / is not agent-owned: deterministic version replacement and task-context compaction do not own long-horizon option generation or deployment.
- Evidence: [`internal/update/update.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/update/update.go), [`internal/agent/compact.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/compact.go), [`cmd/arkex/main.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/cmd/arkex/main.go).
- Basis: bounded native source inspection.
- Confidence: high.
- Caveats: external maintainer product strategy is outside the assessed operating runtime.

### Absence scope

- Surfaces inspected: model selection, provider plugins, updater, release tools, context compacting and session prompts.
- Plausible first-party paths checked: update feed as external sensing, release manager as S4, model switching as capability adaptation, context summary as organizational learning.
- Why no material first-party path remains: these facilities deliver user-selected fixed functionality, not an independent strategic feedback and future-capability change process.

## S5 — Policy and identity

- State: —
- Function: no legitimate ultimate system-purpose/identity authority and policy balance with S3/S4 is implemented in the running session.
- Disturbance / variety regulated: malicious operations and untrusted paths need permission checks, but do not by themselves create organizational identity disputes.
- Decisive decision or feedback right: operator config selects plan/build/auto and approves individual operations; static rules enforce denies and workspace boundary.
- Decision owner: no first-party S5 actor identified at the assessed recursion.
- Supporting / enforcement mechanisms: `ConfigPolicy`, `ModePolicy`, `Scope`, human approver, project configs and signed release keys.
- Closure path: requested tool → allow/deny/trust decision → execution or refusal; no durable identity-purpose proposal → legitimate ultimate policy decision → organizational return loop.
- Why this is / is not agent-owned: permissions and trust establish per-action legitimacy only, not a governing identity/autonomy balance.
- Evidence: [`internal/agent/policy.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/policy.go), [`internal/agent/mode.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/mode.go), [`internal/agent/scope.go`](https://github.com/attrition-tech/arkex/blob/0c4f2b17cc9d8593e5f378bdf6d32263bc72a9d8/internal/agent/scope.go).
- Basis: current safety/permission path contrasted with absent policy-identity ownership.
- Confidence: medium-high.
- Caveats: upstream maintainers govern future releases but are not an embedded policy actor coupled to one coding session.

### Absence scope

- Surfaces inspected: config permissions, trusted paths, interactive/noninteractive behavior, all modes, provider selection and release identity keys.
- Plausible first-party paths checked: user as S5 through tool approval, static security policy as S5, maintainer governance as embedded S5, release signing as authority.
- Why no material first-party path remains: action permission and software-integrity mechanisms do not decide the system's legitimate organizational purpose or S3/S4 relation.

## Distributed OSS parent arrangement

The product has maintainers, release automation and a signed update path, but those are external development/distribution surfaces. No first-party inter-agent control or parent metasystem returning S3/S4/S5 governance to the running coding session is established by those surfaces.

## Self-hosted and non-human modes

Local OpenAI-compatible or ChatGPT-backed provider connections instantiate the same core agent loop. Interactive and print modes differ in whether approval prompts can be surfaced; print mode fails closed when one is required. Build/plan/auto are permission postures, not additional organizational agents. A deterministic local fake HTTP provider is a test fixture, not a live LLM.

## Recursion

The evidenced viable operational level is one arkex task/session, in which the model-backed actor is S1. External shell processes, the model API, release mechanisms, user-launched parallel processes and saved sessions do not by themselves create nested independently viable units or higher-function ownership.

## Variety and escalation

Tool outcomes, context overflow, repeated calls and approval problems return to the same producing agent or the human prompt; a stuck loop pauses for the operator. There is no first-party S2 interference attenuation, whole-current S3 priority intervention, separate S3* audit, prospective S4 redesign or S5 identity decision circuit.

## Evidence gaps

- This is a frozen first-party source assessment, not a live LLM efficacy evaluation. Go tests exercise deterministic fakes, policies, tools, TUI and release logic only.
- No externally assembled multi-agent system or independent reviewer is credited as a standard arkex runtime function.
- Tests and source code do not prove accuracy of a connected user's chosen model or safety of commands outside the heuristic permission scope.
