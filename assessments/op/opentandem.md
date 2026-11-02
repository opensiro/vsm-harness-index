---
harness_id: opentandem
project_name: OpenTandem
repository: https://github.com/opentandem/opentandem
review_ref: 01335e7c313861bf7134d33f363eb2c079009788
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

# OpenTandem

## Review boundary

- System in focus: the public OpenTandem CLI and locally installed Runner controlling supported coding-agent sessions on an operator's machine, not the unshipped OpenTandem cloud service.
- Purpose and identity: receive remote coding tasks, launch the selected autonomous coding agent in its project, stream work events, and retain or resume task sessions.
- Relevant environment: operator requests, local repositories and files, installed coding CLIs and provider accounts, remote task/control messages, interruptions and machine restarts.
- Standard-distribution boundary: the public CLI's pairing/Runner lifecycle and the Node.js Runner distribution, with adapter-driven execution of installed agents; the externally hosted account/server is an input/output dependency.
- Credited operating / distribution surfaces: `cli/core.cjs`, `cli/service.cjs`, `runner/core/machine-daemon.mjs`, `runner/adapters/`, the persistent `runner/core/runner-local-store.mjs` and documented installed Runner mode.
- Adjacent first-party surfaces excluded from ownership: the hosted server and web app, whose implementation is explicitly not included in the Runner repository; test-only fixtures, Runner bundling/CI, preview/demo assets and upstream contributor governance. External Claude Code, Codex, Pi, OpenCode, Gemini and other agent implementations retain their own model/tool reasoning internals.
- First-party operating / deployment modes considered: CLI-installed background Runner connected to the hosted service, source-started Runner with a real paired account, supported adapter-based interactive/resumed/headless tasks, and deterministic scheduling/tool bridges. No real account or paid-provider E2E was exercised.
- Recursion level: one local Runner installation with one or more autonomous coding-task cells. A vendor agent's own tool loop is lower recursion; the opaque hosted coordination service is outside the evidence boundary.
- Reviewed revision: `opentandem/opentandem@01335e7c313861bf7134d33f363eb2c079009788` (GitHub repository ID 1435201868), frozen in candidate intake #2578 and assessment controller #2579.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The first-party [Runner guide](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/README.md) explicitly separates the open local Runner from the hosted OpenTandem server/web app. The [CLI](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/cli/README.md) pairs the machine with a human-approved account, installs a per-machine background service and manages restart/update. The [daemon](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/machine-daemon.mjs) long-polls the server for a task, chooses an installed adapter, starts a native agent subprocess, follows output/tool events, publishes results and resumes or reconstructs interrupted native sessions. [Adapters](https://github.com/opentandem/opentandem/tree/01335e7c313861bf7134d33f363eb2c079009788/runner/adapters) define native commands, session handling and output semantics; [SQLite local store](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/runner-local-store.mjs) retains local conversation/run evidence. Scheduling and goal commands are available as tools, but their remote API and server-side judgments are not open-source evidence. File transfer, preview permissions, quota probes and heartbeat are supporting runtime controls, not separate autonomous governance.

## Operational model

Operational S1 cells are model-driven coding-agent sessions launched by the Runner for different tasks/workspaces. The agent chooses substantive code/tool actions; OpenTandem chooses the adapter and transports run requests, events, permissions and persistence. The person chooses machine pairing, agent/task selection and whether to approve actions. A concurrency ceiling, session queue, task ID, heartbeat or command selector is deterministic machinery and is not evidence of autonomous S2/S3 judgment. The hosted service is not reconstructed from marketing claims.

## S1 — Operations

- State: A
- Function: perform coding/tool tasks in operator-selected repositories using supported launched autonomous agents, with retained session context.
- Disturbance / variety regulated: different user instructions, changing file contents, tool observations, interrupted sessions and model/provider behavior.
- Decisive decision or feedback right: select next coding/tool action in response to observations within each launched agent session.
- Decision owner: the running model-driven coding agent (one S1 cell), instantiated and driven by first-party Runner adapter/dispatch.
- Supporting / enforcement mechanisms: daemon claim loop, adapter registry, subprocess supervision, context reconstruction, uploaded files, session ID and SQLite records.
- Closure path: remote task → Runner claim → selected adapter/agent subprocess → tool/action stream and completed answer → event pump/server reply and resumption on later instruction.
- Boundary reachability: `pollOnce` dispatches `executeRun` in the shipped daemon; `executeRun` resolves the registered runtime/adapter and invokes normal resumed/new task execution, not just a test fixture. Actual provider code remains external.
- Why this is / is not agent-owned: model-agent decisions determine substantive task actions; removing the coding agent leaves a task transport/session launcher, not equivalent autonomous coding behavior.
- Evidence: [Runner guide](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/README.md), [machine-daemon.mjs](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/machine-daemon.mjs), [adapters/index.mjs](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/adapters/index.mjs).
- Basis: structural
- Confidence: high
- Caveats: source-level first-party composition of external native agent CLIs; no authenticated service or paid-provider run and no claim that their internals are authored by OpenTandem.

