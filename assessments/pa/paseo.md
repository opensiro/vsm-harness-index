---
harness_id: paseo
project_name: Paseo
repository: https://github.com/getpaseo/paseo
review_ref: d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Paseo

## Review boundary

- System in focus: Paseo's first-party daemon/control surface at frozen revision d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b, including AgentManager lifecycle, provider adapters, process/session state, workspaces/worktrees, clients, schedules, MCP host tools and subagent bookkeeping.
- Purpose and identity: provide one durable local/self-hosted control surface for launching, resuming, observing and composing coding agents across desktop, mobile, web, CLI and SDK clients.
- Relevant environment: external Claude Code, Codex, GitHub Copilot, OpenCode, Pi/OMP and ACP agent processes; their model providers; repositories/filesystems; users and remote clients.
- Standard-distribution boundary: Paseo daemon/server, clients, lifecycle persistence, workspace/worktree control, provider process adapters, schedules and first-party MCP tools are inside. The supported coding-agent executables, provider-native child agents and their reasoning/tool loops remain external.
- Credited operating / distribution surfaces: README.md; docs/agent-lifecycle.md; docs/providers.md; docs/custom-providers.md; packages/server agent manager/provider adapters; workspace/worktree lifecycle; MCP server/tool catalog; schedules and client/SDK control paths.
- Adjacent first-party surfaces excluded from ownership: repository contributor instructions, release skills, tests/e2e fixtures, CI/release workflows, website marketing surfaces and provider implementation details that merely translate external protocols.
- First-party operating / deployment modes considered: local daemon; desktop-managed daemon; headless/remote daemon; direct prompt/follow-up; SDK/API launch; schedules; agent-created subagents through Paseo MCP; provider-native subagents.
- Recursion level: one Paseo control plane supervising one or more external coding-agent sessions. Provider reasoning sessions are environmental workers, not Paseo-owned S1 reasoning loops.
- Reviewed revision: d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Paseo runs a local daemon that clients use to create and control coding-agent sessions. The README requires at least one supported agent CLI and describes the daemon as managing those coding agents. Provider adapters spawn or connect to the configured external agent process and translate its native protocol into Paseo's normalized session/timeline/permission interface.

AgentManager owns durable identity, lifecycle and persistence around those provider sessions. The lifecycle documentation explicitly says that provider processes own work parked inside them and that provider-managed child agents retain underlying runtime ownership at the provider. Paseo may import a child handle, expose it in the UI, archive it and route later prompts through the provider adapter, but it does not become the child's reasoning owner.

Paseo also exposes agent-scoped creation tools. A running agent can ask Paseo to create another managed agent or workspace, and skills such as handoff/advisor/committee teach an agent how to orchestrate other agents through Paseo. The orchestration decision originates in the calling external agent; Paseo supplies the reliable lifecycle/control substrate.

Counterfactual owner test: remove the external provider/agent executables while retaining the daemon, persisted agent records, clients, worktrees, schedules, MCP tools and process/session management. Paseo can still represent configuration and lifecycle state, but it cannot interpret an open-ended coding objective, choose substantive repository actions, observe semantic results and decide the next task action. First-party autonomous S1 therefore does not close.

Primary evidence:

- [README.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/README.md) — Paseo is one interface for external coding agents and requires an installed agent CLI.
- [docs/agent-lifecycle.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/agent-lifecycle.md) — durable lifecycle belongs to Paseo while provider runtime/process ownership and provider-native child execution remain with the provider.
- [docs/providers.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/providers.md) and [docs/custom-providers.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/custom-providers.md) — provider adapters launch external tools/protocols and normalize their capabilities rather than implement the reasoning loop.

## Operational model

A user, client integration, schedule or already-running agent asks the Paseo daemon to create or continue an agent session. Paseo selects the configured provider adapter, establishes the workspace/process/session boundary, then sends prompts and host capabilities to the external coding-agent runtime. The external runtime performs open-ended reasoning and emits messages/tool/permission events. Paseo persists and presents those events and can interrupt, resume, archive or compose sessions.

