---
harness_id: tinyagi
project_name: TinyAGI
repository: https://github.com/TinyAGI/tinyagi
review_ref: 2db3a03a891b302c460f624d6c5a0523b8aa3528
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-21
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TinyAGI

## Review boundary

- System in focus: the first-party TinyAGI runtime/control layer at pinned revision `2db3a03a891b302c460f624d6c5a0523b8aa3528`, including its daemon/queue processor, provider adapters, per-agent workspace/config/prompt assembly, team handoff/chat-room protocol, SQLite queues, schedules/heartbeat, channels, plugins, server APIs and TinyOffice management surfaces.
- Purpose and identity: provide a continuously running local multi-agent/multi-team environment around terminal-agent CLIs, with isolated workspaces, persistent routing/state, team collaboration, external channels and operator management.
- Relevant environment: human operator; Claude Code, Codex CLI and OpenCode/provider runtimes; model/provider services behind those CLIs; Discord/Telegram/WhatsApp/API clients; repositories/files acted on by the spawned agents; local filesystem, SQLite and OS process environment.
- Standard-distribution boundary: TinyAGI owns message intake/routing, queue durability/retry/recovery, team/tag parsing, workspace and prompt construction, process invocation/lifecycle, schedules/heartbeat, channels, persistent chat/agent history, APIs and management UI. The autonomous planning/tool/action loops inside `claude`, `codex` and other supported agent CLIs remain adjacent runtimes. Calling those CLIs with a TinyAGI-built system prompt does not by itself transfer their task-level decision loop into first-party TinyAGI ownership.
- Credited operating / distribution surfaces: `packages/main/src/index.ts`; `packages/core/src/invoke.ts`; `packages/core/src/adapters/*`; `packages/core/src/agent.ts`; `packages/core/src/queues.ts`; `packages/core/src/router.ts`; `packages/core/src/schedules.ts`; `packages/core/src/memory.ts`; `packages/main/src/heartbeat.ts`; `packages/teams/src/*`; server APIs; bundled `.agents/skills/*`; TinyOffice runtime management surfaces.
- Adjacent first-party surfaces excluded from ownership: repository CI/release workflows, development tests/docs/examples and design/marketing material not wired into the shipped runtime. External CLI internals, model/provider reasoning, their private planners/tool loops/approvals/session logic and external services are not credited as TinyAGI-owned VSM functions.
- First-party operating / deployment modes considered: background daemon and container operation; single-agent and multi-agent operation; team leader routing and agent-to-agent handoffs; parallel per-agent queue processing; persistent chat rooms; scheduled and heartbeat-triggered invocation; multiple supported CLI providers; TinyOffice/API/CLI management.
- Recursion level: the TinyAGI daemon/team runtime. Individual spawned CLI agents may each be viable lower-recursion systems, but their autonomous internal operation is not inherited by TinyAGI solely because TinyAGI configures, invokes, routes and observes them.
- Reviewed revision: `2db3a03a891b302c460f624d6c5a0523b8aa3528`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

TinyAGI provides substantial first-party runtime infrastructure. `packages/main/src/index.ts` receives and claims queued work, chooses a configured agent, invokes it, persists responses, applies retry/dead-letter behavior and forwards team responses into the first-party handoff/chat-room layer. `docs/QUEUE.md` documents SQLite transactional message state, per-agent sequential promise chains, cross-agent parallelism, stale-message recovery and dead-letter handling. `docs/TEAMS.md` documents team leader routing, fan-out and direct agent-to-agent handoffs, persistent team chat rooms and loop caps.

The actor boundary is nevertheless explicit in implementation. `packages/core/src/invoke.ts` builds the TinyAGI system prompt/workspace configuration, resolves a provider adapter and delegates execution to that adapter. The Claude adapter spawns the external `claude` command with the prompt/message; the Codex adapter spawns `codex exec` / `codex exec resume`. The returned CLI output is then parsed by TinyAGI and fed back into its queue/team machinery. `docs/AGENTS.md` likewise states that conversation history is managed by the Claude/Codex CLI and illustrates the queue processor ending at those CLI processes.

