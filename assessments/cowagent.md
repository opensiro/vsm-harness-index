---
harness_id: cowagent
project_name: CowAgent
repository: https://github.com/zhayujie/CowAgent
review_ref: 7c55a61e1bccb82c99d97a4a436f598c079f7c9d
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: A(P)
---

# CowAgent

## Review boundary

- System in focus: the first-party CowAgent self-hosted personal-agent runtime at the frozen candidate revision, including its agent/model/tool execution loop, persistent workspaces and memory, multi-Agent team/delegation path, authenticated Web operator surface, schedulers, and the shipped Self-Evolution subsystem.
- Purpose and identity: provide a long-running personal AI assistant that autonomously handles user and scheduled work through tools and skills, can organize multiple independently configured Agents into teams, preserves durable memory/knowledge, and adapts its reusable capabilities and persona over time.
- Relevant environment: users and channel conversations, files and shell/browser state, external services and MCP tools, model-provider responses, scheduled events, accumulated conversation history, and operator decisions made through the authenticated Web console.
- Standard-distribution boundary: the shipped CowAgent runtime and supported Web/channel/self-hosted modes at the pinned revision. External model providers, MCP servers, messaging platforms, and downstream modifications are outside first-party ownership even when CowAgent transports their outputs.
- Credited operating / distribution surfaces: `agent/chat/service.py`, `bridge/agent_bridge.py`, built-in tools including `agent_delegate`, workspaces/memory/prompt machinery, `agent/evolution/*`, `agent/admin.py`, `channel/web/api/agents.py`, scheduler integration, and the standard configuration/template paths that wire these surfaces into supported runtime modes.
- Adjacent first-party surfaces excluded from ownership: repository tests, release/CI machinery, contributor material, documentation screenshots, website/blog content, and examples are used only as corroborating evidence; they do not supply an organizational owner unless the corresponding path is wired into the shipped runtime.
- First-party operating / deployment modes considered: normal Web/IM personal-agent execution; team conversations with independently configured Agents and synchronous delegation; authenticated operator roster/core-file administration; per-Agent schedulers; and default-enabled Self-Evolution on new standard installations.
- Recursion level: one running CowAgent installation, including its roster of operational Agents, is the system-in-focus. Individual team Agents are distinct S1 units for coordination analysis, but separate workspaces and delegated runs do not by themselves prove each is a recursively viable lower-level system.
- Reviewed revision: `7c55a61e1bccb82c99d97a4a436f598c079f7c9d`.
- Observation date: 2026-09-20.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

The batch #89 candidate pin is preserved. Current upstream is newer; no behavior from revisions after the frozen candidate SHA is used to upgrade this standalone classification.

## Repository architecture

CowAgent owns its agent loop rather than merely wrapping another agent product. `ChatService` builds an `AgentStreamExecutor` over the selected Agent, model, system prompt and first-party tool set, then repeatedly streams model reasoning, tool calls, tool results, subagent events and final output. `AgentBridge` constructs the model/tool runtime, maintains per-Agent/per-session instances, restores shared team transcripts, applies session preferences, runs per-Agent schedulers, and starts the Self-Evolution trigger.

The multi-Agent layer gives named Agents separate profiles/workspaces, memory, model choices, skills and knowledge. Team conversations can directly address a member or let one Agent invoke `agent_delegate`. Delegation is bounded by the conversation roster, an optional source→target allowlist, maximum depth and cycle checks. Each source→target/root-conversation relay receives a stable private session. Importantly for S2, concurrent handoffs to the same relay session are serialized by a dedicated lock specifically so they cannot interleave in the target transcript; the caller waits for the coordinated delegated result before continuing.

The authenticated Web operator surface supplies installation-wide roster and channel-binding administration. It can create/update/archive/delete Agents, choose the default Agent, set model and selected skills/knowledge, switch knowledge ownership, and live-rebind channel instances. A write rebuilds the registry/router, reconciles per-Agent schedulers and evicts only changed Agent runtimes so the decision applies on subsequent work without a restart. The same surface reads/writes `AGENT.md`, `RULE.md` and other core files, then evicts the edited runtime so the next instance reloads the changed identity/policy context.

Self-Evolution is a separate short-lived review Agent, started by the normal `AgentBridge` idle trigger and enabled in the standard configuration template. After sufficient conversation activity becomes idle, it reviews the external interaction, decides whether durable adaptation is justified, and may patch a broken skill, create a reusable workflow likely to be needed again, consolidate durable memory/knowledge, finish a left-behind task, or—in deliberately rare cases—revise `AGENT.md` after an explicit repeated identity/personality/style signal. Changes are workspace-scoped, backed up, committed only when real guarded files changed, recorded, and loaded into later operation.

