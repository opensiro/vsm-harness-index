---
harness_id: company-brain
project_name: Company Brain
repository: https://github.com/supermemoryai/company-brain
review_ref: 0071d6164991ce5dccddbd645bcac631ee477572
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Company Brain

## Review boundary

- System in focus: one self-hosted Company Brain deployment for one Slack-backed organization, centered on the first-party `CompanyBrainAgent` Durable Object and its shipped memory, tool, scheduling, proactivity, approval, lease and configuration paths at pinned revision `0071d6164991ce5dccddbd645bcac631ee477572`.
- Purpose and identity: act as a persistent company-aware Slack teammate that recalls permission-scoped organizational context, answers questions, invokes connected tools, performs bounded actions, runs scheduled work and may speak proactively when it judges that it can add useful information.
- Relevant environment: Slack users/channels, organization administrators, Supermemory-backed memory containers, connected MCP/Google/GitHub-style tools, external model providers, Cloudflare runtime/storage, repositories and other SaaS systems reached through tools.
- Standard-distribution boundary: the open-source Company Brain application and documented self-hosted Cloudflare deployment, including the per-organization agent, Slack event/turn path, memory graph, tool assembly/execution, automations, chime-in, approvals/leases, sandbox integration and administrator configuration shipped at the pinned revision. External model inference, Slack itself, Supermemory service internals, MCP providers and downstream custom modifications remain environment.
- Credited operating / distribution surfaces: `CompanyBrainAgent`; explicit Slack turns and chime-in; model/tool turn loop; permission-scoped memory search/writeback; MCP/embedded tools; write approvals and temporary leases; scheduled automations; workspace prompt and proactivity/model configuration as wired into subsequent turns.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests, deployment/setup helpers, observability/analytics, documentation-only future long-horizon research behavior, rollout/install UX, billing/trial machinery and repository maintainer governance. These may corroborate implementation but are not credited as separate organizational decision owners.
- First-party operating / deployment modes considered: ordinary DM/@mention turns; proactive channel chime-in; scheduled automations; read and write tool use with approvals; sandbox/code execution when configured; administrator-managed workspace prompt/proactivity/model settings; self-hosted Slack deployment.
- Recursion level: the assessed organization is one Company Brain installation serving one organization. Individual turns, fibers, scheduled jobs, tool calls and research tasks are activities of the same installed agent rather than separately credited viable S1 workcells at this recursion.
- Reviewed revision: `0071d6164991ce5dccddbd645bcac631ee477572`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Company Brain is a TypeScript/Cloudflare application whose central runtime actor is `CompanyBrainAgent`, one Durable Object instance per organization. Slack events enter the worker, are classified into explicit turns, proactive chime-in, context-only or lifecycle handling, and the main turn path chooses whether to answer directly, search memory, call live tools or do deeper tool work. The agent persists turn/approval/automation/research state in Durable Object SQL and uses organization/user/channel-scoped memory containers for durable company context.

The operating loop can search company memory, inspect Slack context, call MCP and embedded integrations, run code/sandbox operations and issue side effects. Consequential writes suspend for explicit approval by the original requester; temporary teammate tool access can be leased only through an explicit approval path. Scheduled automations wake independently and generate fresh read-only digests under the destination's permission scope. Chime-in is unscheduled model-mediated participation gated by usefulness/confidence rules and deterministic rate/room constraints.

The standard deployment nevertheless remains organizationally centered on one Company Brain agent per organization. Fibers, scheduled tasks, research passes and tool calls extend or recover that operational loop; the reviewed distribution does not expose them as durable sibling operational units with independent identities whose interference must be coordinated. Observability, retries, fallback models and approvals constrain execution but do not create a separate whole-system controller or independent audit organization.

Administrators/owners do have a first-party policy path. They can change persistent workspace-wide guidance and organization-level behavior settings. The workspace prompt is stored in the organization agent and injected into subsequent turns as persistent high-priority workspace context, below fixed system/safety/authorization rules but above learned memory/style defaults. This gives a legitimate parent authority a runtime return path for installation-level operating policy.

Primary evidence:

- [`README.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/README.md) — product boundary, memory, tools, proactive behavior, sandbox and scheduled work.
- [`docs/architecture.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/architecture.md) — one `CompanyBrainAgent` per organization, Slack turn path, memory/tool/storage architecture and approval behavior.
- [`docs/agent.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/agent.md) — Durable Object surface, turn fibers/recovery, models, scheduling, research, approvals and tool assembly.
- [`docs/guide/permissions.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/guide/permissions.md) — permission graph, owner/admin authority and explicit access/lease approval.
- [`docs/guide/automations.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/guide/automations.md) — scheduled autonomous work, chime-in behavior and scope/guardrails.
- [`docs/guide/use-cases/long-horizon-research.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/guide/use-cases/long-horizon-research.md) — explicit boundary that dedicated long-running research mode is not present in this build.
- [`src/brain/turn/agent.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/turn/agent.ts) — first-party per-organization agent shell and runtime surfaces.
- [`src/brain/turn/compute.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/turn/compute.ts) — primary turn computation path.
- [`src/brain/turn/tools.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/turn/tools.ts) — assembled operational tool surface.
- [`src/brain/turn/approval.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/turn/approval.ts) — requester-owned consequential-action approval path.
- [`src/brain/turn/research.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/turn/research.ts) — onboarding company/environment research aspects and their informational output.
- [`src/brain/prompt/build.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/prompt/build.ts) — workspace prompt returned into subsequent agent behavior.
- [`src/routes/workspace-prompt.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/routes/workspace-prompt.ts) — administrator-facing workspace policy update surface.

## Operational model

The primary S1 unit is the installed Company Brain agent itself. It absorbs open-ended Slack requests and channel events, selects whether and how to use memory/tools, iterates over model/tool results and returns answers or external side effects. Scheduled automations and proactive chime-in create additional triggers for the same operational actor rather than separate viable units. Deterministic runtime code supplies persistence, access boundaries, approvals, scheduling, retries, provider fallback and rate limits.

At the selected recursion, no first-party sibling S1 organization is established. The installation therefore has rich operational capability but little evidence of an internal VSM metasystem. Parent governance is materially different: owner/admin configuration can set persistent installation-wide operating guidance, and that decision is injected into later model turns, giving a closed parent-governed policy path.

## S1 — Operations

- State: A
- Function: provide company-context-aware answers and bounded actions in response to Slack interaction, scheduled work and proactive participation.
- Disturbance / variety regulated: open-ended employee questions, changing channel context, heterogeneous company memory, connected-tool state, tool errors, authorization constraints, model/tool results and conversational follow-up.
- Decisive decision or feedback right: choose the operational response path for a turn — whether to answer, search memory, inspect live tools, invoke tools/sandbox, continue the tool loop, ask for access/approval or finish the turn with a result.
- Decision owner: the configured main model acting inside the first-party `CompanyBrainAgent` turn loop.
- Supporting / enforcement mechanisms: Slack event routing/triage, Durable Object state, permission-scoped memory containers, model-provider fallback, tool assembly, deterministic authorization, approval suspension/resume, scheduling, retries/recovery, sandbox execution and terminal `finish_turn` protocol.
- Closure path: Slack event/automation/chime trigger enters the organization agent → model receives scoped context and available tools → model selects memory/tool/action steps → tool results and failures return to the loop → the model revises or completes work → final answer/action result is published and durable context may be written back for subsequent operation.
- Boundary reachability: the shipped Slack deployment routes ordinary user turns to the per-organization `CompanyBrainAgent`; the model/tool loop, memory and tool assembly are production paths in the reviewed distribution rather than examples or development-only surfaces.
- Why this is / is not agent-owned: deterministic runtime machinery constrains permissions, retries and publication, but does not reproduce the substantive open-ended selection of sources, tools, intermediate actions and answer content if the model decision-maker is removed. The agent therefore owns the relevant operational discretion.
- Evidence: [`docs/architecture.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/architecture.md); [`docs/agent.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/agent.md); [`src/brain/turn/compute.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/turn/compute.ts); [`src/brain/turn/tools.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/turn/tools.ts).
- Basis: explicit + structural
- Confidence: high
- Caveats: external model inference is a dependency, while the first-party harness owns the operational loop and applies the model's decisions to memory, Slack and connected tools.

## S2 — Coordination

- State: —
- Function: no material installation-level S2 function is established at the selected recursion.
- Disturbance / variety regulated: no specific interference, conflict or oscillation among distinct durable S1 units is evidenced because the standard deployment centers one organization-level Company Brain operational actor.
- Decisive decision or feedback right: none established for inter-S1 coordination.
- Decision owner: none established.
- Supporting / enforcement mechanisms: event dedupe, fibers, schedules, rate limits, permissions, channel scopes, leases and queues organize execution of the same agent but do not establish a disturbance-specific relation among sibling S1 units.
- Closure path: no qualifying inter-S1 coordination closure identified.
- Why this is / is not agent-owned: multi-step work, concurrent events and scheduled jobs remain internal execution variety of one installed agent; generic sequencing or shared state is not credited as S2.
- Evidence: [`docs/architecture.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/architecture.md); [`docs/agent.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/agent.md); [`docs/guide/automations.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/guide/automations.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: downstream operators could compose multiple Company Brain installations or external agents, but that is outside the reviewed standard-distribution boundary.

### Absence scope

- Surfaces inspected: runtime/architecture docs, per-organization agent surface, Slack turn/chime paths, automations, memory scopes, leases/approvals and tool assembly.
- Plausible first-party paths checked: scheduled automations as possible sibling operations, fibers/recovered turns as possible independent workcells, channel-specific memory/proactivity as possible coordination, and tool/lease mechanisms as possible cross-unit conflict regulation.
- Why no material first-party path remains: all inspected paths are triggers, state partitions, access controls or execution mechanisms around one organization-level operational agent; no durable distinct S1 units plus concrete inter-S1 disturbance and disturbance-specific feedback loop are shipped at this recursion.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-installation current-control function is established beyond the operational agent's own task execution and deterministic runtime constraints.
- Disturbance / variety regulated: runtime limits, tool authorization, approvals, schedules and retries regulate individual operations, but no separate installation-wide current portfolio of sibling S1 commitments/resources is evidenced.
- Decisive decision or feedback right: none established for whole-system current regulation at the selected recursion.
- Decision owner: none established.
- Supporting / enforcement mechanisms: chime budgets, model step limits, approval/lease gates, schedules, provider fallback, event dedupe and per-turn recovery.
- Closure path: no qualifying whole-system S3 closure identified.
- Why this is / is not agent-owned: the main agent can decide what to do inside its own turn, but that is S1 discretion. Deterministic limits and requester approvals constrain actions without supplying a distinct whole-system current view plus authority over multiple operational commitments.
- Evidence: [`docs/agent.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/agent.md); [`docs/guide/permissions.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/guide/permissions.md); [`docs/guide/automations.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/guide/automations.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: administrator configuration and individual write approvals are real parent controls, but the inspected evidence does not reconstruct them as S3 current control on behalf of a multi-S1 whole.

### Absence scope

- Surfaces inspected: agent state/method surface, automations, approvals/leases, turn limits/recovery, proactivity controls, storage and observability descriptions.
- Plausible first-party paths checked: Durable Object as possible manager, automation manager as possible portfolio controller, approval/lease escalation as possible supervisory intervention, proactivity/rate settings as possible resource regulation and billing/step limits as possible budget control.
- Why no material first-party path remains: these mechanisms manage execution, authorization or configuration of the same agent and its requests; no first-party whole-system current view with a distinct decision right over sibling S1 resources, commitments, priorities or exceptions is established.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit path is established for operational claims.
- Disturbance / variety regulated: ordinary tool results, memory retrieval, traces and permission checks provide evidence and safeguards, but the reviewed runtime does not assign a separate auditor independent access to operational reality and return audit findings into current control.
- Decisive decision or feedback right: none established for complementary audit judgment.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Sentry/PostHog observability, ordinary tool corroboration, approval checks, terminal/finalization validation, logging and optional sandbox artifacts.
- Closure path: no qualifying independent audit-to-control closure identified.
- Why this is / is not agent-owned: source checking inside the same operating turn and routine runtime validation are in-band assurance; they do not create the complementary access/independence required for S3*.
- Evidence: [`docs/architecture.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/architecture.md); [`docs/agent.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/agent.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: the runtime may cross-check live tool evidence for answer quality, but the inspected path does not establish a distinct complementary auditor whose findings regulate S1 through S3.

### Absence scope

- Surfaces inspected: observability, approval/finalization, tool corroboration, memory/tool paths, research, tests/docs describing runtime assurance.
- Plausible first-party paths checked: live-tool corroboration as possible direct-reality audit, post-turn reflection as possible reviewer, telemetry as possible independent observation, requester approval as possible auditor and sandbox outputs as possible complementary evidence.
- Why no material first-party path remains: the inspected mechanisms are ordinary source use, operational reflection, telemetry or human authorization; no sufficiently independent audit judgment plus a returned control path over operational claims is shipped at the assessed boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed external-and-prospective adaptation loop is established for changing the installation's future capability or organizational design.
- Disturbance / variety regulated: Company Brain can inspect external/current company information and recent milestones, but the shipped research/automation paths primarily produce context or answers rather than adaptation options that change present capability.
- Decisive decision or feedback right: none established for prospective adaptation of the harness.
- Decision owner: none established.
- Supporting / enforcement mechanisms: signup company research, live web/tool search, scheduled digests, persistent memory, skills and administrator configuration.
- Closure path: external information can enter research/memory/answers, but no first-party path is evidenced from environmental/future distinction → adaptation-option generation → decision → changed current capability/S3.
- Why this is / is not agent-owned: sensing competitors, milestones or external tool state is not itself S4. The reviewed code does not show the agent converting those distinctions into prospective capability/organizational changes and closing them back into runtime behavior.
- Evidence: [`src/brain/turn/research.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/turn/research.ts); [`docs/guide/use-cases/long-horizon-research.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/guide/use-cases/long-horizon-research.md); [`docs/guide/automations.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/guide/automations.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: workspace administrators can manually change models, skills and policy after learning external information, but no first-party S4-specific parent adaptation loop linking that sensing to returned capability change is reconstructed in the standard distribution.

### Absence scope

- Surfaces inspected: signup company research, connector/web search, automations, memory/skills descriptions, model configuration and documented long-horizon research boundary.
- Plausible first-party paths checked: competitor/recent-milestone research as external sensing, scheduled digests as longitudinal intelligence, memory/reflection as learning, skills as capability evolution and model/settings changes as adaptation.
- Why no material first-party path remains: these surfaces either gather information, answer current tasks, persist context or expose generic human configuration; they do not ship a function-specific prospective adaptation decision loop whose returned decision changes current capability.

## S5 — Policy and identity

- State: P
- Function: retain installation-level operating policy and legitimate ultimate authority with the organization owner/admin, then return that policy into subsequent agent behavior.
- Disturbance / variety regulated: competing local conversational defaults, learned interaction style, memory-derived behavior and changing organization-wide priorities/workflow conventions that require a stable authoritative policy source above ordinary agent adaptation.
- Decisive decision or feedback right: set or revise persistent workspace-wide guidance and related organization-level behavior configuration that governs how the installed agent should operate across later turns.
- Decision owner: legitimate parent human authority — the deployment owner/admin role.
- Supporting / enforcement mechanisms: admin authorization, workspace-prompt storage on the organization agent, bounded prompt length, prompt assembly precedence, model/proactivity/skill settings and fixed system/safety/authorization constraints.
- Closure path: an owner/admin decides installation-wide operating guidance → writes the workspace prompt/configuration through the first-party admin surface → the value is persisted on the organization agent → subsequent turn prompt construction injects it as high-priority workspace context → later operational decisions are governed by the returned policy until revised.
- Boundary reachability: owner/admin configuration is part of the shipped self-hosted product and the stored workspace prompt is read by the same production turn path; the parent decision does not rely on repository-development governance or an adjacent external controller.
- Why this is / is not agent-owned: the main agent consumes and follows the policy but does not own the ultimate right to set it. Removing the administrator while leaving prompt-injection machinery in place leaves only enforcement of previously selected guidance, so ownership remains at the parent recursion.
- Identity / ultimate-policy issue: what persistent organization-wide priorities, workflow conventions, terminology and operating guidance Company Brain should follow across users/turns, subject to fixed higher system/safety/authorization rules.
- Ultimate authority in each claimed mode: parent mode only — deployment owner/admin. No autonomous first-party S5 mode is established.
- Return-to-operation path: admin policy update → persistent workspace prompt/configuration → `build` of later turn context → agent behavior under that policy → future Slack/tool operation.
- Evidence: [`docs/guide/permissions.md`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/docs/guide/permissions.md); [`src/routes/workspace-prompt.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/routes/workspace-prompt.ts); [`src/brain/configuration.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/configuration.ts); [`src/brain/prompt/build.ts`](https://github.com/supermemoryai/company-brain/blob/0071d6164991ce5dccddbd645bcac631ee477572/src/brain/prompt/build.ts).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: a workspace prompt or setting is not S5 merely by existing. The positive mapping relies specifically on legitimate admin ownership plus a first-party persisted return path that makes the organization-wide policy govern subsequent runtime behavior.

## Distributed OSS parent arrangement

The repository is open source, but project maintainer/contributor governance is not used to justify the S5 parent state. The credited parent is local to each deployed Company Brain organization: its owner/admin role owns the installation-wide policy path and the decision returns directly into that installation's subsequent turns.

## Self-hosted and non-human modes

The reviewed distribution is self-hosted and explicitly exposes human owner/admin configuration. No alternative first-party non-human S5 ownership mode was established. Ordinary autonomous operation remains S1; human write approvals and access leasing are task/authorization controls and are not promoted to S3 or S5 unless they close the corresponding organizational function.