Team collaboration does not introduce a hidden first-party planner. `docs/TEAMS.md` explicitly says “No central orchestrator — agents communicate directly.” `packages/teams/src/routing.ts` parses `[@teammate: message]` and `[#team: message]` tags that appear in an agent response, while `packages/teams/src/conversation.ts` deterministically validates and enqueues those selected recipients. Thus TinyAGI owns the transport/validation semantics, but the choice to hand off, fan out or post to a chat room originates in the adjacent CLI agent response.

Schedules, heartbeat, memory and bundled skills extend the operating substrate without changing that ownership result. The heartbeat reads a configured markdown prompt and enqueues it to an agent. The scheduler enqueues configured messages on cron/one-time triggers. The memory module indexes first-party workspace memory files into the next system prompt, and the bundled memory skill instructs the running agent how to create/update/reorganize those files. Those mechanisms persist and re-present context, but the discretionary choice of what the context means and what to do next remains inside the external CLI agent.

Primary evidence:

- [`packages/main/src/index.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/main/src/index.ts) — queue processing, agent routing/invocation, per-agent promise chains, team-response handling and runtime lifecycle.
- [`packages/core/src/invoke.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/invoke.ts) — first-party workspace/prompt/provider assembly followed by delegation to a provider adapter.
- [`packages/core/src/adapters/claude.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/adapters/claude.ts) — spawns the external `claude` CLI and returns/parses its agent output.
- [`packages/core/src/adapters/codex.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/adapters/codex.ts) — spawns external `codex exec` / resume and returns/parses its agent output.
- [`docs/TEAMS.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/docs/TEAMS.md) — direct agent collaboration with no central orchestrator, handoff/fan-out mechanics, persistent chat room and loop protection.
- [`packages/teams/src/routing.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/teams/src/routing.ts) and [`packages/teams/src/conversation.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/teams/src/conversation.ts) — deterministic parsing/validation/enqueueing of handoffs chosen in agent responses.
- [`docs/QUEUE.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/docs/QUEUE.md) — durable queue, per-agent ordering, retries/dead letters and stale recovery.
- [`packages/core/src/agent.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/agent.ts) — system-prompt construction from first-party instructions, team data, memory and user configuration.
- [`packages/main/src/heartbeat.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/main/src/heartbeat.ts) and [`packages/core/src/schedules.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/schedules.ts) — timed re-invocation by enqueuing prompts to configured agents.
- [`packages/core/src/memory.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/memory.ts) and [`.agents/skills/memory/SKILL.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/.agents/skills/memory/SKILL.md) — persistent memory indexing plus an instruction surface executed by the external agent.

## Operational model

A channel/API/schedule/heartbeat message enters TinyAGI's SQLite queue. The first-party processor selects a target agent or configured team leader, batches/serializes work per agent, builds the workspace/system prompt and starts the configured terminal-agent CLI. That adjacent CLI performs the autonomous task interpretation and tool/reasoning loop, returning text/events to TinyAGI. TinyAGI records/streams the result and parses first-party handoff/chat-room syntax; if the external agent chose a teammate, TinyAGI deterministically enqueues another invocation. Failures are retried and can become dead-letter records; stale in-flight work can be recovered.

The counterfactual owner test is decisive. Remove Claude Code/Codex/OpenCode while leaving the TinyAGI daemon, queue, teams, scheduler, heartbeat, memory index and UI intact: messages can still be stored, routed, scheduled, retried and managed, but no first-party actor remains that can interpret an arbitrary request, choose tools/actions, judge evidence or decide that a teammate should receive a novel subtask. Remove TinyAGI while leaving one of those CLIs: that CLI still contains its own autonomous agent loop, although it loses TinyAGI's durable multi-agent organization. The standard TinyAGI distribution therefore does not establish first-party autonomous S1 ownership at the declared repository boundary.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit closes the general task-level decision/action loop inside the TinyAGI repository boundary.
- Disturbance / variety regulated: arbitrary user/project requests, tool/environment observations, implementation failures, repository state and task ambiguity.
- Decisive decision or feedback right: interpret the request and observations, choose the next substantive plan/tool/action, evaluate returned evidence and revise execution.
- Decision owner: the configured external terminal-agent CLI process, such as Claude Code or Codex CLI.
- Supporting / enforcement mechanisms: TinyAGI queue, routing, prompt construction, isolated workspaces, provider adapters, process lifecycle, schedules, heartbeat, plugins and response delivery.
- Closure path: request → TinyAGI queue/router/prompt builder → external CLI agent reasoning/tool loop → response/events → TinyAGI persistence/routing → external CLI agent on the next invocation or continuation. The autonomous task loop closes in the adjacent runtime.
- Why this is / is not agent-owned: first-party code spawns and configures an already-agentic CLI; the Claude adapter literally executes `claude`, and the Codex adapter executes `codex exec`. TinyAGI does not implement the task-level choice loop those commands perform.
- Evidence: [`packages/core/src/invoke.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/invoke.ts), [`packages/core/src/adapters/claude.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/adapters/claude.ts), [`packages/core/src/adapters/codex.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/adapters/codex.ts), [`docs/AGENTS.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/docs/AGENTS.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: an assembled TinyAGI deployment is plainly agentic because it includes external autonomous agents. This finding concerns repository-relative first-party ownership, not whether the complete deployment performs autonomous work.

### Absence scope

- Surfaces inspected: daemon/queue processor; provider adapters; prompt/workspace assembly; team runtime; scheduler/heartbeat; memory/skills; server/API and management surfaces.
- Plausible first-party paths checked: provider adapter as S1; TinyAGI system prompt as transfer of S1 ownership; scheduled/heartbeat execution as S1; team leader wrapper as a first-party operational agent.
- Why no material first-party path remains: every general autonomous task choice still requires an adjacent terminal-agent CLI; first-party code supplies organization, persistence, context and process control around that actor.

## S2 — Coordination

- State: —
- Function: TinyAGI implements meaningful cross-agent coordination substrate, but the coordinated autonomous S1 units at this recursion are adjacent CLI agents rather than first-party TinyAGI operations.
- Disturbance / variety regulated: message ordering, conflicting concurrent invocation of one agent, team handoffs, fan-out/backflow/cross-talk, runaway handoff chains and shared team visibility.
- Decisive decision or feedback right: choose whether a novel task should be handed off/fanned out and what commitment/message another operational unit should receive.
- Decision owner: the external CLI agent chooses teammate/chat-room tags in its response; TinyAGI validates, orders and enqueues those choices.
- Supporting / enforcement mechanisms: per-agent promise chains, team membership/leader configuration, teammate validation, tagged handoff parser, persistent chat rooms, pending/loop caps, queue transactions and isolated workspaces.
- Closure path: external agent decides to emit a teammate/chat-room tag → TinyAGI validates and enqueues it → recipient external agent receives the message and changes later behavior. TinyAGI closes transport/attenuation mechanics, but the coordinated S1 actors and discretionary coordination decision are external at this boundary.
- Why this is / is not agent-owned: team/fan-out topology is not enough by itself. The documentation explicitly says there is no central orchestrator and agents communicate directly; first-party team code parses decisions embedded in their responses.
- Evidence: [`docs/TEAMS.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/docs/TEAMS.md), [`packages/teams/src/routing.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/teams/src/routing.ts), [`packages/teams/src/conversation.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/teams/src/conversation.ts), [`docs/QUEUE.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/docs/QUEUE.md).
- Basis: structural absence at declared ownership boundary.
- Confidence: high.
- Caveats: at a wider assembled-system boundary that intentionally treats the hosted CLI agents as constituent S1 units, TinyAGI's queue/serialization/team protocol would be material S2 evidence. That is a different system-in-focus.

### Absence scope

- Surfaces inspected: team leader routing, handoff/fan-out parser, chat-room broadcast, per-agent chains, queue ordering/retry, loop caps and isolated workspaces.
- Plausible first-party paths checked: team topology as S2; queue serialization as S2; leader routing as S2; teammate validation/loop protection as S2.
- Why no material first-party path remains: the substrate addresses concrete interference, but the autonomous S1 units and discretionary handoff choices it coordinates belong to external CLI processes under the repository-relative boundary.

## S3 — Inside-and-now control

- State: —
- Function: TinyAGI provides deterministic and human-operated current-control surfaces, but no first-party autonomous whole-system S3 owner over first-party S1 operations is established.
- Disturbance / variety regulated: current queue backlog, failed/dead messages, stuck processing, active agent processes, agent/team configuration, task state, channel/service state and runtime restart/kill needs.
- Decisive decision or feedback right: choose current system-wide priorities/resource commitments or substantive interventions among operations, distinct from applying configured retry/lifecycle rules.
- Decision owner: operator/TinyOffice/API for management choices; external agents for task judgments; deterministic TinyAGI code for queue recovery/retry/process lifecycle.
- Supporting / enforcement mechanisms: TinyOffice control UI, queue status/dead-letter APIs, kill/restart controls, agent/team/task APIs, stale-message recovery, retry limits, daemon/channel/service lifecycle and SSE state.
- Closure path: configured rule or human/API action → first-party TinyAGI enforcement → queue/process/runtime state changes. No evidence establishes an autonomous first-party organizational controller that interprets whole-system current state and chooses discretionary corrective commitments.
- Why this is / is not agent-owned: runtime supervision and deterministic enforcement are real, but Profile 0.2.3 separates enforcement authority from organizational decision ownership. A management portal or queue recovery loop does not become S3 merely because it can alter current execution.
- Evidence: [`packages/main/src/index.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/main/src/index.ts), [`docs/QUEUE.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/docs/QUEUE.md), TinyOffice/server management surfaces at the pinned tree.
- Basis: structural absence.
- Confidence: high.
- Caveats: strong operational control exists; `—` means no qualifying first-party S3 decision owner was established, not an absence of monitoring or enforcement.

### Absence scope

- Surfaces inspected: TinyOffice control pages, server agent/team/task/queue/service/settings routes, process kill/restart, retry/dead-letter/recovery and daemon/channel lifecycle.
- Plausible first-party paths checked: queue processor as S3; TinyOffice as S3; stale recovery/dead-letter as S3; team leader role as S3; scheduler/heartbeat as whole-system S3.
- Why no material first-party path remains: current-control choices are either deterministic policy, explicit human/API management, or external-agent decisions; no autonomous first-party whole-system controller closes the organizational loop.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established beyond normal queue/log/history/monitoring surfaces.
- Disturbance / variety regulated: false or incomplete operational claims, hidden runtime failure, divergence between agent-reported work and independent operational reality.
- Decisive decision or feedback right: independently challenge ordinary operational reporting through materially different evidence access and return the finding into control.
- Decision owner: no qualifying first-party independent auditor identified.
- Supporting / enforcement mechanisms: logs, SSE events, queue status, persistent agent/team chat history, dead-letter records and TinyOffice visualization.
- Closure path: routine runtime events and persistence feed observability/management; no separate independent audit actor/path with complementary evidence and corrective feedback closure was established.
- Why this is / is not agent-owned: logging, persistence, visualization and a `reviewer` role configured as another external agent do not automatically constitute S3*.
- Evidence: [`docs/QUEUE.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/docs/QUEUE.md), [`docs/TEAMS.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/docs/TEAMS.md), first-party SSE/log/server surfaces in the pinned tree.
- Basis: structural absence.
- Confidence: high.
- Caveats: users may configure a reviewer agent, but its review judgment remains an adjacent CLI-agent operation and is not a distinct first-party independent audit channel by configuration name alone.

### Absence scope

- Surfaces inspected: logs/SSE, queue/dead-letter status, persisted agent history/chat history, TinyOffice visualization, reviewer-role examples and team event surfaces.
- Plausible first-party paths checked: reviewer agent as S3*; logging/SSE as S3*; persistent histories as S3*; dead-letter inspection as S3*.
- Why no material first-party path remains: the identified mechanisms are ordinary observability/persistence or externally executed role specialization; no first-party complementary auditor with distinct access and returned corrective judgment is wired into operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: TinyAGI supplies persistent memory, schedules and mutable skill/workspace surfaces, but no first-party prospective adaptation judgment loop closes independently of the external agent intelligence.
- Disturbance / variety regulated: changing user/project context, future scheduled needs, learned preferences/knowledge and opportunities to alter later capability.
- Decisive decision or feedback right: distinguish a prospective environmental change, generate an adaptation option and decide how current capability should change in response.
- Decision owner: the external CLI agent decides what knowledge is worth persisting, how to reorganize memory, whether to create/use skills and how to interpret scheduled/heartbeat context; the human can also configure schedules/prompts/skills.
- Supporting / enforcement mechanisms: hierarchical workspace memory, memory index injection into future system prompts, bundled memory/skill-manager/skill-creator instructions, schedules and heartbeat re-invocation.
- Closure path: external agent or human causes memory/skill/config change → TinyAGI persists or re-injects that material → a later external CLI invocation sees changed context/capability. The storage/re-presentation path is first-party, but the prospective distinction and adaptation judgment are not.
- Why this is / is not agent-owned: the bundled memory skill explicitly tells the agent to save proactively and prune/update stale memories, which is a strong adaptation support path; however those choices are executed by the adjacent CLI agent. Memory/learning labels therefore do not transfer S4 ownership to TinyAGI.
- Evidence: [`packages/core/src/memory.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/memory.ts), [`.agents/skills/memory/SKILL.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/.agents/skills/memory/SKILL.md), [`packages/core/src/agent.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/agent.ts), [`packages/core/src/schedules.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/schedules.ts), [`packages/main/src/heartbeat.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/main/src/heartbeat.ts).
- Basis: structural absence at declared ownership boundary.
- Confidence: high.
- Caveats: the assembled deployment can exhibit durable learning/adaptation because its external agents can write these first-party stores. The Index does not borrow those actors' discretionary intelligence into repository-relative TinyAGI ownership.

