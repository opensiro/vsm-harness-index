---
harness_id: nanoclaw
project_name: NanoClaw
repository: https://github.com/nanocoai/nanoclaw
review_ref: 7902716b5b930215dbee4f56b8fb5b938d40468d
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

# NanoClaw

## Review boundary

- System in focus: the first-party NanoClaw v2 host/control plane at pinned revision `7902716b5b930215dbee4f56b8fb5b938d40468d`, including host routing, entity/session databases, per-session container lifecycle, mailbox transport, scheduling/recovery, channel/provider registries, `ncl` control surfaces, approval/guard machinery and first-party self-modification plumbing.
- Purpose and identity: securely host separately operating AI agents in isolated per-session containers, route messages between channels and those agents, persist session/group state, schedule work, control lifecycle and expose bounded administration/capability-change mechanisms.
- Relevant environment: user/channel messages, configured agent groups, Anthropic Claude Agent SDK and optional alternative external agent providers, model providers, MCP servers, OneCLI credential service, Docker, channel adapters and human owner/admin decisions.
- Standard-distribution boundary: NanoClaw's Node host, container/agent-runner bridge, mailbox/polling code, first-party host tools, databases, scheduling, guards/approvals, group/session/container management and bundled Claude provider adapter are first-party. The autonomous model/tool reasoning loop implemented by `@anthropic-ai/claude-agent-sdk` remains an adjacent agent runtime even though NanoClaw invokes it from its container and supplies prompts/tools/policy. Skill-installed Codex/OpenCode/Ollama or other provider runtimes are likewise not borrowed as NanoClaw organizational decision owners.
- Credited operating / distribution surfaces: root host process; `src/router.ts`, session/container lifecycle and host sweep; central/per-session DBs; `container/agent-runner` mailbox and provider bridge; `ncl` CLI/guard/approval surfaces; scheduling/system-action handling; first-party self-mod request/apply path.
- Adjacent first-party surfaces excluded from ownership: repository setup/migration/customization flows that hand judgment to Claude Code; contributor/CI/test surfaces; channel/provider branches not installed in the frozen trunk; external agent SDK internals; external model inference, MCP services, OneCLI and Docker runtime behavior.
- First-party operating / deployment modes considered: default Claude-backed per-session containers, multiple agent groups/sessions, scheduled tasks, group/global `ncl` scopes, owner/admin approval flows and the shipped package/MCP self-modification mechanism.
- Recursion level: NanoClaw host/control plane itself. Each hosted Claude/Codex/OpenCode/etc. agent can independently be an operational system and requires its own repository-relative assessment; NanoClaw does not inherit that agent's S1 simply because it supplies isolation, transport, policy and lifecycle.
- Reviewed revision: `7902716b5b930215dbee4f56b8fb5b938d40468d`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

NanoClaw explicitly describes a host architecture of `messaging apps → host process (router) → inbound.db → container (Bun, Claude Agent SDK) → outbound.db → host process (delivery)`. The host owns entity routing, per-session mailboxes, container spawn/idle lifecycle, recurrence/stale recovery and delivery. Each session has its own container and inbound/outbound SQLite pair, while an agent group supplies shared workspace/instructions/configuration.

The container-side `agent-runner` is a bridge around a registered provider. Its first-party poll loop reads pending mailbox messages, formats them, invokes `provider.query()`, translates provider events into NanoClaw messages and persists continuation/ack state. In the frozen trunk, the provider registry imports only `claude`. `ClaudeProvider.query()` calls `query()` from `@anthropic-ai/claude-agent-sdk`, handing the SDK the prompt, continuation, system prompt, allowed/disallowed tools, MCP servers, model settings and hooks. The SDK then owns the model/tool agent execution that produces assistant/tool/result events. NanoClaw observes/translates those events but does not implement the substantive next-task/next-tool decision loop itself.

This distinction remains true despite NanoClaw's substantial control-plane functionality. The host can create/manage agent groups, sessions, wirings and scheduled tasks; its guard layer can allow, deny or hold agent-initiated administration for owner/admin approval; its self-mod tools can request packages or a new MCP server and, after approval, persist config, rebuild/restart the container and notify the hosted agent. Those are real first-party hosting, governance and capability-management paths around an adjacent autonomous agent. They do not transfer that external agent runtime's ordinary S1 decision right into NanoClaw.

