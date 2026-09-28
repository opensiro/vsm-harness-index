---
harness_id: platypus
project_name: Platypus
repository: https://github.com/willdady/platypus
review_ref: 5dda4dcdb92c209c8c8df953f0e9261cd018c2d7
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Platypus

## Review boundary

- System in focus: one self-hosted Platypus Workspace operating cell at pinned revision `5dda4dcdb92c209c8c8df953f0e9261cd018c2d7`, including first-party Agent execution, Trigger-fired unattended runs, Workspace-scoped Boards/Dashboards/tools, callable Sub-Agents, run lifecycle, Memory/Context and Workspace policy surfaces.
- Purpose and identity: provide a durable team Workspace in which configured model-driven Agents perform substantive work interactively or unattended, can delegate bounded specialist work, act on shared Workspace resources, and run from schedules/events while remaining isolated from other Workspaces.
- Relevant environment: Workspace users and owner/admin authority, user requests, scheduled time, Workspace events, Boards/Dashboards and their records, tool/MCP/browser/sandbox observations, model/provider endpoints, stored memory/context, run failures and feedback cycles between event-driven operations.
- Standard-distribution boundary: the public self-hosted application at the frozen revision. External model providers, MCP servers, remote web/data sources and plugin-provided implementations are dependencies unless their organizational decision is made by first-party Platypus runtime code.
- Credited operating / distribution surfaces: `runs/agent-runner.ts`; `services/chat-execution.ts`; model/tool drive; Trigger scheduling/firing/event dispatch; Trigger run-rate breaker; Workspace resources/tools; first-party Sub-Agent delegation; Workspace Context composition and owner/admin update surfaces.
- Adjacent first-party surfaces excluded from ownership: repository contributor governance; CI/release machinery; docs/tests except as evidence; user-authored arbitrary Agent topologies that are possible but not wired as a first-party organizational function; Organization-wide administration except where it is a parent authority for the assessed Workspace; generic CRUD/tool availability without a closed function at this recursion.
- First-party operating / deployment modes considered: interactive Agent Chat; headless Trigger Agent runs; event-triggered Agent runs; callable Sub-Agent delegation; Agent/Trigger management tools; Workspace Memory/Context; Boards/Dashboards/Notifications; sandbox/MCP/web tools.
- Recursion level: one Workspace is the system-in-focus. Individual model-driven Agent runs, including Trigger-backed runs, are S1 operational units when they perform substantive Workspace outcomes. A coordinator Agent with its Sub-Agents may form a narrower task-level organization, but that nested recursion is not silently lifted into Workspace-level S3/S3*.
- Reviewed revision: `5dda4dcdb92c209c8c8df953f0e9261cd018c2d7`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Platypus is a full-stack multi-tenant AgentOS. A Workspace contains reusable Agents whose saved configuration pins model/provider, Instructions, tools, Skills and optional Sub-Agents. The backend resolves each turn, composes a first-party system prompt, builds the available tool surface and drives the model/tool loop through the shared `AgentRunner`. The same runner supports interactive Chats and headless Trigger executions, with run lifecycle, timeouts, persistence and cancellation managed server-side.

Sub-Agents are first-party delegated Agent runs. The parent receives one `delegate` tool and the catalogue of configured specialists, chooses a target and gives it a self-contained task. A delegated Agent keeps its own model, Instructions and tools, returns its result to the parent, and cannot recursively delegate further. This is a useful nested task organization but delegation by itself is not credited as Workspace-level S2 or S3.

The stronger coordination witness is the event-trigger runtime. Trigger-fired Agents can mutate shared Workspace entities such as Board records, which can emit events that fire other Triggers. Platypus explicitly documents that two Triggers can hand the same record back and forth without crossing the self-actor guard. A first-party rolling run-rate breaker counts normal runs per `Trigger × entity` and suppresses excess firings before another Agent is invoked. This is a concrete interference/oscillation attenuation path and is credited as S2, with deterministic/runtime ownership.

No first-party Workspace-wide current regulator was found. Platypus exposes rich Agent/Trigger management, run listings, Boards, Dashboards and a parent Agent can coordinate specialists inside one task, but these surfaces do not establish a standing actor that observes the Workspace's current operational portfolio as a whole and closes a current-control loop over it. Likewise, user-configurable reviewer/fact-checker Agents are possible through ordinary Sub-Agent composition, but the platform does not wire a separate complementary audit path that independently checks normal S1 results and feeds findings into correction.

