---
harness_id: coworkos
project_name: CoworkOS
repository: https://github.com/RUC-NLPIR/CoworkOS
review_ref: baf03c30db56160690f9d03bfa7dee925bad6cfd
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-04
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# CoworkOS

## Review boundary

- System in focus: The shipped CLI/Desktop CoworkOS Main-agent session and its optional task subagents, project applications, shared revisioned artifacts and user-enabled standing goals/watchers.
- Purpose and identity: Execute long-horizon user work through model-selected tools, delegated scoped workers, verified shared artifacts and optionally recurring external-event monitoring.
- Relevant environment: User-chosen project filesystem, versioned document/CAD/PPT resources, model-provider API, asynchronous task callbacks, external watch events, workspace state, human interventions and time.
- Standard-distribution boundary: Installable `coworkos-app` composition, first-party `.pi/extensions/cowork.ts` and `.pi/runtime/tools`, TypeScript Main `PiSession` adapter around the external `@earendil-works/pi-agent-core` model loop, coordinator, resource candidates, goal and watch supervisors.
- Credited operating / distribution surfaces: [Cowork main prompt](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/prompts/cowork-main.md), [session bridge](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/pi-session.ts), [coordinator](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/coordinator-runtime.ts), [resource bridge](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/runtime/application-bridge.ts), [goal/watch supervisors](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/watch-supervisor.ts).
- Adjacent first-party surfaces excluded from ownership: Research paper benchmark and self-improvement claim, developer/test/e2e code, bundled optional application installers, external model inference and `pi-agent-core` internals, authoring skills absent from a specific run.
- First-party modes considered: CLI/Desktop Main session, optional synchronous/asynchronous Subagent collaboration, app-scoped `candidate` submissions, long-standing managed goals and approved monitoring packages. Merely installing the package does not activate the monitoring mode.
- Recursion level: One user project/task with a Main-owned portfolio of delegated worker cells and optional durable goal; the published multi-task desktop UI is not automatically a higher viable organization.
- Reviewed revision: `baf03c30db56160690f9d03bfa7dee925bad6cfd` on 2026-11-04; generated/current Profile 0.2.4, Methodology 0.3.7.

## Repository architecture

