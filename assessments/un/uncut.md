---
harness_id: uncut
project_name: UNCUT
repository: https://github.com/Balanov/uncut
review_ref: e1512a702de846eb701e0383d9ae031bad528c0f
reviewed_at: 2026-11-02
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

# UNCUT

## Review boundary

- System in focus: the shipped UNCUT 0.1.1 headless coding-agent CLI and its first-party Go model/tool loop at the frozen source revision.
- Purpose and identity: perform coding tasks in a local workspace through an OpenAI-compatible model, four built-in file/shell tools, complete tool feedback and optional append-only session continuation.
- Relevant environment: operator task and workspace, provider model responses, file and command outcomes, invalid/truncated provider results, session state and operating-system signals.
- Standard-distribution boundary: `cmd/uncut` and `internal/harness` running as one local coding agent; the configured external model is the decision actor, while the provider service, task repository, shell programs and operator remain outside the UNCUT software boundary.
- Credited operating / distribution surfaces: `cmd/uncut/main.go`, `internal/harness/run.go`, `tools.go`, `provider.go`, `session.go`, and the shipped `ToolDefinitions`.
- Adjacent first-party surfaces excluded from ownership: `bench/` performance/proof programs, `*_test.go` fixtures, documentation examples, GitHub CI/release workflows and the maintainer's software-development organization. These support evidence but are not an installed independent governance or audit actor.
- First-party operating / deployment modes considered: one-shot CLI, piped text input, NDJSON event stream, resume from append-only JSONL conversation, optional `AGENTS.md` instructions, configurable provider/model and hard `--max-steps`/timeout limits.
- Recursion level: one active UNCUT agent execution/session and its workspace-facing operations. Tool calls are actions of the same agent, not distinct enduring S1 operational cells.
- Reviewed revision: `e1512a702de846eb701e0383d9ae031bad528c0f`.
- Observation date: 2026-11-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The CLI assembles a workspace-scoped executor and an OpenAI-compatible Chat Completions provider, optionally loads `AGENTS.md` and prior session messages, and enters `Runner.Run`. Each model turn receives the full current message history and four tool definitions. The model selects file reads, whole-file writes, single replacements or shell commands; the executor returns their complete text/error, and the next model turn can react. A model message without tool calls terminates with a final answer. A provider truncation, empty final answer, exhausted step limit or unsupported finish reason fails rather than being accepted as success.

`Session` persists messages and tool results as append-only synced JSONL and restores them for subsequent CLI invocations. `--json` emits events for an external observer but does not install an independent decision-maker. Path resolution limits file tools to a configured workspace; step limits, request timeout, UTF-8 checks and session-record validation are deterministic safeguards. Shell command execution is a tool action within the same unit, not a peer agent or independent audit.

Primary entry/source: [CLI](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/cmd/uncut/main.go), [runner](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/run.go), [tools](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/tools.go), [session](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/session.go), [README](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/README.md).

## Operational model

The model-backed actor owns substantive coding choices, tool selection, interpretation of file/command results and whether to continue or return the completed task. UNCUT's Go runtime executes those chosen calls and enforces preconfigured bounds without selecting the coding objective or a whole-system policy. The operator chooses instructions, model, workspace and limits; the session carries past observations across invocations without independently learning a new organizational capability.

## S1 — Operations

- State: A
- Function: complete a user-requested coding/investigation outcome through a model-chosen sequence of workspace actions.
- Disturbance / variety regulated: unknown source organization, edit/test outcomes, command failures and incomplete information discovered while implementing the task.
- Decisive decision or feedback right: select and revise file/shell operations from returned evidence, decide whether more work is needed, and issue the final result.
- Decision owner: the configured model-backed coding agent in `Runner.Run`.
- Supporting / enforcement mechanisms: Go call loop, four tool implementations, workspace path guard, provider adapter, session log, step budget, timeout and output-error handling.
- Closure path: task prompt → model tool call → `Executor.Execute` → tool result appended to message history → next model judgment/action or final answer.
- Boundary reachability: the standard `uncut` CLI constructs `Runner` with provider and executor and invokes `Runner.Run`; no dogfood-only or sample integration is needed.
- Why this is / is not agent-owned: with the model removed the runtime can expose tools and enforce limits but cannot select substantive edits or interpret feedback into task completion.
- Evidence: [main.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/cmd/uncut/main.go), [run.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/run.go), [tools.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/tools.go), [run_test.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/run_test.go).
- Basis: explicit + structural.
- Confidence: high for the wired model/tool feedback path; live provider task success is not claimed.
- Caveats: model quality and credentials are external; the shell can act broadly within OS permissions despite the file-tool workspace check.