Memory summarizes prior Chat activity and Context supplies persistent framing; Triggers react to schedules/events and Agents can use web/MCP tools. These mechanisms do not establish a distinct external-and-prospective adaptation function. Workspace identity/policy does have a parent-owned path: the Workspace `context` field is administered by the Workspace Owner or Org Admin and is rendered into the system prompt for Workspace operation, so changes return into later Agent runs. That closes parent-governed S5.

## Operational model

At Workspace recursion, model-driven Agent runs are S1. Event-trigger Agent runs can interfere by recursively producing events on the same shared entity; deterministic first-party breaker logic attenuates that loop, giving S2=`C`. Generic orchestration and management surfaces do not establish a Workspace-wide S3 owner, and ordinary Sub-Agent composition does not establish a distinct S3* audit channel. Memory/event reaction do not satisfy outside-and-then S4. The legitimate Workspace owner/admin controls durable Workspace Context returned into later system prompts, giving S5=`P`.

## S1 — Operations

- State: A
- Function: perform substantive Workspace work through model-driven Agent runs that interpret an instruction/request, select tools, observe results and continue until the bounded run outcome is produced.
- Disturbance / variety regulated: heterogeneous user and Trigger instructions, shared Workspace resource state, tool/MCP/browser/sandbox observations, external information, provider/model variation and task-specific failures.
- Decisive decision or feedback right: choose semantic next actions and tool calls from the current objective/context, interpret returned observations and revise later actions within the run.
- Decision owner: the model-driven Agent resolved and driven through Platypus's first-party run/turn machinery.
- Supporting / enforcement mechanisms: `AgentRunner`, `prepareChatTurn`, run registry/lifecycle, model generation limits, first-party tool assembly, scoped Workspace principals, sandbox/MCP/tool execution and Trigger sinks/timeouts.
- Closure path: user or Trigger instruction → first-party turn resolves Agent/model/tools/context → model selects action/tool → observation returns into the model loop → later action changes from the observation → Chat/Trigger outcome is persisted or emitted.
- Boundary reachability: ordinary interactive Chats and first-party Trigger firing both invoke the shipped Agent run path. Trigger execution explicitly calls `agentRunner.generate` under a Workspace-scoped Trigger principal.
- Why this is / is not agent-owned: removing the model actor while retaining schedules, API routes, tool schemas, persistence and run lifecycle leaves execution infrastructure but removes the semantic task decisions that produce the substantive operational result.
- Evidence: [`README.md`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/README.md); [`apps/backend/src/runs/agent-runner.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/runs/agent-runner.ts); [`apps/backend/src/services/trigger-firing.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/services/trigger-firing.ts); [`apps/docs/content/concepts/agents.mdx`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/docs/content/concepts/agents.mdx).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model/provider internals remain dependencies; `A` credits the model actor reached through Platypus's first-party harness, not autonomous ownership by deterministic run support code.

## S2 — Coordination

