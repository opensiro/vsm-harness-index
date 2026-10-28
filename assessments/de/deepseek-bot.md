---
harness_id: deepseek-bot
project_name: deepseek-bot
repository: https://github.com/rlaope/deepseek-bot
review_ref: d247b0c9e8c4c7c07a7e8b113077fdc0353e5247
reviewed_at: 2026-10-28
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
autonomy_s5: P
---

# deepseek-bot

## Review boundary

- System in focus: deepseek-bot's shipped long-running personal-agent gateway composition, persona/home and conversation execution adapter.
- Purpose and identity: one persistent personal agent that carries out requested work and authorized reminders/watches across terminal and messaging conversations.
- Relevant environment: users, workspace/documents, external information and MCP services, model provider, messaging transports and operator deployment.
- Standard-distribution boundary: repository gateway profile/bundle, in-process agent/session adapter, agent instructions/persona, recall/context, background/watch services and confinement/approval integration.
- Credited operating / distribution surfaces: index.ts, profile/package.json and cordis.patch.yml, agent/AGENTS.md and SOUL.md, notes/recall, transports and watch/service paths wired by installation.
- Adjacent first-party surfaces excluded from ownership: repository development AGENTS/CLAUDE, scenario runner and tests, QA/benchmark claims, release/maintenance work; underlying DeepSeek Harness supplies engine services, not borrowed organizational conclusions.
- First-party operating / deployment modes considered: installed gateway with standard preset, local terminal plus one messenger, durable conversation resume, tenant homes, operator deployment policy and user-directed persona changes; mock tests are corroboration only.
- Recursion level: one deployed personal-agent organization with conversation operations; no model-provider/company recursion is assessed.
- Reviewed revision: `d247b0c9e8c4c7c07a7e8b113077fdc0353e5247`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The plugin runs inside a DeepSeek Harness gateway and explicitly resolves/mounts its agent preset, creates or resumes in-process agent handles, submits identified messages, waits for completion and flushes durable sessions. The first-party profile supplies the base/schedule/plugin composition and tool/permission wiring; the installed agent home supplies identity and operating rules. Before turns, the adapter reads SOUL/USER/MEMORY, channel-scoped recall and current conversation context, reinjecting standing context when its digest changes. It serializes conversation turns, limits global concurrency, gates destructive actions, confines tenant reads and uploads named results. Background jobs keep an agent alive until delivery or a configured deadline. Model-authored watch files are run read-only with baseline/change/rate-limit semantics. Health probes supervise connection/service health. Source-development agents and provider-backed scenario tests are adjacent.

## Operational model

The substantive S1 actor is the in-process model/tool agent assembled by the shipped profile and adapter, not the messaging transport. Memory and watch mechanisms support its work. First-party identity instructions distinguish user-owned identity changes from autonomous task/memory editing and from operator-owned deployment settings. The S5 parent mode below is specifically the user-directed purpose/persona return path; credentials, routine approval prompts and technical settings are not automatically S5. Conversation serialization and generic inherited subagent facilities do not by themselves establish inter-unit coordination or whole-system control.

## S1 — Operations

- State: A
- Function: carry out user-requested personal-agent work with tools and durable context
- Disturbance / variety regulated: new requests, unfamiliar files/information, tool failures, interruptions and delayed work
- Decisive decision or feedback right: choose tool actions, interpret results, revise output and complete requested work
- Decision owner: model agent created/resumed through the first-party gateway composition
- Supporting / enforcement mechanisms: DeepSeek engine services, mounted standard preset/tools, context/recall, durable sessions, confinement and approval transport
- Closure path: inbound request → profile/preset and contextualized agent.followup → model/tool results → resumed decisions → answer/artifact or background completion delivery
- Why this is / is not agent-owned: removing the model preserves transport/session machinery but removes substantive work choices
- Boundary reachability: profile/package.json installs base/schedule/deepbot bundles; index.ts mounts the agent preset and ships the personal-agent instructions/home rather than leaving an arbitrary external ACP command uncomposed
- Evidence: [index.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/index.ts), [profile/package.json](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/profile/package.json), [profile/cordis.patch.yml](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/profile/cordis.patch.yml), [agent/AGENTS.md](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/agent/AGENTS.md), [types/core.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/types/core.ts).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