### Absence scope

- Surfaces inspected: memory index, bundled memory/skill surfaces, prompt assembly, schedules, heartbeat, mutable agent workspace/config and TinyOffice memory/skills/schedule tabs.
- Plausible first-party paths checked: persistent memory as S4; proactive memory skill as S4; skill creation/management as S4; schedules/heartbeat as S4; editable system prompt/SOUL as future adaptation.
- Why no material first-party path remains: first-party mechanisms store, trigger and re-present adaptations, but the external/prospective distinction and choice of adaptation are made by the external CLI agent or human/operator.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy adjudication loop is established at the TinyAGI system recursion.
- Disturbance / variety regulated: system identity, ultimate purpose/policy boundaries and unresolved conflicts between current operation and future adaptation would require legitimate authority and a returned governance decision.
- Decisive decision or feedback right: adjudicate identity/ultimate policy rather than merely configure agent personality, provider, model, team membership or ordinary operational settings.
- Decision owner: user/operator authors configuration, prompts and the SOUL template/customization; external CLI agents consume those instructions. No autonomous first-party S5 owner or function-specific parent-governed identity closure was established.
- Supporting / enforcement mechanisms: `SOUL.md`, `AGENTS.md`, configurable system prompts/prompt files, provider/model/team settings and TinyOffice settings/control surfaces.
- Closure path: operator/configuration supplies identity/policy text → TinyAGI injects it into later external-agent invocations. The reviewed evidence does not establish identity-level issue → legitimate parent authority → returned ultimate-policy decision → subsequent runtime governance.
- Why this is / is not agent-owned: `SOUL.md` explicitly describes who the agent is, but a static/editable identity document is not automatically S5. Likewise settings and ordinary operator approvals/configuration do not satisfy the Profile's identity-level closure test.
- Evidence: [`SOUL.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/SOUL.md), [`packages/core/src/agent.ts`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/packages/core/src/agent.ts), [`docs/AGENTS.md`](https://github.com/TinyAGI/tinyagi/blob/2db3a03a891b302c460f624d6c5a0523b8aa3528/docs/AGENTS.md).
- Basis: structural absence.
- Confidence: high.
- Caveats: humans retain ultimate authority over their local deployment. Methodology 0.3.5 does not publish `P` from generic configuration/approval alone without evidence that a specific S5 identity/policy issue is routed to the parent and returned into governance.

### Absence scope

- Surfaces inspected: SOUL identity template, built-in/user AGENTS instructions, system-prompt/prompt-file configuration, provider/model/team settings, TinyOffice settings/control and agent-management APIs.
- Plausible first-party paths checked: SOUL as S5; system prompt as S5; operator settings as S5=P; provider/model/team configuration as ultimate-policy closure.
- Why no material first-party path remains: these surfaces define or constrain configuration/identity text, but no runtime identity/ultimate-policy adjudication-and-return loop is evidenced.

## Distributed OSS parent arrangement

The assessment covers the shipped TinyAGI runtime, not the GitHub contributor organization. Maintainer/release/contributor governance is adjacent development activity and is not borrowed into runtime S3/S4/S5 ownership.

## Self-hosted and non-human modes

TinyAGI can run continuously as a background daemon/container and can re-invoke agents from schedules, heartbeat and external channels without continuous human input. Those modes demonstrate autonomous *deployment behavior* around the adjacent agent runtimes, but they do not change who owns the substantive task-level decisions. Self-hosting and always-on operation therefore do not by themselves establish a first-party S1 actor or parent-mode higher functions.

## Recursion

Each configured Claude Code/Codex/OpenCode agent is a natural lower-recursion operational system with its own conversation/session and tool loop. TinyAGI supplies isolated workspaces and organization around those systems. At the repository-relative boundary, however, those lower-recursion autonomous loops are external dependencies. Their viability is not inherited by the enclosing TinyAGI daemon merely through process invocation and first-party prompts.

## Variety and escalation

TinyAGI attenuates important runtime variety through transactional queues, per-agent ordering, retries/dead-letter, stale recovery, team membership validation, handoff loop caps, isolated workspaces and explicit process lifecycle. It amplifies reach through multiple parallel agents, channels, schedules, plugins and team broadcasts. It transduces agent-selected collaboration decisions through a structured tag protocol into durable messages.

Those are substantive harness capabilities and should not be reduced to “just routing”. The classification still follows function ownership: the first-party layer enforces and persists selected paths, while adjacent CLI agents make the substantive operational and handoff judgments. Similarly, management UI and configured roles do not automatically become S3/S3*/S5.

## Evidence gaps

No material evidence gap changes the boundary conclusion. The inspected frozen implementation directly shows the subprocess commands used for Claude and Codex and the first-party route from queue → `invokeAgent` → provider adapter → external CLI. Bundled skills and prompts were treated as first-party instruction/configuration surfaces but not as proof that TinyAGI itself implements the autonomous actor executing those instructions.

**Proposed terminal outcome:** `excluded-no-agentic-vsm`. TinyAGI is a substantive durable multi-agent harness/control substrate, but at the pinned standard-distribution boundary it does not supply its own autonomous operational decision/action loop. The Index should record the completed assessment without borrowing Claude Code/Codex/OpenCode autonomy into first-party TinyAGI ownership.