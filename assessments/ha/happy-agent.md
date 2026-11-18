---
harness_id: happy-agent
project_name: Happy Agent
repository: https://github.com/slopus/happy-agent
review_ref: bd2bd009c30ca7202f793bd9189ecadc495aeae7
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Happy Agent

## Review boundary

- System in focus: One installed Happy Agent daemon and project/task agent collection, running first-party Pi-derived and native model-specific coding loops, tools, persistent sessions, task API and optional Auto permission reviewer.
- Purpose and identity: Let model-backed coding agents carry out project tasks in durable, locally controlled sessions with operator-visible statuses, permissions and review of risky calls.
- Relevant environment: Source files and shells, provider inference results, task/session requests, tool effects, permission/policy review, and a project user's current portfolio of active sessions.
- Standard-distribution boundary: Public daemon, happy-agent-base AgentBase and AgentSystemLocal, first-party modules including native agent tools, tasks, API and Auto reviewer, with configured external model inference transports. Optional whole third-party agent/ACP delegation is an adjacent operating mode, not proof of native agent ownership by Happy.
- Credited operating / distribution surfaces: Supported desktop/API/CLI daemon path, first-party AgentBase model/tool loop, durable task agents, public API agent/status and abort controls, Auto mode's independent private reviewer and fail-closed permission decision.
- Adjacent first-party surfaces excluded from ownership: Internal `master-plans/` future designs, test/CI and developer recipes not installed into the shipped runtime, cloud/mobile service governance outside the daemon, independent third-party Claude/Codex/ACP harness internals.
- First-party operating / deployment modes considered: Local installed daemon with configured Pi/Claude SDK/Codex-native/Grok model transport; attended client/project agent collection; optional Auto permission mode with separate private model reviewer and a supported local compute backend.
- Recursion level: One installed daemon's project work cell, with multiple independently operating task agents and their legitimate project operator.
- Reviewed revision: bd2bd009c30ca7202f793bd9189ecadc495aeae7.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

AgentSystemLocal owns and restores multiple durably configured agent instances and one per-agent lock rather than a collection-wide work lock. AgentBase owns the model-response/tool-execution cycle, tool result commit and next-stage state; per-agent model transports may use Pi or first-party adaptations for Codex/Claude/Grok. The daemon exposes live project and workspace agent collections and selected agent abort/steering through its first-party API. Auto permissions are reviewed by AutoModule's separate private AgentSystemLocal, own database, access-restricted tools, historical evidence and private reviewer model; PermissionsModule enforces resulting allow, denial or unavailable state on a call. Peer messages deliver information but do not provide a proven collision arbitration loop. Separately launched whole vendor/ACP coding agents remain outside Happy's native decision ownership.

## Operational model

A project task agent makes its own model-directed substantive decisions over tools, receives the committed results and persists task/session state. Two or more sessions can run independently; the project operator sees their current project/workspace ownership and can stop a selected live agent or change its permission mode/goal. Under Auto mode, an independent, read-only model reviewer may investigate the actual pending action and surrounding history on a separate evidence surface, return a risk/authorization verdict and cause the tool call to run, be elevated for that call, or be refused; this is a bounded complementary audit of proposed operational behavior, not general correctness verification of finished code.

## S1 — Operations