- State: C
- Function: attenuate recursive interference between event-driven operational Agent runs acting on the same Workspace entity by bounding repeated Trigger firings in a rolling window.
- Disturbance / variety regulated: two event Triggers can hand one record back and forth, each Agent write producing the next event after the previous run finishes; this can create an unbounded multi-run oscillation that repeatedly consumes full Agent drives even though the single-Agent self-actor guard is never crossed.
- Decisive decision or feedback right: suppress the next firing for a specific `Trigger × entity` once the deployment-level rolling run ceiling is reached, preventing another Agent run from starting.
- Decision owner: deterministic first-party Trigger breaker/runtime policy.
- Supporting / enforcement mechanisms: event causation tracking, self-actor guard, event debounce, `trigger_run` history, rolling `maxRuns/windowSeconds`, suppression records and retention that preserves the counted evidence window.
- Closure path: distinct Trigger-backed Agent operations mutate a shared entity → later matching Workspace event attempts another Trigger firing → breaker reads recent per-Trigger/per-entity run history → excess firing is recorded as `suppressed` before Agent invocation → the oscillating operational chain is attenuated.
- Boundary reachability: `fireTrigger` checks `shouldSuppressTriggerRun` on ordinary event firings and calls `suppressTriggerRun` instead of `runTrigger`; the breaker is a standing runtime property configured at deployment boot, not a test-only mechanism.
- Why this is / is not agent-owned: Agents cause the operational writes/events, but the coordination decision that bounds the inter-operation feedback loop is deterministic first-party runtime logic and operator-configured ceiling. No model actor owns the breaker judgment, so the state is `C`, not `A`.
- Distinct S1 units: separate Trigger-fired model-driven Agent runs in the same Workspace, potentially using different Triggers/Agents, each capable of substantive mutations on shared Workspace entities.
- Inter-S1 disturbance: repeated event causation can produce a feedback oscillation in which two Trigger/Agent paths hand the same entity back and forth and repeatedly invoke full model/tool runs.
- Attenuating coordination relation: a rolling per-`Trigger × entity` run-rate breaker suppresses excess event firings before a further S1 Agent run begins; a short debounce and self-actor guard provide additional but incomplete attenuation.
- Feedback into subsequent S1 behaviour: once the ceiling is reached, the next matching operational unit is not invoked at all; later Agent behaviour is therefore changed by the accumulated interaction history rather than merely logged.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the implementation and comments name the cross-Trigger feedback-cycle failure mode, explain why self-actor and debounce are insufficient, and apply a mechanism specifically to attenuate that inter-operation oscillation. The finding does not rely on Sub-Agent routing, queues or shared Boards alone.
- Evidence: [`apps/backend/src/services/trigger-breaker.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/services/trigger-breaker.ts); [`apps/backend/src/services/trigger-firing.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/services/trigger-firing.ts); [`apps/backend/src/services/event-dispatch.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/services/event-dispatch.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: S2 is scoped to the event-driven Trigger organization. Sub-Agent delegation by itself is not treated as S2, and no autonomous coordination owner is inferred from model-driven S1 actors.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party Workspace-wide current-control function is established at the assessed recursion.
- Disturbance / variety regulated: individual Agent runs have step/time limits, Trigger runs have lifecycle/breaker controls, and a coordinator Agent can delegate a bounded task to specialists; these mechanisms regulate local execution but do not constitute a standing current-control function for the Workspace as a whole.
- Decisive decision or feedback right: no first-party actor/path was found that receives a whole-Workspace current view of operational Agents/commitments/resources and closes decisions over their current priorities, allocation, constraints or synergy on behalf of the whole.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: Agent/Trigger CRUD, Agent discovery, run registries and run lists, Trigger scheduler/breaker, Boards/Dashboards, Sub-Agent delegation, generation/time limits and owner/admin controls.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: a top-level Agent may coordinate its own configured Sub-Agents inside one task and an Agent may be granted generic management tools, but neither is a first-party Workspace regulator at this recursion. Tool availability plus user-authored instructions would require composition of the missing function rather than demonstrate it in the shipped organizational path.
- Evidence: [`apps/docs/content/building-with-platypus/agents.mdx`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/docs/content/building-with-platypus/agents.mdx); [`apps/backend/src/tools/agent-management.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/tools/agent-management.ts); [`apps/backend/src/runs/agent-runner.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/runs/agent-runner.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: at the narrower recursion of one configured coordinator-plus-specialists task, the parent Agent may exercise local orchestration. This assessment does not lift that nested task role into Workspace-level S3.

### Absence scope

- Surfaces inspected: Agent and Sub-Agent runtime; Agent discovery/management tools; Trigger scheduler/firing/breaker/run history; Boards and Dashboards as shared Workspace state; run registry/lifecycle; Workspace administration and system-prompt assembly.
- Plausible first-party paths checked: top-level coordinator Agent as S3; generic `create/update/deleteAgent` tooling; Trigger scheduling/run monitoring; Workspace home/run listings; Boards/Dashboards as control state; owner/admin management.
- Why no material first-party path remains: the coordinator sees and regulates one composed task, management tools expose optional CRUD rather than a standing whole-system regulator, and deterministic scheduler/lifecycle mechanisms govern individual runs/triggers. No inspected path combines whole-Workspace current state with a function-specific current-control authority and feedback loop.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary-audit function is established at Workspace recursion.
- Disturbance / variety regulated: no positive S3* claim is made. Platypus can host an Agent whose user-authored role is reviewing/fact-checking, but ordinary configurable specialist delegation is not itself an independent audit architecture.
- Decisive decision or feedback right: no shipped path was found in which an ordinary S1 outcome is automatically or structurally challenged through a distinct complementary evidence channel and the audit finding returns into correction/current control.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: Sub-Agent delegation, run status/events, tool-result records, Trigger run pages and generic reviewer/fact-checker Agent configurations are available but insufficient for positive S3* closure.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: a user can configure a specialist called a reviewer and ask a parent Agent to call it, but that is task composition chosen by the user/model, not a first-party complementary audit path with established independence, evidence access and corrective closure.
- Evidence: [`apps/docs/content/concepts/agents.mdx`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/docs/content/concepts/agents.mdx); [`apps/docs/content/building-with-platypus/agents.mdx`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/docs/content/building-with-platypus/agents.mdx); [`apps/backend/src/runs/run-events.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/runs/run-events.ts).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a specific user-created multi-agent configuration could implement audit semantics using Platypus primitives. Repository-relative assessment does not credit arbitrary downstream compositions as a shipped first-party S3* function.