Methodology 0.3.5 says an autonomous-harness assessment should use the Index exclusion state rather than force S1 classification when the standard distribution does not establish its own autonomous operational decision/action loop. The proposed terminal outcome is therefore `excluded-no-agentic-vsm`; the all-`—` local vector documents the reviewed control-plane boundary while that exclusion is under review.

Primary evidence:

- [`README.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/README.md) — explicit host→container architecture, isolated agent groups/sessions, Claude Agent SDK as the native agent backend, scheduling and administrative capabilities.
- [`CLAUDE.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/CLAUDE.md) — source-of-truth entity/session architecture, `ncl` control plane, self-modification and group/global scope semantics.
- [`container/agent-runner/src/index.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/container/agent-runner/src/index.ts) — provider construction followed by the first-party mailbox/poll-loop bridge.
- [`container/agent-runner/src/poll-loop.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/container/agent-runner/src/poll-loop.ts) — mailbox formatting, provider invocation, provider-event processing and lifecycle/ack handling.
- [`container/agent-runner/src/providers/index.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/container/agent-runner/src/providers/index.ts) — frozen trunk registers the Claude provider.
- [`container/agent-runner/src/providers/claude.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/container/agent-runner/src/providers/claude.ts) — direct invocation of `@anthropic-ai/claude-agent-sdk` `query()` with NanoClaw configuration/hooks, followed by event translation.
- [`src/cli/dispatch.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/src/cli/dispatch.ts) and [`src/cli/guard.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/src/cli/guard.ts) — first-party administrative control, scoping and approval handling around hosted groups/sessions.
- [`container/agent-runner/src/mcp-tools/self-mod.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/container/agent-runner/src/mcp-tools/self-mod.ts) and [`src/modules/self-mod/apply.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/src/modules/self-mod/apply.ts) — agent-requested, admin-approved persistent package/MCP changes and restart/re-entry mechanics.
- [`docs/architecture.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/docs/architecture.md) — host/container message flow, single-writer DB design, scheduling and container-lifecycle intent, with code explicitly declared authoritative where documentation drifts.

## Operational model

A channel event reaches NanoClaw's host, which maps platform identifiers through messaging-group/agent-group/session state, writes the message into that session's `inbound.db` and wakes/spawns its container. The first-party agent-runner sees the pending message and calls its configured provider. Under the standard frozen trunk that provider delegates the autonomous agent query to Anthropic's Claude Agent SDK. SDK-produced events are translated back through NanoClaw's poll loop and written to `outbound.db`; the host then delivers them to the channel.

If the SDK-backed agent chooses tools, reasons from tool observations, revises its task plan and produces an outcome, that discretionary task-level loop belongs to the adjacent SDK-backed agent. Removing the SDK/hosted agent while leaving NanoClaw's router, databases, scheduler, container manager, guard, `ncl` and delivery machinery intact leaves no first-party autonomous actor that can interpret an arbitrary user task, select substantive actions from observations and iterate to the outcome.

## S1 — Operations

- State: —
- Function: no first-party autonomous task-level operational decision/action loop is established inside the NanoClaw control-plane boundary.
- Disturbance / variety regulated: NanoClaw regulates channel/message transport, routing, session/container lifecycle, scheduling, isolation and provider integration; task/environment variety is interpreted and acted on by the hosted external agent runtime.
- Decisive decision or feedback right: choose the next substantive task/tool/action from current task history and returned observations.
- Decision owner: the adjacent Claude Agent SDK-backed agent (or another installed external agent provider), outside NanoClaw's first-party organizational ownership.
- Supporting / enforcement mechanisms: host router, session DBs, container runner, first-party poll loop, provider adapter, MCP registration, system prompt composition, guards/approvals, scheduling and delivery.
- Closure path: channel message → NanoClaw host/mailbox → NanoClaw calls external agent provider → external agent runtime chooses tools/actions and interprets results → NanoClaw translates/delivers provider events. The decisive operational loop closes in the provider runtime, not NanoClaw.
- Why this is / is not agent-owned: the first-party poll loop owns transport/lifecycle around `provider.query()`; the Claude provider directly invokes the external Claude Agent SDK for the autonomous query/tool loop and translates its events rather than replacing that loop.
- Evidence: [`container/agent-runner/src/poll-loop.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/container/agent-runner/src/poll-loop.ts), [`container/agent-runner/src/providers/claude.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/container/agent-runner/src/providers/claude.ts), [`README.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this does not deny that a running NanoClaw installation contains an autonomous agent; it keeps ownership repository-relative and does not borrow the adjacent SDK/provider's S1 into NanoClaw.

### Absence scope

- Surfaces inspected: host/container architecture, agent-runner bootstrap, first-party poll loop, provider registry, Claude provider adapter, built-in MCP tools, scheduling, routing and container lifecycle.
- Plausible first-party paths checked: poll loop as agent loop; Claude provider adapter as agent loop; built-in MCP tools; scheduled task processing; host routing/container lifecycle as autonomous operations.
- Why no material first-party path remains: all generic task reasoning/tool choice still crosses `provider.query()` into the separately implemented agent runtime; remaining first-party paths are deterministic transport, lifecycle, policy, scheduling or tool plumbing.

## S2 — Coordination

- State: —
- Function: no qualifying first-party S2 coordination function is established at the NanoClaw recursion.
- Disturbance / variety regulated: NanoClaw prevents low-level mailbox writer contention and isolates sessions/containers, but no organizational interference/conflict/oscillation among first-party S1 units is established because NanoClaw does not own the hosted agents' S1 decision loops.
- Decisive decision or feedback right: no S2-specific organizational coordination discretion is established inside the boundary.
- Decision owner: none established within NanoClaw.
- Supporting / enforcement mechanisms: per-session isolation, separate inbound/outbound DB writers, routing, per-channel queue/concurrency choices, host sweep workqueue and session/container lifecycle.
- Closure path: no qualifying first-party S1 interference → coordination decision → changed subsequent S1 behavior path is established.
- Why this is / is not agent-owned: isolation and routing deliberately avoid infrastructure collisions, but they do not establish organizational coordination among NanoClaw-owned operational agents.
- Evidence: [`docs/architecture.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/docs/architecture.md), [`README.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: multiple hosted external agents may coordinate through messages in a customized installation; sharing NanoClaw infrastructure does not by itself make their coordination a first-party NanoClaw function.

### Absence scope

- Surfaces inspected: agent groups/sessions, routing/entity model, mailbox split, Chat SDK channel concurrency, host sweep workqueue, agent-to-agent message transport and container isolation.
- Plausible first-party paths checked: session isolation as S2; single-writer DB design; channel queues/concurrency; host workqueue; routing between groups; agent-to-agent transport.
- Why no material first-party path remains: these paths regulate infrastructure transport/contention or expose communication, not a first-party organizational attenuation loop over a concrete disturbance among NanoClaw-owned S1 units.

## S3 — Inside-and-now control

- State: —
- Function: NanoClaw exposes rich current administration of hosted groups/sessions/tasks, but no first-party autonomous whole-system S3 owner is established for NanoClaw-owned S1 operations.
- Disturbance / variety regulated: current group/session/task/container state, routing/wiring and lifecycle can be inspected or changed, while the substantive operational commitments belong to adjacent hosted agents.
- Decisive decision or feedback right: whole-installation administrative mutations are chosen by the host operator/admin or proposed by the external hosted agent and may be approval-gated; NanoClaw runtime enforces those choices.
- Decision owner: no autonomous first-party NanoClaw S3 owner established.
- Supporting / enforcement mechanisms: global/group `ncl` scopes, group/session/task listings, group create/update/delete/restart, guard decisions, owner/admin approvals, DB state and container restart machinery.
- Closure path: operator or hosted-agent request → first-party guard/approval/CLI machinery → DB/container mutation → changed hosted-runtime state. This is administration around externally owned S1 rather than whole-system autonomous regulation of NanoClaw-owned operations.
- Why this is / is not agent-owned: `ncl` gives a hosted agent a strong control surface, including global scope for an owner agent group, but the model making that discretionary proposal remains the adjacent provider agent; mutating commands frequently hold for human admin approval.
- Evidence: [`CLAUDE.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/CLAUDE.md), [`src/cli/dispatch.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/src/cli/dispatch.ts), [`src/cli/guard.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/src/cli/guard.ts), [`src/cli/resources/groups.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/src/cli/resources/groups.ts).
- Basis: explicit + structural absence at the declared repository boundary.
- Confidence: high.
- Caveats: this classification is not a statement that the control plane is weak; it separates strong administrative enforcement from ownership of an internally owned operational organization.

### Absence scope

- Surfaces inspected: `ncl` resource model, group/global CLI scope, guard decisions, approval replay, group/session/task controls, container restart and current DB state.
- Plausible first-party paths checked: global owner-agent CLI as autonomous S3; human approval as parent S3; scheduler/container lifecycle as S3; group/session management as S3.
- Why no material first-party path remains: the discretionary agent proposal belongs to the adjacent provider runtime, generic human approval does not by itself establish parent S3, and deterministic host controls administer externally owned agent operations rather than a NanoClaw-owned S1 portfolio.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit actor/path is established that makes a distinct claim about operational reality and closes corrective feedback into first-party NanoClaw S1 behavior.
- Disturbance / variety regulated: guards, validation, heartbeats, stale detection and logs can detect policy/runtime conditions, but they are enforcement/health mechanisms rather than independent organizational audit judgment.
- Decisive decision or feedback right: none established for a complementary audit verdict with corrective return into NanoClaw-owned S1.
- Decision owner: none established within NanoClaw.
- Supporting / enforcement mechanisms: guard allow/hold/deny decisions, input/config validation, processing acknowledgements, heartbeat/stale recovery, logs and approval records.
- Closure path: no independent complementary evidence path → audit judgment → corrective operational return is established.
- Why this is / is not agent-owned: runtime guards and health checks deterministically validate/enforce the same operating surfaces; there is no separate auditor with sufficiently independent access and judgment.
- Evidence: [`CLAUDE.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/CLAUDE.md), [`src/cli/guard.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/src/cli/guard.ts), [`docs/architecture.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/docs/architecture.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: external provider agents or operators can perform reviews, but NanoClaw does not inherit those external audit loops.

### Absence scope

- Surfaces inspected: guard pipeline, approvals, message/status acknowledgements, heartbeat/stale recovery, logs, mount/security validation and CLI validation.
- Plausible first-party paths checked: guards as S3*; stale/crash recovery as S3*; approval review as S3*; logs/diagnostics as S3*.
- Why no material first-party path remains: reviewed mechanisms enforce policy, validate requests or recover runtime state through ordinary operational evidence; none supplies an independent complementary audit judgment with corrective closure.

## S4 — Outside-and-then adaptation

- State: —
- Function: NanoClaw exposes persistent capability-change mechanisms, but no first-party autonomous outside-and-then intelligence loop is established at the NanoClaw control-plane boundary.
- Disturbance / variety regulated: package/MCP requests can respond to capability needs and permanently change a hosted agent group's runtime, but the need/options originate in the adjacent hosted agent or human customization process.
- Decisive decision or feedback right: `install_packages` and `add_mcp_server` requests are generated by the hosted external agent and require admin approval before first-party apply/restart machinery executes them.
- Decision owner: external hosted agent proposes the change; human admin owns the approval; NanoClaw deterministically applies it. No first-party autonomous S4 owner is established.
- Supporting / enforcement mechanisms: self-mod MCP tools, approval cards, container-config DB mutation, image rebuild, restart and `on_wake` re-entry notification.
- Closure path: external hosted agent requests capability → NanoClaw sends admin approval → approved request mutates persistent group config/rebuilds/restarts → hosted external agent resumes with changed capability. The adaptation path is real but its sensing/options/decisive judgment are not an autonomous NanoClaw S4 loop.
- Why this is / is not agent-owned: first-party NanoClaw supplies a strong apply/closure primitive; the autonomous proposer is the adjacent provider agent, while the legitimate decisive approval remains human. The evidence does not establish a NanoClaw-owned prospective intelligence actor, and ordinary customization by Claude Code is outside the assessed runtime boundary.
- Evidence: [`container/agent-runner/src/mcp-tools/self-mod.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/container/agent-runner/src/mcp-tools/self-mod.ts), [`src/modules/self-mod/apply.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/src/modules/self-mod/apply.ts), [`CLAUDE.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/CLAUDE.md).
- Basis: explicit + structural absence at the declared boundary.
- Confidence: medium-high.
- Caveats: as a capability-management primitive, this path could participate in S4 of a larger composed organization; that does not transfer the external agent/human ownership into NanoClaw's standalone assessment.

### Absence scope

- Surfaces inspected: self-mod MCP tools/apply handlers, template/restamp paths, skill-install/customization philosophy, scheduling, persistent group/container configuration and setup/debug handoffs to Claude Code.
- Plausible first-party paths checked: package/MCP self-mod as S4; template restamping; `/customize`; skill-installed providers/channels; scheduled tasks; persistent memory.
- Why no material first-party path remains: no first-party NanoClaw autonomous actor performs external/future sensing, develops adaptation options and owns their return into capability; the strongest capability-change path is external-agent proposal plus human approval plus deterministic application.

## S5 — Identity / ultimate policy

- State: —
- Function: no first-party autonomous identity/ultimate-policy closure is established for NanoClaw as an organization.
- Disturbance / variety regulated: owner/admin roles, group identity/instructions, CLI scope, guards and approvals constrain operation but do not establish runtime adjudication of organizational identity or constitutional policy.
- Decisive decision or feedback right: ultimate role/policy/instruction changes remain operator/developer configuration or human approval decisions around the hosted agent runtime.
- Decision owner: no autonomous first-party NanoClaw S5 owner established.
- Supporting / enforcement mechanisms: user roles, owner/admin privileges, `cli_scope`, guards, approval records, group `CLAUDE.md`, container configuration and host-only command restrictions.
- Closure path: static/operator-authored policy and approvals constrain subsequent host behavior; no identity/ultimate-policy question → authoritative organizational adjudication → returned governing decision loop is established.
- Why this is / is not agent-owned: NanoClaw has strong policy enforcement, but policy/approval existence is not S5, and the provider agent's own identity/prompt judgments are outside the repository boundary.
- Evidence: [`CLAUDE.md`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/CLAUDE.md), [`src/cli/guard.ts`](https://github.com/nanocoai/nanoclaw/blob/7902716b5b930215dbee4f56b8fb5b938d40468d/src/cli/guard.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: an operator or larger organization can act as a parent authority, but the standalone NanoClaw repository does not operationally close a first-party S5 path at this recursion.

### Absence scope

- Surfaces inspected: owner/admin role model, CLI scope, guard/approval pipeline, group identity/instructions, container configuration, host-only restrictions and customization flow.
- Plausible first-party paths checked: admin approval as S5; owner role as S5; `CLAUDE.md`/personality as S5; guard policy as S5; source customization as S5.
- Why no material first-party path remains: these surfaces define or enforce configuration and ordinary operational authority; they do not reconstruct a runtime identity/ultimate-policy adjudication loop inside NanoClaw.

## Distributed OSS / parent arrangement

NanoClaw is intentionally designed for operator customization and can sit inside a broader human-governed organization. Its owner/admin approval surfaces and source-level customization make such parent arrangements practical. This standalone assessment does not import those humans, Claude Code customization sessions or external agent runtimes as NanoClaw-owned VSM functions.

## Self-hosted / non-human modes

The host, DBs and container lifecycle are self-hosted, but the default autonomous agent still comes from the Claude Agent SDK. Switching to another provider does not create a NanoClaw-owned autonomous S1 merely because the provider is local or open-weight; each provider's agent loop remains separately implemented unless NanoClaw itself supplies the decisive operational loop.

## Recursion

Agent groups and sessions are strong containment/identity structures, and multiple hosted agents can form a larger composed organization. At the NanoClaw repository boundary, however, those autonomous operational units are provider-agent systems rather than NanoClaw-owned S1 units. Spawning more isolated sessions therefore does not by itself establish VSM recursion owned by NanoClaw.

## Variety and escalation

NanoClaw attenuates substantial infrastructural variety through channel normalization, entity routing, container isolation, mailbox persistence, stale recovery, scheduling, credential mediation and guards. Approval holds escalate privileged changes to owner/admin humans. These are meaningful runtime and governance mechanisms, but the autonomous task-level agent variety remains handled by the adjacent provider runtime.

## Evidence gaps

- The frozen trunk registers only the Claude provider; provider/channel branches are intentionally not borrowed into this review.
- A larger composed deployment that treats hosted provider agents plus NanoClaw control plane as one system-in-focus could support different VSM mappings, but that would be a different assessment boundary.
- The package/MCP self-mod path is explicitly documented because it is close to S4; under the standalone NanoClaw boundary, the autonomous proposer is external and the decisive approval is human, so it is not promoted to an autonomous NanoClaw S4 state.
- Proposed terminal outcome after review: `excluded-no-agentic-vsm` because the standard distribution does not establish a first-party autonomous S1 operational decision/action loop.