## S2 — Coordination

- State: —
- Function: no material first-party coordination among distinct operating S1 units is supplied.
- Disturbance / variety regulated: no shipped peer-agent interference or oscillation is identified at this single-agent boundary.
- Decisive decision or feedback right: none established for inter-S1 adjustment.
- Decision owner: none established.
- Supporting / enforcement mechanisms: sequential tool-call execution and one shared conversation/session.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: sequencing multiple tool calls from one model is not the coordination of distinct autonomous S1 units.
- Evidence: [run.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/run.go), [types.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/types.go), [README](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/README.md).
- Basis: bounded structural absence.
- Confidence: high.
- Caveats: external shell commands could launch independent agents, but UNCUT does not ship and coordinate such a peer organization.

### Absence scope

- Surfaces inspected: CLI flags, runner, tool definitions/executor, session and documented modes.
- Plausible first-party paths checked: subagent creation, peer task reservations, contention feedback, worktree coordination, conflict reconciliation and subsequent peer adjustment.
- Why no material first-party path remains: the distribution implements one conversation/runner and generic serial tool actions, without distinct packaged S1 peers or an inter-peer disturbance-control relation.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system supervisory current-control loop exists above the one S1 agent.
- Disturbance / variety regulated: per-run step/time limits and tool errors are bounded locally, without whole-system resource/commitment management.
- Decisive decision or feedback right: none established for substantive cross-unit current control.
- Decision owner: none established.
- Supporting / enforcement mechanisms: `--max-steps`, HTTP timeout, context cancellation and error exits.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the operator preselects limits and the runtime enforces them; the coding agent does not gain a whole-system live view or authority to reallocate independent units' commitments.
- Evidence: [main.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/cmd/uncut/main.go), [run.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/run.go).
- Basis: bounded structural absence.
- Confidence: high.
- Caveats: a single S1 agent can choose its next local action; that is not by itself a higher-recursion S3 decision.

### Absence scope

- Surfaces inspected: CLI configuration, runner's status/step/error paths, event emission and session model.
- Plausible first-party paths checked: live supervisor/controller actor, whole-current operations view, intervention/resource reallocation, parent current-control return and agent-selected system-wide commitments.
- Why no material first-party path remains: only one S1 loop and fixed operating limits are shipped, with no distinct whole-system current-control closure.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit channel is installed.
- Disturbance / variety regulated: file/test evidence may be inspected by the ordinary coding agent, but no separate complementary audit challenges its reporting.
- Decisive decision or feedback right: none established for an independent audit judgment.
- Decision owner: none established.
- Supporting / enforcement mechanisms: `read_file`, `run_command`, full tool-result logging and optional NDJSON observation.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: the same S1 model may run tests or read diffs; these ordinary feedback operations and emitted logs do not supply an independent auditor and corrective-return decision.
- Evidence: [tools.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/tools.go), [run.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/run.go), [README](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/README.md).
- Basis: bounded structural absence.
- Confidence: high.
- Caveats: an external operator can audit emitted events or instruct a separate reviewer, but such an auditor is not a shipped first-party organizational path.

### Absence scope