### Absence scope

- Surfaces inspected: parent/Sub-Agent execution and return path; run events/status/history; Trigger runs; Boards/Dashboards; Agent configuration/docs; generic reviewer/fact-checker composition described as a possible specialist pattern.
- Plausible first-party paths checked: specialist reviewer Sub-Agent; run-event logging as audit; Trigger run inspection; operator run pages; security guardrails; model/provider checks.
- Why no material first-party path remains: ordinary run telemetry is the same operational/reporting path rather than complementary access, and configurable Sub-Agents are not deterministically independent auditors. No first-party path establishes a claim-under-audit, separate evidence route, audit decision owner and return-to-operation closure.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established at the assessed Workspace recursion.
- Disturbance / variety regulated: Platypus can search the web, call MCP/data sources, react to Workspace events and retain Memory from prior Chats, but those capabilities support current task execution or internally retrospective recall rather than a distinct future/environment adaptation function.
- Decisive decision or feedback right: no first-party path was found that models material external/future distinctions, develops adaptation options for the Workspace organization from them and returns those options into present S3/capability policy as a closed organizational conversation.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: web/MCP tools, scheduled/event Triggers, Memory extraction/retrieval, user/Workspace Context, Skills and Agent management.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: model Agents can research outside information as part of S1 and may use generic management tools afterward if configured, but the repository does not wire those primitives into a distinct prospective adaptation role/loop at Workspace level.
- Evidence: [`apps/docs/content/concepts/memory-and-context.mdx`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/docs/content/concepts/memory-and-context.mdx); [`README.md`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/README.md); [`apps/docs/content/building-with-platypus/triggers.mdx`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/docs/content/building-with-platypus/triggers.mdx).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: generic composability may permit a downstream user to build an S4-like research/adaptation workflow; that is not credited without a first-party closed function in the reviewed repository.

### Absence scope

- Surfaces inspected: Memory extraction/retrieval; web and MCP capability descriptions; scheduled/event Trigger architecture; Agent/Skill management; Workspace/Organization Context; Boards/Dashboards; Sub-Agent composition.
- Plausible first-party paths checked: Memory as adaptation; web-search Agent as environmental scan; scheduled research Trigger; event-driven response; Agent self/peer modification through management tools; Skills as adaptive capability.
- Why no material first-party path remains: Memory is extracted from prior Chat text, Triggers respond to configured time/events, and external research remains ordinary task execution. The primitives are not connected into a distinct external/prospective intelligence role with option formation and return-to-current-control closure.

## S5 — Policy and identity