## S2 — Coordination

- State: —
- Function: no first-party S2-specific discretionary coordination path established
- Disturbance / variety regulated: concurrent turns, duplicate transport delivery and tenant context crossing
- Decisive decision or feedback right: serialize one conversation, apply configured concurrency and bind each session to its home
- Decision owner: deterministic adapter/configuration, not a coordinating agent
- Supporting / enforcement mechanisms: per-conversation promise chain, global queue, durable session keys and read/tenant fences
- Closure path: queued turns and scoped context enter subsequent requests, without autonomous inter-S1 conflict regulation
- Why this is / is not agent-owned: serialization of one conversational operation and isolation/routing alone do not establish S2
- Evidence: [index.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/index.ts), [transports/composite.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/transports/composite.ts), [docs/how-it-works.md](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/docs/how-it-works.md).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: global/per-conversation queues, tenant/session adoption, transports, background jobs and inherited subagent references
- Plausible first-party paths checked: same-session concurrent use/retry, queued steering, tenant isolation, duplicate events and subagent display
- Why no material first-party path remains: these supply bounded execution/context routing; no first-party relation gives an actor a specific inter-operational conflict/oscillation response and returned coordination discretion; hypothetical custom subagent schemes are not credited

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control organization established
- Disturbance / variety regulated: busy conversations, timeouts and background-job lifetime
- Decisive decision or feedback right: configured concurrency/deadlines and per-conversation stop/usage/model choices
- Decision owner: operator for fixed deployment constraints; user/model for local task decisions
- Supporting / enforcement mechanisms: global cap, cancellation registry, job keep/release limits, usage totals and health restart
- Closure path: local stop or timeout cancels work; no whole-personal-agent portfolio resource/commitment judgment-return loop
- Why this is / is not agent-owned: hard limits and direct stop/approval do not own S3 or establish a qualifying parent mode
- Evidence: [index.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/index.ts), [usage.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/usage.ts), [service/health-check.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/service/health-check.ts), [docs/limitations.md](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/docs/limitations.md).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: queue/cap, background retention, stop/usage/model commands, approvals and operator/service modes
- Plausible first-party paths checked: global maxConcurrency, job deadline/cancellation, per-thread metrics and external health recovery
- Why no material first-party path remains: inspected paths govern task/service lifecycle under selected rules; no shipped regulator or parent interface closes whole-system commitments/resources beyond those generic controls

## S3* — Complementary audit

- State: —
- Function: no complementary independent operational audit established
- Disturbance / variety regulated: possible task errors, memory hygiene and disconnected gateway health
- Decisive decision or feedback right: self-verify task work, inspect note budgets or restart unhealthy connection
- Decision owner: operational model or deterministic hygiene/health service, not an independent complementary auditor
- Supporting / enforcement mechanisms: mock tests, scenario tooling, logging, persona checks and health probe
- Closure path: routine task verification, note tidy-up advice or service restart
- Why this is / is not agent-owned: self-checks and technical liveness checks do not establish materially independent organizational audit
- Evidence: [agent/SOUL.md](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/agent/SOUL.md), [notes.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/notes.ts), [service/health-check.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/service/health-check.ts), [tools/persona-check.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/tools/persona-check.ts).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: task self-verification, note/persona checks, service health, mock/scenario separation and recall index
- Plausible first-party paths checked: external health probe, document structural checks, reported tests and retained session artifacts
- Why no material first-party path remains: these check production shape/liveness or occur in adjacent QA; none supplies independent audit judgment that challenges operational claims through complementary access and returns corrective control

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally prospective capability-adaptation loop established
- Disturbance / variety regulated: changed external watch values, recalled conversations and growing notes
- Decisive decision or feedback right: create requested watches, retain facts/skills and respond when a condition changes
- Decision owner: operational agent and user request; no specific S4 adaptation owner
- Supporting / enforcement mechanisms: read-only watch runner, recall ranker, note hygiene and filesystem skills
- Closure path: observation/recall enters a task reply or maintained notes, not a prospective capability option returned into current regulation
- Why this is / is not agent-owned: external sensing and reusable memory alone are not outside-and-then adaptation
- Evidence: [watch/watch.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/watch/watch.ts), [agent/AGENTS.md](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/agent/AGENTS.md), [recallContext.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/recallContext.ts), [notes.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/notes.ts), [docs/limitations.md](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/docs/limitations.md).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

