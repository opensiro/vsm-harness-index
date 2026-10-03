---
harness_id: clawmanager
project_name: ClawManager
repository: https://github.com/Yuan-lab-LLM/ClawManager
review_ref: 576e4bb5440d453fd25300586e57ce81cb616f31
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# ClawManager

## Review boundary

- System in focus: the first-party ClawManager Team organization at frozen revision `576e4bb5440d453fd25300586e57ce81cb616f31`, including Team creation/templates, platform-owned Leader/Worker role contracts, Team Redis/event protocol, workflow ledger, work assignments/revisions, review gates, recovery monitor, shared artifacts and final-synthesis closure. Generic managed-runtime lifecycle and AI Gateway/security surfaces are considered where they support this Team mode.
- Purpose and identity: convert a user Team goal into coordinated multi-agent work whose roles, delegation protocol, dependencies, validation contracts, recovery and final completion are defined and closed by ClawManager.
- Relevant environment: user goals, Team member outputs, shared artifacts, dependency state, runtime/tool failures, review evidence, managed OpenClaw/Hermes execution, AI Gateway/model availability, and operator/platform constraints.
- Standard-distribution boundary: ClawManager's Team service, compiled Team role prompts/personas, Team protocol/ledger, Redis bus, shared Team workspace, review contracts and runtime integration are inside. OpenClaw/Hermes inference/tool internals remain external dependencies; ClawManager receives credit only for organizational roles and feedback paths its shipped Team mode defines and closes.
- Credited operating / distribution surfaces: `README.md`; `docs/team-workspaces-guide_en.md`; `backend/internal/services/team_service.go`; Team models/migrations; custom Team template compilation and tests; managed Team runtime injection.
- Adjacent first-party surfaces excluded from ownership: ordinary single-instance lifecycle/admin operations; repository CI/tests as actors; standalone Security Protection/AI Gateway administration where no Team decision loop is involved; external OpenClaw/Hermes internal organizations beyond the ClawManager-injected Team role.
- First-party operating / deployment modes considered: built-in and custom Team workspaces; Leader-mediated collaboration; OpenClaw Lite Leader; OpenClaw/Hermes Lite Workers; structured plans/assignments; dependency and revision tracking; review-required validation assignments; Monitor-triggered recovery; Leader final synthesis.
- Recursion level: one ClawManager Team is the focal organization. Team Workers are S1 units; the Team Leader is the metasystemic coordinating/current-control actor. OpenClaw/Hermes runtime internals below each injected Team role are lower-level/external.
- Reviewed revision: `576e4bb5440d453fd25300586e57ce81cb616f31`.
- Observation date: 2026-10-04.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

ClawManager's standard Team mode is more than a runtime launcher. The product provisions one Leader and multiple Workers, compiles platform-owned role/system prompts, injects a stable Team runtime contract, maintains a durable Team workflow ledger, routes assignments and results through the Team bus, tracks dependencies/revisions/review targets, and accepts root completion only through the Leader's final synthesis.

The first-party Leader contract explicitly names the Leader an “orchestration controller,” instructs it to decompose goals, assign work, coordinate dependencies, reconcile member results and verification, manage recovery, and publish the final answer. These rules are platform-owned and deliberately immutable even when a user generates a custom Team role overlay. Worker roles receive task-scoped identity, collaboration and artifact contracts through the same first-party injection path.

The backend does not merely trust natural-language completion claims. Assignment identity/revision, dependency state, review-required flags, validation target assignment/revision, workflow phases and root-completion state are persisted. A Worker completion closes only that assignment. The Leader may close the root only after required current assignments/reviews are complete and the workflow is sealed; failed/stale work requires a structured recovery or Leader waiver.

Primary evidence:

- [`README.md`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/README.md)
- [`docs/team-workspaces-guide_en.md`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/docs/team-workspaces-guide_en.md)
- [`backend/internal/services/team_service.go`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/services/team_service.go)
- [`backend/internal/services/team_custom_role_profile_test.go`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/services/team_custom_role_profile_test.go)
- [`backend/internal/db/migrations/035_harden_team_event_protocol.sql`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/db/migrations/035_harden_team_event_protocol.sql)
- [`backend/internal/db/migrations/037_add_team_workflow_ledger.sql`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/db/migrations/037_add_team_workflow_ledger.sql)
- [`backend/internal/db/migrations/042_add_team_review_contract.sql`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/db/migrations/042_add_team_review_contract.sql)

## Operational model

A user gives a goal to the Team Leader. The Leader reads the first-party Team roster/context, creates a plan, assigns bounded work to Workers, observes returned events/artifacts, coordinates dependencies and recovery, explicitly assigns validation where required, reconciles those results, and finally publishes the Team synthesis. ClawManager transports and persists the organizational conversation, enforces immutable assignment/review contracts, and prevents a Worker result from becoming a root completion without the Leader's closing decision.

