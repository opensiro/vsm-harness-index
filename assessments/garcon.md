---
harness_id: garcon
project_name: Garcon
repository: https://github.com/cfal/garcon
review_ref: c278477494960465fe5aab71004588a46f6539ce
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Garcon

## Review boundary

- System in focus: one self-hosted Garcon coding/agent workspace, including first-party direct model-chat sessions, supervised heterogeneous coding agent chats, durable tickets and claim APIs, chat messages and delegation provenance, task/chat/terminal controls, human supervisory UI and Git review/control features.
- Purpose and identity: give a local operator a coherent workspace to run multiple coding-agent sessions, coordinate tickets and chat work, inspect actual files/diffs, intervene, and deliver reviewed changes; direct model sessions also produce interactive text answers in the same interface.
- Relevant environment: operator and workstation, source repositories/working directories, tool and Git state, installed third-party coding agents, model provider endpoints, terminal processes and browser.
- Standard-distribution boundary: shipped Bun server, Garcon web UI/CLI, ticket/chat controllers, and direct provider adapter packages. External Claude Code/Codex/Cursor/OpenCode/Amp/Factory Droid/Pi reasoning and their internal tool-use/session control are not Garcon-owned. Optional companion `cfal/garcon-skills` is separate from first-party distribution.
- Credited operating / distribution surfaces: `server-agents/common/src/direct/*` direct text-agent model/session loop; first-party `server/chats`, `server/tickets`, `server/routes` and `web` coordination/operator pathways.
- Adjacent first-party surfaces excluded from ownership: repository development/CI, screenshot demonstrations, third-party agent internals and companion skills code, GitHub's PR review actions outside Garcon, example preambles not activated in the inspected deployment.
- First-party operating / deployment modes considered: single-user local workspace, authenticated self-hosted browser and CLI, multiple concurrent chats, direct model-provider mode, external coding-agent process mode, optional in-chat agent ticket commands, human steering/permission/status and Git diff inspection.
- Recursion level: one Garcon-managed workspace with independently operating agent/chat sessions; the Garcon open-source maintainers and other users' workspaces are separate systems.
- Reviewed revision: `c278477494960465fe5aab71004588a46f6539ce`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The first-party `DirectChatRuntimeBase` creates durable sessions and dispatches model turns through OpenAI-compatible chat, Responses and Anthropic-compatible direct adapters. In the Chat adapter the first-party `streamSession` constructs model/history messages, calls `/chat/completions` with streaming, accumulates response text and hands it back to the managed chat session. This is a genuinely first-party model-backed interactive S1 path, although **not** evidence Garcon owns external coding agents' autonomous coding/tool loops. Non-direct adapters start selected host-installed coding-agent runtimes; Garcon manages processes, streams, turn delivery, approval and session state, not their provider-specific cognition.

Garcon's ticket service is a first-party durable SQLite domain: tickets may have owners, links, revisions and histories, with in-chat ticket mutation commands admitted by `TicketCommandController`. Its claim transition refuses an agent/chat owner when another owner already holds the ticket and returns an explicit conflict rather than silently double-claiming the work. A release removes the owner and makes the ticket available to subsequent work. The controller returns the operation outcome to the requesting chat. The human UI also exposes a ticket board and chat catalogue; the server provides run/steer/interrupt/stop and Git views so operators can inspect and revise live current work.

Sources: [direct-chat-runtime-base.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server-agents/common/src/direct/direct-chat-runtime-base.ts); [openai-compatible-chat-runtime.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server-agents/common/src/direct/openai-compatible-chat-runtime.ts); [openai-compatible-responses-runtime.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server-agents/common/src/direct/openai-compatible-responses-runtime.ts); [anthropic-compatible-chat-runtime.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server-agents/common/src/direct/anthropic-compatible-chat-runtime.ts); [mutations.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/tickets/mutations.ts); [service.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/tickets/service.ts); [command-controller.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/tickets/command-controller.ts); [inter-agent-message-controller.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/chats/inter-agent-message-controller.ts); [README.md](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/README.md).

## Operational model

The operational units are individually model-driven chat sessions that produce responses/outputs in the user's working environment. Garcon itself instantiates direct provider model sessions; externally installed coding agents are independent operational actors **composed** through Garcon's startup and control APIs, and may have richer internal tool autonomy that must not be credited to Garcon's first-party agent implementation. Ticket contention is an explicit constructor coordination surface for concurrently running/participating chats, not autonomous ticket negotiation. The operator owns current portfolio and process interventions in a supported parent-governed workspace mode. Static queues, history, Git diff views and permissions remain support mechanisms unless their VSM-specific decision/feedback path is reconstructed.

