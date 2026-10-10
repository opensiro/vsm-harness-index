---
harness_id: orgtree
project_name: Orgtree
repository: https://github.com/Maurdekye/orgtree
review_ref: 0008ccb94edfb986396c49ced3e2d2c885e1fb16
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Orgtree

## Review boundary

- System in focus: one locally installed Orgtree V2 desktop engine and user-created organization, including first-party persistent agent hierarchy, charters, model/provider launches, shared docket, mail/audiences, staffing actions, scoped resource reservations and optional designated model-driven coordinator.
- Purpose and identity: perform ongoing coding/investigation through a persistent team of hosted model-driven working agents with explicit human-created roles, task responsibilities, delegation and corrective staffing.
- Relevant environment: user projects and repositories, external CLI/model providers (Claude Code, Codex, Antigravity, OpenRouter), tool/file permissions, human owner, Git integration resources and local desktop state.
- Standard-distribution boundary: packaged Electron desktop/Python engine and shipped agent-facing MCP/docket/staffing/reservation operations; external model inference, proprietary provider tool loops and standalone companion mailhub are adjacent dependencies, not credited as Orgtree authorship.
- Credited operating / distribution surfaces: `engine/backend/orgtree/{supervisor,api,store,ledger,mcptool,reservations,openrouter_harness}.py`, bundled coordinator charter and installer-supported agent/user UI.
- Adjacent first-party surfaces excluded from ownership: V1 importer, developer/test/benchmark/release tools, unshipped features and companion runtime internals; generic sample review charter alone does not satisfy S3* without a bound enacted review loop.
- First-party operating / deployment modes considered: Windows V2 desktop with hired model-driven providers, persistent agent roles and org hierarchy; multi-worker org with reservation/docket tool access; optional designated coordinator using bundled charter and atomic staffing tools; human operator charter/access configuration.
- Recursion level: one user-created organization and its managed live agents; independent users' orgs and OSS maintainer organization are different systems.
- Reviewed revision: `0008ccb94edfb986396c49ced3e2d2c885e1fb16`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Orgtree's installed V2 desktop bundles a persistent Python engine and local organization store. Hired model-backed agents run using supported external provider CLIs or OpenRouter adapter, while first-party nodes maintain charter, parent/child authority, delegated tool/folder grants, history, messages and shared docket items. Hiring/staffing actions are exposed as first-party callable agent tools, including atomic `orgtree_staff` which creates a task, seats a worker and assigns ownership before notification/wake.

A separate scoped resource-reservation subsystem records exclusive `resource` and commit candidate/base claims under the org document lock. Attempts to acquire an already held live resource by another actor are explicitly refused, including when a competing candidate/base is supplied; liveness/heartbeat safeguards prevent unsafe lease stealing. This is a real concurrency-specific constructor beyond simple mail or task listing. The bundled coordinator charter provides an optional model-owned whole-current staffing mode based on docket, org tree, worker status and returned evidence; it does not become active merely by calling a node 'coordinator'. Review charter guidance is not automatically a bound independent audit.

Sources: [README.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md); [mcptool.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/mcptool.py); [api.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/api.py); [store.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/store.py); [ledger.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/ledger.py); [reservations.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/reservations.py); [coordinator.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md); [openrouter_harness.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/openrouter_harness.py); [supervisor.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/supervisor.py).

## Operational model

Independent provider-backed coding agents are real operational S1 units. The first-party organization engine mediates permissions, delegation, mutual resource claims, durable task ownership and hierarchical communications. An optional hired coordinator uses the same agent model to decide present staffing and work allocation across the subordinate organization. External Claude/Codex inference is an explicit implementation dependency, not a source of unearned S3*/S4/S5.

## S1 — Operations

