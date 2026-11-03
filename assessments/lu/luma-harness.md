---
harness_id: luma-harness
project_name: Luma Harness
repository: https://github.com/Gavriel-lab/luma-harness
review_ref: 24dbf80a75a4bce048739bd2f149c5d447569b77
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Luma Harness

## Review boundary

- System in focus: one locally hosted Luma v0.2 desktop/mobile work organization consisting of a human owner, model-driven coordinator role, authoritative host/Broker, configured model-driven Pi or qualified CLI work executors, tickets/plans/attempts, submitted artifact reviews and originating-conversation return.
- Purpose and identity: translate a person's bounded project request into an approved multi-worker plan, genuine scoped artifact production, evidence-based internal review and a separate final human acceptance before declaring project complete.
- Relevant environment: user project goals, file workspaces and tools, authorized participant changes, work dependencies, failing build/test checks, stale/retried attempts, model-provider failures, lost heartbeats, approval changes, restarts and shared desktop/mobile access.
- Standard-distribution boundary: public MIT `apps/desktop/electron/bridgeBroker.cjs`, `bridgeLauncher.cjs`, `dataStore.cjs`, coordinator MCP connector, managed Pi bridge (`apps/desktop/connectors/pi/`), controlled tool/forwarder path, authoritative desktop app and supported mobile-relay contract. Shipped v0.2 Pi execution path has concrete worker code; other third-party CLI adapters are treated as qualification-dependent.
- Credited operating / distribution surfaces: owner-approved collaborative plan version; model-driven coordinator using `xiaowu_workbench` to form/dispatch work and inspect actual artifact evidence; registered worker using a current ContextPacket and restricted tool loop; Broker attempt/heartbeat/report, review decision and corrected resubmission, internal acceptance and user-acceptance handoff.
- Adjacent first-party surfaces excluded from ownership: external OpenAI-compatible model/API service, third-party Pi SDK internal architecture outside the wrapped managed-worker role, other CLI agent internal tool loops, optional Cloudflare Access deployment, private user memory plugins, synthetic UI/model smokes, themes, Luma repository development and host OS security guarantees not supplied by the app.
- First-party deployment/mode reachability: packaged Windows app or public source build with registered coordinator and embedded Pi worker, configured member API Profiles, approved workspace and explicit plan; desktop and mobile share one authoritative host. Real API accounts, CLI versions, physical phone and VPS require separate qualification.
- Recursion level: one Luma installation and its collaborative work ticket/project. Multiple separately registered worker lanes are operational units; a model-driven coordinator runs first-party task control and can separately challenge worker reports. Human owner and provider organizations are external authority/dependency boundaries.
- Frozen source revision: `24dbf80a75a4bce048739bd2f149c5d447569b77` (`codex/public-release`), observed 2026-11-03; Profile 0.2.4 and released Skills assessment Methodology 0.3.7.

## Repository architecture

Luma's authoritative desktop host persists members, conversations, tickets, plans, jobs and reports; mobile is an authenticated client of the same authority, not a second agent organization. The coordinator model is connected through a limited `xiaowu_workbench` MCP that offers snapshot, create/update-plan, dispatch, artifact read, reject-review and accept. Plan creation is not execution: the human must approve an exact plan version before dependency-based dispatch. A registered Pi Bridge worker claims a current Broker attempt, receives an authority-built ContextPacket, performs model-driven read/write/edit/run calls only within an approved workspace and reports actual artifact paths, checks and unknowns. The Broker holds stale attempts, orders events, persists current state and rejects unauthorized/wrong-version changes. On submission, a separate model-driven coordinator can inspect evidence and issue internal acceptance or explicit return for repair; complete collaborative projects still wait for the human's final acceptance. The automated background reviewer can also run on report summary/check fields, but **that report-only subpath is not, by itself, independent artifact verification**. Positive S3* evidence is bounded to a configured coordinator that invokes the shipped artifact-reading tool and challenges the actual worker result. Persistence/recovery avoids treating a lost connection as completed work.