## S2 — Coordination

- State: —
- Function: no shipped local inter-S1 interference-specific coordination judgment/return established.
- Disturbance / variety regulated: potential simultaneous workspace edits and competing agent tasks were checked, but no local regulation of that specific cross-agent conflict is demonstrated.
- Decisive decision or feedback right: resolving an actual conflict among distinct active coding-task cells is not provided by the reviewed local distribution.
- Decision owner: not established; the operator and proprietary server could organize work outside the local open-source boundary.
- Supporting / enforcement mechanisms: bounded `MAX_RUNS`, per-run IDs, claim isolation, task concurrency, and duplicate *Runner process* suppression.
- Closure path: task execution and lifecycle ordering exist, but no conflict-specific decision feeds one cell's collision resolution into another cell's subsequent task behavior.
- Why this is / is not agent-owned: limiting process count and preventing two daemon copies competing for the same machine is not agent-chosen attenuation of inter-S1 oscillation.
- Evidence: [daemon poll/execute](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/machine-daemon.mjs), [CLI Runner pool](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/cli/core.cjs), [runner thread-lane tests](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/tests/thread-lanes.test.ts).
- Basis: structural
- Confidence: medium
- Caveats: no conclusion about unseen hosted team-collaboration implementation.

### Absence scope

- Surfaces inspected: Runner/CLI guides, daemon claim/execution/poll and concurrency paths, adapter registry, RunnerPool, local task records and thread-lane tests.
- Plausible first-party paths checked: simultaneous task dispatch, one-machine duplicate daemon suppression, shared session metadata, task queue and per-agent tool bridges.
- Why no material first-party path remains: these protect transport and task identity, but the open local distribution does not implement a specific feedback regulation of conflicting distinct S1 outcomes; hypothetical server-side collaboration is outside the evidence boundary.

## S3 — Inside-and-now control

- State: —
- Function: no evidenced first-party whole-installation discretionary current-control authority.
- Disturbance / variety regulated: current run count, machine limits, cancellation, connectivity, tool permissions and provider quota.
- Decisive decision or feedback right: prioritizing or reallocating operating-cell commitments/resources for the whole is not shown as a local agent-owned or returned parent decision.
- Decision owner: operator/server selects runs and policies; the Runner enforces static limits and dispatches one supplied task.
- Supporting / enforcement mechanisms: process count ceiling, status/heartbeat, terminate/restart, agent-install slots and error reporting.
- Closure path: operational start/stop/status alters individual runs; no separate whole-system current-control negotiation or decision-return loop is demonstrated.
- Why this is / is not agent-owned: local process enforcement remains after removing any hypothetical S3 agent; no such agent makes a discretionary cross-cell decision here.
- Evidence: [machine-daemon.mjs](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/machine-daemon.mjs), [CLI lifecycle](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/cli/core.cjs).
- Basis: structural
- Confidence: medium
- Caveats: hosted server's scheduling/portfolio controls are explicitly not credited.

### Absence scope

