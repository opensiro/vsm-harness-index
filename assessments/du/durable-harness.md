---
harness_id: durable-harness
project_name: durable-harness
repository: https://github.com/vercel-labs/durable-harness
review_ref: ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# durable-harness

## Review boundary

- System in focus: the shipped `durable-harness` TypeScript package at frozen `ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741`, including its first-party `pi()` agent factory, model/host-tool composition, durable `Agent`/session/handler/chat-route construction, virtual/sandbox coding tools, Pi-durable storage/resume bridge, external CLI adapters and Workflow SDK World scheduling.
- Purpose and identity: expose AI coding-agent sessions as durable workflow runs where conversation, model/tool calls, tool effects and resumption are recorded in a World, with host tool execution isolated from the server Function.
- Relevant environment: a developer's program providing model/credentials/tools, user chat sessions, virtual or Vercel Sandbox workspace, Workflow SDK World log/queue, model provider, optional Pi SDK, optional OpenCode/Claude Code/Codex peers and distributed restarts.
- Standard-distribution boundary: package's first-party `pi({ model, tools, instructions })` composition with `kernelAgent` and first-party `createCodingTools`, and its durable session workflow. The model/tool loop is implemented by supported Pi agent/harness peer libraries (`harness-world-pi`, `pi-agent-core`), invoked via the first-party published factory and offered real first-party workspace tools. The separately installed Claude Code/Codex/OpenCode CLIs and custom downstream `durableAgent({ harness: myHarness })` do not supply the positive S1 claim.
- Credited operating / distribution surfaces: `packages/durable-harness/src/{pi,agent,workspace,environments,world,flow,registry,tools,pi-durable,sandbox-harness}.ts`; published package `./pi`, `./pi-durable` and chat/flow routes; direct first-party model/tool wiring and real built-in virtual/sandbox tool feedback under the supported Pi mode.
- Adjacent first-party surfaces excluded from ownership: CI/build/release scripts, benchmark tests, example applications as proof of default deployment, docs for remote Vercel services, user-authored harness/agent, telemetry-only hooks and the separate lower-level policy of Claude/Codex/OpenCode agent runtimes.
- First-party operating / deployment modes considered: `pi({model,tools})` with first-party coding tools on a durable virtual workspace or sandbox; `piHarness()` raw integration; standalone `pi-durable` `resumeWith(Harness.open)` storage adapter; `durableAgent(custom harness)`; external Claude Code/Codex/OpenCode adapters; session chat route/queue/restart and token/trace policies. Positive operational ownership is specifically from the first mode.
- Recursion level: one first-party constructed Pi coding agent hosted as a durable session; the package may host many sessions, but a World queue is not assumed to form an S2 or S3 metasystem without a specific inter-session regulatory decision/feedback relation.
- Reviewed revision: `ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741`.
- Observation date: 2026-10-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The package is not itself a new language-model reasoning kernel. Its `Agent` interface is a durable session and server surface; `kernelAgent` registers a supplied `Harness` with Workflow SDK `World`, `durableSessions`, a queue consumer and a resumable chat route. `durableAgent` accepts user-supplied harnesses; adapters for Claude Code and Codex launch their own sandboxed runtimes. Those paths alone would be lifecycle machinery around an outside agent.

There is one narrower, material first-party operational path. The published `durable-harness/pi` factory takes a model and optional custom host tools, constructs a Pi model/provider stream, calls the supported `rawPiHarness` agent-core composition with instructions and tools, and returns a concrete `Harness` whose `drive(ctx)` invokes that agent on the World-backed session. First-party `createCodingTools` registers `read`, `bash`, `edit` and `write` tools on virtual or Vercel Sandbox workspace semantics. The model-backed Pi actor selects tool invocations from a task; the host tools execute and report results; the Pi peer runtime supplies iterative model/tool recurrence; `durableSessions` persists and resumes this operating session. The first-party **composition and supported invocation path**, not a claimed in-repository reimplementation of `pi-agent-core`, is the basis for S1=A.

Other branches must not be conflated. `pi-durable` deliberately says `Harness.open()` is Pi's own autonomous runtime and this package supplies `WorldStorage`, `resumeWith` and backstop; it is not an independent S1 witness. `fxTools()` supplies tools to libfx's own agent. Claude Code/Codex run vendor agents in sandboxes, not locally owned coding brains. The World queue and session fencing stabilize processing after crashes, but no first-party autonomous meta-manager over a population of these S1s is shown. Observability/authorization/budget gates do not themselves decide independent audit, prospective organization design or ultimate policy.

Primary frozen evidence:

- [`packages/durable-harness/src/pi.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/pi.ts) — public `pi()`, dynamic Pi provider/model construction, `rawPiHarness` and `drive(ctx)` return, first-party coding host tools.
- [`packages/durable-harness/src/agent.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/agent.ts) — `durableAgent`/`kernelAgent` and first-party durable sessions/chat/queue registration.
- [`packages/durable-harness/src/workspace.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/workspace.ts) — virtual/sandbox workspaces.
- [`packages/durable-harness/src/flow.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/flow.ts) — common durable queue handler routing sessions to the correct registered harness.
- [`packages/durable-harness/src/pi-durable.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/pi-durable.ts) — Pi-owned `Harness.open` vs first-party durability adapter distinction.
- [`packages/durable-harness/src/claude-code.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/claude-code.ts) and [`codex.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/codex.ts) — adjacent external agent driver modes.
- [`packages/durable-harness/package.json`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/package.json) — published `./pi`, `./pi-durable` modes and optional Pi/agent peer dependencies.

## Operational model

Supported `pi()` application constructs a Pi model and registers first-party host tools → a user starts/sends a durable session → the World-backed kernel invokes Pi's `drive(ctx)` → Pi model processes objective/history, chooses registered tool or response → first-party workspace tool executes and returns data → Pi receives the observation and chooses its next action. Crash/replay semantics reconstruct the operation from the event log. In this composite standard-distribution mode the autonomous operational choice is model-owned and the first-party factory supplies the concrete configured actor, work tools and return channel; other vendor CLI modes are excluded from attribution.

## S1 — Operations

- State: A
- Function: perform a task-specific model/tool coding operation using a published first-party Pi agent factory with real workspace tools and feedback.
- Disturbance / variety regulated: varying chat objectives, file contents, shell results, editing alternatives, failed commands and interrupted durable execution.
- Decisive decision or feedback right: Pi model actor selects the next `read`, `bash`, `edit`, `write` or response action after seeing task/session evidence and previous tool results.
- Decision owner: model-backed Pi actor instantiated by first-party `pi()` mode; imported Pi agent-core drives the recurrence, while first-party durable-harness supplies its registered tools, configured model and session route. The World queue and tools enforce/transport choices without exercising coding discretion.
- Supporting / enforcement mechanisms: `rawPiHarness`, configurable provider `streamFn`/model, `kernelAgent`/durableSessions, host coding tools, virtual/sandbox workspace, event log replay, sandbox fencing and session time budgets.
- Closure path: chat/session → first-party constructed Pi agent `drive` → model request/tool selection → first-party workspace tool returns result → Pi agent observes result and continues; state survives restarts in World.
- Boundary reachability: `./pi` is an exported package entrypoint and its documented `pi({model, tools:[...createCodingTools(virtual())]})` returns a registered `Agent` with operational `chatRoute`/queue handler; it is not a test-only wrapper or project plan.
- Why this is / is not agent-owned: without the model-backed Pi actor, durability and tool adapters can persist/run fixed work but cannot choose task-specific next edits from evidence. Without first-party `pi()` composition, external CLI processes are still agents but do not make this package's supported Pi actor appear.
- Evidence: [`pi.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/pi.ts); [`agent.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/agent.ts); [`package.json`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/package.json).
- Basis: explicit + structural construction.
- Confidence: medium-high for exported first-party construction; imported Pi library supplies loop internals, and no model/provider run was performed.
- Caveats: `pi()` requires installation of optional compatible Pi peers and a configured model/credential; this is a supported opt-in standard mode, not a claim all `durable-harness` deployments use it. An arbitrary custom `durableAgent` or external Claude/Codex CLI path does not automatically own S1 at this repository boundary.

## S2 — Coordination

- State: —
- Function: durable session queueing and workspace isolation are shown, but no first-party inter-S1 interference regulation with an autonomous coordination return loop is established.
- Disturbance / variety regulated: concurrent turns, duplicate queue deliveries, crash retries and stale writers can interfere in a **single session**; the kernel serializes/fences these. Multiple independent coding sessions can coexist but no shared-workspace collision/negotiation between two agent-owned S1 units is demonstrated.
- Decisive decision or feedback right: choose a coordination intervention based on concrete interference between distinct S1 units and return it to their future operational behavior.
- Decision owner: fixed World queue/lease/fence behavior for per-session consistency; no dedicated cross-S1 agentic coordinator identified.
- Supporting / enforcement mechanisms: `durableSessions`, `World` event log/queue, sandbox fencing, per-session route, workspace locking and serialization.
- Closure path: message enters one session's queue → workflow dispatches correct `Harness` and preserves exactly-once-ish observed effects → that same session continues. No separate inter-S1 conflict observation → coordination judgment → changed sibling S1 commitments path was found.
- Why this is / is not agent-owned: same-session durability and worker-leasing correctness are not themselves a first-party S2 metasystem; queue dispatch does not imply inter-S1 functional regulation.
- Evidence: [`agent.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/agent.ts); [`flow.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/flow.ts); [`pi-durable.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/pi-durable.ts).
- Basis: structural absence.
- Confidence: medium-high.
- Caveats: a downstream app could combine multiple agents sharing state and supply its own S2 policy; such composition is outside this review.