### Absence scope

- Surfaces inspected: watch creation/change detection, reminder delivery, recall selection, note/skill writing and operator MCP setup
- Plausible first-party paths checked: externally monitored conditions, model-selected recall implications, procedural skills and operator-added tools
- Why no material first-party path remains: shipped procedures produce requested reports or retain work methods; they do not develop prospective environmental adaptation options and close a capability-change conversation with current control; a future custom watch/workflow is not credited

## S5 — Policy and identity

- State: P
- Function: parent-governed maintenance of the personal agent’s identity and purpose
- Disturbance / variety regulated: a user changes who the agent is, whose agent it is or its durable role/voice
- Decisive decision or feedback right: authorize an identity/purpose change and return it as the governing persona
- Decision owner: legitimate user/owner in the installed personal-agent mode; model records the directive, not an autonomous ultimate authority
- Supporting / enforcement mechanisms: agent-home SOUL.md, explicit user-only identity-change instruction, contextualized inbound speaker and standing-context digest/reload
- Closure path: user identity directive → operational model applies the user-owned persona change in SOUL.md → adapter rereads and reinjects changed [who you are] context → subsequent turns follow that identity
- Why this is / is not agent-owned: parent owns who-you-are choice; file editing and digest injection implement its return. Autonomous memory/rule tidying is not credited as S5=A
- Boundary reachability: installed agent/AGENTS.md specifically says SOUL changes only when the user changes who the agent is; identityText permits writing it and contextPreamble rereads that exact file before turns
- Identity / ultimate-policy issue: durable personal-agent identity, owner and purpose in SOUL.md, distinct from ordinary task approval or a model/provider setting
- Ultimate authority in each claimed mode: the user/owner for persona/purpose in this supported parent mode; no autonomous S5 mode or project-governance authority is claimed
- Return-to-operation path: writable SOUL.md is reread as [who you are], digest-gated changed content precedes the next user request; tests corroborate persona injection, not the semantic ownership judgment
- Evidence: [agent/AGENTS.md](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/agent/AGENTS.md), [agent/SOUL.md](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/agent/SOUL.md), [index.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/index.ts), [test/core.test.ts](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/test/core.test.ts), [profile/cordis.patch.yml](https://github.com/rlaope/deepseek-bot/blob/d247b0c9e8c4c7c07a7e8b113077fdc0353e5247/profile/cordis.patch.yml).
- Basis: structural.
- Confidence: medium-high for bounded source inspection.
- Caveats: source-based ownership mapping; no live model/provider run or effectiveness claim.

## Distributed OSS parent arrangement

The positive parent mode is local to the personal-agent deployment/tenant, not an organization-level claim about repository maintainers. Contributor instructions and release decisions do not supply this runtime’s S5.

## Self-hosted and non-human modes

Operators select platform/provider/credentials and confinement outside the agent home. User-directed identity governance is a different right from those technical settings. The source does not establish autonomous ultimate-policy resolution or a fully non-human organization.

## Recursion

Conversation sessions, tenants and background jobs are operational decomposition. Their existence does not establish complete recursively viable units.

## Variety and escalation

Context/recall amplify the operational model’s distinctions; channel scoping, permission gates, timeouts and sandbox fences attenuate exposure/action. Model-written watches are requested sensing work. Refusals and health failures do not automatically establish algedonic governance.

## Evidence gaps

Source-based supported-mode assessment; no live provider, real messaging account or browser-quality/agent E2E run. The DeepSeek engine is an external release-candidate dependency with documented interface risks. Native build passed; mock core 484/484, dry-run watches 20/20 and note hygiene 14/14 checks passed. These validate wiring/behavior, not independent semantic review. S5=P is bounded to user-owned identity return, not all security, commercial or deployment-policy decisions.