- Surfaces inspected: daemon task claim/poll, concurrency and execution gates, CLI process pool, runner status and documented supported modes.
- Plausible first-party paths checked: `MAX_RUNS` cap, heartbeat/quota metrics, task cancellation, daemon restart, runtime selection and administrative account pairing.
- Why no material first-party path remains: local features dispatch or enforce already selected run/control parameters, without a whole-current S3 view plus discretionary shared-commitment authority and returned regulation.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit of operational result claims with corrective return in the shipped local Runner.
- Disturbance / variety regulated: false successful agent output, unsafe tool side effects and missing run artifacts were investigated as candidate claims.
- Decisive decision or feedback right: no independent auditor makes a contradictory evidence judgment and requires changed task behavior before accepted completion.
- Decision owner: routine producer agent and operator remain owners of ordinary work; deterministic validators secure transport and recordings.
- Supporting / enforcement mechanisms: tool summaries, event traces, file-access checks, local SQLite, Runner tests and authentication tickets.
- Closure path: tool/result events are reported; no independent audit verdict → corrective workflow loop exists in the local distribution.
- Why this is / is not agent-owned: logs and unit tests cannot become a separate audit agent simply by recording or testing the normal run.
- Evidence: [machine-daemon.mjs](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/machine-daemon.mjs), [local store](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/runner-local-store.mjs), [runner tests](https://github.com/opentandem/opentandem/tree/01335e7c313861bf7134d33f363eb2c079009788/runner/tests).
- Basis: structural
- Confidence: medium
- Caveats: no attribution to a remote server review or an external agent's own optional verification.

### Absence scope

- Surfaces inspected: daemon event/report paths, local recorder, runtime adapter result handling, transfer/security checks, shipped runner tests.
- Plausible first-party paths checked: tool result summaries, failed-run/cancel status, permission verification, preview ticket validation and possible reviewer agent selection.
- Why no material first-party path remains: these are operational reporting, hard security enforcement or selectable ordinary external workers; no independent complementary evidence/owner with enforced corrective return is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: no local outside-and-future adaptation-option selection with closure into current installation capability.
- Disturbance / variety regulated: changing model availability, provider versions, future scheduled tasks and agent update availability.
- Decisive decision or feedback right: selecting organizational capability changes in response to future/environmental evidence is not implemented as an S4 judgment.
- Decision owner: developers/server issue update metadata, users select or schedule tasks; Runner performs adapter/version actions.
- Supporting / enforcement mechanisms: adapter probing, update plans, scheduled task tools and session recovery.
- Closure path: environment/probe data can affect operational configuration or rerun a task, but no first-party agent turns future distinctions into capability adaptation options and feeds an authorized option back to current control.
- Why this is / is not agent-owned: automatic probe/update code does not autonomously judge strategic adaptation; a scheduled goal is an operational task, not itself S4.
- Evidence: [machine-daemon.mjs](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/machine-daemon.mjs), [runner adapter interface](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/README.md).
- Basis: structural
- Confidence: medium
- Caveats: external web app/account may supply other capabilities, not evaluated here.

### Absence scope

- Surfaces inspected: Runner lifecycle/update, runtime probes, schedule tools, goal/recovery handlers and CLI documentation.
- Plausible first-party paths checked: agent-version update, model catalog probes, time-triggered tasks, schedule/goal retries and session memory.
- Why no material first-party path remains: none of the shipped local paths links external prospective sensing to a discretionary adaptive option and returned changed present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy deliberation and authoritative return loop in the local Runner boundary.
- Disturbance / variety regulated: account pairing, permission policy, file-read restrictions, user preferences and deployment configuration.
- Decisive decision or feedback right: unresolved ultimate-identity choice and legitimate parent adjudication are not provided by the local runtime.
- Decision owner: human account owner provides prior permissions; fixed code enforces them. These are operational constraints, not proved S5 ownership.
- Supporting / enforcement mechanisms: pairing/credential verification, runtime permission modes, signed control tickets, restrictive file paths and manual connection management.
- Closure path: permission settings govern individual tasks, but no identity-level issue → ultimate authority → policy decision → return into organizational regulation is shipped.
- Why this is / is not agent-owned: removing the agent leaves these fixed account/permission controls unchanged; no agent governs organizational identity.
- Evidence: [CLI README](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/cli/README.md), [runner-p2p.mjs](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/runner-p2p.mjs), [machine-daemon.mjs](https://github.com/opentandem/opentandem/blob/01335e7c313861bf7134d33f363eb2c079009788/runner/core/machine-daemon.mjs).
- Basis: structural
- Confidence: medium
- Caveats: no claim about OpenTandem company's higher-recursion institutional governance.

### Absence scope

- Surfaces inspected: CLI/Runner user guides, pairing and credential code, machine control tickets, runtime policy/permissions, execution and scheduling.
- Plausible first-party paths checked: account owner authorization, user-approved remote pairing, permission prompts, control messages and config/agent selection.
- Why no material first-party path remains: these govern access and already-chosen task boundaries; no distinct identity/ultimate-policy matter is escalated to a legitimate authority with policy adjudication and return-to-operation closure.

## Distributed OSS parent arrangement

External installation users and independent open-source contributors are not one in-boundary S3/S4/S5 parent organization. Pairing and permissions are attributed to the account owner only as operational inputs; an organization-level parent decision path was not reconstructed from GitHub maintainers or a remote, uninspected service.

## Self-hosted and non-human modes

The open Runner can be built or launched from source but requires a service account to execute normal remote tasks. It does not ship a self-contained first-party server or a policy metasystem. Agent/provider choices are lower-recursion execution modes, not evidence of autonomous S3–S5 or a separately closed `(P)` topology.

## Recursion

Each supported coding-agent session is an operational cell that may have its own internal control organization supplied by its vendor. Merely spawning several such sessions does not prove viable recursion within the public Runner.

## Variety and escalation

Adapter specialization, resumable sessions, local record persistence, retries, tool/file gating and bounded process concurrency attenuate execution variety. Error reporting returns failures to users/server, but ordinary status channels do not alone prove an algedonic escalation channel or an S3/S4/S5 decisive authority.

## Evidence gaps

The public repository explicitly excludes the hosted server and web app, so their inter-agent collaboration, queue priority and governance cannot support positive claims at this local evidence boundary. No production account, model provider, paid tool or live multi-machine execution was used. The first-party Runner bundle's `npm run selftest` passed offline with Node 24.22.1 on the reviewed source; this validates packaging, not model-driven VSM closure. The assessment does not treat externally implemented agent loops as OpenTandem-authored reasoning.
