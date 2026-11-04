---
harness_id: lightspeed
project_name: Lightspeed
repository: https://github.com/smartcomputer-ai/lightspeed
review_ref: 2873e77dca4325aac116b81db2b520502c037ac4
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: P
---

# Lightspeed

## Review boundary

- System in focus: One managed persistent Lightspeed bot, with its routed agent sessions, event inbox, user/operator, optional self-configuration and child agents. The aggregate multi-tenant Lightspeed deployment is supporting infrastructure, not this bot's governing identity.
- Purpose and identity: Conduct one standing delegated job in response to external events and messages across durable sessions, with operator-defined brief and profiles.
- Relevant environment: Scheduled work, webhook/HTTP/poll changes, chat, federation events, changing user needs, provider/tool failures, competing incoming event deliveries, permission and resource limits.
- Standard-distribution boundary: First-party Rust event-sourced harness, Temporal session and bot controllers, profile/tool construction, model-facing bot status/event/trigger/brief tools, UI/API bot administration, optional subagents and bot federation. Postgres/Temporal and external providers are dependencies.
- Credited operating / distribution surfaces: [README](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/README.md), [bot guide](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/bots-and-triggers.md), [bot tool definitions](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/bots/src/tools.rs), [bot tool execution](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/temporal-runtime/src/bots/tools.rs), [bot controller](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/temporal-workflow/src/workflows/bots/controller.rs), [status views](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/bots/src/views.rs).
- Adjacent first-party surfaces excluded from ownership: Infrastructure orchestration, platform administration of unrelated bots/universes, example software factories, documentation-only use cases, evaluations, tests and OSS maintainer organization. Other independent bots and external model/MCP implementations do not donate functional rights.
- First-party operating / deployment modes considered: Single bot Main and keyed/event sessions, configured trigger admission/routing, default run limits, enabled selfConfig and emit grants, human Operator/Admin changes, subagent delegation, federation and operator-controlled pause/reset.
- Recursion level: One standing bot with several operational session/worker cells, one bot controller and a legitimate human Operator parent; not the entire shared multi-tenant deployment.
- Reviewed revision: 2873e77dca4325aac116b81db2b520502c037ac4 (GitHub repository ID 1153407906).
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The durable session core reduces committed events into state and asks a model to choose tools; adapters perform effects and record results. A named bot adds a standing brief, one Main session, optional routed per-key/per-event sessions, triggers and its own controller workflow. Controller queues or coalesces admitted events, owns session lifecycle and applies operator/model configuration. Model-facing bot tools can inspect current event/session status, resolve events, edit triggers and change the standing brief when the operator has granted selfConfig. Federation posts events to other bots and optionally returns outcome receipts. Subagents are bounded child sessions with distinct profiles. A human Operator/Admin can inspect Activity, configure job and trigger policy, alter run limits, pause/replay/reset and govern the bot. [Agent loop](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/how-it-works/agent-loop-and-durability.md), [controller](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/temporal-workflow/src/workflows/bots/controller.rs), [bot document](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/api/src/bots.rs).

## Operational model

The bot's S1 is the model-directed event response, not the deterministic Temporal workflow itself. The same bot may run different autonomous routed sessions, but static routing and queueing do not automatically establish S2. The Main bot model can inspect the whole bot and revise trigger admission when self-configuration is allowed, giving a bounded autonomous current-control path and prospective adaptation of how the bot senses and acts. Human Operator/Admin separately owns broader whole-bot limits, lifecycle and standing job identity. These modes are not a claim that a random unconfigured deployment autonomously exercises every right.

## S1 — Operations

- State: A
- Function: Interpret incoming work and execute model-directed actions in a durable bot session.
- Disturbance / variety regulated: Unpredictable external events, files and tool results, model/provider failures, tasks with open-ended next steps.
- Decisive decision or feedback right: Select tools, read event details, invoke subagents or external actions and choose the event disposition.
- Decision owner: First-party model-facing agent loop within each configured Lightspeed bot session.
- Supporting / enforcement mechanisms: Event-sourced reducer, Temporal recovery, CAS references, tool registry, one-active-run admission, profile grants, tools and fixed budget controls.
- Closure path: Event starts session run, model reads evidence and calls tools, effects are committed and returned for next model step; bot_event_resolve records the agent's decision.
- Boundary reachability: The documented local stack starts session and bot workers; a created bot gets Main and configured routed sessions with model, standing brief and event tools.
- Why this is / is not agent-owned: The LLM chooses meaningful event actions and outcome, whereas the workflow merely preserves and executes their effects.
- Evidence: [core agent drive and durable loop](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/how-it-works/agent-loop-and-durability.md), [bot instructions/outcome tool](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/bots/src/tools.rs), [bot event guide](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/bots-and-triggers.md).
- Basis: structural.
- Confidence: high.
- Caveats: No external provider or deployed fleet was run in this source review.