- State: P
- Function: maintain durable Workspace-level mission/identity framing that is injected into later Agent operation across the Workspace.
- Disturbance / variety regulated: drift or disagreement about the Workspace's standing domain, purpose, terminology and shared framing that all Agent runs should operate within.
- Decisive decision or feedback right: set or revise the Workspace `context` field that Platypus injects into the Workspace fragment of the system prompt for subsequent operation.
- Decision owner: legitimate parent authority — the Workspace Owner or Organization Admin through the supported Workspace update surface.
- Supporting / enforcement mechanisms: Workspace ownership/authorization, `workspaceUpdateSchema`, persisted Workspace row, first-party prompt-context resolution and `workspaceFragment` composition.
- Closure path: Workspace identity/policy issue → owner/admin edits the persisted Workspace Context → subsequent turn/run resolution reads current Workspace state → system-prompt composition emits the Workspace id/context fragment → later model-driven S1 operation is framed by the changed Workspace policy/identity.
- Boundary reachability: the normal Workspace update route is available to authorized Workspace administration, and the canonical system-prompt contract states that the Workspace fragment is always part of the composed prompt and includes Workspace Context when present.
- Why this is / is not agent-owned: no inspected first-party tool gives ordinary Workspace Agents legitimate authority to rewrite the Workspace's authoritative `context` field. Agent Instructions and agent-management tools govern constituent Agents, not the Workspace-wide identity surface. The decisive S5 right therefore remains parent-owned.
- Identity / ultimate-policy issue: what this Workspace is for and the standing shared framing/terminology under which every Agent operation in the Workspace should interpret its work.
- Ultimate authority in each claimed mode: Parent (`P`) — Workspace Owner or Organization Admin authorized to update the Workspace record.
- Return-to-operation path: parent update → persisted Workspace Context → first-party turn resolution → `workspaceFragment` in composed system prompt → subsequent Agent/Trigger runs operate with the changed shared framing.
- Evidence: [`apps/docs/content/concepts/memory-and-context.mdx`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/docs/content/concepts/memory-and-context.mdx); [`apps/docs/content/concepts/system-prompt.mdx`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/docs/content/concepts/system-prompt.mdx); [`apps/backend/src/system-prompt.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/system-prompt.ts); [`apps/backend/src/routes/workspace.ts`](https://github.com/willdady/platypus/blob/5dda4dcdb92c209c8c8df953f0e9261cd018c2d7/apps/backend/src/routes/workspace.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: per-Agent Instructions are not used as the Workspace-level S5 witness because they govern constituent S1 configurations rather than the whole Workspace. Organization identity is an additional parent framing layer but is not needed to establish this `P` finding.

## Distributed OSS parent arrangement

The public repository's maintainer/contributor governance sits outside the deployed Workspace boundary and is not used to donate S5. The parent mode above is a runtime relationship inside the product: an authorized Workspace Owner/Organization Admin changes the Workspace's durable context and the first-party prompt pipeline returns it into subsequent operation.

## Self-hosted and non-human modes

Platypus supports unattended Trigger runs and self-hosted operation. A Trigger acts on behalf of the Workspace owner, but that delegation does not make the Trigger or Agent an S5 owner. Deployment-level environment settings such as the Trigger breaker ceiling are deterministic regulatory configuration, not S5 identity authority.

## Recursion

A Workspace may contain many Agents, each optionally composed with a flat set of Sub-Agents. This assessment credits those model-driven runs as Workspace S1 units. A coordinator Agent and its specialists can form a narrower nested task organization, but its local delegation does not automatically become Workspace-level S3. Conversely, the Trigger feedback-cycle S2 finding is made at Workspace recursion because it regulates interaction among separate event-driven operational Agent runs sharing Workspace entities.

## Variety and escalation

Platypus attenuates operational variety through Workspace tenancy boundaries, scoped resources, model/tool step limits, run timeouts, Trigger debounce/self-actor guards/run-rate breaker, bounded Sub-Agent depth and provider/tool validation. It amplifies operational response through specialized Agents, Sub-Agents, Skills, MCP, sandbox/web tools, Boards and Triggers. Owner/admin configuration and run cancellation are escalation/control mechanisms but are not promoted to VSM functions without the required function-specific closure.

## Evidence gaps

- S2 is intentionally narrow: it credits the explicitly documented two-Trigger/shared-entity feedback oscillation and first-party breaker, not multi-agent naming or delegation generally.
- Platypus can be configured with a top-level coordinator Agent, reviewer specialist or management-capable Agent. Those are powerful composition primitives but do not by themselves establish Workspace-level S3/S3* in repository-relative assessment.
- Memory, external tools and schedules are not promoted to S4 without a distinct external-and-prospective adaptation role and return conversation.
- S5 uses the Workspace-wide Context lifecycle, not per-Agent editable prompts. The parent-owned context is structurally returned into the canonical system prompt for subsequent operation.
