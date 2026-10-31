---
harness_id: minecraft-agent-harness
project_name: minecraft-agent-harness
repository: https://github.com/yc-software/minecraft-agent-harness
review_ref: 775d558689f5e4eaa0f1d0d7a320035190b1fce6
reviewed_at: 2026-10-31
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

# minecraft-agent-harness

## Review boundary

- System in focus: The shipped Node.js Minecraft agent runner, including its supported single-agent and team modes, at the frozen commit.
- Purpose and identity: Let model-directed Minecraft players observe, act, communicate and persist while pursuing user-defined world objectives.
- Relevant environment: Minecraft Java server, Mineflayer body and physics, other players/agents, provider APIs, local/Docker/E2B machines and operator configuration.
- Standard-distribution boundary: `minecraft-agent run` and `minecraft-agent team` with the first-party CLI, game/body tools, model-session scheduler, persistent mailbox and optional shared machine.
- Credited operating / distribution surfaces: `src/cli.js`, `src/agent.js`, `src/model/session.js`, `src/tools/game/`, `src/body/`, `src/comms/` and `src/shared-machine/` wired from `bin/minecraft-agent.js`.
- Adjacent first-party surfaces excluded from ownership: Tests, example team definitions, CI, patches for dependencies, documentation and contributor/release processes do not act as runtime VSM decision owners.
- First-party operating / deployment modes considered: Real-provider single-agent and team runs; configured local, Docker or E2B sandbox; optional shared execution; restart and session recovery. The remote model, Mineflayer and the pi SDK are dependencies, not first-party metasystems.
- Recursion level: One configured game-running team as the whole, with individual model-directed players as S1; single-agent mode is the degenerate one-cell case.
- Reviewed revision: `775d558689f5e4eaa0f1d0d7a320035190b1fce6`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI creates a configured Mineflayer body and model session for each agent. `createMinecraftSession` wraps pi's `createAgentSession`, injects fresh world observations before calls, exposes game/workspace/message tools, and persists/resumes the transcript and wake scheduler. Model-selected game tools flow through an interruptible action runner; damage and urgent messages can wake the model, and a child-process supervisor retries reconnections. In team mode `runTeam` starts separate agent processes, a shared SQLite mailbox and optional shared command machine, with identity/directory tools and direct messages. A shared executor queues commands up to a fixed concurrency limit and logs authors, but does not decide how agents partition or renegotiate their Minecraft work. [Architecture](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/docs/architecture.md), [team mode](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/docs/multi-agent.md), [CLI](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/cli.js), [session](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/model/session.js), [agent](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/agent.js).

## Operational model

Each model-directed player has an objective, environment and bounded action discretion. Its LLM chooses tools based on observations; the first-party wrapper executes actions and returns results. In team mode several such operational cells may communicate, but the launcher and shared resources implement transportation/limits rather than a whole-team discretionary manager. Configuration and safety rules are developer/operator-owned. A player's local session recovery and action reaction remain S1 feedback until distinct higher-function evidence is established.

## S1 — Operations

- State: A
- Function: A player autonomously investigates, moves, builds, gathers, interacts and responds to environmental events in pursuit of its game objective.
- Disturbance / variety regulated: Visible world state, danger, hunger/oxygen, location, other players, tools, failed actions and unsolicited messages.
- Decisive decision or feedback right: Interpret observations and select the next tool/action or response at each model turn.
- Decision owner: The model-backed agent in the supported real-provider run; an external LLM supplies inference while the shipped harness closes the acting loop.
- Supporting / enforcement mechanisms: Mineflayer, pi SDK, `transformContext`, tool validation, abortable action runner, event coalescing, timeout and retry guards, session file and sandbox.
- Closure path: World/mailbox observation → model-selected game/communication tool → first-party action runner → new world/tool result and next observation to the model.
- Boundary reachability: `run` and `team` wire the agent session and tools into launched live Mineflayer processes; the path is not merely an example or test.
- Why this is / is not agent-owned: Removing model decision-making leaves deterministic tool execution and restart mechanics, not autonomous choice of game actions; the model is the decisive S1 actor.
- Evidence: [src/agent.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/agent.js), [src/model/session.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/model/session.js), [game tools](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/tools/game/runtime.js), [docs/architecture.md](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/docs/architecture.md).
- Basis: structural.
- Confidence: high.
- Caveats: This is the source-wired agent mode, not an observed claim of gameplay success or safety.

## S2 — Coordination