- Surfaces inspected: complete built-in tool set, model loop, event stream, session persistence and first-party tests/docs.
- Plausible first-party paths checked: independent reviewer actor, complementary raw-evidence access, adjudicated audit verdict and findings returned to current control.
- Why no material first-party path remains: one model both performs and checks work; events/tests carry ordinary feedback but do not instantiate a complementary audit decision owner.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective organizational adaptation loop is supplied.
- Disturbance / variety regulated: changes in future tools/models/environment are left to external operator choices, rather than modeled by a first-party capability-adaptation process.
- Decisive decision or feedback right: none established for future-oriented adaptation options.
- Decision owner: none established.
- Supporting / enforcement mechanisms: reusable session messages, configurable provider URL/model, system instructions and `AGENTS.md` loading.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: conversation continuation, current-task replanning and manual provider selection do not develop externally grounded future options and return them into durable present capability.
- Evidence: [main.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/cmd/uncut/main.go), [session.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/session.go), [README](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/README.md).
- Basis: bounded structural absence.
- Confidence: high.
- Caveats: a user could ask for strategic research as an ordinary task, but the standard harness lacks a continuing S4 feedback mechanism.

### Absence scope

- Surfaces inspected: session/continuation, provider selection, CLI instructions, runner and documented features/non-features.
- Plausible first-party paths checked: external change sensing, prospective option formulation, capability/policy revision and return of adopted options to operating control.
- Why no material first-party path remains: observed state persistence and configurable endpoint are present-task support/configuration, not a shipped organizational adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy decision loop is closed at the running harness boundary.
- Disturbance / variety regulated: operating instructions and tool scope constrain the coding task, but identity-level conflict is not routed to authoritative governance and returned.
- Decisive decision or feedback right: none established at ultimate-policy level.
- Decision owner: none established.
- Supporting / enforcement mechanisms: static default system prompt, optional workspace `AGENTS.md`, CLI choices, file path validation and hard limits.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the operator sets instructions and limits, the Go runtime enforces tool semantics, and no shipped identity-policy proposal/decision/return route exists; a generic human task instruction is not S5 parent closure.
- Evidence: [main.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/cmd/uncut/main.go), [tools.go](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/internal/harness/tools.go), [README](https://github.com/Balanov/uncut/blob/e1512a702de846eb701e0383d9ae031bad528c0f/README.md).
- Basis: bounded structural absence.
- Confidence: high.
- Caveats: repository-maintainer policy/release decisions belong to an adjacent OSS development organization rather than this CLI session.

### Absence scope

- Surfaces inspected: system prompt/AGENTS loading, flags, executor policy/limits, session and repository governance/development boundary.
- Plausible first-party paths checked: identity-level proposal, legitimate internal/parent ultimate-policy authority, authoritative return to the running agent and changed subsequent operation.
- Why no material first-party path remains: instructions and execution guards are preselected constraints; no first-party identity/ultimate-policy decision-and-return path is installed.

## Distributed OSS parent arrangement

The GitHub project's developers and contributors can publish releases or change UNCUT's future code, but their repository governance is adjacent to the assessed local CLI instance. No organization-level S3/S4/S5 parent loop is inferred from the maintainer project or from arbitrary local users.

## Self-hosted and non-human modes

The headless CLI supports hosted or local OpenAI-compatible model endpoints and optionally resumes a local session. Neither endpoint choice nor local operator configuration supplies a distinct evidenced parent-governed S3/S4/S5 mode.

## Recursion

The one running model/tool loop is the supported S1 unit. Tool calls are subordinate actions rather than viable nested operational units; the frozen implementation ships no separate agent/subagent hierarchy.

## Variety and escalation

UNCUT addresses coding-task variety through model/tool feedback. Provider truncation, malformed/empty final responses, session corruption and step exhaustion fail explicitly; the caller can retry or choose different settings. Those exits are local failure/recovery boundaries, not independent algedonic/S3/S4/S5 evidence.

## Evidence gaps

No model-backed end-to-end task was run during this review. The source and tests support the installed S1 feedback path and the bounded no-material-first-party-path conclusions for S2–S5; semantic claims do not depend on live provider quality. Native Go tests were not executed because the review environment lacks the `go` toolchain.
