---
harness_id: happyhands
project_name: HappyHands
repository: https://github.com/ShuaiMXu/happyhands
review_ref: d469a02cb9b98c5f1a85b05201f5401bbec20ebf
reviewed_at: 2026-11-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: P
---

# HappyHands

## Review boundary

- System in focus: The HappyHands local product-experience harness in the lightweight Skill and optional source Workbench modes.
- Purpose and identity: Turn product-task evidence into an approved visual design policy, a bounded change, and a directly verified result.
- Relevant environment: A user-supplied product repository and preview, browser-rendered evidence, a coding-agent CLI, independent model inference and the product operator.
- Standard-distribution boundary: The installed CLI and reference bundle, source Workbench, capture, run ledger, planning, execution and review components. Host browsers and model/CLI execution services are dependencies.
- Credited operating / distribution surfaces: Source-bound diagnosis and repair, isolated worktree execution, independent visual review, operator control and Foundation decisions, and project-memory/Expertise paths to the extent they demonstrably affect operation.
- Adjacent first-party surfaces excluded from ownership: Sample products, static exported reports, development CI and tests, and external method authors or CLI providers as autonomous organizations.
- First-party operating / deployment modes considered: Codex-backed lightweight and local Workbench, review and first-render bootstrap, manual and delegated repair, and supported operator review. Claude and DSH compatibility is limited to evidenced paths.
- Recursion level: One product's review and repair operation, with an isolated repair worker below it and a human product operator as parent.
- Reviewed revision: `d469a02cb9b98c5f1a85b05201f5401bbec20ebf`.
- Observation date: 2026-11-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The CLI and Workbench operate a source-bound Run ledger. The first-party harness captures browser states, scopes findings and plans, runs a configured coding agent in an isolated worktree, recaptures and checks the result, and routes immutable evidence to independent Visual QA and human judgment. The Foundation stores the project's approved visual language. [docs/architecture.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/architecture.md#L35-L71), [docs/architecture.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/architecture.md#L94-L105), [packages/workbench/service.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/workbench/service.js#L354-L397).

## Operational model

The regular operational outcome is a bounded product change with evidence, or an explicit inability to repair. The implementation worker can decide which evidence-backed candidates reproduce and what scoped edits to make. The operator owns the permitted repair scope and the final decision, with the visual reviewer separately evaluating the rendered result.

## S1 — Operations

