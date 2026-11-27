---
harness_id: zeroburn
project_name: ZeroBurn
repository: https://github.com/thoufeeque22/zeroburn
review_ref: 5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: —
---

# ZeroBurn

## Review boundary

- System in focus: A ZeroBurn workspace installation in a host that implements the documented Antigravity workspace plugin, subagent and workflow interfaces.
- Purpose and identity: Carry out coding tickets under first-party rules, with scoped workers, compact evidence and defensive audit.
- Relevant environment: A target Git workspace, configured host/model accounts and optional local model or graph services.
- Standard-distribution boundary: The installed .agents policy, first-party tool hooks, workflow scripts and role definitions. Host services execute model turns and tools.
- Credited operating / distribution surfaces: Registered roles, documented single-chat and multi-stage operating modes, lease and audit scripts, installed rule maintenance.
- Adjacent first-party surfaces excluded from ownership: Benchmark and developer evaluation, external host internals, deployment-specific target projects and publisher release process.
- First-party operating / deployment modes considered: Single-chat work for small changes, staged or parallel work for larger tickets, and an optional rules-maintenance role.
- Recursion level: One installed workspace workflow. Ticket and slice work scopes are nested below the workspace.
- Reviewed revision: 5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

This is a host-native workflow distribution. It supplies project instructions, role registration, separate development and audit responsibilities, artifact handoffs and scripts that depend on host-provided agent and tool interfaces. Pre-tool hooks can enforce an advisory file lease and work output can be fed back to the orchestrator as concise reports.

## Operational model

The main session or an installed development agent selects edits and verification actions within a ticket scope and reports outcomes. The orchestrator selects work stages and can adjust the scope of an active ticket when discovery or audit changes the evidence. Host, Git and model services support the roles. The owner retains particular scope and intervention decisions.

## S1 — Operations

