---
harness_id: 1code
project_name: 1Code
repository: https://github.com/21st-dev/1code
review_ref: 9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e
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

# 1Code

## Review boundary

- System in focus: the first-party 1Code desktop/web control application at frozen revision `9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e`, including worktree/sandbox/session lifecycle, message queues, automation/task API, Git/PR delivery, plan/review UI, MCP/plugin/configuration and agent integration routers.
- Purpose and identity: launch, isolate, monitor and steer coding-agent sessions locally or in cloud sandboxes, and expose their work through a collaborative developer UI/API.
- Relevant environment: users, Git repositories, Claude Code/Codex runtimes, model/provider credentials, sandboxes, GitHub/Linear/Slack events and MCP services.
- Standard-distribution boundary: 1Code Electron/web/server integration, worktree/sandbox/session/queue/automation/Git/UI code is inside. Claude Code/Claude Agent SDK and Codex/ACP agent runtimes are external decision-making engines even when their binaries/packages are bundled or downloaded by 1Code.
- Credited operating / distribution surfaces: README.md; package.json; `src/main/lib/trpc/routers/claude.ts`; `src/main/lib/trpc/routers/codex.ts`; worktree, chat/session, agent/configuration and automation surfaces.
- Adjacent first-party surfaces excluded from ownership: repository contributor/CI/release tooling, project-development CLAUDE.md/AGENTS.md, and the internal reasoning/tool loops of bundled external agent runtimes.
- First-party operating / deployment modes considered: local Claude/Codex sessions, isolated worktrees, background/cloud execution, queued/forked chats, plan mode, automations/API tasks and follow-up steering.
- Recursion level: one 1Code-managed coding work organization around one or more externally implemented coding-agent sessions.
- Reviewed revision: `9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e`.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The frozen README defines 1Code as an “open-source coding agent client” for Claude Code, Codex and other agents. Source builds explicitly require `claude:download` and `codex:download`; the README says agent functionality does not work correctly without those binaries. The source then supplies first-party routers, worktrees, queues, sandboxes, terminal/Git surfaces and UI around those engines. `codex.ts` uses an ACP provider over Codex, while Claude integration is built around the Claude agent runtime/configuration and bundled Claude binary.

Counterfactual owner test: remove Claude/Codex agent runtimes while retaining 1Code's worktrees, sandboxes, chat/session DB, message queue, automations, Git/PR delivery and UI. The remaining application can create and control execution environments but cannot interpret an open-ended coding objective, choose semantic code/tool actions from observations and continue the reasoning loop. First-party S1 therefore does not close.

Primary evidence:

- [README.md](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md)
- [package.json](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/package.json)
- [Claude router](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/trpc/routers/claude.ts)
- [Codex router](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/trpc/routers/codex.ts)

## Operational model

A user, automation or API request selects a project/session and an agent runtime. 1Code prepares a worktree/sandbox and integration settings, starts or connects to the selected external agent, streams its messages/tool activity, persists session state and exposes queue/plan/review/Git controls. The external agent runtime owns the semantic objective/action/observation loop.

## S1 — Operations

- State: —
- Function: no first-party autonomous open-ended coding operation is established.
- Disturbance / variety regulated: workspace isolation, session/process availability, queues, Git delivery and agent configuration are regulated; semantic coding-task variety is absorbed by Claude/Codex.
- Decisive decision or feedback right: interpret the objective, choose semantic repository/tool actions, evaluate results and choose the next action or completion.
- Decision owner: external Claude Code/Claude agent or Codex agent runtime.
- Supporting / enforcement mechanisms: worktrees, sandboxes, tRPC routers, queues, session persistence, Git/PR tooling, MCP/plugins and UI.
- Closure path: prompt/task → 1Code integration → external agent reasoning/tool loop → repository/tool result → external agent next decision → 1Code stream/state.
- Why this is / is not agent-owned: 1Code hosts and controls the operation but does not supply the task-semantic decision loop.
- Evidence: README.md; package.json; Claude and Codex routers.
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: bundling/downloading an agent binary is distribution support, not transfer of its organizational decision ownership.

### Absence scope

- Surfaces inspected: README/build dependencies, Claude/Codex routers, chat/session lifecycle, worktrees, sandboxes, queues, automations/API, MCP/plugins and Git/PR delivery.
- Plausible first-party paths checked: desktop “agent” mode; plan mode; automation executor; API task executor; Claude router; Codex router.
- Why no material first-party path remains: every open-ended coding path depends on a separate Claude/Codex agent runtime for semantic action selection.

## S2 — Coordination

- State: —
- Function: isolation, queues and multi-session UI exist without a first-party autonomous inter-S1 interference attenuation judgment loop.
- Disturbance / variety regulated: worktrees reduce cross-session file interference; queues serialize user prompts; multiple sessions can coexist.
- Decisive decision or feedback right: select/revise a coordination response to a concrete disturbance among distinct operational S1 units and feed it back into their behaviour.
- Decision owner: user/external agents or deterministic configuration; no first-party autonomous owner established.
- Supporting / enforcement mechanisms: per-chat worktrees, message queues, sandbox/session separation, Kanban/session views.
- Closure path: deterministic isolation/queue rules constrain external sessions; no first-party agent chooses an interference-specific coordination response.
- Why this is / is not agent-owned: isolation and ordering can support coordination but do not establish agent-owned S2 discretion here.
- Evidence: README.md; worktree/chat/session surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: external Claude subagents are not imported as first-party S1/S2 units.

### Absence scope