### Absence scope

- Surfaces inspected: session/world queue, durable message routing, virtual/sandbox workspace, fencing/recovery, agent registration and chat API.
- Plausible first-party paths checked: session serialization as S2, global flow handler as coordinator, queue consistency as inter-agent conflict management and sandbox fencing as S2.
- Why no material first-party path remains: mechanisms protect one session's replay/execution and route independent sessions, without a concrete first-party cross-S1 disturbance-to-feedback relation.

## S3 — Inside-and-now control

- State: —
- Function: no independent first-party whole-current portfolio manager owns priorities/resources/commitments of multiple live durable agents.
- Disturbance / variety regulated: request deadlines, process crashes, session state, message backlogs and unfinished tool effects are recovered under fixed policies, not evaluated as a changing mission-wide portfolio.
- Decisive decision or feedback right: review all current agent commitments and change their relative priorities/resources or interventions.
- Decision owner: app developer/operator chooses agents, models, budgets and messages; deterministic queue/backstop enforces per-session running conditions.
- Supporting / enforcement mechanisms: `Agent.sessions`, `World` queue, handler registry, `maxInvocationMs`/deadline margin, telemetry, backstop and explicit chat API.
- Closure path: per-session event log → handler/backstop resumes work by fixed rule. No whole-system managerial view → discretionary current control → altered distributed S1 commitment path is supplied.
- Why this is / is not agent-owned: durable infrastructure and session list/close/send APIs do not instantiate a standing current-control actor; arbitrary downstream scheduling code is not credited.
- Evidence: [`agent.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/agent.ts); [`flow.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/flow.ts); [`pi-durable.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/pi-durable.ts).
- Basis: structural absence.
- Confidence: medium-high.
- Caveats: an application parent can govern its agent fleet through these APIs but is not a complete shipped mode of this package.

### Absence scope

- Surfaces inspected: registration/registry, session/handler APIs, queue and backstop, timeouts, instrumentation and app-supplied chat/agent configurations.
- Plausible first-party paths checked: durable queue as S3, session list/close API as parent S3=P, recovery backstop as manager, and model choice as resource control.
- Why no material first-party path remains: available APIs expose operations without a complete first-party whole-current decision-and-return loop.

## S3* — Complementary audit

- State: —
- Function: tracing, checkpoints, replay and tool-result observation do not create a separate independent audit challenge to agent claims.
- Disturbance / variety regulated: lost events, model/tool errors, partial effects, bad tool output and untrusted public routes can be recorded or prevented, but no autonomous independent judgment of task correctness was established.
- Decisive decision or feedback right: independently test a production S1's completion/evidence claim and return correction that changes subsequent work.
- Decision owner: none established; deterministic replay/trace machinery records/guards, and any model self-correction remains within Pi's production loop.
- Supporting / enforcement mechanisms: OpenTelemetry/Agent Runs, event-log checkpoints, `replay:'safe'|'never'`, crash handling, route authorization and sandbox safety checks.
- Closure path: model/tool event → durable log/trace and retry semantics → production session continues. No separate evidential reviewer → assessment → corrective return is wired.
- Why this is / is not agent-owned: extra logging/validation of execution semantics is not complementary independence from the acting Pi model.
- Evidence: [`pi.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/pi.ts); [`instrumentation/checkpoints.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/instrumentation/checkpoints.ts); [`agent.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/agent.ts).
- Basis: structural absence.
- Confidence: high.
- Caveats: downstream applications could add independent judges; none is automatically supplied by durable trace storage.

### Absence scope

