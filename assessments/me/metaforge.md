---
harness_id: metaforge
project_name: MetaForge
repository: https://github.com/FidelOdok/MetaForge
review_ref: 6f39fdcfec4599e2cd68780432c26e6a4c14af96
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# MetaForge

## Review boundary

- System in focus: One supported MetaForge project design-flow organization: model-led design phases, shared digital twin, gate reviewer and human project authority.
- Purpose and identity: Produce coherent traceable hardware design artifacts and evidence across disciplines under an approved project flow.
- Relevant environment: Project requirements, engineering tools/results, shared twin artifacts, component/standards knowledge, provider availability and human engineering decisions.
- Standard-distribution boundary: Deployed gateway/design-flow worker and native model/tool harness, twin/version/constraint APIs, server gate-review mode and project approval UI. The recursion is one project design program, not all projects or the MetaForge developer organization.
- Credited operating / distribution surfaces: Packaged phase runner/model tool loop, persistent Temporal flow, twin branch/merge constructors, approved flow versions, project gate reviewer with read-only review tools, retry/rework propagation and human approval modes.
- Adjacent first-party surfaces excluded from ownership: Repository contributor agents, CI, evaluation judges/benchmarks, illustrative tests and planner/generator/evaluator protocol stubs are not credited as deployed owners. External CAD/solver/model/MCP services retain their own implementation roles.
- First-party operating / deployment modes considered: Server-driven project design flow with human off/default gate policy; optional advise/auto_clean/expiry-bounded auto server reviewer; native chat/tool harness; first-party iteration/twin constructors. MCP-only external-agent and client-reviewer modes are inspected but do not donate an actor to the server mode.
- Recursion level: One deployed project design-flow program; discipline/phase cells are operational units, without claiming each cell has a complete recursive metasystem.
- Reviewed revision: 6f39fdcfec4599e2cd68780432c26e6a4c14af96
- Observation date: 2026-11-19
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Gateway/worker binds DesignFlowActivities to a real phase runner and gate reviewer. A frozen approved flow dispatches model-led phase tool turns, stores deliverables in the twin, checks gates and persists waits/signals through Temporal. Retry/rework passes specific findings and revision context into the affected phase and invalidates/re-executes dependent work. The native harness centralizes provider/tool/gate services. Optional server reviewer runs a separate read-only model turn, can inspect twin nodes, histories and constraint evidence, and posts a structured recommendation. Project policy decides whether humans act or permitted reviewer decisions apply. Twin three-way merge and branch/constraint constructors expose conflict-aware integration; standalone advisory session-lock code is not treated as active wiring.

## Operational model

Discipline/phase work cells transform project requirements into designs, analyses and recorded evidence. At this declared project recursion, whole-program phase commitments and cross-phase rework can be regulated by the authorized reviewer in auto mode or the human in default/advisory modes. The same reviewer audit judgment is analyzed separately from its delegated current-control decision. This is not autonomous fleet control over all server projects.

## S1 — Operations

- State: A
- Function: Produce hardware-design artifacts and evidence through model-led phase/tool work.
- Disturbance / variety regulated: Unknown design choices, tool failures and unmet project requirements.
- Decisive decision or feedback right: Select engineering/tool actions, revise work from checks and produce phase deliverables.
- Decision owner: Configured first-party phase/chat model actor.
- Supporting / enforcement mechanisms: HarnessRuntime/build_agent_runtime, provider pipeline, native/MCP tool registry, twin storage, frozen flow and activity retries.
- Closure path: Bound phase runner performs tool turns; artifacts/checks return into phase context and later retries/rework; results persist in the project run.
- Why this is / is not agent-owned: Configured model actors choose domain work; tool transport and fixed flow cannot replace their design discretion.
- Evidence: [README.md](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/README.md); [orchestrator/design_flow/temporal_flow.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/temporal_flow.py); [api_gateway/runs/flow_worker.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/runs/flow_worker.py); [api_gateway/chat/harness_backend.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/chat/harness_backend.py); [orchestrator/harness/react.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/harness/react.py); [orchestrator/harness/runtime.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/harness/runtime.py)
- Basis: structural
- Confidence: high
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Boundary reachability: flow_worker.build_activities binds _run_phase and _review_gate; the deployed worker executes those activities rather than relying on the adjacent three-agent protocol examples.