- State: A
- Function: execute bounded coding/investigation tasks through separately instantiated provider-backed autonomous working agents, supported by Orgtree persistent organizations and tooling.
- Disturbance / variety regulated: evolving user tasks, codebase complexity, failing tests, external model/tool feedback and revised instructions.
- Decisive decision or feedback right: each hired model-driven agent chooses steps and code/tool activity within its charter, provider and granted scope.
- Decision owner: selected Claude/Codex/OpenRouter-model agent actor hosted by Orgtree; private provider cognition is an external implementation, not Orgtree-authored organizational logic.
- Supporting / enforcement mechanisms: persistent agent nodes, charters, provider adapters and session runners, tool/folder grants, CLI/MCP tools and queued conversation.
- Closure path: user/coordinator supplies job and charter → model-driven agent starts under configured provider → model makes work/tool decisions against repo/task feedback → changes/response reach retained transcript and docket → next local agent step reflects updated context.
- Boundary reachability: the Windows packaged engine + desktop explicitly creates agents, starts their model turns and offers first-party OpenRouter/provider adapters; not a development-only agent.
- Why this is / is not agent-owned: without the model-driven actor Orgtree has no comparable discretionary task-solving capability; retaining a chart and provider launch without inference only transports work.
- Evidence: [README.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md); [supervisor.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/supervisor.py); [openrouter_harness.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/openrouter_harness.py); [openrouter.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/openrouter.py); [providers.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/providers.py); [mcptool.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/mcptool.py)
- Basis: explicit + structural.
- Confidence: high for assembled installed provider mode.
- Caveats: OpenRouter model inference and external coding-agent internal tool execution are third-party; Orgtree's own persistent control wiring is the credited harness boundary.

## S2 — Coordination

- State: C
- Function: attenuate conflicting resource ownership by separate operating agents attempting concurrent work or integration.
- Disturbance / variety regulated: two active workers may try to land incompatible changes or mutate the same shared resource/candidate/base under separate responsibilities.
- Decisive decision or feedback right: grant one held reservation and refuse a competing claimant while live owner/heartbeat exists, with scoped recovery only after staleness proof.
- Decision owner: deterministic first-party resource reservation handler; workers/coordinator select target resources but the conflict gate is constructor-enforced, not autonomously resolved.
- Supporting / enforcement mechanisms: persistent reservation rows under document lock, resource key, candidate/base pairing, owner identity, lease/heartbeat, error projection of holder, renewal/release/land.
- Closure path: agent A acquires scoped shared resource → agent B requests same resource with incompatible ownership → first-party `ReservationError` names still-live holder and refuses B → B must defer/reconcile work, preventing duplicate land → release/recovery makes resource available for subsequent work.
- Boundary reachability: reservation module is in shipped Python engine's org document/API control path and is described as runtime durable scoped resource reservations, with standard agent-facing coordination tools.
- Why this is / is not agent-owned: the decisive arbitration is deterministic; there is no independent agent choosing winners. This is S2=C for a specific inter-worker collision, not generic organization-chart messaging.
- Distinct S1 units: two independently hired provider-backed coding-agent nodes working toward commits against one shared repository/integration resource.
- Inter-S1 disturbance: simultaneous integrations or mutable resource claims create conflicting ownership and duplicate/stale actions.
- Attenuating coordination relation: `reservations.execute(action=acquire)` checks active holder, normalized resource and scope, denies different live claimant unless holder actually ceased; lease alone never steals live claim.
- Feedback into subsequent S1 behaviour: refusal returns holder/resource and reason to calling agent, so it defers or selects other work; only a valid held actor can perform related mutation/landing.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a concrete inter-S1 exclusive-resource conflict is damped at admission rather than relying on ordinary mail, hierarchical titles, queue ordering, or shared storage.
- Evidence: [reservations.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/reservations.py); [api.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/api.py); [ledger.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/ledger.py); [mcptool.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/mcptool.py); [README.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md)
- Basis: structural + explicit.
- Confidence: medium-high for scoped reservation mode.
- Caveats: reservation metadata does not itself sandbox files, and overlap query is advisory for declared paths; credit is restricted to exclusive *resource* ownership arbitration.

## S3 — Inside-and-now control