- Surfaces inspected: worktree isolation, queues, background sessions, sub-agent UI, automations and multi-session views.
- Plausible first-party paths checked: per-chat worktrees; queue arbitration; Kanban/task routing; sub-agent display.
- Why no material first-party path remains: no first-party autonomous coordination actor closes a concrete inter-S1 attenuation loop.

## S3 — Inside-and-now control

- State: —
- Function: process/session/workspace lifecycle and operator steering exist without an autonomous whole-system current-control judgment.
- Disturbance / variety regulated: running sessions, queues, sandbox health, Git state, plan approval and background tasks.
- Decisive decision or feedback right: discretionary allocation/prioritization/intervention across current operational commitments.
- Decision owner: human/operator or external agent; first-party code transports/enforces commands.
- Supporting / enforcement mechanisms: session/Kanban UI, stop/follow-up controls, automation/task API, queues, sandbox lifecycle.
- Closure path: current state → human/external judgment or deterministic rule → 1Code control action → later external-agent operation.
- Why this is / is not agent-owned: visibility and lifecycle control do not establish first-party autonomous S3 ownership.
- Evidence: README.md; session/task/automation surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: background-agent continuity is operational hosting rather than S3 discretion.

### Absence scope

- Surfaces inspected: session/Kanban status, queues, sandbox lifecycle, plan controls, task API and background agents.
- Plausible first-party paths checked: automation scheduler; queue manager; session supervisor; plan approval; stop/follow-up.
- Why no material first-party path remains: no first-party autonomous whole-system controller selects current priorities/resources/commitments.

## S3* — Complementary audit

- State: —
- Function: diff previews, plan review and execution history expose evidence but do not package an independent first-party semantic auditor.
- Disturbance / variety regulated: users can inspect plans, diffs, commands and PR delivery.
- Decisive decision or feedback right: independently challenge an operational result from complementary access and return corrective findings.
- Decision owner: human/user or external agent.
- Supporting / enforcement mechanisms: diff viewer, Git client, plan review UI, tool-event display and rollback.
- Closure path: execution evidence → user/external review → optional follow-up/rollback.
- Why this is / is not agent-owned: evidence presentation and approval are not an independent first-party audit judgment.
- Evidence: README.md.
- Basis: structural absence review.
- Confidence: high.
- Caveats: a hosted external agent may review work, but its cognition remains external.

### Absence scope

- Surfaces inspected: plan review, diff preview, Git/PR state, tool events, rollback, automation history.
- Plausible first-party paths checked: plan approval; diff review; PR review automation; rollback.
- Why no material first-party path remains: no separately instantiated first-party semantic evaluator with complementary evidence and corrective-return ownership is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: durable sessions, skills, models/providers and automations exist without autonomous prospective organizational adaptation.
- Disturbance / variety regulated: users can alter agents/models/providers/plugins/skills and recurring triggers.
- Decisive decision or feedback right: interpret external/prospective change and select a durable capability adaptation.
- Decision owner: user/maintainer or external agent.
- Supporting / enforcement mechanisms: model selector, skills, plugins/MCP, CLAUDE.md/AGENTS.md, automations and persisted state.
- Closure path: external/user selection → configuration → later external-agent run.
- Why this is / is not agent-owned: persistence/configurability/recurrence do not create a first-party prospective adaptation chooser.
- Evidence: README.md; settings/plugin/skill surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: external agents may reason about future changes inside their own loops.

### Absence scope

- Surfaces inspected: skills, plugins/MCP, model/provider selection, memory/project instructions, automations and persistent chats.
- Plausible first-party paths checked: memory as learning; automation as adaptation; model switching; skill changes.
- Why no material first-party path remains: durable capability changes are selected outside the first-party control plane.

## S5 — Policy and identity

- State: —
- Function: permissions, authentication, configuration and branch safety enforce policy without autonomous identity/ultimate-policy resolution.
- Disturbance / variety regulated: credentials, project/worktree boundaries, provider settings, plan approval and execution modes.
- Decisive decision or feedback right: resolve identity/ultimate-policy tensions and return authoritative policy into operation.
- Decision owner: user/operator/configuration.
- Supporting / enforcement mechanisms: auth/credential storage, plan/agent modes, settings, branch/worktree safety and access controls.
- Closure path: externally selected policy → first-party enforcement → external-agent operation.
- Why this is / is not agent-owned: policy enforcement is not autonomous policy ownership.
- Evidence: README.md; configuration/auth surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: archived repository status is provenance, not an S5 state.

### Absence scope

- Surfaces inspected: auth/credentials, modes, project/worktree policy, plugins/settings and approval UI.
- Plausible first-party paths checked: plan approval; branch safety; auth/provider settings; AGENTS/CLAUDE instructions.
- Why no material first-party path remains: ultimate policy decisions originate with users/maintainers or external agents.

## Recursion

1Code is assessed as the control/client organization around external coding-agent sessions. Its worktree, queue, automation and Git surfaces are first-party mechanisms, while the reasoning actors remain separate systems.

## Variety and escalation

1Code attenuates variety through worktree/sandbox isolation, queues, session persistence, automation triggers, Git/PR integration, MCP/plugins and operator UI. Semantic coding variety is delegated to external agent runtimes; approval/steering escalates to the user.

## Evidence gaps

- Frozen archived revision only.
- Proprietary hosted-service internals not present in the repository are not credited.
- Claude/Codex internal functions are not imported even when binaries are packaged/downloaded by 1Code.

## Assessment summary

At the frozen revision, 1Code is a substantial agent client/control plane around Claude Code and Codex. Its own repository controls isolation, lifecycle, automation, queueing and delivery, but the open-ended reasoning/tool loop remains in the external agent runtimes. Proposed terminal disposition: excluded-no-agentic-vsm.

**Vector:** — · — · — · — · — · —