- State: A
- Function: Implement a scoped product-experience repair or page composition in the isolated target.
- Disturbance / variety regulated: Different UI defects, source conditions and verification evidence require task-specific implementation choices.
- Decisive decision or feedback right: Choose how to reproduce a finding, whether it is actionable, and which bounded source edits resolve it.
- Decision owner: The configured implementation agent reached through the shipped runner.
- Supporting / enforcement mechanisms: Source-bound plan, selected finding set, worktree, execution limit, captured originals and structural checks.
- Closure path: The Workbench creates or reads a confirmed scope, invokes the runner, captures the changed preview and records checks and the result for review.
- Boundary reachability: The automatic repair action and the CLI execute command both reach the bundled isolated runner.
- Why this is / is not agent-owned: Without the agent the harness can capture and validate, but it cannot make the supported task-specific implementation decisions.
- Evidence: [docs/harness.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/harness.md#L7-L13), [docs/harness.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/harness.md#L100-L106), [packages/workbench/service.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/workbench/service.js#L354-L397), [packages/harness-core/runner.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/harness-core/runner.js#L122-L156).
- Basis: structural
- Confidence: high
- Caveats: Repair authority is user-delegated. Final QA and acceptance are separate decisions.

## S2 — Coordination

- State: —
- Function: Regulate interference among multiple independent S1 production units.
- Disturbance / variety regulated: Concurrent product edit work or shared component edits could interfere if the harness supplied multiple coequal workers.
- Decisive decision or feedback right: No material inter-S1 coordination right is shipped in the assessed product loop.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Run identity, per-run action and stage locks, isolated worktrees and job capacity.
- Closure path: The Workbench serializes incompatible stages in a single run and isolates separate executions. Review batches return QA evidence.
- Why this is / is not agent-owned: The operating chain uses one implementation worker per repair. Reviewers and deterministic checks are different organizational roles, and the inspected job controls supply no decision path for interference among distinct S1 units.
- Evidence: [packages/workbench/service.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/workbench/service.js#L336-L382), [packages/workbench/direction-execution.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/workbench/direction-execution.js#L5-L27), [docs/architecture.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/architecture.md#L97-L105).
- Basis: structural
- Confidence: medium
- Caveats: Concurrent service jobs and separate runs do not by themselves establish a coordinated shared S1 mandate.

### Absence scope

- Surfaces inspected: Workbench actions, job management, direction preparation, repair and independent regional review.
- Plausible first-party paths checked: Multiple jobs per Workbench, regional review, direction alternatives, worktree isolation and source-change guards.
- Why no material first-party path remains: The shipped workflows prevent duplicate steps and separate runs, but do not furnish a function-specific path for coordinating competing production units on the same product commitment.

## S3 — Inside-and-now control

- State: P
- Function: Regulate the active review and repair commitment from source-bound evidence and verification state.
- Disturbance / variety regulated: Stale or false findings, insufficient evidence, failed repair and revised scope can invalidate the current commitment.
- Decisive decision or feedback right: Determine which scoped work may run, and on failed QA decide whether to reject or direct a fresh evidence-bound review.
- Decision owner: The product operator using the Workbench or CLI.
- Supporting / enforcement mechanisms: Run-wide state, source binding, per-stage gates, explicit repair requests, a retained worktree and judgment records.
- Closure path: The operator chooses a repair scope or a new evidence-backed review and the service binds that choice to the plan or review. Rejection ends that run and acceptance requires a separate QA pass.
- Boundary reachability: Shipped Workbench actions and CLI tools expose source review, execution authorization and result control over the same ledger.
- Why this is / is not agent-owned: The implementation agent judges the edits inside its remit. The operator owns intervention on the current commitment and the disposition of the result.
- Whole-system current view: For the assessed product run the ledger and workbench aggregate baseline, findings, plan, worktree result, after evidence, QA and judgment.
- Current-control decision scope: Scope the active repair, reject the result or return it for evidence-bound review before the next decision.
- Evidence: [docs/harness.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/harness.md#L100-L110), [docs/harness.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/harness.md#L289-L295), [packages/workbench/service.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/workbench/service.js#L336-L382), [packages/harness-core/workflow.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/harness-core/workflow.js#L35-L48).
- Basis: structural
- Confidence: medium
- Caveats: Scope is the product run, not management of the upstream project or several unrelated workspaces.

## S3* — Complementary audit

- State: A
- Function: Independently audit whether the change achieves the user task without material visual regression.
- Disturbance / variety regulated: The executor's report and deterministic layout checks can miss actual experience regressions.
- Decisive decision or feedback right: Issue a visual verdict from directly captured, source-bound before and after evidence.
- Decision owner: The separate configured Visual QA model session in the shipped model-review mode.
- Supporting / enforcement mechanisms: Immutable originals, coverage and state binding, checks, separate review context and judgment gate.
- Closure path: A failing or incomplete review blocks acceptance. New evidence can trigger a fresh review, whose result governs the next operator disposition.
- Boundary reachability: The Workbench review path invokes the shipped reviewer after recapture and structural evaluation. The lightweight CLI also exposes model review.
- Why this is / is not agent-owned: The independent reviewer reasons over direct evidence and reports findings, while the runtime checks provenance and enforces gates.
- Claim being audited: The repaired user experience meets the task without unacceptable visual regression.
- Ordinary reporting path: Implementation result, changed files, executor claims and structural evaluation.
- Complementary access path: Matched original browser captures and bound specialist evidence in a separate review session.
- Independence boundary: Visual QA is produced separately from the implementation session and checks the actual changed render.
- Who acts on findings: The workflow blocks acceptance and the product operator can reject or direct new evidence and independent re-review.
- Evidence: [docs/experience-orchestration.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/experience-orchestration.md#L29-L43), [packages/workbench/ai-review.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/workbench/ai-review.js#L180-L222), [packages/workbench/ai-review.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/workbench/ai-review.js#L225-L248), [packages/harness-core/workflow.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/harness-core/workflow.js#L35-L48).
- Basis: structural
- Confidence: high
- Caveats: The review covers the planned states and does not imply whole-site quality or human approval.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Develop and return a prospective adaptation of the harness's future product-review capability.
- Disturbance / variety regulated: Changed product needs and repeated visual failures may motivate new method choices.
- Decisive decision or feedback right: Select a reviewed adaptation and make it affect future operation.
- Decision owner: The operator can admit cases and approve durable design changes. A maintainer can publish and activate Expertise metadata.
- Supporting / enforcement mechanisms: Source-bound case admissions, future-plan retrieval, independent regression reports and versioned release pointers.
- Closure path: Admitted cases can enter later plans as references. Expertise activation changes a release pointer, but the inspected operational runner did not establish that the pointer changes the loaded capability.
- Why this is / is not agent-owned: The concrete case path changes context for later work. The inspected release path has a gap between recording activation and changing operational method selection.
- Evidence: [docs/experience-cases.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/experience-cases.md#L20-L43), [docs/project-memory-lifecycle-2026-10-18.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/project-memory-lifecycle-2026-10-18.md#L25-L45), [packages/skill-core/releases.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/skill-core/releases.js#L17-L46), [packages/skill-core/releases.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/skill-core/releases.js#L72-L89).
- Basis: structural
- Confidence: medium
- Caveats: The packaged, versioned methods and the source repository's maintainer release lifecycle need an evidenced return into the operating mode before a stronger S4 state.

## S5 — Policy and identity

- State: P
- Function: Set the durable design and experience rules that govern future product work.
- Disturbance / variety regulated: Observed or proposed visual conventions may conflict with the product's intended identity and standards.
- Decisive decision or feedback right: Decide whether proposed brand, design and reusable rules are approved, replaced or deprecated as the authoritative Foundation.
- Decision owner: The human product owner/operator authorized to approve the product's Foundation.
- Supporting / enforcement mechanisms: Observed inventory, explicit reasoned decisions, version binding and plans constrained by the approved snapshot.
- Closure path: The extracted or staged proposal reaches the operator, whose approval writes an immutable Foundation and updates the Experience Spec. Bootstrap plans and execution load and check the same approved version.
- Boundary reachability: The shipped workbench and CLI expose Foundation approval, with a ledger gate and a subsequent runner check.
- Why this is / is not agent-owned: Extraction and generation implement or propose design choices. The human decides what visual language is authoritative for the product.
- Identity / ultimate-policy issue: Which visual language, design principles, brand voice and reusable design rules future product work must preserve.
- Ultimate authority in each claimed mode: The product operator acting for the product through explicit Foundation approval.
- Return-to-operation path: The approved version becomes a prerequisite and input to first-render planning and execution.
- Evidence: [docs/architecture.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/architecture.md#L35-L44), [docs/harness.md](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/docs/harness.md#L102-L112), [packages/harness-core/store.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/harness-core/store.js#L370-L416), [packages/harness-core/runner.js](https://github.com/ShuaiMXu/happyhands/blob/d469a02cb9b98c5f1a85b05201f5401bbec20ebf/packages/harness-core/runner.js#L122-L144).
- Basis: structural
- Confidence: high
- Caveats: This is product-experience identity, not authority over the upstream HappyHands repository.

## Distributed OSS parent arrangement

The authoritative Foundation decision belongs to the product operator at this recursion. Upstream maintainers and authors of imported methods are separate.

## Self-hosted and non-human modes

The local workflow can automate implementation and review after scoped delegation. It retains human Foundation and final acceptance decisions.

## Recursion

The product review-and-repair operation includes a scoped implementation cell and a distinct visual reviewer. Evidence capture and structural checks support their loops.

## Variety and escalation

Source and evidence freshness gates, scoped repair, failed QA, and operator judgment regulate different disturbances. No additional system-level algedonic channel is established.

## Evidence gaps

The review is based on pinned source and documented modes. No live browser/model repair was run for this assessment. The S4 uncertainty concerns the runtime effect of the Expertise release pointer and the capability-level status of admitted cases.