- State: A
- Function: whole-current organization control by a designated persistent coordinator agent managing job assignment, staffing, review gates and blocked work across subordinate agent units.
- Disturbance / variety regulated: duplicate staffing, missing/blocked assignments, forgotten post-compaction decisions and unattended review/implementation tasks across active workers.
- Decisive decision or feedback right: the configured coordinator model selects whether to create/assign/reassign docket tasks, hire staff with work, inspect subordinate evidence, or escalate disputed facts to user.
- Decision owner: an explicitly hired model-backed coordinator in the supported first-party preset/agent-management mode; neither static org hierarchy nor credit checks autonomously owns these choices.
- Supporting / enforcement mechanisms: bundled coordinator charter, first-party `orgtree_staff`, `orgtree_work`, hire/rehire, task ownership notifications, direct chat/mail, active org/docket state and transcript view.
- Closure path: coordinator sees user request and persistent docket/agent/tree state → interprets workload/ownership/report evidence → decides which unit should perform/review work → first-party staffing/assignment API writes owner and delivers wake instruction → worker's next agent turn executes and returns progress/evidence.
- Boundary reachability: README explicitly supports a human hiring a coordinator and bundled charter presets; live agent-facing `orgtree_staff` tool performs atomic seat+work assignment, and associated hire/work operations are in the packaged engine.
- Why this is / is not agent-owned: the coordinator model exercises discretion over present organizational allocations; removing it leaves only human input and deterministic staffing APIs, not equivalent automated current control.
- Whole-system current view: coordinator can inspect the parent org tree and its own subordinates, shared docket, messages, transcripts and status/evidence; the charter directs it to check for already running work before staffing.
- Current-control decision scope: decide who owns each new feature/investigation, when a review is required, who responds to a blocked specialist, and when to retain/retire agent seats.
- Evidence: [README.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md); [coordinator.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md); [mcptool.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/mcptool.py); [api.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/api.py); [ledger.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/ledger.py); [supervisor.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/supervisor.py)
- Basis: explicit + structural.
- Confidence: medium-high in supported coordinator operating mode.
- Caveats: the coordinator is optional and must be hired/chartered; a passive org chart and basic hierarchy alone do not yield S3=A, and no credit is given to a private provider team manager.

## S3* — Complementary audit

- State: ?
- Function: independent challenge of ordinary operational/implementation reports with direct evidence and corrective feedback.
- Disturbance / variety regulated: implementation claims that misstate source changes, tests or production behavior.
- Decisive decision or feedback right: the review-workflow charter proposes distinct redteam reviewer roles and coordinator approval, but a guaranteed separately instantiated independent audit-and-return closure is not shown for all supported organizations.
- Decision owner: undetermined for first-party enacted S3*; optional model reviewer would own judgment only if explicitly hired, given direct evidence, and returned findings alter later work.
- Supporting / enforcement mechanisms: review charter preset, code/test evidence, docket review items, transcript/file inspection and work-evidence git provenance.
- Closure path: a reviewer may inspect implementation and report findings; actual invocation, independence of reviewer from implementer and mandatory correction/acceptance loop remain mode-dependent and were not reconstructed to publication threshold.
- Boundary reachability: review charter and tooling ship, but user-selected workflow alone does not prove operational closure in current assessment boundary.
- Why this is / is not agent-owned: a role label or proposed review checklist cannot substitute for an evidenced independent, different decision owner and a corrective return.
- Claim being audited: agent implementing a feature has delivered correct code.
- Ordinary reporting path: implementer conversation, docket progress and claimed completion.
- Complementary access path: reviewer direct source/commit/test inspection and runtime work-evidence tools are possible.
- Independence boundary: role separation is configurable rather than guaranteed; no canonical independent audit workflow bound in all modes.
- Who acts on findings: coordinator/user may require changes, but obligatory first-party return from independent findings is not conclusively established.
- Evidence: [review-workflow.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/review-workflow.md); [coordinator.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md); [workitems.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/workitems.py); [workevidence.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/workevidence.py); [mcptool.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/mcptool.py)
- Basis: explicit + unresolved.
- Confidence: medium in uncertain closure.
- Caveats: do not turn the charter's redteam guidance into positive S3* on documentation alone; retain ?.

## S4 — Outside-and-then intelligence