Primary evidence:

- [`agent/chat/service.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/agent/chat/service.py)
- [`bridge/agent_bridge.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/bridge/agent_bridge.py)
- [`agent/tools/agent_delegate/agent_delegate.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/agent/tools/agent_delegate/agent_delegate.py)
- [`agent/admin.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/agent/admin.py)
- [`channel/web/api/agents.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/channel/web/api/agents.py)
- [`agent/evolution/config.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/agent/evolution/config.py)
- [`agent/evolution/trigger.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/agent/evolution/trigger.py)
- [`agent/evolution/executor.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/agent/evolution/executor.py)
- [`agent/evolution/prompts.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/agent/evolution/prompts.py)
- [`agent/prompt/builder.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/agent/prompt/builder.py)
- [`agent/prompt/workspace.py`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/agent/prompt/workspace.py)
- [`config-template.json`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/config-template.json)
- [`docs/memory/self-evolution.mdx`](https://github.com/zhayujie/CowAgent/blob/7c55a61e1bccb82c99d97a4a436f598c079f7c9d/docs/memory/self-evolution.mdx)

## Operational model

The primary S1 units are live CowAgent Agents. Each receives a user, channel, scheduled or delegated objective, uses its configured model to choose successive tool/skill actions, incorporates returned observations and continues until a final result or runtime stop. In team mode several independently configured Agents can act as sibling operational units, with delegation results returning to the source Agent's tool loop.

Deterministic runtime components route messages, persist context, enforce permissions, serialize a conflicting relay session, and execute operator changes, but those mechanisms are not automatically credited with organizational decision ownership. The authenticated operator owns the installation-wide current-control mode. Separately, the default-enabled Self-Evolution review Agent owns prospective adaptation judgments over reusable skills/knowledge and a tightly bounded autonomous identity-evolution path. The authenticated operator retains a distinct parent identity/policy mode through the same first-party distribution.

## S1 — Operations

- State: A
- Function: autonomously transform user/scheduled/delegated objectives into environment-facing tool/skill work and returned outcomes.
- Disturbance / variety regulated: heterogeneous user objectives, model uncertainty, tool results/errors, files/shell/browser/service state, channel messages, and follow-up observations encountered during a trajectory.
- Decisive decision or feedback right: choose the next reasoning/tool/skill action, incorporate returned observations, delegate bounded work when useful, or stop with a final response.
- Decision owner: the running CowAgent Agent/model actor inside the first-party `AgentStreamExecutor` loop.
- Supporting / enforcement mechanisms: `ChatService`, `AgentBridge`, provider adapters, prompt/workspace construction, tool registry, permissions, session persistence, scheduler integration and context controls.
- Closure path: each tool result, delegated result or new model observation returns into the first-party executor context and can change the next autonomous action until completion.
- Boundary reachability: the credited executor/bridge/tool path is the normal shipped Web/channel runtime and is instantiated directly by standard CowAgent operation at the pinned revision.
- Why this is / is not agent-owned: deterministic code supplies transport, limits and execution, while the model actor owns the discretionary next-action choice on each loop iteration.
- Evidence: pinned `agent/chat/service.py` and `bridge/agent_bridge.py`; `README.md` corroborates the shipped planning/tool execution boundary.
- Basis: `structural` and `explicit`.
- Confidence: high.
- Caveats: model/provider/tool availability, permissions and iteration limits constrain the Agent's operational discretion but do not replace its next-action judgment.

## S2 — Coordination

- State: C
- Function: attenuate a concrete interference between sibling operational Agents when concurrent delegations target the same persistent relay conversation.
- Disturbance / variety regulated: concurrent handoffs to one source→target relay session would otherwise interleave turns in the target Agent's transcript and corrupt the shared conversational state used by later delegated work.
- Decisive decision or feedback right: serialize admission to that target relay session so exactly one delegated turn occupies it at a time; timeout rather than permit an overlapping handoff when the lock cannot be acquired within policy.
- Decision owner: constructor-owned at the assessed boundary. The first-party S2-specific serialization primitive is complete and operational, but the conflict policy itself is deterministic/developer-selected rather than autonomously chosen by an Agent.
- Supporting / enforcement mechanisms: per-relay `_relay_lock`, stable relay-session derivation, delegation roster/ACL, depth/cycle checks, timeout and synchronous result return.
- Closure path: a source Agent's delegation blocks on the relay lock; after the prior target turn finishes and releases the lock, the next delegated target run executes against a non-interleaved transcript and its result returns to the waiting source Agent, changing that source's subsequent S1 behavior.
- Boundary reachability: `agent_delegate` is a shipped team tool attached to normal team turns through `AgentBridge`; no downstream coordinator or test-only actor is required for the serialization path.
- Why this is / is not agent-owned: Agents autonomously decide to delegate and select the teammate/task, but once two handoffs conflict the coordination choice is a fixed first-party lock policy. CowAgent therefore exposes a real S2-specific construction path without an autonomous owner of the conflict-regulation decision.
- Evidence: pinned `agent/tools/agent_delegate/agent_delegate.py` and team-session support in `bridge/agent_bridge.py`.
- Basis: `structural`.
- Confidence: high.
- Caveats: other team features such as speaker selection, shared transcripts and ordinary handoff are not separately credited as S2 merely because they connect Agents.
- Distinct S1 units: independently configured live CowAgent Agents with separate profiles/workspaces and first-party execution loops participating in one team conversation.
- Inter-S1 disturbance: overlapping delegated turns to the same target relay session can interleave in the target transcript.
- Attenuating coordination relation: the first-party per-relay lock queues competing handoffs and allows only one target turn at a time.
- Feedback into subsequent S1 behaviour: the coordinated target result is returned synchronously to the delegating source Agent's tool loop; timeout/failure likewise returns a result that changes the source Agent's next decision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the lock exists specifically because concurrent sibling handoffs would interfere by interleaving one operational transcript, and it changes admission/timing to suppress that identified disturbance before results feed back to the source Agent.

## S3 — Inside-and-now control

- State: P
- Function: regulate the currently configured CowAgent installation as a whole by changing which operational Agents are available, which models/capabilities they use, and which live channel instances/teams route work to them.
- Disturbance / variety regulated: current mismatch between installed operational capacity and the operator's desired roster, agent availability, model/capability allocation, shared/own knowledge mode, default ownership and live channel/team bindings.
- Decisive decision or feedback right: create/update/archive/delete an Agent, make an Agent default, enable/disable it, alter its model/skills/knowledge allocation, or rebind a running channel/team to a different Agent roster.
- Decision owner: the authenticated self-hosted operator is the legitimate parent actor in this supported mode.
- Supporting / enforcement mechanisms: `AgentAdminService`, roster revision checks, Web authentication, registry/router rebuilding, scheduler reconciliation, targeted live-runtime eviction and hot channel rebinding.
- Closure path: the operator submits a first-party Web/API decision; CowAgent persists it, updates the live registry/router or channel binding, starts/stops the affected schedulers and evicts changed Agent instances so subsequent current work is executed under the returned control decision.
- Boundary reachability: the authenticated Web console and its `/api/agents` administration paths are a standard shipped self-hosted operating surface documented as the unified configuration hub, not a development-only control plane.
- Why this is / is not agent-owned: no standard first-party autonomous Agent is given installation-wide roster/model/capability/channel authority. The decisive current-control choice comes from the authenticated operator; runtime code only validates, persists and enforces it.
- Evidence: pinned `agent/admin.py`, `channel/web/api/agents.py`, and `bridge/agent_bridge.py` scheduler/runtime reconciliation.
- Basis: `explicit` and `structural`.
- Confidence: medium-high.
- Caveats: this claim is limited to installation-level current capability/resource control. Per-task steering/cancel and permission enforcement alone would not establish S3, and the assessment does not treat every settings edit as an S3 decision.
- Whole-system current view: `AgentAdminService.snapshot()` exposes the installation's full current Agent roster, default Agent and channel instances; the same authenticated surface operates over that roster rather than one worker-local state.
- Current-control decision scope: availability of S1 units, current model/capability allocation, default Agent, channel/team routing and scheduler participation for the running installation.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary and sufficiently independent audit function was established at the declared installation boundary.
- Disturbance / variety regulated: none established as an S3* witness; ordinary tool feedback, run/event recording and Self-Evolution review do not provide a materially independent route to operational reality for checking production claims.
- Decisive decision or feedback right: no S3*-specific independent audit judgment/feedback right is supplied.
- Decision owner: not established.
- Supporting / enforcement mechanisms: execution/tool events, conversation/run persistence, evolution records/backups, logs and operator inspection surfaces.
- Closure path: no independent audit finding→corrective-current-control loop was established; recorded events and evolution changes serve their primary execution/adaptation purposes.
- Why this is / is not agent-owned: there is no qualifying audit function whose decisive judgment could be assigned to an autonomous Agent.
- Evidence: pinned chat/executor event path, conversation storage, Web/admin surfaces, and `agent/evolution/*` review path.
- Basis: `structural`.
- Confidence: high.
- Caveats: a downstream deployment could add an independent verifier or external monitor, but that composed system would be outside this frozen first-party boundary.

### Absence scope

- Surfaces inspected: primary agent execution/events, delegation/team paths, conversation/run persistence, logs, permission/admin controls, Self-Evolution review/record/backup machinery, standard docs/configuration and the available Web control surfaces at the pinned revision.
- Plausible first-party paths checked: tool execution feedback, delegated/subagent event relays, stored run state, operator logs, Self-Evolution transcript review and change detection/rollback.
- Why no material first-party path remains: each identified path either participates in ordinary production reporting, deterministic enforcement or adaptation from the same transcript/workspace evidence; none establishes a complementary sufficiently independent observation channel plus audit judgment that closes back into current control.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert externally observed conversation patterns and capability failures into prospective adaptations of reusable future capability.
- Disturbance / variety regulated: changing user preferences and recurring work patterns, skill defects discovered in real use, reusable workflows not yet encoded as capabilities, and unfinished work whose recurrence or omission would reduce future fit.
- Decisive decision or feedback right: after an idle conversation, decide autonomously whether there is a clear durable signal and whether to patch an existing skill, create a new reusable skill, consolidate knowledge/memory, or take no adaptation action.
- Decision owner: the isolated first-party Self-Evolution review Agent/model actor.
- Supporting / enforcement mechanisms: idle trigger thresholds, restricted evolution toolset, guarded workspace paths, pre-change backup, snapshot diff/change detection, transactional rollback and evolution records.
- Closure path: the review Agent senses conversation-derived external signals, selects and writes an adaptation, the executor commits only real guarded changes, and later normal Agent runs load/use the revised skill/knowledge/persona state; if no clear signal exists it explicitly leaves capability unchanged.
- Boundary reachability: Self-Evolution is started by normal `AgentBridge` initialization, its configuration class defaults enabled, and the standard pinned `config-template.json` ships `self_evolution_enabled: true`; the decision actor is therefore reachable in the supported distribution without borrowing a dogfood or contributor agent.
- Why this is / is not agent-owned: trigger timing, backups and write guards are deterministic support, but the model review Agent owns the discretionary judgment of whether a past external interaction predicts future reusable need and which permitted adaptation to make.
- Evidence: pinned `agent/evolution/config.py`, `trigger.py`, `executor.py`, `prompts.py`, `bridge/agent_bridge.py`, `config-template.json` and `docs/memory/self-evolution.mdx`.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: simple memory consolidation alone is not the credited S4 witness. The positive mapping relies on the separately evidenced prospective skill-adaptation path: detecting a workflow likely to be wanted again or a skill defect exposed in use, autonomously generating an adaptation, and returning that change into later capability.
- External distinction: the review consumes user conversation and actual skill/task experience from the environment, including repeated preferences, failures and emergent workflows.
- Future / prospective distinction: the evolution prompt explicitly asks whether a workflow is reusable and likely to be wanted again, and documentation defines the goal as creating/fixing skills so they can be reused next time and future conversations improve.
- Adaptation option generated: patch a defective skill, encode an emergent workflow as a new reusable skill, consolidate durable knowledge/memory, complete suitable unfinished work, or deliberately make no change.
- Path back into current capability / S3: committed workspace/skill/knowledge changes are the same first-party artifacts read by subsequent normal Agent operation; operator rollback remains a separate parent intervention path rather than the owner of the autonomous adaptation judgment.

## S5 — Policy and identity

- State: A(P)
- Function: govern the Agent's durable identity/personality and highest-level workspace behavioral principles through first-party identity files that are loaded into subsequent system prompts.
- Disturbance / variety regulated: drift between the Agent's durable identity/behavioral principles and explicit repeated signals about what the assistant should be, plus explicit operator decisions to redefine those identity/policy artifacts.
- Decisive decision or feedback right: in the autonomous mode, decide whether an explicit repeated identity/personality/style signal is strong enough to justify a bounded `AGENT.md` identity revision; in the parent mode, authoritatively edit `AGENT.md`/`RULE.md` through the authenticated core-file administration surface.
- Decision owner: base mode — the isolated Self-Evolution review Agent for the deliberately narrow autonomous identity-evolution decision; parent mode — the authenticated self-hosted operator as ultimate authority over the installation's core identity/policy files.
- Supporting / enforcement mechanisms: evolution signal criteria and guarded writes/backups; `AgentAdminService` core-file revision checks and atomic writes; authenticated Web endpoint; prompt/workspace loader; targeted runtime eviction after operator edits.
- Closure path: autonomous mode: repeated identity-level external signal → review-Agent identity judgment → guarded `AGENT.md` edit → subsequent runtime loads the changed persona. Parent mode: authenticated operator reads/edits a core identity/policy file → atomic persistence and cached-Agent eviction → subsequent Agent instance reloads that file into its system prompt.
- Boundary reachability: both modes are shipped supported runtime paths: default-enabled Self-Evolution may edit `AGENT.md` under its standard guard, while the authenticated Web Agents API exposes core-file read/write and immediately evicts the changed runtime.
- Why this is / is not agent-owned: the base identity change is not a static prompt or automatic parser; the review Agent must judge whether a rare explicit repeated signal warrants changing its own identity artifact. The separate operator mode retains parent authority to set or override the same identity/policy surface, hence `A(P)` rather than plain `A`.
- Evidence: pinned `agent/evolution/prompts.py`, `executor.py`, `agent/prompt/workspace.py`, `agent/prompt/builder.py`, `agent/admin.py` and `channel/web/api/agents.py`.
- Basis: `explicit` and `structural`.
- Confidence: medium-high.
- Caveats: ordinary permission settings, tool approvals, memory/preferences and per-task steering are not credited as S5. The autonomous claim is narrowly limited to the explicit first-party `AGENT.md` identity-evolution path; operator edits establish the separate parent mode.
- Identity / ultimate-policy issue: `AGENT.md` is explicitly defined by the shipped templates as the Agent's identity/personality and is loaded with `RULE.md` into the system-prompt context; this is materially different from ordinary task or tool policy.
- Ultimate authority in each claimed mode: base (`A`) — Self-Evolution Agent decides whether the standard rare-signal criterion warrants a durable identity edit; parent (`P`) — authenticated operator directly owns the authoritative core-file edit and may override/undo Agent evolution.
- Return-to-operation path: both modes persist the core file used by prompt construction; operator writes additionally evict the cached runtime, and later Agent initialization reloads the changed identity/policy context.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Self-Evolution review Agent | Idle conversation contains an explicit repeated identity/personality/style signal that the review Agent judges worth durable learning | guarded `AGENT.md` edit is committed and loaded into later normal Agent prompts | `agent/evolution/prompts.py`, `executor.py`, `prompt/workspace.py` |
| Parent (`P`) | authenticated self-hosted operator | operator chooses to edit the Agent's core identity/policy file | atomic core-file write → live Agent eviction → next runtime reloads the edited context | `agent/admin.py`, `channel/web/api/agents.py`, `prompt/builder.py` |

## Recursion

Team members have separate profiles, workspaces, memory, skills/knowledge selections and autonomous S1 loops, and delegation can be nested within bounded depth. Those facts establish operational differentiation and coordination variety, not full VSM recursion. The frozen evidence does not establish that every team Agent independently carries a complete S1–S5 metasystem for its own lower-level organization, so no stronger recursive-viability claim is made.

## Variety and escalation

CowAgent absorbs variety through heterogeneous tools/skills/models, separate Agent workspaces, team delegation, model fallback, persistent memory/knowledge, scheduled work and later Self-Evolution. Delegation policy bounds targets/depth, rejects cycles, serializes a conflicting relay and returns failures/timeouts to the source Agent. Permission modes constrain environment-changing operations. Parent escalation is available through the authenticated Web control plane for roster/capability/channel decisions and through direct core identity/policy edits; evolution changes are backed up and explicitly reversible.

## Evidence gaps

- The S3 parent classification is scoped to installation-level operational capacity and live routing; the frozen distribution does not expose a single autonomous whole-installation S3 actor, and no such actor is inferred from delegation or schedulers.
- S3* remains negative because no sufficiently independent complementary audit channel was found; post-hoc Self-Evolution uses the same conversation/workspace evidence for adaptation rather than independent operational verification.
- S5 autonomous ownership is intentionally narrow. If later methodology requires the ultimate identity signal itself to originate internally rather than allowing an Agent to exercise authoritative judgment over externally supplied identity signals, the base `A` portion should be rechecked; the parent `P` path is independently established.