## S1 — Operations

- State: A
- Function: perform bounded Team work that contributes a concrete artifact, analysis, implementation, test/review result or other assigned deliverable to the Team goal.
- Disturbance / variety regulated: heterogeneous user goals, member-specific domain work, shared evidence/artifacts, tool/repository state, runtime observations and assignment-specific acceptance criteria.
- Decisive decision or feedback right: a model-backed Team member interprets its ClawManager-issued role/assignment against live evidence, chooses semantic actions/tools, and returns a structured result/artifact that advances its assignment.
- Decision owner: the model-backed Worker (or Leader for a directly handled self-contained operation) operating under ClawManager's first-party compiled Team role and runtime contract.
- Supporting / enforcement mechanisms: generated SOUL/AGENTS/system prompts; Team roster; shared workspace; Team tools; runtime adapters; assignment identity/revision; event bus; artifact paths.
- Closure path: Leader-issued assignment → ClawManager Team envelope/role contract → member model/tool loop acts on the assigned environment → member reports result/evidence/artifacts through Team channel → ClawManager records the assignment outcome and exposes it to subsequent Team control.
- Boundary reachability: built-in/custom Team creation provisions the runtime member and injects ClawManager-owned role/system prompts and Team tool contract automatically; downstream users do not need to build the role→assignment→result feedback loop.
- Why this is / is not agent-owned: removing the model-backed Team member while retaining the ledger/bus leaves an assignment record but removes the semantic work decision loop. The operational discretion is therefore agent-owned; external runtime internals are dependencies beneath a first-party ClawManager role.
- Evidence: [`docs/team-workspaces-guide_en.md`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/docs/team-workspaces-guide_en.md); [`backend/internal/services/team_service.go`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/services/team_service.go); [`backend/internal/services/team_custom_role_profile_test.go`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/services/team_custom_role_profile_test.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic managed OpenClaw/Hermes instances outside Team mode are not imported into this S1 claim.

## S2 — Coordination

- State: A
- Function: attenuate cross-member dependency, handoff, duplicate-work and ownership interference among distinct Team Workers.
- Disturbance / variety regulated: multiple Workers can own different assignments whose inputs/outputs depend on one another; premature downstream execution, silent role takeover, stale revisions or ambiguous handoffs can create inconsistent work and duplicated/conflicting effort.
- Decisive decision or feedback right: the Leader decides the Team work decomposition, assignment owners, dependency ordering, handoffs and corrective reassignment, and can revise those choices from returned member/recovery evidence.
- Decision owner: the ClawManager-injected autonomous Team Leader role.
- Supporting / enforcement mechanisms: `team_send`; Team roster; stable assignment/work IDs; dependencies; plan/phase ledger; revision checks; Leader-mediated bus topology; waiting-dependency receipts; ownership-conflict guards.
- Closure path: user/root goal → Leader creates plan and assigns owners/dependencies → ClawManager records/routes assignments → Workers execute/report → Leader reconciles dependency/result state and issues subsequent handoffs, corrected assignments or recovery actions → later Worker behavior changes under that coordination.
- Boundary reachability: Leader-mediated collaboration is a shipped Team mode, the Leader prompt/protocol is compiled by ClawManager, and the Team bus/ledger supplies the concrete assignment and return channel.
- Why this is / is not agent-owned: deterministic dependency/revision guards enforce the plan, but the Leader owns the discretionary decomposition, ownership and recovery choices. Removing the Leader leaves guards and queues but not materially the same inter-member coordination judgment.
- Evidence: [`docs/team-workspaces-guide_en.md`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/docs/team-workspaces-guide_en.md); [`backend/internal/services/team_service.go`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/services/team_service.go); [`backend/internal/db/migrations/037_add_team_workflow_ledger.sql`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/db/migrations/037_add_team_workflow_ledger.sql).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Redis transport and dependency fields alone would not establish S2; the positive witness is the first-party Leader decision loop over those concrete cross-S1 disturbances.
- Distinct S1 units: independently assigned Team Workers with separate member identities/roles and assignment outputs.
- Inter-S1 disturbance: dependencies, conflicting/stale assignment ownership, premature downstream execution, duplicated role takeover and incomplete handoffs can make one Worker's behavior invalidate or block another's contribution.
- Attenuating coordination relation: the Leader decomposes work, assigns member owners, declares dependency/revision contracts, coordinates handoffs/recovery and reconciles returned results before the next assignment decisions.
- Feedback into subsequent S1 behaviour: Leader-issued Team assignments/revisions/recovery messages change which Worker acts, what evidence it consumes, when it may proceed and what deliverable/validation contract it must satisfy.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the first-party Leader contract explicitly regulates cross-member dependencies, role boundaries, handoffs and recovery for identifiable interference modes, rather than merely routing independent messages.

## S3 — Inside-and-now control

- State: A
- Function: regulate the Team's current commitments as a whole: plan state, active assignments, recovery, acceptance/waiver and final root-task disposition.
- Disturbance / variety regulated: running/waiting/failed/stale member work, incomplete required phases, review gaps, dependency blockers, ambiguous quiet/stalled attempts and competing current commitments.
- Decisive decision or feedback right: the Leader decides the current plan/assignment structure, whether to wait, recover, reissue/reassign, accept/waive failed/stale required work, proceed to synthesis, or complete/fail the root task.
- Decision owner: the autonomous Team Leader operating under ClawManager's platform-owned orchestration and completion contract.
- Supporting / enforcement mechanisms: workflow states and plan/ledger versions; Team Kanban; member/task events; Monitor diagnostics; required/optional assignment flags; review state; structured waivers; root-completion gate.
- Closure path: current Team ledger/member/review evidence reaches the Leader → Leader makes a current-control judgment → Team tools publish/revise assignments, recovery, progress, waiver or final completion → ClawManager persists/enforces that decision and changes subsequent Team execution/root state.
- Boundary reachability: standard Team mode injects the Leader role and exposes Team task/status/control tools and authoritative roster/ledger context; the control loop is part of the shipped Team workflow rather than a downstream supervisor.
- Why this is / is not agent-owned: Monitor and ledger provide observations/enforcement, but they deliberately do not manufacture business completion. The Leader owns the business-aware current intervention and final root decision.
- Evidence: [`docs/team-workspaces-guide_en.md`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/docs/team-workspaces-guide_en.md); [`backend/internal/services/team_service.go`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/services/team_service.go); [`backend/internal/db/migrations/037_add_team_workflow_ledger.sql`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/db/migrations/037_add_team_workflow_ledger.sql).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: platform administrators also have lifecycle controls, but no distinct parent-governed S3 mode is claimed here; the positive base mode is the Team Leader's current-control loop.
- Whole-system current view: the Leader receives the Team roster, plan/phase context, active assignment/result/review state, shared artifacts and Monitor/recovery facts for the root task.
- Current-control decision scope: current assignment ownership/dependencies, recovery/reassignment, acceptance/waiver of required work, transition into synthesis, and authoritative Team root completion/failure.

## S3* — Complementary audit

- State: A
- Function: challenge producer assignments through separately assigned evidence/code-review/API-test/QA validation and feed the verdict into Team completion/control.
- Disturbance / variety regulated: a producing Worker may report a result that is incomplete, incorrect, stale relative to a newer artifact revision, or unsupported by sufficient evidence.
- Decisive decision or feedback right: a separately assigned validation member inspects the target assignment/revision using review-specific evidence access and reports a verdict/findings that can satisfy or block the durable review gate.
- Decision owner: the autonomous model-backed validation Worker under a ClawManager verification role/assignment.
- Supporting / enforcement mechanisms: `reviewRequired`; validation assignment marker; validation target assignment/revision; dedicated evidence/code-review/API-test guidance; review artifact kind; immutable review-gate inheritance; Leader completion contract.
- Closure path: Leader marks production work as requiring review and assigns a validation target → independent Team validation member inspects source/diff/artifacts/API/evidence → validation result is recorded against target/revision → Leader receives and reconciles the verdict → root completion remains blocked or proceeds; changed artifacts invalidate prior review and require fresh validation.
- Boundary reachability: ClawManager ships verification-role classification/guidance and durable review-target/revision fields in standard Team service code; the Leader can assign these roles through the same Team workflow.
- Why this is / is not agent-owned: review gating is deterministic support, while the semantic review/evidence verdict is produced by a distinct autonomous validation role. This is complementary to the producer's ordinary result path rather than the same actor's mandatory self-check.
- Evidence: [`backend/internal/services/team_service.go`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/services/team_service.go); [`backend/internal/db/migrations/042_add_team_review_contract.sql`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/db/migrations/042_add_team_review_contract.sql); [`docs/team-workspaces-guide_en.md`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/docs/team-workspaces-guide_en.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: not every Team task requires review. S3* is evidenced as a first-party reachable complementary mode when the Leader establishes a separate validation assignment.
- Claim being audited: the producer assignment's result/artifact at a specific assignment ID and revision satisfies its required correctness/evidence contract.
- Ordinary reporting path: producer Worker reports its assignment result, evidence and artifact references to the Leader/Team ledger.
- Complementary access path: a distinct validation Worker receives a validation assignment targeting that producer assignment/revision and uses source/diff/static evidence, APIs and/or Browser where relevant.
- Independence boundary: the validation assignment is owned by a separate Team member/role and durable review target; producer events cannot clear the inherited review-required gate.
- Who acts on findings: the Team Leader reconciles the validation verdict, coordinates correction/revision when needed and may complete the root only after required reviews are satisfied or a permitted explicit risk decision is recorded.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective Team adaptation loop was established.
- Disturbance / variety regulated: custom Team templates, model catalogs, provider health, security information and runtime versions can change, but inspected Team operation focuses on the current user goal and current capability.
- Decisive decision or feedback right: not established for sensing external/future change, developing organizational adaptation options and returning one into present Team capability.
- Decision owner: not established as a first-party S4 owner.
- Supporting / enforcement mechanisms: custom-template generation/refinement; AI Gateway model selection; runtime upgrades; Skill Hub/resources; platform administration.
- Closure path: not applicable at S4; configuration and current-task planning do not establish outside-and-then adaptation closure.
- Why this is / is not agent-owned: model-generated custom Team composition responds to explicit user configuration intent, while Leader planning responds to the current task. Neither is an external/prospective organizational intelligence loop.
- Evidence: [`README.md`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/README.md); [`docs/team-workspaces-guide_en.md`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/docs/team-workspaces-guide_en.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: platform evolution by maintainers is adjacent governance/development, not runtime Team S4.

### Absence scope

- Surfaces inspected: custom Team generation/refinement, model gateway/catalog, runtime rollout, skills/resources, Team planning/recovery and security/platform surfaces.
- Plausible first-party paths checked: natural-language Team redesign; model/provider routing; runtime upgrade safety; reusable resource changes; security event response.
- Why no material first-party path remains: located paths either configure the system, react to current execution state, or belong to maintainer/admin operation. No shipped Team agent models external/future change and develops durable adaptation options coupled back to S3.

## S5 — Policy and identity

- State: —
- Function: no material first-party Team identity/ultimate-policy decision loop was established.
- Disturbance / variety regulated: Team templates, role boundaries, platform risk/security rules, quotas, approvals and runtime policies constrain operation, but they do not constitute a Team-level ultimate-policy authority.
- Decisive decision or feedback right: not established for an identity/ultimate-policy dispute reaching legitimate authority and returning as governing Team policy.
- Decision owner: not established as a first-party S5 owner.
- Supporting / enforcement mechanisms: immutable Team protocol rules; role profiles; AI Gateway risk rules; administrator security controls; quotas/approvals.
- Closure path: not applicable at S5; no identity-level escalation/decision/return loop was found in the standard Team mode.
- Why this is / is not agent-owned: the Leader has strong operational authority but remains bounded by a first-party Team contract; that does not make it the ultimate policy authority.
- Evidence: [`README.md`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/README.md); [`backend/internal/services/team_service.go`](https://github.com/Yuan-lab-LLM/ClawManager/blob/576e4bb5440d453fd25300586e57ce81cb616f31/backend/internal/services/team_service.go).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: admin policy/security enforcement is institutionally important but is not S5 without an identity-level decision path.

### Absence scope

- Surfaces inspected: Team identity/role contracts; custom templates; platform policy/security/risk controls; admin/approval/quota surfaces; runtime governance.
- Plausible first-party paths checked: immutable Leader contract; custom role refinement; emergency circuit breaker; risk rules; admin approvals; Team root completion.
- Why no material first-party path remains: these paths bound or control current work. No first-party actor adjudicates the Team's ultimate identity/purpose or S3–S4 policy tension and returns that judgment as subsequent governing policy.

## Recursion

The focal viable organization is a ClawManager Team. Workers are operational S1 units; the Leader closes cross-worker coordination and current whole-Team control. Reviewers/validators provide complementary audit access over producer assignments. Managed OpenClaw/Hermes internals remain lower-level/external execution dependencies beneath first-party ClawManager roles.

## Variety and escalation

ClawManager amplifies operational variety through specialized Team roles and model-backed Worker/Leader judgment, while attenuating cross-member variety with a Leader-mediated protocol, durable assignment/dependency/revision contracts and shared artifacts. Monitor surfaces exceptional/stale conditions to the Leader for business-aware recovery. Required review adds a complementary validation channel before final synthesis. External-prospective adaptation and identity-policy closure remain outside the evidenced Team runtime.

## Evidence gaps

No evidence gap requires `?` at the frozen revision. The main ownership boundary is explicit: ClawManager does not inherit generic internal functions from OpenClaw/Hermes, but it does ship the Team role prompts, member identities, workflow/communication contract, review topology and return paths that define the assessed organization.

**Vector:** A · A · A · A · — · —
