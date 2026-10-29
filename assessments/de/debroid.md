---
harness_id: debroid
project_name: Debroid
repository: https://github.com/PatilShreyas/debroid
review_ref: b87f489bd02dcfb5c8c37fa2a4340847c9e48adb
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-29
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Debroid

## Review boundary

- System in focus: Debroid's installed Kotlin CLI and local JDWP/ADB debugger daemon at the frozen revision, not the external coding agent invoking it.
- Purpose and identity: expose live Android process inspection, breakpoints, stepping, mutation, and JSON results to a human or an external AI coding assistant.
- Relevant environment: Android apps/devices, ADB, JVM debugging sessions, external terminal/agent clients and their debugging objectives.
- Standard-distribution boundary: `Main.kt` → `CliRunner` commands → daemon IPC → `DaemonServer` → `JdiSessionManager` / `JdiSession`; installed skill instructions are tool-use documentation.
- Credited operating / distribution surfaces: CLI commands, daemon/server, JDWP/ADB core and packaged `skills/debroid-cli/SKILL.md`.
- Adjacent first-party surfaces excluded from ownership: Android sample application, Kotlin unit tests, CI/releases/update scripts and contributor workflow; the external Claude/Codex/OpenCode/Cursor agent is not implemented by Debroid.
- First-party operating / deployment modes considered: direct interactive commands, background daemon, multiple debugger sessions, packaged skill loaded by an external agent.
- Recursion level: one deployed debugger tool/service connected to an external agent and Android app.
- Reviewed revision: `b87f489bd02dcfb5c8c37fa2a4340847c9e48adb`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The source has a Clikt command tree that takes explicit command arguments (`launch`, `attach`, `break`, `catch-exception`, `watch`, `poll`, `locals`, `eval`, `set-var`, `step`, `resume`), passes typed requests to a local daemon and serializes debugger results. The daemon accepts socket requests and invokes JDI session methods; `JdiSessionManager` controls attached Android sessions. It does not submit a goal to a model, call an inference provider, select tools by model judgment, or automatically iterate debugging hypotheses. The shipped `SKILL.md` tells **another** agent how to call the CLI, including when to poll and ask the user to act; it is not a packaged autonomous agent actor.

Primary source at exact review ref:

- [README and integration identity](https://github.com/PatilShreyas/debroid/blob/b87f489bd02dcfb5c8c37fa2a4340847c9e48adb/README.md)
- [CLI entry](https://github.com/PatilShreyas/debroid/blob/b87f489bd02dcfb5c8c37fa2a4340847c9e48adb/cli/src/main/kotlin/dev/shreyaspatil/debroid/Main.kt)
- [Typed command-to-IPC execution](https://github.com/PatilShreyas/debroid/blob/b87f489bd02dcfb5c8c37fa2a4340847c9e48adb/cli/src/main/kotlin/dev/shreyaspatil/debroid/cli/CliRunner.kt)
- [Daemon command dispatch](https://github.com/PatilShreyas/debroid/blob/b87f489bd02dcfb5c8c37fa2a4340847c9e48adb/cli/src/main/kotlin/dev/shreyaspatil/debroid/cli/DaemonServer.kt)
- [JDI session management](https://github.com/PatilShreyas/debroid/blob/b87f489bd02dcfb5c8c37fa2a4340847c9e48adb/core/src/main/kotlin/dev/shreyaspatil/debroid/jdi/JdiSessionManager.kt)
- [External-agent skill](https://github.com/PatilShreyas/debroid/blob/b87f489bd02dcfb5c8c37fa2a4340847c9e48adb/skills/debroid-cli/SKILL.md)

## Operational model

The external user or AI agent chooses a diagnostic question and invokes a concrete `debroid` command. The CLI marshals the command to a daemon. The daemon executes a debugger operation on an Android process and returns JSON. The external actor interprets that observation and chooses the next diagnostic action. Persistence of JDI sessions, deferred breakpoints and asynchronous event polling is support machinery, not a decision-making agent loop. Removing the external agent while leaving Debroid's CLI/daemon running removes the open-ended hypothesis → tool selection → observation → revision loop.

## S1 — Operations

- State: —
- Function: Debroid provides operational debugger actions but no first-party autonomous agent S1 that absorbs an open-ended debugging task.
- Disturbance / variety regulated: process attachment, breakpoints, exceptions, stack/variable inspection and debugger command syntax; task-level diagnostic uncertainty remains with the client.
- Decisive decision or feedback right: interpret a debugging objective, choose a diagnostic intervention from results, and decide the subsequent investigative action or completion.
- Decision owner: external AI coding agent or human operator, not the Debroid CLI/daemon.
- Supporting / enforcement mechanisms: command parser, typed IPC requests, daemon, ADB/JDI sessions and JSON response serialization.
- Closure path: external choice → CLI request → daemon/JDI operation → JSON result → external actor's next choice; no autonomous choice returns inside the first-party debugger.
- Why this is / is not agent-owned: debugger execution is deterministic request fulfillment; no packaged model/tool/reasoning loop owns the next diagnostic decision.
- Evidence: `Main.kt`, `CliRunner.kt`, `DaemonServer.kt`, `JdiSessionManager.kt`, packaged `SKILL.md` (links above).
- Basis: explicit integration contract and structural source inspection.
- Confidence: high.
- Caveats: an external AI agent using Debroid can have S1=A at that **larger composed boundary**, which is not this repo's first-party Debroid ownership.

### Absence scope

- Surfaces inspected: README, installed skill, CLI entry/command registration/IPC, daemon dispatch, JDI manager and sample/test separation.
- Plausible first-party paths checked: CLI automatic daemon startup, event polling, expression evaluator, skill-specified debugging workflow and multi-session support.
- Why no material first-party path remains: all require a concrete external command or predefined debugger event; none supplies first-party goal interpretation and model-owned next-action choice.

## S2 — Coordination

- State: —
- Function: no inter-agent S1 interference attenuation path is supplied at the debugger boundary.
- Disturbance / variety regulated: client concurrency and multiple debugger sessions are transport/session concerns, not demonstrated conflict between autonomous S1 units.
- Decisive decision or feedback right: choose an attenuation response to a concrete cross-S1 conflict and return it to subsequent S1 behavior.
- Decision owner: not present; daemon thread handling and session bookkeeping are deterministic.
- Supporting / enforcement mechanisms: socket clients, thread pool, session manager and session-id routing.
- Closure path: command dispatch to a selected debugging session; no S2-specific returned adjustment to distinct autonomous operations.
- Why this is / is not agent-owned: sessions and clients do not become autonomous operational units by multiplexing.
- Evidence: `DaemonServer.kt`, `JdiSessionManager.kt` (links above).
- Basis: structural negative review.
- Confidence: high.
- Caveats: external agents could coordinate their use of Debroid, but that composition is outside the shipped debugger.

### Absence scope

- Surfaces inspected: daemon socket/worker logic, session manager, command dispatch and documented external-agent workflow.
- Plausible first-party paths checked: shared daemon with multiple client sockets, session replacement, synchronized debugger access and events.
- Why no material first-party path remains: no distinct first-party agent S1 pair, evidenced inter-S1 conflict or coordination judgment/feedback loop is present.

## S3 — Inside-and-now control

- State: —
- Function: daemon lifecycle and debugger session management are not discretionary whole-system current control over agent S1 work.
- Disturbance / variety regulated: daemon availability, session attachment, disconnects and stopped Android threads.
- Decisive decision or feedback right: prioritize current agent commitments/resources or make whole-system interventions on their behalf.
- Decision owner: external caller chooses `launch`, `detach`, `resume`, `shutdown` and other control commands; daemon executes them.
- Supporting / enforcement mechanisms: session map, daemon startup/shutdown, per-session operations and thread pool.
- Closure path: explicit external command → deterministic daemon action; no first-party whole-S1 current view and discretionary returned supervisory decision.
- Why this is / is not agent-owned: runtime enforcement of debug state does not own operational commitment choices.
- Evidence: `CliRunner.kt`, `DaemonServer.kt`, `JdiSessionManager.kt`.
- Basis: structural negative review.
- Confidence: high.
- Caveats: operator commands do not establish S3 parent mode without an in-boundary S3 function and returned control loop.

### Absence scope

- Surfaces inspected: daemon/session lifecycle, thread/run control and external CLI control actions.
- Plausible first-party paths checked: daemon manager as supervisor, session replacement and stopping/resuming threads as intervention.
- Why no material first-party path remains: no whole-system view and discretionary resource/commitment decision over autonomous S1 units, whether agent-owned, constructor-owned or parent-returned.

## S3* — Complementary audit

- State: —
- Function: raw debugger inspection is complementary evidence **for an external actor**, not a first-party independent audit judgment loop.
- Disturbance / variety regulated: runtime state, exception events, locals, breakpoints and watched fields.
- Decisive decision or feedback right: independently judge an operational claim against complementary reality and return a corrective finding into control.
- Decision owner: external agent/human who decides which inspection to perform and interprets the JSON result.
- Supporting / enforcement mechanisms: JDI snapshots, variable inspection, event queue and watchpoints.
- Closure path: external request → raw debug result → external judgment; no Debroid-owned corrective audit decision or returned control.
- Why this is / is not agent-owned: evidence access alone does not make the source of evidence its independent evaluator.
- Evidence: `DaemonServer.kt`, `JdiSession.kt`, README and skill (links above).
- Basis: structural negative review.
- Confidence: high.
- Caveats: this tool could support a separate first-party S3* actor in an external agent harness.

### Absence scope

- Surfaces inspected: breakpoints, event polling, variable inspection, expression evaluation, daemon request/response and skill guidance.
- Plausible first-party paths checked: runtime inspection as complementary audit; exception traps as challenge to an ordinary report.
- Why no material first-party path remains: no independent first-party audit actor, semantic judgment or corrective return; the CLI only presents requested observations.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective adaptation of an autonomous harness's future capability is shipped.
- Disturbance / variety regulated: debugger version updates and device/application changes are technical maintenance or present-task debugging concerns.
- Decisive decision or feedback right: evaluate future external changes and select capability adaptations returned into current operation.
- Decision owner: external user/agent/maintainer; no first-party autonomous prospective selector.
- Supporting / enforcement mechanisms: binary update utilities and debugger command repertoire.
- Closure path: release/update or external tool-use decision; no S4 option-to-capability return loop.
- Why this is / is not agent-owned: an updater and a task-specific diagnostic workflow are not future-oriented organizational adaptation.
- Evidence: `cli/src/main/kotlin/dev/shreyaspatil/debroid/cli/update/AutoUpdateManager.kt`, `CliRunner.kt`, README.
- Basis: structural negative review.
- Confidence: high.
- Caveats: developers may improve Debroid across releases, outside the assessed product's autonomous runtime.

### Absence scope

- Surfaces inspected: updater, command tree, README release/install sections, packaged skill and runtime dispatch.
- Plausible first-party paths checked: binary auto-update, agent-guided troubleshooting, device event-driven responses.
- Why no material first-party path remains: none develops and judges external prospective options with a returned autonomous change to current capability.

## S5 — Policy and identity

- State: —
- Function: CLI usage instructions and debugger permissions constrain operations, but no identity/ultimate-policy adjudication is shipped.
- Disturbance / variety regulated: allowed debugger commands, user responsibility, Android process permissions and CLI/skill configuration.
- Decisive decision or feedback right: settle an identity/ultimate-policy issue and return an authoritative governing decision into subsequent operation.
- Decision owner: external user/project maintainer/host agent; the daemon executes fixed commands.
- Supporting / enforcement mechanisms: command arguments, OS/JDWP capabilities, skill instructions and packaged software configuration.
- Closure path: outside decision/configuration → tool invocation; no first-party identity-policy matter → legitimate authority → returned governing decision loop.
- Why this is / is not agent-owned: declarative skill rules and technical access constraints are not S5 decision ownership.
- Evidence: README, `skills/debroid-cli/SKILL.md`, `CliRunner.kt`, `DaemonServer.kt`.
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: an external organization's governance does not become Debroid's packaged S5.

### Absence scope

- Surfaces inspected: CLI command policy, skill instructions, daemon behavior, update/install path and external-agent integration.
- Plausible first-party paths checked: skill rules as constitutional policy, operator stop/approval as parent mode, version update as policy return.
- Why no material first-party path remains: these constrain or transport choices made elsewhere and do not supply a genuine identity-level decision and closure in the shipped tool.

## Recursion

Debroid's daemon sessions, JDI targets and external-agent clients are technical components, not evidenced recursively viable S1 organizations at the assessed boundary.

## Variety and escalation

Typed debugger commands attenuate API/Android runtime complexity into JSON. Debugging uncertainty, hypothesis selection and corrective decisions are escalated to the external AI agent or user. JDI/ADB errors and daemon lifecycle handling are deterministic tool-local recovery.

## Evidence gaps

- Static source-first inspection at the frozen revision only; Android/JDWP native integration tests and external provider-backed agent runs were not executed.
- This exclusion is boundary-relative: Debroid may be valuable as a tool in another harness; such a composition needs its own separate assessment.

## Assessment summary

**Proposed disposition: `excluded-no-agentic-vsm`.** Debroid is an Apache-2.0 headless Android debugger and external-agent tool integration, not a first-party autonomous AI agent harness at the pinned standard-distribution boundary. The external agent owns task interpretation, adaptive tool choice and next-action feedback. No shipped first-party agentic S1 closure is established, so the six-function vector is bounded negative (`— · — · — · — · — · —`).