## S2 — Coordination

- State: C
- Function: Construct conflict-aware integration among operational design cells sharing versioned work products.
- Disturbance / variety regulated: Two design branches modify/delete the same work product incompatibly; downstream constraints can invalidate a proposed integration.
- Decisive decision or feedback right: Compose branch ownership/integration and decide responses to conflict and cross-domain constraint feedback.
- Decision owner: Developer/operator assembling the first-party twin/iteration path; deterministic merge/validation supports the arrangement. No autonomous coordination discretion is credited.
- Supporting / enforcement mechanisms: Isolated iteration branches, three-way content/structural conflict detection, cross-domain constraint evaluation and conflict-returning merge.
- Closure path: Iteration constructor produces on an isolated branch, validates against the twin, and only attempts accepted integration; incompatible branch edits raise MergeConflict and prevent silent overwrite.
- Why this is / is not agent-owned: A concrete shared-artifact coordination constructor exists; a bound autonomous actor revising conflict/integration policy is not established.
- Evidence: [orchestrator/iteration_controller.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/iteration_controller.py); [twin_core/versioning/merge.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/twin_core/versioning/merge.py); [twin_core/versioning/branch.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/twin_core/versioning/branch.py); [twin_core/constraint_engine/cross_domain.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/twin_core/constraint_engine/cross_domain.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Distinct S1 units: Separate domain/phase design agents producing changes to shared project work products on different branches.
- Inter-S1 disturbance: Both sides changing one work product to different content, or deleting an artifact another cell modified, can silently destroy the other contribution.
- Attenuating coordination relation: Isolated branches plus three-way conflict rejection and cross-domain constraint checks before integration.
- Feedback into subsequent S1 behaviour: Conflicts/failed constraints prevent acceptance and return failed/refinement state; the constructor exposes the actual incompatible artifacts instead of overwriting them.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The path explicitly detects competing content/structural edits to identical artifact IDs and blocks destructive integration, beyond a generic DAG or mailbox.
- Boundary reachability: These are shipped first-party Python/twin APIs used by IterationController. The claim is constructor-level and does not assert that every design-flow phase uses this optional iteration controller.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate current project phase commitments and cross-phase corrective work on behalf of the complete design program.
- Disturbance / variety regulated: A phase can satisfy superficial checks while leaving substantive omissions or requiring revision of earlier dependent work.
- Decisive decision or feedback right: Choose permitted approve/retry/rework disposition over the current project and return specific corrective commitments to affected phases.
- Decision owner: Base: configured server gate-review agent under project auto policy. Parent: legitimate human project reviewer in off/advise or reserved-decision modes.
- Supporting / enforcement mechanisms: Project/twin review brief, read-only model review, approval policy/ledger, frozen flow, gate signals and dependency-aware rework engine.
- Closure path: Reviewer posts structured recommendations; permitted auto dispositions become attributed gate decisions. Human mode records human decisions. Retry/rework reasons return through Temporal into the selected phase and dependent execution.
- Why this is / is not agent-owned: The reviewer/human selects between materially different current-program continuation and rework outcomes; policy and Temporal merely bound/enforce that selection. Removing the deciding actor leaves a waiting gate.
- Evidence: [README.md](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/README.md); [orchestrator/design_flow/temporal_flow.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/temporal_flow.py); [api_gateway/runs/flow_worker.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/runs/flow_worker.py); [api_gateway/runs/gate_review.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/runs/gate_review.py); [api_gateway/approvals/policy.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/approvals/policy.py); [mcp_core/profiles.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/mcp_core/profiles.py); [mcp_core/plugin_skills/gate-review/SKILL.md](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/mcp_core/plugin_skills/gate-review/SKILL.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Whole-system current view: At the project-run recursion: approved phase objectives/deliverables, earlier decisions and reasons, current gate findings and relevant shared project twin records, with read tools for further inspection.
- Current-control decision scope: Continue, retry current commitments or rework an earlier phase and its dependent outputs. This exceeds selecting a worker but does not include server-wide fleet allocation.
- Boundary reachability: The deployed worker binds gate reviewer activity; review_gate reads effective project policy and runs the server reviewer. Auto mode can decide permitted retry/rework; default/advise returns the same project gate to a human.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Server reviewer under permitted auto policy | Open project gate with current evidence | Attributed approve/retry/rework disposition changes subsequent phase execution | gate_review.py; approvals/policy.py; temporal_flow.py |
| Parent (`P`) | Human project reviewer | Default off/advise mode, unavailable reviewer or reserved decision | Human gate decision/feedback resumes, retries or reworks project phases | policy.py; temporal_flow.py; README.md |

## S3* — Complementary audit

- State: A
- Function: Challenge phase readiness and grounding with a separate read-only evidence-inspecting reviewer.
- Disturbance / variety regulated: A successful phase report or passing presence checks can hide unsupported quantities, wrong artifacts or missing substantive evidence.
- Decisive decision or feedback right: Choose additional read observations and render an independent structured review of the producing phase claims.
- Decision owner: Separate server reviewer model turn using the gate-review rubric and review-only tool allowlist.
- Supporting / enforcement mechanisms: Review brief, twin node/history/query/verification tools, policy/ledger, posted concerns and rework feedback.
- Closure path: Recommendations and concerns are posted to the exact gate; permitted automatic decisions or human review feed retry/rework reasons back into subsequent phases.
- Why this is / is not agent-owned: The reviewer makes the discretionary evidence/judgment choice in a separate read-only turn; parsing and policy application do not own that audit judgment.
- Evidence: [README.md](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/README.md); [orchestrator/design_flow/temporal_flow.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/temporal_flow.py); [api_gateway/runs/flow_worker.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/runs/flow_worker.py); [api_gateway/runs/gate_review.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/runs/gate_review.py); [api_gateway/approvals/policy.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/approvals/policy.py); [mcp_core/profiles.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/mcp_core/profiles.py); [mcp_core/plugin_skills/gate-review/SKILL.md](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/mcp_core/plugin_skills/gate-review/SKILL.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Claim being audited: Phase work substantively satisfies required deliverables and grounded engineering claims.
- Ordinary reporting path: Producing phase summary/artifact record and deterministic gate checks.
- Complementary access path: Reviewer can query twin nodes, thread/history, constraint violations and verification relationships rather than relying solely on the producer summary.
- Independence boundary: Separate reviewer turn with no engineering-state write tools; same provider is permitted. Bridge-backed read access is required for the credited path; brief-only failure fallback is not credited.
- Who acts on findings: Permitted project reviewer decision or legitimate human gate authority; Temporal returns reasons into retry/rework.
- Boundary reachability: flow_worker binds _review_gate, connects MCP bridge and invokes packaged review_gate; enabled server policy runs run_chat_turn with its own review session and REVIEW_TOOLS.

## S4 — Outside-and-then intelligence

- State: —
- Function: No externally prospective harness-capability adaptation loop established.
- Disturbance / variety regulated: Future external changes that require adapting the harness organization.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Tailored/approved flow versions, supplier knowledge, experience consolidation and constraint/spec revalidation.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: Engineering research/design tailoring primarily transforms the current project; reusable versioning alone does not establish outside-and-then organizational adaptation.
- Evidence: [README.md](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/README.md); [orchestrator/design_flow/temporal_flow.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/temporal_flow.py); [api_gateway/runs/flow_worker.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/runs/flow_worker.py); [orchestrator/design_flow/generator.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/generator.py); [orchestrator/design_flow/versions.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/versions.py); [orchestrator/design_flow/prior_lessons.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/prior_lessons.py); [orchestrator/workflows/design_escalation.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/workflows/design_escalation.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/README.md); [orchestrator/design_flow/temporal_flow.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/temporal_flow.py); [api_gateway/runs/flow_worker.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/runs/flow_worker.py); [orchestrator/design_flow/generator.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/generator.py); [orchestrator/design_flow/versions.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/versions.py); [orchestrator/design_flow/prior_lessons.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/prior_lessons.py); [orchestrator/workflows/design_escalation.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/workflows/design_escalation.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Flow proposal operations and immutable versions, current design revalidation/escalation and stored prior lessons.
- Why no material first-party path remains: These expose current-project workflow/design decisions and knowledge reuse without an established future-environment adaptation option returning into harness current capability.

## S5 — Policy and identity

- State: —
- Function: No established identity/ultimate-policy issue and returned-authority loop.
- Disturbance / variety regulated: Unsettled identity or ultimate-policy tensions of the design organization.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Approved flows, project reviewer policy ceilings/expiry, permission tiers, sign-off/spending reservations and static policy engine.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: Legitimate human authority constrains ordinary actions and delegated gate decisions, but configuration and ordinary engineering approvals alone are not runtime S5 closure.
- Evidence: [README.md](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/README.md); [orchestrator/design_flow/temporal_flow.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/temporal_flow.py); [api_gateway/runs/flow_worker.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/runs/flow_worker.py); [api_gateway/approvals/policy.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/approvals/policy.py); [api_gateway/approvals/policy_routes.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/approvals/policy_routes.py); [orchestrator/harness/policy.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/harness/policy.py); [orchestrator/design_flow/versions.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/versions.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/README.md); [orchestrator/design_flow/temporal_flow.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/temporal_flow.py); [api_gateway/runs/flow_worker.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/runs/flow_worker.py); [api_gateway/approvals/policy.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/approvals/policy.py); [api_gateway/approvals/policy_routes.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/api_gateway/approvals/policy_routes.py); [orchestrator/harness/policy.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/harness/policy.py); [orchestrator/design_flow/versions.py](https://github.com/FidelOdok/MetaForge/blob/6f39fdcfec4599e2cd68780432c26e6a4c14af96/orchestrator/design_flow/versions.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Approval policy modes/routes, frozen flow approval, tool permission holds and engineering sign-off reservations.
- Why no material first-party path remains: The inspected standard distribution records/enforces authority but does not supply a distinct identity/ultimate-policy issue → authority decision → returned policy-resolution path.

## Distributed OSS parent arrangement

Repository maintenance and contributor approvals are outside the deployed product recursion. Multiple contributors do not establish organization-level parent governance in the assessed harness.

## Self-hosted and non-human modes

Human project authority chooses the approved flow and permitted reviewer policy. Server auto mode is optional, ceiling/expiry constrained and never silently grants spending or sign-off authority. A reviewer failure returns to a human wait. Human and autonomous S3 are alternative evidenced modes, not simultaneous ultimate owners.

## Recursion

No claim of recursively complete VSM units is made. Execution phases, provider instances and nested calls do not establish recursive viability.

## Variety and escalation

Gate findings, nonconvergent coupled values and failed/unavailable reviews hold work or feed bounded retry/rework. Final sign-offs/spending remain human-reserved. Frozen flow versions, policy ceilings and explicit actors preserve the decision boundary; no S5 is inferred merely from these controls.

## Evidence gaps

No live engineering-tool, model or Temporal integration was executed. S3/S3* positives are limited to supported server reviewer modes with working gateway/MCP read access; a brief-only fallback is not credited as complementary evidence access. S2 is a constructor claim, not installed autonomous coordination. No engineering accuracy, production readiness, global-fleet autonomy or organizational viability claim follows.