## S2 — Coordination

- State: —
- Function: No function-specific agent-owned or constructor-complete inter-S1 conflict regulator is established for this bot's multiple sessions.
- Disturbance / variety regulated: Busy-session delivery, repeated events and load bursts are attenuated mechanically; no separately evidenced interference among distinct viable operational sessions is resolved.
- Decisive decision or feedback right: A configured trigger picks queue/steer/append/coalesce, but this ordinarily changes admission to a target session rather than resolving a conflict among distinct S1 cells.
- Decision owner: Operator/model can set trigger policies; deterministic bot controller dispatches and deduplicates, without a verified distinct inter-S1 conflict decision.
- Supporting / enforcement mechanisms: Event ids, CEL route keys, busy delivery modes, coalescing, rate/breaker limits, federation receipts and subagent limits.
- Closure path: Buffered events are eventually delivered; a sender may get a receipt, but no source witness ties this ordinary traffic to a corrective decision between separately operating S1 cells.
- Why this is / is not agent-owned: A message bus, per-session queue, default scheduler and delegation are not alone S2, even though their safety/throughput roles are useful.
- Evidence: [controller lanes and state](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/temporal-workflow/src/workflows/bots/controller/state.rs), [event route policies](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/bots-and-triggers.md), [federation](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/subagents-and-federation.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A configured concrete multi-bot workplace may add inter-S1 interference regulation; generic interoperability is not counted.

### Absence scope

- Surfaces inspected: Bot controller queues/lanes, delivery policies, federation requests/receipts, subagent profile limits, trigger routing.
- Plausible first-party paths checked: Same-session event contention, multiple independently configured bots, cross-bot messages, subagent concurrency and durable promises.
- Why no material first-party path remains: The inspected generic paths regulate deliveries and single-run safety, without an identified corrective inter-S1 conflict and resultant feedback changing separate S1 decisions at this recursion.

## S3 — Inside-and-now control

- State: A(P)
- Function: Oversee the current standing bot's event/session portfolio, admission constraints, work intake and bot-level interventions.
- Disturbance / variety regulated: Repeated failed events, flooded inbox, multiple active delivery threads, budget exhaustion and mismatched routing or work cadence.
- Decisive decision or feedback right: In selfConfig mode the Main model can inspect all current sessions, recent/active deliveries, buffers and run usage, then revise trigger routes, filters, cadence and busy-session policies. Human Operator can additionally alter whole-bot run budgets, pause/replay/reset and related current commitments.
- Decision owner: Model in the enabled selfConfig Main mode (A); legitimate human Operator/Admin controlling the bot's full settings and Activity (P).
- Supporting / enforcement mechanisms: bot_status, bot_event_list/read, bot_trigger_put/delete, controller config signals, run budgets, breaker, session status and role-checked Platform actions.
- Closure path: Current bot status exposes overloaded/failed work; model/operator revises trigger/control settings; API validates them; subsequent event admission and routed-session operation change.
- Boundary reachability: Bot tools are declared in the shipped selfConfig mode and re-checked against the live grant; bot controller picks up configuration. Operator/Admin bot settings and Activity exist in shipped web/UI and core API.
- Why this is / is not agent-owned: The model selects intake/priority constraints from whole-bot feedback in the autonomous mode; scheduler executes them. Separately, the authorized operator selects broader intervention and resource limits, so the parent mode is real rather than inferred from a pause button alone.
- Whole-system current view: bot_status includes sessions, their busy states, active/recent deliveries, buffers, processed events, daily runs and breaker; Operator Activity supplies the same run/outcome context across the bot.
- Current-control decision scope: Change which incoming events are filtered, routed, batched or queued and when future deliveries start; in parent mode also daily resource limit, pause, event replay and session reset.
- Evidence: [bot_status view](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/bots/src/views.rs), [self-configuration tool declarations](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/bots/src/tools.rs), [tool execution and grant checks](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/temporal-runtime/src/bots/tools.rs), [operations and bot management](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/bots-and-triggers.md), [Operator role](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/access-and-security/people-and-roles.md).
- Basis: structural.
- Confidence: medium for autonomous S3; high for parent bot management closure.
- Caveats: The autonomous mode requires selfConfig granted by an Operator; the model cannot directly widen limits or reconfigure a different bot. Adjusting one ordinary session tool call is not S3.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Self-configured Main bot model | Bot-wide active/recent deliveries, busy session/routing observations | Chosen trigger filter/route/cadence update changes later bot admissions | [status and tools](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/temporal-runtime/src/bots/tools.rs) |
| Parent (`P`) | Authorized human Operator/Admin | Whole-bot Activity, run budget, failed/queued event and lifecycle state | Update resource limits, pause, route/trigger configuration or reset; controller applies to subsequent work | [bot administration](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/bots-and-triggers.md) |

## S3* — Complementary audit

- State: —
- Function: No separate independent complementary S3 audit is wired to challenge ordinary bot operations.
- Disturbance / variety regulated: Incorrect event handling, misleading tool results or missing outcomes can be observed, but no separate challenge authority is established.
- Decisive decision or feedback right: Activity, session transcripts and event outcomes are accessible; ordinary user/agent review does not create an independent audit verdict.
- Decision owner: Bot model for normal event resolution, operator for routine investigation; optional reviewer subagents remain delegated operational checks.
- Supporting / enforcement mechanisms: Event-sourced history, workflow logs, subagent transcripts, receipt records and event replay.
- Closure path: Logs/status assist current troubleshooting; no independent sampled reality channel with a corrective audit judgment is guaranteed to reach S3.
- Why this is / is not agent-owned: Replay, normal QA and status dashboards are evidence-supporting infrastructure, not an independently governed S3* path.
- Evidence: [subagent reviews and limits](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/subagents-and-federation.md), [Activity/events](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/bots-and-triggers.md), [durable log](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/how-it-works/agent-loop-and-durability.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A user may attach a truly separate auditor bot, but it is not part of the base bot boundary.

### Absence scope

- Surfaces inspected: Event logs, Activity, subagent review example, outcome receipts, workflow replay and status tools.
- Plausible first-party paths checked: Read-only review subagent, separate bot federation reviewer, logs, replay and operator manual investigation.
- Why no material first-party path remains: These are optional delegated tasks or ordinary reporting; they do not close an independently owned complementary audit judgment through bot-level control.

## S4 — Outside-and-then intelligence

- State: A
- Function: Revise future environmental sensing and standing bot action opportunities in response to external observations.
- Disturbance / variety regulated: Newly relevant external signals, stale polling/routing assumptions, changing schedules and information sources.
- Decisive decision or feedback right: A persistent bot model can read incoming external events and current trigger configuration, then select and install a new or revised schedule, poll, webhook, filter or route to govern future work.
- Decision owner: Model in the first-party selfConfig bot mode; operator initially controls that grant and can override the setup.
- Supporting / enforcement mechanisms: bot_event_read, bot_trigger_list, bot_trigger_put/delete, polling cursors, schedule reconciliation, server-validated filters and controller.
- Closure path: External event/evidence changes the model's judgment of what should be watched next; a prospective trigger option becomes persisted configuration and later yields changed work admission and present S3 control context.
- Boundary reachability: SelfConfig bot tools are real admitted workflow bindings; put_trigger calls the core service and schedules are reconciled into the running controller.
- Why this is / is not agent-owned: Deterministic polling does not choose which future signals matter; the self-configured bot model can decide the changed future monitoring and enact it.
- External distinction: New webhook, monitored HTTP/command output or peer event represents a changing outside system, not internal task-memory alone.
- Future / prospective distinction: A rewritten future polling schedule, source/filter or alert routing applies to later events rather than completing only the present response.
- Adaptation option generated: Model-authored new/modified watch trigger, cadence, filter and routing policy.
- Path back into current capability / S3: bot_trigger_put persists and reconciles the trigger so subsequent event arrivals alter the S3 work portfolio and S1 sessions.
- Evidence: [bot trigger tools and descriptions](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/bots/src/tools.rs), [put_trigger implementation](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/temporal-runtime/src/bots/tools.rs), [polling/schedules and external feeds](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/bots-and-triggers.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: Requires an enabled selfConfig grant and a model choosing prospective changes; static operator-configured polling by itself would not be autonomous S4.

## S5 — Policy and identity

- State: P
- Function: Retain legitimate human authority over the standing bot's job/identity, capability grants and final purpose changes.
- Disturbance / variety regulated: The bot's standing brief or authorized role may no longer match human institutional purpose or risk boundaries.
- Decisive decision or feedback right: A human Operator/Admin can redefine the bot's standing job and authorized profile and self-configuration permissions after examining outcomes, including disallowing further self-revision.
- Decision owner: Legitimate human Operator/Admin within the bot's universe; bot model cannot widen its own capabilities or override operator policy.
- Supporting / enforcement mechanisms: Bot Job/Settings, role-gated bot document update, immutable bot ID, profile grants, live selfConfig and emit permission rechecks, controller idle-boundary reapplication.
- Closure path: Operator recognizes a standing-purpose or authority conflict from the bot's Activity/conversation; revises Job brief/profile/grant; controller re-applies standing instructions and permissions; future operations follow the new identity decision.
- Boundary reachability: Operator/Admin bot edits are admitted through role-checked Platform/core API and bot configuration reconciliation; subsequent Main sessions use the modified standing brief/profile/permissions.
- Why this is / is not agent-owned: This credit is to the legitimate parent human's identity-level decision and its enforceable return, not to the existence of prompt text or an approval of one tool.
- Identity / ultimate-policy issue: Whether this persistent bot should keep its ongoing job, change its standing instructions or retain self-configuration/federation authority in its universe.
- Ultimate authority in each claimed mode: Operator/Admin for the scoped bot and universe; no autonomous S5 right is claimed merely from bot_brief_put.
- Return-to-operation path: Bot document/config update and session reconcile at idle change the instructions/grants for subsequent routed work.
- Evidence: [bot job and settings lifecycle](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/using-lightspeed/bots-and-triggers.md), [human permission hierarchy](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/docs/documentation/access-and-security/people-and-roles.md), [bot document](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/api/src/bots.rs), [controller config reconcile](https://github.com/smartcomputer-ai/lightspeed/blob/2873e77dca4325aac116b81db2b520502c037ac4/crates/temporal-workflow/src/workflows/bots/controller.rs).
- Basis: structural.
- Confidence: medium.
- Caveats: Routine message approval or role check is not S5; this parent mapping applies to a bot-wide standing mission/authority revision, not ordinary event handling or the entire platform.

## Distributed OSS parent arrangement

Self-hosted Lightspeed can run many independent bots and users, but no one project-wide OSS contributor organization governs those installed bots. The credited parent is the actual per-universe Operator/Admin who controls a particular bot, not repository maintainers or a generic SaaS vendor.

## Self-hosted and non-human modes

At least one local bot can operate with model-driven trigger edits under selfConfig; the standard web Platform lets a legitimate human manage the same bot in a broader parent mode. Human approval of individual MCP calls is distinct from parent S3/S5 resource and standing-identity decisions. Distributed Temporal workers and attached VMs are implementation machinery, not independent policy owners.

## Recursion

Per-key/per-event sessions and their children are operational work cells at the bot recursion. The bot's Main session may inspect aggregate work and adjust admission. A separate bot is its own standing organization; federation does not automatically create a higher-recursion S2/S3 institution among them.

## Variety and escalation

Inputs are authenticated/admitted, filtered, routed or queued; the model resolves event work and can alter subsequent trigger selection under a constrained grant. Run limits and breakers bound overload; the human Operator can intervene with profile, job, budget or lifecycle decisions. A federated receipt conveys an outcome rather than proving independent audit or mutual conflict resolution.

## Evidence gaps

Assessment is from frozen first-party Rust code and shipped documentation. No live Temporal/Postgres/LLM fleet was run, no adversarial inter-bot contention was reproduced, and no real mission-conflict history was observed. Autonomous S3/S4 are supported opt-in rights, and S5 is the supported legitimate parent management route rather than an observation of a particular organization's practice.
