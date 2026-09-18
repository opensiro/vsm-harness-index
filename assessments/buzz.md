---
harness_id: buzz
project_name: Buzz
repository: https://github.com/block/buzz
review_ref: 8953cbfff58ed768d996677fed3af0e3bac64a20
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Buzz

## Review boundary

- System in focus: the public Buzz human-agent workspace/runtime at pinned revision `8953cbfff58ed768d996677fed3af0e3bac64a20`, including the first-party `buzz-agent` loop, `buzz-acp` managed-agent bridge/pool, relay and signed-event services, CLI, workflow runtime, and Desktop owner-review surfaces that alter managed-agent and project-channel state.
- Purpose and identity: provide a self-hostable shared workspace in which autonomous agents and humans operate through common channels, repositories, issues, workflows, signed events, and managed-agent surfaces.
- Relevant environment: human requests and owner decisions, channel conversations, repositories/issues/PRs and git events, external model/tool/MCP providers, and concurrent managed-agent activity across a Buzz community.
- Standard-distribution boundary: the public `block/buzz` distribution at the pinned revision. External ACP agents such as Goose, Codex, and Claude Code, external model providers/MCP servers, and private Block deployment/release systems are dependencies or adjacent systems rather than Buzz-owned organizational actors.
- Credited operating / distribution surfaces: `buzz-agent` + `buzz-dev-mcp`; installed `buzz-acp` managed-agent execution and per-channel queueing; relay/channel/project runtime; agent-facing `buzz` CLI; shipped Desktop agent-management and project-channel owner-review flows; shipped workflow/event machinery only where implemented at the pinned revision.
- Adjacent first-party surfaces excluded from ownership: `.github` contributor/CI/release/security-review machinery; tests, conformance/test clients, benchmarks and evaluation-only surfaces; documentation stories or roadmap/vision claims not closed by shipped runtime code; private/internal Block deployment behavior; the workflow approval record/event path marked TODO and described as still being wired at the pinned revision.
- First-party operating / deployment modes considered: direct first-party `buzz-agent` coding/work agent; managed ACP agents attached to Buzz channels; multi-process `buzz-acp --agents N` operation; owner-reviewed managed-agent create/update requests; owner-reviewed project-channel creation; event/YAML workflows as deterministic support.
- Recursion level: one Buzz community/workspace containing one or more autonomous agent operational units plus a legitimate project/community owner. Individual managed agents may have their own lower-level identity and memory, but those lower-level functions are not automatically credited to the community recursion.
- Reviewed revision: `8953cbfff58ed768d996677fed3af0e3bac64a20`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Buzz combines a signed-event collaboration substrate with first-party and externally hosted agent execution surfaces. The first-party `buzz-agent` implements a model/tool loop and can use `buzz-dev-mcp` for shell/file work. `buzz-acp` connects managed ACP agents to Buzz channels, can launch up to 32 agent subprocesses, maintains session/channel state, and serializes work per channel while allowing different channels to proceed concurrently.

The relay/event model is the shared source of truth for channels, messages, project resources, git/workflow events, and observer frames. A tamper-evident per-community audit hash chain records activity, but the audit service records/verifies events rather than supplying an independent model-driven judgment.

Buzz also exposes a narrow agent-to-owner management protocol. Managed agents can send owner-encrypted signed draft requests to create or update another managed-agent persona/configuration or to add a project channel. Desktop validates origin/ownership and presents the proposal to the legitimate owner; only the owner-review path invokes the mutations that create/start an agent, modify a persona, or create the requested project channel.

The YAML workflow runtime supplies message/reaction/diff/schedule/webhook triggers and deterministic actions. An approval action can suspend workflow execution, but at the reviewed revision the approval-record/event wiring is explicitly unfinished, so that path is not credited as a separate positive ownership loop.

Primary evidence:

- [`README.md`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/README.md) — public product boundary, shared human/agent workspace, shipped agent/CLI/ACP/workflow surfaces, and the explicit note that workflow approval gates are still being wired.
- [`VISION_AGENT.md`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/VISION_AGENT.md) — first-party `buzz-agent` model/tool loop, `buzz-dev-mcp`, context management, and concurrent sessions.
- [`ARCHITECTURE.md`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/ARCHITECTURE.md) — relay/source-of-truth and crate/runtime architecture.
- [`crates/buzz-acp/README.md`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/crates/buzz-acp/README.md) — managed ACP process pool, per-channel queues/session isolation, owner control commands, concurrency and recovery semantics.
- [`crates/buzz-acp/src/base_prompt.md`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/crates/buzz-acp/src/base_prompt.md) — supported agent-facing project/agent management, collaboration, memory and work conventions.
- [`crates/buzz-cli/src/agent_management.rs`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/crates/buzz-cli/src/agent_management.rs) — signed owner-encrypted agent/project management draft protocol.
- [`desktop/src/features/agents/useAgentManagement.ts`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/desktop/src/features/agents/useAgentManagement.ts) — owned-request validation and returned create/update mutations over current managed-agent/persona/channel/runtime state.
- [`desktop/src/features/projects/useProjectChannelRequests.ts`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/desktop/src/features/projects/useProjectChannelRequests.ts) — project-owner resolution, approval, and returned project-channel creation.
- [`crates/buzz-workflow/src/schema.rs`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/crates/buzz-workflow/src/schema.rs) and [`crates/buzz-workflow/src/executor.rs`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/crates/buzz-workflow/src/executor.rs) — event-triggered workflow support and the incomplete approval wiring at this revision.
- [`crates/buzz-audit/src/lib.rs`](https://github.com/block/buzz/blob/8953cbfff58ed768d996677fed3af0e3bac64a20/crates/buzz-audit/src/lib.rs) — tamper-evident per-community audit chain, used as supporting evidence rather than S3* ownership.

## Operational model

Autonomous model-driven agents are the primary S1 units. A first-party `buzz-agent` can inspect and mutate a working environment through model-selected tools; managed ACP agents can perform similar channel-triggered work through supported external ACP runtimes, but external runtime intelligence is not credited to Buzz itself where a positive finding can be established from the first-party agent path.

Buzz supplies a concrete coordination relation for parallel managed-agent execution: multiple subprocesses may operate concurrently, but a single channel is serialized so two workers do not process that channel at once. That relation is deterministic runtime machinery rather than an autonomous coordinating agent, so it establishes S2 as a constructor-owned path rather than `A`.

At the community/project recursion, current-control changes to operational capacity and structure are deliberately parent-governed. Managed agents can propose a new agent, modify an existing agent's runtime/model/prompt/response policy, or propose a new project channel, but the shipped Desktop path requires legitimate owner review before the corresponding current-state mutation occurs. No equivalent autonomous whole-workspace S3 owner was established.

## S1 — Operations

- State: A
- Function: perform autonomous coding, research, communication and tool-mediated work in response to Buzz channel/user goals.
- Disturbance / variety regulated: user requests, repository/workspace state, tool results, channel context, implementation uncertainty and changing local task conditions.
- Decisive decision or feedback right: choose the next substantive model/tool action and iterate until the requested bounded outcome is completed or the agent determines it cannot proceed.
- Decision owner: the model-driven first-party `buzz-agent` actor.
- Supporting / enforcement mechanisms: `buzz-dev-mcp`, Buzz CLI, channel context, session/context management, relay events, tool adapters and workspace conventions.
- Closure path: a Buzz request enters the agent loop; the model selects tool/reasoning actions; tool/environment observations return; the agent continues until it publishes/returns the operational result or stops on a blocker.
- Boundary reachability: `buzz-agent` and its documented `buzz-dev-mcp` operating path are shipped first-party runtime surfaces at the pinned revision and do not depend on contributor/CI or private Block machinery.
- Why this is / is not agent-owned: the runtime and prompts bound available actions, but the substantive task decisions remain model-driven inside the first-party execution loop.
- Evidence: `VISION_AGENT.md`, `README.md`, and `crates/buzz-acp/src/base_prompt.md`.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: external ACP harnesses provide additional supported S1 actors, but the `A` classification does not rely on importing their internal organizational functions.

## S2 — Coordination

- State: C
- Function: attenuate destructive duplicate/concurrent processing among parallel managed-agent workers that share a Buzz channel/session surface while retaining useful cross-channel parallelism.
- Disturbance / variety regulated: two autonomous worker subprocesses processing the same channel concurrently could act on overlapping event batches/session context, emit duplicate or inconsistent responses, or race on channel-scoped operational state.
- Decisive decision or feedback right: admit at most one in-flight agent turn for a channel while allowing independent channels to dispatch concurrently, then release queued channel work after the in-flight turn completes.
- Decision owner: the deterministic `buzz-acp` queue/session runtime; no model-driven S2 owner is established for this decision at the pinned revision.
- Supporting / enforcement mechanisms: per-channel queues, in-flight tracking, batched pending events, scoped sessions and the multi-process ACP worker pool.
- Closure path: incoming events are assigned to a channel queue; a channel with an active prompt does not dispatch a second worker; queued events remain pending and are drained into subsequent work only after the channel becomes available.
- Boundary reachability: the per-channel serialization relation is part of the shipped `buzz-acp` multi-agent operating mode and is documented for the same 1–32 process pool used by managed agents.
- Why this is / is not agent-owned: the S2 disturbance and first-party feedback relation are concrete, but the decisive coordination choice is runtime-deterministic rather than model-owned; an autonomous coordination owner therefore remains uncomposed.
- Evidence: `crates/buzz-acp/README.md` and its documented shared-identity/per-channel queue and event-loop semantics.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: ordinary mentions, delegation, callback conventions and channel messaging are not credited as S2; the positive finding rests on the concrete same-channel concurrency disturbance and its serialization path.
- Distinct S1 units: two or more independently running managed ACP agent subprocesses from the supported `--agents N` pool, each capable of executing autonomous channel work.
- Inter-S1 disturbance: simultaneous processing of one channel by multiple workers would expose the same channel/session work to overlapping autonomous actions and duplicate/conflicting outputs.
- Attenuating coordination relation: `buzz-acp` serializes each channel so the same channel is never processed by two agents simultaneously while permitting different channels to run concurrently.
- Feedback into subsequent S1 behaviour: a worker does not receive the next queued batch for that channel until the current in-flight turn clears; queued arrivals are then drained/batched into the next turn.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism exists specifically to prevent concurrent managed-agent interference on a shared channel/session surface, not merely to choose a recipient or order a generic workflow.

## S3 — Inside-and-now control

- State: P
- Function: regulate current community/project operational capacity and structure by deciding whether managed agents are created/reconfigured and whether new project channels are admitted.
- Disturbance / variety regulated: a managed agent may identify a need for new operational capacity, a changed role/runtime/model/response policy, or a new project channel, but unilateral mutation could change shared current commitments, access and capacity without legitimate project/community authority.
- Decisive decision or feedback right: approve or reject the proposed current-state change; on approval, create/start the managed agent or modify its persona/configuration, or create the requested project channel with the selected template/visibility/TTL.
- Decision owner: the legitimate human/project owner in the shipped Desktop owner-review mode.
- Supporting / enforcement mechanisms: owner-encrypted signed observer requests, managed-agent/channel origin validation, current personas/managed agents/channels/projects/runtimes/templates queries, owner identity checks and Desktop mutations.
- Closure path: managed agent sends a bounded draft request → Desktop resolves current project/agent context and legitimate owner → owner approves → first-party mutation creates/starts or updates the agent, or creates the project channel → subsequent operation uses the changed roster/configuration/channel structure.
- Boundary reachability: the draft protocol, observer relay, owner-review hooks and create/update/project-channel mutations are all shipped first-party CLI/Desktop/runtime surfaces at the pinned revision; closure does not rely on contributor governance or a private deployment.
- Why this is / is not agent-owned: the proposing agent may formulate the desired change, but the decisive authority is intentionally retained by the legitimate owner. No first-party autonomous or constructor S3 ownership mode over the whole community was established, so the publication state is standalone `P`.
- Evidence: `crates/buzz-cli/src/agent_management.rs`, `desktop/src/features/agents/useAgentManagement.ts`, `desktop/src/features/projects/projectChannelRequest.ts`, `desktop/src/features/projects/useProjectChannelRequests.ts`, and the agent-facing management instructions in `crates/buzz-acp/src/base_prompt.md`.
- Basis: `explicit` and `structural`.
- Confidence: medium-high.
- Caveats: workflow approval suspension is not used as the witness because the corresponding approval-record/event wiring is unfinished at the reviewed revision. Changing an individual agent's system prompt is treated here as current roster/configuration control at the community recursion, not automatically as community-level S5.
- Whole-system current view: the owner-review surfaces resolve the current managed-agent/persona roster, channels/projects, available runtimes and relevant templates/ownership for the community/project before applying a change.
- Current-control decision scope: current operational capacity/agent roster, managed-agent behavior/runtime configuration, and project-channel structure used by subsequent work.

## S3* — Complementary audit

- State: —
- Function: no materially separate first-party autonomous complementary-audit function is established at the reviewed community/runtime boundary.
- Disturbance / variety regulated: Buzz records signed events and exposes review/audit-oriented data, but the inspected operating surfaces do not supply a distinct autonomous auditor with complementary access, protected judgment and a corrective return path.
- Decisive decision or feedback right: none established for a qualifying S3* function.
- Decision owner: none established.
- Supporting / enforcement mechanisms: tamper-evident audit hash chains, observer events, workflow/git events, ordinary agent review capability and contributor/CI review machinery.
- Closure path: not applicable; the audit chain can record/verify integrity but does not independently judge operational claims and force returned correction.
- Why this is / is not agent-owned: logging, event integrity and an agent's ordinary ability to review work do not establish organizationally independent complementary audit; adjacent contributor/security-review tooling is outside the assessed runtime ownership boundary.
- Evidence: `crates/buzz-audit/src/lib.rs`, `README.md`, runtime/agent documentation, and the excluded contributor/CI surfaces.
- Basis: `explicit` and `absence review`.
- Confidence: high.
- Caveats: future shipped reviewer/approval wiring could change this finding and would require new-ref reassessment.

### Absence scope

- Surfaces inspected: first-party agent/ACP runtime, relay/observer/audit services, workflows, CLI, Desktop managed-agent/project control, repository architecture/docs and adjacent contributor/CI review surfaces.
- Plausible first-party paths checked: tamper-evident audit log, git/review stories, workflow approval/review actions, observer telemetry, ordinary agent review behavior and `.github` security/contributor review machinery.
- Why no material first-party path remains: none of the shipped runtime candidates at the pin combine independent auditor ownership, materially complementary access and a returned correction/block path; the strongest separate review tooling is either ordinary S1 work, data/integrity support, unfinished workflow glue, or an adjacent contributor system.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct first-party outside-and-prospective intelligence function is established at the community recursion.
- Disturbance / variety regulated: Buzz supports search, durable memory, scheduled/event-triggered work and agent learning conventions, but these mechanisms do not by themselves model changing external/future conditions and return organizational adaptation into current control.
- Decisive decision or feedback right: none established for a qualifying S4 adaptation function.
- Decision owner: none established.
- Supporting / enforcement mechanisms: core/cold agent memory, context compaction, schedules/webhooks/workflows, repository/git events, search and project history.
- Closure path: not applicable; no first-party environment/future distinction → adaptation option → returned community capability/control change loop was established.
- Why this is / is not agent-owned: memory hygiene, task research, reacting to events and changing an individual agent after an owner request remain operational/current adaptation mechanisms rather than a separate S4 conversation.
- Evidence: `crates/buzz-acp/src/base_prompt.md`, workflow schema/executor, `README.md`, `VISION_AGENT.md` and architecture material.
- Basis: `absence review`.
- Confidence: high.
- Caveats: a deployment may build strategic/research agents on Buzz, but deployment-specific agent roles are separate systems-in-focus and are not inherited by the generic runtime.

### Absence scope

- Surfaces inspected: agent prompts/memory, schedules/workflows/webhooks, search/history, project/repository integrations, agent-management/project-channel proposals, architecture/vision material and runtime source surfaces.
- Plausible first-party paths checked: context summarization, durable memory lessons, scheduled/continuous work, event-driven workflows, external git/repository events, agent self-management drafts and roadmap/vision claims.
- Why no material first-party path remains: the inspected paths either preserve/execute current work or allow configured current-state changes; none establishes a distinct external-and-future intelligence owner with an adaptation option and closed return into present community capability.

## S5 — Policy and identity

- State: —
- Function: no community-level identity/ultimate-policy authority loop is established at the reviewed recursion.
- Disturbance / variety regulated: owner-authored agent personas/system prompts, response policy, permissions, project ownership, access controls and workflow rules constrain operation, but they do not establish a distinct legitimate conversation that resolves Buzz-community identity or ultimate policy and returns that judgment into operation.
- Decisive decision or feedback right: none established for a qualifying community-level S5 function.
- Decision owner: none established for that function.
- Supporting / enforcement mechanisms: personas/system prompts, owner review, project ownership, channel membership/visibility, authentication/authorization, runtime/provider/model configuration and workflow policy.
- Closure path: not applicable; no community identity/ultimate-policy issue → legitimate S5 judgment → authoritative returned policy loop is evidenced.
- Why this is / is not agent-owned: individual managed-agent identity can be authored or changed under owner review, but that is a lower-recursion agent-persona decision. Static permissions/policies and ordinary owner control over current resources do not become S5 at the community recursion.
- Evidence: agent-management request/approval code, project-channel owner checks, `crates/buzz-acp/src/base_prompt.md`, README/architecture and standard configuration surfaces.
- Basis: `absence review`.
- Confidence: high.
- Caveats: this finding does not claim that a particular Buzz deployment cannot define an S5 actor; it states that the generic pinned distribution does not supply one for the declared system-in-focus.

### Absence scope

- Surfaces inspected: agent/persona creation and update, project/channel ownership, access/auth controls, workflow/config policy, base prompts, public governance/docs and runtime management surfaces.
- Plausible first-party paths checked: owner changes to system prompts/runtime/model/response policy, project owner approvals, channel policy, static identity/configuration, public contributor governance and human presence in shared rooms.
- Why no material first-party path remains: these paths either govern lower-recursion agent identity or current operational configuration/access; no supported community-level ultimate-purpose/policy tension is decided by a legitimate S5 authority and returned as organization-wide policy.

## Recursion

Buzz is naturally capable of hosting nested organizations, but the assessment fixes one community/workspace as the system-in-focus. Managed agents are S1 units at that recursion. Their own prompt/memory identity can be analyzed at a lower recursion, but it is not promoted to community S5. A project or channel can also host a more specialized organization, but such a deployment would require its own evidence and assessment.

## Variety and escalation

The model/tool loops, external ACP adapters and parallel worker pool amplify operational variety. Per-channel serialization attenuates a concrete concurrency disturbance. Signed events, origin/ownership checks, permissions and audit chains constrain action/evidence integrity. When a managed agent wants to change current organizational capacity or project structure, the owner-reviewed draft protocol escalates the matter to the legitimate parent and returns an approved mutation into later operation.

## Evidence gaps

The reviewed revision documents broader stories around agent review and approval, while workflow approval glue is explicitly incomplete. Those aspirational/partial paths are not credited. No private Block deployment behavior is used. A later release that ships an independent reviewer, autonomous whole-community regulator, strategic adaptation loop or community-level policy authority should be evaluated as new-ref evidence rather than projected backward onto this pin.

## Admission conclusion

Canonical vector: `A C P — — —`.