- State: —
- Function: No shipped S2-specific anti-interference decision/feedback loop among team players was established.
- Disturbance / variety regulated: Concurrent players could obstruct one another or contend for world space and shared-machine resources.
- Decisive decision or feedback right: No first-party explicit inter-player conflict recognition/attenuation decision is wired as team coordination.
- Decision owner: Players may voluntarily negotiate over messages; no separate first-party S2 owner or constructed conflict loop is established.
- Supporting / enforcement mechanisms: Direct messages, SQLite mailbox/read cursors, shared files, process staggering and shared-command queue (concurrency four).
- Closure path: Message/result delivery returns to recipients for optional S1 choices; no guaranteed interference-to-coordination-to-changed-S1 loop is implemented.
- Why this is / is not agent-owned: Messaging and command concurrency can support collaboration but do not, by themselves, identify a particular interference and close its mutual adjustment.
- Evidence: [docs/multi-agent.md](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/docs/multi-agent.md), [src/tools/game/communication.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/tools/game/communication.js), [src/shared-machine/server.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/shared-machine/server.js).
- Basis: structural.
- Confidence: medium.
- Caveats: A team can invent agreements at runtime; this does not establish a shipped S2-specific harness path.

### Absence scope

- Surfaces inspected: Team CLI, multi-agent guide, communication tools, mailbox store, shared command-server queue, agent configuration and model session.
- Plausible first-party paths checked: Peer messages, shared plans/files, command admission, process staggering and team objectives for evidence of a specific conflict detector/negotiation protocol and corrective return.
- Why no material first-party path remains: The supplied paths transport work and cap executor concurrency; they do not implement an inter-S1 interference-specific regulatory relation. Hypothetical agent-authored negotiations require unprovided behavior.

## S3 — Inside-and-now control

- State: —
- Function: No current whole-team resource/priority/commitment control with discretionary intervention was found.
- Disturbance / variety regulated: Team capacity, child exits, tool timeouts and objective progress.
- Decisive decision or feedback right: No operational actor revises cross-player priorities or shared commitments from a team-wide current view.
- Decision owner: Operator sets team objective, models and shared-machine settings before start; launcher/supervisor execute fixed constraints.
- Supporting / enforcement mechanisms: Static team config, per-agent scheduler, spawn stagger, child restart, command queue and watchdog.
- Closure path: Per-player restarts and tool-result events return to individual S1s; no whole-team S3 decision is returned to regulate all cells.
- Why this is / is not agent-owned: Starting multiple agents, retrying a failed child or enforcing concurrency does not supply a decisive team manager or parent-governed S3 mode.
- Evidence: [src/cli.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/cli.js), [src/model/session.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/model/session.js), [src/shared-machine/server.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/shared-machine/server.js).
- Basis: structural.
- Confidence: high.
- Caveats: An external human may manually coordinate the team; that is not a first-party closed parent-mode S3 path at this boundary.

### Absence scope

- Surfaces inspected: CLI team supervisor, configuration, per-agent scheduler, shared execution, game tool definitions and team documentation.
- Plausible first-party paths checked: Child lifecycle/restart, shared resource queue, agent directory and common objective for current whole-system sensing, discretionary allocation and returned intervention.
- Why no material first-party path remains: These implement fixed launch/liveness and individual operations, not a team-wide current-regulation judgment and subsequent cross-unit control.

## S3* — Complementary audit

- State: —
- Function: No independent operational-claim audit with corrective return is implemented in the game-running distribution.
- Disturbance / variety regulated: Incorrect game-status and completion claims.
- Decisive decision or feedback right: No complementary independent judgment can challenge the agent's ordinary progress report and cause controlled correction.
- Decision owner: The same agent observes the world for its own next actions; development tests are not runtime reviewers.
- Supporting / enforcement mechanisms: World observations, diagnostic telemetry, session history and command log.
- Closure path: Ordinary observations return to the producing S1; logs/test assertions do not drive separate audit-to-control intervention.
- Why this is / is not agent-owned: A second raw observation or saved history is not independent S3* ownership without an independently controlled challenge and returned finding.
- Evidence: [src/agent.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/agent.js), [src/model/session.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/model/session.js), [docs/architecture.md](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/docs/architecture.md).
- Basis: structural.
- Confidence: high.
- Caveats: A player/server operator may inspect logs independently outside the shipped control path.

### Absence scope