Agent-to-agent orchestration is similarly mediated: an external parent agent invokes a first-party Paseo MCP tool; Paseo creates the child and wires notification/lifecycle state; the child and parent decisions execute through their provider runtimes.

## S1 — Operations

- State: —
- Function: no first-party autonomous open-ended operational agent loop is established.
- Disturbance / variety regulated: Paseo regulates process/session availability, workspace placement, persistence, interruption and client access around coding work; semantic task variety is handled by the external provider agent.
- Decisive decision or feedback right: interpret the coding objective, choose substantive tool/repository actions, evaluate their results and choose the next action.
- Decision owner: the configured external coding-agent/provider runtime.
- Supporting / enforcement mechanisms: daemon, AgentManager, provider adapters, workspace/worktree manager, persisted timelines, permission transport and process controls.
- Closure path: prompt/control request → Paseo provider adapter → external agent reasoning/action loop → provider events/results → Paseo timeline/client.
- Boundary reachability: Paseo's control machinery is shipped and reachable, but ordinary task execution requires a provider runtime or external ACP/CLI agent.
- Why this is / is not agent-owned: first-party code owns lifecycle and host integration, not the open-ended reasoning/action feedback loop.
- Evidence: [README.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/README.md); [docs/agent-lifecycle.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/agent-lifecycle.md); [docs/providers.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/providers.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: provider adapters may expose Paseo-native host tools, but tool hosting does not transfer provider reasoning ownership.

### Absence scope

- Surfaces inspected: daemon/AgentManager lifecycle, provider adapters, workspaces/worktrees, sessions, schedules, clients/SDK, MCP tools, subagents and provider configuration.
- Plausible first-party paths checked: daemon as agent; lifecycle manager as S1; schedules as S1; Paseo MCP create_agent as S1; imported provider child as first-party S1.
- Why no material first-party path remains: every open-ended task path ultimately requires an external provider agent to choose semantic actions.

## S2 — Coordination

- State: —
- Function: Paseo provides orchestration primitives but no first-party autonomous S2 owner over Paseo-owned S1 units.
- Disturbance / variety regulated: parent/child relationships, handoff/advisor/committee patterns, workspace placement and finish notifications regulate multi-agent composition.
- Distinct S1 units: managed sessions can represent multiple external agents, but their S1 loops remain provider-owned.
- Inter-S1 disturbance: duplicate/overlapping work, parent-child lifecycle and return of delegated results are materially represented.
- Attenuating coordination relation: Paseo can create child agents, stamp parentage, notify parents on finish/permission and cascade/detach lifecycle.
- Feedback into subsequent S1 behaviour: child completion/permission events can wake or inform the external parent agent.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the primitives explicitly support delegated child work and return-to-parent coordination, but the discretionary coordination judgment is made by the external parent agent.
- Decisive decision or feedback right: decide whether/what to delegate and how to use returned child results.
- Decision owner: external parent/provider agent.
- Supporting / enforcement mechanisms: agent-scoped create_agent MCP, parent-agent metadata, notify-on-finish, child lifecycle, skills and provider-subagent import.
- Closure path: external parent decides delegation → Paseo creates/routes child → external child acts → Paseo notifies parent → external parent decides next step.
- Boundary reachability: orchestration primitives are first-party, but the coordinating actor is external.
- Why this is / is not agent-owned: deterministic composition support is not itself the autonomous coordination decision owner.
- Evidence: [docs/agent-lifecycle.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/agent-lifecycle.md); [README.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/README.md).
- Basis: explicit + structural negative publication review.
- Confidence: high.
- Caveats: Paseo is a useful constructor/control substrate for multi-agent organizations; that does not import their autonomous S2 owner.

### Absence scope

- Surfaces inspected: child creation, provider subagents, parent notifications, skills/handoff patterns, workspace relations and lifecycle cascade.
- Plausible first-party paths checked: create_agent tool as S2 owner; committee skill as S2; lifecycle cascade as coordination; imported provider subagents.
- Why no material first-party path remains: the first-party substrate executes coordination mechanics while external agents own coordination judgments and all underlying S1 loops.

## S3 — Inside-and-now control

- State: —
- Function: no first-party autonomous whole-system current-control loop is established.
- Disturbance / variety regulated: process health, interruption, archive/reload, session split-brain avoidance, workspace state and client attention are regulated.
- Whole-system current view: Paseo aggregates agent/workspace lifecycle and activity state.
- Current-control decision scope: first-party logic makes deterministic lifecycle/safety decisions, while task/resource priorities and commitments are user/external-agent decisions.
- Decisive decision or feedback right: discretionary current intervention across an internal operational organization.
- Decision owner: no qualifying autonomous first-party owner; control is split between deterministic daemon rules, users and external provider agents.
- Supporting / enforcement mechanisms: AgentManager queues, interrupt semantics, archive/reload rules, workspace activity aggregation and process supervision.
- Closure path: lifecycle facts can deterministically alter process/session state; semantic current-control decisions remain outside.
- Boundary reachability: lifecycle control is shipped, but the necessary internal S1 organization and discretionary controller are absent.
- Why this is / is not agent-owned: robust process/session supervision is enforcement, not whole-system organizational judgment.
- Evidence: [docs/agent-lifecycle.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/agent-lifecycle.md).
- Basis: structural negative review.
- Confidence: high.
- Caveats: users can supervise many agents through Paseo, but a generic operator surface is not sufficient for Methodology S3 parent notation.

### Absence scope

- Surfaces inspected: lifecycle state, runtime residency, cancellation, archive/reload, workspace activity, clients and session controls.
- Plausible first-party paths checked: AgentManager as S3; process supervisor; workspace activity aggregation; user command center.
- Why no material first-party path remains: control is deterministic lifecycle enforcement or external human/provider discretion rather than autonomous whole-system current control.

## S3* — Complementary audit

- State: —
- Function: no independent first-party semantic audit/challenge loop with corrective return is established.
- Disturbance / variety regulated: timelines, provider events, status and permission records expose activity and failures.
- Claim being audited: whether external agent work is semantically correct or meets the task objective.
- Ordinary reporting path: provider-generated messages/tool events/timeline.
- Complementary access path: Paseo independently persists lifecycle and stream metadata but does not establish an independent semantic evaluator.
- Independence boundary: storage/transport is separate from provider reasoning, but no separate judgment owner is shown.
- Who acts on findings: users or external agents.
- Decisive decision or feedback right: independently challenge/accept work and return correction.
- Decision owner: no first-party autonomous auditor.
- Supporting / enforcement mechanisms: timelines, status/error records, permission requests and client review.
- Closure path: recorded evidence → external/human interpretation → optional follow-up.
- Boundary reachability: observability is first-party; independent audit judgment is not.
- Why this is / is not agent-owned: recording an external agent's stream is not a complementary audit.
- Evidence: [docs/agent-lifecycle.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/agent-lifecycle.md).
- Basis: structural negative review.
- Confidence: high.
- Caveats: a user can launch a separate reviewer agent, but that reviewer remains an external provider runtime.

### Absence scope

- Surfaces inspected: timelines, errors, permissions, subagent tracking, client review and session history.
- Plausible first-party paths checked: timeline as audit; provider diagnostics; separate reviewer via orchestration.
- Why no material first-party path remains: evidence capture exists without an independent first-party semantic audit judgment and corrective return.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party autonomous prospective adaptation loop is established.
- Disturbance / variety regulated: schedules, provider discovery/configuration and plugin/provider updates affect future sessions.
- External distinction: provider capabilities and external events/configuration can be observed.
- Future / prospective distinction: users can change provider/model/workspace/schedule configuration for later runs.
- Adaptation option generated: no autonomous first-party process is shown selecting strategic/capability adaptation from external intelligence.
- Path back into current capability / S3: operator configuration or software update changes later capability.
- Decisive decision or feedback right: choose prospective adaptation and reinject it.
- Decision owner: users/maintainers/external agents.
- Supporting / enforcement mechanisms: provider catalog/config, schedules, plugins, persisted profiles and session restore.
- Closure path: no autonomous sense → model future → choose adaptation → reinject loop.
- Boundary reachability: configuration is shipped; adaptation judgment is external.
- Why this is / is not agent-owned: dynamic provider discovery and scheduling are capability/config mechanics, not prospective intelligence ownership.
- Evidence: [docs/providers.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/providers.md); [docs/custom-providers.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/custom-providers.md).
- Basis: structural negative review.
- Confidence: high.
- Caveats: external agents can reason about future changes using Paseo tools, but their reasoning is outside the first-party boundary.

### Absence scope

- Surfaces inspected: schedules, provider catalog/discovery, profiles, plugins, session restore and configuration.
- Plausible first-party paths checked: provider discovery as S4; schedules; plugin updates; persistent sessions/learning.
- Why no material first-party path remains: these surfaces expose or configure future capability without autonomously choosing adaptation.

## S5 — Policy and identity

- State: —
- Function: no first-party autonomous identity/ultimate-policy resolution loop is established.
- Disturbance / variety regulated: provider selection, permissions, tool availability, workspace isolation and daemon configuration constrain execution.
- Identity / ultimate-policy issue: configuration expresses operator policy rather than runtime resolution of an identity/ultimate-policy tension.
- Ultimate authority in each claimed mode: user/operator configuration and external provider policy.
- Return-to-operation path: configuration is applied to later sessions.
- Decisive decision or feedback right: resolve ultimate identity/policy and authoritatively govern operation.
- Decision owner: human/operator; no autonomous first-party owner.
- Supporting / enforcement mechanisms: config.json, provider profiles, permission handling, plugins, workspace controls and client authentication/connectivity.
- Closure path: operator setting → daemon/provider enforcement → external-agent operation.
- Boundary reachability: enforcement is shipped; ultimate-policy judgment remains external.
- Why this is / is not agent-owned: permissions and provider configuration implement selected policy rather than autonomously own S5.
- Evidence: [docs/custom-providers.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/docs/custom-providers.md); [README.md](https://github.com/getpaseo/paseo/blob/d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b/README.md).
- Basis: structural negative review.
- Confidence: high.
- Caveats: self-hosting gives users strong parent control, but ordinary configuration alone is not S5 parent closure.

### Absence scope

- Surfaces inspected: provider/tool configuration, permissions, plugins, workspace isolation, daemon/client modes and self-hosting.
- Plausible first-party paths checked: provider profile as identity; permissions as S5; self-hosted operator as parent S5.
- Why no material first-party path remains: no runtime identity/ultimate-policy decision loop beyond operator-selected configuration is established.

## Recursion

Paseo is assessed as a control/lifecycle layer around externally implemented agent runtimes. It can compose those runtimes into parent/child organizations and preserve durable relationships, but provider cognition remains separate.

## Variety and escalation

Paseo attenuates variety with provider normalization, durable lifecycle state, workspaces/worktrees, cancellation semantics, permissions, schedules, parent-child tracking and cross-device control. Failures and permission checkpoints are surfaced to users or parent agents. These are meaningful harness capabilities without a first-party autonomous S1.

## Evidence gaps

- Frozen-ref only; later repository changes are not considered.
- Provider-specific reasoning, memory and native subagents are intentionally not imported.
- Hosted/relay infrastructure is transport, not evidence of autonomous organizational ownership.
- External agents can use Paseo's own MCP tools to create sophisticated organizations; that constructor use does not make Paseo the decision owner.

## Assessment summary

At frozen revision d636abd7a4ce302e7ccb9eb6074f637c6dd4d83b, Paseo is a durable first-party lifecycle, workspace and orchestration control plane for external coding-agent processes. The provider process owns the open-ended objective → decision → action → observation → next-decision loop, including provider-native child agents. Under Profile 0.2.4 / Methodology 0.3.6, first-party autonomous S1 does not close, so the proposed terminal disposition is excluded-no-agentic-vsm.

**Vector:** — · — · — · — · — · —