- State: ?
- Function: prospective monitoring of environmental possibilities with chosen adaptation options that modify future organization capabilities.
- Disturbance / variety regulated: changes in provider models, incoming work and external demands not yet handled by current staffing.
- Decisive decision or feedback right: operator can change providers/accounts/charters; reactive account fallback and persisted history do not show independently owned prospective environment scanning and adaptation choices.
- Decision owner: unresolved.
- Supporting / enforcement mechanisms: persistent agent history, provider availability, account fallback, model selection and handoff.
- Closure path: switch to another account may allow an interrupted turn to finish, but no evidential prospective exploration → future capability-change decision → return into current operations is established.
- Boundary reachability: provider/continuity components ship; positive S4 not inferred from them.
- Why this is / is not agent-owned: resilience/fallback is a reactive resource workaround rather than outside-and-then strategic intelligence.
- External distinction: external model/provider availability changes are observed reactively.
- Future / prospective distinction: no separately evidenced future-option research, beyond current-task orchestration.
- Adaptation option generated: unverified.
- Path back into current capability / S3: no S4-specific returned adaptation established.
- Evidence: [providers.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/providers.py); [accounts.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/accounts.py); [handoff.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/handoff.py); [README.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md)
- Basis: structural + unresolved.
- Confidence: medium in insufficient evidence.
- Caveats: future configured roles might act prospectively, but no such supported first-party loop was proven at this frozen ref.

## S5 — Policy and identity

- State: ?
- Function: decide ultimate purpose and identity of the whole organization when constitutive conflicts arise.
- Disturbance / variety regulated: changes to legitimate goals, final authority and organizational identity rather than ordinary permission/staffing.
- Decisive decision or feedback right: human operator sets charters and capacity/access constraints, but no distinct ultimate-policy issue→authority→returned operation was reconstructed.
- Decision owner: human owner configures charter/permissions and deployment boundaries; distinct S5 ownership unresolved.
- Supporting / enforcement mechanisms: persistent agent identities, charter text, hierarchy, folder/tool grants, capacity and delegation budget, audience request path.
- Closure path: charters and permissions affect later agent execution, but this is normal configuration rather than evidence of an enacted identity-level decision loop.
- Boundary reachability: charter/edit controls are standard shipped mode; no positive S5 based on them.
- Why this is / is not agent-owned: an autonomous coordinator following a founder's charter is not authorized to define or change the organization's ultimate identity by being called 'coordinator'.
- Identity / ultimate-policy issue: not established as a resolved runtime issue.
- Ultimate authority in each claimed mode: no positive S5 parent or autonomous mode demonstrated.
- Return-to-operation path: config reaches agent prompts and enforcement but does not prove whole-purpose adjudication.
- Evidence: [README.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/README.md); [schema.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/schema.py); [mcptool.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/mcptool.py); [api.py](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/backend/orgtree/api.py); [coordinator.md](https://github.com/Maurdekye/orgtree/blob/0008ccb94edfb986396c49ced3e2d2c885e1fb16/engine/docs/charters/coordinator.md)
- Basis: structural + unresolved.
- Confidence: medium in insufficient evidence.
- Caveats: persisted roles and delegated grants are not organizational ultimate identity decisions.

## Distributed OSS parent arrangement

The GitHub project maintainer organization is distinct from a single installed user-created Orgtree team. Provider services and account billing are external suppliers. No broad OSS governance authority is credited to runtime S3–S5.

## Self-hosted and non-human modes

The local engine can stay active after the desktop UI closes and autonomously hosted workers continue work through their provider tool loops. The explicit coordinator operating mode supplies model-owned S3 decisions; if only human-managed workers exist without a coordinator, no S3=A claim applies to that configuration. Human founder approval, grants and charters remain external authority constraints, not autonomous S5.

## Recursion

The focal whole is the organization managed by one Orgtree engine. Worker nodes are local operational agents; coordinator is a metasystem role only when configured and given actual staffing decisions. Higher-level project/enterprise governing bodies are separate recursions.

## Variety and escalation

Work-cell models absorb task complexity; exclusive resource reservations attenuate concurrent integration collisions, while org-owned staffing assigns current work and budget across workers; direct mail, audience escalation and human charter permission setting constrain action but are not independently credited as higher VSM functions without demonstrated closure.

## Evidence gaps

- Confirm live simultaneous reservation conflict and returned loser behavior with two hosted coding agents before extrapolating S2 from source structure to all file conflicts.
- Inspect runtime coordinator with multiple actual worker/docket units before claiming general S3 across unconfigured orgs.
- A review-workflow charter exists, but no automatic independent audit–judgment–correction closure is proven for S3*.
- No prospective S4 sensing/adaptation or identity-level S5 governing dispute was established at the frozen public revision.
- No end-to-end commercial-provider-backed run was conducted; evidence consists of pinned first-party repository implementation and packaged documented modes.