The CLI and dashboard connect to a `PiSession` that builds the model/tools and records complete-turn checkpoints. A model-driven Main can select tools, issue independently scoped `call_subagent` tasks, poll durable progress, read their private output and decide final artifact acceptance. The `CoordinatorRuntime` and lease scheduler handle dispatch, isolated workspaces, callbacks, retries and user/peer messages. Application resources are revisioned: a Subagent produces a private candidate at a pinned resource revision, and Main may inspect it before `accept_resource_candidate` atomically integrates or rejects it. Optional `manage_goal` and activated virtual-agent watchers sense events/time and wake Main with an external fact for plan revision. [README](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/README.md), [main prompt #L39-L52](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/prompts/cowork-main.md#L39-L52), [coordinator-runtime.ts#L263-L425](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/coordinator-runtime.ts#L263-L425).

## Operational model

Main is the accountable model-driven agent at the chosen project recursion. Subagents perform bounded separate S1 work in private directories; their reports are provisional, not automatically accepted. Deterministic scheduler and version gates enforce model decisions but do not alone own coordination or management. Long-term goal monitoring is conditional on a user/agent-created goal and explicitly activated durable watcher, and does not mean a benchmark's training outcomes are credited to this runtime.

## S1 — Operations

- State: A
- Function: Choose next tools, inspect files/results, perform code/document/visual work and revise a current user task from feedback.
- Disturbance / variety regulated: New project requirements, mismatched source files, failed commands/model calls, application render errors and updated user instructions.
- Decisive decision or feedback right: The model chooses tool actions, task solutions and next revisions after seeing tool outcomes, not just a fixed command list.
- Decision owner: Main `PiSession` model and optional task-specific subagent model loops; pi-agent-core supplies an external generic loop but the shipped composition owns prompts/tools/checkpoints.
- Supporting / enforcement mechanisms: Tool capability selection, provider adapter, turn limits, checkpoints, task workspace and headless/desktop run surfaces.
- Closure path: User task → model/tool call → first-party tool result or error → resumed model action or explicit final turn.
- Boundary reachability: `coworkos-app` installed CLI/desktop reaches Main sessions with actual registered tool collections.
- Why this is / is not agent-owned: The model makes substantive task and edit choices; the TypeScript session adapter and tool guards enforce constraints.
- Evidence: [pi-session.ts#L115-L210](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/pi-session.ts#L115-L210), [run-service.ts#L207-L335](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/run-service.ts#L207-L335), [main prompt #L16-L52](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/prompts/cowork-main.md#L16-L52).
- Basis: structural
- Confidence: high for first-party composed agent/tool feedback.
- Caveats: Paid model-provider execution was not reproduced; this is a code-path classification, not a performance result.

## S2 — Coordination

- State: A
- Distinct S1 units: Independently running model-backed task subagents with private workspaces, making candidate changes to the same shared document/resource or checking interdependent evidence.
- Inter-S1 disturbance: Two subagents can base edits on the same older shared resource revision; accepting the stale candidate would overwrite newer changes or invalidate another cell's work.
- Attenuating coordination relation: Scoped `read` versus `candidate` grants, private subagent draft, revision compare-and-swap in `accept_resource_candidate`, and Main's explicit re-read/redelegate instruction on collision.
- Feedback into subsequent S1 behaviour: A rejected `revision_conflict` leaves the current document intact; Main reads the current version, changes the affected worker's scope and re-delegates a new candidate.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The version-conflict witness, exclusion of stale writes and returned Main-to-worker corrective plan directly attenuate an identified shared-artifact interference between parallel operational cells.
- Function: Regulate cross-worker edit collisions and mismatched artifact dependencies while preserving independent task execution.
- Disturbance / variety regulated: Revision races, overlapping subagent edits, private candidate conflicts and stale evidence.
- Decisive decision or feedback right: Select whether to accept a candidate, which changed resource to inspect and how to reassign conflicting work.
- Decision owner: Model-driven Main, instructed in first-party standard prompt to check and re-delegate; deterministic resource store enforces revision safety.
- Supporting / enforcement mechanisms: Resource candidate IDs/baseRevision, transactional acceptance, explicit scoped tools, peer message and durable callbacks.
- Closure path: Worker candidate → Main inspection → atomic acceptance or revision conflict → latest resource read → new Subagent instruction/candidate.
- Boundary reachability: App-scoped candidate mode and the `accept_resource_candidate` tool are exposed in the standard application/CLI composition, when the user works with supported shared resources.
- Why this is / is not agent-owned: The Main model decides the corrective coordination response. Compare-and-swap only prevents an unsafe stale write; it does not select the next division of work.
- Evidence: [main prompt #L39-L51](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/prompts/cowork-main.md#L39-L51), [application-bridge.ts#L829-L875](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/runtime/application-bridge.ts#L829-L875), [resource-store.ts#L450-L490](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/applications/resource-store.ts#L450-L490).
- Basis: structural
- Confidence: medium-high for app-resource candidate mode; generic filesystem editing alone has no such protected S2 path.
- Caveats: The effective coordination actor is Main; no self-organizing peer conflict negotiation is assumed from `send_peer_message`.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: Main can query per-run total/running/failed/completed task counts and inspect each subagent's tool traces, diagnostics, deliverables, pending callbacks and active questions through first-party status/wait tools.
- Current-control decision scope: Decide the number/scope/timing of subagent tasks, which run to cancel or steer, which candidate to adopt, whether to reallocate work after a failure and when current task commitments are complete.
- Function: Manage current subagent portfolio and accountable integration of ongoing project work.
- Disturbance / variety regulated: Parallel bottlenecks, stalled or redundant workers, wrong deliverables, missing evidence, unexpected cancellations and unsatisfied task completion criteria.
- Decisive decision or feedback right: Start/stop/steer bounded worker assignments and accept/reject completed work after whole-run progress and artifact evidence.
- Decision owner: Main model in the supported delegated-task mode; deterministic coordinator, status tool, queues, human UI and resources execute or constrain those decisions.
- Supporting / enforcement mechanisms: `get_subagent_status`, `wait_for_subagents`, `send_subagent_message`, `cancel_subagent`, durable scheduler, artifact boundaries and model Main acceptance.
- Closure path: Whole-run status/callback/artifact feedback → Main resource and priority decision → reassign/steer/cancel/accept workers → changed subsequent work and verified final output.
- Boundary reachability: Main prompt and standard coordination tools expose these rights in the installed CLI/Desktop task flow.
- Why this is / is not agent-owned: Model Main selects current intervention based on a cross-worker view; deterministic lease priorities alone would not establish autonomous S3.
- Evidence: [progress.ts#L49-L165](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/progress.ts#L49-L165), [coordination.ts#L345-L535](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/runtime/tools/coordination.ts#L345-L535), [main prompt #L39-L52](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/prompts/cowork-main.md#L39-L52).
- Basis: structural
- Confidence: medium-high when subagents are actually used.
- Caveats: User cancel/steer controls exist as ordinary intervention; a distinct complete parent-governed S3 mode is not inferred solely from UI buttons.

## S3* — Complementary audit

- State: —
- Function: No sufficiently separate complementary-audit decision/feedback channel established apart from ordinary Main acceptance of worker artifacts.
- Disturbance / variety regulated: Incorrect worker claims and faulty artifacts are relevant, but task-level verification/inspection is assigned to the same Main that owns daily integration.
- Decisive decision or feedback right: Independently sample actual operational reality, challenge the normal reporting path and return an auditor's finding to accountable correction; no shipped dedicated assessor closes that role.
- Decision owner: Main can inspect raw candidate files and optionally delegate independent fact-checking; there is no distinct mandated or condition-triggered auditing actor in the base system.
- Supporting / enforcement mechanisms: `browse_workspace`, candidate read, source refs, test outputs, revisioned artifact review, optional independent Subagent task.
- Closure path: Main reviews ordinary work and accepts/reassigns; no established independent findings channel bypassing or checking Main's own standard report.
- Why this is / is not agent-owned: A truthful worker result check and the ability to call a generic reviewer do not alone establish complementary S3* ownership.
- Evidence: [main prompt #L43-L52](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/prompts/cowork-main.md#L43-L52), [progress.ts#L55-L85](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/progress.ts#L55-L85), [application-bridge.ts#L829-L875](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/runtime/application-bridge.ts#L829-L875).
- Basis: structural
- Confidence: medium; optional high-risk independent-review composition remains available.
- Caveats: A deployment with an explicitly independent auditor could change the result; it is not credited without that first-party standard mode.

### Absence scope

- Surfaces inspected: Main prompts, resource candidate acceptance, generic subagent review tool, status/trace views, artifact integration, run-service and optional monitoring.
- Plausible first-party paths checked: Main directly validating worker outputs, delegating independent fact checks, UI resource review, application revision checks and watcher summaries.
- Why no material first-party path remains: Each is normal S3 acceptance or user-selected generic verification, not a distinct audit sampling mandate and finding-to-Main control path with independent judgment.

## S4 — Outside-and-then intelligence

- State: A
- External distinction: Watchers poll externally changing research/web/file sources, or rule-packaged conditions and user-defined long-term goal events; those new observations can differ from the Main's last task snapshot.
- Future / prospective distinction: Durable goal plans name a next review time, waiting condition and prospective next action, and a later event/review prompts Main to reconsider the plan rather than merely repeat the current coding turn.
- Adaptation option generated: Main model changes monitoring sources/thresholds, future goal plan or next action, requests human judgment when needed, and optionally revises persistent watcher definitions.
- Path back into current capability / S3: `GoalSupervisor`/`WatchSupervisor` deliver revisioned external events to Main Inbox, Main changes the stored goal's plan/monitoring and dispatches subsequent subagent or local work accordingly.
- Function: Sustain prospective model-driven adaptation of a standing goal in response to future environmental evidence and time.
- Disturbance / variety regulated: Evolving outside information, missing/expired monitoring, long-idle plans, new evidence and goals that need human escalation.
- Decisive decision or feedback right: Choose a revised goal strategy, watch conditions and work initiation after an external change is observed.
- Decision owner: Main model when managed-goal/virtual-agent monitoring is activated; deterministic watchers handle polling/idempotent wake and human answers can constrain a particular adaptation.
- Supporting / enforcement mechanisms: Durable GoalStore, `manage_goal`/`publish_goal_update`, `WatchSupervisor`, `GoalSupervisor`, nextReviewAt, pending external events and monitor state.
- Closure path: Environmental trigger or future review tick → durable Inbox wake → Main assesses outside change → stored goal/monitor adaptation → renewed current work/next review.
- Boundary reachability: Documented standing-goal mode exists in the shipped CLI/Desktop tools, but requires explicit goal and watcher activation, not automatic creation from ordinary task wording.
- Why this is / is not agent-owned: The watcher does not choose strategy; Main model judges the changing situation and returns revised future action into its work portfolio.
- Evidence: [goal-supervisor.ts#L13-L115](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/goal-supervisor.ts#L13-L115), [watch-supervisor.ts#L95-L165](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/watch-supervisor.ts#L95-L165), [goals.ts#L130-L205](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/.pi/runtime/tools/goals.ts#L130-L205).
- Basis: structural
- Confidence: medium-high for conditional monitored-goal mode.
- Caveats: Paper-reported RSI training/evaluation gains are not reproduced or imported as runtime S4. A no-watcher ordinary session does not automatically retain prospective capability.

## S5 — Policy and identity

- State: —
- Function: No first-party organization-level ultimate-policy issue with an authoritative ruling returned into current project governance is demonstrated.
- Disturbance / variety regulated: Unsafe tools, permission mistakes and unknown user requirements are handled through ordinary access controls or task-local `askhuman`.
- Decisive decision or feedback right: Decide a binding change to the project's ultimate identity/constitutional policy after a legitimate appeal; no such path is wired.
- Decision owner: User chooses goals/tool grants, Main chooses task actions, deterministic runtime enforces access and completion contracts.
- Supporting / enforcement mechanisms: Role prompt, capability grants, app-resource scopes, human decisions and optional watch policy/notification settings.
- Closure path: Tool/user clarification constrains current work; no identity-level proposal → ultimate authority → changed governance for subsequent runs.
- Why this is / is not agent-owned: A named Main persona, tool permission and human request are not evidence of autonomous or legitimate-parent S5 by themselves.
- Evidence: [agent-identity.ts](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/domain/agent-identity.ts), [task-capabilities.ts](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/task-capabilities.ts), [goal-management.ts#L230-L355](https://github.com/RUC-NLPIR/CoworkOS/blob/baf03c30db56160690f9d03bfa7dee925bad6cfd/src/runtime/goal-management.ts#L230-L355).
- Basis: structural
- Confidence: medium-high.
- Caveats: Maintainer governance of the OSS project is a separate recursion and is not automatically transferred into a user's runtime task.

### Absence scope

- Surfaces inspected: Main identity prompt, capability grants, goal decision requests, user-steering route, resource scopes, tool registry and project maintenance.
- Plausible first-party paths checked: Identity/persona config, human `needs_input`, goal stop/complete, safety prompts, watcher notification policy and workspace administrator actions.
- Why no material first-party path remains: They affect execution or individual goals, without an ultimate policy dispute, authoritative organizational ruling and binding returned governance of subsequent project operation.

## Distributed OSS parent arrangement

The paper's institution, project maintainers and remote model providers are not credited as an operator-level VSM parent. Users retain authority over their projects and optional decisions; no separate complete S3/S4/S5 parent mode was established from configuration alone.

## Self-hosted and non-human modes

The installed CLI can use configured third-party providers and user-owned local workspaces; dedicated Main/subagents are model-backed but external `pi-agent-core` is only a loop dependency. Periodic monitoring requires an explicitly active first-party watch cycle.

## Recursion

Main and subordinate task workers form one user-task recursion. A long-standing goal is a sustained operating mode of the same task organization. Many named Virtual Agents or a UI gallery do not establish a new higher-recursion policy layer.

## Variety and escalation

Delegation, model tool selection, application adapters and watch definitions amplify ability to respond to project variety. Permission scopes, revisioned candidates, durable leases, backoff/abort and explicit review attenuate unsafe variation. A stale resource returns to Main for a new worker instruction; a goal waiting for a legitimate user answer remains blocked rather than being silently decided.

## Evidence gaps

- Source inspection covers the shipped runtime and main prompt but does not reproduce a paid model session, desktop external app operation or claimed paper benchmark.
- S2 `A` depends on model Main exercising the conflict-redelegation path for shared app resources, not on generic filesystem writes; S4 `A` is conditional on a standing goal with activated monitoring. S3* remains uncredited without a first-party independent audit decision boundary.