- State: A
- Function: Implement scoped changes and produce a checked workspace artifact for a ticket.
- Disturbance / variety regulated: Variable project changes, tool and test results, and remediation from prior stages.
- Decisive decision or feedback right: Select implementation and verification actions and adapt them to results within the work scope.
- Decision owner: The active model-backed session or registered development role in the supported host.
- Supporting / enforcement mechanisms: Workspace plugin registration, role brief, configured tools, artifact paths and verification wrappers.
- Closure path: The development agent reads the blueprint, selects edits and tests, acts on results and returns the development report. A returned review can drive another work turn.
- Boundary reachability: The first-party distribution ships its registered development role, tool selection, evidence obligations and workflow dispatch to a compatible workspace host. The host supplies the underlying model/turn machinery.
- Why this is / is not agent-owned: Removing the worker leaves execution hooks and checks but removes the discretionary choice of code changes and corrective actions.
- Evidence: [.agents/AGENTS.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/AGENTS.md#L25-L44), [.agents/plugins/zeroburn/agents/dev-agent.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/plugins/zeroburn/agents/dev-agent.md#L9-L34), [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L95-L110)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The positive state is scoped to the documented plugin-capable host. The standalone benchmark and generic script wrappers do not supply this loop.

## S2 — Coordination

- State: C
- Function: Reduce concurrent write interference when operational workers share a workspace.
- Disturbance / variety regulated: Parallel ticket slices can propose incompatible edits to one path.
- Decisive decision or feedback right: Allocate or revise write scopes and respond to conflicting file claims.
- Decision owner: The installed file-lease mechanism exposes a coordination-specific control path. Binding the worker identity and lease lifetime needs host-side composition.
- Supporting / enforcement mechanisms: First-party lease claim/release functions and write hook.
- Closure path: A competing claim fails or the edit hook denies a conflicting write. The caller can then change scope, wait or release the claim.
- Boundary reachability: The orchestration distribution directs the optional shared-workspace mode to supply lease scopes and worker IDs to the bundled guard.
- Why this is / is not agent-owned: The guard follows the configured file owner. Setup and composition determine who can make allocation decisions and how rejected work returns.
- Distinct S1 units: Parallel builders independently implementing ticket slices in one workspace.
- Inter-S1 disturbance: An edit by one worker can overwrite or conflict with another worker's planned changes.
- Attenuating coordination relation: Path-specific claims and the pre-tool guard deny conflicting writes for an identified worker.
- Feedback into subsequent S1 behaviour: Rejected claims or edits require rescoping or waiting before the worker can continue on that path.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The relation directly targets concurrent writes to the same file rather than moving tasks among agents.
- Evidence: [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L42-L47), [.agents/scripts/repo_digest.py](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/scripts/repo_digest.py#L69-L91), [.agents/hooks/pre-tool-guard.mjs](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/hooks/pre-tool-guard.mjs#L70-L84)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Advisory file state is a read/write mechanism, without an atomic claim guarantee. Enforcement is conditional on the host hook and worker identity.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate active ticket commitments, including splitting scope, skipping completed work and deciding what stage can proceed.
- Disturbance / variety regulated: Discovery can change blast radius, a resumed branch can already contain work, and audit can invalidate completion.
- Decisive decision or feedback right: Decide which current stages and slice commitments are needed and whether to hold or redirect work.
- Decision owner: The coordinating host agent under the installed workflow, and the human owner in the distinct escalation mode.
- Supporting / enforcement mechanisms: Resume gate, blueprint and stage reports, workflow return flags and human gates.
- Closure path: The orchestrator uses current work and audit findings to select stages and redirect remediation. Unresolved scope or exhausted audit iterations return to the owner for the decision governing progression.
- Boundary reachability: The bundled orchestrator instructions and audit workflow apply within the standard staged host mode and describe the returned operator actions.
- Why this is / is not agent-owned: The orchestrator chooses within the allowed paths based on current evidence. In the supervised path the owner decides whether outstanding scope or results permit continued work.
- Whole-system current view: Ticket, current branch state, blueprint, stage artifacts, findings and outstanding slice boundaries.
- Current-control decision scope: Current ticket/slice commitments, escalation under material scope changes and the remedy path before progression.
- Evidence: [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L69-L87), [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L95-L110), [.agents/scripts/parallel-audit.py](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/scripts/parallel-audit.py#L334-L352)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Routine sequencing and fixed audit caps are support. Scope selection and escalation return are the credited decisions.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Orchestrating model session | Current branch, plan or review changes the remaining commitments. | Select stages or redirect the job to QA/development and re-audit. | [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L69-L87), [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L103-L110) |
| Parent (`P`) | Workspace owner | Discovery requires a split decision or material findings persist after the audit limit. | Hold current work for owner decision and use the accepted scope or remediation direction to proceed. | [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L95-L109), [.agents/scripts/parallel-audit.py](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/scripts/parallel-audit.py#L334-L352) |

## S3* — Complementary audit

- State: A
- Function: Examine implementation and verification claims directly from changes in the workspace.
- Disturbance / variety regulated: The builder's report and ordinary quality evidence can miss defects or understated change scope.
- Decisive decision or feedback right: Identify material findings from a directly inspected diff and decide whether additional tests are required.
- Decision owner: Separate auditor model, with deterministic checks and local review supplying other inputs.
- Supporting / enforcement mechanisms: Read-only role, diff/check inputs, structured auditor response and non-model routing of findings.
- Closure path: The audit path emits verified findings and a test signal. The orchestrator routes remediation to development or to QA followed by development before a bounded re-audit.
- Boundary reachability: The installed workflow invokes the bundled auditor to examine the actual work and supplies the disposition to the standard staged run.
- Why this is / is not agent-owned: The reviewer chooses and evaluates findings and the test request. The workflow combines sources and applies its fixed severity policy.
- Claim being audited: The delivered project change satisfies the ticket scope and verification commitments.
- Ordinary reporting path: Development report and QA artifacts from the producing workflow.
- Complementary access path: Direct workspace diff and scoped source inspection, alongside the original blueprint and check results.
- Independence boundary: Separate role and context, read-only on application source. It can use findings from other checks without relying on the producer's assertion.
- Who acts on findings: The orchestration agent reopens remediation and may route new tests. Repeated material failure reaches the owner.
- Evidence: [.agents/scripts/parallel-audit.py](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/scripts/parallel-audit.py#L354-L373), [.agents/scripts/parallel-audit.py](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/scripts/parallel-audit.py#L421-L449), [.agents/scripts/parallel-audit.py](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/scripts/parallel-audit.py#L451-L486), [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L103-L109)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The aggregate decision includes static and local findings. The cloud auditor is a discretionary contributor, and its verdict is not the sole input to the gate.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Prospective adaptation of installed workflow rules and model-specific workarounds.
- Disturbance / variety regulated: Runtime and model changes can make installed practices stale across future tickets.
- Decisive decision or feedback right: Choose and apply a change to the installed rule set based on a prospective assessment.
- Decision owner: The bundled system role proposes edits and refers to owner approval. The end-to-end supported evaluation route is uncertain.
- Supporting / enforcement mechanisms: Expiry tags, optional maintenance triggers, release detection and an owner-invoked update utility.
- Closure path: The role describes a proposed rule diff, approval and subsequent edit. A host-specific prospective audit dependency and return into subsequent effective operating rules were not established from this revision.
- Why this is / is not agent-owned: The installed role supplies a concrete candidate path, but evidence does not settle whether a complete function-specific adaptation loop is available in the declared host setup.
- Evidence: [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L112-L119), [.agents/plugins/zeroburn/agents/system-agent.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/plugins/zeroburn/agents/system-agent.md#L9-L21), [.agents/hooks/session-start.mjs](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/hooks/session-start.mjs#L216-L224), [.agents/scripts/init.mjs](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/scripts/init.mjs#L208-L242)
- Basis: Structural evidence with unresolved host integration.
- Confidence: medium
- Caveats: Issue triage and version notification alone do not settle prospective ownership.

## S5 — Policy and identity

- State: —
- Function: Ultimate identity or delegation governance was sought in the workspace plugin.
- Disturbance / variety regulated: Conflicting mandates between target project, plugin and host.
- Decisive decision or feedback right: No supplied route for a last-resort purpose or identity decision.
- Decision owner: Owner configures the workspace and gives operational permissions.
- Supporting / enforcement mechanisms: Static invariant and role files, scoped approval gates and configuration.
- Closure path: Operating limits and approved maintenance edits affect work within the existing mandate.
- Why this is / is not agent-owned: The system role is directed to preserve the invariants. The documented owner gates address current work and accepted maintenance.
- Evidence: [.agents/AGENTS.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/AGENTS.md#L7-L31), [.agents/base/ORCHESTRATION.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/base/ORCHESTRATION.md#L95-L110), [.agents/plugins/zeroburn/agents/system-agent.md](https://github.com/thoufeeque22/zeroburn/blob/5f4f3fc8991677d0bd3ceb8ef01f2ee3d08e6d2d/.agents/plugins/zeroburn/agents/system-agent.md#L13-L21)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The upstream release process is outside the installed workspace boundary.

### Absence scope

- Surfaces inspected: Global invariants, role and permissions, human gates and the maintenance role.
- Plausible first-party paths checked: Routing an identity or ultimate-policy dispute to legitimate authority with a binding return to installed operation.
- Why no material first-party path remains: The reviewed paths preserve an externally selected mandate and return limited work or rule decisions. No distinct identity adjudication path is supplied.

## Recursion

The reviewed workspace plugin organizes tickets and, for larger work, nested implementing slices. The host is a dependency and external repository governance stays at its own boundary.

## Variety and escalation

Branch and worktree selection, resumable stage routing, test output filtering and separate audit findings regulate current task variation. The optional scoped-write hook attenuates parallel edit conflict. Audit exhaustion raises a bounded request for human decision.

## Evidence gaps

Static source analysis. No host workflow, provider action, local inference, deployment or upstream write was executed. The full host-specific rule adaptation path remains unresolved, so S4 is unknown.
