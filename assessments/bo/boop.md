---
harness_id: boop
project_name: Boop
repository: https://github.com/raroque/boop-agent
review_ref: 31979130b1371acd9defbea115279a06c63c1fb4
reviewed_at: 2026-10-25
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

# Boop

## Review boundary

- System in focus: The self-hosted, first-party Boop personal-assistant runtime that handles an iMessage or local-chat user turn, delegates tool-bearing work to execution agents, stores memory and automations, and returns results. This is **not** the upstream Claude Agent SDK, Codex app-server, hosted Composio, Sendblue, or the organization developing Boop.
- Purpose and identity: Convert the user's changing personal requests into answers, drafts, authorized external actions and recurring agent work, with conversation continuity.
- Relevant environment: User requests and confirmations, incoming iMessages and selected Gmail events, integration/tool responses, provider errors, stored memories, time and external application state.
- Standard-distribution boundary: Published `server/`, `convex/`, bundled debug UI and documented local server/Electron setup, with the operator's supported Claude or Codex runtime, Convex and optional integrations configured. The model SDK/provider supplies inference; Boop's installed application supplies the dispatcher, agent tools, worker lifecycle, memory, scheduling and return path. No independent model weights or upstream SDK governance are credited to Boop.
- Credited operating / distribution surfaces: [inbound and turn handler](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/interaction-agent.ts#L319-L585), [spawned work-cell runtime](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/execution-agent.ts#L125-L278), [Claude adapter](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/runtimes/claude.ts), [Codex adapter](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/runtimes/codex-app-server.ts), [draft execution](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/draft-tools.ts), [automations](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/automations.ts), and [memory consolidation](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/consolidation.ts).
- Adjacent first-party surfaces excluded from ownership: Electron packaging, setup scripts, developer instructions, repository contribution/CI/tests, demo replies and showcase assets, integration vendors' hosted agent or authentication machinery, and any operator's separate Claude/Codex workflows not invoked by the shipped Boop request path. The debug dashboard is reviewed as an operator support surface, not automatically a metasystem owner.
- First-party operating / deployment modes considered: Standard local server with Claude Agent SDK or Codex app-server provider, iMessage/web chat ingress, dispatcher with limited tools, spawned execution agents with explicit integration scope, confirmed-draft path, scheduled automation and background memory consolidation; optional browser/Apple integrations only when enabled.
- Recursion level: One deployed personal-agent service and its active operational work cells. A spawned subagent, tool request, memory record or cron item is not automatically another viable organizational recursion.
- Reviewed revision: `31979130b1371acd9defbea115279a06c63c1fb4`, frozen in [discovery #2036](https://github.com/opensiro/vsm-harness-index/issues/2036) and [serial control #2037](https://github.com/opensiro/vsm-harness-index/issues/2037).
- Observation date: 2026-10-25.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

An inbound turn is persisted to Convex, merged with bounded conversation history and fed to a model-backed **interaction dispatcher**. Its prompt can choose to answer or invoke a first-party `spawn_agent` tool, but the dispatcher is explicitly denied direct web/filesystem/third-party action tools. `spawnExecutionAgent` creates and persists a separate work record, constructs tools/MCP integrations, invokes the selected Claude or Codex runtime and feeds text/tool events and final status back to the dispatcher. Thus provider cognition is external, but the user-goal → model-choice → first-party spawn → tool/result → returned-answer loop is deliberately shipped, not only a configuration sample. [turn and tool construction](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/interaction-agent.ts#L319-L570); [execution loop and state](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/execution-agent.ts#L125-L278).

The application also stages external sends as pending drafts for the user's confirmation, supports scheduled tasks that call the same work-cell runtime, and runs cleanup, stale-agent detection and a three-stage model-assisted memory consolidation cycle. Convex persists agents, messages, memory and draft states; Sendblue/Composio and provider SDKs are adjacent external services. A dashboard provides observation of agent status and resource usage. [draft staging/approval](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/draft-tools.ts#L18-L119); [scheduler](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/automations.ts#L45-L140); [server startup](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/index.ts#L30-L65).

## Operational model

The ordinary S1 actor is a configured model-backed dispatcher and its delegated model-backed execution work cell(s). Each consumes the current user/task context and chooses task content or offered tools; first-party code enforces tool limits, runs integrations, records state and returns results. Recurring automations instantiate an execution work cell from a user-approved schedule; proactive email classification supplies an optional event-triggered notice. The user remains the source of external-action approval and provider/integration configuration. Deterministic background memory maintenance, lifecycle status, and an operator debug surface support this S1 operation without automatically establishing separate S2–S5 ownership.

## S1 — Operations

- State: A
- Function: Interpret a user's message or a previously specified automation task and produce a context-sensitive answer, research/tool-mediated result, or staged external action.
- Disturbance / variety regulated: Diverse message intents, incomplete task context, integration returns and failures, action confirmation and changing tool observations.
- Decisive decision or feedback right: The runtime-invoked autonomous dispatcher decides answer versus delegated work and writes the task it delegates; each execution agent chooses how to respond and which exposed tools to invoke after seeing returns.
- Decision owner: Configured model-backed dispatcher/execution agents in the first-party Boop turn path. The external inference service executes cognition, but Boop actually assembles and invokes these actors; deterministic spawn, tool filtering and storage are support/enforcement.
- Supporting / enforcement mechanisms: Bounded history, model/runtime adapter, permissions/allowed-tool lists, Convex messages/logs, scoped integrations, timeouts/abort, draft persistence, cron and usage accounting.
- Closure path: Incoming user message → `handleUserMessage` → model chooses response or `spawn_agent` → `spawnExecutionAgent` returns tool/result/status → dispatcher returns user-facing reply; independently, a due configured automation starts the same execution agent and stores/notifies outcome.
- Boundary reachability: Both `handleUserMessage` and `spawnExecutionAgent` are imported by shipped server routes/scheduler. The dispatcher has an actual model-runtime call and first-party `spawn_agent` callback, not merely a README proposal.
- Why this is / is not agent-owned: Removing the model-backed actor leaves webhook delivery, a database, static schedules and tools but no discretionary interpretation of arbitrary user goals or next tool selection. The developer and user set the operating envelope; the model-backed actor owns ordinary in-envelope task choices.
- Evidence: [model-selected dispatcher tools and result](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/interaction-agent.ts#L451-L585); [tool-bearing worker and return](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/execution-agent.ts#L157-L278); [runtime provider selection](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/runtimes/index.ts#L1-L23).
- Basis: Structural first-party assembly of a model-to-tool-to-result loop; explicit packaged operating mode.
- Confidence: High for code-path existence; no claim of empirical agent effectiveness or verified vendor integration.
- Caveats: This is an application orchestration of installed Claude/Codex runtime agents, not first-party inference weights or ownership of the external SDK's independent internal architecture. The shipped Boop dispatcher/worker integration is the credited loop.

## S2 — Coordination

- State: —
- Function: No separately established first-party regulation of interference/oscillation among distinct operational work cells at the Boop service recursion.
- Disturbance / variety regulated: Concurrent delegated tasks might conflict over external accounts, memory or repeated notifications; such possibility alone is not an observed S2 witness.
- Decisive decision or feedback right: No source-shipped conflict judgment/negotiation or returned inter-S1 adjustment distinguished from parent-to-child delegation, tool scope and message deduplication.
- Decision owner: Not established. A single dispatcher assigns tasks; user approval applies to external drafts, not general inter-worker coordination.
- Supporting / enforcement mechanisms: Per-agent Convex logs/status, tool-scope filtering, Sendblue/webhook dedup, scheduled runs, draft status, shared memory and worker abort.
- Closure path: Generic execution results return to the dispatcher; the reviewed code does not feed a specific inter-S1 conflict resolution into the next actions of two independently operating work cells.
- Why this is / is not agent-owned: Model task delegation and static duplication gates do not become S2 because two work cells can exist or a message can be sent twice.
- Evidence: [dispatcher spawn](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/interaction-agent.ts#L470-L520); [independent scheduled agent runs](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/automations.ts#L45-L135); [proactive email delivery dedup](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/proactive-email.ts#L27-L60).
- Basis: Bounded negative, source-first functional search.
- Confidence: Medium-high for the reviewed standard runtime; no assertion about downstream private integrations.
- Caveats: External backends may impose locks/quotas and operators can manually coordinate tasks; neither establishes a Boop-owned inter-S1 conflict closure.

### Absence scope

- Surfaces inspected: Interaction/worker dispatch, automations, agent persistence/status, drafts, memory, proactive-email dedup, server lifecycle and debug dashboard.
- Plausible first-party paths checked: Parallel execution-agent spawns, shared memory, webhook deduplication, draft confirmation, scheduled concurrency and abort/retry.
- Why no material first-party path remains: These route/delegate work or prevent duplicate events at transport/action boundaries; no concrete two-S1 interference witness and corresponding specific coordination decision/feedback changing both units' subsequent operation was found in the shipped mode.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-current organization-wide discretionary control of resources, priorities or commitments is established.
- Disturbance / variety regulated: Stale jobs, worker failures, usage growth and concurrent tasks can threaten the active service, but packaged responses are local lifecycle enforcement or human-selected settings.
- Decisive decision or feedback right: Whole-system reallocation or intervention judgment is not supplied. Abort/retry applies to an individual worker; stale-heartbeat failure marking is deterministic.
- Decision owner: User/operator for runtime configuration and manual task intervention; code for fixed stale-state and scheduling rules. No autonomous or first-party complete S3 parent-control loop is shown.
- Supporting / enforcement mechanisms: Agent state dashboard, token/usage summaries, abort controllers, configured model, tool whitelist, heartbeat sweep and retry endpoint.
- Closure path: A failed/stale work cell can be marked failed, retried or cancelled locally, but the observed path does not choose/revise current *whole-system* commitments based on a current global view.
- Why this is / is not agent-owned: A dashboard plus per-agent lifecycle API is observation/enforcement, not a managerial decision right over the whole; the dispatcher selects work for a user request, not S3 across active operations.
- Evidence: [stale-heartbeat sweep](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/heartbeat.ts#L9-L40); [worker cancellation/retry](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/execution-agent.ts#L279-L315); [server endpoints](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/index.ts#L143-L169); [dashboard metrics](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/debug/src/components/DashboardPanel.tsx).
- Basis: Bounded negative under first-party standard modes.
- Confidence: Medium; operator intervention rights exist but are not shown as whole-current S3 governance.
- Caveats: Operator self-hosting or dashboard administration is not by itself an evidenced S3 `P` mode at this recursion.

### Absence scope

- Surfaces inspected: Active-job and usage dashboard, worker status/cancel/retry, heartbeat, scheduler, memory cleanup, runtime settings and dispatcher.
- Plausible first-party paths checked: Operator dashboard→intervention, agent retry/cancel, fixed stale-agent expiration, model selection and automation cadence.
- Why no material first-party path remains: No first-party loop joins the global current state to a legitimate whole-service resource/commitment judgment and returned multi-unit current-control change; reviewed actions enforce configured bounds or act on one job.

## S3* — Complementary audit

- State: —
- Function: The reviewed service has quality/checking and memory consolidation, but no sufficiently independent complementary audit of ordinary S1 claims feeding a separate current-control path.
- Disturbance / variety regulated: Incorrect agent outputs and erroneous stored memories could distort future replies; memory maintenance checks a proposed rewrite, not a separately sourced audit of overall agent operations.
- Decisive decision or feedback right: A memory-proposer/adversary/judge sequence does make a model judgment over merge/prune proposals; it is not presented as an independent audit of S1 reports/actual external results at the assessed service recursion.
- Decision owner: The model-backed judge for the narrow memory-maintenance operation; no evidenced complementary system-level S3* audit owner.
- Supporting / enforcement mechanisms: Memory snapshots, proposer/adversary prompts, JSON verdict parse, Convex memory mutations, agent logs and ordinary tool traces.
- Closure path: Judge-approved memory edits return to memory state, not as audit findings to a distinct current-control owner that can correct S1's operational assertions.
- Why this is / is not agent-owned: Multiple roles and an adversarial prompt do not prove an independent complementary organizational channel; all stages work on the same memory-proposal payload and shared original memory list.
- Evidence: [proposer/adversary/judge and memory apply](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/consolidation.ts#L168-L465); [ordinary agent logging](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/execution-agent.ts#L196-L234).
- Basis: Structural negative at declared recursion; a narrower memory-maintenance criticism path does exist.
- Confidence: Medium, specifically limited by the chosen service-level organizational boundary.
- Caveats: The consolidation judge is not ignored; its evidenced judgment is credited to memory maintenance, not automatically S3* complementary access to external operational reality.

### Absence scope

- Surfaces inspected: Consolidation proposer/adversary/judge, active memory records, execution traces, dashboard, drafts and external-action flow.
- Plausible first-party paths checked: Adversarial memory challenge, independent model choice, original memory snapshots, execution logs and approval-before-send.
- Why no material first-party path remains: Consolidation compares proposed changes against the same persisted memories as routine maintenance. No shipped independent direct-evidence sampling/replay of agent outcomes plus audit-finding return to whole-current correction was established.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party outside/future sensing → adaptation-option judgment → update of Boop's present operational capability is established.
- Disturbance / variety regulated: Changing provider capabilities, external user needs and integration landscapes might demand future adaptation, but the shipped routines react to current events/tasks.
- Decisive decision or feedback right: The proactive classifier judges whether a current email merits notifying the user; memory consolidation revises stored context; neither owns an externally prospective capability-adaptation choice.
- Decision owner: Operator configures provider/integrations and upgrades the app; ordinary model work cells reason about present user tasks.
- Supporting / enforcement mechanisms: Gmail rubric, preference memory, cron, local memory decay/consolidation, runtime/model selection UI and installed integration catalog.
- Closure path: Current emails may trigger messages; memory edits affect later prompt context, but no prospective environmental model develops an adaptation option and returns it to operational capability/S3.
- Why this is / is not agent-owned: Proactive alerts are external event reactions; storing corrected memories is not a future-oriented capability redesign; runtime switching is user configuration.
- Evidence: [proactive classifier](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/proactive-email.ts#L1-L160); [memory consolidation](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/consolidation.ts#L168-L465); [runtime settings](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/self-tools.ts#L100-L170).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: A user can task an execution agent to research the future, but an arbitrary S1 research output is not an installed harness S4 adaptation loop.

### Absence scope

- Surfaces inspected: Proactive Gmail, automation, memory consolidation and cleaning, dispatcher/tool selection, runtime self-configuration and integration management.
- Plausible first-party paths checked: New-email classification, scheduled future tasks, user preference learning, proactive notifications, model switching and memory rewrites.
- Why no material first-party path remains: These manage a current user task, saved context or operator-selected runtime setting. None closes a standing externally/prospectively grounded adaptation decision into a new present organizational capability.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate-identity/policy dispute and legitimate authority return path is established for the personal-agent service.
- Disturbance / variety regulated: Sending messages or accessing sensitive accounts requires limits, but these are ordinary action permissions and configured tool safety rather than a demonstrated S5 deliberation.
- Decisive decision or feedback right: The user confirms a draft's ordinary external action; the dispatcher is restricted to spawn/memory/automation tools. No service-level identity change or ultimate-policy deliberation is routed and returned.
- Decision owner: User/operator controls service purpose, credentials, settings and action confirmation externally. The model-backed dispatcher owns bounded S1 task choices, not ultimate identity rights.
- Supporting / enforcement mechanisms: Draft staging, `send_draft`/reject flow, allowed/disallowed tools, browser setting and isolated Codex read-only mode.
- Closure path: Confirmation leads to a worker executing a pending draft; settings alter runtime options. Neither is identity/ultimate-policy question → legitimate parent decision → binding return to future operations.
- Why this is / is not agent-owned: A prompt role, static tool restriction, local runtime switch or user saying "send it" does not amount to S5 even when security-relevant.
- Evidence: [draft confirmation and commit](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/draft-tools.ts#L18-L120); [dispatcher allow/deny list](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/interaction-agent.ts#L527-L570); [Codex isolation/config](https://github.com/raroque/boop-agent/blob/31979130b1371acd9defbea115279a06c63c1fb4/server/runtimes/codex-app-server.ts#L64-L157).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: Operator governance and software-project maintainer policy remain real but are not part of an evidenced operational S5 parent return loop of the assessed service.

### Absence scope

- Surfaces inspected: System/worker prompts, draft approval, runtime config, tool permissions, local browser and Apple modes, server routes and developer governance.
- Plausible first-party paths checked: User confirms draft, operator switches model/provider, trusted local access policy, action-tool denial, runtime isolation and contributor decisions.
- Why no material first-party path remains: Reviewed decisions are task permissions, runtime configuration or out-of-bound development governance. No supported identity-level question is routed to an ultimate authority and returned as a binding operational identity/policy revision.

## Distributed OSS parent arrangement

The maintained source is an installable personal service, not one shared runtime over repository contributors. Separate downstream local users each control their own deployment, credentials and sensitive external-action approvals. Contributor issues, releases or repository ownership do not automatically become S3/S4/S5 parent governance of an installed Boop instance.

## Self-hosted and non-human modes

The documented local server and Electron setup permit unattended scheduled work cells, but the operator still selects integrations and confirms staged external actions. Multi-agent spawning and three-role memory maintenance are not proof of a recursively complete non-human organization. No function-specific S3/S4/S5 parent mode is credited merely because a local administrator can observe or configure the service.

## Recursion

A delegated execution agent has its own task and tool environment but receives its goal from the top-level dispatcher and returns to that dispatcher. The source does not establish separate durable S2–S5 metasystems inside each spawned worker. Memory consolidation stages and scheduled tasks are operations/support within the Boop service, not autonomous recursive organizations by name.

## Variety and escalation

Requests, tool returns and incoming email create local variety. The dispatcher splits tasks by need for outside tools, the worker's scoped integrations attenuate actions, and memory/previous conversation amplify context. Tool errors and stale-agent cancellation return as statuses/logs; user draft approval is a bounded external-action gate, not automatically an algedonic channel, S3 intervention or S5 decision.

## Evidence gaps

- No provider, live LLM, browser, iMessage, integration or agent-quality run was performed; conclusions are about reachable pinned first-party code and supplied standard modes, not reliability or actual model effectiveness.
- Positive S1 assumes a legitimately configured documented Claude or Codex local runtime. The model/provider's internal cognitive loop and governance are not credited to Boop; Boop's dispatcher, controlled spawn/tool path and return are.
- The negative S3* judgment is service-recursion-relative. Memory-proposal adversarial QA is acknowledged but does not demonstrate complementary direct access to external S1 operational reality or return to whole-current control.
- Actual operator behavior in deployed instances is not observed; no `P` mode is inferred merely from debug views, settings or individual cancel/approve actions.