## S1 — Operations

- State: A
- Function: execute model-directed interactive chat work within first-party managed direct-provider sessions, alongside externally backed coding-agent work cells whose internal cognition is not credited.
- Disturbance / variety regulated: changing user prompts, model responses, historical chat context, provider response variability and interrupted sessions.
- Decisive decision or feedback right: the configured model in each Garcon direct chat chooses the substantive answer and follow-up response to the local conversation context.
- Decision owner: the model-driven direct chat agent instantiated by Garcon; external provider performs inference but Garcon owns session orchestration and decision delivery.
- Supporting / enforcement mechanisms: session store and checkpoint, `DirectChatRuntimeBase`, direct adapter `streamSession`, provider API and response streaming, host chat registry, turn/abort controls.
- Closure path: operator input into running direct session → first-party adapter sends accumulated session history to model → model returns discretionary content → Garcon saves/delivers result → subsequent prompt consumes updated context.
- Boundary reachability: first-party direct OpenAI/Anthropic-compatible packages are part of shipped supported provider modes, not just development mocks.
- Why this is / is not agent-owned: without model inference there is no comparable discretionary text response, while Garcon's session/transport alone merely routes and persists history.
- Evidence: [direct-chat-runtime-base.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server-agents/common/src/direct/direct-chat-runtime-base.ts); [openai-compatible-chat-runtime.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server-agents/common/src/direct/openai-compatible-chat-runtime.ts); [openai-compatible-responses-runtime.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server-agents/common/src/direct/openai-compatible-responses-runtime.ts); [README.md](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: direct adapters reviewed here primarily provide text/media conversation, **not** a Garcon-native autonomous coding tool executor. Rich coding-agent S1 belongs to external adapters. A provider API key and actual compatible model are required for live model turns.

## S2 — Coordination

- State: C
- Function: attenuate competing claims for the same shared ticket by distinct chat/agent work units, returning owner-conflict or release results into subsequent work.
- Disturbance / variety regulated: concurrently operating agent chats attempting to take incompatible ownership of a shared item of work; double claiming can generate conflicting edits/commitments.
- Decisive decision or feedback right: authorize/refuse a claim from a named chat owner on the same ticket; release it so a new owner may proceed.
- Decision owner: deterministic first-party ticket mutation service implements operator/agent-selected owner constraints; there is no first-party autonomous S2 decision actor changing the conflict policy.
- Supporting / enforcement mechanisms: durable owner keys, expected ticket revision, synchronous transaction, claim/release mutation, ticket-command dispatcher and response to source chat.
- Closure path: source agent chat submits claim ticket command → shared ticket transaction checks existing assignee → incompatible claimant receives `TICKET_ALREADY_CLAIMED` and cannot take the ticket → source gets a response and can select other work; after release the next claim can succeed.
- Boundary reachability: ticket commands are installed in first-party `TicketCommandController` for chat-originated commands and use the same `TicketService` as browser/API actions; local ticket board is a shipped feature.
- Why this is / is not agent-owned: conflict damping is specific to the first-party constructor transaction, while the substantive choice of which ticket to pursue is made by the chat/agent or human; an external agent's strategy is not imputed to Garcon.
- Distinct S1 units: two independently running attached coding-agent chat work units in a shared Garcon workspace (each with a process/session and local assigned outcomes), with optional first-party direct model chat units in the same host.
- Inter-S1 disturbance: two work units try to claim the same durable ticket and would otherwise both assume responsibility for one item, risking duplicate/conflicting work.
- Attenuating coordination relation: `mutateTicket` claim branch refuses different existing `assignee`; revision check and owner-only release constrain conflicting mutation.
- Feedback into subsequent S1 behaviour: `TicketCommandController` reports the ticket conflict/success response in the originating chat's transcript and blocks competing assignment; subsequent work can adapt to the result or wait for the release.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a concrete conflict over *exclusive ticket ownership* is regulated, not simply passing messages or ordering delegated jobs.
- Evidence: [mutations.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/tickets/mutations.ts); [service.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/tickets/service.ts); [command-controller.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/tickets/command-controller.ts); [agent-command-replies.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/chats/agent-command-replies.ts); [README.md](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/README.md).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: this establishes a scoped **ticket-claim constructor path** in a multi-chat configuration, not automatic prevention of overlapping file edits across all concurrently running agents; the model's selection remains outside the deterministic enforcement owner.

## S3 — Inside-and-now control

- State: P
- Function: human oversight and corrective regulation of current workspace work commitments, chat processes and delivery state.
- Disturbance / variety regulated: stalled/busy agent sessions, competing priorities, incorrect task assignments and partially completed repository changes.
- Decisive decision or feedback right: authorized human operator reviews whole workspace tickets/chat status and revises priorities/owners, starts/steers/stops work, stages actual changes or triggers correction.
- Decision owner: authenticated human workspace operator in the supported self-hosted parent-governed mode; not a runtime budget or autonomous Garcon S3 manager.
- Supporting / enforcement mechanisms: UI ticket board and chat catalogue, ticket HTTP mutation service, streaming live chat/turn/permission statuses, CLI start/steer/stop controls, Git diff view and staging.
- Closure path: operator observes current ticket portfolio and active chat/process states → changes ticket owner/status or steering input → first-party command/API mutates durable state or chat queue → subsequent run/session receives changed instruction or commitment.
- Boundary reachability: browser + CLI are standard distribution surfaces; authentication is enabled by default and operator can manage the complete local workspace.
- Why this is / is not agent-owned: the model does not globally revise work distribution merely because Garcon displays it; the human sees the whole portfolio and selects interventions.
- Whole-system current view: local operator sees the workspace's aggregate ticket board, live agent chats, statuses/transcripts and repository changes.
- Current-control decision scope: human changes active workload commitments, ticket assignments, process continuation/stop, steering and integration/staging decisions for the workspace.
- Parent mode: operator acts as legitimate controller for the locally self-hosted working organization; the view–decision–API/command–later-operation loop is accessible first-party. No parent control of the broader OSS community is inferred.
- Evidence: [README.md](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/README.md); [service.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/tickets/service.ts); [http.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/tickets/http.ts); [TicketDetail.svelte](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/web/src/lib/components/tickets/TicketDetail.svelte); [chats.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/routes/chats.ts); [git.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/routes/git.ts).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: this is the **local human parent operating mode**, not a claim of whole-current autonomous agent governance, and not an inference from the existence of any individual approval button.

## S3* — Complementary audit

- State: ?
- Function: challenge ordinary reports of agent work through an independent operational-evidence channel; complete autonomous/constructor audit closure is not established.
- Disturbance / variety regulated: a chat claiming success despite source differences, failures or unverifiable edits.
- Decisive decision or feedback right: no established first-party independently adjudicating agent beyond a human examining the available Git/terminal artifacts.
- Decision owner: unresolved for a positive S3* assessment; operator can inspect but a distinct guaranteed correction loop is not evidenced.
- Supporting / enforcement mechanisms: diff/staging UI, terminal, transcript reasoning/tool views, fork/delegation history and workflow status.
- Closure path: actual Git diffs and artifacts can be inspected separately from a chat report, but no evidenced independent reviewer → judgment → returned correction process is established as part of the assessed first-party audit function.
- Boundary reachability: Git review and transcript controls ship in the workspace; independence and audit ownership do not follow from visibility alone.
- Why this is / is not agent-owned: external coding agents and optional review prompts might perform checks, but their autonomous audit judgments cannot be attributed to the Garcon runtime without first-party binding evidence.
- Claim being audited: a completed chat or ticket produced the requested code change correctly.
- Ordinary reporting path: chat messages, status, ticket completion and transcript.
- Complementary access path: operator Git diff and working tree inspection rather than only the claim narrative.
- Independence boundary: no separately proven independent organizational reviewer with bounded direct evidence access and returned action.
- Who acts on findings: human operator may steer further work; systematic independent audit closure unverified.
- Evidence: [git.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/routes/git.ts); [README.md](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/README.md); [inter-agent-message-controller.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/chats/inter-agent-message-controller.ts).
- Basis: structural + unresolved.
- Confidence: medium (in insufficiency).
- Caveats: `?` deliberately does not claim absence. Inspect any configured independent review workflow before promotion.

## S4 — Outside-and-then intelligence

- State: ?
- Function: prospectively sense external development demands and adapt the future capabilities of the whole workspace.
- Disturbance / variety regulated: future project requirements, external technology shifts and changed delivery constraints.
- Decisive decision or feedback right: unestablished; schedules and stored context preserve work but do not alone choose prospective adaptations.
- Decision owner: unresolved between operator, external agent and any internal first-party adaptive unit.
- Supporting / enforcement mechanisms: scheduled prompts, handoff/context artifacts, session history and search/export.
- Closure path: history may be retrieved or scheduled prompts run, but no external/prospective adaptation option and corresponding capability-change return was established.
- Boundary reachability: these tools ship but their presence is not function-specific S4 closure.
- Why this is / is not agent-owned: persistence and scheduled triggers do not imply that the model internally controls future system capabilities.
- External distinction: external project demands not tied to a first-party sampled prospectively adaptive function.
- Future / prospective distinction: pending tasks and time triggers alone are not prospective intelligence.
- Adaptation option generated: unverified.
- Path back into current capability / S3: no reconstructable first-party return.
- Evidence: [agent-schedule-controller.ts](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/server/chats/agent-schedule-controller.ts); [README.md](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/README.md).
- Basis: structural + unresolved.
- Confidence: medium (in insufficiency).
- Caveats: no `—` claim because optional scripts or configured models might support a future-facing process beyond the inspected scope.

## S5 — Policy and identity

- State: ?
- Function: settle identity or ultimate purpose/policy of the focal workspace, not just ordinary permissions.
- Disturbance / variety regulated: changes that would require an ultimate-governance decision concerning purpose, legitimate authority or what work is admissible.
- Decisive decision or feedback right: operator controls authentication, agent/provider configuration, prompts and permissions, but an identity-level policy decision/return loop was not reconstructed.
- Decision owner: operator owns configuration and action permission decisions; ownership of the distinct S5 function is unresolved.
- Supporting / enforcement mechanisms: auth, account/workspace settings, permission approval controls, preambles and process/command constraints.
- Closure path: authorization and operator settings constrain actions, but an evidenced ultimate-policy issue → legitimate parent decision → returned policy governing subsequent operation was not shown.
- Boundary reachability: supported local/authenticated modes and their controls are real; they do not automatically establish S5.
- Why this is / is not agent-owned: a model selecting tool calls subject to static permission policy does not own identity governance.
- Identity / ultimate-policy issue: no concrete runtime change-of-identity/purpose dispute with authoritative resolution found.
- Ultimate authority in each claimed mode: no positive S5 ownership configuration claimed.
- Return-to-operation path: ordinary tool/permission configuration reaches execution, but that is not evidence of identity-level closure.
- Evidence: [security.md](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/docs/security.md); [README.md](https://github.com/cfal/garcon/blob/c278477494960465fe5aab71004588a46f6539ce/README.md).
- Basis: explicit + unresolved.
- Confidence: medium (in insufficiency).
- Caveats: withholding `P` is intentional: first-party human approval alone is not whole-workspace S5.

## Distributed OSS parent arrangement

Multiple Garcon contributors independently running coding agents do not form one operational parent organization merely by sharing an OSS codebase. The credited parent mode is the single self-hosted operator's whole-workspace current regulation; no project-wide S3/S4/S5 owner is inferred.

## Self-hosted and non-human modes

Self-hosted Garcon can run supported direct model chats and supervised coding-agent workers. Human steering/permission decisions are optional for some turns but provide the evidenced local S3 parent controller. Third-party coding sessions may employ rich autonomous tool loops, but Garcon's first-party *direct* adapters reviewed here are bounded model chat, not a first-party code-execution runtime. The S2 ticket ownership path becomes applicable when multiple chat owners use the first-party ticket command surface.

## Recursion

One workspace is the focus, individual direct/external chat sessions are local operational units, and nested delegated sessions are not treated as an autonomous viable organization solely because parentage is recorded. Other operators' Garcon workspaces and GitHub maintainer organization are distinct recursions.

## Variety and escalation

Models and external worker agents handle local tasks; tickets can reserve exclusive owner commitments; Garcon queues and inter-chat messages support coordination but are not separate S2 witnesses without a specific conflict; humans can steer, stop, review source and reallocate current work. Scheduler execution and transcript handoffs preserve context, not automatically S4 adaptation.

## Evidence gaps

- Confirm the first-party ticket-command surface in a multi-chat self-hosted deployment, including competing claim resolution and the distinct S1 owners receiving the error or later release; S2=C should not be extrapolated to all simultaneous file writes.
- Inspect whether any standard first-party review process provides independent raw-evidence audit judgments and returned corrective work, beyond the operator's UI-only diff inspection.
- Check separate prospective adaptation and ultimate-policy procedures before changing S4/S5 uncertain states.
- No provider-backed end-to-end execution or real competing-ticket concurrency experiment was performed; review reflects frozen source and documented first-party distribution.