- Surfaces inspected: Session observations and telemetry, shared-machine author log, agent callbacks and tests/docs.
- Plausible first-party paths checked: Model observations, event records, command log and team peer messages for an independent audit actor, evidence bypass and corrective feedback.
- Why no material first-party path remains: Those are ordinary operating/replay surfaces; no separately controlled challenge-to-correction loop is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: No external-and-prospective adaptation of harness/team capability is established.
- Disturbance / variety regulated: Future world goals, provider changes and new game conditions could require adaptation.
- Decisive decision or feedback right: No first-party actor judges prospective options and changes later harness capability from external distinctions.
- Decision owner: Agents plan current gameplay; developer/operator changes models, tools and configuration outside the runtime adaptation loop.
- Supporting / enforcement mechanisms: Transcript persistence, experience history, tool extensibility and reconnect resume.
- Closure path: Memory and world changes inform current S1 decisions, not an outside/then capability-change loop through present control.
- Why this is / is not agent-owned: Survival adaptation and task planning in the live world are S1, not necessarily prospective organizational S4.
- Evidence: [src/model/session.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/model/session.js), [docs/architecture.md](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/docs/architecture.md), [src/config.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/config.js).
- Basis: structural.
- Confidence: high.
- Caveats: Model reasoning may form future game plans, but no supported system-level S4 return into capability was found.

### Absence scope

- Surfaces inspected: System prompt, game session/compaction/recovery, team settings, tool extension entry points and architecture documentation.
- Plausible first-party paths checked: Persistence, planned game objectives, provider configuration and dynamic event response for prospective environmental modeling and persistent capability adaptation.
- Why no material first-party path remains: Shipped changes govern current gameplay or human-edited configuration; no prospective option-adoption loop is wired at team/harness recursion.

## S5 — Policy and identity

- State: —
- Function: No ultimate-policy/identity adjudication and return path is supplied at the team boundary.
- Disturbance / variety regulated: Safety, operator-set role/objective and permitted world/shell actions.
- Decisive decision or feedback right: No legitimate runtime authority resolves identity-level tension and returns binding policy to subsequent operations.
- Decision owner: Developer/operator specify objectives, prompts, team settings and static guards; models choose within those boundaries.
- Supporting / enforcement mechanisms: Chat slash-command guard, tool schemas, action limits, per-agent sandboxes and configuration.
- Closure path: Refused actions or changed settings affect ordinary current operation; no identity-policy proposal → ultimate parent decision → returned binding policy channel is shipped.
- Why this is / is not agent-owned: Static role descriptions and operator controls do not establish S5 merely because they constrain agents.
- Evidence: [src/config.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/config.js), [src/prompt.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/prompt.js), [src/body/chat-guard.js](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/src/body/chat-guard.js), [docs/configuration.md](https://github.com/yc-software/minecraft-agent-harness/blob/775d558689f5e4eaa0f1d0d7a320035190b1fce6/docs/configuration.md).
- Basis: structural.
- Confidence: high.
- Caveats: Human ability to edit configuration or stop a process does not establish the function-specific parent closure.

### Absence scope

- Surfaces inspected: CLI/configuration, prompts, permissions/game guard, team deployment, messages and session/control docs.
- Plausible first-party paths checked: Team objective/personality changes, provider and tool policy, sandbox controls and messaging for identity-level issue escalation to legitimate authority and binding return.
- Why no material first-party path remains: They are preselected settings, lower-level action refusal and ordinary communication, without a shipped ultimate-policy decision conversation.

## Distributed OSS parent arrangement

The MIT codebase can be installed by independent operators. Its public developer workflow does not instantiate a shared organization-level parent for game-running cells. A local operator can change team configuration, but no first-party S3/S4/S5 parent-return mode is established by that control alone.

## Self-hosted and non-human modes

Local/Docker/E2B machines and a real model provider support the same operational choice loop. Optional team mode adds multiple S1 agents, not an automatically viable recursive organization. Deterministic restart, queue and guard controls do not own the discretionary organizational decisions they enforce.

## Recursion

Each player can persist and regulate local action, but the code does not establish a complete lower-level metasystem for each player or a team-level identity/current/future governance closure. Team nesting is not itself a VSM recursion proof.

## Variety and escalation

Perception and tool schemas attenuate action choices; urgent events amplify timely S1 feedback, with errors backed off and reconnections resumed. A child failure is retried by deterministic code. No exception path to a distinct higher whole-system authority or proven algedonic channel was credited.

## Evidence gaps

Static source-pinned assessment; no live Minecraft world, paid-provider E2E, stability, security or coordination outcome trial. Generic peer negotiation may be constructed by users, but no specific first-party conflict protocol was found in the shipped sources. Future implementation changes require a new-ref review.