- Surfaces inspected: agent runs tracing, checkpoints, tool-effect replay, chat response errors, code tests and sandbox authorization.
- Plausible first-party paths checked: trace/checkpoints as independent evidence path, replay status as an auditor, tool errors as S3* and downstream custom harness as first-party reviewer.
- Why no material first-party path remains: all checked mechanisms report or enforce the production session rather than instantiate a distinct independent audit owner and return loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-facing prospective learning/capability redesign actor was found.
- Disturbance / variety regulated: provider availability, deployment restarts, future queue arrivals and workload durations vary, but the package preserves/restarts configured harnesses instead of choosing future strategic alternatives.
- Decisive decision or feedback right: assess external future conditions and adopt a changed organizational capability or tool repertoire.
- Decision owner: application author/config controls harness selection, model/tools and world; deterministic recovery policies follow existing settings.
- Supporting / enforcement mechanisms: durable log, backstop timers, model provider configuration, workspaces, extensible `durableAgent` harness factory and deployment options.
- Closure path: no external/future signal → first-party prospective option generation → adoption decision → changed future capability loop is instantiated. Resumption retains the existing capability, not a new strategy.
- Why this is / is not agent-owned: a saved or resumed agent session is continuity of S1, not prospective S4 adaptation.
- Evidence: [`agent.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/agent.ts); [`pi-durable.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/pi-durable.ts); [`workspace.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/workspace.ts).
- Basis: structural absence.
- Confidence: high.
- Caveats: developer plugins/custom harnesses may implement their own S4, but generic `durableAgent` composition does not supply one.

### Absence scope

- Surfaces inspected: first-party Pi agent factory, world/session lifecycle, sandbox/virtual tools, recovery, versioned providers and exported customization APIs.
- Plausible first-party paths checked: World replay as organizational learning, backstop as proactive strategy, provider choice as S4 and custom harness extension as first-party adoption.
- Why no material first-party path remains: mechanisms preserve current configured operation and lack a distinct future-facing option/selection/persistent capability feedback owner.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate-purpose/identity policy adjudication loop for the durable agent organization is established.
- Disturbance / variety regulated: route authentication, public sandbox budget, tool permissions, trusted workspaces and deployment configuration constrain what a session may do.
- Decisive decision or feedback right: resolve a governing identity/ultimate-policy conflict under legitimate authority and return that ruling as durable policy affecting later autonomous operations.
- Decision owner: app developer/operator sets auth/model/tools/budgets and supplies session purpose; runtime only checks configured limits.
- Supporting / enforcement mechanisms: `chatRoute.authorize`, `allowPublicSandbox`, sandbox cost/fencing, model/tools/instructions option and World session storage.
- Closure path: app author selects permissions and config → first-party route/handler checks enforce them. No first-party identity conflict/legitimate ultimate authority judgment/revised authoritative policy return is shown.
- Why this is / is not agent-owned: permissions and cost limits enforce already selected operational boundaries; neither prove dynamic governance of the agent organization's ultimate identity.
- Evidence: [`agent.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/agent.ts); [`sandbox-harness.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/sandbox-harness.ts); [`pi.ts`](https://github.com/vercel-labs/durable-harness/blob/ea8aa4060cf4fb8cd39737ce8ab21c4e0f40c741/packages/durable-harness/src/pi.ts).
- Basis: structural absence.
- Confidence: high.
- Caveats: application owner legitimately governs the wider deployed product; that authority is not a shipped S5 policy-closure loop in this reusable package.

### Absence scope

- Surfaces inspected: chat authorization, publicly exposed sandbox protections, model/instructions config, session identifiers, registration names, budgets and sandbox execution isolation.
- Plausible first-party paths checked: `authorize` callback as S5=P, `allowPublicSandbox` as identity gate, sandbox budget as policy, agent name as identity and model instructions as durable constitution.
- Why no material first-party path remains: the observed controls accept external configuration and enforce access/cost, but do not decide and return ultimate organizational policy.

## Recursion

The credited recursion is the concrete Pi coding session instantiated through the published first-party factory and registered onto durable workflow infrastructure. The same package can host separately implemented Claude/Codex/OpenCode agents or developer-defined harnesses, but their autonomy is not counted as first-party function ownership. Multiple durable sessions do not automatically form a new viable metasystem.

## Variety and escalation

Durability attenuates machine/process variety with intent-before-effect records, replay rules, queue continuation, sandbox fencing, virtual workspaces and registration/route checks. The Pi operating actor amplifies task-response variety by selecting model-driven tools from real feedback. Parent app configuration controls access and model/tool selection; no observed independent portfolio manager, evidence auditor, future adaptation actor or identity adjudicator closes the higher functions.

## Evidence gaps

- Source-first at immutable commit, no live model/provider/Pi agent/Claude/Codex/Browser quality execution. Script and repository contract checks support artifact integrity, not LLM reliability.
- S1=A rests on the explicitly exported first-party `pi()` agent **composition** using a compatible optional peer Pi runtime; the model/tool recurrence implementation belongs to that peer. The annotation does not credit every custom or vendor harness run through this package.
- Inter-session interference, separate whole-current prioritization, independent review and prospective governance cannot be inferred from queue names, session logs or built-in Vercel integration.
- This is an experimental 0.0.x package according to its README. No production viability or crash-recovery performance was measured here.

## Assessment summary

The first-party standard distribution can instantiate a model-driven Pi agent with registered coding tools and real feedback through its published `pi()` path, so the narrow supported operational S1=A claim is justified. Its main durable infrastructure preserves those operations across restarts but does not by itself establish S2/S3/S3*/S4/S5 as independently owned VSM functions. This result is bounded to the supported Pi construction rather than borrowing autonomy from the separately launched Claude/Codex/OpenCode agent runtimes.