Pinned first-party evidence:

- [README: public v0.2 operating path and explicit qualification limits](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/README.en.md)
- [Architecture: authority, plan approval, attempt/review/return and mobile identity](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/docs/ARCHITECTURE.md)
- [Embedded Pi mode: real tools, authorization, coordinator review and human completion](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/docs/PI.md)
- [Verification: controlled worker/model tests versus unverified real accounts](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/docs/VERIFICATION.md)
- [Work Broker: plan approval, attempts, coordinator review and artifact access](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/apps/desktop/electron/bridgeBroker.cjs)
- [Coordinator MCP tool with exact ticket/attempt decisions and artifact reads](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/apps/desktop/connectors/coordinator.mjs)
- [Coordinator prompt requires reading actual artifacts before acceptance](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/examples/coordinator-prompt.md)
- [Pi worker claim/context/heartbeat/report execution loop](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/apps/desktop/connectors/pi/worker.mjs)
- [Pi model/tool runner](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/apps/desktop/connectors/pi/runner.mjs)
- [Pi controlled-path and tool restrictions](https://github.com/Gavriel-lab/luma-harness/blob/24dbf80a75a4bce048739bd2f149c5d447569b77/apps/desktop/connectors/pi/controlled-tools.mjs)

## Operational model

The owner authorizes the work plan and workspace. A first-party-instructed coordinator model determines present task decomposition/assignments, calls the bounded Broker and interprets current artifact/review evidence. A separate managed worker model chooses substantive work steps inside the authorized workspace through the embedded Pi model/tool interface. The Broker owns permission checks, scoped attempts, idempotency, snapshot context, revision and return states, not the model's substantive choices. A model-driven coordinator can act as a distinct reviewer of a worker artifact where it uses `artifact` to inspect source independently of the implementer's summary; a summary-only automatic review does not meet that same evidence standard. The release's synthetic tests establish transport/contract behavior, not observed correctness from every configured model.

## S1 — Operations

- State: A
- Function: autonomously perform a scoped work ticket's substantive file edits, project commands, test checks and deliverable/report production under the approved human workspace and acceptance criteria.
- Disturbance / variety regulated: ambiguous implementation details, variable source files, compilation/test failures, path-specific edits and unexpected allowed tool outputs.
- Decisive decision or feedback right: decide concrete code/text modifications, permitted read/write/edit/run tool sequence, retry behavior and honest report of tests, artifacts and remaining unknowns.
- Decision owner: the registered first-party-managed Pi worker model in `PiRunner` and `runPiBridge`, backed by the configured member's external model API. Luma controls the invocation/permission boundary; the unwrapped external Pi SDK is not credited with unrelated higher functions.
- Supporting / enforcement mechanisms: per-member API Profile, host model forwarder, authorized ContextPacket, short-lived Broker token, `validateControlledPath`, restricted tools and project command runner, event ordering, heartbeat/attempt lineage and staged delivery.
- Closure path: approved task/dispatch → Pi worker claims unique attempt and obtains current context → model chooses allowed changes/commands → workspace/test feedback → submitted artifact paths/checks/unknowns → rejection for repair or controlled acceptance.
- Boundary reachability: `apps/desktop/connectors/pi/worker.mjs`, `runner.mjs` and `controlled-tools.mjs` are shipped local executor paths and connected to current Broker authority. `docs/PI.md` explicitly distinguishes real read/write/test from API-only chat.
- Why this is / is not agent-owned: without the model-driven execution loop, Broker/permissions can accept only submissions and enforce scope, not choose task-specific edits or error corrections.
- Evidence: pinned `docs/PI.md`, `apps/desktop/connectors/pi/worker.mjs`, `runner.mjs`, `controlled-tools.mjs`, `bridgeBroker.cjs`.
- Basis: explicit + structural.
- Confidence: medium-high for embedded Pi mode and first-party wiring, bounded by controlled fixture rather than live model account E2E.
- Caveats: Pi project processes run with the host OS user's privileges, **not** an OS sandbox; real provider entitlements and other CLI versions remain independently qualified.

## S2 — Coordination

- State: —
- Function: no distinct implemented lateral conflict attenuation between independent worker operations with returned peer-behavior feedback is sufficiently established.
- Disturbance / variety regulated: multiple workers and dependencies coexist, and a second attempt can be stale, but no demonstrated runtime resolution of two independent worker edits/claims against the same contested file/resource is specified.
- Decisive decision or feedback right: Broker deduplicates requests, invalidates stale attempts, enforces one member's current job/identity and sequences task dependencies; these are vertical task custody and S3 management, not an independent S2 policy/right for cross-worker disturbances.
- Decision owner: constructor-authored Broker identity/attempt/dispatch predicates, not an autonomous peer coordination role.
- Supporting / enforcement mechanisms: attempt/job/request IDs, stale-attempt rejection, registered member binding, dependency-based dispatch, stored task status, ContextPacket permissions and revision handling.
- Closure path: duplicate or outdated report/claim → Broker returns stale/conflict error or blocks wrong-version promotion → legitimate current attempt proceeds; no specific peer-pair source-write collision and returned inter-S1 remedy was evidenced.
- Why this is / is not agent-owned: keeping attempt state consistent is real but chiefly current-task custody; neither message routing nor task ordering alone is enough to claim S2 closure.
- Distinct S1 units: separately registered Pi or CLI workers assigned to independently scoped tickets/tasks under one approved project.
- Inter-S1 disturbance: possible shared-folder edit collisions or conflicting dependency assumptions; shipped sources do not demonstrate systematic detection and resolution between these distinct workers.
- Attenuating coordination relation: bounded task/attempt ownership and current-context protection; useful guards, but not source-supported lateral worker interference management.
- Feedback into subsequent S1 behaviour: stale attempts are refused; this affects replacement attempts, not established peer workers negotiating or avoiding a particular cross-S1 collision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: no S2-specific evidence survives the distinction, so positive S2 is withheld.
- Evidence: pinned `docs/ARCHITECTURE.md`, `apps/desktop/electron/bridgeBroker.cjs`, `apps/desktop/connectors/pi/worker.mjs`.
- Basis: bounded absence.
- Confidence: medium-high for inspected standard work path.
- Caveats: a custom executor or human-specified workspace partition could prevent collisions; those arrangements are not shown to be a standard Luma-owned S2 feedback mechanism.

### Absence scope

- Surfaces inspected: Broker claim/report/attempt identity and replay rules, dependency scheduler, coordinator workbench, Pi workspace tools and approval/revision transition paths.
- Plausible first-party paths checked: duplicate request dedup as peer arbitration, stale-attempt return as S2, dependency-based dispatch as mutual coordination, ContextPacket per-worker scope as S2 and chat/relay message routing.
- Why no material first-party path remains: each path protects authorization and vertical state/ordering without evidenced case-specific collision detection and corrective return among separate concurrent S1 workers.

## S3 — Inside-and-now control

- State: A
- Function: a model-driven coordinator controls current ticket decomposition, assignment, review/rework and work-state changes under a user-approved plan version.
- Disturbance / variety regulated: changing work dependencies, failed worker attempts, insufficient acceptance evidence, delayed or lost executor heartbeats, partial plan revisions and stale reports across current tasks.
- Decisive decision or feedback right: inspect authoritative workbench, propose concrete scoped tasks and owners, invoke `create-ticket`/`update-plan`, connect or dispatch approved work, reject an exact report with reasons, or internally accept after review; decide what a returned failure requires within authorized project scope.
- Decision owner: configured first-party `agent_coordinator` model using Luma's bounded MCP capability, while only the human owner can approve plan versions or grant final project acceptance. The Broker's static gate conditions remain constructor C support.
- Supporting / enforcement mechanisms: `xiaowu_workbench` MCP, current snapshot, project-plan version, assignee constraints, `scheduleCoordinatorWork`, Broker mutations, attempt lineage, review/correction records and originating-conversation handoff.
- Closure path: owner request / current snapshot → coordinator model selects plan, tasks, workers and corrective steps → user plan approval if required → Broker dispatch/worker execution → reports, artifacts, failures and reviews return → coordinator adjusts current work or returns exact findings, then escalates final approval to user.
- Boundary reachability: `apps/desktop/connectors/coordinator.mjs` is a shipped model-facing tool; `docs/PI.md` and `docs/ARCHITECTURE.md` describe configured coordinator with actual workbench access; Broker authorizes the same endpoints. `examples/coordinator-prompt.md` supplies a supported coordinator role.
- Why this is / is not agent-owned: coordinator model selects substantive decomposition and response to results through first-party-authorized tools. Broker validation is not the sole control decider, but neither can the model waive human plan/final acceptance.
- Whole-system current view: approved project/plan revision, registered workers, task dependencies and statuses, active job/attempts, review reports, artifacts/checks, cancellations, rework and conversation-return status.
- Current-control decision scope: present project execution, worker assignment and evidence-driven return; not future company portfolio strategy or constitutional identity.
- Evidence: pinned `apps/desktop/connectors/coordinator.mjs`, `apps/desktop/electron/bridgeBroker.cjs`, `docs/PI.md`, `docs/ARCHITECTURE.md`, `examples/coordinator-prompt.md`.
- Basis: explicit + structural.
- Confidence: medium-high for configured model coordinator and shipped current-control path.
- Caveats: an API Profile that merely chats without an enabled coordinator/worker connection is not this supported S3=A mode. User approval requirements remain hard gates; controlled test fixtures do not measure autonomous model performance.

## S3* — Complementary audit

- State: A
- Function: separately from the implementing worker, a configured coordinator model challenges a submitted attempt against actual on-disk deliverables and acceptance checks, returning a concrete reject/repair verdict before internal acceptance.
- Disturbance / variety regulated: worker self-report that overstates completion, omitted/incorrect artifacts, missing test evidence and incomplete task acceptance.
- Decisive decision or feedback right: call `artifact` on a submitted job/path, compare its contents and reported checks with task acceptance, and issue a binding `reject-review` with reason against exact attempt/report identifiers or internally `accept` if supported.
- Decision owner: an independently invoked coordinator model/reviewer role (`agent_coordinator`), distinct from the registered Pi worker and from its output generation; Broker validates target identity and enforces review decision.
- Supporting / enforcement mechanisms: coordinator workbench `snapshot`/`artifact`/`reject-review`/`accept`, read of approved artifact path via Broker, report/check/unknown metadata, exact attempt+report ID, preserved rejected evidence and repair/redispatch, final human acceptance.
- Closure path: worker submits report and actual artifact → current ticket enters review → distinct coordinator accesses the submitted artifact itself and acceptance evidence → model challenges/accepts or rejects exact report with reasons → Broker returns rejected work for correction and keeps old evidence; eventual positive review still awaits human final completion.
- Boundary reachability: the shipped coordinator MCP exposes `artifact` for authorized submitted text files, plus `reject-review` and `accept`; README/architecture/PI and `examples/coordinator-prompt.md` require the coordinator to examine actual artifacts and checks before acceptance. This is a **conditional configured coordinator mode** with actual tool use.
- Why this is / is not agent-owned: a different model-driven actor can inspect substantive file evidence and formulate case-specific negative findings; deterministic report-format checks or a purely summary-based verifier are not the source of the positive claim.
- Claim being audited: a particular Pi/CLI worker's submitted deliverables meet task acceptance criteria.
- Ordinary reporting path: implementing worker's summary, checks/unknowns and artifact list submitted via `report`.
- Complementary access path: coordinator `artifact` reads up to 16 KB of the actual allowlisted text file inside the authorized workspace, rather than taking only the summary as proof; additional task/check context comes from authoritative snapshot.
- Independence boundary: reviewer role and invocation are separate from worker, but it can use the same underlying model service and has only bounded artifact access; this is role/evidence-path independence, not guaranteed independent provider/human audit.
- Who acts on findings: Broker checks exact current job/attempt/report and returns rejected task for repair, preserving prior evidence; accepted work advances to pending final human acceptance.
- Evidence: pinned `apps/desktop/connectors/coordinator.mjs`, `apps/desktop/electron/bridgeBroker.cjs` (`artifact`, `rejectReview`, `attachCoordinatorReviewer`), `examples/coordinator-prompt.md`, `docs/PI.md`.
- Basis: explicit + structural.
- Confidence: medium; auditor evidence access is supported but configuration/actual invocation dependent.
- Caveats: the automatically spawned background coordinator review prompt currently provides report summary, check list and artifact **names**, not proof that it read the underlying files. **Report-only automatic review by itself does not justify S3*=A**. This positive ownership applies only to the separately supported model coordinator mode that actually calls `artifact`; if that path is absent in a deployment the score must be narrowed. Synthetic tests do not prove empirical reviewer independence.

## S4 — Outside-and-then intelligence

- State: —
- Function: no closed first-party future-capability or external-environment adaptation function beyond current request/plan handling was demonstrated.
- Disturbance / variety regulated: new owner goals, past conversation memory and proactive/diary features are contextual inputs or auxiliary product modes rather than supported anticipation of how Luma's organizational capability must change.
- Decisive decision or feedback right: coordinator chooses present plan revisions within approved project scope, and humans can change member/API configuration; no prospectively accountable S4 actor updates the harness's long-term operating repertoire.
- Decision owner: external user/maintainer for future mission and model/provider choices, with current coordinator for bounded work steps.
- Supporting / enforcement mechanisms: saved history and optional private memory, activity schedules, revision logic, dynamic task creation, development roadmap/docs.
- Closure path: new/changed task → current draft or amendment → user approval and execution; no first-party model of an outside future environment → capability proposal → authorized changed future organization state is demonstrated.
- Why this is / is not agent-owned: a model revising a project plan after errors is present-work S3, not itself a future-facing S4 adaptation mandate.
- Evidence: pinned `docs/ARCHITECTURE.md`, `docs/PI.md`, `apps/desktop/electron/bridgeBroker.cjs`, README.
- Basis: bounded absence.
- Confidence: medium-high.
- Caveats: a human team using Luma could run an S4 practice with it, or optional memory plugins could learn; neither is borrowed into core first-party operating ownership.

### Absence scope

- Surfaces inspected: coordinator plan/scope revision, memory and diary references, workbench contract, authority persistence, scheduling and public release/verification documents.
- Plausible first-party paths checked: autonomous coordinator replanning as strategy, retained memory as future-environment learning, owner model/API configuration as capability adaptation, release roadmap as a runtime S4.
- Why no material first-party path remains: these support bounded active project revisions or external customization and do not include the necessary prospective environment assessment and durable internal capability decision/feedback loop.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/policy adjudication loop for the Luma work organization was found.
- Disturbance / variety regulated: owner identity, member-role configuration, plan approval, final acceptance and workspace/API access are fixed or changed through human settings and constructor checks, not deliberated as constitutional organizational policy by an internal S5 actor.
- Decisive decision or feedback right: only the human user may approve collaborative plans and finally accept the project; coordinator/model tokens are explicitly rejected for those endpoints.
- Decision owner: external owner for defining identity/mission and final authorization; static Broker/host permission code for enforcement.
- Supporting / enforcement mechanisms: persistent `agent_owner` versus `agent_coordinator` identities, authority mutation channel, explicit plan-version approval, final user-accept route, protected profiles/context, current grants and no chat-based privilege escalation.
- Closure path: human project/permission decision → verified host/Broker state → bounded execution → final human acceptance; there is no ultimate identity/policy dispute internally adjudicated and returned as a new legitimate standing policy.
- Why this is / is not agent-owned: a review/plan gate and coordinator leadership are real S3 controls but not autonomous S5 ultimate-identity governance; even strongly enforced role identity is not a deliberative policy function.
- Evidence: pinned `docs/ARCHITECTURE.md`, `docs/PI.md`, `apps/desktop/electron/bridgeBroker.cjs`, `apps/desktop/connectors/coordinator.mjs`.
- Basis: bounded absence.
- Confidence: high for explicit user-gated policy boundary.
- Caveats: a real owner organization may independently govern an OpenSiro-style policy plane outside Luma; this assessment does not credit it to the executable public harness.

### Absence scope

- Surfaces inspected: human plan approval, final acceptance, owner/coordinator/member identity, protected credential and workspace grants, authority mutations, mobile Access and privacy/safe execution guidance.
- Plausible first-party paths checked: final human approval as an internal S5 return, coordinator deciding task policy as constitutional authority, protocol role IDs as organizational identity evolution and OAuth/Access membership as ultimate policy.
- Why no material first-party path remains: each is external human authorization, fixed constructor safeguard or present project control, with no bounded ultimate mission dispute → legitimate S5 adjudication → authoritative policy return.

## Distributed OSS parent arrangement

Separate users install public Luma with their own API providers, registered members, workspaces and optional remote/mobile infrastructure. The owner identity inside each host and project's GitHub maintainers do not constitute a shared parent S5 across OSS installations. Hosted Cloudflare services forward authenticated operations but do not govern a second organizational recursion or confer additional model authority.

## Recursion

The assessed recursion is a human-authorized Luma project in one authoritative host. Distinct model-driven workers execute S1 tasks, the model-driven coordinator holds current project S3 rights, and a distinct coordinator reviewer mode can challenge worker artifacts (S3*) where direct evidence access is used. No independently closed inter-worker S2 or S4/S5 policy loop is imported from model SDK/provider or adjacent cloud services.

## Variety and escalation

Approved plans and bounded ContextPackets attenuate task ambiguity and permission risk, while model-driven Pi workers handle source/test variety. Broker lineage, stale attempt controls and persistent status keep current work from being silently duplicated, and coordinator actions replan/dispatch/reject or accept under human-approved constraints. In the evidence-inspecting reviewer mode, a separate model challenges actual artifacts and returns correction. Uncertain interruption and final project completion escalate to the owner; source delivery and report-only background review are not automatically independent auditing.

## Evidence gaps

- Frozen source, published docs and first-party controlled-fixture tests were inspected; no configured real provider API, external CLI login, physical phone or live deployment was exercised here.
- Public `docs/VERIFICATION.md` reports Windows synthetic/controlled executor and packaged Pi bridge checks; these are code-path evidence, not validation of arbitrary model reasoning/credential/OS combinations.
- Embedded Pi tools constrain allowed paths but execute project Node code with host OS-user privileges, not a separate OS sandbox.
- S3*=A specifically requires the configured independent coordinator to read actual submitted artifact content via the provided `artifact` operation. The default automatic background review prompt is report-oriented, and a summary-only pass would not satisfy the claimed complementary evidence path.
- Broker attempt de-duplication and dependency scheduling were not counted as lateral S2, because no separate S1 worker-write collision arbitration/feedback loop was established.
- No future capability strategy or ultimate S5 policy was inferred from user approval, stored memory, role names or optional hosted services.

## Assessment summary

Proposed included for the supported human-approved collaborative execution and evidence-inspecting coordinator mode: **A · — · A · A · — · —**. Managed model-driven Pi workers own S1; the configured coordinator can own project-level current S3 planning/rework, and—only with actual artifact tool reads—a separate challenge to worker evidence supplies S3*. Attempt custody, dispatch ordering, human final authority and report-only auto review do not independently supply S2/S4/S5 or universal audit independence.