- State: A
- Function: Perform requested project tasks through a native model-backed agent choosing substantive tool and subtask work.
- Disturbance / variety regulated: Open-ended task requests, source changes, tool results, provider feedback and interruptions.
- Decisive decision or feedback right: Select coding/tool actions and subsequent task steps after receiving first-party executed tool results.
- Decision owner: First-party AgentBase model session, not the daemon's fixed scheduling or an optional external ACP agent.
- Supporting / enforcement mechanisms: Pi/model transport, AgentSystemLocal lifecycle, compute tools, session persistence, permission mode and tool-result commit.
- Closure path: AgentBase collects model tool calls, invokes tools and commits outcomes into durable conversation state; further model turns act on returned results and clients receive events.
- Boundary reachability: Standard installed daemon starts native provider-backed sessions with native prompt and tools without requiring external vendor whole-agent delegation; desktop/API clients connect to the daemon.
- Why this is / is not agent-owned: The native model chooses actual task-specific tool actions; first-party substrate constrains execution and feeds results back without replacing the decision.
- Evidence: [installed first-party and foreign modes](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/README.md#L130-L189), [agent system creation/restore](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-base/sources/AgentSystemLocal.ts#L211-L240), [native AgentBase tool invocation and commit](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-base/sources/AgentBase.ts#L4742-L5037), [native model response/tool collection](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-base/sources/AgentBase.ts#L5092-L5459).
- Basis: structural
- Confidence: high
- Caveats: Source-based, no live inference subscription executed; native modes credited independently of delegated vendor whole-agent internals.

## S2 — Coordination

- State: —
- Function: Peer inboxes and per-agent locks communicate or serialize one agent's own lifecycle but do not establish a first-party inter-S1 conflict-attenuation decision.
- Disturbance / variety regulated: Two agents may compete for source files, resources or commitments across the same workspace.
- Decisive decision or feedback right: A controller would need to detect their specific interference, decide conflict resolution and return affected task constraints.
- Decision owner: Task author/agent may message another peer; no S2-specific arbitration owner was evidenced.
- Supporting / enforcement mechanisms: PeerMessagingModule, Task membership, Teammates tools, per-agent locks and session-ownership checks.
- Closure path: Messages reach peer inboxes and independently running agents may react, but no shipped conflict witness, selected resolution or binding returned coordination of competing S1s is shown.
- Why this is / is not agent-owned: P2P delivery, per-agent mutual exclusion and user task membership are not independently proven inter-agent disturbance attenuation.
- Evidence: [peer module boundary](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/peerMessaging/README.md#L1-L20), [per-agent locking](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-base/sources/AgentSystemLocal.ts#L95-L102), [team loop-in](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/teammates/README.md#L1-L18)
- Basis: structural
- Confidence: medium
- Caveats: May be supplemented by user-composed coordination; not credited without a first-party closure.

### Absence scope

- Surfaces inspected: Native agent collection, peer protocol, Teammates, project/task list, concurrent agent calls and scheduling.
- Plausible first-party paths checked: Checked automatic conflict/oscillation detection, shared resource arbitration, link to downstream S1 constraint. Found only communication, agent-local serialization and task membership.
- Why no material first-party path remains: P2P delivery, per-agent mutual exclusion and user task membership are not independently proven inter-agent disturbance attenuation.

## S3 — Inside-and-now control

- State: P
- Function: Parent controls the current project portfolio of several agent sessions and intervenes in live work.
- Disturbance / variety regulated: Active tasks can become unsafe, obsolete or conflicting with a human project's changing current commitments.
- Decisive decision or feedback right: From a project/workspace agent collection and focused agent state, choose which run to abort, which mode/goal to adjust and when to resume or retire tasks.
- Decision owner: Legitimate project owner/operator through authenticated installed daemon client/API; not a separately claimed automatic project-wide manager.
- Supporting / enforcement mechanisms: API owner-agent series for projects/workspaces, durable task records, abort route with expectedRunId conflict guard, permission mode per session, goal pause/resume.
- Closure path: Project-wide agent records and focused run state inform operator choice; the abort endpoint checks active run identity, invokes the abort system and returns the new focused agent resource; later task behavior is altered.
- Boundary reachability: Supported first-party daemon project/workspace and task APIs with per-agent abort endpoint and user-facing project controls; not a test harness or external provider console.
- Whole-system current view: First-party project/workspace owner-agent series and task associations enumerate current agents, with focused current run information.
- Current-control decision scope: Operator can terminate a chosen active run and change task or permission state for subsequent operations; controls apply across multiple agents under that project's authority.
- Why this is / is not agent-owned: The operator exercises the portfolio management choice; abort dispatch and API state updates are enforcement, not autonomous management judgement.
- Evidence: [persistent agents and local system](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-base/sources/AgentSystemLocal.ts#L95-L158), [project/workspace owner agent series](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/api/ApiModule.ts#L9553-L9578), [focused abort with conflict guard](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/api/ApiModule.ts#L5176-L5195), [persisted goals and modes](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/README.md#L287-L342).
- Basis: structural
- Confidence: medium
- Caveats: P applies only to an attended project with multiple agents and client control. No autonomous S3 loop or fleet-level optimization is claimed; API status may vary by installed module config.

## S3* — Complementary audit

- State: A
- Function: Separately inspect and decide the risk/authorization of a native agent's proposed sensitive operational action before execution.
- Disturbance / variety regulated: A coding agent may attempt a workspace/network/shell action inconsistent with user intent or safety restrictions and ordinary self-report is insufficient.
- Decisive decision or feedback right: A private reviewer model judges the pending action against user history and independently readable local evidence, may deny a call or grant bounded temporary elevation; refusal is returned to agent's tool feedback.
- Decision owner: A distinct private read-only model reviewer in AutoModule's isolated AgentSystemLocal; PermissionsModule enforces verdict and fails closed when unavailable.
- Supporting / enforcement mechanisms: Separate private storage/lock/provider catalog and reviewer ID, uncompacted user/action transcript provenance, read-only inspection tools, permission reviewer budget and typed risk/authorization classification.
- Closure path: Sensitive call → PermissionsModule asks private reviewer → reviewer investigates transcript and read-only local evidence → returned verdict is consumed to allow/deny or grant just this call elevated capability; refusal/success enters main agent tool result and project audit log.
- Boundary reachability: Auto is a supported installed session permission mode, and AutoModule supplies built-in reviewer to PermissionsModule; no user-written external reviewer skill is needed.
- Claim being audited: Whether the main agent's particular proposed action is safe and authorized by user's actual request and current policy, not whether completed code is correct.
- Ordinary reporting path: Main model's plan, proposed tool request and ordinary session context.
- Complementary access path: Independent reviewer private agent with provenance-preserving transcript and read-only compute/history inspection against local evidence.
- Independence boundary: Separate agent system/database, private identities and tools; reviewer cannot mutate the main agent's workspace; candidate action cannot approve itself.
- Who acts on findings: PermissionsModule denies or permits the exact action (temporary elevation only for that call), then returns a refusal/execution result to main S1; project operator can inspect the recorded decision.
- Why this is / is not agent-owned: A distinct model actor makes a substantive risk and authorization judgment and the harness enforces it, rather than merely running deterministic ACL checks.
- Evidence: [Auto mode contract](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/README.md#L312-L341), [private independent reviewer ownership](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/auto/AutoModule.ts#L70-L96), [actual private reviewer send](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/auto/AutoModule.ts#L542-L609), [returned allow/deny, one-call elevation](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/permissions/PermissionsModule.ts#L462-L505), [reviewer inspection surface](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/auto/impl/AutoReviewComputeModule.ts#L12-L48).
- Basis: structural
- Confidence: medium
- Caveats: Scope is permission/safety auditing of a proposed operational action, not independent testing of produced code, whole-project S3* audit or a provider-independent second model. Requires configured functional Auto model route; a single reviewed action is the bounded claim.

## S4 — Outside-and-then intelligence

- State: —
- Function: No evidenced separate owner selecting an outside-future adaptation and returning it as a new capability to the whole installed project agent collective.
- Disturbance / variety regulated: External tool APIs, market/task demands and prospective platform changes may require future capability redesign.
- Decisive decision or feedback right: A distinct S4 decision would sense future external conditions, choose platform/project adaptation and enact a durable operating change.
- Decision owner: Task agents can plan current user goals, and operators configure providers; no built-in prospective environmental decision owner is established.
- Supporting / enforcement mechanisms: Persistent goals, model/provider switching, history/compaction, schedules and planned future module designs.
- Closure path: Persisted goals and scheduled messages change task execution but do not close an independent future-organization adaptation judgment.
- Why this is / is not agent-owned: Task continuation, /goal, scheduling and model routing are current operational capabilities; roadmap master-plans are not shipped prospective decision loops.
- Evidence: [durable goal controls](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/README.md#L287-L310), [native provider modes](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/README.md#L152-L188), [scheduled module](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/scheduling/SchedulingModule.ts#L1-L140)
- Basis: structural
- Confidence: medium
- Caveats: A developer can build such a function with tasks or plugins, but this is not a shipped first-party S4 closure.

### Absence scope

- Surfaces inspected: Agent sessions, native goal/scheduling, model routing, future master-plans, skills and project settings.
- Plausible first-party paths checked: Searched for externally distinguished prospective change, independent future adaptation authority and returned durable system capability evolution.
- Why no material first-party path remains: Task continuation, /goal, scheduling and model routing are current operational capabilities; roadmap master-plans are not shipped prospective decision loops.

## S5 — Policy and identity

- State: —
- Function: Human-chosen permission modes and task goals constrain individual operations, but no explicit ultimate project identity/mandate issue with authoritative return is demonstrated.
- Disturbance / variety regulated: The daemon may execute unsafe tools or need to reconcile differing user or organization demands.
- Decisive decision or feedback right: A legitimate S5 owner would settle a concrete mission/identity or ultimate policy disagreement and return binding system-wide rules into later operations.
- Decision owner: Operator selects session permissions and user goals; the reviewer judges each transient tool request, not ultimate organizational identity.
- Supporting / enforcement mechanisms: Workspace-write/Auto/read-only/full-access policy, session auth, persisted project config, temporary reviewer elevation.
- Closure path: These settings constrain specific calls and sessions, but no independent organization policy issue, ultimate authority decision and returned project mandate is established.
- Why this is / is not agent-owned: Permission selection, security review and account identity checks are not equivalent to S5's ultimate policy/identity reconciliation.
- Evidence: [session permission modes](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/README.md#L312-L348), [per-call denial/elevation](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/packages/happy-agent-modules/sources/permissions/PermissionsModule.ts#L462-L505), [task goal controls](https://github.com/slopus/happy-agent/blob/bd2bd009c30ca7202f793bd9189ecadc495aeae7/README.md#L302-L310)
- Basis: structural
- Confidence: medium
- Caveats: No claim that Happy as a broader company lacks policy governance; company-level identity is outside this installed agent-cell recursion.

### Absence scope

- Surfaces inspected: Permission and team modules, human/auto review, persistent tasks, project config and authenticated clients.
- Plausible first-party paths checked: Sought a first-party ultimate mission/identity conflict, legitimate deciding authority and binding return over all S1 activities.
- Why no material first-party path remains: Permission selection, security review and account identity checks are not equivalent to S5's ultimate policy/identity reconciliation.

## Distributed OSS parent arrangement

The open-source maintainers and Happy desktop/cloud products are distinct from the installed task-agent runtime. Their release choices cannot be borrowed as the deployed project's S5. Parent S3 here is a legitimately authorized operator acting through the shipped daemon API and project views; Auto reviewer provides a narrow separately owned decision over risky actions.

## Self-hosted and non-human modes

Native local model-backed sessions are feasible through configured provider transports. The private Auto reviewer uses the installed model route and read-only compute; when the provider is unavailable the permission request fails closed. Third-party whole agents over ACP are supported but do not grant first-party internal agent autonomy.

## Recursion

At the project level, concurrently running native agents are independent S1 cells, while AgentSystemLocal and modules host persistent work. The Auto reviewer is complementary operational assurance of individual risky tool calls. Inter-peer communication does not alone instantiate a distinct S2 controller; company-level policy belongs to a larger external recursion.

## Variety and escalation

Agent loops react to returned tools and persistent client messages; session permissions gate risky tool calls. The separate model reviewer may challenge authorization and deny a step with feedback; otherwise clients may terminate live work and restore goals. No outside-and-future adaptation or ultimate mandate closure is demonstrated.

## Evidence gaps

The assessment is structural and pinned to the public source revision, without live paid inference or independent second human audit. S3 P depends on project-wide multi-agent views and authorized local API. S3* A covers optional Auto permission scrutiny, not independent final-code testing. Team/cloud and future roadmap artifacts are excluded unless wired to a standard first-party deployed mode.
